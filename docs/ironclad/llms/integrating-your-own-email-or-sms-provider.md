# Source: https://clickwrap-developer.ironcladapp.com/docs/integrating-your-own-email-or-sms-provider.md

# Integrating your own email or SMS provider

Don't want to use our emails or SMS messages? Simply set up a new integration to configure using your own.

In this article we'll share how to set up integrations to your own SMS and email providers. You'll learn how to:

1. Catch a "Request Sent" webhook when a signature request is sent to your signer.
2. Learn how to process the webhook in order to include the right information in your email or SMS message.

## What you'll need to get started

To get started with this guide, you'll need the following:

* API access
* Access and knowledge on setting up [Webhooks](https://developer.pactsafe.com/docs/working-with-pactsafe-webhooks)
* A service or functioning endpoint for Ironclad Clickwrap Webhooks to reach out to (AWS' Lambda is great for things like this)

## Primary data flows for integration

There are three primary data flows to consider when building your own integration to an email or SMS provider:

1. Catch a webhook when signature requests are **sent** to your signer
2. Catch a webhook when a signature request is **signed** by a signer
3. Catch a webhook when a signature request is **completed** by *all* parties

> 📘 Note: Reminders aren't scoped for this integration
>
> Ironclad Clickwrap sends reminders when a signer hasn't signed after 3, 7, and 14 days. If you'd like to setup reminders, you'll also want to set up a recurring job that uses these reminders. Currently, there is no "Request Reminder" webhook but this is something we'll consider for the roadmap.

### Getting started

You'll first want to set up a webhook with 3 events enabled: "Request Sent", "Request Signed", and "Request Complete". Click here to go to your [Integrations](https://app.pactsafe.com/settings/integrations), add a "Webhook", and follow the instructions [here](https://developer.pactsafe.com/docs/working-with-pactsafe-webhooks) for more detail.

Next, you will want to build a dedicated service to catch webhooks fired by Ironclad Clickwrap in your own service and then handle accordingly.

> 🚧 Note: What if the webhooks fails to reach my own web service?
>
> Failed webhook events **will** retry on a regular cadence for up to 24 hours should any failures occur.

### 1. Catch a webhook when signature requests are sent to your signer

If you're using the REST API to process signature requests in Ironclad Clickwrap, you're likely calling a POST to `/requests/:request_id/send` to deliver the finalized signature request to your signer(s). Upon doing this, Ironclad Clickwrap will trigger a webhook called "Request Sent" to any webhooks currently configured on the account.

Below are the 4 steps to your integration to deliver the SMS or email from your own provider.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        <p>
          Step
        </p>
      </th>

      <th>
        <p>
          Description
        </p>
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        <ol><li>Catch "Request Sent" webhook</li></ol>
      </td>

      <td>
        <p>An example of this webhook can be <a href="https://developer.pactsafe.com/docs/working-with-pactsafe-webhooks#section-request-sent">found here</a>.</p>
      </td>
    </tr>

    <tr>
      <td>
        <ol start="2"><li>Make HTTP GET request</li></ol>
      </td>

      <td>
        <p>The below properties within the request are what you'll need for the next step:</p>

        ```
        GET => /v1.1/requests/:request_id
        {
          "signers": [
            {
              "send_to": {
                "email": true,
                "mobile_number": true
              },
              "signer": {
                "email": "info@pactsafe.com",
                "mobile_number": "+13175551234"
              },
              "request_url": "..."
            }
          ]
        }
        ```
      </td>
    </tr>

    <tr>
      <td>
        <ol start="3"><li>Shorten Signing URL</li></ol>
      </td>

      <td>
        <p>Next, you can take the signing URL (the <code>request\_url</code> property) for your signer and shorten it using an API like Bit.ly or <a href="https://www.rebrandly.com">Rebrandly</a>.</p>
      </td>
    </tr>

    <tr>
      <td>
        <ol start="4"><li>Send SMS or email</li></ol>
      </td>

      <td>
        Once you've shortened the link, you can trigger the email or SMS to your own provider passing in the mobile number or email address, signing URL, and other metadata that you may want to leverage from Ironclad Clickwrap.Example SMS:\
        You've been sent "PS Employment Agreement" by Ironclad Clickwrap. Please review & sign: [https://bit.ly/2131NDa](https://bit.ly/2131NDa)
      </td>
    </tr>
  </tbody>
</Table>

### 2. Catch a webhook when signature requests are signed by one of your signers

If you have more than one signer, you'll want to keep track of individual signers completing as they sign. Ironclad Clickwrap will trigger a webhook called "Request Signed" to any webhooks currently configured on the account every time any signer signs a signature request.

> 📘 Note: If you only have one signer
>
> If you only have one signer on your signature request, Ironclad Clickwrap will send both a "Request Signed" and "Request Complete" (asynchronously, so not necessarily in order) for the final signature on the signature request.

Below are the steps to follow when a signature request is signed.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Step
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **1. Catch "Request Signed" webhook**
      </td>

      <td>
        An example of this webhook can be [found here](https://developer.pactsafe.com/docs/working-with-pactsafe-webhooks#section-request-signed).
      </td>
    </tr>

    <tr>
      <td>
        **2. Make HTTP GET request**
      </td>

      <td>
        The below properties within the request are what you'll need for the next step:\`\`\`\
        GET => /v1.1/requests/:request\_id

        \{\
        "signers":  Sent" webhook when a signature request is sent to your signer.
        2\. Learn how to process the webhook in order to include the right information in your email or SMS message.

        ## What you'll need to get started

        To get started wit\
        }

        ```


        ```
      </td>
    </tr>

    <tr>
      <td>
        **3. Send SMS or email**
      </td>

      <td>
        You can update signers via email or SMS that others have signed the request or update the status in your system.Example SMS:\
        Eric Smith has signed "Employment Agreement". One more signature is needed to complete the document.
      </td>
    </tr>
  </tbody>
</Table>

### 2. Catch a webhook when signature requests are completed by all signers

When the signature request is complete, you'll want to notify all signers via email or SMS with a link to review and download the signature request PDF. Ironclad Clickwrap will trigger a webhook called "Request Complete" to any webhooks currently configured on the account every time a signature request is completed.

Below are the steps to follow when a signature request is completed:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Step
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **1. Catch "Request Completed" webhook**
      </td>

      <td>
        An example of this webhook can be [found here](https://developer.pactsafe.com/docs/working-with-pactsafe-webhooks#section-request-complete).
      </td>
    </tr>

    <tr>
      <td>
        **2. Make HTTP GET request**
      </td>

      <td>
        The below properties within the request are what you'll need for the next step:\`\`\`\
        GET => /v1.1/requests/:request\_id

        \{\
        "signers":  Sent" webhook when a signature request is sent to your signer.
        2\. Learn how to process the webhook in order to include the right information in your email or SMS message.

        ## What you'll need to get started

        To get started wit\
        }

        ```


        ```
      </td>
    </tr>

    <tr>
      <td>
        **3. Shorten Signing URL**
      </td>

      <td>
        Next, you can take the signing URL (the `request_url` property) for your signer and shorten it using an API like Bit.ly or [Rebrandly](https://www.rebrandly.com).
      </td>
    </tr>

    <tr>
      <td>
        **4. Send SMS or email**
      </td>

      <td>
        Once you've shortened the link for each signer that's on the signature request, you can loop through each signer and trigger the email or SMS through your own provider passing in the mobile number or email address, shortened signing URL, and other metadata that you may want to leverage from PactSafe.Example SMS:\
        "PS Employment Agreement" has been accepted by all parties. Download your document here: [https://bit.ly/2131NDa](https://bit.ly/2131NDa)
      </td>
    </tr>
  </tbody>
</Table>