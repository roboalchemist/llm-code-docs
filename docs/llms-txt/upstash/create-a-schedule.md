# Source: https://upstash.com/docs/qstash/api-refence/schedules/create-a-schedule.md

# Create a Schedule

> Create a schedule to send messages periodically



## OpenAPI

````yaml qstash/openapi.yaml post /v2/schedules/{destination}
openapi: 3.1.0
info:
  title: QStash REST API
  description: |
    QStash is a message queue and scheduler built on top of Upstash Redis.
  version: 2.0.0
  contact:
    name: Upstash
    url: https://upstash.com
servers:
  - url: https://qstash.upstash.io
security:
  - bearerAuth: []
  - bearerAuthQuery: []
tags:
  - name: Messages
    description: Publish and manage messages
  - name: Queues
    description: Manage message queues
  - name: Schedules
    description: Create and manage scheduled messages
  - name: URL Groups
    description: Manage URL groups and endpoints
  - name: DLQ
    description: Dead Letter Queue operations
  - name: Logs
    description: Log operations
  - name: Signing Keys
    description: Manage signing keys
  - name: Flow Control
    description: Monitor flow control keys
paths:
  /v2/schedules/{destination}:
    post:
      tags:
        - Schedules
      summary: Create a Schedule
      description: Create a schedule to send messages periodically
      parameters:
        - name: destination
          in: path
          required: true
          schema:
            type: string
          description: >
            Destination can either be a valid URL where the message gets sent
            to, or a URL Group name. 

            - If the destination is a URL, make sure the URL is prefixed with a
            valid protocol (http:// or https://)

            - If the destination is a URL Group, a new message will be created
            for each endpoint in the group.
        - name: Upstash-Cron
          in: header
          required: true
          schema:
            type: string
            examples:
              - '*/5 * * * *'
              - CRON_TZ=America/New_York */5 * * * *
          description: >
            Cron expression defining the schedule frequency. QStash republishes
            this message whenever the cron expression triggers.


            Timezones are supported and can be specified with the cron
            expression. 


            The maximum schedule resolution is 1 minute.
        - name: Upstash-Schedule-Id
          in: header
          schema:
            type: string
          description: >
            Assign a custom schedule ID to the created schedule. This header
            allows you to set the schedule ID yourself instead of QStash
            assigning a random ID.


            If a schedule with the provided ID exists, the settings of the
            existing schedule will be updated with the new settings.
        - name: Content-Type
          in: header
          schema:
            type: string
          description: >
            `Content-Type` is the MIME type of the message.


            We highly recommend sending a `Content-Type` header along, as this
            will help your destination API to understand the content of the
            message.


            Set this to whatever data you are sending through QStash, if your
            message is json, then use `application/json`. Some frameworks like
            Next.js will not parse your body correctly if the content type is
            not correct.


            Examples:

            - `application/json`

            - `application/xml`

            - `application/octet-stream`

            - `text/plain`
        - name: Upstash-Method
          in: header
          schema:
            type: string
            enum:
              - GET
              - POST
              - PUT
              - PATCH
              - DELETE
            default: POST
          description: The HTTP method to use when sending the request to your API.
        - name: Upstash-Timeout
          in: header
          schema:
            type: string
            examples:
              - 5s
              - 2m
              - 1h
          description: >
            Specifies the maximum duration the request is allowed to take before
            timing out.


            This parameter can be used to shorten the default allowed timeout
            value on your plan. See Max HTTP Connection Timeout on the pricing
            page for default values.


            The format of this header is `<value><unit>` where value is a number
            and unit is one of:

            - `s` for seconds

            - `m` for minutes

            - `h` for hours.
        - name: Upstash-Retries
          in: header
          schema:
            type: integer
          description: >
            How many times should this message be retried in case the
            destination API returns an error or is not available.

            The total number of deliveries is 1 (initial attempt) + retries.


            If it is not provided, the plan default retry value will be used:

            - Free Plan: 3 retries

            - Paid Plans: 5 retries
        - name: Upstash-Retry-Delay
          in: header
          schema:
            type: string
          description: >
            Customize the delay between retry attempts when message delivery
            fails.


            By default, QStash uses exponential backoff. You can override this
            by providing a mathematical expressions to compute next delay. This
            expression is computed after each failed attempt.


            You can use the special variable `retried`, which is current retry
            attempt. The `retried` is 0 for the first retry. This variable is
            provided during computation of the expression by QStash.


            Supported functions: 

            | Function    | Description                          |

            |-------------|--------------------------------------|

            | `pow(x, y)`| Returns x raised to the power of y|

            | `exp(x)`| Returns e raised to the power of x|

            | `sqrt(x)`| Takes the square root of x|

            | `abs(x)`| Returns the absolute value of x|

            | `floor(x)`| Returns the largest integer less than or equal to x|

            | `ceil(x)`| Returns the smallest integer greater than or equal to
            x|

            | `round(x)`| Rounds x to the nearest integer|

            | `min(x, y)`| Returns the smaller of x and y|

            | `max(x, y)`| Returns the larger of x and y|


            Examples:

            - `1000`: Fixed 1 second delay

            - `1000 * (1 + retried)`: Linear backoff

            - `pow(2, retried) * 1000`: Exponential backoff

            - `max(1000, pow(2, retried) * 100)`: Exponential with minimum 1s
            delay
        - name: Upstash-Delay
          in: header
          schema:
            type: string
            examples:
              - 50s
              - 1d10m
              - 10h
              - 1d
          description: >
            Delay the message delivery.


            The format of this header is `<value><unit>` where value is a number
            and unit is one of:

            - `s` for seconds

            - `m` for minutes

            - `h` for hours.

            - `d` for days.
        - name: Upstash-Forward-*
          in: header
          schema:
            type: string
          description: >
            You can send custom headers to your endpoint along with your
            message.


            To send a custom header, prefix the header name with
            `Upstash-Forward-`. We will strip prefix and send them to the
            destination.


            | Header | Forwarded As |

            |--------|--------------|

            | Upstash-Forward-My-Header: my-value | My-Header: my-value |

            | Upstash-Forward-Authorization: Bearer <token> | Authorization:
            Bearer <token> |
        - name: Upstash-Callback
          in: header
          schema:
            type: string
          description: >
            You can define a callback url that will be called after each
            attempt. See the content of what will be delivered to a callback
            here

            The callback URL must be prefixed with a valid protocol (http:// or
            https://)


            Callbacks are charged as a regular message.

            Callbacks will use the retry setting from the original request.
        - name: Upstash-Callback-Forward-*
          in: header
          schema:
            type: string
          description: >
            You can send custom headers along with your callback message.

            To send a custom header, prefix the header name with
            `Upstash-Callback-Forward-`. We will strip prefix and them to the
            callback URL.


            Example: 

            - `Upstash-Callback-Forward-My-Header: my-value` will be forwarded
            as `My-Header: my-value` to your callback destination.
        - name: Upstash-Callback-*
          in: header
          schema:
            type: string
          description: >
            You can customize the callback message configuration.


            | Header | Description |

            |--------|--------------|

            | Upstash-Callback-Method | HTTP method to use for the callback
            request. Default is POST. |

            | Upstash-Callback-Timeout | Timeout for the callback request.
            Format is same as Upstash-Timeout header. |

            | Upstash-Callback-Retries | Number of retries for the callback
            request. Default is same as original message retries. |

            | Upstash-Callback-Retry-Delay | Retry delay for the callback
            request. Format is same as Upstash-Retry-Delay header. |
        - name: Upstash-Failure-Callback
          in: header
          schema:
            type: string
          description: >
            You can define a failure callback url that will be called when a
            delivery is failed. That is when all the defined retries are
            exhausted. See the content of what will be delivered to a failure
            callback here

            The failure callback url must be prefixed with a valid protocol
            (http:// or https://)

            Callbacks are charged as a regular message.

            Callbacks will use the retry setting from the original request.
        - name: Upstash-Failure-Callback-Forward-*
          in: header
          schema:
            type: string
          description: >
            You can send custom headers along with your failure callback
            message.

            To send a custom header, prefix the header name with
            `Upstash-Failure-Callback-Forward-`. We will strip prefix and them
            to the failure callback URL.


            Example: 

            - `Upstash-Failure-Callback-Forward-My-Header: my-value` will be
            forwarded as `My-Header: my-value` to your failure callback
            destination.
        - name: Upstash-Failure-Callback-*
          in: header
          schema:
            type: string
          description: >
            You can customize the failure callback message configuration.


            | Header | Description |

            |--------|--------------|

            | Upstash-Failure-Callback-Method | HTTP method to use for the
            callback request. Default is POST. |

            | Upstash-Failure-Callback-Timeout | Timeout for the callback
            request. Format is same as Upstash-Timeout header. |

            | Upstash-Failure-Callback-Retries | Number of retries for the
            callback request. Default is same as original message retries. |

            | Upstash-Failure-Callback-Retry-Delay | Retry delay for the
            callback request. Format is same as Upstash-Retry-Delay header. |
      requestBody:
        description: The raw request message passed to the endpoints as is
        content:
          text/plain:
            schema:
              type: string
          application/json:
            schema:
              type: object
          application/octet-stream:
            schema:
              type: string
              format: binary
      responses:
        '200':
          description: Schedule created successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  scheduleId:
                    type: string
                    description: Unique identifier for the schedule
        '400':
          description: >-
            Schedule ID is invalid. Schedule IDs can only contain alphanumeric
            characters, hyphens, periods, and underscores.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '412':
          description: Exceeded the maximum number of schedules allowed.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    Error:
      type: object
      required:
        - error
      properties:
        error:
          type: string
          description: Error message
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: QStash authentication token
    bearerAuthQuery:
      type: apiKey
      in: query
      name: qstash_token
      description: QStash authentication token passed as a query parameter

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://upstash.com/docs/llms.txt