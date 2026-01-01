# Source: https://braintrust.dev/docs/api-reference/groups/delete-group.md

# Delete group

> Delete a group object by its id



## OpenAPI

````yaml openapi.yaml delete /v1/group/{group_id}
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
    delete:
      tags:
        - Groups
      summary: Delete group
      description: Delete a group object by its id
      operationId: deleteGroupId
      parameters:
        - $ref: '#/components/parameters/GroupIdParam'
      responses:
        '200':
          description: Returns the deleted group object
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt