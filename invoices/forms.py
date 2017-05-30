from django import forms

from invoices.models import Customer
import datetime

class InvoiceForm(forms.Form):
    FORMAT_CHOICES = (
        ('pdf', 'PDF'),
        ('docx', 'MS Word'),
    )
    number = forms.IntegerField(label='Invoice number:')
    place = forms.CharField(label='Place:')
    date = forms.DateField(label='Invoice Date:', initial=datetime.date.today)
    payment_date = forms.DateField(label='Payment Due Date:', initial=datetime.date.today)
    uic = forms.CharField(label='UIC:')
    vat_no = forms.CharField(label='VAT No.:')
    client_vat_no = forms.CharField(label="Buyer VAT No.:")
    bank = forms.CharField(label='Bank:')
    iban_number = forms.CharField(label='IBAN (EUR)')
    address = forms.CharField(label='Address:')
    client_address = forms.CharField(label='Buyer Address:')
    delivery_address = forms.CharField(label='Delivery address:')
    item_id = forms.IntegerField()
    item_description = forms.CharField()
    quantity = forms.IntegerField()
    unit_price = forms.IntegerField()
    amount = forms.IntegerField()
    value = forms.IntegerField()
    format = forms.ChoiceField(choices=FORMAT_CHOICES)
