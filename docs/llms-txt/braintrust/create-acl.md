# Source: https://braintrust.dev/docs/api-reference/acls/create-acl.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create acl

> Create a new acl. If there is an existing acl with the same contents as the one specified in the request, will return the existing acl unmodified



## OpenAPI

````yaml openapi.yaml post /v1/acl
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
  /v1/acl:
    post:
      tags:
        - Acls
      summary: Create acl
      description: >-
        Create a new acl. If there is an existing acl with the same contents as
        the one specified in the request, will return the existing acl
        unmodified
      operationId: postAcl
      requestBody:
        description: Any desired information about the new acl object
        required: false
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AclItem'
      responses:
        '200':
          description: Returns the new acl object
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Acl'
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
    AclItem:
      type: object
      properties:
        object_type:
          $ref: '#/components/schemas/AclObjectType'
        object_id:
          type: string
          format: uuid
          description: The id of the object the ACL applies to
        user_id:
          type: string
          nullable: true
          format: uuid
          description: >-
            Id of the user the ACL applies to. Exactly one of `user_id` and
            `group_id` will be provided
        group_id:
          type: string
          nullable: true
          format: uuid
          description: >-
            Id of the group the ACL applies to. Exactly one of `user_id` and
            `group_id` will be provided
        permission:
          $ref: '#/components/schemas/Permission'
          nullable: true
          description: >-
            Permission the ACL grants. Exactly one of `permission` and `role_id`
            will be provided
        restrict_object_type:
          $ref: '#/components/schemas/AclObjectType'
          nullable: true
          description: >-
            When setting a permission directly, optionally restricts the
            permission grant to just the specified object type. Cannot be set
            alongside a `role_id`.
        role_id:
          type: string
          nullable: true
          format: uuid
          description: >-
            Id of the role the ACL grants. Exactly one of `permission` and
            `role_id` will be provided
      required:
        - object_type
        - object_id
      description: >-
        An ACL grants a certain permission or role to a certain user or group on
        an object.


        ACLs are inherited across the object hierarchy. So for example, if a
        user has read permissions on a project, they will also have read
        permissions on any experiment, dataset, etc. created within that
        project.


        To restrict a grant to a particular sub-object, you may specify
        `restrict_object_type` in the ACL, as part of a direct permission grant
        or as part of a role.
    Acl:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the acl
        object_type:
          $ref: '#/components/schemas/AclObjectType'
        object_id:
          type: string
          format: uuid
          description: The id of the object the ACL applies to
        user_id:
          type: string
          nullable: true
          format: uuid
          description: >-
            Id of the user the ACL applies to. Exactly one of `user_id` and
            `group_id` will be provided
        group_id:
          type: string
          nullable: true
          format: uuid
          description: >-
            Id of the group the ACL applies to. Exactly one of `user_id` and
            `group_id` will be provided
        permission:
          $ref: '#/components/schemas/Permission'
          nullable: true
          description: >-
            Permission the ACL grants. Exactly one of `permission` and `role_id`
            will be provided
        restrict_object_type:
          $ref: '#/components/schemas/AclObjectType'
          nullable: true
          description: >-
            When setting a permission directly, optionally restricts the
            permission grant to just the specified object type. Cannot be set
            alongside a `role_id`.
        role_id:
          type: string
          nullable: true
          format: uuid
          description: >-
            Id of the role the ACL grants. Exactly one of `permission` and
            `role_id` will be provided
        _object_org_id:
          type: string
          format: uuid
          description: The organization the ACL's referred object belongs to
        created:
          type: string
          nullable: true
          format: date-time
          description: Date of acl creation
      required:
        - id
        - object_type
        - object_id
        - _object_org_id
      description: >-
        An ACL grants a certain permission or role to a certain user or group on
        an object.


        ACLs are inherited across the object hierarchy. So for example, if a
        user has read permissions on a project, they will also have read
        permissions on any experiment, dataset, etc. created within that
        project.


        To restrict a grant to a particular sub-object, you may specify
        `restrict_object_type` in the ACL, as part of a direct permission grant
        or as part of a role.
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