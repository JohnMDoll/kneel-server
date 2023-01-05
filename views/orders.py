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

def create_order(order):
    """posts a new order"""
    max_id = ORDERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the order dictionary
    order["id"] = new_id

    # Add the order dictionary to the list
    ORDERS.append(order)

    # Return the dictionary with `id` property added
    return order

def delete_order(id):
    """deletes existing order with specified id"""
    order_index = -1

    # Iterate the ORDERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Store the current index.
            order_index = index

    # If the order was found, use pop(int) to remove it from list
    if order_index >= 0:
        ORDERS.pop(order_index)

def update_order(id, new_order):
    """updates an existing order with matching id with passed new order info"""
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Update the value.
            ORDERS[index] = new_order
            break
        