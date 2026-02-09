# Source: https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md

# Specify product tax codes and tax behavior

Add tax codes and tax behavior to your products and prices to automatically calculate tax.

> [Log in](https://dashboard.stripe.com/settings/tax) or [sign up](https://dashboard.stripe.com/register) for Stripe to enable Stripe Tax.

Stripe Tax uses product tax codes to associate products with their applicable tax rates. Assign each of your [products a tax code](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md#tax-code-on-product) to automatically apply the rate and other taxability rules.

Tax codes within Stripe are always the same across different jurisdictions. However, individual products might have tax treatments that differ by location, and Stripe maintains current rate and taxability information for you, while staying up to date with any changing regulations.

See our [list of available tax codes](https://docs.stripe.com/tax/tax-codes.md).

## Preset tax codes 

When activating Stripe Tax you can set two types of preset tax codes: one for products and one for shipping. You can set both in the [Tax settings](https://dashboard.stripe.com/settings/tax) in the Dashboard.

### Preset product tax code 

We use the preset if you don’t explicitly specify a `tax_code` on your *products* (Products represent what your business sells—whether that's a good or a service) or in [product_data](https://docs.stripe.com/api/prices/create.md#create_price-product_data) on your transactions. As you process payments, we also use the preset tax code to display the tax thresholds you might be approaching or have exceeded, under the **Threshold monitoring** section in your tax settings.

### Preset shipping tax code 

The preset shipping tax code  represents the tax treatment for shipping fees when charged. We use this if you don’t explicitly specify a `tax_code` on a shipping rate. Stripe Tax allows you to change the default shipping treatment to Nontaxable if you don’t want to charge any tax on shipping fees. We recommend you leave the default as “Shipping” to ensure the correct tax is always charged.

Tax rules for shipping fees typically follow one of two methods, depending on the state or country:

- **Proportional Allocation Method:** Shipping fees are taxed at the same rate as the items being shipped. If an order contains items with different tax rates or a mix of taxable and non-taxable goods, the shipping cost is divided proportionally based on the value of the goods. The tax rate of each item is then applied to its corresponding share of the shipping fee.
- **Highest Tax Rate Method:** The entire shipping fee is taxed at the highest rate applied to any item in the order. For example, if a customer buys a tax-exempt item and a fully taxable item, the shipping cost is taxed at the higher rate.

To charge tax on shipping for subscriptions, you can create a Product or pass `product_data` for a line item called “shipping” and select the shipping `tax_code`.

## Tax behavior 

You must specify a `tax_behavior` on a price, or a default tax behavior in the tax settings in the Dashboard, which determines how tax is presented to the buyer. This allows you to localize your checkout depending on the market.

Tax-exclusive prices are common in the US and Canada and for B2B sales in other countries. Set the tax behavior to exclusive to add tax to the subtotal amount specified in your price.

Tax-inclusive prices are common for B2C sales in many markets outside the US. When set to inclusive, the amount your buyer pays remains constant, regardless of the tax amount (zero or positive). This applies to sales subject to reverse charge as well. The unit price differs between transactions subject to reverse charge and those that aren’t. If no tax applies, the tax-inclusive price is the unit price. If the tax amount is positive, the unit price is lower, excluding the tax amount.

### Set a default tax behavior  (Recommended)

You can define a default tax behavior that applies to every price that has no tax behavior defined. You can setup the default tax behavior in the [Stripe Tax settings](https://dashboard.stripe.com/settings/tax) under the **Include tax in prices** section.

After you set the default tax behavior, all prices that don’t have a `tax_behavior` defined, use this setting and are ready for Stripe Tax. The options for the default tax behavior are:

- **Automatic**: The tax behavior is based on the currency that’s chosen for a product price. For the currencies `USD` and `CAD` the tax behavior is exclusive. For all other currencies the tax behavior is inclusive. This also works with *multi-currency Prices* (A single Price object can support multiple currencies. Each purchase uses one of the supported currencies for the Price, depending on how you use the Price in your integration).
- **Inclusive**: *Inclusive tax* (Inclusive tax is tax that doesn't change the final purchase price—the price the buyer sees already includes it. Examples of inclusive tax include VAT and GST outside of the US) is already included in the price. For example, a product has the price defined as 5.00 USD. The final price the customer pays is 5.00 USD.
- **Exclusive**: *Exclusive tax* (Exclusive tax is tax that changes the final purchase price—the listed price the buyer sees doesn't include it, and it's added to the total. An example of exclusive tax is US sales tax) is added on top of the price. For example, a product has the price defined as 5.00 USD. The tax charged on this product could be 10% and would result in a final price of 5.50 USD. (Tax rates might differ—this is only an explanatory example.)

To override this setting for an individual price, [set a tax behavior on a price](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md#setting-tax-behavior-on-a-price-\(optional\)).

## Set tax behavior on a price  (Optional)

You can set the tax behavior for a *Price* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) when creating it with the Dashboard or the API. When creating a Price in the Dashboard, you can inspect the impact of your pricing model on your revenue.

> You can’t change `tax_behavior` after it’s been set to **exclusive** or **inclusive**.

To create a Price with `tax_behavior` through the API:

```curl
curl https://api.stripe.com/v1/prices \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d unit_amount=10000 \
  -d currency=usd \
  -d product="{{PRODUCT_ID}}" \
  -d tax_behavior=exclusive \
  -d "recurring[interval]"=month
```

```cli
stripe prices create  \
  --unit-amount=10000 \
  --currency=usd \
  --product="{{PRODUCT_ID}}" \
  --tax-behavior=exclusive \
  -d "recurring[interval]"=month
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

price = client.v1.prices.create({
  unit_amount: 10000,
  currency: 'usd',
  product: '{{PRODUCT_ID}}',
  tax_behavior: 'exclusive',
  recurring: {interval: 'month'},
})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
price = client.v1.prices.create({
  "unit_amount": 10000,
  "currency": "usd",
  "product": "{{PRODUCT_ID}}",
  "tax_behavior": "exclusive",
  "recurring": {"interval": "month"},
})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$price = $stripe->prices->create([
  'unit_amount' => 10000,
  'currency' => 'usd',
  'product' => '{{PRODUCT_ID}}',
  'tax_behavior' => 'exclusive',
  'recurring' => ['interval' => 'month'],
]);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PriceCreateParams params =
  PriceCreateParams.builder()
    .setUnitAmount(10000L)
    .setCurrency("usd")
    .setProduct("{{PRODUCT_ID}}")
    .setTaxBehavior(PriceCreateParams.TaxBehavior.EXCLUSIVE)
    .setRecurring(
      PriceCreateParams.Recurring.builder()
        .setInterval(PriceCreateParams.Recurring.Interval.MONTH)
        .build()
    )
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
Price price = client.v1().prices().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const price = await stripe.prices.create({
  unit_amount: 10000,
  currency: 'usd',
  product: '{{PRODUCT_ID}}',
  tax_behavior: 'exclusive',
  recurring: {
    interval: 'month',
  },
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PriceCreateParams{
  UnitAmount: stripe.Int64(10000),
  Currency: stripe.String(stripe.CurrencyUSD),
  Product: stripe.String("{{PRODUCT_ID}}"),
  TaxBehavior: stripe.String(stripe.PriceTaxBehaviorExclusive),
  Recurring: &stripe.PriceCreateRecurringParams{
    Interval: stripe.String(stripe.PriceRecurringIntervalMonth),
  },
}
result, err := sc.V1Prices.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new PriceCreateOptions
{
    UnitAmount = 10000,
    Currency = "usd",
    Product = "{{PRODUCT_ID}}",
    TaxBehavior = "exclusive",
    Recurring = new PriceRecurringOptions { Interval = "month" },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Prices;
Price price = service.Create(options);
```

For a *multi-currency Price* (A single Price object can support multiple currencies. Each purchase uses one of the supported currencies for the Price, depending on how you use the Price in your integration), use the [currency_options.<currency>.tax_behavior](https://docs.stripe.com/api/prices/create.md#create_price-currency_options-tax_behavior) parameter to set different tax behaviors for different currencies.

In some cases, you might want to use a custom price that hasn’t been pre-configured. You can pass in `price_data` instead of a price ID. For example, accepting a one time payment for a custom price with the [hosted version of Checkout](https://docs.stripe.com/checkout/quickstart.md) looks like this:

```curl
curl https://api.stripe.com/v1/checkout/sessions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "line_items[0][price_data][currency]"=usd \
  -d "line_items[0][price_data][unit_amount]"=10000 \
  -d "line_items[0][price_data][tax_behavior]"=exclusive \
  -d "line_items[0][price_data][product]"="{{PRODUCT_ID}}" \
  -d "line_items[0][quantity]"=2 \
  -d mode=payment \
  --data-urlencode success_url="https://example.com/success"
```

```cli
stripe checkout sessions create  \
  -d "line_items[0][price_data][currency]"=usd \
  -d "line_items[0][price_data][unit_amount]"=10000 \
  -d "line_items[0][price_data][tax_behavior]"=exclusive \
  -d "line_items[0][price_data][product]"="{{PRODUCT_ID}}" \
  -d "line_items[0][quantity]"=2 \
  --mode=payment \
  --success-url="https://example.com/success"
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

session = client.v1.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: 'usd',
        unit_amount: 10000,
        tax_behavior: 'exclusive',
        product: '{{PRODUCT_ID}}',
      },
      quantity: 2,
    },
  ],
  mode: 'payment',
  success_url: 'https://example.com/success',
})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
session = client.v1.checkout.sessions.create({
  "line_items": [
    {
      "price_data": {
        "currency": "usd",
        "unit_amount": 10000,
        "tax_behavior": "exclusive",
        "product": "{{PRODUCT_ID}}",
      },
      "quantity": 2,
    },
  ],
  "mode": "payment",
  "success_url": "https://example.com/success",
})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$session = $stripe->checkout->sessions->create([
  'line_items' => [
    [
      'price_data' => [
        'currency' => 'usd',
        'unit_amount' => 10000,
        'tax_behavior' => 'exclusive',
        'product' => '{{PRODUCT_ID}}',
      ],
      'quantity' => 2,
    ],
  ],
  'mode' => 'payment',
  'success_url' => 'https://example.com/success',
]);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SessionCreateParams params =
  SessionCreateParams.builder()
    .addLineItem(
      SessionCreateParams.LineItem.builder()
        .setPriceData(
          SessionCreateParams.LineItem.PriceData.builder()
            .setCurrency("usd")
            .setUnitAmount(10000L)
            .setTaxBehavior(SessionCreateParams.LineItem.PriceData.TaxBehavior.EXCLUSIVE)
            .setProduct("{{PRODUCT_ID}}")
            .build()
        )
        .setQuantity(2L)
        .build()
    )
    .setMode(SessionCreateParams.Mode.PAYMENT)
    .setSuccessUrl("https://example.com/success")
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
Session session = client.v1().checkout().sessions().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: 'usd',
        unit_amount: 10000,
        tax_behavior: 'exclusive',
        product: '{{PRODUCT_ID}}',
      },
      quantity: 2,
    },
  ],
  mode: 'payment',
  success_url: 'https://example.com/success',
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CheckoutSessionCreateParams{
  LineItems: []*stripe.CheckoutSessionCreateLineItemParams{
    &stripe.CheckoutSessionCreateLineItemParams{
      PriceData: &stripe.CheckoutSessionCreateLineItemPriceDataParams{
        Currency: stripe.String(stripe.CurrencyUSD),
        UnitAmount: stripe.Int64(10000),
        TaxBehavior: stripe.String("exclusive"),
        Product: stripe.String("{{PRODUCT_ID}}"),
      },
      Quantity: stripe.Int64(2),
    },
  },
  Mode: stripe.String(stripe.CheckoutSessionModePayment),
  SuccessURL: stripe.String("https://example.com/success"),
}
result, err := sc.V1CheckoutSessions.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new Stripe.Checkout.SessionCreateOptions
{
    LineItems = new List<Stripe.Checkout.SessionLineItemOptions>
    {
        new Stripe.Checkout.SessionLineItemOptions
        {
            PriceData = new Stripe.Checkout.SessionLineItemPriceDataOptions
            {
                Currency = "usd",
                UnitAmount = 10000,
                TaxBehavior = "exclusive",
                Product = "{{PRODUCT_ID}}",
            },
            Quantity = 2,
        },
    },
    Mode = "payment",
    SuccessUrl = "https://example.com/success",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Checkout.Sessions;
Stripe.Checkout.Session session = service.Create(options);
```

## Set a tax code on a product  (Recommended)

When creating Products in the Dashboard you can set your `tax_code` in the dropdown by searching for any available [tax code](https://docs.stripe.com/tax/tax-codes.md). If you don’t, Stripe Tax uses the preset tax code defined on the [Dashboard](https://dashboard.stripe.com/settings/tax). If a product could fit multiple codes, for example, a SaaS product used for personal or business use depending on the type of customer, we recommend creating two separate products in Stripe and assigning the appropriate code to each.

To create a Product with `tax_code` using the API:

```curl
curl https://api.stripe.com/v1/products \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d name="Test Product" \
  -d tax_code="{{TAXCODE_ID}}"
```

```cli
stripe products create  \
  --name="Test Product" \
  --tax-code="{{TAXCODE_ID}}"
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

product = client.v1.products.create({
  name: 'Test Product',
  tax_code: '{{TAXCODE_ID}}',
})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
product = client.v1.products.create({
  "name": "Test Product",
  "tax_code": "{{TAXCODE_ID}}",
})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$product = $stripe->products->create([
  'name' => 'Test Product',
  'tax_code' => '{{TAXCODE_ID}}',
]);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ProductCreateParams params =
  ProductCreateParams.builder()
    .setName("Test Product")
    .setTaxCode("{{TAXCODE_ID}}")
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
Product product = client.v1().products().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const product = await stripe.products.create({
  name: 'Test Product',
  tax_code: '{{TAXCODE_ID}}',
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ProductCreateParams{
  Name: stripe.String("Test Product"),
  TaxCode: stripe.String("{{TAXCODE_ID}}"),
}
result, err := sc.V1Products.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new ProductCreateOptions
{
    Name = "Test Product",
    TaxCode = "{{TAXCODE_ID}}",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Products;
Product product = service.Create(options);
```

In some cases, you might want to use a custom product that hasn’t been pre-configured. You can pass in `product_data` instead of a product ID. For example, accepting a one time payment for a custom product with the [hosted version of Checkout](https://docs.stripe.com/checkout/quickstart.md) looks like this:

```curl
curl https://api.stripe.com/v1/checkout/sessions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "line_items[0][price_data][currency]"=usd \
  -d "line_items[0][price_data][unit_amount]"=10000 \
  -d "line_items[0][price_data][tax_behavior]"=exclusive \
  -d "line_items[0][price_data][product_data][name]"="Test Product" \
  -d "line_items[0][price_data][product_data][tax_code]"="{{TAXCODE_ID}}" \
  -d "line_items[0][quantity]"=2 \
  -d mode=payment \
  --data-urlencode success_url="https://example.com/success"
```

```cli
stripe checkout sessions create  \
  -d "line_items[0][price_data][currency]"=usd \
  -d "line_items[0][price_data][unit_amount]"=10000 \
  -d "line_items[0][price_data][tax_behavior]"=exclusive \
  -d "line_items[0][price_data][product_data][name]"="Test Product" \
  -d "line_items[0][price_data][product_data][tax_code]"="{{TAXCODE_ID}}" \
  -d "line_items[0][quantity]"=2 \
  --mode=payment \
  --success-url="https://example.com/success"
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

session = client.v1.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: 'usd',
        unit_amount: 10000,
        tax_behavior: 'exclusive',
        product_data: {
          name: 'Test Product',
          tax_code: '{{TAXCODE_ID}}',
        },
      },
      quantity: 2,
    },
  ],
  mode: 'payment',
  success_url: 'https://example.com/success',
})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
session = client.v1.checkout.sessions.create({
  "line_items": [
    {
      "price_data": {
        "currency": "usd",
        "unit_amount": 10000,
        "tax_behavior": "exclusive",
        "product_data": {"name": "Test Product", "tax_code": "{{TAXCODE_ID}}"},
      },
      "quantity": 2,
    },
  ],
  "mode": "payment",
  "success_url": "https://example.com/success",
})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$session = $stripe->checkout->sessions->create([
  'line_items' => [
    [
      'price_data' => [
        'currency' => 'usd',
        'unit_amount' => 10000,
        'tax_behavior' => 'exclusive',
        'product_data' => [
          'name' => 'Test Product',
          'tax_code' => '{{TAXCODE_ID}}',
        ],
      ],
      'quantity' => 2,
    ],
  ],
  'mode' => 'payment',
  'success_url' => 'https://example.com/success',
]);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SessionCreateParams params =
  SessionCreateParams.builder()
    .addLineItem(
      SessionCreateParams.LineItem.builder()
        .setPriceData(
          SessionCreateParams.LineItem.PriceData.builder()
            .setCurrency("usd")
            .setUnitAmount(10000L)
            .setTaxBehavior(SessionCreateParams.LineItem.PriceData.TaxBehavior.EXCLUSIVE)
            .setProductData(
              SessionCreateParams.LineItem.PriceData.ProductData.builder()
                .setName("Test Product")
                .setTaxCode("{{TAXCODE_ID}}")
                .build()
            )
            .build()
        )
        .setQuantity(2L)
        .build()
    )
    .setMode(SessionCreateParams.Mode.PAYMENT)
    .setSuccessUrl("https://example.com/success")
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
Session session = client.v1().checkout().sessions().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: 'usd',
        unit_amount: 10000,
        tax_behavior: 'exclusive',
        product_data: {
          name: 'Test Product',
          tax_code: '{{TAXCODE_ID}}',
        },
      },
      quantity: 2,
    },
  ],
  mode: 'payment',
  success_url: 'https://example.com/success',
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CheckoutSessionCreateParams{
  LineItems: []*stripe.CheckoutSessionCreateLineItemParams{
    &stripe.CheckoutSessionCreateLineItemParams{
      PriceData: &stripe.CheckoutSessionCreateLineItemPriceDataParams{
        Currency: stripe.String(stripe.CurrencyUSD),
        UnitAmount: stripe.Int64(10000),
        TaxBehavior: stripe.String("exclusive"),
        ProductData: &stripe.CheckoutSessionCreateLineItemPriceDataProductDataParams{
          Name: stripe.String("Test Product"),
          TaxCode: stripe.String("{{TAXCODE_ID}}"),
        },
      },
      Quantity: stripe.Int64(2),
    },
  },
  Mode: stripe.String(stripe.CheckoutSessionModePayment),
  SuccessURL: stripe.String("https://example.com/success"),
}
result, err := sc.V1CheckoutSessions.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new Stripe.Checkout.SessionCreateOptions
{
    LineItems = new List<Stripe.Checkout.SessionLineItemOptions>
    {
        new Stripe.Checkout.SessionLineItemOptions
        {
            PriceData = new Stripe.Checkout.SessionLineItemPriceDataOptions
            {
                Currency = "usd",
                UnitAmount = 10000,
                TaxBehavior = "exclusive",
                ProductData = new Stripe.Checkout.SessionLineItemPriceDataProductDataOptions
                {
                    Name = "Test Product",
                    TaxCode = "{{TAXCODE_ID}}",
                },
            },
            Quantity = 2,
        },
    },
    Mode = "payment",
    SuccessUrl = "https://example.com/success",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Checkout.Sessions;
Stripe.Checkout.Session session = service.Create(options);
```

## Create a shipping rate with tax code  (Optional)

Checkout payment mode allows you to set shipping rates and charge tax on shipping. You can automatically calculate tax on shipping charges by setting the tax code on the shipping rate in the Dashboard or [API](https://docs.stripe.com/api/shipping_rates.md).

```curl
curl https://api.stripe.com/v1/shipping_rates \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d display_name="Ground shipping" \
  -d type=fixed_amount \
  -d "fixed_amount[amount]"=500 \
  -d "fixed_amount[currency]"=usd \
  -d tax_behavior=inclusive \
  -d tax_code="{{TAXCODE_ID}}"
```

```cli
stripe shipping_rates create  \
  --display-name="Ground shipping" \
  --type=fixed_amount \
  -d "fixed_amount[amount]"=500 \
  -d "fixed_amount[currency]"=usd \
  --tax-behavior=inclusive \
  --tax-code="{{TAXCODE_ID}}"
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

shipping_rate = client.v1.shipping_rates.create({
  display_name: 'Ground shipping',
  type: 'fixed_amount',
  fixed_amount: {
    amount: 500,
    currency: 'usd',
  },
  tax_behavior: 'inclusive',
  tax_code: '{{TAXCODE_ID}}',
})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
shipping_rate = client.v1.shipping_rates.create({
  "display_name": "Ground shipping",
  "type": "fixed_amount",
  "fixed_amount": {"amount": 500, "currency": "usd"},
  "tax_behavior": "inclusive",
  "tax_code": "{{TAXCODE_ID}}",
})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$shippingRate = $stripe->shippingRates->create([
  'display_name' => 'Ground shipping',
  'type' => 'fixed_amount',
  'fixed_amount' => [
    'amount' => 500,
    'currency' => 'usd',
  ],
  'tax_behavior' => 'inclusive',
  'tax_code' => '{{TAXCODE_ID}}',
]);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ShippingRateCreateParams params =
  ShippingRateCreateParams.builder()
    .setDisplayName("Ground shipping")
    .setType(ShippingRateCreateParams.Type.FIXED_AMOUNT)
    .setFixedAmount(
      ShippingRateCreateParams.FixedAmount.builder()
        .setAmount(500L)
        .setCurrency("usd")
        .build()
    )
    .setTaxBehavior(ShippingRateCreateParams.TaxBehavior.INCLUSIVE)
    .setTaxCode("{{TAXCODE_ID}}")
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
ShippingRate shippingRate = client.v1().shippingRates().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const shippingRate = await stripe.shippingRates.create({
  display_name: 'Ground shipping',
  type: 'fixed_amount',
  fixed_amount: {
    amount: 500,
    currency: 'usd',
  },
  tax_behavior: 'inclusive',
  tax_code: '{{TAXCODE_ID}}',
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ShippingRateCreateParams{
  DisplayName: stripe.String("Ground shipping"),
  Type: stripe.String("fixed_amount"),
  FixedAmount: &stripe.ShippingRateCreateFixedAmountParams{
    Amount: stripe.Int64(500),
    Currency: stripe.String(stripe.CurrencyUSD),
  },
  TaxBehavior: stripe.String(stripe.ShippingRateTaxBehaviorInclusive),
  TaxCode: stripe.String("{{TAXCODE_ID}}"),
}
result, err := sc.V1ShippingRates.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new ShippingRateCreateOptions
{
    DisplayName = "Ground shipping",
    Type = "fixed_amount",
    FixedAmount = new ShippingRateFixedAmountOptions { Amount = 500, Currency = "usd" },
    TaxBehavior = "inclusive",
    TaxCode = "{{TAXCODE_ID}}",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.ShippingRates;
ShippingRate shippingRate = service.Create(options);
```

## See also

- [Checkout and Tax](https://docs.stripe.com/tax/checkout.md)
- [Invoicing and Tax](https://docs.stripe.com/tax/invoicing.md)
- [Determining customer locations](https://docs.stripe.com/tax/customer-locations.md)
