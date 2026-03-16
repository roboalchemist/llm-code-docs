# Source: https://docs.rootly.com/api-reference/services/creates-a-service.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creates a service

> Creates a new service from provided data



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json post /v1/services
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
  /v1/services:
    post:
      tags:
        - Services
      summary: Creates a service
      description: Creates a new service from provided data
      operationId: createService
      parameters: []
      requestBody:
        content:
          application/vnd.api+json:
            schema:
              $ref: '#/components/schemas/new_service'
        required: true
      responses:
        '201':
          description: service created
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/service_response'
        '401':
          description: responds with unauthorized for invalid token
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/errors_list'
        '422':
          description: invalid request
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/errors_list'
      security:
        - bearer_auth: []
components:
  schemas:
    new_service:
      type: object
      properties:
        data:
          type: object
          properties:
            type:
              type: string
              enum:
                - services
            attributes:
              type: object
              properties:
                name:
                  type: string
                  description: The name of the service
                description:
                  type: string
                  description: The description of the service
                  nullable: true
                public_description:
                  type: string
                  description: The public description of the service
                  nullable: true
                notify_emails:
                  type: array
                  description: Emails to attach to the service
                  items:
                    type: string
                  nullable: true
                color:
                  type: string
                  description: The hex color of the service
                  nullable: true
                position:
                  type: integer
                  description: Position of the service
                  nullable: true
                show_uptime:
                  type: boolean
                  description: Show uptime
                  nullable: true
                show_uptime_last_days:
                  type: integer
                  description: Show uptime over x days
                  enum:
                    - 30
                    - 60
                    - 90
                  nullable: true
                  default: 60
                backstage_id:
                  type: string
                  description: >-
                    The Backstage entity id associated to this service. eg:
                    :namespace/:kind/:entity_name
                  nullable: true
                pagerduty_id:
                  type: string
                  description: The PagerDuty service id associated to this service
                  nullable: true
                external_id:
                  type: string
                  description: The external id associated to this service
                  nullable: true
                opsgenie_id:
                  type: string
                  description: The Opsgenie service id associated to this service
                  nullable: true
                opsgenie_team_id:
                  type: string
                  description: The Opsgenie team id associated to this service
                  nullable: true
                cortex_id:
                  type: string
                  description: The Cortex group id associated to this service
                  nullable: true
                service_now_ci_sys_id:
                  type: string
                  description: The Service Now CI sys id associated to this service
                  nullable: true
                github_repository_name:
                  type: string
                  description: >-
                    The GitHub repository name associated to this service. eg:
                    rootlyhq/my-service
                  nullable: true
                github_repository_branch:
                  type: string
                  description: >-
                    The GitHub repository branch associated to this service. eg:
                    main
                  nullable: true
                gitlab_repository_name:
                  type: string
                  description: >-
                    The GitLab repository name associated to this service. eg:
                    rootlyhq/my-service
                  nullable: true
                gitlab_repository_branch:
                  type: string
                  description: >-
                    The GitLab repository branch associated to this service. eg:
                    main
                  nullable: true
                environment_ids:
                  type: array
                  description: Environments associated with this service
                  items:
                    type: string
                  nullable: true
                service_ids:
                  type: array
                  description: Services dependent on this service
                  items:
                    type: string
                  nullable: true
                owner_group_ids:
                  type: array
                  description: Owner Teams associated with this service
                  items:
                    type: string
                  nullable: true
                owner_user_ids:
                  type: array
                  description: Owner Users associated with this service
                  items:
                    type: integer
                  nullable: true
                kubernetes_deployment_name:
                  type: string
                  description: >-
                    The Kubernetes deployment name associated to this service.
                    eg: namespace/deployment-name
                  nullable: true
                alerts_email_enabled:
                  type: boolean
                  description: Enable alerts through email
                  nullable: true
                alert_urgency_id:
                  type: string
                  description: The alert urgency id of the service
                  nullable: true
                escalation_policy_id:
                  type: string
                  description: The escalation policy id of the service
                  nullable: true
                slack_channels:
                  type: array
                  description: Slack Channels associated with this service
                  items:
                    type: object
                    properties:
                      id:
                        type: string
                        description: Slack channel ID
                      name:
                        type: string
                        description: Slack channel name
                    required:
                      - id
                      - name
                  nullable: true
                slack_aliases:
                  type: array
                  description: Slack Aliases associated with this service
                  items:
                    type: object
                    properties:
                      id:
                        type: string
                        description: Slack alias ID
                      name:
                        type: string
                        description: Slack alias name
                    required:
                      - id
                      - name
                  nullable: true
                alert_broadcast_enabled:
                  type: boolean
                  description: Enable alerts to be broadcasted to a specific channel
                  nullable: true
                alert_broadcast_channel:
                  type: object
                  description: Slack channel to broadcast alerts to
                  properties:
                    id:
                      type: string
                      description: Slack channel ID
                    name:
                      type: string
                      description: Slack channel name
                  required:
                    - id
                  nullable: true
                incident_broadcast_enabled:
                  type: boolean
                  description: Enable incidents to be broadcasted to a specific channel
                  nullable: true
                incident_broadcast_channel:
                  type: object
                  description: Slack channel to broadcast incidents to
                  properties:
                    id:
                      type: string
                      description: Slack channel ID
                    name:
                      type: string
                      description: Slack channel name
                  required:
                    - id
                  nullable: true
                properties:
                  type: array
                  items:
                    type: object
                    description: Set a value for a catalog property
                    properties:
                      catalog_property_id:
                        type: string
                        description: Catalog property ID
                      value:
                        type: string
                        description: The property value
                    required:
                      - catalog_property_id
                      - value
                  description: Array of property values for this service.
              additionalProperties: false
              required:
                - name
          required:
            - type
            - attributes
      required:
        - data
    service_response:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
              description: Unique ID of the service
            type:
              type: string
              enum:
                - services
            attributes:
              type: object
              allOf:
                - $ref: '#/components/schemas/service'
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
    service:
      type: object
      properties:
        name:
          type: string
          description: The name of the service
        slug:
          type: string
          description: The slug of the service
        description:
          type: string
          description: The description of the service
          nullable: true
        public_description:
          type: string
          description: The public description of the service
          nullable: true
        notify_emails:
          type: array
          description: Emails attached to the service
          items:
            type: string
          nullable: true
        color:
          type: string
          description: The hex color of the service
          nullable: true
        position:
          type: integer
          description: Position of the service
          nullable: true
        backstage_id:
          type: string
          description: >-
            The Backstage entity id associated to this service. eg:
            :namespace/:kind/:entity_name
          nullable: true
        external_id:
          type: string
          description: The external id associated to this service
          nullable: true
        pagerduty_id:
          type: string
          description: The PagerDuty service id associated to this service
          nullable: true
        opsgenie_id:
          type: string
          description: The Opsgenie service id associated to this service
          nullable: true
        cortex_id:
          type: string
          description: The Cortex group id associated to this service
          nullable: true
        service_now_ci_sys_id:
          type: string
          description: The Service Now CI sys id associated to this service
          nullable: true
        github_repository_name:
          type: string
          description: >-
            The GitHub repository name associated to this service. eg:
            rootlyhq/my-service
          nullable: true
        github_repository_branch:
          type: string
          description: 'The GitHub repository branch associated to this service. eg: main'
          nullable: true
        gitlab_repository_name:
          type: string
          description: >-
            The GitLab repository name associated to this service. eg:
            rootlyhq/my-service
          nullable: true
        gitlab_repository_branch:
          type: string
          description: 'The GitLab repository branch associated to this service. eg: main'
          nullable: true
        kubernetes_deployment_name:
          type: string
          description: >-
            The Kubernetes deployment name associated to this service. eg:
            namespace/deployment-name
          nullable: true
        environment_ids:
          type: array
          description: Environments associated with this service
          items:
            type: string
          nullable: true
        service_ids:
          type: array
          description: Services dependent on this service
          items:
            type: string
          nullable: true
        owner_group_ids:
          type: array
          description: Owner Teams associated with this service
          items:
            type: string
          nullable: true
        owner_user_ids:
          type: array
          description: Owner Users associated with this service
          items:
            type: integer
          nullable: true
        alert_urgency_id:
          type: string
          description: The alert urgency id of the service
          nullable: true
        escalation_policy_id:
          type: string
          description: The escalation policy id of the service
          nullable: true
        alerts_email_enabled:
          type: boolean
          description: Enable alerts through email
          nullable: true
        alerts_email_address:
          type: string
          description: Email generated to send alerts to
          nullable: true
        slack_channels:
          type: array
          description: Slack Channels associated with this service
          items:
            type: object
            properties:
              id:
                type: string
                description: Slack channel ID
              name:
                type: string
                description: Slack channel name
            required:
              - id
              - name
          nullable: true
        slack_aliases:
          type: array
          description: Slack Aliases associated with this service
          items:
            type: object
            properties:
              id:
                type: string
                description: Slack alias ID
              name:
                type: string
                description: Slack alias name
            required:
              - id
              - name
          nullable: true
        alert_broadcast_enabled:
          type: boolean
          description: Enable alerts to be broadcasted to a specific channel
          nullable: true
        alert_broadcast_channel:
          type: object
          description: Slack channel to broadcast alerts to
          properties:
            id:
              type: string
              description: Slack channel ID
            name:
              type: string
              description: Slack channel name
          nullable: true
        incident_broadcast_enabled:
          type: boolean
          description: Enable incidents to be broadcasted to a specific channel
          nullable: true
        incident_broadcast_channel:
          type: object
          description: Slack channel to broadcast incidents to
          properties:
            id:
              type: string
              description: Slack channel ID
            name:
              type: string
              description: Slack channel name
          nullable: true
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
        properties:
          type: array
          items:
            type: object
            description: Set a value for a catalog property
            properties:
              catalog_property_id:
                type: string
                description: Catalog property ID
              value:
                type: string
                description: The property value
            required:
              - catalog_property_id
              - value
          description: Array of property values for this service.
          nullable: true
      required:
        - name
        - created_at
        - updated_at
  securitySchemes:
    bearer_auth:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).