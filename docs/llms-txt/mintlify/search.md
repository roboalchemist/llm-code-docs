# Source: https://www.mintlify.com/docs/api/assistant/search.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Search documentation

> Perform semantic and keyword searches across your documentation with configurable filtering and pagination.



## OpenAPI

````yaml discovery-openapi.json post /v1/search/{domain}
openapi: 3.0.1
info:
  title: Mintlify Assistant API
  description: An API to integrate Mintlify discovery features into your product.
  version: 1.0.0
servers:
  - url: https://api.mintlify.com/discovery
security:
  - bearerAuth: []
paths:
  /v1/search/{domain}:
    post:
      summary: Search documentation
      description: >-
        Perform semantic and keyword searches across your documentation with
        configurable filtering and pagination.
      parameters:
        - name: domain
          in: path
          required: true
          schema:
            type: string
          description: >-
            The domain identifier from your `domain.mintlify.app` URL. Can be
            found at the end of your dashboard URL. For example,
            `dashboard.mintlify.com/organization/domain` has a domain identifier
            of `domain`.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - query
              properties:
                query:
                  type: string
                  description: >-
                    The search query to execute against your documentation
                    content.
                pageSize:
                  type: number
                  default: 10
                  description: >-
                    Number of search results to return. Defaults to 10 if not
                    specified.
                filter:
                  type: object
                  description: Optional filtering parameters to narrow search results.
                  properties:
                    version:
                      type: string
                      description: Filter results by documentation version.
                    language:
                      type: string
                      description: Filter results by content language.
      responses:
        '200':
          description: Search results
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    content:
                      type: string
                      description: The matching content from your documentation.
                    path:
                      type: string
                      description: The path or URL to the source document.
                    metadata:
                      type: object
                      description: Additional metadata about the search result.
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        The Authorization header expects a Bearer token. Use an assistant API
        key (prefixed with `mint_dsc_`). This is a public key safe for use in
        client-side code. Generate one on the [API keys
        page](https://dashboard.mintlify.com/settings/organization/api-keys) in
        your dashboard.

````