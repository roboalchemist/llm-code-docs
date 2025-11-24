# Source: https://dev.writer.com/api-reference/application-api/put-application-graphs.md

# Associate graphs

> Updates the list of Knowledge Graphs associated with a no-code chat agent.

## OpenAPI

````yaml put /v1/applications/{application_id}/graphs
paths:
  path: /v1/applications/{application_id}/graphs
  method: put
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
                The ID of the no-code agent to update.


                Only no-code agents with chat capabilities can have associated
                Knowledge Graphs. No-code agents with text generation and
                research capabilities do not support Knowledge Graphs.
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              graph_ids:
                allOf:
                  - type: array
                    description: >-
                      A list of Knowledge Graph IDs to associate with the
                      application. Note that this will replace the existing list
                      of Knowledge Graphs associated with the application, not
                      add to it.
                    items:
                      type: string
                      format: uuid
            required: true
            title: application_graph_ids_request
            refIdentifier: '#/components/schemas/application_graph_ids_request'
            requiredProperties:
              - graph_ids
        examples:
          example:
            value:
              graph_ids:
                - 3c90c3cc-0d44-4b50-8888-8dd25736052a
    codeSamples:
      - lang: cURL
        source: >-
          curl --location --request PUT
          https://api.writer.com/v1/applications/{application_id}/graphs \
           --header "Authorization: Bearer <token>" \
           --header "Content-Type: application/json" \
          --data-raw
          '{"graph_ids":["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e","182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e","182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]}'
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            const applicationGraphsResponse = await client.applications.graphs.update('application_id', {
              graph_ids: ['182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e'],
            });

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
          application_graphs_response = client.applications.graphs.update(
              application_id="application_id",
              graph_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
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