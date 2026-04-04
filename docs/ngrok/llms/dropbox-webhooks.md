# Source: https://ngrok.com/docs/integrations/webhooks/dropbox-webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Dropbox Webhooks

> Develop and test Dropbox webhooks from localhost.

This guide explains how to use ngrok to receive Dropbox webhooks on your localhost app.

By integrating ngrok with Dropbox, you can:

* Develop and test Dropbox webhooks locally without deploying to a public environment or setting up HTTPS.
* Inspect and troubleshoot requests from Dropbox in real time via the inspection UI and API.
* Modify and replay Dropbox webhook requests with a single click instead of reproducing events manually in your Dropbox account.
* Secure your app with Dropbox webhook validation provided by ngrok.
  Invalid requests are blocked by ngrok before reaching your app.

## What you'll need

* An [ngrok account](https://ngrok.com/signup) and your [authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).
* The [ngrok agent](https://ngrok.com/download) installed.
* [Node.js](https://nodejs.org/) installed (for the sample app, or use your own app).
* A Dropbox account.

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
  Your app is now exposed at that URL for use with Dropbox.

## 3. Configure Dropbox to send webhooks

Dropbox can send webhook requests to your app when events occur in your account.
To register for those events:

* Sign in to the [Dropbox site](https://dropbox.com/) and open the [Dropbox developer site](https://www.dropbox.com/developers/apps).
* On the **My apps** page, click **Create app**.
* On the **Create a new app** page, click **Scoped access**, click **App folder** under **Choose the type of access you need**, enter a name in **App name**, check the terms and conditions, and click **Create app**.
* On your app page, enter your ngrok URL in the **Webhook URIs** field (for example, `https://1a2b-3c4d-5e6f-7g8h-9i0j.ngrok.app`) and click **Add** in the **Webhooks** section.
* Confirm your localhost app receives a one-time call from Dropbox and logs the challenge parameter in the terminal.
* Confirm your webhook appears in the **Webhooks** section with **Enabled** status.

### Run webhooks with Dropbox and ngrok

With **App folder** access, Dropbox creates a folder with your app's name under **Apps**.
To trigger new calls from Dropbox to your app:

* In [Dropbox](https://dropbox.com/), go to **Apps** under **All files** in the left menu.
* Click your app's folder and upload a file by dragging it from your desktop into the folder.

Dropbox sends a POST request to your app when the upload completes.

<Note>
  The payload does not include file or folder changes; it only indicates which users have changes.
  Your app must call the Dropbox API to get the latest changes for each user.
</Note>

<Tip>
  You can create an app with **Scoped access** and **Full Dropbox** to receive notifications for any folder.
</Tip>

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

ngrok can verify that incoming requests are from your Dropbox webhook so only that traffic reaches your app.

<Note>
  Webhook verification is limited to 500 validations per month on free accounts.
  If you need more, you can upgrade to Hobbyist or Pay-as-you-go.
  See [TPU Pricing](/pricing-limits/traffic-policy-unit-pricing/) for details.
</Note>

To add verification:

* On the [Dropbox developer site](https://www.dropbox.com/developers/apps), click your app, open the **Settings** tab, click **Show** for **App secret**, and copy the value.

* Create a Traffic Policy file named `dropbox_policy.yml`.
  Replace `{your app secret}` with the value you copied:

  ```yaml  theme={null}
  on_http_request:
    - actions:
        - type: verify-webhook
          config:
            provider: dropbox
            secret: "{your app secret}"
  ```

* Restart ngrok with the policy file:

  ```bash  theme={null}
  ngrok http 3000 --traffic-policy-file dropbox_policy.yml
  ```

* Upload a new file to your app folder in Dropbox to trigger the webhook.

Your app should receive the request and log it in the terminal.


Built with [Mintlify](https://mintlify.com).