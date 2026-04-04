# Source: https://ngrok.com/docs/integrations/webhooks/slack-webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Slack Webhooks

> Develop and test Slack webhooks from localhost.

This guide shows you how to use ngrok to receive Slack webhooks on your localhost app.
Slack requires your application to be available at an HTTPS endpoint.

By integrating ngrok with Slack, you can:

* Develop and test Slack webhooks locally without deploying to a public environment or setting up HTTPS.
* Inspect and troubleshoot requests from Slack in real time via the inspection UI and API.
* Modify and replay Slack webhook requests with a single click instead of reproducing events manually in your Slack account.
* Secure your app with Slack webhook validation provided by ngrok.
  Invalid requests are blocked by ngrok before reaching your app.

## What you'll need

* An [ngrok account](https://ngrok.com/signup) and your [authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).
* The [ngrok agent](https://ngrok.com/download) installed.
* [Node.js](https://nodejs.org/) installed (for the sample app, or use your own app).
* A Slack account.

## 1. Start your app

For this tutorial, you can use the [sample Node.js app on GitHub](https://github.com/ngrok/ngrok-webhook-nodejs-sample).

To install the sample, run the following in a terminal:

```bash  theme={null}
git clone https://github.com/ngrok/ngrok-webhook-nodejs-sample.git
cd ngrok-webhook-nodejs-sample
npm install
```

Then start the app (Slack sample):

```bash  theme={null}
npm run startSlack
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
  Your app is now exposed at that URL for use with Slack.

## 3. Configure Slack to send webhooks

Slack can send webhook requests to your app when events occur in your workspace.
To register for those events:

* Sign in to the [Slack Web app](https://app.slack.com/) (you can use **use Slack in your browser**).
* Open the [Slack API portal](https://api.slack.com/apps) and click **Create an App**.
* In **Create an app**, click **From scratch**, enter an **App Name**, select a workspace under **Pick a workspace to develop your app in**, and click **Create App**.
* On **Basic Information**, expand **Add features and functionality** and click **Event Subscriptions**.
* On **Event Subscriptions**, turn **Enable Events** on.
  In **Request URL**, enter your ngrok URL (for example, `https://1a2b-3c4d-5e6f-7g8h-9i0j.ngrok.app`).

<Note>
  Slack makes a one-time call to your app with a challenge parameter and expects the app to respond with that value.
  See the [Slack Events API handshake](https://api.slack.com/apis/events-api#handshake) for details.
</Note>

* Under **Subscribe to events on behalf of users**, click **Add Workspace Event**, select `message.im`, and click **Save Changes**.
* In the left menu, click **Install App**, then **Install to Workspace**, and **Allow**.

### Run webhooks with Slack and ngrok

Because you subscribed to `message.im` and installed the app, you can trigger webhooks by sending a direct message:

* In the [Slack Web app](https://app.slack.com/) or desktop app, confirm your app appears under **Apps**.
* Direct message a user in the workspace, or message **Slackbot** with something like `Hello Slack bot!` and send it.

Confirm your localhost app receives the notification.

<Tip>
  Slack sends different request body contents and headers depending on the event.
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

ngrok can verify that incoming requests are from your Slack webhook so only that traffic reaches your app.

<Note>
  Webhook verification is limited to 500 validations per month on free accounts.
  If you need more, you can upgrade to Hobbyist or Pay-as-you-go.
  See [TPU Pricing](/pricing-limits/traffic-policy-unit-pricing/) for details.
</Note>

To add verification:

* On **Basic Information** for your Slack app, click **Show** for **Signing Secret** and copy the value.

* Create a Traffic Policy file named `slack_policy.yml`.
  Replace `{your signing secret}` with the value you copied:

  ```yaml  theme={null}
  on_http_request:
    - actions:
        - type: verify-webhook
          config:
            provider: slack
            secret: "{your signing secret}"
  ```

* Restart ngrok with the policy file:

  ```bash  theme={null}
  ngrok http 3000 --traffic-policy-file slack_policy.yml
  ```

* Send a message to **Slackbot** (for example, `Hello Slack bot!`) to trigger the webhook.

Your app should receive the request and log it in the terminal.


Built with [Mintlify](https://mintlify.com).