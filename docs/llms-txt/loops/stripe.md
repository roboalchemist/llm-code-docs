# Source: https://loops.so/docs/integrations/stripe.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Stripe

> Sync contacts and send emails triggered by events in Stripe.

<Info>
  Our Stripe integration lets you:

  * Create and update contacts
  * Send events to trigger loops
</Info>

Our Stripe integration is built on top of our [Incoming webhooks](/integrations/incoming-webhooks) feature. This system lets you send webhooks from supported platforms directly to Loops so you can easily sync users and customers as well as send automated emails.

[Please read our guide about incoming webhooks](/integrations/incoming-webhooks)

With Stripe, you can sync user data to Loops for customer and invoice-related events.

## Supported events

We accept the following events:

* `checkout.session.completed`
* `customer.created`
* `customer.deleted`
* `customer.updated`
* `invoice.paid`
* `invoice.payment_failed`
* `invoice.upcoming`

[Stripe webhook docs](https://docs.stripe.com/webhooks)

If you send other events, they will be ignored.

<Info>
  If you would like to see more events supported, please let us know by sending
  an email to [help@loops.so](mailto:help@loops.so). Please keep in mind only
  events that contain an email address are able to be processed.
</Info>

## Synced data

We sync the following Stripe data to your Loops contacts for every incoming event:

* Email address
* First and last name (optional)

We use the email addresses of Stripe customers to match contacts in your Loops audience. If the email address is not found in Loops, we will create a new contact.

The `customer.deleted` event can be used to delete or unsubscribe your Stripe customers from your Loops audience.

## Create a webhook endpoint in Loops

[Follow the instructions here](/integrations/incoming-webhooks#create-webhook-endpoints-in-loops) to create a new webhook endpoint, which will allow you to send webhook events directly to Loops.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=be75ea5d3e49aaa75248d6d157d5780b" alt="Endpoint form" data-og-width="2280" width="2280" data-og-height="1556" height="1556" data-path="images/create-endpoint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=9e0e8289abc76ba6a6eb278ed097a779 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=1f45e6a6c27d3847f4f37cbd47c3aab6 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=b98f9ba7cac487f8e38da5f1fbb328b3 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=2e969b5ad5d478635aa17783cc3b363b 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=2ec8f95dee66d9ddf4ca52460700d87c 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=31ff8ef99563162302b0f8a62985cc2d 2500w" />

## Create a webhook in Stripe

Next, you need to set up webhooks in Stripe.

Go to **Developers** and then **[Webhooks](https://dashboard.stripe.com/webhooks)**.

Click **+ Add endpoint**. Paste in the endpoint URL from Loops, then select the event(s) you want to send (see our [supported events](#supported-events) above).

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/stripe-webhook.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=13fe0fa4248ca24591b1d656c9bd87ac" alt="Adding a webhook in Stripe" data-og-width="2280" width="2280" data-og-height="1635" height="1635" data-path="images/stripe-webhook.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/stripe-webhook.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=b9e84cff33a9480bd677928a5a350d4b 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/stripe-webhook.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=4e400d8367b9352c1f541906ac3a0cbd 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/stripe-webhook.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=85f33d713bb4656340d764ee2163c9c4 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/stripe-webhook.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=dbf3e2c20961ed65a5ad50892cc4a278 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/stripe-webhook.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=96fc2a897418cd28fb0a1e8bb72a7678 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/stripe-webhook.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=283dfa270ae0dea7d066bd295e2422ff 2500w" />

Click **Add endpoint** to finish.

The last step is to copy the signing secret into Loops. On the webhook page in Stripe, click **Reveal** to show the secret in the page. Copy the secret and paste it into the **Signing Secret** field in Loops.

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/stripe-secret.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=f981626e32de38761616f09628885fb0" alt="Reveal Stripe secret" data-og-width="2280" width="2280" data-og-height="795" height="795" data-path="images/stripe-secret.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/stripe-secret.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=4a7cab352f9cb40111122c1be562b95b 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/stripe-secret.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=b2c18a2905b74855bbd9a5d992e10635 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/stripe-secret.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=80eccfcbb6afcb441426fa6de65f2595 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/stripe-secret.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=561e76e18336edf4c0554b120d45ab5b 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/stripe-secret.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=5f6a566520154392cc9b51baa40b70b1 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/stripe-secret.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=ff76530e3f5422d86f88cce135d13085 2500w" />

Now you're all set up.

## Testing Stripe webhooks

You can test a `customer.*` webhook by creating a new customer in the [Customers](https://dashboard.stripe.com/customers) page in Stripe.

You can also use the Stripe CLI tool to mimic events, by using the [`trigger` command](https://docs.stripe.com/cli/trigger).

You can see all sent webhooks by going to **Developers -> Webhooks** and then clicking on an endpoint.

On Loops' end, You will see new contacts appear in your [Audience](https://app.loops.so/audience) page, and triggered events in the [Events](https://app.loops.so/settings?page=events) page.

## Examples

Here are some examples of how you can send data from Stripe to Loops to sync contacts and trigger useful emails to your customers.

### Syncing customers to Loops

Create or update contacts in your Loops audience when a customer is created or updated in Stripe.

1. Create a new Stripe webhook endpoint in Loops ([instructions](/integrations/incoming-webhooks#create-webhook-endpoints-in-loops)).
2. In Stripe, create a new webhook ([instructions above](#create-a-webhook-in-stripe)) for the `customer.created` and `customer.updated` events and paste in your endpoint's URL.
3. In Loops, make sure `customer.created` and `customer.updated` are toggled on on the Stripe settings page.

### Send an email to all new Stripe customers

Send an email from Loops when a new customer is created in Stripe.

1. Create a new loop in Loops using our **Stripe - New Customer** template.
2. For the loop trigger, select **Event received** and enter `newStripeCustomer` (or something similar).
3. Set up your Stripe webhook endpoint in Loops ([instructions](/integrations/incoming-webhooks#create-webhook-endpoints-in-loops)).
4. In Stripe, create a new webhook ([instructions above](#create-a-webhook-in-stripe)) for the `customer.created` event and paste in your endpoint's URL.
5. In Loops, make sure `customer.created` is toggled on, and select the event name you chose in Step 2 from the **Trigger an event** field.

### Send an email to Stripe Checkout customers

Send an email from Loops when a customer pays via Stripe Checkout.

1. Create a new loop in Loops using our **Stripe - Payment Successful** template.
2. For the loop trigger, select **Event received** and enter `stripeCheckout` (or something similar).
3. Set up your Stripe webhook endpoint in Loops ([instructions](/integrations/incoming-webhooks#create-webhook-endpoints-in-loops)).
4. In Stripe, create a new webhook ([instructions above](#create-a-webhook-in-stripe)) for the `checkout.session.completed` event and paste in your endpoint's URL.
5. In Loops, make sure `checkout.session.completed` is toggled on, and select the event name you chose in Step 2 from the **Trigger an event** field.

### Successful payment email

Send an email from Loops when an invoice is paid in Stripe.

1. Create a new loop in Loops using our **Stripe - Payment Successful** template.
2. For the loop trigger, select **Event received** and enter `successfulPayment` (or something similar).
3. Set up your Stripe webhook endpoint in Loops ([instructions](/integrations/incoming-webhooks#create-webhook-endpoints-in-loops)).
4. In Stripe, create a new webhook ([instructions above](#create-a-webhook-in-stripe)) for the `invoice.paid` event and paste in your endpoint's URL.
5. In Loops, make sure `invoice.paid` is toggled on, and select the event name you chose in Step 2 from the **Trigger an event** field.

### Failed payment email

Send an email from Loops when an invoice payment fails in Stripe.

1. Create a new loop in Loops using our **Stripe - Payment Failed** template.
2. For the loop trigger, select **Event received** and enter `failedPayment` (or something similar).
3. Set up your Stripe webhook endpoint in Loops ([instructions](/integrations/incoming-webhooks#create-webhook-endpoints-in-loops)).
4. In Stripe, create a new webhook ([instructions above](#create-a-webhook-in-stripe)) for the `invoice.payment_failed` event and paste in your endpoint's URL.
5. In Loops, make sure `invoice.payment_failed` is toggled on, and select the event name you chose in Step 2 from the **Trigger an event** field.
