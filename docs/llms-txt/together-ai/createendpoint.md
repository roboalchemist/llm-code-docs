# Source: https://docs.together.ai/reference/createendpoint.md

# Create A Dedicated Endpoint

> Creates a new dedicated endpoint for serving models. The endpoint will automatically start after creation. You can deploy any supported model on hardware configurations that meet the model's requirements.



## OpenAPI

````yaml POST /endpoints
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
  /endpoints:
    post:
      tags:
        - Endpoints
      summary: Create a dedicated endpoint, it will start automatically
      description: >-
        Creates a new dedicated endpoint for serving models. The endpoint will
        automatically start after creation. You can deploy any supported model
        on hardware configurations that meet the model's requirements.
      operationId: createEndpoint
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateEndpointRequest'
      responses:
        '200':
          description: '200'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DedicatedEndpoint'
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
    CreateEndpointRequest:
      type: object
      required:
        - model
        - hardware
        - autoscaling
      properties:
        display_name:
          type: string
          description: A human-readable name for the endpoint
          examples:
            - My Llama3 70b endpoint
        model:
          type: string
          description: The model to deploy on this endpoint
          examples:
            - meta-llama/Llama-3-8b-chat-hf
        hardware:
          type: string
          description: The hardware configuration to use for this endpoint
          examples:
            - 1x_nvidia_a100_80gb_sxm
        autoscaling:
          $ref: '#/components/schemas/Autoscaling'
          description: Configuration for automatic scaling of the endpoint
        disable_prompt_cache:
          type: boolean
          description: Whether to disable the prompt cache for this endpoint
          default: false
        disable_speculative_decoding:
          type: boolean
          description: Whether to disable speculative decoding for this endpoint
          default: false
        state:
          type: string
          description: The desired state of the endpoint
          enum:
            - STARTED
            - STOPPED
          default: STARTED
          example: STARTED
        inactive_timeout:
          type: integer
          description: >-
            The number of minutes of inactivity after which the endpoint will be
            automatically stopped. Set to null, omit or set to 0 to disable
            automatic timeout.
          nullable: true
          example: 60
        availability_zone:
          type: string
          description: >-
            Create the endpoint in a specified availability zone (e.g.,
            us-central-4b)
    DedicatedEndpoint:
      type: object
      description: Details about a dedicated endpoint deployment
      required:
        - object
        - id
        - name
        - display_name
        - model
        - hardware
        - type
        - owner
        - state
        - autoscaling
        - created_at
      properties:
        object:
          type: string
          enum:
            - endpoint
          description: The type of object
          example: endpoint
        id:
          type: string
          description: Unique identifier for the endpoint
          example: endpoint-d23901de-ef8f-44bf-b3e7-de9c1ca8f2d7
        name:
          type: string
          description: System name for the endpoint
          example: devuser/meta-llama/Llama-3-8b-chat-hf-a32b82a1
        display_name:
          type: string
          description: Human-readable name for the endpoint
          example: My Llama3 70b endpoint
        model:
          type: string
          description: The model deployed on this endpoint
          example: meta-llama/Llama-3-8b-chat-hf
        hardware:
          type: string
          description: The hardware configuration used for this endpoint
          example: 1x_nvidia_a100_80gb_sxm
        type:
          type: string
          enum:
            - dedicated
          description: The type of endpoint
          example: dedicated
        owner:
          type: string
          description: The owner of this endpoint
          example: devuser
        state:
          type: string
          enum:
            - PENDING
            - STARTING
            - STARTED
            - STOPPING
            - STOPPED
            - ERROR
          description: Current state of the endpoint
          example: STARTED
        autoscaling:
          $ref: '#/components/schemas/Autoscaling'
          description: Configuration for automatic scaling of the endpoint
        created_at:
          type: string
          format: date-time
          description: Timestamp when the endpoint was created
          example: '2025-02-04T10:43:55.405Z'
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
    Autoscaling:
      type: object
      description: Configuration for automatic scaling of replicas based on demand.
      required:
        - min_replicas
        - max_replicas
      properties:
        min_replicas:
          type: integer
          format: int32
          description: >-
            The minimum number of replicas to maintain, even when there is no
            load
          examples:
            - 2
        max_replicas:
          type: integer
          format: int32
          description: The maximum number of replicas to scale up to under load
          examples:
            - 5
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt