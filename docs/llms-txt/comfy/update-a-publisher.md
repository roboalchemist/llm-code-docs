# Source: https://docs.comfy.org/api-reference/registry/update-a-publisher.md

# Update a publisher

## OpenAPI

````yaml https://api.comfy.org/openapi put /publishers/{publisherId}
paths:
  path: /publishers/{publisherId}
  method: put
  servers:
    - url: https://api.comfy.org
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path:
        publisherId:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              createdAt:
                allOf:
                  - &ref_0
                    description: The date and time the publisher was created.
                    format: date-time
                    type: string
              description:
                allOf:
                  - &ref_1
                    type: string
              id:
                allOf:
                  - &ref_2
                    description: >-
                      The unique identifier for the publisher. It's akin to a
                      username. Should be lowercase.
                    type: string
              logo:
                allOf:
                  - &ref_3
                    description: URL to the publisher's logo.
                    type: string
              members:
                allOf:
                  - &ref_4
                    description: A list of members in the publisher.
                    items:
                      $ref: '#/components/schemas/PublisherMember'
                    type: array
              name:
                allOf:
                  - &ref_5
                    type: string
              source_code_repo:
                allOf:
                  - &ref_6
                    type: string
              status:
                allOf:
                  - &ref_7
                    $ref: '#/components/schemas/PublisherStatus'
              support:
                allOf:
                  - &ref_8
                    type: string
              website:
                allOf:
                  - &ref_9
                    type: string
            required: true
            refIdentifier: '#/components/schemas/Publisher'
        examples:
          example:
            value:
              createdAt: '2023-11-07T05:31:56Z'
              description: <string>
              id: <string>
              logo: <string>
              members:
                - id: <string>
                  role: <string>
                  user:
                    email: <string>
                    id: <string>
                    name: <string>
              name: <string>
              source_code_repo: <string>
              status: PublisherStatusActive
              support: <string>
              website: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              createdAt:
                allOf:
                  - *ref_0
              description:
                allOf:
                  - *ref_1
              id:
                allOf:
                  - *ref_2
              logo:
                allOf:
                  - *ref_3
              members:
                allOf:
                  - *ref_4
              name:
                allOf:
                  - *ref_5
              source_code_repo:
                allOf:
                  - *ref_6
              status:
                allOf:
                  - *ref_7
              support:
                allOf:
                  - *ref_8
              website:
                allOf:
                  - *ref_9
            refIdentifier: '#/components/schemas/Publisher'
        examples:
          example:
            value:
              createdAt: '2023-11-07T05:31:56Z'
              description: <string>
              id: <string>
              logo: <string>
              members:
                - id: <string>
                  role: <string>
                  user:
                    email: <string>
                    id: <string>
                    name: <string>
              name: <string>
              source_code_repo: <string>
              status: PublisherStatusActive
              support: <string>
              website: <string>
        description: Publisher updated successfully
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_10
                    type: string
              message:
                allOf:
                  - &ref_11
                    type: string
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: &ref_12
              - error
              - message
        examples:
          example:
            value:
              error: <string>
              message: <string>
        description: Bad request, invalid input data
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Unauthorized
        examples: {}
        description: Unauthorized
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_10
              message:
                allOf:
                  - *ref_11
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_12
        examples:
          example:
            value:
              error: <string>
              message: <string>
        description: Publisher not found
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_10
              message:
                allOf:
                  - *ref_11
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_12
        examples:
          example:
            value:
              error: <string>
              message: <string>
        description: Internal server error
  deprecated: false
  type: path
components:
  schemas:
    PublisherMember:
      properties:
        id:
          description: The unique identifier for the publisher member.
          type: string
        role:
          description: The role of the user in the publisher.
          type: string
        user:
          $ref: '#/components/schemas/PublisherUser'
      type: object
    PublisherStatus:
      enum:
        - PublisherStatusActive
        - PublisherStatusBanned
      type: string
    PublisherUser:
      properties:
        email:
          description: The email address for this user.
          type: string
        id:
          description: The unique id for this user.
          type: string
        name:
          description: The name for this user.
          type: string
      type: object

````