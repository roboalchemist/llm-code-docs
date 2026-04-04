# Source: https://docs.ultravox.ai/api-reference/tools/tools-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ultravox.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List Tools

> Retrieves all available tools



## OpenAPI

````yaml get /api/tools
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/tools:
    get:
      tags:
        - tools
      description: List all tools in your account.
      operationId: tools_list
      parameters:
        - name: cursor
          required: false
          in: query
          description: The pagination cursor value.
          schema:
            type: string
        - in: query
          name: ownership
          schema:
            type: string
          description: The ownership used to filter results
        - name: pageSize
          required: false
          in: query
          description: Number of results to return per page.
          schema:
            type: integer
        - in: query
          name: search
          schema:
            type: string
          description: The search string used to filter results
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaginatedToolList'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    PaginatedToolList:
      type: object
      required:
        - results
      properties:
        next:
          type: string
          nullable: true
          format: uri
          example: http://api.example.org/accounts/?cursor=cD00ODY%3D"
        previous:
          type: string
          nullable: true
          format: uri
          example: http://api.example.org/accounts/?cursor=cj0xJnA9NDg3
        results:
          type: array
          items:
            $ref: '#/components/schemas/Tool'
        total:
          type: integer
          example: 123
    Tool:
      type: object
      properties:
        toolId:
          type: string
          format: uuid
          readOnly: true
        name:
          type: string
          maxLength: 40
        created:
          type: string
          format: date-time
          readOnly: true
        definition:
          $ref: '#/components/schemas/ultravox.v1.BaseToolDefinition'
        ownership:
          allOf:
            - $ref: '#/components/schemas/OwnershipEnum'
          readOnly: true
      required:
        - created
        - definition
        - name
        - ownership
        - toolId
    ultravox.v1.BaseToolDefinition:
      type: object
      properties:
        modelToolName:
          type: string
          description: >-
            The name of the tool, as presented to the model. Must match
            ^[a-zA-Z0-9_-]{1,64}$.
        description:
          type: string
          description: The description of the tool.
        dynamicParameters:
          type: array
          items:
            $ref: '#/components/schemas/ultravox.v1.DynamicParameter'
          description: The parameters that the tool accepts.
        staticParameters:
          type: array
          items:
            $ref: '#/components/schemas/ultravox.v1.StaticParameter'
          description: The static parameters added when the tool is invoked.
        automaticParameters:
          type: array
          items:
            $ref: '#/components/schemas/ultravox.v1.AutomaticParameter'
          description: >-
            Additional parameters that are automatically set by the system when
            the tool is invoked.
        requirements:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.ToolRequirements'
          description: >-
            Requirements that must be fulfilled when creating a call for the
            tool to be used.
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
            - $ref: '#/components/schemas/ultravox.v1.BaseHttpToolDetails'
          description: Details for an HTTP tool.
        client:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.BaseClientToolDetails'
          description: >-
            Details for a client-implemented tool. Only body parameters are
            allowed
             for client tools.
        dataConnection:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.BaseDataConnectionToolDetails'
          description: >-
            Details for a tool implemented via a data connection websocket. Only
            body
             parameters are allowed for data connection tools.
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
      description: >-
        The base definition of a tool that can be used during a call. Exactly
        one
         implementation (http or client) should be set.
    OwnershipEnum:
      enum:
        - public
        - private
      type: string
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
    ultravox.v1.ToolRequirements:
      type: object
      properties:
        httpSecurityOptions:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.SecurityOptions'
          description: Security requirements for an HTTP tool.
        requiredParameterOverrides:
          type: array
          items:
            type: string
          description: >-
            Dynamic parameters that must be overridden with an explicit (static)
            value.
      description: >-
        The requirements for using a tool, which must be satisfied when creating
        a call with the tool.
    ultravox.v1.BaseHttpToolDetails:
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
      description: Details for invoking a tool via HTTP.
    ultravox.v1.BaseClientToolDetails:
      type: object
      properties: {}
      description: Details for invoking a tool expected to be implemented by the client.
    ultravox.v1.BaseDataConnectionToolDetails:
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
    ultravox.v1.SecurityOptions:
      type: object
      properties:
        options:
          type: array
          items:
            $ref: '#/components/schemas/ultravox.v1.SecurityRequirements'
          description: >-
            The options for security. Only one must be met. The first one that
            can be
             satisfied will be used in general. The single exception to this rule is
             that we always prefer a non-empty set of requirements over an empty set
             unless no non-empty set can be satisfied.
      description: The different options for satisfying a tool's security requirements.
    ultravox.v1.SecurityRequirements:
      type: object
      properties:
        requirements:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/ultravox.v1.SecurityRequirement'
          description: Requirements keyed by name.
        ultravoxCallTokenRequirement:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.UltravoxCallTokenRequirement'
          description: >-
            An additional special security requirement that can be automatically
            fulfilled
             during call creation. If a tool has this requirement set, a token identifying
             the call and relevant scopes will be created during call creation and set as
             an X-Ultravox-Call-Token header when the tool is invoked.
             Such tokens are only verifiable by the Ultravox service and primarily exist
             for built-in tools (though it's possible for third-party tools that wrap a
             built-in tool to make use of them as well).
      description: The security requirements for a request. All requirements must be met.
    ultravox.v1.SecurityRequirement:
      type: object
      properties:
        queryApiKey:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.QueryApiKeyRequirement'
          description: An API key must be added to the query string.
        headerApiKey:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.HeaderApiKeyRequirement'
          description: An API key must be added to a custom header.
        httpAuth:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.HttpAuthRequirement'
          description: The HTTP authentication header must be added.
      description: >-
        A single security requirement that must be met for a tool to be
        available. Exactly one
         of query_api_key, header_api_key, or http_auth should be set.
    ultravox.v1.UltravoxCallTokenRequirement:
      type: object
      properties:
        scopes:
          type: array
          items:
            type: string
          description: The scopes that must be present in the token.
      description: >-
        A security requirement that will automatically be fulfilled during call
        creation.
         The generated token will be set as an X-Ultravox-Call-Token header when the tool
         is invoked. The token is only verifiable by the Ultravox service and should not be
         used for authentication by any other service.
         The token will also be invalid as soon as the call is completed.
    ultravox.v1.QueryApiKeyRequirement:
      type: object
      properties:
        name:
          type: string
          description: The name of the query parameter.
      description: >-
        A security requirement that will cause an API key to be added to the
        query string.
    ultravox.v1.HeaderApiKeyRequirement:
      type: object
      properties:
        name:
          type: string
          description: The name of the header.
      description: >-
        A security requirement that will cause an API key to be added to the
        header.
    ultravox.v1.HttpAuthRequirement:
      type: object
      properties:
        scheme:
          type: string
          description: The scheme of the HTTP authentication, e.g. "Bearer".
      description: >-
        A security requirement that will cause an HTTP authentication header to
        be added.
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````