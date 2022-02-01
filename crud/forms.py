from django import forms 
from crud.models import User

# class Student(forms.ModelForm):
#     class Meta:
#         model = User
#         fields =[
#             'name',
#             'email',
#             'password'
#         ]
#         widgets = {
#             'name':forms.TextInput(attrs = {
#                 'class':'form-control',
#                 'placeholder':'name'
#             }),
#             'email':forms.EmailInput(attrs = {
#                 'class':'form-control'
#             }),
#             'password':forms.PasswordInput(attrs = {
#                 'class':'form-control'
#             })

#         }

class Student(forms.Form):
    name = forms.CharField(max_length = 50,label = False,widget = forms.TextInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Name'

        }
    ))

    email = forms.EmailField(label = False,widget = forms.EmailInput(
        attrs = {
            'class':'form-control',
             'placeholder':'Email'
            }
    ))
    password = forms.CharField( max_length= 10,label = False,widget = forms.PasswordInput(
        attrs = {
            'class':'form-control',
             'placeholder':'Password'
            }
    ))