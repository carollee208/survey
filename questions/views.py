from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from questions.models import Question, Response, User
from questions.forms import UserForm, UserModelForm

def questions(request):
    errors = []
    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if not request.POST.get('first_name', ''):
            errors.append('Enter First Name.')
        if not request.POST.get('last_name', ''):
            errors.append('Enter Last Name.')
        if not request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid email address.')
        if not request.POST.get('address', ''):
            errors.append('Enter address')
        if not request.POST.get('city', ''):
            errors.append('Enter city')
        if not request.POST.get('state'):
            errors.append('Enter state')
        if not request.POST.get('country'):
            errors.append('Enter country')
        if not request.POST.get('age'):
            errors.append('Enter age')
        if not request.POST.get('gender'):
            errors.append('Enter gender') 
        if not errors:
            if form.is_valid():
                instance = form.save(commit=False)
                user = User.objects.get(first_name=first_name, last_name=last_name, email=email, address=address, city=city, state=state, country=country, age=age, gender=gender)
                instance.user = user
                instance.save() 
            return HttpResponseRedirect("/thanks/")
    return render(request, 'questions.html', {
        'errors': errors,
        'First Name': request.POST.get('first_name',''),
        'Last Name': request.POST.get('last_name', ''),
        'Email': request.POST.get('email', ''),
        'Address': request.POST.get('address', ''),
        'City': request.POST.get('city', ''),
        'State': request.POST.get('state', ''),
        'Country': request.POST.get('country', ''),
        'Age': request.POST.get('age', ''),
        'Gender': request.POST.get('gender', ''),
    })

def thanks(request):
    return render(request,'thanks.html')
 
