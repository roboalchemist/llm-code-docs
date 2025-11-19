# Source: https://trigger.dev/docs/management/tasks/trigger.md

# Trigger

> Trigger a task by its identifier.

## OpenAPI

````yaml v3-openapi POST /api/v1/tasks/{taskIdentifier}/trigger
paths:
  path: /api/v1/tasks/{taskIdentifier}/trigger
  method: post
  servers:
    - url: https://api.trigger.dev
      description: Trigger.dev API
  request:
    security:
      - title: secretKey
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >
                Use your project-specific Secret API key. Will start with
                `tr_dev_`, `tr_prod`, `tr_stg`, etc.


                You can find your Secret API key in the API Keys section of your
                Trigger.dev project dashboard.


                Our TypeScript SDK will default to using the value of the
                `TRIGGER_SECRET_KEY` environment variable if it is set. If you
                are using the SDK in a different environment, you can set the
                key using the `configure` function.


                ```typescript

                import { configure } from "@trigger.dev/sdk";


                configure({ accessToken: "tr_dev_1234" });

                ```
          cookie: {}
    parameters:
      path:
        taskIdentifier:
          schema:
            - type: string
              required: true
              description: The id of a task
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              payload:
                allOf:
                  - description: The payload can include any valid JSON
              context:
                allOf:
                  - description: The context can include any valid JSON
              options:
                allOf:
                  - type: object
                    properties:
                      queue:
                        $ref: '#/components/schemas/QueueOptions'
                      concurrencyKey:
                        type: string
                        description: Scope the concurrency limit to a specific key.
                      idempotencyKey:
                        type: string
                        description: >-
                          An optional property that specifies the idempotency
                          key used to prevent creating duplicate runs. If you
                          provide an existing idempotency key, we will return
                          the existing run ID.
                      ttl:
                        $ref: '#/components/schemas/TTL'
                      delay:
                        $ref: '#/components/schemas/Delay'
                      tags:
                        type:
                          - array
                          - string
                        example:
                          - user_123456
                          - product_4629101
                        description: >
                          Tags to attach to the run. Tags can be used to filter
                          runs in the dashboard and using the SDK.


                          You can set up to 5 tags per run, they must be less
                          than 64 characters each.


                          We recommend prefixing tags with a namespace using an
                          underscore or colon, like `user_1234567` or
                          `org:9876543`. Stripe uses underscores.
                        items:
                          type: string
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
                          The machine preset to use for this run. This will
                          override the task's machine preset and any defaults.
            required: true
            refIdentifier: '#/components/schemas/TriggerTaskRequestBody'
        examples:
          example:
            value:
              payload: <any>
              context: <any>
              options:
                queue:
                  name: <string>
                  concurrencyLimit: 500
                concurrencyKey: <string>
                idempotencyKey: <string>
                ttl: 1h42m
                delay: <string>
                tags:
                  - user_123456
                  - product_4629101
                machine: small-2x
    codeSamples:
      - lang: typescript
        source: |-
          import { task } from "@trigger.dev/sdk";

          export const myTask = await task({
            id: "my-task",
            run: async (payload: { message: string }) => {
              console.log("Hello, world!");
            }
          });

          // Somewhere else in your code
          await myTask.trigger({ message: "Hello, world!" }, {
            idempotencyKey: "unique-key-123",
            concurrencyKey: "user123-task",
            queue: {
              name: "my-task-queue",
              concurrencyLimit: 5
            },
          });
      - lang: curl
        source: |-
          curl -X POST "https://api.trigger.dev/api/v1/tasks/my-task/trigger" \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer tr_dev_1234" \
            -d '{
                  "payload": {
                    "message": "Hello, world!"
                  },
                  "context": {
                    "user": "user123"
                  },
                  "options": {
                    "queue": {
                      "name": "default",
                      "concurrencyLimit": 5
                    },
                    "concurrencyKey": "user123-task",
                    "idempotencyKey": "unique-key-123"
                  }
                }'
      - lang: python
        source: |-
          import requests

          url = "https://api.trigger.dev/api/v1/tasks/my-task/trigger"
          headers = {
              "Content-Type": "application/json",
              "Authorization": "Bearer tr_dev_1234"
          }
          data = {
              "payload": {
                  "message": "Hello, world!"
              },
              "context": {
                  "user": "user123"
              },
              "options": {
                  "queue": {
                      "name": "default",
                      "concurrencyLimit": 5
                  },
                  "concurrencyKey": "user123-task",
                  "idempotencyKey": "unique-key-123"
              }
          }

          response = requests.post(url, headers=headers, json=data)
          print(response.json())
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    description: The ID of the run that was triggered.
                    example: run_1234
            refIdentifier: '#/components/schemas/TriggerTaskResponse'
        examples:
          example:
            value:
              id: run_1234
        description: Task triggered successfully
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_0
                    type: string
                    example: Something went wrong
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: &ref_1
              - error
        examples:
          example:
            value:
              error: Something went wrong
        description: Invalid request parameters or body
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              error: Something went wrong
        description: Unauthorized request
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              error: Something went wrong
        description: Resource not found
  deprecated: false
  type: path
components:
  schemas:
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

````