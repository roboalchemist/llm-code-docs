# Source: https://docs.edgeimpulse.com/apis/studio/dsp/get-processed-sample-from-features-array.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get processed sample (from features array)

> Takes in a features array and runs it through the DSP block. This data should have the same frequency as set in the input block in your impulse.



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/dsp/{dspId}/run
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
  /api/{projectId}/dsp/{dspId}/run:
    post:
      tags:
        - DSP
      summary: Get processed sample (from features array)
      description: >-
        Takes in a features array and runs it through the DSP block. This data
        should have the same frequency as set in the input block in your
        impulse.
      operationId: runDspOnFeaturesArray
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/DspIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DspRunRequestWithFeatures'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DspRunResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    DspIdParameter:
      name: dspId
      in: path
      required: true
      description: DSP Block ID, use the impulse functions to retrieve the ID
      schema:
        type: integer
  schemas:
    DspRunRequestWithFeatures:
      type: object
      required:
        - features
        - params
        - drawGraphs
        - requestPerformance
      properties:
        features:
          type: array
          description: >-
            Array of features. If you have multiple axes the data should be
            interleaved (e.g. [ax0_val0, ax1_val0, ax2_val0, ax0_val1, ax1_val1,
            ax2_val1]).
          items:
            type: integer
        params:
          type: object
          description: DSP parameters with values
          example:
            scale-axes: '10'
          additionalProperties:
            type: string
            nullable: true
        drawGraphs:
          type: boolean
          description: Whether to generate graphs (will take longer)
        requestPerformance:
          type: boolean
          description: Whether to request performance info (will take longer unless cached)
    DspRunResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - features
            - graphs
          properties:
            features:
              type: array
              description: >-
                Array of processed features. Laid out according to the names in
                'labels'
              items:
                type: number
            graphs:
              type: array
              description: Graphs to plot to give an insight in how the DSP process ran
              items:
                $ref: '#/components/schemas/DspRunGraph'
            labels:
              type: array
              description: Labels of the feature axes
              items:
                type: string
            state_string:
              type: string
              description: String representation of the DSP state returned
            performance:
              $ref: '#/components/schemas/DspPerformance'
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
    DspRunGraph:
      type: object
      required:
        - name
        - type
      properties:
        name:
          type: string
          description: Name of the graph
          example: Frequency domain
        image:
          type: string
          description: Base64 encoded image, only present if type is 'image'
        imageMimeType:
          type: string
          description: >-
            Mime type of the Base64 encoded image, only present if type is
            'image'
        X:
          type: object
          description: >-
            Values on the x-axis per plot. Key is the name of the raw feature.
            Present if type is 'logarithmic' or 'linear'.
          example:
            accX:
              - 3
              - 5
              - 7
            accY:
              - 2
              - 1
              - 5
          additionalProperties:
            type: array
            items:
              type: number
        'y':
          type: array
          description: Values of the y-axis. Present if type is 'logarithmic' or 'linear'.
          example:
            - 0
            - 0.5
            - 1
          items:
            type: number
        suggestedXMin:
          type: number
          description: Suggested minimum value of x-axis
        suggestedXMax:
          type: number
          description: Suggested maxium value of x-axis
        suggestedYMin:
          type: number
          description: Suggested minimum value of y-axis
        suggestedYMax:
          type: number
          description: Suggested maximum value of y-axis
        type:
          type: string
          description: Type of graph (either `logarithmic`, `linear` or `image`)
        lineWidth:
          type: number
          description: >-
            Width of the graph line (if type is `logarithmic` or `linear`).
            Default 3.
        smoothing:
          type: boolean
          description: Whether to apply smoothing to the graph.
        axisLabels:
          type: object
          description: Labels for the graph x and y axes.
          required:
            - X
            - 'y'
          properties:
            X:
              type: string
            'y':
              type: string
        highlights:
          type: object
          description: Indices of points to highlight, per axis.
          additionalProperties:
            type: array
            items:
              type: number
    DspPerformance:
      type: object
      required:
        - latency
        - ram
      properties:
        latency:
          type: integer
        ram:
          type: integer
        customDspString:
          type: string
          description: >-
            If the project latencyDevice has custom DSP hardware, this value
            contains a device specific latency metric (eg. cycles)
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