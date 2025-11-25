# Source: https://docs.zapier.com/powered-by-zapier/managing-app-authentication/get-authentications.md

# Source: https://docs.zapier.com/powered-by-zapier/api-reference/authentications/get-authentications.md

# Source: https://docs.zapier.com/powered-by-zapier/managing-app-authentication/get-authentications.md

# Source: https://docs.zapier.com/powered-by-zapier/api-reference/authentications/get-authentications.md

# Source: https://docs.zapier.com/powered-by-zapier/managing-app-authentication/get-authentications.md

# Source: https://docs.zapier.com/powered-by-zapier/api-reference/authentications/get-authentications.md

# Get Authentications

> Fetch the available Authentications for the provided App. This will only return Authentications that are owned by the user and not those that are shared with them, since it's not possible to create Zaps with Authentications you don't own.

#### OAuth

This endpoint requires the `authentication` OAuth scope.

## OpenAPI

````yaml https://api.zapier.com/schema get /v2/authentications
paths:
  path: /v2/authentications
  method: get
  servers:
    - url: https://api.zapier.com
  request:
    security:
      - title: OAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: oauth2
              description: >-
                See our OAuth2 authentication documentation here:
                https://docs.zapier.com/powered-by-zapier/api-reference/authentication
          cookie: {}
    parameters:
      path: {}
      query:
        app:
          schema:
            - type: string
              required: true
              description: A canonical App ID, as provided by the `/apps` endpoint.
              format: uuid
        limit:
          schema:
            - type: integer
              description: >-
                Used for paginating results. Specifies the maximum number of
                items to return per page. If this value is not set, it defaults
                to 10.
        offset:
          schema:
            - type: integer
              description: Used for paginating results. Specifies the offset to use.
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              links:
                allOf:
                  - allOf:
                      - $ref: '#/components/schemas/Links'
                    description: The links object returned in paginated response bodies.
              meta:
                allOf:
                  - allOf:
                      - $ref: '#/components/schemas/BaseMeta'
                    description: The meta object returned in paginated response bodies.
              data:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/Authentication'
                    description: The Authentications present, provided they exist
            description: |-
              Base Response definition to be used in other Response Serializers.

              Be sure to include the `data` field after using this class
            refIdentifier: '#/components/schemas/AuthenticationResponse'
            requiredProperties:
              - links
              - meta
        examples:
          AuthenticationsForGoogleSheets:
            summary: Authentications for Google Sheets
            value:
              links:
                next: null
                prev: null
              meta:
                count: 1
                limit: 10
                offset: 0
              data:
                - type: authentication
                  id: example_akLLd8kB
                  app: 81f613aa-c98a-4383-a5fc-195e68647217
                  is_expired: false
                  title: Google Sheets some.user@mycompany.example
        description: ''
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              errors:
                allOf:
                  - &ref_0
                    type: array
                    items:
                      $ref: '#/components/schemas/Error'
                    description: An array of error objects.
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: &ref_1
              - errors
        examples:
          MalformedRequest.:
            summary: Malformed request.
            value:
              errors:
                - status: 400
                  code: parse_error
                  title: ParseError
                  detail: Malformed request.
                  source: null
                  meta:
                    source: ZAPIER
                    full_details:
                      message: Malformed request.
                      code: parse_error
        description: This schema can be expected for 4xx 'Malformed request.' errors
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              errors:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              errors:
                - status: 123
                  code: <string>
                  title: <string>
                  detail: <string>
                  source:
                    pointer: <string>
                    parameter: <string>
                    header: <string>
                  meta: {}
        description: 401 Response
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              errors:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              errors:
                - status: 123
                  code: <string>
                  title: <string>
                  detail: <string>
                  source:
                    pointer: <string>
                    parameter: <string>
                    header: <string>
                  meta: {}
        description: 403 Response
    '409':
      application/json:
        schemaArray:
          - type: object
            properties:
              errors:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              errors:
                - status: 123
                  code: <string>
                  title: <string>
                  detail: <string>
                  source:
                    pointer: <string>
                    parameter: <string>
                    header: <string>
                  meta: {}
        description: 409 Response
    '429':
      application/json:
        schemaArray:
          - type: object
            properties:
              errors:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              errors:
                - status: 123
                  code: <string>
                  title: <string>
                  detail: <string>
                  source:
                    pointer: <string>
                    parameter: <string>
                    header: <string>
                  meta: {}
        description: 429 Response
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              errors:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_1
        examples:
          AServerErrorOccurred.:
            summary: A server error occurred.
            value:
              errors:
                - status: 500
                  code: error
                  title: APIException
                  detail: A server error occurred.
                  source: null
                  meta:
                    source: ZAPIER
                    full_details:
                      message: A server error occurred.
                      code: error
        description: This schema can be expected for 5xx 'A server error occurred.' errors
    '503':
      application/json:
        schemaArray:
          - type: object
            properties:
              errors:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              errors:
                - status: 123
                  code: <string>
                  title: <string>
                  detail: <string>
                  source:
                    pointer: <string>
                    parameter: <string>
                    header: <string>
                  meta: {}
        description: 503 Response
  deprecated: false
  type: path
