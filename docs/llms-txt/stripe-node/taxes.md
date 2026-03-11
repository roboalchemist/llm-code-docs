# Source: https://docs.stripe.com/invoicing/taxes.md

# Source: https://docs.stripe.com/payments/checkout/taxes.md

# Collect taxes

Learn how to collect taxes with Stripe Tax.

# Stripe-hosted page

> This is a Stripe-hosted page for when payment-ui is stripe-hosted. View the full page at https://docs.stripe.com/payments/checkout/taxes?payment-ui=stripe-hosted.

Stripe Tax allows you to calculate the tax on your one-time and recurring payments when you use Checkout. You can enable Stripe Tax to automatically compute taxes on all of your Checkout purchases and subscriptions.

## Create a Checkout Session

You can create Checkout sessions for one-time and recurring purchases.

To calculate tax for new customers, Checkout validates and uses the provided shipping or billing address. For existing customers, Checkout calculates tax by validating and using the attached customer shipping or billing address. If you capture a new billing or shipping address for an existing customer, Checkout won’t automatically override the previous billing or shipping information. You must explicitly request customer address changes.

### Apple Pay and Google Pay

To ensure that Google Pay is offered as a payment method while using Stripe Tax in Checkout, you must either require collecting a shipping address, or provide an existing customer with a saved shipping address. Apple Pay with Stripe Tax displays only when the customer’s browser supports Apple Pay version 12 or greater.

## Calculate tax for new customers

If you don’t pass in an existing customer when creating a Checkout session, Checkout creates a new customer and automatically saves the billing address and shipping information. Checkout uses the shipping address entered during the session to determine the customer’s location for calculating tax. If you don’t collect shipping information, Checkout uses the billing address.

```curl
curl https://api.stripe.com/v1/checkout/sessions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "line_items[0][price]"="{{PRICE_ID}}" \
  -d "line_items[0][quantity]"=2 \
  -d "automatic_tax[enabled]"=true \
  -d mode=payment \
  --data-urlencode success_url="https://example.com/success"
```

## Optional: Update your products and prices

