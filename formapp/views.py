from django.shortcuts import render
from django.views import generic
from .models import Message
from .forms import MessageForm

# Create your views here.

from django.http import HttpResponse


class HomePageView(generic.ListView):
    template_name = 'formapp/HomePage.html'
    context_object_name = 'message_list'

    def get_queryset(self):
        return Message.objects.all()

def FirstPage(request):
    return render(request, 'formapp/FirstPage.html')


def SecondPage(request):
    return render(request, 'formapp/SecondPage.html')

def ThirdPage(request):
    context_object_name = 'message_list'
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'formapp/ThirdPage.html', {context_object_name: Message.objects.filter().order_by('pk')[:1], 'form': MessageForm()})
    else:
        form = MessageForm(request.POST)   
    return render(request, 'formapp/ThirdPage.html', {'form': form})