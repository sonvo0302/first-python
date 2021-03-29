from django.shortcuts import render,HttpResponse
from django.views import View
from django.contrib.auth import authenticate,login,decorators
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
# Create your views here.

def index(request):
    HttpResponse('Xin chào')

class LoginClass(View):
    def get(self,request):
        return render(request,'LoginApp/login.html')
    def post(self,request):
        tendangnhap =request.POST.get('username')
        matkhau =request.POST.get('password')
        my_user=authenticate(username=tendangnhap,password=matkhau)
        if my_user is None:
            return HttpResponse('user is not exist')

        login(request,my_user)
        return render(request,'LoginApp/success.html')

class ViewUser(LoginRequiredMixin,View):
    login_url = '/login/'

    def get(self,request):
        return HttpResponse('<h1>Day la view cua user</h1>')

    def post(self,request):
        pass
@decorators.login_required(login_url='/login/')
def view_product(request):
    return HttpResponse('xem sản phẩm')

class AddPost(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request):
        f=PostForm();
        context={'form':f}
        return render(request,'LoginApp/add_post.html',context)
    def post(self,request):
        f=PostForm(request.POST)
        if f.is_valid():
            if request.user.has_perm('LoginApp.add_post'):
                f.save()
                return HttpResponse('ok')
            else: return HttpResponse('no permission')
            #print(request.user.get_all_permission())
        else:
            return HttpResponse('add fail')
        return HttpResponse('Error Form')