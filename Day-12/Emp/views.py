from django.shortcuts import render,redirect
from Emp.models import UsrRg

# Create your views here.
def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def login(request):
	return render(request,'html/login.html')

def registration(request):
	if request.method=="POST":
		u=request.POST['uname']
		p=request.POST['pd']
		m=request.POST['eml']
		a=request.POST['ag']
		d={'us':u,'em':m,'age':a,'ps':p}
		return UsrRg(request,'html/details.html',{'d':d})
	return render(request,'html/register.html')


def crud(req):
	if req.method=="POST":
		un=req.POST['username']
		email=req.POST['email']
		pas=req.POST['password']
		age=req.POST['age']
		data2=UsrRg.objects.all()
		if len(un)!=0:
			data=UsrRg.objects.create(username=un,password=pas,email=email,age=age)
			return render(req,'html/actions.html',{'info':data2})
		data2=UsrRg.objects.all()
	return render(req,'html/actions.html')


def deletedata(req,id):
	data=UsrRg.objects.get(id=id)
	data.delete()
	return redirect("/cr")
		