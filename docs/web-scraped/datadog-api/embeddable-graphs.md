# Source: https://docs.datadoghq.com/api/latest/embeddable-graphs/

# Embeddable Graphs
Manage embeddable graphs through the API. See [Embeddable Graphs with Template Variables](https://docs.datadoghq.com/dashboards/guide/embeddable-graphs-with-template-variables/) for more information.
## [Revoke embed](https://docs.datadoghq.com/api/latest/embeddable-graphs/#revoke-embed)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/embeddable-graphs/#revoke-embed-v1)


GET https://api.ap1.datadoghq.com/api/v1/graph/embed/{embed_id}/revokehttps://api.ap2.datadoghq.com/api/v1/graph/embed/{embed_id}/revokehttps://api.datadoghq.eu/api/v1/graph/embed/{embed_id}/revokehttps://api.ddog-gov.com/api/v1/graph/embed/{embed_id}/revokehttps://api.datadoghq.com/api/v1/graph/embed/{embed_id}/revokehttps://api.us3.datadoghq.com/api/v1/graph/embed/{embed_id}/revokehttps://api.us5.datadoghq.com/api/v1/graph/embed/{embed_id}/revoke
### Overview
Revoke a specified embed. This endpoint requires the `embeddable_graphs_share` permission.
### Arguments
#### Path Parameters
Name
Type
Description
embed_id [_required_]
string
ID of the embed.
### Response
  * [200](https://docs.datadoghq.com/api/latest/embeddable-graphs/#RevokeEmbeddableGraph-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/embeddable-graphs/#RevokeEmbeddableGraph-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/embeddable-graphs/#RevokeEmbeddableGraph-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/embeddable-graphs/#RevokeEmbeddableGraph-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/embeddable-graphs/)
  * [Example](https://docs.datadoghq.com/api/latest/embeddable-graphs/)


A JSON object containing the success message
Expand All
Field
Type
Description
success
string
Message.
```
{
  "success": "Embed 00000000000 successfully enabled."
}
```

Copy
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/embeddable-graphs/)
  * [Example](https://docs.datadoghq.com/api/latest/embeddable-graphs/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not found
  * [Model](https://docs.datadoghq.com/api/latest/embeddable-graphs/)
  * [Example](https://docs.datadoghq.com/api/latest/embeddable-graphs/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/embeddable-graphs/)
  * [Example](https://docs.datadoghq.com/api/latest/embeddable-graphs/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/embeddable-graphs/?code-lang=curl)


#####  Revoke embed
Copy
```
                  # Path parameters  
export embed_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/graph/embed/${embed_id}/revoke" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

* * *
## [Enable embed](https://docs.datadoghq.com/api/latest/embeddable-graphs/#enable-embed)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/embeddable-graphs/#enable-embed-v1)


GET https://api.ap1.datadoghq.com/api/v1/graph/embed/{embed_id}/enablehttps://api.ap2.datadoghq.com/api/v1/graph/embed/{embed_id}/enablehttps://api.datadoghq.eu/api/v1/graph/embed/{embed_id}/enablehttps://api.ddog-gov.com/api/v1/graph/embed/{embed_id}/enablehttps://api.datadoghq.com/api/v1/graph/embed/{embed_id}/enablehttps://api.us3.datadoghq.com/api/v1/graph/embed/{embed_id}/enablehttps://api.us5.datadoghq.com/api/v1/graph/embed/{embed_id}/enable
### Overview
Enable a specified embed. This endpoint requires the `embeddable_graphs_share` permission.
### Arguments
#### Path Parameters
Name
Type
Description
embed_id [_required_]
string
ID of the embed.
### Response
  * [200](https://docs.datadoghq.com/api/latest/embeddable-graphs/#EnableEmbeddableGraph-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/embeddable-graphs/#EnableEmbeddableGraph-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/embeddable-graphs/#EnableEmbeddableGraph-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/embeddable-graphs/#EnableEmbeddableGraph-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/embeddable-graphs/)
  * [Example](https://docs.datadoghq.com/api/latest/embeddable-graphs/)


A JSON object containing the success message
Expand All
Field
Type
Description
success
string
Message.
```
{
  "success": "Embed 00000000000 successfully enabled."
}
```

Copy
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/embeddable-graphs/)
  * [Example](https://docs.datadoghq.com/api/latest/embeddable-graphs/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not found
  * [Model](https://docs.datadoghq.com/api/latest/embeddable-graphs/)
  * [Example](https://docs.datadoghq.com/api/latest/embeddable-graphs/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/embeddable-graphs/)
  * [Example](https://docs.datadoghq.com/api/latest/embeddable-graphs/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/embeddable-graphs/?code-lang=curl)


#####  Enable embed
Copy
```
                  # Path parameters  
export embed_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/graph/embed/${embed_id}/enable" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

* * *
## [Get specific embed](https://docs.datadoghq.com/api/latest/embeddable-graphs/#get-specific-embed)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/embeddable-graphs/#get-specific-embed-v1)


GET https://api.ap1.datadoghq.com/api/v1/graph/embed/{embed_id}https://api.ap2.datadoghq.com/api/v1/graph/embed/{embed_id}https://api.datadoghq.eu/api/v1/graph/embed/{embed_id}https://api.ddog-gov.com/api/v1/graph/embed/{embed_id}https://api.datadoghq.com/api/v1/graph/embed/{embed_id}https://api.us3.datadoghq.com/api/v1/graph/embed/{embed_id}https://api.us5.datadoghq.com/api/v1/graph/embed/{embed_id}
### Overview
Get the HTML fragment for a previously generated embed with `embed_id`.
### Arguments
#### Path Parameters
Name
Type
Description
embed_id [_required_]
string
Token of the embed.
### Response
  * [200](https://docs.datadoghq.com/api/latest/embeddable-graphs/#GetEmbeddableGraph-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/embeddable-graphs/#GetEmbeddableGraph-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/embeddable-graphs/#GetEmbeddableGraph-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/embeddable-graphs/#GetEmbeddableGraph-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/embeddable-graphs/)
  * [Example](https://docs.datadoghq.com/api/latest/embeddable-graphs/)


Embeddable graph.
Expand All
Field
Type
Description
dash_name
string
Name of the dashboard the graph is on (null if none).
dash_url
string
URL of the dashboard the graph is on (null if none).
embed_id
string
ID of the embed.
graph_title
string
Title of the graph.
html
string
HTML fragment for the embed (iframe).
revoked
boolean
Boolean flag for whether or not the embed is revoked.
shared_by
int64
ID of the use who shared the embed.
```
{
  "dash_name": "string",
  "dash_url": "string",
  "embed_id": "string",
  "graph_title": "string",
  "html": "string",
  "revoked": false,
  "shared_by": "integer"
}
```

Copy
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/embeddable-graphs/)
  * [Example](https://docs.datadoghq.com/api/latest/embeddable-graphs/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not found
  * [Model](https://docs.datadoghq.com/api/latest/embeddable-graphs/)
  * [Example](https://docs.datadoghq.com/api/latest/embeddable-graphs/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/embeddable-graphs/)
  * [Example](https://docs.datadoghq.com/api/latest/embeddable-graphs/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/embeddable-graphs/?code-lang=curl)


#####  Get specific embed
Copy
```
                  # Path parameters  
export embed_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/graph/embed/${embed_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

* * *
## [Create embed](https://docs.datadoghq.com/api/latest/embeddable-graphs/#create-embed)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/embeddable-graphs/#create-embed-v1)


POST https://api.ap1.datadoghq.com/api/v1/graph/embedhttps://api.ap2.datadoghq.com/api/v1/graph/embedhttps://api.datadoghq.eu/api/v1/graph/embedhttps://api.ddog-gov.com/api/v1/graph/embedhttps://api.datadoghq.com/api/v1/graph/embedhttps://api.us3.datadoghq.com/api/v1/graph/embedhttps://api.us5.datadoghq.com/api/v1/graph/embed
### Overview
Creates a new embeddable graph.
Note: If an embed already exists for the exact same query in a given organization, the older embed is returned instead of creating a new embed.
If you are interested in using template variables, see [Embeddable Graphs with Template Variables](https://docs.datadoghq.com/dashboards/faq/embeddable-graphs-with-template-variables).
This endpoint requires the `embeddable_graphs_share` permission.
### Request
#### Body Data (required)
Embeddable Graph body
  * [Model](https://docs.datadoghq.com/api/latest/embeddable-graphs/)
  * [Example](https://docs.datadoghq.com/api/latest/embeddable-graphs/)


Expand All
Field
Type
Description
graph_json [_required_]
string
The graph definition in JSON.
Same format that is available on the JSON tab of the graph editor.
legend
enum
The flag determining if the graph includes a legend. Allowed enum values: `yes,no`
default: `no`
size
enum
The size of the graph. Allowed enum values: `small,medium,large,xlarge`
default: `medium`
timeframe
enum
The timeframe for the graph. Allowed enum values: `1_hour,4_hours,1_day,2_days,1_week`
default: `1_hour`
title
string
Determines graph title. Must be at least 1 character.
default: `Embed created through API`
```
{
  "graph_json": "",
  "legend": "string",
  "size": "string",
  "timeframe": "string",
  "title": "string"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/embeddable-graphs/#CreateEmbeddableGraph-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/embeddable-graphs/#CreateEmbeddableGraph-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/embeddable-graphs/#CreateEmbeddableGraph-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/embeddable-graphs/#CreateEmbeddableGraph-429-v1)


Payload accepted
  * [Model](https://docs.datadoghq.com/api/latest/embeddable-graphs/)
  * [Example](https://docs.datadoghq.com/api/latest/embeddable-graphs/)


Embeddable graph.
Expand All
Field
Type
Description
dash_name
string
Name of the dashboard the graph is on (null if none).
dash_url
string
URL of the dashboard the graph is on (null if none).
embed_id
string
ID of the embed.
graph_title
string
Title of the graph.
html
string
HTML fragment for the embed (iframe).
revoked
boolean
Boolean flag for whether or not the embed is revoked.
shared_by
int64
ID of the use who shared the embed.
```
{
  "dash_name": "string",
  "dash_url": "string",
  "embed_id": "string",
  "graph_title": "string",
  "html": "string",
  "revoked": false,
  "shared_by": "integer"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/embeddable-graphs/)
  * [Example](https://docs.datadoghq.com/api/latest/embeddable-graphs/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/embeddable-graphs/)
  * [Example](https://docs.datadoghq.com/api/latest/embeddable-graphs/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/embeddable-graphs/)
  * [Example](https://docs.datadoghq.com/api/latest/embeddable-graphs/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/embeddable-graphs/?code-lang=curl)


#####  Create embed
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/graph/embed" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "graph_json": ""
}
EOF  

                
```

* * *
## [Get all embeds](https://docs.datadoghq.com/api/latest/embeddable-graphs/#get-all-embeds)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/embeddable-graphs/#get-all-embeds-v1)


GET https://api.ap1.datadoghq.com/api/v1/graph/embedhttps://api.ap2.datadoghq.com/api/v1/graph/embedhttps://api.datadoghq.eu/api/v1/graph/embedhttps://api.ddog-gov.com/api/v1/graph/embedhttps://api.datadoghq.com/api/v1/graph/embedhttps://api.us3.datadoghq.com/api/v1/graph/embedhttps://api.us5.datadoghq.com/api/v1/graph/embed
### Overview
Gets a list of previously created embeddable graphs.
### Response
  * [200](https://docs.datadoghq.com/api/latest/embeddable-graphs/#ListEmbeddableGraphs-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/embeddable-graphs/#ListEmbeddableGraphs-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/embeddable-graphs/#ListEmbeddableGraphs-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/embeddable-graphs/)
  * [Example](https://docs.datadoghq.com/api/latest/embeddable-graphs/)


Response with embeddable graphs.
Field
Type
Description
embedded_graphs
[object]
List of embeddable graphs.
dash_name
string
Name of the dashboard the graph is on (null if none).
dash_url
string
URL of the dashboard the graph is on (null if none).
embed_id
string
ID of the embed.
graph_title
string
Title of the graph.
html
string
HTML fragment for the embed (iframe).
revoked
boolean
Boolean flag for whether or not the embed is revoked.
shared_by
int64
ID of the use who shared the embed.
```
{
  "embedded_graphs": [
    {
      "dash_name": "string",
      "dash_url": "string",
      "embed_id": "string",
      "graph_title": "string",
      "html": "string",
      "revoked": false,
      "shared_by": "integer"
    }
  ]
}
```

Copy
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/embeddable-graphs/)
  * [Example](https://docs.datadoghq.com/api/latest/embeddable-graphs/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/embeddable-graphs/)
  * [Example](https://docs.datadoghq.com/api/latest/embeddable-graphs/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/embeddable-graphs/?code-lang=curl)


#####  Get all embeds
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/graph/embed" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

* * *
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=fd9aa011-ce81-43d3-87f0-bcd076dfdcd2&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=34972677-6c1f-4022-b59b-da703673f644&pt=Embeddable%20Graphs&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fembeddable-graphs%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=fd9aa011-ce81-43d3-87f0-bcd076dfdcd2&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=34972677-6c1f-4022-b59b-da703673f644&pt=Embeddable%20Graphs&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fembeddable-graphs%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=039bf8d6-d5e7-445e-a511-d08471592dbc&bo=2&sid=aa811b10f0bf11f0ab045579f582e260&vid=aa815aa0f0bf11f0b365ed070b1e7cb2&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Embeddable%20Graphs&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fembeddable-graphs%2F&r=&lt=1033&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=444324)
