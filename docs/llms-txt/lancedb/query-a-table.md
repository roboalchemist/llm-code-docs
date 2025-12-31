# Source: https://docs.lancedb.com/api-reference/rest/table/query-a-table.md

# Query a table

> Query table `id` with vector search, full text search and optional SQL filtering.
Returns results in Arrow IPC file or stream format.

REST NAMESPACE ONLY
REST namespace returns the response as Arrow IPC file binary data
instead of the `QueryTableResponse` JSON object.




## OpenAPI

````yaml api-reference/rest/openapi.yml post /v1/table/{id}/query
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
  /v1/table/{id}/query:
    parameters:
      - $ref: '#/components/parameters/id'
      - $ref: '#/components/parameters/delimiter'
    post:
      tags:
        - Table
        - Data
      summary: Query a table
      description: >
        Query table `id` with vector search, full text search and optional SQL
        filtering.

        Returns results in Arrow IPC file or stream format.


        REST NAMESPACE ONLY

        REST namespace returns the response as Arrow IPC file binary data

        instead of the `QueryTableResponse` JSON object.
      operationId: QueryTable
      requestBody:
        description: Query request
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/QueryTableRequest'
        required: true
      responses:
        '200':
          $ref: '#/components/responses/QueryTableResponse'
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
    QueryTableRequest:
      type: object
      required:
        - vector
        - k
      properties:
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
    ErrorResponse:
      type: object
      description: Common JSON error response model
      properties:
        error:
          type: string
          description: a brief, human-readable message about the error
          example: Incorrect username or password
        code:
          type: integer
          minimum: 400
          maximum: 600
          description: >
            HTTP style response code, where 4XX represents client side errors 

            and 5XX represents server side errors.


            For implementations that uses HTTP (e.g. REST namespace),

            this field can be optional in favor of the HTTP response status
            code.

            In case both values exist and do not match, the HTTP response status
            code should be used.
          example: 404
        type:
          type: string
          description: |
            An optional type identifier string for the error.
            This allows the implementation to specify their internal error type,
            which could be more detailed than the HTTP standard status code.
          example: /errors/incorrect-user-pass
        detail:
          type: string
          description: |
            an optional human-readable explanation of the error.
            This can be used to record information such as stack trace.
          example: Authentication failed due to incorrect username or password
        instance:
          type: string
          description: >
            a string that identifies the specific occurrence of the error.

            This can be a URI, a request or response ID, 

            or anything that the implementation can recognize to trace specific
            occurrence of the error.
          example: /login/log/abc123
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
    QueryTableResponse:
      description: Query results in Arrow IPC file format
      content:
        application/vnd.apache.arrow.file:
          schema:
            type: string
            format: binary
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lancedb.com/llms.txt