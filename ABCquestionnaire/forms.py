from django import forms
from ABCquestionnaire.models import Value
from django.forms.widgets import RadioSelect
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

options=[
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
    ]

# class HorizontalRadioRenderer(RadioSelect.renderer):
#     def render(self):
#         return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class ValueForm(forms.ModelForm):
    # SN=forms.CharField(label='Please input your Student No',widget=forms.TextInput(attrs={'placeholder':'Student No'}),)
    choice1=forms.ChoiceField(choices=options, widget=RadioSelect(),)
    choice2=choice3=choice4=choice5=choice6=choice7=choice8=choice9=choice10=choice11=choice12=choice13=choice14=choice15=choice16=choice17=forms.ChoiceField(choices=options, widget=RadioSelect(),)  
    # def clean_choice1(self):
    #     data = self.cleaned_data.get('choice1')
    #     if not data:
    #         self.add_error("choice1","Please select one of these options") 
    # allchoices=([choice1,choice2,choice3,choice4,choice5,choice6,choice7,choice8,choice9,choice10,choice11,choice12,choice13,choice14,choice15,choice16,choice17])
    
    # choice=forms.ChoiceField(choices=options, widget=RadioSelect())

    # def clean(self):
    #     data=self.cleaned_data['choice1']
    #     if not data:
    #         self.add_error('choice1', 'Please select an option in the right')
    #     return data

    class Meta:
        model=Value
        fields=["choice1","choice2","choice3","choice4","choice5","choice6","choice7","choice8","choice9","choice10","choice11","choice12","choice13","choice14","choice15","choice16","choice17",]
        