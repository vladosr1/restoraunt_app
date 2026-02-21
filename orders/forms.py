from django import forms
from .models import Order

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["full_name", "phone", "address", "comment", "payment_method"]
        widgets = {
            "comment": forms.Textarea(attrs={"rows": 3}),
        }