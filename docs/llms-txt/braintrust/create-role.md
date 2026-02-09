# Source: https://braintrust.dev/docs/api-reference/roles/create-role.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create role

> Create a new role. If there is an existing role with the same name as the one specified in the request, will return the existing role unmodified



## OpenAPI

````yaml openapi.yaml post /v1/role
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
    post:
      tags:
        - Roles
      summary: Create role
      description: >-
        Create a new role. If there is an existing role with the same name as
        the one specified in the request, will return the existing role
        unmodified
      operationId: postRole
      requestBody:
        description: Any desired information about the new role object
        required: false
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateRole'
      responses:
        '200':
          description: Returns the new role object
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Role'
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
  schemas:
    CreateRole:
      type: object
      properties:
        name:
          type: string
          minLength: 1
          description: Name of the role
        description:
          type: string
          nullable: true
          description: Textual description of the role
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
        org_name:
          type: string
          nullable: true
          description: >-
            For nearly all users, this parameter should be unnecessary. But in
            the rare case that your API key belongs to multiple organizations,
            you may specify the name of the organization the role belongs in.
      required:
        - name
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