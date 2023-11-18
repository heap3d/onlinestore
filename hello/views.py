from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from onlinestore.settings import STATIC_DIR


# Create your views here.
def say_hello(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello World!</h1>
            <h2>Server Generated Page</h2>
            <p>The current time is { now.isoformat(sep=' ', timespec='seconds') }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)


def helloworld(request):
    now = datetime.now()
    return render(request, 'helloworld.html', {'curtime': now.isoformat(sep=' ', timespec='seconds')})
 

def index(request):
    now = datetime.now()
    print(STATIC_DIR)
    return render(request, 'main.html', {'curtime': now.isoformat(sep=' ', timespec='seconds'), 'staticdir': STATIC_DIR})

