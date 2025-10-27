from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'app_1/home.html')
    # return HttpResponse('Hello From App_1/Home')