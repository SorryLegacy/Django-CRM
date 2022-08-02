from django import forms


class OrderForm(forms.Form):
    """Form for get data from customer"""
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class' : 'form-control'}))