from django.shortcuts import render
from django.http import HttpResponse

def showTest(request):
    res=render(request,'exam/test.html')
    que="Question ?"
    a="a"
    b="b"
    c="c"
    d="d"
    level='easy'
    data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level}
    res=render(request,'exam/test.html',context=data)
    return res

def showResult(request):
    s="<h1>this is result<h1>"
    return HttpResponse(s)
