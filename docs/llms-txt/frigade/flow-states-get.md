# Source: https://docs.frigade.com/api-reference/flows/flow-states-get.md

# Get User Flow State

> Get the state of a User in all Flows

## OpenAPI

````yaml get /v1/public/flowStates
paths:
  path: /v1/public/flowStates
  method: get
  request:
    security:
      - title: bearer
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Authentication header of the form `Bearer: <token>`, where
                `<token>` is either your public or private API key. [See when to
                use which](/v2/api-reference/authorization)
          cookie: {}
    parameters:
      path: {}
      query:
        userId:
          schema:
            - type: string
              required: true
              description: The ID of the user
        groupId:
          schema:
            - type: string
              required: false
              description: Optional ID of the group
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              eligibleFlows:
                allOf:
                  - description: >-
                      List of Flows that the user is eligible for as well as the
                      user's state in each Flow
                    type: array
                    items:
                      $ref: '#/components/schemas/StatefulFlow'
              ineligibleFlows:
                allOf:
                  - description: >-
                      List of Flow IDs that the user is ineligible for (for
                      instance if a Flow is turned off)
                    type: array
                    items:
                      type: string
            refIdentifier: '#/components/schemas/PublicUserFlowStateV2'
        examples:
          example:
            value:
              eligibleFlows:
                - flowSlug: flow_abc
                  flowName: Onboarding Checklist
                  flowType: ANNOUNCEMENT
                  data:
                    steps:
                      - id: step_abc
                        $state:
                          completed: true
                          skipped: true
                          started: true
                          visible: true
                          blocked: true
                          lastActionAt: '2024-09-01T00:00:00.000Z'
                          flowResponses:
                            - flowSlug: flow_abc
                              actionType: STARTED_STEP
                              stepId: step-1
                              data: '{"key": "value"}'
                              createdAt: '2024-01-01T00:00:00Z'
                  $state:
                    currentStepId: step_abc
                    currentStepIndex: 1
                    completed: true
                    started: true
                    skipped: true
                    visible: true
                    lastActionAt: '2024-09-01T00:00:00.000Z'
                    flowResponses:
                      - flowSlug: flow_abc
                        actionType: STARTED_STEP
                        stepId: step-1
                        data: '{"key": "value"}'
                        createdAt: '2024-01-01T00:00:00Z'
                  version: 1
              ineligibleFlows:
                - <string>
        description: The Flow state for the User was found
  deprecated: false
  type: path
components:
  schemas:
    ExternalizedFlowResponse:
      type: object
      properties:
        flowSlug:
          type: string
          description: The ID of the Flow
          example: flow_abc
        stepId:
          type: string
          description: The ID of the Step
          example: step-1
        data:
          type: string
          description: >-
            The JSON serialized data of the Flow response (for instance form
            data).
          example: '{"key": "value"}'
        actionType:
          type: string
          description: >-
            The action type of the step. Possible values: `STARTED_STEP`,
            `COMPLETED_STEP`, `SKIPPED_STEP`, `NOT_STARTED_STEP`,
            `STARTED_FLOW`, `COMPLETED_FLOW`, `SKIPPED_FLOW`, `NOT_STARTED_FLOW`
          example: STARTED_STEP
        createdAt:
          format: date-time
          type: string
          description: The timestamp of the flow response
          example: '2024-01-01T00:00:00Z'
      required:
        - flowSlug
        - stepId
        - data
        - actionType
        - createdAt
    StatefulStepState:
      type: object
      properties:
        completed:
          type: boolean
          description: Whether the Step is completed
          example: true
        skipped:
          type: boolean
          description: Whether the Step has been skipped
          example: true
        started:
          type: boolean
          description: Whether the Step has been started
          example: true
        visible:
          type: boolean
          description: Whether the Step is visible (based on `visibilityCriteria`)
          example: true
        blocked:
          type: boolean
          description: Whether the Step is blocked (based on `startCriteria`)
          example: true
        lastActionAt:
          format: date-time
          type: string
          description: The last time the user took an action on the Step
          example: '2024-09-01T00:00:00.000Z'
        flowResponses:
          description: >-
            The flow responses associated with the user in the Step. This is
            only available when using a private API key.
          example:
            - flowSlug: flow_abc
              actionType: STARTED_STEP
              stepId: step-1
              data: '{"key": "value"}'
              createdAt: '2024-01-01T00:00:00Z'
          type: array
          items:
            $ref: '#/components/schemas/ExternalizedFlowResponse'
    StatefulStep:
      type: object
      properties:
        id:
          type: string
          description: The Step ID
          example: step_abc
        $state:
          description: The Step State
          allOf:
            - $ref: '#/components/schemas/StatefulStepState'
    StatefulFlowData:
      type: object
      properties:
        steps:
          description: List of Steps in the Flow
          type: array
          items:
            $ref: '#/components/schemas/StatefulStep'
    StatefulFlowState:
      type: object
      properties:
        currentStepId:
          type: string
          description: The current step (if any) the user is on
          example: step_abc
        currentStepIndex:
          type: number
          description: >-
            The index of the current step in the Flow. Will be -1 if the user
            has not started the Flow
          example: 1
        completed:
          type: boolean
          description: Whether the Flow is completed
          example: true
        started:
          type: boolean
          description: Whether the Flow has been started
          example: true
        skipped:
          type: boolean
          description: Whether the Flow has been skipped/dismissed
          example: true
        visible:
          type: boolean
          description: Whether the Flow is visible (based on the Flow's Targeting)
          example: true
        lastActionAt:
          format: date-time
          type: string
          description: The last time the user took an action on the Flow
          example: '2024-09-01T00:00:00.000Z'
        flowResponses:
          description: >-
            The flow responses associated with the user in the Flow. This is
            only available when using a private API key.
          example:
            - flowSlug: flow_abc
              actionType: STARTED_STEP
              stepId: step-1
              data: '{"key": "value"}'
              createdAt: '2024-01-01T00:00:00Z'
          type: array
          items:
            $ref: '#/components/schemas/ExternalizedFlowResponse'
    StatefulFlow:
      type: object
      properties:
        flowSlug:
          type: string
          description: The Flow Slug
          example: flow_abc
        flowName:
          type: string
          description: The Flow Name
          example: Onboarding Checklist
        flowType:
          type: string
          description: The Flow Type
          example: ANNOUNCEMENT
        data:
          description: The Flow's metadata including the user's state in each step
          allOf:
            - $ref: '#/components/schemas/StatefulFlowData'
        $state:
          description: The user's state in the Flow
          allOf:
            - $ref: '#/components/schemas/StatefulFlowState'
        version:
          type: number
          description: The version number of the Flow
          example: 1

````