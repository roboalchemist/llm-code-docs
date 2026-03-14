# Source: https://docs.edgeimpulse.com/apis/studio/projects/list-versions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List versions

> Get all versions for this project.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/versions
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
  /api/{projectId}/versions:
    get:
      tags:
        - Projects
      summary: List versions
      description: Get all versions for this project.
      operationId: listVersions
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListVersionsResponse'
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
    ListVersionsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - nextVersion
            - versions
            - customLearnBlocks
            - runModelTestingWhileVersioning
          properties:
            nextVersion:
              type: integer
            versions:
              type: array
              items:
                type: object
                required:
                  - id
                  - version
                  - description
                  - bucket
                  - created
                properties:
                  id:
                    type: integer
                  version:
                    type: integer
                  description:
                    type: string
                  bucket:
                    type: object
                    required:
                      - path
                    properties:
                      id:
                        type: integer
                      name:
                        type: string
                      organizationName:
                        type: string
                      path:
                        type: string
                      bucket:
                        type: string
                  created:
                    type: string
                    format: date-time
                  userId:
                    type: integer
                  userName:
                    type: string
                  userPhoto:
                    type: string
                  publicProjectId:
                    type: integer
                  publicProjectUrl:
                    type: string
                  trainingAccuracy:
                    type: number
                    description: Accuracy calculated during training, using validation set.
                  testAccuracy:
                    type: number
                    description: Accuracy on test set.
                  trainingmAP50:
                    type: number
                    description: >-
                      Mean Average Precision @ IoU=50 on validation set (for
                      object detection projects).
                  testmAP50:
                    type: number
                    description: >-
                      Mean Average Precision @ IoU=50 on test set (for object
                      detection projects).
                  accuracyBasedOnImpulse:
                    type: string
                    description: >-
                      If your project had multiple impulses, this field
                      indicates which impulse was used to calculate the accuracy
                      metrics.
                  totalSamplesCount:
                    type: string
                  license:
                    $ref: '#/components/schemas/PublicProjectLicense'
            customLearnBlocks:
              type: array
              description: >-
                If you have any custom learn blocks (e.g. blocks you pushed
                through Bring Your Own Model), then these are listed here. We
                use these to show a warning in the UI that these blocks will
                also be available in a public version.
              items:
                type: object
                required:
                  - author
                  - name
                properties:
                  author:
                    type: string
                  name:
                    type: string
            runModelTestingWhileVersioning:
              type: boolean
              description: >-
                Whether the 'Run model testing while versioning' checkbox should
                be enabled.
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
    PublicProjectLicense:
      type: string
      enum:
        - Apache-2.0
        - BSD-3-Clause
        - BSD-3-Clause-Clear
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