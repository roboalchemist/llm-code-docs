# Source: https://documentation.onesignal.com/docs/en/personalization-properties-and-tags.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Personalize with properties

> Personalize OneSignal messages using predefined properties and custom data tags. Access user, subscription, journey, message, template, and app-level data with Liquid syntax across email, push, SMS, and webhooks.

Use properties (such as user tags and identifiers like External ID) to personalize messages and delivery payloads with [Liquid syntax](./using-liquid-syntax).

OneSignal renders Liquid placeholders **at send time**, using data already stored on the user, subscription, Journey, message, template, app, or organization. You can use this data to personalize messages, [Journey webhooks](./journeys-webhook), and [Event Streams](./event-streams).

***

## When to use property personalization

Use property personalization to render content at send time using data that already exists in OneSignal—most commonly user tags, External ID, and subscription fields like email or phone number.

This is the right approach when:

* The data is already stored in OneSignal
* You want Liquid placeholders replaced automatically when the message sends
* You don't need to fetch or compute fresh data at delivery time

<Note>
  If the value must be fetched or computed at send time (for example, live pricing or inventory), use [Data Feeds](./data-feeds) or our [API with `custom_data`](./personalization-api-custom-data).

  If the value comes from the event that caused a user to enter or progress through a Journey, use [Custom Event personalization](./personalization-custom-event).
</Note>

### Channel support

Each channel supports specific property types and fields.

