# Source: https://docs.wandb.ai/weave/reference/service-api/calls/call-stats.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Call Stats



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /calls/stats
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /calls/stats:
    post:
      tags:
        - Calls
      summary: Call Stats
      operationId: call_stats_calls_stats_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CallStatsReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CallStatsRes'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - HTTPBasic: []
components:
  schemas:
    CallStatsReq:
      properties:
        project_id:
          type: string
          title: Project Id
        start:
          type: string
          format: date-time
          title: Start
          description: Inclusive start time (UTC, ISO 8601).
        end:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: End
          description: Exclusive end time (UTC, ISO 8601). Defaults to now if omitted.
        granularity:
          anyOf:
            - type: integer
            - type: 'null'
          title: Granularity
          description: >-
            Bucket size in seconds (e.g., 3600 for 1 hour). If omitted,
            auto-selected based on time range. Will be adjusted if it would
            produce more than 10,000 buckets.
        usage_metrics:
          anyOf:
            - items:
                $ref: '#/components/schemas/UsageMetricSpec'
              type: array
            - type: 'null'
          title: Usage Metrics
          description: >-
            Usage metrics (tokens, cost) to compute. Grouped by timestamp and
            model.
        call_metrics:
          anyOf:
            - items:
                $ref: '#/components/schemas/CallMetricSpec'
              type: array
            - type: 'null'
          title: Call Metrics
          description: >-
            Call-level metrics (latency, counts) to compute. Grouped by
            timestamp only.
        filter:
          anyOf:
            - $ref: '#/components/schemas/CallsFilter'
            - type: 'null'
        timezone:
          type: string
          title: Timezone
          description: IANA timezone for bucket alignment (e.g., 'America/New_York')
          default: UTC
      additionalProperties: false
      type: object
      required:
        - project_id
        - start
      title: CallStatsReq
      description: Request for aggregated call statistics over a time range.
    CallStatsRes:
      properties:
        start:
          type: string
          format: date-time
          title: Start
          description: Resolved start time (UTC)
        end:
          type: string
          format: date-time
          title: End
          description: Resolved end time (UTC)
        granularity:
          type: integer
          title: Granularity
          description: Bucket size used (in seconds)
        timezone:
          type: string
          title: Timezone
          description: Timezone used for bucket alignment
        usage_buckets:
          items:
            additionalProperties: true
            type: object
          type: array
          title: Usage Buckets
          description: >-
            Usage metrics by model. Each bucket contains 'timestamp', 'model',
            and aggregated metric values.
          default: []
        call_buckets:
          items:
            additionalProperties: true
            type: object
          type: array
          title: Call Buckets
          description: >-
            Call-level metrics. Each bucket contains 'timestamp' and aggregated
            metric values.
          default: []
      type: object
      required:
        - start
        - end
        - granularity
        - timezone
      title: CallStatsRes
      description: Response containing time-series call statistics.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    UsageMetricSpec:
      properties:
        metric:
          type: string
          enum:
            - input_tokens
            - output_tokens
            - total_tokens
            - input_cost
            - output_cost
            - total_cost
          title: Metric
          description: Metric to aggregate. Token metrics are normalized across providers.
        aggregations:
          items:
            $ref: '#/components/schemas/AggregationType'
          type: array
          title: Aggregations
          description: Basic aggregation functions to apply
          default:
            - sum
        percentiles:
          items:
            type: number
          type: array
          title: Percentiles
          description: >-
            Percentile values to compute (0-100). E.g., [50, 95, 99] for p50,
            p95, p99
          default: []
      additionalProperties: false
      type: object
      required:
        - metric
      title: UsageMetricSpec
      description: Specification for a usage metric to aggregate (grouped by model).
    CallMetricSpec:
      properties:
        metric:
          type: string
          enum:
            - latency_ms
            - call_count
            - error_count
          title: Metric
          description: Metric to aggregate.
        aggregations:
          items:
            $ref: '#/components/schemas/AggregationType'
          type: array
          title: Aggregations
          description: Basic aggregation functions to apply
          default:
            - sum
        percentiles:
          items:
            type: number
          type: array
          title: Percentiles
          description: >-
            Percentile values to compute (0-100). E.g., [50, 95, 99] for p50,
            p95, p99
          default: []
      additionalProperties: false
      type: object
      required:
        - metric
      title: CallMetricSpec
      description: >-
        Specification for a call-level metric to aggregate (not grouped by
        model).
    CallsFilter:
      properties:
        op_names:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Op Names
        input_refs:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Input Refs
        output_refs:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Output Refs
        parent_ids:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Parent Ids
        trace_ids:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Trace Ids
        call_ids:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Call Ids
        thread_ids:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Thread Ids
        turn_ids:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Turn Ids
        trace_roots_only:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Trace Roots Only
        wb_user_ids:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Wb User Ids
        wb_run_ids:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Wb Run Ids
      additionalProperties: false
      type: object
      title: CallsFilter
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
    AggregationType:
      type: string
      enum:
        - sum
        - avg
        - min
        - max
        - count
      title: AggregationType
      description: Basic aggregation functions for metrics.
  securitySchemes:
    HTTPBasic:
      type: http
      scheme: basic

````