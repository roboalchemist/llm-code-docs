# Source: https://checklyhq.com/docs/api-reference/incident-updates/create-an-incident-update.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create an incident update

> Creates a new update for an incident.



## OpenAPI

````yaml post /v1/incidents/{incidentId}/updates
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
  /v1/incidents/{incidentId}/updates:
    post:
      tags:
        - Incident Updates
      summary: Create an incident update
      description: Creates a new update for an incident.
      operationId: postV1IncidentsIncidentidUpdates
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
        - name: incidentId
          in: path
          schema:
            type: string
            x-format:
              guid: true
          required: true
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Model214'
      responses:
        '200':
          description: Successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/IncidentResults'
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
    Model214:
      type: object
      properties:
        status:
          $ref: '#/components/schemas/Model213'
        description:
          type: string
          description: A description about the status update.
          example: We found the issue and we are working on it.
      required:
        - status
        - description
    IncidentResults:
      type: array
      items:
        $ref: '#/components/schemas/Model217'
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
    Model213:
      type: string
      description: >-
        The incident update status. Must be one of
        INVESTIGATING,IDENTIFIED,MONITORING,RESOLVED,MAINTENANCE
      example: INVESTIGATING
      enum:
        - INVESTIGATING
        - IDENTIFIED
        - MONITORING
        - RESOLVED
        - MAINTENANCE
    Model217:
      type: object
      properties:
        status:
          $ref: '#/components/schemas/Model216'
        description:
          type: string
          description: A description about the status update.
          example: We found the issue and we are working on it.
        id:
          type: string
          description: The incident update universal and unique identificator.
          example: e50ad839-1b90-4955-b716-1c6edbda57cb
          x-format:
            guid: true
        created_at:
          type: string
          format: date
          description: The timestamp when the incident update was created.
          example: '2022-09-08T19:41:28.658Z'
        updated_at:
          type: string
          format: date
          description: The timestamp when last the update.
          example: '2022-09-08T20:41:28.658Z'
          nullable: true
      required:
        - status
        - description
        - id
        - created_at
        - updated_at
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
    Model216:
      type: string
      description: >-
        The incident update status. Must be one of
        INVESTIGATING,IDENTIFIED,MONITORING,RESOLVED,MAINTENANCE
      example: INVESTIGATING
      enum:
        - INVESTIGATING
        - IDENTIFIED
        - MONITORING
        - RESOLVED
        - MAINTENANCE
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