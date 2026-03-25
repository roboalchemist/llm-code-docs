# Source: https://ngrok.com/docs/integrations/webhooks/zoom-webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Zoom Webhooks

> Develop and test Zoom webhooks from localhost.

This guide shows you how to use ngrok to receive Zoom webhooks on your localhost app.

By integrating ngrok with Zoom, you can:

* Develop and test Zoom webhooks locally without deploying to a public environment or setting up HTTPS.
* Inspect and troubleshoot requests from Zoom in real time via the inspection UI and API.
* Modify and replay Zoom webhook requests with a single click instead of reproducing events manually in your Zoom account.
* Secure your app with Zoom webhook validation provided by ngrok.
  Invalid requests are blocked by ngrok before reaching your app.

## What you'll need

* An [ngrok account](https://ngrok.com/signup) and your [authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).
* The [ngrok agent](https://ngrok.com/download) installed.
* [Node.js](https://nodejs.org/) installed (for the sample app, or use your own app).
* A Zoom account.

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
  Your app is now exposed at that URL for use with Zoom.

## 3. Configure Zoom to send webhooks

Zoom can send webhook requests to your app when meeting and other events occur.
This guide uses the **Webhook Only** app type (free Zoom account).

* Sign in to the [Zoom Marketplace](https://marketplace.zoom.us/).
* Click **Develop** > **Build App**, select **Webhook Only**, enter a **Name**, and click **Create**.
* Complete registration with **Company Name**, developer **Name**, and **Email**, then click **Continue**.
* On **Feature**, turn **Event subscriptions** on and click **Add Event Subscriptions**.
* Enter your ngrok URL in **Event notification endpoint URL** (for example, `https://1a2b-3c4d-5e6f-7g8h-9i0j.ngrok.app`).
* Copy the **Secret Token** for use in verification.
* Click **Add Events**, select events (e.g. **Start Meeting**, **End Meeting**), click **Done**, then **Save** and **Continue**.
* When you see **Your app is activated on the account**, Zoom is ready to send events. You can review the webhook under **Manage** on the Marketplace page.

### Run webhooks with Zoom and ngrok

After the webhook is added, start a meeting in your Zoom account and end it after a few seconds.
Your localhost app receives notifications for both events.

<Tip>
  Zoom sends different request body contents and headers depending on the event.
  Each request includes an **authorization** header with the **Secret Token**; you can validate this in your app or use ngrok’s webhook verification below.
</Tip>

You can review **Manage** > **Call Logs** > **Webhook Logs** in the Marketplace to compare request bodies with what your app received.

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

ngrok can verify that incoming requests are from your Zoom webhook so only that traffic reaches your app.

<Note>
  Webhook verification is limited to 500 validations per month on free accounts.
  If you need more, you can upgrade to Hobbyist or Pay-as-you-go.
  See [TPU Pricing](/pricing-limits/traffic-policy-unit-pricing/) for details.
</Note>

To add verification:

* Use the **Secret Token** you copied when configuring the webhook (see [Configure Zoom to send webhooks](#3-configure-zoom-to-send-webhooks)).

* Create a Traffic Policy file named `zoom_policy.yml`.
  Replace `{your secret token}` with that value:

  ```yaml  theme={null}
  on_http_request:
    - actions:
        - type: verify-webhook
          config:
            provider: zoom
            secret: "{your secret token}"
  ```

* Restart ngrok with the policy file:

  ```bash  theme={null}
  ngrok http 3000 --traffic-policy-file zoom_policy.yml
  ```

* Start and then end a meeting in Zoom to trigger the webhook.

Your app should receive the request and log it in the terminal.


Built with [Mintlify](https://mintlify.com).