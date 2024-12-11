from django import forms


class RegistrationForm(forms.Form):
    name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email=forms.EmailField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'})) 
    confirm_password=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'})) 
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        
        if name and len(name) < 9:
            self.add_error('name','name must be greater than')
    