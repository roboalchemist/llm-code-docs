# Source: https://checklyhq.com/docs/api-reference/status-page-incidents/retrieve-an-incident-by-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve an incident by id.

> Get incident details including incident history and affected services.



## OpenAPI

````yaml get /v1/status-pages/incidents/{incidentId}
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
  /v1/status-pages/incidents/{incidentId}:
    get:
      tags:
        - Status Page Incidents
      summary: Retrieve an incident by id.
      description: Get incident details including incident history and affected services.
      operationId: getV1StatuspagesIncidentsIncidentid
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
      responses:
        '200':
          description: Successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StatusPageV2Incident'
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
    StatusPageV2Incident:
      type: object
      properties:
        name:
          type: string
          maxLength: 255
        severity:
          $ref: '#/components/schemas/IncidentSeverity'
        id:
          type: string
          x-format:
            guid: true
        services:
          $ref: '#/components/schemas/IncidentServices'
        incidentUpdates:
          $ref: '#/components/schemas/IncidentUpdates'
        lastUpdateStatus:
          $ref: '#/components/schemas/StatusPageIncidentStatus'
        duration:
          type: integer
          nullable: true
        created_at:
          type: string
          format: date
        updated_at:
          type: string
          format: date
      required:
        - name
        - severity
        - id
        - services
        - incidentUpdates
        - lastUpdateStatus
        - created_at
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
    IncidentSeverity:
      type: string
      enum:
        - CRITICAL
        - MAJOR
        - MEDIUM
        - MINOR
    IncidentServices:
      type: array
      items:
        $ref: '#/components/schemas/StatusPageV2Service'
    IncidentUpdates:
      type: array
      items:
        $ref: '#/components/schemas/StatusPageV2IncidentUpdateWithId'
    StatusPageIncidentStatus:
      type: string
      enum:
        - INVESTIGATING
        - IDENTIFIED
        - MONITORING
        - RESOLVED
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
    StatusPageV2Service:
      type: object
      properties:
        name:
          type: string
        id:
          type: string
          x-format:
            guid: true
        accountId:
          type: string
          x-format:
            guid: true
        created_at:
          type: string
          format: date
        updated_at:
          type: string
          format: date
          nullable: true
      required:
        - name
        - id
        - accountId
        - created_at
    StatusPageV2IncidentUpdateWithId:
      type: object
      properties:
        description:
          type: string
        status:
          $ref: '#/components/schemas/StatusPageIncidentStatus'
        publicIncidentUpdateDate:
          type: string
          format: date-time
          default: '2026-03-25T20:35:10.907Z'
        notifySubscribers:
          type: boolean
          default: false
        id:
          type: string
          x-format:
            guid: true
        created_at:
          type: string
          format: date
      required:
        - description
        - id
        - created_at
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