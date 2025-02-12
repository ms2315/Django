
class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response 

    def __call__(self, request):
        
        '''
        Here is the request phase Before execute view
        '''
        
        print(f"🔍 Middleware BEFORE request: {request.path} ") 

        response = self.get_response(request) 
        
        '''
        Here is the request phase Before execute view
        '''

        if response is None:  
            print("🚨 LoggerMiddleware detected a None response, returning error JSON")
            
        print(f"✅ Middleware AFTER response: {response.status_code}") 

        return response
        