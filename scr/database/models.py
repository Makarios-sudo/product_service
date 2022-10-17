from datetime import datetime
from .db import db


class Product(db.Document):
    product_name = db.StringField(required=True)
    sale_price = db.IntField()
    discount_price = db.IntField()
    total_cost_price = db.IntField()
    color = db.StringField()
    image = db.StringField()
    created_at = db.DateTimeField(auto_now_add=True, default=datetime.now)

    meta = {
        "ordering" :["-created_at"]
    }


class ProductCategory(db.Document):
    category_name = db.StringField(required=True)
    created_at = db.DateTimeField(auto_now_add=True, default=datetime.now)

    meta = {
        "ordering" :["-created_at"]
    }


class ProductSubCategory(db.Document):
    fabric_type = db.StringField(required=True)
    created_at = db.DateTimeField(auto_now_add=True, default=datetime.now)

    meta = {
        "ordering" :["-created_at"]
    }




