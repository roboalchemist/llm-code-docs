# Source: https://dev.writer.com/api-reference/tool-api/text-to-graph.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Text-to-graph

> Performs name entity recognition on the supplied text accepting a maximum of 35000 words.



## OpenAPI

````yaml post /v1/tools/text-to-graph
openapi: 3.0.3
info:
  title: API
  version: '1.0'
servers:
  - url: https://api.writer.com
security:
  - bearerAuth: []
paths:
  /v1/tools/text-to-graph:
    post:
      tags:
        - Tools API
      summary: Text-to-graph
      description: >-
        Performs name entity recognition on the supplied text accepting a
        maximum of 35000 words.
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/text_to_graph_request'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/text_to_graph_response'
              example:
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
      security:
        - bearerAuth: []
components:
  schemas:
    text_to_graph_request:
      title: text_to_graph_request
      required:
        - text
      type: object
      properties:
        text:
          type: string
          description: The text to convert into a graph structure. Maximum of 35,000 words.
    text_to_graph_response:
      title: text_to_graph_response
      required:
        - graph
      type: object
      properties:
        graph:
          type: array
          description: >-
            The graph structure generated from the input text, represented by a
            string array of entities and relationships.
          items:
            type: array
            description: >-
              A string array of entities and relationships representing the
              graph structure generated from the input text.
            items:
              type: string
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: >-
        Bearer authentication header of the form `Bearer <token>`, where
        `<token>` is your [Writer API
        key](https://dev.writer.com/api-reference/api-keys).

````