from django.shortcuts import render
from django.views.generic import TemplateView

from account.forms import RegisterForm
from django.views import View
# Create your views here.
class Register(View):
    def get(self, request):
        register_form = RegisterForm
        context = {
            'register_form' : register_form
        }
        return render(request, '', context)
    def post(self, request):
        pass

class Test(TemplateView):
    template_name = 'account/register.html'
