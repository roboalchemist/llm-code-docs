# Source: https://braintrust.dev/docs/api-reference/acls/list-acls.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List acls

> List out all acls. The acls are sorted by creation date, with the most recently-created acls coming first



## OpenAPI

````yaml openapi.yaml get /v1/acl
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
    get:
      tags:
        - Acls
      summary: List acls
      description: >-
        List out all acls. The acls are sorted by creation date, with the most
        recently-created acls coming first
      operationId: getAcl
      parameters:
        - $ref: '#/components/parameters/AppLimitParam'
        - $ref: '#/components/parameters/StartingAfter'
        - $ref: '#/components/parameters/EndingBefore'
        - $ref: '#/components/parameters/Ids'
        - $ref: '#/components/parameters/AclObjectType'
        - $ref: '#/components/parameters/AclObjectId'
        - $ref: '#/components/parameters/AclListUserId'
        - $ref: '#/components/parameters/AclListGroupId'
        - $ref: '#/components/parameters/AclListPermission'
        - $ref: '#/components/parameters/AclListRestrictObjectType'
        - $ref: '#/components/parameters/AclListRoleId'
      responses:
        '200':
          description: Returns a list of acl objects
          content:
            application/json:
              schema:
                type: object
                properties:
                  objects:
                    type: array
                    items:
                      $ref: '#/components/schemas/Acl'
                    description: A list of acl objects
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
    AclObjectType:
      schema:
        $ref: '#/components/schemas/AclObjectType'
      required: true
      description: The object type that the ACL applies to
      name: object_type
      in: query
    AclObjectId:
      schema:
        $ref: '#/components/schemas/AclObjectId'
      required: true
      description: The id of the object the ACL applies to
      name: object_id
      in: query
    AclListUserId:
      schema:
        $ref: '#/components/schemas/AclListUserId'
      required: false
      description: >-
        Id of the user the ACL applies to. Exactly one of `user_id` and
        `group_id` will be provided
      name: user_id
      in: query
    AclListGroupId:
      schema:
        $ref: '#/components/schemas/AclListGroupId'
      required: false
      description: >-
        Id of the group the ACL applies to. Exactly one of `user_id` and
        `group_id` will be provided
      name: group_id
      in: query
    AclListPermission:
      schema:
        $ref: '#/components/schemas/AclListPermission'
      required: false
      description: >-
        Each permission permits a certain type of operation on an object in the
        system


        Permissions can be assigned to to objects on an individual basis, or
        grouped into roles
      name: permission
      in: query
    AclListRestrictObjectType:
      schema:
        $ref: '#/components/schemas/AclListRestrictObjectType'
      required: false
      description: The object type that the ACL applies to
      name: restrict_object_type
      in: query
    AclListRoleId:
      schema:
        $ref: '#/components/schemas/AclListRoleId'
      required: false
      description: >-
        Id of the role the ACL grants. Exactly one of `permission` and `role_id`
        will be provided
      name: role_id
      in: query
  schemas:
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
    AclObjectId:
      type: string
      format: uuid
      description: The id of the object the ACL applies to
    AclListUserId:
      type: string
      format: uuid
      description: >-
        Id of the user the ACL applies to. Exactly one of `user_id` and
        `group_id` will be provided
    AclListGroupId:
      type: string
      format: uuid
      description: >-
        Id of the group the ACL applies to. Exactly one of `user_id` and
        `group_id` will be provided
    AclListPermission:
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
    AclListRestrictObjectType:
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
    AclListRoleId:
      type: string
      format: uuid
      description: >-
        Id of the role the ACL grants. Exactly one of `permission` and `role_id`
        will be provided
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