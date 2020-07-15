# Extract-Data-From-Xero-API

Official python SDK for Xero API generated by OpenAPI spec for oAuth 2

<h3>Features</h3>
XERO API Client with oauth2 token integration.</br>
Automatic OAuth 2 token refresh before token expiration.</br>
Class based interface for Xero API endpoints.</br>
Model classes used to represent API data.</br>
Currently Supported API sets:</br>
Accounting API</br>
Assets API</br>
Projects API</br>
AU Payroll API</br>
Error handling for ease of use.</br>

<h3>Starter Project</h3>
oauth 2 flow to obtain a token</br>
token refresh</br>
identity to obtain tenant_id</br>
organisation endpoint</br>
create contact</br>
create multiple contacts</br>
get invoices using where clause</br>

<h3>Extract Invoices</h3>

<h4>Invoice</h4>

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | See Invoice Types | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**line_items** | [**list[LineItem]**](LineItem.md) | See LineItems | [optional] 
**date** | **date** | Date invoice was issued – YYYY-MM-DD. If the Date element is not specified it will default to the current date based on the timezone setting of the organisation | [optional] 
**due_date** | **date** | Date invoice is due – YYYY-MM-DD | [optional] 
**line_amount_types** | [**LineAmountTypes**](LineAmountTypes.md) |  | [optional] 
**invoice_number** | **str** | ACCREC – Unique alpha numeric code identifying invoice (when missing will auto-generate from your Organisation Invoice Settings) (max length &#x3D; 255) | [optional] 
**reference** | **str** | ACCREC only – additional reference number (max length &#x3D; 255) | [optional] 
**branding_theme_id** | **str** | See BrandingThemes | [optional] 
**url** | **str** | URL link to a source document – shown as “Go to [appName]” in the Xero app | [optional] 
**currency_code** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**currency_rate** | **float** | The currency rate for a multicurrency invoice. If no rate is specified, the XE.com day rate is used. (max length &#x3D; [18].[6]) | [optional] 
**status** | **str** | See Invoice Status Codes | [optional] 
**sent_to_contact** | **bool** | Boolean to set whether the invoice in the Xero app should be marked as “sent”. This can be set only on invoices that have been approved | [optional] 
**expected_payment_date** | **date** | Shown on sales invoices (Accounts Receivable) when this has been set | [optional] 
**planned_payment_date** | **date** | Shown on bills (Accounts Payable) when this has been set | [optional] 
**cis_deduction** | **float** | CIS deduction for UK contractors | [optional] 
**sub_total** | **float** | Total of invoice excluding taxes | [optional] 
**total_tax** | **float** | Total tax on invoice | [optional] 
**total** | **float** | Total of Invoice tax inclusive (i.e. SubTotal + TotalTax). This will be ignored if it doesn’t equal the sum of the LineAmounts | [optional] 
**total_discount** | **float** | Total of discounts applied on the invoice line items | [optional] 
**invoice_id** | **str** | Xero generated unique identifier for invoice | [optional] 
**has_attachments** | **bool** | boolean to indicate if an invoice has an attachment | [optional] [default to False]
**is_discounted** | **bool** | boolean to indicate if an invoice has a discount | [optional] 
**payments** | [**list[Payment]**](Payment.md) | See Payments | [optional] 
**prepayments** | [**list[Prepayment]**](Prepayment.md) | See Prepayments | [optional] 
**overpayments** | [**list[Overpayment]**](Overpayment.md) | See Overpayments | [optional] 
**amount_due** | **float** | Amount remaining to be paid on invoice | [optional] 
**amount_paid** | **float** | Sum of payments received for invoice | [optional] 
**fully_paid_on_date** | **date** | The date the invoice was fully paid. Only returned on fully paid invoices | [optional] 
**amount_credited** | **float** | Sum of all credit notes, over-payments and pre-payments applied to invoice | [optional] 
**updated_date_utc** | **datetime** | Last modified date UTC format | [optional] 
**credit_notes** | [**list[CreditNote]**](CreditNote.md) | Details of credit notes that have been applied to an invoice | [optional] 
**attachments** | [**list[Attachment]**](Attachment.md) | Displays array of attachments from the API | [optional] 
**has_errors** | **bool** | A boolean to indicate if a invoice has an validation errors | [optional] [default to False]
**status_attribute_string** | **str** | A string to indicate if a invoice status | [optional] 
**validation_errors** | [**list[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 
**warnings** | [**list[ValidationError]**](ValidationError.md) | Displays array of warning messages from the API | [optional] 


<h4>Extract Contacts</h4>

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **str** | Xero identifier | [optional] 
**contact_number** | **str** | This can be updated via the API only i.e. This field is read only on the Xero contact screen, used to identify contacts in external systems (max length &#x3D; 50). If the Contact Number is used, this is displayed as Contact Code in the Contacts UI in Xero. | [optional] 
**account_number** | **str** | A user defined account number. This can be updated via the API and the Xero UI (max length &#x3D; 50) | [optional] 
**contact_status** | **str** | Current status of a contact – see contact status types | [optional] 
**name** | **str** | Full name of contact/organisation (max length &#x3D; 255) | [optional] 
**first_name** | **str** | First name of contact person (max length &#x3D; 255) | [optional] 
**last_name** | **str** | Last name of contact person (max length &#x3D; 255) | [optional] 
**email_address** | **str** | Email address of contact person (umlauts not supported) (max length  &#x3D; 255) | [optional] 
**skype_user_name** | **str** | Skype user name of contact | [optional] 
**contact_persons** | [**list[ContactPerson]**](ContactPerson.md) | See contact persons | [optional] 
**bank_account_details** | **str** | Bank account number of contact | [optional] 
**tax_number** | **str** | Tax number of contact – this is also known as the ABN (Australia), GST Number (New Zealand), VAT Number (UK) or Tax ID Number (US and global) in the Xero UI depending on which regionalized version of Xero you are using (max length &#x3D; 50) | [optional] 
**accounts_receivable_tax_type** | **str** | The tax type from TaxRates | [optional] 
**accounts_payable_tax_type** | **str** | The tax type from TaxRates | [optional] 
**addresses** | [**list[Address]**](Address.md) | Store certain address types for a contact – see address types | [optional] 
**phones** | [**list[Phone]**](Phone.md) | Store certain phone types for a contact – see phone types | [optional] 
**is_supplier** | **bool** | true or false – Boolean that describes if a contact that has any AP  invoices entered against them. Cannot be set via PUT or POST – it is automatically set when an accounts payable invoice is generated against this contact. | [optional] 
**is_customer** | **bool** | true or false – Boolean that describes if a contact has any AR invoices entered against them. Cannot be set via PUT or POST – it is automatically set when an accounts receivable invoice is generated against this contact. | [optional] 
**default_currency** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**xero_network_key** | **str** | Store XeroNetworkKey for contacts. | [optional] 
**sales_default_account_code** | **str** | The default sales account code for contacts | [optional] 
**purchases_default_account_code** | **str** | The default purchases account code for contacts | [optional] 
**sales_tracking_categories** | [**list[SalesTrackingCategory]**](SalesTrackingCategory.md) | The default sales tracking categories for contacts | [optional] 
**purchases_tracking_categories** | [**list[SalesTrackingCategory]**](SalesTrackingCategory.md) | The default purchases tracking categories for contacts | [optional] 
**tracking_category_name** | **str** | The name of the Tracking Category assigned to the contact under SalesTrackingCategories and PurchasesTrackingCategories | [optional] 
**tracking_category_option** | **str** | The name of the Tracking Option assigned to the contact under SalesTrackingCategories and PurchasesTrackingCategories | [optional] 
**payment_terms** | [**PaymentTerm**](PaymentTerm.md) |  | [optional] 
**updated_date_utc** | **datetime** | UTC timestamp of last update to contact | [optional] 
**contact_groups** | [**list[ContactGroup]**](ContactGroup.md) | Displays which contact groups a contact is included in | [optional] 
**website** | **str** | Website address for contact (read only) | [optional] 
**branding_theme** | [**BrandingTheme**](BrandingTheme.md) |  | [optional] 
**batch_payments** | [**BatchPaymentDetails**](BatchPaymentDetails.md) |  | [optional] 
**discount** | **float** | The default discount rate for the contact (read only) | [optional] 
**balances** | [**Balances**](Balances.md) |  | [optional] 
**attachments** | [**list[Attachment]**](Attachment.md) | Displays array of attachments from the API | [optional] 
**has_attachments** | **bool** | A boolean to indicate if a contact has an attachment | [optional] [default to False]
**validation_errors** | [**list[ValidationError]**](ValidationError.md) | Displays validation errors returned from the API | [optional] 
**has_validation_errors** | **bool** | A boolean to indicate if a contact has an validation errors | [optional] [default to False]
**status_attribute_string** | **str** | Status of object | [optional] 
