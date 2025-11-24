# Source: https://docs.apify.com/api/v2/getting-started.md

# Getting started with Apify API

The Apify API provides programmatic access to the https://docs.apify.com. The API is organized around https://en.wikipedia.org/wiki/Representational_state_transfer HTTP endpoints.

<!-- -->

The diagram illustrates the basic workflow when using the Apify API:

1. Your application communicates with the Apify API by sending requests to run Actors and receiving results back.

2. When you request to run an Actor, the Apify API creates and manages an Actor run instance on the platform.

3. The Actor processes data and stores results in Apify's storage systems:

   <!-- -->

   * **Dataset**: Structured storage optimized for tabular or list-type data, ideal for scraped items or processed results.
   * **Key-Value Store**: Flexible storage for various data types (including images, JSON, HTML, and text), perfect for configuration settings and non-tabular outputs.

## Prerequisites

Before you can start using the API, check if you have all the necessary prerequisites:

* An Apify account with an API token.
* A tool to make HTTP requests (cURL, Postman, or your preferred programming language).

## Authentication

You must authenticate all API requests presented on this page. You can authenticate using your API token:


```
Authorization: Bearer YOUR_API_TOKEN
```


You can find your API token in the Apify Console under **https://console.apify.com/settings/integrations**.

### Verify your account

To check your API credentials or account details:

Endpoint


```
GET https://api.apify.com/v2/users/me
```


Expected response codes:

* `200`

## Basic workflow

The most common workflow involving Apify API consists of the following steps:

1. Running an Actor.
2. Retrieving the results.

### 1. Run an Actor

#### Synchronously

For shorter runs where you need immediate results:

Endpoint


```
POST https://api.apify.com/v2/acts/:actorId/run-sync
```


Expected response codes:

* `201`
* `400`
* `408`

#### Asynchronously

For longer-running operations or when you don't need immediate results.

Endpoint


```
POST https://api.apify.com/v2/acts/:actorId/runs
```


Expected response codes:

* `201`

### 2. Retrieve results

#### From a Dataset

Most Actors store their results in a dataset:

Endpoint


```
GET https://api.apify.com/v2/datasets/:datasetId/items
```


Optional query parameters:

* `format=json` (default), other possible formats are:

  <!-- -->

  * jsonl
  * xml
  * html
  * csv
  * xlsx
  * rss

* `limit=100` (number of items to retrieve)

* `offset=0` (pagination offset)

Expected response codes:

* `200`

#### From a Key-value store

Endpoint


```
GET https://api.apify.com/v2/key-value-stores/:storeId/records/:recordKey
```


Expected response codes:

* `200`
* `302`

### Additional operations

#### Get log

You can get a log for a specific run or build of an Actor.

Endpoint


```
GET https://api.apify.com/v2/logs/:buildOrRunId
```


Expected response codes:

* `200`

#### Monitor run status

Endpoint


```
GET https://api.apify.com/v2/actor-runs/:runId
```


Expected response codes:

* `200`

#### Store data in Dataset

To store your own data in a Dataset:

Endpoint


```
POST https://api.apify.com/v2/datasets/:datasetId/items
```


If any item in the request fails validation, the entire request will be rejected.

Expected response codes:

* `201`
* `400`

#### Store data in Key-value store

To store your own data in a Key-value store:

Endpoint


```
PUT https://api.apify.com/v2/key-value-stores/:storeId/records/:recordKey
```


Include your data in the request body and set the appropriate `Content-Type` header.

Expected response codes:

* `201`

## HTTP Status Code Descriptions

### `200` OK

The request has succeeded.

### `201` Created

The request has been fulfilled and a new resource has been created.

### `302` Found

A redirection response indicating that the requested resource has been temporarily moved to a different URL.

### `400` Bad Request

The server cannot process the request due to client error, such as request syntax, invalid request parameters, or invalid data format. This occurs when:

* The request body contains invalid data
* Required parameters are missing
* Data validation fails for Dataset items

### `408` Request Timeout

The server timed out waiting for the request to complete.

## Next steps

* Explore more advanced API endpoints in our full https://docs.apify.com/api/v2.md.

* Learn about webhooks to get notified when your runs finish.

* Check out Apify client libraries for the following programming languages:

  <!-- -->

  * https://docs.apify.com/api/client/js
  * https://docs.apify.com/api/client/python
