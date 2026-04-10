# Source: https://dub.co/docs/conversions/sales/stripe.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dub.co/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Stripe

> Learn how to track sale conversion events with Stripe and Dub

<Note>
  Conversion tracking requires a [Business plan](https://dub.co/pricing)
  subscription or higher.
</Note>

When it comes to [conversion tracking](/conversions/quickstart), a `sale` event happens when a user purchases your product or service. Examples include:

* Subscribing to a paid plan
* Usage expansion (upgrading from one plan to another)
* Purchasing a product from your online store

<Frame>
  <img className="rounded-lg border border-gray-100" src="https://assets.dub.co/help/conversion-sale-event.png" alt="A diagram showing how lead events are tracked in the conversion funnel" />
</Frame>

In this guide, we will be focusing on tracking sale events with Stripe as the payment processor by leveraging Dub's Stripe integration.

## Installing the Dub Stripe integration

Dub comes with a powerful Stripe integration that automatically listens to payment events on Stripe and track them as sales on Dub.

Here's how you can install the Dub Stripe integration:

<Steps>
  <Step title="Find Dub on the Stripe App Marketplace">
    Navigate to the [Dub Stripe Integration](https://d.to/stripe/app) on the Stripe App Marketplace.

    <Frame>
      <img src="https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-marketplace.png?fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=ac43cb50d81677dbf96b05bb87616096" alt="The Dub integration page on the Stripe App Marketplace" data-og-width="2632" width="2632" data-og-height="1960" height="1960" data-path="images/stripe/stripe-app-marketplace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-marketplace.png?w=280&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=9d959078b6fd4566de544d56a11fcd50 280w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-marketplace.png?w=560&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=e0d80b5eb1c20f5d3f2c14711926a633 560w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-marketplace.png?w=840&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=83163af2dbd1e1ba65936c3563e6b434 840w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-marketplace.png?w=1100&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=8c039b4d54e767f9b107520a3fa2de6e 1100w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-marketplace.png?w=1650&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=696e61c8dbf177d94c5e57e182d74446 1650w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-marketplace.png?w=2500&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=e08ef8e19731d452414bafc039320c0e 2500w" />
    </Frame>
  </Step>

  <Step title="Install the Stripe app">
    On the top right, click on **Install app** to install the Dub app on your Stripe account.

    <Frame>
      <img src="https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-install.png?fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=a4cfd0ca21ead504258089f0ce8d5d7b" alt="The Stripe integration installation flow" data-og-width="2560" width="2560" data-og-height="1950" height="1950" data-path="images/stripe/stripe-app-install.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-install.png?w=280&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=6ef9a14d41f5f909c9d110b17725a96c 280w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-install.png?w=560&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=27306f241da3c682506d8661df3fa227 560w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-install.png?w=840&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=1fb08c2fce7406cb5cf43ec424273574 840w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-install.png?w=1100&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=51bfbc4349d06948c900612d8f28562f 1100w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-install.png?w=1650&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=7c86181c1534b6a603848a0a34f75dd0 1650w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-install.png?w=2500&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=9571823c356e38ae90666d62526138ac 2500w" />
    </Frame>

    <Tip>
      Alternatively, you can also install the Stripe app in a [Stripe
      sandbox](https://docs.stripe.com/sandboxes) first to test your end-to-end flow
      without involving real money.
    </Tip>

    Once the app is installed, click on **Continue to app settings** to finish the installation.

    <Frame>
      <img src="https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-install-continue.png?fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=779b38f857dd437d4b060c99be96284e" alt="Continue to app settings" data-og-width="2568" width="2568" data-og-height="1950" height="1950" data-path="images/stripe/stripe-app-install-continue.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-install-continue.png?w=280&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=7ed6f974a815e81deff792bc11f1a3e7 280w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-install-continue.png?w=560&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=0ad758fa5743f3fc772e0fd19c884812 560w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-install-continue.png?w=840&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=c5dace68a6ca2d7489c24b2595533479 840w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-install-continue.png?w=1100&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=ba4792423debcaf49347de597863ce40 1100w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-install-continue.png?w=1650&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=33fe844813182530f23535fadfb9759e 1650w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-install-continue.png?w=2500&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=10be037f25547551dfbffc3233197071 2500w" />
    </Frame>
  </Step>

  <Step title="Connect Stripe to your Dub workspace">
    In the app settings page, click on **Connect workspace** to connect your Stripe account with your Dub workspace.

    <Frame>
      <img src="https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-connect-workspace.png?fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=5fb5b64b7f1e3d4202276b608aa75263" alt="Connect Stripe to Dub" data-og-width="2206" width="2206" data-og-height="1490" height="1490" data-path="images/stripe/stripe-app-connect-workspace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-connect-workspace.png?w=280&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=d47ac51df0b6485634e68136cf247015 280w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-connect-workspace.png?w=560&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=e8babdccc479ca6c0c18414af6ea93ab 560w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-connect-workspace.png?w=840&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=c711e2c11d3f67ba905d7de67d255c79 840w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-connect-workspace.png?w=1100&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=18e2f4a5fdba22a66a67dd26c9cacfd8 1100w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-connect-workspace.png?w=1650&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=af87b9750925ceba2c91858790e76878 1650w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-connect-workspace.png?w=2500&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=7faabbbccf9e3ff976ce8a5b1e0f9af8 2500w" />
    </Frame>

    This will redirect you to the [Dub OAuth flow](/integrations/quickstart), where you can select the Dub workspace you want to connect to your Stripe account.

    <Frame>
      <img src="https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/select-dub-workspace.png?fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=b986d20c9ee907d984cc87cc3b6dd20b" alt="Select the Dub workspace you want to connect to your Stripe account" data-og-width="2396" width="2396" data-og-height="1632" height="1632" data-path="images/stripe/select-dub-workspace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/select-dub-workspace.png?w=280&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=bea4ba44bfcd00f590689dd06dc5a932 280w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/select-dub-workspace.png?w=560&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=7bbbe9b621c656b47d8584cb1a149a7c 560w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/select-dub-workspace.png?w=840&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=52dd368651984177b702fe5f52de1f4c 840w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/select-dub-workspace.png?w=1100&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=1874b4a923c0a8d3ce3b5f8469c2adac 1100w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/select-dub-workspace.png?w=1650&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=1eb9bcfc8997f8636ad858946716514d 1650w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/select-dub-workspace.png?w=2500&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=ddb59fde05ed4dd14e484faf4b009b00 2500w" />
    </Frame>

    Once you click on **Authorize**, you will be redirected back to the Dub app settings page on Stripe, where you should see that the integration is now installed.

    <Frame>
      <img src="https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-installed.png?fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=c745f70375a01b7630995938192eea7a" alt="The Stripe integration is now installed" data-og-width="1874" width="1874" data-og-height="1300" height="1300" data-path="images/stripe/stripe-app-installed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-installed.png?w=280&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=d7ef733d19eac38b59c208a814eec25d 280w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-installed.png?w=560&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=ea85b2c6ef826ccc18f7c6916abe71ea 560w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-installed.png?w=840&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=d9ac7911238f9508ad6844a9fa4673df 840w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-installed.png?w=1100&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=963290b55b20e7bfcad27e95201fa439 1100w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-installed.png?w=1650&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=b381b589ef4417280aa8dd3e0827b266 1650w, https://mintcdn.com/dub/ndS7bf_otKoJnZYr/images/stripe/stripe-app-installed.png?w=2500&fit=max&auto=format&n=ndS7bf_otKoJnZYr&q=85&s=10d4a808d1dfcda19d82c33718a79a6b 2500w" />
    </Frame>
  </Step>
</Steps>

Once the integration is installed, Dub will automatically listen to the following events on Stripe and track them as sales on Dub:

* `customer.created`: When a new customer is created
* `customer.updated`: When a customer is updated
* `checkout.session.completed`: When a customer completes a checkout session
* `invoice.paid`: When an invoice is paid (for tracking recurring subscriptions)
* `charge.refunded`: When a charge is refunded (for tracking refunds and updating payout commissions for [Dub Partners](https://dub.partners))

## Tracking sales with the Dub Stripe integration

Depending on your setup, there are a few ways you can track sales with the Dub Stripe integration.

* [Option 1: Using Stripe Payment Links](#option-1%3A-using-stripe-payment-links)
* [Option 2: Using Stripe Checkout (recommended)](#option-2%3A-using-stripe-checkout-recommended)
* [Option 3: Using Stripe Customers](#option-3%3A-using-stripe-customers)

### Option 1: Using Stripe Payment Links

<Tip>
  For this option to work, you need to [install the Dub Stripe
  integration](#installing-the-dub-stripe-integration) and [enable conversion
  tracking for your
  links](/conversions/quickstart#step-1%3A-enable-conversion-tracking-for-your-links)
  first.
</Tip>

<Note>
  When using Stripe Payment Links, lead and sale events are tracked but lead webhooks and [lead
  rewards](https://dub.co/help/article/partner-rewards#configuring-reward-types)
  will not be generated.
</Note>

If you're using [Stripe Payment Links](https://docs.stripe.com/payment-links), simply add a `?dub_client_reference_id=1` query parameter to your Stripe Payment Link when shortening it on Dub.

Then, when a user clicks on the shortened link, Dub will automatically append the unique click ID as the `client_reference_id` [query parameter](https://docs.stripe.com/payment-links/url-parameters) to the payment link.

<Frame>
  <img src="https://assets.dub.co/cms/conversions-payment-links.jpg" alt="Stripe payment link with Dub click ID" />
</Frame>

Finally, when the user completes the checkout flow, Dub will automatically [track the sale event](/api-reference/endpoint/track-sale) and [update the customer's `customerExternalId`](/api-reference/endpoint/update-a-customer) with their Stripe customer ID for future reference.

Alternatively, if you have a marketing site that you're redirecting your users to first, you can do this instead:

1. [Install the @dub/analytics client-side SDK](/sdks/client-side/introduction), which automatically detects the `dub_id` in the URL and stores it as a first-party cookie on your site.
2. Then, retrieve and append the `dub_id` value as the `client_reference_id` parameter to the payment links on your pricing page / CTA button (prefixed with `dub_id_`).

   ```
   https://buy.stripe.com/xxxxxx?client_reference_id=dub_id_xxxxxxxxxxxxxx
   ```

<AccordionGroup>
  <Accordion title="What if I'm using Stripe Pricing Tables?">
    If you're using [Stripe Pricing Tables](https://docs.stripe.com/payments/checkout/pricing-table) – you'd want to pass the Dub click ID as a [`client-reference-id` attribute](https://docs.stripe.com/payments/checkout/pricing-table#handle-fulfillment-with-the-stripe-api) instead:

    <CodeGroup>
      ```html HTML theme={null}
      <body>
        <h1>We offer plans that help any business!</h1>
        <!-- Paste your embed code script here. -->
        <script async src="https://js.stripe.com/v3/pricing-table.js"></script>
        <stripe-pricing-table
          pricing-table-id="{{PRICING_TABLE_ID}}"
          publishable-key="pk_test_51ODHJvFacAXKeDpJsgWLQJSzBIDtCUFN6MoB4IIXKJDfWdFmiEO4JuvAU1A0Y2Ri4m4q1egIfwYy3s72cUBRCwXC00GQhEZuXa"
          client-reference-id="dub_id_xxxxxxxxxxxxxx"
        >
        </stripe-pricing-table>
      </body>
      ```

      ```jsx React theme={null}
      import * as React from "react";

      function PricingPage() {
        // Paste the stripe-pricing-table snippet in your React component
        return (
          <stripe-pricing-table
            pricing-table-id="'{{PRICING_TABLE_ID}}'"
            publishable-key="pk_test_51ODHJvFacAXKeDpJsgWLQJSzBIDtCUFN6MoB4IIXKJDfWdFmiEO4JuvAU1A0Y2Ri4m4q1egIfwYy3s72cUBRCwXC00GQhEZuXa"
            client-reference-id="dub_id_xxxxxxxxxxxxxx"
          ></stripe-pricing-table>
        );
      }

      export default PricingPage;
      ```
    </CodeGroup>
  </Accordion>

  <Accordion title="What if I'm using Stripe's Checkout Sessions API?">
    If you're using Stripe's [Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions/object) for a recurring subscription service, you might want to check out our [Stripe Checkout option](#option-2%3A-using-stripe-checkout-recommended) instead.

    If your setup doesn't involve a [lead event](/conversions/leads/introduction) and goes straight to the Stripe checkout flow (e.g. for one-time purchases), you can simply pass the Dub click ID (prefixed with `dub_id_`) as the [`client_reference_id` parameter](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-client_reference_id) to enable conversion tracking with Dub.

    <CodeGroup>
      ```javascript Node.js theme={null}
      const session = await stripe.checkout.sessions.create({
        success_url: "https://example.com/success",
        line_items: [
          {
            price: "price_xxxxxxxxxxxxxxxx",
            quantity: 2,
          },
        ],
        mode: "payment",
        client_reference_id: "dub_id_xxxxxxxxxxxxxx",
      });
      ```

      ```python Python theme={null}
        stripe.checkout.Session.create(
          success_url="https://example.com/success",
          line_items=[{"price": "price_xxxxxxxxxxxxxxxx", "quantity": 2}],
          mode="payment",
          client_reference_id="dub_id_xxxxxxxxxxxxxx",
        )
      ```

      ```go Go theme={null}
        params := &stripe.CheckoutSessionParams{
          SuccessURL: stripe.String("https://example.com/success"),
          LineItems: []*stripe.CheckoutSessionLineItemParams{
            &stripe.CheckoutSessionLineItemParams{
              Price: stripe.String("price_xxxxxxxxxxxxxxxx"),
              Quantity: stripe.Int64(2),
            },
          },
          Mode: stripe.String(string(stripe.CheckoutSessionModePayment)),
          ClientReferenceID: stripe.String("dub_id_xxxxxxxxxxxxxx"),
        };
        result, err := session.New(params);
      ```

      ```php PHP theme={null}
        $stripe->checkout->sessions->create([
          'success_url' => 'https://example.com/success',
          'line_items' => [
            [
              'price' => 'price_xxxxxxxxxxxxxxxx',
              'quantity' => 2,
            ],
          ],
          'mode' => 'payment',
          'client_reference_id' => "dub_id_xxxxxxxxxxxxxx",
        ]);
      ```

      ```ruby Ruby theme={null}
        Stripe::Checkout::Session.create({
          success_url: 'https://example.com/success',
          line_items: [
            {
              price: 'price_xxxxxxxxxxxxxxxx',
              quantity: 2,
            },
          ],
          mode: 'payment',
          client_reference_id: "dub_id_xxxxxxxxxxxxxx",
        })
      ```
    </CodeGroup>
  </Accordion>
</AccordionGroup>

### Option 2: Using Stripe Checkout (recommended)

If you have a custom checkout flow that uses Stripe's `checkout.sessions.create` API, you'd want to associate the [Stripe customer object](https://docs.stripe.com/api/customers/object) with the user's unique ID in your database (which we tracked in the [lead conversion tracking step](/conversions/leads/introduction)).

This will allow Dub to automatically listen for purchase events from Stripe and associate them with the original click event (and by extension, the link that the user came from).

<Accordion title="How does this work?">
  Remember in the [lead conversion tracking guide](/conversions/leads/introduction), we passed the user's unique user ID along with the click event ID in the `dub.track.lead` call?

  ```javascript Node.js theme={null}
  await dub.track.lead({
    clickId,
    eventName: "Sign Up",
    customerExternalId: user.id, // the unique user ID of the customer in your database
    customerName: user.name,
    customerEmail: user.email,
    customerAvatar: user.image,
  });
  ```

  Under the hood, Dub records the user as a customer and associates them with the click event that they came from.

  Then, when the user makes a purchase, Dub will automatically associate the checkout session details (invoice amount, currency, etc.) with the customer – and by extension, the original click event.
</Accordion>

First, you'll need to complete the following prerequisites:

1. [Install the Dub Stripe integration](#installing-the-dub-stripe-integration)
2. [Enable conversion tracking for your links](/conversions/quickstart#step-1%3A-enable-conversion-tracking-for-your-links)
3. [Install the @dub/analytics client-side SDK](/sdks/client-side/introduction)
4. [Install the Dub server-side SDK](/sdks/overview#server-side-sdks)

Then, when you [create a checkout session](https://docs.stripe.com/api/checkout/sessions/create), pass your customer's unique user ID in your database as the `dubCustomerExternalId` value in the `metadata` field.

```javascript Node.js theme={null}
import { stripe } from "@/lib/stripe";

const user = {
  id: "user_123",
  email: "user@example.com",
  teamId: "team_xxxxxxxxx",
};

const priceId = "price_xxxxxxxxx";

const stripeSession = await stripe.checkout.sessions.create({
  customer_email: user.email,
  success_url: "https://app.domain.com/success",
  line_items: [{ price: priceId, quantity: 1 }],
  mode: "subscription",
  client_reference_id: user.teamId,
  metadata: {
    dubCustomerExternalId: user.id, // the unique user ID of the customer in your database
  },
});
```

This way, when the customer completes their checkout session, Dub will automatically associate the checkout session details (invoice amount, currency, etc.) with the customer – and by extension, the original click event.

<Warning>
  If you're using [guest checkout](https://docs.stripe.com/payments/checkout/guest-customers) (e.g. with `mode: "payment"`), the `customer` field in the `checkout.session.completed` webhook event will be `null`, and sales won't be tracked on Dub.

  To fix this, set `customer_creation` to `always` when [creating your checkout session](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer_creation):

  ```javascript Node.js theme={null}
  const stripeSession = await stripe.checkout.sessions.create({
    // ... other options
    customer_creation: "always", // ensures a Stripe customer is created
  });
  ```
</Warning>

### Option 3: Using Stripe Customers

<Note>
  When using Stripe Customers, lead and sale events are tracked but [lead
  rewards](https://dub.co/help/article/partner-rewards#configuring-reward-types)
  will not be generated.
</Note>

Alternatively, if you don't use Stripe's [checkout session creation flow](#option-2%3A-using-stripe-checkout-recommended), you can also pass the user ID and the click event ID (`dub_id`) in the [Stripe customer creation flow](https://docs.stripe.com/api/customers/create).

First, you'll need to complete the following prerequisites:

1. [Install the Dub Stripe integration](#installing-the-dub-stripe-integration)
2. [Enable conversion tracking for your links](/conversions/quickstart#step-1%3A-enable-conversion-tracking-for-your-links)
3. [Install the @dub/analytics client-side SDK](/sdks/client-side/introduction)

Then, when you [create a Stripe customer](https://docs.stripe.com/api/customers/create), pass the user's unique user ID in your database as the `dubCustomerExternalId` value in the `metadata` field.

```javascript Node.js theme={null}
import { stripe } from "@/lib/stripe";

const user = {
  id: "user_123",
  email: "user@example.com",
  teamId: "team_xxxxxxxxx",
};

const dub_id = req.headers.get("dub_id");

await stripe.customers.create({
  email: user.email,
  name: user.name,
  metadata: {
    dubCustomerExternalId: user.id,
    dubClickId: dub_id,
  },
});
```

Alternatively, you can also pass the `dubCustomerExternalId` and `dubClickId` values in the `metadata` field of the [Stripe customer update flow](https://docs.stripe.com/api/customers/update):

```javascript Node.js theme={null}
import { stripe } from "@/lib/stripe";

const user = {
  id: "user_123",
  email: "user@example.com",
  teamId: "team_xxxxxxxxx",
};

const dub_id = req.headers.get("dub_id");

await stripe.customers.update(user.id, {
  metadata: {
    dubCustomerExternalId: user.id,
    dubClickId: dub_id,
  },
});
```

This way, when the customer makes a purchase, Dub will automatically associate the purchase details (invoice amount, currency, etc.) with the original click event.

## Tracking free trials

Dub supports tracking [subscription free trials](https://docs.stripe.com/billing/subscriptions/trials) as lead events on Dub. This is useful for products with free trials since you might want to track trial activations as part of your attribution flow.

To enable free trial tracking, go to your Stripe integration settings and enable the **Track Free Trials** option:

<Frame>
  <img src="https://mintcdn.com/dub/6rN5iSUCyHVhamFj/images/stripe/stripe-integration-settings.png?fit=max&auto=format&n=6rN5iSUCyHVhamFj&q=85&s=72035e5a76c4cf39cfb163b3ebb80846" alt="The Stripe integration settings page" data-og-width="1556" width="1556" data-og-height="774" height="774" data-path="images/stripe/stripe-integration-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/6rN5iSUCyHVhamFj/images/stripe/stripe-integration-settings.png?w=280&fit=max&auto=format&n=6rN5iSUCyHVhamFj&q=85&s=aac17b1763b88ade48e5379b7f3b8a1f 280w, https://mintcdn.com/dub/6rN5iSUCyHVhamFj/images/stripe/stripe-integration-settings.png?w=560&fit=max&auto=format&n=6rN5iSUCyHVhamFj&q=85&s=7fab354db3a790489feabfab2b7022e1 560w, https://mintcdn.com/dub/6rN5iSUCyHVhamFj/images/stripe/stripe-integration-settings.png?w=840&fit=max&auto=format&n=6rN5iSUCyHVhamFj&q=85&s=7613cb6507fdfba39bc99a064ddc3036 840w, https://mintcdn.com/dub/6rN5iSUCyHVhamFj/images/stripe/stripe-integration-settings.png?w=1100&fit=max&auto=format&n=6rN5iSUCyHVhamFj&q=85&s=e2ee07c452f809d5c7120be76de4e2a4 1100w, https://mintcdn.com/dub/6rN5iSUCyHVhamFj/images/stripe/stripe-integration-settings.png?w=1650&fit=max&auto=format&n=6rN5iSUCyHVhamFj&q=85&s=d4ecc21e01625138d4e727fe6a955904 1650w, https://mintcdn.com/dub/6rN5iSUCyHVhamFj/images/stripe/stripe-integration-settings.png?w=2500&fit=max&auto=format&n=6rN5iSUCyHVhamFj&q=85&s=5e8ec24f5bbfaa85f4d92cb2a87ca329 2500w" />
</Frame>

Optionally, you can also configure the integration to track the [provisioned quantity](https://docs.stripe.com/billing/subscriptions/quantities) in the subscription as separate lead events.

This is useful if you have a [lead-based reward](https://dub.co/help/article/partner-rewards#configuring-reward-types) for your [partner program](https://dub.co/partners) and want to reward partners for each unit of the subscription that their customers purchase (e.g. \$50 per lead/provisioned seat).

<Tip>
  To differentiate between [manually tracked lead events](/conversions/leads/introduction) and free trial lead events for lead reward types, use the `Customer` `Source` [reward condition](https://dub.co/help/article/partner-rewards#adding-reward-conditions) to filter for `free trial` lead events:

  <Frame>
    <img src="https://mintcdn.com/dub/6rN5iSUCyHVhamFj/images/stripe/lead-reward-free-trials.png?fit=max&auto=format&n=6rN5iSUCyHVhamFj&q=85&s=5b82fa83f75ea165b0b1c6ca726b8c4b" alt="The lead reward free trial condition" data-og-width="2014" width="2014" data-og-height="1158" height="1158" data-path="images/stripe/lead-reward-free-trials.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/6rN5iSUCyHVhamFj/images/stripe/lead-reward-free-trials.png?w=280&fit=max&auto=format&n=6rN5iSUCyHVhamFj&q=85&s=99e7162d36299682fc350753b3ed80ff 280w, https://mintcdn.com/dub/6rN5iSUCyHVhamFj/images/stripe/lead-reward-free-trials.png?w=560&fit=max&auto=format&n=6rN5iSUCyHVhamFj&q=85&s=973a8325bce280637d6d1a6972e8ff23 560w, https://mintcdn.com/dub/6rN5iSUCyHVhamFj/images/stripe/lead-reward-free-trials.png?w=840&fit=max&auto=format&n=6rN5iSUCyHVhamFj&q=85&s=8ca2781234118978c340926abf56178f 840w, https://mintcdn.com/dub/6rN5iSUCyHVhamFj/images/stripe/lead-reward-free-trials.png?w=1100&fit=max&auto=format&n=6rN5iSUCyHVhamFj&q=85&s=936940d37370a6bb414d5a1522875295 1100w, https://mintcdn.com/dub/6rN5iSUCyHVhamFj/images/stripe/lead-reward-free-trials.png?w=1650&fit=max&auto=format&n=6rN5iSUCyHVhamFj&q=85&s=3cc7cd833cb27e20d5f34c41c9626057 1650w, https://mintcdn.com/dub/6rN5iSUCyHVhamFj/images/stripe/lead-reward-free-trials.png?w=2500&fit=max&auto=format&n=6rN5iSUCyHVhamFj&q=85&s=9856dc3d61ab6cbd09644e8a12dc3999 2500w" />
  </Frame>
</Tip>

## Currency conversion support

If you're using [Stripe's Adaptive Pricing](https://docs.stripe.com/payments/checkout/adaptive-pricing) feature, Dub will record the sale amount using the currency of your Stripe account:

```json checkout.session.completed theme={null}
// Stripe checkout.session.completed event payload
{
  "id": "{{EVENT_ID}}",
  "object": "event",
  "type": "checkout.session.completed",
  "data": {
    "object": {
      "id": "{{SESSION_ID}}",
      "object": "checkout.session",
      "currency": "cad",
      "amount_subtotal": 2055,
      "amount_total": 2055,
      "currency_conversion": {
        "amount_subtotal": 1500,
        "amount_total": 1500, // this is the amount that Dub will record
        "source_currency": "usd", // the currency of your Stripe account
        "fx_rate": "1.37"
      }
    }
  }
}
```

If you're not using Stripe Adaptive Pricing, Dub will record the sale amount in the default currency of your Dub workspace. This means that if you pass a different currency, it will be automatically converted to USD for reporting consistency – using the latest foreign exchange rates.

```json checkout.session.completed theme={null}
// Stripe checkout.session.completed event payload
{
  "id": "{{EVENT_ID}}",
  "object": "event",
  "type": "checkout.session.completed",
  "data": {
    "object": {
      "id": "{{SESSION_ID}}",
      "object": "checkout.session",
      "currency": "cad",
      "amount_subtotal": 2055,
      "amount_total": 2055 // this will be converted from CAD to USD
    }
  }
}
```

<Note>
  The default currency for all Dub workspaces is currently set to `USD`. We will
  add the ability to customize that in the future.
</Note>

## Tax handling

When tracking sale conversions from Stripe, Dub automatically excludes taxes from the final sale amount to ensure accurate revenue reporting.

For **checkout sessions**, Dub calculates the sale amount by subtracting the tax amount from the total:

```javascript  theme={null}
// Sale amount calculation for checkout sessions
saleAmount = amount_total - total_details.amount_tax;
```

For **invoices**, Dub uses the `total_excluding_tax` field when available:

```javascript  theme={null}
// Sale amount calculation for invoices
saleAmount = total_excluding_tax ?? amount_paid;
```

This ensures that the sale amounts recorded in Dub reflect the actual revenue before taxes, providing more accurate metrics for:

* Revenue tracking and reporting
* Partner commission calculations
* Analytics and conversion metrics

<Note>
  Tax amounts are automatically excluded from all sale events tracked through
  the Stripe integration, including one-time purchases, subscriptions, and
  recurring invoices.
</Note>

## View conversion results

And that's it – you're all set! You can now sit back, relax, and watch your conversion revenue grow. We provide 3 different views to help you understand your conversions:

* **Time-series**: A [time-series view](https://app.dub.co/dub/analytics?view=timeseries) of the number clicks, leads and sales.

<Frame>
  <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=7380bc6120ade538b2b65eefdc76d3ed" alt="Time-series line chart" data-og-width="2400" width="2400" data-og-height="1260" height="1260" data-path="images/conversions/timeseries-chart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=430758e529cd22c5d28f976ee7da5379 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=9cf861c9aa7cf680f46ce32585303d2b 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=999b05a7805bd208b4649fc67a3b45e0 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=42baa1d9d42c26ed191875fef033128a 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=127ee673f66f2079f236985ec754416e 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=1c0696bb18043dd86388f03d09aed450 2500w" />
</Frame>

* **Funnel chart**: A [funnel chart view](http://app.dub.co/analytics?view=funnel) visualizing the conversion & dropoff rates across the different steps in the conversion funnel (clicks → leads → sales).

<Frame>
  <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=6275caafcfc3be6d8b498149222f225e" alt="Funnel chart view showing the conversion & dropoff rates from clicks → leads → sales" data-og-width="2400" width="2400" data-og-height="1260" height="1260" data-path="images/conversions/funnel-chart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=df57b14d04dd585c5236f6fcf16a4963 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=fc1689a06ce8ceecf1487faca8730d06 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=b69533d460a2bc95964d7f6d2e5f23f4 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=43b86431662a4c214a36fbf5405abb4a 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=687f900f0b8732301c43c8ee18ca7dd4 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=aed9e63c7fd1fb67c463920c73911cba 2500w" />
</Frame>

* **Real-time events stream**: A [real-time events stream](https://app.dub.co/events) of every single conversion event that occurs across all your links in your workspace.

<Frame>
  <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=c2467f9fa2e755f06b3e7b147fa0bd81" alt="The Events Stream dashboard on Dub" data-og-width="2400" width="2400" data-og-height="1260" height="1260" data-path="images/conversions/events-table.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=8e747ccc2f01015e014a9b4fbc98d588 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=4a0c65b37cf99181b712beb063e46dc2 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=345d5b0b36c6f2093ea7b6a97d73ff49 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=5deb48ab5e08bf2e31447fd32615c05e 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=33d6f27b5c067eb8586cfea15fe0a040 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=132a7592c8ecf518b31c043dad2093f4 2500w" />
</Frame>

## Example Apps

<CardGroup cols={2}>
  <Card title="Dub + Stripe Demo App" icon="github" href="https://github.com/dubinc/examples/tree/main/conversions/stripe" color="#333333">
    See the full example on GitHub.
  </Card>
</CardGroup>
