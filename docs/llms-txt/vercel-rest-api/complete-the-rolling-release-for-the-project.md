# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/rolling-release/complete-the-rolling-release-for-the-project.md

# Complete the rolling release for the project

> Force-complete a Rolling Release. The canary deployment will begin serving 100% of the traffic.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/projects/{idOrName}/rolling-release/complete
paths:
  path: /v1/projects/{idOrName}/rolling-release/complete
  method: post
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        idOrName:
          schema:
            - type: string
              required: true
              description: Project ID or project name (URL-encoded)
      query:
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              canaryDeploymentId:
                allOf:
                  - description: The ID of the canary deployment to complete
                    type: string
            requiredProperties:
              - canaryDeploymentId
        examples:
          example:
            value:
              canaryDeploymentId: <string>
    codeSamples:
      - label: completeRollingRelease
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.rollingRelease.completeRollingRelease({
              idOrName: "<value>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              rollingRelease:
                allOf:
                  - nullable: true
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
                          id:
                            type: string
                            description: A string holding the unique ID of the deployment
                            example: dpl_89qyp1cskzkLrVicDaZoDbjyHuDJ
                          name:
                            type: string
                            description: >-
                              The name of the project associated with the
                              deployment at the time that the deployment was
                              created
                            example: my-project
                          url:
                            type: string
                            description: A string with the unique URL of the deployment
                            example: my-instant-deployment-3ij3cxz9qr.now.sh
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
                          source:
                            type: string
                            enum:
                              - api-trigger-git-deploy
                              - cli
                              - clone/repo
                              - git
                              - import
                              - import/repo
                              - redeploy
                              - v0-web
                            description: Where was the deployment created from
                            example: cli
                          createdAt:
                            type: number
                            description: >-
                              A number containing the date when the deployment
                              was created in milliseconds
                            example: 1540257589405
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
                        required:
                          - id
                          - name
                          - url
                          - createdAt
                          - readyState
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
                          id:
                            type: string
                            description: A string holding the unique ID of the deployment
                            example: dpl_89qyp1cskzkLrVicDaZoDbjyHuDJ
                          name:
                            type: string
                            description: >-
                              The name of the project associated with the
                              deployment at the time that the deployment was
                              created
                            example: my-project
                          url:
                            type: string
                            description: A string with the unique URL of the deployment
                            example: my-instant-deployment-3ij3cxz9qr.now.sh
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
                          source:
                            type: string
                            enum:
                              - api-trigger-git-deploy
                              - cli
                              - clone/repo
                              - git
                              - import
                              - import/repo
                              - redeploy
                              - v0-web
                            description: Where was the deployment created from
                            example: cli
                          createdAt:
                            type: number
                            description: >-
                              A number containing the date when the deployment
                              was created in milliseconds
                            example: 1540257589405
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
                        required:
                          - id
                          - name
                          - url
                          - createdAt
                          - readyState
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
                              description: >-
                                Whether to linearly shift traffic over the
                                duration of this stage
                              example: false
                          required:
                            - index
                            - isFinalStage
                            - targetPercentage
                            - requireApproval
                            - duration
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
                            description: >-
                              Whether to linearly shift traffic over the
                              duration of this stage
                            example: false
                        required:
                          - index
                          - isFinalStage
                          - targetPercentage
                          - requireApproval
                          - duration
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
                            description: >-
                              Whether to linearly shift traffic over the
                              duration of this stage
                            example: false
                        required:
                          - index
                          - isFinalStage
                          - targetPercentage
                          - requireApproval
                          - duration
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
                      - state
                      - currentDeployment
                      - canaryDeployment
                      - queuedDeploymentId
                      - advancementType
                      - stages
                      - activeStage
                      - nextStage
                      - startedAt
                      - updatedAt
                    type: object
                    description: >-
                      Rolling release information including configuration and
                      document details, or null if no rolling release exists
            description: >-
              The response format for rolling release endpoints that return
              rolling release information
            requiredProperties:
              - rollingRelease
        examples:
          example:
            value:
              rollingRelease:
                state: ACTIVE
                currentDeployment:
                  id: dpl_abc123
                  name: my-shop@main
                  url: my-shop.vercel.app
                  target: production
                  source: git
                  createdAt: 1716206500000
                  readyState: READY
                  readyStateAt: 1716206800000
                canaryDeployment:
                  id: dpl_def456
                  name: my-shop@9c7e2f4
                  url: 9c7e2f4-my-shop.vercel.app
                  target: production
                  source: git
                  createdAt: 1716210100000
                  readyState: READY
                  readyStateAt: 1716210400000
                queuedDeploymentId: dpl_ghi789
                advancementType: manual-approval
                stages:
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
                  index: 1
                  isFinalStage: false
                  targetPercentage: 25
                  requireApproval: true
                  duration: null
                nextStage:
                  index: 2
                  isFinalStage: false
                  targetPercentage: 60
                  requireApproval: true
                  duration: null
                startedAt: 1716210500000
                updatedAt: 1716210600000
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the request query is invalid.
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404': {}
  deprecated: false
  type: path
components:
  schemas: {}

````