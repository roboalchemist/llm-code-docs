# Source: https://docs.edgeimpulse.com/apis/studio/organizations/white-label-admin--get-user-jobs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# White Label Admin - Get user jobs

> White label admin only  API to get the list of all project jobs for a user.



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/whitelabel/users/{userId}/jobs
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
  /api/organizations/{organizationId}/whitelabel/users/{userId}/jobs:
    get:
      tags:
        - Organizations
      summary: White Label Admin - Get user jobs
      description: >-
        White label admin only  API to get the list of all project jobs for a
        user.
      operationId: whitelabelAdminGetUserJobs
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/UserIdParameter'
        - $ref: '#/components/parameters/LimitResultsParameter'
        - $ref: '#/components/parameters/OffsetResultsParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListJobsResponse'
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
      schema:
        type: integer
    UserIdParameter:
      name: userId
      in: path
      required: true
      description: User ID
      schema:
        type: integer
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
  schemas:
    ListJobsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - jobs
            - totalJobCount
          properties:
            jobs:
              type: array
              description: Active jobs
              items:
                $ref: '#/components/schemas/Job'
            totalJobCount:
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
    Job:
      type: object
      required:
        - id
        - key
        - created
        - category
        - categoryKey
        - jobNotificationUids
      properties:
        id:
          type: integer
          description: >-
            Job id, use this to refer back to the job. The web socket API also
            uses this ID.
        category:
          type: string
          description: User-friendly category (e.g. "Training model")
        categoryKey:
          type: string
          description: Machine-readable category (e.g. "learn-train-studio-wrapper")
        key:
          type: string
          description: >
            External job identifier, this can be used to categorize jobs, and
            recover job status. E.g. set this to 'keras-192' for a Keras
            learning block with ID 192. When a user refreshes the page you can
            check whether a job is active for this ID and re-attach.
        created:
          type: string
          format: date-time
          description: When the job was created.
        started:
          type: string
          format: date-time
          description: When the job was started.
        finished:
          type: string
          format: date-time
          description: When the job was finished.
        finishedSuccessful:
          type: boolean
          description: Whether the job finished successfully.
        jobNotificationUids:
          type: array
          description: The IDs of users who should be notified when a job is finished.
          items:
            type: integer
        additionalInfo:
          type: string
          description: Additional metadata associated with this job.
        computeTime:
          type: number
          description: >-
            Job duration time in seconds from start to finished, measured by k8s
            job watcher.
        createdByUser:
          $ref: '#/components/schemas/CreatedUpdatedByUser'
          description: The user who started this job.
        categoryCount:
          type: integer
          description: >-
            Some job categories keep a counter on the job number, e.g. in
            synthetic data, so we know what the 1st, 2nd etc. job was in the UI.
        metadata:
          type: object
          description: Structured job metadata
    CreatedUpdatedByUser:
      type: object
      required:
        - id
        - name
        - username
      properties:
        id:
          type: integer
        name:
          type: string
        username:
          type: string
        photo:
          type: string
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