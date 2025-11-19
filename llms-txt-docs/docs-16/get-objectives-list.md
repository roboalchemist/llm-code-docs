# Source: https://docs.tavus.io/api-reference/objectives/get-objectives-list.md

# Get Objectives

> This endpoint returns a list of all objectives.


## OpenAPI

````yaml get /v2/objectives
paths:
  path: /v2/objectives
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
      path: {}
      query:
        limit:
          schema:
            - type: integer
              description: The number of objectives to return per page. Default is 10.
        page:
          schema:
            - type: integer
              description: The page number to return. Default is 1.
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
                  - type: array
                    items:
                      type: object
                      properties:
                        objectives_id:
                          type: string
                          description: Unique identifier for the objective
                          example: o12345
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
                            Mapping of objective names to conditions that must
                            be satisfied for that objective to be activated
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
                            the current objective is completed
                          items:
                            type: string
                          example:
                            - get_patient_name
                        callback_url:
                          type: string
                          description: >-
                            URL that will receive notifications when the
                            objective is completed
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
              total_count:
                allOf:
                  - type: integer
                    description: The total number of objectives
                    example: 25
        examples:
          example:
            value:
              data:
                - objectives_id: o12345
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
              total_count: 25
        description: Successfully retrieved objectives
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