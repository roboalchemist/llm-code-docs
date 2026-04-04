# Source: https://ngrok.com/docs/integrations/webhooks/chargify-webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Chargify Webhooks

> Develop and test Chargify webhooks from localhost.

This guide walks you through using ngrok to receive Chargify webhooks on your localhost app.

By integrating ngrok with Chargify, you can:

* Develop and test Chargify webhooks locally without deploying to a public environment or setting up HTTPS.
* Inspect and troubleshoot requests from Chargify in real time via the inspection UI and API.
* Modify and replay Chargify webhook requests with a single click instead of reproducing events manually in your Chargify account.
* Secure your app with Chargify webhook validation provided by ngrok.
  Invalid requests are blocked by ngrok before reaching your app.

## What you'll need

* An [ngrok account](https://ngrok.com/signup) and your [authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).
* The [ngrok agent](https://ngrok.com/download) installed.
* [Node.js](https://nodejs.org/) installed (for the sample app, or use your own app).
* A Chargify account.

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
  Your app is now exposed at that URL for use with Chargify.

## 3. Configure Chargify to send webhooks

Chargify can send webhook requests to your app when events occur in your account.
To register for those events:

* Sign in to [Chargify](https://www.chargify.com/).
* On the home page, select a site from the **Site** dropdown at the top.
* Click **Config**, **Settings**, and then **Webhooks**.
* On the **Webhooks** page, click **Add New Endpoint**.
* On the **Add New Endpoint** page, enter your ngrok URL in the **Webhook URL** field (for example, `https://1a2b-3c4d-5e6f-7g8h-9i0j.ngrok.app`).
* Select the **Events** you want (for this tutorial, select all) and click **Add**.

### Run webhooks with Chargify and ngrok

Chargify sends different request body contents depending on the event.
To trigger new calls from Chargify to your app:

* On your Chargify site, go to **Tools** and then **Webhook Testing**.
* On the **Webhook Testing** page, select one of the events you subscribed to, select the webhook, and click **Send**.

Confirm your localhost app receives the event and logs both headers and body in the terminal.

You can verify the webhook call in Chargify: go to **Tools**, **Webhook Panel**, and click **Details** for the webhook call.

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

ngrok can verify that incoming requests are from your Chargify webhook so only that traffic reaches your app.

<Note>
  Webhook verification is limited to 500 validations per month on free accounts.
  If you need more, you can upgrade to Hobbyist or Pay-as-you-go.
  See [TPU Pricing](/pricing-limits/traffic-policy-unit-pricing/) for details.
</Note>

To add verification:

* On your Chargify site, click **Edit current Site** from the **Site** dropdown at the top.

* On the **Site** page, copy the value of the **Site Shared Key**.

* Create a Traffic Policy file named `chargify_policy.yml`.
  Replace `{your site shared key}` with the value you copied:

  ```yaml  theme={null}
  on_http_request:
    - actions:
        - type: verify-webhook
          config:
            provider: chargify
            secret: "{your site shared key}"
  ```

* Restart ngrok with the policy file:

  ```bash  theme={null}
  ngrok http 3000 --traffic-policy-file chargify_policy.yml
  ```

* Go to **Webhook Testing** and send a new test notification to your webhook.

Your app should receive the request and log it in the terminal.


Built with [Mintlify](https://mintlify.com).