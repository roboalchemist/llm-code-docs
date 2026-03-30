# Source: https://docs.brightdata.com/api-reference/account-management-api/Get_the_total_cost_and_bandwidth_stats_for_a_Zone.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Total cost & bandwidth for a zone

> Get the total cost and bandwidth stats for a Zone

<Tip>
  Paste your API key to the authorization field. To get an API key, [Create an account](https://brightdata.com/?hs_signup=1\&utm_source=docs\&utm_campaign=playground) and learn [how to generate an API key](/api-reference/authentication#how-do-i-generate-a-new-api-key%3F)
</Tip>


## OpenAPI

````yaml openapi GET /zone/cost
openapi: 3.0.1
info:
  title: Bright Data API
  description: >-
    Integrate Bright Data APIs to your pipeline and secure high-end scraping
    precision
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /zone/cost:
    get:
      description: Get the total cost and bandwidth stats for a Zone
      parameters:
        - in: query
          name: zone
          description: Zone name
          required: true
          schema:
            type: string
        - in: query
          name: from
          description: Start
          required: false
          schema:
            type: string
        - in: query
          name: to
          description: End
          required: false
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                example:
                  ID:
                    back_m2:
                      bw: 0
                      cost: 0
                    back_m1:
                      bw: 36557298
                      cost: 0
                    back_m0:
                      bw: 1219004
                      cost: 0
                    back_d2:
                      bw: 82190
                      cost: 0
                    back_d1:
                      bw: 0
                      cost: 0
                    back_d0:
                      bw: 0
                      cost: 0
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