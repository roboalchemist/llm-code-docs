# Source: https://docs.firehydrant.com/docs/honeycomb-integration.md

# Honeycomb

Honeycomb provides observability monitoring for your cloud infrastructure. Use alerts from Honeycomb to power incidents and notifications in FireHydrant.

> 🚧 Honeycomb and Signals
>
> If you're looking to connect Honeycomb to FireHydrant to create alerts in Signals, checkout the Signals Integration guide for [Honeycomb](https://docs.firehydrant.com/docs/honeycomb-integration). This document describes setting up the integration for Alert Routing, which does not connect to FireHydrant's Signals system.

## Configuration steps

### 1. Install integration on FireHydrant

1. Authorize the Honeycomb integration on [FireHydrant's integrations page](https://app.firehydrant.io/organizations/integrations)
2. Once you click **Authorize Application**, you'll see a webhook URL provided

### 2. Add trigger to Honeycomb

1. Navigate to the **Integrations** section of your Team Settings page within Honeycomb
2. Click **Add Recipient** under **Trigger Recipients**
3. Select **Webhook**, give it a name and paste the webhook url supplied on this page

### 3. Set up Trigger

1. Navigate to the new Trigger page
2. Add the Honeycomb query you'd like to alert on. Set Threshold, Duration and Frequency according to your alert's needs
3. Click **Add Recipient**, and set the recipient to the one added previously

### 4. Test the Webhook

1. Find the trigger you created earlier in step in the Triggers list.
2. Click **Test** on the line with your Trigger and confirm to launch the test.
3. Confirm that the webhook successfully reaches FireHydrant in the logs below.

## Next Steps

Setup Alert Routes. For any Honeycomb alerts that come into FireHydrant, configure alert routing to open incidents, send Slack messages, and more automatically. Learn more by visiting [Alert Routing](https://docs.firehydrant.com/docs/alert-routing).