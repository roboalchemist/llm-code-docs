# Source: https://docs.tavus.io/api-reference/objectives/create-objectives.md

# Create Objectives

> This endpoint creates a new objective for a persona. Objectives provide goal-oriented instructions that help guide conversations toward specific achievements and desired outcomes.


## OpenAPI

````yaml post /v2/objectives
paths:
  path: /v2/objectives
  method: post
  servers:
    - url: https://tavusapi.com
  request:
    security:
      - title: apiKey
        parameters:
          query: {}
          header:
            x-api-key:
              type: apiKey
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: array
                    description: Array of objectives to create
                    items:
                      type: object
                      properties:
                        objective_name:
                          type: string
                          description: >-
                            A descriptive name for the objective. This must be a
                            string value without spaces.
                          example: ask_if_new_patient
                        objective_prompt:
                          type: string
                          description: >-
                            The detailed prompt that defines what the objective
                            should accomplish.
                          example: >-
                            Ask the patient if they are new or have been here
                            before
                        confirmation_mode:
                          type: string
                          description: >-
                            How the objective completion should be confirmed. If
                            set to `manual`, the user will be prompted to
                            confirm the objective completion. If set to `auto`,
                            the LLM will determine whether the objective was
                            completed or not.
                          enum:
                            - auto
                            - manual
                          default: auto
                          example: auto
                        output_variables:
                          type: array
                          description: >-
                            Optional list of variables that should be extracted
                            or collected during the objective.
                          items:
                            type: string
                          example:
                            - patient_status
                        modality:
                          type: string
                          description: >-
                            The communication modality for the objective. If set
                            to `verbal`, the objective will be completed by the
                            user's responses. If set to `visual`, the objective
                            can only be completed by visual / perception cues
                            observed by Raven.
                          enum:
                            - verbal
                            - visual
                          default: verbal
                          example: verbal
                        next_conditional_objectives:
                          type: object
                          description: >-
                            A mapping of objective names to conditions that must
                            be satisfied for that objective to be activated.
                          additionalProperties:
                            type: string
                          example:
                            new_patient_intake_process: >-
                              If the patient has never been to the practice
                              before
                            existing_patient_intake_process: If the patient has been to the practice before
                        next_required_objectives:
                          type: array
                          description: >-
                            List of objective names that will be activated once
                            the current objective is completed.
                          items:
                            type: string
                          example:
                            - get_patient_name
                        callback_url:
                          type: string
                          description: >-
                            Optional URL that will receive notifications when
                            the objective is completed.
                          example: https://your-server.com/webhook
                      required:
                        - objective_name
                        - objective_prompt
            requiredProperties:
              - data
        examples:
          example:
            value:
              data:
                - objective_name: ask_if_new_patient
                  objective_prompt: Ask the patient if they are new or have been here before
                  confirmation_mode: auto
                  output_variables:
                    - patient_status
                  modality: verbal
                  next_conditional_objectives:
                    new_patient_intake_process: If the patient has never been to the practice before
                    existing_patient_intake_process: If the patient has been to the practice before
                  next_required_objectives:
                    - get_patient_name
                  callback_url: https://your-server.com/webhook
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              objectives_id:
                allOf:
                  - type: string
                    description: Unique identifier for the created objective
                    example: o12345
              objective_name:
                allOf:
                  - type: string
                    description: Name of the objective
                    example: New Objectives
              status:
                allOf:
                  - type: string
                    description: Current status of the objective
                    example: active
              created_at:
                allOf:
                  - type: string
                    description: ISO 8601 timestamp of when the objective was created
                    example: '2024-01-15T10:30:00Z'
        examples:
          example:
            value:
              objectives_id: o12345
              objective_name: New Objectives
              status: active
              created_at: '2024-01-15T10:30:00Z'
        description: Objective created successfully
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
                    description: Error message describing the validation failure
                    example: objective_name is required
        examples:
          example:
            value:
              message: objective_name is required
        description: Bad Request - Invalid input parameters
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
                    description: The error message.
                    example: Invalid access token
        examples:
          example:
            value:
              message: Invalid access token
        description: UNAUTHORIZED
  deprecated: false
  type: path
components:
  schemas: {}

````