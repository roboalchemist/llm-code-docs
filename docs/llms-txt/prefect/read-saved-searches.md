# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/savedsearches/read-saved-searches.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Saved Searches

> Query for saved searches.



## OpenAPI

````yaml post /saved_searches/filter
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /saved_searches/filter:
    post:
      tags:
        - SavedSearches
      summary: Read Saved Searches
      description: Query for saved searches.
      operationId: read_saved_searches_saved_searches_filter_post
      parameters:
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_read_saved_searches_saved_searches_filter_post
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/SavedSearch'
                title: Response Read Saved Searches Saved Searches Filter Post
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_read_saved_searches_saved_searches_filter_post:
      properties:
        offset:
          type: integer
          minimum: 0
          title: Offset
          default: 0
        limit:
          type: integer
          title: Limit
          description: Defaults to PREFECT_API_DEFAULT_LIMIT if not provided.
      type: object
      title: Body_read_saved_searches_saved_searches_filter_post
    SavedSearch:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        created:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Created
        updated:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Updated
        name:
          type: string
          title: Name
          description: The name of the saved search.
        filters:
          items:
            $ref: '#/components/schemas/SavedSearchFilter'
          type: array
          title: Filters
          description: The filter set for the saved search.
      type: object
      required:
        - name
        - id
        - created
        - updated
      title: SavedSearch
      description: >-
        An ORM representation of saved search data. Represents a set of filter
        criteria.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    SavedSearchFilter:
      properties:
        object:
          type: string
          title: Object
          description: The object over which to filter.
        property:
          type: string
          title: Property
          description: The property of the object on which to filter.
        type:
          type: string
          title: Type
          description: The type of the property.
        operation:
          type: string
          title: Operation
          description: The operator to apply to the object. For example, `equals`.
        value:
          title: Value
          description: A JSON-compatible value for the filter.
      type: object
      required:
        - object
        - property
        - type
        - operation
        - value
      title: SavedSearchFilter
      description: A filter for a saved search model. Intended for use by the Prefect UI.
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
        input:
          title: Input
        ctx:
          type: object
          title: Context
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````

Built with [Mintlify](https://mintlify.com).