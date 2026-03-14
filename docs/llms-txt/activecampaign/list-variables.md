# Source: https://developers.activecampaign.com/reference/list-variables.md

# List Variables

Retrieve a list of personalization variables

```json GET /personalizations (Example RESPONSE)
{
  "personalizations": [
    {
      "name": "address",
      "tag": "awesometag",
      "format": "html",
      "content": "this is the first content",
      "listIds": "1,2,3",
      "listNames": "List1,List2,List3",
      "listsCount": "3",
			"isLocked": false,
      "links": [
        
      ],
      "id": "1"
    },
    {
      "name": "phone",
      "tag": "greattag",
      "format": "html",
      "content": "this is the second one",
      "listIds": "3,4",
      "listNames": "List3,List4",
      "listsCount": "2",
			"isLocked": false,
      "links": [
        
      ],
      "id": "2"
    },
    {
      "name": "nice\n",
      "tag": "hellotag",
      "format": "text",
      "content": "this is the third one",
      "listIds": "1,3",
      "listNames": "List1,List3",
      "listsCount": "2",
			"isLocked": false,
      "links": [
        
      ],
      "id": "3"
    },
    {
      "name": "hahah",
      "tag": "goodtag",
      "format": "html",
      "content": "fourth",
      "listIds": "1,4",
      "listNames": "List1,List4",
      "listsCount": "2",
			"isLocked": false,
      "links": [
        
      ],
      "id": "4"
    },
    {
      "name": "hello world",
      "tag": "nicetag",
      "format": "text",
      "content": "fifth",
      "listIds": "2,3,4",
      "listNames": "List2,List3,List4",
      "listsCount": "3",
			"isLocked": true,
      "links": [
        
      ],
      "id": "5"
    }
  ],
  "meta": {
    "total": "5"
  }
}
```

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "v3",
    "version": "3"
  },
  "servers": [
    {
      "url": "https://{youraccountname}.api-us1.com/api/3",
      "variables": {
        "youraccountname": {
          "default": "youraccountname"
        }
      }
    }
  ],
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "apiKey",
        "name": "Api-Token",
        "in": "header",
        "x-default": ""
      }
    }
  },
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/personalizations": {
      "get": {
        "summary": "List Variables",
        "description": "Retrieve a list of personalization variables",
        "operationId": "list-variables",
        "parameters": [
          {
            "name": "orders[format]",
            "in": "query",
            "description": "Order variables by format (ASC/DESC)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "orders[tag]",
            "in": "query",
            "description": "Order variables by tag (ASC/DESC)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "orders[name]",
            "in": "query",
            "description": "Order variables by name (ASC/DESC)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "orders[content]",
            "in": "query",
            "description": "Order variables by content (ASC/DESC)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filter[name]",
            "in": "query",
            "description": "Filter by variable name",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filter[tag]",
            "in": "query",
            "description": "Filter by variable tag",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filter[listName]",
            "in": "query",
            "description": "Filter by name of list",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filter[content]",
            "in": "query",
            "description": "Contents of variable",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filter[format]",
            "in": "query",
            "description": "Filter by tag format (html, text)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Result limit (Default: 20)",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 20
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "personalizations": [
                        {
                          "name": "address",
                          "tag": "awesometag",
                          "format": "html",
                          "content": "this is the first content",
                          "listIds": "1,2,3",
                          "listNames": "List1,List2,List3",
                          "listsCount": "3",
                          "isLocked": false,
                          "links": [],
                          "id": "1"
                        },
                        {
                          "name": "phone",
                          "tag": "greattag",
                          "format": "html",
                          "content": "this is the second one",
                          "listIds": "3,4",
                          "listNames": "List3,List4",
                          "listsCount": "2",
                          "isLocked": false,
                          "links": [],
                          "id": "2"
                        },
                        {
                          "name": "nice\n",
                          "tag": "hellotag",
                          "format": "text",
                          "content": "this is the third one",
                          "listIds": "1,3",
                          "listNames": "List1,List3",
                          "listsCount": "2",
                          "isLocked": false,
                          "links": [],
                          "id": "3"
                        },
                        {
                          "name": "hahah",
                          "tag": "goodtag",
                          "format": "html",
                          "content": "fourth",
                          "listIds": "1,4",
                          "listNames": "List1,List4",
                          "listsCount": "2",
                          "isLocked": false,
                          "links": [],
                          "id": "4"
                        },
                        {
                          "name": "hello world",
                          "tag": "nicetag",
                          "format": "text",
                          "content": "fifth",
                          "listIds": "2,3,4",
                          "listNames": "List2,List3,List4",
                          "listsCount": "3",
                          "isLocked": true,
                          "links": [],
                          "id": "5"
                        }
                      ],
                      "meta": {
                        "total": "5"
                      }
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "personalizations": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "name": {
                            "type": "string",
                            "example": "address"
                          },
                          "tag": {
                            "type": "string",
                            "example": "awesometag"
                          },
                          "format": {
                            "type": "string",
                            "example": "html"
                          },
                          "content": {
                            "type": "string",
                            "example": "this is the first content"
                          },
                          "listIds": {
                            "type": "string",
                            "example": "1,2,3"
                          },
                          "listNames": {
                            "type": "string",
                            "example": "List1,List2,List3"
                          },
                          "links": {
                            "type": "array"
                          },
                          "id": {
                            "type": "string",
                            "example": "1"
                          }
                        }
                      }
                    },
                    "meta": {
                      "type": "object",
                      "properties": {
                        "total": {
                          "type": "string",
                          "example": "5"
                        }
                      }
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
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          }
        },
        "deprecated": false
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": false,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```