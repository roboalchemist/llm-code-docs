# Source: https://docs.klarna.com/payments/in-store-payments/additional-resources/best-practices-for-partners.md

# Best practices for partners

## Follow our best practices to get the most out of your In-store integration.

## Add UI elements for each distribution status

Here are some examples of the UI elements you can implement for each distribution status.

### Status: DISTRIBUTED

Display the QR code so the customer can scan it. Make sure to set the display's brightness to maximum.


![Best_practices_QR_code.png](Best_practices_QR_code.png)
*Best_practices_QR_code.png*

### Status: ACCESSED

To notify the store personnel that the customer accessed a payment session, display a "Payment in progress" message.


![Best_practices_Loading.png](Best_practices_Loading.png)
*Best_practices_Loading.png*

### Status: COMPLETED

Once the customer completes a payment, display a "Payment is done" message.


![Best_practices_Succes.png](Best_practices_Succes.png)
*Best_practices_Succes.png*

### Status: CANCELLED

If the customer cancels a payment, display a "Payment is canceled" message.


![Best_practices_Cancelled.png](Best_practices_Cancelled.png)
*Best_practices_Cancelled.png*

### Status: FAILED

If a payment fails, display a “Something went wrong” message. We recommend that you also show the related session_id as this will help Klarna's support to easily identify what went wrong.


![Best_practices_error.png](Best_practices_error.png)
*Best_practices_error.png*

## All statuses

- To allow the customer to cancel the payment at any time, add a cancelation button to the UI.


![Best_practices_cancel_button.png](Best_practices_cancel_button.png)
*Best_practices_cancel_button.png*

- Display an additional dialog to make sure that the customer doesn't cancel the payment by accident.


![Best_practices_Cancel.png](Best_practices_Cancel.png)
*Best_practices_Cancel.png*

## Set a payment session timeout

Completing a transaction may take longer for new customers. For that reason, we recommend that you set a timeout on a payment session that allows the customers to log into Klarna using two-factor authentication after they scan the QR code. If you set a timeout, actively cancel a session after timeout so that the payment session doesn’t stay open for the full 46 hours.