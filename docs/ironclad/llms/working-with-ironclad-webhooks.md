# Source: https://clickwrap-developer.ironcladapp.com/docs/working-with-ironclad-webhooks.md

# Getting Started with Webhooks

## Learn about webhooks and how events are triggered for your Site

Webhooks allow you to automate custom backend actions and downstream processes in response to acceptances that are logged in Ironclad Clickwrap. As Ironclad Clickwrap is usually integrated into existing customer flows - ie. checkout flows, user signup - we can take advantage of webhooks to ensure this information is passed on to relevant systems.

### Setting up your Ironclad Clickwrap Webhook

Login to your account and navigate to [Settings > Integrations](https://app.pactsafe.com/settings/integrations). If you don't have Integrations enabled in your account, please contact your Implementation Consultant or our Support team at [support@ironcladhq.com](mailto:support@ironcladhq.com) and we'll help you out!

Use the following steps to configure your Ironclad Clickwrap webhook:

1. Click **Add Hook** on the Integrations page.
2. Name your Webhook.
3. Add your webhook endpoint’s URL in **URL**.
4. Set to the **HTTP Method** to GET or POST.
5. Select the [event types](https://clickwrap-developer.ironcladapp.com/docs/webhook-events) you want to receive notifications for.
6. Click **Save**.

<Image title="Screen Shot 2022-11-09 at 5.31.05 PM.png" alt={2432} src="https://files.readme.io/ab36396-Screen_Shot_2022-11-09_at_5.31.05_PM.png">
  A view within the Ironclad Clickwrap Web App of the webhook configuration interface.
</Image>

### URL

In the URL field, define where you want Ironclad Clickwrap to forward events. For testing purposes, you can set up a local webhook host (eg. [ngrok](https://ngrok.com/)).

### HTTP Method

We generally recommend going with POST as some additional data may be passed. We will pass parameters for the Webhook as query string variables in `GET` and a request body with `POST`. The examples for this Guide are `POST`.

### Secret Code

The secret code allows you to create a more secure connection to the Webhook. We'll pass the secret code in an HTTP Header called `Pactsafe-Webhook-Token`. This field is optional and only necessary for an extra level of security and confirmation that the webhook is coming from the Ironclad Clickwrap platform.

### Webhook Event

Select the event that you want to be notified about - [here](https://clickwrap-developer.ironcladapp.com/docs/webhook-events) is an exhaustive list of all available webhooks and example payloads.