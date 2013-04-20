# -*- coding:utf-8 -*-
import datetime
from django.http import HttpResponse

## hello视图
## 一个视图就是一个函数
def hello(request):
	## 返回一个HttpResponse对象
	## 这个对象包含了文本“Hello World!”
    return HttpResponse("Hello World!")

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
	## 用 assert False 去调试
	assert False
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)
