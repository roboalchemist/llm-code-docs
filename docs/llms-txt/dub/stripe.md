# Source: https://dub.co/docs/conversions/sales/stripe.md

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
      <img src="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-marketplace.png?fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=e7cce5cca6ef3da4612678c1ea1b4171" alt="The Dub integration page on the Stripe App Marketplace" data-og-width="1340" width="1340" data-og-height="993" height="993" data-path="images/stripe/stripe-app-marketplace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-marketplace.png?w=280&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=7f2636abdc3b10e9e1fc9e39cf4fa4ee 280w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-marketplace.png?w=560&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=205db0d24d21987178fd6d8e0e8bffae 560w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-marketplace.png?w=840&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=84fb60be555a40840186e8fa9e51c357 840w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-marketplace.png?w=1100&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=d566c4c6a61de3c33fec1bb9c1cbe860 1100w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-marketplace.png?w=1650&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=13094b4ce82c3dd3374b4a4896416034 1650w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-marketplace.png?w=2500&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=1306cc653c2d9b795c39f1edca32964f 2500w" />
    </Frame>
  </Step>

  <Step title="Install the Stripe app">
    On the top right, click on **Install app** to install the Dub app on your Stripe account.

    <Frame>
      <img src="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-install.png?fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=e80d6bf163cc6d2516997dca0557c776" alt="The Stripe integration installation flow" data-og-width="1325" width="1325" data-og-height="964" height="964" data-path="images/stripe/stripe-app-install.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-install.png?w=280&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=93181a1a975aec3403291374209ed785 280w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-install.png?w=560&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=64cfc0d3d2bc7916c46fd30d33a5bc10 560w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-install.png?w=840&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=fb76783214e1b02a6f968a5035770b14 840w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-install.png?w=1100&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=709dba497ab89b9390805cce8c4e1982 1100w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-install.png?w=1650&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=a6f7170dca388594f6418c6ce0cd334e 1650w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-install.png?w=2500&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=99f0dd9b1f951948c4aecb786c1bce1f 2500w" />
    </Frame>

    <Tip>
      Alternatively, you can also install the Stripe app in a [Stripe sandbox](https://docs.stripe.com/sandboxes) first to test
      your end-to-end flow without involving real money.
    </Tip>

    Once the app is installed, click on **Continue to app settings** to finish the installation.

    <Frame>
      <img src="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-install-continue.png?fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=02df497eb3dce3cc474865305f727652" alt="Continue to app settings" data-og-width="1264" width="1264" data-og-height="855" height="855" data-path="images/stripe/stripe-app-install-continue.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-install-continue.png?w=280&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=3a9b16306215e3054a3c433ffe744dd2 280w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-install-continue.png?w=560&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=26eae0ab46c075d5e6a9bc2a0a84cfa3 560w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-install-continue.png?w=840&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=db4ed3ce4dfd87a56e4ae26300289ebb 840w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-install-continue.png?w=1100&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=647202cdab9fc3b1d2242394cbe9c033 1100w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-install-continue.png?w=1650&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=ff35f11d9cd7006160b9e820a7174047 1650w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-install-continue.png?w=2500&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=a69b1fcc97665ea903ae4f75caf0dd78 2500w" />
    </Frame>
  </Step>

  <Step title="Connect Stripe to your Dub workspace">
    In the app settings page, click on **Connect workspace** to connect your Stripe account with your Dub workspace.

    <Frame>
      <img src="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-connect-workspace.png?fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=e2a8612e59068a456bcbb8873d7b9a0d" alt="Connect Stripe to Dub" data-og-width="1712" width="1712" data-og-height="845" height="845" data-path="images/stripe/stripe-app-connect-workspace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-connect-workspace.png?w=280&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=156067c801c43c268b49cc58a17c24e9 280w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-connect-workspace.png?w=560&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=6a74dcebd4ffeadbefd352666c547973 560w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-connect-workspace.png?w=840&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=379e1750ddc85fe46c5b66c68a328c31 840w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-connect-workspace.png?w=1100&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=46e7913f145fb710546e4f3457fde4ed 1100w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-connect-workspace.png?w=1650&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=bdfbf2b8a9f73a448395001bb8b1875e 1650w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-connect-workspace.png?w=2500&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=a8c4c559547d0f2a3f97bb5116b14e9e 2500w" />
    </Frame>

    This will redirect you to the [Dub OAuth flow](/integrations/quickstart), where you can select the Dub workspace you want to connect to your Stripe account.

    <Frame>
      <img src="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/select-dub-workspace.png?fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=507a2f6a329b10b0f3362fed30b45a09" alt="Select the Dub workspace you want to connect to your Stripe account" data-og-width="1084" width="1084" data-og-height="771" height="771" data-path="images/stripe/select-dub-workspace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/select-dub-workspace.png?w=280&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=ea14fdaffbec53a73ec97f1709266102 280w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/select-dub-workspace.png?w=560&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=1df2007387e1be63e6995db483dc8258 560w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/select-dub-workspace.png?w=840&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=d60eff5c7e4412135145ec9289ac405d 840w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/select-dub-workspace.png?w=1100&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=b4d52c066cea9eb96bc525eca0726d47 1100w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/select-dub-workspace.png?w=1650&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=f19c67d0498a229868f159678b35594e 1650w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/select-dub-workspace.png?w=2500&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=a1fb74026172f2906ddf1b859c187bf3 2500w" />
    </Frame>

    Once you click on **Authorize**, you will be redirected back to the Dub app settings page on Stripe, where you should see that the integration is now installed.

    <Frame>
      <img src="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-installed.png?fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=f51caac85233a51918084c10962a4f33" alt="The Stripe integration is now installed" data-og-width="1057" width="1057" data-og-height="558" height="558" data-path="images/stripe/stripe-app-installed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-installed.png?w=280&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=00c157698e1348fff6ceb734bdca8df6 280w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-installed.png?w=560&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=62dec831f32d81857bebd303b4468319 560w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-installed.png?w=840&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=5b6bd7596a3c48e274b4c47ba228b075 840w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-installed.png?w=1100&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=7d9d59cf969f93994a77054ff4093c54 1100w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-installed.png?w=1650&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=3e25e3100d51970498cebe3e7a6e39b9 1650w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/stripe/stripe-app-installed.png?w=2500&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=bbeb91808eb821ca8d3e5a098b93f9ea 2500w" />
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
  When using Stripe Payment Links, lead webhooks and [lead rewards](https://dub.co/help/article/partner-rewards#configuring-reward-types) are not created. Only sale events will be tracked.
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

Then, when you [create a checkout session](https://docs.stripe.com/api/checkout/sessions/create), pass your customer's unique user ID in your database as the `dubCustomerId` value in the `metadata` field.

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
    dubCustomerId: user.id, // the unique user ID of the customer in your database
  },
});
```

This way, when the customer completes their checkout session, Dub will automatically associate the checkout session details (invoice amount, currency, etc.) with the customer – and by extension, the original click event.

### Option 3: Using Stripe Customers

Alternatively, if you don't use Stripe's [checkout session creation flow](#option-2%3A-using-stripe-checkout-recommended), you can also pass the user ID and the click event ID (`dub_id`) in the [Stripe customer creation flow](https://docs.stripe.com/api/customers/create).

First, you'll need to complete the following prerequisites:

1. [Install the Dub Stripe integration](#installing-the-dub-stripe-integration)
2. [Enable conversion tracking for your links](/conversions/quickstart#step-1%3A-enable-conversion-tracking-for-your-links)
3. [Install the @dub/analytics client-side SDK](/sdks/client-side/introduction)

Then, when you [create a Stripe customer](https://docs.stripe.com/api/customers/create), pass the user's unique user ID in your database as the `dubCustomerId` value in the `metadata` field.

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
    dubCustomerId: user.id,
    dubClickId: dub_id,
  },
});
```

