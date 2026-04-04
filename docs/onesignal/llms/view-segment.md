# Source: https://documentation.onesignal.com/reference/view-segment.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# View segment

> Retrieve details for a single segment by its ID, including subscriber count and optionally segment metadata and filters.

## Overview

Retrieve details for a single segment by its ID. By default, this endpoint returns only the subscriber count. Use the optional `include-segment-detail` parameter to also retrieve segment metadata and filters.

<Note>
  The `segment_id` can be found using the [View segments](/reference/view-segments) API or in the URL of the segment when viewing it in the dashboard.
</Note>

<Warning>
  **User-based segments not supported**: Segments containing message event or custom event filters (user-based segments) are not yet supported via this API. Attempting to fetch these segments will return a 400 error. These segments can only be managed through the dashboard UI.
</Warning>

***

## How to use this API

### Basic usage

By default, this endpoint returns only the subscriber count for the segment:

```json  theme={null}
{
  "subscriber_count": 12345
}
```

### Include segment details

To retrieve full segment details including metadata and filters, set `include-segment-detail=true`:

```
GET /apps/{app_id}/segments/{segment_id}?include-segment-detail=true
```

This returns the subscriber count along with a `payload` object containing segment details:

<CodeGroup>
  ```json Simple filter theme={null}
  {
    "subscriber_count": 12345,
    "payload": {
      "id": "4414c404-56a3-11ed-9b6a-0242ac120002",
      "name": "Subscribed Users",
      "created_at": 1658584650,
      "source": "custom",
      "filters": [
        {
          "field": "session_count",
          "relation": ">",
          "value": "5"
        }
      ]
    }
  }
  ```

  ```json With AND/OR operators theme={null}
  {
    "subscriber_count": 5678,
    "payload": {
      "id": "5525d515-67b4-22fe-0c7b-1353bd231113",
      "name": "Engaged Users",
      "created_at": 1658584650,
      "source": "custom",
      "filters": [
        {"field": "session_count", "relation": ">", "value": "2"},
        {"operator": "AND"},
        {"field": "tag", "key": "level", "relation": "=", "value": "10"},
        {"operator": "OR"},
        {"field": "last_session", "relation": "<", "hours_ago": "24"}
      ]
    }
  }
  ```

</CodeGroup>

### Filters format

The `filters` array uses the **same format** as the [Create segment](/reference/create-segments) API. This means you can:

* Read filters from this endpoint
* Modify them as needed
* Use them directly with the [Update segment](/reference/update-segment) or [Create segment](/reference/create-segments) APIs

The array contains filter objects and operator objects:

**Filter object** - defines a condition:

| Field                   | Type    | Description                                                                                                                                                   |
| ----------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `field`                 | string  | The filter type: `tag`, `last_session`, `first_session`, `session_count`, `session_time`, `language`, `app_version`, `location`, `country`, `email`, `rooted` |
| `relation`              | string  | The comparison operator: `>`, `<`, `=`, `!=`, `exists`, `not_exists`, `time_elapsed_gt`, `time_elapsed_lt`                                                    |
| `value`                 | string  | The filter value (for most filter types)                                                                                                                      |
| `key`                   | string  | The filter key (required for `tag` filters)                                                                                                                   |
| `hours_ago`             | string  | Hours ago value (for `last_session`/`first_session` filters)                                                                                                  |
| `radius`, `lat`, `long` | string  | Location parameters (for `location` filters)                                                                                                                  |
| `unsupported_in_api`    | boolean | If `true`, this filter cannot be used with Create/Update segment APIs (see note below)                                                                        |

**Operator object** - combines filters:

| Field      | Type   | Description                                                                        |
| ---------- | ------ | ---------------------------------------------------------------------------------- |
| `operator` | string | Either `AND` or `OR`. Filters connected with `AND` have higher priority than `OR`. |

<Warning>
  Some segments created via the dashboard UI may contain filter types not supported by the public API (e.g., `message_event`, `custom_event`). These filters will include `unsupported_in_api: true`. You cannot use these filters when creating or updating segments via the API.
</Warning>

### Payload fields

| Field        | Type    | Description                                                            |
| ------------ | ------- | ---------------------------------------------------------------------- |
| `id`         | string  | The unique identifier for the segment (UUID v4).                       |
| `name`       | string  | The segment name (max 128 characters).                                 |
| `created_at` | integer | Unix timestamp when the segment was created.                           |
| `source`     | string  | The source of the segment: `default`, `custom`, or `quickstart`.       |
| `filters`    | array   | Array of filter and operator objects that define the segment criteria. |

