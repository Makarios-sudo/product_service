from ..views.product import ProductsApi, ProductApi, ProductSearchApi
from ..views.productCategory import PrdouctCategoryApi, ProductCategoriesApi, PrdouctCategorySearchApi
from ..views.productSubCategory import ProductSubCategoriesApi, ProductSubCategoryApi, ProductSubCategorySearchApi


def initialize_routes(api):
    api.add_resource(ProductsApi, "/api/products")
    api.add_resource(ProductApi, "/api/product/<id>")
    api.add_resource(ProductSearchApi, '/api/products/search/')

    api.add_resource(ProductCategoriesApi, "/api/product_category")
    api.add_resource(PrdouctCategoryApi, "/api/product_category/<id>")
    api.add_resource(PrdouctCategorySearchApi, "/api/product_category/search/")

    api.add_resource(ProductSubCategoriesApi, "/api/product_sub_category")
    api.add_resource(ProductSubCategoryApi, "/api/product_sub_category/<id>")
    api.add_resource(ProductSubCategorySearchApi, "/api/product_sub_category/search/")
    




