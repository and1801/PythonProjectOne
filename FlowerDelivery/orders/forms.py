from django import forms

class OrderForm(forms.Form):
    delivery_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Дата доставки'
    )
    delivery_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        label='Время доставки'
    )
    address = forms.CharField(
        max_length=255,
        label='Адрес доставки'
    )
    comment = forms.CharField(
        widget=forms.Textarea,
        required=False,
        label='Комментарий'
    )