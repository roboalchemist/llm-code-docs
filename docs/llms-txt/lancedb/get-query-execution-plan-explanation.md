# Source: https://docs.lancedb.com/api-reference/rest/table/get-query-execution-plan-explanation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lancedb.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get query execution plan explanation

> Get the query execution plan for a query against table `id`.
Returns a human-readable explanation of how the query will be executed.

REST NAMESPACE ONLY
REST namespace returns the response as a plain string
instead of the `ExplainTableQueryPlanResponse` JSON object.




## OpenAPI

````yaml api-reference/rest/openapi.yml post /v1/table/{id}/explain_plan
openapi: 3.1.1
info:
  title: Lance Namespace Specification
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0.html
  version: 1.0.0
  description: >
    This OpenAPI specification is a part of the Lance namespace specification.
    It contains 2 parts:


    The `components/schemas`, `components/responses`, `components/examples`,
    `tags` sections define

    the request and response shape for each operation in a Lance Namespace
    across all implementations.

    See https://lance.org/format/namespace/operations for more details.


    The `servers`, `security`, `paths`, `components/parameters` sections are for
    the 

    Lance REST Namespace implementation, which defines a complete REST server
    that can work with Lance datasets.

    See https://lance.org/format/namespace/rest for more details.
servers:
  - url: '{scheme}://{host}:{port}/{basePath}'
    description: Generic server URL with all parts configurable
    variables:
      scheme:
        default: http
      host:
        default: localhost
      port:
        default: '2333'
      basePath:
        default: ''
  - url: '{scheme}://{host}/{basePath}'
    description: Server URL when the port can be inferred from the scheme
    variables:
      scheme:
        default: http
      host:
        default: localhost
      basePath:
        default: ''
security:
  - OAuth2: []
  - BearerAuth: []
  - ApiKeyAuth: []
tags:
  - name: Namespace
    description: |
      Operations that are related to a namespace
  - name: Table
    description: |
      Operations that are related to a table
  - name: Index
    description: |
      Operations that are related to an index
  - name: Tag
    description: |
      Operations that are related to tags
  - name: Transaction
    description: |
      Operations that are related to a transaction
  - name: Metadata
    description: >
      Operations that only interact with object metadata and should be
      computationally lightweight
  - name: Data
    description: >
      Operations that interact with object data and might be computationally
      intensive
paths:
  /v1/table/{id}/explain_plan:
    parameters:
      - $ref: '#/components/parameters/id'
      - $ref: '#/components/parameters/delimiter'
    post:
      tags:
        - Table
        - Data
      summary: Get query execution plan explanation
      description: |
        Get the query execution plan for a query against table `id`.
        Returns a human-readable explanation of how the query will be executed.

        REST NAMESPACE ONLY
        REST namespace returns the response as a plain string
        instead of the `ExplainTableQueryPlanResponse` JSON object.
      operationId: ExplainTableQueryPlan
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ExplainTableQueryPlanRequest'
      responses:
        '200':
          $ref: '#/components/responses/ExplainTableQueryPlanResponse'
        '400':
          $ref: '#/components/responses/BadRequestErrorResponse'
        '401':
          $ref: '#/components/responses/UnauthorizedErrorResponse'
        '403':
          $ref: '#/components/responses/ForbiddenErrorResponse'
        '404':
          $ref: '#/components/responses/NotFoundErrorResponse'
        '503':
          $ref: '#/components/responses/ServiceUnavailableErrorResponse'
        5XX:
          $ref: '#/components/responses/ServerErrorResponse'
