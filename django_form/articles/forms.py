from django import forms

class ArticleForm(forms.Form):
    # max, min 길이 지정 가능 optional
    title= forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class':'my-title',
                'placeholder':'Enter the title!',
            }
        )
    )
    content=forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'my-content',
                'placeholder':'Enter the content',
                'row':5,
                'cols':50,
            }
        )
    )