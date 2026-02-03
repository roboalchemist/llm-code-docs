# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-regex-validator-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute regex-validator evaluator

> Validate text against a regex pattern

**Request Body:**
- `input.text` (string, required): The text to validate against a regex pattern
- `config.regex` (string, optional): The regex pattern to match against
- `config.should_match` (bool, optional): Whether the text should match the regex
- `config.case_sensitive` (bool, optional): Case-sensitive matching
- `config.dot_include_nl` (bool, optional): Dot matches newlines
- `config.multi_line` (bool, optional): Multi-line mode



## OpenAPI

````yaml post /v2/evaluators/execute/regex-validator
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/regex-validator:
    post:
      tags:
        - evaluators
      summary: Execute regex-validator evaluator
      description: >-
        Validate text against a regex pattern


        **Request Body:**

        - `input.text` (string, required): The text to validate against a regex
        pattern

        - `config.regex` (string, optional): The regex pattern to match against

        - `config.should_match` (bool, optional): Whether the text should match
        the regex

        - `config.case_sensitive` (bool, optional): Case-sensitive matching

        - `config.dot_include_nl` (bool, optional): Dot matches newlines

        - `config.multi_line` (bool, optional): Multi-line mode
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.RegexValidatorRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.RegexValidatorResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.ErrorResponse'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.ErrorResponse'
      security:
        - BearerAuth: []
components:
  schemas:
    request.RegexValidatorRequest:
      properties:
        config:
          $ref: '#/components/schemas/request.RegexValidatorConfigRequest'
        input:
          $ref: '#/components/schemas/request.RegexValidatorInput'
      required:
        - input
      type: object
    response.RegexValidatorResponse:
      properties:
        is_valid_regex:
          example: true
          type: boolean
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    request.RegexValidatorConfigRequest:
      properties:
        case_sensitive:
          example: true
          type: boolean
        dot_include_nl:
          example: true
          type: boolean
        multi_line:
          example: true
          type: boolean
        regex:
          example: .*
          type: string
        should_match:
          example: true
          type: boolean
      type: object
    request.RegexValidatorInput:
      properties:
        text:
          example: user@example.com
          type: string
      required:
        - text
      type: object
  securitySchemes:
    BearerAuth:
      description: Type "Bearer" followed by a space and JWT token.
      in: header
      name: Authorization
      type: apiKey

````