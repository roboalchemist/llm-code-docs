# Source: https://documentation.onesignal.com/reference/list-audit-logs.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List audit logs

> Retrieve a paginated, time-scoped list of audit log events for an organization. Requires an Enterprise plan. Supports filtering by app, action, actor, target, and IP address.

## Overview

The List audit logs API returns a record of actions taken within your organization — who did what, when, and from where. Use it to support compliance workflows, security investigations, and activity monitoring.

<Note>
  This endpoint requires an Enterprise plan with the audit logs entitlement enabled. Contact your account manager to enable access. See [Audit logs](/docs/en/audit-logs) for a feature overview.
</Note>

***

## How to use this API

Authenticate with your [Organization API Key](/docs/en/keys-and-ids#organization-api-key). App-level API keys are not accepted.

### Time range

Every initial request requires a `start_time`. Results are returned in ascending chronological order.

* The maximum lookback window is **90 days**.
* `start_time` must be an ISO 8601 timestamp within the last 90 days.
* `end_time` is optional and defaults to the current time.
* Historical data is only available from **2026-02-18T00:00:00Z** onward.

### Cursor-based pagination

When a response contains more results than the requested `limit`, the response includes `has_more: true` and a `next_cursor` value. Pass `next_cursor` as the `cursor` parameter in the next request. When using a cursor, `start_time` and `end_time` are not required.

<Warning>
  When `app_ids` is set, org-level events (those not associated with any specific app) are always included in results alongside the filtered app events.
</Warning>

## OpenAPI

````yaml GET /organizations/{organization_id}/audit_logs
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /organizations/{organization_id}/audit_logs:
    get:
      summary: List audit logs
      description: >-
        Retrieve a paginated, time-scoped list of audit log events for an
        organization. Requires an Enterprise plan with the audit logs
        entitlement enabled.
      operationId: list-audit-logs
      parameters:
        - name: organization_id
          in: path
          description: >-
            The UUID of the organization to retrieve audit logs for. Must match
            the authenticated Organization API Key.
          required: true
          schema:
            type: string
            default: YOUR_ORG_ID
        - name: Authorization
          in: header
          description: >-
            Your Organization API key with prefix `Key `. See [Keys &
            IDs](/docs/keys-and-ids).
          required: true
          schema:
            type: string
            default: Key YOUR_ORGANIZATION_API_KEY
        - name: start_time
          in: query
          description: >-
            Start of the time range in ISO 8601 format (e.g.
            `2026-02-01T00:00:00Z`). Required unless `cursor` is provided. Must
            be within the last 90 days and no earlier than
            `2026-02-18T00:00:00Z`.
          schema:
            type: string
        - name: end_time
          in: query
          description: >-
            End of the time range in ISO 8601 format. Defaults to the current
            time. Must be after `start_time`.
          schema:
            type: string
        - name: cursor
          in: query
          description: >-
            Pagination cursor returned in a previous response as `next_cursor`.
            When provided, `start_time` and `end_time` are ignored.
          schema:
            type: string
        - name: limit
          in: query
          description: >-
            Maximum number of events to return per page. Minimum `1`, maximum
            `100`. Values outside this range are clamped automatically.
          schema:
            type: integer
            default: 100
            minimum: 1
            maximum: 100
        - name: app_ids
          in: query
          description: >-
            Filter events by app UUID. Accepts up to 10 values. Org-level events
            are always included. Repeat the parameter for multiple values:
            `app_ids=uuid1&app_ids=uuid2`.
          style: form
          explode: true
          schema:
            type: array
            items:
              type: string
            maxItems: 10
        - name: actions
          in: query
          description: >-
            Filter by action type (e.g. `notification.sent`, `segment.created`).
            Accepts up to 20 values. Repeat the parameter for multiple values:
            `actions=notification.sent&actions=segment.created`.
          style: form
          explode: true
          schema:
            type: array
            items:
              type: string
            maxItems: 20
        - name: actor_ids
          in: query
          description: >-
            Filter by actor UUID (the user or service that performed the
            action). Accepts up to 10 values. Repeat the parameter for multiple
            values: `actor_ids=uuid1&actor_ids=uuid2`.
          style: form
          explode: true
          schema:
            type: array
            items:
              type: string
            maxItems: 10
        - name: actor_emails
          in: query
          description: >-
            Filter by actor email address. Accepts up to 10 values. Repeat the
            parameter for multiple values:
            `actor_emails=a@example.com&actor_emails=b@example.com`.
          style: form
          explode: true
          schema:
            type: array
            items:
              type: string
            maxItems: 10
        - name: target_types
          in: query
          description: >-
            Filter by the type of resource the action was performed on (e.g.
            `notification`, `segment`, `journey`). Accepts up to 10 values.
            Repeat the parameter for multiple values:
            `target_types=notification&target_types=segment`.
          style: form
          explode: true
          schema:
            type: array
            items:
              type: string
            maxItems: 10
        - name: target_ids
          in: query
          description: >-
            Filter by the UUID of the resource the action was performed on.
            Accepts up to 10 values. Repeat the parameter for multiple values:
            `target_ids=uuid1&target_ids=uuid2`.
          style: form
          explode: true
          schema:
            type: array
            items:
              type: string
            maxItems: 10
        - name: ip_addresses
          in: query
          description: >-
            Filter by the IP address the action originated from. Accepts up to
            10 values. Repeat the parameter for multiple values:
            `ip_addresses=203.0.113.1&ip_addresses=203.0.113.2`.
          style: form
          explode: true
          schema:
            type: array
            items:
              type: string
            maxItems: 10
      responses:
        '200':
          description: '200'
          content:
            application/json:
              schema:
                type: object
                properties:
                  audit_logs:
                    type: array
                    description: >-
                      Array of audit log events, ordered by `occurred_at`
                      ascending.
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          description: UUID of the audit log event.
                        organization_id:
                          type: string
                          description: UUID of the organization the event belongs to.
                        app_id:
                          type: string
                          description: >-
                            UUID of the app the event is associated with. Absent
                            for org-level events.
                        action:
                          type: string
                          description: >-
                            The action that was performed (e.g.
                            `notification.sent`, `segment.created`,
                            `member.invited`).
                        occurred_at:
                          type: string
                          description: >-
                            RFC 3339 timestamp of when the event occurred (e.g.
                            `2026-02-18T12:34:56Z`).
                        version:
                          type: integer
                          description: Schema version of the event payload.
                        actor:
                          type: object
                          description: >-
                            The user or service that performed the action.
                            Absent if the actor is unknown.
                          properties:
                            type:
                              type: string
                              description: Actor type (e.g. `user`, `service`).
                            id:
                              type: string
                              description: UUID of the actor.
                            name:
                              type: string
                              description: >-
                                Display name of the actor. Absent if
                                unavailable.
                            email:
                              type: string
                              description: >-
                                Email address of the actor. Absent if
                                unavailable.
                            metadata:
                              type: object
                              description: Additional actor-specific data.
                        targets:
                          type: array
                          description: >-
                            The resources the action was performed on. May be
                            empty for org-level events.
                          items:
                            type: object
                            properties:
                              type:
                                type: string
                                description: >-
                                  Resource type (e.g. `notification`, `segment`,
                                  `journey`, `app`).
                              id:
                                type: string
                                description: UUID of the resource.
                              name:
                                type: string
                                description: >-
                                  Display name of the resource. Absent if
                                  unavailable.
                              metadata:
                                type: object
                                description: Additional resource-specific data.
                        context:
                          type: object
                          description: >-
                            Request context at the time of the event. Absent if
                            context was not captured.
                          properties:
                            ip:
                              type: string
                              description: IP address the request originated from.
                            user_agent:
                              type: string
                              description: User agent of the client that made the request.
                            country:
                              type: string
                              description: Country code derived from the request IP.
                            metadata:
                              type: object
                              description: Additional context-specific data.
                        metadata:
                          type: object
                          description: >-
                            Additional event-specific data that does not fit
                            into the standard fields.
                  has_more:
                    type: boolean
                    description: >-
                      `true` if additional events exist beyond this page. Use
                      `next_cursor` to fetch the next page.
                  next_cursor:
                    type: string
                    description: >-
                      Opaque cursor to pass as `cursor` in the next request.
                      Only present when `has_more` is `true`.
              examples:
                Result:
                  value:
                    audit_logs:
                      - id: a1b2c3d4-0000-0000-0000-000000000001
                        organization_id: YOUR_ORG_ID
                        app_id: YOUR_APP_ID
                        action: segment.created
                        occurred_at: '2026-02-18T10:22:01Z'
                        version: 1
                        actor:
                          type: user
                          id: u1b2c3d4-0000-0000-0000-000000000001
                          name: Jane Smith
                          email: jane@example.com
                          metadata: {}
                        targets:
                          - type: segment
                            id: s1b2c3d4-0000-0000-0000-000000000001
                            name: High-value users
                            metadata: {}
                        context:
                          ip: 203.0.113.42
                          user_agent: Mozilla/5.0
                          country: US
                          metadata: {}
                        metadata: {}
                    has_more: true
                    next_cursor: eyJv...
        '400':
          description: '400'
          content:
            application/json:
              examples:
                Result:
                  value: '{}'
              schema:
                type: object
                properties: {}
        '403':
          description: '403'
          content:
            application/json:
              examples:
                Result:
                  value: '{}'
              schema:
                type: object
                properties: {}

````

Built with [Mintlify](https://mintlify.com).
