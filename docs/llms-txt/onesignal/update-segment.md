# Source: https://documentation.onesignal.com/reference/update-segment.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update segment

> Update an existing segment's name and/or filters. The name parameter is always required. When filters are provided, all existing filters are replaced with the new ones.

## Overview

Update an existing segment's name and/or filters. This API allows you to modify [Segments](/docs/en/segmentation) programmatically without having to delete and recreate them.

<Note>
  The `name` parameter is always required, even if you're not changing it. When filters are provided, all existing filters are **replaced** with the new ones. Omit the `filters` parameter to keep existing filters intact. The `filters` array cannot be empty—if provided, it must contain at least one filter.
</Note>

***

## How to use this API

### Update segment name only

To update just the segment name without changing filters:

```json  theme={null}
{
  "name": "New Segment Name"
}
```

### Update segment filters

To update the segment filters (this replaces all existing filters), provide the `name` (required) and `filters`:

```json  theme={null}
{
  "name": "Updated Segment",
  "filters": [
    {"field": "session_count", "relation": ">", "value": "5"},
    {"operator": "AND"},
    {"field": "tag", "key": "subscription", "relation": "=", "value": "premium"}
  ]
}
```

### Filter syntax

The filter syntax is identical to the [Create segment](/reference/create-segments) API. Available filters include:

* `tag` - Filter by user tags
* `last_session` - Filter by last active time
* `first_session` - Filter by first session time
* `session_count` - Filter by number of sessions
* `session_time` - Filter by total usage duration
* `language` - Filter by user language
* `app_version` - Filter by app version
* `location` - Filter by GPS coordinates
* `country` - Filter by country

Use `AND` and `OR` operators to combine filters:

```json  theme={null}
{
  "name": "Engaged Premium Users",
  "filters": [
    {"field": "tag", "key": "plan", "relation": "=", "value": "premium"},
    {"operator": "AND"},
    {"field": "session_count", "relation": ">", "value": "10"},
    {"operator": "OR"},
    {"field": "tag", "key": "vip", "relation": "=", "value": "true"}
  ]
}
```

***

## Response

### Success response

```json  theme={null}
{
  "success": true,
  "id": "7ed2887d-bd24-4a81-8220-4b256a08ab19"
}
```

### Error responses

| Status Code | Description                                                                              |
| ----------- | ---------------------------------------------------------------------------------------- |
| 400         | Bad request - Invalid filters, duplicate segment name, or segment used by active Journey |
| 403         | Forbidden - API not available for your plan                                              |
| 404         | Not found - Segment does not exist                                                       |
| 429         | Rate limit exceeded                                                                      |

***

## OpenAPI

````yaml PATCH /apps/{app_id}/segments/{segment_id}
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
    patch:
      summary: Update segment
      description: >-
        Update an existing segment's name and/or filters. The name parameter is
        always required. When filters are provided, all existing filters are
        replaced with the new ones.
      operationId: update-segment
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
            The `segment_id` can be found in the URL of the segment when viewing
            it in the dashboard.
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
              properties:
                name:
                  type: string
                  description: Required. The segment name. Maximum 128 characters.
                  default: YOUR_SEGMENT_NAME
                filters:
                  type: array
                  description: >-
                    Optional. When provided, replaces all existing filters.
                    Filters define the segment based on user properties like
                    tags, activity, or location using flexible AND/OR logic.
                    Limited to 200 total entries, including fields and `OR`
                    operators. See [Create segment](/reference/create-segments)
                    for filter syntax.
                  items:
                    oneOf:
                      - title: Filter
                        description: Required. The filter object.
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
        '200':
          description: '200'
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
                      true if the segment was updated successfully, false
                      otherwise.
                    default: true
                  id:
                    type: string
                    description: The UUID of the updated segment.
        '400':
          description: '400'
          content:
            application/json:
              examples:
                Result:
                  value:
                    success: false
                    errors:
                      - Segment name is already taken.
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: false
                    default: true
                  errors:
                    type: array
                    items:
                      type: string
                      example: Segment name is already taken.
        '403':
          description: '403'
          content:
            application/json:
              examples:
                Result:
                  value:
                    success: false
                    errors:
                      - This API is not available for applications on your plan.
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: false
                  errors:
                    type: array
                    items:
                      type: string
                      example: This API is not available for applications on your plan.
        '404':
          description: '404'
          content:
            application/json:
              examples:
                Result:
                  value:
                    success: false
                    errors:
                      - segment not found
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: false
                  errors:
                    type: array
                    items:
                      type: string
                      example: segment not found
        '429':
          description: '429'
          content:
            application/json:
              examples:
                Result:
                  value:
                    errors:
                      - code: Rate Limit Exceeded
                        title: Example error title
                        meta: {}
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        code:
                          type: string
                          example: Rate Limit Exceeded
                        title:
                          type: string
                          example: Example error title
                        meta:
                          type: object
                          properties: {}
      deprecated: false
      security: []

````

Built with [Mintlify](https://mintlify.com).
