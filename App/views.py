from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse, redirect
from datetime import datetime
from App.models import Contact
from App.models import Service




# Manually message is successfully send or not
from django.contrib import messages   
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
import pickle



from django.shortcuts import render


from django.shortcuts import render
import pickle

def mlmodel(request):
    if request.method == 'POST':
        type = int(request.POST['type'])
        carpetarea = int(request.POST['carpetarea'])
        metrodistence = int(request.POST['metrodistence'])
        ecodistence = int(request.POST['ecodistence'])
        malldistence = int(request.POST['malldistence'])

        data = [[type, carpetarea, metrodistence, ecodistence, malldistence]]
        with open('E:/ML_VIDEO/ML - Classes/Djproject/Djproject/Hello/model1.pkl', 'rb') as file:
            model = pickle.load(file)
        res = model.predict(data)

        context = {
            'prediction': res[0]
        }
        return render(request, 'mlmodel.html', context)

    return render(request, 'mlmodel.html')





def Index(request):
    return render(request,'index.html')
def about(request):
    return render(request, 'about.html')
def analytics(request):
    return render(request, 'analytics.html')
   
def services(request):
    if request.method == "POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        address=request.POST.get('address')
        streetaddress=request.POST.get('streetaddress')
        city=request.POST.get('city')
        state=request.POST.get('state')
        abc=request.POST.get('abc')
        status=request.POST.get('status')
        residential=request.POST.get('residential')
        ybd=request.POST.get('ybd')
        dop=request.POST.get('dop')
        famt=request.POST.get('famt')
        asf=request.POST.get('asf','Na')
        loan=request.POST.get('loan')
        desc=request.POST.get('desc')
        services=Service(name=name, phone=phone,email=email,
                         address=address,streetaddress=streetaddress,city=city,
                         state=state,abc=abc,status=status,residential=residential,
                         ybd=datetime.today(),dop=datetime.today(),famt=famt,asf=asf,loan=loan,desc=desc)
        

        services.save()
        messages.success(request,'Your message has been sent')
        return redirect('services')
    else:
        abc=['Residential','Commercial','Industrial','Hospitality','REIT','Retail','Other']
        status=['Self Use','Rental','Under Construction','Disputed']
        residential=['Apartment','Independent Floor','Independent House','Villa']
        return render(request,'services.html',{'abc': abc,'status':status,'residential':residential})
    
        
        





def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email, phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,'Your message has been sent')
    return render(request, 'contact.html')

