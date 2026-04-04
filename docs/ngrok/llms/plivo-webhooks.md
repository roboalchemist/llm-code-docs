# Source: https://ngrok.com/docs/integrations/webhooks/plivo-webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Plivo Webhooks

> Develop and test Plivo webhooks from localhost.

This guide shows you how to use ngrok to receive Plivo webhooks on your localhost app.

By integrating ngrok with Plivo, you can:

* Develop and test Plivo webhooks locally without deploying to a public environment or setting up HTTPS.
* Inspect and troubleshoot requests from Plivo in real time via the inspection UI and API.
* Modify and replay Plivo webhook requests with a single click instead of reproducing events manually in your Plivo account.
* Secure your app with Plivo webhook validation provided by ngrok.
  Invalid requests are blocked by ngrok before reaching your app.

## What you'll need

* An [ngrok account](https://ngrok.com/signup) and your [authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).
* The [ngrok agent](https://ngrok.com/download) installed.
* [Node.js](https://nodejs.org/) installed (for the sample app, or use your own app).
* A Plivo account.

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
  Your app is now exposed at that URL for use with Plivo.

## 3. Configure Plivo to send webhooks

Plivo can send webhook requests to your app when SMS and MMS messages are sent to your Plivo numbers.
To register for those events:

* Sign in to the [Plivo Console](https://console.plivo.com/).
* Click **Messaging** and **PHLO** under **Applications**.
* On **Your PHLOs**, click **Create New PHLO** and **Build My Own**.
* On the PHLO page, click the pencil next to the title, name it (for example, `Webhook PHLO`), and click **Save**.
* Drag **HTTP Request** from the left panel to the center and click it.
* In the right panel, set **HTTP Method** to **POST** and enter your ngrok URL in the URL field (for example, `https://1a2b-3c4d-5e6f-7g8h-9i0j.ngrok.app`).
* Click **FETCH RESPONSE**, confirm the response in **Response**, and click **VALIDATE**.
* Drag a line from **Incoming Message** on **Start** to the **HTTP Request** component and click **Save**.
* Click **Phone Numbers** and select a number (or **Buy Number** if needed).
* On the phone number page, set **Application Type** to **PHLO**, **PHLO Name** to your PHLO, and click **Update Number**.

### Run webhooks with Plivo and ngrok

Plivo sends different request body contents depending on the event.
To trigger a call: send an SMS to your Plivo phone number.

Confirm your localhost app receives the notification and logs both headers and body in the terminal.

You can verify in Plivo: **Messaging**, **SMS/MMS** under **Logs**, then open a log and check **Status Callbacks**.

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

ngrok can verify that incoming requests are from your Plivo webhook so only that traffic reaches your app.

<Note>
  Webhook verification is limited to 500 validations per month on free accounts.
  If you need more, you can upgrade to Hobbyist or Pay-as-you-go.
  See [TPU Pricing](/pricing-limits/traffic-policy-unit-pricing/) for details.
</Note>

To add verification:

* In the [Plivo Console](https://console.plivo.com/), click the eye icon next to **Auth Token** and copy the value.

* Create a Traffic Policy file named `plivo_policy.yml`.
  Replace `{your auth token}` with the value you copied:

  ```yaml  theme={null}
  on_http_request:
    - actions:
        - type: verify-webhook
          config:
            provider: plivo
            secret: "{your auth token}"
  ```

* Restart ngrok with the policy file:

  ```bash  theme={null}
  ngrok http 3000 --traffic-policy-file plivo_policy.yml
  ```

* Send an SMS to your Plivo number to trigger the webhook.

Your app should receive the request and log it in the terminal.


Built with [Mintlify](https://mintlify.com).