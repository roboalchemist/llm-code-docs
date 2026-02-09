# Source: https://docs.tavus.io/api-reference/objectives/get-objectives.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Objective

> This endpoint returns a single objective by its unique identifier.




## OpenAPI

````yaml get /v2/objectives/{objectives_id}
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
  /v2/objectives/{objectives_id}:
    parameters:
      - name: objectives_id
        in: path
        required: true
        description: The unique identifier of the objective.
        schema:
          type: string
          example: o12345
    get:
      tags:
        - Objectives
      summary: Get Objective
      description: |
        This endpoint returns a single objective by its unique identifier.
      operationId: getObjective
      parameters:
        - name: objectives_id
          in: path
          required: true
          description: The unique identifier of the objective.
          schema:
            type: string
            example: o12345
      responses:
        '200':
          description: Successfully retrieved objective
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
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
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message.
                    example: Invalid objectives_id
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
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message.
                    example: Objective not found
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: apiKey
      in: header
      name: x-api-key

````