# Source: https://braintrust.dev/docs/api-reference/functions/invoke-function.md

# Invoke function

> Invoke a function.



## OpenAPI

````yaml openapi.yaml post /v1/function/{function_id}/invoke
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
  /v1/function/{function_id}/invoke:
    post:
      tags:
        - Functions
      summary: Invoke function
      description: Invoke a function.
      operationId: postFunctionIdInvoke
      parameters:
        - $ref: '#/components/parameters/FunctionIdParam'
      requestBody:
        description: Function invocation parameters
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/InvokeApi'
      responses:
        '200':
          description: Function invocation response
          content:
            application/json:
              schema:
                nullable: true
      security:
        - bearerAuth: []
        - {}
components:
  parameters:
    FunctionIdParam:
      schema:
        $ref: '#/components/schemas/FunctionIdParam'
      required: true
      description: Function id
      name: function_id
      in: path
  schemas:
    InvokeApi:
      type: object
      properties:
        input:
          nullable: true
          description: Argument to the function, which can be any JSON serializable value
        expected:
          nullable: true
          description: The expected output of the function
        metadata:
          type: object
          nullable: true
          additionalProperties:
            nullable: true
          description: >-
            Any relevant metadata. This will be logged and available as the
            `metadata` argument.
        tags:
          type: array
          nullable: true
          items:
            type: string
          description: Any relevant tags to log on the span.
        messages:
          type: array
          items:
            $ref: '#/components/schemas/ChatCompletionMessageParam'
          description: If the function is an LLM, additional messages to pass along to it
        parent:
          $ref: '#/components/schemas/InvokeParent'
        stream:
          type: boolean
          nullable: true
          description: >-
            Whether to stream the response. If true, results will be returned in
            the Braintrust SSE format.
        mode:
          $ref: '#/components/schemas/StreamingMode'
        strict:
          type: boolean
          nullable: true
          description: >-
            If true, throw an error if one of the variables in the prompt is not
            present in the input
        mcp_auth:
          type: object
          additionalProperties:
            type: object
            properties:
              oauth_token:
                type: string
                description: The OAuth token to use
          description: Map of MCP server URL to auth credentials
        version:
          type: string
          description: The version of the function
      description: The request to invoke a function
    FunctionIdParam:
      type: string
      format: uuid
      description: Function id
    ChatCompletionMessageParam:
      anyOf:
        - type: object
          properties:
            content:
              anyOf:
                - type: string
                  default: ''
                  title: text
                - type: array
                  items:
                    $ref: '#/components/schemas/ChatCompletionContentPartText'
                  title: array
            role:
              type: string
              enum:
                - system
            name:
              type: string
          required:
            - role
          title: system
        - type: object
          properties:
            content:
              anyOf:
                - type: string
                  default: ''
                  title: text
                - type: array
                  items:
                    $ref: '#/components/schemas/ChatCompletionContentPart'
                  title: array
            role:
              type: string
              enum:
                - user
            name:
              type: string
          required:
            - role
          title: user
        - type: object
          properties:
            role:
              type: string
              enum:
                - assistant
            content:
              anyOf:
                - type: string
                - type: array
                  items:
                    $ref: '#/components/schemas/ChatCompletionContentPartText'
                - type: 'null'
            function_call:
              type: object
              nullable: true
              properties:
                arguments:
                  type: string
                name:
                  type: string
              required:
                - arguments
                - name
            name:
              type: string
              nullable: true
            tool_calls:
              type: array
              nullable: true
              items:
                $ref: '#/components/schemas/ChatCompletionMessageToolCall'
            reasoning:
              type: array
              nullable: true
              items:
                $ref: '#/components/schemas/ChatCompletionMessageReasoning'
          required:
            - role
          title: assistant
        - type: object
          properties:
            content:
              anyOf:
                - type: string
                  default: ''
                  title: text
                - type: array
                  items:
                    $ref: '#/components/schemas/ChatCompletionContentPartText'
                  title: array
            role:
              type: string
              enum:
                - tool
            tool_call_id:
              type: string
              default: ''
          required:
            - role
          title: tool
        - type: object
          properties:
            content:
              type: string
              nullable: true
            name:
              type: string
            role:
              type: string
              enum:
                - function
          required:
            - content
            - name
            - role
          title: function
        - type: object
          properties:
            content:
              anyOf:
                - type: string
                  default: ''
                  title: text
                - type: array
                  items:
                    $ref: '#/components/schemas/ChatCompletionContentPartText'
                  title: array
            role:
              type: string
              enum:
                - developer
            name:
              type: string
          required:
            - role
          title: developer
        - type: object
          properties:
            role:
              type: string
              enum:
                - model
            content:
              type: string
              nullable: true
          required:
            - role
          title: fallback
    InvokeParent:
      anyOf:
        - type: object
          properties:
            object_type:
              type: string
              enum:
                - project_logs
                - experiment
                - playground_logs
            object_id:
              type: string
              description: The id of the container object you are logging to
            row_ids:
              type: object
              nullable: true
              properties:
                id:
                  type: string
                  description: The id of the row
                span_id:
                  type: string
                  description: The span_id of the row
                root_span_id:
                  type: string
                  description: The root_span_id of the row
              required:
                - id
                - span_id
                - root_span_id
              description: Identifiers for the row to to log a subspan under
            propagated_event:
              type: object
              nullable: true
              additionalProperties:
                nullable: true
              description: Include these properties in every span created under this parent
          required:
            - object_type
            - object_id
          description: Span parent properties
          title: span_parent_struct
        - type: string
          description: >-
            The parent's span identifier, created by calling `.export()` on a
            span
      description: Options for tracing the function call
    StreamingMode:
      type: string
      nullable: true
      enum:
        - auto
        - parallel
        - null
      description: The mode format of the returned value (defaults to 'auto')
    ChatCompletionContentPartText:
      type: object
      properties:
        text:
          type: string
          default: ''
        type:
          type: string
          enum:
            - text
        cache_control:
          type: object
          properties:
            type:
              type: string
              enum:
                - ephemeral
          required:
            - type
      required:
        - type
    ChatCompletionContentPart:
      anyOf:
        - $ref: '#/components/schemas/ChatCompletionContentPartTextWithTitle'
        - $ref: '#/components/schemas/ChatCompletionContentPartImageWithTitle'
        - $ref: '#/components/schemas/ChatCompletionContentPartFileWithTitle'
      title: chat_completion_content_part
    ChatCompletionMessageToolCall:
      type: object
      properties:
        id:
          type: string
        function:
          type: object
          properties:
            arguments:
              type: string
            name:
              type: string
          required:
            - arguments
            - name
        type:
          type: string
          enum:
            - function
      required:
        - id
        - function
        - type
    ChatCompletionMessageReasoning:
      type: object
      properties:
        id:
          type: string
          nullable: true
        content:
          type: string
          nullable: true
      description: >-
        Note: This is not part of the OpenAI API spec, but we added it for
        interoperability with multiple reasoning models.
    ChatCompletionContentPartTextWithTitle:
      type: object
      properties:
        text:
          type: string
          default: ''
        type:
          type: string
          enum:
            - text
        cache_control:
          type: object
          properties:
            type:
              type: string
              enum:
                - ephemeral
          required:
            - type
      required:
        - type
      title: text
    ChatCompletionContentPartImageWithTitle:
      type: object
      properties:
        image_url:
          type: object
          properties:
            url:
              type: string
            detail:
              anyOf:
                - type: string
                  enum:
                    - auto
                  title: auto
                - type: string
                  enum:
                    - low
                  title: low
                - type: string
                  enum:
                    - high
                  title: high
          required:
            - url
        type:
          type: string
          enum:
            - image_url
      required:
        - image_url
        - type
      title: image_url
    ChatCompletionContentPartFileWithTitle:
      type: object
      properties:
        file:
          $ref: '#/components/schemas/ChatCompletionContentPartFileFile'
        type:
          type: string
          enum:
            - file
      required:
        - file
        - type
      title: file
    ChatCompletionContentPartFileFile:
      type: object
      properties:
        file_data:
          type: string
        filename:
          type: string
        file_id:
          type: string
          title: The ID of an uploaded file to use as input.
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt