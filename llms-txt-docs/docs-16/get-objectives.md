# Source: https://docs.tavus.io/api-reference/objectives/get-objectives.md

# Get Objective

> This endpoint returns a single objective by its unique identifier.


## OpenAPI

````yaml get /v2/objectives/{objectives_id}
paths:
  path: /v2/objectives/{objectives_id}
  method: get
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
      path:
        objectives_id:
          schema:
            - type: string
              required: true
              description: The unique identifier of the objective.
              example: o12345
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: object
                    properties:
                      objective_name:
                        type: string
                        description: Name of the objective
                        example: ask_if_new_patient
                      objective_prompt:
                        type: string
                        description: >-
                          The detailed prompt that defines what the objective
                          should accomplish
                        example: >-
                          Ask the patient if they are new or have been here
                          before
                      confirmation_mode:
                        type: string
                        description: How the objective completion should be confirmed
                        example: auto
                      output_variables:
                        type: array
                        description: >-
                          List of variables that should be extracted or
                          collected during the objective
                        items:
                          type: string
                        example:
                          - patient_status
                      modality:
                        type: string
                        description: The communication modality for the objective
                        example: verbal
                      next_conditional_objectives:
                        type: object
                        description: >-
                          Mapping of objective names to conditions that must be
                          satisfied for that objective to be activated
                        additionalProperties:
                          type: string
                        example:
                          new_patient_intake_process: If the patient has never been to the practice before
                          existing_patient_intake_process: If the patient has been to the practice before
                      next_required_objectives:
                        type: array
                        description: >-
                          List of objective names that will be activated once
                          the current objective is completed
                        items:
                          type: string
                        example:
                          - get_patient_name
                      callback_url:
                        type: string
                        description: >-
                          URL that will receive notifications when the objective
                          is completed
                        example: https://your-server.com/webhook
                      created_at:
                        type: string
                        description: ISO 8601 timestamp of when the objective was created
                        example: '2024-01-15T10:30:00Z'
                      updated_at:
                        type: string
                        description: >-
                          ISO 8601 timestamp of when the objective was last
                          updated
                        example: '2024-01-15T10:30:00Z'
        examples:
          example:
            value:
              data:
                objective_name: ask_if_new_patient
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
                created_at: '2024-01-15T10:30:00Z'
                updated_at: '2024-01-15T10:30:00Z'
        description: Successfully retrieved objective
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message.
                    example: Invalid objectives_id
        examples:
          example:
            value:
              error: Invalid objectives_id
        description: Bad Request
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
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message.
                    example: Objective not found
        examples:
          example:
            value:
              error: Objective not found
        description: Not Found
  deprecated: false
  type: path
components:
  schemas: {}

````