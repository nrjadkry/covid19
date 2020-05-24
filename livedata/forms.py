from django import forms

class CovidForm(forms.Form):
	country=forms.CharField(required=True)
