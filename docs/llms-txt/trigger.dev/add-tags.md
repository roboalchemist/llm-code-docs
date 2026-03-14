# Source: https://trigger.dev/docs/management/runs/add-tags.md

> ## Documentation Index
> Fetch the complete documentation index at: https://trigger.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add tags to a run

> Adds one or more tags to a run. Runs can have a maximum of 10 tags. Duplicate tags are ignored.



## OpenAPI

````yaml v3-openapi POST /api/v1/runs/{runId}/tags
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
  /api/v1/runs/{runId}/tags:
    parameters:
      - $ref: '#/components/parameters/runId'
    post:
      tags:
        - runs
      summary: Add tags to a run
      description: >-
        Adds one or more tags to a run. Runs can have a maximum of 10 tags.
        Duplicate tags are ignored.
      operationId: add_run_tags_v1
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - tags
              properties:
                tags:
                  $ref: '#/components/schemas/RunTags'
      responses:
        '200':
          description: Successful request
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Successfully set 2 new tags.
        '400':
          description: Invalid request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
        '401':
          description: Unauthorized request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    enum:
                      - Invalid or Missing API Key
        '422':
          description: Too many tags
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: Runs can only have 10 tags.
      security:
        - secretKey: []
      x-codeSamples:
        - lang: typescript
          label: SDK
          source: |-
            import { runs } from "@trigger.dev/sdk";

            await runs.addTags("run_1234", ["tag-1", "tag-2"]);
        - lang: typescript
          label: Fetch
          source: |-
            await fetch("https://api.trigger.dev/api/v1/runs/run_1234/tags", {
              method: "POST",
              headers: {
                "Authorization": `Bearer ${process.env.TRIGGER_SECRET_KEY}`,
                "Content-Type": "application/json",
              },
              body: JSON.stringify({ tags: ["tag-1", "tag-2"] }),
            });
components:
  parameters:
    runId:
      in: path
      name: runId
      required: true
      schema:
        type: string
      description: >
        The ID of an run, starts with `run_`. The run ID will be returned when
        you trigger a run on a task.
      example: run_1234
  schemas:
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