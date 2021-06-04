# I created this file

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')



def analyze(request):
    djtext = request.POST.get('text', 'default')
    # See here in index.html name of textarea is "text" so we have put text above
    # To see wether cheackbox are on or off.
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspace = request.POST.get('extraspace', 'off')
    numberremover = request.POST.get('numberremover','off')


    # see in index.html name of check box is removepunc  
    #print(removepunc)
    #print(djtext)
    analyzed = djtext
    purposes = ""
    if removepunc == "on":
        analyzed = ""
        punctuations = punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        purposes = purposes + "punctuations"
        params = {'purpose':purposes, 'analyzed_text':analyzed}
        #return render(request, 'analyze.html', params)

    
    if uppercase == "on":
        upper = ""
        for char in analyzed:
            upper = upper + char.upper()
        analyzed = upper
        purposes = purposes + " Uppercased"
        params = {'purpose':purposes, 'analyzed_text':upper}
    
    if newlineremover == "on":
        newline = ""
        for char in analyzed:
            if char != "\n" and char !="\r":
                newline = newline + char
        analyzed = newline
        purposes = purposes + " New line remover"
        params = {'purpose':purposes, 'analyzed_text':newline}
    
  

    if extraspace == "on":
        extraspace_txt = ""
        for i in range(len(analyzed)):
            if analyzed[i] == " " and analyzed[i+1] == " ":
                extraspace_txt = extraspace_txt + ""
                pass
            else:
                extraspace_txt = extraspace_txt + analyzed[i]
        analyzed = extraspace_txt
        purposes = purposes + " Extraspace Remover"
        params = {'purpose':purposes, 'analyzed_text':extraspace_txt}

    if (numberremover == "on"):
        numrevoerr = ""
        numbers = '0123456789'

        for char in analyzed:
            if char not in numbers:
                numrevoerr = numrevoerr + char
        
        params = {'purpose': 'Removed NewLines', 'analyzed_text': numrevoerr}
        djtext = analyzed
    
    """else:
        return HttpResponse('Error')"""
    
    
    return render(request, 'analyze.html', params)
    
    

    
    
    
    

 

