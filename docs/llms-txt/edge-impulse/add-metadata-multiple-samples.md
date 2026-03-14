# Source: https://docs.edgeimpulse.com/apis/studio/raw-data/add-metadata-multiple-samples.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add metadata (multiple samples)

> Add specific metadata for multiple samples.



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/raw-data/batch/add-metadata
openapi: 3.0.0
info:
  title: Edge Impulse API
  version: 1.0.0
servers:
  - url: https://studio.edgeimpulse.com/v1
security:
  - ApiKeyAuthentication: []
  - JWTAuthentication: []
  - JWTHttpHeaderAuthentication: []
  - OAuth2: []
paths:
  /api/{projectId}/raw-data/batch/add-metadata:
    post:
      tags:
        - Raw data
      summary: Add metadata (multiple samples)
      description: Add specific metadata for multiple samples.
      operationId: batchAddMetadata
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/RawDataCategoryQueryParameter'
        - $ref: '#/components/parameters/FiltersLabelsParameter'
        - $ref: '#/components/parameters/FiltersFilenameParameter'
        - $ref: '#/components/parameters/FiltersMaxLengthParameter'
        - $ref: '#/components/parameters/FiltersMinLengthParameter'
        - $ref: '#/components/parameters/FiltersMinFrequencyParameter'
        - $ref: '#/components/parameters/FiltersMaxFrequencyParameter'
        - $ref: '#/components/parameters/FiltersSignatureParameter'
        - $ref: '#/components/parameters/FiltersDisabledParameter'
        - $ref: '#/components/parameters/FiltersIdsParameter'
        - $ref: '#/components/parameters/FiltersExcludeIdsParameter'
        - $ref: '#/components/parameters/FiltersMinLabelParameter'
        - $ref: '#/components/parameters/FiltersMaxLabelParameter'
        - $ref: '#/components/parameters/SearchQueryParameter'
        - $ref: '#/components/parameters/FiltersDataTypeParameter'
        - $ref: '#/components/parameters/FiltersMinIdParameter'
        - $ref: '#/components/parameters/FiltersMaxIdParameter'
        - $ref: '#/components/parameters/FiltersMetadataParameter'
        - $ref: '#/components/parameters/FiltersMinDateParameter'
        - $ref: '#/components/parameters/FiltersMaxDateParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/BatchAddMetadataRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                anyOf:
                  - $ref: '#/components/schemas/GenericApiResponse'
                  - $ref: '#/components/schemas/StartJobResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    RawDataCategoryQueryParameter:
      name: category
      in: query
      required: true
      description: Which of the three acquisition categories to retrieve data from
      schema:
        $ref: '#/components/schemas/RawDataFilterCategory'
    FiltersLabelsParameter:
      name: labels
      in: query
      required: false
      description: >-
        Only include samples with a label within the given list of labels, given
        as a JSON string
      schema:
        example: '["idle", "snake"]'
        type: string
    FiltersFilenameParameter:
      name: filename
      in: query
      required: false
      description: Only include samples whose filename includes the given filename
      schema:
        type: string
    FiltersMaxLengthParameter:
      name: maxLength
      in: query
      required: false
      description: Only include samples shorter than the given length, in milliseconds
      schema:
        type: integer
    FiltersMinLengthParameter:
      name: minLength
      in: query
      required: false
      description: Only include samples longer than the given length, in milliseconds
      schema:
        type: integer
    FiltersMinFrequencyParameter:
      name: minFrequency
      in: query
      required: false
      description: >-
        Only include samples with higher frequency than given frequency, in
        hertz
      schema:
        type: number
    FiltersMaxFrequencyParameter:
      name: maxFrequency
      in: query
      required: false
      description: Only include samples with lower frequency than given frequency, in hertz
      schema:
        type: number
    FiltersSignatureParameter:
      name: signatureValidity
      in: query
      required: false
      description: Include samples with either valid or invalid signatures
      schema:
        type: string
        enum:
          - both
          - valid
          - invalid
    FiltersDisabledParameter:
      name: includeDisabled
      in: query
      required: false
      description: Include only enabled or disabled samples (or both)
      schema:
        type: string
        enum:
          - both
          - enabled
          - disabled
    FiltersIdsParameter:
      name: ids
      in: query
      required: false
      description: >-
        Only include samples with an ID within the given list of IDs, given as a
        JSON string
      schema:
        example: '[1, 2, 3]'
        type: string
    FiltersExcludeIdsParameter:
      name: excludeIds
      in: query
      required: false
      description: >-
        Exclude samples with an ID within the given list of IDs, given as a JSON
        string
      schema:
        example: '[4, 5, 6]'
        type: string
    FiltersMinLabelParameter:
      name: minLabel
      in: query
      required: false
      description: Only include samples with a label >= this value
      schema:
        type: number
    FiltersMaxLabelParameter:
      name: maxLabel
      in: query
      required: false
      description: Only include samples with a label < this value
      schema:
        type: number
    SearchQueryParameter:
      name: search
      in: query
      required: false
      description: Search query
      schema:
        example: <id> <name>
        type: string
    FiltersDataTypeParameter:
      name: dataType
      in: query
      required: false
      description: Include only samples with a particular data type
      schema:
        type: string
        enum:
          - audio
          - image
    FiltersMinIdParameter:
      name: minId
      in: query
      required: false
      description: Include only samples with an ID >= this value
      schema:
        type: integer
    FiltersMaxIdParameter:
      name: maxId
      in: query
      required: false
      description: Include only samples with an ID < this value
      schema:
        type: integer
    FiltersMetadataParameter:
      name: metadata
      in: query
      required: false
      description: >
        Filter samples by metadata key-value pairs, provided as a JSON string.

        Each item in the filter list is an object with the following properties:
            - "key": Metadata key to filter on.
            - "op": Operator ("eq" for positive match, "neq" for negative match).
            - "values": (optional) Array of values to match/exclude. If omitted or empty, matches/excludes all values for the key.
        In addition to filter objects, the following option objects can be
        specified:
            - { "no_metadata": boolean } - If true, include samples without any metadata
            - { "filters_combinator": ("and" | "or") } - Specifies the combinator and matching mode:
                - "and": All filter items must match (logical AND).
                - "or": Any filter item may match (logical OR); samples with metadata keys not present in the filters are included.
      schema:
        example: >
          Example 1: returns samples where metadata key "foo" is 'bar' or 'baz'
          AND

          metadata key "k" is "v".

          [
              { "no_metadata": true },
              { "filters_combinator": "and" },
              { "key": "foo", "op": "eq", "values": ["bar", "baz"] },
              { "key": "k", "op": "eq", "values": ["v"] }
          ]


          Example 2: returns samples where metadata key "foo" is not 'bar'.
          Samples

          without any metadata are filtered out.

          [
              { "no_metadata": false },
              { "filters_combinator": "or" },
              { "key": "foo", "op": "neq", "values": ["bar"] }
          ]
        type: string
    FiltersMinDateParameter:
      name: minDate
      in: query
      required: false
      description: Only include samples that where added after the date given
      schema:
        type: string
        format: date-time
        example: '2023-01-01T00:00:00.000Z'
    FiltersMaxDateParameter:
      name: maxDate
      in: query
      required: false
      description: Only include samples that were added before the date given
      schema:
        type: string
        format: date-time
        example: '2024-12-31T00:00:00.000Z'
  schemas:
    BatchAddMetadataRequest:
      type: object
      required:
        - metadataKey
        - metadataValue
      properties:
        metadataKey:
          type: string
        metadataValue:
          type: string
    GenericApiResponse:
      type: object
      required:
        - success
      properties:
        success:
          type: boolean
          description: Whether the operation succeeded
        error:
          type: string
          description: Optional error description (set if 'success' was false)
    StartJobResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - id
          properties:
            id:
              type: integer
              description: Job identifier. Status updates will include this identifier.
              example: 12873488112
    RawDataFilterCategory:
      type: string
      enum:
        - training
        - testing
        - post-processing
        - all
  securitySchemes:
    ApiKeyAuthentication:
      type: apiKey
      in: header
      name: x-api-key
    JWTAuthentication:
      type: apiKey
      in: cookie
      name: jwt
    JWTHttpHeaderAuthentication:
      type: apiKey
      in: header
      name: x-jwt-token
    OAuth2:
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: /v1/oauth/authorize
          tokenUrl: /v1/oauth/token
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information
        implicit:
          authorizationUrl: /v1/oauth/authorize
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information
        password:
          tokenUrl: /v1/oauth/token
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information
        clientCredentials:
          tokenUrl: /v1/oauth/token
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information

````

Built with [Mintlify](https://mintlify.com).