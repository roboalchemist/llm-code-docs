# Source: https://dub.co/docs/sdks/client-side/features/conversion-tracking.md

# Client-side conversion tracking

> Learn how to use the @dub/analytics script to track conversion events on the client-side

`@dub/analytics` is a client-side script for [tracking conversion events](/conversions/quickstart) with Dub.

By default, the script handles the detection of the `dub_id` query parameter and storing it as a first-party cookie:

<Frame>
  <img className="rounded-lg border border-gray-100" src="https://assets.dub.co/help/conversion-click-event.png" alt="A diagram showing how click events are tracked in the conversion funnel" />
</Frame>

Then, when a conversion event occurs (e.g. a user signs up for an account), you can check for the `dub_id` cookie and attribute the conversion to the original click by [tracking a lead event](/conversions/leads/introduction).

<Frame>
  <img className="rounded-lg border border-gray-100" src="https://assets.dub.co/help/conversion-lead-event.png" alt="A diagram showing how lead events are tracked in the conversion funnel" />
</Frame>

Finally, when the user completes a purchase (e.g. subscribing to a plan, purchasing a product, etc.), you can [track a sale event](/conversions/sales/introduction). Under the hood, Dub will automatically attribute the sale to the original link click.

<Frame>
  <img className="rounded-lg border border-gray-100" src="https://assets.dub.co/help/conversion-sale-event.png" alt="A diagram showing how sale events are tracked in the conversion funnel" />
</Frame>

## Quickstart

First, you'll need to enable conversion tracking for your Dub links to be able to start tracking conversions:

<Tip>
  If you're using [Dub Partners](/partners/quickstart), you can skip this step
  since partner links will have conversion tracking enabled by default.
</Tip>

