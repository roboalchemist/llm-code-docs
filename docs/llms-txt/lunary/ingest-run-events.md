# Source: https://docs.lunary.ai/docs/api/runs/ingest-run-events.md

# Ingest run events

> This endpoint is for reporting data from platforms not supported by our SDKs.

You can use either your project's Public or Private Key as the Bearer token in the Authorization header.

The expected body is an array of Event objects.

For LLM calls, you would first track a `start` event with the `input` data.
Once your LLM call succeeds, you would need to send an `end` event to the API endpoint with the `output` data from the LLM call.

For a full step-by-step guide on sending LLM data to the Lunary API, see the [Custom Integration](/docs/integrations/custom) guide.




## OpenAPI

````yaml https://api.lunary.ai/v1/openapi post /v1/runs/ingest
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/runs/ingest:
    post:
      tags:
        - Runs
      summary: Ingest run events
      description: >
        This endpoint is for reporting data from platforms not supported by our
        SDKs.


        You can use either your project's Public or Private Key as the Bearer
        token in the Authorization header.


        The expected body is an array of Event objects.


        For LLM calls, you would first track a `start` event with the `input`
        data.

        Once your LLM call succeeds, you would need to send an `end` event to
        the API endpoint with the `output` data from the LLM call.


        For a full step-by-step guide on sending LLM data to the Lunary API, see
        the [Custom Integration](/docs/integrations/custom) guide.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                events:
                  oneOf:
                    - $ref: '#/components/schemas/Event'
                    - type: array
                      items:
                        $ref: '#/components/schemas/Event'
            example:
              events:
                - type: llm
                  event: start
                  runId: some-unique-id
                  name: gpt-4
                  timestamp: '2022-01-01T00:00:00Z'
                  input:
                    - role: user
                      content: Hello world!
                  tags:
                    - tag1
                  extra:
                    temperature: 0.5
                    max_tokens: 100
      responses:
        '200':
          description: Successful ingestion
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/IngestResponse'
              example:
                results:
                  - id: some-unique-id
                    success: true
        '401':
          description: Project does not exist
        '402':
          description: Incorrect project id format
      security:
        - BearerAuth: []
components:
  schemas:
    Event:
      type: object
      description: >-
        Represents an event in the Lunary API for tracking LLM calls and related
        operations.
      properties:
        type:
          type: string
          enum:
            - llm
            - chain
            - agent
            - tool
            - log
            - embed
            - retriever
            - chat
            - convo
            - message
            - thread
          description: The type of event being reported.
        event:
          type: string
          description: The specific event name (e.g., "start" or "end").
        level:
          type: string
          description: The logging level of the event.
        runId:
          type: string
          description: A unique identifier for the run.
        parentRunId:
          type: string
          description: The ID of the parent run, if applicable.
        timestamp:
          type: string
          format: date-time
          description: The time the event occurred.
        input:
          type: object
          description: >-
            The input data for the event, typically in OpenAI chat message
            format.
        tags:
          type: array
          items:
            type: string
          description: Tags associated with the event.
        name:
          type: string
          description: The name of the event or model.
        output:
          type: object
          description: >-
            The output data from the event, typically in OpenAI chat message
            format.
        message:
          oneOf:
            - type: string
            - type: object
          description: A message associated with the event.
        extra:
          type: object
          description: Additional data such as temperature, max_tokens, tools, etc.
        feedback:
          type: object
          description: Feedback data for the event.
        templateId:
          type: string
          description: The ID of the template used, if applicable.
        templateVersionId:
          type: string
          description: The version ID of the template used, if applicable.
        metadata:
          type: object
          description: Additional metadata for the event.
        tokensUsage:
          type: object
          properties:
            prompt:
              type: number
              description: The number of tokens used in the prompt.
            completion:
              type: number
              description: The number of tokens used in the completion.
        error:
          type: object
          properties:
            message:
              type: string
              description: The error message, if an error occurred.
            stack:
              type: string
              description: The error stack trace, if available.
        appId:
          type: string
          description: The ID of the application or project.
      additionalProperties: true
      example:
        type: llm
        event: start
        runId: some-unique-id
        name: gpt-4
        timestamp: '2022-01-01T00:00:00Z'
        input:
          - role: user
            content: Hello world!
        tags:
          - tag1
        extra:
          temperature: 0.5
          max_tokens: 100
    IngestResponse:
      type: object
      description: The response from the ingestion API.
      properties:
        results:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
                description: The ID of the ingested event.
              success:
                type: boolean
                description: Indicates if the ingestion was successful.
              error:
                type: string
                description: Error message if the ingestion failed.
      example:
        results:
          - id: some-unique-id
            success: true
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt