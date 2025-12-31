# Source: https://docs.klarna.com/platform-solutions/acquiring-partners/stripe/payments/data-handling.md

# Source: https://docs.klarna.com/platform-solutions/acquiring-partners/adyen/payments/data-handling.md

# Source: https://docs.klarna.com/platform-solutions/acquiring-partners/stripe/payments/data-handling.md

# Source: https://docs.klarna.com/platform-solutions/acquiring-partners/adyen/payments/data-handling.md

# Source: https://docs.klarna.com/platform-solutions/acquiring-partners/stripe/payments/data-handling.md

# Source: https://docs.klarna.com/platform-solutions/acquiring-partners/adyen/payments/data-handling.md

# Source: https://docs.klarna.com/platform-solutions/acquiring-partners/stripe/payments/data-handling.md

# Source: https://docs.klarna.com/platform-solutions/acquiring-partners/adyen/payments/data-handling.md

# Source: https://docs.klarna.com/platform-solutions/acquiring-partners/stripe/payments/data-handling.md

# Source: https://docs.klarna.com/platform-solutions/acquiring-partners/adyen/payments/data-handling.md

# Source: https://docs.klarna.com/platform-solutions/acquiring-partners/stripe/payments/data-handling.md

# Data handling with Stripe

## Data handling

### Address and phone validations

Make sure to validate all addresses and phone numbers before sharing them with Stripe. Rejections due to mismatched or incorrect addresses late in the process can negatively affect acceptance rates, so ensuring these are correct early on is critical.

### Billing country and address

Billing country and billing email are always required for Klarna transactions. Make sure to provide the correct information for all payment sessions to avoid the transactions being rejected.

## On-site messaging

Use Klarna On-site messaging to raise awareness of Klarna's flexible payment options and other benefits throughout the shopping journey. With only a few lines of code, you’ll have our dynamic messaging up and running in no time. And the result? An uplift in average order value, improved conversion, and expanded customer base. Klarna On-site messaging isn’t currently enabled by Stripe, but you can add it to your store by following the [Klarna integration guide](https://docs.klarna.com/on-site-messaging). Contact Stripe support for more information and access. Relevant information and access can be obtained by reaching out to Stripe Support.

## Express button

Simplify the checkout experience and give your customers a fast and convenient way to shop with Klarna, even if it’s their first time visiting your website. Adding our Express button is an effortless way to increase conversion.  Express button isn’t currently enabled by Stripe, but you can add it to your store by following the [Klarna integration guide](https://docs.klarna.com/express-button.md). Contact Stripe support for more information and access. Relevant information and access can be obtained by reaching out to Stripe Support, which will also trigger whitelisting of your production URL.  When integrating the Express Button, make sure not to collect the customer’s billing address again, as Klarna will provide the details back to you in a callback.

## Branding

If you want to update your store's branding information within Klarna-owned assets, please contact Stripe support. Ensure you include the branding assets presented in the [brand configuration guide](https://docs.klarna.com/platform-solutions/acquiring-partners/stripe/payments/data-handling.md).  To ensure you’re seeing the full benefit of Klarna in your store, we highly recommend including upstream elements to educate the customer about Klarna’s availability. [See the available marketing guidelines and campaign assets](https://docs.klarna.com/marketing).