from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

def hello_query(request):
    return HttpResponse(str("hello_from_server"))


def my_main_page(request):
    return render(request, 'prilogenie111/my_main_page.html', {})


@csrf_exempt
def get_proizved(request):
    s = str(request.body)
    print("-------------------------------------------");
    print("Body: " + s)
    mass = []
    mass = s.split("_")
    a = mass[1]
    b = mass[2]
    print("A = " + a)
    print("B = " + b)
    ans = int(a) * int(b)
    print("Ans = " + str(ans))
    print("-------------------------------------------");
    return HttpResponse(str(ans))

# gunicorn max_ajax_post.wsgi
