# Source: https://docs.vast.ai/api-reference/serverless/get-endpoint-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# get endpoint logs

> Retrieves logs for a specific endpoint by name.

CLI Usage: `vastai get endpoint logs <endpoint_name> [--tail <num_lines>]`



## OpenAPI

````yaml api-reference/openapi.json post /get_endpoint_logs/
openapi: 3.1.0
info:
  title: Vast.ai API
  description: >-
    Welcome to Vast.ai 's API documentation. Our API allows you to
    programmatically manage GPU instances, handle machine operations, and
    automate your AI/ML workflow. Whether you're running individual GPU
    instances or managing a fleet of machines, our API provides comprehensive
    control over all Vast.ai  platform features.
  version: 1.0.0
  contact:
    name: Vast.ai Support
    url: https://discord.gg/vast
servers:
  - url: https://console.vast.ai
    description: Production server
security:
  - BearerAuth: []
paths:
  /get_endpoint_logs/:
    post:
      tags:
        - Serverless
      summary: get endpoint logs
      description: >-
        Retrieves logs for a specific endpoint by name.


        CLI Usage: `vastai get endpoint logs <endpoint_name> [--tail
        <num_lines>]`
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - endpoint
              properties:
                endpoint:
                  type: string
                  description: Name of the endpoint
                  example: vLLM-Qwen3-8B
                tail:
                  type: integer
                  description: Number of log lines to retrieve from the end
                  default: 10000
                  example: 1000
      responses:
        '200':
          description: Successfully retrieved endpoint logs.
          content:
            application/json:
              schema:
                oneOf:
                  - title: Success - Logs Retrieved
                    type: object
                    properties:
                      logs:
                        type: string
                        description: The endpoint logs
                        example: |-
                          2023-10-01 12:00:00 - Worker started
                          2023-10-01 12:01:00 - Request processed
                  - title: Error Response
                    type: string
                    description: >-
                      Error message when endpoint not found or authentication
                      fails
                    example: >-
                      authenticate_endpoint_apikey: invalid api_key or endpoint
                      vLLM-Qwen3-8B not found
      security:
        - BearerAuth: []
      servers:
        - url: https://run.vast.ai
          description: Production server
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````