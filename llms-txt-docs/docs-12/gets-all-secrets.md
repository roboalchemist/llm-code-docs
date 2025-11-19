# Source: https://docs.baseten.co/reference/management-api/secrets/gets-all-secrets.md

# Get all secrets

## OpenAPI

````yaml get /v1/secrets
paths:
  path: /v1/secrets
  method: get
  servers:
    - url: https://api.baseten.co
  request:
    security:
      - title: ApiKeyAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: apiKey
              description: >-
                You must specify the scheme 'Api-Key' in the Authorization
                header. For example, `Authorization: Api-Key <Your_Api_Key>`
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - lang: bash
        source: |
          curl --request GET \
          --url https://api.baseten.co/v1/secrets \
          --header "Authorization: Api-Key $BASETEN_API_KEY"
      - lang: python
        source: |-
          import requests
          import os
          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
          url = "https://api.baseten.co/v1/secrets"

          headers = {"Authorization": f"Api-Key {API_KEY}"}

          response = requests.request(
              "GET",
              url,
              headers=headers,
              json={}
          )

          print(response.text)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              secrets:
                allOf:
                  - items:
                      $ref: '#/components/schemas/SecretV1'
                    title: Secrets
                    type: array
            title: SecretsV1
            description: A list of Baseten secrets.
            refIdentifier: '#/components/schemas/SecretsV1'
            requiredProperties:
              - secrets
        examples:
          example:
            value:
              secrets:
                - created_at: '2023-11-07T05:31:56Z'
                  name: <string>
        description: A list of Baseten secrets.
  deprecated: false
  type: path
components:
  schemas:
    SecretV1:
      description: A Baseten secret. Note that we do not support retrieving secret values.
      properties:
        created_at:
          description: Time the secret was created in ISO 8601 format
          format: date-time
          title: Created At
          type: string
        name:
          description: Name of the secret
          title: Name
          type: string
      required:
        - created_at
        - name
      title: SecretV1
      type: object

````