from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/contact.html', {'content':['Tel 098 294 0231',
    'Email green13cafe@gmail.com']})
