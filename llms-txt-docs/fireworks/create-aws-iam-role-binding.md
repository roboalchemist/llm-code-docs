# Source: https://docs.fireworks.ai/api-reference-dlde/create-aws-iam-role-binding.md

# Create Aws Iam Role Binding

## OpenAPI

````yaml post /v1/accounts/{account_id}/awsIamRoleBindings
paths:
  path: /v1/accounts/{account_id}/awsIamRoleBindings
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
                  - &ref_0
                    type: string
                    description: >-
                      The principal that is allowed to assume the AWS IAM role.
                      This must be

                      the email address of the user.
              role:
                allOf:
                  - &ref_1
                    type: string
                    description: >-
                      The AWS IAM role ARN that is allowed to be assumed by the
                      principal.
            required: true
            refIdentifier: '#/components/schemas/gatewayAwsIamRoleBinding'
            requiredProperties: &ref_2
              - principal
              - role
        examples:
          example:
            value:
              principal: <string>
              role: <string>
        description: The properties of the AWS IAM role binding being created.
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              accountId:
                allOf:
                  - type: string
                    description: The account ID that this binding is associated with.
                    readOnly: true
              createTime:
                allOf:
                  - type: string
                    format: date-time
                    description: The creation time of the AWS IAM role binding.
                    readOnly: true
              principal:
                allOf:
                  - *ref_0
              role:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/gatewayAwsIamRoleBinding'
            requiredProperties: *ref_2
        examples:
          example:
            value:
              accountId: <string>
              createTime: '2023-11-07T05:31:56Z'
              principal: <string>
              role: <string>
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas: {}

````