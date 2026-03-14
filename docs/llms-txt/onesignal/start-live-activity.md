# Source: https://documentation.onesignal.com/reference/start-live-activity.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Start Live Activity

> Remotely start a Live Activity on iOS devices via OneSignal's REST API. Define the activity type, target users, and send dynamic, updatable content directly to a Live Activity interface.

## Overview

Remotely start an iOS Live Activity using OneSignal’s REST API. Live Activities provide real-time updates directly on the lock screen and Dynamic Island (on supported devices), enhancing user engagement with ongoing events like sports games, deliveries, or countdowns.

***

## How to use this API

1. Define a Live Activity in your app. See [Live Activities developer setup](/docs/en/live-activities-developer-setup) to get started.
2. Use the `activity_type` parameter to specify the type of the Live Activity UI to use.
3. Select your target audience to receive the Live Activity. Target all or individual users.
4. Generate a unique `activity_id` to track and manage your Live Activity.
5. Use the `event_attributes` parameter to initialize the Live Activity with static data.
6. Use the `event_updates` parameter to update the Live Activity with dynamic content.

### Select your target audience

Before sending a message, you need to determine who should receive it. OneSignal offers three targeting options:

1. **Aliases & Subscription IDs**: Send messages to specific users using unique identifiers such as External ID (recommended), OneSignal ID, custom alias, or subscription ID.
2. **Segments**: Target predefined user groups based on attributes and behavior.
3. **Filters**: Create custom targeting rules using user properties, such as tags, location, or activity.

