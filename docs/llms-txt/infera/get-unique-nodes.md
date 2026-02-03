# Source: https://docs.infera.org/api-reference/endpoint/get-unique-nodes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.infera.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Unique Nodes



## OpenAPI

````yaml get /unique_nodes
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers:
  - url: https://api.infera.org/
    description: Infera production servers
security: []
paths:
  /unique_nodes:
    get:
      summary: Get Unique Nodes
      operationId: get_unique_nodes_unique_nodes_get
      parameters:
        - name: model_name
          in: query
          required: true
          schema:
            type: string
            title: Model Name
        - name: start_date
          in: query
          required: false
          schema:
            anyOf:
              - type: string
                format: date-time
              - type: 'null'
            description: Start date for the range (ISO format)
            title: Start Date
          description: Start date for the range (ISO format)
        - name: end_date
          in: query
          required: false
          schema:
            anyOf:
              - type: string
                format: date-time
              - type: 'null'
            description: End date for the range (ISO format)
            title: End Date
          description: End date for the range (ISO format)
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
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
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````