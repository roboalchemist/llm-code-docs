# Source: https://docs.rootly.com/api-reference/communications-templates/shows-a-communications-template.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Shows a communications template

> Shows details of a communications template



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json get /v1/communications/templates/{id}
openapi: 3.0.1
info:
  title: Rootly API v1
  version: v1
  description: >+
    # How to generate an API Key?

    - **Organization dropdown** > **Organization Settings** > **API Keys**


    # JSON:API Specification

    Rootly is using **JSON:API** (https://jsonapi.org) specification:

    - JSON:API is a specification for how a client should request that resources
    be fetched or modified, and how a server should respond to those requests.

    - JSON:API is designed to minimize both the number of requests and the
    amount of data transmitted between clients and servers. This efficiency is
    achieved without compromising readability, flexibility, or discoverability.

    - JSON:API requires use of the JSON:API media type
    (**application/vnd.api+json**) for exchanging data.


    # Authentication and Requests

    We use standard HTTP Authentication over HTTPS to authorize your requests.

    ```
      curl --request GET \
    --header 'Content-Type: application/vnd.api+json' \

    --header 'Authorization: Bearer YOUR-TOKEN' \

    --url https://api.rootly.com/v1/incidents

    ```


    <br/>


    # Rate limiting

    - There is a default limit of **5** **GET**, **HEAD**, and **OPTIONS** calls
    **per API key** every **60 seconds** (0 hours). The limit is calculated over
    a **0-hour sliding window** looking back from the current time. While the
    limit can be configured to support higher thresholds, you must first contact
    your **Rootly Customer Success Manager** to make any adjustments.

    - There is a default limit of **3** **POST**, **PUT**, **PATCH** or
    **DELETE** calls **per API key** every **60 seconds** (0 hours). The limit
    is calculated over a **0-hour sliding window** looking back from the current
    time. While the limit can be configured to support higher thresholds, you
    must first contact your **Rootly Customer Success Manager** to make any
    adjustments.

    - When rate limits are exceeded, the API will return a **429 Too Many
    Requests** HTTP status code with the response: `{"error": "Rate limit
    exceeded. Try again later."}`

    - **X-RateLimit headers** are included in every API response, providing
    real-time rate limit information:
      - **X-RateLimit-Limit** - The maximum number of requests permitted and the time window (e.g., "1000, 1000;window=3600" for 1000 requests per hour)
      - **X-RateLimit-Remaining** - The number of requests remaining in the current rate limit window
      - **X-RateLimit-Used** - The number of requests already made in the current window
      - **X-RateLimit-Reset** - The time at which the current rate limit window resets, in UTC epoch seconds

    # Pagination

    - Pagination is supported for all endpoints that return a collection of
    items.

    - Pagination is controlled by the **page** query parameter


    ## Example

    ```
      curl --request GET \
    --header 'Content-Type: application/vnd.api+json' \

    --header 'Authorization: Bearer YOUR-TOKEN' \

    --url https://api.rootly.com/v1/incidents?page[number]=1&page[size]=10

    ```

  x-logo:
    url: https://rootly-heroku.s3.us-east-1.amazonaws.com/swagger/v1/logo.png
servers:
  - url: https://api.rootly.com
security: []
paths:
  /v1/communications/templates/{id}:
    parameters:
      - name: id
        in: path
        description: Communications Template ID
        required: true
        schema:
          type: string
    get:
      tags:
        - Communications Templates
      summary: Shows a communications template
      description: Shows details of a communications template
      operationId: getCommunicationsTemplate
      responses:
        '200':
          description: communications template found
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/communications_template_response'
        '404':
          description: communications template not found
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/errors_list'
      security:
        - bearer_auth: []
components:
  schemas:
    communications_template_response:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
              description: Unique ID of the communications template
            type:
              type: string
              enum:
                - communications_templates
            attributes:
              type: object
              allOf:
                - $ref: '#/components/schemas/communications_template'
          required:
            - id
            - type
            - attributes
      required:
        - data
    errors_list:
      type: object
      properties:
        errors:
          type: array
          items:
            type: object
            properties:
              title:
                type: string
              status:
                type: string
              code:
                type: string
                nullable: true
              detail:
                type: string
                nullable: true
            required:
              - title
              - status
    communications_template:
      type: object
      properties:
        name:
          type: string
          description: The name of the communications template
        slug:
          type: string
          description: The slug of the communications template
        description:
          type: string
          description: The description of the communications template
          nullable: true
        position:
          type: integer
          description: Position of the communications template
          nullable: true
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
        communication_type_id:
          type: string
          description: The communication type ID
        communication_template_stages:
          type: array
          description: Communication template stages
          nullable: true
          items:
            type: object
            properties:
              data:
                type: object
                properties:
                  id:
                    type: string
                    description: ID of the communication template stage
                  type:
                    type: string
                    enum:
                      - communications_template_stages
                  attributes:
                    type: object
                    properties:
                      email_body:
                        type: string
                        description: Email body for the stage
                        nullable: true
                      email_subject:
                        type: string
                        description: Email subject for the stage
                        nullable: true
                      slack_content:
                        type: string
                        description: Slack content for the stage
                        nullable: true
                      sms_content:
                        type: string
                        description: SMS content for the stage
                        nullable: true
                      created_at:
                        type: string
                        description: Date of creation
                      updated_at:
                        type: string
                        description: Date of last update
                      communication_stage:
                        type: object
                        properties:
                          id:
                            type: string
                            description: The communication stage ID
                          name:
                            type: string
                            description: The communication stage name
                      communication_template:
                        type: object
                        properties:
                          id:
                            type: string
                            description: The communication template ID
                          name:
                            type: string
                            description: The communication template name
        communication_type:
          type: object
          properties:
            id:
              type: string
              description: ID of the communication type
            name:
              type: string
              description: Name of the communication type
      required:
        - name
        - position
        - created_at
        - updated_at
  securitySchemes:
    bearer_auth:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).