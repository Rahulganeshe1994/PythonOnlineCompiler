from django.shortcuts import render
import sys



def index(request):
    return render(request,'index.html',)

def runcode(request):
    if request.method == 'POST':
        codearea=request.POST['codearea']
        try:
             data= sys.stdout
             sys.stdout = open('file.txt','w')

             exec(codearea)
             sys.stdout.close()
             sys.stdout=data

             output =open('file.txt','r').read()
        except Exception as e:
            sys.stdout=data
            output=e
    return render(request,"index.html",{'codearea':codearea,'output':output})

      

