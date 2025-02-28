import psycopg2
import json
import uuid
from sqlalchemy import Table, MetaData, select
from sqlalchemy.dialects.postgresql import insert
from generate_data.connect import engine

# Function to insert category data recursively
def insert_category(conn, categories_table, category_info, parent_id=None):
    # Ensure that category_info is a dictionary
    if isinstance(category_info, dict):
        category_name = category_info.get('text')
    else:
        print(f"Unexpected category_info type: {type(category_info)} - {category_info}")
        return

    # Check if the category already exists
    sel = select(categories_table.c.category_id).where(categories_table.c.category_name == category_name)
    result = conn.execute(sel).fetchone()

    if result is None:
        # Generate new ID if category does not exist
        new_category_id = str(uuid.uuid4())
        stmt = insert(categories_table).values(
            category_id=new_category_id,
            category_name=category_name,
            parent_category_id=parent_id
        ).on_conflict_do_nothing(index_elements=['category_id'])
        conn.execute(stmt)
    else:
        # Use existing ID
        new_category_id = result[0]

    # Handle children properly (check if it's a dict or list)
    children = category_info.get('children', {})
    
    if isinstance(children, dict):  # Expected format
        for child_info in children.values():
            insert_category(conn, categories_table, child_info, new_category_id)
    elif isinstance(children, list):  # Handle empty lists
        for child_info in children:
            insert_category(conn, categories_table, child_info, new_category_id)


def insert_categories():
    # Initialize metadata
    metadata = MetaData()
    categories_table = Table('categories', metadata, autoload_with=engine, schema='parts_catalog')
    
    # Load JSON data
    with open('generate_data/categories.json', 'r') as file:
        categories = json.load(file)['categories']
    
    try:
        with engine.connect() as conn:
            conn.execution_options(isolation_level="AUTOCOMMIT")  # Auto-commit mode
            for category_id, category_info in categories.items():  # Iterate over categories
                insert_category(conn, categories_table, category_info)
        print("Category Data inserted successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")

# Example usage
insert_categories()
