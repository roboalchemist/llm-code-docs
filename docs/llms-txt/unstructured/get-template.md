# Source: https://docs.unstructured.io/api-reference/templates/get-template.md

# Get Template

> Retrieve detailed information and DAG for a specific template.



## OpenAPI

````yaml https://platform.unstructuredapp.io/openapi.json get /api/v1/templates/{template_id}
openapi: 3.1.0
info:
  title: Platform API
  version: 3.0.5
servers:
  - url: https://platform.unstructuredapp.io/
    description: Unstructured Platform API
    x-speakeasy-server-id: platform-api
security: []
paths:
  /api/v1/templates/{template_id}:
    get:
      tags:
        - templates
      summary: Get Template
      description: Retrieve detailed information and DAG for a specific template.
      operationId: get_template
      parameters:
        - name: template_id
          in: path
          required: true
          schema:
            type: string
            title: Template Id
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
                $ref: '#/components/schemas/TemplateDetail'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    TemplateDetail:
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
        nodes:
          items:
            $ref: '#/components/schemas/TemplateNode'
          type: array
          title: Nodes
      type: object
      required:
        - id
        - name
        - version
        - last_updated
        - description
        - nodes
      title: TemplateDetail
      description: Full template details including nodes.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    TemplateNode:
      properties:
        id:
          type: string
          title: Id
        name:
          type: string
          title: Name
        type:
          type: string
          title: Type
        subtype:
          type: string
          title: Subtype
        settings:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Settings
      type: object
      required:
        - id
        - name
        - type
        - subtype
      title: TemplateNode
      description: A node in a template DAG.
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.unstructured.io/llms.txt