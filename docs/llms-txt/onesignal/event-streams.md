# Source: https://documentation.onesignal.com/docs/en/event-streams.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Event Streams

> Send message data out of OneSignal in real-time to your chosen destination.

Event Streams allows you to send message data out of OneSignal in real-time to your chosen destination. Event streams are a great way to connect OneSignal to other products within your marketing ecosystem. They enable your team to trigger corresponding messaging, maintain records, and much more.

Available event types include:

* Push message events (sent, delivered, clicked, dismissed, etc.)
* Email events (sent, opened, clicked, bounced, unsubscribed, etc.)
* SMS events (sent, delivered, failed, opted out, etc.)
* In-app message events (impression, clicked, dismissed, etc.)
* Live Activity events (sent, delivered, confirmed delivery, failed, unsubscribed, clicked)

## Common use cases

1. **Customer journey mapping and personalization**: stream events to a CRM or Customer Data Platform (CDP) to build comprehensive customer profiles and tailor campaigns across various touchpoints.
2. **Analysis and reporting**: send message events (e.g., sends, opens, clicks) to a data warehouse to analyze engagement patterns or long-term trends across channels.
3. **Compliance and regulatory reporting**: stream all message-sent data to a data warehouse for auditing and compliance purposes.
4. **AI and predictive models**: send message event data to in-house AI or predictive models to create comprehensive customer cohorts and understand churn risks—such as email unsubscribes or message dismissals, which may indicate potential churn.
5. **Marketing automation**: send engagement events (like message opens or clicks) to other tools to automatically trigger the next steps in the user journey or update customer profiles and recent activity.
6. **Data fragmentation**: valuable customer data often resides in separate tools (such as customer engagement platforms, CRMs, analytics tools, and data warehouses). Event streaming helps centralize this data, increasing visibility into valuable first-party data and allowing for faster revenue outcomes.
7. **Slow communication between systems**: by sending live engagement events to other systems, you can trigger actions immediately after an event occurs, rather than waiting hours or days for batched updates. This eliminates reliance on manual imports or data syncs.
8. **Spend bloat and technical debt**: instead of managing multiple intermediary tools, you can directly connect OneSignal with your data warehouse. This reduces the costly overhead of managing multiple integrations or custom data pipelines, lessens technical debt, and preserves valuable technical resources for product and marketing.

### How to partner with your technical team

Setting up Event Streams requires collaboration with your technical team. Here are some tips to facilitate the conversation:

