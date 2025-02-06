from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from ..config import settings

def get_llm():
    tokenizer = AutoTokenizer.from_pretrained(settings.LLM_MODEL)
    model = AutoModelForCausalLM.from_pretrained(settings.LLM_MODEL)

    return pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_length=200,
        temperature=0.7
    )
