from datetime import datetime
import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

#Function Example 1 : HTTP Trigger
#Functions work with decorators
@app.function_name(name='TimeZoneHttpTrigger')
@app.route(route='timezone', auth_level = func.AuthLevel.ANONYMOUS)
def TimeZoneHttpTrigger(req: func.HttpRequest) -> func.HttpResponse:
    """
    """
    logging.info('Timezone HTTP trigger function received a request')

    timezone = req.get_json().get('timezone')
    
    #extension of the task : check if there is a timezone variable that exist

    if not timezone:
        try:
            req_body = req.get_body()
        except ValueError:
            pass
        else:
            timezone = req_body.get('timezone')
    
    if timezone:
        return func.HttpResponse(
            f'{timezone}'
        )
    else:
        return func.HttpResponse(
            "Please send an appropriate request to the API",
            status_code=200
        )
    return func.HttpResponse(f'{timezone}')
