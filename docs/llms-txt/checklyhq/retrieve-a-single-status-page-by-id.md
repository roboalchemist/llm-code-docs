# Source: https://checklyhq.com/docs/api-reference/status-pages/retrieve-a-single-status-page-by-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve a single status page by id.

> Get status page data, including cards and services.



## OpenAPI

````yaml get /v1/status-pages/{statusPageId}
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
  /v1/status-pages/{statusPageId}:
    get:
      tags:
        - Status Pages
      summary: Retrieve a single status page by id.
      description: Get status page data, including cards and services.
      operationId: getV1StatuspagesStatuspageid
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
        - name: statusPageId
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
                $ref: '#/components/schemas/StatusPageV2WithId'
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
    StatusPageV2WithId:
      type: object
      properties:
        name:
          type: string
        description:
          type: string
          nullable: true
          maxLength: 500
        url:
          type: string
          x-convert:
            case: lower
        customDomain:
          type: string
          description: >-
            A custom user domain, e.g. "status.example.com". See the docs on
            updating your DNS and SSL usage.
          nullable: true
          x-convert:
            case: lower
        themeColors:
          $ref: '#/components/schemas/StatusPageV2ThemeColors'
        logo:
          type: string
          nullable: true
          x-format:
            uri:
              scheme:
                - http
                - https
        redirectTo:
          type: string
          nullable: true
          x-format:
            uri:
              scheme:
                - http
                - https
        favicon:
          type: string
          nullable: true
          x-format:
            uri:
              scheme:
                - http
                - https
        defaultTheme:
          $ref: '#/components/schemas/defaultTheme'
        cards:
          $ref: '#/components/schemas/StatusPageV2Cards'
        id:
          type: string
          x-format:
            guid: true
        whiteLabel:
          type: boolean
        isPrivate:
          type: boolean
          default: false
      required:
        - name
        - url
        - id
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
    StatusPageV2ThemeColors:
      type: object
      nullable: true
      properties:
        light:
          $ref: '#/components/schemas/StatusPageThemeColors'
        dark:
          $ref: '#/components/schemas/StatusPageThemeColors'
      required:
        - light
        - dark
    defaultTheme:
      type: string
      default: AUTO
      enum:
        - LIGHT
        - DARK
        - AUTO
    StatusPageV2Cards:
      type: array
      items:
        $ref: '#/components/schemas/StatusPageV2Card'
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
    StatusPageThemeColors:
      type: object
      properties:
        bodyBackgroundColor:
          type: string
          pattern: ^#([0-9A-F]{3}|[0-9A-F]{6})$
        headerBackgroundColor:
          type: string
          pattern: ^#([0-9A-F]{3}|[0-9A-F]{6})$
        headerFontColor:
          type: string
          pattern: ^#([0-9A-F]{3}|[0-9A-F]{6})$
        titleFontColor:
          type: string
          pattern: ^#([0-9A-F]{3}|[0-9A-F]{6})$
        bodyFontColor:
          type: string
          pattern: ^#([0-9A-F]{3}|[0-9A-F]{6})$
        bodyFontColorMuted:
          type: string
          pattern: ^#([0-9A-F]{3}|[0-9A-F]{6})$
        navigationFontColor:
          type: string
          pattern: ^#([0-9A-F]{3}|[0-9A-F]{6})$
        linkFontColor:
          type: string
          pattern: ^#([0-9A-F]{3}|[0-9A-F]{6})$
        cardBackgroundColor:
          type: string
          pattern: ^#([0-9A-F]{3}|[0-9A-F]{6})$
        borderColor:
          type: string
          pattern: ^#([0-9A-F]{3}|[0-9A-F]{6})$
        primaryButtonBackgroundColor:
          type: string
          pattern: ^#([0-9A-F]{3}|[0-9A-F]{6})$
        primaryButtonFontColor:
          type: string
          pattern: ^#([0-9A-F]{3}|[0-9A-F]{6})$
      required:
        - bodyBackgroundColor
        - headerBackgroundColor
        - headerFontColor
        - titleFontColor
        - bodyFontColor
        - bodyFontColorMuted
        - navigationFontColor
        - linkFontColor
        - cardBackgroundColor
        - borderColor
        - primaryButtonBackgroundColor
        - primaryButtonFontColor
    StatusPageV2Card:
      type: object
      properties:
        id:
          type: string
          x-format:
            guid: true
        name:
          type: string
        services:
          $ref: '#/components/schemas/StatusPageV2CardServices'
        created_at:
          type: string
          format: date
        updated_at:
          type: string
          format: date
          nullable: true
      required:
        - id
        - name
        - created_at
    StatusPageV2CardServices:
      type: array
      items:
        $ref: '#/components/schemas/StatusPageV2Service'
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