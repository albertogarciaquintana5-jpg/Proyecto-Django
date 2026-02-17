from django import forms
from ProyectoALmacen.models import childs, fathers, classroom

class ChildsForm(forms.ModelForm):
    class Meta:
        model = childs
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'average': forms.NumberInput(attrs={'class': 'form-control'}),
            'father': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'school': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class FathersForm(forms.ModelForm):
    class Meta:
        model = fathers
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = classroom
        fields = '__all__'
        widgets = {
            'clase': forms.TextInput(attrs={'class': 'form-control'}),
            'entrytime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'departuretime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'sites': forms.NumberInput(attrs={'class': 'form-control'}),
        }
