# Source: https://docs.edenai.co/api-reference/universal-ai-info/list-subfeatures.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# List Subfeatures

> List all subfeatures for a specific feature.

Args:
    feature: Feature name (e.g., 'text', 'image', 'ocr', 'translation')

Returns:
    Dictionary with feature name and list of its subfeatures.



## OpenAPI

````yaml openapi/v3-openapi.json get /v3/info/{feature}
openapi: 3.1.0
info:
  title: Eden AI API V3
  version: 3.0.0
servers:
  - url: https://api.edenai.run
    description: Production server
security: []
paths:
  /v3/info/{feature}:
    get:
      tags:
        - Universal-ai-info
      summary: List Subfeatures
      description: |-
        List all subfeatures for a specific feature.

        Args:
            feature: Feature name (e.g., 'text', 'image', 'ocr', 'translation')

        Returns:
            Dictionary with feature name and list of its subfeatures.
      operationId: list_subfeatures_v3_info__feature__get
      parameters:
        - name: feature
          in: path
          required: true
          schema:
            type: string
            title: Feature
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: object
                additionalProperties: true
                title: Response List Subfeatures V3 Info  Feature  Get
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

Built with [Mintlify](https://mintlify.com).