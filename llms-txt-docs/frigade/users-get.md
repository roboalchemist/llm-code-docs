# Source: https://docs.frigade.com/api-reference/users/users-get.md

# Find a User

> Find a user by ID

## OpenAPI

````yaml get /v1/users
paths:
  path: /v1/users
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
        foreignId:
          schema:
            - type: string
              required: true
        userId:
          schema:
            - type: string
              required: true
              description: The ID of the user
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              userId:
                allOf:
                  - type: string
                    description: The ID of the user as defined in your own application
                    example: d34daa11-3745-4ac0-880e-d4b4d51fe13f
              createdAt:
                allOf:
                  - format: date-time
                    type: string
                    description: The date and time the user was created
                    example: '2024-01-01T00:00:00Z'
              modifiedAt:
                allOf:
                  - format: date-time
                    type: string
                    description: The date and time the user was last modified
                    example: '2024-01-01T00:00:00Z'
              properties:
                allOf:
                  - type: string
                    description: The properties of the user
                    example:
                      email: john@doe.com
                      firstName: John
                      lastName: Doe
                      imageUrl: https://example.com/john-doe.jpg
              isGuest:
                allOf:
                  - type: boolean
                    description: Whether the user is a guest
                    example: false
              email:
                allOf:
                  - type: string
                    description: The email address of the user
                    example: john@doe.com
              firstName:
                allOf:
                  - type: string
                    description: The first name of the user
                    example: John
              lastName:
                allOf:
                  - type: string
                    description: The last name of the user
                    example: Doe
              userFlowStates:
                allOf:
                  - description: The user's state in the Flows they have interacted with
                    type: array
                    items:
                      $ref: '#/components/schemas/UserFlowState'
              trackingEvents:
                allOf:
                  - description: The tracking events associated with the user
                    example:
                      - event: SignedUp
                        properties:
                          source: landing-page
                          campaign: summer-sale
                        createdAt: '2024-01-01T00:00:00Z'
                    type: array
                    items:
                      $ref: '#/components/schemas/ExternalizedTrackingEvent'
            refIdentifier: '#/components/schemas/ExternalizedUser'
        examples:
          example:
            value:
              userId: d34daa11-3745-4ac0-880e-d4b4d51fe13f
              createdAt: '2024-01-01T00:00:00Z'
              modifiedAt: '2024-01-01T00:00:00Z'
              properties:
                email: john@doe.com
                firstName: John
                lastName: Doe
                imageUrl: https://example.com/john-doe.jpg
              isGuest: false
              email: john@doe.com
              firstName: John
              lastName: Doe
              userFlowStates:
                - flowSlug: flow_abc
                  flowState: COMPLETED_FLOW
                  flowResponses:
                    - flowSlug: flow_abc
                      actionType: STARTED_STEP
                      stepId: step-1
                      data: '{"key": "value"}'
                      createdAt: '2024-01-01T00:00:00Z'
              trackingEvents:
                - event: SignedUp
                  properties:
                    source: landing-page
                    campaign: summer-sale
                  createdAt: '2024-01-01T00:00:00Z'
        description: The user was successfully found
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The user was not found
        examples: {}
        description: The user was not found
  deprecated: false
  type: path
components:
  schemas:
    ExternalizedTrackingEvent:
      type: object
      properties:
        event:
          type: string
          description: The name of the tracking event
          example: SignedUp
        properties:
          type: object
          description: The properties of the tracking event
          example:
            source: landing-page
            campaign: summer-sale
      required:
        - event
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
    UserFlowState:
      type: object
      properties:
        flowSlug:
          type: string
          description: The ID of the Flow
          example: flow_abc
        flowState:
          type: string
          description: >-
            The user's state in the Flow. Possible values: `COMPLETED_FLOW`,
            `STARTED_FLOW`, `NOT_STARTED_FLOW`, `SKIPPED_FLOW`
          example: COMPLETED_FLOW
        flowResponses:
          description: The flow responses associated with the user
          example:
            - flowSlug: flow_abc
              actionType: STARTED_STEP
              stepId: step-1
              data: '{"key": "value"}'
              createdAt: '2024-01-01T00:00:00Z'
          type: array
          items:
            $ref: '#/components/schemas/ExternalizedFlowResponse'
      required:
        - flowSlug
        - flowState

````