<Tabs>
  <Tab title="Email">
    Supports [User & Subscription properties](#user-&-subscription-properties) in:

    * Subject, Reply-to, and Pre-header
    * Message body
    * HTML attributes (for example: `<img src="{{ image_url }}" />`)
    * Button actions (URLs, mailto, etc.)
  </Tab>

  <Tab title="Push">
    Supports [User & Subscription properties](#user-&-subscription-properties) in:

    * Title (`headings`), Subtitle, Body (`contents`)
    * Image URL
    * Launch URL: `https://example.com/{{last_category_viewed}}`

    <Warning>
      The `data` (additional data) field does not support Liquid syntax.
    </Warning>
  </Tab>

  <Tab title="SMS">
    Supports [User & Subscription properties](#user-&-subscription-properties) in:

    * Message body (`contents`)
  </Tab>

  <Tab title="In-app messages">
    Only support Tag substitution. Properties, Custom Events, and other data sources are not available at this time.

    * Tags must be set before the user starts a new app session.
    * Tag substitution may not appear when using test-send flows.

    **Block editor:** Text, Button, and Image blocks\
    **HTML editor:** Text elements and attributes (`src`, `href`, `action`, `data`)
  </Tab>

  <Tab title="Live Activities">
    Supports [User & Subscription properties](#user-&-subscription-properties) in:

    * `event_updates`
    * `contents`
    * `headings`
  </Tab>
</Tabs>

***

## How property personalization works

OneSignal replaces Liquid placeholders with the corresponding property values for the user and subscription being messaged.

```liquid Liquid theme={null}
Hi {{ first_name | default: "friend" }}!
Congrats on reaching level {{ level | default: "1" }}!
```

If a user has tags `first_name: Jon` and `level: 5`, they see:

```liquid Text theme={null}
Hi Jon! 
Congrats on reaching level 5!
```

If a user has no tags set, they see the default values instead.

***

## Property Liquid reference

Use this section to look up the exact object and field names available in Liquid.

### User & Subscription properties

Use `user` for user-level data. Use `subscription` when you need channel-specific values like email address or phone number.

<ParamField body="user.tags">
  The [Tags](./add-user-data-tags) of the User. You can reference the tags in several ways:

* Use the `key` directly or place the key after `tags`
* Example tags set: `first_name: Jon, level: 5`

  ```liquid Liquid theme={null}
  Your first name is {{ first_name }}.
  Your first name is {{ user.tags.first_name }}.
  Your level is {{ level }}.
  Your level is {{ user.tags.level }}.
  ```

* Iterate over tags with for-loop syntax. This example outputs key:value pairs separated by commas.

  ```liquid Liquid theme={null}
  {% for tag in user.tags %}
  {{ tag[0] }}: {{ tag[1] }}
  {% unless forloop.last %}, 
  {% endunless %}{% endfor %}
  ```

</ParamField>

<ParamField body="user.external_id">
  The [External ID](./users#external-id) of the User.

  ```liquid Liquid theme={null}
  Your user ID is {{ user.external_id }}.
  Your user ID is {{ subscription.external_id }}.
  ```

</ParamField>

<ParamField body="user.onesignal_id">
  The [OneSignal ID](./users) of the User.

  ```liquid Liquid theme={null}
  Your OneSignal user ID is {{ user.onesignal_id }}.
  ```

</ParamField>

<ParamField body="subscription.email">
  The email address of the email Subscription being messaged.

  ```liquid Liquid theme={null}
  Thanks for subscribing with email {{ subscription.email }}.
  ```

</ParamField>

<ParamField body="subscription.phone_number">
  The phone number of the SMS Subscription being messaged.

  ```liquid Liquid theme={null}
  Thanks for subscribing with phone number {{ subscription.phone_number }}.
  ```

</ParamField>

<ParamField body="user.language">
  The language code of the user.

  ```liquid Liquid theme={null}
  Preferred language: {{ user.language }}
  Preferred language: {{ subscription.language }}
  ```

</ParamField>

<ParamField body="user.subscriptions">
  The [Subscriptions](./subscriptions) of the User.

* Iterate over subscriptions with for-loop syntax.
* This example outputs each subscription's token and ID separated by commas.

  ```json JSON theme={null}
  {
    "subscriptions": "{% for subscription in user.subscriptions %}{% if subscription.subscription_token %}{{ subscription.subscription_token }}: {{ subscription.id }}{% unless forloop.last %}, {% endunless %}{% endif %}{% endfor %}"
  }
  ```

</ParamField>

<ParamField body="subscription.unsubscribe_token">
  The token used with the [Unsubscribe email with token API](/reference/unsubscribe-with-token).

  ```liquid Liquid theme={null}
  Unsubscribe: https://your-domain.com/unsubscribe?token={{ subscription.unsubscribe_token }}
  ```

</ParamField>

### Journey properties

The `journey` object lets you reference the Journey name or access [Custom Event Personalization](./personalization-custom-event) for the Journey.

<ParamField body="journey.name">
  The name of the Journey.

  ```json JSON theme={null}
  {
    "journey_name": "{{ journey.name }}"
  }
  ```

</ParamField>

### Message properties

The `message` object provides access to the message ID, name, and template ID that can be helpful for [Event Streams](./event-streams) along with access to [custom\_data](./personalization-api-custom-data) for personalizing messages sent from your backend.

<ParamField body="message.id">
  The ID of the message set by OneSignal.

  ```json JSON theme={null}
  {
    "message_id": "{{ message.id }}"
  }
  ```

</ParamField>

<ParamField body="message.name">
  The name of the message set by you, the sender.

  ```json JSON theme={null}
  {
    "message_name": "{{ message.name }}"
  }
  ```

</ParamField>

<ParamField body="message.template_id">
  The ID of the template set by OneSignal.

  ```json JSON theme={null}
  {
    "template_id": "{{ message.template_id }}"
  }
  ```

</ParamField>

### Template properties

The `template` object provides access to the template ID and name about the [Template](./templates) used to send the message. This can be helpful for [Event Streams](./event-streams).

<ParamField body="template.id">
  The ID of the template set by OneSignal.

  ```json JSON theme={null}
  {
    "template_id": "{{ template.id }}"
  }
  ```

</ParamField>

<ParamField body="template.name">
  The name of the template set by you, the sender.

  ```json JSON theme={null}
  {
    "template_name": "{{ template.name }}"
  }
  ```

</ParamField>

***

### App and organization properties

The `app` and `org` objects provide details about the [App and Organization](./apps-organizations) that sent the message. This can be helpful for [Event Streams](./event-streams).

<ParamField body="app.id">
  The ID of the app set by OneSignal.

  ```json JSON theme={null}
  {
    "app_id": "{{ app.id }}"
  }
  ```

</ParamField>

<ParamField body="app.name">
  The name of the app set by you, the owner of the app.

  ```json JSON theme={null}
  {
    "app_name": "{{ app.name }}"
  }
  ```

</ParamField>

<ParamField body="org.id">
  The ID of the Organization set by OneSignal.

  ```json JSON theme={null}
  {
    "org_id": "{{ org.id }}"
  }
  ```

</ParamField>

<ParamField body="org.name">
  The name of the Organization set by you, the owner of the Organization.

  ```json JSON theme={null}
  {
    "org_name": "{{ org.name }}"
  }
  ```

</ParamField>

***

## Example: Abandoned cart templates using tags

This example shows how to personalize abandoned cart messages using user tags. It builds on the [Abandoned Cart tutorial](./abandoned-cart).

**Example tags set:**

```json JSON theme={null}
{
  "cart_updated": "unix_timestamp_seconds",
  "product_image": "https://i.imgur.com/ssPCfbC.png",
  "product_name": "24 Pack of Acorns",
  "product_quantity": "1",
  "product_price": "$12.99",
  "cart_items_count": "4",
  "cart_url": "https://yourdomain.com/cart"
}
```

### Email template

<Steps>
  <Step title="Create a new email template">
    Navigate to **Messages > Templates > New Email Template** and open the Drag & Drop Editor.
  </Step>

  <Step title="Add the layout structure">
    Create five rows:

    * Rows 1, 2, and 4: one column with a **Paragraph** block
    * Row 3: four columns with **HTML | Paragraph | Paragraph | Paragraph**
    * Row 5: one column with a **Button** block

    <Frame caption="Starter email template for abandoned cart">
      <img src="https://mintcdn.com/onesignal/v-hm59YoewwF90UX/images/email/starter-template-abandoned-cart.png?fit=max&auto=format&n=v-hm59YoewwF90UX&q=85&s=551e9ec4618f64fdc0b6ab610a537c48" width="2968" height="2124" data-path="images/email/starter-template-abandoned-cart.png" />
    </Frame>
  </Step>

  <Step title="Add liquid to paragraph blocks">
    In row 1, add:

    ```liquid Liquid theme={null}
    We're holding onto {{cart_items_count}} items in your cart, but don't wait too long, other squirrels are getting ahead!
    ```

    In row 2, add a description of what the user is looking at:

    ```liquid Text theme={null}
    Currently in your cart:
    ```

    In row 4, add another CTA:

    ```liquid Text theme={null}
    Checkout now while supplies last!
    ```
  </Step>

  <Step title="Display the most recent item">
    In row 3, configure the four columns:

    **Column 1 (HTML block):**

    ```html HTML theme={null}
    <img src="{{product_image}}" alt="Image" style="max-width:100%;" />
    ```

    **Columns 2–4 (Text blocks):**

    * Column 2: `{{product_name}}`
    * Column 3: `{{product_quantity}}`
    * Column 4: `{{product_price}}`
  </Step>

  <Step title="Add the cart URL to the button">
    In the row 5 **Button** block, set the Action URL to:

    ```liquid  theme={null}
    {{cart_url}}
    ```

    <Frame caption="Finished base email template for abandoned cart without styling">
      <img src="https://mintcdn.com/onesignal/v-hm59YoewwF90UX/images/email/finished-template-abandoned-cart-tags.png?fit=max&auto=format&n=v-hm59YoewwF90UX&q=85&s=a46cb86b4725c27c360b9f7cd96ab305" width="2968" height="2124" data-path="images/email/finished-template-abandoned-cart-tags.png" />
    </Frame>
  </Step>

  <Step title="Test & preview the template">
    Send a test email to yourself using the **Test & preview** button.

    * Make sure the tags are set on your email Subscription.

    <Frame caption="Preview email with tags">
      <img src="https://mintcdn.com/onesignal/v-hm59YoewwF90UX/images/email/test-email-with-tags.png?fit=max&auto=format&n=v-hm59YoewwF90UX&q=85&s=307a846a3fec6676658ac4c653590110" width="2968" height="2124" data-path="images/email/test-email-with-tags.png" />
    </Frame>
  </Step>

  <Step title="Style the template">
    <Check>Success! Now you can apply your own styling to the template. See [Design emails with drag-and-drop](./design-emails-with-drag-and-drop).</Check>
  </Step>
</Steps>

### Push template

Push notifications have limited space, so display one item and mention the total count.

**Message field:**

Display item and count with correct grammar using [conditional statements](./using-liquid-syntax#if-elsif-else).

```liquid Liquid theme={null}
{% assign item_count = cart_items_count | plus: 0 %}
{% if item_count == 1 %}
You left {{product_name}} in your cart.
{% endif %}
{% if item_count == 2 %}
You left {{product_name}} and {{item_count | minus: 1}} more item in your cart.
{% endif %}
{% if item_count > 2 %}
You left {{product_name}} and {{item_count | minus: 1}} more items in your cart.
{% endif %}
```

**Image field:**

```liquid Liquid theme={null}
{{product_image | default: "https://i.imgur.com/ssPCfbC.png"}}
```

**Launch URL field:**

```liquid Liquid theme={null}
{{cart_url | default: "https://yourdomain.com/cart"}}
```

<Frame caption="Preview push template personalization with Test & preview">
  <img src="https://mintcdn.com/onesignal/Up-pAJT_jbhthm6E/images/push/preview-push-template-personalization-with-test-preview.png?fit=max&auto=format&n=Up-pAJT_jbhthm6E&q=85&s=97db90a05acdf4ed30f54a76b1d63b98" width="2880" height="2036" data-path="images/push/preview-push-template-personalization-with-test-preview.png" />
</Frame>

<Check>Success! You can now create more templates and use them in the [Abandoned Cart Journey](./abandoned-cart).</Check>

***

## Related pages

<Columns cols={2}>
  <Card title="Message personalization" href="./message-personalization" icon="sparkles">
    Overview of all personalization options in OneSignal, including when to use Custom Events vs other methods.
  </Card>

  <Card title="Tags" href="./add-user-data-tags" icon="tag">
    Learn how to set tags on users via SDK, API, or CSV import.
  </Card>

  <Card title="Using Liquid syntax" href="./using-liquid-syntax" icon="droplet">
    Complete Liquid reference with filters, conditionals, loops, and string manipulation.
  </Card>

  <Card title="Templates" href="./templates" icon="file">
    Create and manage reusable message templates for use in Journeys.
  </Card>

  <Card title="In-app message examples" href="./example-tag-substitution" icon="mobile">
    Display personalized in-app messages based on tags.
  </Card>

  <Card title="Abandoned cart tutorial" href="./abandoned-cart" icon="cart-shopping">
    Build an abandoned cart Journey using Tags and Properties.
  </Card>
</Columns>

<Info>
  Need help?

  Chat with our Support team or email `support@onesignal.com`

  Please include:

* Details of the issue you're experiencing and steps to reproduce if available
* Your OneSignal App ID
* The External ID or Subscription ID if applicable
* The URL to the message you tested in the OneSignal Dashboard if applicable
* Any relevant [logs or error messages](/docs/en/capturing-a-debug-log)

  We're happy to help!
</Info>

***

Built with [Mintlify](https://mintlify.com).
