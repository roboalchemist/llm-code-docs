# Source: https://docs.statsig.com/api-reference/warehouse-connections/update-warehouse-connection-parameters.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Warehouse Connection Parameters



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json patch /console/v1/wh_connections
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
  /console/v1/wh_connections:
    patch:
      tags:
        - Warehouse Connections
      summary: Update Warehouse Connection Parameters
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/WhConnectionUpdateDto'
      responses:
        '200':
          description: Connection updated successfully
          content:
            application/json:
              schema:
                properties:
                  message:
                    type: string
                example:
                  message: Connection updated successfully
              example:
                message: Connection updated successfully
        '403':
          description: Insufficient permissions.
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: integer
                    enum:
                      - 403
                  message:
                    type: string
                required:
                  - status
                  - message
              examples:
                Forbidden resource:
                  value:
                    status: 403
                    message: >-
                      Forbidden. The request was valid, but the server is
                      refusing action. You might not have the necessary
                      permissions to access the resource.
      security:
        - STATSIG-API-KEY: []
components:
  schemas:
    WhConnectionUpdateDto:
      type: object
      properties:
        databricks:
          type: object
          properties:
            host:
              type: string
            path:
              type: string
            accessToken:
              type: string
            stagingDatabase:
              type: string
              description: >-
                Statsig will use this Database to save intermediate tables in
                the experimentation pipeline. Must be a database that the
                service user has write access to.
            oauthClientID:
              type: string
              nullable: true
            consoleComputePath:
              type: string
              nullable: true
              description: >-
                An optional separate path that Statsig will use to run
                interactive queries made from the Console.
        snowflake:
          type: object
          properties:
            accountName:
              type: string
            serviceUserName:
              type: string
            serviceUserPassword:
              type: string
            privateKey:
              type: string
              nullable: true
            keyPassPhrase:
              type: string
              nullable: true
            stagingDatabaseName:
              type: string
              description: The database containing the staging schema
            stagingSchemaName:
              type: string
              description: >-
                Statsig will use this Schema to save intermediate tables in the
                experimentation pipeline. Must be a schema that the service user
                has write access to.
            computeWarehouse:
              type: string
              description: >-
                The warehouse that Statsig will use to run queries. Must be a
                warehouse that the service user has access to.
            consoleComputeWarehouse:
              type: string
              nullable: true
              description: >-
                An optional warehouse that Statsig will use to run interactive
                queries made from the Console.
        bigquery:
          type: object
          properties:
            privateKey:
              type: string
              description: >-
                Private key for a first-party service account to use for the
                BigQuery connection.
            project:
              type: string
              description: The project that Statsig will use to run queries.
            consoleComputeProject:
              type: string
              description: >-
                An optional project that Statsig will use to run interactive
                queries made from the Console.
            stagingDataset:
              type: string
              description: >-
                Statsig will use this dataset to save intermediate tables in the
                experimentation pipeline. Must be a dataset that the service
                user has write access to.
        redshift:
          type: object
          properties:
            host:
              type: string
              description: The name of the Redshift cluster.
            port:
              type: number
              description: The port of the Redshift cluster.
              format: double
            database:
              type: string
              description: The database of the Redshift cluster.
            username:
              type: string
              description: The username of the admin of the Redshift cluster.
            password:
              type: string
              description: The password of the admin.
            stagingSchema:
              type: string
              description: The schema to use for staging tables.
            useSshTunnel:
              type: boolean
            sshUsername:
              type: string
            sshPort:
              type: number
              format: double
            sshHost:
              type: string
            sshPrivateKey:
              type: string
            sshPublicKey:
              type: string
            verifyCA:
              type: boolean
              description: Whether to verify CA over SSL.
            useAssumeRole:
              type: boolean
              description: Whether to use an IAM role to connect to the Redshift cluster.
            roleArn:
              type: string
            region:
              type: string
              description: >-
                The AWS region of your Redshift cluster. Needed if using an IAM
                Role to connect.
        athena:
          type: object
          properties:
            region:
              type: string
              description: The AWS region of your resources.
            bucket:
              type: string
              description: The name of your S3 bucket.
            dataCatalog:
              type: string
              description: The name of your Athena Data Source/Catalog.
            useCatalogInQueryContext:
              type: boolean
              description: >-
                Whether to specify the Data Catalog when making calls to your
                Athena instance via the SDK. This can be helpful to avoid
                needing to specify the same catalog in SQL for all queries.
            database:
              type: string
              description: The name of the database to use for staging tables.
            queryResultLocation:
              type: string
              description: The S3 location for Athena query results.
            workgroup:
              type: string
              description: The name of the Athena Workgroup to use for query results.
            roleArn:
              type: string
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).