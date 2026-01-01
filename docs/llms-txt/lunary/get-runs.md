# Source: https://docs.lunary.ai/docs/api/runs/get-runs.md

# Get runs

> The Runs API endpoint allows you to retrieve data about specific runs from your Lunary application.

The most common run types are 'llm', 'agent', 'chain', 'tool', 'thread' and 'chat'.

It supports various filters to narrow down the results according to your needs.

This endpoint supports GET requests and expects query parameters for filtering the results.




## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/runs
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/runs:
    get:
      tags:
        - Runs
      summary: Get runs
      description: >
        The Runs API endpoint allows you to retrieve data about specific runs
        from your Lunary application.


        The most common run types are 'llm', 'agent', 'chain', 'tool', 'thread'
        and 'chat'.


        It supports various filters to narrow down the results according to your
        needs.


        This endpoint supports GET requests and expects query parameters for
        filtering the results.
      parameters:
        - in: query
          name: type
          schema:
            type: string
            enum:
              - llm
              - trace
              - thread
        - in: query
          name: search
          schema:
            type: string
        - in: query
          name: models
          schema:
            type: array
            items:
              type: string
        - in: query
          name: tags
          schema:
            type: array
            items:
              type: string
        - in: query
          name: tokens
          schema:
            type: string
        - in: query
          name: exportType
          schema:
            type: string
            enum:
              - csv
              - jsonl
        - in: query
          name: minDuration
          schema:
            type: string
        - in: query
          name: maxDuration
          schema:
            type: string
        - in: query
          name: startTime
          schema:
            type: string
        - in: query
          name: endTime
          schema:
            type: string
        - in: query
          name: parentRunId
          schema:
            type: string
        - in: query
          name: limit
          schema:
            type: string
        - in: query
          name: page
          schema:
            type: string
        - in: query
          name: order
          schema:
            type: string
        - in: query
          name: sortField
          schema:
            type: string
        - in: query
          name: sortDirection
          schema:
            type: string
            enum:
              - asc
              - desc
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: number
                  page:
                    type: number
                  limit:
                    type: number
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/Run'
              example:
                total: 200
                page: 1
                limit: 10
                data:
                  - type: llm
                    name: gpt-5
                    createdAt: '2025-10-01T12:00:00Z'
                    endedAt: '2025-10-01T12:00:03Z'
                    duration: 3
                    tokens:
                      completion: 100
                      prompt: 50
                      total: 150
                    feedback: null
                    status: success
                    tags:
                      - example
                    templateSlug: example-template
                    templateVersionId: 1234
                    input:
                      - role: user
                        content: Hello world!
                    output:
                      - role: assistant
                        content: Hello. How are you?
                    error: null
                    user:
                      id: '11111111'
                      externalId: user123
                      createdAt: '2021-12-01T12:00:00Z'
                      lastSeen: '2022-01-01T12:00:00Z'
                      props:
                        name: Jane Doe
                        email: user1@apple.com
                    cost: 0.05
                    params:
                      temperature: 0.5
                      maxTokens: 100
                      tools: []
                    metadata: null
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt