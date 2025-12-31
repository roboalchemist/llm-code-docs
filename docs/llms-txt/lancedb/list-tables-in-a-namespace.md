# Source: https://docs.lancedb.com/api-reference/rest/namespace/list-tables-in-a-namespace.md

# List tables in a namespace

> List all child table names of the parent namespace `id`.

REST NAMESPACE ONLY
REST namespace uses GET to perform this operation without a request body.
It passes in the `ListTablesRequest` information in the following way:
- `id`: pass through path parameter of the same name
- `page_token`: pass through query parameter of the same name
- `limit`: pass through query parameter of the same name




## OpenAPI

````yaml api-reference/rest/openapi.yml get /v1/namespace/{id}/table/list
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
  /v1/namespace/{id}/table/list:
    parameters:
      - $ref: '#/components/parameters/id'
      - $ref: '#/components/parameters/delimiter'
      - $ref: '#/components/parameters/page_token'
      - $ref: '#/components/parameters/limit'
    get:
      tags:
        - Namespace
        - Table
        - Metadata
      summary: List tables in a namespace
      description: >
        List all child table names of the parent namespace `id`.


        REST NAMESPACE ONLY

        REST namespace uses GET to perform this operation without a request
        body.

        It passes in the `ListTablesRequest` information in the following way:

        - `id`: pass through path parameter of the same name

        - `page_token`: pass through query parameter of the same name

        - `limit`: pass through query parameter of the same name
      operationId: ListTables
      responses:
        '200':
          $ref: '#/components/responses/ListTablesResponse'
        '400':
          $ref: '#/components/responses/BadRequestErrorResponse'
        '401':
          $ref: '#/components/responses/UnauthorizedErrorResponse'
        '403':
          $ref: '#/components/responses/ForbiddenErrorResponse'
        '404':
          $ref: '#/components/responses/NotFoundErrorResponse'
        '406':
          $ref: '#/components/responses/UnsupportedOperationErrorResponse'
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
    page_token:
      name: page_token
      description: Pagination token from a previous request
      in: query
      required: false
      schema:
        $ref: '#/components/schemas/PageToken'
    limit:
      name: limit
      description: Maximum number of items to return
      in: query
      required: false
      schema:
        $ref: '#/components/schemas/PageLimit'
  responses:
    ListTablesResponse:
      description: A list of tables
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ListTablesResponse'
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
    UnsupportedOperationErrorResponse:
      description: >-
        Not Acceptable / Unsupported Operation. The server does not support this
        operation.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          example:
            type: /errors/unsupported-operation
            title: The server does not support this operation
            status: 406
            detail: ''
            instance: /v1/namespaces
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
  schemas:
    PageToken:
      description: >
        An opaque token that allows pagination for list operations (e.g.
        ListNamespaces).


        For an initial request of a list operation, 

        if the implementation cannot return all items in one response,

        or if there are more items than the page limit specified in the request,

        the implementation must return a page token in the response,

        indicating there are more results available.


        After the initial request, 

        the value of the page token from each response must be used

        as the page token value for the next request.


        Caller must interpret either `null`, 

        missing value or empty string value of the page token from

        the implementation's response as the end of the listing results.
      type: string
      nullable: true
    PageLimit:
      description: |
        An inclusive upper bound of the 
        number of results that a caller will receive.
      type: integer
      nullable: true
    ListTablesResponse:
      type: object
      required:
        - tables
      properties:
        tables:
          type: array
          uniqueItems: true
          description: >
            The list of names of all the tables under the connected namespace
            implementation.

            This should recursively list all the tables in all child namespaces.

            Each string in the list is the full identifier in string form.
          items:
            type: string
        page_token:
          $ref: '#/components/schemas/PageToken'
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