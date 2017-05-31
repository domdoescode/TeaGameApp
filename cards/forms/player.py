from django import forms


class PlayerForm(forms.Form):

    name = forms.CharField(label='Player Name', max_length=100)
    drink_type = forms.ChoiceField(choices=(
        ("Tea", 'tea'),
        ("Coffee", 'coffee'),
    ))
    milk = forms.BooleanField(label="Milk?")
    sugar = forms.IntegerField(label="Sugars?")
