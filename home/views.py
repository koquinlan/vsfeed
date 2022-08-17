from django.shortcuts import render

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        template_name = "home/userhome.html"
    else:
        template_name = "home/home.html"

    return render(
        request,
        template_name,
        {},
    )
