# Source: https://docs.lunary.ai/docs/api/runs/get-a-specific-run.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a specific run

> Retrieve detailed information about a specific run by its ID.



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/runs/{id}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/runs/{id}:
    get:
      tags:
        - Runs
      summary: Get a specific run
      description: Retrieve detailed information about a specific run by its ID.
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Run'
        '404':
          description: Run not found
components:
  schemas:
    Run:
      type: object
      properties:
        id:
          type: string
        projectId:
          type: string
        isPublic:
          type: boolean
        feedback:
          $ref: '#/components/schemas/Feedback'
        parentFeedback:
          $ref: '#/components/schemas/Feedback'
        type:
          type: string
        name:
          type: string
        createdAt:
          type: string
          format: date-time
        endedAt:
          type: string
          format: date-time
        duration:
          type: number
        templateVersionId:
          type: string
        templateSlug:
          type: string
        cost:
          type: number
        tokens:
          type: object
          properties:
            completion:
              type: number
            prompt:
              type: number
            total:
              type: number
        tags:
          type: array
          items:
            type: string
        input:
          type: object
        output:
          type: object
        error:
          type: object
        status:
          type: string
        siblingRunId:
          type: string
        params:
          type: object
        metadata:
          type: object
        firstMessage:
          type: object
          description: First message captured in the conversation thread, when available.
        messagesCount:
          type: integer
          description: Total number of messages within the conversation thread.
        user:
          type: object
          properties:
            id:
              type: string
            externalId:
              type: string
            createdAt:
              type: string
              format: date-time
            lastSeen:
              type: string
              format: date-time
            props:
              type: object
        traceId:
          type: string
    Feedback:
      type: object
      properties:
        score:
          type: number
        flags:
          type: array
          items:
            type: string
        comment:
          type: string

````