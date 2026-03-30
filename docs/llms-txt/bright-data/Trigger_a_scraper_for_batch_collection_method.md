# Source: https://docs.brightdata.com/api-reference/scraper-studio-api/Trigger_a_scraper_for_batch_collection_method.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Trigger a Scraper Asynchronously for Batch Collection

> Trigger a scraper for batch collection method



## OpenAPI

````yaml web-scraper-ide-rest-api POST /dca/trigger
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
  /dca/trigger:
    post:
      description: Trigger a scraper for batch collection method
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
        - name: queue_next
          in: query
          schema:
            type: integer
            default: 1
          description: >-
            If there's already something in the crawl queue, push this job into
            the queue
        - name: queue
          in: query
          schema:
            type: string
          description: >-
            Send another batch of requests that will start after the last one is
            finished
        - name: confirm_cancel
          in: query
          schema:
            type: integer
            default: 1
          description: >-
            Cancel running job and run instead, submit the request and cancel
            running one
        - name: no_downloads
          in: query
          schema:
            type: integer
            default: 1
          description: Disable media file download
        - name: deadline
          in: query
          schema:
            type: string
          description: >-
            Set job time deadline, job will be terminated after specified time.
            `h` for hours, `m` for minutes, `s` for seconds.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  url:
                    type: string
                    format: uri
            examples:
              request:
                value:
                  - url: https://targetwebsite.com/product_id/
      responses:
        '200':
          description: OK
          content:
            application/json:
              examples:
                response:
                  value:
                    collection_id: ID_DATASET
                    start_eta: '2021-11-07T13:26:22.702Z'
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