<AccordionGroup>
  <Accordion title="Option 1: On a workspace-level">
    To enable conversion tracking for all future links in a workspace, you can do the following:
    To enable conversion tracking for all future links in a workspace, you can do the following:

    1. Navigate to your [workspace's Analytics settings page](https://app.dub.co/settings/analytics).
    2. Toggle the **Workspace-level Conversion Tracking** switch to enable conversion tracking for the workspace.

    <Frame>
      <img src="https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=f810945d33a42f45de3e06647b2cfd15" alt="Enabling conversion tracking for a workspace" data-og-width="3082" width="3082" data-og-height="1529" height="1529" data-path="images/conversions/enable-conversion-tracking-workspace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?w=280&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=514f7549b9a65a40fc4224ea68859e06 280w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?w=560&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=9c002882f7093efb76ae4be72e5f0312 560w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?w=840&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=d4da71527556174d30b71c0f9acdad6f 840w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?w=1100&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=c887363f92b258c3493267e2f4a3dd8e 1100w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?w=1650&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=e1b23eb5cf148df63105fdc572e6936b 1650w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?w=2500&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=1623f4206427342d87df828a17d66438 2500w" />
    </Frame>

    This option will enable conversion tracking in the [Dub Link Builder](https://dub.co/help/article/dub-link-builder) for all future links.
  </Accordion>

  <Accordion title="Option 2: On a link-level">
    If you don't want to enable conversion tracking for all your links in a workspace, you can also opt to enable it on a link-level.

    To enable conversion tracking for a specific link, open the [Dub Link Builder](https://dub.co/help/article/dub-link-builder) for a link and toggle the **Conversion Tracking** switch.

    <Frame>
      <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=4153d4a981e2a13324464ca3d30625cd" alt="Enabling conversion tracking for a link" data-og-width="2345" width="2345" data-og-height="908" height="908" data-path="images/conversions/enable-conversion-tracking.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=0984b50a4b6987e7bc4f8f3975559d0e 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=673093d978579d5cd19e22b2c786f6a4 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=94cb269be979162dd8bb74b2a5b614e9 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=4572ec2e03c96b50d1da93f8b3f04636 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=f0a017e718cc81ae682e89809e4dab25 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=078ec13ca0166c3b751d24271c1d2171 2500w" />
    </Frame>

    <Tip>
      You can also use the `C` keyboard shortcut when inside the link builder to
      quickly enable conversion tracking for a given link.
    </Tip>
  </Accordion>

  <Accordion title="Option 3: Via the API">
    Alternatively, you can also enable conversion tracking programmatically via the [Dub API](/api-reference/introduction). All you need to do is pass `trackConversion: true` when creating or updating a link:

    <CodeGroup>
      ```javascript Node.js theme={null}
      const link = await dub.links.create({
        url: "https://dub.co",
        trackConversion: true,
      });
      ```

      ```python Python theme={null}
      link = d.links.create(url="https://dub.co", track_conversion=True)
      ```

      ```go Go theme={null}
      link, err := d.Links.Create(ctx, &dub.CreateLinkRequest{
          URL: "https://dub.co",
          TrackConversion: true,
      })
      ```

      ```ruby Ruby theme={null}
      s.links.create_many(
        ::OpenApiSDK::Operations::CreateLinkRequest.new(
          url: "https://dub.co",
          track_conversion: true,
        )
      )
      ```
    </CodeGroup>
  </Accordion>
</AccordionGroup>

***

Then, you'll need to install the Dub client-side script and set up the necessary configuration for client-side conversion tracking:

<Steps>
  <Step title="Allowlist your site's domain">
    Then, you'll need to allowlist your site's domain to allow the client-side conversion events to be ingested by Dub.

    To do that, navigate to your [workspace's Analytics settings page](https://app.dub.co/settings/analytics) and add your site's domain to the **Allowed Hostnames** list.

    This provides an additional layer of security by ensuring only authorized domains can track conversions using your publishable key.

    <Frame>
      <img src="https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/allowed-hostnames.png?fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=da26eba128e89211e7bfd7cf46ba32e0" alt="Enabling conversion tracking for a workspace" data-og-width="2979" width="2979" data-og-height="2018" height="2018" data-path="images/conversions/allowed-hostnames.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/allowed-hostnames.png?w=280&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=58dbd9580cedff38a40a0f6ad6fe7188 280w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/allowed-hostnames.png?w=560&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=ace60f5cf513d21281be79ead24189e6 560w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/allowed-hostnames.png?w=840&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=33fff99044f2b77702dcc24ade6f67d7 840w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/allowed-hostnames.png?w=1100&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=134d6038e2ad8da21e39a7b8e797fee2 1100w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/allowed-hostnames.png?w=1650&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=b3051b73df5fdf2bd16b5db5aa4d34a5 1650w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/allowed-hostnames.png?w=2500&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=e3f56a578de0f460c8a77f08aa33e437 2500w" />
    </Frame>

    You can group your hostnames when adding them to the allow list:

    * `example.com`: Tracks traffic **only** from `example.com`.
    * `*.example.com`: Tracks traffic from **all subdomains** of `example.com`, but **not** from `example.com` itself.

    <Tip>
      When testing things out locally, you can add `localhost` to the **Allowed
      Hostnames** list temporarily. This will allow local events to be ingested by
      Dub. Don't forget to remove it once you're ready to go live!
    </Tip>
  </Step>

  <Step title="Generate your publishable key">
    Before you can track conversions on the client-side, you need to generate a [publishable key](/api-reference/publishable-keys) from your Dub workspace.

    To do that, navigate to your [workspace's Analytics settings page](https://app.dub.co/settings/analytics) and generate a new publishable key under the **Publishable Key** section.

    <Frame>
      <img src="https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=76add1f30a997ba897f10acdc21b51b5" alt="Enabling conversion tracking for a workspace" data-og-width="2985" width="2985" data-og-height="2021" height="2021" data-path="images/conversions/publishable-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?w=280&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=f0f995d217914793d81c0a42ccda502a 280w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?w=560&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=62a390272e2b24b6ae8cf3ba98dac66f 560w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?w=840&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=cdb86db75f933f33be21d4a0e8293227 840w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?w=1100&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=ab9b7ec6577587e197e1fefeaa250216 1100w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?w=1650&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=ab5f37e61472d2c6118f7b640a5fdb50 1650w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?w=2500&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=6d83d47d0988ee0d895606f8b2e683c6 2500w" />
    </Frame>
  </Step>

  <Step title="Install @dub/analytics package">
    Next, install the Dub analytics script in your application.

    You can install the `@dub/analytics` script in several different ways:

    <CardGroup>
      <Card title="React" icon="react" href="/sdks/client-side/installation-guides/react" horizontal />

      <Card title="Manual installation" icon="browser" href="/sdks/client-side/installation-guides/manual" horizontal />

      <Card
        title="Framer"
        icon={
    <svg
      width="74"
      height="111"
      viewBox="0 0 74 111"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      className="w-7 h-7"
    >
      <path d="M0 0H73.8374V36.9892H36.9187L0 0Z" fill="#eb5611" />
      <path d="M0 36.989H36.9187L73.8374 73.9796H0V36.989Z" fill="#eb5611" />
      <path d="M0 73.9797H36.9187V110.97L0 73.9797Z" fill="#eb5611" />
    </svg>
  }
        href="/sdks/client-side/installation-guides/framer"
        horizontal
      />

      <Card title="Shopify" icon="shopify" href="/sdks/client-side/installation-guides/shopify" horizontal />

      <Card title="WordPress" icon="wordpress" href="/sdks/client-side/installation-guides/wordpress" horizontal />

      <Card title="Webflow" icon="webflow" href="/sdks/client-side/installation-guides/webflow" horizontal />

      <Card title="Google Tag Manager" icon="google" href="/sdks/client-side/installation-guides/google-tag-manager" horizontal />
    </CardGroup>

    You must configure the **publishable key** you generated in step 1 when installing the analytics script. Without this key, client-side conversion tracking will not work.

    <CodeGroup>
      ```typescript React theme={null}
      import { Analytics as DubAnalytics } from '@dub/analytics/react';

      export default function RootLayout({
        children,
      }) {
        return (
          <html lang="en">
            <body className={inter.className}>{children}</body>
            <DubAnalytics
              ...
              publishableKey="dub_pk_xxxxxxxx" // Replace with your publishable key
            />
          </html>
        );
      }
      ```

      ```html Other theme={null}
      <script>
        !(function (c, n) {
          c[n] =
            c[n] ||
            function () {
              (c[n].q = c[n].q || []).push(arguments);
            };
          ["trackClick", "trackLead", "trackSale"].forEach(
            (t) => (c[n][t] = (...a) => c[n](t, ...a))
          );
          var s = document.createElement("script");
          s.defer = 1;
          s.src = "https://www.dubcdn.com/analytics/script.conversion-tracking.js";
          s.setAttribute("data-publishable-key", "dub_pk_xxxxxxxx"); // Replace with your publishable key
          document.head.appendChild(s);
        })(window, "dubAnalytics");
      </script>
      ```
    </CodeGroup>
  </Step>
</Steps>

## Client-side lead tracking

Once the analytics script is installed, you can start tracking lead events in your application on the client-side.

### Track leads from URL query parameters

If you redirect users to a thank-you page after a successful action, you can track leads by reading query parameters from the URL.

<CodeGroup>
  ```typescript React theme={null}
  import { useAnalytics } from "@dub/analytics/react";
  import { useEffect } from "react";

  export function ThankYouPage() {
    const { trackLead } = useAnalytics();

    useEffect(() => {
      // Get query parameters from URL
      const params = new URLSearchParams(window.location.search);
      const email = params.get("email");
      const name = params.get("name");

      if (email) {
        // Track the lead event
        trackLead({
          eventName: "Sign Up",
          customerExternalId: email, // can also be customer email
          customerName: name || undefined,
          customerEmail: email,
        });
      }
    }, [trackLead]);

    return <div>Thank you for signing up!</div>;
  }
  ```

  ```html HTML / Other Frameworks theme={null}
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Thank You</title>
    </head>
    <body>
      <div>Thank you for signing up!</div>

      <script>
        // Get query parameters from URL
        const params = new URLSearchParams(window.location.search);
        const email = params.get("email");
        const name = params.get("name");

        if (email) {
          // Track the lead event
          dubAnalytics.trackLead({
            eventName: "Sign Up",
            customerExternalId: email, // can also be customer email
            customerName: name || undefined,
            customerEmail: email,
          });
        }
      </script>
    </body>
  </html>
  ```
</CodeGroup>

### Track leads from form submissions

You can also track leads directly when users submit a form on your website.

<CodeGroup>
  ```typescript React theme={null}
  import { useAnalytics } from "@dub/analytics/react";
  import { useState } from "react";

  export function SignUpForm() {
    const { trackLead } = useAnalytics();
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const handleSubmit = (e: React.FormEvent) => {
      e.preventDefault();

      // Track the lead event
      trackLead({
        eventName: "Sign Up",
        customerExternalId: email,
        customerName: name,
        customerEmail: email,
      });
    };

    return (
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <button type="submit">Sign Up</button>
      </form>
    );
  }
  ```

  ```html HTML / Other Frameworks theme={null}
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Sign Up</title>
    </head>
    <body>
      <form id="signupForm">
        <input type="text" id="name" required />
        <input type="email" id="email" required />
        <button type="submit">Sign Up</button>
      </form>

      <script>
        document
          .getElementById("signupForm")
          .addEventListener("submit", function (e) {
            e.preventDefault();

            const name = document.getElementById("name").value;
            const email = document.getElementById("email").value;

            // Track the lead event
            dubAnalytics.trackLead({
              eventName: "Sign Up",
              customerExternalId: email,
              customerName: name,
              customerEmail: email,
            });
          });
      </script>
    </body>
  </html>
  ```
</CodeGroup>

Here's the full list of attributes you can pass when sending a lead event:

| Property             | Required | Description                                                                                                                                                                                                                                                                                                                                                                       |
| :------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `clickId`            | **Yes**  | The unique ID of the click that the lead conversion event is attributed to. You can read this value from `dub_id` cookie. If an empty string is provided (i.e. if you're using [tracking a deferred lead event](/conversions/leads/deferred)), Dub will try to find an existing customer with the provided `customerExternalId` and use the `clickId` from the customer if found. |
| `eventName`          | **Yes**  | The name of the lead event to track. Can also be used as a unique identifier to associate a given lead event for a customer for a subsequent sale event (via the `leadEventName` prop in `/track/sale`).                                                                                                                                                                          |
| `customerExternalId` | **Yes**  | The unique ID of the customer in your system. Will be used to identify and attribute all future events to this customer.                                                                                                                                                                                                                                                          |
| `customerName`       | No       | The name of the customer. If not passed, a random name will be generated (e.g. "Big Red Caribou").                                                                                                                                                                                                                                                                                |
| `customerEmail`      | No       | The email address of the customer.                                                                                                                                                                                                                                                                                                                                                |
| `customerAvatar`     | No       | The avatar URL of the customer.                                                                                                                                                                                                                                                                                                                                                   |
| `mode`               | No       | The mode to use for tracking the lead event. `async` will not block the request; `wait` will block the request until the lead event is fully recorded in Dub; `deferred` will defer the lead event creation to a subsequent request.                                                                                                                                              |
| `metadata`           | No       | Additional metadata to be stored with the lead event. Max 10,000 characters.                                                                                                                                                                                                                                                                                                      |

**When to track leads**

You should track lead events after successful user actions such as:

* User registration or account creation
* Newsletter subscription
* Contact form submission
* Demo request or trial signup
* Download of gated content

Ensure the event is triggered **only after the backend confirms the action was completed successfully**. This guarantees accurate lead data and prevents false or incomplete entries.

## Client-side sale tracking

Once the analytics script is installed, you can start tracking sale events in your application on the client-side.

### Track sales from URL query parameters

If you redirect users to a confirmation page after a successful purchase, you can track sales by reading query parameters from the URL.

<CodeGroup>
  ```typescript React theme={null}
  import { useAnalytics } from "@dub/analytics/react";
  import { useEffect } from "react";

  export function OrderConfirmationPage() {
    const { trackSale } = useAnalytics();

    useEffect(() => {
      // Get query parameters from URL
      const params = new URLSearchParams(window.location.search);
      const customerId = params.get("customer_id");
      const amount = params.get("amount");
      const invoiceId = params.get("invoice_id");

      if (customerId && amount) {
        // Track the sale event
        trackSale({
          eventName: "Purchase",
          customerExternalId: customerId, // can also be customer email
          amount: parseInt(amount), // Amount in cents
          invoiceId: invoiceId || undefined,

          // Additional props for direct sale tracking (without prior lead event):
          // clickId: "cm3w...", // Read from dub_id cookie
          // customerName: "John Doe",
          // customerEmail: "john@example.com",
          // customerAvatar: "https://example.com/avatar.jpg",
        });
      }
    }, [trackSale]);

    return <div>Thank you for your purchase!</div>;
  }
  ```

  ```html HTML / Other Frameworks theme={null}
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Order Confirmation</title>
    </head>
    <body>
      <div>Thank you for your purchase!</div>

      <script>
        // Get query parameters from URL
        const params = new URLSearchParams(window.location.search);
        const customerId = params.get("customer_id");
        const amount = params.get("amount");
        const invoiceId = params.get("invoice_id");

        if (customerId && amount) {
          // Track the sale event
          dubAnalytics.trackSale({
            eventName: "Purchase",
            customerExternalId: customerId, // can also be customer email
            amount: parseInt(amount), // Amount in cents
            invoiceId: invoiceId || undefined,

            // Additional props for direct sale tracking (without prior lead event):
            // clickId: "cm3w...", // Read from dub_id cookie
            // customerName: "John Doe",
            // customerEmail: "john@example.com",
            // customerAvatar: "https://example.com/avatar.jpg",
            // currency: "usd",
            // paymentProcessor: "stripe",
            // metadata: { plan: "pro" },
          });
        }
      </script>
    </body>
  </html>
  ```
</CodeGroup>

### Track sales from form submissions

You can also track sales directly when users complete a checkout form on your website.

<CodeGroup>
  ```typescript React theme={null}
  import { useAnalytics } from "@dub/analytics/react";
  import { useState } from "react";

  export function CheckoutForm() {
    const { trackSale } = useAnalytics();
    // …
  }
    const handleSubmit = (e: React.FormEvent) => {
      e.preventDefault();

      // Track the sale event
      trackSale({
        eventName: "Purchase",
        customerExternalId: "cus_RBfbD57H", // can also be customer email
        amount: 5000, // $50.00
        invoiceId: "in_1MtHbELkdIwH",

        // For direct sale tracking (without prior lead event):
        // clickId: "cm3w...", // Read from dub_id cookie
        // customerName: "John Doe",
        // customerEmail: "john@example.com",
        // customerAvatar: "https://example.com/avatar.jpg",
      });
    };

    return (
      <form onSubmit={handleSubmit}>
        ...
      </form>
    );
  }
  ```

  ```html HTML / Other Frameworks theme={null}
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Checkout</title>
    </head>
    <body>
      <form id="checkoutForm">
        ...
        <button type="submit">Checkout</button>
      </form>

      <script>
        document.getElementById("checkoutForm").addEventListener("submit", function (e) {
          e.preventDefault();

          // Track the sale event
          dubAnalytics.trackSale({
            eventName: "Purchase",
            customerExternalId: "cus_RBfbD57H", // can also be customer email
            amount: 5000, // $50.00
            invoiceId: "in_1MtHbELkdIwH",

            // Additional props for direct sale tracking (without prior lead event):
            // clickId: "cm3w...", // Read from dub_id cookie
            // customerName: "John Doe",
            // customerEmail: "john@example.com",
            // customerAvatar: "https://example.com/avatar.jpg",
            // currency: "usd",
            // paymentProcessor: "stripe",
            // metadata: { plan: "pro" },
          });
        });
      </script>
    </body>
  </html>
  ```
</CodeGroup>

Here are the properties you can include when sending a sale event:

| Property             | Required | Description                                                                                                                                                |
| :------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `customerExternalId` | **Yes**  | The unique ID of the customer in your system. Will be used to identify and attribute all future events to this customer.                                   |
| `amount`             | **Yes**  | The amount of the sale in cents.                                                                                                                           |
| `paymentProcessor`   | No       | The payment processor that processed the sale (e.g. [Stripe](/conversions/sales/stripe), [Shopify](/conversions/sales/shopify)). Defaults to "custom".     |
| `eventName`          | No       | The name of the event. Defaults to "Purchase".                                                                                                             |
| `invoiceId`          | No       | The invoice ID of the sale. Can be used as a idempotency key – only one sale event can be recorded for a given invoice ID.                                 |
| `currency`           | No       | The currency of the sale. Defaults to "usd".                                                                                                               |
| `metadata`           | No       | An object containing additional information about the sale.                                                                                                |
| `clickId`            | No       | **\[For direct sale tracking]**: The unique ID of the click that the sale conversion event is attributed to. You can read this value from `dub_id` cookie. |
| `customerName`       | No       | **\[For direct sale tracking]**: The name of the customer. If not passed, a random name will be generated.                                                 |
| `customerEmail`      | No       | **\[For direct sale tracking]**: The email address of the customer.                                                                                        |
| `customerAvatar`     | No       | **\[For direct sale tracking]**: The avatar URL of the customer.                                                                                           |

**When to track sale**

Track sale events only after a user successfully completes a purchase or payment-related action, such as:

* Completing a checkout or order
* Subscription payment
* Invoice payment
* Any paid trial or demo conversion

Ensure the event is triggered **only after the backend confirms the payment was successful**. This guarantees accurate sale data and prevents false or incomplete entries.
