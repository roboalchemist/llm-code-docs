# Source: https://docs.agent.ai/api-reference/create-output/save-to-file.md

# Save To File

> Save text content as a downloadable file.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/create_file
paths:
  path: /action/create_file
  method: post
  servers:
    - url: https://api-lr.agent.ai/v1
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer token from your account
                ([https://agent.ai/user/integrations#api](https://agent.ai/user/integrations#api))
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              file_type:
                allOf:
                  - type: string
                    description: Enter the output file type (i.e. PDF).
                    enum:
                      - pdf
                      - docx
                      - html
                      - md
                      - odt
                      - tex
                      - azw3
                      - epub
                      - png
                    default: pdf
                    example: pdf
              body:
                allOf:
                  - type: string
                    description: >-
                      Provide the content to be saved in the file, including
                      text, bullet points, or other structured information.
                    example: >-
                      # Sample Document


                      This is a sample document content that will be saved to a
                      file.
              output_variable_name:
                allOf:
                  - type: string
                    description: Provide a variable name to store the file URL to.
                    pattern: ^[a-zA-Z0-9_]+$
                    example: saved_file
            required: true
            requiredProperties:
              - file_type
              - body
              - output_variable_name
        examples:
          example:
            value:
              file_type: pdf
              body: |-
                # Sample Document

                This is a sample document content that will be saved to a file.
              output_variable_name: saved_file
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    description: HTTP status code of the action response
              response:
                allOf:
                  - type: object
                    description: Response data from the action
            refIdentifier: '#/components/schemas/ActionResponse'
        examples:
          example:
            value:
              status: 200
              response:
                saved_file: https://s3.example.com/asset-uploads/document.pdf
        description: File saved successfully
    '400':
      application/json:
        schemaArray:
          - type: any
        examples:
          example:
            value: <any>
        description: Bad request
  deprecated: false
  type: path
components:
  schemas: {}

````