# Source: https://docs.edgeimpulse.com/apis/studio/projects/set-target-constraints.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Set target constraints

> Set target constraints for a project. Use the constraints object to capture hardware attributes of your target device, along with an application budget to allow guidance on performance and resource usage



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/target-constraints
openapi: 3.0.0
info:
  title: Edge Impulse API
  version: 1.0.0
servers:
  - url: https://studio.edgeimpulse.com/v1
security:
  - ApiKeyAuthentication: []
  - JWTAuthentication: []
  - JWTHttpHeaderAuthentication: []
  - OAuth2: []
paths:
  /api/{projectId}/target-constraints:
    post:
      tags:
        - Projects
      summary: Set target constraints
      description: >-
        Set target constraints for a project. Use the constraints object to
        capture hardware attributes of your target device, along with an
        application budget to allow guidance on performance and resource usage
      operationId: setTargetConstraints
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TargetConstraints'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenericApiResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
  schemas:
    TargetConstraints:
      type: object
      required:
        - targetDevices
        - applicationBudgets
      properties:
        selectedTargetBasedOn:
          type: string
          description: >-
            A type explaining how the target was chosen. If updating this
            manually, use the 'user-configured' type
          enum:
            - user-configured
            - default
            - default-accepted
            - recent-project
            - connected-device
        targetDevices:
          type: array
          description: >-
            The potential targets for the project, where each entry captures
            hardware attributes that allow target guidance throughout the Studio
            workflow. The first target in the list is considered as the selected
            target for the project.
          items:
            $ref: '#/components/schemas/TargetConstraintsDevice'
        applicationBudgets:
          type: array
          description: >-
            A list of application budgets to be configured based on target
            device. An application budget enables guidance on performance and
            resource usage. The first application budget in the list is
            considered as the selected budget for the project.
          items:
            $ref: '#/components/schemas/ApplicationBudget'
    GenericApiResponse:
      type: object
      required:
        - success
      properties:
        success:
          type: boolean
          description: Whether the operation succeeded
        error:
          type: string
          description: Optional error description (set if 'success' was false)
    TargetConstraintsDevice:
      type: object
      properties:
        processors:
          type: array
          description: Target processors
          items:
            $ref: '#/components/schemas/TargetProcessor'
        board:
          type: string
          description: The exact dev board part number, if available
        name:
          type: string
          description: Display name in Studio
        latencyDevice:
          type: string
          description: MCU identifier, if available
          example: cortex-m4f-80mhz
    ApplicationBudget:
      type: object
      description: >-
        Specifies limits for your specific application, as available RAM and ROM
        for the model's operation and the maximum allowed latency.
      properties:
        latencyPerInferenceMs:
          $ref: '#/components/schemas/ResourceRange'
        energyPerInferenceJoules:
          $ref: '#/components/schemas/ResourceRange'
        memoryOverhead:
          $ref: '#/components/schemas/TargetMemory'
    TargetProcessor:
      type: object
      properties:
        part:
          type: string
          description: The exact part number, if available
        format:
          type: string
          description: >-
            Processor type, serving as a broad descriptor for the intended
            use-case
          example: low-end MCU
        architecture:
          type: string
          description: >-
            Processor family, informing about the processor's instruction set
            and core design
          example: Cortex-M
        specificArchitecture:
          type: string
          description: >-
            Processor architecture, informing about the specific processor, if
            known
          example: Cortex-M0+
        accelerator:
          type: string
          description: Target accelerator, if any
          example: Arm Cortex-U55
        fpu:
          type: boolean
          description: Does the target processor have a floating point unit
        clockRateMhz:
          $ref: '#/components/schemas/ResourceRange'
          description: Clock rate of the processor
        memory:
          $ref: '#/components/schemas/TargetMemory'
    ResourceRange:
      type: object
      description: Describes range of expected availability for an arbitrary resource
      properties:
        minimum:
          type: number
        maximum:
          type: number
    TargetMemory:
      type: object
      description: RAM and ROM specifications of target
      properties:
        ram:
          $ref: '#/components/schemas/MemorySpec'
        rom:
          $ref: '#/components/schemas/MemorySpec'
    MemorySpec:
      type: object
      description: Describes performance characteristics of a particular memory type
      properties:
        fastBytes:
          $ref: '#/components/schemas/ResourceRange'
        slowBytes:
          $ref: '#/components/schemas/ResourceRange'
  securitySchemes:
    ApiKeyAuthentication:
      type: apiKey
      in: header
      name: x-api-key
    JWTAuthentication:
      type: apiKey
      in: cookie
      name: jwt
    JWTHttpHeaderAuthentication:
      type: apiKey
      in: header
      name: x-jwt-token
    OAuth2:
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: /v1/oauth/authorize
          tokenUrl: /v1/oauth/token
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information
        implicit:
          authorizationUrl: /v1/oauth/authorize
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information
        password:
          tokenUrl: /v1/oauth/token
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information
        clientCredentials:
          tokenUrl: /v1/oauth/token
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information

````

Built with [Mintlify](https://mintlify.com).