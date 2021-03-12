from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from rest_framework.parsers import JSONParser

from .forms import ChoiceForm
from .models import Question, Choice
# Create your views here.
def index(request):
    myname="Son"
    taisan = ["Phone", "Laptop", "Plane"]
    context ={"name":myname,"taisan":taisan}
    return render(request,"polls/index.html",context)
def new_choice(request):
    form=ChoiceForm();
    if(request.method=='POST'):
        form=ChoiceForm(request.POST);
        if form.is_valid():
            form.save();
            return render(request, 'polls/choice_new.html',{"form":ChoiceForm()})
    return render(request,'polls/choice_new.html',{"form":form})
def updateChoice(request, pk):
	choice = Choice.objects.get(id=pk)
	form = ChoiceForm(instance=choice)
	if request.method == 'POST':
		form = ChoiceForm(request.POST, instance=choice)
		if form.is_valid():
			form.save()
			return render(request, 'polls/choice_new.html', {"form":ChoiceForm()})

	context = {'form':form};    
	return render(request, 'polls/choice_new.html', context)

def deleteChoice(request, pk):
	choice = Choice.objects.get(id=pk)
	if request.method == "POST":
		choice.delete()
		return render('/')

	context = {'item':choice}
	return render(request, 'accounts/delete.html', context)
# def new_choice(request):
#     q = Question.objects.all();
#     if(request.method=='GET'):
#         return render(request,"polls/choice_new.html",{"question":q});
#     if(request.method=='POST'):
#
#         # question = request.POST['dropdown1'];
#         # choice_text =request.POST['text_choice'];
#         # vote=0
#         form = ChoiceForm(request.POST);
#         form.save();
#         # form = Choice();
#         # form.question=request.POST['dropdown1'];
#         # form.choice_text=request.POST['text_choice'];
#         # form.save();
#         return render(request,"polls/question_list.html",{"question":q,"choice":form});

def viewlist(request):
    list_question = Question.objects.all();
    context = {"dsquest": list_question}
    return render(request,"polls/question_list.html",context)

def viewDetail(request,pk):
    q = Question.objects.get(pk=pk);
    context = {"question": q}
    return render(request, "polls/detail_question.html", context)




def vote(request,pk):
    q=Question.objects.get(pk=pk);
    try:
        dulieu=request.POST["choice"];
        c=q.choice_set.get(pk=dulieu);
    except:
        HttpResponse('Lỗi không có choice');
    c.vote=c.vote+1;
    c.save();
    return  render(request,"polls/result.html",{"question":q});
