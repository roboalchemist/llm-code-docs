# Source: https://developer.mixpanel.com/reference/replace-lookup-table.md

# Replace a Lookup Table

Lookup Tables must be [created via our UI](https://docs.mixpanel.com/docs/data-structure/lookup-tables#how-do-i-upload-a-lookup-table). Once a Lookup Table is created, its contents can be replaced via this API.

```sh
curl -XPUT 'https://api.mixpanel.com/lookup-tables/ID?project_id={YOUR_PROJECT_ID}' \
     -u 'SERVICE_ACCOUNT_USER:SERVICE_ACCOUNT_PASS' \
     -H 'Content-Type: text/csv' \
     --data 'id,artist,genre,is_platinum,name,num_listens,release_date,is_top_40
c994bb,Drake,Pop,True,Hotline Bling,1700000000,2015-10-18T22:00:00,true
d8d949,Gipsy Kings,Flamenco,False,Bamboleo,1170000,1987-07-12T05:00:00,false
a43fb8,Daft Punk,House,False,Aerodynamic,41000000,2001-03-12T07:30:00,false
'
```

```python
import requests

data = """id,artist,genre,is_platinum,name,num_listens,release_date,is_top_40
c994bb,Drake,Pop,True,Hotline Bling,1700000000,2015-10-18T22:00:00,true
d8d949,Gipsy Kings,Flamenco,False,Bamboleo,1170000,1987-07-12T05:00:00,false
a43fb8,Daft Punk,House,False,Aerodynamic,41000000,2001-03-12T07:30:00,false
"""

id = "LOOKUP_TABLE_ID"
project_id = "PROJECT_ID"

resp = requests.put(
    f"https://api.mixpanel.com/lookup-tables/{id}?project_id={project_id}",
    headers={"Content-Type": "text/csv",
    auth=(SERVICE_ACCOUNT_USER, SERVICE_ACCOUNT_PASS),
    data=data
)
print(resp.json()
```

### Validation

* The first column of the lookup table is assumed to be the ID of the row. All ID values must be unique.
* The first row of the lookup table is a header row. The values in the header must be unique, as each one uniquely identifies a column of the table. These will appear as properties of the lookup table in Mixpanel's UI.
* The CSV must be valid according to RFC4180.
* If the `Content-Encoding: gzip` header is supplied, the table will be decompressed before parsing.

#### Types

* Integers or floats will be parsed as numbers.
* RFC3339 timestamps (`2021-08-21T05:36:01Z`) will parsed as datetimes.
* `true` or `false` (case-insensitive) will be parsed as boolean.
* Empty fields (two adjacent commas) will be treated as `undefined`
* Comma separated, quoted strings in square brackets (`"[""Free"",""Paid"",""Enterprise""]"`) will be parsed as list of strings.
* All other values will be treated as strings.

#### Errors

Lookup Tables are replaced in their entirety or not replaced at all. When the Lookup Table fails to meet the above validation, we return an error that looks as follows:

```json
{
  "error": "some data points in the request failed validation",
  "failed_records": [
    {
      "index": 2,
      "message": "invalid row: row indexes 1 and 2 have the same primary key"
    },
    {
      "index": 3,
      "message": "invalid row: wrong number of fields"
    }
  ],
  "status": 0
}
```

We will return at most the first 10 rows that failed validation.

### Limits

This endpoint will return a 429 error if called more than 100 times in a rolling 24 hour window. We recommend updating lookup tables at most hourly to stay within this limit.

This endpoint will return a 413 error if a Lookup Table exceeds 100MB uncompressed. In practice, this translates to 1-2M rows. If you have a lookup table that exceeds the limit, we recommend pruning the number of columns to those that are useful to analysis. Removing long URLs or user-generated content can bring a lookup table within this limit. If you still exceed the limit, please reach out to us at [apis@mixpanel.com](mailto:apis@mixpanel.com) -- we'd love to hear your use case!

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
      "name": "Lookup Tables",
      "description": "Enrich existing event and profile properties"
    }
  ],
  "paths": {
    "/lookup-tables/{id}": {
      "put": {
        "operationId": "replace-lookup-table",
        "tags": [
          "Lookup Tables"
        ],
        "security": [
          {
            "ServiceAccount": []
          },
          {
            "ProjectSecret": []
          }
        ],
        "summary": "Replace a Lookup Table",
        "description": "",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "The ID of the lookup table to replace which can be retreived from Lexicon under the lookup table's details, click [here](https://docs.mixpanel.com/docs/data-structure/lookup-tables#where-can-i-find-the-id-of-the-lookup-table-for-apis-path-params) for more info."
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
              "default": "text/csv",
              "enum": [
                "text/csv"
              ]
            }
          }
        ],
        "requestBody": {
          "content": {
            "text/csv": {
              "schema": {
                "type": "string",
                "format": "blob",
                "default": "id,field1,field2\nkey1,v1,z1\nkey2,z1,z2\n"
              }
            }
          }
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/LookupTableReceived"
          },
          "400": {
            "$ref": "#/components/responses/LookupTableInvalid"
          },
          "401": {
            "$ref": "#/components/responses/StrictUnauthorized"
          },
          "404": {
            "$ref": "#/components/responses/StrictNotFound"
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
      }
    },
    "responses": {
      "LookupTableReceived": {
        "description": "A 200 response indicates all records were successfully ingested.",
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "properties": {
                "code": {
                  "type": "integer"
                },
                "status": {
                  "type": "string"
                }
              },
              "example": {
                "code": 200,
                "status": "OK"
              }
            }
          }
        }
      },
      "LookupTableInvalid": {
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
                "failed_records": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "index": {
                        "type": "number"
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
                "error": "Some data points in the request failed validation.",
                "status": "Bad Request",
                "failed_records": [
                  {
                    "index": 2,
                    "message": "primary key is required and cannot be blank"
                  },
                  {
                    "index": 3,
                    "message": "invalid row: wrong number of fields"
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
      "StrictNotFound": {
        "description": "A 404 response indicates that the entity to replace was not found.",
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
                "code": 200,
                "error": "Lookup table with id 'f077cb07-008a-4955-8a4a-b4c163db3a87' was not found.",
                "status": "Not Found"
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