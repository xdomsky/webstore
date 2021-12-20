from django.shortcuts import redirect, render
from .models import kontakt

# Create your views here.
def index(request):
    context = {}
    if request.POST:
        new_msg = kontakt.objects.create(name=request.POST['name'], email=request.POST['email'], phone=request.POST['phone'], msg=request.POST['msg'])
        new_msg.save()
        return redirect("Store:index")
    return render(request, 'Store/index.html', context)