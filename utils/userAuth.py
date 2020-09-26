from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
import json

class AuthMiddleware(MiddlewareMixin):
  def process_request(self, request):
    # result = { 'code': '13', 'msg': '没有登陆'}
    # return HttpResponse(json.dumps(result), content_type="application/json")
    print(12313132132)
  
  def process_response(self, request, response):
    return response

  def process_exception(self, request, exception):#引发错误 才会触发这个方法
    print(exception, request.path)
    result = { 'code': -1, 'msg': str(exception), 'url': request.path}
    return HttpResponse(json.dumps(result), content_type="application/json") #返回错误信息
