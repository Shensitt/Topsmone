from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Ваше имя", min_length = 2, max_length = 100)
    city = forms.CharField(label="Ваш город", min_length = 2, max_length = 100, required=False)
    job = forms.CharField(label="Ваша профессия или род занятий", min_length = 2, max_length = 100)
    gender = forms.ChoiceField(label="Ваш пол", 
                               choices=[('1', 'Мужской'), ('2','Женский')], 
                               widget=forms.RadioSelect)
    notice = forms.BooleanField(label="Получать новости сайта на e-mail?", required=False)    
    email = forms.CharField(label="Ваш e-mail",min_length=7)
    message = forms.CharField(label="Сообщение", widget=forms.Textarea(attrs={'rows':8, 'cols':40}))