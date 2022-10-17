import datetime
from flask import Response, jsonify, request
from ..database.models import ProductCategory
from flask_restful import Resource
from mongoengine.errors import (
    FieldDoesNotExist, DoesNotExist,ValidationError, InvalidQueryError
)
from ..utility.errors import (
    SchemaValidationError, InternalServerError, UpdatingProductCategoryError,
    DeletingProductCategoryError, ProductCategoryNotExistsError,FieldDoesNotExistError
)



class ProductCategoriesApi(Resource):

    def get(self):
        try:
            productCategories = ProductCategory.objects.all()
            return Response(
                productCategories.to_json(), 
                mimetype="application/json", 
                status=200
            )
        except DoesNotExist:
            raise ProductCategoryNotExistsError
        except Exception:
            raise InternalServerError


    def post(self):
        try:
            body = request.get_json()
            productCategories = ProductCategory.objects.create(
                category_name = body["category_name"]
            )
            productCategories.save()
            return Response(
                productCategories.to_json(), 
                mimetype="application/json", 
                status=200
            )
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except Exception as e:
            raise InternalServerError



class PrdouctCategoryApi(Resource):
    def get(self, id):
        
        
        try:
            productCategory = ProductCategory.objects.get(id=id)
            return Response(
                productCategory.to_json(), 
                mimetype="application/json",
                status=200
        )
        except:
            return jsonify(
                
                message="that Id does not exist",
                status=404
            )


    def put(self, id):
        update_productCategory = ProductCategory.objects.get(id=id)
        body = request.get_json()

        update_productCategory.update(
            category_name = body["category_name"]
        )
        update_productCategory.save()
        return Response(
            update_productCategory.to_json(),
            mimetype="application/json",
            status=200
        )
    
    def delete(self, id):
        delete_productCategory = ProductCategory.objects.get(id=id)
        delete_productCategory.delete()
        return jsonify({
            "message": "product_category was successfully deleted"
        })



class PrdouctCategorySearchApi(Resource):
    def get(self):
        category_name = request.args.get("category_name")
        created_at = request.args.get("created_at")

        if category_name:
            productCategory = ProductCategory.objects(category_name__icontains = category_name)
        elif created_at:
            productCategory = ProductCategory.objects(created_at__icontains = datetime.datetime.now())
        else:
            return jsonify({
                "messeage":"please enter a valid field and value"
            })
        
        return Response(
            productCategory.to_json(),
            mimetype="application/json",
            status=200
        )