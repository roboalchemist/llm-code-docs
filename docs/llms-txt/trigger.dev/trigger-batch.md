# Source: https://trigger.dev/docs/management/tasks/trigger-batch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://trigger.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Trigger task batch

> Batch trigger a specific task with up to 1,000 payloads. All items in the batch run the same task.



## OpenAPI

````yaml v3-openapi POST /api/v1/tasks/{taskIdentifier}/batch
openapi: 3.1.0
info:
  title: Trigger.dev v3 REST API
  description: >-
    The REST API lets you trigger and manage runs on Trigger.dev. You can
    trigger a run, get the status of a run, and get the results of a run. 
  version: 2024-04
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0.html
servers:
  - url: https://api.trigger.dev
    description: Trigger.dev API
security: []
paths:
  /api/v1/tasks/{taskIdentifier}/batch:
    parameters:
      - $ref: '#/components/parameters/taskIdentifier'
    post:
      tags:
        - tasks
      summary: Batch trigger a specific task
      description: >-
        Batch trigger a specific task with up to 1,000 payloads. All items in
        the batch run the same task.
      operationId: batch_trigger_task_by_id_v1
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - items
              properties:
                items:
                  type: array
                  description: >-
                    An array of payloads to trigger the task with (max 1,000
                    items).
                  maxItems: 1000
                  items:
                    $ref: '#/components/schemas/TriggerTaskRequestBody'
      responses:
        '200':
          description: Batch triggered successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BatchTriggerTaskResponse'
        '400':
          description: Invalid request parameters or body
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '401':
          description: Unauthorized request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: Task not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - secretKey: []
      x-codeSamples:
        - lang: typescript
          source: |-
            import { task } from "@trigger.dev/sdk";

            export const myTask = task({
              id: "my-task",
              run: async (payload: { message: string }) => {
                console.log("Hello, world!");
              }
            });

            // Somewhere else in your code
            await myTask.batchTrigger([
              { payload: { message: "Hello, world!" } },
              { payload: { message: "Hello again!" } },
            ]);
        - lang: curl
          source: |-
            curl -X POST "https://api.trigger.dev/api/v1/tasks/my-task/batch" \
              -H "Content-Type: application/json" \
              -H "Authorization: Bearer tr_dev_1234" \
              -d '{
                    "items": [
                      { "payload": { "message": "Hello, world!" } },
                      { "payload": { "message": "Hello again!" } }
                    ]
                  }'
components:
  parameters:
    taskIdentifier:
      in: path
      name: taskIdentifier
      required: true
      schema:
        type: string
      description: The id of a task
      example: my-task
  schemas:
    TriggerTaskRequestBody:
      type: object
      properties:
        payload:
          description: The payload can include any valid JSON
        context:
          description: The context can include any valid JSON
        options:
          type: object
          properties:
            queue:
              $ref: '#/components/schemas/QueueOptions'
            concurrencyKey:
              type: string
              description: Scope the concurrency limit to a specific key.
            idempotencyKey:
              type: string
              description: >-
                An optional property that specifies the idempotency key used to
                prevent creating duplicate runs. If you provide an existing
                idempotency key, we will return the existing run ID.
            ttl:
              $ref: '#/components/schemas/TTL'
            delay:
              $ref: '#/components/schemas/Delay'
            tags:
              allOf:
                - $ref: '#/components/schemas/RunTags'
              description: >
                Tags to attach to the run. Tags can be used to filter runs in
                the dashboard and using the SDK.


                You can set up to 10 tags per run, each must be less than 128
                characters.


                We recommend prefixing tags with a namespace using an underscore
                or colon, like `user_1234567` or `org:9876543`. Stripe uses
                underscores.
            machine:
              type: string
              enum:
                - micro
                - small-1x
                - small-2x
                - medium-1x
                - medium-2x
                - large-1x
                - large-2x
              example: small-2x
              description: >-
                The machine preset to use for this run. This will override the
                task's machine preset and any defaults.
    BatchTriggerTaskResponse:
      type: object
      required:
        - batchId
        - runs
      properties:
        batchId:
          type: string
          description: The ID of the batch that was triggered
          example: batch_1234
        runs:
          type: array
          items:
            type: string
          description: An array of run IDs that were triggered
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
          example: Something went wrong
      required:
        - error
    QueueOptions:
      type: object
      properties:
        name:
          type: string
          description: >-
            You can define a shared queue and then pass the name in to your
            task.
        concurrencyLimit:
          type: integer
          minimum: 0
          maximum: 1000
          description: >-
            An optional property that specifies the maximum number of concurrent
            run executions. If this property is omitted, the task can
            potentially use up the full concurrency of an environment.
    TTL:
      type:
        - string
        - number
      description: >-
        The time-to-live for this run. If the run is not executed within this
        time, it will be removed from the queue and never execute. You can use a
        string in this format: `1h`, `1m`, `1h42m` or a number of seconds (min.
        1).
      example: 1h42m
    Delay:
      type: string
      description: >
        The delay before the task is executed. This can be a Date object, a
        string like `1h` or a date-time string.


        * "1h" - 1 hour

        * "30d" - 30 days

        * "15m" - 15 minutes

        * "2w" - 2 weeks

        * "60s" - 60 seconds

        * new Date("2025-01-01T00:00:00Z")
    RunTags:
      oneOf:
        - $ref: '#/components/schemas/RunTag'
        - type: array
          items:
            $ref: '#/components/schemas/RunTag'
          maxItems: 10
          uniqueItems: true
          example:
            - user_123456
            - product_4629101
      description: One or more tags to attach to a run. Runs can have a maximum of 10 tags.
    RunTag:
      type: string
      maxLength: 128
      description: A single run tag. Must be less than 128 characters.
      example: user_123456
  securitySchemes:
    secretKey:
      type: http
      scheme: bearer
      description: >
        Use your project-specific Secret API key. Will start with `tr_dev_`,
        `tr_prod`, `tr_stg`, etc.


        You can find your Secret API key in the API Keys section of your
        Trigger.dev project dashboard.


        Our TypeScript SDK will default to using the value of the
        `TRIGGER_SECRET_KEY` environment variable if it is set. If you are using
        the SDK in a different environment, you can set the key using the
        `configure` function.


        ```typescript

        import { configure } from "@trigger.dev/sdk";


        configure({ accessToken: "tr_dev_1234" });

        ```

````

Built with [Mintlify](https://mintlify.com).