# Source: https://docs.frigade.com/api-reference/groups/groups-get.md

# Find a Group

> Find a group by ID

## OpenAPI

````yaml get /v1/groups
paths:
  path: /v1/groups
  method: get
  request:
    security:
      - title: bearer
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Authentication header of the form `Bearer: <token>`, where
                `<token>` is either your public or private API key. [See when to
                use which](/v2/api-reference/authorization)
          cookie: {}
    parameters:
      path: {}
      query:
        groupId:
          schema:
            - type: string
              required: true
              description: The ID of the group
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
                    description: The name of the group
                    example: Acme Inc.
              groupId:
                allOf:
                  - type: string
                    description: The ID of the group as defined in your own application
                    example: x34daa11-3745-4ac0-880e-d4b4d51fe13f
              createdAt:
                allOf:
                  - format: date-time
                    type: string
                    description: The date the group was created
                    example: '2021-01-01T00:00:00.000Z'
              modifiedAt:
                allOf:
                  - format: date-time
                    type: string
                    description: The date the group was last modified
                    example: '2021-01-01T00:00:00.000Z'
              properties:
                allOf:
                  - type: string
                    description: The properties of the group
                    example:
                      name: Acme Inc.
                      companyUrl: https://example.com
                      logoUrl: https://example.com/logo.jpg
              membersCount:
                allOf:
                  - type: number
                    description: The number of members in the group
                    example: 42
              trackingEvents:
                allOf:
                  - description: The tracking events associated with the group
                    example:
                      - event: SignedUp
                        properties:
                          source: landing-page
                          campaign: summer-sale
                        createdAt: '2024-01-01T00:00:00Z'
                    type: array
                    items:
                      type: string
            refIdentifier: '#/components/schemas/ExternalizedUserGroup'
        examples:
          example:
            value:
              name: Acme Inc.
              groupId: x34daa11-3745-4ac0-880e-d4b4d51fe13f
              createdAt: '2021-01-01T00:00:00.000Z'
              modifiedAt: '2021-01-01T00:00:00.000Z'
              properties:
                name: Acme Inc.
                companyUrl: https://example.com
                logoUrl: https://example.com/logo.jpg
              membersCount: 42
              trackingEvents:
                - event: SignedUp
                  properties:
                    source: landing-page
                    campaign: summer-sale
                  createdAt: '2024-01-01T00:00:00Z'
        description: The group was successfully found
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The group was not found
        examples: {}
        description: The group was not found
  deprecated: false
  type: path
components:
  schemas: {}

````