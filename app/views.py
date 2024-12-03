from django.shortcuts import render

def jinja_print(request):
    d={'name':'Mercy','age':22}
    return render(request,'jinja_print.html',context=d)

