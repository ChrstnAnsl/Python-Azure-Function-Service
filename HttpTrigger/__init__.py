import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Your function logic here
    return func.HttpResponse("Hello from Azure Functions!")
