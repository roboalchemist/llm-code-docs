# Source: https://docs.datafold.com/api-reference/lineagev2/get-available-type-filters-for-search.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get available type filters for search

> Returns available type filters for narrowing search results (e.g., type:table, type:column).



## OpenAPI

````yaml openapi-public.json get /api/v1/lineagev2/search/types
openapi: 3.1.0
info:
  contact:
    email: support@datafold.com
    name: API Support
  description: >-
    The Datafold API reference is a guide to our available endpoints and
    authentication methods.

    If you're just getting started with Datafold, we recommend first checking
    out our [documentation](https://docs.datafold.com).


    :::info
      To use the Datafold API, you should first create a Datafold API Key,
      which should be stored as a local environment variable named DATAFOLD_API_KEY.
      This can be set in your Datafold Cloud's Settings under the Account page.
    :::
  title: Datafold API
  version: latest
servers:
  - description: Default server
    url: https://app.datafold.com
security:
  - ApiKeyAuth: []
paths:
  /api/v1/lineagev2/search/types:
    get:
      tags:
        - lineagev2
      summary: Get available type filters for search
      description: >-
        Returns available type filters for narrowing search results (e.g.,
        type:table, type:column).
      operationId: lineagev2_search_types
      parameters:
        - in: query
          name: prefix
          required: false
          schema:
            default: ''
            title: Prefix
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TypeSuggestionsResponse'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    TypeSuggestionsResponse:
      properties:
        types:
          items:
            $ref: '#/components/schemas/TypeSuggestion'
          title: Types
          type: array
      required:
        - types
      title: TypeSuggestionsResponse
      type: object
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          title: Detail
          type: array
      title: HTTPValidationError
      type: object
    TypeSuggestion:
      properties:
        description:
          title: Description
          type: string
        example:
          title: Example
          type: string
        type:
          title: Type
          type: string
      required:
        - type
        - description
        - example
      title: TypeSuggestion
      type: object
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          title: Location
          type: array
        msg:
          title: Message
          type: string
        type:
          title: Error Type
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
      type: object
  securitySchemes:
    ApiKeyAuth:
      description: Use the 'Authorization' header with the format 'Key <api-key>'
      in: header
      name: Authorization
      type: apiKey

````