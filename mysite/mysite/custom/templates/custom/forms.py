from django import from .forms import 
from django.contrib.auth.models import User

class CReg(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    re_password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']
    def clean(self):
        super(CReg,self).clean()
        p=self.cleaned_data.get("password")
        p1=self.cleaned_data.get("re_password")
        if p!=p1:
            raise forms.ValidationError("password didn't match")