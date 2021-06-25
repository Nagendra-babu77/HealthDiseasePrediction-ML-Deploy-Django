from django import forms
from django.forms import TextInput


class cancerform(forms.Form):
    mean_radius = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Mean Radius','style':'width: 130px; height: 28px', 'class': 'form-control'}))
    mean_texture = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Mean Texture','style':'width: 130px; height: 28px', 'class': 'form-control'}))
    mean_perimeter = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Mean Permeter','style':'width: 130px; height: 28px', 'class': 'form-control'}))
    mean_area = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Mean Area','style':'width: 130px; height: 28px', 'class': 'form-control'}))
    mean_smoothness = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Mean Smoothness','style':'width: 130px; height: 28px', 'class': 'form-control'}))


class diabetesform(forms.Form):
    Pregnancies = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Pregnancies','class': 'form-control'}))
    Glucose = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Glucose','class': 'form-control'}))
    Blood_Pressure = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Blood Pressure','class': 'form-control'}))
    Skin_Thickness = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Skin Thickness','class': 'form-control'}))
    Insulin = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Insulin','class': 'form-control'}))
    BMI = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'BMI','class': 'form-control'}))
    Diabetes_Pedigree_Function = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'DiabetesPedigreeFunction','class': 'form-control'}))
    Age = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Age', 'class': 'form-control'}))


sex_choice=[(1,'Male'),(0,'Female')]
cp_choice=[(0,'No Pain'),(1,'Medium'),(2,'High'),(3,'Very High')]
bs_choice=[(1,'Yes'),(0,'No')]
ecg_choice=[(0,'Low'),(1,'Medium'),(2,'High')]
slope_choice=[(0,'Unsloping'),(1,'Flat'),(2,'Down Sloping')]
ca_choice=[(0,0),(1,1),(2,2),(3,3)]

class heartform(forms.Form):
    age = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Age', 'class': 'form-control'}))
    Sex = forms.CharField(widget=forms.Select(choices=sex_choice,attrs={'placeholder':'Sex', 'class': 'form-control'}))
    Chest_Pain_Level = forms.CharField(widget=forms.Select(choices=cp_choice,attrs={'placeholder':'ChestPainLevel','class': 'form-control'}))
    Blood_Pressure = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'BloodPressure', 'class': 'form-control'}))
    Cholestoral = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Cholestoral', 'class': 'form-control'}))
    Blood_Sugar = forms.CharField(widget=forms.Select(choices=bs_choice,attrs={'placeholder':'Blood Sugar', 'class': 'form-control'}))
    ECG_Result = forms.CharField(widget=forms.Select(choices=ecg_choice,attrs={'placeholder':'Electrocardiographic Result', 'class': 'form-control'}))
    Maximum_Heart_Beat = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Maximum Heart Beat', 'class': 'form-control'}))
    Exercise_induced_Angina = forms.CharField(widget=forms.Select(choices=bs_choice,attrs={'placeholder':'exercise induced Angina', 'class': 'form-control'}))
    Depression_level = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Depression Level', 'class': 'form-control'}))
    Condition_During_Peak_Exercise = forms.CharField(widget=forms.Select(choices=slope_choice,attrs={'placeholder':'Condition During Peak Exercise', 'class': 'form-control'}))
    Result_of_Fluoroscopy = forms.CharField(widget=forms.Select(choices=ca_choice,attrs={'placeholder':'Result of Fluoroscopy', 'class': 'form-control'}))
    Thallium_Test = forms.CharField(widget=forms.Select(choices=ca_choice,attrs={'placeholder':'Thallium Test', 'class': 'form-control'}))


    