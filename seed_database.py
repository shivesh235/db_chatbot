# seed_database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.database.models import Base, Supplier, Product
from backend.config import settings

def seed_database():
    # Create engine and session
    engine = create_engine(settings.DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    try:
        # Create sample suppliers
        suppliers = [
            Supplier(
                name="TechCorp Industries",
                contact_info="contact@techcorp.com | +1-555-0123",
                product_categories="Laptops, Desktops, Accessories"
            ),
            Supplier(
                name="Digital Solutions Ltd",
                contact_info="info@digitalsolutions.com | +1-555-0124",
                product_categories="Smartphones, Tablets, Wearables"
            ),
            Supplier(
                name="Office Supplies Pro",
                contact_info="sales@officesuppliespro.com | +1-555-0125",
                product_categories="Printers, Scanners, Office Equipment"
            )
        ]
        
        db.add_all(suppliers)
        db.commit()

        # Create sample products
        products = [
            # TechCorp products
            Product(
                name="ProBook X1",
                brand="TechCorp",
                price=999.99,
                category="Laptops",
                description="15-inch business laptop with Intel i7",
                supplier_id=1
            ),
            Product(
                name="WorkStation Pro",
                brand="TechCorp",
                price=1499.99,
                category="Desktops",
                description="High-performance desktop workstation",
                supplier_id=1
            ),
            # Digital Solutions products
            Product(
                name="SmartPhone X",
                brand="Digital",
                price=799.99,
                category="Smartphones",
                description="5G smartphone with 6.7-inch display",
                supplier_id=2
            ),
            Product(
                name="TabPro 12",
                brand="Digital",
                price=599.99,
                category="Tablets",
                description="12-inch tablet with stylus support",
                supplier_id=2
            ),
            # Office Supplies products
            Product(
                name="LaserJet 2000",
                brand="OfficePro",
                price=299.99,
                category="Printers",
                description="Color laser printer for business",
                supplier_id=3
            ),
            Product(
                name="ScanMaster 500",
                brand="OfficePro",
                price=199.99,
                category="Scanners",
                description="High-speed document scanner",
                supplier_id=3
            )
        ]
        
        db.add_all(products)
        db.commit()
        
        print("Database seeded successfully!")
        
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()