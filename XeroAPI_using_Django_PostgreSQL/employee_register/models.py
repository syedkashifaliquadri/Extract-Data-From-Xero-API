from django.db import models

# Create your models here.

class InvoiceTypes(models.Model):
    ACCPAY = models.IntegerField(max_length=50)
    ACCREC = models.IntegerField(max_length=50)



class AddressType(models.Model):
    address_type = models.CharField(max_length=500)
    address_line1 = models.CharField(max_length=500)
    address_line2 = models.CharField(max_length=500)
    address_line3 = models.CharField(max_length=500)
    address_line4 = models.CharField(max_length=500)
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    attention_to = models.CharField(max_length=255)


class ContactPerson(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email_address = models.CharField(max_length=500)
    include_in_emails = models.BooleanField()


class Phone(models.Model):
    phone_type = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=500)
    phone_area_code = models.CharField(max_length=500)
    phone_country_code = models.CharField(max_length=500)


class SalesTrackingCategory(models.Model):
    tracking_category_name = models.CharField(max_length=500)
    tracking_option_name = models.CharField(max_length=500)


class ContactGroup(models.Model):
    name = models.CharField(max_length=500)
    status = models.CharField(max_length=500)
    contact_group_id = models.CharField(max_length=500)

class BrandingTheme(models.Model):
    branding_theme_id = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    logo_url = models.CharField(max_length=500)
    BTtype = models.CharField(max_length=500)
    sort_order = models.IntegerField(max_length=500)
    created_date_utc = models.DateTimeField(auto_now_add=True,null=True)

class BatchPaymentDetails(models.Model):
    bank_account_number =  models.CharField(max_length=500)
    bank_account_name =  models.CharField(max_length=500)
    details =  models.CharField(max_length=500)
    code =  models.CharField(max_length=500)
    reference =  models.CharField(max_length=500)

class Attachment(models.Model):
    attachment_id = models.CharField(max_length=500)
    file_name = models.CharField(max_length=500)
    url =  models.CharField(max_length=500)
    mime_type = models.CharField(max_length=500)
    content_length = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    include_online = models.BooleanField()

class ValidationError(models.Model):
    message = models.CharField(max_length=500)

class AccountsReceivable(models.Model):
    outstanding = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    overdue = models.DecimalField(decimal_places=3,max_digits=10,null=True)

class AccountsPayable(models.Model):
    outstanding = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    overdue = models.DecimalField(decimal_places=3,max_digits=10,null=True)

class Balances(models.Model):
    accounts_receivable = models.ForeignKey(AccountsReceivable, on_delete=models.CASCADE)
    accounts_payable = models.ForeignKey(AccountsPayable, on_delete=models.CASCADE)




class Contact(models.Model):
    contact_number	= models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    contact_status = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50)
    skype_user_name	 = models.CharField(max_length=50)
    contact_persons	 = models.ForeignKey(ContactPerson, on_delete=models.CASCADE)
    bank_account_details = models.CharField(max_length=50)
    tax_number = models.CharField(max_length=50)
    accounts_receivable_tax_type = models.CharField(max_length=50)
    accounts_payable_tax_type = models.CharField(max_length=50)
    addresses = models.ForeignKey(AddressType, on_delete=models.CASCADE)
    phones = models.ForeignKey(Phone, on_delete=models.CASCADE)
    is_supplier	 = models.BooleanField()
    is_customer = models.BooleanField()
    xero_network_key = models.CharField(max_length=50) 
    sales_default_account_code = models.CharField(max_length=50)
    purchases_default_account_code = models.CharField(max_length=50)
    sales_tracking_categories = models.ForeignKey(SalesTrackingCategory, on_delete=models.CASCADE)
    purchases_tracking_categories = models.ForeignKey(SalesTrackingCategory, on_delete=models.CASCADE)
    tracking_category_name = models.CharField(max_length=50)
    tracking_category_option = models.CharField(max_length=50)
    updated_date_utc = models.DateTimeField(auto_now_add=True,null=True)
    contact_groups = models.CharField(ContactGroup, on_delete=models.CASCADE)
    website = models.CharField(max_length=50)
    branding_theme = models.ForeignKey(BrandingTheme, on_delete=models.CASCADE)
    batch_payments = models.ForeignKey(BatchPaymentDetails, on_delete=models.CASCADE)
    discount = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    balances = models.ForeignKey(Balances, on_delete=models.CASCADE)
    attachments = models.ForeignKey(Attachment, on_delete=models.CASCADE)
    has_attachments	 = models.BooleanField()
    validation_errors =  models.ForeignKey(ValidationError, on_delete=models.CASCADE)
    has_validation_errors = models.BooleanField()
    status_attribute_string = models.CharField(max_length=50)

        
class LineItemTracking(models.Model):
    tracking_category_id = models.CharField(max_length=500)
    tracking_option_id = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    option = models.CharField(max_length=500)



