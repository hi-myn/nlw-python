from src.views.http_types.http_response import HttpResponse
from .error_type.http_unprocessable_entity import HttpUnprocessableEntityError

# exceptions - errors are treated like objects
def handle_errors(error: Exception) -> HttpResponse: 
    if isinstance(error, HttpUnprocessableEntityError):
        # customized errorClique para usar esta alternativa
        # send to a log or notification email - future implemations
        return HttpResponse( 
            status_code= error.status_code,
            body = {
                "errors" : [{
                    "title" : error.name,
                    "detail" : error.message
                }]
            }
        )


    return HttpResponse(
        status_code = 500,
        body = {
            "errors": [{
                "title": "Server Error", 
                "detail": str(error)
            }]
        }
    )
