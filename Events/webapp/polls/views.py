from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Choice, Question ,Signup , Comments
from django.template import loader
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import *
from .forms import Login_form ,Sign_up ,AddQuestion ,CommentsForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers


@login_required(login_url='/polls/loginid/')
def index(request):
    my_questions = []
    latest_question_list = Question.objects.order_by('-pub_date')#[:9]
    for question in latest_question_list:
        if question.pub_date < timezone.now():
            my_questions.append(question)
        
    template = loader.get_template('polls/index.html')
    context = {
        'my_questions': my_questions,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/polls/loginid/')
def detail(request,question_id):
   try:
       question = Question.objects.get(pk=question_id)
   except Question.DoesNotExist:
       raise Http404("Question does not exist")
   return render(request, 'polls/detail.html', {'question': question})

@csrf_exempt
@login_required(login_url='/polls/loginid/')
def vote(request, question_id):
    data = []
    choices = []
    kchoices = []
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        choices = question.choice_set.all()
        for nchoice in choices:
            kchoices.append({"choice" : nchoice.choice_text , "votes" :  nchoice.votes , "choice_id" : nchoice.id})
           
        data  = {"q_text" : question.question_text , "choices" : kchoices}
        return JsonResponse(data = data , safe = False)
        #return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def fetchvote(request,question_id):
    i = 0
    data = []
    choices = []
    kchoices = []
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    for nchoice in choices:
        kchoices.append({"choice" : nchoice.choice_text , "votes" :  nchoice.votes , "choice_id" : nchoice.id ,"inde" : i })
        i = i + 1 
    data  = {"q_text" : question.question_text , "choices" : kchoices }
    print(data)
    return JsonResponse(data = data , safe = False)


@login_required(login_url='/polls/loginid/')
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def loginid(request):
    form = Login_form(request.POST or None)
    if request.method == "POST":
        
        if form.is_valid():
            user = form.check_login()
            if user is not None:
                if user.is_active:
                    login(request, user)
                    print ("hello")
                    return HttpResponseRedirect(reverse('polls:index'))
            else :
                print ("bye")
                return HttpResponse("Invalid Email and password")
        else :
            form = Login_form()
    return render(request,'polls/login_user.html', {'form': form })
    
    

#def login(request):
#    if request.method == "POST":
#        form = Login_form(request.POST)
#        if form.is_valid():
 #           print ("hello")

            
#    else:
 #       form = Login_form()

#    return render(request,'polls/login_user.html', {'form': form })


#def authenticate(request):
#    m = User.objects.get(username=request.POST.get('username',False)
#    if m.password == request.POST.get('password' , False):
#        request.session['member_id'] = m.id
#        return HttpResponse("You're logged in.")
#    else:
#        return HttpResponse("Your username and password didn't match.")

#def signup(request):
#     if request.method == "POST":
#        form = Sign_up(request.POST)
#        if form.is_valid():
#            print ("hello")
#            form.create_new_user()
#        else :
#            print ("bye")
#     else:
#        form = Sign_up()
#
#     return render(request,'polls/signup_user.html', {'form': form })
def signup(request):
     if request.method == "POST":
        form = Sign_up(request.POST)
        if form.is_valid():
            print ("hello")
            form.create_new_user()
        else :
            print ("bye")
     else:
        form = Sign_up()

     return render(request,'polls/signup_user.html', {'form': form })


def logoutid(request):
    logout(request)
    return HttpResponseRedirect(reverse('polls:login'))


def addquestion(request):
    if request.method == "POST":
        form = AddQuestion(request.POST)
        if form.is_valid():
            print("hey")
            q = form.create_new_question()
        else:
            print("bye")

    else:
        form = AddQuestion()
    return render(request , 'polls/addquestion.html',{'form':form})


def fetchdata(request):
    data = {"data":[{"id":1388534400000,"text":"Hey there!","author":"Pete Hunt"},{"id":1420070400000,"text":"React is *great*!","author":"Paul O\u2019Shannessy"},{"id":1466768846854,"text":"hello","author":"hey"},{"id":1466768846856,"text":"hello","author":"hello"},{"id":1466768846756,"text":"hello","author":"bye"},{"id":1466768846769,"text":"ello","author":"bye"}]}
    return JsonResponse(data)


def fetchit(request):
    return render(request , 'polls/fetchit.html')



@csrf_exempt
def comment(request):
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            obj = form.create_new_comment()
            jsonDict = {"comment":obj.msg, "author":obj.author}
            return JsonResponse(data = jsonDict,safe = False)
    else:
        form = CommentsForm()
    print (form.errors)
    return render(request , 'polls/comments.html' ,{'form':form})


def image(request):
    print("here")
    data = {"data":[{"url" : "https://s3-us-west-2.amazonaws.com/fs-blog-images/drink_pea2.jpg"},{"url" : "https://s3-us-west-2.amazonaws.com/fs-blog-images/drink_pea1.jpg"}]}
    return JsonResponse(data = data)


def getImage(request):
    num = add.delay(19,9)
    send_simple_message.delay()
    print (num)
    return render(request, 'polls/indexreact.html')


@csrf_exempt
def fetchQuestion(request):
    
    data = []
    kchoice = []
    ques_obj = Question.objects.all()
    for ques_list in ques_obj:
        choice = ques_list.choice_set.all()
        kchoice = []
        
        for nchoices in choice:
            kchoice.append({"choice_id" : nchoices.id , "choice_text" : nchoices.choice_text , "ques_id" : nchoices.question_id , "votes" : nchoices.votes })
            
        data.append({"q_id" : ques_list.id , "question_text" : ques_list.question_text , "choices" :  kchoice})
        

    return JsonResponse(data = data , safe = False)

@csrf_exempt
def questionurl(request):
    return render(request, 'polls/fetchQuestions.html')


@csrf_exempt
def questionaddreact(request):
   
    kchoice = []
    if request.method == "POST":
        form = AddQuestion(request.POST)
        if form.is_valid():
            print("hey")
            choices = form.create_new_question()
            for nchoices in choices:
              kchoice.append({"choice_id" : nchoices.id , "choice_text" : nchoices.choice_text , "ques_id" : nchoices.question_id ,"votes" : nchoices.votes })
              
            jsonDict = {"q_id" : choices[0].question_id , "question_text" : choices[0].question.question_text , "choices" : kchoice}
            return JsonResponse(data = jsonDict , safe =  False)
        else:
            print("bye")

    else:
        form = AddQuestion()
    return render(request , 'polls/addquestion.html',{'form':form})

@csrf_exempt
def questionurls(request):
    return render(request , 'polls/maptofor.html')

@csrf_exempt
def questionadd(request):
    
    name = [] 
    choices = []
    kchoice = []
    if request.method == "POST":
        num = int(request.POST['num'])
        name = request.POST.getlist('name[]')
        question = request.POST['question']
        q = Question(question_text = question,pub_date = timezone.now())
        q.save()
        #print(question)
        #print(name)
        #print(num)
        for i in range(0,num+1):
            choices.append(q.choice_set.create(choice_text=name[i], votes=0))
            #print(name[i])
        #print (request.POST)

        for nchoices in choices:
            kchoice.append({"choice_id" : nchoices.id , "choice_text" : nchoices.choice_text , "ques_id" : nchoices.question_id , "votes" : nchoices.votes })
            
        jsonDict = {"q_id" : choices[0].question_id , "question_text" : choices[0].question.question_text , "choices" : kchoice}
    return JsonResponse(data = jsonDict , safe =  False)
    


        

