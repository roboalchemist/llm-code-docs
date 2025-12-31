# Source: https://docs.turso.tech/cli/group/unarchive.md

# Source: https://docs.turso.tech/api-reference/groups/unarchive.md

# Source: https://docs.turso.tech/cli/group/unarchive.md

# Source: https://docs.turso.tech/api-reference/groups/unarchive.md

# Source: https://docs.turso.tech/cli/group/unarchive.md

# Source: https://docs.turso.tech/api-reference/groups/unarchive.md

# Source: https://docs.turso.tech/cli/group/unarchive.md

# Source: https://docs.turso.tech/api-reference/groups/unarchive.md

# Unarchive Group

> Unarchive a group that has been archived due to inactivity.

## OpenAPI

````yaml POST /v1/organizations/{organizationSlug}/groups/{groupName}/unarchive
paths:
  path: /v1/organizations/{organizationSlug}/groups/{groupName}/unarchive
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
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              group:
                allOf:
                  - $ref: '#/components/schemas/Group'
                    description: The group that was unarchived
        examples:
          example:
            value:
              group:
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
  schemas:
    BaseGroup:
      type: object
      properties:
        name:
          type: string
          description: The group name, unique across your organization.
          example: default
        version:
          type: string
          description: >-
            The current libSQL server version the databases in that group are
            running.
          example: v0.23.7
          deprecated: true
        uuid:
          type: string
          description: The group universal unique identifier (UUID).
          example: 0a28102d-6906-11ee-8553-eaa7715aeaf2
        locations:
          type: array
          items:
            type: string
          description: An array of location keys the group is located.
          example:
            - lhr
            - ams
            - bos
          deprecated: true
        primary:
          type: string
          description: The primary location key.
          example: us-east-1
        delete_protection:
          type: boolean
          description: >-
            The current status for delete protection. If enabled, the group and
            all its databases cannot be deleted.
          example: false
    Group:
      allOf:
        - $ref: '#/components/schemas/BaseGroup'
        - type: object

````