components:
  parameters:
    id:
      name: id
      description: >
        `string identifier` of an object in a namespace, following the Lance
        Namespace spec.

        When the value is equal to the delimiter, it represents the root
        namespace.

        For example, `v1/namespace/$/list` performs a `ListNamespace` on the
        root namespace.
      in: path
      required: true
      schema:
        type: string
    delimiter:
      name: delimiter
      description: >
        An optional delimiter of the `string identifier`, following the Lance
        Namespace spec.

        When not specified, the `$` delimiter must be used.
      in: query
      required: false
      schema:
        type: string
  schemas:
    ExplainTableQueryPlanRequest:
      type: object
      required:
        - query
      properties:
        identity:
          $ref: '#/components/schemas/Identity'
        context:
          $ref: '#/components/schemas/Context'
        id:
          type: array
          items:
            type: string
        query:
          $ref: '#/components/schemas/QueryTableRequest'
        verbose:
          type: boolean
          default: false
          description: Whether to return verbose explanation
    Identity:
      type: object
      description: |
        Identity information of a request.
      properties:
        api_key:
          type: string
          description: |
            API key for authentication.

            REST NAMESPACE ONLY
            This is passed via the `x-api-key` header.
        auth_token:
          type: string
          description: |
            Bearer token for authentication.

            REST NAMESPACE ONLY
            This is passed via the `Authorization` header
            with the Bearer scheme (e.g., `Bearer <token>`).
    Context:
      type: object
      description: >
        Arbitrary context for a request as key-value pairs.

        How to use the context is custom to the specific implementation.


        REST NAMESPACE ONLY

        Context entries are passed via HTTP headers using the naming convention

        `x-lance-ctx-<key>: <value>`. For example, a context entry

        `{"trace_id": "abc123"}` would be sent as the header
        `x-lance-ctx-trace_id: abc123`.
      additionalProperties:
        type: string
    QueryTableRequest:
      type: object
      required:
        - vector
        - k
      properties:
        identity:
          $ref: '#/components/schemas/Identity'
        context:
          $ref: '#/components/schemas/Context'
        id:
          type: array
          items:
            type: string
        bypass_vector_index:
          type: boolean
          description: Whether to bypass vector index
        columns:
          type: object
          nullable: true
          description: >
            Optional columns to return. Provide either column_names or
            column_aliases, not both.
          properties:
            column_names:
              type: array
              items:
                type: string
              description: List of column names to return
            column_aliases:
              type: object
              additionalProperties:
                type: string
              description: Object mapping output aliases to source column names
        distance_type:
          type: string
          description: Distance metric to use
        ef:
          type: integer
          minimum: 0
          description: Search effort parameter for HNSW index
        fast_search:
          type: boolean
          description: Whether to use fast search
        filter:
          type: string
          description: Optional SQL filter expression
        full_text_query:
          type: object
          nullable: true
          description: >-
            Optional full-text search query. Provide either string_query or
            structured_query, not both.
          properties:
            string_query:
              $ref: '#/components/schemas/StringFtsQuery'
            structured_query:
              $ref: '#/components/schemas/StructuredFtsQuery'
        k:
          type: integer
          minimum: 0
          description: Number of results to return
        lower_bound:
          type: number
          format: float
          description: Lower bound for search
        nprobes:
          type: integer
          minimum: 0
          description: Number of probes for IVF index
        offset:
          type: integer
          minimum: 0
          description: Number of results to skip
        prefilter:
          type: boolean
          description: Whether to apply filtering before vector search
        refine_factor:
          type: integer
          format: int32
          minimum: 0
          description: Refine factor for search
        upper_bound:
          type: number
          format: float
          description: Upper bound for search
        vector:
          type: object
          nullable: true
          description: >-
            Query vector(s) for similarity search. Provide either single_vector
            or multi_vector, not both.
          properties:
            single_vector:
              type: array
              items:
                type: number
                format: float
              description: Single query vector
            multi_vector:
              type: array
              items:
                type: array
                items:
                  type: number
                  format: float
              description: Multiple query vectors for batch search
        vector_column:
          type: string
          description: Name of the vector column to search
        version:
          type: integer
          format: int64
          minimum: 0
          description: Table version to query
        with_row_id:
          type: boolean
          description: If true, return the row id as a column called `_rowid`
    ErrorResponse:
      type: object
      description: Common JSON error response model
      required:
        - code
      properties:
        error:
          type: string
          description: A brief, human-readable message about the error.
          example: Table 'users' not found in namespace 'production'
        code:
          type: integer
          minimum: 0
          description: |
            Lance Namespace error code identifying the error type.

            Error codes:
              0 - Unsupported: Operation not supported by this backend
              1 - NamespaceNotFound: The specified namespace does not exist
              2 - NamespaceAlreadyExists: A namespace with this name already exists
              3 - NamespaceNotEmpty: Namespace contains tables or child namespaces
              4 - TableNotFound: The specified table does not exist
              5 - TableAlreadyExists: A table with this name already exists
              6 - TableIndexNotFound: The specified table index does not exist
              7 - TableIndexAlreadyExists: A table index with this name already exists
              8 - TableTagNotFound: The specified table tag does not exist
              9 - TableTagAlreadyExists: A table tag with this name already exists
              10 - TransactionNotFound: The specified transaction does not exist
              11 - TableVersionNotFound: The specified table version does not exist
              12 - TableColumnNotFound: The specified table column does not exist
              13 - InvalidInput: Malformed request or invalid parameters
              14 - ConcurrentModification: Optimistic concurrency conflict
              15 - PermissionDenied: User lacks permission for this operation
              16 - Unauthenticated: Authentication credentials are missing or invalid
              17 - ServiceUnavailable: Service is temporarily unavailable
              18 - Internal: Unexpected server/implementation error
              19 - InvalidTableState: Table is in an invalid state for the operation
              20 - TableSchemaValidationError: Table schema validation failed
          example: 4
        detail:
          type: string
          description: >
            An optional human-readable explanation of the error.

            This can be used to record additional information such as stack
            trace.
          example: The table may have been dropped or renamed
        instance:
          type: string
          description: >
            A string that identifies the specific occurrence of the error.

            This can be a URI, a request or response ID,

            or anything that the implementation can recognize to trace specific
            occurrence of the error.
          example: /v1/table/production$users/describe
    StringFtsQuery:
      type: object
      required:
        - query
      properties:
        columns:
          type: array
          items:
            type: string
        query:
          type: string
    StructuredFtsQuery:
      type: object
      required:
        - query
      properties:
        query:
          $ref: '#/components/schemas/FtsQuery'
    FtsQuery:
      type: object
      description: >
        Full-text search query. Exactly one query type field must be provided.

        This structure follows the same pattern as AlterTransactionAction to
        minimize

        differences and compatibility issues across codegen in different
        languages.
      properties:
        match:
          $ref: '#/components/schemas/MatchQuery'
        phrase:
          $ref: '#/components/schemas/PhraseQuery'
        boost:
          $ref: '#/components/schemas/BoostQuery'
        multi_match:
          $ref: '#/components/schemas/MultiMatchQuery'
        boolean:
          $ref: '#/components/schemas/BooleanQuery'
    MatchQuery:
      type: object
      required:
        - terms
      properties:
        boost:
          type: number
          format: float
        column:
          type: string
        fuzziness:
          type: integer
          format: int32
          minimum: 0
        max_expansions:
          type: integer
          description: |-
            The maximum number of terms to expand for fuzzy matching.
            Default to 50.
          minimum: 0
        operator:
          $ref: '#/components/schemas/Operator'
          description: |-
            The operator to use for combining terms.
            This can be either `And` or `Or`, it's 'Or' by default.
            - `And`: All terms must match.
            - `Or`: At least one term must match.
        prefix_length:
          type: integer
          format: int32
          description: >-
            The number of beginning characters being unchanged for fuzzy
            matching.

            Default to 0.
          minimum: 0
        terms:
          type: string
    PhraseQuery:
      type: object
      required:
        - terms
      properties:
        column:
          type: string
        slop:
          type: integer
          format: int32
          minimum: 0
        terms:
          type: string
    BoostQuery:
      type: object
      description: >-
        Boost query that scores documents matching positive query higher and
        negative query lower
      required:
        - positive
        - negative
      properties:
        positive:
          $ref: '#/components/schemas/FtsQuery'
        negative:
          $ref: '#/components/schemas/FtsQuery'
        negative_boost:
          type: number
          format: float
          description: 'Boost factor for negative query (default: 0.5)'
          default: 0.5
    MultiMatchQuery:
      type: object
      required:
        - match_queries
      properties:
        match_queries:
          type: array
          items:
            $ref: '#/components/schemas/MatchQuery'
    BooleanQuery:
      type: object
      description: Boolean query with must, should, and must_not clauses
      required:
        - should
        - must
        - must_not
      properties:
        must:
          type: array
          items:
            $ref: '#/components/schemas/FtsQuery'
          description: Queries that must match (AND)
        must_not:
          type: array
          items:
            $ref: '#/components/schemas/FtsQuery'
          description: Queries that must not match (NOT)
        should:
          type: array
          items:
            $ref: '#/components/schemas/FtsQuery'
          description: Queries that should match (OR)
    Operator:
      type: string
      description: >
        The operator to use for combining terms.

        Case insensitive, supports both PascalCase and snake_case. Valid values
        are:

        - And: All terms must match.

        - Or: At least one term must match.
  responses:
    ExplainTableQueryPlanResponse:
      description: Query execution plan explanation
      content:
        application/json:
          schema:
            type: string
            description: Human-readable query execution plan
    BadRequestErrorResponse:
      description: >-
        Indicates a bad request error. It could be caused by an unexpected
        request body format or other forms of request validation failure, such
        as invalid json. Usually serves application/json content, although in
        some cases simple text/plain content might be returned by the server's
        middleware.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          example:
            type: /errors/bad-request
            title: Malformed request
            status: 400
            detail: ''
            instance: /v1/namespaces
    UnauthorizedErrorResponse:
      description: >-
        Unauthorized. The request lacks valid authentication credentials for the
        operation.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          example:
            type: /errors/unauthorized-request
            title: No valid authentication credentials for the operation
            status: 401
            detail: ''
            instance: /v1/namespaces
    ForbiddenErrorResponse:
      description: Forbidden. Authenticated user does not have the necessary permissions.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          example:
            type: /errors/forbidden-request
            title: Not authorized to make this request
            status: 403
            detail: ''
            instance: /v1/namespaces
    NotFoundErrorResponse:
      description: A server-side problem that means can not find the specified resource.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          example:
            type: /errors/not-found-error
            title: Not found Error
            status: 404
            detail: ''
            instance: /v1/namespaces/{ns}
    ServiceUnavailableErrorResponse:
      description: >-
        The service is not ready to handle the request. The client should wait
        and retry. The service may additionally send a Retry-After header to
        indicate when to retry.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          example:
            type: /errors/service-unavailable
            title: Slow down
            status: 503
            detail: ''
            instance: /v1/namespaces
    ServerErrorResponse:
      description: >-
        A server-side problem that might not be addressable from the client
        side. Used for server 5xx errors without more specific documentation in
        individual routes.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          example:
            type: /errors/server-error
            title: Internal Server Error
            status: 500
            detail: ''
            instance: /v1/namespaces
  securitySchemes:
    OAuth2:
      type: oauth2
      flows:
        clientCredentials:
          tokenUrl: /oauth/token
          scopes: {}
    BearerAuth:
      type: http
      scheme: bearer
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-api-key

````