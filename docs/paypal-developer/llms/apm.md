# Alternative payment methods

With alternative payment methods, customers across the globe can pay with their bank accounts, wallets, and other local payment methods. For example, a customer in the Netherlands might want to pay using iDEAL, which is used by more than half of consumers in the Netherlands for online purchases, whereas a customer in Belgium on the same website might want to pay using Bancontact, a popular payment method there.

Integrate alternative payment methods so you can:

- Present the alternative payment methods that you want to offer.
- Customize the experience for collecting buyer information.
- Get your buyers, paying through an alternative payment method, checked out in as few steps as possible.

## Available payment methods

| Payment method | Payment type | Payment flow | Countries | Currencies | Minimum amount | Refunds |
| --- | --- | --- | --- | --- | --- | --- |
| [Apple Pay](https://developer.paypal.com/docs/checkout/apm/apple-pay/) | push | direct | [Country list](https://developer.paypal.com/docs/checkout/apm/apple-pay/#link-supportedcountriesandcurrencies) | [Currency list](https://developer.paypal.com/docs/checkout/apm/apple-pay/#link-supportedcountriesandcurrencies) | 1 USD | Up to 180 days |
| [Bancontact](https://developer.paypal.com/docs/checkout/apm/bancontact/) | bank redirect | redirect | Belgium | EUR | 1 EUR | Within 180 days |
| [BLIK](https://developer.paypal.com/docs/checkout/apm/blik/) | bank redirect | redirect | Poland | PLN | 1 PLN | Within 180 days |
| [eps](https://developer.paypal.com/docs/checkout/apm/eps/) | bank redirect | redirect | Austria | EUR | 1 EUR | Within 180 days |
| [Google Pay](https://developer.paypal.com/docs/checkout/apm/google-pay/) | push | direct | [Country list](https://developer.paypal.com/docs/checkout/apm/google-pay/#link-supportedcountriesandcurrencies) | [Currency list](https://developer.paypal.com/docs/checkout/apm/google-pay/#link-supportedcountriesandcurrencies) | 1 USD | Up to 180 days |
| [iDEAL](https://developer.paypal.com/docs/checkout/apm/ideal/) | bank redirect | redirect | Netherlands | EUR | 0.01 EUR | Within 180 days |
| [Multibanco](https://developer.paypal.com/docs/checkout/apm/multibanco/) | voucher | redirect | Portugal | EUR | N/A | N/A |
| [MyBank](https://developer.paypal.com/docs/checkout/apm/mybank/) | bank redirect | redirect | Italy | EUR | N/A | Within 180 days |
| [Pay upon Invoice](https://developer.paypal.com/docs/checkout/apm/pay-upon-invoice/) | deferred payment | direct | Germany | EUR | 5 EUR | Within 180 days |
| [Przelewy24](https://developer.paypal.com/docs/checkout/apm/przelewy24/) | bank redirect | redirect | Poland | PLN EUR | 1 PLN | Within 180 days |
| [Trustly](https://developer.paypal.com/docs/checkout/apm/trustly/) | bank redirect | redirect | AT, DE, DK, EE, ES, FI, GB, LT, LV, NL, NO, SE | EUR, DKK, SEK, GBP, NOK | 0.01 EUR | Up to 365 days |

**warning**

giropay was sunset on June 30, 2024. PayPal will not support giropay payments starting July 1, 2024. Offer your users PayPal wallet and other alternative payment methods. [Learn more](https://www.paypal.com/us/cshelp/article/giropay-deprecation-help1183)

Sofort was sunset on April 18, 2024. PayPal will not support Sofort payments starting April 19, 2024. Offer your users PayPal wallet and other alternative payment methods. [Learn more](https://www.paypal.com/us/cshelp/article/sofort-deprecation-help1145)