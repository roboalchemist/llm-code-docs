# Source: https://ngrok.com/docs/integrations/webhooks/okta-webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Okta Webhooks

> Develop and test Okta webhooks from localhost.

This guide explains how to use ngrok to receive Okta webhooks on your localhost app.

By integrating ngrok with Okta, you can:

* Develop and test Okta webhooks locally without deploying to a public environment or setting up HTTPS.
* Inspect and troubleshoot requests from Okta in real time via the inspection UI and API.
* Modify and replay Okta webhook requests with a single click instead of reproducing events manually in your Okta account.
* Secure your app with Okta webhook validation provided by ngrok.
  Invalid requests are blocked by ngrok before reaching your app.

## What you'll need

* An [ngrok account](https://ngrok.com/signup) and your [authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).
* The [ngrok agent](https://ngrok.com/download) installed.
* [Node.js](https://nodejs.org/) installed (for the sample app, or use your own app).
* An Okta account.

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
npm run startOkta
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
  Your app is now exposed at that URL for use with Okta.

## 3. Configure Okta to send webhooks

Okta can send webhook requests to your app when events occur in your account.
To register for those events:

* Sign in to your Okta tenant (for example, `https://mytenant.okta.com/`).
* Click **Workflow**, **Event Hooks**, and then **Create Event Hook**.
* On **Add Event Hook Endpoint**, enter a name in **Name** (for example, `My Webhook`) and your ngrok URL in **URL** (for example, `https://1a2b-3c4d-5e6f-7g8h-9i0j.ngrok.app`).
* In **Subscribe to events**, select **User sign in attempt** and click **Save & Continue**.
* On the **Verification** page, click **Verify** so Okta can contact your localhost through ngrok.

### Run webhooks with Okta and ngrok

Okta sends different request body contents depending on the event.
To test your webhook:

* On the **Event Hooks** page, click **Actions** for your webhook and then **Preview**.
* On the **Preview** page, select an **Event Type** and click **Deliver Request**.

Confirm your localhost app receives the event and logs both headers and body in the terminal.

You can also trigger events by signing out of the Okta console and signing in again, then clicking **Admin** to enter the admin console.

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


Built with [Mintlify](https://mintlify.com).