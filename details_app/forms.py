from django import forms

from .models import DetailsModel

class DetailForm(forms.ModelForm):
    #print(dir(forms.widgets))
    class Meta:
        model = DetailsModel
        fields = ['first_name','last_name','age','address','gmail','phone','images'] 

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    gmail = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    phone = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}), required=True)
                                                                                              #Ensure that the 
                                                                                              #DetailForm allows the images field to be cleared.