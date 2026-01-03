# Source: https://braintrust.dev/docs/api-reference/roles/list-roles.md

# List roles

> List out all roles. The roles are sorted by creation date, with the most recently-created roles coming first



## OpenAPI

````yaml openapi.yaml get /v1/role
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
  /v1/role:
    get:
      tags:
        - Roles
      summary: List roles
      description: >-
        List out all roles. The roles are sorted by creation date, with the most
        recently-created roles coming first
      operationId: getRole
      parameters:
        - $ref: '#/components/parameters/AppLimitParam'
        - $ref: '#/components/parameters/StartingAfter'
        - $ref: '#/components/parameters/EndingBefore'
        - $ref: '#/components/parameters/Ids'
        - $ref: '#/components/parameters/RoleName'
        - $ref: '#/components/parameters/OrgName'
      responses:
        '200':
          description: Returns a list of role objects
          content:
            application/json:
              schema:
                type: object
                properties:
                  objects:
                    type: array
                    items:
                      $ref: '#/components/schemas/Role'
                    description: A list of role objects
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
    RoleName:
      schema:
        $ref: '#/components/schemas/RoleName'
      required: false
      description: Name of the role to search for
      name: role_name
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
    Role:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the role
        org_id:
          type: string
          nullable: true
          format: uuid
          description: >-
            Unique id for the organization that the role belongs under


            A null org_id indicates a system role, which may be assigned to
            anybody and inherited by any other role, but cannot be edited.


            It is forbidden to change the org after creating a role
        user_id:
          type: string
          nullable: true
          format: uuid
          description: Identifies the user who created the role
        created:
          type: string
          nullable: true
          format: date-time
          description: Date of role creation
        name:
          type: string
          description: Name of the role
        description:
          type: string
          nullable: true
          description: Textual description of the role
        deleted_at:
          type: string
          nullable: true
          format: date-time
          description: Date of role deletion, or null if the role is still active
        member_permissions:
          type: array
          nullable: true
          items:
            type: object
            properties:
              permission:
                $ref: '#/components/schemas/Permission'
              restrict_object_type:
                $ref: '#/components/schemas/AclObjectType'
                nullable: true
            required:
              - permission
          description: (permission, restrict_object_type) tuples which belong to this role
        member_roles:
          type: array
          nullable: true
          items:
            type: string
            format: uuid
          description: >-
            Ids of the roles this role inherits from


            An inheriting role has all the permissions contained in its member
            roles, as well as all of their inherited permissions
      required:
        - id
        - name
      description: >-
        A role is a collection of permissions which can be granted as part of an
        ACL


        Roles can consist of individual permissions, as well as a set of roles
        they inherit from
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
    RoleName:
      type: string
      description: Name of the role to search for
    OrgName:
      type: string
      description: Filter search results to within a particular organization
    Permission:
      type: string
      enum:
        - create
        - read
        - update
        - delete
        - create_acls
        - read_acls
        - update_acls
        - delete_acls
      description: >-
        Each permission permits a certain type of operation on an object in the
        system


        Permissions can be assigned to to objects on an individual basis, or
        grouped into roles
    AclObjectType:
      type: string
      enum:
        - organization
        - project
        - experiment
        - dataset
        - prompt
        - prompt_session
        - group
        - role
        - org_member
        - project_log
        - org_project
      description: The object type that the ACL applies to
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