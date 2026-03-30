# Source: https://ngrok.com/docs/integrations/webhooks/tiktok-webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# TikTok Webhooks

> Develop and test TikTok webhooks from localhost.

This guide walks you through using ngrok to receive TikTok webhooks on your localhost app.

By integrating ngrok with TikTok, you can:

* Develop and test TikTok webhooks locally without deploying to a public environment or setting up HTTPS.
* Inspect and troubleshoot requests from TikTok in real time via the inspection UI and API.
* Modify and replay TikTok webhook requests with a single click instead of reproducing events manually in your TikTok app.
* Secure your app with TikTok webhook validation provided by ngrok.
  Invalid requests are blocked by ngrok before reaching your app.

## What you'll need

* An [ngrok account](https://ngrok.com/signup) and your [authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).
* The [ngrok agent](https://ngrok.com/download) installed.
* [Node.js](https://nodejs.org/) installed (for the sample app, or use your own app).
* A TikTok Developer account.

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
  Your app is now exposed at that URL for use with TikTok.

## 3. Configure TikTok to send webhooks

TikTok can send webhook requests to your app when events occur in your TikTok app.
To register for those events:

* Sign in to the [TikTok Developer Portal](https://developers.tiktok.com/).
* Click **Manage apps** and **Connect an app** (or open an existing app).
* Upload an **App icon**, set **Category** to **Others**, add a **Description**, enable **Configure for Web**, enter a **Website URL**, and click **Save changes**.
* On the app page, click **Add products** and **Add** for **Webhooks** (you may need to add **Login Kit** first).
* Under **Webhooks**, enter your ngrok URL in **Callback URL** (for example, `https://1a2b-3c4d-5e6f-7g8h-9i0j.ngrok.app`).
* Click **Test URL** and **Send**, confirm your app receives the notification and returns 200, then click **Done** and **Save changes**.

<Note>
  You may need to set **Terms of Service URL**, **Privacy Policy URL**, and **Redirect domain** in **Login Kit**.
  If the app is not published, click **Submit for review**.
</Note>

### Run webhooks with TikTok and ngrok

By default you are subscribed to all events.
TikTok sends different request body contents depending on the event.

After your app is approved, associate a user with your app.
TikTok will send notifications to your localhost app for events such as account deauthorization, video upload failure, or video published.
Confirm your localhost app receives these event notifications and logs both headers and body in the terminal.

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

ngrok can verify that incoming requests are from your TikTok webhook so only that traffic reaches your app.

<Note>
  Webhook verification is limited to 500 validations per month on free accounts.
  If you need more, you can upgrade to Hobbyist or Pay-as-you-go.
  See [TPU Pricing](/pricing-limits/traffic-policy-unit-pricing/) for details.
</Note>

To add verification:

* In the [TikTok Developer Portal](https://developers.tiktok.com/), open **Manage apps**, click your app, click the eye icon to reveal **Client secret**, and copy the value.

* Create a Traffic Policy file named `tiktok_policy.yml`.
  Replace `{your webhook secret}` with the value you copied:

  ```yaml  theme={null}
  on_http_request:
    - actions:
        - type: verify-webhook
          config:
            provider: tiktok
            secret: "{your webhook secret}"
  ```

* Restart ngrok with the policy file:

  ```bash  theme={null}
  ngrok http 3000 --traffic-policy-file tiktok_policy.yml
  ```

* Use your TikTok app (or trigger an event as in [Run webhooks with TikTok and ngrok](#run-webhooks-with-tiktok-and-ngrok)) to send a request.

Your app should receive the request and log it in the terminal.


Built with [Mintlify](https://mintlify.com).