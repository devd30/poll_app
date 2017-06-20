from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Choice, Question ,Signup ,Comments
from django.utils import timezone

class Login_form(forms.Form):
	username = forms.CharField(label = "your name",max_length = "100")
	password = forms.CharField(max_length=32, widget=forms.PasswordInput)

	def check_login(self):
	     username = self.cleaned_data['username']
	     password = self.cleaned_data['password'] 
	     user = authenticate(username = username,password = password)
	     return user

class Sign_up(forms.Form):
	username = forms.CharField(label = "your name",max_length = "100")
	password = forms.CharField(max_length=32, widget=forms.PasswordInput)

	def create_new_user(self):
		username = self.cleaned_data['username']
		password = self.cleaned_data['password']
		user = User.objects.create_user(username,username,password)
		user.save()


class AddQuestion(forms.Form):
    question = forms.CharField(label = "Add Question" , max_length = "100")
    choice1  = forms.CharField(label = "choice 1" , max_length = "100")
    choice2  = forms.CharField(label = "choice 2" , max_length = "100")
    choice3  = forms.CharField(label = "choice 3", max_length = "100")
    choice4  = forms.CharField(label = "choice 4", max_length = "100" , required = False)
    choice5  = forms.CharField(label = "choice 5", max_length = "100" , required = False)

    def create_new_question(self):
        question = self.cleaned_data['question']
        choice1  = self.cleaned_data['choice1']
        choice2  = self.cleaned_data['choice2']
        choice3  = self.cleaned_data['choice3']
        choice4  = self.cleaned_data['choice4']
        choice5  = self.cleaned_data['choice5']
        q = Question(question_text = question,pub_date = timezone.now())
        q.save()
        cobj1 =  q.choice_set.create(choice_text=choice1, votes=0)
        cobj2 =  q.choice_set.create(choice_text=choice2, votes=0)
        cobj3 =  q.choice_set.create(choice_text=choice3, votes=0)
        choice = [cobj1 , cobj2 , cobj3]
        #q.choice_set.create(choice_text=choice4, votes=0)
        #q.choice_set.create(choice_text=choice5, votes=0)
        return choice



class CommentsForm(forms.Form):
    author = forms.CharField(label = "Name", max_length = "100")
    msg = forms.CharField(label = "Comment" , max_length = "500")

    def create_new_comment(self):
        author = self.cleaned_data['author']
        msg = self.cleaned_data['msg']
        obj = Comments(author = author , msg = msg)
        obj.save()
        return obj


#class Qadd(forms.Form):
#    question = forms.CharField(max_length = "100")
#    name = forms.CharField(max_length = "100")
#    def qadd():
#         q = Question(question_text = question,pub_date = timezone.now())
#         q.save()
#         return q
