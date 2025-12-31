# Source: https://docs.vespa.ai/en/reference/api/document-v1.html.md

# /document/v1 API reference

 

This is the /document/v1 API reference documentation. Use this API for synchronous [Document](../../schemas/documents.html) operations to a Vespa endpoint - refer to [reads and writes](../../writing/reads-and-writes.html) for other options.

The [document/v1 API guide](../../writing/document-v1-api-guide.html) has examples and use cases.

 **Note:** Mapping from document IDs to /document/v1/ URLs is found in [document IDs](../../schemas/documents.html#id-scheme) - also see [troubleshooting](../../writing/document-v1-api-guide.html#troubleshooting).

Some examples use _number_ and _group_[document id](../../schemas/documents.html#document-ids) modifiers. These are special cases that only work as expected for document types with [mode=streaming or mode=store-only](../applications/services/content.html#document). Do not use group or number modifiers with regular indexed mode document types.

## Configuration

To enable the API, add `document-api` in the serving container cluster - [services.xml](../applications/services/container.html):

```
<services>
    <container>\<document-api/\>
```

## HTTP requests

| HTTP request | document/v1 operation | Description |
| --- | --- | --- |
| GET | 

_Get_ a document by ID or _Visit_ a set of documents by selection.

 |
| | Get | Get a document:
```
/document/v1/<namespace>/<document-type>/docid/<document-id>
/document/v1/<namespace>/<document-type>/number/<numeric-group-id>/<document-id>
/document/v1/<namespace>/<document-type>/group/<text-group-id>/<document-id>
```
 Optional parameters: 
- [cluster](#cluster)
- [fieldSet](#fieldset)
- [timeout](#timeout)
- [tracelevel](#tracelevel)

 |
| | Visit | 

Iterate over and get all documents, or a [selection](#selection) of documents, in chunks, using [continuation](#continuation) tokens to track progress. Visits are a linear scan over the documents in the cluster.

```
/document/v1/
```
 It is possible to specify namespace and document type with the visit path:
```
/document/v1/<namespace>/<document-type>/docid
```
 Documents can be grouped to limit accesses to a subset. A group is defined by a numeric ID or string — see [id scheme](../../schemas/documents.html#id-scheme).
```
/document/v1/<namespace>/<document-type>/group/<group>
/document/v1/<namespace>/<document-type>/number/<number>
```
 Mandatory parameters: 
- [cluster](#cluster) - Visits can only retrieve data from _one_ content cluster, so `cluster` **must** be specified for requests at the root `/document/v1/` level, or when there is ambiguity. This is required even if the application has only one content cluster.

 Optional parameters: 
- [bucketSpace](#bucketspace) - Parent documents are [global](../applications/services/content.html#document) and in the `global` [bucket space](#bucketspace). By default, visit will visit non-global documents in the `default` bucket space, unless document type is indicated, and is a global document type. 
- [concurrency](#concurrency) - Use to configure backend parallelism for each visit HTTP request.
- [continuation](#continuation)
- [fieldSet](#fieldset)
- [selection](#selection)
- [sliceId](#sliceid)
- [slices](#slices) - Split visiting of the document corpus across more than one HTTP request—thus allowing the concurrent use of more HTTP containers—use the `slices` and `sliceId` parameters.
- [stream](#stream) - It's recommended enabling streamed HTTP responses, with the [stream](#stream) parameter, as this reduces memory consumption and reduces HTTP overhead.
- [timeout](#timeout)
- [tracelevel](#tracelevel)
- [wantedDocumentCount](#wanteddocumentcount)
- [fromTimestamp](#fromtimestamp)
- [toTimestamp](#totimestamp)
- [includeRemoves](#includeRemoves)

 Optional request headers: 
- [Accept](#accept) - specify the desired response format.

 |
| POST | 

_Put_ a given document, by ID, or _Copy_ a set of documents by selection from one content cluster to another.

 |
| | Put | Write the document contained in the request body in JSON format.
```
/document/v1/<namespace>/<document-type>/docid/<document-id>
/document/v1/<namespace>/<document-type>/group/<group>
/document/v1/<namespace>/<document-type>/number/<number>
```
 Optional parameters: 
- [condition](#condition) - Use for conditional writes.
- [route](#route)
- [timeout](#timeout)
- [tracelevel](#tracelevel)

 |
| | Copy | 

Write documents visited in source [cluster](#cluster) to the [destinationCluster](#destinationcluster) in the same application. A [selection](#selection) is mandatory —&nbsp;typically the document type. Supported paths (see [visit](#visit) above for semantics):

```
/document/v1/
/document/v1/<namespace>/<document-type>/docid/
/document/v1/<namespace>/<document-type>/group/<group>
/document/v1/<namespace>/<document-type>/number/<number>
```
 Mandatory parameters: 
- [cluster](#cluster)
- [destinationCluster](#destinationcluster)
- [selection](#selection)

 Optional parameters: 
- [bucketSpace](#bucketspace)
- [continuation](#continuation)
- [timeChunk](#timechunk)
- [timeout](#timeout)
- [tracelevel](#tracelevel)

 |
| PUT | 

_Update_ a document with the given partial update, by ID, or _Update where_ the given selection is true.

 |
| | Update | Update a document with the partial update contained in the request body in the [document update JSON format](../schemas/document-json-format.html#update).
```
/document/v1/<namespace>/<document-type>/docid/<document-id>
```
 Optional parameters: 
- [condition](#condition) - use for conditional writes
- [create](#create) - use to create empty documents when updating non-existent ones.
- [route](#route)
- [timeout](#timeout)
- [tracelevel](#tracelevel)

 |
| | Update where | 

Update visited documents in [cluster](#cluster) with the partial update contained in the request body in the [document update JSON format](../schemas/document-json-format.html#update). Supported paths (see [visit](#visit) above for semantics):

```
/document/v1/<namespace>/<document-type>/docid/
/document/v1/<namespace>/<document-type>/group/<group>
/document/v1/<namespace>/<document-type>/number/<number>
```
 Mandatory parameters: 
- [cluster](#cluster)
- [selection](#selection)

 Optional parameters: 
- [bucketSpace](#bucketspace) - See [visit](#visit), `default` or `global` bucket space
- [continuation](#continuation)
- [stream](#stream)
- [timeChunk](#timechunk)
- [timeout](#timeout)
- [tracelevel](#tracelevel)

 |
| DELETE | 

_Remove_ a document, by ID, or _Remove where_ the given selection is true.

 |
| | Remove | Remove a document.
```
/document/v1/<namespace>/<document-type>/docid/<document-id>
```
 Optional parameters: 
- [condition](#condition)
- [route](#route)
- [timeout](#timeout)
- [tracelevel](#tracelevel)

 |
| | Delete where | 

Delete visited documents from [cluster](#cluster). Supported paths (see [visit](#visit) above for semantics):

```
/document/v1/
/document/v1/<namespace>/<document-type>/docid/
/document/v1/<namespace>/<document-type>/group/<group>
/document/v1/<namespace>/<document-type>/number/<number>
```
 Mandatory parameters: 
- [cluster](#cluster)
- [selection](#selection)

 Optional parameters: 
- [bucketSpace](#bucketspace) - See [visit](#visit), `default` or `global` bucket space
- [continuation](#continuation)
- [stream](#stream)
- [timeChunk](#timechunk)
- [timeout](#timeout)
- [tracelevel](#tracelevel)

 |

## Request parameters

| Parameter | Type | Description |
| --- | --- | --- |
| bucketSpace | String | 

Specify the bucket space to visit. Document types marked as `global` exist in a separate _bucket space_ from non-global document types. When visiting a particular document type, the bucket space is automatically deduced based on the provided type name. When visiting at a root `/document/v1/` level this information is not available, and the non-global ("default") bucket space is visited by default. Specify `global` to visit global documents instead. Supported values: `default` (for non-global documents) and `global`.

 |
| cluster | String | 

Name of [content cluster](../../content/content-nodes.html) to GET from, or visit.

 |
| concurrency | Integer | 

Sends the given number of visitors in parallel to the backend, improving throughput at the cost of resource usage. Default is 1. When `stream=true`, concurrency limits the maximum concurrency, which is otherwise unbounded, but controlled by a dynamic throttle policy.

 **Important:** Given a concurrency parameter of _N_, the worst case for memory used while processing the request grows linearly with _N_, unless [stream](#stream) mode is turned on. This is because the container currently buffers all response data in memory before sending them to the client, and all sent visitors must complete before the response can be sent.
 |
| condition | String | 

For test-and-set. Run a document operation conditionally — if the condition fails, a _412 Precondition Failed_ is returned. See [example](../../writing/document-v1-api-guide.html#conditional-writes).

 |
| continuation | String | 

When visiting, a continuation token is returned as the `"continuation"` field in the JSON response, as long as more documents remain. Use this token as the `continuation` parameter to visit the next chunk of documents. See [example](../../writing/document-v1-api-guide.html#data-dump).

 |
| create | Boolean | 

If `true`, updates to non-existent documents will create an empty document to update. See [create if nonexistent](../../writing/document-v1-api-guide.html#create-if-nonexistent).

 |
| destinationCluster | String | 

Name of [content cluster](../../content/content-nodes.html) to copy to, during a copy visit.

 |
| dryRun | Boolean | 

Used by the [vespa-feed-client](../../clients/vespa-feed-client.html) using `--speed-test` for bandwidth testing, by setting to `true`.

 |
| fieldSet | String | 

A [field set string](../../schemas/documents.html#fieldsets) with the set of document fields to fetch from the backend. Default is the special `[document]` fieldset, returning all _document_ fields. To fetch specific fields, use the name of the document type, followed by a comma-separated list of fields (for example `music:artist,song` to fetch two fields declared in `music.sd`).

 |
| route | String | 

The route for single document operations, and for operations generated by [copy](#copy), [update](#update-where) or [deletion](#delete-where) visits. Default value is `default`. See [routes](../../writing/document-routing.html).

 |
| selection | String | 

Select only a subset of documents when [visiting](../../writing/visiting.html) — details in [document selector language](../writing/document-selector-language.html).

 |
| sliceId | Integer | 

The slice number of the visit represented by this HTTP request. This number must be non-negative and less than the number of [slices](#slices) specified for the visit - e.g., if the number of slices is 10, `sliceId` is in the range [0-9].

 **Note:** If the number of distribution bits change during a sliced visit, the results are undefined. Thankfully, this is a very rare occurrence and is only triggered when adding content nodes.
 |
| slices | Integer | 

Split the document corpus into this number of independent slices. This lets multiple, concurrent series of HTTP requests advance the same logical visit independently, by specifying a different [sliceId](#sliceid) for each.

 |
| stream | Boolean | 

Whether to stream the HTTP response, allowing data to flow as soon as documents arrive from the backend. This obsoletes the [wantedDocumentCount](#wanteddocumentcount) parameter. The HTTP status code will always be 200 if the visit is successfully initiated. Default value is false.

 |
| format.tensors | String | 

Controls how tensors are rendered in the result.

| Value | Description |
| --- | --- |
| `short` | **Default**. Render the tensor value in an object having two keys, "type" containing the value, and "cells"/"blocks"/"values" ([depending on the type](../schemas/document-json-format.html#tensor)) containing the tensor content.  
 Render the tensor content in the [type-appropriate short form](../schemas/document-json-format.html#tensor). |
| `long` | Render the tensor value in an object having two keys, "type" containing the value, and "cells" containing the tensor content.  
 Render the tensor content in the [general verbose form](../schemas/document-json-format.html#tensor). |
| `short-value` | Render the tensor content directly.  
 Render the tensor content in the [type-appropriate short form](../schemas/document-json-format.html#tensor). |
| `long-value` | Render the tensor content directly.  
 Render the tensor content in the [general verbose form](../schemas/document-json-format.html#tensor). |

 |
| timeChunk | String | 

Target time to spend on one chunk of a copy, update or remove visit; with optional ks, s, ms or µs unit. Default value is 60.

 |
| timeout | String | 

Request timeout in seconds, or with optional ks, s, ms or µs unit. Default value is 180s.

 |
| tracelevel | Integer | 

Number in the range [0,9], where higher gives more details. The trace dumps which nodes and chains the document operation has touched. See [routes](../../writing/document-routing.html).

 |
| wantedDocumentCount | Integer | 

Best effort attempt to not respond to the client before `wantedDocumentCount` number of documents have been visited. Response may still contain fewer documents if there are not enough matching documents left to visit in the cluster, or if the visiting times out. This parameter is intended for the case when you have relatively few documents in your cluster and where each visit request would otherwise process only a handful of documents.

The maximum value of `wantedDocumentCount` is bounded by an implementation-specific limit to prevent excessive resource usage. If the cluster has many documents (on the order of tens of millions), there is no need to set this value.

 |
| fromTimestamp | Integer | 

Filters the returned document set to only include documents that were last modified at a time point equal to or higher to the specified value, in microseconds from UTC epoch. Default value is 0 (include all documents).

 |
| toTimestamp | Integer | 

Filters the returned document set to only include documents that were last modified at a time point lower than the specified value, in microseconds from UTC epoch. Default value is 0 (sentinel value; include all documents). If non-zero, must be greater than, or equal to, `fromTimestamp`.

 |
| includeRemoves | Boolean | 

Include recently removed document IDs, along with the set of returned documents. By default, only documents currently present in the corpus are returned in the `"documents"` array of the response; when this parameter is set to `"true"`, documents that were recently removed, and whose tombstones still exist, are also included in that array, as entries on the form `{ "remove": "id:ns:type::foobar" }`. See [here](/en/operations/self-managed/admin-procedures.html#data-retention-vs-size) for specifics on tombstones, including their lifetime.

 |

## HTTP request headers

| Header | Values | Description |
| --- | --- | --- |
| Accept | `application/json` or `application/jsonl` | 

The [Accept](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Accept) header lets the client specify to the server what [media (MIME) types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types) it accepts as the response format.

All Document V1 API calls support `application/json` for returning [JSON](#json) responses. [Streaming visiting](#stream) additionally supports `application/jsonl` for returning [JSON Lines](#json-lines) (JSONL) since Vespa 8.593.

To ensure compatibility with older versions, make sure to check the `Content-Type`[HTTP response header](#http-response-headers). A JSONL response will always have a `Content-Type` media type of `application/jsonl`, and JSON wil always have a media type of `application/json`.

 Multiple acceptable types can be specified. JSONL will be returned if (and only if) `application/jsonl` is part of the list _and_ no other media types have a higher [quality value](https://httpwg.org/specs/rfc9110.html#quality.values). 

Example:

```
Accept: application/jsonl
```

If the client accepts both JSON and JSONL, the server will respond with JSONL:

```
Accept: application/json, application/jsonl
```

For backwards compatibility, if no `Accept` header is provided (or if no provided media types are acceptable) `application/json` is assumed.

 |

## Request body

POST and PUT requests must include a body for single document operations; PUT must also include a body for [update where](#update-where) visits. A field has a _value_ for a POST and an _update operation object_ for PUT. Documents and operations use the [document JSON format](../schemas/document-json-format.html). The document fields must match the [schema](../../basics/schemas.html):

```
```
{
    "fields": {
        "<fieldname>": "<value>"
    }
}
```
```

```
```
{
    "fields": {
        "<fieldname>": {
            "<update-operation>" : "<value>"
        }
    }
}
```
```

The _update-operation_ is most often `assign` - see [update operations](../schemas/document-json-format.html#update-operations) for the full list. Values for `id` / `put` / `update` in the request body are silently dropped. The ID is generated from the request path, regardless of request body data - example:

```
```
{
    "put" : "id:mynamespace:music::123",
    "fields": {
        "title": "Best of"
    }
}
```
```

This makes it easier to generate a feed file that can be used for both the [vespa-feed-client](../../clients/vespa-feed-client.html) and this API.

## HTTP status codes

| Code | Description |
| --- | --- |
| 200 | OK. Attempts to remove or update a non-existent document also yield this status code (see 412 below). |
| 204 | No Content. Successful response to OPTIONS request. |
| 400 | Bad request. Returned for undefined document types + other request errors. See [13465](https://github.com/vespa-engine/vespa/issues/13465) for defined document types not assigned to a content cluster when using PUT. Inspect `message` for details. |
| 404 | Not found; the document was not found. This is only used when getting documents. |
| 405 | Method Not Allowed. HTTP method is not supported by the endpoint. Valid combinations are listed [above](#http-requests) |
| 412 | [condition](#condition) is not met. Inspect `message` for details. This is also the result when a condition if specified, but the document does not exist. |
| 413 | Content too large; used for POST and PUT requests that are above the [request size limit](../../writing/document-v1-api-guide.html#request-size-limit). |
| 429 | Too many requests; the document API has too many inflight feed operations, retry later. |
| 500 | Server error; an unspecified error occurred when processing the request/response. |
| 503 | Service unavailable; the document API was unable to produce a response at this time. |
| 504 | Gateway timeout; the document API failed to respond within the given (or default 180s) timeout. |
| 507 | Insufficient storage; the content cluster is out of memory or disk space. |

## HTTP response headers

| Header | Values | Description |
| --- | --- | --- |
| X-Vespa-Ignored-Fields | true | 

Will be present and set to 'true' only when a put or update contains one or more fields which were [ignored since they are not present in the document type](../applications/services/container.html#ignore-undefined-fields). Such operations will be applied exactly as if they did not contain the field operations referencing non-existing fields. References to non-existing fields in field _paths_ are not detected.

 |
| Content-Type | `application/json` or `application/jsonl` | 

The [media type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types) (MIME type) of the response body.

Either `application/json` for [JSON](#json) responses or `application/jsonl` for [JSON Lines](#json-lines) (JSONL) responses.

The content type may include additional parameters such as `charset`.

Example header:

```
Content-Type: application/json; charset=UTF-8
```
 |

## Response formats

Responses are by default in JSON format. [Streaming visiting](#stream)supports an optional [JSON Lines](#json-lines) (JSONL) response format since Vespa 8.593.

### JSON

JSON responses have the following fields:

| Field | Description |
| --- | --- |
| pathId | Request URL path — always included. |
| message | An error message — included for all failed requests. |
| id | Document ID — always included for single document operations, including _Get_. |
| fields | The requested document fields — included for successful _Get_ operations. |
| documents[] | Array of documents in a visit result — each document has the _id_ and _fields_. |
| documentCount | Number of visited and selected documents. If [includeRemoves](#includeRemoves) is `true`, this also includes the number of returned removes (tombstones). |
| continuation | Token to be used to get the next chunk of the corpus - see [continuation](#continuation). |

GET can include a `fields` object if a document was found in a _GET_ request

```
```
{
    "pathId": "<pathid>",
    "id": "<id>",
    "fields": {
    }
}
```
```

A GET _visit_ result can include an array of `documents`plus a [continuation](#continuation):

```
```
{
    "pathId": "<pathid>",
    "documents": [
        {
            "id": "<id>",
            "fields": {
            }
        }
    ],
    "continuation": "<continuation string>",
    "documentCount": 123
}
```
```

A continuation indicates the client should make further requests to get more data, while lack of a continuation indicates an error occurred, and that visiting should cease, or that there are no more documents.

A `message` can be returned for failed operations:

```
```
{
    "pathId": "<pathid>",
    "message": "<message text>"
}
```
```

### JSON Lines

A JSON Lines (JSONL) response is a stream of newline-separated JSON objects. Each line contains exactly one JSON object, and each JSON object takes up exactly one line. No line breaks are allowed within an object.

JSONL is an optional response format for [streaming visiting](#stream), enabling efficient client-side parsing and fine-grained, continuous tracking of visitor progress. The JSONL response format is currently not supported for any other operations than streaming visiting.

The JSONL response format is enabled by providing a HTTP [Accept](#accept) request header that specifies `application/jsonl` as the preferred response type, and will have a [Content-Type](#content-type) of `application/jsonl` if the server is on a version that supports JSONL visiting. Clients must check the `Content-Type` header to ensure they are getting the format they expect.

JSONL support requires Vespa 8.593 or newer.

Example response body:

```
```
{"put":"id:ns:music::one","fields":{"foo":"bar"}}
{"put":"id:ns:music::two","fields":{"foo":"baz"}}
{"continuation":{"token":"...","percentFinished":40.0}}
{"put":"id:ns:music::three","fields":{"foo":"zoid"}}
{"remove":"id:ns:music::four"}
{"continuation":{"token":"...","percentFinished":50.0}}
{"continuation":{"token":"...","percentFinished":60.0}}
{"put":"id:ns:music::five","fields":{"foo":"berg"}}
{"continuation":{"token":"...","percentFinished":70.0}}
{"sessionStats":{"documentCount":5}}
{"continuation":{"percentFinished":100.0}}
```
```

Note that the `"..."` values are placeholders for (from a client's perspective) opaque string values.

#### JSONL response objects

 **Note:** To be forwards compatible with future extensions to the response format, ignore unknown objects and fields.

| Object | Description |
| --- | --- |
| put | A document [Put](../schemas/document-json-format.html#put) operation in the same format as that accepted by Vespa's JSONL feed API. |
| remove | A document [Remove](../schemas/document-json-format.html#remove) operation in the same format as that accepted by Vespa's JSONL feed API. Only present if [includeRemoves](#includeRemoves) is `true`. |
| continuation | 

A visitor [continuation](#continuation).

Possible sub-object fields:

| Field name | Description |
| --- | --- |
| `token` | 

An opaque string value representing the current visitor progress through the data space. This value can be provided as part of a subsequent visitor request to continue visiting from where the last request left off. Clients should not attempt to parse the contents of this string, as it's considered an internal implementation detail and may be changed (in a backwards compatible way) without any prior announcement.

 |
| `percentFinished` | A floating point number between 0 and 100 (inclusive) that gives an approximation of how far the visitor has progressed through the data space. |

The last line of a successful request should always be a `continuation` object.

If (and only if) visiting has completed, the last `continuation` object will have a `percentFinished` value of `100` and will _not_ have a `token` field.

 |
| message | 

A message received from the backend visitor session. Can be used by clients to report problems encountered during visiting.

Possible sub-object fields:

| Field name | Description |
| --- | --- |
| `text` | The actual message, in unstructured text |
| `severity` | The severity of the message. One of `info`, `warning` or `error`. |

 |
| sessionStats | 

Statistics from the backend visitor session.

Possible sub-object fields:

| Field name | Description |
| --- | --- |
| `documentCount` | The number of visited and selected documents. If [includeRemoves](#includeRemoves) is `true`, this also includes the number of returned removes (tombstones). |

 |

Note that it's possible for a successful response to contain zero `put` or `remove` objects if the [selection](#selection) did not match any documents.

#### Differences from the JSON format

The biggest difference in semantics between the JSON and JSONL response formats is when, and how, [continuation](#continuation) objects are returned.

In the JSON format a continuation is included _once_ at the very end of the response object and covers the progress made by the entire request. If the request somehow fails after receiving 99% of all documents but prior to receiving the continuation field, the client must retry the entire request from the previously known continuation value. This can result in getting many requested documents twice; once from the incomplete first request and once more from the second request that covers the same part of the data space.

In the JSON Lines format, a contination object is emitted to the stream _every time_ a backend data [bucket](../../content/buckets.html) has been fully visited, as well as at the end of the response stream. This may happen many times in a response. Each continuation object _subsumes_ the progress of previously emitted continuations, meaning that a client only needs to remember the _most recent_ continuation value it observed in the response. If the request fails prior to completion, the client can specify the most recent continuation in the next request; it will then only receive duplicates for the data buckets that were actively being processed when the request failed.

 Copyright © 2025 - [Cookie Preferences](#)

### On this page:

- [Configuration](#configuration)
- [HTTP requests](#http-requests)
- [Request parameters](#request-parameters)
- [HTTP request headers](#http-request-headers)
- [Request body](#request-body)
- [HTTP status codes](#http-status-codes)
- [HTTP response headers](#http-response-headers)
- [Response formats](#response-formats)
- [JSON](#json)
- [JSON Lines](#json-lines)

