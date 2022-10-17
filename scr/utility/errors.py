class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class UpdatingProductError(Exception):
    pass

class DeletingProductError(Exception):
    pass

class ProductNotExistsError(Exception):
    pass

class FieldDoesNotExistError(Exception):
    pass



errors = {
    "InternalServerError": {
        "message": "Something went wrong on the code",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "UpdatingProductError": {
         "message": "Updating Product added by other is forbidden",
         "status": 403
     },
     "DeletingProductError": {
         "message": "Deleting Product added by other is forbidden",
         "status": 403
     },
     "ProductNotExistsError": {
         "message": "Product with given id doesn't exists",
         "status": 400
     },     
     "FieldDoesNotExistError": {
        "message": "The field is invalid",
        "status": 400
     },

}


### productCategory Errors

class UpdatingProductCategoryError(Exception):
    pass

class DeletingProductCategoryError(Exception):
    pass

class ProductCategoryNotExistsError(Exception):
    pass

class FieldDoesNotExistError(Exception):
    pass


errors = {
     
    "UpdatingProductCategoryError": {
         "message": "Updating Product added by other is forbidden",
         "status": 403
     },
     "DeletingProductCategoryError": {
         "message": "Deleting Product added by other is forbidden",
         "status": 403
     },
     "ProductCategoryNotExistsError": {
         "message": "Product with given id doesn't exists",
         "status": 400
     }, 
     "FieldDoesNotExistError": {
        "message": "The field is invalid",
        "status": 400
     }    
}

