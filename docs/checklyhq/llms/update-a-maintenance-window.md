# Source: https://checklyhq.com/docs/api-reference/maintenance-windows/update-a-maintenance-window.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a maintenance window

> Updates a maintenance window.



## OpenAPI

````yaml put /v1/maintenance-windows/{id}
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
  /v1/maintenance-windows/{id}:
    put:
      tags:
        - Maintenance windows
      summary: Update a maintenance window
      description: Updates a maintenance window.
      operationId: putV1MaintenancewindowsId
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
            type: integer
            x-constraint:
              sign: positive
          required: true
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/MaintenanceWindowCreate'
      responses:
        '200':
          description: Successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MaintenanceWindow'
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
    MaintenanceWindowCreate:
      type: object
      properties:
        name:
          type: string
          description: The maintenance window name.
          example: Maintenance Window
        tags:
          $ref: '#/components/schemas/MaintenanceWindowTagList'
        startsAt:
          type: string
          format: date
          description: The start date of the maintenance window.
          example: '2022-08-24'
        endsAt:
          type: string
          format: date
          description: The end date of the maintenance window.
          example: '2022-08-25'
        repeatInterval:
          type: number
          description: >-
            The repeat interval of the maintenance window from the first
            occurance.
          example: 'null'
          default: null
          nullable: true
          minimum: 1
        repeatUnit:
          type: string
          description: The repeat strategy for the maintenance window.
          example: DAY
        repeatEndsAt:
          type: string
          format: date
          description: The end date where the maintenance window should stop repeating.
          example: 'null'
          nullable: true
      required:
        - name
        - startsAt
        - endsAt
        - repeatUnit
    MaintenanceWindow:
      type: object
      properties:
        id:
          type: number
          description: The id of the maintenance window.
          example: 1
        name:
          type: string
          description: The maintenance window name.
          example: Maintenance Window
        tags:
          $ref: '#/components/schemas/MaintenanceWindowTagList'
        startsAt:
          type: string
          format: date
          description: The start date of the maintenance window.
          example: '2022-08-24'
        endsAt:
          type: string
          format: date
          description: The end date of the maintenance window.
          example: '2022-08-25'
        repeatInterval:
          type: number
          description: >-
            The repeat interval of the maintenance window from the first
            occurance.
          example: 'null'
          default: null
          nullable: true
          minimum: 1
        repeatUnit:
          type: string
          description: The repeat strategy for the maintenance window.
          example: DAY
        repeatEndsAt:
          type: string
          format: date
          description: The end date where the maintenance window should stop repeating.
          example: 'null'
          nullable: true
        created_at:
          type: string
          format: date
          description: The creation date of the maintenance window.
        updated_at:
          type: string
          format: date
          description: The last date that the maintenance window was updated.
          nullable: true
      required:
        - id
        - name
        - startsAt
        - endsAt
        - repeatUnit
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
    MaintenanceWindowTagList:
      type: array
      description: The names of the checks and groups maintenance window should apply to.
      example:
        - production
      items:
        type: string
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