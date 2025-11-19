# Source: https://docs.apify.com/api/v2/act-runs-last-get.md

# Get last run


```
GET 
https://api.apify.com/v2/acts/:actorId/runs/last
```


This is not a single endpoint, but an entire group of endpoints that lets you to retrieve and manage the last run of given Actor or any of its default storages. All the endpoints require an authentication token.

The endpoints accept the same HTTP methods and query parameters as the respective storage endpoints. The base path represents the last Actor run object is:

`/v2/acts/{actorId}/runs/last{?token,status}`

Using the `status` query parameter you can ensure to only get a run with a certain status (e.g. `status=SUCCEEDED`). The output of this endpoint and other query parameters are the same as in the  endpoint.

In order to access the default storages of the last Actor run, i.e. log, key-value store, dataset and request queue, use the following endpoints:

* `/v2/acts/{actorId}/runs/last/log{?token,status}`
* `/v2/acts/{actorId}/runs/last/key-value-store{?token,status}`
* `/v2/acts/{actorId}/runs/last/dataset{?token,status}`
* `/v2/acts/{actorId}/runs/last/request-queue{?token,status}`

These API endpoints have the same usage as the equivalent storage endpoints. For example, `/v2/acts/{actorId}/runs/last/key-value-store` has the same HTTP method and parameters as the  endpoint.

Additionally, each of the above API endpoints supports all sub-endpoints of the original one:

#### Key-value store

* `/v2/acts/{actorId}/runs/last/key-value-store/keys{?token,status}` 
* `/v2/acts/{actorId}/runs/last/key-value-store/records/{recordKey}{?token,status}` 

#### Dataset

* `/v2/acts/{actorId}/runs/last/dataset/items{?token,status}` 

#### Request queue

* `/v2/acts/{actorId}/runs/last/request-queue/requests{?token,status}` 
* `/v2/acts/{actorId}/runs/last/request-queue/requests/{requestId}{?token,status}` 
* `/v2/acts/{actorId}/runs/last/request-queue/head{?token,status}` 

For example, to download data from a dataset of the last succeeded Actor run in XML format, send HTTP GET request to the following URL:


```
https://api.apify.com/v2/acts/{actorId}/runs/last/dataset/items?token={yourApiToken}&format=xml&status=SUCCEEDED
```


In order to save new items to the dataset, send HTTP POST request with JSON payload to the same URL.

## Request

## Responses

* 200

**Response Headers**

