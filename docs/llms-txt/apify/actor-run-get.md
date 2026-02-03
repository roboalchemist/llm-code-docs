# Source: https://docs.apify.com/api/v2/actor-run-get.md

# Get run


```
GET 
https://api.apify.com/v2/actor-runs/:runId
```


This is not a single endpoint, but an entire group of endpoints that lets you retrieve the run or any of its default storages.

The endpoints accept the same HTTP methods and query parameters as the respective storage endpoints.

The base path that represents the Actor run object is:

`/v2/actor-runs/{runId}{?token}`

In order to access the default storages of the Actor run, i.e. log, key-value store, dataset and request queue, use the following endpoints:

* `/v2/actor-runs/{runId}/log{?token}`
* `/v2/actor-runs/{runId}/key-value-store{?token}`
* `/v2/actor-runs/{runId}/dataset{?token}`
* `/v2/actor-runs/{runId}/request-queue{?token}`

These API endpoints have the same usage as the equivalent storage endpoints.

For example, `/v2/actor-runs/{runId}/key-value-store` has the same HTTP method and parameters as the  endpoint.

Additionally, each of the above API endpoints supports all sub-endpoints of the original one:

#### Log

* `/v2/actor-runs/{runId}/log` 

#### Key-value store

* `/v2/actor-runs/{runId}/key-value-store/keys{?token}` 
* `/v2/actor-runs/{runId}/key-value-store/records/{recordKey}{?token}` 

#### Dataset

* `/v2/actor-runs/{runId}/dataset/items{?token}` 

#### Request queue

* `/v2/actor-runs/{runId}/request-queue/requests{?token}` 
* `/v2/actor-runs/{runId}/request-queue/requests/{requestId}{?token}` 
* `/v2/actor-runs/{runId}/request-queue/head{?token}` 

For example, to download data from a dataset of the Actor run in XML format, send HTTP GET request to the following URL:


```
https://api.apify.com/v2/actor-runs/{runId}/dataset/items?format=xml
```


In order to save new items to the dataset, send HTTP POST request with JSON payload to the same URL.

Gets an object that contains all the details about a specific run of an Actor.

By passing the optional `waitForFinish` parameter the API endpoint will synchronously wait for the run to finish. This is useful to avoid periodic polling when waiting for Actor run to complete.

This endpoint does not require the authentication token. Instead, calls are authenticated using a hard-to-guess ID of the run. However, if you access the endpoint without the token, certain attributes, such as `usageUsd` and `usageTotalUsd`, will be hidden.

## Request

## Responses

* 200
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
