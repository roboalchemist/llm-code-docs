# Source: https://braintrust.dev/docs/api-reference/acls/batch-update-acls.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Batch update acls

> Batch update acls. This operation is idempotent, so adding acls which already exist will have no effect, and removing acls which do not exist will have no effect.



## OpenAPI

````yaml openapi.yaml post /v1/acl/batch_update
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
  /v1/acl/batch_update:
    post:
      tags:
        - Acls
      summary: Batch update acls
      description: >-
        Batch update acls. This operation is idempotent, so adding acls which
        already exist will have no effect, and removing acls which do not exist
        will have no effect.
      operationId: aclBatchUpdate
      requestBody:
        description: Acls to add/remove.
        required: false
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AclBatchUpdateRequest'
      responses:
        '200':
          description: A success status
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AclBatchUpdateResponse'
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
    AclBatchUpdateRequest:
      type: object
      properties:
        add_acls:
          type: array
          nullable: true
          items:
            $ref: '#/components/schemas/AclItem'
        remove_acls:
          type: array
          nullable: true
          items:
            $ref: '#/components/schemas/AclItem'
    AclBatchUpdateResponse:
      type: object
      properties:
        added_acls:
          type: array
          items:
            $ref: '#/components/schemas/Acl'
        removed_acls:
          type: array
          items:
            $ref: '#/components/schemas/Acl'
      required:
        - added_acls
        - removed_acls
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