class LineItem(models.Model):
    line_item_id = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    quantity = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    unit_amount = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    item_code = models.CharField(max_length=500)
    account_code = models.CharField(max_length=500)
    tax_type = models.CharField(max_length=500)
    tax_amount = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    line_amount = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    tracking = models.ForeignKey(LineItemTracking, on_delete=models.CASCADE)
    discount_rate = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    discount_amount = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    repeating_invoice_id = models.CharField(max_length=500)



class Payment(models.Model):
    invoice = models.ForeignKey(Invoices, on_delete=models.CASCADE)
    prepayment = models.ForeignKey(Prepayment, on_delete=models.CASCADE)
    overpayment = models.ForeignKey(Overpayment, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=500)
    credit_note_number = models.CharField(max_length=500)
    code = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True,null=True)
    currency_rate = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    amount = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    reference = models.CharField(max_length=500)
    is_reconciled = models.BooleanField()
    status = models.CharField(max_length=500)
    payment_type = models.CharField(max_length=500)
    updated_date_utc = models.DateTimeField(auto_now_add=True,null=True)
    payment_id = models.CharField(max_length=500)
    bank_account_number = models.CharField(max_length=500)
    particulars = models.CharField(max_length=500)
    details = models.CharField(max_length=500)
    has_account = models.BooleanField()
    has_validation_errors = models.BooleanField()
    status_attribute_string = models.CharField(max_length=500)
    validation_errors = models.ForeignKey(Contact, on_delete=models.CASCADE)

class Prepayment(models.Model):
    Ptype = models.CharField(max_length=500)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=500)
    line_items = models.ForeignKey(LineItem, on_delete=models.CASCADE)
    sub_total = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    total_tax = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    total = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    reference = models.CharField(max_length=500)
    updated_date_utc = models.DateTimeField(auto_now_add=True,null=True)
    prepayment_id = models.CharField(max_length=500)
    currency_rate = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    remaining_credit = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    allocations = models.ForeignKey(Allocation, on_delete=models.CASCADE)
    applied_amount = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    has_attachments = models.BooleanField()
    attachments = models.ForeignKey(ValidationError, on_delete=models.CASCADE)


class Overpayment(models.Model):
    Ptype = models.CharField(max_length=500)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=500)
    line_items = models.ForeignKey(LineItem, on_delete=models.CASCADE)
    sub_total = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    total_tax = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    total = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    updated_date_utc = models.DateTimeField(auto_now_add=True,null=True)
    overpayment_id = models.CharField(max_length=500)
    currency_rate = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    remaining_credit = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    allocations = models.ForeignKey(Allocation, on_delete=models.CASCADE)
    applied_amount = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    has_attachments = models.BooleanField()
    attachments = models.ForeignKey(Attachment, on_delete=models.CASCADE)

class Allocation(models.Model):
    invoice = models.ForeignKey(InvoiceTypes, on_delete=models.CASCADE)
    overpayment = models.ForeignKey(InvoiceTypes, on_delete=models.CASCADE)
    prepayment = models.ForeignKey(InvoiceTypes, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    status_attribute_string = models.CharField(max_length=500)
    validation_errors = models.ForeignKey(ValidationError, on_delete=models.CASCADE)


class ValidationError(models.Model):
    message = models.CharField(max_length=500)


class Invoices(models.Model):
    Itype = models.ForeignKey(InvoiceTypes, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    line_items = models.ForeignKey(LineItem, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True,null=True)
    due_date = models.DateTimeField(auto_now_add=True,null=True)
    invoice_number = models.CharField(max_length=500)
    reference = models.CharField(max_length=500)
    branding_theme_id = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    currency_rate =  models.DecimalField(decimal_places=3,max_digits=10,null=True)
    status = models.CharField(max_length=500)
    sent_to_contact = models.BooleanField()
    expected_payment_date = models.DateTimeField(auto_now_add=True,null=True)
    planned_payment_date = models.DateTimeField(auto_now_add=True,null=True)
    cis_deduction = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    sub_total = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    total_tax = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    total = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    total_discount = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    invoice_id = models.CharField(max_length=500)
    has_attachments = models.BooleanField()
    is_discounted = models.BooleanField()
    payments = models.ForeignKey(Payment, on_delete=models.CASCADE)
    prepayments = models.ForeignKey(Prepayment, on_delete=models.CASCADE)
    overpayments = models.ForeignKey(Overpayment, on_delete=models.CASCADE)
    amount_due = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    amount_paid = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    fully_paid_on_date = models.DateTimeField(auto_now_add=True,null=True)
    amount_credited = models.DecimalField(decimal_places=3,max_digits=10,null=True)
    updated_date_utc = models.DateTimeField(auto_now_add=True,null=True)
    attachments = models.ForeignKey(Attachment, on_delete=models.CASCADE)
    has_errors = models.BooleanField()
    status_attribute_string = models.CharField(max_length=500)
    validation_errors = models.ForeignKey(ValidationError, on_delete=models.CASCADE)
    warnings = models.ForeignKey(ValidationError, on_delete=models.CASCADE)



