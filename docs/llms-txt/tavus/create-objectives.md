# Source: https://docs.tavus.io/api-reference/objectives/create-objectives.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Objectives

> This endpoint creates a new objective for a persona. Objectives provide goal-oriented instructions that help guide conversations toward specific achievements and desired outcomes.




## OpenAPI

````yaml post /v2/objectives
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
    post:
      tags:
        - Objectives
      summary: Create Objectives
      description: >
        This endpoint creates a new objective for a persona. Objectives provide
        goal-oriented instructions that help guide conversations toward specific
        achievements and desired outcomes.
      operationId: createObjectives
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                data:
                  type: array
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
                          set to `manual`, the user will be prompted to confirm
                          the objective completion. If set to `auto`, the LLM
                          will determine whether the objective was completed or
                          not.
                        enum:
                          - auto
                          - manual
                        default: auto
                        example: auto
                      output_variables:
                        type: array
                        description: >-
                          Optional list of variables that should be extracted or
                          collected during the objective.
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
                          new_patient_intake_process: If the patient has never been to the practice before
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
                          Optional URL that will receive notifications when the
                          objective is completed.
                        example: https://your-server.com/webhook
                    required:
                      - objective_name
                      - objective_prompt
              required:
                - data
      responses:
        '200':
          description: Objective created successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  objectives_id:
                    type: string
                    description: Unique identifier for the created objective
                    example: o12345
                  objective_name:
                    type: string
                    description: Name of the objective
                    example: New Objectives
                  status:
                    type: string
                    description: Current status of the objective
                    example: active
                  created_at:
                    type: string
                    description: ISO 8601 timestamp of when the objective was created
                    example: '2024-01-15T10:30:00Z'
        '400':
          description: Bad Request - Invalid input parameters
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    description: Error message describing the validation failure
                    example: objective_name is required
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