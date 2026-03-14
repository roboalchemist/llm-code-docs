# Source: https://docs.edgeimpulse.com/apis/studio/dsp/get-metadata.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get metadata

> Retrieve the metadata from a generated DSP block.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/dsp/{dspId}/metadata
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
  /api/{projectId}/dsp/{dspId}/metadata:
    get:
      tags:
        - DSP
      summary: Get metadata
      description: Retrieve the metadata from a generated DSP block.
      operationId: getDspMetadata
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/DspIdParameter'
        - $ref: '#/components/parameters/ExcludeIncludedSamplesParameter'
        - $ref: '#/components/parameters/OptionalDSPCategoryParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DSPMetadataResponse'
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
    ExcludeIncludedSamplesParameter:
      name: excludeIncludedSamples
      in: query
      required: false
      description: >-
        Whether to exclude 'includedSamples' in the response (as these can slow
        down requests significantly).
      schema:
        type: boolean
    OptionalDSPCategoryParameter:
      name: category
      in: query
      required: false
      description: Which of the acquisition categories to get metadata from
      schema:
        type: string
        enum:
          - training
          - testing
          - all
  schemas:
    DSPMetadataResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - $ref: '#/components/schemas/DSPMetadata'
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
    DSPMetadata:
      type: object
      required:
        - created
        - generated
        - dspConfig
        - labels
        - featureCount
        - windowCount
        - includedSamples
        - windowSizeMs
        - windowIncreaseMs
        - padZeros
        - frequency
        - outputConfig
      properties:
        created:
          type: string
          format: date-time
          description: Date when the features were created
        generated:
          type: boolean
          description: Whether features were generated
        dspConfig:
          type: object
          additionalProperties:
            type: string
        labels:
          type: array
          description: Labels in the dataset when generator ran
          items:
            type: string
        featureLabels:
          type: array
          description: >-
            Names of the generated features. Only set if axes have explicit
            labels.
          items:
            type: string
        windowCount:
          type: integer
        featureCount:
          type: integer
          description: Number of features for this DSP block
        includedSamples:
          type: array
          description: >-
            The included samples in this DSP block. Note that these are sorted
            in the same way as the `npy` files are laid out. So with the
            `windowCount` parameter you can exactly search back to see which
            file contributed to which windows there.
          items:
            type: object
            required:
              - id
              - windowCount
            properties:
              id:
                type: integer
              windowCount:
                type: integer
        windowSizeMs:
          type: integer
          description: Length of the sliding window when generating features.
        windowIncreaseMs:
          type: integer
          description: Increase of the sliding window when generating features.
        padZeros:
          type: boolean
          description: Whether data was zero-padded when generating features.
        frequency:
          type: number
          description: Frequency of the original data in Hz.
        outputConfig:
          type: object
          description: Information about the output of the DSP block
          required:
            - type
            - shape
          properties:
            type:
              type: string
              description: Output type of the DSP block
              enum:
                - image
                - spectrogram
                - flat
            shape:
              type: object
              description: The shape of the block output
              required:
                - width
              properties:
                width:
                  description: >-
                    Available on all types. Denotes the width of an 'image' or
                    'spectrogram', or the number of features in a 'flat' block.
                  type: integer
                height:
                  description: Only available for type 'image' and 'spectrogram'
                  type: integer
                channels:
                  description: Only available for type 'image'
                  type: integer
                frames:
                  description: Number of frames, only available for type 'image'
                  type: integer
        fftUsed:
          type: array
          items:
            type: integer
        resamplingAlgorithmVersion:
          type: number
          description: >-
            The version number of the resampling algorithm used (for resampled
            time series data only)
        featureExplorerJobId:
          type: integer
          description: >-
            When specified, a job is running (asynchronously) to generate the
            feature explorer.
        featureExplorerJobFailed:
          description: >-
            If this is set, then the feature explorer job failed (get the status
            by getting the job logs for 'featureExplorerJobId').
          type: boolean
        featureImportanceJobId:
          type: integer
          description: >-
            When specified, a job is running (asynchronously) to generate
            feature importance.
        featureImportanceJobFailed:
          description: >-
            If this is set, then the feature importance job failed (get the
            status by getting the job logs for 'featureImportanceJobId').
          type: boolean
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