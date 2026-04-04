# Source: https://www.courier.com/docs/platform/analytics/custom-domain-tracking.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Domain Tracking

> Use a custom tracking domain instead of ct0.app for branded link tracking in email notifications.

<Note>
  **Availability**: Custom Domain Tracking is available for Enterprise customers. Contact [Courier Support](mailto:support@courier.com) or your account team for access.
</Note>

By default, Courier uses `ct0.app` for link tracking. Enterprise customers can use a custom tracking domain (e.g., `tracking.mywebsite.com`) for a more branded experience and improved deliverability.

## Why Use Custom Domain Tracking?

* **Brand consistency**: Links in emails display your domain instead of a third-party tracker
* **Improved trust**: Recipients are more likely to click links from a recognizable domain
* **Better deliverability**: Custom domains can help avoid spam filters that flag common tracking domains

## Setup Process

Custom domain tracking setup requires coordination with Courier Support.

<Steps>
  <Step title="Provide your tracking URL">
    Contact Courier Support with your desired tracking subdomain, typically something like `tracking.mywebsite.com`.
  </Step>

  <Step title="Add DNS records">
    Courier will provide two DNS records to add:

    1. **Certificate validation record**: Required for Courier's infrastructure to accept requests from your domain. Courier Support will provide the specific values.

    2. **CNAME record**: Point your tracking subdomain to Courier's tracking infrastructure.

    ```
    tracking.mywebsite.com  CNAME  tracking.ct0.app
    ```
  </Step>

  <Step title="Activation">
    After DNS records propagate, Courier Support will enable the feature for your workspace. Once activated, all tracked links in your notifications will use your custom domain.
  </Step>
</Steps>

## Verification

After setup, test by sending a notification with tracked links. The links should resolve through your custom domain rather than `ct0.app`.
