from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
        responsibility for interacting with HTTP
    '''
    def authenticate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body["product_code"]
        print(product_code)
        #Lógica
        #retorno
        return HttpResponse(status_code=200,body={"hello": "word"})
