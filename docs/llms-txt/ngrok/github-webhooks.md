# Source: https://ngrok.com/docs/integrations/webhooks/github-webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GitHub Repository Webhooks

> Develop and test GitHub webhooks from localhost.

This guide walks you through using ngrok to receive GitHub repository webhooks on your localhost app.

By integrating ngrok with GitHub, you can:

* Develop and test GitHub webhooks locally without deploying to a public environment or setting up HTTPS.
* Inspect and troubleshoot requests from GitHub in real time via the inspection UI and API.
* Modify and replay GitHub webhook requests with a single click instead of reproducing events manually in GitHub.
* Secure your app with GitHub webhook validation provided by ngrok.
  Invalid requests are blocked by ngrok before reaching your app.

## What you'll need

* An [ngrok account](https://ngrok.com/signup) and your [authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).
* The [ngrok agent](https://ngrok.com/download) installed.
* [Node.js](https://nodejs.org/) installed (for the sample app, or use your own app).
* Your GitHub account and a repository.

## 1. Start your app

For this tutorial, you can use the [sample Node.js app on GitHub](https://github.com/ngrok/ngrok-webhook-nodejs-sample).

To install the sample, run the following in a terminal:

```bash  theme={null}
git clone https://github.com/ngrok/ngrok-webhook-nodejs-sample.git
cd ngrok/ngrok-webhook-nodejs-sample
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

With your app running locally, expose it with ngrok.

* Copy [your ngrok authtoken](https://dashboard.ngrok.com/get-started/your-authtoken) from the dashboard.

<Tip>
  The ngrok agent uses your authtoken to authenticate when you start a tunnel.
</Tip>

* Start ngrok:

  ```bash  theme={null}
  ngrok http 3000
  ```

* Copy the URL ngrok displays.
  Your app is now exposed at that URL for use with GitHub.

## 3. Configure GitHub to send webhooks

GitHub can send webhook requests to your app when repository events occur.
To register for those events:

* Sign in to [GitHub](https://github.com).
* Open a repository from your repositories list.

<Tip>
  If you don't have a repository, create an empty one first.
</Tip>

* In the repository, go to **Settings** and select **Webhooks** in the left menu.
* Click **Add webhook**.
* In **Payload URL**, paste the ngrok URL (for example, `https://1a2b-3c4d-5e6f-7g8h-9i0j.ngrok.app`).
* Set **Content type** to `application/json`.
* Choose which events trigger the webhook (for this example, select **Just the push event**).
* Leave the webhook active and click **Add webhook**.

### Run webhooks with GitHub and ngrok

After you add the webhook, GitHub sends POST requests to your app through ngrok.

To compare what GitHub sends with what your app receives:

* Open the webhook you created.
* Click the **Recent Deliveries** tab.
* Select a delivery by ID.

Compare that delivery's headers and body with what your application received; they should match.

<Note>
  The payload your app receives depends on the events you chose.
  Because this example uses **Just the push event**, push changes to the repository to trigger new webhook calls.
  To resend a request, click **Redeliver** in the **Recent Deliveries** tab on the webhook page.
</Note>

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

ngrok can verify that incoming requests are from your GitHub webhook so only that traffic reaches your app.

<Note>
  Webhook verification is limited to 500 validations per month on free accounts.
  If you need more, you can upgrade to Hobbyist or Pay-as-you-go.
  See [TPU Pricing](/pricing-limits/traffic-policy-unit-pricing/) for details.
</Note>

To add verification:

* Create a Traffic Policy file named `github_policy.yml`.
  Replace `{your secret}` with the **Secret** from your GitHub webhook:

  ```yaml  theme={null}
  on_http_request:
    - actions:
        - type: verify-webhook
          config:
            provider: github
            secret: "{your secret}"
  ```

* Restart ngrok with the policy file:

  ```bash  theme={null}
  ngrok http 3000 --traffic-policy-file github_policy.yml
  ```

* Resend a delivery from your GitHub webhook.

Your app should receive the request and log it in the terminal.


Built with [Mintlify](https://mintlify.com).