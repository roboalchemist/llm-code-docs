# Source: https://docs.klarna.com/platform-solutions/acquiring-partners/stripe/payments/data-handling.md

# Source: https://docs.klarna.com/platform-solutions/acquiring-partners/adyen/payments/data-handling.md

# Data handling with Adyen

## Address & phone validation

Make sure to validate all addresses and phone numbers before sharing them with Adyen. Rejections due to mismatched or incorrect addresses late in the process can have a negative impact on acceptance rates, so ensuring these are correct early on is critical.

## Tax handling with discounts

You need to declare the tax amounts and VAT for your Klarna orders. It’s crucial to declare discounts and taxes correctly. Make sure to follow the [invoice lines and discounts guidance in Adyen Docs](https://docs.adyen.com/payment-methods/klarna/invoice-lines) to avoid integration issues.

## Extra merchant data (EMD)

[Extra merchant data](https://docs.klarna.com/api/payments/#operation/createCreditSession!path=attachment&t=request) is a set of additional information typically unavailable during the checkout flow. This information may consist of data about the customer performing the transaction, the products or services associated with the transaction, or the seller and their affiliates. Depending on the business category or the type of goods you sell, sending EMD data may be a mandatory requirement.  Here are some examples of business categories where sending EMD is mandatory:

- Travel (flight, train, bus, car rental, hotel)
- Marketplaces
- Tickets and events 
- Subscriptions
- Vouchers and gift cards

## Product and image URLs

You can share the [`imageUrl`](https://docs.klarna.com/api/payments/#operation/createOrder!path=order_lines/image_url&t=request) and the [`productUrl`](https://docs.klarna.com/api/payments/#operation/createOrder!path=order_lines/product_url&t=request) with Adyen. This lets Klarna use these resources in your communication with the customer to improve the post-purchase experience in the Klarna app. This helps the end customer to visualize the purchase they have made.