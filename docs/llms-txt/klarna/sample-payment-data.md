# Source: https://docs.klarna.com/resources/developer-tools/sample-data/sample-payment-data.md

# Sample payment data

## Test your integration of Klarna Payment methods in playground environment using sample payment data to ensure compliance and a reliable integration.

## Payment methods

The following payment methods are available for testing Klarna Payments.

### Direct debit

To test the direct debit payment flow from a customer's perspective, use an IBAN-format number. For example, the following sample IBAN number will work for a test store in Germany: *DE1152 0513 7351 2071 0131*.  <em>Sweden</em> In Sweden, use the following sample Personal number: *19770111-6050.*

### Credit card

To test the card payment flow from a customer's perspective, use the following card details in the loaded Klarna widget:

- **Credit card number:***4111 1111 1111 1111*
- **CVC:** *123*
- **Expiration date:** *12/28* or any other future date in MM/YY format
- Card number to trigger a [3-D Secure](https://en.wikipedia.org/wiki/3-D_Secure) flow: *4687388888888881*


![ Card payment UI flow|332x332px](f3b83884-e264-4e26-b223-d8d458ad4375_PN_card.gif)
*Card payment UI flow|332x332px*

### Debit card

To test the card payment flow from a customer's perspective, use the following card details in the loaded Klarna widget:

- **Credit card number:***4012 8888 8888 1881*
- **CVC:** *123*
- **Expiration date:** *12/28* or any other future date in MM/YY format

<em>United States of America</em> In the US, use the debit card to test Financing. In addition, when prompted for a Social Security Number (SSN), use *123456789*

### Direct bank transfer

To test a direct bank transfer payment flow from a customer's perspective, look for *Demo Bank* in the loaded Klarna widget.


![ Bank transfer payment UI flow|389x389px](8a1c8a6c-2f1b-4d00-a2a7-1b648f048c0d_dbt_bank_search.gif)
*Bank transfer payment UI flow|389x389px*