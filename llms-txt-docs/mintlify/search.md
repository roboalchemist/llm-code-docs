# Source: https://mintlify.com/docs/api/assistant/search.md

# Search documentation

> Perform semantic and keyword searches across your documentation with configurable filtering and pagination.

## OpenAPI

````yaml POST /search/{domain}
paths:
  path: /search/{domain}
  method: post
  servers:
    - url: https://api-dsc.mintlify.com/v1
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                The Authorization header expects a Bearer token. See the
                [Assistant API Key
                documentation](/docs/api-reference/introduction#assistant-api-key)
                for details on how to get your API key.
          cookie: {}
    parameters:
      path:
        domain:
          schema:
            - type: string
              required: true
              description: >-
                The domain identifier from your `domain.mintlify.app` URL. Can
                be found at the end of your dashboard URL. For example,
                `dashboard.mintlify.com/organization/domain` has a domain
                identifier of `domain`.
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              query:
                allOf:
                  - type: string
                    description: >-
                      The search query to execute against your documentation
                      content.
              pageSize:
                allOf:
                  - type: number
                    default: 10
                    description: >-
                      Number of search results to return. Defaults to 10 if not
                      specified.
              filter:
                allOf:
                  - type: object
                    description: Optional filtering parameters to narrow search results.
                    properties:
                      version:
                        type: string
                        description: Filter results by documentation version.
                      language:
                        type: string
                        description: Filter results by content language.
            required: true
            requiredProperties:
              - query
        examples:
          example:
            value:
              query: <string>
              pageSize: 10
              filter:
                version: <string>
                language: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - type: object
                  properties:
                    content:
                      type: string
                      description: The matching content from your documentation.
                    path:
                      type: string
                      description: The path or URL to the source document.
                    metadata:
                      type: object
                      description: >-
                        Additional metadata about the search result, including
                        relevance scoring and other contextual information.
        examples:
          example:
            value:
              - content: <string>
                path: <string>
                metadata: {}
        description: Search results
  deprecated: false
  type: path
components:
  schemas: {}

````