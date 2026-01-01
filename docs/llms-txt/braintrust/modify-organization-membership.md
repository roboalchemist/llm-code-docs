# Source: https://braintrust.dev/docs/api-reference/organizations/modify-organization-membership.md

# Modify organization membership

> Modify organization membership



## OpenAPI

````yaml openapi.yaml patch /v1/organization/members
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
  /v1/organization/members:
    patch:
      tags:
        - Organizations
      summary: Modify organization membership
      description: Modify organization membership
      operationId: patchOrganizationMembers
      requestBody:
        description: Members to add/remove
        required: false
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PatchOrganizationMembers'
      responses:
        '200':
          description: A success status
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PatchOrganizationMembersOutput'
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
    PatchOrganizationMembers:
      type: object
      properties:
        invite_users:
          type: object
          nullable: true
          properties:
            ids:
              type: array
              nullable: true
              items:
                type: string
                format: uuid
                description: Unique identifier for the user
              description: Ids of existing users to invite
            emails:
              type: array
              nullable: true
              items:
                type: string
              description: Emails of users to invite
            service_accounts:
              type: array
              nullable: true
              items:
                type: object
                properties:
                  name:
                    type: string
                  token_name:
                    type: string
                    nullable: true
                required:
                  - name
              description: Service accounts to create
            send_invite_emails:
              type: boolean
              nullable: true
              description: If true, send invite emails to the users who wore actually added
            group_ids:
              type: array
              nullable: true
              items:
                type: string
                format: uuid
                description: Unique identifier for the group
              description: Optional list of group ids to add newly-invited users to.
            group_names:
              type: array
              nullable: true
              items:
                type: string
                description: Name of the group
              description: Optional list of group names to add newly-invited users to.
            group_id:
              type: string
              nullable: true
              format: uuid
              description: Singular form of group_ids
            group_name:
              type: string
              nullable: true
              description: Singular form of group_names
          description: Users to invite to the organization
        remove_users:
          type: object
          nullable: true
          properties:
            ids:
              type: array
              nullable: true
              items:
                type: string
                format: uuid
                description: Unique identifier for the user
              description: Ids of users to remove
            emails:
              type: array
              nullable: true
              items:
                type: string
              description: Emails of users to remove
          description: Users to remove from the organization
        org_name:
          type: string
          nullable: true
          description: >-
            For nearly all users, this parameter should be unnecessary. But in
            the rare case that your API key belongs to multiple organizations,
            or in case you want to explicitly assert the organization you are
            modifying, you may specify the name of the organization.
        org_id:
          type: string
          nullable: true
          description: >-
            For nearly all users, this parameter should be unnecessary. But in
            the rare case that your API key belongs to multiple organizations,
            or in case you want to explicitly assert the organization you are
            modifying, you may specify the id of the organization.
    PatchOrganizationMembersOutput:
      type: object
      properties:
        status:
          type: string
          enum:
            - success
        org_id:
          type: string
          description: The id of the org that was modified.
        send_email_error:
          type: string
          nullable: true
          description: >-
            If invite emails failed to send for some reason, the patch operation
            will still complete, but we will return an error message here
        added_users:
          type: array
          nullable: true
          items:
            type: object
            properties:
              id:
                type: string
                format: uuid
              email:
                type: string
                nullable: true
              api_key:
                type: string
                nullable: true
              token_name:
                type: string
                nullable: true
            required:
              - id
          description: >-
            If service accounts with tokens were created, this will contain the
            added users with their API keys
      required:
        - status
        - org_id
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