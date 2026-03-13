# Source: https://ngrok.com/docs/integrations/webhooks/box-webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Box Webhooks

> Develop and test Box webhooks from localhost.

This guide explains how to use ngrok to receive Box webhooks on your localhost app.

By integrating ngrok with Box, you can:

* Develop and test Box webhooks locally without deploying to a public environment or setting up HTTPS.
* Inspect and troubleshoot requests from Box in real time via the inspection UI and API.
* Modify and replay Box webhook requests with a single click instead of reproducing events manually in your Box account.
* Secure your app with Box webhook validation provided by ngrok.
  Invalid requests are blocked by ngrok before reaching your app.

## What you'll need

* An [ngrok account](https://ngrok.com/signup) and your [authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).
* The [ngrok agent](https://ngrok.com/download) installed.
* [Node.js](https://nodejs.org/) installed (for the sample app, or use your own app).
* A Box account.

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
  Your app is now exposed at that URL for use with Box.

## 3. Configure Box to send webhooks

Box can send webhook requests to your app when events occur in your account.
To register for those events:

* Sign in to [Box](https://box.com/) and click **Dev Console** in the left menu.
* On the Box Developer console, click **Create New App**, then **Custom App**.
* In the **Custom App** popup, select **Server Authentication (with JWT)**, enter a name in **App name**, and click **Create**.
* On the app page, open the **Configuration** tab, check **Manage Webhooks** under **Developer Actions**, and click **Save Changes**.
* Open the **Authorization** tab, click **Review and Submit**, enter a description in **App Description** (for example, `Requesting Access`), and click **Submit**.
* In [Box Admin Console](https://app.box.com/master), go to **Apps**, **Custom App Manager**, click **View** on your app, then **Authorize** and **Authorize** again.
* Back in the [Box Developer Console](https://app.box.com/developers/console), open your app, click the **Webhook** tab, click **Create Webhook**, then **V2**.
* On **Create a Webhook**, paste the ngrok URL in **URL Address** (for example, `https://1a2b-3c4d-5e6f-7g8h-9i0j.ngrok.app`).
* For **Content Type**, click **Choose an item** and select a folder from your Box account.
* Under **File Triggers**, check **File Uploaded** and click **Create Webhook**.

### Run webhooks with Box and ngrok

With the **File Uploaded** trigger, Box sends a notification to your app when you upload files to the chosen folder.

* In [Box](https://box.com/), upload a file from your desktop to the folder you selected when creating the webhook.

Confirm your localhost app receives the **FILE.UPLOADED** event and logs both headers and body in the terminal.

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

ngrok can verify that incoming requests are from your Box webhook so only that traffic reaches your app.

<Note>
  Webhook verification is limited to 500 validations per month on free accounts.
  If you need more, you can upgrade to Hobbyist or Pay-as-you-go.
  See [TPU Pricing](/pricing-limits/traffic-policy-unit-pricing/) for details.
</Note>

To add verification:

* In the [Box Developer Console](https://app.box.com/developers/console), open your app, go to the **Webhook** tab, and click **Manage Signature Keys**.

* On **Manage Signature Keys**, click **Generate Key** in **Primary Key** and click **COPY** to copy the primary key value.

* Create a Traffic Policy file named `box_policy.yml`.
  Replace `{your primary key}` with the value you copied:

  ```yaml  theme={null}
  on_http_request:
    - actions:
        - type: verify-webhook
          config:
            provider: box
            secret: "{your primary key}"
  ```

* Restart ngrok with the policy file:

  ```bash  theme={null}
  ngrok http 3000 --traffic-policy-file box_policy.yml
  ```

* Upload a file to the folder you selected for the webhook to trigger a request.

Your app should receive the request and log it in the terminal.


Built with [Mintlify](https://mintlify.com).