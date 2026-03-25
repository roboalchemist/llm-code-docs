# Source: https://docs.startree.ai/corecapabilities/query_data/query_interfaces/query-using-rest-API.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Querying Pinot using the REST API

You can query your Pinot data by sending a POST request to the Pinot broker's `/query/sql` endpoint. This endpoint accepts a JSON body containing your SQL query.

The basic structure of the request involves:

* **Method:** POST
* **Endpoint:** `/query/sql`
* **Request Body:** A JSON object with a single key, `sql`, whose value is your SQL query string.
* **Headers:** You will typically need to set the `Content-Type` header to `application/json`. If you are using StarTree Cloud, you will also need an `Authorization` header with a Bearer token. StarTree Trial accounts require an additional `database` header.

## Prerequisites

1. [Obtain a service token](#obtaining-a-service-token) for authentication.

2. [Find your Pinot Broker URL](#finding-your-broker-url).

## Examples

Here are some examples using the curl command-line tool:

### Example 1: Querying StarTree Cloud

When querying a Pinot cluster hosted on StarTree Cloud, you need to include an API token for authentication.

```bash  theme={null}
curl --location --request POST 'https://broker.pinot.<your url>.startree.cloud/query/sql' \
  --header 'Authorization: Bearer <API Token>' \
  --header 'Content-Type: application/json' \
  --data-raw '{"sql":"select * from myTable limit 10"}'
```

Remember to replace `<your url>` with your specific StarTree Cloud URL and `<API Token>` with your generated token.

### Example 2: Querying a local Pinot broker

If you have a Pinot broker running locally (for example, on localhost:8099), you can query it directly:

```bash  theme={null}
curl -H "Content-Type: application/json" -X POST \
  -d '{"sql":"select * from myTable limit 10"}' \
  http://localhost:8099/query/sql
```

Replace `yourTableName` with the actual name of your table.

## Obtaining a Service Token

You can cenerate an API token in the [Data Portal](/corecapabilities/security/manage-api-tokens#generating-an-api-token) or using the [REST API](/api-reference/introduction#authentication-%26-prerequisites).

This token is used in the Authorization header of your API requests.

## Finding Your Broker URL

To find the correct Broker URL for your table in StarTree Cloud:

1. Access the Data Portal.
2. Click on **Tables**.
3. Select the specific table you want to query.
4. The Broker URL for that table will be displayed, and you can copy it to your clipboard.

Built with [Mintlify](https://mintlify.com).
