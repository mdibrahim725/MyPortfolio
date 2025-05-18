from django import forms
from base.models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactModel
        fields=['full_name','email','mobile_no','email_subject','message_box']
        widgets={
            'full_name':forms.TextInput(
                attrs={
                    'placeholder':'Enter Your Fullname',
                    'id':'contactname',
                    'required':True
                }
            ),
            'email':forms.TextInput(
                attrs={
                    'placeholder':'Enter Your Email Address',
                    'id':'contactemail',
                    'required':True
                }
            ),
              'mobile_no':forms.TextInput(
                attrs={
                    'placeholder':'Enter Your Mobile number',
                    'id':'contactmobile',
                    'required':True
                }
            ),
              'email_subject':forms.TextInput(
                attrs={
                    'placeholder':'Enter Subject',
                    'id':'contactemailsubject',
                    'required':True
                }
            ),
              'message_box':forms.Textarea(
                attrs={
                    'placeholder':'Your Message',
                    'id':'contactmessage',
                    'required':True,
                    'class':'message-box',
                }
            ),
        }
