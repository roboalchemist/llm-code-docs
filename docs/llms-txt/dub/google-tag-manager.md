# Source: https://dub.co/docs/sdks/client-side/installation-guides/google-tag-manager.md

# Source: https://dub.co/docs/conversions/sales/google-tag-manager.md

# Source: https://dub.co/docs/conversions/leads/google-tag-manager.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dub.co/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Tag Manager

> Learn how to track lead conversion events with Google Tag Manager and Dub

<Note>
  Conversion tracking requires a [Business plan](https://dub.co/pricing)
  subscription or higher.
</Note>

When it comes to [conversion tracking](/conversions/quickstart), a `lead` event happens when a user performs an action that indicates interest in your product or service. This could be anything from:

* Signing up for an account
* Booking a demo meeting
* Joining a mailing list

<Frame>
  <img className="rounded-lg border border-gray-100" src="https://assets.dub.co/help/conversion-lead-event.png" alt="A diagram showing how lead events are tracked in the conversion funnel" />
</Frame>

In this guide, we will be focusing on tracking new user sign-ups for a SaaS application that uses Google Tag Manager to manage client-side tracking scripts.

## Prerequisites

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

## Set up Dub Analytics in Google Tag Manager

To track lead conversion events with Google Tag Manager, you'll need to install the Dub analytics script and configure lead tracking tags.

### Step 1: Add Dub Analytics Script to GTM

First, you'll need to add the Dub analytics script to your website using Google Tag Manager.

In your GTM workspace, navigate to the **Tags** section and click **New** to create a new tag.

<Frame>
  <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/google-tag-manager/gtm-new-tag.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=0cfbc7b1e007b875e07ce1f1dc515a2d" alt="GTM New Tag" width="1440" height="1024" data-og-width="1724" data-og-height="883" data-path="images/conversions/google-tag-manager/gtm-new-tag.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/google-tag-manager/gtm-new-tag.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=74ce03be3bf713f4c490b5dbfa94765c 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/google-tag-manager/gtm-new-tag.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=bcf8538cba389b7ffac4a54e161a64fc 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/google-tag-manager/gtm-new-tag.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=b804e8f707831306a5e0e9ce41aa7829 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/google-tag-manager/gtm-new-tag.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=262905c3f40f6c3b63ea36bda8d9e617 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/google-tag-manager/gtm-new-tag.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=7bb5ecd68dc271c4a3875102d9c33051 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/google-tag-manager/gtm-new-tag.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=33af6a4952dc13d40341b6dd8859d398 2500w" />
</Frame>

Select **Custom HTML** as the tag type and add the following code:

```html  theme={null}
<script>
  (function (c, n) {
    c[n] =
      c[n] ||
      function () {
        (c[n].q = c[n].q || []).push(arguments);
      };

    var methods = ["trackClick", "trackLead", "trackSale"];
    for (var i = 0; i < methods.length; i++) {
      (function (method) {
        c[n][method] = function () {
          var args = Array.prototype.slice.call(arguments);
          args.unshift(method);
          c[n].apply(null, args);
        };
      })(methods[i]);
    }

    var s = document.createElement("script");
    s.defer = 1;
    s.src = "https://www.dubcdn.com/analytics/script.conversion-tracking.js";
    s.setAttribute("data-publishable-key", "dub_pk_xxxxxxxx"); // Replace with your publishable key
    document.head.appendChild(s);
  })(window, "dubAnalytics");
</script>
```

<Warning>
  Make sure to replace `dub_pk_xxxxxxxx` with your actual [publishable
  key](https://dub.co/docs/api-reference/publishable-keys) from your Dub
  workspace (under the [Analytics settings
  page](https://app.dub.co/settings/analytics))
</Warning>

Configure the tag to fire on **All Pages** by setting the trigger to **All Pages - Page View**.

Name this tag "Dub Analytics Script" and save it.

### Step 2: Create User-Defined Variable for dub\_id Cookie

To read the `dub_id` cookie that Dub Analytics sets, you'll need to create a User-Defined Variable in Google Tag Manager.

In your GTM workspace, navigate to the **Variables** section and click **New** to create a new variable.

<Frame>
  <img src="https://mintcdn.com/dub/0qTWKCmxoHXve81d/images/conversions/google-tag-manager/gtm-dub-id-cookie-variable.png?fit=max&auto=format&n=0qTWKCmxoHXve81d&q=85&s=7f15c28151c737b96609a81e1068a614" alt="GTM Dub ID Cookie Variable" width="1440" height="1024" data-og-width="1708" data-og-height="819" data-path="images/conversions/google-tag-manager/gtm-dub-id-cookie-variable.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/0qTWKCmxoHXve81d/images/conversions/google-tag-manager/gtm-dub-id-cookie-variable.png?w=280&fit=max&auto=format&n=0qTWKCmxoHXve81d&q=85&s=c9092e7fd7bb6b045f9ea86f24a8e472 280w, https://mintcdn.com/dub/0qTWKCmxoHXve81d/images/conversions/google-tag-manager/gtm-dub-id-cookie-variable.png?w=560&fit=max&auto=format&n=0qTWKCmxoHXve81d&q=85&s=300d2834a7727cbcfe7db0b520d0cb85 560w, https://mintcdn.com/dub/0qTWKCmxoHXve81d/images/conversions/google-tag-manager/gtm-dub-id-cookie-variable.png?w=840&fit=max&auto=format&n=0qTWKCmxoHXve81d&q=85&s=a69ddecf24447d03eff638ca405a9532 840w, https://mintcdn.com/dub/0qTWKCmxoHXve81d/images/conversions/google-tag-manager/gtm-dub-id-cookie-variable.png?w=1100&fit=max&auto=format&n=0qTWKCmxoHXve81d&q=85&s=5d1c69cdf10ac39700fd854eb9062f76 1100w, https://mintcdn.com/dub/0qTWKCmxoHXve81d/images/conversions/google-tag-manager/gtm-dub-id-cookie-variable.png?w=1650&fit=max&auto=format&n=0qTWKCmxoHXve81d&q=85&s=5084890e0ffee44bf8f2d573efbf1234 1650w, https://mintcdn.com/dub/0qTWKCmxoHXve81d/images/conversions/google-tag-manager/gtm-dub-id-cookie-variable.png?w=2500&fit=max&auto=format&n=0qTWKCmxoHXve81d&q=85&s=754f0f7bf20cec565bc56c26a7f23129 2500w" />
</Frame>

Configure the variable with the following settings:

* **Variable Type**: Select **1st Party Cookie**
* **Cookie Name**: Enter `dub_id`
* **Variable Name**: Name it "Dub ID Cookie"

Click **Save** to create the variable.

<Note>
  This variable will automatically read the `dub_id` cookie value set by the Dub
  Analytics script. You can use this variable in your tags to pass the Dub ID
  when tracking conversion events.
</Note>

### Step 3: Tracking lead events

There are two ways to track lead events with Google Tag Manager:

* [Thank You Page Tracking (Recommended)](#option-1%3A-thank-you-page-tracking-recommended)
* [Form Submission Tracking](#option-2%3A-form-submission-tracking)

#### Option 1: Thank You Page Tracking (Recommended)

This method tracks leads when users land on a thank-you or success page after completing a form. This approach is more reliable as it's less likely to be blocked by ad blockers and provides better data accuracy.

Create a **Custom HTML** tag with the following code:

```html  theme={null}
<script>
  (function () {
    // Get query parameters from URL
    var params = new URLSearchParams(window.location.search);
    var email = params.get("email");
    var name = params.get("name");

    // Get dub_id from cookie using GTM variable
    var clickId = {{Dub ID Cookie}} || "";

    // Only track the lead event if email and clickId are present
    if (email && clickId) {
      dubAnalytics.trackLead({
        eventName: "Sign Up",
        customerExternalId: email,
        customerName: name || email,
        customerEmail: email,
        clickId: clickId,
      });
    }
  })();
</script>
```

<Note>
  **Important**: Make sure to pass along the `email` and `name` query parameters
  to the thank-you page so that the lead event can be attributed to the correct
  customer.
</Note>

Configure this tag to fire on specific pages by creating a **Page View** trigger with conditions:

* Trigger Type: **Page View**
* This trigger fires on: **Some Page Views**
* Add conditions like:
  * **Page URL** contains `/thank-you`
  * Or **Page Path** equals `/success`
  * Or whatever URL pattern matches your thank-you pages

Name this tag "Dub Lead Tracking - Thank You Page" and save it.

#### Option 2: Form Submission Tracking

This method tracks leads immediately when users submit forms on your website. Note that this approach may be less reliable due to ad blockers and timing issues.

Create a **Custom HTML** tag with the following code:

```html  theme={null}
<script>
  (function () {
    // Get form data - customize these selectors based on your form
    var name = document.getElementById("name")
      ? document.getElementById("name").value
      : "";
    var email = document.getElementById("email")
      ? document.getElementById("email").value
      : "";

    // Get dub_id from cookie using GTM variable
    var clickId = {{Dub ID Cookie}} || "";

    // Only track the lead event if email and clickId are present
    if (email && clickId) {
      dubAnalytics.trackLead({
        eventName: "Sign Up",
        customerExternalId: email,
        customerName: name || email,
        customerEmail: email,
        clickId: clickId,
      });
    }
  })();
</script>
```

<Note>
  **Important**: You'll need to customize the DOM selectors
  (`getElementById('name')`, `getElementById('email')`) to match your actual
  form field IDs or use different methods to capture the form data based on your
  website's structure.
</Note>

Configure this tag to fire on **Form Submission** by creating a new trigger:

* Trigger Type: **Form Submission**
* This trigger fires on: **Some Forms** (or **All Forms** if you want to track all form submissions)
* Add conditions to specify which forms should trigger lead tracking

Name this tag "Dub Lead Tracking - Form Submission" and save it.

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

## Testing your setup

To test your GTM setup, you can use the **Preview** mode in Google Tag Manager:

1. **Enable Preview Mode**: In your GTM workspace, click the **Preview** button in the top right corner
2. **Enter your website URL** and click **Connect**
3. **Test your chosen tracking method**:
   * **For Option 1 (Thank You Page)**: Navigate to your thank-you page with query parameters (e.g., `?email=test@example.com&name=Test User`)
   * **For Option 2 (Form Submission)**: Navigate to a page with a form and submit a test form
4. **Check the GTM debugger** to see if your tags are firing correctly

### Verify lead tracking

You can also verify that leads are being tracked by:

1. **Checking your browser's developer console** for any JavaScript errors
2. **Using the Network tab** to see if requests are being sent to Dub's analytics endpoint
3. **Viewing your Dub dashboard** to confirm that lead events are appearing in your analytics

### Common troubleshooting tips

* **Tag not firing**: Check that your triggers are configured correctly and that the conditions match your page structure
* **Missing publishable key**: Ensure you've replaced the placeholder with your actual publishable key
* **Query parameters missing** (Option 1): Ensure your form redirects to the thank-you page with the required query parameters
* **Form data not captured** (Option 2): Verify that your DOM selectors match your actual form field IDs or names

<Warning>
  **Client-Side Tracking Limitations**:

  * **Ad blockers** – Users with ad blockers may prevent tracking scripts from loading
  * **JavaScript disabled** – Events won't be tracked if users have JavaScript disabled
  * **Network issues** – Failed network requests won't retry automatically
  * **Privacy concerns** – Some users may block client-side tracking for privacy reasons

  For more accurate conversion tracking, consider using [server-side conversion tracking](/conversions/leads/introduction)
</Warning>

## View your conversions

Once you've completed the setup, all your tracked conversions will show up in [Dub Analytics](https://dub.co/analytics). We provide 3 different views to help you understand your conversions:

* **Time-series**: A [time-series view](https://app.dub.co/dub/analytics?view=timeseries) of the number clicks, leads and sales.

<Frame>
  <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=7380bc6120ade538b2b65eefdc76d3ed" alt="Time-series line chart" data-og-width="2400" width="2400" data-og-height="1260" height="1260" data-path="images/conversions/timeseries-chart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=430758e529cd22c5d28f976ee7da5379 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=9cf861c9aa7cf680f46ce32585303d2b 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=999b05a7805bd208b4649fc67a3b45e0 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=42baa1d9d42c26ed191875fef033128a 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=127ee673f66f2079f236985ec754416e 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=1c0696bb18043dd86388f03d09aed450 2500w" />
</Frame>

* **Funnel chart**: A [funnel chart view](http://app.dub.co/analytics?view=funnel) visualizing the conversion & dropoff rates across the different steps in the conversion funnel (clicks → leads → sales).

<Frame>
  <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=6275caafcfc3be6d8b498149222f225e" alt="Funnel chart view showing the conversion & dropoff rates from clicks → leads → sales" data-og-width="2400" width="2400" data-og-height="1260" height="1260" data-path="images/conversions/funnel-chart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=df57b14d04dd585c5236f6fcf16a4963 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=fc1689a06ce8ceecf1487faca8730d06 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=b69533d460a2bc95964d7f6d2e5f23f4 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=43b86431662a4c214a36fbf5405abb4a 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=687f900f0b8732301c43c8ee18ca7dd4 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=aed9e63c7fd1fb67c463920c73911cba 2500w" />
</Frame>

* **Real-time events stream**: A [real-time events stream](https://app.dub.co/events) of every single conversion event that occurs across all your links in your workspace.

<Frame>
  <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=c2467f9fa2e755f06b3e7b147fa0bd81" alt="The Events Stream dashboard on Dub" data-og-width="2400" width="2400" data-og-height="1260" height="1260" data-path="images/conversions/events-table.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=8e747ccc2f01015e014a9b4fbc98d588 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=4a0c65b37cf99181b712beb063e46dc2 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=345d5b0b36c6f2093ea7b6a97d73ff49 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=5deb48ab5e08bf2e31447fd32615c05e 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=33d6f27b5c067eb8586cfea15fe0a040 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=132a7592c8ecf518b31c043dad2093f4 2500w" />
</Frame>
