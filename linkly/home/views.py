from django.shortcuts import render , redirect, HttpResponse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .models import UrlModel
import uuid
def homePage(request):
   if request.method == 'POST':
      link_ = request.POST["link"].replace('https://','').replace('http://','') # remove httpos:// keyworl form url
      link = 'http://' + link_
      # VALIDATING URL
      try:
         validate = URLValidator()
         validate(link)
      except ValidationError as e:
         return render(request,'index.html',{"error":list(e)[0],"submit_link":link_})

      #genarated random uuid and splite 8 byte
      short_ = str(uuid.uuid4()).replace('-','')[:8]
      # save url
      URL = UrlModel(main_url=link,short_url=short_)
      URL.save()

      return render(request,'index.html',{"link":'http://127.0.0.1:8000/'+short_,"submit_link":link_})
   return render(request,'index.html')

def shortUrl(request,slug):
   try:
      url = UrlModel.objects.get(short_url__exact=slug)
   except:
      return HttpResponse('wrong url')

   url.serve_count = url.serve_count + 1
   url.save()
   return redirect(url.main_url)