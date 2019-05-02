# from django import forms
from django.forms import ModelForm, Form
from django_jsonforms.forms import JSONSchemaField

class FlexibleForm(Form):

    json = JSONSchemaField(
        schema='static/static.json',
        options='static/options.json'
    )


# class CreateCsvForm(forms.Form):
#     register = forms.CharField()
#     headers = forms.CharField(widget=forms.Textarea)


# class UpdateCsvForm(forms.Form):
#
#     def __init__(self, *args, **kwargs):
#         extra = kwargs.pop('extra')
#         super(UpdateCsvForm, self).__init__(*args, **kwargs)
#
#         for i, heading in enumerate(extra):
