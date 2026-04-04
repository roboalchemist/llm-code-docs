# Source: https://www.traceloop.com/docs/api-reference/metrics/get-metrics-with-filtering-and-grouping.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get metrics with filtering and grouping

> Retrieves metrics data with support for filtering, sorting, and pagination. Metrics are grouped by metric name with individual data points. Supports filtering by direct column fields (bool_value, trace_id, etc.), label fields (labels.agent_name, labels.trace_id), and attribute fields (attributes.*).



## OpenAPI

````yaml post /v2/metrics
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/metrics:
    post:
      tags:
        - metrics
      summary: Get metrics with filtering and grouping
      description: >-
        Retrieves metrics data with support for filtering, sorting, and
        pagination. Metrics are grouped by metric name with individual data
        points. Supports filtering by direct column fields (bool_value,
        trace_id, etc.), label fields (labels.agent_name, labels.trace_id), and
        attribute fields (attributes.*).
      operationId: get-metrics
      parameters:
        - description: Project ID
          in: path
          name: project_id
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/request.GetMetricsRequest'
        description: >-
          Metrics query parameters including filters, environments, and
          pagination
        required: true
      responses:
        '200':
          description: Grouped metrics with data points
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.GetMetricsResponse'
        '400':
          description: Invalid request parameters
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.ErrorResponse'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.ErrorResponse'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.ErrorResponse'
components:
  schemas:
    request.GetMetricsRequest:
      properties:
        cursor:
          type: integer
        environments:
          items:
            type: string
          type: array
        filters:
          items:
            $ref: '#/components/schemas/shared.FilterCondition'
          type: array
        from_timestamp_sec:
          type: integer
        limit:
          type: integer
        logical_operator:
          $ref: '#/components/schemas/evaluator.LogicalOperator'
        metric_name:
          type: string
        metric_source:
          type: string
        sort_by:
          type: string
        sort_order:
          type: string
        to_timestamp_sec:
          type: integer
      type: object
    response.GetMetricsResponse:
      properties:
        metrics:
          $ref: '#/components/schemas/response.PaginatedMetricsResponse'
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    shared.FilterCondition:
      properties:
        field:
          type: string
        operator:
          type: string
        value:
          type: string
        valueType:
          type: string
        values:
          items:
            type: string
          type: array
      type: object
    evaluator.LogicalOperator:
      enum:
        - AND
        - OR
      type: string
      x-enum-varnames:
        - LogicalOperatorAnd
        - LogicalOperatorOr
    response.PaginatedMetricsResponse:
      properties:
        data:
          items:
            $ref: '#/components/schemas/response.MetricGroup'
          type: array
        next_cursor:
          type: string
        total_points:
          type: integer
        total_results:
          type: integer
      type: object
    response.MetricGroup:
      properties:
        metric_name:
          type: string
        organization_id:
          type: string
        points:
          items:
            $ref: '#/components/schemas/response.MetricPoint'
          type: array
      type: object
    response.MetricPoint:
      properties:
        bool_value:
          type: boolean
        enum_value:
          type: string
        event_time:
          type: integer
        labels:
          additionalProperties:
            type: string
          type: object
        numeric_value:
          type: number
      type: object

````