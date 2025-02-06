from typing import List, Dict, Any
from langgraph.graph import StateGraph
from langchain import LLMChain, PromptTemplate
from sqlalchemy.orm import Session
from sqlalchemy import or_
from ..database.models import Product, Supplier
from ..utils.llm_utils import get_llm

class ChatAgent:
    def __init__(self, db: Session, llm=None):
        self.db = db
        self.llm = llm or get_llm()
        self.setup_graph()

        # ✅ Compile the graph before running it
        self.executor = self.graph.compile()

    def setup_graph(self):
        """Initializes the LangGraph chatbot agent."""
        self.graph = StateGraph(dict)  # ✅ Use StateGraph

        # Define processing nodes
        self.graph.add_node("query_classifier", self.classify_query)
        self.graph.add_node("product_retriever", self.retrieve_products)
        self.graph.add_node("supplier_retriever", self.retrieve_suppliers)
        self.graph.add_node("response_generator", self.generate_response)

        # ✅ Conditional routing function
        self.graph.add_conditional_edges(
            "query_classifier",
            self.route_query
        )

        # Define normal edges
        self.graph.add_edge("product_retriever", "response_generator")
        self.graph.add_edge("supplier_retriever", "response_generator")

        # Set entry point
        self.graph.set_entry_point("query_classifier")

    def classify_query(self, state: dict) -> dict:
        """Classifies the query and sets the next node in the state."""
        query = state["query"].lower()
        if any(word in query for word in ["product", "brand", "price"]):
            state["next"] = "product_retriever"
        else:
            state["next"] = "supplier_retriever"
        return state  # ✅ Ensure we return updated state

    def route_query(self, state: dict) -> str:
        """Determines the next node based on classification."""
        return state["next"]

    def retrieve_products(self, state: dict) -> dict:
        """Fetches product data based on query."""
        query = state["query"]
        products = self.db.query(Product).filter(
            or_(
                Product.name.ilike(f"%{query}%"),
                Product.brand.ilike(f"%{query}%"),
                Product.category.ilike(f"%{query}%")
            )
        ).all()
        state["results"] = [self._product_to_dict(p) for p in products]
        return state

    def retrieve_suppliers(self, state: dict) -> dict:
        """Fetches supplier data based on query."""
        query = state["query"]
        suppliers = self.db.query(Supplier).filter(
            or_(
                Supplier.name.ilike(f"%{query}%"),
                Supplier.product_categories.ilike(f"%{query}%")
            )
        ).all()
        state["results"] = [self._supplier_to_dict(s) for s in suppliers]
        return state

    def generate_response(self, state: dict) -> dict:
        """Uses LLM to generate a chatbot response."""
        results = state["results"]
        query = state["query"]

        prompt = PromptTemplate(
            input_variables=["query", "data"],
            template="Based on the query '{query}', here is the relevant information: {data}. "
                    "Please provide a concise and informative summary."
        )

        chain = LLMChain(llm=self.llm, prompt=prompt)
        state["response"] = chain.run(query=query, data=results)
        return state  # ✅ Return updated state

    @staticmethod
    def _product_to_dict(product: Product) -> Dict:
        """Converts a Product object to a dictionary."""
        return {
            "id": product.id,
            "name": product.name,
            "brand": product.brand,
            "price": product.price,
            "category": product.category,
            "description": product.description
        }

    @staticmethod
    def _supplier_to_dict(supplier: Supplier) -> Dict:
        """Converts a Supplier object to a dictionary."""
        return {
            "id": supplier.id,
            "name": supplier.name,
            "contact_info": supplier.contact_info,
            "product_categories": supplier.product_categories
        }
