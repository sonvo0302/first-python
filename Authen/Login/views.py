from django.shortcuts import render,HttpResponse
from django.views import View
from django.contrib.auth import authenticate,login,decorators
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

def IndexClass(request):
    return HttpResponse('Xin chào')

class LoginClass(View):
    def get(self,request):
        return render(request,'Login/login.html')
    def post(self,request):
        tendangnhap =request.POST.get('username')
        matkhau =request.POST.get('password')
        my_user=authenticate(username=tendangnhap,password=matkhau)
        if my_user is None:
            return HttpResponse('user is not exist')

        login(request,my_user)
        return render(request,'Login/success.html')
# Create your views here.
class ViewUser(LoginRequiredMixin,View):
    login_url = '/user/login/'

    def get(self,request):
        return HttpResponse('<h1>Day la view cua user</h1>')

    def post(self,request):
        pass
@decorators.login_required(login_url='/user/login/')
def view_product(request):
    return HttpResponse('xem sản phẩm')
