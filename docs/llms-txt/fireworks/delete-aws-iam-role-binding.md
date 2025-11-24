# Source: https://docs.fireworks.ai/api-reference-dlde/delete-aws-iam-role-binding.md

# Delete Aws Iam Role Binding

## OpenAPI

````yaml post /v1/accounts/{account_id}/awsIamRoleBindings:delete
paths:
  path: /v1/accounts/{account_id}/awsIamRoleBindings:delete
  method: post
  servers:
    - url: https://api.fireworks.ai
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer authentication using your Fireworks API key. Format:
                Bearer <API_KEY>
          cookie: {}
    parameters:
      path:
        account_id:
          schema:
            - type: string
              required: true
              description: The Account Id
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              principal:
                allOf:
                  - type: string
                    description: >-
                      The principal that is allowed to assume the AWS IAM role.
                      This must be

                      the email address of the user.
              role:
                allOf:
                  - type: string
                    description: >-
                      The AWS IAM role ARN that is allowed to be assumed by the
                      principal.
            required: true
            title: |-
              The AWS IAM role binding being deleted.
              Must specify account_id, principal, and role.
        examples:
          example:
            value:
              principal: <string>
              role: <string>
        description: |-
          The AWS IAM role binding being deleted.
          Must specify account_id, principal, and role.
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties: {}
        examples:
          example:
            value: {}
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas: {}

````