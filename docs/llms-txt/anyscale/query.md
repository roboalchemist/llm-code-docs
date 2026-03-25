# Source: https://docs.anyscale.com/services/query.md

# Query an Anyscale service

[View Markdown](/services/query.md)

# Query an Anyscale service

This page provides an overview of how to query an Anyscale service.

Anyscale services support diverse Python applications implemented with Ray Serve. The guidance on this page is general. You must construct queries based on the logic implemented in your Ray Serve applications.

Anyscale enables bearer tokens for all services by default. You must include the bearer token to authenticate queries to your Anyscale service. You can optionally disable this behavior. See [Remove the bearer token](/services/deploy.md#bearer).

## Anyscale service endpoint URL[​](#url "Direct link to Anyscale service endpoint URL")

Anyscale uses the following URL format for deployed services:

```
<service-name>-<5-digit-random-hex>.<cloud-id>.s.anyscaleuserdata.com
```

The `query_url` field displays the URL when you run the following command with the Anyscale CLI:

```
anyscale service status --name <service-name>
```

In the Anyscale console, the URL displays as part of the example queries.

## Get an example query[​](#example-query "Direct link to Get an example query")

You can use the Anyscale console to generate an example query for your endpoint. Complete the following steps:

1. [Log in to the Anyscale console](https://console.anyscale.com/).
2. Click **Services**.
3. Click on the name of your service.
4. Click **Query**.

The endpoint URL displays with basic `curl` or Python query logic.

You can use the displayed query to generate a basic response from your endpoint. Depending on how you've implemented your application, you might need to modify the query to include a routing path and additional query parameters.

## Run sample queries from FastAPI[​](#fastapi "Direct link to Run sample queries from FastAPI")

You can optionally use FastAPI to control HTTP handling logic in Ray Serve applications. When you build an application with FastAPI, the Anyscale console includes a link to FastAPI documentation that lets you run sample queries against your defined routes.

To view FastAPI docs and run a sample query, complete the following steps:

1. [Log in to the Anyscale console](https://console.anyscale.com/).
2. Click **Services**.
3. Click on the name of your service.
4. Locate your deployment under **Deployments**. In the **API docs** column, click **View**. The FastAPI docs display.
5. Click a routing path to expand the docs and see example queries and responses. Click **Try it out** to open an editable query.
6. Click **Execute** to run your query. Your application logic runs and the response for your query displays.

See the following pages for more details:

* [FastAPI automatic docs](https://fastapi.tiangolo.com/features/#automatic-docs)
* [Ray docs on FastAPI HTTP Deployments](https://docs.ray.io/en/latest/serve/http-guide.html#fastapi-http-deployments)
