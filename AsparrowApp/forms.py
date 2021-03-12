from AsparrowApp.models import Enqiury
from django import forms
class EnquiryForm(forms.ModelForm):
    class Meta:
        model= Enqiury
        fields = "__all__"