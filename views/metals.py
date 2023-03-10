import sqlite3
import models

METALS = [
    {
        "id": 1,
        "metal": "Sterling Silver",
        "price": 12.42
    },
    {
        "id": 2,
        "metal": "14K Gold",
        "price": 736.4
    },
    {
        "id": 3,
        "metal": "24K Gold",
        "price": 1258.9
    },
    {
        "id": 4,
        "metal": "Platinum",
        "price": 795.45
    },
    {
        "id": 5,
        "metal": "Palladium",
        "price": 1241.0
    }
]


def get_all_metals():
    """returns all listed metal objects"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute(
            "SELECT * FROM Metals"
        )

    dataset = db_cursor.fetchall()
    metals = []
    for row in dataset:
        metal = models.Metal(row['id'], row['metal'], row['price'] )

        metals.append(metal.__dict__)

    return metals

def get_single_metal(id):
    """returns an metal matching an metal id"""
    requested_metal = None
    for metal in METALS:
        if metal["id"] == id:
            requested_metal = metal
    return requested_metal

def update_metal(id, new_metal):
    """replaces existing db metal entry with new data"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        UPDATE Metals
            SET
                metal = ?,
                price = ?
        WHERE id = ?
        """, (new_metal['metal'], new_metal['price'], id, ),
        )

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    return True
