# Source: https://trigger.dev/docs/management/runs/update-metadata.md

# Update metadata

> Update the metadata of a run.

## OpenAPI

````yaml v3-openapi PUT /api/v1/runs/{runId}/metadata
paths:
  path: /api/v1/runs/{runId}/metadata
  method: put
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
        runId:
          schema:
            - type: string
              required: true
              description: >
                The ID of an run, starts with `run_`. The run ID will be
                returned when you trigger a run on a task.
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              metadata:
                allOf:
                  - type: object
                    description: The new metadata to set on the run.
                    example:
                      key: value
            required: true
        examples:
          example:
            value:
              metadata:
                key: value
    codeSamples:
      - label: Save metadata
        lang: typescript
        source: |-
          import { metadata, task } from "@trigger.dev/sdk";

          export const myTask = task({
            id: "my-task",
            run: async () => {
              await metadata.save({ key: "value" });
            }
          });
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              metadata:
                allOf:
                  - type: object
                    description: The updated metadata of the run.
        examples:
          example:
            value:
              metadata: {}
        description: Successful request
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    enum:
                      - Invalid or missing run ID
                      - Invalid metadata
        examples:
          example:
            value:
              error: Invalid or missing run ID
        description: Invalid request
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    enum:
                      - Invalid or Missing API key
        examples:
          example:
            value:
              error: Invalid or Missing API key
        description: Unauthorized request
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    enum:
                      - Task Run not found
        examples:
          example:
            value:
              error: Task Run not found
        description: Resource not found
  deprecated: false
  type: path
components:
  schemas: {}

````