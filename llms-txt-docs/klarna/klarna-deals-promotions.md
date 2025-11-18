# Source: https://docs.klarna.com/payments/web-payments/additional-resources/use-cases/klarna-deals-promotions.md

# Klarna deals promotions

## Incentivize Klarna shoppers and boost conversion with an auto-applied deal on your site that is seamless to use.

## What is a Klarna deal?

A **Klarna deal** is a discount that is automatically applied at the checkout when paying with Klarna at your store. This solution can be offered both in your site and/or across Klarna ecosystem. This capability allows you to strategically influence customer decisions at the point of purchase, boosting conversion as well as driving returning shoppers transactions. Klarna deals can be leveraged both on one time purchases as well as for subscriptions and on-demand payments.

### Prerequisites

In order to enable Klarna deals in your website you need to:

- Due to local legal regulations, to enable Klarna deals in UK, you must offer Pay Now as a payment method. 
- [On-site messaging standard implementation](https://docs.klarna.com/conversion-boosters/on-site-messaging/integrate-on-site-messaging.md) in product and cart pages on your site to allow enablement of Klarna deal messaging. *If On-site messaging is not enabled on your site, you need to promote Klarna deal either on site banner and/or the product page.*
- If you wish to gate the Klarna deal only to **new customers to your brand**, Extra Merchant Data will be required to allow identification of new customer. Learn more in the [next sections](https://docs.klarna.com/payments/web-payments/additional-resources/use-cases/klarna-deals-promotions.md)
- If you wish to offer a**discount only based on what the customer is buying**, `order_lines` implementation will be required in order to allow assortment inclusion or exclusion feature of Klarna deals. Learn more in the [next sections](https://docs.klarna.com/payments/web-payments/additional-resources/use-cases/klarna-deals-promotions.md)

## Shopper experience

Klarna deals enables an fully embedded user experience by leveraging existing On-site messaging placements as well Klarna payment widget presentation at the checkout to communicate active deals when paying with Klarna.


![ Enable a seamless user experience across the entire shopping journey](Zo0HSx5LeNNTw7mx_KlarnaDealsflow.jpeg)
*Enable a seamless user experience across the entire shopping journey*

## Campaign configuration

If you are already accepting Klarna as payment method in your store and you have On-site messaging enabled, Klarna deals is available out of the box and can be easily enabled by your Klarna representative with not additional technical effort on your side. When configuring a Klarna deal campaign, you will be able to define the following parameters according to your campaign needs: **Discount type:** 

- proportional (e.g. 25% off)
- fixed (e.g. \$25 off)

**Time frame**:

- start date for campaign
- end date for campaign

**Capping and minimun:**

- Minimum order amount to unlock deal (orders above \$100)
- Max discount amount that is granted (e.g. \$20)

**Budget Control:**

- Maximum budget for the campaign.
- Budget capping to stop the campaign when reached

**Audience segmentation**:

- Opened to all customers checking out with Klarna.
- New to Klarna only
- New to Merchant only

**Assortment exclusion or inclusion to consider:**

- Product brand
- Product category
- Product name
- Product ID or reference

## Audience segmentation

When setting-up a Klarna deal that will be offered on your website there are three possible segmentations possible to determine who will get the discount.

- **All users**: where everyone paying with Klarna on the merchant site will get access to the deal.
- **New to Klarna:** where only users paying with Klarna for the first time or who didn't make a purchase in the past 12 months will get access to the deal.
- **New to merchant:**where only users who never paid with the merchant before will get access to the deal. This is a key feature when you are looking to acquire new customers by offering discounts only to users who never shopped at your store before directly at the point of checkout, regardless if they have paid with Klarna before or not.

There are no additional technical requirements to enable **All users**and**New to Klarna**segmentation. To enable **New to merchant**segmentation it is required that you send **“Extra Merchant Data”** (EMD) as part of their integration with Klarna, as early as possible in the checkout flow (i.e. on create_session).

### Extra Merchant Data for Klarna deals

**Extra Merchant Data** (EMD) are additional data points that you can share with Klarna and that is not typically available during the checkout flow. This information may consist of data about the consumer performing the transaction, the product/services associated with the transaction or about the seller and their affiliates. Understand more about EMD and how to send it in [our guidelines](https://docs.klarna.com/payments/web-payments/additional-resources/use-cases/extra-merchant-data.md) For Klarna deals you will be require to send at least one of the following 2 “packages”:

- `payment_history_simple`: this package’s properties tell us if the user paid before or not in your store.
- `payment_history_full`: this package’s properties tell us the number of purchases the user made at your store.

## Assortment exclusion or inclusion

The assortment exclusion or inclusion feature allows you to selectively exclude or include certain products or categories from the discount offerings. This feature provides greater control and flexibility over the deals and promotions displayed to customers. For this feature to be enable, `order_lines` should be [shared during the session creation.](https://docs.klarna.com/api/payments/#operation/createCreditSession!path=order_lines&t=request)

### Order lines for Klarna deals

The following fields are the ones that can be leveraged for building the assortment logic

- `name`**name**: in some cases brand names are also present as part of the product name, in that case, `name` could also be used to do brand exclusion.
- `reference`**reference** and `product_url`**product_url**: reference can be SKU (e.g 7365638)
- `brand`**brand** for exclusion or inclusion of the products based on their brand.
- `category_path`**category_path** for exclusion or inclusion based on specific category.

Assortment exclusion or inclusion feature is highly dependent of the `order_lines` quality, for example if `category_path` data point is not received, a Klarna deal can’t be configured for a category exclusion.