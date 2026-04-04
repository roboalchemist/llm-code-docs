# Source: https://documentation.onesignal.com/docs/en/links.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# URLs, links, & deep links

> Learn how to set up and use URLs, links, and deep links in OneSignal messages including Push, Email, In-App Messages, and SMS.

## Overview

You can include URLs and deep links in Push, Email, In-App Messages, and SMS. This guide explains how to set up these links correctly, how link tracking works, and when to use deep links.

<Note>
  For more advanced linking like custom schemes or app routing, see our [Deep Linking](./deep-linking) guide.
</Note>

## Channel linking options

Depending on the messaging channel you are using, you can set up links in the following ways.

<Tabs>
  <Tab title="Push Notifications">
    ## Launch URL

    Use the Launch URL to open a link when the notification is clicked. This typically opens in the default browser and should start with `https://`.

    <Info>
      To use `http://` URLs with Apple devices, you must setup the [NSAppTransportSecurity](https://developer.apple.com/documentation/bundleresources/information_property_list/nsapptransportsecurity) property in your app's `Info.plist` file.
    </Info>

    If you’re using a mobile deep link like `your-custom-scheme://`, results may vary. See [Deep Linking](./deep-linking).

    ### Targeting multiple platforms

    If you send a single message to both web and mobile users, use:

    * `url` — for general targeting across all platforms.
    * `web_url` — for web push Subscriptions.
    * `app_url` — for mobile Subscriptions.

    <Frame caption="OneSignal Dashboard – Launch URL Field">
      <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/3176c50-Screenshot_2024-06-04_at_10.18.55_AM.png?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=90aaca88db7caaccc840ea32d442d4c1" width="1228" height="394" data-path="images/docs/3176c50-Screenshot_2024-06-04_at_10.18.55_AM.png" />
    </Frame>

    ## Additional data

    Instead of Launch URL, you can use the **Additional Data** field (`data` in the API) to send custom data with your push and handle this data in your app using the SDK's Notification Click Listener via the `additionalData` property. This might be a better option than Launch URL to provide more flexibility.

    <Frame caption="Send a URL to read within your app via the Additional Data field.">
      <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/b65f0d4-Screenshot_2024-06-04_at_10.27.12_AM.png?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=b9b003ba3969c173db361e1f52d37360" width="1470" height="278" data-path="images/docs/b65f0d4-Screenshot_2024-06-04_at_10.27.12_AM.png" />
    </Frame>
  </Tab>

  <Tab title="Email">
    <Note>
      For unsubscribe links, see [Unsubscribe Links & Email Subscriptions](./unsubscribe-links-email-subscriptions) for details.
    </Note>

    <Frame caption="Click Activity table for trackable links">
      <img src="https://mintcdn.com/onesignal/3PUtCumasMeFG2p0/images/docs/link_tracking.png?fit=max&auto=format&n=3PUtCumasMeFG2p0&q=85&s=318dab483003dac8e1203ab75b5c2756" width="957" height="312" data-path="images/docs/link_tracking.png" />
    </Frame>

    OneSignal automatically tracks user clicks of links within your emails. This tracking is performed at two levels:

    * **Per email**, where any click of any link is counted per email or email template. This is used to calculate message-level click-through rate and click-to-open rate. This is reported as both:
      * **Total clicks**, where the same user clicking the same link in the same delivered email multiple times is counted multiple times
      * **Unique clicks**, where the same user licking the same link in the same delivered email multiple times is counted once

    * **Per link per email**, where any click of any link is counted for that specific link within an email or email template. This is also reported as total and unique counts. OneSignal will calculate link-level click stats for the first 30 links found in each email.

    Tracking email link clicks requires changing the URL to capture the event, then redirecting the user back to the original URL you set. This happens almost instantly but may cause unexpected behavior, particularly with deep links. For example, a URL like:

    `https://some-domain.com/the-page`

    will be obfuscated to something like:

    `https://some-domain/c/eJxU0D2uGzEMBODTrDoZJPW3...`

    It will then immediately redirect to the intended URL.

    This behavior is normal and nearly invisible to users. However, it may have unexpected behavior when using [Deep links](./deep-linking) and may require you to [Disable Link Click Tracking](#disable-link-click-tracking).

    ### Enable link click tracking

    This feature is enabled by default and in most cases does not require further configuration. As long as **Track link clicks** is checked for your email or email template, OneSignal will track link clicks.

    In some cases, especially if you are constructing links with Liquid syntax we may not detect a link and track it automatically. You can explicitly tell us to track a link using Liquid like so:

    ```
    {{ 'https://onesignal.com' | track_link }}
    ```

    ### Disable link click tracking

    To disable click tracking for all links in an entire email:

    * Dashboard: Uncheck **Track link clicks**.
    * API: Set `disable_email_click_tracking: true`.

    <Frame caption="Track link clicks is disabled.">
      <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/8d3292a5cb0b24a4b5bc8f9ae1074f513c3fed310045a6b6c534b94e344a401b-Screenshot_2025-02-14_at_11.50.38_AM.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=889e3b62608b8b6a982d841191bcae0a" width="1756" height="718" data-path="images/docs/8d3292a5cb0b24a4b5bc8f9ae1074f513c3fed310045a6b6c534b94e344a401b-Screenshot_2025-02-14_at_11.50.38_AM.png" />
    </Frame>

    To disable an individual link from being tracked while **Track link clicks** is enabled, you can explicitly opt out of individual links using Liquid like so:

    ```
    {{ 'https://some-domain.com/the-page' | do_not_track_link }}
    ```

    ### View Click Tracking Statistics

    Email-level click tracking statistics are displayed at the top of the page for each email and email template in the Click-Through Rate card.

    Link-level click tracking statistics are displayed in the Click Activity panel for each email and email template. The first 30 links will be tracked, with the remainder summarized as “All other links.”

    <Warning>
      * Disabling tracking means no click data (CTR will show "N/A") in the [Email Message Reports](./email-message-reports) Click-Through Rate.
      * All links will be untracked—no selective disabling.
    </Warning>
  </Tab>

  <Tab title="In-App Messages">
    In-app message image, button, and background elements have URL [In-App Click Actions](./iam-click-actions) and HTML in-app messages have the `openUrl` method in the [In-App JS Library](./in-app-message-api).

    Depending on how your links are setup, you may need to deep link via the **Action Name** following the [Deep Linking](./deep-linking) guide.
  </Tab>

  <Tab title="SMS">
    OneSignal provides trackable shortened links that you can add to any SMS.

    **Dashboard URL Shortener**

    To create a trackable shortened URL, click the **Insert Trackable Link** link beneath the message input box, and enter your link into the modal:

    <Frame caption="A modal for inputting the trackable link">
      <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/trackable_sms_1.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=1a56512d4801622cdb3cbf03e48e4c65" width="1198" height="781" data-path="images/docs/trackable_sms_1.png" />
    </Frame>

    Click the **Insert trackable link** button to add the short link to your message:

    <Frame caption="An example of a message preview with a trackable link.">
      <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/trackable_sms_2.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=6906052ad77fdbef31a3ed5a406d4a69" width="1519" height="897" data-path="images/docs/trackable_sms_2.png" />
    </Frame>

    In the message preview, the link will appear in your message as the placeholder like `1sgnl.co/XXXX`, which will be replaced with a trackable link for each user when the message is sent:

    <Frame caption="An example of a trackable link as it appears on a device.">
      <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/trackable_sms_3.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=627e22caedd413d193a403aef6070b68" width="1242" height="1044" data-path="images/docs/trackable_sms_3.png" />
    </Frame>

    **API URL Shortener**

    To send trackable links via our API, please see our [SMS create message API reference](/reference/sms).
  </Tab>
</Tabs>

***

## Dynamic URLs

You can create custom, user-specific URLs with [Liquid Syntax](./using-liquid-syntax) and data from:

* User Properties (e.g., `external_id`, `email`)
* Tags stored in OneSignal
* `custom_data` sent via the API
* Custom Events (from Journeys)

This enables personalized links in your messages that lead users to content tailored just for them.

<Tabs>
  <Tab title="User Properties">
    Inject values like `external_id` or `email` directly into URLs.

    Example:

    ```
      https://yourdomain.com/profile/user={{subscription.external_id}}
    ```

    If the user's `external_id` is 12345, the final URL will be:

    ```
    https://yourdomain.com/profile/user=12345
    ```

    Similarly:

    ```
    https://yourdomain.com/profile/email={{subscription.email}}
    ```

    If the user has an email address of `john@example.com`, the final URL will be:

    ```
    https://yourdomain.com/profile/email=john@example.com
    ```
  </Tab>

  <Tab title="Data Tags">
    Reference user tags stored in OneSignal.

    Example:

    ```
    https://yourdomain.com/topic/{{tag_key}}
    ```

    If the user has a tag `tag_key` with a value of `technology`, the final URL will be:

    ```
    https://yourdomain.com/topic/technology
    ```

    If the tag `tag_key` is not set, the URL will be:

    ```
    https://yourdomain.com/topic/
    ```

    Use the `default` filter to set a default value if the tag is not set.

    ```
    https://yourdomain.com/topic/{{tag_key | default: 'unknown'}}
    ```

    If the `tag_key` is not set, the URL with the `default` filter will become:

    ```
    https://yourdomain.com/topic/unknown
    ```
  </Tab>

  <Tab title="custom_data">
    Using our Create message APIs and Templates. You can set the URL in the template with specific Liquid syntax to reference the `custom_data` object in the API request.

    Example template URL:

    ```
    https://yourdomain.com/invoice={{message.custom_data.invoice_number}}
    ```

    Example API request with `custom_data`:

    ```json  theme={null}
    {
        "template_id": "YOUR_TEMPLATE_ID",
        "custom_data": {
            "invoice_number": "12345"
        }
    }
    ```

    The final URL will be:

    ```
    https://yourdomain.com/invoice=12345
    ```
  </Tab>

  <Tab title="Custom Events">
    Personalize URLs using **Custom Events** captured in **Journeys**.\
    You can directly reference event properties or assign the event to a variable for cleaner syntax.

    **Reference event properties directly:**

    ```
    https://yourdomain.com/order/{{ journey.event.purchase.properties.order_id }}
    ```

    If the most recent `purchase` event included `"order_id": "98765"`, the final URL will be:

    ```
    https://yourdomain.com/order/98765
    ```

    **Or assign the event for readability:**

    ```
    {% assign event = journey.event.purchase %}
    https://yourdomain.com/order/{{ event.properties.order_id }}
    ```

    **Access the most recent stored event in the Journey:**

    ```
    https://yourdomain.com/product/{{ journey.last_event.properties.product_id | default: 'unknown' }}
    ```

    **Event names with spaces or special characters (hash notation):**

    ```
    https://yourdomain.com/status/{{ journey.event["order status"].properties.current_status }}
    ```

    <Note>
      Custom Events can be referenced only in **Templates used within Journeys**.\
      Use <code>journey.first\_event</code>, <code>journey.last\_event</code>, or <code>journey.event.\<name></code> to access event data directly in Liquid, or assign them to a variable for reuse.
    </Note>
  </Tab>
</Tabs>

**Best practices**:

* Only set data tags, custom event properties, or `custom_data` for parts of the URL. Don't include the protocol (`https://` or `your-app-scheme://`) and domain in the substituted values.
* Use the `default` filter to set a fallback if a value is not present.

<Note>
  For more details, see:

* [Message Personalization](./message-personalization)
* [Using Liquid Syntax](./using-liquid-syntax)
</Note>

***

## UTM Parameters

UTM parameters help track the performance of message campaigns by appending `source`, `medium`, and `campaign` details to URLs. Simply add your UTM parameters directly into the URLs of your messages.

You can have OneSignal automatically add UTMs to push notification Launch URLs sent from the Dashboard.

<Accordion title="Automatic UTMs for push notifications." icon="circle-chevron-down">
  Navigate to **Settings > Push & In-app > UTM Settings** and **Turn on automated UTM tagging**.

  Once enabled, OneSignal appends the provided values that you can edit:

* **Source** = `utm_source` defaults to `onesignal`
* **Medium** = `utm_medium` defaults to `push`
* **Campaign** = `utm_campaign` defaults to `{{ sendDate }}-{{ title }}`
  * `sendDate`: Date sent
  * `title`: First 15 alphanumeric characters, underscores, or hyphens from the message title

  Example:

  ```
  https://test.com?utm_source=onesignal&utm_medium=push&utm_campaign=2020-06-03-sale-today
  ```

  <Warning>
    UTM tagging from the dashboard does **not** work with:

    * Emails, SMS, In-app messages
    * Journeys, Templates,Automated messages
    * API requests
    * The "Send Test Message" button
    * Additional data fields

    For these cases, you must manually add UTM parameters in your templates or API payloads.
  </Warning>

#### URL handling and overrides

  If you add different UTMs to your push launch URLs with this feature enabled, these new UTMs set manually will override the UTM Parameters set within the dashboard automatic feature.
</Accordion>

***

## FAQ

### How can I link to the app store?

You can enter the store link as the launch URL. Examples:

**Android** - `https://developer.android.com/distribute/marketing-tools/linking-to-google-play.html` **iOS** - get the link to the app store page, but replace `https://` with `itms-apps://`.

### Can I link to another app?

For push and in-app messages, in most cases, you can setup a URL Scheme and deep link using the protocol `x://`. For example, [deep linking into Whatsapp](https://faq.whatsapp.com/425247423114725/?locale=vi_VN\&cms_platform=iphone), you can use: `whatsapp://wa.me/15551234567`

For email and sms, you will need to use the `https://` app store link.

### Can I prevent linking to my app or site?

Currently on mobile apps, anytime the user clicks the push it will open the app.

**Web Push:** If you do not want to link to any page or url, you can add `?_osp=do_not_open` to the end of a URL like this `https://yoursite.com/page?_osp=do_not_open` as the launch url, this will prevent the push from going to any url upon click and will just dismiss the push.

***

Built with [Mintlify](https://mintlify.com).
