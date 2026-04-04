# Source: https://docs.ox.security/api-documentation/api-reference/api--audit/queries/get-logs-count.md

# getLogsCount

Get the total count of audit logs matching the specified criteria.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetLogsCount($input: GetLogsInput) {
  getLogsCount(input: $input) {
    count
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "input": {
    "logTypes": ["Authentication"],
    "logNames": ["AddCredentials"],
    "userEmails": ["example"],
    "limit": 100,
    "skip": 0,
    "orderBy": {
      "field": "example",
      "direction": "ASC"
    },
    "dateRange": {
      "from": "1672531200000",
      "to": "1704067199000"
    }
  }
}
```

{% endtab %}

{% tab title="cURL" %}

```shell
curl -X POST \
https://api.cloud.ox.security/api/apollo-gateway \
-H 'Content-Type: application/json' \
-H 'Authorization: YOUR_API_TOKEN' \
-d '{
 "query": "query GetLogsCount($input: GetLogsInput) { getLogsCount(input: $input) { count } }",
 "variables": {
    "input": {
      "logTypes": ["Authentication"],
      "logNames": ["AddCredentials"],
      "userEmails": ["example"],
      "limit": 100,
      "skip": 0,
      "orderBy": {
        "field": "example",
        "direction": "ASC"
      },
      "dateRange": {
        "from": "1672531200000",
        "to": "1704067199000"
      }
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetLogsCount($input: GetLogsInput) { getLogsCount(input: $input) { count } }';

fetch("https://api.cloud.ox.security/api/apollo-gateway", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "Authorization": "YOUR_API_TOKEN"
  },
  body: JSON.stringify({
    query: query,
    // This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.
    variables: {
      input: {
        logTypes: ["Authentication"],
        logNames: ["AddCredentials"],
        userEmails: ["example"],
        limit: 100,
        skip: 0,
        orderBy: {
          field: "example",
          direction: "ASC"
        },
        dateRange: {
          from: "1672531200000",
          to: "1704067199000"
        }
      }
    }
  })
})
.then(response => response.json())
.then(result => console.log(JSON.stringify(result, null, 2)))
.catch(error => console.error('Error:', error));
```

{% endtab %}

{% tab title="Python" %}

```python
import requests

query = 'query GetLogsCount($input: GetLogsInput) { getLogsCount(input: $input) { count } }'

response = requests.post(
  "https://api.cloud.ox.security/api/apollo-gateway",
  headers={
    "Content-Type": "application/json",
    "Authorization": "YOUR_API_TOKEN"
  },
  json={
    "query": query,
    # This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.
    "variables": {
      "input": {
        "logTypes": ["Authentication"],
        "logNames": ["AddCredentials"],
        "userEmails": ["example"],
        "limit": 100,
        "skip": 0,
        "orderBy": {
          "field": "example",
          "direction": "ASC"
        },
        "dateRange": {
          "from": "1672531200000",
          "to": "1704067199000"
        }
      }
    }
  }
)

if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
```

{% endtab %}
{% endtabs %}

### Arguments

You can use the following argument(s) to customize your `getLogsCount` query.

| Argument                                                                                                                | Description                               | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| input [`GetLogsInput`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/inputs/get-logs-input) | Filter parameters for counting audit logs | <p>logTypes <a href="../types/enums/log-type"><code>\[LogType!]</code></a><br>logNames <a href="../types/enums/log-name"><code>\[LogName!]</code></a><br>userEmails <code>\[String!]</code><br>limit <code>Float</code><br>skip <code>Float</code><br>orderBy <a href="../types/inputs/log-order-by"><code>LogOrderBy</code></a><br>dateRange <a href="../types/inputs/log-date-range"><code>LogDateRange</code></a></p> |

### Fields

Return type: [`AuditLogCount!`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/audit-log-count)

You can use the following field(s) to specify what information your `getLogsCount` query will return. Please note that some fields may have their own subfields.

| Field         | Description                                | Supported fields |
| ------------- | ------------------------------------------ | ---------------- |
| count `Float` | Total number of matching audit log entries |                  |
