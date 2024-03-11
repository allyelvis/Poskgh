# Import necessary libraries
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated in-memory database for stock levels
stock_data = {
    "product1": 100,
    "product2": 200,
    # Add more products and initial stock levels
}

# Endpoint for real-time sales data
@app.route("/sales", methods=["POST"])
def record_sales():
    try:
        data = request.get_json()
        product_id = data.get("product_id")
        quantity_sold = data.get("quantity_sold")

        # Update stock levels
        if product_id in stock_data:
            stock_data[product_id] -= quantity_sold
            return jsonify({"message": f"Sale recorded for {product_id}."}), 200
        else:
            return jsonify({"error": f"Product {product_id} not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint for checking stock levels
@app.route("/stock/<product_id>", methods=["GET"])
def get_stock(product_id):
    if product_id in stock_data:
        return jsonify({"stock_level": stock_data[product_id]}), 200
    else:
        return jsonify({"error": f"Product {product_id} not found."}), 404

if __name__ == "__main__":
    app.run(debug=True)
