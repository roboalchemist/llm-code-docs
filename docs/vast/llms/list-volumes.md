# Source: https://docs.vast.ai/api-reference/volumes/list-volumes.md

> ## Documentation Index
>>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# list volumes

> Retrieve information about all volumes rented by you.

CLI Usage: `vastai show volumes`



## OpenAPI

````yaml api-reference/openapi.json get /api/v0/volumes/
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
  /api/v0/volumes/:
    get:
      tags:
        - Volumes
      summary: list volumes
      description: |-
        Retrieve information about all volumes rented by you.

        CLI Usage: `vastai show volumes`
      responses:
        '200':
          description: Success response
          content:
            application/json:
              schema:
                type: object
                properties:
                  volumes:
                    type: array
                    items:
                      $ref: '#/components/schemas/Volume'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                type: object
                properties:
                  detail:
                    type: string
                    example: Authentication credentials were not provided.
        '429':
          description: Too Many Requests
          content:
            application/json:
              schema:
                type: object
                properties:
                  detail:
                    type: string
                    example: API requests too frequent endpoint threshold=5.5
      security:
        - BearerAuth: []
components:
  schemas:
    Volume:
      type: object
      properties:
        instances:
          type: array
          description: List of instances using this volume
          items:
            type: object
        driver_version:
          type: string
          description: NVIDIA driver version
        cuda_max_good:
          type: number
          description: Maximum CUDA version supported
        machine_id:
          type: integer
          description: Unique identifier for the machine
        public_ipaddr:
          type: string
          description: Public IP address
        reliability2:
          type: number
          description: Reliability score of the host
        host_id:
          type: integer
          description: Unique identifier for the host
        cpu_name:
          type: string
          description: Name/model of the CPU
        mobo_name:
          type: string
          description: Name/model of the motherboard
        disk_space:
          type: number
          description: Disk space in GB
        disk_name:
          type: string
          description: Name/model of the disk
        inet_up:
          type: number
          description: Upload internet speed in Mbps
        inet_down:
          type: number
          description: Download internet speed in Mbps
        storage_total_cost:
          type: number
          description: Total cost for storage
        os_version:
          type: string
          description: Operating system version
        verification:
          type: string
          description: Verification status
        static_ip:
          type: boolean
          description: Whether the machine has a static IP
        cpu_arch:
          type: string
          description: CPU architecture
        start_date:
          type: number
          description: Start date as Unix timestamp
        id:
          type: integer
          description: Unique identifier for the volume
        status:
          type: string
          description: Current status of the volume
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````