# Source: https://dev.writer.com/api-reference/application-api/get-application-graphs.md

# Retrieve graphs

> Retrieve Knowledge Graphs associated with a no-code agent that has chat capabilities.

## OpenAPI

````yaml get /v1/applications/{application_id}/graphs
paths:
  path: /v1/applications/{application_id}/graphs
  method: get
  servers:
    - url: https://api.writer.com
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer authentication header of the form `Bearer <token>`, where
                `<token>` is your [Writer API
                key](https://dev.writer.com/api-reference/api-keys).
          cookie: {}
    parameters:
      path:
        application_id:
          schema:
            - type: string
              required: true
              description: >-
                The ID of the no-code agent for which to retrieve Knowledge
                Graphs.
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - lang: cURL
        source: >-
          curl --location --request GET
          https://api.writer.com/v1/applications/{application_id}/graphs \
           --header "Authorization: Bearer <token>"
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            const applicationGraphsResponse = await client.applications.graphs.list('application_id');

            console.log(applicationGraphsResponse.graph_ids);
          }

          main();
      - lang: Python
        source: |-
          import os
          from writerai import Writer

          client = Writer(
              api_key=os.environ.get("WRITER_API_KEY"),  # This is the default and can be omitted
          )
          application_graphs_response = client.applications.graphs.list(
              "application_id",
          )
          print(application_graphs_response.graph_ids)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              graph_ids:
                allOf:
                  - type: array
                    description: >-
                      A list of Knowledge Graphs associated with the
                      application.
                    items:
                      type: string
                      format: uuid
            title: application_graphs_response
            refIdentifier: '#/components/schemas/application_graphs_response'
            requiredProperties:
              - graph_ids
        examples:
          example:
            value:
              graph_ids:
                - 3c90c3cc-0d44-4b50-8888-8dd25736052a
        description: Successful
  deprecated: false
  type: path
components:
  schemas: {}

````