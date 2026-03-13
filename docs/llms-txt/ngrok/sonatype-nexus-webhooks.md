# Source: https://ngrok.com/docs/integrations/webhooks/sonatype-nexus-webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sonatype Nexus Webhooks

> Develop and test Sonatype Nexus webhooks from localhost.

This guide walks you through using ngrok to receive Sonatype Nexus webhooks on your localhost app.

By integrating ngrok with Sonatype Nexus, you can:

* Develop and test Sonatype Nexus webhooks locally without deploying to a public environment or setting up HTTPS.
* Inspect and troubleshoot requests from Sonatype Nexus in real time via the inspection UI and API.
* Modify and replay Sonatype Nexus webhook requests with a single click instead of reproducing events manually in your Sonatype Nexus account.
* Secure your app with Sonatype Nexus webhook validation provided by ngrok.
  Invalid requests are blocked by ngrok before reaching your app.

## What you'll need

* An [ngrok account](https://ngrok.com/signup) and your [authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).
* The [ngrok agent](https://ngrok.com/download) installed.
* [Node.js](https://nodejs.org/) installed (for the sample app, or use your own app).
* A Sonatype Nexus Repository Manager instance.

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
  Your app is now exposed at that URL for use with Sonatype Nexus.

## 3. Configure Sonatype Nexus to send webhooks

Sonatype Nexus can send webhook requests to your app when events occur in your repository.
To register for those events:

* Sign in to your **Sonatype Nexus Repository Manager** (the URL depends on where you deployed it).
* In the left menu, click **System**, **Capabilities**, and **Create capability** on the **Capabilities** page.
* Under **Select Capability Type**, choose **Webhook: Global** or **Webhook: Repository** (for this example, **Webhook: Global**).
* On **Create Webhook**, enter your ngrok URL in **URL** (for example, `https://1a2b-3c4d-5e6f-7g8h-9i0j.ngrok.app`).
* In **Available**, click **repository** and use the greater-than button to move it to **Selected**.

### Run webhooks with Sonatype Nexus and ngrok

Sonatype Nexus sends different request body contents depending on the event.
To trigger a call to your app:

* In the Sonatype Nexus UI, click **Repository** and **Repositories**, then (for example) **apt (hosted)**.
* Click **Create Repository**, choose a **Recipe**, enter **Name**, **Distribution**, and **Signing Key**, and click **Create repository**.

Confirm your localhost app receives an event notification and logs both headers and body in the terminal.

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

ngrok can verify that incoming requests are from your Sonatype Nexus webhook so only that traffic reaches your app.

<Note>
  Webhook verification is limited to 500 validations per month on free accounts.
  If you need more, you can upgrade to Hobbyist or Pay-as-you-go.
  See [TPU Pricing](/pricing-limits/traffic-policy-unit-pricing/) for details.
</Note>

To add verification:

* In your **Sonatype Nexus Repository Manager**, go to **System**, **Capabilities**, and the webhook capability you created (**Webhook: Global** or **Webhook: Repository**).

* On the **Webhook** page, open the **Settings** tab and enter a value in **Secret Key** (for example, `12345`).

* Create a Traffic Policy file named `sonatype_nexus_policy.yml`.
  Replace `{your webhook secret}` with the **Secret Key** value:

  ```yaml  theme={null}
  on_http_request:
    - actions:
        - type: verify-webhook
          config:
            provider: sonatype_nexus
            secret: "{your webhook secret}"
  ```

* Restart ngrok with the policy file:

  ```bash  theme={null}
  ngrok http 3000 --traffic-policy-file sonatype_nexus_policy.yml
  ```

* Trigger an event (for example, create a repository as above) to send a request.

Your app should receive the request and log it in the terminal.


Built with [Mintlify](https://mintlify.com).