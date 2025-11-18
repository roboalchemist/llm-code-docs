# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/multi-currency-payments.md

# Multi-currency payments

## This article explains the behavior and limitations of multicurrency payments using Klarna in the Shopify store.

Shopify restricts all alternative payment methods, such as Klarna payments, to only process orders in the store’s base currency, as documented in [this Shopify help center article](https://help.shopify.com/en/manual/payments/shopify-payments/multi-currency/conversions#shopify-payments-and-other-payment-providers). As stated in the documentation, *“Only Shopify Payments can process payments in a customer's local (presentment) currency. If your customer chooses a payment option from a different payment provider, then their payment is made in the currency of your store”*. This limitation is documented in [the Known constraints section of this documentation](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/known-constraints.md). If you’re using Shopify Plus and would like to hide Klarna payments in checkout based on certain cart data, please refer to the [Shopify Plus: custom scripts documentation](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/shopify-plus-custom-scripts). **In summary:**

- Shopify restricts Klarna payments to only process orders in the store’s base currency.