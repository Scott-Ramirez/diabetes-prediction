from django import forms

class DiabetesPredictionForm(forms.Form):
    age = forms.IntegerField(label='Edad')
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Prefiero no decirlo')
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Género')
    weight = forms.FloatField(label='Peso (kg)')
    height = forms.FloatField(label='Altura (m)')
    fasting_glucose = forms.FloatField(label='Glucemia en Ayunas (mg/dl)')
