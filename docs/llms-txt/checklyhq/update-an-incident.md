# Source: https://checklyhq.com/docs/api-reference/incidents/update-an-incident.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update an incident

> Updates an incident.



## OpenAPI

````yaml put /v1/incidents/{id}
openapi: 3.0.0
info:
  title: Checkly Public API
  version: v1
  description: >-
    These are the docs for the newly released Checkly Public API. If you have
    any questions, please do not hesitate to get in touch with us.
servers:
  - url: https://api.checklyhq.com
security:
  - Bearer: []
tags: []
paths:
  /v1/incidents/{id}:
    put:
      tags:
        - Incidents
      summary: Update an incident
      description: Updates an incident.
      operationId: putV1IncidentsId
      parameters:
        - name: x-checkly-account
          in: header
          schema:
            type: string
            description: >-
              Your Checkly account ID, you can find it at
              https://app.checklyhq.com/settings/account/general
            x-format:
              guid: true
          description: >-
            Your Checkly account ID, you can find it at
            https://app.checklyhq.com/settings/account/general
        - name: id
          in: path
          schema:
            type: string
            x-format:
              guid: true
          required: true
        - name: probe
          in: query
          schema:
            type: boolean
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Model220'
      responses:
        '200':
          description: Successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Model221'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UnauthorizedError'
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ForbiddenError'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NotFoundError'
        '429':
          description: Too Many Requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TooManyRequestsError'
components:
  schemas:
    Model220:
      type: object
      properties:
        name:
          type: string
          description: A name used to describe the incident.
          example: Service outage
        impact:
          $ref: '#/components/schemas/impact'
        startedAt:
          type: string
          format: date-time
          description: Used to indicate when incident starts to be active.
          example: '2022-11-25 12:34:56'
          nullable: true
        stoppedAt:
          type: string
          format: date-time
          description: Used to indicate when incident turns to inactive.
          example: '2022-11-25 13:34:56'
          nullable: true
      required:
        - name
        - impact
    Model221:
      type: object
      properties:
        name:
          type: string
          description: A name used to describe the incident.
          example: Service outage
        impact:
          $ref: '#/components/schemas/impact'
        startedAt:
          type: string
          format: date-time
          description: Used to indicate when incident starts to be active.
          example: '2022-11-25 12:34:56'
          nullable: true
        stoppedAt:
          type: string
          format: date-time
          description: Used to indicate when incident turns to inactive.
          example: '2022-11-25 13:34:56'
          nullable: true
        dashboardId:
          type: number
          description: The dashboard ID where the incident will be shown.
          example: 1234
        id:
          type: string
          description: The incident universal and unique identificator.
          example: e50ad839-1b90-4955-b716-1c6edbda57cb
          x-format:
            guid: true
        created_at:
          type: string
          format: date
          description: The timestamp when the incident was created.
          example: '2022-09-08T19:41:28.658Z'
        updated_at:
          type: string
          format: date
          description: The timestamp when last the incident update.
          example: '2022-09-08T20:41:28.658Z'
          nullable: true
        incidentUpdates:
          type: string
          nullable: true
      required:
        - name
        - impact
        - dashboardId
        - id
        - created_at
        - updated_at
    UnauthorizedError:
      type: object
      properties:
        statusCode:
          type: number
          enum:
            - 401
        error:
          $ref: '#/components/schemas/error'
        message:
          type: string
          example: Bad Token
        attributes:
          $ref: '#/components/schemas/attributes'
      required:
        - statusCode
        - error
    ForbiddenError:
      type: object
      properties:
        statusCode:
          type: number
          enum:
            - 403
        error:
          $ref: '#/components/schemas/Model1'
        message:
          type: string
          example: Forbidden
      required:
        - statusCode
        - error
    NotFoundError:
      type: object
      properties:
        statusCode:
          type: number
          enum:
            - 404
        error:
          $ref: '#/components/schemas/Model3'
        message:
          type: string
          example: Not Found
      required:
        - statusCode
        - error
    TooManyRequestsError:
      type: object
      properties:
        statusCode:
          type: number
          enum:
            - 429
        error:
          $ref: '#/components/schemas/Model2'
        message:
          type: string
          example: Too Many Requests
        attributes:
          $ref: '#/components/schemas/attributes'
      required:
        - statusCode
        - error
    impact:
      type: string
      description: Used to indicate the impact or severity.
      example: MINOR
      default: MINOR
      enum:
        - MAINTENANCE
        - MAJOR
        - MINOR
    error:
      type: string
      enum:
        - Unauthorized
    attributes:
      type: object
    Model1:
      type: string
      enum:
        - Forbidden
    Model3:
      type: string
      enum:
        - Not Found
    Model2:
      type: string
      enum:
        - Too Many Requests
  securitySchemes:
    Bearer:
      type: http
      scheme: bearer
      bearerFormat: Bearer
      description: >-
        The Checkly Public API uses API keys to authenticate requests. You can
        get the API Key
        [here](https://app.checklyhq.com/settings/user/api-keys). Your API key
        is like a password:  keep it secure!

        Authentication to the API is performed using the Bearer auth method in
        the Authorization header and using the account ID.

        For example, set **Authorization** header while using cURL: `curl -H
        "Authorization: Bearer [apiKey]" "X-Checkly-Account: [accountId]"` 

````

Built with [Mintlify](https://mintlify.com).