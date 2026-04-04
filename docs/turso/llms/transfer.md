# Source: https://docs.turso.tech/cli/group/transfer.md

# Source: https://docs.turso.tech/api-reference/groups/transfer.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Transfer Group

> Transfer a group to another organization that you own or a member of.

<Info>
  You can only transfer groups to organizations you own or are an admin.
</Info>

<Warning>
  Existing database URL and tokens will continue to work, but should update your application to use the new URL and token as soon as possible.
</Warning>

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X POST 'https://api.turso.tech/v1/organizations/{organizationSlug}/groups/{groupName}/transfer' \
  -H 'Authorization: Bearer TOKEN' \
  -d '{
      "organization": "new-organization-slug"
  }'
  ```
</RequestExample>


## OpenAPI

````yaml POST /v1/organizations/{organizationSlug}/groups/{groupName}/transfer
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
  /v1/organizations/{organizationSlug}/groups/{groupName}/transfer:
    post:
      summary: Transfer Group
      description: Transfer a group to another organization that you own or a member of.
      operationId: transferGroup
      parameters:
        - $ref: '#/components/parameters/organizationSlug'
        - $ref: '#/components/parameters/groupName'
      requestBody:
        description: Receiving Organization details.
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                organization:
                  type: string
                  description: The slug of the organization to transfer the group to.
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Group'
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