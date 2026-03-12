# Source: https://documentation.onesignal.com/docs/en/data-feeds.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data feeds

> Learn how to use Data Feeds to pull real-time data from your APIs into OneSignal messages.

Data Feeds let you pull **real-time data from your APIs directly into messages** at send time. This allows you to deliver highly personalized content without pre-loading data into OneSignal.

Use Data Feeds when your data changes frequently, such as:

* A user’s current rewards balance
* Latest order status
* Personalized product recommendations

Other personalization methods (like tags or dynamic content) are great for static data, but **Data Feeds are best for live, fast-changing values**.

<Note>
  Data Feeds are currently available **only for email messages sent through Journeys**.
  Need another channel? [Fill out this short survey](https://survey.survicate.com/954895d3e7ed1348/?p=anonymous).
</Note>

***

## How Data Feeds Work

1. **Create a Data Feed** – Configure how OneSignal connects to your API.
2. **Attach the Data Feed** to a message template.
3. **Insert response fields** in your message using [Liquid syntax](https://shopify.github.io/liquid/).
4. **At send time**, OneSignal makes an API call for each recipient, parses the response, and injects the data into your message.

### Example: Display reward points

Suppose you want to show each customer their rewards balance:

```liquid  theme={null}
Hi {{ first_name }},

You have {{ data_feed.rewards.points }} points!
Your membership status is {{ data_feed.rewards.status_level }}.

Keep shopping to earn more points!
```

When Sarah gets this email, she'll see her actual points balance and membership status in place of `{{ data_feed.rewards.points }}` and `{{ data_feed.rewards.status_level }}`.

We'll use this example to show you how to set up a Data Feed step by step below.

## Creating and using a Data Feed

### 1. Set up your Data Feed configuration

Navigate to **Data > Data Feeds** in the sidebar to see the list of existing Data Feeds and create a new one.

Each Data Feed must have:

* **Name**: A descriptive name like "Customer Rewards API" to help you distinguish it in your list of feeds. We recommend these be unique, but it’s not required.
* **Alias**: A short name like rewards that you’ll use in Liquid syntax. These must be unique, contain no spaces, and can only contain lower-case alphanumeric characters with no special symbols.
* **Method**: How we should contact your API. Usually this is GET but POST is also supported.
* **URL**: The address of the API. You can include Liquid syntax, enabling us to call the API to fetch user-specific data.

For example, perhaps your rewards endpoint might be formatted this way, where you would use a data tag to insert the external ID (stored in OneSignal) to fetch that user’s rewards data:

```liquid  theme={null}
https://acme.com/customers/user_id={{ external_id }}/rewards
```

* **Headers**: Enter header key-value pairs as needed by your API specifications. A typical important use will be to include authentication information. These fields also support Liquid syntax in case it is needed.
* **Body**: Should your API require it, you can include a body in the request in JSON format. This editor supports Liquid syntax, just like [Journey Webhooks](./journeys-webhook#personalization).

For example, instead of in the URL string as above, your API might need you to specify the user’s ID in the body of the request:

```json  theme={null}
{
 "customer_id": "{{ subscription.external_id }}"
}
```

A complete Data Feed configuration might look something like this:

<Frame caption="Data Feed configuration example">
  <img src="https://mintcdn.com/onesignal/pJu1B0q7HE_EbGFK/images/dashboard/data-feed-configuration-example.png?fit=max&auto=format&n=pJu1B0q7HE_EbGFK&q=85&s=d000fa94b02ee58c15b089fa7f9ad834" width="901" height="1142" data-path="images/dashboard/data-feed-configuration-example.png" />
</Frame>

**We recommend testing your feed before using it.** You test it using Test Subscriptions, so make sure your test subscription attributes will return a real result from your API.

Finally, **Activate** your new Data Feed so it’s ready for use.

### 2. Attach the Data Feed to your message template

Attach your Data Feed to your message template so that OneSignal knows to use it.

1. Navigate to **Messages > Templates**
2. In the Message section, select the **Personalization** button

<Frame caption="Personalization button options">
  <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/dashboard/data-feeds-personalization-button.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=a2b46a9c67cc0ce86c469c407d2afbac" width="1940" height="614" data-path="images/dashboard/data-feeds-personalization-button.png" />
</Frame>

1. Toggle on **Data Feeds** and select your feed

<Frame caption="Data Feeds section in the message composer">
  <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/dashboard/data-feeds-option.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=ca51e5f38a54b8550b3256ad76843947" width="978" height="762" data-path="images/dashboard/data-feeds-option.png" />
</Frame>

1. Save your template

### 3. Use the data in your message

Use Liquid syntax to insert the response data anywhere in your message. In our example, let’s say that the response for Sarah, whose external\_id is `1a1-b2c3`, is a simple JSON blob like this:

```json  theme={null}
{
 "external_id": a1-b2c3,
 "points": 193,
 "status_level": "Gold"
}
```

We want to insert the number of points and the status level into the message, which is accomplished via typical dot notation:

```liquid  theme={null}
You have {{ data_feed.rewards.points }} points!
Your membership status is {{ data_feed.rewards.status_level }}.
```

This tells OneSignal:

* Use a Data Feed
* Use the `rewards` Data Feed
  * Recall: the `rewards` feed knows to call the API with the `external_id` of the recipient
* From the response, insert the value of the `points` item (193) and the `status_level` item (Gold)

***

## Requirements and Limits

Your API needs to:

* **Accept single-step authentication** with auth tokens in headers
* **Respond quickly.** Under 250ms recommended (this directly affects send speed)
* **Return JSON.** Other formats are not supported at this time.
  * If you have a use case relying on an alternative format, we want to hear from you! Fill out this [short survey here](https://survey.survicate.com/954895d3e7ed1348/?p=anonymous).
* **Handle your volume and rate of message sends.** If your API has a low rate limit, this will prevent us from delivering your messages quickly.
* **Return reasonably-sized payloads.** We recommend keeping responses under 50kb for best performance.

Current limits:

* **One Data Feed per template.** We expect to increase this limit in the future. Fill out this [short survey here](https://survey.survicate.com/954895d3e7ed1348/?p=anonymous) to let us know you need this.
* **One API call per Data Feed per message.** Fetch everything you need in one call.
* **Journeys only.** Not yet available for other sending methods. Fill out this [short survey here](https://survey.survicate.com/954895d3e7ed1348/?p=anonymous) to let us know you need this.
* **No chaining calls.** The payload from one Data Feed cannot be used to call another.

***

## Setting up your API

Before creating a Data Feed, ensure your API can handle these requirements:

### Authentication

Your API should accept authentication via headers:

```
Authorization: Bearer YOUR_TOKEN
```

or

```
X-API-Key: YOUR_KEY
```

### JSON Request Body

If you need to include a body in the request, your API should accept JSON. This may mean your headers need to include `Content: application/json`.

### JSON Response

Your API should return a JSON object. Typically this means your headers will include `Accept: application/json`.

### Personalization Parameters

You'll typically pass user identifiers in the URL like this:

```liquid  theme={null}
https://api.example.com/users/{{external_id}}/data
https://api.example.com/rewards?email={{email | url_encode}}
```

And/or in the body:

```json JSON theme={null}
{
 "customer_id": "{{ external_id }}",
 "email": "{{ subscription.email }}"
}
```

Make sure this data will exist in OneSignal (usually as data tags, but other options are available such as [custom events properties](#examples-%26-advanced-use-cases)).

### Rate Limits

Consider your API's rate limits. If you're sending to 10,000 users in rapid succession, we'll make 10,000 API calls. Ensure your API can handle this volume.

### Error Handling

If your API returns an error or doesn't have data for a user, the message won't be sent to that recipient. Make sure your API returns data for all expected users.

***

## Getting Started Checklist

Before implementing Data Feeds, answer these questions:

* What data do I want to show in my message? Working backwards from a simple outline with the items to be populated from your API identified will help you organize your thinking.
* Is this data available via a single API endpoint?
* How will I authenticate API requests?
* What identifier or other data item will I use to fetch personalized data?
* Is that identifier already stored in OneSignal? If not, how will it be populated?
* Can my API handle the volume of requests I'll generate?
* What happens if my API doesn't have data for a user?

***

## Examples & advanced use cases

Data Feeds can be used with Liquid syntax or in combination with other features in creative ways to produce more complex personalization.

<Tabs>
  <Tab title="Iterating with loops: abandoned cart">
    ### Iterating with loops: abandoned cart

    Let's say you have a Data Feed cart that returns an array of items in the user's cart, plus the cart total dollar amount:

    ```json JSON theme={null}
    {
      "items": [
        {
          "name": "Blue Running Shoes",
          "price": 84.00,
          "image_url": "https://acme.com/blue-running-shoes.png"
        },
        {
          "name": "Protein Bar",
          "price": 5.99,
          "image_url": "https://acme.com/protein-bar.png"
        }
      ],
      "total": 89.99
    }
    ```

    If you want to show each item in the cart, plus the cart total, you can use a for loop in Liquid:

    ```html HTML theme={null}
    <ul>
      {% for item in data_feed.cart.items %}
        <li>
          <strong>{{ item.name }}</strong><br>
          ${{ item.price }}<br>
          <img src="{{ item.image_url }}" alt="{{ item.name }}">
        </li>
      {% endfor %}
    </ul>

    <p>Cart total: ${{ data_feed.cart.total }}</p>

    ```

    This will result in:

    ```text  theme={null}
    - Blue Running Shoes
    - $84.00
    - <running shoes image>
    - Protein Bar
    - $5.99
    - <protein bar image>
    Cart total: $89.99
    ```

    <Note>
      If you're using the email block editor, when inserting this sort of complex Liquid syntax, particularly if you need to include images or links, for best results use the custom HTML block element.
    </Note>

    <Tip>
      Want to see how to trigger this abandoned cart email using custom events? Check out the **Custom events properties** tab for the complete workflow.
    </Tip>
  </Tab>

  <Tab title="Custom events properties">
    ### Custom events properties

    Continuing the previous abandoned cart example, how might we know how to fetch that particular cart in the first place?

    One method might be to create a Journey triggered by a `cart_abandoned` [custom event](./custom-events), where the properties includes a cart\_id. In this example that event is being sent to OneSignal via API:

    ```bash curl theme={null}
    curl --request POST \
      --url https://api.onesignal.com/apps/{app_id}/custom_events \
      --header 'Accept: application/json' \
      --data '{
      "events": [
        {
          "name": "cart_abandoned",
          "external_id": "user_12345",
          "properties": {
            "cart_id": 98765
          }
        }
      ]
    }'
    ```

    <Frame caption="Custom event for Journey entry">
      <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/dashboard/data-feed-custom-event-journey-entry.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=6bb357d09ef9a2830ee6e9a19109afc1" width="936" height="548" data-path="images/dashboard/data-feed-custom-event-journey-entry.png" />
    </Frame>

    The user `user_12345` enters the journey when this event is fired, then reaches a node sending an email. That email template is set up with the `cart` Data Feed, where the URL is set to retrieve the contents of a particular cart like so:

    ```liquid  theme={null}
    https://acme.com/carts/{{ journey.event.cart_abandoned.data.cart_id }}
    ```

    Thus, when this particular event is ingested and triggers the Journey:

    1. The `cart_id` value of `98765` will be stored to the Journey
    2. When the email step is reached, the `cart` Data Feed will reference that `cart_id` value and use it to call the cart API
    3. The returned JSON properties will be parsed and inserted into the email as in the previous example above

    <Tip>
      Want to see how to conditionally display Data Feed content based on order status? Check out the **Conditional display: order status** tab to learn more.
    </Tip>
  </Tab>

  <Tab title="Conditional display: order status">
    ### Conditional display: order status

    Let's say you want to include the status of a customer's order, but only include a tracking number link if the order has been shipped. You can use an `if` statement to do so:

    ```liquid  theme={null}
    Your order is {{data_feed.order.status}}!

    {% if data_feed.order.tracking_number != empty %}
    Track it here: {{data_feed.order.tracking_url}}
    {% endif %}
    ```

    Here, the tracking link will only be displayed if the `tracking_number` exists.
  </Tab>

  <Tab title="Automation without personalization">
    ### Automation without personalization

    Data Feeds can be used to automatically insert up-to-date information into your messages without necessarily needing to be personalized per recipient.

    For example, perhaps you insert a banner image at the top of your emails and change it monthly to keep up with holidays and other monthly events. Rather than remembering to upload a new image to OneSignal and changing all your templates each month, you might set up a Data Feed that fetches the current banner image URL from your CMS or other asset-management location.

    You would set up a `banner` Data Feed that points to an endpoint **without** any variables in the URL like so:

    ```liquid  theme={null}
    https://acme.com/assets/email-banner
    ```

    Which returns a response with the current banner URL:

    ```json JSON theme={null}
    {
     "banner_url": "https://acme.com/assets/email-banner/2025july.png"
    }
    ```

    You'd set your email template to use `{{ data_feed.banner.banner_url }}` as the image source URL, automating this process going forward.
  </Tab>

  <Tab title="Personalized coupon codes">
    ### Personalized coupon codes

    This example covers how to send personalized, single-use coupon codes in emails using a Data Feed that fetches a unique value from your API for each recipient.

    ### Goal

    Send an email such as:

    > Hi George,
    >
    > Complete your booking in the next 2 hours and save 10% with your personal code: XYZ123ABC

    Each user receives a unique coupon code, generated live via an external API call when the email is sent, valid for the given time window, and scoped to that user.

    ### Prerequisites

    * [Email channel configured](./email-setup) in OneSignal (your app has email capability enabled)
    * An external API that accepts a user identifier (for example, [`external_id`](./users#external-id)) and campaign identifier, and returns JSON with the coupon code, discount, and expiration
    * A unique identifier (such as `external_id`) for each user that your API can use to generate coupons
    * A [segment](./segmentation) or trigger (for example, "abandoned search in last 24h") used to send the email through a OneSignal Journey

    ### Step 1: Create the Data Feed

    <Steps>
      <Step title="Navigate to Data Feeds">
        In your OneSignal app, select **Data feeds** from the navigation bar, then click **New data feed**.
      </Step>

      <Step title="Configure the Data Feed">
        Configure the following fields:

        * **Data Feed Name**: `coupon_code_generator`
        * **Alias**: `coupon`
        * **Method**: `GET`
        * **URL**: `https://api.example.com/generate-coupon?userId={{ external_id }}&campaign=AbandonedBooking10`
        * **Headers**:
          ```json  theme={null}
          {
            "Authorization": "Bearer YOUR_API_TOKEN"
          }
          ```
      </Step>

      <Step title="Reference the API response">
        When the API returns JSON like this:

        ```json  theme={null}
        {
          "code": "AB10-5F3K-HT9L",
          "discount_percent": "10%",
          "expires_in_hours": 2
        }
        ```

        You can reference its values in your email template as:

        * `{{ data_feed.coupon.code }}`
        * `{{ data_feed.coupon.discount_percent }}`
        * `{{ data_feed.coupon.expires_in_hours }}`
      </Step>

      <Step title="Test and activate the Data Feed">
        Click **Send Test** to verify your configuration, then click **Activate** to make the Data Feed available for use in templates.
      </Step>
    </Steps>

    **API and system requirements:**

    * The API must return JSON and respond within approximately 250 ms
    * It must accept the identifier you pass (for example, `external_id`) in the URL or body
    * Ensure your API handles the expected call volume
    * One Data Feed per template is allowed
    * Data Feeds currently work only with email messages in Journeys

    ### Step 2: Create the email template

    1. In OneSignal, go to **Messages → Email → New Template**
    2. Use the Data Feed alias and fields within your message body. For example:

    ```html  theme={null}
    <h2>Hi {{ first_name }},</h2>
    <p>
    Complete your booking in the next {{ data_feed.coupon.expires_in_hours }} hours and save
    {{ data_feed.coupon.discount_percent }} with your personal code:
    <strong>{{ data_feed.coupon.code }}</strong>
    </p>

    <p><a href="https://example.com/checkout?coupon={{ data_feed.coupon.code }}">Use Code Now →</a></p>
    ```

    <Note>
      * Use Liquid syntax in the form `{{ data_feed.<alias>.<field> }}`
      * Make sure the Data Feed is attached to the template
      * If using the drag-and-drop editor with custom Liquid logic, use an HTML block
    </Note>

    ### Step 3: Attach the Data Feed and trigger the email

    1. In the template composer, under **Personalization**, toggle **Data Feeds** and select your feed (`coupon_code_generator`)
    2. This ensures OneSignal makes the API call at send time for each recipient, populates the data, and injects it into the email
    3. Set up a Journey to automate the message:
       * **Entry condition**: Segment such as "abandoned search in last 24 hours"
       * **[Wait until](./custom-events#wait-until-event)**: Create a `booking_completed` custom event. Configure the wait to exit the Journey if this event fires, or continue after 1 hour. If they complete a booking, they exit without receiving the email; otherwise, they continue to receive the coupon.
       * **Send email**: Use the personalized coupon email template
       * Ensure the Journey uses the email channel and that recipients are subscribed to email

    ### Step 4: Manage coupon redemption and tracking

    Your backend should:

    1. Record each generated code along with `userId`, `code`, `campaign`, `expiration_time`, and a `redeemed` flag
    2. Validate and mark codes as redeemed upon checkout
    3. Log the redemption data (user, campaign, and time) for ROI analysis

    ### Complete workflow example

    | Step | Event                                    | Action                                                                                       |
    | ---- | ---------------------------------------- | -------------------------------------------------------------------------------------------- |
    | 1    | User triggers "abandoned search" segment | User enters Journey via segment                                                              |
    | 2    | Journey triggers email send              | OneSignal attaches Data Feed, calls your API with the user's `external_id` and campaign name |
    | 3    | API returns JSON                         | OneSignal populates data feed coupon fields and sends email                                  |
    | 4    | User receives email                      | Example: "Hi George! Save 10% with your personal code: AB10-5F3K-HT9L"                       |
    | 5    | User redeems code                        | Backend validates and logs redemption                                                        |

    ### Testing

    * Test with a user who has a known `external_id`
    * Call your API manually to confirm correct JSON responses
    * Use **Preview** in the OneSignal template editor to verify that data feed coupon fields populate
    * Check API logs for latency and errors
    * If a Data Feed call fails, OneSignal will skip sending the message to that recipient

    ### Key takeaways

    * Data Feeds allow real-time, send-time API calls for user-specific personalization
    * Currently supported for **email messages in Journeys** only
    * Each template can have one Data Feed
    * Use Liquid syntax `{{ data_feed.alias.field }}` to include dynamic data
    * Ensure your API meets the JSON, latency, and scalability requirements
    * If the Data Feed fails, OneSignal will not send the message to that recipient
  </Tab>
</Tabs>

***

## Troubleshooting

### My data isn't showing

1. Check that your Data Feed is attached to the template
2. Verify your Liquid syntax matches your JSON structure exactly
3. Test your API endpoint manually to ensure it's returning data
4. Check that the user has the required data tags (like `external_id`)

### Messages are sending slowly

1. Check your API response time
2. Ensure your API can handle concurrent requests

### Some recipients aren't getting messages

1. Your API might not have data for those users
2. Check the error log in the Data Feed configuration for 404s or errors
3. Check your API logs for 404s or errors
4. Verify those users have the required identifiers in OneSignal

***

Built with [Mintlify](https://mintlify.com).
