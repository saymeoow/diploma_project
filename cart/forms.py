from django import forms


SNEAKERS_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
SNEAKERS_SIZE_CHOISES = [(i, str(i)) for i in range(36, 46)]


class CartAddSneakersForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=SNEAKERS_QUANTITY_CHOICES,
        coerce=int,)
    sizes = forms.TypedChoiceField(
        choices=SNEAKERS_SIZE_CHOISES,
        coerce=int,)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
