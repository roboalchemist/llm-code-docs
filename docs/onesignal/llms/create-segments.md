# Source: https://documentation.onesignal.com/reference/create-segments.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create segment

> Programmatically create segments in your OneSignal app using flexible filters and targeting rules.

## Overview

Use this API to create new [Segments](/docs/en/segmentation) programmatically. These segments are then accessible in the OneSignal Dashboard and usable in messages, Journeys, and in-app messaging campaigns.

<Note>
  To modify an existing segment, use the [Update segment](/reference/update-segment) API.
</Note>

***

## How to use this API

This endpoint allows your backend to define audience segments by passing in a combination of filters and logical operators like `"AND"` and `"OR"`, mirroring the segmentation capabilities of the OneSignal Dashboard.

### Name the segment

The name of the segment as it shows in the OneSignal dashboard and accessible via the `included_segments` and `excluded_segments` targeting parameters.

### Define the `filters`

Available filters:

* [operator](#operator)
* [tag](#tag)
* [last\_session](#last_session)
* [first\_session](#first_session)
* [session\_count](#session_count)
* [session\_time](#session_time-1)
* [language](#language)
* [app\_version](#app_version)
* [location](#location)
* [country](#country)

### `operator`

**Description**

Allows you to combine or separate properties. Filters combined with an `"AND"` have higher priority than `"OR"` filters.

* `"AND"` = the 2+ connected filters must be satisfied for the recipient to be included. Filter entries use this by default and its not required to be included.
* `"OR"` = the 2 filters separated by the `"OR"` operator are mutually exclusive. The recipients only need to satisfy the conditions on either side of the `"OR"` operator.

<CodeGroup>
  ```json AND example theme={null}
  // Users must satisfy both filters to be included.
  // Notice the AND operator is not required

  "filters": [
  {"field": "tag", "key": "level", "relation": "=", "value": "10"},
  {"field": "language", "relation": "=","value": "en"}
  ]

  // The same example using the AND operator. This is not required.
  "filters": [
  {"field": "tag", "key": "level", "relation": "=", "value": "10"},
  {"operator": "AND"},
  {"field": "language", "relation": "=","value": "en"}
  ]

  ```

  ```json OR example theme={null}
  // Users can satisfy either filter to be included.

  "filters": [
    {"field": "tag", "key": "level", "relation": "=", "value": "10"},
    {"operator": "OR"},
    {"field": "tag", "key": "level", "relation": "=", "value": "20"}
  ]
  ```

  ```json Combinations theme={null}
  // In this example, users must either have:
  // The specified session_count AND tag requirement
  // Or it will be all records where last_session is satisfied
  {
    "name": "2 filters or 1",
    "filters": [
      {"field": "session_count", "relation": ">", "value": "2"},
      {"operator": "AND"},
      {"field": "tag", "relation": "!=", "key": "tag_key", "value": "1"},
      {"operator": "OR"},
      {"field": "last_session", "relation": "<", "hours_ago": "30"}
    ]
  }

  // Similar to the first example, this shows how to require a specific field
  // across other filters

  {
    "name": "3 filters, 1 required across all",
    "filters": [
      {"field": "session_count", "relation": ">", "value": "2"},
      {"operator": "AND"},
      {"field": "tag", "relation": "!=", "key": "tag_key", "value": "1"},
      {"operator": "OR"},
      {"field": "last_session", "relation": "<", "hours_ago": "30"},
      {"operator": "AND"},
      {"field": "tag", "relation": "!=", "key": "tag_key", "value": "1"}
    ]
  }
  ```

</CodeGroup>

### `tag`

**Description**

Maps to the [Tags](/docs/en/add-user-data-tags) set on [Users](/docs/en/users).

**Do not use tags for targeting individual users like a "user id".** Instead use [External ID](/docs/en/users) or custom [Aliases](/docs/en/aliases) and the `include_aliases` targeting property.

* `relation` = `">"`, `"<"`, `"="`, `"!="`, `"exists"`, `"not_exists"`, `"time_elapsed_gt"`, (time elapsed greater than) and `"time_elapsed_lt"` (time elapsed less than)
  * The `time_elapsed_gt/lt` fields correspond to [Time Operators](/docs/en/time-operators) and require a paid plan.
* `key` = Tag key to compare.
* `value` = Tag value to compare. Not required for `"exists"` or `"not_exists"`.

<CodeGroup>
  ```json json theme={null}
  "filters": [
    {"field": "tag", "key": "level", "relation": "=", "value": "10"}
  ]
  ```
</CodeGroup>

### `last_session`

**Description**

Maps to the last active time the [Subscriptions](/docs/en/subscriptions) used the app.

* `relation` = `">"` or `"<"`
* `hours_ago` = number of hours before or after the user's last session. Example: `"1.1"`

<CodeGroup>
  ```json json theme={null}
  "filters": [
    {"field": "last_session", "relation": ">","hours_ago": "10"}
  ]
  ```
</CodeGroup>

### `first_session`

**Description**

Maps to the first date and time the [Users](/docs/en/users) were created within OneSignal.

* `relation` = `">"` or `"<"`
* `hours_ago` = number of hours before or after the user's first session. Example: `"1.1"`

<CodeGroup>
  ```json json theme={null}
  "filters": [
    {"field": "first_session", "relation": "<","hours_ago": "24"}
  ]
  ```
</CodeGroup>

### `session_count`

**Description**

Maps to the amount of sessions for the [Subscriptions](/docs/en/subscriptions).

* `relation` = `">"`, `"<"`, `"="` or `"!="`
* `value` = number sessions. Example: `"1"`

<CodeGroup>
  ```json json theme={null}
  "filters": [
    {"field": "session_count", "relation": ">","value": "5"}
  ]
  ```
</CodeGroup>

### `session_time`

**Description**

Maps to the usage duration of your [Subscriptions](/docs/en/subscriptions) which is the total number of seconds they had your app open.

* `relation` = `">"` or `"<"`
* `value` = Time in seconds the user has been in your app. Example: 1 day is `"86400"` seconds

<CodeGroup>
  ```json json theme={null}
  "filters": [
    {"field": "session_time", "relation": ">","value": "86400"}
  ]
  ```
</CodeGroup>

### `language`

**Description**

Maps to the language code of your [Users](/docs/en/users). See [Multi-Language Messaging](/docs/en/multi-language-messaging) for details and [supported language codes](/docs/en/multi-language-messaging#supported-languages).

* `relation` = `"="` or `"!="`
* `value` = 2 character language code. Example: `"en"`.

<CodeGroup>
  ```json json theme={null}
  "filters": [
    {"field": "language", "relation": "=","value": "en"},
    {"operator": "OR"},
    {"field": "language", "relation": "=","value": "es"}
  ]
  ```
</CodeGroup>

### `app_version`

**Description**

Maps to your app version set on [Subscriptions](/docs/en/subscriptions).

* `relation` = `">"`, `"<"`, `"="` or `"!="`
* `value` = app version. Example: `"1.0.0"`

<CodeGroup>
  ```json json theme={null}
  "filters": [
    {"field": "app_version", "relation": "=","value": "1.0.1"}
  ]
  ```
</CodeGroup>

### `location`

**Description**

Maps to the GPS coordinates of the device. Location tracking must be turned on and accepted by the user. See [Location-Triggered Notifications](/docs/en/location-triggered-event) for more details.

* `radius` = in meters
* `lat` = latitude
* `long` = longitude

<CodeGroup>
  ```json json theme={null}
  "filters": [
    {"field": "location", "radius": "1000","lat": "37.77", "long":"-122.43"}
  ]
  ```
</CodeGroup>

### `country`

**Description**

Maps to the country code of your [Users](/docs/en/users). Uses ISO 3166-1 Alpha-2 format (two-letter country code).

* `relation` = `"="` or `"!="`
* `value` = Two-letter country code in uppercase. Example: `"US"`, `"GB"`, `"CA"`.

<CodeGroup>
  ```json json theme={null}
  "filters": [
    {"field": "country", "relation": "=", "value": "US"}
  ]
  ```
</CodeGroup>

***

## OpenAPI

````yaml POST /apps/{app_id}/segments
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /apps/{app_id}/segments:
    post:
      summary: Create segment
      description: >-
        Programmatically create segments in your OneSignal app using flexible
        filters and targeting rules.
      operationId: create-segments
      parameters:
        - name: app_id
          in: path
          description: >-
            Your OneSignal App ID in UUID v4 format. See [Keys &
            IDs](/docs/keys-and-ids).
          schema:
            type: string
            default: YOUR_APP_ID
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
        - name: Content-Type
          in: header
          required: true
          schema:
            type: string
            default: application/json; charset=utf-8
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required:
                - name
                - filters
              properties:
                id:
                  type: string
                  description: >-
                    UUID of the segment. If left empty, it will be assigned
                    automatically.
                name:
                  type: string
                  description: >-
                    An internal name you set to help organize and track
                    Segments. Maximum 128 characters.
                  default: YOUR_SEGMENT_NAME
                filters:
                  type: array
                  description: >-
                    Filters define the segment based on user properties like
                    tags, activity, or location using flexible AND/OR logic.
                    Limited to 200 total entries, including fields and `OR`
                    operators. See [Sending messages with the OneSignal
                    API](/reference/create-message#filters).
                  items:
                    oneOf:
                      - title: Filter
                        description: Required. The fitler object.
                        required:
                          - field
                          - relation
                        type: object
                        properties:
                          field:
                            type: string
                            description: The name of the filter to use.
                            enum:
                              - tag
                              - last_session
                              - first_session
                              - session_count
                              - session_time
                              - language
                              - app_version
                              - location
                              - country
                          relation:
                            type: string
                            description: >-
                              Used with most filters. See details on the
                              specific filter.
                            enum:
                              - '='
                              - '!='
                              - '>'
                              - <
                              - exists
                              - not_exists
                              - time_elapsed_gt
                              - time_elapsed_lt
                          key:
                            type: string
                            description: Used with the `tag` filter. This is the tag `key`.
                          value:
                            type: string
                            description: >-
                              The value of the `field` or tag `key` in which you
                              want to filter with.
                      - title: Operator
                        type: object
                        properties:
                          operator:
                            type: string
                            description: >-
                              Chain filter conditions with implicit `AND` and
                              `OR` logic. Never end your `filters` object with
                              an `operator`. See
                              [filters](/reference/create-message#filters) for
                              more.
                            enum:
                              - AND
                              - OR
                            default: AND
                  minItems: 1
                  maxItems: 200
      responses:
        '201':
          description: '201'
          content:
            application/json:
              examples:
                Result:
                  value:
                    success: true
                    id: 7ed2887d-bd24-4a81-8220-4b256a08ab19
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    description: >-
                      true if the segment was created successfully, false
                      otherwise.
                    default: true
                  id:
                    type: string
                    description: The UUID of the created segment.
        '400':
          description: '400'
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    description: If the segment was created successfully.
                  errors:
                    type: array
                    items:
                      type: string
                      description: The reason why the segment was not created.
      deprecated: false
      security: []

````

Built with [Mintlify](https://mintlify.com).
