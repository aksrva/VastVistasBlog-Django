from django import forms


class CodeSubmissionForm(forms.Form):
    language = forms.ChoiceField(choices=[('python', 'Python'),
                                          ('javascript', 'JavaScript')])
    source_code = forms.CharField(widget=forms.Textarea, label='Source Code')
