# Source: https://documentation.onesignal.com/docs/en/sending-whatsapp-messages-via-journey-webhooks.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Send WhatsApp Messages via Journey Webhooks

> Send WhatsApp messages automatically using OneSignal Journeys and webhooks.

## Requirements

* Paid plan that supports both Journeys and Webhooks
* [WhatsApp Business Platform](https://developers.facebook.com/docs/whatsapp/) + [Webhooks Setup](https://developers.facebook.com/docs/whatsapp/business-management-api/guides/set-up-webhooks/)
* WhatsApp recipients

<Info>
  While the following guide uses the Facebook/Meta API, Twilio can also be used to Post WhatsApp messages.
</Info>

## Setup

### 1. Import recipients phone numbers

WhatsApp supporting numbers should be uploaded as a data tag to a User.

**Here's an example:**

<Frame caption="WhatsApp phone number data tag example">
  <img src="https://mintcdn.com/onesignal/6tscVAtiSqz353kV/images/docs/9d6d60f-Screenshot_2023-12-11_at_4.18.55_PM.png?fit=max&auto=format&n=6tscVAtiSqz353kV&q=85&s=7da1071cc2d4d5d0532b5421e30fc037" width="1478" height="127" data-path="images/docs/9d6d60f-Screenshot_2023-12-11_at_4.18.55_PM.png" />
</Frame>

<Warning>
  Please add numbers in the E.164 format, but without the + sign. The number +16463938787 should be added as 16463938787.
</Warning>

### 2. Obtain Webhook code

Once you have created your Meta/Facebook Business account and have activated your WhatsApp Module, you'll be given an API access token.

You'll be able to find this information under WhatsApp -> API Setup

<Frame caption="WhatsApp API setup credentials screen">
  <img src="https://mintcdn.com/onesignal/MUgio66t0sYhGEvj/images/docs/6accf9b-Screenshot_2023-12-11_at_4.20.11_PM.png?fit=max&auto=format&n=MUgio66t0sYhGEvj&q=85&s=80c1e9b33b021e551a495009e18bb473" width="1438" height="496" data-path="images/docs/6accf9b-Screenshot_2023-12-11_at_4.20.11_PM.png" />
</Frame>

### 3. Create a Webhook Template

* Within OneSignal, click on: **Data > Webhooks > New Webhook**
* Copy over the credentials. It should look like this:

<Frame caption="WhatsApp webhook configuration template">
  <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/d9e43cc-Screenshot_2023-12-11_at_4.20.49_PM.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=7fb711e8ee8dc46c0338adb7562ee75a" width="1470" height="1019" data-path="images/docs/d9e43cc-Screenshot_2023-12-11_at_4.20.49_PM.png" />
</Frame>

<Warning>
  `{{user.tags.WhatsApp_number}}` tag key is added as the "to" number as highlighted above.
</Warning>

### 4. Create a Journey

You can now create your Journey and add your new WhatsApp Webhook.

<Frame caption="WhatsApp webhook selection">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/journeys/whatsapp-webhook-selection.gif?s=bebc2ab65e99877c31e22eda7bff8080" width="600" height="319" data-path="images/journeys/whatsapp-webhook-selection.gif" />
</Frame>

When testing, please make sure of the following:

* The subscription id in which you have added the WhatsApp number has an external id
* The subscription id matches the Journey included segment(s)

***

Built with [Mintlify](https://mintlify.com).
