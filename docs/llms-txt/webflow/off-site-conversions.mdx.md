# Source: https://developers.webflow.com/browser/custom-goals/off-site-conversions.mdx

***

title: Off-site conversions
slug: custom-goals/off-site-conversions
description: Track conversions that happen outside your Webflow site
hidden: false
'og:title': Off-site conversions
'og:description': Track conversions that happen outside your Webflow site
-------------------------------------------------------------------------

Off-site conversions track actions that happen outside your Webflow site. Use them when your customer journey continues beyond your website — whether that's closing a deal over the phone, processing a signup in your CRM, or tracking an in-app purchase. Reporting an off-site conversion to Webflow lets you connect those downstream actions back to the optimizations visitors saw on your site.

<Note title="Enterprise plans only">
  Off-site conversion tracking is only available for Analyze and Optimize Enterprise plans.
</Note>

## How off-site conversions work

1. A visitor comes to your site
2. The [client-side API](/browser/custom-goals/off-site-conversions/setUserId) captures their user ID using `wf.setUserId()`
3. Later, the visitor converts outside your site (e.g., over the phone, in your CRM)
4. Your backend triggers the [server-side API](/browser/custom-goals/off-site-conversions/server-api) to send that conversion data to Webflow
5. Webflow validates the data (authorization token, timestamps, etc.)
6. The verified conversion is attributed to the optimization that the visitor viewed

<Info>
  Off-site conversions are imported in nightly batches, so conversions may not appear in Analyze/Optimize until the following day.
</Info>

## Tracking off-site conversions

Tracking off-site conversions requires creating custom goals on the Webflow site and implementing the client-side and server-side APIs in your backend:

<Steps>
  ### Part 1: Create a custom goal in Webflow

  These steps are completed by a Webflow user in your Webflow site dashboard. Learn more here: [Configure off-site conversions tracking](https://help-optimize.webflow.com/hc/en-us/articles/40810076772243-Track-offline-conversions#optimize-config).

  ### Part 2: Configure the backend

  Your development team needs to implement both the [client-side](/browser/custom-goals/off-site-conversions/setUserId) and [server-side](/browser/custom-goals/off-site-conversions/server-api) APIs on the backend to connect an off-site conversion to a custom goal in Webflow.
</Steps>

<Note>
  Every off-site conversion setup is different. Your exact configuration depends on your tools and system integrations. Use the following as building blocks.
</Note>

Before getting started, developers need:

* The off-site conversion authorization token
* The custom goal `event_name`
* Your Analyze/Optimize Account ID (provided in the generated code snippet for the custom goal)

<Warning title="Compliance considerations">
  Off-site conversion tracking involves sending user identifiers between your systems and Webflow. Before implementing:

  * Ensure you have appropriate consent mechanisms in place
  * Review your privacy policy to include disclosures about this data sharing
  * Consult with your legal and privacy teams about your specific obligations

  For guidance on protecting PII when calling `wf.setUserId()`, review our [recommended guidelines](/browser/custom-goals/off-site-conversions/setUserId#choosing-a-user-id).
</Warning>

## Example: Credit card signups

In this example, a visitor applies for a credit card on your site, but the actual approval happens later after a review process. Assumes you've created a custom goal in Webflow with the event name `application_accepted`.

<Steps>
  ### Step 1: Set the user ID (client-side)

  When the visitor submits their application:

  ```javascript
  wf.ready(function() {
      wf.setUserId('applicationId', '123456789');
  });
  ```

  ### Step 2: Send the conversion (server-side)

  When the application is approved, your backend sends the event:

  ```http
  POST /event HTTP/1.1
  Host: log.intellimize.co
  Authorization: ApiKey AbCdEf123456
  Content-Type: application/json

  {
      "customerId": "123456789",
      "eventName": "application_accepted",
      "userDomain": "applicationId",
      "userId": "123456789",
      "actionId": "23823940",
      "actionTimestamp": 1578316150000,
      "value": 149.99
  }
  ```
</Steps>

The conversion is now attributed to whatever optimization the visitor saw when they submitted their application.

## API reference

<CardGroup>
  <Card
    title="setUserId()"
    href="/browser/custom-goals/off-site-conversions/setUserId"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/OptimizeUser.svg" alt="" className="hidden dark:block" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/OptimizeUser.svg" alt="" className="block dark:hidden" />
            </>
        }
  >
    Client-side API to identify visitors with a known user ID
  </Card>

  <Card
    title="Server-side API"
    href="/browser/custom-goals/off-site-conversions/server-api"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Code.svg" alt="" className="hidden dark:block" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Code.svg" alt="" className="block dark:hidden" />
            </>
        }
  >
    HTTPS endpoint for sending off-site conversion data back to Webflow
  </Card>
</CardGroup>
