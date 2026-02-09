# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/known-constraints.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/known-constraints.md

# Known constraints for Klarna Payments in Shopify

## Read about some limitations that can affect your Klarna with Shopify integration.

## 1. Klarna Payments accepts orders only for customer billing addresses in the markets that match the store base currency

- Currently, Klarna Payments accepts orders only for customers with billing addresses in the markets that match the currency of the order. See the [list of supported markets and currencies in Klarna payments documentation](https://docs.klarna.com/payments/web-payments/before-you-start/data-requirements/puchase-countries-currencies-locales.md).
- Customers in non-supported markets based on the order's currency are shown an error message on Klarna payment page load that the Klarna order can’t be placed or an error in Shopify checkout ("Your payment can’t be processed for technical reasons. Try again or use a different payment method."), depending upon the Klarna account configuration and Shopify store settings, for example, when theKlarna account doesn't support the store's single base currency.
- Shopify limits Klarna payments as an alternative payment method, the same for all alternative payments methods, to always transact only in the store’s single base currency, [as documented in this Shopify help article](https://help.shopify.com/en/manual/payments/shopify-payments/multi-currency/conversions#shopify-payments-and-other-payment-providers). Even if the store displays prices in multiple currencies, including in checkout or using Shopify Markets, Shopify will update the order's currency to the store's single base currency when redirecting to the alternative payment provider. 
- If you need to support multiple currencies with Klarna, you can use multiple Shopify stores or an alternative checkout, for example, [Global-e](https://www.global-e.com/).
- For example, if the store base currency is SEK, Klarna payments will be able to accept orders for customers whose billing country is Sweden. Customers with addresses in other countries will see an error message, for example one shown in the screenshot below. The exact error message may differ depending on region and Klarna product (for example: "We can't offer you this payment method right now" or “Option not available”.) For stores with base currency of EUR, Klarna can accept orders for multiple regions which transact in EUR. For other countries, a single region is supported for each currency.


![ The exact error message may differ based on region and other data.](9679d839-68a5-4d25-8835-6edcca9536b8_shopify.jpeg)
*The exact error message may differ based on region and other data.*

## 2. Klarna requests customers to enter their phone number

Even if customers previously entered their phone number in Shopify checkout, Shopify may not share that phone number with payments integrations when email is required in checkout. Thus [Klarna may ask the customer to enter their phone number again](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/how-to-handle-customer-data.md).

## 3. Renaming the payment method isn’t supported

While some [Shopify custom script code](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/shopify-plus-custom-scripts) works for payment methods integrated via Shopify's new payments app integrations, [renaming the payment method isn’t currently supported by Shopify](https://community.shopify.com/c/payments-shipping-and/can-you-add-or-change-the-name-of-payment-options/m-p/2040190), as payment providers can configure translations for the payment method name. With the new Klarna payment integration for Shopify, translations aren’t needed since the name "Klarna" works in any language. You can find the list of translated payment method names in [this article](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/language-locale-and-translations.md).

## 4. Klarna logo is not supported to be automatically included in theme footer

Currently, the payment method footer injection isn’t supported by Shopify's new payments platform. As a workaround, instead of using liquid code `shop.enabled_payment_types`[shop.enabled_payment_types](https://shopify.dev/api/liquid/objects/shop#shop-enabled_payment_types), you may update your store's footer theme code directly, for example, by adding the code below, but you'll need to test what works for your store's specific theme. You can also refer to [another solution posted in the Shopify community](https://community.shopify.com/c/shopify-design/klarna-logo-doesn-t-show-in-footer/m-p/1589308).

``` ruby
{% assign enabled_payment_types = 'paymenttype1,paymenttype2,klarna' | remove: ' ' | split: ',' %}
```

Use this code to update your store's footer theme.

## 5. The amount paid by the customer to Klarna doesn't match the Shopify order total

If customers update a related, but different Shopify session separately from the Shopify session used to place the Klarna order, the order totals between the Shopify and Klarna orders may not match, but the **Paid by customer** amount for the Shopify order should always match the Klarna order total. While not ideal, this is working as expected and designed. Make sure to only fulfill order line items paid for by the customer.


![ The Shopify amount should always match the Klarna order total.](14a33393-3606-4c96-be11-59b944533084_Screenshot.jpeg)
*The Shopify amount should always match the Klarna order total.*

## Feedback and support

If you need additional support, please reach out to [your region's Merchant Support team](http://klarna.com/merchant-support). [The Shopify community](https://community.shopify.com/) is a good place for Shopify questions, support, and feedback, in addition to [the Shopify help center](https://help.shopify.com/).