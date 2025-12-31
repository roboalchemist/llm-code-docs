# Source: https://upstash.com/docs/qstash/api-refence/messages/publish-a-message.md

# Publish a Message

> Publish a message to the specified destination



## OpenAPI

````yaml qstash/openapi.yaml post /v2/publish/{destination}
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
  /v2/publish/{destination}:
    post:
      tags:
        - Messages
      summary: Publish a Message
      description: Publish a message to the specified destination
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


            Note that destination must be publicly accessible over the internet.
            If you are working with local endpoints, consider using QStash local
            development server or a public tunnel service.
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


            | Header | Forwarded To Destination As |

            |--------|--------------|

            | Upstash-Forward-My-Header: my-value | My-Header: my-value |

            | Upstash-Forward-Authorization: Bearer <token> | Authorization:
            Bearer <token> |
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
              - 1d1h30m
          description: >
            Specifies the maximum duration the request is allowed to take before
            timing out.


            This parameter can be used to shorten the default allowed timeout
            value on your plan. See `Max HTTP Connection Timeout` on the pricing
            page for default [values](https://upstash.com/pricing/qstash).


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


            By default, QStash uses [exponential
            backoff](/qstash/features/retry). You can override this by providing
            a mathematical expressions to compute next delay. This expression is
            computed after each failed attempt.


            You can use the special variable `retried`, which is how many times
            the message has been retried. The `retried` is 0 for the first
            retry.


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
              - 1d10h30m
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
        - name: Upstash-Not-Before
          in: header
          schema:
            type: integer
          description: >
            Delay the message delivery until a certain timestamp in the future.


            The format is a unix timestamp in seconds, based on the UTC
            timezone.


            When both `Upstash-Not-Before` and `Upstash-Delay` headers are
            provided, `Upstash-Not-Before` will take precedence.
        - name: Upstash-Label
          in: header
          schema:
            type: string
          description: >
            Label to assign to the message for easier identification and
            filtering in logs and DLQ.
        - name: Upstash-Flow-Control-Key
          in: header
          schema:
            type: string
          description: >
            Flow Control Key to use for rate limiting messages.


            Make sure you pass `Upstash-Flow-Control-Value` header as well to
            define the limits for the key.
        - name: Upstash-Flow-Control-Value
          in: header
          schema:
            type: string
          description: >
            Flow Control parallelism, rate and period values to use for rate
            limiting messages for the given key.


            Make sure you pass `Upstash-Flow-Control-Key` header as well to
            define the key.
        - name: Upstash-Deduplication-Id
          in: header
          schema:
            type: string
          description: >
            Deduplication ID to use for de-duplicating messages.


            If a message with the same deduplication ID was published in the
            last 10 minutes, the new message will be ignored.
        - name: Upstash-Content-Based-Deduplication
          in: header
          schema:
            type: string
            enum:
              - 'true'
              - 'false'
            default: 'false'
          description: >
            Enable content based deduplication.


            When enabled, QStash will compute a hash of the message body and use
            it as deduplication ID.

            If a message with the same content was published in the last 10
            minutes, the new message will be ignored.
        - name: Upstash-Callback
          in: header
          schema:
            type: string
          description: >
            You can define a callback url that will be called after message
            delivery, either success or failure. See the content of what will be
            delivered to a callback
            [here](/qstash/features/callbacks#how-do-i-use-callbacks).


            - Callback URL must be prefixed with a valid protocol (http:// or
            https://)

            - Callbacks are charged as a regular message.

            - Callbacks will use the retry setting from the original request.
        - name: Upstash-Callback-Forward-*
          in: header
          schema:
            type: string
          description: >
            You can send custom headers along with your callback message.

            To send a custom header, prefix the header name with
            `Upstash-Callback-Forward-`. We will strip prefix and them to the
            callback URL.


            | Header | Forwarded To Callback Destination As |

            |--------|--------------|

            | Upstash-Callback-Forward-My-Header: my-value | My-Header: my-value
            |

            | Upstash-Callback-Forward-Authorization: Bearer <token> |
            Authorization: Bearer <token> |
        - name: Upstash-Callback-*
          in: header
          schema:
            type: string
          description: >
            You can customize the callback message configuration.


            See [the Configuring
            Callbacks](/qstash/features/callbacks#configuring-callbacks) section
            to learn more.


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


            - Failure callback URL must be prefixed with a valid protocol
            (http:// or https://)

            - Failure callbacks are charged as a regular message.

            - Failure callbacks will use the retry setting from the original
            request.
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


            | Header | Forwarded To Callback Destination As |

            |--------|--------------|

            | Upstash-Failure-Callback-Forward-My-Header: my-value | My-Header:
            my-value |

            | Upstash-Failure-Callback-Forward-Authorization: Bearer <token> |
            Authorization: Bearer <token> |
        - name: Upstash-Failure-Callback-*
          in: header
          schema:
            type: string
          description: >
            You can customize the failure callback message configuration.


            See [the Configuring
            Callbacks](/qstash/features/callbacks#configuring-callbacks) section
            to learn more.


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
          description: Message(s) published successfully
          content:
            application/json:
              schema:
                oneOf:
                  - $ref: '#/components/schemas/PublishResponse'
                    description: Published to a URL destination
                  - type: object
                    description: >-
                      Published to URL Group and created multiple messages for
                      each endpoint the URL Group
                    properties:
                      messages:
                        type: array
                        items:
                          $ref: '#/components/schemas/PublishToUrlGroupResponse'
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    PublishResponse:
      type: object
      properties:
        messageId:
          type: string
          description: >-
            Unique identifier for the published message or the old message ID if
            deduplicated
        deduplicated:
          type: boolean
          description: >-
            Whether this message is a duplicate and was not sent to the
            destination.
    PublishToUrlGroupResponse:
      type: object
      properties:
        messageId:
          type: string
          description: >-
            Unique identifier for the published message or the old message ID if
            deduplicated
        deduplicated:
          type: boolean
          description: >-
            Whether this message is a duplicate and was not sent to the
            destination.
        url:
          type: string
          description: Destination URL of the URL Group endpoint.
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