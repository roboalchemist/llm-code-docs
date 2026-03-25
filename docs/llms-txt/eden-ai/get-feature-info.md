# Source: https://docs.edenai.co/api-reference/universal-ai-info/get-feature-info.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Feature Info

> Get detailed information for a specific feature/subfeature.

Args:
    feature: Feature name (e.g., 'text', 'image', 'ocr', 'translation')
    subfeature: Subfeature name (e.g., 'ai_detection', 'ocr', 'generation')
    format: Schema output format (simplified or json_schema)

Returns:
    - Input schema
    - Output schema
    - Available providers and their models



## OpenAPI

````yaml openapi/v3-openapi.json get /v3/info/{feature}/{subfeature}
openapi: 3.1.0
info:
  title: Eden AI API V3
  version: 3.0.0
servers:
  - url: https://api.edenai.run
    description: Production server
security: []
paths:
  /v3/info/{feature}/{subfeature}:
    get:
      tags:
        - Universal-ai-info
      summary: Get Feature Info
      description: |-
        Get detailed information for a specific feature/subfeature.

        Args:
            feature: Feature name (e.g., 'text', 'image', 'ocr', 'translation')
            subfeature: Subfeature name (e.g., 'ai_detection', 'ocr', 'generation')
            format: Schema output format (simplified or json_schema)

        Returns:
            - Input schema
            - Output schema
            - Available providers and their models
      operationId: get_feature_info_v3_info__feature___subfeature__get
      parameters:
        - name: feature
          in: path
          required: true
          schema:
            type: string
            title: Feature
        - name: subfeature
          in: path
          required: true
          schema:
            type: string
            title: Subfeature
        - name: format
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/SchemaFormat'
            description: >-
              Schema format: 'simplified' for flat readable format,
              'json_schema' for full Pydantic JSON Schema
            default: simplified
          description: >-
            Schema format: 'simplified' for flat readable format, 'json_schema'
            for full Pydantic JSON Schema
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: object
                additionalProperties: true
                title: Response Get Feature Info V3 Info  Feature   Subfeature  Get
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    SchemaFormat:
      type: string
      enum:
        - simplified
        - json_schema
      title: SchemaFormat
      description: Output format for schema information.
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

Built with [Mintlify](https://mintlify.com).