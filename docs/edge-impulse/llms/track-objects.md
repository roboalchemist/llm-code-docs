# Source: https://docs.edgeimpulse.com/apis/studio/raw-data/track-objects.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Track objects

> Track objects between two samples. Source sample should have bounding boxes set.



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/raw-data/track-objects
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
  /api/{projectId}/raw-data/track-objects:
    post:
      tags:
        - Raw data
      summary: Track objects
      description: >-
        Track objects between two samples. Source sample should have bounding
        boxes set.
      operationId: trackObjects
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TrackObjectsRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TrackObjectsResponse'
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
    TrackObjectsRequest:
      type: object
      required:
        - sourceSampleId
        - nextSampleId
      properties:
        sourceSampleId:
          type: integer
        nextSampleId:
          type: integer
    TrackObjectsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - boundingBoxes
          properties:
            boundingBoxes:
              type: array
              items:
                $ref: '#/components/schemas/BoundingBox'
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
    BoundingBox:
      type: object
      description: >-
        This has the _absolute values_ for x/y/w/h (so 0..x (where x is the w/h
        of the image))
      required:
        - label
        - x
        - 'y'
        - width
        - height
      properties:
        label:
          type: string
        x:
          type: integer
        'y':
          type: integer
        width:
          type: integer
        height:
          type: integer
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