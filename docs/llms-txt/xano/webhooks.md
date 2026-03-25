# Source: https://docs.xano.com/building-backend-features/webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Webhooks

> Webhooks are specialized API endpoints designed to be triggered based on other events

<Info>
  **Quick Summary**

  Webhooks are API endpoints specifically designed for one system to **automatically push** information to another when a specific **event** happens. For example, Slack provides you with a webhook URL. This URL is ready and listening, much like your own API endpoint.

  But here’s the key difference:

  1. Something like a **form submission endpoint** receives data because the *user initiated* the request (e.g., they clicked 'Submit').

  2. The **Slack webhook** receives data because *your server*, after processing the form (the **event**), *initiated* a new request, automatically pushing the form details *to* Slack's URL. Slack didn't ask for it; your system sent it because something happened.

  You'd build webhooks in Xano typically to ingest information ***pushed*** from other places — like if a user pays for something via Stripe, or they perform an action in your app that you want to log.
</Info>

<Frame>
  <iframe width="609" height="342" src="https://www.youtube.com/embed/y5mmGCy7q1A" title="Building Webhooks | A Practical Example using Typeform" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

## Building Webhooks

<Steps>
  <Step title="Create a new API endpoint with a POST method">
    1. Click + Add API Endpoint from inside one of your API groups.

    2. Choose **Custom API Endpoint** and fill in the details. Make sure to select **POST** as the verb.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/ea5a3112-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=a4224c767e6277b9827a960eda8ffff8" width="435" height="77" data-path="images/ea5a3112-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Add a Get All Raw Input function">
    Typically, webhooks need to be able to dynamically process data that might look a little different between requests. So, we use [Get All Raw Input](/the-function-stack/functions/utility-functions#get-all-raw-input) to make sure that we aren't confined to just the inputs that are defined in the inputs section.

    You'll need to choose the encoding, or the format, of the data being sent to this endpoint. This will more often than not be JSON.

    While Get All Raw Input offers flexibility, always check the documentation of the service *sending* the webhook. They will specify the structure (schema) of the data payload you should expect.
  </Step>

  <Step title="Process the output of Get All Raw Input as needed">
    From here, the process is completely unique to whatever data is being sent to the webhook, and what you need to do with it.

    **Examples:**

    * Store the data in a database table using [Add Record](/the-function-stack/functions/database-requests/add-record)

    * If the webhook is receiving a list of items, loop against them using [For Each Loop](/the-function-stack/functions/data-manipulation/loops#for-each-loop)

    * Transform or manipulate the data using [Filters](/the-function-stack/filters) or an [Expression](/the-function-stack/data-types/expression)

    * Send the data to another service, such as an analytics platform, using an [External API Request](/the-function-stack/functions/apis-and-lambdas/external-api-request)

    * Begin a more in-depth process using a combination of the above to perform multiple actions, such as transforming data, storing it, and sending [Emails](/building-backend-features/emails)
  </Step>
</Steps>

## Securing your Webhooks

Just like any other API endpoint you're building, it's important to ensure that they are built securely. Webhooks have some more specific-to-them ways that they are usually kept locked up.

<Steps>
  <Step title="Signature Verification (recommended)">
    The service you're accepting requests from may offer signature verification. At a high level, this means that you would cross-check the signature they sent with your own calculated signature, using a private key that only you and the service are aware of, and ensure that they match.

    <Tip>
      **If they match**: The request is verified and you can proceed.
    </Tip>

    <Warning>
      **If they don't match**: you should deny the request
    </Warning>

    In general, this process follows a typical flow:

    * Extract the signature provided in the request headers

    * Ensure you have a raw, unaltered copy of the request body (which you do using Get All Raw Input)

    * Use the proper [Security](/the-function-stack/filters/security) filter (such as [hmac\_sha256 / hmac384 / hmac512](/the-function-stack/filters/security#hmac_sha256-hmac384-hmac512)) to encode your own signature, and ensure that it matches with the one you extracted from the request.
  </Step>

  <Step title="Check a static token provided in the headers">
    Similar to how standard [User Authentication & User Data](/building-backend-features/user-authentication-and-user-data) works, some services may just send an API key or bearer token as part of the request header. You'll want to compare this against your own stored key and ensure that they match.

    It's also good practice to rotate this token on a regular basis to ensure that it is not compromised.
  </Step>
</Steps>

<Tip>
  **Tip**

  Use [Middleware](/building/logic/middleware) or [Custom Functions](/building/logic/custom-functions) to build your webhook verification and quickly deploy it across multiple function stacks.
</Tip>


Built with [Mintlify](https://mintlify.com).