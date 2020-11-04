from django.http import HttpResponse
import json
from django.views.decorators.http import require_http_methods, require_POST
from django.template.context_processors import csrf
from first.models import onemore as model

@require_http_methods(['POST'])
def add_book(request):
  # pub_obj = model.Publish.objects.filter(pk=1).first()
  # pub_id = pub_obj.pk

  book = model.Book1.objects.create(title="冲灵剑法", price=100, pub_date="2004-04-04", publish_id=request.POST.get('publish_id'))
  result = {'code': 0, 'msg': '添加成功'}
  return HttpResponse(json.dumps(result), content_type="application/json")

@require_http_methods(['GET'])
def get_book(request):
  # pub_obj = model.Publish.objects.filter(pk=1).first()
  # pub_id = pub_obj.pk

  books = model.Book1.objects.all()
  temp = []
  for book in books:
    res = book.authors.all()
    authors = []
    for i in res:
      authors.append(i.name)


    temp.append({
      'title': book.title,
      'price': str(book.price),
      'pub_date': str(book.pub_date),
      'publish': {
        'city': book.publish.city,
        'name': book.publish.name
      },
      'authors': authors
    })

    
  result = {'code': 0, 'msg': '查询成功', 'data': temp}
  return HttpResponse(json.dumps(result), content_type="application/json")

@require_http_methods(['POST'])
def add_author(request):
  # 找到书
  book = model.Book1.objects.filter(id=request.POST.get('book_id')).first()

  wang = model.Author.objects.filter(name='令狐冲').first()
  li = model.Author.objects.filter(name='任我行').first()
  book.authors.add(wang, li)
  result = {'code': 0, 'msg': '添加成功'}
  return HttpResponse(json.dumps(result), content_type="application/json")