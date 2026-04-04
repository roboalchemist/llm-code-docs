# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/rolling-release/update-the-active-rolling-release-to-the-next-stage-for-a-project.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Update the active rolling release to the next stage for a project

> Advance a rollout to the next stage. This is only needed when rolling releases is configured to require manual approval.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/projects/{idOrName}/rolling-release/approve-stage
openapi: 3.0.3
info:
  title: Vercel REST API & SDK
  description: >-
    The [`@vercel/sdk`](https://www.npmjs.com/package/@vercel/sdk) is a
    type-safe Typescript SDK that allows you to access the resources and methods
    of the Vercel REST API. Learn how to [install
    it](https://vercel.com/docs/rest-api/sdk#installing-vercel-sdk) and
    [authenticate](https://vercel.com/docs/rest-api/sdk#authentication) with a
    Vercel access token.
  contact:
    email: support@vercel.com
    name: Vercel Support
    url: https://vercel.com/support
  version: 0.0.1
servers:
  - url: https://api.vercel.com
    description: Production API
security: []
paths:
  /v1/projects/{idOrName}/rolling-release/approve-stage:
    post:
      tags:
        - rolling-release
      summary: Update the active rolling release to the next stage for a project
      description: >-
        Advance a rollout to the next stage. This is only needed when rolling
        releases is configured to require manual approval.
      operationId: approveRollingReleaseStage
      parameters:
        - name: idOrName
          description: Project ID or project name (URL-encoded)
          in: path
          required: true
          schema:
            description: Project ID or project name (URL-encoded)
            type: string
        - description: The Team identifier to perform the request on behalf of.
          in: query
          name: teamId
          schema:
            type: string
            example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        - description: The Team slug to perform the request on behalf of.
          in: query
          name: slug
          schema:
            type: string
            example: my-team-url-slug
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required:
                - nextStageIndex
                - canaryDeploymentId
              properties:
                nextStageIndex:
                  description: The index of the stage to transition to
                  type: number
                canaryDeploymentId:
                  description: >-
                    The id of the canary deployment to approve for the next
                    stage
                  type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                properties:
                  rollingRelease:
                    nullable: true
                    properties:
                      state:
                        type: string
                        enum:
                          - ACTIVE
                          - COMPLETE
                          - ABORTED
                        description: The current state of the rolling release
                        example: ACTIVE
                      currentDeployment:
                        nullable: true
                        properties:
                          name:
                            type: string
                            description: >-
                              The name of the project associated with the
                              deployment at the time that the deployment was
                              created
                            example: my-project
                          createdAt:
                            type: number
                            description: >-
                              A number containing the date when the deployment
                              was created in milliseconds
                            example: 1540257589405
                          id:
                            type: string
                            description: A string holding the unique ID of the deployment
                            example: dpl_89qyp1cskzkLrVicDaZoDbjyHuDJ
                          readyState:
                            type: string
                            enum:
                              - BUILDING
                              - ERROR
                              - INITIALIZING
                              - QUEUED
                              - READY
                              - CANCELED
                            description: >-
                              The state of the deployment depending on the
                              process of deploying, or if it is ready or in an
                              error state
                            example: READY
                          readyStateAt:
                            type: number
                          source:
                            type: string
                            enum:
                              - import
                              - api-trigger-git-deploy
                              - cli
                              - clone/repo
                              - git
                              - import/repo
                              - redeploy
                              - v0-web
                            description: Where was the deployment created from
                            example: cli
                          target:
                            nullable: true
                            type: string
                            enum:
                              - staging
                              - production
                            description: >-
                              If defined, either `staging` if a staging alias in
                              the format `<project>.<team>.now.sh` was assigned
                              upon creation, or `production` if the aliases from
                              `alias` were assigned. `null` value indicates the
                              "preview" deployment.
                            example: null
                          url:
                            type: string
                            description: A string with the unique URL of the deployment
                            example: my-instant-deployment-3ij3cxz9qr.now.sh
                        required:
                          - createdAt
                          - id
                          - name
                          - readyState
                          - url
                        type: object
                        description: The current deployment receiving production traffic
                        example:
                          id: dpl_abc123
                          name: my-shop@main
                          url: my-shop.vercel.app
                          target: production
                          source: git
                          createdAt: 1716206500000
                          readyState: READY
                          readyStateAt: 1716206800000
                      canaryDeployment:
                        nullable: true
                        properties:
                          name:
                            type: string
                            description: >-
                              The name of the project associated with the
                              deployment at the time that the deployment was
                              created
                            example: my-project
                          createdAt:
                            type: number
                            description: >-
                              A number containing the date when the deployment
                              was created in milliseconds
                            example: 1540257589405
                          id:
                            type: string
                            description: A string holding the unique ID of the deployment
                            example: dpl_89qyp1cskzkLrVicDaZoDbjyHuDJ
                          readyState:
                            type: string
                            enum:
                              - BUILDING
                              - ERROR
                              - INITIALIZING
                              - QUEUED
                              - READY
                              - CANCELED
                            description: >-
                              The state of the deployment depending on the
                              process of deploying, or if it is ready or in an
                              error state
                            example: READY
                          readyStateAt:
                            type: number
                          source:
                            type: string
                            enum:
                              - import
                              - api-trigger-git-deploy
                              - cli
                              - clone/repo
                              - git
                              - import/repo
                              - redeploy
                              - v0-web
                            description: Where was the deployment created from
                            example: cli
                          target:
                            nullable: true
                            type: string
                            enum:
                              - staging
                              - production
                            description: >-
                              If defined, either `staging` if a staging alias in
                              the format `<project>.<team>.now.sh` was assigned
                              upon creation, or `production` if the aliases from
                              `alias` were assigned. `null` value indicates the
                              "preview" deployment.
                            example: null
                          url:
                            type: string
                            description: A string with the unique URL of the deployment
                            example: my-instant-deployment-3ij3cxz9qr.now.sh
                        required:
                          - createdAt
                          - id
                          - name
                          - readyState
                          - url
                        type: object
                        description: The canary deployment being rolled out
                        example:
                          id: dpl_def456
                          name: my-shop@9c7e2f4
                          url: 9c7e2f4-my-shop.vercel.app
                          target: production
                          source: git
                          createdAt: 1716210100000
                          readyState: READY
                          readyStateAt: 1716210400000
                      queuedDeploymentId:
                        nullable: true
                        type: string
                        description: >-
                          The ID of a deployment queued for the next rolling
                          release
                        example: dpl_ghi789
                      advancementType:
                        type: string
                        enum:
                          - automatic
                          - manual-approval
                        description: The advancement type of the rolling release
                        example: manual-approval
                      stages:
                        items:
                          properties:
                            index:
                              type: number
                              description: The zero-based index of the stage
                              example: 0
                            isFinalStage:
                              type: boolean
                              enum:
                                - false
                                - true
                              description: >-
                                Whether or not this stage is the final stage
                                (targetPercentage === 100)
                              example: false
                            targetPercentage:
                              type: number
                              description: >-
                                The percentage of traffic to serve to the canary
                                deployment (0-100)
                              example: 25
                            requireApproval:
                              type: boolean
                              enum:
                                - false
                                - true
                              description: >-
                                Whether or not this stage requires manual
                                approval to proceed
                            duration:
                              nullable: true
                              type: number
                              description: >-
                                Duration in seconds for automatic advancement,
                                null for manual stages or the final stage
                              example: null
                            linearShift:
                              type: boolean
                              enum:
                                - false
                                - true
                              description: >-
                                Whether to linearly shift traffic over the
                                duration of this stage
                              example: false
                          required:
                            - duration
                            - index
                            - isFinalStage
                            - requireApproval
                            - targetPercentage
                          type: object
                          description: All stages configured for this rolling release
                          example:
                            - index: 0
                              isFinalStage: false
                              targetPercentage: 5
                              requireApproval: true
                              duration: null
                            - index: 1
                              isFinalStage: false
                              targetPercentage: 25
                              requireApproval: true
                              duration: null
                            - index: 2
                              isFinalStage: false
                              targetPercentage: 60
                              requireApproval: true
                              duration: null
                            - index: 3
                              isFinalStage: true
                              targetPercentage: 100
                              requireApproval: false
                              duration: null
                        type: array
                        description: All stages configured for this rolling release
                        example:
                          - index: 0
                            isFinalStage: false
                            targetPercentage: 5
                            requireApproval: true
                            duration: null
                          - index: 1
                            isFinalStage: false
                            targetPercentage: 25
                            requireApproval: true
                            duration: null
                          - index: 2
                            isFinalStage: false
                            targetPercentage: 60
                            requireApproval: true
                            duration: null
                          - index: 3
                            isFinalStage: true
                            targetPercentage: 100
                            requireApproval: false
                            duration: null
                      activeStage:
                        nullable: true
                        properties:
                          index:
                            type: number
                            description: The zero-based index of the stage
                            example: 0
                          isFinalStage:
                            type: boolean
                            enum:
                              - false
                              - true
                            description: >-
                              Whether or not this stage is the final stage
                              (targetPercentage === 100)
                            example: false
                          targetPercentage:
                            type: number
                            description: >-
                              The percentage of traffic to serve to the canary
                              deployment (0-100)
                            example: 25
                          requireApproval:
                            type: boolean
                            enum:
                              - false
                              - true
                            description: >-
                              Whether or not this stage requires manual approval
                              to proceed
                          duration:
                            nullable: true
                            type: number
                            description: >-
                              Duration in seconds for automatic advancement,
                              null for manual stages or the final stage
                            example: null
                          linearShift:
                            type: boolean
                            enum:
                              - false
                              - true
                            description: >-
                              Whether to linearly shift traffic over the
                              duration of this stage
                            example: false
                        required:
                          - duration
                          - index
                          - isFinalStage
                          - requireApproval
                          - targetPercentage
                        type: object
                        description: >-
                          The currently active stage, null if the rollout is
                          aborted
                        example:
                          index: 1
                          isFinalStage: false
                          targetPercentage: 25
                          requireApproval: true
                          duration: null
                      nextStage:
                        nullable: true
                        properties:
                          index:
                            type: number
                            description: The zero-based index of the stage
                            example: 0
                          isFinalStage:
                            type: boolean
                            enum:
                              - false
                              - true
                            description: >-
                              Whether or not this stage is the final stage
                              (targetPercentage === 100)
                            example: false
                          targetPercentage:
                            type: number
                            description: >-
                              The percentage of traffic to serve to the canary
                              deployment (0-100)
                            example: 25
                          requireApproval:
                            type: boolean
                            enum:
                              - false
                              - true
                            description: >-
                              Whether or not this stage requires manual approval
                              to proceed
                          duration:
                            nullable: true
                            type: number
                            description: >-
                              Duration in seconds for automatic advancement,
                              null for manual stages or the final stage
                            example: null
                          linearShift:
                            type: boolean
                            enum:
                              - false
                              - true
                            description: >-
                              Whether to linearly shift traffic over the
                              duration of this stage
                            example: false
                        required:
                          - duration
                          - index
                          - isFinalStage
                          - requireApproval
                          - targetPercentage
                        type: object
                        description: >-
                          The next stage to be activated, null if not in ACTIVE
                          state
                        example:
                          index: 2
                          isFinalStage: false
                          targetPercentage: 60
                          requireApproval: true
                          duration: null
                      startedAt:
                        type: number
                        description: >-
                          Unix timestamp in milliseconds when the rolling
                          release started
                        example: 1716210500000
                      updatedAt:
                        type: number
                        description: >-
                          Unix timestamp in milliseconds when the rolling
                          release was last updated
                        example: 1716210600000
                    required:
                      - activeStage
                      - advancementType
                      - canaryDeployment
                      - currentDeployment
                      - nextStage
                      - queuedDeploymentId
                      - stages
                      - startedAt
                      - state
                      - updatedAt
                    type: object
                    description: >-
                      Rolling release information including configuration and
                      document details, or null if no rolling release exists
                required:
                  - rollingRelease
                type: object
                description: >-
                  The response format for rolling release endpoints that return
                  rolling release information
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: ''
        '500':
          description: ''
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````