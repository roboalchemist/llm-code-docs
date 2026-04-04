# Source: https://developer.mixpanel.com/reference/import-events.md

# Import Events

Use this API to send batches of events from your servers to Mixpanel.

## Request Format

Each request ingests a batch of events into Mixpanel. We accept up to 2000 events and 10MB uncompressed per request. Events are part of the request body.

We support Content-Type `application/json` or `application/x-ndjson`:

```json JSON
[
  {"event": "Signup", "properties": {"time": 1618716477000,"distinct_id": "91304156-cafc-4673-a237-623d1129c801","$insert_id": "29fc2962-6d9c-455d-95ad-95b84f09b9e4","Referred by": "Friend","URL": "mixpanel.com/signup"}},
  {"event": "Purchase", "properties": {"time": 1618716477000,"distinct_id": "91304156-cafc-4673-a237-623d1129c801","$insert_id": "935d87b1-00cd-41b7-be34-b9d98dd08b42","Item": "Coffee", "Amount": 5.0}}
]
```

```json ndJSON
{"event": "Signup", "properties": {"time": 1618716477000,"distinct_id": "91304156-cafc-4673-a237-623d1129c801","$insert_id": "29fc2962-6d9c-455d-95ad-95b84f09b9e4","Referred by": "Friend","URL": "mixpanel.com/signup"}}
{"event": "Purchase", "properties": {"time": 1618716477000,"distinct_id": "91304156-cafc-4673-a237-623d1129c801","$insert_id": "935d87b1-00cd-41b7-be34-b9d98dd08b42","Item": "Coffee", "Amount": 5.0}}
```

We also support `Content-Encoding: gzip` to reduce network egress.

## Authentication

