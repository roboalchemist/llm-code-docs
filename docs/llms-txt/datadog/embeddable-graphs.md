# Source: https://docs.datadoghq.com/api/latest/embeddable-graphs.md

---
title: Embeddable Graphs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Embeddable Graphs
---

# Embeddable Graphs

Manage embeddable graphs through the API. See [Embeddable Graphs with Template Variables](https://docs.datadoghq.com/dashboards/guide/embeddable-graphs-with-template-variables/) for more information.

## Revoke embed{% #revoke-embed %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/graph/embed/{embed_id}/revoke |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/graph/embed/{embed_id}/revoke |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/graph/embed/{embed_id}/revoke      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/graph/embed/{embed_id}/revoke      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/graph/embed/{embed_id}/revoke     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/graph/embed/{embed_id}/revoke |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/graph/embed/{embed_id}/revoke |

### Overview

Revoke a specified embed. This endpoint requires the `embeddable_graphs_share` permission.

### Arguments

#### Path Parameters

| Name                       | Type   | Description      |
| -------------------------- | ------ | ---------------- |
| embed_id [*required*] | string | ID of the embed. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A JSON object containing the success message

| Field   | Type   | Description |
| ------- | ------ | ----------- |
| success | string | Message.    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "success": "Embed 00000000000 successfully enabled."
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not found
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

##### 
                  \# Path parametersexport embed_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/graph/embed/${embed_id}/revoke" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}

## Enable embed{% #enable-embed %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/graph/embed/{embed_id}/enable |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/graph/embed/{embed_id}/enable |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/graph/embed/{embed_id}/enable      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/graph/embed/{embed_id}/enable      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/graph/embed/{embed_id}/enable     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/graph/embed/{embed_id}/enable |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/graph/embed/{embed_id}/enable |

### Overview

Enable a specified embed. This endpoint requires the `embeddable_graphs_share` permission.

### Arguments

#### Path Parameters

| Name                       | Type   | Description      |
| -------------------------- | ------ | ---------------- |
| embed_id [*required*] | string | ID of the embed. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A JSON object containing the success message

| Field   | Type   | Description |
| ------- | ------ | ----------- |
| success | string | Message.    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "success": "Embed 00000000000 successfully enabled."
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not found
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

##### 
                  \# Path parametersexport embed_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/graph/embed/${embed_id}/enable" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}

## Get specific embed{% #get-specific-embed %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                    |
| ----------------- | --------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/graph/embed/{embed_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/graph/embed/{embed_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/graph/embed/{embed_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/graph/embed/{embed_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/graph/embed/{embed_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/graph/embed/{embed_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/graph/embed/{embed_id} |

### Overview

Get the HTML fragment for a previously generated embed with `embed_id`.

### Arguments

#### Path Parameters

| Name                       | Type   | Description         |
| -------------------------- | ------ | ------------------- |
| embed_id [*required*] | string | Token of the embed. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Embeddable graph.

| Field       | Type    | Description                                           |
| ----------- | ------- | ----------------------------------------------------- |
| dash_name   | string  | Name of the dashboard the graph is on (null if none). |
| dash_url    | string  | URL of the dashboard the graph is on (null if none).  |
| embed_id    | string  | ID of the embed.                                      |
| graph_title | string  | Title of the graph.                                   |
| html        | string  | HTML fragment for the embed (iframe).                 |
| revoked     | boolean | Boolean flag for whether or not the embed is revoked. |
| shared_by   | int64   | ID of the use who shared the embed.                   |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not found
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

##### 
                  \# Path parametersexport embed_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/graph/embed/${embed_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}

## Create embed{% #create-embed %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                          |
| ----------------- | ----------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/graph/embed |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/graph/embed |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/graph/embed      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/graph/embed      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/graph/embed     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/graph/embed |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/graph/embed |

### Overview



Creates a new embeddable graph.

Note: If an embed already exists for the exact same query in a given organization, the older embed is returned instead of creating a new embed.

If you are interested in using template variables, see [Embeddable Graphs with Template Variables](https://docs.datadoghq.com/dashboards/faq/embeddable-graphs-with-template-variables).
This endpoint requires the `embeddable_graphs_share` permission.


### Request

#### Body Data (required)

Embeddable Graph body

{% tab title="Model" %}

| Field                        | Type   | Description                                                                            |
| ---------------------------- | ------ | -------------------------------------------------------------------------------------- |
| graph_json [*required*] | string | The graph definition in JSON.                                                          | Same format that is available on the JSON tab of the graph editor. |
| legend                       | enum   | The flag determining if the graph includes a legend. Allowed enum values: `yes,no`     |
| size                         | enum   | The size of the graph. Allowed enum values: `small,medium,large,xlarge`                |
| timeframe                    | enum   | The timeframe for the graph. Allowed enum values: `1_hour,4_hours,1_day,2_days,1_week` |
| title                        | string | Determines graph title. Must be at least 1 character.                                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "graph_json": "",
  "legend": "string",
  "size": "string",
  "timeframe": "string",
  "title": "string"
}
```

{% /tab %}

### Response

{% tab title="200" %}
Payload accepted
{% tab title="Model" %}
Embeddable graph.

| Field       | Type    | Description                                           |
| ----------- | ------- | ----------------------------------------------------- |
| dash_name   | string  | Name of the dashboard the graph is on (null if none). |
| dash_url    | string  | URL of the dashboard the graph is on (null if none).  |
| embed_id    | string  | ID of the embed.                                      |
| graph_title | string  | Title of the graph.                                   |
| html        | string  | HTML fragment for the embed (iframe).                 |
| revoked     | boolean | Boolean flag for whether or not the embed is revoked. |
| shared_by   | int64   | ID of the use who shared the embed.                   |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

##### 
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/graph/embed" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "graph_json": ""
}
EOF
                
{% /tab %}

## Get all embeds{% #get-all-embeds %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                         |
| ----------------- | ---------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/graph/embed |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/graph/embed |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/graph/embed      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/graph/embed      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/graph/embed     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/graph/embed |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/graph/embed |

### Overview

Gets a list of previously created embeddable graphs.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response with embeddable graphs.

| Parent field    | Field           | Type     | Description                                           |
| --------------- | --------------- | -------- | ----------------------------------------------------- |
|                 | embedded_graphs | [object] | List of embeddable graphs.                            |
| embedded_graphs | dash_name       | string   | Name of the dashboard the graph is on (null if none). |
| embedded_graphs | dash_url        | string   | URL of the dashboard the graph is on (null if none).  |
| embedded_graphs | embed_id        | string   | ID of the embed.                                      |
| embedded_graphs | graph_title     | string   | Title of the graph.                                   |
| embedded_graphs | html            | string   | HTML fragment for the embed (iframe).                 |
| embedded_graphs | revoked         | boolean  | Boolean flag for whether or not the embed is revoked. |
| embedded_graphs | shared_by       | int64    | ID of the use who shared the embed.                   |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="403" %}
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

##### 
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/graph/embed" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}
