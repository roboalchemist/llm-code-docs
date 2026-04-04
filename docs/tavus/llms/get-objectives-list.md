# Source: https://docs.tavus.io/api-reference/objectives/get-objectives-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Objectives

> This endpoint returns a list of all objectives.




## OpenAPI

````yaml get /v2/objectives
openapi: 3.0.3
info:
  title: Tavus Developer API Collection
  version: 1.0.0
  contact: {}
servers:
  - url: https://tavusapi.com
security:
  - apiKey: []
tags:
  - name: Videos
  - name: Replicas
  - name: Conversations
  - name: Personas
  - name: Replacements
  - name: Transcriptions
  - name: Documents
paths:
  /v2/objectives:
    get:
      tags:
        - Objectives
      summary: Get Objectives
      description: |
        This endpoint returns a list of all objectives.
      operationId: getObjectives
      parameters:
        - in: query
          name: limit
          schema:
            type: integer
          description: The number of objectives to return per page. Default is 10.
        - in: query
          name: page
          schema:
            type: integer
          description: The page number to return. Default is 1.
      responses:
        '200':
          description: Successfully retrieved objectives
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
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
                    type: integer
                    description: The total number of objectives
                    example: 25
        '401':
          description: UNAUTHORIZED
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    description: The error message.
                    example: Invalid access token
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: apiKey
      in: header
      name: x-api-key

````