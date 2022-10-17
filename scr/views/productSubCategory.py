import datetime
from flask import Response, jsonify, request
from flask_restful import Resource

from scr.database.models import ProductSubCategory


class ProductSubCategoriesApi(Resource):
        
    def get(self):
        product_sub = ProductSubCategory.objects.all()
        return Response(
            product_sub.to_json(),
            mimetype="apllication/json",
            status=200
        ) 

    def post(self):
        body = request.get_json()
        product_sub = ProductSubCategory.objects.create(
            fabric_type = body["fabric_type"]
        )
        product_sub.save()
        return Response(
            product_sub.to_json(),
            mimetype="apllication/json",
            status=200
        ) 



class ProductSubCategoryApi(Resource):
    def get(self, id):
        try:
            
            product_sub = ProductSubCategory.objects.get(id=id)
            return Response(
                product_sub.to_json(),
                mimetype="application/json",
                status=200
            )
        except:
            return jsonify({
                "message":"that Id does not exist",   
            })


    def put(self, id):
        try:
            update_product_sub = ProductSubCategory.objects.get(id=id)
            body = request.get_json()

            update_product_sub.update(
                fabric_type  = body["fabric_type"]
            )
            update_product_sub.save()
            return Response(
                update_product_sub.to_json(),
                mimetype="application/json",
                status=200
            )
        except:
            return jsonify({
                "message":"an error occurred"
            })


    def delete(self, id):
        try:
            product_sub = ProductSubCategory.objects.get(id=id)
            product_sub.delete()
            return jsonify({
                "message":"product_sub_category deleted successfully"
            })    
        except:
            return jsonify({
                "message":"that Id does not exist"
            })



class ProductSubCategorySearchApi(Resource):
    def get(self):
        fabric_type = request.args.get("fabric_type")
        created_at = request.args.get("created_at")

        if fabric_type:
            product_sub = ProductSubCategory.objects(fabric_type__icontains = fabric_type)
        elif created_at:
            product_sub =  ProductSubCategory.objects(created_at__lte = datetime.datetime.now())
        else:
            return jsonify({
                "messeage":"please enter a valid field and value"
            })
        
        return Response(
            product_sub.to_json(),
            mimetype="application/json",
            status=200
        )