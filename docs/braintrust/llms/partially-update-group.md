# Source: https://braintrust.dev/docs/api-reference/groups/partially-update-group.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Partially update group

> Partially update a group object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.



## OpenAPI

````yaml openapi.yaml patch /v1/group/{group_id}
openapi: 3.1.1
info:
  version: 1.0.0
  title: Braintrust API
  description: >-
    API specification for the backend data server. The API is hosted globally at

    https://api.braintrust.dev or in your own environment.


    You can access the OpenAPI spec for this API at
    https://github.com/braintrustdata/braintrust-openapi.
  license:
    name: Apache 2.0
servers:
  - url: https://api.braintrust.dev
security:
  - bearerAuth: []
  - {}
paths:
  /v1/group/{group_id}:
    patch:
      tags:
        - Groups
      summary: Partially update group
      description: >-
        Partially update a group object. Specify the fields to update in the
        payload. Any object-type fields will be deep-merged with existing
        content. Currently we do not support removing fields or setting them to
        null.
      operationId: patchGroupId
      parameters:
        - $ref: '#/components/parameters/GroupIdParam'
      requestBody:
        description: Fields to update
        required: false
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PatchGroup'
      responses:
        '200':
          description: Returns the group object
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Group'
        '400':
          description: >-
            The request was unacceptable, often due to missing a required
            parameter
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '401':
          description: No valid API key provided
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '403':
          description: The API key doesn’t have permissions to perform the request
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '429':
          description: >-
            Too many requests hit the API too quickly. We recommend an
            exponential backoff of your requests
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '500':
          description: Something went wrong on Braintrust's end. (These are rare.)
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
      security:
        - bearerAuth: []
        - {}
components:
  parameters:
    GroupIdParam:
      schema:
        $ref: '#/components/schemas/GroupIdParam'
      required: true
      description: Group id
      name: group_id
      in: path
  schemas:
    PatchGroup:
      type: object
      properties:
        description:
          type: string
          nullable: true
          description: Textual description of the group
        name:
          type: string
          nullable: true
          minLength: 1
          description: Name of the group
        add_member_users:
          type: array
          nullable: true
          items:
            type: string
            format: uuid
          description: A list of user IDs to add to the group
        remove_member_users:
          type: array
          nullable: true
          items:
            type: string
            format: uuid
          description: A list of user IDs to remove from the group
        add_member_groups:
          type: array
          nullable: true
          items:
            type: string
            format: uuid
          description: A list of group IDs to add to the group's inheriting-from set
        remove_member_groups:
          type: array
          nullable: true
          items:
            type: string
            format: uuid
          description: A list of group IDs to remove from the group's inheriting-from set
    Group:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the group
        org_id:
          type: string
          format: uuid
          description: |-
            Unique id for the organization that the group belongs under

            It is forbidden to change the org after creating a group
        user_id:
          type: string
          nullable: true
          format: uuid
          description: Identifies the user who created the group
        created:
          type: string
          nullable: true
          format: date-time
          description: Date of group creation
        name:
          type: string
          description: Name of the group
        description:
          type: string
          nullable: true
          description: Textual description of the group
        deleted_at:
          type: string
          nullable: true
          format: date-time
          description: Date of group deletion, or null if the group is still active
        member_users:
          type: array
          nullable: true
          items:
            type: string
            format: uuid
          description: Ids of users which belong to this group
        member_groups:
          type: array
          nullable: true
          items:
            type: string
            format: uuid
          description: >-
            Ids of the groups this group inherits from


            An inheriting group has all the users contained in its member
            groups, as well as all of their inherited users
      required:
        - id
        - org_id
        - name
      description: >-
        A group is a collection of users which can be assigned an ACL


        Groups can consist of individual users, as well as a set of groups they
        inherit from
    GroupIdParam:
      type: string
      format: uuid
      description: Group id
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API key or JWT
      description: >-
        Most Braintrust endpoints are authenticated by providing your API key as
        a header `Authorization: Bearer [api_key]` to your HTTP request. You can
        create an API key in the Braintrust [organization settings
        page](https://www.braintrustdata.com/app/settings?subroute=api-keys).

````