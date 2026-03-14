# Source: https://docs.edgeimpulse.com/apis/studio/impulse/set-thresholds.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Set thresholds

> Set thresholds (e.g. min. confidence rating, or min. anomaly score) for an impulse.



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/impulse/{impulseId}/set-thresholds
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
  /api/{projectId}/impulse/{impulseId}/set-thresholds:
    post:
      tags:
        - Impulse
      summary: Set thresholds
      description: >-
        Set thresholds (e.g. min. confidence rating, or min. anomaly score) for
        an impulse.
      operationId: setImpulseThresholds
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/ImpulseIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SetImpulseThresholdsRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SetImpulseThresholdsResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    ImpulseIdParameter:
      name: impulseId
      in: path
      required: true
      description: Impulse ID
      schema:
        type: integer
  schemas:
    SetImpulseThresholdsRequest:
      type: object
      required:
        - thresholds
        - allowCreatingRegenerateModelTestingJobs
      properties:
        thresholds:
          type: array
          items:
            type: object
            required:
              - blockId
              - key
              - value
            properties:
              blockId:
                type: integer
                description: Learn block ID for which you want to set the threshold
              key:
                type: string
                description: Threshold identifier (see BlockThreshold#key)
              value:
                description: New threshold value
                oneOf:
                  - type: number
                  - type: string
        allowCreatingRegenerateModelTestingJobs:
          type: boolean
          description: >
            Whether a call to this function is allowed to create jobs to
            regenerate model testing results

            (e.g. object detection datasets, or large datasets).

            This option is here because further calls to setImpulseThresholds
            are blocked

            while model testing jobs are running (so e.g. live classification
            has this to FALSE).
        forceRunRegenerateModelTestingInJob:
          type: boolean
          description: >-
            If set, this'll force the creation of a job to regenerate the model
            testing results.
    SetImpulseThresholdsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - hadModelTestingResults
            - regenerateModelTestingStatus
          properties:
            hadModelTestingResults:
              description: >-
                Whether there were model testing results available before
                calling this function.
              type: boolean
            regenerateModelTestingStatus:
              description: >
                Altering thresholds invalidates model testing results. We try to
                regenerate the results where possible.

                You'll get either

                "not_regenerated" (e.g. no model testing results, or dataset
                does not support fast regeneration, like for object detection
                models);

                "regenerated" (regeneration successful);

                "started_job" (regenerate is possible, but requires a job, that
                was kicked off - e.g. for large test sets);

                "requires_job" (requires a job, but
                "allowCreatingRegenerateModelTestingJobs" was false - start a
                new job manually via regenerateModelTestingSummary).

                If a job was started then "regenerateModelTestingResultsJobId"
                is set.
              type: string
              enum:
                - not_regenerated
                - regenerated
                - started_job
                - requires_job
            regenerateModelTestingResultsJobId:
              description: >
                If there previously were model testing results, and your dataset
                supports fast re-generation of model testing results

                (e.g. no object detection blocks), but your dataset is too big
                to re-generate results inline (e.g. >20K test set samples) -

                then a job is kicked off to regenerate the results. This field
                contains the job ID.
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