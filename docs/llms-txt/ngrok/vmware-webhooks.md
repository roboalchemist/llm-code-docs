# Source: https://ngrok.com/docs/integrations/webhooks/vmware-webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# VMware Workspace ONE Webhooks

> Develop and test VMware webhooks from localhost.

This guide shows you how to use ngrok to receive VMware Workspace ONE webhooks on your localhost app.

By integrating ngrok with VMware Workspace ONE, you can:

* Develop and test VMware Workspace ONE webhooks locally without deploying to a public environment or setting up HTTPS.
* Inspect and troubleshoot requests from VMware Workspace ONE in real time via the inspection UI and API.
* Modify and replay VMware Workspace ONE webhook requests with a single click instead of reproducing events manually in your VMware Workspace ONE account.
* Secure your app with VMware Workspace ONE webhook validation provided by ngrok.
  Invalid requests are blocked by ngrok before reaching your app.

## What you'll need

* An [ngrok account](https://ngrok.com/signup) and your [authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).
* The [ngrok agent](https://ngrok.com/download) installed.
* [Node.js](https://nodejs.org/) installed (for the sample app, or use your own app).
* A VMware Workspace ONE account.

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
  Your app is now exposed at that URL for use with VMware Workspace ONE.

## 3. Configure VMware Workspace ONE to send webhooks

VMware Workspace ONE can send webhook requests to your app when events occur in Workspace ONE UEM.
To register for those events:

* Sign in to [VMware Workspace ONE](https://console.cloud.vmware.com/).
* Click **LAUNCH SERVICE** for **Workspace ONE**, then **MANAGE** for **Unified Endpoint Management**.
* Go to **GROUPS & SETTINGS** > **All Settings** > **Advanced** (System) > **API** > **Event Notifications**.
* On **Event Notifications**, select **Override** and click **ADD RULE**.
* In **Add Event Notification**, enter a **Target Name** (for example, `My Webhook`) and your ngrok URL in **Target URL** (for example, `https://1a2b-3c4d-5e6f-7g8h-9i0j.ngrok.app`).
* Choose **JSON** as **Format**, click **TEST CONNECTION**, and confirm your app receives the request and "Test is successful" appears.
* In **Events**, set **ENABLED** for the events you want and click **SAVE**.

### Run webhooks with VMware Workspace ONE and ngrok

To trigger events (e.g. device enrollment):

* In Workspace ONE, go to **DEVICES** > **List View** > **ADD DEVICE**.
* Select a user, enter a valid **Email address** in **Messaging**, and click **SAVE** (create a user if needed).
* The user receives an activation email; opening the link and enrolling the device triggers events.

Confirm your localhost app receives notifications and logs both headers and body in the terminal.

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

ngrok can verify that incoming requests are from your VMware Workspace ONE webhook so only that traffic reaches your app.

<Note>
  Webhook verification is limited to 500 validations per month on free accounts.
  If you need more, you can upgrade to Hobbyist or Pay-as-you-go.
  See [TPU Pricing](/pricing-limits/traffic-policy-unit-pricing/) for details.
</Note>

To add verification:

* In [VMware Workspace ONE](https://console.cloud.vmware.com/), go to **Event Notifications** (as above), click your webhook, and **EDIT**.

* On **Edit Event Notification**, enter **Username** and **Password** (and **Confirm Password**), then click **SAVE**.

* Create a Traffic Policy file named `vmware_policy.yml`.
  Replace `{username}` and `{password}` with the values you set:

  ```yaml  theme={null}
  on_http_request:
    - actions:
        - type: verify-webhook
          config:
            provider: vmware_workspace
            secret: "{username}::{password}"
  ```

* Restart ngrok with the policy file:

  ```bash  theme={null}
  ngrok http 3000 --traffic-policy-file vmware_policy.yml
  ```

* Trigger an event again (e.g. device enrollment) to send a request.

Your app should receive the request and log it in the terminal.


Built with [Mintlify](https://mintlify.com).