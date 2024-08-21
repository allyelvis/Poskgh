import mysql.connector

class RestaurantPOS:
    def __init__(self, db_host: str, db_user: str, db_password: str, db_name: str):
        self.db_connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )

    def place_order(self, item_id: int, quantity: int):
        if item_id <= 0:
            raise ValueError("Invalid item ID.")
        if quantity <= 0:
            raise ValueError("Invalid quantity.")

        cursor = self.db_connection.cursor()

        # Check if enough stock is available
        cursor.execute("SELECT stock_quantity FROM items WHERE id = %s", (item_id,))
        result = cursor.fetchone()
        if not result or result[0] < quantity:
            return "Insufficient stock to fulfill the order."

        cursor.execute("UPDATE items SET stock_quantity = stock_quantity - %s WHERE id = %s", (quantity, item_id))
        self.db_connection.commit()

        return "Order placed successfully."

    def get_inventory(self):
        cursor = self.db_connection.cursor(dictionary=True)
        cursor.execute("SELECT id, name, price, stock_quantity FROM items")
        inventory = cursor.fetchall()
        return inventory
