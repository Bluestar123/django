from django.http import HttpResponse
import json
from django.views.decorators.http import require_http_methods, require_POST
from django.template.context_processors import csrf
from first import models

@require_http_methods(['GET'])
def index(request):
  
  result = {"password": 'assadf', "encrypt": '4e43332', 'id': request.GET.get("id")}
  return HttpResponse(json.dumps(result), content_type="application/json")

@require_http_methods(['POST'])
def post(request):
  # print(sadf)  异常中间件返回
  result = {"password": '11111', "encrypt": '22222222', 'id': request.POST.get("id")}
  return HttpResponse(json.dumps(result), content_type="application/json")



def get_csrf(request):
        #生成 csrf 数据，发送给前端
    x = csrf(request)
    csrf_token = x['csrf_token']
    return HttpResponse(csrf_token)

@require_http_methods(['POST'])
def add_book(request):
  print('add_book')
  title = request.POST.get("title") or ''

  price = request.POST.get("price")
  publish = request.POST.get("publish")
  date = request.POST.get("date")
  book = models.Book.objects.get_or_create(title=title,price=price,publish=publish,pub_date=date)
  return HttpResponse(json.dumps({'code': 0, 'msg': '添加成功'}), content_type="application/json")

@require_http_methods(['GET'])
def get_book(request):
  books = models.Book.objects.all()
  temp = []
  for i in books:
    print(i.price)
    temp.append({
      'title': i.title,
      'price': i.price.to_eng_string(),
      'publish': i.publish,
      'pub_date': str(i.pub_date),
      'create_time': str(i.create_time)[0:19]
    })
  print(temp)
  return HttpResponse(json.dumps({'code': 0, 'msg': '成功', 'list': temp}), content_type="application/json")



@require_http_methods(['GET'])
def get_book_by_id(request):
  books = models.Book.objects.filter(pk=request.GET.get('id'))
  temp = []
  for i in books:
    print(i.price)
    temp.append({
      'title': i.title,
      'price': i.price.to_eng_string(),
      'publish': i.publish,
      'pub_date': str(i.pub_date),
      'create_time': str(i.create_time)[0:19]
    })
  return HttpResponse(json.dumps({'code': 0, 'msg': '成功', 'list': temp}), content_type="application/json")
