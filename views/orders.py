import sqlite3
import models

ORDERS = [
    {
        "id": 1,
        "metalId": 3,
        "sizeId": 2,
        "styleId": 3,
        "timestamp": 1614659931693
    }
]


def get_all_orders():
    """returns all orders from db"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            o.id,
            o.metal_id,
            Metals.metal,
            Metals.price AS metal_price,
            o.size_id,
            Sizes.carets,
            Sizes.price AS size_price,
            o.style_id,
            Styles.style,
            Styles.price as style_price,
            o.timestamp
        FROM Orders o
        JOIN Sizes ON Sizes.id = o.size_id
        JOIN Metals ON Metals.id = o.metal_id
        JOIN Styles ON Styles.id = o.style_id
        """
        )
        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()
        orders = []
        # Create an order instance from the current row
        for row in dataset:
            order = models.Order(
                row['id'],
                row['metal_id'],
                row['size_id'],
                row['style_id'],
                row['timestamp'],
            )

            style = models.Style(
                row['style_id'],
                row['style'],
                row['style_price']
                )

            size = models.Size(
                row['size_id'],
                row['carets'],
                row['size_price']
            )

            metal = models.Metal(
                row['metal_id'],
                row['metal'],
                row['metal_price']
            )
        
            order.style = style.__dict__
            order.size = size.__dict__
            order.metal = metal.__dict__

            orders.append(order.__dict__)
    return orders


def get_single_order(id):
    """returns an order matching an order id"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        order = None
        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            o.id,
            o.metal_id,
            Metals.metal,
            Metals.price AS metal_price,
            o.size_id,
            Sizes.carets,
            Sizes.price AS size_price,
            o.style_id,
            Styles.style,
            Styles.price as style_price,
            o.timestamp
        FROM Orders o
        JOIN Sizes ON Sizes.id = o.size_id
        JOIN Metals ON Metals.id = o.metal_id
        JOIN Styles ON Styles.id = o.style_id
        WHERE o.id = ?
        """, (id,)
        )
        # Convert rows of data into a Python list
        data = db_cursor.fetchone()
        # Create an order instance from the current row
        order = models.Order(
            data['id'],
            data['metal_id'],
            data['size_id'],
            data['style_id'],
            data['timestamp'],
        )

        style = models.Style(data['style_id'], data['style'], data['style_price'])

        size = models.Size(data['size_id'], data['carets'], data['size_price'])

        metal = models.Metal(data['metal_id'], data['metal'], data['metal_price'])
        order.style = style.__dict__
        order.size = size.__dict__
        order.metal = metal.__dict__

        order = (order.__dict__)

    return order


def create_order(order):
    """posts a new order"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        # Just use these. It's a Black Box.
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        INSERT INTO Orders
            (metal_id, size_id, style_id, timestamp)
        VALUES
            ( ?, ?, ?, ?);
        """, (order['metalId'], order['sizeId'], order['styleId'], order['timestamp'],)
        )
        id = db_cursor.lastrowid
        order['id'] = id
    return order


def delete_order(id):
    """deletes existing order with specified id"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        # Just use these. It's a Black Box.
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            DELETE FROM Orders
                WHERE id = ?
            """, (id,),
        )


def update_order(id, new_order):
    """updates an existing order with matching id with passed new order info"""
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Update the value.
            ORDERS[index] = new_order
            break
