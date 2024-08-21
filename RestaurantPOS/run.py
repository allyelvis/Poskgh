from src.restaurant_pos import RestaurantPOS
from config import db_config

def main():
    pos = RestaurantPOS(
        db_host=db_config.DB_HOST,
        db_user=db_config.DB_USER,
        db_password=db_config.DB_PASSWORD,
        db_name=db_config.DB_NAME
    )

    # Placing an order
    try:
        order_confirmation = pos.place_order(1, 5)
        print(order_confirmation)
    except ValueError as e:
        print(f"Error placing order: {e}")

    # Retrieving inventory information
    inventory = pos.get_inventory()
    for item in inventory:
        print(f"Item ID: {item['id']}, Name: {item['name']}, Price: {item['price']}, Stock Quantity: {item['stock_quantity']}")

if __name__ == "__main__":
    main()
