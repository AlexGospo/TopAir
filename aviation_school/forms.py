from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    phone = forms.CharField(label='Phone', widget=forms.TextInput(attrs={'type': 'tel'}))
    message = forms.CharField(widget=forms.Textarea)