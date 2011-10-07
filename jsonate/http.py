from django.http import HttpResponse
from jsonate import jsonate

class JsonateResponse(HttpResponse):
    """
    Subclass of HttpResponse that turns just about anything into JSON
    via jsonate() and returns the result with mimetype "application/json"
    """
<<<<<<< HEAD
    def __init__(self, content,request=None, mimetype='application/json', *args, **kwargs):
        ret = jsonate(content)          #:MUST be JSON str
        callback = request.GET.get('callback',None ) if request else None
        if callback:
            ret = callback + "(%s);" % ret
        super(JsonateResponse, self).__init__(ret, mimetype, *args, **kwargs)
=======
    def __init__(self, content, mimetype='application/json', jsonp_callback=False, *args, **kwargs):
        json_content = jsonate(content)
        if jsonp_callback:
            json_content = jsonp_callback + "(" + json_content + ");"
        
        super(JsonateResponse, self).__init__(json_content, mimetype, *args, **kwargs)
>>>>>>> 7b1a191b3e0e15929054cc659d2b24f02d4a4b2e
