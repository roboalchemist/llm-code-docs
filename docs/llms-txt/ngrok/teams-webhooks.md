# Source: https://ngrok.com/docs/integrations/webhooks/teams-webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft Teams Webhooks

> Develop and test Microsoft Teams webhooks from localhost.

This guide explains how to use ngrok to receive Microsoft Teams webhooks on your localhost app.

By integrating ngrok with Microsoft Teams, you can:

* Develop and test Microsoft Teams webhooks locally without deploying to a public environment or setting up HTTPS.
* Inspect and troubleshoot requests from Microsoft Teams in real time via the inspection UI and API.
* Modify and replay Microsoft Teams webhook requests with a single click instead of reproducing events manually in your Microsoft Teams account.
* Secure your app with Microsoft Teams webhook validation provided by ngrok.
  Invalid requests are blocked by ngrok before reaching your app.

## What you'll need

* An [ngrok account](https://ngrok.com/signup) and your [authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).
* The [ngrok agent](https://ngrok.com/download) installed.
* [Node.js](https://nodejs.org/) installed (for the sample app, or use your own app).
* A Microsoft account and a Microsoft Teams page with an app.

<Note>
  This integration requires an ngrok Pro or Enterprise license because Microsoft Teams validates your ngrok domain and certificate.
</Note>

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
  You need a reserved domain: in the dashboard, expand **Universal Gateway**, click **Domains**, then **+ Create Domain** or **+ New Domain**, and reserve a domain (for example, `myexample.ngrok.app`).
</Tip>

* Start ngrok with your reserved domain:

  ```bash  theme={null}
  ngrok http 3000 --url myexample.ngrok.app
  ```

* Copy the URL ngrok displays (for example, `https://myexample.ngrok.app`).
  Your app is now exposed at that URL for use with Microsoft Teams.

## 3. Configure Microsoft Teams to send webhooks

Microsoft Teams can send webhook requests to your app when you use an outgoing webhook in a channel.
To set it up:

* Sign in to the [Microsoft Teams web interface](https://teams.microsoft.com/) (or use the Teams app).
* Click **Teams**, select a channel, and click the **+** at the top of the team page.
* In **Add a tab**, click **Manage apps** and then **Create an outgoing webhook** at the bottom.
* In **Create an outgoing webhook**, enter **Name** and **Description** (for example, `My local app`) and your ngrok URL in **Callback URL** (for example, `https://myexample.ngrok.app`).
* Click **Create** and note the **Security token** on the confirmation popup, then click **Close**.

### Run webhooks with Microsoft Teams and ngrok

The outgoing webhook acts as a bot: when you @mention it, it sends the message to your app.

* In a channel, type `@My local app` (or your webhook name) and press Enter.

Your localhost app receives the notification and logs both headers and body in the terminal.
The bot may reply with a message such as `{ message: "Thank you for the message" }`.

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

ngrok can verify that incoming requests are from your Microsoft Teams webhook so only that traffic reaches your app.

<Note>
  Webhook verification is limited to 500 validations per month on free accounts.
  If you need more, you can upgrade to Hobbyist or Pay-as-you-go.
  See [TPU Pricing](/pricing-limits/traffic-policy-unit-pricing/) for details.
</Note>

To add verification:

* Use the **Security token** you copied when creating the outgoing webhook (see [Configure Microsoft Teams to send webhooks](#3-configure-microsoft-teams-to-send-webhooks)).

* Create a Traffic Policy file named `teams_policy.yml`.
  Replace `{your app secret}` with that Security token:

  ```yaml  theme={null}
  on_http_request:
    - actions:
        - type: verify-webhook
          config:
            provider: microsoft_teams
            secret: "{your app secret}"
  ```

* Restart ngrok with the policy file:

  ```bash  theme={null}
  ngrok http 3000 --traffic-policy-file teams_policy.yml
  ```

* In Teams, send another message using the @mention for your webhook.

Your app should receive the request and log it in the terminal.


Built with [Mintlify](https://mintlify.com).