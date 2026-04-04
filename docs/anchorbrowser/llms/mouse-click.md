# Source: https://docs.anchorbrowser.io/api-reference/os-level-control/mouse-click.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Mouse Click

> Performs a mouse click at the specified coordinates



## OpenAPI

````yaml openapi-mintlify.yaml post /v1/sessions/{sessionId}/mouse/click
openapi: 3.1.0
info:
  title: AnchorBrowser API
  version: 1.0.0
  description: APIs to manage all browser-related actions and configuration.
servers:
  - url: https://api.anchorbrowser.io
    description: API server
security: []
paths:
  /v1/sessions/{sessionId}/mouse/click:
    post:
      tags:
        - OS Level Control
      summary: Mouse Click
      description: Performs a mouse click at the specified coordinates
      parameters:
        - name: sessionId
          in: path
          required: true
          description: The ID of the browser session
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/MouseSingleClickRequestSchema'
      responses:
        '200':
          description: Click performed successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
        '400':
          description: Invalid coordinates or parameters
        '404':
          description: Session not found
        '500':
          description: Failed to perform click
      security:
        - api_key_header: []
components:
  schemas:
    MouseSingleClickRequestSchema:
      type: object
      description: >-
        Mouse click request. Must provide either (x, y) coordinates or a
        selector, but not both.
      properties:
        x:
          type: number
          description: X coordinate
        'y':
          type: number
          description: Y coordinate
        button:
          type: string
          description: Mouse button to use
          enum:
            - left
            - middle
            - right
        selector:
          type: string
          description: A valid CSS selector for the requested element
        timeout:
          type: number
          description: >-
            If a selector was passed, timeout in ms for waiting for the DOM
            element to be selected. Defaults to 5000 (5 seconds).
          x-stainless-naming:
            python:
              method_argument: selector_timeout_ms
            typescript:
              method_argument: selectorTimeoutMs
        index:
          type: number
          description: >-
            If a selector was passed and multiple elements match the selector,
            the index of the element in the list (0-based). Defaults to 0.
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````