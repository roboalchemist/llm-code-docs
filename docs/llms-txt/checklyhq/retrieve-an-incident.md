# Source: https://checklyhq.com/docs/api-reference/incidents/retrieve-an-incident.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve an incident

> Shows details of a specific incident. Uses the "includeAllIncidentUpdates" query parameter to obtain all updates.



## OpenAPI

````yaml get /v1/incidents/{id}
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
    get:
      tags:
        - Incidents
      summary: Retrieve an incident
      description: >-
        Shows details of a specific incident. Uses the
        "includeAllIncidentUpdates" query parameter to obtain all updates.
      operationId: getV1IncidentsId
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
        - name: includeAllIncidentUpdates
          in: query
          schema:
            type: boolean
            description: You use it to include all the incident updates.
            example: true
            default: false
          description: You use it to include all the incident updates.
      responses:
        '200':
          description: Successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Model219'
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
    Model219:
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
          $ref: '#/components/schemas/Model218'
      required:
        - name
        - impact
        - dashboardId
        - id
        - created_at
        - updated_at
        - incidentUpdates
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
    Model218:
      type: array
      description: >-
        The first incident update with the status and description. It must be
        only one element.
      example:
        - id: 01f477f8-4293-4e1c-82bd-99797720434c
          status: RESOLVED
          description: The service is up and all is recovered.
          incidentId: 3abcfdfe-ae2d-4632-8dd1-18dd871e18fc
          created_at: '2022-09-08T20:56:48.425Z'
          updated_at: null
        - id: 1f0640f8-1910-4137-b91d-ed152faa92e6
          status: INVESTIGATING
          description: The service is down and affects all the regions.
          incidentId: 3abcfdfe-ae2d-4632-8dd1-18dd871e18fc
          created_at: '2022-09-08T18:56:48.425Z'
          updated_at: null
      minItems: 1
      items:
        $ref: '#/components/schemas/Model217'
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