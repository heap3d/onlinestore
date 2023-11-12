from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def say_hello(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello World!</h1>
            <h2>Server Generated Page</h2>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)


def helloworld(request):
    return render(request, 'helloworld.html')
 

def index(request):
    return render(request, 'main.html')
