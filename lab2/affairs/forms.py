from django import forms
from .models import Trainee
 
 
# creating a form
class StudentForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Trainee
 
        # specify fields to be used
        fields = [
              'name',
              'bdate',
              'intake',
              'track',
        ]
    bdate = forms.DateField(
        widget=forms.DateInput(format='%m/%d/%Y', attrs={'class': 'datepicker'}),
        input_formats=('%m/%d/%Y', )
        )

class TraineeForm(forms.Form):
              name= forms.CharField(max_length=20)
              bdate=forms.DateField(label='Birth Date')
              intake=forms.CharField(max_length=20)
              track=forms.CharField(max_length=20)