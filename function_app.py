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

    return func.HttpResponse(f'{timezone}')
