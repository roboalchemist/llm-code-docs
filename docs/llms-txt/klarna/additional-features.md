# Source: https://docs.klarna.com/payments/web-payments/additional-resources/use-cases/additional-features.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/payments-for-shopify/additional-features.md

# Source: https://docs.klarna.com/payments/web-payments/additional-resources/use-cases/additional-features.md

# Additional features

## Depending on the market and the details of your Klarna deal, you may be able to add some extra features to your store.

<em>United Kingdom,United States of America</em>

## Dynamic promotional offers

Klarna lets you dynamically trigger promotional credit offers. Your Klarna account manager can help you determine the criteria for custom offers and a standard naming convention that will be referred to when requesting such offers via our API. When initiating a payment session in which you want to offer custom financing, you have to include one or multiple promotional codes in the `custom_payment_method_id` array in the create session request. <em>Finland,Norway,Sweden</em>

## Using SmartPost with Klarna

If you're using SmartPost as a shipping option, you must share the following details with Klarna when creating an order:

- The SmartPost address in the `billing_address`\[ billing_address object when creating an order\].
- The phone number to which the SmartPost SMS PIN is sent. We use this phone number for risk assessment.