# Source: https://docs.agent.ai/api-reference/use-ai/convert-text-to-speech.md

# Convert text to speech

> Convert text to a generated audio voice file.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/output_audio
paths:
  path: /action/output_audio
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
              text_to_speech:
                allOf:
                  - type: string
                    description: Text to convert to speech.
            required: true
            requiredProperties:
              - output_variable_name
        examples:
          example:
            value:
              text_to_speech: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - &ref_0
                    type: integer
                    format: int32
                    description: HTTP status code of the action response
              response:
                allOf:
                  - &ref_1
                    type: object
                    description: Response data from the action
            refIdentifier: '#/components/schemas/ActionResponse'
        examples:
          example:
            value:
              status: 200
              response: >-
                https://s3.us-east-2.amazonaws.com/asset-uploads.agent.ai/4oi2001mommncnj6.mp3
        description: Generated audio output
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - *ref_0
              response:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/ActionResponse'
        examples:
          example:
            value:
              status: 400
              error: Input text_to_speech is not provided.
              response: null
        description: Generated audio output
  deprecated: false
  type: path
components:
  schemas: {}

````