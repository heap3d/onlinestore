from datetime import datetime
from django.shortcuts import render


# Create your views here.
def index(request):
    now = datetime.now()
    return render(
        request, 
        'hello/index.html', 
        {'curtime': now.isoformat(sep=' ', timespec='seconds')}
        )
