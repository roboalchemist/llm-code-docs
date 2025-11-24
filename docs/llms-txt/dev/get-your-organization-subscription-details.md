# Source: https://dev.writer.com/api-reference-legacy/billing/get-your-organization-subscription-details.md

# Get your organization subscription details

## OpenAPI

````yaml get /billing/subscription
paths:
  path: /billing/subscription
  method: get
  servers:
    - url: https://enterprise-api.writer.com
  request:
    security: []
    parameters:
      path: {}
      query: {}
      header:
        Authorization:
          schema:
            - type: string
              required: true
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              subscriptionId:
                allOf:
                  - type: string
              meta:
                allOf:
                  - $ref: '#/components/schemas/MetaData'
              createdAt:
                allOf:
                  - type: string
                    format: date-time
              seats:
                allOf:
                  - type: integer
              productName:
                allOf:
                  - type: string
                    enum:
                      - free
                      - pro
                      - team
                      - enterprise
                      - legacy
              status:
                allOf:
                  - type: string
                    enum:
                      - trialing
                      - active
                      - past_due
                      - incomplete
                      - incomplete_expired
                      - unpaid
                      - canceled
              usage:
                allOf:
                  - $ref: '#/components/schemas/Usage'
            refIdentifier: '#/components/schemas/SubscriptionPublicResponseApi'
            requiredProperties:
              - subscriptionId
              - meta
              - createdAt
              - seats
              - productName
              - status
              - usage
        examples:
          example:
            value:
              subscriptionId: <string>
              meta:
                teamCount: 123
                termsCount: 123
                snippetsCount: 123
                ssoAccess: true
                reporting: {}
                portal: {}
                styleguide: {}
                tier: enterprise-1
              createdAt: '2023-11-07T05:31:56Z'
              seats: 123
              productName: free
              status: trialing
              usage:
                team:
                  value: 123
                  limit: 123
                user:
                  value: 123
                  limit: 123
                words:
                  value: 123
                  limit: 123
                coWriteWords:
                  value: 123
                  limit: 123
        description: ''
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              tpe:
                allOf:
                  - &ref_0
                    type: string
              errors:
                allOf:
                  - &ref_1
                    type: array
                    items:
                      $ref: '#/components/schemas/FailMessage'
              extras:
                allOf:
                  - &ref_2
                    $ref: '#/components/schemas/Json'
            refIdentifier: '#/components/schemas/FailResponse'
            requiredProperties: &ref_3
              - tpe
              - extras
        examples:
          example:
            value:
              tpe: <string>
              errors:
                - description: <string>
                  key: <string>
                  extras: <any>
              extras: <any>
        description: Bad Request
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              tpe:
                allOf:
                  - *ref_0
              errors:
                allOf:
                  - *ref_1
              extras:
                allOf:
                  - *ref_2
            refIdentifier: '#/components/schemas/FailResponse'
            requiredProperties: *ref_3
        examples:
          example:
            value:
              tpe: <string>
              errors:
                - description: <string>
                  key: <string>
                  extras: <any>
              extras: <any>
        description: Unauthorized
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              tpe:
                allOf:
                  - *ref_0
              errors:
                allOf:
                  - *ref_1
              extras:
                allOf:
                  - *ref_2
            refIdentifier: '#/components/schemas/FailResponse'
            requiredProperties: *ref_3
        examples:
          example:
            value:
              tpe: <string>
              errors:
                - description: <string>
                  key: <string>
                  extras: <any>
              extras: <any>
        description: Forbidden
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              tpe:
                allOf:
                  - *ref_0
              errors:
                allOf:
                  - *ref_1
              extras:
                allOf:
                  - *ref_2
            refIdentifier: '#/components/schemas/FailResponse'
            requiredProperties: *ref_3
        examples:
          example:
            value:
              tpe: <string>
              errors:
                - description: <string>
                  key: <string>
                  extras: <any>
              extras: <any>
        description: Not Found
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              tpe:
                allOf:
                  - *ref_0
              errors:
                allOf:
                  - *ref_1
              extras:
                allOf:
                  - *ref_2
            refIdentifier: '#/components/schemas/FailResponse'
            requiredProperties: *ref_3
        examples:
          example:
            value:
              tpe: <string>
              errors:
                - description: <string>
                  key: <string>
                  extras: <any>
              extras: <any>
        description: Internal Server Error
  deprecated: false
  type: path
components:
  schemas:
    FailMessage:
      required:
        - description
        - key
        - extras
      type: object
      properties:
        description:
          type: string
        key:
          type: string
        extras:
          $ref: '#/components/schemas/Json'
    Json: {}
    MetaData:
      required:
        - teamCount
        - termsCount
        - snippetsCount
        - ssoAccess
        - reporting
        - portal
        - styleguide
      type: object
      properties:
        teamCount:
          type: integer
        termsCount:
          type: integer
        snippetsCount:
          type: integer
        ssoAccess:
          type: boolean
        reporting:
          $ref: '#/components/schemas/Map_V'
        portal:
          $ref: '#/components/schemas/Map_V'
        styleguide:
          $ref: '#/components/schemas/Map_V'
        tier:
          type: string
          enum:
            - enterprise-1
            - enterprise-2
            - enterprise-3
            - enterprise-4
    Usage:
      required:
        - team
        - user
        - words
        - coWriteWords
      type: object
      properties:
        team:
          $ref: '#/components/schemas/UsageItem'
        user:
          $ref: '#/components/schemas/UsageItem'
        words:
          $ref: '#/components/schemas/UsageItem'
        coWriteWords:
          $ref: '#/components/schemas/UsageItem'
    Map_V:
      type: object
      additionalProperties:
        type: string
    UsageItem:
      required:
        - value
        - limit
      type: object
      properties:
        value:
          type: integer
          format: int64
        limit:
          type: integer
          format: int64

````