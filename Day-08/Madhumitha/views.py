from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return HttpResponse("<h2 style='color:pink;background-color:#000080'>This is Madhumitha</h2>")


def chk(request):
	return HttpResponse("<script>alert('Hi Good afternoon')</script><h2>Welcome</h2>")

def homepage(request):
	return render(request,'ht/homepage.html')

def lgn(re):
	return render(re,'ht/login.html')

def reg(rt):
	return render(rt,'ht/register.html')