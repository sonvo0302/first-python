from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= ('title','content','created_at',)
        widgets ={
            'title':forms.TextInput(attrs={'class':'tieude'}),
        }
    def __init__(self,*args,**kwargs):
        super(PostForm,self).__init__(*args,**kwargs)

class SendEmail(forms.Form):
    title=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'tieude'}))
    email=forms.EmailField()
    content=forms.CharField(widget=forms.Textarea(attrs={'class':'content','id':'noidung'}))
    cc =forms.BooleanField(required=False)

