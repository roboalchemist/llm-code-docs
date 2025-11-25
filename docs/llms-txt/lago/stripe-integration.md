# Source: https://getlago.com/docs/integrations/payments/stripe-integration.md

# Stripe

> Lago's native integration with Stripe allows you to collect payments automatically when new invoices are generated.

## Watch the demo video

<iframe width="100%" height="400" src="https://www.youtube.com/embed/NH8MCMaHeFM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />

## Integration setup[](#integration-setup "Direct link to heading")

To set up the integration with Stripe through the user interface:

1. In the side menu, select **"Settings"**;
2. Select the **"Integrations"** tab;
3. Click **"Stripe"** and add a new connection;
4. Give this new connection a name and a code;
5. Enter your Stripe API key ([locate your API key](https://support.stripe.com/questions/locate-api-keys-in-the-dashboard)); and
6. Click **"Connect to Stripe"** to confirm.

<Info>
  By default, customers created in Lago are not automatically created in Stripe.
  If you want your Lago customers to be added to Stripe, you need to activate
  this option ([learn more](#new-customer)).
</Info>

## Redirect url after checkout[](#checkout-redirect-url "Direct link to heading")

After establishing the connection with Stripe, set a success URL where your end customer will be directed after completing the checkout.
Please note that if it's not defined, your end customer will be redirected to Stripe's website.

Please note that you can edit or delete the redirect URL, and this will only affect new checkout URLs created.

<Warning>
  URL defined should always begin with `http://` or `https://`.
</Warning>

## Customer information[](#customer-information "Direct link to heading")

To collect payments automatically, the customer must exist in both the Lago and
Stripe databases.

### New customer[](#new-customer "Direct link to heading")

If the customer does not already exist in Stripe, you can first create them in
Lago, either via the user interface or [the API](/api-reference/customers/create).
When adding customer information, you must:

1. Define Stripe as the **default payment provider**;
2. Leave the field associated with the **Stripe customer ID** blank;
3. **Enable** the option to automatically create the customer in Stripe; and
4. Define payment method options for this customer. Possible values are `card`, `link`, `sepa_debit`, `us_bank_account`, `bacs_debit`, `boleto`, `crypto` or `customer_balance`.

The customer will automatically be added to Stripe. Stripe will then return the
customer ID, which will be stored in Lago.

<Frame caption="Creation of a new customer with Stripe">
  <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/payments/images/stripe-customer-new.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=f42a03276df140022f9da0acdbd0521f" data-og-width="997" width="997" data-og-height="998" height="998" data-path="guide/payments/images/stripe-customer-new.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/payments/images/stripe-customer-new.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=2f50b1e118a94b2fb1bcd868c303c155 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/payments/images/stripe-customer-new.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=176f278a2c6f7e08b6fbe65b5e834765 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/payments/images/stripe-customer-new.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=02a09872f94995b26a020f8d8765fa5e 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/payments/images/stripe-customer-new.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=66c72b3589246f6ee13ee11ac4df4c27 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/payments/images/stripe-customer-new.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=572565df5b271f5cdd8d500586f58f07 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/payments/images/stripe-customer-new.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=ff9174a147e5dee4860ceae50ceb96e9 2500w" />
</Frame>

### Existing customer[](#existing-customer "Direct link to heading")

If the customer already exists in Stripe but not in Lago, you should create the
customer record, either via the user interface or
[the API](/api-reference/customers/create). When adding customer
information, you must:

1. Define Stripe as the **default payment provider**;
2. Provide the **Stripe customer ID**;
3. **Disable** the option to automatically create the customer in Stripe; and
4. Define payment method options for this customer. Possible values are `card`, `link`, `sepa_debit`, `us_bank_account`, `bacs_debit`, `boleto`, `crypto` or `customer_balance`.

<Frame caption="Migration of an existing Stripe customer">
  <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/payments/images/stripe-customer-migration.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=b22df7a4757dd4bd783adaa3acc584da" data-og-width="901" width="901" data-og-height="1009" height="1009" data-path="guide/payments/images/stripe-customer-migration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/payments/images/stripe-customer-migration.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=09bd56796bda77b26bfb904ea9479f02 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/payments/images/stripe-customer-migration.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=2e80d7bd96d31223b957f7ee8ca5d714 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/payments/images/stripe-customer-migration.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=1a4a3a06f672681fa374f0f59055e9c2 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/payments/images/stripe-customer-migration.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=0b223a66dc73e7917237f59a129ca1f7 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/payments/images/stripe-customer-migration.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=eec5ae554dfa3d443863a357143a2e36 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/payments/images/stripe-customer-migration.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=f7f1a8dcd6f446d043b3fe7a664212b9 2500w" />
</Frame>

## Supported payment methods

Lago's Stripe integration accommodates a variety of payment methods, both generic and region-specific.
The checkout URL provided by Lago is designed to handle multiple payment options seamlessly.

### General payment methods

<AccordionGroup>
  <Accordion title="Card payments" icon="credit-card">
    Lago's Stripe integration includes a universal card payment method that supports various currencies, ideal for global transactions.
    This method is set as the default to facilitate recurring payments, ensuring Lago can process charges for your customers efficiently.

    ```bash  theme={"dark"}
        LAGO_URL="https://api.getlago.com"
    API_KEY="__YOUR_API_KEY__"

    curl --location --request POST "$LAGO_URL/api/v1/customers" \
      --header "Authorization: Bearer $API_KEY" \
      --header 'Content-Type: application/json' \
      --data-raw '{
        "customer": {
          "external_id": "5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba",
          "address_line1": "5230 Penfield Ave",
          "billing_configuration": {
            "invoice_grace_period": 3,
            "payment_provider": "stripe",
            "provider_customer_id": "cus_12345",
            "sync": true,
            "sync_with_provider": true,
            "provider_payment_methods": ["card"]
          }
        }
      }'
    ```
  </Accordion>

  <Accordion title="Link" icon="link">
    For card transactions, you can enable the [Link](https://stripe.com/payments/link) feature to offer one-click payments.
    Link automatically fills in your customers' payment information, ensuring a seamless and secure checkout experience.

    <Warning>
      If you are using the `link` feature, it must be used in conjunction with `card`.
    </Warning>

    ```bash  theme={"dark"}
    LAGO_URL="https://api.getlago.com"
    API_KEY="__YOUR_API_KEY__"

    curl --location --request POST "$LAGO_URL/api/v1/customers" \
      --header "Authorization: Bearer $API_KEY" \
      --header 'Content-Type: application/json' \
      --data-raw '{
        "customer": {
          "external_id": "5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba",
          "address_line1": "5230 Penfield Ave",
          "billing_configuration": {
            "invoice_grace_period": 3,
            "payment_provider": "stripe",
            "provider_customer_id": "cus_12345",
            "sync": true,
            "sync_with_provider": true,
            "provider_payment_methods": ["card", "link"]
          }
        }
      }'
    ```
  </Accordion>

  <Accordion title="Bank Transfers (Customer Balance)" icon="envelope-open-dollar">
    Lago now accepts invoice payments via Stripe bank transfers (customer balance). Supported methods include:

    * JPY: Japan
    * GBP: United Kingdom
    * EUR: Specific SEPA countries (see Stripe documentation)
    * MXN: Mexico
    * USD: United States, United Kingdom, and select SEPA countries

    <Warning>
      If you are using the `customer_balance` payment method in Lago, no other payment method can be selected.
    </Warning>

    ```bash  theme={"dark"}
    LAGO_URL="https://api.getlago.com"
    API_KEY="__YOUR_API_KEY__"

    curl --location --request POST "$LAGO_URL/api/v1/customers" \
      --header "Authorization: Bearer $API_KEY" \
      --header 'Content-Type: application/json' \
      --data-raw '{
        "customer": {
          "external_id": "5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba",
          "address_line1": "5230 Penfield Ave",
          "billing_configuration": {
            "invoice_grace_period": 3,
            "payment_provider": "stripe",
            "provider_customer_id": "cus_12345",
            "sync": true,
            "sync_with_provider": true,
            "provider_payment_methods": ["customer_balance"]
          }
        }
      }'
    ```
  </Accordion>
</AccordionGroup>

### Localized payment methods

<AccordionGroup>
  <Accordion title="SEPA debits (EU only)" icon="money-bill-transfer">
    For European customers, Lago supports Stripe SEPA Debit (Single Euro Payments Area).
    Accepting a mandate through this method authorizes you to debit your customers' accounts for recurring payments via Lago.
    The designated payment method for SEPA transactions within Lago is identified as `sepa_debit`.
    It's important to note that **this payment option is exclusive to invoices in `EUR` currency**.

    ```bash  theme={"dark"}
        LAGO_URL="https://api.getlago.com"
    API_KEY="__YOUR_API_KEY__"

    curl --location --request POST "$LAGO_URL/api/v1/customers" \
      --header "Authorization: Bearer $API_KEY" \
      --header 'Content-Type: application/json' \
      --data-raw '{
        "customer": {
          "external_id": "5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba",
          "address_line1": "5230 Penfield Ave",
          "billing_configuration": {
            "invoice_grace_period": 3,
            "payment_provider": "stripe",
            "provider_customer_id": "cus_12345",
            "sync": true,
            "sync_with_provider": true,
            "provider_payment_methods": ["sepa_debit"]
          }
        }
      }'
    ```
  </Accordion>

  <Accordion title="ACH debits (US only)" icon="flag-usa">
    For US-based transactions, Lago integrates Stripe ACH Debit, leveraging the Automated Clearing House for electronic bank-to-bank payments.
    Upon accepting a mandate, you gain authorization to execute recurring debits from your customers' accounts through Lago.
    The designated payment method for ACH transactions within Lago is identified as `us_bank_account`.
    It's important to note that **this payment option is exclusive to invoices in `USD` currency**.

    ```bash  theme={"dark"}
    LAGO_URL="https://api.getlago.com"
    API_KEY="__YOUR_API_KEY__"

    curl --location --request POST "$LAGO_URL/api/v1/customers" \
      --header "Authorization: Bearer $API_KEY" \
      --header 'Content-Type: application/json' \
      --data-raw '{
        "customer": {
          "external_id": "5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba",
          "address_line1": "5230 Penfield Ave",
          "billing_configuration": {
            "invoice_grace_period": 3,
            "payment_provider": "stripe",
            "provider_customer_id": "cus_12345",
            "sync": true,
            "sync_with_provider": true,
            "provider_payment_methods": ["us_bank_account"]
          }
        }
      }'
    ```
  </Accordion>

  <Accordion title="BACS debits (UK only)" icon="credit-card-front">
    For UK transactions, Lago integrates Stripe BACS Debit, utilizing the UK's BACS system for direct bank-to-bank payments.
    By accepting a mandate with this method, you're authorized to initiate recurring debits from your customers' accounts through Lago.
    The specific payment method for BACS transactions within Lago is designated as `bacs_debit`.
    It's important to note that **this payment method is exclusively for invoices in `GBP` currency.**

    ```bash  theme={"dark"}
    LAGO_URL="https://api.getlago.com"
    API_KEY="__YOUR_API_KEY__"

    curl --location --request POST "$LAGO_URL/api/v1/customers" \
      --header "Authorization: Bearer $API_KEY" \
      --header 'Content-Type: application/json' \
      --data-raw '{
        "customer": {
          "external_id": "5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba",
          "address_line1": "5230 Penfield Ave",
          "billing_configuration": {
            "invoice_grace_period": 3,
            "payment_provider": "stripe",
            "provider_customer_id": "cus_12345",
            "sync": true,
            "sync_with_provider": true,
            "provider_payment_methods": ["bacs_debit"]
          }
        }
      }'
    ```
  </Accordion>

  <Accordion title="Boleto (BRL only)" icon="brazilian-real-sign">
    For transactions in Brazil, you can process payments using Boleto vouchers.
    In Lago, this payment method is identified as `boleto`.
    Note that Boleto is only valid for invoices denominated in Brazilian Real (BRL). Additionally, Boleto payments cannot be refunded and are unlikely to be successfully disputed.

    ```bash  theme={"dark"}
    LAGO_URL="https://api.getlago.com"
    API_KEY="__YOUR_API_KEY__"

    curl --location --request POST "$LAGO_URL/api/v1/customers" \
      --header "Authorization: Bearer $API_KEY" \
      --header 'Content-Type: application/json' \
      --data-raw '{
        "customer": {
          "external_id": "5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba",
          "address_line1": "5230 Penfield Ave",
          "billing_configuration": {
            "invoice_grace_period": 3,
            "payment_provider": "stripe",
            "provider_customer_id": "cus_12345",
            "sync": true,
            "sync_with_provider": true,
            "provider_payment_methods": ["boleto"]
          }
        }
      }'
    ```
  </Accordion>

  <Accordion title="Crypto (Stablecoins)" icon="btc">
    Lago invoices can be paid via Stripe Crypto for USD-denominated invoices only. Please note that payments must be made using stablecoins, such as USDC or USDP.

    ```bash  theme={"dark"}
    LAGO_URL="https://api.getlago.com"
    API_KEY="__YOUR_API_KEY__"

    curl --location --request POST "$LAGO_URL/api/v1/customers" \
      --header "Authorization: Bearer $API_KEY" \
      --header 'Content-Type: application/json' \
      --data-raw '{
        "customer": {
          "external_id": "5eb02857-a71e-4ea2-bcf9-57d3a41bc6ba",
          "address_line1": "5230 Penfield Ave",
          "billing_configuration": {
            "invoice_grace_period": 3,
            "payment_provider": "stripe",
            "provider_customer_id": "cus_12345",
            "sync": true,
            "sync_with_provider": true,
            "provider_payment_methods": ["crypto"]
          }
        }
      }'
    ```
  </Accordion>
</AccordionGroup>

## Stripe Checkout: storing customer's payment method information

<Info>
  Checkout page shows only selected payment methods for customers.
</Info>

When Lago automatically creates a customer in Stripe, you will receive a checkout link from Lago to facilitate the storage of your customer's payment method information.

The payload sent by Lago will have the following structure, with the checkout link stored under `checkout_url`:

```json  theme={"dark"}
{
  "webhook_type": "customer.checkout_url_generated",
  "object_type": "payment_provider_customer_checkout_url",
  "payment_provider_customer_checkout_url": {
    "lago_customer_id": "88d23508-47fd-46bb-a87e-50c50f3cb371",
    "external_customer_id": "hooli_1234",
    "payment_provider": "stripe",
    "checkout_url": "https://checkout.stripe.com/c/pay/prod_c15sTbBMLep5FKOA9b9pZBiRBBYYSU1IJ5T89I5TTtpKgzE380JSmxnVYz#fidkdWxOYHw"
  }
}
```

<Warning>
  Note: The checkout link automatically expires after 24 hours!
</Warning>

By utilizing this provided checkout link, your customers can perform a pre-authorization payment. It's important to note that the pre-authorization payment will not collect any funds from the customer. Once the pre-authorization is confirmed, Lago will send the payment method details and securely store them into Stripe for future transactions.

## Regenerate checkout link on demand

In cases where your end customer has not had the opportunity to complete the checkout process to inform their payment method
or wishes to modify the saved payment information, you can generate a new checkout link using the designated [endpoint](/api-reference/customers/psp-checkout-url).

```bash  theme={"dark"}
POST /api/v1/customers/:customer_external_id/checkout_url
```

Upon successful generation, the new checkout link will be available in the endpoint response, and it will not be delivered through a webhook message.
It is important to note that the new link will inherit the same expiration setting as the original one.

It is crucial to be aware that if a customer is not associated with any payment provider, the response will contain an error message.

## Default payment method

When you add a new payment method in Stripe, **Lago automatically sets it as the default**.
This guarantees that Lago uses the latest payment method for a customer. However, if you manually designate one of
multiple payment methods as the default, Lago will use it for payments instead the most recent one.

## Payment intents[](#payment-intents "Direct link to heading")

Once Stripe is connected and the customer exists in both databases, you can
start collecting payments.

### Succeeded payments

Each time a new invoice with an **amount greater than zero** is generated by
Lago, a payment intent will automatically be created. Stripe will record the
invoice ID and process the payment. If the payment is successful, the status of
the payment will switch from `pending` to `succeeded`.

### Failed payments

If the payment fails, the status of the payment will switch from `pending` to
`failed` and Lago will generate an `invoice.payment_failure`
[webhook](/api-reference/webhooks/messages).

### Payments requiring validation

When a payment requires multi-step authentication, such as 3D Secure (3DS), Lago triggers a `payment.requires_action` [webhook](/api-reference/webhooks/messages#payment-requires-action).
This webhook provides the details for completing the 3DS process. Depending on your integration, you'll get a Stripe Checkout URL or details
to use in your integration (like with Stripe Link).

The invoice will be marked `pending` and the payment as `processing` until the 3DS process is completed.

It's important to note that payments in Europe can request 3DS due to [SCA regulations](https://stripe.com/en-fr/guides/strong-customer-authentication)
and most payments in India require 3DS authentication due to [RBI regulations](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12051\&Mode=0).

### Minimum payment amount

If the new invoice amount falls below the [minimum amount supported by Stripe](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts), the payment status will remain as `pending`.

<Warning>
  A valid payment method for the customer must be defined in Stripe for the
  payment intent to succeed ([learn how to save payment
  details](https://stripe.com/docs/payments/save-and-reuse)).
</Warning>

## Payment disputes

In the event of a **lost** payment dispute within Stripe, Lago initiates an automatic response by marking the relevant invoice as disputed lost. This action involves populating the `dispute_lost_at` field with the timestamp when the dispute was lost. Following this update:

* The invoice becomes non-voidable;
* Generating a credit note is possible; however, refunding the payment back to the original payment method is not permitted; and
* The invoice cannot be resent for collection.

## Restricted Stripe API key

In case you're using Lago Cloud, and want to limit the scope granted to the Stripe API key which is shared with Lago, you can create a [restricted Stripe API key](https://docs.stripe.com/keys-best-practices#limit-access). At minimum, you'll need to grant it the following resource permissions, otherwise Stripe integration will not work properly:

* Core
  * Charges - `Write` (to create refunds when creating credit notes)
  * Customers - `Write`
  * Events - `Read` (to receive webhooks with event details)
  * Funding Instructions - `Write` (to create and read bank details)
  * Payment Intents - `Write` (to create payments)
  * Payment Methods - `Write` (to update customer's payment methods)
* Checkout
  * Checkout Sessions - `Write` (to generate checkout URLs)
* Webhook
  * Webhook Endpoints - `Write` (to create and update webhooks)
