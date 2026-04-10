# Source: https://dev.writer.com/home/analyze-images.md

# Source: https://dev.writer.com/api-reference/vision-api/analyze-images.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Analyze images

> Submit images and documents with a prompt to generate an analysis. Supports JPG, PNG, PDF, and TXT files up to 7MB each.



## OpenAPI

````yaml post /v1/vision
openapi: 3.0.3
info:
  title: API
  version: '1.0'
servers:
  - url: https://api.writer.com
security:
  - bearerAuth: []
paths:
  /v1/vision:
    post:
      tags:
        - Vision
      summary: Analyze images
      description: >-
        Submit images and documents with a prompt to generate an analysis.
        Supports JPG, PNG, PDF, and TXT files up to 7MB each.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/vision_request'
            example:
              model: palmyra-vision
              variables:
                - name: image_1
                  file_id: f1234
                - name: image_2
                  file_id: f9876
              prompt: >-
                Describe the difference between the image {{image_1}} and the
                image {{image_2}}.
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              example:
                data: >-
                  Image f1234 shows a densely crowded urban beach with many
                  umbrellas, while image f9876 depicts a sparsely populated
                  tropical beach with clear turquoise water and lush greenery
              schema:
                $ref: '#/components/schemas/vision_response'
      security:
        - bearerAuth: []
components:
  schemas:
    vision_request:
      title: Vision Request
      required:
        - model
        - prompt
        - variables
      type: object
      properties:
        model:
          type: string
          description: The model to use for image analysis.
          enum:
            - palmyra-vision
        prompt:
          type: string
          description: >-
            The prompt to use for the image analysis. The prompt must include
            the name of each image variable, surrounded by double curly braces
            (`{{}}`). For example, `Describe the difference between the image
            {{image_1}} and the image {{image_2}}`.
        variables:
          type: array
          items:
            $ref: '#/components/schemas/vision_request_file_variable'
    vision_response:
      title: Vision Response
      required:
        - data
      type: object
      properties:
        data:
          type: string
          description: The result of the image analysis.
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