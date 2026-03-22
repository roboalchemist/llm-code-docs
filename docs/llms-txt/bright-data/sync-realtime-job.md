# Source: https://docs.brightdata.com/api-reference/scraper-studio-api/initiate-a-realtime-job/sync-realtime-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Trigger a Scraper Synchronously for real-time collection

> Trigger a scraper for batch collection method

<Warning>
  You can trigger only **single-input** APIs. Make sure the payload is **an object, not an array of objects**.
</Warning>


## OpenAPI

````yaml web-scraper-ide-rest-api POST /dca/crawl
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
  /dca/crawl:
    post:
      description: Trigger a scraper for batch collection method
      parameters:
        - name: collector
          in: query
          required: true
          schema:
            type: string
          description: A unique identification of scraper
        - name: timeout
          in: query
          required: true
          schema:
            type: string
            example: 50s
          description: Request timeout duration. Must be between 25s and 50s.
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
                  url: https://www.ebay.com/itm/326972541236
      responses:
        '200':
          description: OK
          content:
            application/json:
              examples:
                response:
                  value:
                    - product_title: >-
                        Apple iPad 11th Gen, 128 GB, Wi-Fi + 5G, 11 in - Silver
                        - BRAND NEW SEALED
                      price:
                        value: 324.99
                        currency: USD
                        symbol: $
                      condition: >-
                        New: A brand-new, unused, unopened, undamaged item in
                        its original packaging (where packaging is ...
                      seller_feedback_percentage: 100% positive feedback
                      seller_items_sold: 173 items sold
                      seller_since: Joined Nov 2012
                      item_specifics:
                        brand: Apple
                        model: Apple iPad (11th generation)
                        processor_model: Apple A16 Bionic
                        operating_system: iPadOS
                      storage_options: []
                      seller_ratings:
                        accurate_description: '--'
                        shipping_cost: '--'
                        shipping_speed: '--'
                        communication: '4.9'
                      product_images:
                        - >-
                          https://i.ebayimg.com/images/g/4a8AAeSw7x5pboS0/s-l1600.webp
                        - >-
                          https://i.ebayimg.com/images/g/4a8AAeSw7x5pboS0/s-l1600.webp
                      feedback_count: 36
                      financing_options:
                        monthly_payment:
                          value: 13.99
                          currency: USD
                          symbol: $
                        payment_plan_duration: (12 monthly payment plan)
                        apr: 13.99%
                      input:
                        url: https://www.ebay.com/itm/326972541236
                      seller_namestest: jwc8109
        '202':
          description: Timeout waiting for crawl results
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: Error code indicating the type of timeout
                  message:
                    type: string
                    description: >-
                      Detailed message about the timeout and instructions for
                      polling results
                  response_id:
                    type: string
                    description: >-
                      Unique identifier for the response to be used for polling
                      results
                required:
                  - error
                  - message
                  - response_id
              example:
                error: crawl_results_timeout
                message: >-
                  Timed out waiting for crawl results (timeout=NaNs). The page
                  crawl is continuing in the background, you can poll a GET
                  request to
                  https://api.brightdata.com/dca/get_result?response_id=ID until
                  the result is ready
                response_id: RESPONSE_ID
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