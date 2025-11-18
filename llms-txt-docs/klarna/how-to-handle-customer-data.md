# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/how-to-handle-customer-data.md

# How to handle customer data

## This article provides guidance on handling customer data in the Shopify Checkout. It explains which are the required fields to prevent errors with Klarna payments.

## Email should be set as required in Shopify Checkout

Klarna payments requires the customer’s name, phone, and email address to place most Klarna orders. If the customer's email address isn't shared with Klarna upon redirection from Shopify to the Klarna payment page, the customer will receive an error message from Klarna and will need to return to the Shopify checkout to enter their email. To avoid this error, we recommend that you choose **Email** for the **Customer contact method**, which you can configure in the store's **Shopify admin**\> **Settings**\> **Checkout and accounts**\> **Customer contact method**[Customer contact method](https://help.shopify.com/manual/orders/notifications/sms-notifications) section. [Read more about contact options in Shopify documentation](https://help.shopify.com/en/manual/orders/notifications). You can set up a field for the customer to enter their phone number as a required field so that the customer’s phone number is also captured when you enable this setting.


![ Choose Email for the Customer contact method.](2c692c35-5e5f-4483-83ba-b06c2aada253_shopify-customer-contact-method.jpeg)
*ChooseEmailfor the Customer contact method.*

## First and last name should be set as required in Shopify Checkout

Klarna requires both the first and last name of the customer, so verify that this option has been selected for the **Customer information** setting.


![ First and last name are required.](614d190f-bf0d-4eb8-91f9-5286bcc28926_First-and-last-name-required.jpeg)
*First and last name are required.*

## Klarna requests consumers to enter their phone number

With the new Shopify payments app integration, Shopify doesn’t share the [customer's shipping phone number](https://shopify.dev/apps/payments/processing-a-payment#request-body-example) with payment integrations. If a customer isn't logged into their Shopify account, Shopify will share either, but not both, the email or phone number, whichever the customer enters in the first **Contact information field** on the first page of Shopify checkout, as shown in the screenshot below.  If the customer is logged into their Shopify account, Shopify will share both the email and the phone number.  Since a Klarna session can’t be started without an email, we recommend that you configure email as required in checkout. When email is required, the customer’s phone number may not be shared by Shopify, and Klarna will have to request, via a modal, for the customer to enter their phone number.


![ TheContact information field can be configured as Email required or Email or mobile phone number.](d1e99397-614b-4c50-89af-07c083f4dbc3_Shopify-checkout-email-or-phone.jpeg)
*TheContact informationfield can be configured asEmail requiredorEmail or mobile phone number.*

Read more about [customer data in Shopify documentation](https://shopify.dev/docs/apps/payments/implementation/process-a-payment/offsite#customer-hash) **In summary:**

- Klarna payments requires the customer’s name, phone, and email address to place orders.
- To avoid errors during the payment process, ensure that the email, first name, and last name are set as required in the Shopify checkout.
- Make sure the **Customer contact method** is set to **Email** so that the customer doesn’t need to return to Shopify checkout to enter their email manually.