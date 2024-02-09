from src.views.http_types.http_response import HttpResponse
from src.errors.errors_type.http_unprocessable_entity_error import HttpUnprocessableEntityError
def handler_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError):
        return HttpResponse(
            # enviar para um log
            # enviar para um email
            status_code=error.code_status,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )
    return HttpResponse(
        status_code=500,
        body={
           "errors": [{
               "title": "Server Error",
               "detail": str(error)
           }]
        }
    )
