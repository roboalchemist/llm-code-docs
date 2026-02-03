# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/language-locale-and-translations.md

# Language, locale, and translations

## This article explains how language, locale, and translations work for the Klarna payment method in Shopify.

## Payment method name translations in the checkout

Klarna configures the translations for the Klarna payment method. For each supported language, one translation is available. Read more about it [in the Shopify documentation](https://shopify.dev/apps/payments/creating-a-payments-app/creating-a-payments-app#payments-app-extension-configuration-fields).

Note the following rules which govern which translation is displayed in the checkout:

- The displayed translation isn't determined by the customer's country or storefront language.
- The translation used in the store's checkout is determined by the store's single checkout language, which is configured in the store’s Shopify admin under **Settings**\> **Checkout and accounts**\> **Manage checkout language**.

The following table shows translated payment method name in each language:

| **Language** | **Translated payment method name**        |
|--------------|-------------------------------------------|
| Czech        | Klarna - Zaplať ve 3 splátkách            |
| Danish       | Klarna - Betal nu eller senere            |
| Dutch        | Klarna - Betaal nu of betaal later        |
| English      | Klarna - Flexible payments                |
| Finnish      | Klarna - Maksa heti tai myöhemmin         |
| French       | Klarna - Payer maintenant, ou plus tard   |
| German       | Klarna - Sofort oder später bezahlen      |
| Greek        | Klarna - 3 άτοκες δόσεις                  |
| Hungarian    | Klarna - Fizetés most vagy fizetés később |
| Italian      | Klarna - Paga in 3 rate                   |
| Norwegian    | Klarna - Betal nå eller senere            |
| Polish       | Klarna - Kup teraz, zapłać później        |
| Portugese    | Klarna - 3 pagamentos sem juros           |
| Spanish      | Klarna - Paga a plazos sin intereses      |
| Swedish      | Klarna - Betala nu eller senare           |

Currently, payment methods can’t be renamed for Shopify Plus merchants via custom scripts. This is a known constraint and you can [read more about it in this Klarna.Docs article](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/known-constraints/#4-renaming-the-payment-method-isnt-supported).

Prior to July 2022, the payment method name was *Klarna*.

## Language and locale

The locale for Klarna payments hosted payment page is set based on the store's language concatenated with the customer's billing address country. For example, the English language selected for a customer with a US billing address entered in Shopify checkout would result in a request locale of `en-US` when Klarna payments is loaded. If the requested locale is supported by Klarna payments, per [Available purchase countries, currencies and locales,](https://docs.klarna.com/klarna-payments/in-depth-knowledge/puchase-countries-currencies-locales/) the locale will be honored. If the locale isn't supported, English is used as a fallback.

Locale isn't configurable in Klarna. You can configure your store's language in the Shopify admin under **Settings**\> **Languages**.

One way to check a store's Shopify language is via the browser’s developer tools, for example, by entering `Shopify.locale` in your browser's developer tools’ **Console**, as shown on the following snippet.

``` http
Shopify.locale
```

Enter Shopify.locale in the Developer tools' console to check a Shopify store's language.


![ You can check a store's Shopify language in your console.](c69dee66-5042-433d-a39c-bb93d1399bff_Shopifylocale.jpeg)
*You can check a store's Shopify language in your console.*

**In summary:**

- Klarna provides translations for the Klarna payment method.
- For each supported language, one translation is available determined by the store's checkout language configuration. 
- The locale for Klarna Payments' hosted payment page is associated with the store's language and the customer's billing address country. 
- Locale configuration is available in the Shopify admin settings.