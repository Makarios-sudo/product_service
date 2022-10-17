
import datetime
import json
from flask import Response, jsonify, request
from ..database.models import Product
from flask_restful import Resource
from mongoengine.errors import (
    FieldDoesNotExist,DoesNotExist,ValidationError, InvalidQueryError, 
)

from ..utility.errors import  (
   SchemaValidationError, InternalServerError, DeletingProductError, 
   UpdatingProductError, ProductNotExistsError
)
from mongoengine.queryset.visitor import Q

class ProductsApi(Resource):

    def get(self):
        products = Product.objects.all()
        return Response( products.to_json(), mimetype="application/json", status=200 )

    def post(self):
        try:
            data = request.get_json()
            product = Product.objects.create(
                product_name = data["product_name"],
                sale_price = data["sale_price"],
                discount_price = data["discount_price"],
                total_cost_price = data["total_cost_price"],
                color = data["color"],
                image = data["image"]
            )
            product.save()
            return Response(product.to_json(), mimetype="application/json", status=200  )
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except Exception as e:
            raise InternalServerError
        

class ProductApi(Resource):
    def get(self, id):
        try:
            product = Product.objects.get(id=id).to_json()
            return Response(product, mimetype="application/json", status=200 )
        except:
            return jsonify(
                
                message="that Id does not exist",
                status=404
            )


    def put(self, id):
        try:
            update_product = Product.objects.get(id=id)
            data = request.get_json()
        
            update_product.update(
                product_name = data["product_name"],
                sale_price = data["sale_price"],
                discount_price = data["discount_price"],
                total_cost_price = data["total_cost_price"],
                color = data["color"],
                image = data["image"]
            )
            update_product.save()
            return Response(update_product.to_json(), mimetype="application/json", status=200)
        except Exception:
            raise  InternalServerError


    def delete(self, id):
        try:
            delete_product = Product.objects.get(id=id)
            delete_product.delete()
            return jsonify({
                "message": "product deleted successfully"
            })
        except Exception:
            raise InternalServerError


class ProductSearchApi(Resource):
     def get(self):
        product_name = request.args.get("product_name")
        sale_price = request.args.get("sale_price")
        discount_price  = request.args.get("discount_price")
        total_cost_price = request.args.get("total_cost_price")
        color = request.args.get("color")
        image = request.args.get("image")
        created_at = request.args.get("created_at")
        
        if product_name:
            products = Product.objects(product_name__icontains = product_name)
        elif sale_price:
            products = Product.objects(sale_price__lte = sale_price)
        elif discount_price:
            products = Product.objects(discount_price__lte = discount_price)
        elif total_cost_price:
            products = Product.objects(total_cost_price__lte = total_cost_price)
        elif color:
            products = Product.objects(color__icontains = color)
        elif image:
            products = Product.objects(image__icontains = image)
        elif created_at:
            products =  Product.objects(created_at__lte = datetime.datetime.now())
        else:
            return jsonify({
                "messeage":"please enter a valid field and value"
            })
            

        return Response( products.to_json(), mimetype="application/json", status=200 )
        