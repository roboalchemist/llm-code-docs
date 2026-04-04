# Source: https://ngrok.com/docs/integrations/webhooks/amazon-sns-webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Amazon SNS Webhooks

> Develop and test Amazon SNS webhooks from localhost.

This guide explains how to use ngrok to receive Amazon SNS topic notifications on your localhost app.

By integrating ngrok with Amazon SNS, you can:

* Develop and test Amazon SNS webhooks locally without deploying to a public environment or setting up HTTPS.
* Inspect and troubleshoot requests from Amazon SNS in real time via the inspection UI and API.
* Modify and replay Amazon SNS webhook requests with a single click instead of reproducing notifications manually in your SNS topic.
* Secure your app with Amazon SNS webhook validation provided by ngrok.
  Invalid requests are blocked by ngrok before reaching your app.

## What you'll need

* An [ngrok account](https://ngrok.com/signup) and your [authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).
* The [ngrok agent](https://ngrok.com/download) installed.
* [Node.js](https://nodejs.org/) installed (for the sample app, or use your own app).
* An [AWS](https://aws.amazon.com/) account.

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
  Your app is now exposed at that URL for use with Amazon SNS.

## 3. Configure Amazon SNS to send webhooks

Amazon SNS can send HTTPS notifications to your app when messages are published to a topic.
To set this up:

* Sign in to [AWS](https://aws.amazon.com/).
* In the AWS console search bar, enter `sns` and open **Simple Notification Service**.
* On the SNS **Dashboard**, click **Topics** in the left menu and click **Create topic**.
* On **Create topic**, select **Standard**, enter a name (for example, `MyTopic`) in **Name**, and click **Create topic**.
* Click **Subscriptions** in the left menu and click **Create subscription**.
* On **Create subscription**, select your topic in **Topic ARN**, select **HTTPS** in **Protocol**, and paste the ngrok URL in **Endpoint** (for example, `https://1a2b-3c4d-5e6f-7g8h-9i0j.ngrok.app`).
* Click **Create subscription**.
* Confirm your localhost app receives a **SubscriptionConfirmation** notification and logs both headers and body in the terminal.
* From the request body, copy the value of **SubscribeURL**.
* On the SNS **Subscriptions** page, select the **Pending confirmation** subscription, click **Confirm subscription**, paste the **SubscribeURL** value in the **url** field, and click **Confirm subscription**.

You should see **Subscription was confirmed successfully**.

### Run webhooks with Amazon SNS and ngrok

Publishing a message to your SNS topic triggers your HTTPS subscription.
To publish a message manually:

* In the AWS console, search for `sns` and open **Simple Notification Service**.
* On the SNS **Dashboard**, click **Topics** and open the topic you created.
* On the topic page, click **Publish message**, enter a subject in **Subject**, enter a body in **Message body to send to the endpoint**, and click **Publish message**.

Confirm your localhost app receives a notification and logs both headers and body in the terminal.

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

ngrok can verify that incoming requests are from your Amazon SNS topic so only that traffic reaches your app.

<Note>
  Webhook verification is limited to 500 validations per month on free accounts.
  If you need more, you can upgrade to Hobbyist or Pay-as-you-go.
  See [TPU Pricing](/pricing-limits/traffic-policy-unit-pricing/) for details.
</Note>

To add verification:

* In the [AWS](https://aws.amazon.com/) console, open the Amazon SNS **Dashboard** and click **Topics**.

* Open your topic and copy the value of **Topic owner**.

* Create a Traffic Policy file named `amazon_sns_policy.yml`.
  Replace `{Topic owner}` with the value you copied:

  ```yaml  theme={null}
  on_http_request:
    - actions:
        - type: verify-webhook
          config:
            provider: sns
            secret: "{Topic owner}"
  ```

* Restart ngrok with the policy file:

  ```bash  theme={null}
  ngrok http 3000 --traffic-policy-file amazon_sns_policy.yml
  ```

* Publish a new message to your topic from the AWS console.

Your app should receive the request and log it in the terminal.


Built with [Mintlify](https://mintlify.com).