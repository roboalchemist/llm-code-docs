# Source: https://docs.fireworks.ai/api-reference/get-dataset-download-endpoint.md

# Get Dataset Download Endpoint

## OpenAPI

````yaml get /v1/accounts/{account_id}/datasets/{dataset_id}:getDownloadEndpoint
paths:
  path: /v1/accounts/{account_id}/datasets/{dataset_id}:getDownloadEndpoint
  method: get
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
        dataset_id:
          schema:
            - type: string
              required: true
              description: The Dataset Id
      query:
        readMask:
          schema:
            - type: string
              required: false
              description: >-
                The fields to be returned in the response. If empty or "*", all
                fields will be returned.
        downloadLineage:
          schema:
            - type: boolean
              required: false
              description: |-
                If true, downloads entire lineage chain (all related datasets).
                Filenames will be prefixed with dataset IDs to avoid collisions.
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              filenameToSignedUrls:
                allOf:
                  - type: object
                    additionalProperties:
                      type: string
                    title: Signed URLs for downloading dataset files
            refIdentifier: '#/components/schemas/gatewayGetDatasetDownloadEndpointResponse'
        examples:
          example:
            value:
              filenameToSignedUrls: {}
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas: {}

````