Alternatively, you can also pass the `dubCustomerId` and `dubClickId` values in the `metadata` field of the [Stripe customer update flow](https://docs.stripe.com/api/customers/update):

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
    dubCustomerId: user.id,
    dubClickId: dub_id,
  },
});
```

This way, when the customer makes a purchase, Dub will automatically associate the purchase details (invoice amount, currency, etc.) with the original click event.

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
saleAmount = amount_total - total_details.amount_tax
```

For **invoices**, Dub uses the `total_excluding_tax` field when available:

```javascript  theme={null}
// Sale amount calculation for invoices
saleAmount = total_excluding_tax ?? amount_paid
```

This ensures that the sale amounts recorded in Dub reflect the actual revenue before taxes, providing more accurate metrics for:

* Revenue tracking and reporting
* Partner commission calculations
* Analytics and conversion metrics

<Note>
  Tax amounts are automatically excluded from all sale events tracked through the Stripe integration, including one-time purchases, subscriptions, and recurring invoices.
</Note>

## Free trials and \$0 sales

Dub does not track free trials or \$0 sale events from Stripe. This means:

* Checkout sessions with `amount_total` of `0` will not be recorded as sale events
* Invoices with `amount_paid` of `0` will not be tracked
* Free trial periods will not generate sale events until the first paid invoice

Sale events will only be tracked when actual revenue is generated (i.e., when the customer is charged a non-zero amount).

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
