# Source: https://ngrok.com/docs/integrations/webhooks/mailgun-webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Mailgun Webhooks

> Develop and test Mailgun webhooks from localhost.

This guide walks you through using ngrok to receive Mailgun webhooks on your localhost app.

By integrating ngrok with Mailgun, you can:

* Develop and test Mailgun webhooks locally without deploying to a public environment or setting up HTTPS.
* Inspect and troubleshoot requests from Mailgun in real time via the inspection UI and API.
* Modify and replay Mailgun webhook requests with a single click instead of reproducing events manually in your Mailgun account.
* Secure your app with Mailgun webhook validation provided by ngrok.
  Invalid requests are blocked by ngrok before reaching your app.

## What you'll need

* An [ngrok account](https://ngrok.com/signup) and your [authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).
* The [ngrok agent](https://ngrok.com/download) installed.
* [Node.js](https://nodejs.org/) installed (for the sample app, or use your own app).
* A Mailgun account.

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
  Your app is now exposed at that URL for use with Mailgun.

## 3. Configure Mailgun to send webhooks

Mailgun can send webhook requests to your app when events occur in your account.
To register for those events:

* Sign in to [Mailgun](https://app.mailgun.com/).
* Click **Sending**, **Webhooks**, and then **Add webhook**.
* On the **New webhook** popup, select **Delivered Messages** in **Event type**, enter your ngrok URL in **URL** (for example, `https://1a2b-3c4d-5e6f-7g8h-9i0j.ngrok.app`).
* Click **Create webhook**.

To test: on the **Webhooks** page, select **Delivered Messages**, enter your ngrok URL in **URL to test**, and click **Test webhook**.
Confirm your localhost app receives the event and logs both headers and body in the terminal, and that a **Response** appears on the **Webhooks** page.

### Run webhooks with Mailgun and ngrok

Mailgun sends different request body contents depending on the event.
To trigger new calls from Mailgun to your app:

* In the [Mailgun Dashboard](https://app.mailgun.com/), go to **Sending** and **Overview**.
* In **Authorized Recipients**, enter a valid email and click **Save Recipient**.
* Have the recipient confirm by clicking the link in the email from Mailgun.
* Send an email (for example, via the Mailgun API). Replace placeholders with values from your account (**API base URL** and **API Key** from **Overview**, your domain from **Domains**, and the authorized recipient email):

  ```bash  theme={null}
  curl --location --request POST 'API_BASE_URL/messages' \
  --header 'Authorization: Basic api:API_KEY' \
  --form 'from="mailgun@YOUR_DOMAIN"' \
  --form 'to="AUTHORIZED_RECIPIENT"' \
  --form 'subject="Hello from Mailgun"' \
  --form 'text="Testing some Mailgun email!"'
  ```

Confirm your localhost app receives the event and logs both headers and body in the terminal.

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

ngrok can verify that incoming requests are from your Mailgun webhook so only that traffic reaches your app.

<Note>
  Webhook verification is limited to 500 validations per month on free accounts.
  If you need more, you can upgrade to Hobbyist or Pay-as-you-go.
  See [TPU Pricing](/pricing-limits/traffic-policy-unit-pricing/) for details.
</Note>

To add verification:

* In [Mailgun](https://app.mailgun.com/), go to **Sending** and **Webhooks**.

* Click the eye icon next to **HTTP webhook signing key** and copy the value.

* Create a Traffic Policy file named `mailgun_policy.yml`.
  Replace `{webhook signing key}` with the value you copied:

  ```yaml  theme={null}
  on_http_request:
    - actions:
        - type: verify-webhook
          config:
            provider: mailgun
            secret: "{webhook signing key}"
  ```

* Restart ngrok with the policy file:

  ```bash  theme={null}
  ngrok http 3000 --traffic-policy-file mailgun_policy.yml
  ```

* Send a new email to an authorized recipient to trigger the webhook.

Your app should receive the request and log it in the terminal.


Built with [Mintlify](https://mintlify.com).