# Source: https://virustotal.readme.io/reference/graphs-update.md

# Update a graph object

```json
{
  "data":{
    "attributes": {
      "private": true
    },
    "type":"graph"
  }
}
```

```json
{
  "data": {
    "attributes": {
      "private": false,
      "nodes": [
        {
          "type":"domain",
          "entity_id":"www.hooli.com",
          "x":-18,
          "y":65,
          "text":"Root Node",
          "index":0
        },
        {
          "type":"relationship",
          "entity_id":"relationships_resolutions_wwwhoolicom",
          "x":-56,
          "y":42,
          "index":1
        },
        {
          "type":"ip_address",
          "entity_id":"8.8.8.8",
          "x":-64,
          "y":0,
          "index":2,
          "fx":3.3,
          "fy":4.4
        },
        {
          "type":"file",
          "entity_id":"131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267",
          "x":-64,
          "y":0,
          "index":2,
          "fx":3.3,
          "fy":4.4
        },
        {
          "type":"url",
          "entity_id":"1a0556926f7e76419d12e4c6ad52f10388af11f2689f6c0fb6111a2b85f131de",
          "x":-64,
          "y":0,
          "index":2,
          "fx":3.3,
          "fy":4.4
        }
      ],
        "links":[
          {
            "source":"www.hooli.com",
            "target":"relationships_resolutions_wwwhoolicom",
            "connection_type":"resolutions"
          },
          {
            "source":"relationships_resolutions_wwwhoolicom",
            "target":"8.8.8.8",
            "connection_type":"resolutions"
          }
        ],
          "position": {
            "x":897,
              "y":388,
                "scale":"1"
          },
            "graph_data": {
              "description": "Hooli.com graph"
            }
    },
      "type": "graph"
  }
}
```

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "virustotal-api-v3",
    "version": "3.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3"
    }
  ],
  "security": [
    {}
  ],
  "paths": {
    "/graphs/{id}": {
      "patch": {
        "summary": "Update a graph object",
        "description": "",
        "operationId": "graphs-update",
        "parameters": [
          {
            "name": "x-apikey",
            "in": "header",
            "description": "Your API key",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "id",
            "in": "path",
            "description": "A 65 char length id which uniquely identify the graph.",
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
                "properties": {
                  "nodes": {
                    "type": "array",
                    "description": "Array of nodes.",
                    "items": {
                      "properties": {
                        "entity_id": {
                          "type": "string",
                          "description": "Node entity id."
                        },
                        "type": {
                          "type": "string",
                          "description": "Node entity type."
                        },
                        "x": {
                          "type": "number",
                          "description": "X position of the node.",
                          "format": "float"
                        },
                        "y": {
                          "type": "number",
                          "description": "Y position of the node.",
                          "format": "float"
                        },
                        "index": {
                          "type": "integer",
                          "description": "Index of the node list.",
                          "format": "int32"
                        },
                        "fx": {
                          "type": "number",
                          "description": "(optional) Force x position.",
                          "format": "float"
                        },
                        "fy": {
                          "type": "number",
                          "description": "(optional) Force y position.",
                          "format": "float"
                        },
                        "text": {
                          "type": "string",
                          "description": "(optional) Node label."
                        },
                        "entity_attributes": {
                          "type": "object",
                          "description": "(optional) Entity related attributes."
                        }
                      },
                      "type": "object"
                    }
                  },
                  "links": {
                    "type": "array",
                    "description": "Array of links.",
                    "items": {
                      "properties": {
                        "source": {
                          "type": "string",
                          "description": "Entity id of the link source."
                        },
                        "target": {
                          "type": "string",
                          "description": "Entity id of the link target."
                        },
                        "connection_type": {
                          "type": "string",
                          "description": "Type of the connection between the source and the target."
                        }
                      },
                      "type": "object"
                    }
                  },
                  "graph_data": {
                    "type": "object",
                    "description": "Highlevel graph data.",
                    "properties": {
                      "version": {
                        "type": "string",
                        "description": "Current version of the graph."
                      }
                    }
                  },
                  "private": {
                    "type": "boolean",
                    "description": "Private status."
                  }
                }
              }
            }
          }
        },
        "deprecated": false,
        "security": []
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": true,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```