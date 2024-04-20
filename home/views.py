from django.http import HttpResponse
from django.template import loader
import re

def home(request):
    template = loader.get_template("home.html")
    context = {
      'is_login': False
    }
    try:
        match = re.findall(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', request.POST["username"])
        if len(match) == 1:
            context = {
              'is_login': True
            }
        return HttpResponse(template.render(context, request))
    except KeyError:
        return HttpResponse(template.render(context, request))
