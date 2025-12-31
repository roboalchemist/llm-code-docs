# Source: https://getlago.com/docs/integrations/payments/moneyhash-integration.md

# Moneyhash

> Moneyhash is a leading payment infrastructure software in Africa and the Middle East.

<Info>
  This integration is community-maintained, and therefore Lago provides only limited support.
</Info>

## About Moneyhash

Moneyhash is a leading payment infrastructure software in Africa and the Middle East.
They help businesses across Emerging Markets to optimize payment performance, scale operations, cut costs, and grow revenue through their all-in-one orchestration platform.

## Connect Moneyhash to Lago

To connect Moneyhash to Lago, navigate to your Lago UI, then go to **Integrations** > **Built by community**, and add a new **Moneyhash Payments** connection:

1. Click **Add a connection**;
2. Type a connection **name**;
3. Type a unique connection **code**;
4. Paste your Moneyhash **API key**; and
5. Paste your Moneyhash **Flow Id**.

<Frame caption="Connect your Moneyhash account from Lago UI">
  <img src="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/moneyhash-payment-integration.png?fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=cf1438ccc954a9c2929c0fd24d77884e" data-og-width="2692" width="2692" data-og-height="1430" height="1430" data-path="integrations/images/moneyhash-payment-integration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/moneyhash-payment-integration.png?w=280&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=e3b738187f5a01cc034063f1bf5c114e 280w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/moneyhash-payment-integration.png?w=560&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=b19c3c25148143c10db151f237bb94a5 560w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/moneyhash-payment-integration.png?w=840&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=2f6d5849ac102d1230c32a96ea30361c 840w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/moneyhash-payment-integration.png?w=1100&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=4a2f79a15547174bccf6955a1929b853 1100w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/moneyhash-payment-integration.png?w=1650&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=989308cab8b9eba8a17934f98585a855 1650w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/moneyhash-payment-integration.png?w=2500&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=5df8dad7ac29f56553816e464e1c8ff4 2500w" />
</Frame>

## Create a webhook endpoint

<Tip>
  To complete this process, you will need:

  * Your Lago **organization ID**, available in the **"API keys & ID"** tab of the
    **"Developers"** section;
  * The **connection code** you created during the Moneyhash setup process.
</Tip>

If you want Lago to automatically retrieve the status of the payments processed
via Moneyhash, you must create a webhook endpoint in Moneyhash. To do so:

1. Log in to your Moneyhash account;
2. Add the following Webhook URL in the **Webhooks** section of the Moneyhash dashboard;
3. Enter the following URL: `https://api.getlago.com/webhooks/moneyhash/{{__YOUR_ORG_ID__}}?code={{__YOUR_CONNECTION_CODE}}` (you must replace `organization_id` with your Lago organization ID, and the `connection_code` by the targeted Lago connection); and
4. Save the creation of this webhook endpoint.

## Collect payments via Moneyhash

### Connect a Lago Customer to Moneyhash

To begin collecting payments for your Lago invoices via Moneyhash, you need to link a Lago customer to a Moneyhash connection.
When creating or editing a customer in Lago, simply select the relevant Moneyhash connection under **external apps** to enable invoice payments.

### Generate a checkout link

Note that payments through Moneyhash does not automatically proceed when Lago generates an invoice. You need to programmatically generate a checkout link by calling the [following endpoint](/api-reference/invoices/payment-url):

```bash Request theme={"dark"}
curl --request POST \
  --url https://api.getlago.com/api/v1/invoices/{lago_id}/payment_url \
  --header 'Authorization: Bearer <token>'
```

By generating this checkout link, you can forward it to your customer to complete payment using their preferred method from India. Once the payment is processed, Lago automatically retrieves the invoice status from Moneyhash.

```json Response theme={"dark"}
{
  "invoice_payment_details": {
    "lago_customer_id": "13b901a90-1a90-1a90-1a90-1a901a901a90",
    "lago_invoice_id": "1e501a90-938s-1a90-1a90-1a901a901a80",
    "external_customer_id": "53dj371e-4ea2-bcf9-57d3a41bc6ba",
    "payment_provider": "moneyhash",
    "payment_url": "https://moneyhash.payment_link"
  }
}
```

### Moneyhash payment errors

If an error occurs during the Moneyhash payment process for a Lago invoice, Lago sends a [`payment_request.payment_failure`](https://docs.getlago.com/api-reference/webhooks/messages#param-payment-request-payment-failure) webhook containing the error details.
