# Source: https://docs.helicone.ai/rest/trace/post-v1tracelog.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Log Trace

> Log a trace to the Helicone API

<Warning>
  <strong>For users in the European Union:</strong> Please use `eu.api.helicone.ai` instead of
  `api.helicone.ai`.
</Warning>


## OpenAPI

````yaml post /v1/trace/log
openapi: 3.0.0
info:
  title: helicone-api
  version: 1.0.0
  license:
    name: MIT
  contact: {}
servers:
  - url: https://api.helicone.ai/
  - url: http://localhost:8585/
security: []
paths:
  /v1/trace/log:
    post:
      tags:
        - Trace
      operationId: LogTrace
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/OTELTrace'
      responses:
        '204':
          description: No content
      security:
        - api_key: []
components:
  schemas:
    OTELTrace:
      properties:
        resourceSpans:
          items:
            properties:
              scopeSpans:
                items:
                  properties:
                    spans:
                      items:
                        properties:
                          droppedLinksCount:
                            type: number
                            format: double
                          links:
                            items: {}
                            type: array
                          status:
                            properties:
                              code:
                                type: number
                                format: double
                            required:
                              - code
                            type: object
                          droppedEventsCount:
                            type: number
                            format: double
                          events:
                            items: {}
                            type: array
                          droppedAttributesCount:
                            type: number
                            format: double
                          attributes:
                            items:
                              properties:
                                value:
                                  properties:
                                    intValue:
                                      type: number
                                      format: double
                                    stringValue:
                                      type: string
                                  type: object
                                key:
                                  type: string
                              required:
                                - value
                                - key
                              type: object
                            type: array
                          endTimeUnixNano:
                            type: string
                          startTimeUnixNano:
                            type: string
                          kind:
                            type: number
                            format: double
                          name:
                            type: string
                          spanId:
                            type: string
                          traceId:
                            type: string
                        required:
                          - droppedLinksCount
                          - links
                          - status
                          - droppedEventsCount
                          - events
                          - droppedAttributesCount
                          - attributes
                          - endTimeUnixNano
                          - startTimeUnixNano
                          - kind
                          - name
                          - spanId
                          - traceId
                        type: object
                      type: array
                    scope:
                      properties:
                        version:
                          type: string
                        name:
                          type: string
                      required:
                        - version
                        - name
                      type: object
                  required:
                    - spans
                    - scope
                  type: object
                type: array
              resource:
                properties:
                  droppedAttributesCount:
                    type: number
                    format: double
                  attributes:
                    items:
                      properties:
                        value:
                          properties:
                            arrayValue:
                              properties:
                                values:
                                  items:
                                    properties:
                                      stringValue:
                                        type: string
                                    required:
                                      - stringValue
                                    type: object
                                  type: array
                              required:
                                - values
                              type: object
                            intValue:
                              type: number
                              format: double
                            stringValue:
                              type: string
                          type: object
                        key:
                          type: string
                      required:
                        - value
                        - key
                      type: object
                    type: array
                required:
                  - droppedAttributesCount
                  - attributes
                type: object
            required:
              - scopeSpans
              - resource
            type: object
          type: array
      required:
        - resourceSpans
      type: object
  securitySchemes:
    api_key:
      type: apiKey
      name: Authorization
      in: header
      description: 'Bearer token authentication. Format: ''Bearer YOUR_API_KEY'''

````