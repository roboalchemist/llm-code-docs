# Source: https://ngrok.com/docs/integrations/webhooks/webex-webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Cisco Webex Webhooks

> Develop and test Webex webhooks from localhost.

This guide walks you through using ngrok to receive Cisco Webex webhooks on your localhost app.

By integrating ngrok with Cisco Webex, you can:

* Develop and test Cisco Webex webhooks locally without deploying to a public environment or setting up HTTPS.
* Inspect and troubleshoot requests from Cisco Webex in real time via the inspection UI and API.
* Modify and replay Cisco Webex webhook requests with a single click instead of reproducing events manually in your Cisco Webex account.
* Secure your app with Cisco Webex webhook validation provided by ngrok.
  Invalid requests are blocked by ngrok before reaching your app.

## What you'll need

* An [ngrok account](https://ngrok.com/signup) and your [authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).
* The [ngrok agent](https://ngrok.com/download) installed.
* [Node.js](https://nodejs.org/) installed (for the sample app, or use your own app).
* A Cisco Webex account.

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
  Your app is now exposed at that URL for use with Cisco Webex.

## 3. Configure Cisco Webex to send webhooks

Cisco Webex can send webhook requests to your app when events occur (e.g. meeting started).
To register:

* Sign in to the [Cisco Webex Developer Portal](https://developer.webex.com/) and obtain a [Personal Access Token](https://developer.webex.com/docs/getting-started#accounts-and-authentication).
* Register the webhook with the API. Example:

  ```bash  theme={null}
  curl --location 'https://webexapis.com/v1/webhooks' \
  --header 'Authorization: Bearer TOKEN' \
  --header 'Content-Type: application/json' --data '{
    "name": "localhost app via ngrok webhook",
    "targetUrl": "URL",
    "resource": "meetings",
    "event": "started",
    "secret": "SECRET_KEY"
  }'
  ```

  Replace `TOKEN` with your Personal Access Token, `URL` with your ngrok URL (e.g. `https://1a2b-3c4d-5e6f-7g8h-9i0j.ngrok.app`), and `SECRET_KEY` with a value used to sign requests.

### Run webhooks with Cisco Webex and ngrok

You subscribed to the **meetings** / **started** event.
To trigger a call:

* Sign in to [Cisco Webex](https://www.webex.com) and click **Start a meeting**.

Confirm your localhost app receives the notification and logs both headers and body in the terminal.

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

ngrok can verify that incoming requests are from your Cisco Webex webhook so only that traffic reaches your app.

<Note>
  Webhook verification is limited to 500 validations per month on free accounts.
  If you need more, you can upgrade to Hobbyist or Pay-as-you-go.
  See [TPU Pricing](/pricing-limits/traffic-policy-unit-pricing/) for details.
</Note>

To add verification:

* Use the **SECRET\_KEY** value you set when registering the webhook (see [Configure Cisco Webex to send webhooks](#3-configure-cisco-webex-to-send-webhooks)).

* Create a Traffic Policy file named `webex_policy.yml`.
  Replace `{your webhook secret}` with that value:

  ```yaml  theme={null}
  on_http_request:
    - actions:
        - type: verify-webhook
          config:
            provider: webex
            secret: "{your webhook secret}"
  ```

* Restart ngrok with the policy file:

  ```bash  theme={null}
  ngrok http 3000 --traffic-policy-file webex_policy.yml
  ```

* Start a meeting in [Cisco Webex](https://www.webex.com) to trigger the webhook.

Your app should receive the request and log it in the terminal.


Built with [Mintlify](https://mintlify.com).