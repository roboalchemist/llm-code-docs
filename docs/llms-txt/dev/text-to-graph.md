# Source: https://dev.writer.com/api-reference/tool-api/text-to-graph.md

# Text-to-graph

> Performs name entity recognition on the supplied text accepting a maximum of 35000 words.

## OpenAPI

````yaml post /v1/tools/text-to-graph
paths:
  path: /v1/tools/text-to-graph
  method: post
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              text:
                allOf:
                  - type: string
                    description: >-
                      The text to convert into a graph structure. Maximum of
                      35,000 words.
            required: true
            title: text_to_graph_request
            refIdentifier: '#/components/schemas/text_to_graph_request'
            requiredProperties:
              - text
        examples:
          example:
            value:
              text: <string>
    codeSamples:
      - lang: cURL
        source: >-
          curl --location --request POST
          https://api.writer.com/v1/tools/text-to-graph \
           --header "Authorization: Bearer <token>" \
           --header "Content-Type: application/json" \
          --data-raw '{"text":"A racecar has very powerful brakes that can
          decelerate from 200 km/h to 0 km/h in a few seconds"}'
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            const response = await client.tools.textToGraph({ text: 'A racecar has very powerful brakes that can decelerate from 200 km/h to 0 km/h in a few seconds' });

            console.log(response.graph);
          }

          main();
      - lang: Python
        source: |-
          import os
          from writerai import Writer

          client = Writer(
              # This is the default and can be omitted
              api_key=os.environ.get("WRITER_API_KEY"),
          )
          response = client.tools.text_to_graph(
              text="A racecar has very powerful brakes that can decelerate from 200 km/h to 0 km/h in a few seconds",
          )
          print(response.graph)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              graph:
                allOf:
                  - type: array
                    description: >-
                      The graph structure generated from the input text,
                      represented by a string array of entities and
                      relationships.
                    items:
                      type: array
                      description: >-
                        A string array of entities and relationships
                        representing the graph structure generated from the
                        input text.
                      items:
                        type: string
            title: text_to_graph_response
            refIdentifier: '#/components/schemas/text_to_graph_response'
            requiredProperties:
              - graph
        examples:
          example:
            value:
              graph:
                - - racecar [RACECAR]
                  - has_component
                  - brakes [COMPONENT]
                - - racecar [RACECAR]
                  - can_perform
                  - decelerate [ACTION]
                - - racecar [RACECAR]
                  - has_property
                  - powerful [PROPERTY]
                - - 200 km/h [VELOCITY]
                  - decreased_to
                  - 0 km/h [VELOCITY]
                - - decelerate [ACTION]
                  - performed_by
                  - racecar [RACECAR]
        description: ''
  deprecated: false
  type: path
components:
  schemas: {}

````