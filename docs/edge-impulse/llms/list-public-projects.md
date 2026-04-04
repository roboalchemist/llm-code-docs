# Source: https://docs.edgeimpulse.com/apis/studio/projects/list-public-projects.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List public projects

> Retrieve the list of all public projects. You don't need any authentication for this method.



## OpenAPI

````yaml .assets/openapi.yaml get /api/projects/public
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
  /api/projects/public:
    get:
      tags:
        - Projects
      summary: List public projects
      description: >-
        Retrieve the list of all public projects. You don't need any
        authentication for this method.
      operationId: listPublicProjects
      parameters:
        - $ref: '#/components/parameters/LimitResultsParameter'
        - $ref: '#/components/parameters/OffsetResultsParameter'
        - $ref: '#/components/parameters/FiltersProjectNameParameter'
        - $ref: '#/components/parameters/FiltersProjectTypesParameter'
        - $ref: '#/components/parameters/SortQueryParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListPublicProjectsResponse'
      security: []
components:
  parameters:
    LimitResultsParameter:
      name: limit
      in: query
      required: false
      description: Maximum number of results
      schema:
        type: integer
    OffsetResultsParameter:
      name: offset
      in: query
      required: false
      description: >-
        Offset in results, can be used in conjunction with LimitResultsParameter
        to implement paging.
      schema:
        type: integer
    FiltersProjectNameParameter:
      name: project
      in: query
      required: false
      description: Only include projects where the name or owner contains this string
      schema:
        type: string
    FiltersProjectTypesParameter:
      name: projectTypes
      in: query
      required: false
      description: >-
        Comma separated list of project types to filter on. Supported values are
        'audio', 'object-detection', 'image', 'accelerometer', 'other'.
      schema:
        type: string
      example: accelerometer,audio,object-detection
    SortQueryParameter:
      name: sort
      in: query
      required: false
      description: Fields and order to sort query by
      schema:
        type: string
        description: >-
          Comma separated list of fields to sort query by. Prefix with a minus
          (-) sign to indicate descending order. Default order is ascending
        example: id,-name
  schemas:
    ListPublicProjectsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - $ref: '#/components/schemas/ListPublicProjects'
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
    ListPublicProjects:
      type: object
      required:
        - projects
        - totalProjectCount
      properties:
        projects:
          type: array
          description: Array with public projects
          items:
            $ref: '#/components/schemas/ProjectPublicData'
        totalProjectCount:
          type: integer
    ProjectPublicData:
      type: object
      required:
        - id
        - name
        - description
        - created
        - owner
        - publicUrl
        - projectType
        - pageViewCount
        - cloneCount
        - tags
      properties:
        id:
          type: integer
          example: 1
        name:
          type: string
          example: Water hammer detection
        description:
          type: string
        created:
          type: string
          format: date-time
          example: '2019-07-21T17:32:28Z'
        owner:
          type: string
          description: User or organization that owns the project
        ownerAvatar:
          type: string
          description: URL to the project owner avatar, if any
        publicUrl:
          type: string
          description: URL of the latest public version of the project, if any
          example: https://studio.edgeimpulse.com/public/40479/latest
        projectType:
          $ref: '#/components/schemas/ProjectType'
        pageViewCount:
          type: integer
        cloneCount:
          type: integer
        totalSamplesCount:
          type: string
        trainingAccuracy:
          type: number
          description: Accuracy on training set.
        testAccuracy:
          type: number
          description: Accuracy on test set.
        readme:
          type: object
          description: Present if a readme is set for this project
          required:
            - markdown
            - html
          properties:
            markdown:
              type: string
            html:
              type: string
        tags:
          type: array
          items:
            type: string
          description: List of project tags
          example:
            - FOMO
            - birds
    ProjectType:
      type: string
      enum:
        - kws
        - audio
        - object-detection
        - image
        - accelerometer
        - other
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