components:
  schemas:
    Apps:
      type: object
      description: An app that integrates with Zapier
      properties:
        id:
          type: string
          description: Unique id of the app
        type:
          type: string
          default: app
          description: The type of this object.
        image:
          type: string
          description: Default image/icon to represent the app.
        links:
          type: object
          additionalProperties: {}
          description: >-
            A url that, when visited, will direct the user to authenticate with
            the app and allow Zapier access to the app, thus creating a new
            Authentication.

                        If value is `null`, then no authentication is required to use the app.
        action_types:
          type: array
          items: {}
          description: A list of action types for this specific App
        title:
          type: string
          description: Human readable name of the app
        images:
          allOf:
            - $ref: '#/components/schemas/AppsImages'
          description: The URL of images (of various sizes) for this specific App
        hex_color:
          type: string
          description: A branded color that can be used to represent the app.
        categories:
          type: array
          items:
            $ref: '#/components/schemas/Category'
          description: >-
            A list of categories to which this app belongs. Helpful in
            identifying apps by type and functionality.
        description:
          type: string
          description: Human readable description of the app.
      required:
        - action_types
        - categories
        - description
        - hex_color
        - id
        - image
        - images
        - links
        - title
    AppsImages:
      type: object
      description: Images/icons of various resolutions to represent the app.
      properties:
        url_16x16:
          type: string
          description: 16x16 resolution image URL
        url_32x32:
          type: string
          description: 32x32 resolution image URL
        url_64x64:
          type: string
          description: 64x64 resolution image URL
        url_128x128:
          type: string
          description: 128x128 resolution image URL
      required:
        - url_128x128
        - url_16x16
        - url_32x32
        - url_64x64
    Authentication:
      type: object
      description: >-
        An Authentication contains various fields, often credentials such as API
        tokens, used to access Partner APIs on

        behalf of a user. The actual fields are held securely by Zapier
      properties:
        type:
          allOf:
            - $ref: '#/components/schemas/AuthenticationTypeEnum'
          readOnly: true
          default: authentication
          description: |-
            The type of this object.

            * `authentication` - authentication
        id:
          type: string
          description: The identifier for this specific Authentication
        app:
          description: An app that integrates with Zapier.
          oneOf:
            - $ref: '#/components/schemas/Apps'
            - type: string
        is_expired:
          type: boolean
          description: >-
            If `true`, this Authentication has expired. It will not be usable,
            and the user needs to be directed to reconnect it.
        title:
          type: string
          description: The title of this specific Authentication
      required:
        - app
        - id
        - is_expired
        - title
        - type
    AuthenticationTypeEnum:
      enum:
        - authentication
      type: string
      description: '* `authentication` - authentication'
    BaseMeta:
      type: object
      description: The meta object returned in paginated response bodies.
      properties:
        count:
          type: integer
          minimum: 0
          description: >-
            The total number of objects in the collection represented by the
            endpoint.
        limit:
          type:
            - integer
            - 'null'
          minimum: 1
          description: The limit value used in the request.
        offset:
          type: integer
          minimum: 0
          default: 0
          description: The offset value used in the request.
      required:
        - count
        - limit
    Category:
      type: object
      description: Category an app belongs to.
      properties:
        slug:
          type: string
          description: The shortened slug name for this category
      required:
        - slug
    Error:
      type: object
      description: Base Error definition
      properties:
        status:
          type: integer
          description: The HTTP status code applicable to this problem.
        code:
          type: string
          description: A unique identifier for this particular occurrence of the problem.
        title:
          type: string
          description: A short summary of the problem.
        detail:
          type: string
          description: >-
            A human-readable explanation specific to this occurrence of the
            problem.
        source:
          oneOf:
            - $ref: '#/components/schemas/ErrorSource'
            - type: 'null'
          description: An object containing references to the primary source of the error.
        meta:
          type:
            - object
            - 'null'
          additionalProperties: {}
          description: Freeform metadata about the error
    ErrorSource:
      type: object
      description: Populates the `source` object inside our error responses.
      properties:
        pointer:
          type: string
          description: >-
            Pointer to the value in the request document that caused the error
            e.g. `/actions`.
        parameter:
          type: string
          description: A string indicating which URI query parameter caused the error.
        header:
          type: string
          description: >-
            A string indicating the name of a single request header which caused
            the error.
    Links:
      type: object
      description: The links object returned in paginated response bodies.
      properties:
        next:
          type:
            - string
            - 'null'
          description: The URL of the next page of paginated results.
        prev:
          type:
            - string
            - 'null'
          description: The URL of the previous page of paginated results.

````