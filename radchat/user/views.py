from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse, HttpResponse

from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as loginn
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .form import signup,CustomAuthenticationForm ,image_form,feedback_form
from django.contrib import messages
from .models import report
from .models import Profile
import boto3
from trp import Document
from django.conf import settings
import openai
import json
from django.views.decorators.csrf import csrf_exempt
import stripe


openai.api_key = "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"

media_root = settings.MEDIA_ROOT

stripe.api_key = settings.STRIPE_PRIVATE_KEY


def home(request):

    if request.method == 'POST':
        form=signup(request.POST)
        form2 =CustomAuthenticationForm(data=request.POST)
        if form2.is_valid():
            user=form2.get_user()
            loginn(request, user)
            return redirect('reports')
        # else:
        #     messages.error(request,('Email already used'))
        if form.is_valid():
            form.save()
            new_user = authenticate(first_name=form.cleaned_data['first_name'],password=form.cleaned_data['password1'],username=form.cleaned_data['username'])
            loginn(request, new_user)
            return redirect('reports')
        # else:
        #     print('retrurn anyway')
        #     return redirect('landing')


    else:
        form2=CustomAuthenticationForm()
    form = signup()
    return render(request,'index.html',{"form":form,'form2':form2,})

@login_required()
def reports(request):
    logged_in_user = request.user
    logged_in_user_posts = report.objects.filter(author=logged_in_user)
    if request.method == 'POST':
        img_form=image_form(request.POST,request.FILES)
        if img_form.is_valid():

            report_img=str(img_form.cleaned_data['report_image'])
            report_img_url=(media_root) +"\\"+ str(report_img)
            image_file = request.FILES['report_image']
            textract_client = boto3.client('textract',
                aws_access_key_id='AKIATU4GQIFAYTS2NAXT',
                aws_secret_access_key='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',
                region_name='us-east-1'
            )
            imageBytes  = bytearray(image_file.read())
            response = textract_client.detect_document_text(Document={'Bytes': imageBytes})
            text = ''
            for item in response['Blocks']:
                if item['BlockType'] == 'LINE':
                    text += item['Text'] + '\n'

            # img_form.save()
            instance = img_form.save(commit=False)
            instance.report_text = text
            instance.save() 
            # report.objects.filter(report_image=img_form.cleaned_data['report_image']).update(report_text=text)

            return redirect('reports')
    else:
        img_form = image_form()

    return render(request,'reports.html', {'reports': logged_in_user_posts,"img_form":img_form,"user":logged_in_user})

@login_required()
def plans(request):

    return render(request,'plans.html')

@login_required()
def logout_user(request):
    logout(request)
    return redirect('landing')


@login_required()
def report_chat(request,report_image):
    report_name=report.objects.get(report_image=report_image)
    counter=1
    model_engine = "text-davinci-003" 
    max_tokens = 200 
    max_tokens2 = 400 
    temperature = 0.5 
    response = openai.Completion.create(
        engine=model_engine,
        prompt=f"Please provide 5 short Frequently Asked Questions without answer for the findings in the report : {report_name.report_text}",
        max_tokens=max_tokens,
        temperature=temperature
    )

    generated_text = response.choices[0].text.split('.')
    generated_text.pop(0)
    count=0
    for i in generated_text[:-1]:
        generated_text[count] = i[:-2]
        count+=1
    generated_text=generated_text[:5]


    if request.method == 'POST':
        question=request.POST.get('input')
        answer = openai.Completion.create(
            engine=model_engine,
            prompt=question,
            max_tokens=max_tokens2,
            temperature=temperature
        )
        counter=0
        answer_text=answer.choices[0].text




        return render(request,'chat.html',{"report":report_name,"faq_list":generated_text,"counter":counter,})
    
    return render(request,'chat.html',{"report":report_name,"faq_list":generated_text,"counter":counter})


@login_required()
def chat(request):
    counter=1
    model_engine = "text-davinci-003" 
    max_tokens2 = 100 
    temperature = 0

    if request.method == 'POST':
        question=request.POST.get('input')
        print(question)
        answer = openai.Completion.create(
            engine=model_engine,
            prompt=question,
            max_tokens=max_tokens2,
            temperature=temperature
        )
        counter=0
        answer_text=answer.choices[0].text
        my_dict = {'question': question,'answer':answer_text}
        json_data = json.dumps(my_dict)



        return HttpResponse(json_data, content_type='application/json')
    


@login_required()
def feedback(request):
    logged_in_user = request.user
    if request.method == 'POST':
        form=feedback_form(request.POST)
        if form.is_valid():


            instance = form.save(commit=False)
            instance.author = logged_in_user
            instance.save() 
            return redirect('reports')
    else:
        form = feedback_form()


        return render(request,'feedback.html',{"form":form,})
    


@login_required()
def help_page(request):


        return render(request,'help.html')





@csrf_exempt
def checkout(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1Mp08ZDJu74hW1xG2qpmeoNa',
            'quantity': 1,
        }],
        mode='subscription',
        success_url=request.build_absolute_uri(reverse('thanks')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('reports')),
    )

    return JsonResponse({
        'session_id' : session.id,
        'stripe_public_key' : settings.STRIPE_PUBLIC_KEY
    })

@csrf_exempt
def checkout2(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1Mp09SDJu74hW1xGY9ZyxoNu',
            'quantity': 1,
        }],
        mode='subscription',
        success_url=request.build_absolute_uri(reverse('thanks2')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('reports')),
    )

    return JsonResponse({
        'session_id' : session.id,
        'stripe_public_key' : settings.STRIPE_PUBLIC_KEY
    })

@csrf_exempt
def checkout3(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1Mp0AwDJu74hW1xGi72DLRSj',
            'quantity': 1,
        }],
        mode='subscription',
        success_url=request.build_absolute_uri(reverse('thanks3')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('reports')),
    )

    return JsonResponse({
        'session_id' : session.id,
        'stripe_public_key' : settings.STRIPE_PUBLIC_KEY
    })




def thanks(request):
    username=request.user
    Profile.objects.filter(user = username).update(plan="individual")
    return redirect('reports')


def thanks2(request):
    username=request.user
    Profile.objects.filter(user = username).update(plan="monthly")
    return redirect('reports')


def thanks3(request):
    username=request.user
    Profile.objects.filter(user = username).update(plan="yearly")
    return redirect('reports')
