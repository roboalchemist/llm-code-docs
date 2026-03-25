# Source: https://ngrok.com/docs/integrations/webhooks/whatsapp-webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# WhatsApp Webhooks

> Develop and test WhatsApp webhooks from localhost.

This guide explains how to use ngrok to receive WhatsApp webhooks on your localhost app.

By integrating ngrok with WhatsApp, you can:

* Develop and test WhatsApp webhooks locally without deploying to a public environment or setting up HTTPS.
* Inspect and troubleshoot requests from WhatsApp in real time via the inspection UI and API.
* Modify and replay WhatsApp webhook requests with a single click instead of reproducing events manually in your WhatsApp account.
* Secure your app with WhatsApp webhook validation provided by ngrok.
  Invalid requests are blocked by ngrok before reaching your app.

## What you'll need

* An [ngrok account](https://ngrok.com/signup) and your [authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).
* The [ngrok agent](https://ngrok.com/download) installed.
* [Node.js](https://nodejs.org/) installed (for the sample app, or use your own app).
* A Facebook app and a business phone number for WhatsApp.

<Note>
  This integration requires an ngrok Pro or Enterprise license because Meta validates your ngrok domain and certificate.
</Note>

## 1. Start your app

For this tutorial, you can use the [sample Node.js app on GitHub](https://github.com/ngrok/ngrok-webhook-nodejs-sample).

To install the sample, run the following in a terminal:

```bash  theme={null}
git clone https://github.com/ngrok/ngrok-webhook-nodejs-sample.git
cd ngrok-webhook-nodejs-sample
npm install
```

Then start the app (Facebook/WhatsApp sample):

```bash  theme={null}
npm run startFacebook
```

The app runs on port 3000 by default.

You can confirm it's running by visiting `http://localhost:3000`.
The app logs request headers and body in the terminal and shows a message in the browser.

## 2. Expose your app with ngrok

Once your app is running locally, you're ready to put it online securely using ngrok.

* Copy [your ngrok authtoken](https://dashboard.ngrok.com/get-started/your-authtoken) from the dashboard.

<Tip>
  The ngrok agent uses your authtoken to authenticate when you start a tunnel.
  You need a reserved domain: in the dashboard, expand **Universal Gateway**, click **Domains**, then **+ Create Domain** or **+ New Domain**, and reserve a domain (e.g. `myexample.ngrok.app`).
</Tip>

* Start ngrok with your reserved domain:

  ```bash  theme={null}
  ngrok http 3000 --url myexample.ngrok.app
  ```

* Copy the URL ngrok displays.
  Your app is now exposed at that URL for use with WhatsApp (use `https://myexample.ngrok.app/webhooks` as the callback URL).

## 3. Configure WhatsApp to send webhooks

WhatsApp can send webhook requests to your app when messages and other events occur.
To set it up:

* Sign in to [Meta for Developers](https://developers.facebook.com/), open **My Apps** and your app.
* Under **WhatsApp**, click **Set up**, then **Configuration** > **Edit**.
* In **Edit webhook's callback URL**, enter your ngrok URL with `/webhooks` (e.g. `https://myexample.ngrok.app/webhooks`), enter a **Verify token** (e.g. `12345`), and click **Verify and save**.
* Confirm your app receives the verification request and logs `WEBHOOK_VERIFIED`.
* Back on **Configuration**, click **Manage**, subscribe to **messages** (and any other fields you need), click **Test** for **messages**, and confirm your app receives the POST.
* Ensure a production or test phone number is associated and **App Mode** is **Live** if needed.

### Run webhooks with WhatsApp and ngrok

* Add the WhatsApp number (or test number) to your contacts and send a message to it.

Confirm your localhost app receives the message and logs both headers and body in the terminal.

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

ngrok can verify that incoming requests are from your WhatsApp webhook so only that traffic reaches your app.

<Note>
  Webhook verification is limited to 500 validations per month on free accounts.
  If you need more, you can upgrade to Hobbyist or Pay-as-you-go.
  See [TPU Pricing](/pricing-limits/traffic-policy-unit-pricing/) for details.
</Note>

To add verification:

* In [Meta for Developers](https://developers.facebook.com/), go to **Settings** > **Basic**, click **Show** for **App secret**, and copy the value.

* Create a Traffic Policy file named `whatsapp_policy.yml`.
  Replace `{your app secret}` with the value you copied:

  ```yaml  theme={null}
  on_http_request:
    - name: "WhatsApp Webhooks"
      actions:
        - type: "webhook-validation"
          config:
            provider: facebook_graph_api
            secret: "{your app secret}"
  ```

* Restart ngrok with the policy file:

  ```bash  theme={null}
  ngrok http 3000 --traffic-policy-file whatsapp_policy.yml
  ```

* Send another message to the WhatsApp number to trigger the webhook.

Your app should receive the request and log it in the terminal.


Built with [Mintlify](https://mintlify.com).