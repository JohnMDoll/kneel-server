STYLES = [
    {
        "id": 1,
        "style": "Classic",
        "price": 500
    },
    {
        "id": 2,
        "style": "Modern",
        "price": 710
    },
    {
        "id": 3,
        "style": "Vintage",
        "price": 965
    }
]

def get_all_styles():
    """returns all listed style objects"""
    return STYLES

def get_single_style(id):
    """returns an style matching an style id"""
    requested_style = None
    for style in STYLES:
        if style["id"] == id:
            requested_style = style
    return requested_style
