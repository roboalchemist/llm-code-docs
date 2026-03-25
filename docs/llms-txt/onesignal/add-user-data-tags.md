# Source: https://documentation.onesignal.com/docs/en/add-user-data-tags.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Tags

> Use OneSignal Data Tags to store user properties and track events for advanced segmentation and personalized messaging.

Data Tags are key-value pairs that let you store custom properties and track user behavior in OneSignal. They enable powerful segmentation and personalization.

<Frame>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/t82DSCUXShk?si=KH_u3zB2N5ci8GLT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

Use tags to:

* Store user traits like `subscription_tier` or `name`
* Track behaviors like `purchases`, `clicks`, or `levels`
* Segment users for messages and Journeys
* Personalize message content

<Frame>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/Z-rYqwEUU0M?si=Qjx2dMdFXwXSuZJR" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

***

## Data tag value formatting rules

All Tag values must be **strings**. You can still store numbers, timestamps, and boolean-like values—just stringify them!

| Value Type   | Format Example                      | Notes                                                                    |
| ------------ | ----------------------------------- | ------------------------------------------------------------------------ |
| String Label | `"free"`, `"VIP"`                   | For user types, privileges, statuses                                     |
| Number       | `"42"`, `"3.14"`                    | Enables numeric filters (`greater than`, `less than`)                    |
| Timestamp    | `"1685400000"`                      | Unix timestamp (in seconds). Use with [Time Operators](./time-operators) |
| Boolean      | `"true"` / `"false"`, `"1"` / `"0"` | Use `"1"`/`"0"` to reduce payload size                                   |

<Frame>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/YTp-jLcajJ0?si=uSRn2cQ7Yur5MAp0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

<Warning>
  **Not supported:** Arrays, objects, nested values, or JSON blobs. If you need to store complex data, use [Custom Events](./custom-events).
</Warning>

### Restricted keywords

The following keywords are restricted and should not be used as tag keys because they are used internally for message personalization:
`message`, `notification`, `subscription`, `user`, `template`, `app`, `org`, `dynamic_content`, `data_feed`, `journey`, `custom_data`

See [Message Personalization](./message-personalization) for more details.

### Tags vs Custom Events

[Tags](/docs/en/add-user-data-tags) and [Custom Events](/docs/en/custom-events) are both ways to add data to your users. However, there are some key differences:

