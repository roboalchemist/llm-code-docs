# Source: https://docs.carv.io/d.a.t.a.-ai-framework/api-documentation/on-chain-data-sql-query.md

# On-chain Data SQL Query

## Schema

If you want to leverage LLM to generate sql queries, you can refer to below schemas as prompt to the LLM:

1. [Ethereum Schema](https://docs.carv.io/d.a.t.a.-ai-framework/api-documentation/on-chain-data-sql-query/ethereum-schema)
2. [BTC Schema](https://docs.carv.io/d.a.t.a.-ai-framework/api-documentation/on-chain-data-sql-query/bitcoin-schema)
3. [Base Schema](https://docs.carv.io/d.a.t.a.-ai-framework/api-documentation/on-chain-data-sql-query/base-schema)
4. [Solana Schema](https://docs.carv.io/d.a.t.a.-ai-framework/api-documentation/on-chain-data-sql-query/solana-schema)

### **POST /ai-agent-backend/sql\_query**

This endpoint allows you to send SQL queries to the CARV backend to fetch on-chain data.

#### **Request Parameters**

| Name         | Location | Type   | Required | Description                   |
| ------------ | -------- | ------ | -------- | ----------------------------- |
| sql\_content | Body     | string | Yes      | The SQL query to be executed. |

#### **Example Request**

```http
curl -X POST https://interface.carv.io/ai-agent-backend/sql_query \
     -H "Content-Type: application/json" \
     -H "Authorization: <YOUR_AUTH_TOKEN>" \
     -d '{"sql_content":"WITH address_activity AS (SELECT from_address AS address, COUNT(*) AS tx_count FROM eth.transactions WHERE date_parse(date, '\''%Y-%m-%d'\'') >= date_add('\''month'\'', -3, current_date) GROUP BY from_address UNION ALL SELECT to_address AS address, COUNT(*) AS tx_count FROM eth.transactions WHERE date_parse(date, '\''%Y-%m-%d'\'') >= date_add('\''month'\'', -3, current_date) GROUP BY to_address) SELECT address, SUM(tx_count) AS total_transactions FROM address_activity GROUP BY address ORDER BY total_transactions DESC LIMIT 1;"}'
```

#### **Example Response**

**200 OK Response**

```json
{
    "code": 0,
    "msg": "Success",
    "data": {
        "column_infos": [
            "address",
            "total_transactions"
        ],
        "rows": [
            {
                "items": [
                    "0xdac17f958d2ee523a2206206994597c13d831ec7",
                    "11021156"
                ]
            }
        ]
    }
}
```

**400 Bad Request Response**

```json
{
  "error": "Invalid SQL query."
}
```

#### **Response Status Codes**

| Status Code | Description | Data Model |
| ----------- | ----------- | ---------- |
| 200         | OK          | Inline     |
| 400         | Bad Request | Inline     |

#### **Response Data Structure**

**200 OK**

<table><thead><tr><th>Field</th><th width="97">Type</th><th>Required</th><th>Constraints</th><th>Description</th></tr></thead><tbody><tr><td>code</td><td>integer</td><td>Yes</td><td>None</td><td>Status code.</td></tr><tr><td>msg</td><td>string</td><td>Yes</td><td>None</td><td>Response message.</td></tr><tr><td>data</td><td>object</td><td>Yes</td><td>None</td><td>Data from the query.</td></tr><tr><td>column_infos</td><td>array</td><td>Yes</td><td>None</td><td>Column headers of data.</td></tr><tr><td>rows</td><td>array</td><td>Yes</td><td>None</td><td>Query result rows.</td></tr></tbody></table>

**400 Bad Request**

| Field | Type   | Required | Constraints | Description    |
| ----- | ------ | -------- | ----------- | -------------- |
| error | string | Yes      | None        | Error message. |
