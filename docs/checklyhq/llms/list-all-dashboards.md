# Source: https://checklyhq.com/docs/api-reference/dashboards/list-all-dashboards.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List all dashboards

> Lists all current dashboards in your account.



## OpenAPI

````yaml get /v1/dashboards
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
  /v1/dashboards:
    get:
      tags:
        - Dashboards
      summary: List all dashboards
      description: Lists all current dashboards in your account.
      operationId: getV1Dashboards
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
        - name: limit
          in: query
          schema:
            type: integer
            description: Limit the number of results
            default: 10
            minimum: 1
            maximum: 100
          description: Limit the number of results
        - name: page
          in: query
          schema:
            type: number
            description: Page number
            default: 1
            x-constraint:
              sign: positive
          description: Page number
      responses:
        '200':
          description: Successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DashboardsList'
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
        '429':
          description: Too Many Requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TooManyRequestsError'
components:
  schemas:
    DashboardsList:
      type: array
      items:
        $ref: '#/components/schemas/Dashboard'
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
    Dashboard:
      type: object
      properties:
        customDomain:
          type: string
          description: >-
            A custom user domain, e.g. "status.example.com". See the docs on
            updating your DNS and SSL usage.
          example: https://status.mycompany.com/
          nullable: true
        customUrl:
          type: string
          description: >-
            A subdomain name under "checklyhq.com". Needs to be unique across
            all users.
          example: status
        logo:
          type: string
          description: A URL pointing to an image file.
          example: https://static.mycompany.com/static/images/logo.svg
          nullable: true
          x-format:
            uri:
              scheme:
                - http
                - https
        favicon:
          type: string
          description: A URL pointing to an image file used as dashboard favicon.
          example: https://static.mycompany.com/static/images/icon.svg
          nullable: true
          x-format:
            uri:
              scheme:
                - http
                - https
        link:
          type: string
          description: A URL link to redirect when dashboard logo is clicked on.
          example: https://www.mycompany.com/
          nullable: true
          x-format:
            uri:
              scheme:
                - http
                - https
        description:
          type: string
          description: >-
            A piece of text displayed below the header or title of your
            dashboard.
          example: My dashboard description
          nullable: true
        width:
          $ref: '#/components/schemas/width'
        refreshRate:
          type: number
          description: How often to refresh the dashboard in seconds.
          default: 60
          enum:
            - 60
            - 300
            - 600
        paginate:
          type: boolean
          description: Determines of pagination is on or off.
          default: true
        paginationRate:
          type: number
          description: How often to trigger pagination in seconds.
          default: 60
          enum:
            - 30
            - 60
            - 300
        checksPerPage:
          type: number
          description: Number of checks displayed per page.
          default: 15
          nullable: true
          minimum: 1
          maximum: 20
        useTagsAndOperator:
          type: boolean
          description: When to use AND operator for tags lookup.
          default: false
          nullable: true
        hideTags:
          type: boolean
          description: Show or hide the tags on the dashboard.
          default: false
        enableIncidents:
          type: boolean
          description: Enable or disable incidents on the dashboard.
          default: false
        expandChecks:
          type: boolean
          description: Expand or collapse checks on the dashboard.
          default: false
        tags:
          $ref: '#/components/schemas/DashboardTagList'
        showHeader:
          type: boolean
          description: Show or hide header and description on the dashboard.
          default: true
        showCheckRunLinks:
          type: boolean
          description: Show or hide check run links on the dashboard.
          default: false
        showGroupNames:
          type: boolean
          description: Show or hide group names on the dashboard.
          default: true
        customCSS:
          type: string
          description: Custom CSS to be applied to the dashboard.
          default: ''
          nullable: true
        isPrivate:
          type: boolean
          description: Determines if the dashboard is public or private.
          default: false
        showP95:
          type: boolean
          description: Show or hide the P95 stats on the dashboard.
          default: true
        showP99:
          type: boolean
          description: Show or hide the P99 stats on the dashboard.
          default: true
        keys:
          $ref: '#/components/schemas/keys'
        id:
          type: number
        dashboardId:
          type: string
          example: '1'
        created_at:
          type: string
          format: date-time
        header:
          type: string
          nullable: true
      required:
        - id
        - dashboardId
        - created_at
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
    Model2:
      type: string
      enum:
        - Too Many Requests
    width:
      type: string
      description: Determines whether to use the full screen or focus in the center.
      default: FULL
      enum:
        - FULL
        - 960PX
    DashboardTagList:
      type: array
      description: >-
        A list of one or more tags that filter which checks to display on the
        dashboard.
      example:
        - production
      items:
        type: string
    keys:
      type: array
      description: Show key for private dashboard.
      items:
        $ref: '#/components/schemas/DashboardKey'
    DashboardKey:
      type: object
      properties:
        id:
          type: string
          x-format:
            guid: true
        rawKey:
          type: string
          example: da_a89026d28a0c45cf9e11b4c3637f3912
        maskedKey:
          type: string
          description: The masked key value.
          example: ...6a1e
        created_at:
          type: string
          format: date
        updated_at:
          type: string
          format: date
          nullable: true
      required:
        - id
        - rawKey
        - maskedKey
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