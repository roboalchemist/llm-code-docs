# Source: https://ngrok.com/docs/integrations/webhooks/calendly-webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Calendly Webhooks

> Develop and test Calendly webhooks from localhost.

This guide explains how to use ngrok to receive Calendly webhooks on your localhost app.

By integrating ngrok with Calendly, you can:

* Develop and test Calendly webhooks locally without deploying to a public environment or setting up HTTPS.
* Inspect and troubleshoot requests from Calendly in real time via the inspection UI and API.
* Modify and replay Calendly webhook requests with a single click instead of reproducing events manually in your Calendly account.
* Secure your app with Calendly webhook validation provided by ngrok.
  Invalid requests are blocked by ngrok before reaching your app.

## What you'll need

* An [ngrok account](https://ngrok.com/signup) and your [authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).
* The [ngrok agent](https://ngrok.com/download) installed.
* [Node.js](https://nodejs.org/) installed (for the sample app, or use your own app).
* A Calendly account.

## 1. Start your app

For this tutorial, you can use the [sample Node.js app on GitHub](https://github.com/ngrok/ngrok-webhook-nodejs-sample).

To install the sample, run the following in a terminal:

```bash  theme={null}
git clone https://github.com/ngrok/ngrok-webhook-nodejs-sample.git
cd ngrok-webhook-nodejs-sample
npm install
```

Then start the app:

```bash  theme={null}
npm start
```

The app runs on port 3000 by default.

You can confirm it's running by visiting `http://localhost:3000`.
The app logs request headers and body in the terminal and shows a message in the browser.

## 2. Expose your app with ngrok

Once your app is running locally, you're ready to put it online securely using ngrok.

* Copy [your ngrok authtoken](https://dashboard.ngrok.com/get-started/your-authtoken) from the dashboard.

<Tip>
  The ngrok agent uses your authtoken to authenticate when you start a tunnel.
</Tip>

* Start ngrok:

  ```bash  theme={null}
  ngrok http 3000
  ```

* Copy the URL ngrok displays.
  Your app is now exposed at that URL for use with Calendly.

## 3. Configure Calendly to send webhooks

Calendly can send webhook requests to your app when events occur in your account.
To register for those events:

* Sign in to [Calendly](https://calendly.com/).
* On the **My Calendly** page, click **Integrations** in the top menu.
* On the **All integrations** page, click the **API and webhooks** tile and then click **Get a token** under the **Personal access tokens** section.
* On the **Before you begin** popup, click **Continue**, enter a name for the token in the **Choose a name for this token** field, click **Create token**, click **Copy token**, and then click **Close**.
* On the **Your personal access tokens** page, scroll down and click **Copy Key** in the **API Key** section.
* Open a terminal and run the following to get your account info:

  ```bash  theme={null}
  curl --request GET --url https://api.calendly.com/users/me \
  --header 'authorization: Bearer TOKEN'
  ```

  Replace `TOKEN` with the token value you copied.
* Copy the value of the **current\_organization** field and the **uri** field from the response.
* Run the following to register the webhook:

  ```bash  theme={null}
  curl --request POST --url https://api.calendly.com/webhook_subscriptions \
  --header 'Authorization: Bearer TOKEN' \
  --header 'Content-Type: application/json' --data '{
  "url": "URL",
  "events": [
      "invitee.created",
      "invitee.canceled"
  ],
  "organization": "ORGANIZATION_URL",
  "user": "USER_URL",
  "scope": "user",
  "signing_key": "KEY"
  }'
  ```

  Replace `URL` with your ngrok URL (for example, `https://1a2b-3c4d-5e6f-7g8h-9i0j.ngrok.app`), `TOKEN` with the Calendly token, `ORGANIZATION_URL` with the **current\_organization** value, `USER_URL` with the **uri** value, and `KEY` with the key you copied.
* Confirm the response contains a **resource** attribute with the information you provided.

### Run webhooks with Calendly and ngrok

Calendly sends different request body contents depending on the event.
To trigger new calls from Calendly to your app:

* Use your Calendly link to schedule a meeting (for example, click **30 Minutes Meeting**, select a date, and click **Confirm**).

<Note>
  If you don't know your Calendly link, go to [Calendly](https://calendly.com/), click **Account** in the top right, click **Share Your Link**, and copy your link.
</Note>

* On the **Enter Details** page, enter your name and email and click **Schedule Event**.

Confirm your localhost app receives the **invitee.created** event and logs both headers and body in the terminal.

### Inspecting requests

ngrok's [Traffic Inspector](https://dashboard.ngrok.com/traffic-inspector) captures all requests made through your ngrok endpoint to your localhost app.
Select any request to view detailed information about both the request and response.

<Info>
  To avoid exposing secrets, accounts only collect traffic metadata by default.
  You must enable full capture in the Observability section of [your account settings](https://dashboard.ngrok.com/settings) to capture complete request and response data.
</Info>

Use the traffic inspector to:

* Validate webhook payloads and response data
* Debug request headers, methods, and status codes
* Troubleshoot integration issues without adding logging to your app

### Replaying requests

Test your webhook handling code without triggering new events from your service using the Traffic Inspector's replay feature:

1. Send a test webhook from your service to generate traffic in your Traffic Inspector.

2. Select the request you want to replay in the traffic inspector.

3. Choose your replay option:
   * Click **Replay** to send the exact same request again
   * Select **Replay with modifications** to edit the request before sending

4. (Optional) Modify the request: Edit any part of the original request, such as changing field values in the request body.

5. Send the request by clicking **Replay**.

Your local application will receive the replayed request and log the data to the terminal.

## Secure webhook requests

ngrok can verify that incoming requests are from your Calendly webhook so only that traffic reaches your app.

<Note>
  Webhook verification is limited to 500 validations per month on free accounts.
  If you need more, you can upgrade to Hobbyist or Pay-as-you-go.
  See [TPU Pricing](/pricing-limits/traffic-policy-unit-pricing/) for details.
</Note>

To add verification:

* In [Calendly](https://calendly.com/), go to **Integrations**, **API and webhooks**, and copy the **API Key** value (the same value you used to register your webhook).

* Create a Traffic Policy file named `calendly_policy.yml`.
  Replace `{your key}` with the value you copied:

  ```yaml  theme={null}
  on_http_request:
    - actions:
        - type: verify-webhook
          config:
            provider: calendly
            secret: "{your key}"
  ```

* Restart ngrok with the policy file:

  ```bash  theme={null}
  ngrok http 3000 --traffic-policy-file calendly_policy.yml
  ```

* Schedule a meeting from your Calendly link to trigger the webhook.

Your app should receive the request and log it in the terminal.


Built with [Mintlify](https://mintlify.com).