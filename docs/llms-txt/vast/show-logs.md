# Source: https://docs.vast.ai/api-reference/instances/show-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# show logs

> Request logs from a specific instance. The logs will be uploaded to S3 and can be retrieved from a generated URL. Supports both container logs and daemon system logs.

CLI Usage: `vastai show logs <instance_id> [--tail <lines>] [--filter <grep>] [--daemon-logs]`



## OpenAPI

````yaml api-reference/openapi.json put /api/v0/instances/request_logs/{id}
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
  /api/v0/instances/request_logs/{id}:
    put:
      tags:
        - Instances
      summary: show logs
      description: >-
        Request logs from a specific instance. The logs will be uploaded to S3
        and can be retrieved from a generated URL. Supports both container logs
        and daemon system logs.


        CLI Usage: `vastai show logs <instance_id> [--tail <lines>] [--filter
        <grep>] [--daemon-logs]`
      parameters:
        - name: id
          in: path
          required: true
          description: ID of the instance to get logs from
          schema:
            type: integer
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                tail:
                  type: string
                  description: Number of lines to show from end of logs
                  example: '1000'
                filter:
                  type: string
                  description: Grep filter to apply to log entries
                daemon_logs:
                  type: string
                  enum:
                    - 'true'
                  description: >-
                    If "true", fetch daemon system logs instead of container
                    logs
      responses:
        '200':
          description: Success response with S3 URL for log retrieval
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
                  result_url:
                    type: string
                    description: S3 URL where logs can be downloaded
                    example: https://s3.amazonaws.com/vast.ai/instance_logs/{hash}.log
                  msg:
                    type: string
                    description: Status message
        '403':
          description: Not authorized
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: not_authorized
                  msg:
                    type: string
                    example: Not authorized to view logs for this instance
        '404':
          description: Instance not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: invalid_id
                  msg:
                    type: string
                    example: Invalid instance id.
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````