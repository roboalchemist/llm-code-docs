# Source: https://developers.kit.com/api-reference/subscribers/list-stats-for-a-subscriber.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List stats for a subscriber

> Retrieve email stats for a specific subscriber. You can filter the stats by providing `email_sent_after` and/or `email_sent_before` query parameters to limit the stats to emails sent within a specific date range.
Note: this functionality was added in June 2025, so no data for events before that date will be included.



## OpenAPI

````yaml api-reference/v4.json get /v4/subscribers/{subscriber_id}/stats
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/subscribers/{subscriber_id}/stats:
    get:
      tags:
        - Subscribers
      summary: List stats for a subscriber
      description: >-
        Retrieve email stats for a specific subscriber. You can filter the stats
        by providing `email_sent_after` and/or `email_sent_before` query
        parameters to limit the stats to emails sent within a specific date
        range.

        Note: this functionality was added in June 2025, so no data for events
        before that date will be included.
      parameters:
        - name: email_sent_after
          description: >-
            Filter to stats for emails sent after this date (YYYY-MM-DD)/nNOTE:
            This functionality was added 2025-06-28 and will only include stats
            for emails sent before this date.
          in: query
          required: false
          schema:
            type: string
          example: '2025-07-01'
        - name: email_sent_before
          description: >-
            Filter to stats for emails sent before this date (YYYY-MM-DD)/nNote:
            this functionality was added in June 2025, so no data for events
            before that date will be included.
          in: query
          required: false
          schema:
            type: string
          example: '2025-08-31'
        - name: subscriber_id
          in: path
          required: true
          schema:
            type: integer
          example: 949
      responses:
        '200':
          description: Returns the stats for a subscriber
          content:
            application/json:
              schema:
                type: object
                properties:
                  subscriber:
                    type: object
                    properties:
                      id:
                        type: integer
                      stats:
                        type: object
                        properties:
                          sent:
                            type: integer
                          opened:
                            type: integer
                          clicked:
                            type: integer
                          bounced:
                            type: integer
                          open_rate:
                            type: number
                            format: float
                          click_rate:
                            type: number
                            format: float
                          last_sent:
                            type: string
                          last_opened:
                            type: string
                          last_clicked:
                            type: string
                          sends_since_last_open:
                            type: integer
                          sends_since_last_click:
                            type: integer
                        required:
                          - sent
                          - opened
                          - clicked
                          - bounced
                          - open_rate
                          - click_rate
                          - last_sent
                          - last_opened
                          - last_clicked
                          - sends_since_last_open
                          - sends_since_last_click
                    required:
                      - id
                      - stats
                required:
                  - subscriber
              example:
                subscriber:
                  id: 949
                  stats:
                    sent: 2
                    opened: 1
                    clicked: 1
                    bounced: 1
                    open_rate: 0.5
                    click_rate: 0.5
                    last_sent: '2025-07-14T00:00:00Z'
                    last_opened: '2025-07-13T12:00:00Z'
                    last_clicked: '2025-07-14T12:00:00Z'
                    sends_since_last_open: 1
                    sends_since_last_click: 0
        '401':
          description: Returns a 401 if the token and/or account cannot be authenticated
          content:
            application/json:
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
                required:
                  - errors
              example:
                errors:
                  - The access token is invalid
      security:
        - API Key: []
        - OAuth2: []
components:
  securitySchemes:
    API Key:
      description: Authenticate API requests via an API Key
      type: apiKey
      in: header
      name: X-Kit-Api-Key
    OAuth2:
      description: Authenticate API requests via an OAuth token
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: https://api.kit.com/v4/oauth/authorize
          tokenUrl: https://api.kit.com/v4/oauth/token
          refreshUrl: https://api.kit.com/v4/oauth/token
          scopes:
            read: Read access to Kit API v4
            write: Write access to Kit API v4

````

Built with [Mintlify](https://mintlify.com).