***

## OpenAPI

````yaml GET /apps/{app_id}/segments/{segment_id}
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /apps/{app_id}/segments/{segment_id}:
    get:
      summary: View segment
      description: >-
        Retrieve details for a single segment by its ID, including subscriber
        count and optionally segment metadata and filters.
      operationId: view-segment
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
        - name: segment_id
          in: path
          description: >-
            The segment's unique identifier. Can be found using the View
            segments API or in the dashboard URL.
          schema:
            type: string
            default: YOUR_SEGMENT_ID
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
        - name: include-segment-detail
          in: query
          description: >-
            Set to `true` to include segment metadata and filters in the
            response.
          required: false
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Basic:
                  value:
                    subscriber_count: 12345
                With Details (simple):
                  value:
                    subscriber_count: 12345
                    payload:
                      id: 4414c404-56a3-11ed-9b6a-0242ac120002
                      name: Subscribed Users
                      created_at: 1658584650
                      source: custom
                      filters:
                        - field: session_count
                          relation: '>'
                          value: '5'
                With Details (AND/OR):
                  value:
                    subscriber_count: 5678
                    payload:
                      id: 5525d515-67b4-22fe-0c7b-1353bd231113
                      name: Engaged Users
                      created_at: 1658584650
                      source: custom
                      filters:
                        - field: session_count
                          relation: '>'
                          value: '2'
                        - operator: AND
                        - field: tag
                          key: level
                          relation: '='
                          value: '10'
                        - operator: OR
                        - field: last_session
                          relation: <
                          hours_ago: '24'
              schema:
                type: object
                properties:
                  subscriber_count:
                    type: integer
                    description: The number of subscribers matching this segment.
                  payload:
                    type: object
                    description: >-
                      Segment details. Only included when
                      `include-segment-detail=true`.
                    properties:
                      id:
                        type: string
                        description: The unique identifier for the segment (UUID v4).
                      name:
                        type: string
                        description: The segment name.
                      created_at:
                        type: integer
                        description: Unix timestamp when the segment was created.
                      source:
                        type: string
                        description: The source of the segment.
                        enum:
                          - default
                          - custom
                          - quickstart
                      filters:
                        type: array
                        description: >-
                          Array of filter and operator objects defining the
                          segment criteria. Uses the same format as the Create
                          segment API, so filters can be directly used to
                          recreate or update the segment.
                        items:
                          oneOf:
                            - type: object
                              description: A filter condition.
                              properties:
                                field:
                                  type: string
                                  description: The filter type.
                                relation:
                                  type: string
                                  description: The comparison operator.
                                  enum:
                                    - '>'
                                    - <
                                    - '='
                                    - '!='
                                    - exists
                                    - not_exists
                                    - time_elapsed_gt
                                    - time_elapsed_lt
                                value:
                                  type: string
                                  description: The filter value.
                                key:
                                  type: string
                                  description: The filter key (used for tag filters).
                                hours_ago:
                                  type: string
                                  description: >-
                                    Hours ago value (used for
                                    last_session/first_session filters).
                                radius:
                                  type: string
                                  description: >-
                                    Radius in meters (used for location
                                    filters).
                                lat:
                                  type: string
                                  description: Latitude (used for location filters).
                                long:
                                  type: string
                                  description: Longitude (used for location filters).
                                unsupported_in_api:
                                  type: boolean
                                  description: >-
                                    If true, this filter type cannot be used
                                    with the Create/Update segment APIs. These
                                    filters were created via the dashboard UI
                                    using features not available in the public
                                    API (e.g., message_event, custom_event
                                    filters).
                            - type: object
                              description: A logical operator to combine filters.
                              properties:
                                operator:
                                  type: string
                                  description: The logical operator.
                                  enum:
                                    - AND
                                    - OR
                              required:
                                - operator
        '400':
          description: '400'
          content:
            application/json:
              examples:
                Missing Authorization:
                  value:
                    errors:
                      - Please include a case-sensitive header of Authorization
                User-based Segment:
                  value:
                    errors:
                      - >-
                        User-based segments (with message event or custom event
                        filters) are not yet supported via the API
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
        '404':
          description: '404'
          content:
            application/json:
              examples:
                Result:
                  value:
                    errors:
                      - segment not found
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
      deprecated: false
      security: []

````

Built with [Mintlify](https://mintlify.com).
