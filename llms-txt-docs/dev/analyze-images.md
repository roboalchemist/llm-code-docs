# Source: https://dev.writer.com/home/analyze-images.md

# Source: https://dev.writer.com/api-reference/vision-api/analyze-images.md

# Analyze images

> Submit images and documents with a prompt to generate an analysis. Supports JPG, PNG, PDF, and TXT files up to 7MB each.

## OpenAPI

````yaml post /v1/vision
paths:
  path: /v1/vision
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
              model:
                allOf:
                  - type: string
                    description: The model to use for image analysis.
                    enum:
                      - palmyra-vision
              prompt:
                allOf:
                  - type: string
                    description: >-
                      The prompt to use for the image analysis. The prompt must
                      include the name of each image variable, surrounded by
                      double curly braces (`{{}}`). For example, `Describe the
                      difference between the image {{image_1}} and the image
                      {{image_2}}`.
              variables:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/vision_request_file_variable'
            required: true
            title: Vision Request
            refIdentifier: '#/components/schemas/vision_request'
            requiredProperties:
              - model
              - prompt
              - variables
        examples:
          example:
            value:
              model: palmyra-vision
              variables:
                - name: image_1
                  file_id: f1234
                - name: image_2
                  file_id: f9876
              prompt: >-
                Describe the difference between the image {{image_1}} and the
                image {{image_2}}.
    codeSamples:
      - lang: cURL
        source: >-
          curl --location --request POST https://api.writer.com/v1/vision \
           --header "Authorization: Bearer <token>" \
           --header "Content-Type: application/json" \
          --data-raw
          '{"model":"palmyra-vision","variables":[{"name":"image_1","file_id":"f1234"},{"name":"image_2","file_id":"f9876"}],"prompt":"Describe
          the difference between the image {{image_1}} and the image
          {{image_2}}."}'
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            const visionResponse = await client.vision.analyze({
              model: 'palmyra-vision',
              prompt: 'Describe the difference between the image {{image_1}} and the image {{image_2}}.',
              variables: [
                { name: 'image_1', file_id: 'f1234' },
                { name: 'image_2', file_id: 'f9876' },
              ],
            });

            console.log(visionResponse.data);
          }

          main();
      - lang: Python
        source: |-
          import os
          from writerai import Writer

          client = Writer(
              api_key=os.environ.get("WRITER_API_KEY"),  # This is the default and can be omitted
          )
          vision_response = client.vision.analyze(
              model="palmyra-vision",
              prompt="Describe the difference between the image {{image_1}} and the image {{image_2}}.",
              variables=[{
                  "name": "image_1",
                  "file_id": "f1234",
              }, {
                  "name": "image_2",
                  "file_id": "f9876",
              }],
          )
          print(vision_response.data)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: string
                    description: The result of the image analysis.
            title: Vision Response
            refIdentifier: '#/components/schemas/vision_response'
            requiredProperties:
              - data
        examples:
          example:
            value:
              data: >-
                Image f1234 shows a densely crowded urban beach with many
                umbrellas, while image f9876 depicts a sparsely populated
                tropical beach with clear turquoise water and lush greenery
        description: Successful response
  deprecated: false
  type: path
components:
  schemas:
    vision_request_file_variable:
      title: Vision Request File Variable
      description: >-
        An array of file variables required for the analysis. The files must be
        uploaded to the Writer platform before they can be used in a vision
        request. Learn how to upload files using the [Files
        API](https://dev.writer.com/api-reference/file-api/upload-files).


        Supported file types: JPG, PNG, PDF, TXT. The maximum allowed file size
        for each file is 7MB.
      required:
        - name
        - file_id
      type: object
      properties:
        name:
          type: string
          description: >-
            The name of the file variable. You must reference this name in the
            prompt with double curly braces (`{{}}`). For example, `Describe the
            difference between the image {{image_1}} and the image {{image_2}}`.
        file_id:
          type: string
          description: >-
            The File ID of the file to analyze. The file must be uploaded to the
            Writer platform before it can be used in a vision request. Supported
            file types: JPG, PNG, PDF, TXT (max 7MB each).

````