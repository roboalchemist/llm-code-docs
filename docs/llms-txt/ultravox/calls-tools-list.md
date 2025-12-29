# Source: https://docs.ultravox.ai/api-reference/calls/calls-tools-list.md

# List Call Tools

> Returns all tools that were available at any point during the call



## OpenAPI

````yaml get /api/calls/{call_id}/tools
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/calls/{call_id}/tools:
    get:
      tags:
        - calls
      operationId: calls_tools_list
      parameters:
        - in: path
          name: call_id
          schema:
            type: string
            format: uuid
          required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/CallTool'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    CallTool:
      type: object
      properties:
        callToolId:
          type: string
          format: uuid
          readOnly: true
        toolId:
          type: string
          format: uuid
          readOnly: true
          nullable: true
        name:
          type: string
          readOnly: true
          description: The possibly overridden name of the tool.
        definition:
          $ref: '#/components/schemas/ultravox.v1.CallTool'
      required:
        - callToolId
        - definition
        - name
        - toolId
    ultravox.v1.CallTool:
      type: object
      properties:
        description:
          type: string
          description: The description of the tool.
        dynamicParameters:
          type: array
          items:
            $ref: '#/components/schemas/ultravox.v1.DynamicParameter'
          description: The parameters presented to the model.
        staticParameters:
          type: array
          items:
            $ref: '#/components/schemas/ultravox.v1.StaticParameter'
          description: Parameters added unconditionally when the tool is invoked.
        automaticParameters:
          type: array
          items:
            $ref: '#/components/schemas/ultravox.v1.AutomaticParameter'
          description: Parameters automatically set by the system.
        timeout:
          pattern: ^-?(?:0|[1-9][0-9]{0,11})(?:\.[0-9]{1,9})?s$
          type: string
          description: >-
            The maximum amount of time the tool is allowed for execution. The
            conversation is frozen
             while tools run, so prefer sticking to the default unless you're comfortable with that
             consequence. If your tool is too slow for the default and can't be made faster, still try to
             keep this timeout as low as possible.
        precomputable:
          type: boolean
          description: >-
            The tool is guaranteed to be non-mutating, repeatable, and free of
            side-effects. Such tools
             can safely be executed speculatively, reducing their effective latency. However, the fact they
             were called may not be reflected in the call history if their result ends up unused.
        http:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.HttpCallToolDetails'
          description: Details for an HTTP tool.
        client:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.ClientCallToolDetails'
          description: >-
            Details for a client-implemented tool. Only body parameters are
            allowed
             for client tools.
        dataConnection:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.DataConnectionCallToolDetails'
          description: Details for invoking a tool via a data connection.
        defaultReaction:
          enum:
            - AGENT_REACTION_UNSPECIFIED
            - AGENT_REACTION_SPEAKS
            - AGENT_REACTION_LISTENS
            - AGENT_REACTION_SPEAKS_ONCE
          type: string
          description: >-
            Indicates the default for how the agent should proceed after the
            tool is invoked.
             Can be overridden by the tool implementation via the X-Ultravox-Agent-Reaction
             header.
          format: enum
        staticResponse:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.StaticToolResponse'
          description: >-
            Static response to a tool. When this is used, this response will be
            returned
             without waiting for the tool's response.
      description: A tool as used for a particular call (omitting auth details).
    ultravox.v1.DynamicParameter:
      type: object
      properties:
        name:
          type: string
          description: The name of the parameter.
        location:
          enum:
            - PARAMETER_LOCATION_UNSPECIFIED
            - PARAMETER_LOCATION_QUERY
            - PARAMETER_LOCATION_PATH
            - PARAMETER_LOCATION_HEADER
            - PARAMETER_LOCATION_BODY
          type: string
          description: Where the parameter is used.
          format: enum
        schema:
          type: object
          description: |-
            The JsonSchema definition of the parameter. This typically
             includes things like type, description, enum values, format,
             other restrictions, etc.
        required:
          type: boolean
          description: Whether the parameter is required.
      description: A dynamic parameter the tool accepts that may be set by the model.
    ultravox.v1.StaticParameter:
      type: object
      properties:
        name:
          type: string
          description: The name of the parameter.
        location:
          enum:
            - PARAMETER_LOCATION_UNSPECIFIED
            - PARAMETER_LOCATION_QUERY
            - PARAMETER_LOCATION_PATH
            - PARAMETER_LOCATION_HEADER
            - PARAMETER_LOCATION_BODY
          type: string
          description: Where the parameter is used.
          format: enum
        value:
          allOf:
            - $ref: '#/components/schemas/google.protobuf.Value'
          description: The value of the parameter.
      description: >-
        A static parameter that is unconditionally added when the tool is
        invoked. This
         parameter is not exposed to or set by the model.
    ultravox.v1.AutomaticParameter:
      type: object
      properties:
        name:
          type: string
          description: The name of the parameter.
        location:
          enum:
            - PARAMETER_LOCATION_UNSPECIFIED
            - PARAMETER_LOCATION_QUERY
            - PARAMETER_LOCATION_PATH
            - PARAMETER_LOCATION_HEADER
            - PARAMETER_LOCATION_BODY
          type: string
          description: Where the parameter is used.
          format: enum
        knownValue:
          enum:
            - KNOWN_PARAM_UNSPECIFIED
            - KNOWN_PARAM_CALL_ID
            - KNOWN_PARAM_CONVERSATION_HISTORY
            - KNOWN_PARAM_OUTPUT_SAMPLE_RATE
            - KNOWN_PARAM_CALL_STATE
            - KNOWN_PARAM_CALL_STAGE_ID
          type: string
          description: The value to set for the parameter.
          format: enum
      description: A parameter that is automatically set by the system.
    ultravox.v1.HttpCallToolDetails:
      type: object
      properties:
        baseUrlPattern:
          type: string
          description: >-
            The base URL pattern for the tool, possibly with placeholders for
            path parameters.
        httpMethod:
          type: string
          description: The HTTP method for the tool.
        authHeaders:
          type: array
          items:
            type: string
          description: Auth headers added when the tool is invoked.
        authQueryParams:
          type: array
          items:
            type: string
          description: Auth query parameters added when the tool is invoked.
        callTokenScopes:
          type: array
          items:
            type: string
          description: >-
            If the tool requires a call token, the scopes that must be present
            in the token.
             If this is empty, no call token will be created.
      description: Details for a CallTool implemented via HTTP requests.
    ultravox.v1.ClientCallToolDetails:
      type: object
      properties: {}
      description: Details for a CallTool implemented by the client.
    ultravox.v1.DataConnectionCallToolDetails:
      type: object
      properties: {}
      description: Details for invoking a tool via a data connection.
    ultravox.v1.StaticToolResponse:
      type: object
      properties:
        responseText:
          type: string
          description: The predefined text response to be returned immediately
      description: >-
        A predefined, static response for a tool. When a tool has a static
        response, it
         can be returned immediately, without waiting for full tool execution.
    google.protobuf.Value:
      description: >-
        Represents a dynamically typed value which can be either null, a number,
        a string, a boolean, a recursive struct value, or a list of values.
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.ultravox.ai/llms.txt