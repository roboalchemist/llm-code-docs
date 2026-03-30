# Source: https://ngrok.com/docs/integrations/webhooks/sendgrid-webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SendGrid Webhooks

> Develop and test SendGrid webhooks from localhost.

This guide explains how to use ngrok to receive SendGrid webhooks on your localhost app.

By integrating ngrok with SendGrid, you can:

* Develop and test SendGrid webhooks locally without deploying to a public environment or setting up HTTPS.
* Inspect and troubleshoot requests from SendGrid in real time via the inspection UI and API.
* Modify and replay SendGrid webhook requests with a single click instead of reproducing events manually in your SendGrid account.
* Secure your app with SendGrid webhook validation provided by ngrok.
  Invalid requests are blocked by ngrok before reaching your app.

## What you'll need

* An [ngrok account](https://ngrok.com/signup) and your [authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).
* The [ngrok agent](https://ngrok.com/download) installed.
* [Node.js](https://nodejs.org/) installed (for the sample app, or use your own app).
* A SendGrid account.

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
  Your app is now exposed at that URL for use with SendGrid.

## 3. Configure SendGrid to send webhooks

SendGrid can send webhook requests to your app with information about events as it processes your email.
To register for those events:

* Sign in to the [SendGrid Dashboard](https://app.sendgrid.com/).
* Click **Settings** and **Mail Settings**.
* On **Mail Settings**, click **Event Webhook**.
* In the **Event Webhook** popup, set **Authorization Method** to `None` and enter your ngrok URL in **HTTP Post URL** (for example, `https://1a2b-3c4d-5e6f-7g8h-9i0j.ngrok.app`).
* Click **Test Your Integration** and confirm your localhost app receives the test.
* Under **DELIVERABILITY DATA**, select **Select All**.
* Under **Event Webhook Status**, set to **ENABLED** and click **Save**.

### Run webhooks with SendGrid and ngrok

To trigger webhooks, send an email through SendGrid (Web API or SMTP); SendGrid notifies your app on delivery success or failure.

* In SendGrid, go to **Email API** and **Integration Guide**.
* Choose **Web API** and **cURL**, enter a key name (for example, `myappkey`), and click **Create Key**.
* Run the curl command from the guide (use your sender identity and a real recipient email).

Confirm your localhost app receives notifications about the email being processed and delivered.

<Tip>
  SendGrid sends different request body contents depending on the events you selected.
</Tip>

You can confirm delivery under **Activity** and **Search** in the SendGrid UI.

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

ngrok can verify that incoming requests are from your SendGrid webhook so only that traffic reaches your app.

<Note>
  Webhook verification is limited to 500 validations per month on free accounts.
  If you need more, you can upgrade to Hobbyist or Pay-as-you-go.
  See [TPU Pricing](/pricing-limits/traffic-policy-unit-pricing/) for details.
</Note>

To add verification:

* In the [SendGrid Dashboard](https://app.sendgrid.com/), go to **Settings** and **Mail Settings**.
* Click **Signed Event Webhook Requests**.
* In the popup, click **Generate Verification Key**, copy the key value, and click **Close**.

<Note>
  Ensure **Signed Event Webhook Request Status** is **ENABLED**.
</Note>

* Create a Traffic Policy file named `sendgrid_policy.yml`.
  Replace `{your verification key}` with the value you copied:

  ```yaml  theme={null}
  on_http_request:
    - actions:
        - type: verify-webhook
          config:
            provider: sendgrid
            secret: "{your verification key}"
  ```

* Restart ngrok with the policy file:

  ```bash  theme={null}
  ngrok http 3000 --traffic-policy-file sendgrid_policy.yml
  ```

* Send an email through SendGrid to trigger the webhook.

Your app should receive the request and log it in the terminal.


Built with [Mintlify](https://mintlify.com).