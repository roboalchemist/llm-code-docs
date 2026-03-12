# Source: https://docs.statsig.com/api-reference/release-pipelines/get-pipeline-trigger.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Pipeline Trigger



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/release_pipeline_triggers/{id}
openapi: 3.0.0
info:
  title: Console API
  description: >-
    The "Console API" is the CRUD API for performing the actions offered on
    console.statsig.com without needing to go through the web UI.

    If you have any feature requests, drop on in to our [slack
    channel](https://www.statsig.com/slack) and let us know.

    <br /><br />

    <b>Authorization</b>

    <br />

    All requests must include the **STATSIG-API-KEY** field in the header. The
    value should be a **Console API Key** which can be created in the Project
    Settings on
    [console.statsig.com/api_keys](https://console.statsig.com/api_keys)

    <br /><br />

    <b>Rate Limiting</b>

    <br />

    Requests to the Console API are limited to <code>~ 100reqs / 10secs and ~
    900reqs / 15 mins</code>.

    <br /><br />

    <b>Keyboard Search</b>

    <br />

    Use <code>Ctrl/Cmd + K</code> to search for specific endpoints.
  version: 20240601.0.0
  contact: {}
servers:
  - url: https://statsigapi.net
security: []
tags: []
paths:
  /console/v1/release_pipeline_triggers/{id}:
    get:
      tags:
        - Release Pipelines
      summary: Get Pipeline Trigger
      parameters:
        - name: id
          required: true
          in: path
          schema:
            type: string
      responses:
        '200':
          description: Get pipeline trigger success
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/ReleasePipelineTriggerResponseDto'
                example:
                  data:
                    id: trigger_1646560789123
                    releasePipelineID: pipeline_123456
                    status: IN_PROGRESS
                    currentPhase: Phase 1
                    currentPhaseID: phase_123456
                    currentPhaseEndTime: 1646560799123
                    creatorID: user_123456
                    createdTime: 1646560789123
                    gateID: gate_123456
                    lastModifierID: user_123456
                    lastModifierName: John Doe
                    actions:
                      - type: STARTED
                        timeMs: 1646560789123
                        phaseID: phase_123456
                        actorID: user_123456
                        actorName: John Doe
                  message: Pipeline trigger retrieved successfully.
              example:
                data:
                  id: trigger_1646560789123
                  releasePipelineID: pipeline_123456
                  status: IN_PROGRESS
                  currentPhase: Phase 1
                  currentPhaseID: phase_123456
                  currentPhaseEndTime: 1646560799123
                  creatorID: user_123456
                  createdTime: 1646560789123
                  gateID: gate_123456
                  lastModifierID: user_123456
                  lastModifierName: John Doe
                  actions:
                    - type: STARTED
                      timeMs: 1646560789123
                      phaseID: phase_123456
                      actorID: user_123456
                      actorName: John Doe
                message: Pipeline trigger retrieved successfully.
      security:
        - STATSIG-API-KEY: []
components:
  schemas:
    SingleDataResponse:
      type: object
      properties:
        message:
          type: string
          description: A simple string explaining the result of the operation.
        data:
          type: object
          description: A single result.
      required:
        - message
        - data
    ReleasePipelineTriggerResponseDto:
      type: object
      properties:
        id:
          type: string
          description: Trigger ID
        releasePipelineID:
          type: string
          description: Release Pipeline ID
        actions:
          type: array
          items:
            type: object
            properties:
              type:
                oneOf:
                  - type: string
                    enum:
                      - STARTED
                      - ABORTED
                      - PAUSED
                      - UNPAUSED
                      - APPROVED_FOR
                      - SKIPPED
                      - FULL_ROLL_OUT
                  - type: string
                    enum:
                      - CLEANED_UP
              timeMs:
                type: number
              phaseID:
                type: string
              actorID:
                type: string
              actorName:
                type: string
            required:
              - type
              - timeMs
              - phaseID
              - actorName
          description: Actions
        creatorID:
          type: string
          description: Trigger Creator ID
        createdTime:
          type: number
          description: Trigger Creation Time
          format: double
        description:
          type: string
          description: Optional description for this trigger
        gateID:
          type: string
          description: Gate ID
        dynamicConfigID:
          type: string
          description: Dynamic Config ID
        lastModifierID:
          type: string
          description: Last modifier ID
        lastModifierName:
          type: string
          description: Last modifier name
        configSnapshotID:
          type: string
          description: The snapshot of the config that this trigger is releasing
        status:
          type: string
          description: Pipeline status with this trigger
        currentPhase:
          type: string
          nullable: true
          description: Current phase
        currentPhaseID:
          type: string
          nullable: true
          description: Current phase ID
        currentPhaseEndTime:
          type: number
          nullable: true
          description: Current phase end time
          format: double
      required:
        - id
        - releasePipelineID
        - actions
        - creatorID
        - createdTime
        - lastModifierID
        - lastModifierName
        - status
        - currentPhase
        - currentPhaseID
        - currentPhaseEndTime
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).