# Source: https://docs.ultravox.ai/api-reference/accounts/accounts-me-usage-calls-get.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ultravox.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Call Usage

> Returns aggregated and per-day call usage data



## OpenAPI

````yaml get /api/accounts/me/usage/calls
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/accounts/me/usage/calls:
    get:
      tags:
        - accounts
      description: Gets aggregated call usage.
      operationId: accounts_me_usage_calls_retrieve
      parameters:
        - in: query
          name: agentIds
          schema:
            type: array
            items:
              type: string
              format: uuid
          description: Filter calls by the agent IDs.
        - in: query
          name: durationMax
          schema:
            type: string
          description: Maximum duration of calls
        - in: query
          name: durationMin
          schema:
            type: string
          description: Minimum duration of calls
        - in: query
          name: fromDate
          schema:
            type: string
            format: date
          description: Start date (inclusive) for filtering calls by creation date
        - in: query
          name: metadata
          schema:
            type: object
            additionalProperties:
              type: string
          description: >-
            Filter calls by metadata. Use metadata.key=value to filter by
            specific key-value pairs.
        - in: query
          name: search
          schema:
            type: string
            minLength: 1
          description: The search string used to filter results
        - in: query
          name: toDate
          schema:
            type: string
            format: date
          description: End date (inclusive) for filtering calls by creation date
        - in: query
          name: voiceId
          schema:
            type: string
            format: uuid
          description: Filter calls by the associated voice ID
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CallUsage'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    CallUsage:
      type: object
      properties:
        allTime:
          allOf:
            - $ref: '#/components/schemas/CallStatistics'
          description: All-time call usage
        daily:
          type: array
          items:
            $ref: '#/components/schemas/DailyCallStatistics'
          description: Call usage per day
      required:
        - allTime
        - daily
    CallStatistics:
      type: object
      properties:
        totalCount:
          type: integer
          description: Total number of calls
        duration:
          type: string
          description: Total duration of all calls
        joinedCount:
          type: integer
          description: Number of calls that were joined
        billedMinutes:
          type: number
          format: double
          description: Total billed minutes.
      required:
        - billedMinutes
        - duration
        - joinedCount
        - totalCount
    DailyCallStatistics:
      type: object
      properties:
        totalCount:
          type: integer
          description: Total number of calls
        duration:
          type: string
          description: Total duration of all calls
        joinedCount:
          type: integer
          description: Number of calls that were joined
        billedMinutes:
          type: number
          format: double
          description: Total billed minutes.
        date:
          type: string
          format: date
          description: Date of usage
      required:
        - billedMinutes
        - date
        - duration
        - joinedCount
        - totalCount
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````