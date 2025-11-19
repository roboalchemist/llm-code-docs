# Source: https://docs.turso.tech/cli/group/transfer.md

# Source: https://docs.turso.tech/api-reference/groups/transfer.md

# Transfer Group

> Transfer a group to another organization that you own or a member of.

## OpenAPI

````yaml POST /v1/organizations/{organizationSlug}/groups/{groupName}/transfer
paths:
  path: /v1/organizations/{organizationSlug}/groups/{groupName}/transfer
  method: post
  servers:
    - url: https://api.turso.tech
      description: Turso's Platform API
  request:
    security: []
    parameters:
      path:
        organizationSlug:
          schema:
            - type: string
              required: true
              description: The slug of the organization or user account.
        groupName:
          schema:
            - type: string
              required: true
              description: The name of the group.
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              organization:
                allOf:
                  - type: string
                    description: The slug of the organization to transfer the group to.
            required: true
        examples:
          example:
            value:
              organization: <string>
        description: Receiving Organization details.
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
                    description: The group name, unique across your organization.
                    example: default
              version:
                allOf:
                  - type: string
                    description: >-
                      The current libSQL server version the databases in that
                      group are running.
                    example: v0.23.7
                    deprecated: true
              uuid:
                allOf:
                  - type: string
                    description: The group universal unique identifier (UUID).
                    example: 0a28102d-6906-11ee-8553-eaa7715aeaf2
              locations:
                allOf:
                  - type: array
                    items:
                      type: string
                    description: An array of location keys the group is located.
                    example:
                      - lhr
                      - ams
                      - bos
                    deprecated: true
              primary:
                allOf:
                  - type: string
                    description: The primary location key.
                    example: us-east-1
              delete_protection:
                allOf:
                  - type: boolean
                    description: >-
                      The current status for delete protection. If enabled, the
                      group and all its databases cannot be deleted.
                    example: false
            refIdentifier: '#/components/schemas/BaseGroup'
        examples:
          example:
            value:
              name: default
              version: v0.23.7
              uuid: 0a28102d-6906-11ee-8553-eaa7715aeaf2
              locations:
                - lhr
                - ams
                - bos
              primary: us-east-1
              delete_protection: false
        description: Successful response
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message
                    example: group not found
        examples:
          example:
            value:
              error: group not found
        description: Group not found
  deprecated: false
  type: path
components:
  schemas: {}

````