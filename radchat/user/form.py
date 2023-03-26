from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import report
from .models import feedback





class signup(UserCreationForm):
    # email=forms.EmailField()
    class Meta:
        model = User
        fields = ('first_name','username','password1')
    def __init__(self, *args, **kwargs):
        super(signup, self).__init__(*args, **kwargs)

        for fieldname in ['first_name', 'password1','username', 'password2']:
            self.fields[fieldname].help_text = None

    def __init__(self, *args, **kwargs):
        super(signup, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None
        self.fields['username'].help_text = None
        self.fields['username'].label = "Email"
        self.fields['first_name'].label = "Name"

class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Email',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['password'].help_text = None
        self.fields['username'].help_text = None




class image_form(forms.ModelForm):
    author = forms.CharField()
    report_image = forms.ImageField()
    class Meta:
        model = report
        fields = ('author','report_image')
    def __init__(self, *args, **kwargs):
        super(image_form, self).__init__(*args, **kwargs)
        self.fields['author'].help_text = None
        self.fields['report_image'].help_text = None



class feedback_form(forms.ModelForm):
    author = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your thought..'}))
    class Meta:
        model = feedback
        fields = ('feedback',)
    def __init__(self, *args, **kwargs):
        super(feedback_form, self).__init__(*args, **kwargs)
        self.fields['author'].help_text = None
        self.fields['feedback'].help_text = None
