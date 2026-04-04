# Source: https://getlago.com/docs/integrations/payments/cashfree-integration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Cashfree Payments

> Make your users pay Lago invoices with Cashfree Payments, India's leading payments and API banking company.

<Info>
  This integration is community-maintained, and therefore Lago provides only limited support.
</Info>

## Payments in India

Cashfree is a leading payment platform in India, offering an end-to-end suite of payment and payout products tailored to the country's needs.
Its extensive coverage of payment methods—including credit/debit cards, net banking, UPI, and popular wallets like Paytm, PhonePe, and Amazon Pay—enables businesses to seamlessly collect payments from Indian customers with minimal friction.
This integration streamlines the collection of Lago invoices in India by leveraging multiple local payment methods.

## Connect Cashfree to Lago

To connect Cashfree to Lago, navigate to your Lago UI, then go to **Integrations** > **Built by community**, and add a new **Cashfree Payments** connection:

1. Click **Add a connection**.
2. Type a connection **name**.
3. Type a unique connection **code**.
4. Paste your Cashfree **Client ID**.
5. Paste your Cashfree **Client Secret**.
6. Provide the **redirect URL** to redirect your users when a payment is processed.

<Frame caption="Connect your Cashfree account from Lago UI">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/cashfree-payment-connection-flow.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=1246341559125631cb74b1ea55bedea3" data-og-width="2938" width="2938" data-og-height="1528" height="1528" data-path="integrations/images/cashfree-payment-connection-flow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/cashfree-payment-connection-flow.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=60f3da9ea560e9044f58e0a82de84997 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/cashfree-payment-connection-flow.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=1e039ffb21e8151d9672b278ea937084 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/cashfree-payment-connection-flow.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=e40bb338e4703ce293224e6466ad3b14 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/cashfree-payment-connection-flow.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=e61c6e97a21a65b6f96ecc084d8d5745 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/cashfree-payment-connection-flow.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=6b24a17e10a5c362ee16c1ffc90c03cb 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/cashfree-payment-connection-flow.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=cb75f920513019154011b5d0c2bfb9d9 2500w" />
</Frame>

## Create a webhook endpoint

<Tip>
  To complete this process, you will need:

  * Your Lago **organization ID**, available in the **"API keys & ID"** tab of the
    **"Developers"** section;
  * The **connection code** you created during the Cashfree setup process.
</Tip>

If you want Lago to automatically retrieve the status of the payments processed
via Cashfree Payments, you must create a webhook endpoint in Cashfree. To do so:

1. Log in to your Cashfree Payments account;
2. Add the following Webhook URL in the **Webhooks** > **Payment Link** section of the Cashfree Payments dashboard;
3. Enter the following URL: `https://api.getlago.com/webhooks/cashfree/{{__YOUR_ORG_ID__}}?code={{__YOUR_CONNECTION_CODE}}` (you must replace `organization_id` with your Lago organization ID, and the `connection_code` by the targeted Lago connection); and
4. Save the creation of this webhook endpoint.

<Frame caption="Webhook endpoint creation in Cashfree Payments">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/cashfree-webhook-connection.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=3b5aef1459bbb62c6616d4e925b98f9a" data-og-width="2904" width="2904" data-og-height="1828" height="1828" data-path="integrations/images/cashfree-webhook-connection.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/cashfree-webhook-connection.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=ce492dbcbdcc40ae9016a1eeaf872d57 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/cashfree-webhook-connection.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=6ca5ac276a2654578065ec835df0b67b 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/cashfree-webhook-connection.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=9c236683e7ae77d86e184ff528d8d5be 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/cashfree-webhook-connection.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=c250eae2a5ed0bc5cc23d23652f5fb41 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/cashfree-webhook-connection.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=ec95b8169f752211b77fb0c567da27e2 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/cashfree-webhook-connection.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=33e411eaa280a54fe4eca8e10773594c 2500w" />
</Frame>

## Collect payments via Cashfree

### Connect a Lago Customer to Cashfree

To begin collecting payments for your Lago invoices via Cashfree, you need to link a Lago customer to a Cashfree connection.
When creating or editing a customer in Lago, simply select the relevant Cashfree connection under **external apps** to enable invoice payments.

<Frame caption="Link Lago Customers to Cashfree Payments">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/cashfree-link-lago-customer.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=175f66a895731fd91ab08d6818c474cf" data-og-width="1307" width="1307" data-og-height="993" height="993" data-path="integrations/images/cashfree-link-lago-customer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/cashfree-link-lago-customer.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=ccd967b9c6c35bb5d6ada5ea46732de3 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/cashfree-link-lago-customer.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=65c9896bd5d3672edc43ea392d5765cf 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/cashfree-link-lago-customer.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=c19942859c2e5458ba98895aa399b62f 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/cashfree-link-lago-customer.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=297fc455ff368a7442cb83e36d9c48e8 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/cashfree-link-lago-customer.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=e09915411cd784719e78dc62f6ccff1e 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/cashfree-link-lago-customer.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=e6334d23518ba84e1d13c1a82dff4590 2500w" />
</Frame>

### Generate a checkout link

Note that payments through Cashfree does not automatically proceed when Lago generates an invoice. You need to programmatically generate a checkout link by calling the [following endpoint](/api-reference/invoices/payment-url):

```bash Request theme={"dark"}
curl --request POST \
  --url https://api.getlago.com/api/v1/invoices/{lago_id}/payment_url \
  --header 'Authorization: Bearer <token>'
```

By generating this checkout link, you can forward it to your customer to complete payment using their preferred method from India. Once the payment is processed, Lago automatically retrieves the invoice status from Cashfree.

```json Response theme={"dark"}
{
  "invoice_payment_details": {
    "lago_customer_id": "13b901a90-1a90-1a90-1a90-1a901a901a90",
    "lago_invoice_id": "1e501a90-938s-1a90-1a90-1a901a901a80",
    "external_customer_id": "53dj371e-4ea2-bcf9-57d3a41bc6ba",
    "payment_provider": "cashfree",
    "payment_url": "https://cashfree.payment_link"
  }
}
```

### Cashfree payment errors

If an error occurs during the Cashfree payment process for a Lago invoice, Lago sends a [`payment_request.payment_failure`](https://docs.getlago.com/api-reference/webhooks/messages#param-payment-request-payment-failure) webhook containing the error details.