1. **Explain the benefits**: share your strategy for using this data and how it can enhance marketing campaigns, personalize user experiences, consolidate data, and reduce technical debt.
2. **Define the scope**: identify where you want the data to be sent, which events you want to track, and the estimated data volume. This will aid in configuring the proper endpoint setup.
3. **Provide technical documentation**: [share OneSignal's technical documentation and setup instructions](./event-streams). Your development team will need to configure the recipient endpoints and the event stream in OneSignal, ensuring data is routed correctly.
4. **Discuss data volume and management**: confirm that your systems can handle real-time data flows. It's recommended that the API handler records events without additional online processing to maintain low response times.
5. **Test and troubleshoot**: conduct tests to ensure everything is functioning smoothly before going live.

By working closely with your technical team, you can unlock the power of event streaming to enhance your growth strategy.

***

## Setup

You can configure a new event stream for your OneSignal application under **Data > Event Streams**.

### Requirements

Events can't be sent unless the following requirements are met:

* A valid URL or IP address pointing to your server HTTP(S) server
* URLs and IP addresses must be publicly routable
* Domains must include a recognized top-level domain (e.g., ".com", ".net")

### Event Selection

Click "Select Events" to select your choice of events to trigger an event stream.

<Frame caption="Trigger Webhook">
  <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/53fa919d7e46937556f32763366a919b104b3d2b366920219a190061830b78c6-Capture-2024-10-24-153011.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=0248aec7696aeebe437310d99960a392" width="951" height="169" data-path="images/docs/53fa919d7e46937556f32763366a919b104b3d2b366920219a190061830b78c6-Capture-2024-10-24-153011.png" />
</Frame>

The data that may be sent with these events all similar enough that you can send events triggered by multiple channels through the same event stream. Another approach would be to define multiple event streams each for a single channel or event for more granular control or to reduce the scale of data sent.

<Frame caption="Event Selection">
  <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/810859b-Screenshot_2024-07-23_at_9.57.33_AM.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=aad6b4931141a63691d21bb7902a32b2" width="1262" height="958" data-path="images/docs/810859b-Screenshot_2024-07-23_at_9.57.33_AM.png" />
</Frame>

#### Event stream filters

You can optionally further refine events by specifying the identifiers of one or more messages or templates, enabling you to receive only events related to specific messages within your app. Refer to the instructions below to enable event stream filtering.

<Frame caption="Filtering events by template">
  <img src="https://mintcdn.com/onesignal/4HyuQPBpu-4xjmQC/images/docs/d3459b5c919e7f10b4712268475c839b05a7e63389942ceec2c98a94019c8db6-image2.png?fit=max&auto=format&n=4HyuQPBpu-4xjmQC&q=85&s=1f4be18daaa363bc74f9ef633a9f07ee" width="1092" height="561" data-path="images/docs/d3459b5c919e7f10b4712268475c839b05a7e63389942ceec2c98a94019c8db6-image2.png" />
</Frame>

Message and template identifiers can be copied by navigating to **Messages > Push, Email, SMS, or Templates**, clicking the action button of the desired message or template, and selecting **Copy Message ID** or **Copy Template ID** from the action menu.

<Frame caption="Copying the Template ID of a template">
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/acf0b79f7368d3ca311fbdb43ce0e60f10f78b3b2b2160e22cf257223a83f888-copy_template_id.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=21e7fabfcde5e814da25916ef5ddc238" width="1616" height="1279" data-path="images/docs/acf0b79f7368d3ca311fbdb43ce0e60f10f78b3b2b2160e22cf257223a83f888-copy_template_id.png" />
</Frame>

Alternatively, you can copy the message/template identifier of what you're viewing directly from the URL :

* Template – `https://dashboard.onesignal.com/apps/{APP_ID}/templates/{TEMPLATE_ID}`
* Push – `https://dashboard.onesignal.com/apps/{APP_ID}/notifications/{MESSAGE_ID}`
* Email – `https://dashboard.onesignal.com/apps/{APP_ID}/email/{MESSAGE_ID}`
* SMS – `https://dashboard.onesignal.com/apps/{APP_ID}/sms/{MESSAGE_ID}`

### Configure the Event Stream

Select the HTTP method, the URL, and add headers for the event stream. This is where authentication should be configured to ensure secure communication between OneSignal and your systems.

The URI and Headers can contain liquid syntax which will come from both the user properties and properties of the event stream.

#### Authentication Headers

You can add authentication headers to validate that requests to your endpoint are genuinely from OneSignal. Common authentication methods include:

* **Authorization Header**: Add an `Authorization` header, where `YOUR_TOKEN` is provided by your system or 3rd party like:
  * `Basic {{YOUR_TOKEN}}`
  * `Bearer {{YOUR_TOKEN}}`
  * `ApiKey {{YOUR_API_KEY}}`
* **Custom Headers**: You can also add custom headers like:
  * `X-API-Key: {{YOUR_API_KEY}}`

*Note: OneSignal does not provide encryption services*

#### Testing Your Configuration

If you are looking for an easy way to test, use [webhook.site](https://webhook.site). Find "Your unique URL" in the center of the page. Copy that URL and use it in the URL field of your event stream configuration.

<Frame caption="Configure Webhook">
  <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/3c3a05f-Configure_Webhook.jpg?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=3c3011e3cfd1bab888044f2151ea1f3c" width="2248" height="822" data-path="images/docs/3c3a05f-Configure_Webhook.jpg" />
</Frame>

#### Disallowed headers

The following headers are restricted and can't be set.

* `content-length`
* `referer`
* `metadata-flavor`
* `x-google-metadata-request`
* `host`
* `x-onesignal*`

### Body

The body for an event stream will be JSON. The body JSON can be defined either as individual key/value pairs or as an editable code block. To change the input method use the first dropdown under the body heading and select the custom body.

<Frame caption="Event Stream Body Options">
  <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/2490576-Screenshot_2023-11-27_at_11.04.42_PM.png?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=f71ea7f3a0aced9003ded0a71edb2e22" width="1388" height="286" data-path="images/docs/2490576-Screenshot_2023-11-27_at_11.04.42_PM.png" />
</Frame>

On the right, you can see an example cURL request built from what has been input during event stream setup

<Frame caption="cURL Preview of Event Stream">
  <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/1a107a3-Screenshot_2023-11-27_at_11.04.49_PM.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=c990246f1ed4d7f972b5a7ce2f5830bb" width="1360" height="400" data-path="images/docs/1a107a3-Screenshot_2023-11-27_at_11.04.49_PM.png" />
</Frame>

### Personalization

You can personalize all fields in your Event Stream with predefined [Event Streams Data](./event-streams-data). This data can be added using [Liquid Syntax](./using-liquid-syntax). This gives you the flexibility to use event streams for nearly any use case.

<Info>
  See [Event Streams Data](./event-streams-data) for a list of all event, message, and user event data available for personalization.
</Info>

#### Example body

Select the "Custom Body" in the drop-down:

<CodeGroup>
  ```json json theme={null}
  {
    "Event Data": {
      "event.kind": "{{ event.kind }}",
      "event.id": "{{ event.id }}",
      "event.timestamp": "{{ event.timestamp }}",
      "event.datetime": "{{ event.datetime }}",
      "event.app_id": "{{ event.app_id }}",
      "event.subscription_device_type": "{{ event.subscription_device_type }}",
      "event.subscription_id": "{{ event.subscription_id }}",
      "event.onesignal_id": "{{ event.onesignal_id }}",
      "event.external_id": "{{ event.external_id }}",
      "event.data.page_name": "{{ event.data.page_name}}",
      "event.data.page_id": "{{ event.data.page_id}}",
      "event.data.target_name": "{{ event.data.target_name}}",
      "event.data.target_id": "{{ event.data.target_id}}",
      "event.data.failure_reason": "{{ event.data.failure_reason}}"
    },
    "Message Data": {
      "message.id": "{{ message.id }}",
      "message.name": "{{ message.name }}",
      "message.title": "{{ message.title.en }}",
      "message.contents": "{{ message.contents.en }}",
      "template_id": "{{ message.template_id }}",
      "message.template_id": "{{ message.template_id }}",
      "message.url": "{{ message.url }}",
      "message.app_url": "{{ message.app_url }}",
      "message.web_url": "{{ message.web_url }}"
    }
  }
  ```
</CodeGroup>

<Frame caption="Custom Body">
  <img src="https://mintcdn.com/onesignal/YOTSrtBSoqdrJ37A/images/docs/4dff42d10dffb762bf72a1c7255fbac2f50fef512541eb7db29e2ee8a117e8c9-Screenshot_2025-01-17_at_2.25.40_PM.png?fit=max&auto=format&n=YOTSrtBSoqdrJ37A&q=85&s=4460da08476423fa1f7c8eac700cfbd3" width="2112" height="1410" data-path="images/docs/4dff42d10dffb762bf72a1c7255fbac2f50fef512541eb7db29e2ee8a117e8c9-Screenshot_2025-01-17_at_2.25.40_PM.png" />
</Frame>

#### Using Liquid Syntax in JSON

When using Liquid syntax within JSON, proper quoting depends on the data type:

**Guidelines for JSON Formatting**

* **Strings** → **Must** wrap in quotes.
* **Numbers** → **Don't** wrap in quotes.
* **Objects** → **Must** not be wrapped in quotes.

**Examples**

#### Strings

**✅ Correct**

<CodeGroup>
  ```json json theme={null}
  // Wrap string values in quotes
  {
    "user_id": "{{ user.onesignal_id }}"
  }
  ```
</CodeGroup>

**❌ Incorrect**

```
{
  "user_id": {{ user.onesignal_id }}
}
```

#### Numbers & Booleans

**✅ Correct**

<CodeGroup>
  ```json json theme={null}
  // Don't wrap numbers or booleans in quotes
  {
    "user_score": {{ user.tags.score }}
  }
  ```
</CodeGroup>

**❌ Incorrect**

```
{
  "user_score": "{{ user.tags.score }}"
}
```

#### Objects

**✅ Correct**

<CodeGroup>
  ```json json theme={null}
  // Don't wrap objects in quotes.
  {
    "user_data": {{ user.tags }}
  }
  ```
</CodeGroup>

**❌ Incorrect**

```
{
  "user_data": "{{ user.tags }}"
}
```

**Best practices for handling multilingual conditionals in liquid syntax**

To avoid issues with language-based conditionals

1. **Use Direct Language Checks**: Always check `user.language` directly in conditionals, not in variables like `userLang`, for better compatibility.
2. **Start Simple**: Begin with basic phrases, then gradually add complexity.
3. **Avoid Over-Nesting**: Keep conditionals flat to prevent parsing issues.
4. **Test Basic Punctuation First**: Start with simple sentences and punctuation before using special characters.
5. **Use Fallbacks**: Ensure a default language (e.g., English) in case of missing translations.
6. **Stick to Standard Keys**: Use standard OneSignal keys like `content/title/en` for reliability.

This approach minimizes parsing errors and ensures compatibility with the system.

<Info>
  For details and options on how to personalize your messages using Liquid syntax, check out our [Using Liquid Syntax Guide](./using-liquid-syntax).
</Info>

***

## Results & Debugging

You can see how your event stream performs over a period of time on the event stream report page under the **Report** tab. This will include all-time numbers, the current status of your event stream, and time series data showing what kind of responses the hook has been receiving. Any HTTP response in the 200 range indicates an event was successfully received, while responses in the 400s and 500s indicate errors. A timeout means the server on the other side didn't manage to respond within a reasonable amount of time so OneSignal closed the connection and assumed it failed.

You can see a sampling of recent requests under the **Logs** tab for even more detail. This will show actual requests and the responses from the other side (if applicable). If your event stream has issues, this is a great place to look first. If you need to change/update your event stream, you can edit it on the form page and send test requests to see the full details you need until you can get it right.

<Frame caption="Event Stream Logs and Metrics">
  <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/b03288f-Screenshot_2023-11-27_at_11.10.42_PM.png?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=5cd4cedc3b1b49d51b4e9fb0e04c31a7" width="1366" height="812" data-path="images/docs/b03288f-Screenshot_2023-11-27_at_11.10.42_PM.png" />
</Frame>

### Retries / Disabling

When an Event Stream request fails for any recoverable reason (for example, status code 429), OneSignal will retry sending the event again after a short delay. This will happen a few times with increasing delays between requests. If enough retries fail in a row, the hook will be marked as 'failed permanently' and will no longer be retried.

If too many separate requests fail in a row, this is probably because of an issue on the receiving end; the receiving end could have errors or have changed/disabled something. OneSignal will continue to send requests to a certain point, but if the requests continue to fail, the event stream might be disabled by OneSignal. If this happens, make sure to spend some time troubleshooting, fixing and then testing the event stream before re-enabling it.

A poorly performing API could lead to event stream disablement. It is important that the API which ingests an event stream is able to handle the volume of events which is produced by message sends. Reviewing the volume of message sends that are produced by your app will reflect the performance required of your API.

We recommend that the API receiving the event stream record an event without any other online processing. This will keep response times low and prevent any latency related issues. Slow response time or status code 429 responses from your API can cause a backlog of events. A consistent backlog of events will lead OneSignal to disable the event stream so you can update your API to handle the required throughput.

OneSignal will send out emails to app admins and org admins when an event stream starts to experience a significant volume of failed events (but has not yet been disabled) as well as an email when the event stream is disabled when too many events have failed to send. There will also be a banner on the event streams index page notifying a OneSignal user of issues with one of their event streams.

Each Event Stream has a unique `event.id` for each event. This can be used as a header or in the body of the message as a way to check and potentially deduplicate requests if you see the same ones coming through.

### Tips for Success

* You typically will want to have event streams connect to your own servers, not third party services.
  * While there is nothing wrong with connecting directly to a third party the following can be harder to manage: It will be more challenging to configure/debug
* The volume of requests will not be managed in OneSignal.
  * Event stream events will be sent out as fast as users hit the steps in your journey and this might overwhelm other services, hit rate limits, or run up YOUR bill unexpectedly. This is especially common when trying to use another messaging channel for something like SMS. The flexibility of event streams means OneSignal does not know what you're trying to accomplish with them, so you may want to create a simple service of your own that accepts the event stream requests and then correctly handles your third-party connection limits, rate limits, and queue.
* Many services have public HTTP APIs which means you can connect to them with an event stream; look for their API docs and examples of how to make an HTTP request to find the right place to get started.

### Message event data limitations

Data for messages sent via our Journeys or API are only available in our system for 30 days. This means that any message events (like clicks, opens, unsubscribes, etc.) that happen 30+ days after the Journey or API message was sent, will not be available in the event stream. This may appear as blank or missing data in your analytics.

To work around this limitation, you can correlate the `message_id` of these clicked/opened/unsubscribed events with the original sent event that has the same `message_id`. The original `sent` event should have the relevant message data (title, template etc).

***

## Testing

Use a tool like [https://webhook.site/](https://webhook.site/) and set the **Your unique URL** provided into the URL parameter in the Event Stream with the POST method.

<Frame caption="The URL matches the &#x22;Your unique URL&#x22; from webhook.site">
  <img src="https://mintcdn.com/onesignal/MUgio66t0sYhGEvj/images/docs/64af09f47cba448ba82b28ffa1d9dfc2309752900d98072f73a06aa0138e24a3-Screenshot_2025-03-04_at_3.31.14_PM.png?fit=max&auto=format&n=MUgio66t0sYhGEvj&q=85&s=e57076d0108dcca27ad6aa2a7d0e1fcd" width="1460" height="706" data-path="images/docs/64af09f47cba448ba82b28ffa1d9dfc2309752900d98072f73a06aa0138e24a3-Screenshot_2025-03-04_at_3.31.14_PM.png" />
</Frame>

Set the events you want to track. In this example, we will use the push events, but any will work.

<Frame caption="Push message events selected, but any can be used for testing.">
  <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/d66663960101c0a9d7a513ac86ebf01c202e66d42d3b445ea4ef27e178f23bbe-Screenshot_2025-03-04_at_3.31.52_PM.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=ebd5aae6ec73eb2c7e63c53ab6ee7e9d" width="1452" height="402" data-path="images/docs/d66663960101c0a9d7a513ac86ebf01c202e66d42d3b445ea4ef27e178f23bbe-Screenshot_2025-03-04_at_3.31.52_PM.png" />
</Frame>

In this example, we will use the above [Example body](#body).

Save the event and set it live.

Send a message to trigger the event. In webhook.site we will see the event with the following data:

<Frame caption="Example using webhook.site">
  <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/dc8857b0e81ef767840eefd953c8d94a24420eb576c20af72156900fb0909d3a-Screenshot_2025-03-04_at_4.49.16_PM.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=b69262aeada09efebd45f0ceffa86044" width="2464" height="1650" data-path="images/docs/dc8857b0e81ef767840eefd953c8d94a24420eb576c20af72156900fb0909d3a-Screenshot_2025-03-04_at_4.49.16_PM.png" />
</Frame>

This shows the following:

* **Host**: the IP address where the request came from. See [REST API overview](/reference/rest-api-overview) for a list of possible IPs.
* **Request Content** the data sent within the body of the event stream.

***

Built with [Mintlify](https://mintlify.com).
