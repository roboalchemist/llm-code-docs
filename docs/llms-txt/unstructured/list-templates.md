# Source: https://docs.unstructured.io/api-reference/templates/list-templates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List Templates

> Retrieve a list of available templates with their metadata.



## OpenAPI

````yaml https://platform.unstructuredapp.io/openapi.json get /api/v1/templates/
openapi: 3.1.0
info:
  title: Platform API
  version: 3.1.0
servers:
  - url: https://platform.unstructuredapp.io/
    description: Unstructured Platform API
    x-speakeasy-server-id: platform-api
security: []
paths:
  /api/v1/templates/:
    get:
      tags:
        - templates
      summary: List Templates
      description: Retrieve a list of available templates with their metadata.
      operationId: list_templates
      parameters:
        - name: unstructured-api-key
          in: header
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            title: Unstructured-Api-Key
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/TemplateListItem'
                title: Response List Templates
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    TemplateListItem:
      properties:
        id:
          type: string
          title: Id
        name:
          type: string
          title: Name
        version:
          type: string
          title: Version
        last_updated:
          type: string
          title: Last Updated
        description:
          type: string
          title: Description
      type: object
      required:
        - id
        - name
        - version
        - last_updated
        - description
      title: TemplateListItem
      description: Template metadata for list responses.
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