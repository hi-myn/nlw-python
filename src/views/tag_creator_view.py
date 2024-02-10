from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
        responsabilities for intercting with HTTP
    '''
    def validate_and_create(self,  http_request: HttpRequest):
        body = http_request.body
        product_code = body["product_code"]

        #business rule logic - creating tags
        print("ESTOU NA MINHA VIEW")

        # http return 
        return HttpResponse(status_code = 200, body={"hello" : "world"})
