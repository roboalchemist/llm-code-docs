# Source: https://docs.stripe.com/invoicing/taxes/tax-rates.md

# Source: https://docs.stripe.com/billing/taxes/tax-rates.md

# Source: https://docs.stripe.com/invoicing/taxes/tax-rates.md

# Source: https://docs.stripe.com/billing/taxes/tax-rates.md

# Source: https://docs.stripe.com/invoicing/taxes/tax-rates.md

# Tax rates and IDs

Assign tax rates to draft invoices for automatic tax calculation.

If you’re looking for automated tax calculation where you don’t need to define the rates, use [Stripe Tax](https://docs.stripe.com/tax.md).

After you [create a tax rate](https://docs.stripe.com/billing/taxes/tax-rates.md), you can assign it:

- On individual *invoice* (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice) items.
- On the entire subtotal of the invoice.

> Stripe recommends that you assign a tax rate on individual invoice items.

## Set tax rates on individual items 

You can set tax rates on individual items using the [Dashboard](https://dashboard.stripe.com/invoices/create) or [API](https://docs.stripe.com/api/tax_rates.md). You can add up to ten tax rates to each line item.

#### Dashboard

If you’re creating an invoice through the Dashboard, assign tax rates to individual line items.

#### API

When you modify or create invoice line items through the API, set the invoice item’s [tax_rates](https://docs.stripe.com/api/invoiceitems/update.md#update_invoiceitem-tax_rates):

```curl
curl https://api.stripe.com/v1/invoiceitems/ii_CWYWo9Ham19N4a \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "tax_rates[]"=txr_1EO66sClCIKljWvs98IiVfHW \
  -d "tax_rates[]"=txr_1EEOvcClCIKljWvsqYb9U0MB
```

```cli
stripe invoiceitems update ii_CWYWo9Ham19N4a \
  -d "tax_rates[0]"=txr_1EO66sClCIKljWvs98IiVfHW \
  -d "tax_rates[1]"=txr_1EEOvcClCIKljWvsqYb9U0MB
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

invoice_item = client.v1.invoice_items.update(
  'ii_CWYWo9Ham19N4a',
  {tax_rates: ['txr_1EO66sClCIKljWvs98IiVfHW', 'txr_1EEOvcClCIKljWvsqYb9U0MB']},
)
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
invoice_item = client.v1.invoice_items.update(
  "ii_CWYWo9Ham19N4a",
  {"tax_rates": ["txr_1EO66sClCIKljWvs98IiVfHW", "txr_1EEOvcClCIKljWvsqYb9U0MB"]},
)
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$invoiceItem = $stripe->invoiceItems->update(
  'ii_CWYWo9Ham19N4a',
  ['tax_rates' => ['txr_1EO66sClCIKljWvs98IiVfHW', 'txr_1EEOvcClCIKljWvsqYb9U0MB']]
);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

InvoiceItemUpdateParams params =
  InvoiceItemUpdateParams.builder()
    .addTaxRate("txr_1EO66sClCIKljWvs98IiVfHW")
    .addTaxRate("txr_1EEOvcClCIKljWvsqYb9U0MB")
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
InvoiceItem invoiceItem = client.v1().invoiceItems().update("ii_CWYWo9Ham19N4a", params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoiceItem = await stripe.invoiceItems.update(
  'ii_CWYWo9Ham19N4a',
  {
    tax_rates: ['txr_1EO66sClCIKljWvs98IiVfHW', 'txr_1EEOvcClCIKljWvsqYb9U0MB'],
  }
);
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.InvoiceItemUpdateParams{
  TaxRates: []*string{
    stripe.String("txr_1EO66sClCIKljWvs98IiVfHW"),
    stripe.String("txr_1EEOvcClCIKljWvsqYb9U0MB"),
  },
  InvoiceItem: stripe.String("ii_CWYWo9Ham19N4a"),
}
result, err := sc.V1InvoiceItems.Update(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new InvoiceItemUpdateOptions
{
    TaxRates = new List<string>
    {
        "txr_1EO66sClCIKljWvs98IiVfHW",
        "txr_1EEOvcClCIKljWvsqYb9U0MB",
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.InvoiceItems;
InvoiceItem invoiceItem = service.Update("ii_CWYWo9Ham19N4a", options);
```

For [type](https://docs.stripe.com/api/invoices/line_item.md#invoice_line_item_object-type) `subscription` or `invoiceitem`, use the line item’s [id](https://docs.stripe.com/api/invoices/line_item.md#invoice_line_item_object-id). For `type=invoiceitem`, you can also use the [invoice_item](https://docs.stripe.com/api/invoices/line_item.md#invoice_line_item_object-invoice_item) value.

> For API version [2018-05-21](https://docs.stripe.com/upgrades.md#2018-05-21) and earlier, you must pass the `unique_line_item_id` parameter instead of the line item’s `id` field. Pass the `id` field that starts with `sli_`.

## Set default tax rates for the entire invoice 

If you sell one type of product, or have simple tax needs, you can set a default tax rate on the invoice. Default tax rates apply to all invoice line items. For more complex use cases, you can also set an item-level tax rate that overrides the default tax rate. You can add up to five default tax rates to each invoice.

#### Dashboard

If you’re creating an invoice through the Dashboard, you can assign a default tax rate after you add an item.

#### API

To set the invoice’s [default_tax_rates](https://docs.stripe.com/api/invoices/update.md#update_invoice-default_tax_rates) through the API:

```curl
curl https://api.stripe.com/v1/invoices/in_18jwqyLlRB0eXbMtrUQ97YBw \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "default_tax_rates[]"=txr_1EO66sClCIKljWvs98IiVfHW \
  -d "default_tax_rates[]"=txr_1EEOvcClCIKljWvsqYb9U0MB
```

```cli
stripe invoices update in_18jwqyLlRB0eXbMtrUQ97YBw \
  -d "default_tax_rates[0]"=txr_1EO66sClCIKljWvs98IiVfHW \
  -d "default_tax_rates[1]"=txr_1EEOvcClCIKljWvsqYb9U0MB
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

invoice = client.v1.invoices.update(
  'in_18jwqyLlRB0eXbMtrUQ97YBw',
  {default_tax_rates: ['txr_1EO66sClCIKljWvs98IiVfHW', 'txr_1EEOvcClCIKljWvsqYb9U0MB']},
)
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
invoice = client.v1.invoices.update(
  "in_18jwqyLlRB0eXbMtrUQ97YBw",
  {"default_tax_rates": ["txr_1EO66sClCIKljWvs98IiVfHW", "txr_1EEOvcClCIKljWvsqYb9U0MB"]},
)
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$invoice = $stripe->invoices->update(
  'in_18jwqyLlRB0eXbMtrUQ97YBw',
  [
    'default_tax_rates' => [
      'txr_1EO66sClCIKljWvs98IiVfHW',
      'txr_1EEOvcClCIKljWvsqYb9U0MB',
    ],
  ]
);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

InvoiceUpdateParams params =
  InvoiceUpdateParams.builder()
    .addDefaultTaxRate("txr_1EO66sClCIKljWvs98IiVfHW")
    .addDefaultTaxRate("txr_1EEOvcClCIKljWvsqYb9U0MB")
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
Invoice invoice = client.v1().invoices().update("in_18jwqyLlRB0eXbMtrUQ97YBw", params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoice = await stripe.invoices.update(
  'in_18jwqyLlRB0eXbMtrUQ97YBw',
  {
    default_tax_rates: ['txr_1EO66sClCIKljWvs98IiVfHW', 'txr_1EEOvcClCIKljWvsqYb9U0MB'],
  }
);
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.InvoiceUpdateParams{
  DefaultTaxRates: []*string{
    stripe.String("txr_1EO66sClCIKljWvs98IiVfHW"),
    stripe.String("txr_1EEOvcClCIKljWvsqYb9U0MB"),
  },
  Invoice: stripe.String("in_18jwqyLlRB0eXbMtrUQ97YBw"),
}
result, err := sc.V1Invoices.Update(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new InvoiceUpdateOptions
{
    DefaultTaxRates = new List<string>
    {
        "txr_1EO66sClCIKljWvs98IiVfHW",
        "txr_1EEOvcClCIKljWvsqYb9U0MB",
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Invoices;
Invoice invoice = service.Update("in_18jwqyLlRB0eXbMtrUQ97YBw", options);
```
