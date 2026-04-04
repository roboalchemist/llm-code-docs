# Source: https://docs.turso.tech/cli/group/unarchive.md

# Source: https://docs.turso.tech/api-reference/groups/unarchive.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Unarchive Group

> Unarchive a group that has been archived due to inactivity.

<Info>
  Databases get archived after 10 days of inactivity for users on a free plan — [learn more](/features/scale-to-zero). You can unarchive inactive groups using the API.
</Info>

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X POST 'https://api.turso.tech/v1/organizations/{organizationSlug}/groups/{groupName}/unarchive' \
  -H 'Authorization: Bearer TOKEN' \
  ```
</RequestExample>


## OpenAPI

````yaml POST /v1/organizations/{organizationSlug}/groups/{groupName}/unarchive
openapi: 3.0.1
info:
  title: Turso Platform API
  description: API description here
  license:
    name: MIT
  version: 0.1.0
servers:
  - url: https://api.turso.tech
    description: Turso's Platform API
security: []
paths:
  /v1/organizations/{organizationSlug}/groups/{groupName}/unarchive:
    post:
      summary: Unarchive Group
      description: Unarchive a group that has been archived due to inactivity.
      operationId: unarchiveGroup
      parameters:
        - $ref: '#/components/parameters/organizationSlug'
        - $ref: '#/components/parameters/groupName'
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  group:
                    $ref: '#/components/schemas/Group'
                    description: The group that was unarchived
        '404':
          $ref: '#/components/responses/GroupNotFoundResponse'
components:
  parameters:
    organizationSlug:
      in: path
      name: organizationSlug
      required: true
      schema:
        type: string
      description: The slug of the organization or user account.
    groupName:
      name: groupName
      in: path
      required: true
      schema:
        type: string
      description: The name of the group.
  schemas:
    Group:
      allOf:
        - $ref: '#/components/schemas/BaseGroup'
        - type: object
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
  responses:
    GroupNotFoundResponse:
      description: Group not found
      content:
        application/json:
          schema:
            type: object
            properties:
              error:
                type: string
                description: The error message
                example: group not found

````