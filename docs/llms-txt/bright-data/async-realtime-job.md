# Source: https://docs.brightdata.com/api-reference/scraper-studio-api/initiate-a-realtime-job/async-realtime-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Trigger a scraper for real-time collection (Asynchronous)

> Trigger a scraper for real-time collection



## OpenAPI

````yaml web-scraper-ide-rest-api POST /dca/trigger_immediate
openapi: 3.1.0
info:
  title: Brightdata API
  description: API for interaction with datasets marketplace
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /dca/trigger_immediate:
    post:
      description: Trigger a scraper for real-time collection
      parameters:
        - name: collector
          in: query
          required: true
          schema:
            type: string
          description: A unique identification of scraper
        - name: version
          in: query
          schema:
            type: string
          description: Set to `dev` to trigger the development version of the scraper
        - name: name
          in: query
          schema:
            type: string
          description: '`human_name` - A human readable name for the batch'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                url:
                  type: string
                  format: uri
            examples:
              request:
                value:
                  url: https://targetwebsite.com/product_id/
      responses:
        '200':
          description: OK
          content:
            application/json:
              examples:
                response:
                  value:
                    response_id: <response_id>
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Use your Bright Data API Key as a Bearer token in the Authorization
        header.


        **How to authenticate:**

        1. Obtain your API Key from the Bright Data account settings at
        https://brightdata.com/cp/setting/users

        2. Include the API Key in the Authorization header of your requests

        3. Format: `Authorization: Bearer YOUR_API_KEY`


        **Example:**

        ```

        Authorization: Bearer
        b5648e1096c6442f60a6c4bbbe73f8d2234d3d8324554bd6a7ec8f3f251f07df

        ```


        Learn how to get your Bright Data API key:
        https://docs.brightdata.com/api-reference/authentication
      bearerFormat: API Key

````