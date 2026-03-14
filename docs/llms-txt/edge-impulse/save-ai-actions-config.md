# Source: https://docs.edgeimpulse.com/apis/studio/projects/save-ai-actions-config.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Save AI Actions config

> Store an AI Actions config. Use `createAIActionsJob` to run the job. Post the full AI Action here w/ all parameters.



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/ai-actions/{actionId}
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
  /api/{projectId}/ai-actions/{actionId}:
    post:
      tags:
        - Projects
      summary: Save AI Actions config
      description: >-
        Store an AI Actions config. Use `createAIActionsJob` to run the job.
        Post the full AI Action here w/ all parameters.
      operationId: updateAIAction
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/ActionIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateAIActionRequest'
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
    ActionIdParameter:
      name: actionId
      in: path
      required: true
      description: AI Action ID
      schema:
        type: integer
  schemas:
    UpdateAIActionRequest:
      required:
        - steps
        - dataCategory
        - setMetadataAfterRunning
      properties:
        name:
          type: string
          description: >-
            User-provided name. If no name is set then displayName on the action
            will be automatically configured based on the transformation block.
        steps:
          type: array
          items:
            $ref: '#/components/schemas/AIActionsConfigStep'
        dataCategory:
          $ref: '#/components/schemas/AIActionsDataCategory'
          description: Type of data to run this AI action on.
        dataMetadataKey:
          description: >-
            Metadata key to filter on. Required if dataCategory is equal to
            "dataWithoutMetadataKey" or "dataWithMetadata".
          type: string
        dataMetadataValue:
          description: >-
            Metadata value to filter on. Required if dataCategory is equal to
            "dataWithMetadata".
          type: string
        setMetadataAfterRunning:
          type: array
          description: >-
            After the action runs, add this key/value pair as metadata on the
            affected samples.
          items:
            type: object
            required:
              - key
              - value
            properties:
              key:
                type: string
              value:
                type: string
        sortOrder:
          description: >-
            Numeric value (1..n) where this action should be shown in the action
            list (and in which order the actions should run when started from a
            data source).
          type: integer
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
    AIActionsConfigStep:
      type: object
      required:
        - transformationBlockId
        - parameters
      properties:
        transformationBlockId:
          description: The selected transformation block ID.
          type: integer
        parameters:
          description: >-
            Parameters for the transformation block. These map back to the
            parameters in OrganizationTransformationBlock 'parameters' property.
          type: object
          additionalProperties:
            type: string
    AIActionsDataCategory:
      type: string
      enum:
        - allData
        - unlabeledData
        - enabledData
        - dataWithoutMetadataKey
        - dataWithMetadata
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