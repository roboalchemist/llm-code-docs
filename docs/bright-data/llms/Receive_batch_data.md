# Source: https://docs.brightdata.com/api-reference/scraper-studio-api/Receive_batch_data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Receive Batch Data

> Receive Batch data

<Note>
  Result data is available for download for 16 days after collection. To avoid expiration, make sure to download the data within 16 days or configure a delivery method to get it automatically to your storage.
</Note>


## OpenAPI

````yaml web-scraper-ide-rest-api GET /dca/dataset
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
  /dca/dataset:
    get:
      description: Receive Batch data
      parameters:
        - name: id
          in: query
          required: true
          schema:
            type: string
          description: The ID of the dataset to retrieve.
      responses:
        '200':
          description: Dataset (Ready)
          content:
            application/json:
              examples:
                response:
                  value:
                    - Image: https://targetwebsite.com/product_id.png
                      Title: product_name
                      Price: product_price
                      input:
                        url: https://targetwebsite.com/product_id/
        '202':
          description: Waiting for Dataset
          content:
            application/json:
              examples:
                response:
                  value:
                    status: building
                    message: Dataset is not ready yet, try again in XXs
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