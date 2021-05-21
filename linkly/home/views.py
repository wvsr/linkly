from django.shortcuts import render , redirect, HttpResponse
from .models import UrlModel
import uuid
def homePage(request):
   if request.method == 'POST':
      link = request.POST["link"]
      short_ = str(uuid.uuid4()).replace('-','')[:8]
      URL = UrlModel(main_url=link,short_url=short_)
      URL.save()
      return render(request,'index.html',{"link":'http://127.0.0.1:8000/'+short_,"submit_link":link})
   return render(request,'index.html')

def shortUrl(request,slug):
   try:
      url = UrlModel.objects.get(short_url__exact=slug).main_url
   except:
      return HttpResponse('wrong url')
   return redirect(url)