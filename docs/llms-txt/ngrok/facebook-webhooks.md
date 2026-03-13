# Source: https://ngrok.com/docs/integrations/webhooks/facebook-webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Facebook Webhooks

> Develop and test Facebook webhooks from localhost.

This guide explains how to use ngrok to receive Facebook webhooks on your localhost app.

By integrating ngrok with Facebook, you can:

* Develop and test Facebook webhooks locally without deploying to a public environment or setting up HTTPS.
* Inspect and troubleshoot requests from Facebook in real time via the inspection UI and API.
* Modify and replay Facebook webhook requests with a single click instead of reproducing events manually in your Facebook account.
* Secure your app with Facebook webhook validation provided by ngrok.
  Invalid requests are blocked by ngrok before reaching your app.

## What you'll need

* An [ngrok account](https://ngrok.com/signup) and your [authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).
* The [ngrok agent](https://ngrok.com/download) installed.
* [Node.js](https://nodejs.org/) installed (for the sample app, or use your own app).
* A Facebook account.

<Note>
  This integration requires an ngrok Pro or Enterprise license because Facebook validates your ngrok domain and certificate.
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
npm run startFacebook
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

* In the dashboard, expand **Universal Gateway** and click **Domains**.

<Tip>
  If you don't have an ngrok Pro or Enterprise license, sign up for one by clicking **Update Subscription** and following the subscribe procedure.
</Tip>

* On the **Domains** page, click **+ Create Domain** or **+ New Domain**.
* In the **Domain** pane, enter a value in the **Domain** field (for example, `myexample.ngrok.app`) and click **Continue**.

<Tip>
  Make sure your domain is available.
</Tip>

* Close the **Start a Tunnel** pane and then close the **Domain** pane.

* Start ngrok with your domain:

  ```bash  theme={null}
  ngrok http 3000 --url myexample.ngrok.app
  ```

* Copy the URL ngrok displays.
  Your app is now exposed at that URL for use with Facebook.

## 3. Configure Facebook to send webhooks

Facebook can send webhook requests to your app when page or account events occur in your account.
To register for those events you need a Facebook page and a Facebook app associated with that page; create them before continuing.

* Sign in to [Meta for Developers](https://developers.facebook.com/).
* Click **My Apps** and then click your app.
* On the app dashboard, click **Add Product** and then **Set up** inside the **Webhooks** tile.
* On the **Webhooks** page, select **Page** from the combo box and click **Subscribe to this object**.
* In the **Edit User subscription** popup, enter your ngrok URL with `/webhooks` at the end in the **Callback URL** field (for example, `https://myexample.ngrok.app/webhooks`).
* Enter `12345` in the **Verify token** field, set the **Include values** slider to **Yes**, and click **Verify and save**.
* Confirm your localhost app receives the validation request and logs `WEBHOOK_VERIFIED` in the terminal.
* Back on the **Webhooks** page, click **Subscribe** for the **feed** field.

<Tip>
  You can subscribe to multiple fields under the **Page** object and other objects; use the same URL for each.
</Tip>

* Click **Test** for the **feed** field, click **Send to My Server**, and confirm your localhost app receives the test post request.
* Set **App Mode** to **Live** at the top of your app page.

### Run webhooks with Facebook and ngrok

Facebook sends different request body contents depending on the object and field you subscribe to.
With the **feed** action you can test by creating a post on your page or liking a post:

* Under **Your Pages and profiles**, click your page.
* On the **Manage Page** screen, click **Create post**, add content, and click **Post**.

Confirm your localhost app receives the feed message and logs both headers and body in the terminal.

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

ngrok can verify that incoming requests are from your Facebook webhook so only that traffic reaches your app.

<Note>
  Webhook verification is limited to 500 validations per month on free accounts.
  If you need more, you can upgrade to Hobbyist or Pay-as-you-go.
  See [TPU Pricing](/pricing-limits/traffic-policy-unit-pricing/) for details.
</Note>

To add verification:

* In [Meta for Developers](https://developers.facebook.com/), go to **My Apps**, then **Settings** and **Basic**.

* On the **Basic Settings** page, click **Show** next to **App secret** and copy the value.

* Create a Traffic Policy file named `facebook_policy.yml`.
  Replace `{your app secret}` with the value you copied:

  ```yaml  theme={null}
  on_http_request:
    - name: "Facebook Webhooks"
      actions:
        - type: "webhook-validation"
          config:
            provider: "facebook_graph_api"
            secret: "{your app secret}"
  ```

* Restart ngrok with the policy file:

  ```bash  theme={null}
  ngrok http 3000 --traffic-policy-file facebook_policy.yml
  ```

* Send a message from the Facebook page you use for your webhook to trigger a request.

Your app should receive the request and log it in the terminal.


Built with [Mintlify](https://mintlify.com).