| Feature        |                      Tags                     |                                          Custom Events                                         |
| -------------- | :-------------------------------------------: | :--------------------------------------------------------------------------------------------: |
| Data usage     |        Segmentation and personalization       | Trigger Journeys without a Segment, Wait Until steps, personalization directly within Journeys |
| Data retention |                    Lifetime                   |        30+ days ([lifetime storage is available](/docs/en/billing-faq#streaming-events))       |
| Data format    |          Key-value strings or numbers         |                                              JSON                                              |
| Data source    | OneSignal SDK, API, or integrations (limited) |                               OneSignal SDK, API, or integrations                              |
| Data access    |    Segmentation and message personalization   |        Journeys and Journey-message-template personalization, Segmentation (Coming soon)       |

The key distinction between Tags and Custom Events is in their depth and use cases. Tags are properties of a user, such as Name, Account Status, or Location. Events are thing that the user has done, such as Purchasing an Item, Completing a Level, or Inviting a Friend. Both tags and events can be used for segmentation and personalization.

In practice, you will likely use both:

* Tags for user properties that are static and don't change often
* Custom Events for real-time scenarios, complex segmentation, and more sophisticated journey workflows

***

## Recommended tag strategies

Data Tags should represent information you want to **use in messages or audience segmentation**. They're not meant to store full user profiles or logs—use your backend database for that.

<Frame>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/DeCnQYA21TY?si=YnAv50tpiiVdNEX7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

### Event-based behavior tags

Track user actions with tags. Great for triggering Journeys, follow-ups, or reminders.

| Key               | Value Example              | Description                                                                     |
| ----------------- | -------------------------- | ------------------------------------------------------------------------------- |
| `cart_update`     | `"1685400000"`             | Last time user added something to cart. Use [Time Operators](./time-operators). |
| `last_order`      | `"1684100000"`             | Last completed purchase timestamp                                               |
| `amount_spent`    | `"100"`                    | Total spent—stringified number, no currency symbol                              |
| `social_share`    | `"2"`                      | Count of social shares or referrals                                             |
| `tutorial_status` | `"step2"` or `"completed"` | Tutorial progress—use readable or numbered string values                        |

### Game activity tags

Used by games to personalize based on user performance.

| Key          | Value Example | Description               |
| ------------ | ------------- | ------------------------- |
| `points`     | `"1250"`      | Experience or game points |
| `level`      | `"8"`         | Current game level        |
| `high_score` | `"3000"`      | Highest score achieved    |

### Account status tags

Use these to target users by account tier or change in status.

| Key               | Value Example           | Description                       |
| ----------------- | ----------------------- | --------------------------------- |
| `user_type`       | `"free"`, `"premium"`   | Subscription or access tier       |
| `has_downgraded`  | `"1"` or `"1685400000"` | Boolean or timestamp of downgrade |
| `user_privileges` | `"admin"`, `"guest"`    | Role-based segmentation           |

<Note>
  Use **External ID** to identify individual users. Do **not** use tags for this purpose. See [External ID](./users#external-id) and [Aliases](./aliases).
</Note>

### Personalization tags

Great for name-based message customization using [Variable Substitution](./message-personalization).

| Key          | Value Example     | Description            |
| ------------ | ----------------- | ---------------------- |
| `first_name` | `"Jon"`           | First name             |
| `last_name`  | `"Smith"`         | Last name              |
| `user_name`  | `"PokeCatcher22"` | Display or screen name |

### Location & demographic tags

Segment users by region or age.

| Key          | Value Example   | Description                                                                       |
| ------------ | --------------- | --------------------------------------------------------------------------------- |
| `region`     | `"New York"`    | Metro area, optionally use [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) |
| `postcode`   | `"94105"`       | Zip or postal code                                                                |
| `location`   | `"Downtown LA"` | Custom string location                                                            |
| `birthdate`  | `"915148800"`   | Unix timestamp in seconds (birth date)                                            |
| `birth_year` | `"1998"`        | Four-digit birth year                                                             |
| `age_range`  | `"18-35"`       | Useful for general audience segmentation                                          |

## How to add, update, and remove Tags

You can manage Tags using any of the methods below, depending on your use case and technical setup.

<Frame>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/e5B3nJyr_ao?si=PfVu4bHMkQJydc41" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

<br />

<Columns cols={2}>
  <Card title="SDK Methods (Recommended)">
    Set tags in real time from your app or website as users perform actions.

    * → [Mobile SDK Reference](./mobile-sdk-reference#data-tags)
    * → [Web SDK Reference](./web-sdk-reference#data-tags)
  </Card>

  <Card title="REST API" href="/reference/update-user">
    Add, update, or remove tags server-side using our REST API.
  </Card>

  <Card title="Journeys" href="./journeys-overview">
    Automatically apply tags as users move through Journey steps.
  </Card>

  <Card title="CSV Import" href="./import">
    Bulk update user tags by uploading a CSV with `external_id` or `subscription_id`.
  </Card>

  <Card title="Web Category Prompts" href="./permission-requests">
    Prompt users to self-select interests, which are stored as tags.
  </Card>

  <Card title="In-App Messages" href="./in-app-messages-setup">
    Collect or update tags based on in-app message click actions.
  </Card>

  <Card title="Manual Entry">
    Directly edit tags from the OneSignal Dashboard.

    * Go to **Audience > Users > User Profile > Tags**
  </Card>

  <Card title="Third-Party Integrations" href="./integrations">
    Some integrations support syncing tags automatically.

    * Segment, HubSpot, Mixpanel, and others
  </Card>
</Columns>

***

## FAQ

### How many tags can I set per user?

Depends on your plan. See your [plan limits](https://onesignal.com/pricing) or [contact sales](https://onesignal.com/contact) to increase your quota.

### What happens to my tags if I exceed plan limits?

There is no limit to the number of tags available within a OneSignal app. The limit applies to how many tags can be set on each individual user at a single time.

You **can’t add or update** tags for users who are at or above their limit. You must delete tags first, then send a second request to add new ones.

Tags already set will persist.

Example:

Your plan limit = 20 tags/user.

* User has 19 tags:
  * ✅ Add 1 new tag = success
  * ❌ Add 2+ new tags = failure
* User has 20 tags:
  * ❌ Add any new tag = failure
  * ✅ Update 1+ existing tag = success

### Where can I check tag usage?

* Dashboard: **Audience > Users > Tags column**
* [Export users](./exporting-data) for a complete view

### How do I reduce tag usage?

* Remove tags using SDK or API
* Use [CSV Import](./import) to bulk delete
* Use fewer, more reusable tags (e.g., `status:active`)

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
