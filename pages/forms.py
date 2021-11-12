from django import forms
from django.urls import reverse_lazy

US_STATES = (
    ("", "---"),
    ("AL", "Alabama"),
    ("AK", "Alaska"),
    ("AZ", "Arizona"),
    ("AR", "Arkansas"),
    ("CA", "California"),
    ("CO", "Colorado"),
    ("CT", "Connecticut"),
    ("DE", "Delaware"),
    ("DC", "District of Columbia"),
    ("FL", "Florida"),
    ("GA", "Georgia"),
    ("HI", "Hawaii"),
    ("ID", "Idaho"),
    ("IL", "Illinois"),
    ("IN", "Indiana"),
    ("IA", "Iowa"),
    ("KS", "Kansas"),
    ("KY", "Kentucky"),
    ("LA", "Louisiana"),
    ("ME", "Maine"),
    ("MD", "Maryland"),
    ("MA", "Massachusetts"),
    ("MI", "Michigan"),
    ("MN", "Minnesota"),
    ("MS", "Mississippi"),
    ("MO", "Missouri"),
    ("MT", "Montana"),
    ("NE", "Nebraska"),
    ("NV", "Nevada"),
    ("NH", "New Hampshire"),
    ("NJ", "New Jersey"),
    ("NM", "New Mexico"),
    ("NY", "New York"),
    ("NC", "North Carolina"),
    ("ND", "North Dakota"),
    ("OH", "Ohio"),
    ("OK", "Oklahoma"),
    ("OR", "Oregon"),
    ("PA", "Pennsylvania"),
    ("RI", "Rhode Island"),
    ("SC", "South Carolina"),
    ("SD", "South Dakota"),
    ("TN", "Tennessee"),
    ("TX", "Texas"),
    ("UT", "Utah"),
    ("VT", "Vermont"),
    ("VA", "Virginia"),
    ("WA", "Washington"),
    ("WV", "West Virginia"),
    ("WI", "Wisconsin"),
    ("WY", "Wyoming"),
)

PAYMENT_METHOD = (
    ("cash", "Cash"),
    ("certified_check", "Certified Check"),
    ("check", "Check"),
    ("money_order", "Money Order"),
)

DOCUMENT_TYPE = (
    ("rent", "Demand for Rent($)"),
    ("non_compliance", "Non-Compliance with the Lease"),
)


class DateInput(forms.DateInput):
    input_type = "date"


class Form0(forms.Form):
    document_type = forms.ChoiceField(
        label="<strong>  Mark the Reason for This Notice </strong>",
        choices=DOCUMENT_TYPE,
        required=True,
        widget=forms.RadioSelect,
    )


class Form1(forms.Form):
    landlord_name = forms.CharField(
        label="<strong> Enter the Landlord's name </strong>",
        max_length=200,
        required=True,
    )


class Form2(forms.Form):
    landlord_street_address = forms.CharField(
        label="Street Adress", max_length=250, required=True
    )
    landlord_street_address_2 = forms.CharField(
        label="Address Line 2", max_length=250, required=False
    )
    landlord_city = forms.CharField(label="City", max_length=250, required=True)
    landlord_state = forms.ChoiceField(label="State", choices=US_STATES, required=True)
    landlord_zip_code = forms.CharField(label="Zip Code", max_length=250, required=True)


class Form3(forms.Form):
    phone = forms.CharField(
        label="<strong> Enter the Landlord's Telephone Number (Optional) </strong>",
        max_length=12,
        required=False,
    )
    email = forms.EmailField(
        label="<strong> Enter the Landlord's Email (Optional) </strong>",
        max_length=50,
        required=False,
    )


class Form4(forms.Form):
    tentant_name = forms.CharField(
        label=" <strong> Enter the Name(s) of the Tenant(s) </strong>",
        max_length=200,
        required=True,
    )


class Form5(forms.Form):
    tentant_street_address = forms.CharField(
        label="Street Adress", max_length=250, required=True
    )
    tentant_street_address_2 = forms.CharField(
        label="Address Line 2",
        max_length=250,
        required=False,
    )
    tentant_city = forms.CharField(label="City", max_length=250, required=True)
    tentant_state = forms.ChoiceField(label="State", choices=US_STATES, required=True)
    tentant_zip_code = forms.CharField(label="Zip Code", max_length=250, required=True)


class Form6(forms.Form):
    lease_begin_date = forms.DateField(
        label="<strong> When did the Lease begin? </strong>",
        widget=DateInput(),
        required=True,
    )


class Form7(forms.Form):
    rent_amount = forms.IntegerField(
        label="<strong> Enter the Amount Due by the Tenant(s) </strong", required=False
    )
    payment_method = forms.ChoiceField(
        label="<strong> Enter The Required Payment Method </strong>",
        choices=PAYMENT_METHOD,
        required=False,
        widget=forms.RadioSelect,
    )


class Form8(forms.Form):
    notice_date = forms.DateField(
        label="<strong> Enter the Date of This Notice? </strong>",
        widget=DateInput(),
        required=True,
    )
