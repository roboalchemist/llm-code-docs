# Source: https://virustotal.readme.io/reference/graphs.md

# Search graphs

Endpoint used to search graphs.

There are a set of multiple modifiers that you can use to refine your search results. You can combine all of them together and use them in conjunction with AND, OR and NOT operators.

Date and numeric fields support the suffix plus or minus to match values greater or less than the passed value. If not sign has been added to the modifier, you will get exact matches. You can use more than once the same modifier in the same query to define ranges: `creation_date:2018-11-1+` `creation_date:2018-11-12-` will match graphs created between 2018-11-1 and 2018-11-22.

**Graph-related modifiers**

| Modifier              | Description                                        | Example                                                              |
| :-------------------- | :------------------------------------------------- | :------------------------------------------------------------------- |
| id:                   | Filters by graph identifier.                       | id:g675a2fd4c8834e288afd71bbbe88f78884e7d21a8c9348b5ab45cc9281cffc3c |
| name:                 | Filters by graph name.                             | name:Wannacry                                                        |
| owner:                | Filters by graphs owned by user.                   | owner:richard\_hendricks                                             |
| group:                | Filters by graphs owned by group.                  | group:piedpiper                                                      |
| visible\_to\_user:    | Filters by graphs visible to user.                 | visible\_to\_user:richard\_hendricks                                 |
| visible\_to\_group:   | Filters by graphs visible to group.                | visible\_to\_group:piedpiper                                         |
| private:              | Filters by private graphs.                         | private:true, private:false                                          |
| creation\_date:       | Filters by the graph creation date.                | creation\_date:2018-11-1                                             |
| last\_modified\_date: | Filters by the last date the graph was modified.   | last\_modified\_date:2018-11-12                                      |
| total\_nodes:         | Filters by graphs containing some amount of nodes. | total\_nodes:100                                                     |
| comments\_count:      | Filter by the number of comments of the graph.     | comments\_count:10+                                                  |
| views\_count:         | Filter by the number of graph views.               | views\_count:1000+                                                   |

**Node-related modifiers**

| Modifier     | Description                                              | Example                                                               |
| :----------- | :------------------------------------------------------- | :-------------------------------------------------------------------- |
| label:       | Filters by graphs containing nodes with a specific label | label:Kill switch                                                     |
| file:        | Filters by graphs containing the file.                   | file:131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267 |
| domain:      | Filters by graphs containing the domain.                 | domain:piedpiper.com                                                  |
| ip\_address: | Filters by graphs containing the ip address.             | ip\_address:1.1.1.1                                                   |
| url:         | Filters by graphs containing the url.                    | url:<https://piedpiper.com/the-box/>                                  |
| actor:       | Filters by graphs containing the actor.                  | actor:funny bear                                                      |
| victim:      | Filters by graphs containing the victim.                 | victim:richard\_hendricks                                             |
| email:       | Filters by graphs containing the email.                  | email:<richard@piedpiper.com>                                         |
| department:  | Filters by graphs containing the department.             | department:engineers                                                  |

In addition to these modifiers, you can do a free search query. The search engine will return graphs that match the query with the content of any field in the graph.

```curl All graphs
curl --request POST \
  --url https://www.virustotal.com/api/v3/graphs \
  --header 'x-apikey: <your API key>'
```
```curl FIlter by user
curl --request POST \
  --url https://www.virustotal.com/api/v3/graphs?filter=owner:bbunny \
  --header 'x-apikey: <your API key>'
```
```curl Attributes selection
curl --request POST \
  --url https://www.virustotal.com/api/v3/graphs?filter=owner:bbunny&attributes=private,graph_data \
  --header 'x-apikey: <your API key>'
```
```curl Filter by domain
curl --request POST \
  --url https://www.virustotal.com/api/v3/graphs?filter=domain:hooli.com \
  --header 'x-apikey: <your API key>'
```

Supported `order` fields are: `name`, `owner`, `creation_date`, `last_modified_date`, `views_count` and `comments_count`.

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
    "/graphs": {
      "get": {
        "summary": "Search graphs",
        "description": "",
        "operationId": "graphs",
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
            "name": "filter",
            "in": "query",
            "description": "Return the graphs matching the given criteria only",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Maximum number graphs to retrieve",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "cursor",
            "in": "query",
            "description": "Continuation cursor",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "order",
            "in": "query",
            "description": "Sort order",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "attributes",
            "in": "query",
            "description": "Specific fields to retrieve",
            "schema": {
              "type": "string"
            }
          }
        ],
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