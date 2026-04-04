# Source: https://docs.apify.com/api/v2/actor-task-runs-last-get.md

# Get last run


```
GET 
https://api.apify.com/v2/actor-tasks/:actorTaskId/runs/last
```


This is not a single endpoint, but an entire group of endpoints that lets you to retrieve and manage the last run of given actor task or any of its default storages. All the endpoints require an authentication token.

The endpoints accept the same HTTP methods and query parameters as the respective storage endpoints. The base path represents the last actor task run object is:

`/v2/actor-tasks/{actorTaskId}/runs/last{?token,status}`

Using the `status` query parameter you can ensure to only get a run with a certain status (e.g. `status=SUCCEEDED`). The output of this endpoint and other query parameters are the same as in the [Run object](https://docs.apify.com/api/v2/actor-run-get.md) endpoint.

In order to access the default storages of the last actor task run, i.e. log, key-value store, dataset and request queue, use the following endpoints:

* `/v2/actor-tasks/{actorTaskId}/runs/last/log{?token,status}`
* `/v2/actor-tasks/{actorTaskId}/runs/last/key-value-store{?token,status}`
* `/v2/actor-tasks/{actorTaskId}/runs/last/dataset{?token,status}`
* `/v2/actor-tasks/{actorTaskId}/runs/last/request-queue{?token,status}`

These API endpoints have the same usage as the equivalent storage endpoints. For example, `/v2/actor-tasks/{actorTaskId}/runs/last/key-value-store` has the same HTTP method and parameters as the [Key-value store object](https://docs.apify.com/api/v2/storage-key-value-stores.md) endpoint.

Additionally, each of the above API endpoints supports all sub-endpoints of the original one:

##### Storage endpoints

* [Dataset - introduction](https://docs.apify.com/api/v2/storage-datasets.md)

* [Key-value store - introduction](https://docs.apify.com/api/v2/storage-key-value-stores.md)

* [Request queue - introduction](https://docs.apify.com/api/v2/storage-request-queues.md)

For example, to download data from a dataset of the last succeeded actor task run in XML format, send HTTP GET request to the following URL:


```
https://api.apify.com/v2/actor-tasks/{actorTaskId}/runs/last/dataset/items?token={yourApiToken}&format=xml&status=SUCCEEDED
```


In order to save new items to the dataset, send HTTP POST request with JSON payload to the same URL.

## Request

## Responses

* 200
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
