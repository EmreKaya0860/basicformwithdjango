from django import forms

from .models import Message

class MessageForm(forms.ModelForm):
    name = forms.TextInput()
    email = forms.TextInput()
    phone = forms.TextInput()
    message = forms.TextInput()
    class Meta:
        model = Message
        fields = ('name', 'email', 'phone', 'message')