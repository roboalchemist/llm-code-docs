# Source: https://www.traceloop.com/docs/api-reference/metrics/get-metrics-high-water-mark.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get metrics high water mark

> Returns the timestamp of the last successfully processed evaluation (high water mark)



## OpenAPI

````yaml get /v2/metrics_hwm
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/metrics_hwm:
    get:
      tags:
        - metrics
      summary: Get metrics high water mark
      description: >-
        Returns the timestamp of the last successfully processed evaluation
        (high water mark)
      operationId: get-metrics-hwm
      responses:
        '200':
          description: High water mark timestamp in milliseconds
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.MetricsHWMResponse'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.ErrorResponse'
components:
  schemas:
    response.MetricsHWMResponse:
      properties:
        high_water_mark:
          type: integer
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object

````