# Source: https://www.traceloop.com/docs/api-reference/evaluators/execute-placeholder-regex-evaluator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute placeholder-regex evaluator

> Validate text against a placeholder regex pattern

**Request Body:**
- `input.placeholder_value` (string, required): The regex pattern to match against
- `input.text` (string, required): The text to validate against the regex pattern
- `config.should_match` (bool, optional): Whether the text should match the regex
- `config.case_sensitive` (bool, optional): Case-sensitive matching
- `config.dot_include_nl` (bool, optional): Dot matches newlines
- `config.multi_line` (bool, optional): Multi-line mode



## OpenAPI

````yaml post /v2/evaluators/execute/placeholder-regex
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/evaluators/execute/placeholder-regex:
    post:
      tags:
        - evaluators
      summary: Execute placeholder-regex evaluator
      description: >-
        Validate text against a placeholder regex pattern


        **Request Body:**

        - `input.placeholder_value` (string, required): The regex pattern to
        match against

        - `input.text` (string, required): The text to validate against the
        regex pattern

        - `config.should_match` (bool, optional): Whether the text should match
        the regex

        - `config.case_sensitive` (bool, optional): Case-sensitive matching

        - `config.dot_include_nl` (bool, optional): Dot matches newlines

        - `config.multi_line` (bool, optional): Multi-line mode
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.PlaceholderRegexRequest'
        description: Request body
        required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.PlaceholderRegexResponse'
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
    request.PlaceholderRegexRequest:
      properties:
        config:
          $ref: '#/components/schemas/request.PlaceholderRegexConfigRequest'
        input:
          $ref: '#/components/schemas/request.PlaceholderRegexInput'
      required:
        - input
      type: object
    response.PlaceholderRegexResponse:
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
    request.PlaceholderRegexConfigRequest:
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
        should_match:
          example: true
          type: boolean
      type: object
    request.PlaceholderRegexInput:
      properties:
        placeholder_value:
          example: '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
          type: string
        text:
          example: user@example.com
          type: string
      required:
        - placeholder_value
        - text
      type: object
  securitySchemes:
    BearerAuth:
      description: Type "Bearer" followed by a space and JWT token.
      in: header
      name: Authorization
      type: apiKey

````