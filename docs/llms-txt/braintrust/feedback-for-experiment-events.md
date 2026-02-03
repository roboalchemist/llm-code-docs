# Source: https://braintrust.dev/docs/api-reference/experiments/feedback-for-experiment-events.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Feedback for experiment events

> Log feedback for a set of experiment events



## OpenAPI

````yaml openapi.yaml post /v1/experiment/{experiment_id}/feedback
openapi: 3.1.1
info:
  version: 1.0.0
  title: Braintrust API
  description: >-
    API specification for the backend data server. The API is hosted globally at

    https://api.braintrust.dev or in your own environment.


    You can access the OpenAPI spec for this API at
    https://github.com/braintrustdata/braintrust-openapi.
  license:
    name: Apache 2.0
servers:
  - url: https://api.braintrust.dev
security:
  - bearerAuth: []
  - {}
paths:
  /v1/experiment/{experiment_id}/feedback:
    post:
      tags:
        - Experiments
      summary: Feedback for experiment events
      description: Log feedback for a set of experiment events
      operationId: postExperimentIdFeedback
      parameters:
        - $ref: '#/components/parameters/ExperimentIdParam'
      requestBody:
        description: An array of feedback objects
        required: false
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/FeedbackExperimentEventRequest'
      responses:
        '200':
          description: Returns a success status
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FeedbackResponseSchema'
        '400':
          description: >-
            The request was unacceptable, often due to missing a required
            parameter
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '401':
          description: No valid API key provided
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '403':
          description: The API key doesn’t have permissions to perform the request
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '429':
          description: >-
            Too many requests hit the API too quickly. We recommend an
            exponential backoff of your requests
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '500':
          description: Something went wrong on Braintrust's end. (These are rare.)
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
      security:
        - bearerAuth: []
        - {}
components:
  parameters:
    ExperimentIdParam:
      schema:
        $ref: '#/components/schemas/ExperimentIdParam'
      required: true
      description: Experiment id
      name: experiment_id
      in: path
  schemas:
    FeedbackExperimentEventRequest:
      type: object
      properties:
        feedback:
          type: array
          items:
            $ref: '#/components/schemas/FeedbackExperimentItem'
          description: A list of experiment feedback items
      required:
        - feedback
    FeedbackResponseSchema:
      type: object
      properties:
        status:
          type: string
          enum:
            - success
      required:
        - status
    ExperimentIdParam:
      type: string
      format: uuid
      description: Experiment id
    FeedbackExperimentItem:
      type: object
      properties:
        id:
          type: string
          description: >-
            The id of the experiment event to log feedback for. This is the row
            `id` returned by `POST /v1/experiment/{experiment_id}/insert`
        scores:
          type: object
          nullable: true
          additionalProperties:
            type: number
            nullable: true
            minimum: 0
            maximum: 1
          description: >-
            A dictionary of numeric values (between 0 and 1) to log. These
            scores will be merged into the existing scores for the experiment
            event
        expected:
          nullable: true
          description: >-
            The ground truth value (an arbitrary, JSON serializable object) that
            you'd compare to `output` to determine if your `output` value is
            correct or not
        comment:
          type: string
          nullable: true
          description: An optional comment string to log about the experiment event
        metadata:
          type: object
          nullable: true
          additionalProperties:
            nullable: true
          description: >-
            A dictionary with additional data about the feedback. If you have a
            `user_id`, you can log it here and access it in the Braintrust UI.
            Note, this metadata does not correspond to the main event itself,
            but rather the audit log attached to the event.
        source:
          type: string
          nullable: true
          enum:
            - app
            - api
            - external
            - null
          description: >-
            The source of the feedback. Must be one of "external" (default),
            "app", or "api"
        tags:
          type: array
          nullable: true
          items:
            type: string
          description: A list of tags to log
      required:
        - id
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API key or JWT
      description: >-
        Most Braintrust endpoints are authenticated by providing your API key as
        a header `Authorization: Bearer [api_key]` to your HTTP request. You can
        create an API key in the Braintrust [organization settings
        page](https://www.braintrustdata.com/app/settings?subroute=api-keys).

````