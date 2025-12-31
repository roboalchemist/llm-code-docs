# Source: https://developers.notion.com/reference/move-page.md

# Move page

Use this API to move an existing Notion page to a new parent.

## Authentication

Requires [bearer token authentication](https://developers.notion.com/notionapi/reference/authentication) with appropriate [page edit permissions](https://developers.notion.com/reference/capabilities#content-capabilities).

## Path parameters

**`page_id`** (required)

* **Type**: `string` (UUIDv4)
* **Description**: The ID of the page to move
  * This must be a regular Notion page, and not a database. Moving databases or other block types in the API is not currently supported.
* **Format**: UUIDs can be provided with or without dashes
* **Example**: `195de9221179449fab8075a27c979105` or `195de922-1179-449f-ab80-75a27c979105`

## Body parameters

**`parent`** (required)

* **Type**: `object`
* **Description**: The new parent location for the page.
  * The bot must have edit access to the new parent.

The `parent` object can be one of two types:

### Page parent

Move the page under another page:

```json
{
  "parent": {
    "type": "page_id",
    "page_id": "<parent-page-id>"
  }
}
```

* **`type`**: Always `"page_id"`
* **`page_id`**: UUID of the parent page (with or without dashes)

> 🚧 Page parent must be a regular Notion page
>
> The `parent[page_id]` parameter must be a page and cannot be any other type of [block](https://developers.notion.com/notionapi/reference/block).
>
> One limited exception: for databases that only have a single [data source](https://developers.notion.com/notionapi/reference/data-source) , the `database_id` *can* be provided under `page_id`, but this is not recommended, since your integration will start encountering HTTP 400 errors if a second data source is added to the database.

### Database parent

Move the page into a database:

```json
{
  "parent": {
    "type": "data_source_id",
    "data_source_id": "<database-data-source-id>"
  }
}
```

* **`type`**: Always `"data_source_id"`
* **`data_source_id`**: UUID of the database's data source (with or without dashes)

**Note**: You must use `data_source_id` rather than `database_id`. Use the [Retrieve a database](https://developers.notion.com/notionapi/reference/database-retrieve) endpoint to get the child data source ID(s) from the database.

## Example requests

### Move page under another page

```curl
curl -X POST https://api.notion.com/v1/pages/195de9221179449fab8075a27c979105/move \
  -H "Authorization: Bearer secret_xxx" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  -d '{
    "parent": {
      "type": "page_id",
      "page_id": "f336d0bc-b841-465b-8045-024475c079dd"
    }
  }'
```

### Move page into a database

```curl
curl -X POST https://api.notion.com/v1/pages/195de9221179449fab8075a27c979105/move \
  -H "Authorization: Bearer secret_xxx" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  -d '{
    "parent": {
      "type": "data_source_id",
      "data_source_id": "1c7b35e6-e67f-8096-bf3f-000ba938459e"
    }
  }'
```

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Notion API",
    "version": "1"
  },
  "servers": [
    {
      "url": "https://api.notion.com"
    }
  ],
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "oauth2",
        "flows": {}
      }
    }
  },
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/v1/pages/{page_id}/move": {
      "post": {
        "summary": "Move page",
        "description": "Use this API to move an existing Notion page to a new parent.",
        "operationId": "move-page",
        "parameters": [
          {
            "name": "page_id",
            "in": "path",
            "description": "The identifier for the Notion page to be moved.",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "parent"
                ],
                "properties": {
                  "parent": {
                    "type": "object",
                    "description": "Details on the new parent to be applied to the page. Pages can either be moved to an existing page, or an existing data source.",
                    "required": [
                      "type"
                    ],
                    "properties": {
                      "type": {
                        "type": "string",
                        "description": "The type of parent being provided. Either a page (`page_id`) or data source (`data_source_id`).",
                        "enum": [
                          "\"page_id\"",
                          "\"data_source_id\""
                        ]
                      },
                      "page_id": {
                        "type": "string",
                        "description": "When `type=page_id`, this identifies the page to use as the new parent."
                      },
                      "data_source_id": {
                        "type": "string",
                        "description": "When `type=data_source_id`, this identifies the data source under which to move the page."
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"object\": \"page\",\n  \"id\": \"195de922-1179-449f-ab80-75a27c979105\",\n  \"created_time\": \"2025-01-15T10:30:00.000Z\",\n  \"last_edited_time\": \"2025-01-15T14:45:00.000Z\",\n  \"created_by\": {\n    \"object\": \"user\",\n    \"id\": \"abc123...\"\n  },\n  \"last_edited_by\": {\n    \"object\": \"user\",\n    \"id\": \"abc123...\"\n  },\n  \"parent\": {\n    \"type\": \"page_id\",\n    \"page_id\": \"new-parent-id\"\n  },\n  \"archived\": false,\n  \"in_trash\": false,\n  \"properties\": { \"Name\": { \"id\": \"title\" } },\n  \"url\": \"https://notion.so/...\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "object": {
                      "type": "string",
                      "example": "page"
                    },
                    "id": {
                      "type": "string",
                      "example": "195de922-1179-449f-ab80-75a27c979105"
                    },
                    "created_time": {
                      "type": "string",
                      "example": "2025-01-15T10:30:00.000Z"
                    },
                    "last_edited_time": {
                      "type": "string",
                      "example": "2025-01-15T14:45:00.000Z"
                    },
                    "created_by": {
                      "type": "object",
                      "properties": {
                        "object": {
                          "type": "string",
                          "example": "user"
                        },
                        "id": {
                          "type": "string",
                          "example": "abc123..."
                        }
                      }
                    },
                    "last_edited_by": {
                      "type": "object",
                      "properties": {
                        "object": {
                          "type": "string",
                          "example": "user"
                        },
                        "id": {
                          "type": "string",
                          "example": "abc123..."
                        }
                      }
                    },
                    "parent": {
                      "type": "object",
                      "properties": {
                        "type": {
                          "type": "string",
                          "example": "page_id"
                        },
                        "page_id": {
                          "type": "string",
                          "example": "new-parent-id"
                        }
                      }
                    },
                    "archived": {
                      "type": "boolean",
                      "example": false,
                      "default": true
                    },
                    "in_trash": {
                      "type": "boolean",
                      "example": false,
                      "default": true
                    },
                    "properties": {
                      "type": "object",
                      "properties": {
                        "Name": {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "string",
                              "example": "title"
                            }
                          }
                        }
                      }
                    },
                    "url": {
                      "type": "string",
                      "example": "https://notion.so/..."
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "examples": {
                  "Same parent": {
                    "value": "{\n  \"object\": \"error\",\n  \"status\": 400,\n  \"code\": \"validation_error\",\n  \"message\": \"New parent must be different from the current parent\"\n}"
                  },
                  "Self parent": {
                    "value": "{\n  \"object\": \"error\",\n  \"status\": 400,\n  \"code\": \"validation_error\",\n  \"message\": \"Parent ID must be different from the child ID: {page_id}\"\n}"
                  },
                  "Moving page under its own descendant": {
                    "value": "{\n  \"object\": \"error\",\n  \"status\": 400,\n  \"code\": \"validation_error\",\n  \"message\": \"New parent {parent_id} cannot be under the hierarchy of child {page_id}\"\n}"
                  },
                  "Page in trash": {
                    "value": "{\n  \"object\": \"error\",\n  \"status\": 400,\n  \"code\": \"validation_error\",\n  \"message\": \"Object {page_id} is in trash and cannot be moved\"\n}"
                  }
                },
                "schema": {
                  "oneOf": [
                    {
                      "title": "Same parent",
                      "type": "object",
                      "properties": {
                        "object": {
                          "type": "string",
                          "example": "error"
                        },
                        "status": {
                          "type": "integer",
                          "example": 400,
                          "default": 0
                        },
                        "code": {
                          "type": "string",
                          "example": "validation_error"
                        },
                        "message": {
                          "type": "string",
                          "example": "New parent must be different from the current parent"
                        }
                      }
                    },
                    {
                      "title": "Self parent",
                      "type": "object",
                      "properties": {
                        "object": {
                          "type": "string",
                          "example": "error"
                        },
                        "status": {
                          "type": "integer",
                          "example": 400,
                          "default": 0
                        },
                        "code": {
                          "type": "string",
                          "example": "validation_error"
                        },
                        "message": {
                          "type": "string",
                          "example": "Parent ID must be different from the child ID: {page_id}"
                        }
                      }
                    },
                    {
                      "title": "Moving page under its own descendant",
                      "type": "object",
                      "properties": {
                        "object": {
                          "type": "string",
                          "example": "error"
                        },
                        "status": {
                          "type": "integer",
                          "example": 400,
                          "default": 0
                        },
                        "code": {
                          "type": "string",
                          "example": "validation_error"
                        },
                        "message": {
                          "type": "string",
                          "example": "New parent {parent_id} cannot be under the hierarchy of child {page_id}"
                        }
                      }
                    },
                    {
                      "title": "Page in trash",
                      "type": "object",
                      "properties": {
                        "object": {
                          "type": "string",
                          "example": "error"
                        },
                        "status": {
                          "type": "integer",
                          "example": 400,
                          "default": 0
                        },
                        "code": {
                          "type": "string",
                          "example": "validation_error"
                        },
                        "message": {
                          "type": "string",
                          "example": "Object {page_id} is in trash and cannot be moved"
                        }
                      }
                    }
                  ]
                }
              }
            }
          },
          "404": {
            "description": "404",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"object\": \"error\",\n  \"status\": 404,\n  \"code\": \"object_not_found\",\n  \"message\": \"Could not find page with ID: {page_id}. Check that you have access and that you're authenticated to the correct workspace.\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "object": {
                      "type": "string",
                      "example": "error"
                    },
                    "status": {
                      "type": "integer",
                      "example": 404,
                      "default": 0
                    },
                    "code": {
                      "type": "string",
                      "example": "object_not_found"
                    },
                    "message": {
                      "type": "string",
                      "example": "Could not find page with ID: {page_id}. Check that you have access and that you're authenticated to the correct workspace."
                    }
                  }
                }
              }
            }
          }
        },
        "deprecated": false,
        "security": [],
        "x-readme": {
          "code-samples": [
            {
              "language": "curl",
              "code": "# Move page under another page\ncurl -X POST https://api.notion.com/v1/pages/195de9221179449fab8075a27c979105/move \\\n  -H \"Authorization: Bearer secret_xxx\" \\\n  -H \"Notion-Version: 2022-06-28\" \\\n  -H \"Content-Type: application/json\" \\\n  -d '{\n    \"parent\": {\n      \"type\": \"page_id\",\n      \"page_id\": \"f336d0bc-b841-465b-8045-024475c079dd\"\n    }\n  }'\n\n# Move page into a database\ncurl -X POST https://api.notion.com/v1/pages/195de9221179449fab8075a27c979105/move \\\n  -H \"Authorization: Bearer secret_xxx\" \\\n  -H \"Notion-Version: 2022-06-28\" \\\n  -H \"Content-Type: application/json\" \\\n  -d '{\n    \"parent\": {\n      \"type\": \"data_source_id\",\n      \"data_source_id\": \"1c7b35e6-e67f-8096-bf3f-000ba938459e\"\n    }\n  }'"
            }
          ],
          "samples-languages": [
            "curl"
          ]
        }
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": false,
    "proxy-enabled": true
  },
  "x-readme-fauxas": true,
  "_id": "606ecc2cd9e93b0044cf6e47:6900f59bfddfeb0da1a992b7"
}
```