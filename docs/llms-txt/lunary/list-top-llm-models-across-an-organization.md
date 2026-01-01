# Source: https://docs.lunary.ai/docs/api/analytics/list-top-llm-models-across-an-organization.md

# List top LLM models across an organization

> Returns the top models used across every project in the authenticated organization.
This endpoint requires an org-level private API key supplied as a bearer token in the `Authorization` header.




## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/analytics/org/models/top
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/analytics/org/models/top:
    get:
      tags:
        - Analytics
      summary: List top LLM models across an organization
      description: >
        Returns the top models used across every project in the authenticated
        organization.

        This endpoint requires an org-level private API key supplied as a bearer
        token in the `Authorization` header.
      parameters:
        - in: query
          name: startDate
          description: >-
            ISO8601 timestamp (inclusive) that bounds the analytics window.
            Requires `endDate` and `timeZone` when provided.
          schema:
            type: string
            format: date-time
        - in: query
          name: endDate
          description: >-
            ISO8601 timestamp (exclusive) that bounds the analytics window.
            Requires `startDate` and `timeZone` when provided.
          schema:
            type: string
            format: date-time
        - in: query
          name: timeZone
          description: IANA time zone identifier used to localize the date range filters.
          schema:
            type: string
      responses:
        '200':
          description: Top models across the organization.
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    name:
                      type: string
                      description: Model name.
                    promptTokens:
                      type: integer
                    completionTokens:
                      type: integer
                    totalTokens:
                      type: integer
                    cost:
                      type: number
                    projectName:
                      type: string
                      nullable: true
                      description: Project contributing the most traffic for the model.
        '401':
          description: >-
            Missing or invalid org API key supplied via the Authorization
            header.
      security:
        - OrgApiKeyAuth: []
components:
  securitySchemes:
    OrgApiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: UUID
      description: >-
        Use an org-level private API key issued by Lunary. Example Authorization
        header: `Bearer 123e4567-e89b-12d3-a456-426614174000`.

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt