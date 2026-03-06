# Source: https://docs.vast.ai/api-reference/network-volumes/add-network-disk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# add network-disk

> Adds a network disk to be used to create network volume offers, or adds machines to an existing network disk.

CLI Usage: `vastai add network_disk <machine_id>... <mount_point> [options]`



## OpenAPI

````yaml api-reference/openapi.json post /api/v0/network_disk/
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
  /api/v0/network_disk/:
    post:
      tags:
        - Network Volumes
      summary: add network-disk
      description: >-
        Adds a network disk to be used to create network volume offers, or adds
        machines to an existing network disk.


        CLI Usage: `vastai add network_disk <machine_id>... <mount_point>
        [options]`
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - mount_point
              properties:
                machine_id:
                  type: integer
                  description: ID of the machine to add network disk to
                machine_ids:
                  type: array
                  items:
                    type: integer
                  description: IDs of machines to add network disk to
                mount_point:
                  type: string
                  description: >-
                    Path to mount point of networked storage on machine or
                    machines
                disk_id:
                  type: integer
                  description: ID of network disk, if adding machines to existing disk
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  disk_id:
                    type: integer
                    description: ID of disk created or added to machines
                example:
                  success: true
                  disk_id: 2
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: invalid_args
                  msg:
                    type: string
                    example: Invalid machine id
        '403':
          description: Forbidden
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
                    example: Only machine owner can add network disk
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````