# Source: https://braintrust.dev/docs/api-reference/groups/list-groups.md

# List groups

> List out all groups. The groups are sorted by creation date, with the most recently-created groups coming first



## OpenAPI

````yaml openapi.yaml get /v1/group
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
  /v1/group:
    get:
      tags:
        - Groups
      summary: List groups
      description: >-
        List out all groups. The groups are sorted by creation date, with the
        most recently-created groups coming first
      operationId: getGroup
      parameters:
        - $ref: '#/components/parameters/AppLimitParam'
        - $ref: '#/components/parameters/StartingAfter'
        - $ref: '#/components/parameters/EndingBefore'
        - $ref: '#/components/parameters/Ids'
        - $ref: '#/components/parameters/GroupName'
        - $ref: '#/components/parameters/OrgName'
      responses:
        '200':
          description: Returns a list of group objects
          content:
            application/json:
              schema:
                type: object
                properties:
                  objects:
                    type: array
                    items:
                      $ref: '#/components/schemas/Group'
                    description: A list of group objects
                required:
                  - objects
                additionalProperties: false
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
    AppLimitParam:
      schema:
        $ref: '#/components/schemas/AppLimitParam'
      required: false
      description: Limit the number of objects to return
      name: limit
      in: query
    StartingAfter:
      schema:
        $ref: '#/components/schemas/StartingAfter'
      required: false
      description: >-
        Pagination cursor id.


        For example, if the final item in the last page you fetched had an id of
        `foo`, pass `starting_after=foo` to fetch the next page. Note: you may
        only pass one of `starting_after` and `ending_before`
      name: starting_after
      in: query
    EndingBefore:
      schema:
        $ref: '#/components/schemas/EndingBefore'
      required: false
      description: >-
        Pagination cursor id.


        For example, if the initial item in the last page you fetched had an id
        of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you
        may only pass one of `starting_after` and `ending_before`
      name: ending_before
      in: query
    Ids:
      schema:
        $ref: '#/components/schemas/Ids'
      required: false
      description: >-
        Filter search results to a particular set of object IDs. To specify a
        list of IDs, include the query param multiple times
      name: ids
      in: query
    GroupName:
      schema:
        $ref: '#/components/schemas/GroupName'
      required: false
      description: Name of the group to search for
      name: group_name
      in: query
      allowReserved: true
    OrgName:
      schema:
        $ref: '#/components/schemas/OrgName'
      required: false
      description: Filter search results to within a particular organization
      name: org_name
      in: query
      allowReserved: true
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
    AppLimitParam:
      type: integer
      nullable: true
      minimum: 0
      description: Limit the number of objects to return
    StartingAfter:
      type: string
      format: uuid
      description: >-
        Pagination cursor id.


        For example, if the final item in the last page you fetched had an id of
        `foo`, pass `starting_after=foo` to fetch the next page. Note: you may
        only pass one of `starting_after` and `ending_before`
    EndingBefore:
      type: string
      format: uuid
      description: >-
        Pagination cursor id.


        For example, if the initial item in the last page you fetched had an id
        of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you
        may only pass one of `starting_after` and `ending_before`
    Ids:
      anyOf:
        - type: string
          format: uuid
        - type: array
          items:
            type: string
            format: uuid
      description: >-
        Filter search results to a particular set of object IDs. To specify a
        list of IDs, include the query param multiple times
    GroupName:
      type: string
      description: Name of the group to search for
    OrgName:
      type: string
      description: Filter search results to within a particular organization
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