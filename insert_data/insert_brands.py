from sqlalchemy import Table, MetaData
from sqlalchemy.dialects.postgresql import insert
from generate_data.connect import engine
from generate_data.gen_brands import generate_brands

# Assuming 'brand_data' is your list of generated brand dictionaries
def insert_brands(brand_data):
    # Initialize metadata
    metadata = MetaData()
    brands_table = Table('brands', metadata, autoload_with=engine, schema='parts_catalog')
        
    try:
        with engine.connect() as conn:
            conn.execution_options(isolation_level="AUTOCOMMIT")  # Auto-commit mode
            for brand in brand_data:
                stmt = insert(brands_table).values(
                    brand_id=brand['brand_id'],
                    brand_name=brand['brand_name']
                )
                # Using ON CONFLICT DO NOTHING to avoid duplicates based on unique constraints
                conn.execute(stmt.on_conflict_do_nothing(index_elements=['brand_name']))
        print("Data inserted successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")
            
# Generate 19 brands
brand_data = generate_brands(19)
# Example usage
insert_brands(brand_data)