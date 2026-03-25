# Source: https://ngrok.com/docs/integrations/webhooks/alchemy-webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Alchemy Webhooks

> Develop and test Alchemy webhooks from localhost.

This guide walks you through using ngrok to receive Alchemy webhooks on your localhost app.

By integrating ngrok with Alchemy, you can:

* Develop and test Alchemy webhooks locally without deploying to a public environment or setting up HTTPS.
* Inspect and troubleshoot requests from Alchemy in real time via the inspection UI and API.
* Modify and replay Alchemy webhook requests with a single click instead of reproducing events manually in your Alchemy account.
* Secure your app with Alchemy webhook validation provided by ngrok.
  Invalid requests are blocked by ngrok before reaching your app.

## What you'll need

* An [ngrok account](https://ngrok.com/signup) and your [authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).
* The [ngrok agent](https://ngrok.com/download) installed.
* [Node.js](https://nodejs.org/) installed (for the sample app, or use your own app).
* An Alchemy account.

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
  Your app is now exposed at that URL for use with Alchemy.

## 3. Configure Alchemy to send webhooks

Alchemy can send webhook requests to your app when events occur in your account.
To register for those events:

* Sign in to the [Alchemy dashboard](https://dashboard.alchemy.com/).
* In the left menu, click the **Data** icon and then **Webhooks**.
* On the **Webhooks** page, click **Create Webhook** for one of the types (for this tutorial, use **Address Activity**).
* Select the **Chain** and **Network** you want to monitor, then paste the ngrok URL in the **WEBHOOK URL** field (for example, `https://1a2b-3c4d-5e6f-7g8h-9i0j.ngrok.app`).
* Click **Test Webhook** and verify your localhost app receives a notification event.
* Enter your wallet address in **Ethereum Address** and click **Create Webhook**.

### Run webhooks with Alchemy and ngrok

Alchemy sends different request body contents depending on the type of webhook.
Because this example uses **Address Activity**, you need to receive or send tokens to your address to trigger events.

To test your webhook:

* In the [Alchemy dashboard](https://dashboard.alchemy.com/), go to **Data** and **Webhooks**.
* In the **Address Activity** section, click the 3 dots for the webhook you registered and click **Send Test Notification**.

Confirm your localhost app receives the test event and logs both headers and body in the terminal.

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

ngrok can verify that incoming requests are from your Alchemy webhook so only that traffic reaches your app.

<Note>
  Webhook verification is limited to 500 validations per month on free accounts.
  If you need more, you can upgrade to Hobbyist or Pay-as-you-go.
  See [TPU Pricing](/pricing-limits/traffic-policy-unit-pricing/) for details.
</Note>

To add verification:

* In the [Alchemy dashboard](https://dashboard.alchemy.com/), go to **Data** and **Webhooks**.

* In the **Address Activity** section, click the 3 dots for your webhook and click **Signing Key**.

* In the popup, copy the **Signing key** value and click **Close**.

* Create a Traffic Policy file named `alchemy_policy.yml`.
  Replace `{your signing key}` with the value you copied:

  ```yaml  theme={null}
  on_http_request:
    - actions:
        - type: verify-webhook
          config:
            provider: alchemy
            secret: "{your signing key}"
  ```

* Restart ngrok with the policy file:

  ```bash  theme={null}
  ngrok http 3000 --traffic-policy-file alchemy_policy.yml
  ```

<Note>
  After restarting ngrok, the tunnel URL changes.
  Alchemy does not allow editing webhook URLs, so it's recommended to create a [reserved domain](/universal-gateway/domains/) on your ngrok account and run the agent with `--domain your-domain.ngrok.app`.
</Note>

* Test the webhook from the Alchemy dashboard or trigger an event with the Alchemy SDK.

Your app should receive the request and log it in the terminal.


Built with [Mintlify](https://mintlify.com).