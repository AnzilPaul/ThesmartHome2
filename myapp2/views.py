from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myapp1.models import Operatelog
# Create your views here.
def output(request):
    return render(request,"myapp2/boutput.html")
    #return HttpResponse("this is output page")
    #bobj=Operatelog.objects.last()
    #status_value=bobj.status
    #return JsonResponse({'statuso':status_value})
    #return render(request,"myapp2/boutput.html",{'statuso':status_value})