# Source: https://docs.helicone.ai/rest/trace/post-v1tracelog.md

# Log Trace

> Log a trace to the Helicone API

## OpenAPI

````yaml post /v1/trace/log
paths:
  path: /v1/trace/log
  method: post
  servers:
    - url: https://api.helicone.ai/
    - url: http://localhost:8585/
  request:
    security:
      - title: api key
        parameters:
          query: {}
          header:
            Authorization:
              type: apiKey
              description: 'Bearer token authentication. Format: ''Bearer YOUR_API_KEY'''
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
              resourceSpans:
                allOf:
                  - items:
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
            required: true
            refIdentifier: '#/components/schemas/OTELTrace'
            requiredProperties:
              - resourceSpans
        examples:
          example:
            value:
              resourceSpans:
                - scopeSpans:
                    - spans:
                        - droppedLinksCount: 123
                          links:
                            - <any>
                          status:
                            code: 123
                          droppedEventsCount: 123
                          events:
                            - <any>
                          droppedAttributesCount: 123
                          attributes:
                            - value:
                                intValue: 123
                                stringValue: <string>
                              key: <string>
                          endTimeUnixNano: <string>
                          startTimeUnixNano: <string>
                          kind: 123
                          name: <string>
                          spanId: <string>
                          traceId: <string>
                      scope:
                        version: <string>
                        name: <string>
                  resource:
                    droppedAttributesCount: 123
                    attributes:
                      - value:
                          arrayValue:
                            values:
                              - stringValue: <string>
                          intValue: 123
                          stringValue: <string>
                        key: <string>
  response:
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: No content
        examples: {}
        description: No content
  deprecated: false
  type: path
components:
  schemas: {}

````