Stripe Tax uses information stored on *products* (Products represent what your business sells—whether that's a good or a service) and *prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) to calculate tax, such as *tax code* (A tax code is the category of your product for tax purposes) and *tax behavior* (Tax behavior determines whether you want to include taxes in the price ("inclusive") or add them on top ("exclusive")). If you don’t explicitly specify these configurations, Stripe Tax will use the default tax code selected in [Tax Settings](https://dashboard.stripe.com/settings/tax).

For more information, see [Specify product tax codes and tax behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md).

## Optional: Calculate tax for existing customers

To calculate tax on an existing customer’s Checkout session, set the `automatic_tax[enabled]` parameter to `true` when you create the session. You can base the tax calculations on the customer’s existing addresses or the new addresses that you collected during checkout:

### Use existing addresses on the customer for taxes

If you’ve already collected your existing customers’ addresses, you can base the tax calculations on those addresses rather than the addresses collected during checkout:

- Which customer address does Checkout use for taxes?

  If available, Checkout uses the customer’s saved [shipping address](https://docs.stripe.com/api/customers/object.md#customer_object-shipping-address) to calculate taxes. Otherwise, Checkout uses the customer’s saved [billing address](https://docs.stripe.com/api/customers/object.md#customer_object-address) to calculate taxes.

- Do the customer addresses have to meet any requirements?

  When using existing addresses for taxes, the customer must either have a valid [shipping address](https://docs.stripe.com/api/customers/object.md#customer_object-shipping-address) or [billing address](https://docs.stripe.com/api/customers/object.md#customer_object-address) saved. You can see whether or not a customer’s saved addresses are valid by checking their [customer.tax.automatic_tax](https://docs.stripe.com/api/customers/object.md#customer_object-tax-automatic_tax) property. If `customer.tax.automatic_tax` value is `supported` or `not_collecting`, the customer’s saved addresses are valid, and you can enable Stripe Tax on Checkout sessions for that customer.

```curl
curl https://api.stripe.com/v1/checkout/sessions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "line_items[0][price]"="{{PRICE_ID}}" \
  -d "line_items[0][quantity]"=2 \
  -d "automatic_tax[enabled]"=true \
  -d customer="{{CUSTOMER_ID}}" \
  -d mode=payment \
  --data-urlencode success_url="https://example.com/success"
```

### Use addresses collected during Checkout for taxes

You can configure Checkout to save a customer’s new billing or shipping addresses. In this case, Checkout calculates the tax by using the address entered during checkout.

- Which address does Checkout use for taxes?

  If you’re [collecting shipping addresses](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-shipping_address_collection), Checkout uses the shipping address entered during the session to calculate taxes. Otherwise, Checkout uses the billing address entered during the session to calculate taxes.

- Where are the addresses collected during Checkout saved?

  If you’re [collecting shipping addresses](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-shipping_address_collection), Checkout saves the shipping address entered during the session to the customer’s [customer.shipping.address](https://docs.stripe.com/api/customers/object.md#customer_object-shipping-address) property. Otherwise, Checkout saves the billing address entered during the session to the customer’s [customer.address](https://docs.stripe.com/api/customers/object.md#customer_object-address) property. In both cases, the address used for taxes will override any existing addresses.

If you’re collecting shipping addresses with Checkout, set the `customer_update[shipping]` property to `auto`. This allows you to copy the shipping information from Checkout to the customer.

```curl
curl https://api.stripe.com/v1/checkout/sessions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "line_items[0][price]"="{{PRICE_ID}}" \
  -d "line_items[0][quantity]"=2 \
  -d "automatic_tax[enabled]"=true \
  -d customer="{{CUSTOMER_ID}}" \
  -d "customer_update[shipping]"=auto \
  -d "shipping_address_collection[allowed_countries][0]"=US \
  -d mode=payment \
  --data-urlencode success_url="https://example.com/success"
```

If you aren’t collecting shipping addresses with Checkout, and you want to use billing addresses entered during checkout for taxes, you must save the billing address to the customer. Set the `customer_update[address]` property to `auto` so that you copy the newly-entered address onto the provided customer.

```curl
curl https://api.stripe.com/v1/checkout/sessions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "line_items[0][price]"="{{PRICE_ID}}" \
  -d "line_items[0][quantity]"=2 \
  -d "automatic_tax[enabled]"=true \
  -d customer="{{CUSTOMER_ID}}" \
  -d "customer_update[shipping]"=auto \
  -d mode=payment \
  --data-urlencode success_url="https://example.com/success"
```

## Optional: Check the response

To see the results of the latest tax calculation, the [total_details.amount_tax](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-total_details) property in the Checkout Session resource shows the calculated tax amount. Additionally, you can use the [Dashboard](https://dashboard.stripe.com/) to view the tax outcome for each payment.


# Embedded form

> This is a Embedded form for when payment-ui is embedded-form. View the full page at https://docs.stripe.com/payments/checkout/taxes?payment-ui=embedded-form.

Stripe Tax allows you to calculate the tax on your one-time and recurring payments when you use Checkout. You can enable Stripe Tax to automatically compute taxes on all of your Checkout purchases and subscriptions.

## Create a Checkout Session

After updating your products and prices, you’re ready to start calculating tax on your Checkout sessions. You can create sessions for one-time and recurring purchases.

To calculate tax for new customers, Checkout validates and uses the provided shipping or billing address. For existing customers, Checkout calculates tax by validating and using the attached customer shipping or billing address. If you capture a new billing or shipping address for an existing customer, Checkout won’t automatically override the previous billing or shipping information. You must explicitly request customer address changes.

### Apple Pay and Google Pay

To ensure that Google Pay is offered as a payment method while using Stripe Tax in Checkout, you must either require collecting a shipping address, or provide an existing customer with a saved shipping address. Apple Pay with Stripe Tax displays only when the customer’s browser supports Apple Pay version 12 or greater.

## Calculate tax for new customers

If you don’t pass in an existing customer when creating a Checkout session, Checkout creates a new customer and automatically saves the billing address and shipping information. Checkout uses the shipping address entered during the session to determine the customer’s location for calculating tax. If you don’t collect shipping information, Checkout uses the billing address.

```curl
curl https://api.stripe.com/v1/checkout/sessions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "line_items[0][price]"="{{PRICE_ID}}" \
  -d "line_items[0][quantity]"=2 \
  -d "automatic_tax[enabled]"=true \
  -d mode=payment \
  -d ui_mode=embedded \
  --data-urlencode return_url="https://example.com/return"
```

## Optional: Update your products and prices

Stripe Tax uses information stored on *products* (Products represent what your business sells—whether that's a good or a service) and *prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) to calculate tax, such as *tax code* (A tax code is the category of your product for tax purposes) and *tax behavior* (Tax behavior determines whether you want to include taxes in the price ("inclusive") or add them on top ("exclusive")). If you don’t explicitly specify these configurations, Stripe Tax will use the default tax code selected in [Tax Settings](https://dashboard.stripe.com/settings/tax).

For more information, see [Specify product tax codes and tax behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md).

## Optional: Calculate tax for existing customers

To calculate tax on an existing customer’s Checkout session, set the `automatic_tax[enabled]` parameter to `true` when you create the session. You can base the tax calculations on the customer’s existing addresses or the new addresses that you collected during checkout:

### Use existing addresses on the customer for taxes

If you’ve already collected your existing customers’ addresses, you can base the tax calculations on those addresses rather than the addresses collected during checkout:

- Which customer address does Checkout use for taxes?

  If available, Checkout uses the customer’s saved [shipping address](https://docs.stripe.com/api/customers/object.md#customer_object-shipping-address) to calculate taxes. Otherwise, Checkout uses the customer’s saved [billing address](https://docs.stripe.com/api/customers/object.md#customer_object-address) to calculate taxes.

- Do the customer addresses have to meet any requirements?

  When using existing addresses for taxes, the customer must either have a valid [shipping address](https://docs.stripe.com/api/customers/object.md#customer_object-shipping-address) or [billing address](https://docs.stripe.com/api/customers/object.md#customer_object-address) saved. You can see whether or not a customer’s saved addresses are valid by checking their [customer.tax.automatic_tax](https://docs.stripe.com/api/customers/object.md#customer_object-tax-automatic_tax) property. If `customer.tax.automatic_tax` value is `supported` or `not_collecting`, the customer’s saved addresses are valid, and you can enable Stripe Tax on Checkout sessions for that customer.

```curl
curl https://api.stripe.com/v1/checkout/sessions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "line_items[0][price]"="{{PRICE_ID}}" \
  -d "line_items[0][quantity]"=2 \
  -d "automatic_tax[enabled]"=true \
  -d customer="{{CUSTOMER_ID}}" \
  -d mode=payment \
  -d ui_mode=embedded \
  --data-urlencode return_url="https://example.com/return"
```

### Use addresses collected during Checkout for taxes

You can configure Checkout to save a customer’s new billing or shipping addresses. In this case, Checkout calculates the tax by using the address entered during checkout.

- Which address does Checkout use for taxes?

  If you’re [collecting shipping addresses](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-shipping_address_collection), Checkout uses the shipping address entered during the session to calculate taxes. Otherwise, Checkout uses the billing address entered during the session to calculate taxes.

- Where are the addresses collected during Checkout saved?

  If you’re [collecting shipping addresses](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-shipping_address_collection), Checkout saves the shipping address entered during the session to the customer’s [customer.shipping.address](https://docs.stripe.com/api/customers/object.md#customer_object-shipping-address) property. Otherwise, Checkout saves the billing address entered during the session to the customer’s [customer.address](https://docs.stripe.com/api/customers/object.md#customer_object-address) property. In both cases, the address used for taxes will override any existing addresses.

If you’re collecting shipping addresses with Checkout, set the `customer_update[shipping]` property to `auto`. This allows you to copy the shipping information from Checkout to the customer.

```curl
curl https://api.stripe.com/v1/checkout/sessions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "line_items[0][price]"="{{PRICE_ID}}" \
  -d "line_items[0][quantity]"=2 \
  -d "automatic_tax[enabled]"=true \
  -d customer="{{CUSTOMER_ID}}" \
  -d "customer_update[shipping]"=auto \
  -d "shipping_address_collection[allowed_countries][0]"=US \
  -d mode=payment \
  -d ui_mode=embedded \
  --data-urlencode return_url="https://example.com/return"
```

If you aren’t collecting shipping addresses with Checkout, and you want to use billing addresses entered during checkout for taxes, you must save the billing address to the customer. Set the `customer_update[address]` property to `auto` so that you copy the newly-entered address onto the provided customer.

```curl
curl https://api.stripe.com/v1/checkout/sessions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "line_items[0][price]"="{{PRICE_ID}}" \
  -d "line_items[0][quantity]"=2 \
  -d "automatic_tax[enabled]"=true \
  -d customer="{{CUSTOMER_ID}}" \
  -d "customer_update[shipping]"=auto \
  -d mode=payment \
  -d ui_mode=embedded \
  --data-urlencode return_url="https://example.com/return"
```

## Optional: Check the response

To see the results of the latest tax calculation, the [total_details.amount_tax](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-total_details) property in the Checkout Session resource shows the calculated tax amount. Additionally, you can use the [Dashboard](https://dashboard.stripe.com/) to view the tax outcome for each payment.

