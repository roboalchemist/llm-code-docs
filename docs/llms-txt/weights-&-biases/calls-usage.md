# Source: https://docs.wandb.ai/weave/reference/service-api/calls/calls-usage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Calls Usage

> Compute aggregated usage for multiple root calls, with descendant rollup.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /calls/usage
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /calls/usage:
    post:
      tags:
        - Calls
      summary: Calls Usage
      description: >-
        Compute aggregated usage for multiple root calls, with descendant
        rollup.
      operationId: calls_usage_calls_usage_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CallsUsageReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CallsUsageRes'
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
    CallsUsageReq:
      properties:
        project_id:
          type: string
          title: Project Id
        call_ids:
          items:
            type: string
          type: array
          title: Call Ids
          description: >-
            Root call IDs to aggregate. Each result key corresponds to one input
            call ID.
        include_costs:
          type: boolean
          title: Include Costs
          description: If true, include cost calculations in the usage.
          default: false
        limit:
          type: integer
          title: Limit
          description: >-
            Maximum number of calls to process across all traces. Acts as a
            safety limit to prevent unbounded memory usage.
          default: 10000
      additionalProperties: false
      type: object
      required:
        - project_id
        - call_ids
      title: CallsUsageReq
      description: >-
        Request to compute aggregated usage for multiple root calls.


        This endpoint returns usage metrics for each requested root call, where
        each

        root's metrics include the sum of its own usage plus all descendants'
        usage.


        Note: All matching calls are loaded into memory for aggregation. For
        very large

        result sets (>10k calls), consider batching root call IDs or using
        narrower

        filters at the application layer.
    CallsUsageRes:
      properties:
        call_usage:
          additionalProperties:
            additionalProperties:
              $ref: '#/components/schemas/LLMAggregatedUsage'
            type: object
          type: object
          title: Call Usage
      type: object
      title: CallsUsageRes
      description: Response with aggregated usage metrics per root call.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    LLMAggregatedUsage:
      properties:
        requests:
          type: integer
          title: Requests
          default: 0
        prompt_tokens:
          type: integer
          title: Prompt Tokens
          default: 0
        completion_tokens:
          type: integer
          title: Completion Tokens
          default: 0
        total_tokens:
          type: integer
          title: Total Tokens
          default: 0
        prompt_tokens_total_cost:
          anyOf:
            - type: number
            - type: 'null'
          title: Prompt Tokens Total Cost
        completion_tokens_total_cost:
          anyOf:
            - type: number
            - type: 'null'
          title: Completion Tokens Total Cost
      type: object
      title: LLMAggregatedUsage
      description: Aggregated usage metrics for a specific LLM.
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
  securitySchemes:
    HTTPBasic:
      type: http
      scheme: basic

````