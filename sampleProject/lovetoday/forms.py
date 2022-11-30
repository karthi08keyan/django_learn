from django import forms

class FormInfo(forms.Form):
    empno = forms.IntegerField()
    name = forms.CharField()
    salary = forms.IntegerField()
    address = forms.CharField()