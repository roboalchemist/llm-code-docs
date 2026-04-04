# Source: https://docs.venice.ai/api-reference/endpoint/image/edit.md

# Edit (aka Inpaint)

> Edit or modify an image based on the supplied prompt. The image can be provided either as a multipart form-data file upload or as a base64-encoded string in a JSON request.

## OpenAPI

````yaml POST /image/edit
paths:
  path: /image/edit
  method: post
  servers:
    - url: https://api.venice.ai/api/v1
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
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
              prompt:
                allOf:
                  - &ref_0
                    type: string
                    maxLength: 1500
                    description: >-
                      The text directions to edit or modify the image. Does best
                      with short but descriptive prompts. IE: "Change the color
                      of", "remove the object", "change the sky to a sunrise",
                      etc.
                    example: Change the color of the sky to a sunrise
              image:
                allOf:
                  - &ref_1
                    anyOf:
                      - {}
                      - type: string
                      - type: string
                        format: uri
                    description: >-
                      The image to edit. Can be either a file upload, a
                      base64-encoded string, or a URL starting with http:// or
                      https://. Image dimensions must be at least 65536 pixels
                      and must not exceed 33177600 pixels. Image URLs must be
                      less than 10MB.
            description: Edit an image based on the supplied prompt.
            refIdentifier: '#/components/schemas/EditImageRequest'
            requiredProperties: &ref_2
              - prompt
              - image
            additionalProperties: false
            example: &ref_3
              prompt: Colorize
              image: iVBORw0KGgoAAAANSUhEUgAAAgAAAAIACAIAAAB7GkOtAAAAIGNIUk0A...
        examples:
          example:
            value:
              prompt: Colorize
              image: iVBORw0KGgoAAAANSUhEUgAAAgAAAAIACAIAAAB7GkOtAAAAIGNIUk0A...
      multipart/form-data:
        schemaArray:
          - type: object
            properties:
              prompt:
                allOf:
                  - *ref_0
              image:
                allOf:
                  - *ref_1
            description: Edit an image based on the supplied prompt.
            refIdentifier: '#/components/schemas/EditImageRequest'
            requiredProperties: *ref_2
            additionalProperties: false
            example: *ref_3
        examples:
          example:
            value:
              prompt: Colorize
              image: iVBORw0KGgoAAAANSUhEUgAAAgAAAAIACAIAAAB7GkOtAAAAIGNIUk0A...
  response:
    '200':
      image/png:
        schemaArray:
          - type: file
            contentEncoding: binary
        examples:
          example: {}
        description: OK
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              details:
                allOf:
                  - type: object
                    properties: {}
                    description: Details about the incorrect input
                    example:
                      _errors: []
                      field:
                        _errors:
                          - Field is required
              error:
                allOf:
                  - type: string
                    description: A description of the error
            refIdentifier: '#/components/schemas/DetailedError'
            requiredProperties:
              - error
        examples:
          example:
            value:
              details:
                _errors: []
                field:
                  _errors:
                    - Field is required
              error: <string>
        description: Invalid request parameters
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_4
                    type: string
                    description: A description of the error
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: &ref_5
              - error
        examples:
          example:
            value:
              error: <string>
        description: Authentication failed
    '402':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_4
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_5
        examples:
          example:
            value:
              error: <string>
        description: Insufficient USD or Diem balance to complete request
    '415':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_4
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_5
        examples:
          example:
            value:
              error: <string>
        description: Invalid request content-type
    '429':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_4
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_5
        examples:
          example:
            value:
              error: <string>
        description: Rate limit exceeded
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_4
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_5
        examples:
          example:
            value:
              error: <string>
        description: Inference processing failed
    '503':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_4
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_5
        examples:
          example:
            value:
              error: <string>
        description: The model is at capacity. Please try again later.
  deprecated: false
  type: path
components:
  schemas: {}

````