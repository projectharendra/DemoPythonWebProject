from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import usersForm

# Create your views here.
def home(request):   
    data = {
        'title':'My Home Page',
        'mydata':'Welcome to My Home Page',
        'clist' : ['PHP','JAVA','DJANGO'],
        'student_details' : 
        [
            {'name':'harendra','phone':'9958271070'},
            {'name':'rakesh','phone':'9313720199'},
        ]
    } 
    # return render(request,"home.html",{"name":"Harendra"})
    return render(request,"home.html",data)


def userForm(request):
    finalans=0
    
    
    try:
        val1 = int(request.GET["num1"])
        val2 = int(request.GET["num2"])
        finalans = val1 + val2
        data = {
            'n1':val1,
            'n2':val2,
            
            'output':finalans
        }
        url = "/about-us/?output={}".format(finalans)
        return HttpResponseRedirect(url)
        # return redirect(url)

    except:
        pass
    return render(request,"userForm.html",{'output':finalans}) 

def aboutUs(request):
    if request.method == "GET":
        output = request.GET.get('output')
    return render(request,"aboutUs.html",{'output':output})    



def add(request):    
    # val1 = int(request.GET["num1"])
    # val2 = int(request.GET["num2"])

    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    res = val1 + val2
    return render(request,"result.html",{'result':res})

def submitform(request):
    finalans=0
    fn = usersForm()
    data = {'form':fn}
    try:
        if request.method == "POST":
         val1 = int(request.POST["num1"])
         val2 = int(request.POST["num2"])
         finalans = val1 + val2
         data = {
            # 'n1':val1,
            # 'n2':val2,
            'form' : fn,
            'output':finalans
         }
        url = "/aboutus/?output={}".format(finalans)
        # return HttpResponseRedirect(url)
        return redirect(url)
        #return HttpResponse(finalans)

    except:
        pass
    return render(request,"userForm.html",data) 

def calculator(request):
    result=0
    try:
        if request.method == "POST":
         val1 = eval(request.POST.get("num1"))
         val2 = eval(request.POST.get("num2"))
         opr = request.POST["opr"]

         if(opr == "+"):
             result = val1 + val2
         elif(opr == "-"):
             result = val1 - val2
         elif(opr == "*"):
             result = val1 * val2
         elif(opr == "/"):
             result = val1 / val2             
    except:  
        pass     
    return render(request,"calculator.html",{'result':result}) 