`/import` requires an Owner or Admin [Service Account](https://developer.mixpanel.com/reference/service-accounts). project\_id, service account username, and service account password are required to authenticate a request.

`/import` also supports [Project Token](https://developer.mixpanel.com/reference/project-token) as an authentication method. You can provide your token as the basic auth username value with an empty password. If project\_id is not specified, the request will be authenticated using the provided token.

## Validation

If you provide the `strict=1` parameter (recommended), `/import` will validate the supplied events and return a 400 status code if **any** of the events fail validation with details of the error. If some events pass validation and others fail, Mixpanel will ingest the events that pass validation. When you encounter a 400 error in production, simply log the JSON response, as it will contain the `$insert_id`s of the invalid events, which can be used to debug.

### High-level requirements

* Each event must be properly formatted JSON.
* Each event must contain an event name, time, distinct\_id, and $insert\_id. These are used to deduplicate events so that this endpoint can be safely retried.
* Each event must be smaller than 1MB of uncompressed JSON.
* Each event must have fewer than 255 properties.
* All nested object properties must have fewer than 255 keys and a max nesting depth is 3.
* All array properties must have fewer than 255 elements.

### Example of an event

```json JSON
{
  "event": "Signed up",
  "properties": {
    "time": 1618716477000,
    "distinct_id": "91304156-cafc-4673-a237-623d1129c801",
    "$insert_id": "29fc2962-6d9c-455d-95ad-95b84f09b9e4",
    "ip": "136.24.0.114",
    "Referred by": "Friend",
    "URL": "mixpanel.com/signup",
  }
}
```

#### event

This is the name of the event. If you're loading data from a data warehouse, we recommend using the name of the table as the name of the event.

We recommend keeping the number of unique event names relatively small and using properties for any variable context attached to the event. For example, instead of tracking events with names "Paid Signup" and "Free Signup", we would recommend tracking an event called "Signup" and having a property "Account Type" with the value "paid" or "free".

#### properties

This is a JSON object representing all the properties about the event. If you're loading data from a data warehouse, we recommend using column names as the names of properties.

##### properties.time

The time at which the event occurred, in seconds or milliseconds since epoch. We require a value for time. We will reject events with time values that are before 1971-01-01 or more than 1 hour in the future as measured on our servers.

If the time value is set in the future, it will be overwritten with the current present time at ingestion.

##### properties.distinct\_id

`distinct_id` identifies the user who performed the event. distinct\_id must be specified on every event, as it is crucial for Mixpanel to perform behavioral analysis (unique users, funnels, retention, cohorts) correctly and efficiently.

If the event is not associated with any user, set distinct\_id to the empty string. Events with an empty distinct\_id will be excluded from all behavioral analysis.

To prevent accidental implementation mistakes, we disallow the following values for distinct\_id:

```
- 00000000-0000-0000-0000-000000000000
- anon
- anonymous
- nil
- none
- null
- n/a
- na
- undefined
- unknown
- <nil>
- 0
- -1
- true
- false
- []
- {}
```

##### properties.$insert\_id

We require that $insert\_id be specified on every event. $insert\_id provides a unique identifier for the event, which we use for deduplication. Events with identical values for (event, time, distinct\_id, $insert\_id) are considered duplicates and only one of them will be surfaced in queries.

$insert\_ids must be ≤ 36 bytes and contain only alphanumeric characters or "-". We also disallow any value for $insert\_id from the list of invalid IDs provided for distinct\_id above.

### Example of a validation error

```json JSON
{
  "code": 400,
  "error": "some data points in the request failed validation",
  "failed_records": [
    {
      "index": 0,
      "$insert_id": "8a66058c-a56d-4ef6-8123-28b7c9f7e82f",
      "field": "properties.time",
      "message": "properties.time' is invalid: must be specified as seconds since epoch"
    },
    {
      "index": 3,
      "$insert_id": "29fc2962-6d9c-455d-95ad-95b84f09b9e4",
      "field": "properties.utm_source",
      "message": "properties.utm_source is invalid: string should be valid utf8"
    },
  ],
  "num_records_imported": 23,
  "status": "Bad Request"
}
```

When any single event in the batch does not pass validation, we return a 400 status code and a response that looks like the above.

`failed_records` includes one row for each of the failed events, with details about the error we found. If some of the rows passed validation, we will ingest them and return their count in `num_records_imported`.

## GeoIP Enrichment

If you supply a property `ip` with an IP address, Mixpanel will automatically do a GeoIP lookup and replace the `ip` property with geographic properties (City, Country, Region). These properties can be used in our UI to segment events geographically.

If you do not supply an `ip` property in your event payload, the IP address of the request will be used to parse for geolocation. You can set manually set the value of `ip` to `0` and our API will skip the geolocation parsing for that event.

This is an example of an event before and after enrichment:

```json Pre-Enrichment
{
  "event": "Signed up",
  "properties": {
    "time": 1618716477000,
    "distinct_id": "91304156-cafc-4673-a237-623d1129c801",
    "$insert_id": "29fc2962-6d9c-455d-95ad-95b84f09b9e4",
    "ip": "136.24.0.114",
    "Referred by": "Friend",
    "URL": "mixpanel.com/signup",
  }
}
```

```json Post-Enrichment
{
  "event": "Signed up",
  "properties": {
    "time": 1618716477000,
    "distinct_id": "91304156-cafc-4673-a237-623d1129c801",
    "$insert_id": "29fc2962-6d9c-455d-95ad-95b84f09b9e4",
    "Referred by": "Friend",
    "URL": "mixpanel.com/signup",
    "$city": "San Francisco",
    "$region": "California",
    "mp_country_code": "US"
  }
}
```

## Rate Limit

To ensure real-time ingestion and quality-of-service, we have a rate limit of 2GB of uncompressed JSON/minute or \~30k events per second, measured on a rolling 1 minute basis.

We recommend the following when it comes to sending data to our API at scale:

* Send data as quickly as possible with concurrent clients until the server returns 429. We see the best results with 10-20 concurrent clients sending 2K events per batch.
* When you see 429s, employ an [exponential backoff with jitter](https://docs.aws.amazon.com/general/latest/gr/api-retries.html) strategy. We recommend starting with a backoff of 2s and doubling backoff until 60s, with 1-5s of jitter.
* We recommend gzip compression and using `Content-Encoding: gzip` to reduce network egress and transfer time.
* In the rare event that our API returns a 502 or 503 status code, we recommend employing the same exponential backoff strategy as with 429s.
* Please do not retry validation errors (400 status code), as they will consistently fail and count toward the rate limit.

If you are an enterprise customer and require a higher limit for a 1-time backfill, please reach out to your sales representative with your project\_id and use-case.

## Common Issues

`$insert_id` is required on all events. This makes it safe to retry `/import` requests. If your events don't already have a unique ID (eg: a UUID/GUID), we recommend computing a hash of some set of properties that make the event semantically unique (eg: distinct\_id + timestamp + some other property) and using the first 36 characters of that hash as the $insert\_id.

We truncate all strings down to 255 characters. Here's what we recommend for the various cases in which this typically happens:

* URLs: We recommend parsing the URL and tracking its individual components (host, path, url params) as properties. This is more useful in analysis, as you can segment events by hostname or a particular URL parameter.
* JSON encoded strings: Sometimes a long string may be a JSON object encoded as a string. We recommend parsing the JSON and flattening it into properties to send with the event. This is similarly much more useful in analysis, as you can filter or breakdown by any key within the JSON.
* Free text / user generated content: Some long fields may include full-text (eg: a search term or a comment). If this property isn't useful for analysis, we recommend excluding it from tracking to Mixpanel to avoid accidentally sending over any PII.

## Guides

See our Cloud Ingestion guides for example usage of this API to integrate with  [Google Pub/Sub](https://docs.mixpanel.com/docs/tracking-methods/integrations/google-pubsub), [Amazon S3](https://docs.mixpanel.com/docs/tracking-methods/integrations/amazon-s3), or [Google Cloud Storage](https://docs.mixpanel.com/docs/tracking-methods/integrations/google-cloud-storage).

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
    "/import": {
      "post": {
        "tags": [
          "Events"
        ],
        "operationId": "import-events",
        "security": [
          {
            "ServiceAccount": []
          },
          {
            "ProjectSecret": []
          },
          {
            "OAuthToken": []
          }
        ],
        "summary": "Import Events",
        "description": "",
        "parameters": [
          {
            "in": "query",
            "name": "strict",
            "required": true,
            "schema": {
              "type": "string",
              "default": "1",
              "enum": [
                "0",
                "1"
              ]
            },
            "description": "When set to 1 (recommended), Mixpanel will validate the batch and return errors per event that failed."
          },
          {
            "in": "query",
            "name": "project_id",
            "required": true,
            "schema": {
              "default": "<YOUR_PROJECT_ID>",
              "type": "string"
            },
            "description": "The Mixpanel project_id, used to authenticate service account credentials."
          },
          {
            "in": "header",
            "name": "Content-Type",
            "schema": {
              "type": "string",
              "default": "application/json",
              "enum": [
                "application/json",
                "application/x-ndjson"
              ]
            }
          },
          {
            "in": "header",
            "name": "Content-Encoding",
            "schema": {
              "type": "string",
              "enum": [
                "gzip"
              ]
            }
          }
        ],
        "requestBody": {
          "required": true,
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
                      "required": [
                        "time",
                        "$insert_id",
                        "distinct_id"
                      ],
                      "properties": {
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
            "$ref": "#/components/responses/StrictReceived"
          },
          "400": {
            "$ref": "#/components/responses/StrictInvalid"
          },
          "401": {
            "$ref": "#/components/responses/StrictUnauthorized"
          },
          "413": {
            "$ref": "#/components/responses/StrictTooLarge"
          },
          "429": {
            "$ref": "#/components/responses/RateLimitExceeded"
          }
        }
      }
    }
  },
  "components": {
    "securitySchemes": {
      "ServiceAccount": {
        "type": "http",
        "scheme": "basic",
        "description": "Service Account"
      },
      "ProjectSecret": {
        "type": "http",
        "scheme": "basic",
        "description": "Project Secret"
      },
      "OAuthToken": {
        "type": "http",
        "scheme": "bearer",
        "description": "OAuth Token"
      }
    },
    "responses": {
      "StrictReceived": {
        "description": "A 200 response indicates all records were successfully ingested.",
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "properties": {
                "code": {
                  "type": "integer"
                },
                "num_records_imported": {
                  "type": "integer"
                },
                "status": {
                  "type": "string"
                }
              },
              "example": {
                "code": 200,
                "num_records_imported": 2000,
                "status": "OK"
              }
            }
          }
        }
      },
      "StrictInvalid": {
        "description": "A 400 response indicates that some records failed validation.",
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "properties": {
                "code": {
                  "type": "integer"
                },
                "error": {
                  "type": "string"
                },
                "status": {
                  "type": "string"
                },
                "num_records_imported": {
                  "type": "integer"
                },
                "failed_records": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "index": {
                        "type": "number"
                      },
                      "insert_id": {
                        "type": "string"
                      },
                      "field": {
                        "type": "string"
                      },
                      "message": {
                        "type": "string"
                      }
                    }
                  }
                }
              },
              "example": {
                "code": 400,
                "num_records_imported": 999,
                "status": "Bad Request",
                "failed_records": [
                  {
                    "index": 0,
                    "insert_id": "13c0b661-f48b-51cd-ba54-97c5999169c0",
                    "field": "properties.time",
                    "message": "'properties.time' is invalid: must be specified as seconds since epoch"
                  }
                ]
              }
            }
          }
        }
      },
      "StrictUnauthorized": {
        "description": "A 401 response indicates invalid credentials.",
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "properties": {
                "code": {
                  "type": "integer"
                },
                "error": {
                  "type": "string"
                },
                "status": {
                  "type": "string"
                }
              },
              "example": {
                "code": 401,
                "error": "Invalid credentials",
                "status": "Unauthorized"
              }
            }
          }
        }
      },
      "StrictTooLarge": {
        "description": "A 413 response indicates that the payload is too large.",
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "properties": {
                "code": {
                  "type": "integer"
                },
                "error": {
                  "type": "string"
                },
                "status": {
                  "type": "string"
                }
              },
              "example": {
                "code": 413,
                "error": "request exceeds max limit of 2097152 bytes",
                "status": "Request Entity Too Large"
              }
            }
          }
        }
      },
      "RateLimitExceeded": {
        "description": "A 429 response indicates rate limits have been exceeded.",
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "properties": {
                "code": {
                  "type": "integer"
                },
                "error": {
                  "type": "string"
                },
                "status": {
                  "type": "string"
                }
              },
              "example": {
                "code": 429,
                "error": "Project exceeded rate limits. Please retry the request with exponential backoff.",
                "status": "Too Many Requests"
              }
            }
          }
        }
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