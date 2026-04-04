# Source: https://docs.together.ai/reference/listhardware.md

# List Available Hardware Configurations

> Returns a list of available hardware configurations for deploying models. When a model parameter is provided, it returns only hardware configurations compatible with that model, including their current availability status.




## OpenAPI

````yaml GET /hardware
openapi: 3.1.0
info:
  title: Together APIs
  description: The Together REST API. Please see https://docs.together.ai for more details.
  version: 2.0.0
  termsOfService: https://www.together.ai/terms-of-service
  contact:
    name: Together Support
    url: https://www.together.ai/contact
  license:
    name: MIT
    url: https://github.com/togethercomputer/openapi/blob/main/LICENSE
servers:
  - url: https://api.together.xyz/v1
security:
  - bearerAuth: []
paths:
  /hardware:
    get:
      tags:
        - Hardware
      summary: List available hardware configurations
      description: >
        Returns a list of available hardware configurations for deploying
        models. When a model parameter is provided, it returns only hardware
        configurations compatible with that model, including their current
        availability status.
      operationId: listHardware
      parameters:
        - name: model
          in: query
          required: false
          schema:
            type: string
          description: >
            Filter hardware configurations by model compatibility. When
            provided, the response includes availability status for each
            compatible configuration.
          example: meta-llama/Llama-3-70b-chat-hf
      responses:
        '200':
          description: List of available hardware configurations
          content:
            application/json:
              schema:
                type: object
                required:
                  - object
                  - data
                properties:
                  object:
                    type: string
                    enum:
                      - list
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/HardwareWithStatus'
        '403':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '500':
          description: Internal error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
components:
  schemas:
    HardwareWithStatus:
      type: object
      description: Hardware configuration details with optional availability status
      required:
        - object
        - id
        - pricing
        - specs
        - updated_at
      properties:
        object:
          type: string
          enum:
            - hardware
        id:
          type: string
          description: Unique identifier for the hardware configuration
          examples:
            - 2x_nvidia_a100_80gb_sxm
        pricing:
          $ref: '#/components/schemas/EndpointPricing'
        specs:
          $ref: '#/components/schemas/HardwareSpec'
        availability:
          $ref: '#/components/schemas/HardwareAvailability'
        updated_at:
          type: string
          format: date-time
          description: Timestamp of when the hardware status was last updated
    ErrorData:
      type: object
      required:
        - error
      properties:
        error:
          type: object
          properties:
            message:
              type: string
              nullable: false
            type:
              type: string
              nullable: false
            param:
              type: string
              nullable: true
              default: null
            code:
              type: string
              nullable: true
              default: null
          required:
            - type
            - message
    EndpointPricing:
      type: object
      description: Pricing details for using an endpoint
      required:
        - cents_per_minute
      properties:
        cents_per_minute:
          type: number
          format: float
          description: Cost per minute of endpoint uptime in cents
          examples:
            - 5.42
    HardwareSpec:
      type: object
      description: Detailed specifications of a hardware configuration
      required:
        - gpu_type
        - gpu_link
        - gpu_memory
        - gpu_count
      properties:
        gpu_type:
          type: string
          description: The type/model of GPU
          examples:
            - a100-80gb
        gpu_link:
          type: string
          description: The GPU interconnect technology
          examples:
            - sxm
        gpu_memory:
          type: number
          format: float
          description: Amount of GPU memory in GB
          examples:
            - 80
        gpu_count:
          type: integer
          format: int32
          description: Number of GPUs in this configuration
          examples:
            - 2
    HardwareAvailability:
      type: object
      description: Indicates the current availability status of a hardware configuration
      required:
        - status
      properties:
        status:
          type: string
          description: The availability status of the hardware configuration
          enum:
            - available
            - unavailable
            - insufficient
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt