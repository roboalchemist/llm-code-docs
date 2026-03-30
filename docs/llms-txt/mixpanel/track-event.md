# Source: https://developer.mixpanel.com/reference/track-event.md

# Track Events

Track events to Mixpanel from client devices. We recommend using one of our client-side SDKs instead of using /track directly, as our SDKs provide queueing, retrying, batching, and more.

## When to use /track vs /import

Typically, we recommend using /import for server-side integrations as it is more scalable and supports ingesting historical data. We only recommend /track for client-side tracking in an environment for which we don't have SDK support or if you're sending data via some other untrusted environment (eg: third-party webhooks that send data to Mixpanel).

|                             | /track                                         | /import                                                               |
| --------------------------- | ---------------------------------------------- | --------------------------------------------------------------------- |
| Events per request          | 2000                                           | 2000                                                                  |
| Authentication              | Project Token, intended for untrusted clients. | Project Secret/Service Account, intended for server-side integration. |
| Compression                 | Gzip allowed                                   | Gzip allowed                                                          |
| Content-Type                | application/x-www-form-urlencoded              | application/json or application/x-ndjson                              |
| Ingesting historical events | Last 5 days only.                              | Any time after 1971-01-01.                                            |

## Limits

The limits for track are the same as /import, [see here](https://developer.mixpanel.com/reference/import-events#rate-limits).

Each event has the following size limits:

* Must be smaller than 1MB of uncompressed JSON.
* Must have fewer than 255 properties.
* All nested object properties must have fewer than 255 keys and max nesting depth is 3.
* All array properties must have fewer than 255 elements.

To ensure real-time ingestion and quality-of-service, we have a rate limit of 2GB of uncompressed JSON/minute or \~30k events per second, measured on a rolling 1 minute basis.

We recommend the following when it comes to sending data to our API at scale:

* Send data as quickly as possible with concurrent clients until the server returns 429. We see the best results with 10-20 concurrent clients sending 2K events per batch.
* When you see 429s, employ an [exponential backoff with jitter](https://docs.aws.amazon.com/general/latest/gr/api-retries.html) strategy. We recommend starting with a backoff of 2s and doubling backoff until 60s, with 1-5s of jitter.
* We recommend gzip compression and using `Content-Encoding: gzip` to reduce network egress and transfer time.
* In the rare event that our API returns a 502 or 503 status code, we recommend employing the same exponential backoff strategy as with 429s.
* Please do not retry validation errors (400 status code), as they will consistently fail and count toward the rate limit.

If you are an Enterprise customer that requires a higher rate limit, please reach out to your CSM with your `project_id` and use case.

# OpenAPI definition

```json
{
  "openapi": "3.0.2",
  "info": {
    "title": "Ingestion API",
    "description": "APIs allowing for event-based tracking and user profile handling.",
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "version": "1.0.0",
    "contact": {
      "url": "https://mixpanel.com/get-support"
    }
  },
  "servers": [
    {
      "url": "https://{region}.mixpanel.com",
      "description": "Mixpanel's data collection server.",
      "variables": {
        "region": {
          "default": "api",
          "enum": [
            "api",
            "api-eu",
            "api-in"
          ],
          "description": "The server location to be used:\n  * `api` - The default (US) servers used for most projects\n  * `api-eu` - EU servers if you are enrolled in EU Data Residency\n  * `api-in` - India servers if you are enrolled in India Data Residency\n"
        }
      }
    }
  ],
  "tags": [
    {
      "name": "Events",
      "description": "Track events."
    }
  ],
  "paths": {
    "/track": {
      "post": {
        "operationId": "track-event",
        "tags": [
          "Events"
        ],
        "summary": "Track Events",
        "description": "",
        "security": [
          {}
        ],
        "parameters": [
          {
            "$ref": "#/components/parameters/UseIpAsDistinctId"
          },
          {
            "$ref": "#/components/parameters/Verbose"
          },
          {
            "$ref": "#/components/parameters/PNGPixel"
          },
          {
            "$ref": "#/components/parameters/JavascriptWithCallback"
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "array",
                "minItems": 1,
                "items": {
                  "type": "object",
                  "required": [
                    "event",
                    "properties"
                  ],
                  "properties": {
                    "event": {
                      "type": "string",
                      "title": "event",
                      "description": "The name of the event."
                    },
                    "properties": {
                      "type": "object",
                      "title": "properties",
                      "description": "A JSON object containing properties of the event.",
                      "properties": {
                        "token": {
                          "type": "string",
                          "title": "token",
                          "description": "Project token."
                        },
                        "time": {
                          "type": "integer",
                          "title": "time",
                          "description": "The time at which the event occurred, in seconds or milliseconds since UTC epoch. If the time value is set in the future, it will be overwritten with the current present time at ingestion."
                        },
                        "distinct_id": {
                          "type": "string",
                          "title": "distinct_id",
                          "description": "The unique identifier of the user who performed the event."
                        },
                        "$insert_id": {
                          "type": "string",
                          "title": "$insert_id",
                          "description": "A unique identifier for the event, used for deduplication. Events with identical values for (event, time, distinct_id, $insert_id) are considered duplicates; only the latest ingested one will be considered in queries."
                        }
                      },
                      "additionalProperties": true
                    }
                  },
                  "additionalProperties": false
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/Received"
          },
          "401": {
            "$ref": "#/components/responses/Unauthorized"
          },
          "403": {
            "$ref": "#/components/responses/Forbidden"
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "ErrorResponse": {
        "type": "object",
        "properties": {
          "error": {
            "type": "string"
          },
          "status": {
            "type": "string",
            "enum": [
              "error"
            ]
          }
        }
      },
      "IntegerPropertyAsBooleanFlag": {
        "type": "integer",
        "minimum": 0,
        "maximum": 1
      }
    },
    "responses": {
      "Received": {
        "content": {
          "text/plain": {
            "schema": {
              "type": "integer",
              "enum": [
                1,
                0
              ]
            },
            "examples": {
              "Valid Data": {
                "value": 1
              },
              "Invalid Data": {
                "value": 0
              }
            }
          }
        },
        "description": "\n* `1` - One or more objects provided are valid. This does not signify a valid project token or secret.\n* `0` - No data objects in the body are valid.\n"
      },
      "Unauthorized": {
        "description": "Unauthorized",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ErrorResponse"
            }
          }
        }
      },
      "Forbidden": {
        "description": "Forbidden",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ErrorResponse"
            }
          }
        }
      }
    },
    "parameters": {
      "UseIpAsDistinctId": {
        "in": "query",
        "name": "ip",
        "required": false,
        "schema": {
          "$ref": "#/components/schemas/IntegerPropertyAsBooleanFlag"
        },
        "description": "If present and equal to 1, Mixpanel will use the ip address of the incoming request and compute a distinct_id using a hash function if no distinct_id is provided. This is different from providing a `properties.ip` value in the Event Object."
      },
      "Verbose": {
        "in": "query",
        "name": "verbose",
        "required": false,
        "schema": {
          "$ref": "#/components/schemas/IntegerPropertyAsBooleanFlag"
        },
        "description": "If present and equal to 1, Mixpanel will respond with a JSON Object describing the success or failure of the tracking call. The returned object will have two keys: `status`, with the value 1 on success and 0 on failure, and `error`, with a string-valued error message if the request wasn't successful. This is useful for debugging during implementation."
      },
      "PNGPixel": {
        "in": "query",
        "name": "img",
        "required": false,
        "schema": {
          "$ref": "#/components/schemas/IntegerPropertyAsBooleanFlag"
        },
        "description": "If present and equal to 1, Mixpanel will serve a 1x1 transparent pixel image as a response to the request. This is useful for adding [Pixel Tracking](https://en.wikipedia.org/wiki/Web_beacon) in places that javascript is not supported."
      },
      "JavascriptWithCallback": {
        "in": "query",
        "name": "callback",
        "required": false,
        "schema": {
          "type": "string"
        },
        "description": "If present, Mixpanel will return a `content-type: text/javascript` with a body that calls a function by value provided. This is useful for creating local callbacks to a successful track call in JavaScript."
      }
    }
  },
  "x-readme-deploy-id": "ingestion",
  "x-explorer-enabled": true,
  "x-proxy-enabled": true,
  "x-samples-enabled": true,
  "x-samples-languages": [
    "curl",
    "node",
    "ruby",
    "javascript",
    "python"
  ]
}
```