<Note>
  You can only use one targeting method per message. For example, you cannot combine alias-based targeting with filters in the same request.

  See [Select your target audience](/reference/create-message#select-your-target-audience) for more information.
</Note>

### Set a unique `activity_id`

* Set a unique `activity_id` to track and manage the Live Activity. This value is crucial for maintaining a consistent reference to the Live Activity across different devices and sessions. Consider using a UUID, CUID, or NanoID for this parameter.
* Ensure that the `activity_id` is unique and consistently used for each Live Activity to avoid conflicts and ensure accurate tracking.

  ```json Example theme={null}
  {
    "activity_id": "217aae2b-42ee-4097-bc3f-b7a6e9d15b9b",
    ...
  }
  ```

<Info>
  See [Live Activities developer setup](/docs/en/live-activities-developer-setup) guide for more information.
</Info>

### Set `event_attributes` to initialize the Live Activity

Set default/static data to display in the Live Activity upon start.

```json Example theme={null}
{
  "event_attributes": {
   "awayTeam": "Away Team Name",
    "homeTeam": "Home Team Name"
  }
}
```

### Set `event_updates` for dynamic content

The content used to update a running Live Activity. The object must conform to the `ContentState` interface defined within your app's Live Activity. See [Live Activities developer setup](/docs/en/live-activities-developer-setup).

Ensure that the `event_updates` object matches the [`ContentState`](https://developer.apple.com/documentation/activitykit/activityattributes/contentstate#) interface exactly as defined in your Live Activity implementation. Inconsistencies can cause Live Activities to fail to display.

```json Example theme={null}
{
  "event_updates": {
    "quarter": 1,
    "homeScore": 70,
    "awayScore": 78,
    "inTimeout": false
  }
}
```

***

## OpenAPI

````yaml POST /apps/{app_id}/activities/activity/{activity_type}
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /apps/{app_id}/activities/activity/{activity_type}:
    post:
      summary: Start Live Activity
      description: >-
        Remotely start a Live Activity on iOS devices via OneSignal's REST API.
        Define the activity type, target users, and send dynamic, updatable
        content directly to a Live Activity interface.
      operationId: start-live-activity
      parameters:
        - name: app_id
          in: path
          description: >-
            Your OneSignal App ID in UUID v4 format. See [Keys &
            IDs](/docs/keys-and-ids).
          schema:
            type: string
          required: true
        - name: Authorization
          in: header
          description: >-
            Your App API key with prefix `Key `. See [Keys &
            IDs](/docs/keys-and-ids).
          required: true
          schema:
            type: string
            default: Key YOUR_APP_API_KEY
        - name: activity_type
          in: path
          description: >-
            The name of the Live Activity defined in your app. This should match
            the `your-nameAttributes` struct used in your app code. See [Live
            Activities developer setup](/docs/live-activities-developer-setup).
            Example: If your app defines a Live Activity as
            `OneSignalWidgetAttributes`, then `activity_type` should be
            `OneSignalWidgetAttributes`.
          schema:
            type: string
          required: true
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required:
                - event
                - activity_id
                - name
                - event_attributes
                - event_updates
                - contents
                - headings
              properties:
                include_aliases:
                  type: object
                  description: >-
                    Target up to 20,000 users by their `external_id`,
                    `onesignal_id`, or your own custom alias. Use with
                    `target_channel` to control the delivery channel. Not
                    compatible with any other targeting parameters like
                    `filters`, `include_subscription_ids`, `included_segments`,
                    or `excluded_segments`. See [Sending messages with the
                    OneSignal API](/reference/create-message#include-aliases).
                  format: json
                  properties:
                    external_id:
                      description: >-
                        An array of external IDs which should be the same as the
                        user ID in your app. This is the recommended method for
                        targeting users. See [Users](/docs/users).
                      type: array
                      items:
                        type: string
                include_subscription_ids:
                  type: array
                  description: >-
                    Target users' specific [subscriptions](/docs/subscriptions)
                    by ID. Include up to 20,000 `subscription_id` per API call.
                    Not compatible with any other targeting parameters like
                    `filters`, `include_aliases`, `included_segments`, or
                    `excluded_segments`. See [Sending messages with the
                    OneSignal API](/reference/create-message).
                  items:
                    type: string
                included_segments:
                  type: array
                  description: >-
                    Target predefined [Segments](/docs/segmentation). Users that
                    are in multiple segments will only be sent the message once.
                    Can be combined with `excluded_segments`. Not compatible
                    with any other targeting parameters like `filters`,
                    `include_aliases`, or `include_subscription_ids`. See
                    [Sending messages with the OneSignal
                    API](/reference/create-message).
                  items:
                    type: string
                excluded_segments:
                  type: array
                  description: >-
                    Exclude users in predefined [Segments](/docs/segmentation).
                    Overrides membership in any segment specified in the
                    `included_segments`. Not compatible with any other targeting
                    parameters like `filters`, `include_aliases`, or
                    `include_subscription_ids`. See [Sending messages with the
                    OneSignal API](/reference/create-message).
                  items:
                    type: string
                filters:
                  type: array
                  description: >-
                    Dynamically target users based on properties like tags,
                    activity, or location using flexible AND/OR logic. Limited
                    to 200 total entries, including fields and `OR` operators.
                    Not compatible with other targeting parameters like
                    `include_aliases`, `include_subscription_ids`,
                    `included_segments`, or `excluded_segments`. See [Sending
                    messages with the OneSignal
                    API](/reference/create-message#filters).
                  items:
                    properties:
                      field:
                        type: string
                        description: The name of the filter to use.
                        default: first_session
                      key:
                        type: string
                        description: Used with the `tag` filter. This is the tag `key`.
                      relation:
                        type: string
                        description: >-
                          Used with most filters. Usually this value is `">"`,
                          `"<"`, `"="`. See the specific filter.
                        default: '>'
                      value:
                        type: string
                        description: >-
                          The value of the `field` or tag `key` in which you
                          want to filter with.
                        default: '1'
                    required:
                      - field
                      - relation
                      - value
                    type: object
                event:
                  type: string
                  description: >-
                    The action to perform on the Live Activity. This request
                    only supports `start`.
                  enum:
                    - start
                  default: start
                activity_id:
                  type: string
                  description: >-
                    An identifier you set when starting the Live Activity to
                    uniquely identify it and associated devices with the event.
                    Save this value because it is required for the [Update Live
                    Activity](/reference/update-live-activity) API. Consider
                    using a UUID, CUID, or NanoID for this parameter.
                event_attributes:
                  type: object
                  description: >-
                    The static data to initialize the Live Activity. See [Live
                    Activities developer
                    setup](/docs/live-activities-developer-setup).
                  format: json
                event_updates:
                  type: object
                  description: >-
                    The content used to update a running Live Activity. The
                    object must conform to the `ContentState` interface defined
                    within your app's Live Activity. See [Live Activities
                    developer setup](/docs/live-activities-developer-setup).
                  format: json
                name:
                  type: string
                  description: >-
                    An internal name you set to help organize and track
                    messages. Not shown to recipients. Maximum 128 characters.
                contents:
                  type: object
                  description: >-
                    The push message body with [language-specific
                    values](/docs/multi-language-messaging#supported-languages).
                  required:
                    - en
                  properties:
                    en:
                      type: string
                      description: >-
                        The required message language type. See [Supported
                        Languages](/docs/multi-language-messaging#supported-languages).
                headings:
                  type: object
                  description: >-
                    The push title with [language-specific
                    values](/docs/multi-language-messaging#supported-languages).
                  required:
                    - en
                  properties:
                    en:
                      type: string
                      description: >-
                        The title in English. Must include the same languages as
                        `contents`.
                stale_date:
                  type: integer
                  description: >-
                    A Unix timestamp (in seconds) that indicates the date the
                    Live Activity is considered outdated. Once this time is
                    reached, the system updates the Live Activity to
                    [`ActivityState.stale`](https://developer.apple.com/documentation/activitykit/activitystate/stale)
                    at which point you can update the Live Activity to indicate
                    that its content is out of date.
                  format: int32
                priority:
                  type: integer
                  description: >-
                    Set the priority based on the urgency of the message. `10` -
                    High priority. `5` - Normal priority. Apple allows a certain
                    budget of High priority updates per hour. Exceeding the
                    budget may throttle your messages. Apple recommends choosing
                    a mix of priority `5` and `10` to prevent throttling. If
                    your app needs more frequent updates, use
                    `NSSupportsLiveActivitiesFrequentUpdates` entry as directed
                    in [Apple's Developer
                    Docs](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications#Determine-the-update-frequency).
                  format: int32
                  enum:
                    - 5
                    - 10
                ios_sound:
                  type: string
                  description: >-
                    The name of a sound file in your app bundle to play when the
                    Live Activity receives an update. If excluded, the system
                    plays the default notification sound. Using the value
                    `"nil"` will silence the sound.
                ios_relevance_score:
                  type: number
                  description: >-
                    A value between `0` and `1`. If you start more than one Live
                    Activity for your app, the Live Activity with the highest
                    relevance score appears in the Dynamic Island. If Live
                    Activities have the same relevance score, the system
                    displays the Live Activity that started first. Additionally,
                    the Relevance Score determines the order of your Live
                    Activities on the Lock Screen.
                  format: double
                idempotency_key:
                  type: string
                  description: >-
                    A unique identifier used to prevent duplicate messages from
                    repeat API calls. See [Idempotent notification
                    requests](/reference/idempotent-notification-requests). Any
                    RFC 9562 UUID supported. Valid for 30 days. Previously
                    called `external_id`.
      responses:
        '201':
          description: '201'
          content:
            application/json:
              schema:
                type: object
                properties:
                  notification_id:
                    type: string
                    description: >-
                      The ID of the Live Activity that was created in UUID v4
                      format.
        '400':
          description: '400'
          content:
            application/json:
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
                      description: >-
                        Reason for the message not being started. Usually due to
                        the activity type not being found in the app.
      deprecated: false

````

Built with [Mintlify](https://mintlify.com).
