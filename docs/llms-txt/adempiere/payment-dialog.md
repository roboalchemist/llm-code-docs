# Source: https://adempiere.gitbook.io/docs/introduction/getting-started/dialogs-and-forms/payment-dialog.md

# Payment Dialog

The **Payment Dialog** provides a convenient way to complete a payment from a **Sales Order** or **Invoice**. It is accessed by clicking on the button for the Payment Rule which can have a number of labels but will have a payment icon such as ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r10Bp5uQ99v3g7o%2Fpayment24.gif?generation=1551809345580665\&alt=media) or ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r136t4_uiYMG3pO%2Fwebui_paymenticon.PNG?generation=1551809345516922\&alt=media).

{% hint style="info" %}
A Payment Rule is simply a description of how the order or invoice will be paid, for example, by cash, check or credit card.
{% endhint %}

![Example of the Payment Rule button in the Web App, showing the rule as Cash.](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r15d6umlxgLa93e%2Fwebui_paymentrulebutton.PNG?generation=1551809345565009\&alt=media)

This convenience is useful for sales that don't use a Point of Sale terminal and where payments are collected immediately when the order or invoice is created. It can also be used to pay Vendor Invoices. It saves the steps involved in opening the **Payment** window and filling out the fields.

The button will also appear on Purchase Orders but will be limited to changing the Payment Rule on the Purchase Order.

{% hint style="warning" %}
This is a simple dialog intended for simple cases. It is not recommended it be used to collect payments to settle a customer account, pay multiple invoices or for complex payment terms with payment schedules.
{% endhint %}

### Restrictions

There are some restrictions:

* The Payment Rule button is only accessible on Order or Invoice documents.
* The Business Partner on the Payment will be the same as on the Order or Invoice so you can't use the button to take a payment for any customer.
* The Payment Rule dialog will not open if the document status is Voided or Reversed.
* If the document status is Completed or Waiting Payment and the ***Grand Total*** field has a non-zero value, a Payment can be generated. Otherwise, only the Payment Rule can be changed.
* Only the Payment Rule can be changed on Purchase Order documents.
* The payment amount shown may not be accurate.  The payment amount shown in the dialog only looks at the base document  and does not consider the state of the Business Partners credit status or balance owing.  Payments made that do not reference this order or invoice may not be considered.

## Description

### Setting the Payment Rule

The Payment Dialog appears as a button, as shown above, displaying the payment icon (![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r1AedGXCvq_sdzP%2Fpayment24.gif?generation=1551809345568533\&alt=media)or ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r1CKeCEfaPVE-Ux%2Fwebui_paymenticon.PNG?generation=1551809345847450\&alt=media) )and labeled with the currently selected method of payment.

Clicking the button will open the Payment Dialog. If the source document is not Completed or Waiting Payment and not yet able or ready to accept payment, the Payment Dialog will appear as a combo box listing various payment rules or methods.

![Payment Dialog showing just the Payment Rule](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r1EBLNSJRnTLSvQ%2Fwebui_paymentformpaytermonly.PNG?generation=1551809345618150\&alt=media)

The Payment Methods in the combo box may vary depending on your setup but generally contain the following values:

* Cash
* Credit Card
* Direct Deposit (appears on purchase orders/vendor invoices)
* Check
* On Credit
* Direct Debit (appears on sales orders/customer invoices)

Selecting one of these Payment Methods will set the Payment Rule in the document to that value meaning the text on the Payment Rule button will change.

Below the combo box, there are two buttons:

* ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r1GqlVKfB_oYtkX%2Fwebui_iconcancel.PNG?generation=1551809345572862\&alt=media)  Cancel - this will close the dialog.
* ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r1IdwqG9VUqLYFy%2Fwebui_iconconfirm.PNG?generation=1551809345499527\&alt=media) Confirm - this will save the Payment Rule value.

## Taking a Payment

If the source document status is Completed or Waiting Payment, the Payment Rule button can be used to create and complete a payment. If a single invoice is involved, either as the source document or if related to the source Order, the payment will be allocated against the invoice.

{% hint style="info" %}
The Payment Rule button can be clicked multiple times and will create a new payment each time. This is useful for mixed payments where, say, the customer wants to pay a portion by cash and the balance by credit card.
{% endhint %}

The ***Amount*** field that appears will display the "unpaid" amount. This is calculated as follows:

* For an Order, If no Invoices are associated with the Order, the Amount will be the ***Grand Total*** of the Order less any payments made towards that Order.
* Otherwise, the Amount will be the Invoice Open Amount less any unallocated payments made towards the Order where the Order is the source document for the dialog or referenced directly from the Invoice if the Invoice is the source document.

Some payment methods can be processed online if a suitable payment processor has been configured to manage the online transactions. If a payment processor has not been configured, the online button will not function and a error will be displayed if it is clicked. Without an online process, some manual care is required to ensure that the payment record will match the actual payment.

