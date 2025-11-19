# Source: https://docs.baseten.co/reference/management-api/secrets/upserts-a-secret.md

# Upsert a secret

> Creates a new secret or updates an existing secret if one with the provided name already exists. The name and creation date of the created or updated secret is returned.

## OpenAPI

````yaml post /v1/secrets
paths:
  path: /v1/secrets
  method: post
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - description: Name of the new or existing secret
                    examples:
                      - my_secret
                    title: Name
                    type: string
              value:
                allOf:
                  - description: Value of the secret
                    examples:
                      - my_secret_value
                    title: Value
                    type: string
            required: true
            title: UpsertSecretRequestV1
            description: A request to create or update a Baseten secret by name.
            refIdentifier: '#/components/schemas/UpsertSecretRequestV1'
            requiredProperties:
              - name
              - value
        examples:
          example:
            value:
              name: my_secret
              value: my_secret_value
    codeSamples:
      - lang: bash
        source: |-
          curl --request POST \
          --url https://api.baseten.co/v1/secrets \
          --header "Authorization: Api-Key $BASETEN_API_KEY" \
          --data '{
            "name": "my_secret",
            "value": "my_secret_value"
          }'
      - lang: python
        source: |-
          import requests
          import os
          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
          url = "https://api.baseten.co/v1/secrets"

          headers = {"Authorization": f"Api-Key {API_KEY}"}

          response = requests.request(
              "POST",
              url,
              headers=headers,
              json={'name': 'my_secret', 'value': 'my_secret_value'}
          )

          print(response.text)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              created_at:
                allOf:
                  - description: Time the secret was created in ISO 8601 format
                    format: date-time
                    title: Created At
                    type: string
              name:
                allOf:
                  - description: Name of the secret
                    title: Name
                    type: string
            title: SecretV1
            description: >-
              A Baseten secret. Note that we do not support retrieving secret
              values.
            refIdentifier: '#/components/schemas/SecretV1'
            requiredProperties:
              - created_at
              - name
        examples:
          example:
            value:
              created_at: '2023-11-07T05:31:56Z'
              name: <string>
        description: >-
          A Baseten secret. Note that we do not support retrieving secret
          values.
  deprecated: false
  type: path
components:
  schemas: {}

````