from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25) # будет использоваться для имени человека, отправляющего пост
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea) # опциональнo, но задан конкретно-прикладной виджет прорисовки поля
    """
    Заранее заданный виджет можно переопределять посредством атрибута widget. В поле comments используется виджет Textarea,
    чтобы отображать его как HTML-элемент <textarea> вместо используемого по умолчанию элемента <input>
    """












