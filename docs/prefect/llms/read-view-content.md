# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/collections/read-view-content.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read View Content

> Reads the content of a view from the prefect-collection-registry.



## OpenAPI

````yaml get /collections/views/{view}
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /collections/views/{view}:
    get:
      tags:
        - Collections
      summary: Read View Content
      description: Reads the content of a view from the prefect-collection-registry.
      operationId: read_view_content_collections_views__view__get
      parameters:
        - name: view
          in: path
          required: true
          schema:
            type: string
            title: View
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: object
                additionalProperties: true
                title: Response Read View Content Collections Views  View  Get
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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