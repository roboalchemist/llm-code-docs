# Source: https://dev.writer.com/api-reference/file-api/get-all-files.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List files

> Retrieve a paginated list of files with optional filtering by status, graph association, and file type.



## OpenAPI

````yaml get /v1/files
openapi: 3.0.3
info:
  title: API
  version: '1.0'
servers:
  - url: https://api.writer.com
security:
  - bearerAuth: []
paths:
  /v1/files:
    get:
      tags:
        - File API
      summary: List files
      description: >-
        Retrieve a paginated list of files with optional filtering by status,
        graph association, and file type.
      operationId: gatewayGetFiles
      parameters:
        - name: before
          in: query
          required: false
          schema:
            type: string
          description: >-
            The ID of the first object in the previous page. This parameter
            instructs the API to return the previous page of results.
        - name: after
          in: query
          required: false
          schema:
            type: string
          description: >-
            The ID of the last object in the previous page. This parameter
            instructs the API to return the next page of results.
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            format: int32
            default: 50
          description: >-
            Specifies the maximum number of objects returned in a page. The
            default value is 50. The minimum value is 1, and the maximum value
            is 100.
        - name: order
          in: query
          required: false
          schema:
            type: string
            default: desc
            enum:
              - asc
              - desc
          description: >-
            Specifies the order of the results. Valid values are asc for
            ascending and desc for descending.
        - name: graph_id
          in: query
          required: false
          schema:
            type: string
            format: uuid
          description: The unique identifier of the graph to which the files belong.
        - name: status
          in: query
          required: false
          schema:
            enum:
              - in_progress
              - completed
              - failed
          description: >-
            Specifies the status of the files to retrieve. Valid values are
            in_progress, completed or failed.
        - name: file_types
          in: query
          required: false
          schema:
            type: string
          description: >-
            The extensions of the files to retrieve. Separate multiple
            extensions with a comma. For example: `pdf,jpg,docx`.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/files_response'
              example:
                data:
                  - id: 7c36a365-392f-43ba-840d-8f3103b42572
                    name: example.pdf
                    created_at: '2024-07-10T12:00:00Z'
                    graph_ids:
                      - 31a8b75a-9a90-432f-8861-942229125333
                    status: in_progress
                  - id: 4bbe6207-737e-486f-a287-c5e95536984a
                    name: image.jpg
                    created_at: '2024-07-09T15:30:00Z'
                    graph_ids:
                      - 31a8b75a-9a90-432f-8861-942229125333
                    status: completed
                  - id: efc86bb4-30a4-40c9-a52a-ecee0d7e071f
                    name: document.txt
                    created_at: '2024-07-08T16:00:00Z'
                    graph_ids:
                      - 31a8b75a-9a90-432f-8861-942229125333
                    status: failed
                has_more: false
                first_id: 7c36a365-392f-43ba-840d-8f3103b42572
                last_id: efc86bb4-30a4-40c9-a52a-ecee0d7e071f
      security:
        - bearerAuth: []
components:
  schemas:
    files_response:
      title: files_response
      required:
        - data
        - has_more
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/file_response'
        has_more:
          type: boolean
          description: Indicates if there are more files available beyond the current page.
        first_id:
          type: string
          description: The ID of the first file in the current response.
        last_id:
          type: string
          description: The ID of the last file in the current response.
    file_response:
      title: file_response
      required:
        - id
        - created_at
        - name
        - graph_ids
        - status
      type: object
      properties:
        id:
          type: string
          description: A unique identifier of the file.
        created_at:
          type: string
          format: date-time
          description: The timestamp when the file was uploaded.
        name:
          type: string
          description: The name of the file.
        graph_ids:
          type: array
          items:
            type: string
            format: uuid
          description: >-
            A list of Knowledge Graph IDs that the file is associated with.


            If you provided a `graphId` during upload, the file is associated
            with that Knowledge Graph. However, the `graph_ids` field in the
            upload response is an empty list. The association will be visible in
            the `graph_ids` list when you retrieve the file using the file
            retrieval endpoint.
        status:
          type: string
          description: The processing status of the file.
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