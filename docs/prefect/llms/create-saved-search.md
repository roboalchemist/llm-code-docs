# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/savedsearches/create-saved-search.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Saved Search

> Creates a new saved search from the provided schema.

If a saved search with the same name already exists, the saved search's fields are
replaced.



## OpenAPI

````yaml put /saved_searches/
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /saved_searches/:
    put:
      tags:
        - SavedSearches
      summary: Create Saved Search
      description: >-
        Creates a new saved search from the provided schema.


        If a saved search with the same name already exists, the saved search's
        fields are

        replaced.
      operationId: create_saved_search_saved_searches__put
      parameters:
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SavedSearchCreate'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SavedSearch'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    SavedSearchCreate:
      properties:
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
      additionalProperties: false
      type: object
      required:
        - name
      title: SavedSearchCreate
      description: Data used by the Prefect REST API to create a saved search.
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