If the payment process was successful, a dialog will appear with the message "Created Payment: \<Payment Document No>". If there was an error, an error message will be displayed.

{% hint style="warning" %}
In most cases, if there is an error, no payment is created. However, in the case where the online process succeeds but the system payment cannot be completed, the payment will be left as draft so that the user can troubleshoot the problem.
{% endhint %}

### **Cash**

Selecting the Payment Rule *Cash* will display the window shown below.

![Example of a Cash Payment](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r1KX8c8zxn7U5rw%2Fwebui_paymentformcash.PNG?generation=1551809345502988\&alt=media)

The Cash Payment requires

| Field              | Description                                                                                                                                                                                         |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ***Cash Journal*** | The Cash Journal where the resulting payment will be recorded.                                                                                                                                      |
| ***Account Date*** | The date of the accounting consequences.  This will also be used as the date of the transaction.  The date may be different than the date of the source document.  The default is the current date. |
| ***Amount***       | The remaining unpaid amount for this document.  Note the restrictions and warnings above.                                                                                                           |

On clicking Confirm (![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r1McOGDMMZXHLTE%2Fwebui_iconconfirm.PNG?generation=1551809345549453\&alt=media)), a cash payment will be created, completed and added to the selected Cash Journal. If possible, the payment will be allocated towards an invoice.

### **Check**

If *Check* is selected in the Payment Rule combo, the Payment Dialog will appear as shown below.

![Payment Dialog for a Check payment](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r1Oth2NwK2AI7PY%2Fwebui_payformcheck.PNG?generation=1551809345684880\&alt=media)

The Check Payment fields require the following

| Field              | Description                                                                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| ***Bank Account*** | The bank account where the check will be deposited.                                                                                   |
| ***Amount***       | The amount of the payment.                                                                                                            |
| ***Routing No***   | The routing number of the source bank from the check. This is generally just used for reference but may be used in online processing. |
| ***Account No***   | The account number from the check.  Again, used for reference.                                                                        |
| ***Check No***     | The check number.  Used for reference.                                                                                                |

{% hint style="info" %}
The system can be configured to overwrite the payment document number with the check information. For a receipt, the resulting document number will look like : "\<Routing No>: \<Account No> \<Check No>. For payments, the outgoing check number will be used.
{% endhint %}

On clicking ![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r1QW5g-_wdu9Whh%2Fwebui_iconconfirm.PNG?generation=1551809346257545\&alt=media) Confirm, the payment information will be saved and allocated to the invoice if possible.

### **Credit Card**

If *Credit Card* is selected in the Payment Rule combo, the Payment Dialog will appear as shown below.

![Example of a Credit Card Payment](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r1UgIU5smc633mC%2Fwebui_payformcreditcard.png?generation=1551809345599898\&alt=media)

Select the appropriate credit card type from the combo box and fill in the other text fields.

The Credit Card fields require the following

| Field                          | Description                                                                                                                                      |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| ***Credit Card***              | Select the credit card type.  These are configured and associated with Bank Accounts.  The list will only include Credit Cards that are accepted |
| ***Name***                     | The card holder name as it appears on the card                                                                                                   |
| ***Number***                   | The card number                                                                                                                                  |
| ***Expires (MMYY)***           | The credit card expiry month and year using the four character MMYY format                                                                       |
| ***Amount***                   | The amount of the payment                                                                                                                        |
| ***Voice Authorization Code*** | When the credit card payment is taken manually and a phone authorization code is received, the code can be entered here for reference.           |

Clicking the "Online" button will attempt to process the credit card information online through the associated payment processor.

### **Direct Debit / Deposit**

If *Direct Debit* or *Direct Deposit* is selected in the Payment Rule combo, the Payment Dialog will appear as shown below. The term debit / deposit will be used with sales orders / purchase orders respectively.

![Example Direct Debit payment.](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r1YHRW_aeWrAEcD%2Fwebui_payformdirectdebit.png?generation=1551809345545619\&alt=media)

The required fields are:

| Fields                     | Description                                                                                                                                   |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| ***Partner Bank Account*** | For Direct debits and deposits, a target bank account is required.  This is defined in the **Business Partner** window, **Bank Account** tab. |
| ***Amount***               | The amount of the payment.                                                                                                                    |

Clicking the Online button will attempt to process the payment online if a suitable payment processor is configured.

Clicking the confirm button will simply create a payment record but will not process the payment online.

### **On Credit**

The On Credit payment will only update the payment terms of the order or invoice. No payment is created.

![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-L_E1p7ertwtNHP6RLn8%2F-L_E1r1aODUQw0JxIhsc%2Fwebui_payformoncredit.png?generation=1551809345782130\&alt=media)
