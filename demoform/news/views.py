from django.shortcuts import render,redirect
from django.http import HttpResponse
from  .forms import PostForm,SendEmail
from django.views import View
from .models import Post
# Create your views here.
class index(View):
    def get(self,request):
        ketqua = 'Hello World'
        return HttpResponse(ketqua)
# class PostClass(View):
#     def get(self,request):
#         c=PostForm()
#         return render(request,'news/add_new.html',{'post':c})

class PostClass(View):
    def get(self,request):
        c = PostForm()
        return render(request, 'news/add_new.html', {'post': c})
    def post(self, request):
        c=PostForm(request.POST)
        if c.is_valid():
            c.save()
            return render(request,'news/news_list.html',{"list":Post.objects.all()})
        else:
            return render(request,'news/add_new.html',{"post":PostForm()})
        return HttpResponse('Error Form')

class PostListClass(View):
    def get(self,request):
        p=Post.objects.all()
        return render(request,'news/news_list.html',{"list":p})

class PostUpdateClass(View):
    def get(self,request,pk):
        p=Post.objects.get(id=pk)
        form = PostForm(instance=p)
        context ={"form":form}
        return render(request,'news/post_update.html',context)
    def post(self,request,pk):
        p=Post.objects.get(id=pk)
        form=PostForm(request.POST,instance=p)
        if form.is_valid():
            form.save()
            return render(request,'news/post_update.html',{"form":form,"message":"Success"})
        else:
            return render(request,'news/post_update.html',{"form":form,"message":"Error"})

class PostDeleteClass(View):
    def get(self,request,pk):
        p = Post.objects.get(id=pk)
        return render(request, 'news/delete.html', {"post": p})

    def post(self, request, pk):
        p = Post.objects.get(id=pk)
        p.delete()
        return render(request,'news/news_list.html',{"list":Post.objects.all()})

def emailview(request):
    e=SendEmail()
    return render(request,'news/email.html',{"e":e})
def process(request):
    if request.method=='POST':
        e=SendEmail(request.POST);
        if e.is_valid():
            tieude=e.cleaned_data['title']
            cc=e.cleaned_data['cc']
            noidung=e.cleaned_data['content']
            email=e.cleaned_data['email']
            context={'td':tieude,'c':cc,'nd':noidung,'email':email}
            #context2={'data':e}
            return render(request,'news/print_email.html',{"e":context})
        else:
            return HttpResponse('Form is not validated')
    else:
        return HttpResponse('Error')