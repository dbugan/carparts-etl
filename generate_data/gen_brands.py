import faker
import uuid
import random

# Initialize Faker instance
fake = faker.Faker()


def generate_brands(numbrands):
    brands = []
    OEM_BRANDS = [
        "Mahle", "BILSTEIN", "AC Schnitzer", "BBS", "Brembo", "Bosch", "ZF",
        "Hella", "MANN-FILTER", "Eibach", "KW Suspension", "LUK", "Recaro",
        "Sachs", "Wagner Tuning", "Schrick", "Pagid", "ATE", "Pierburg"
    ]
    
    for _ in range(numbrands):  # Fixed variable name
        brand = {
            "brand_id": uuid.uuid4(),  # Use uuid.uuid4() instead of fake.uuid4()
            "brand_name": random.choice(OEM_BRANDS),  # Use random.choice() instead of fake.random.choice()
        }
        brands.append(brand)
    return brands

# Example usage
num_brands = 19
brand_data = generate_brands(num_brands)
