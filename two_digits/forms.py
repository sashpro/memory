from django import forms

class DigitForm(forms.Form):
    digit = forms.CharField()
    word = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass