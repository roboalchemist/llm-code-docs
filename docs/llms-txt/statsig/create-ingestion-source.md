# Source: https://docs.statsig.com/api-reference/ingestions/create-ingestion-source.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Ingestion Source



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json post /console/v1/ingestion
openapi: 3.0.0
info:
  title: Console API
  description: >-
    The "Console API" is the CRUD API for performing the actions offered on
    console.statsig.com without needing to go through the web UI.

    If you have any feature requests, drop on in to our [slack
    channel](https://www.statsig.com/slack) and let us know.

    <br /><br />

    <b>Authorization</b>

    <br />

    All requests must include the **STATSIG-API-KEY** field in the header. The
    value should be a **Console API Key** which can be created in the Project
    Settings on
    [console.statsig.com/api_keys](https://console.statsig.com/api_keys)

    <br /><br />

    <b>Rate Limiting</b>

    <br />

    Requests to the Console API are limited to <code>~ 100reqs / 10secs and ~
    900reqs / 15 mins</code>.

    <br /><br />

    <b>Keyboard Search</b>

    <br />

    Use <code>Ctrl/Cmd + K</code> to search for specific endpoints.
  version: 20240601.0.0
  contact: {}
servers:
  - url: https://statsigapi.net
security: []
tags: []
paths:
  /console/v1/ingestion:
    post:
      tags:
        - Ingestions
      summary: Create Ingestion Source
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/IngestionSourceCreateContractDto'
      responses:
        '200':
          description: Create Ingestion Success
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/IngestionDto'
                example:
                  type: databricks
                  dataset: Metrics
                  source_name: ingestion-1
                  query: SELECT * FROM TABLE
                  column_mapping:
                    unit_id: string
                    id_type: string
                    dateid: string
                    metric_name: string
                    metric_value: string
                    numerator: string
                    denominator: string
                  use_delta_sharing: false
                  share: string
                  schema: string
                  table: string
                  enabled: false
              example:
                type: databricks
                dataset: Metrics
                source_name: ingestion-1
                query: SELECT * FROM TABLE
                column_mapping:
                  unit_id: string
                  id_type: string
                  dateid: string
                  metric_name: string
                  metric_value: string
                  numerator: string
                  denominator: string
                use_delta_sharing: false
                share: string
                schema: string
                table: string
                enabled: false
        '400':
          description: Invalid request. Please check the request input and try again.
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: integer
                    enum:
                      - 400
                  message:
                    type: string
                required:
                  - status
                  - message
              examples:
                Invalid Request:
                  value:
                    status: 400
                    message: Ingestion source already exists with name {source_name}
        '404':
          description: Not Found. The requested resource could not be found.
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: integer
                    enum:
                      - 404
                  message:
                    type: string
                required:
                  - status
                  - message
              examples:
                Not Found:
                  value:
                    status: 404
                    message: Ingestion of type {type} not found.
      security:
        - STATSIG-API-KEY: []
components:
  schemas:
    IngestionSourceCreateContractDto:
      oneOf:
        - type: object
          properties:
            dataset:
              type: string
              enum:
                - Metrics
            column_mapping:
              type: object
              properties:
                unit_id:
                  type: string
                  description: >-
                    The unique user identifier this metric is for. This might
                    not necessarily be a user_id - it could be a custom_id of
                    some kind. Make sure this is in the same format as your
                    logged unit_ids.
                id_type:
                  type: string
                  description: >-
                    The id_type the unit_id represents. Must be valid id_type.
                    Default Statsig types are user_id/stable_id, but you may
                    have generated custom id_types. Make sure this matches (case
                    sensitive) a customID in your project, or you won’t get
                    experiment results.
                dateid:
                  type: string
                  description: >-
                    Date of the daily metric, ISO formatted (ex. 2021-02-17).
                    We’ll load custom metrics to whatever date you use here.
                metric_name:
                  type: string
                  description: String format. Not null. Length < 128 characters.
                metric_value:
                  default: 'null'
                  type: string
                  description: >-
                    Numeric value for the metric. This OR both of numerator and
                    denominator need to be provided.
                numerator:
                  default: 'null'
                  type: string
                  description: >-
                    Required for ratio metrics. If present along with a
                    denominator in any record, the metric will be treated as
                    ratio and only calculated for users with non-null
                    denominators
                denominator:
                  default: 'null'
                  type: string
                  description: >-
                    Required for ratio metrics. If present along with a
                    numerator in any record, the metric will be treated as ratio
                    and only calculated for users with non-null numerators.
              required:
                - unit_id
                - id_type
                - dateid
                - metric_name
            type:
              type: string
              enum:
                - redshift
                - bigquery-v2
                - snowflake-v2
                - databricks
                - azure-synapse
                - s3
                - athena
                - adls
            source_name:
              type: string
            query:
              type: string
            use_delta_sharing:
              type: boolean
              enum:
                - true
            share:
              type: string
            schema:
              type: string
            table:
              type: string
            enabled:
              type: boolean
          required:
            - dataset
            - type
            - source_name
        - type: object
          properties:
            dataset:
              type: string
              enum:
                - Events
            column_mapping:
              type: object
              properties:
                unit_id:
                  type: string
                  description: >-
                    The unique user identifier this event is for. This might not
                    necessarily be a single column for userID - it could be
                    spread across multiple columns for deviceID etc.
                event_name:
                  type: string
                  description: >-
                    Name of the event. String under 128 characters, using ‘_’
                    for spaces.
                timestamp:
                  type: string
                  description: Unix timestamp in seconds of the event (ex. 1613584800)
                ids:
                  default: {}
                  type: object
                  additionalProperties:
                    type: string
                metadata:
                  default: {}
                  type: object
                  additionalProperties:
                    type: string
                metadata_object:
                  default: 'null'
                  type: string
                event_value:
                  default: ''
                  type: string
              required:
                - event_name
                - timestamp
                - ids
            type:
              type: string
              enum:
                - redshift
                - bigquery-v2
                - snowflake-v2
                - databricks
                - azure-synapse
                - s3
                - athena
                - adls
            source_name:
              type: string
            query:
              type: string
            use_delta_sharing:
              type: boolean
              enum:
                - true
            share:
              type: string
            schema:
              type: string
            table:
              type: string
            enabled:
              type: boolean
          required:
            - dataset
            - type
            - source_name
        - type: object
          properties:
            dataset:
              type: string
              enum:
                - Exposures
                - export_exposures
            column_mapping:
              type: object
              properties:
                experiment:
                  type: string
                  description: Unique identifier for the experiment.
                group_id:
                  type: string
                  description: Unique identifier for the experiment groups.
                unit_id:
                  type: string
                  description: >-
                    The unique user identifier this exposure is for. This might
                    not necessarily be a single column for userID - it could be
                    spread across multiple columns for deviceID etc.
                timestamp:
                  type: string
                  description: Unix timestamp in seconds of the event (ex. 1613584800)
                ids:
                  default: {}
                  type: object
                  additionalProperties:
                    type: string
                metadata:
                  default: {}
                  type: object
                  additionalProperties:
                    type: string
                metadata_object:
                  default: 'null'
                  type: string
                event_value:
                  default: ''
                  type: string
              required:
                - experiment
                - group_id
                - timestamp
                - ids
            type:
              type: string
              enum:
                - redshift
                - bigquery-v2
                - snowflake-v2
                - databricks
                - azure-synapse
                - s3
                - athena
                - adls
            source_name:
              type: string
            query:
              type: string
            use_delta_sharing:
              type: boolean
              enum:
                - true
            share:
              type: string
            schema:
              type: string
            table:
              type: string
            enabled:
              type: boolean
          required:
            - dataset
            - type
            - source_name
    SingleDataResponse:
      type: object
      properties:
        message:
          type: string
          description: A simple string explaining the result of the operation.
        data:
          type: object
          description: A single result.
      required:
        - message
        - data
    IngestionDto:
      type: object
      properties:
        id:
          type: string
        type:
          type: string
        enabled:
          type: boolean
        data:
          type: object
      required:
        - id
        - type
        - enabled
        - data
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).