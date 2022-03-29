from django.forms import ModelForm,TextInput,ImageField
from .models import Weather,Car

# Create the form class.
class CityForm(ModelForm):
   class Meta:
        model = Weather
        fields = ['city']
        widgets={'city' : TextInput(attrs={
            'placeholder':'Name of the city'
        }
        )
        }



class CarForm(ModelForm):
   class Meta:
        model = Car
        fields = ['carname','owner_phone','price','description','photo',]
        widgets = {'carname': TextInput(attrs={
            'placeholder': 'Enter Carname',
            'class':'form-control'
        }
        ),
            'owner_phone': TextInput(attrs={
                'placeholder': "Enter owner's phone",
                 'class':'form-control'
        }
            ),
            'price': TextInput(attrs={
                 'placeholder': 'Enter  a price',
                  'class': 'form-control'
        }
        ),
            'description' : TextInput(attrs={
                            'placeholder' : 'Enter description',
                            'class' : 'form-control'
        }
        ),


        }
