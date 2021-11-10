from django import forms


class Form2(forms.Form):
    landlord_name = forms.CharField(max_length=250, required=True)

    landlord_name.widget.attrs.update(
        {
            "class": "form-control",
            "placeholder": "Your name",
        }
    )
