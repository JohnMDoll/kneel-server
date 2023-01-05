ORDERS = [
    {
        "id": 1,
        "orderId": 3,
        "sizeId": 2,
        "styleId": 3,
        "timestamp": 1614659931693
    }
]

def get_all_orders():
    """returns all listed order objects"""
    return ORDERS

def get_single_order(id):
    """returns an order matching an order id"""
    requested_order = None
    for order in ORDERS:
        if order["id"] == id:
            requested_order = order
    return requested_order
