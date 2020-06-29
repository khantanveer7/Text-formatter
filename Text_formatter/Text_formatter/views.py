from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html' )
    

def analyze(request):
    text = request.POST.get('text', 'default')
    uppercase = request.POST.get('uppercase', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    removepunc = request.POST.get('removepunc', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    if (removepunc == "on"):
        punctuations = '''~!"#$%&'()*+,-./:;<=>?@[\]^_`{|}'''
        analyzed = ""
        for char in text:
            if char  not in punctuations:
                analyzed =  analyzed + char 
        params = {'analyzed_text' : analyzed }
        text = analyze
        
    if(uppercase == "on" ):
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()
        params = {'analyzed_text' : analyzed }
        text = analyze
       

    if(lowercase == "on"):
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.lower()
        params = {'analyzed_text' : analyzed }
        text = analyze
        

    if (spaceremove == "on"):
        analyzed = ""
        for index, char in enumerate(text):
            if text [index] == " " and text[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char    
        params = {'analyzed_text' : analyzed }

    
    if (removepunc != "on" and uppercase != "on" and lowercase != "on" and spaceremove != "on"):
        return HttpResponse("<h1> ERROR </h1>")   

    return render (request, 'analyze.html' , params)
        
    




    

