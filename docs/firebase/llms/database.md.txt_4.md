# Source: https://firebase.google.com/docs/reference/rest/database.md.txt

# Firebase Database REST API

## API Usage


You can use any Firebase Realtime Database URL as a REST endpoint. All you need to
do is append `.json` to the end of the URL and send a request
from your favorite HTTPS client.

**HTTPS is required.** Firebase only responds to encrypted traffic so that your data remains safe.
You can choose the region in which to create a Realtime Database instance. Choice of region affects the database URL. Examples on this page are for region `us-central1`, with URL scheme `<dbname>.firebaseio.com`. For currently-supported regions and URL schemes, see the guides topic on [selecting
locations in Firebase projects](https://firebase.google.com/docs/projects/locations#rtdb-locations).

### GET - Reading Data


Data from your Realtime Database can be read by issuing an HTTP
`GET` request to an endpoint. The following example
demonstrates how you might retrieve a user's
name that you had previously stored in Realtime Database.

```
curl 'https://[PROJECT_ID].firebaseio.com/users/jack/name.json'
```

> [!IMPORTANT]
> In the examples on this page, you would replace `[PROJECT_ID]` with the identifier of your Firebase project.


A successful request is indicated by a `200 OK` HTTP
status code. The response contains the data associated with the
path in the `GET` request.

```
{ "first": "Jack", "last": "Sparrow" }
```

### PUT - Writing Data

You can write data with a `PUT` request.

```
curl -X PUT -d '{ "first": "Jack", "last": "Sparrow" }' \
  'https://[PROJECT_ID].firebaseio.com/users/jack/name.json'
```


A successful request is indicated by a `200 OK` HTTP
status code. The response contains the data specified in the
`PUT` request.

```
{ "first": "Jack", "last": "Sparrow" }
```

### POST - Pushing Data


To accomplish the equivalent of the JavaScript `push()`
method (see [Lists of Data](https://firebase.google.com/docs/database/web/lists-of-data#append_to_a_list_of_data)),
you can issue a `POST` request.

```
curl -X POST -d '{"user_id" : "jack", "text" : "Ahoy!"}' \
  'https://[PROJECT_ID].firebaseio.com/message_list.json'
```


A successful request is indicated by a `200 OK` HTTP status
code. The response contains the child name of the new data
specified in the `POST` request.

```
{ "name": "-INOQPH-aV_psbk3ZXEX" }
```

### PATCH - Updating Data


You can update specific children at a location without overwriting
existing data using a `PATCH` request. Named children in the
data being written with `PATCH` are overwritten, but omitted
children are not deleted. This is equivalent to the JavaScript
`update()` function.

```
curl -X PATCH -d '{"last":"Jones"}' \
 'https://[PROJECT_ID].firebaseio.com/users/jack/name/.json'
```


A successful request is indicated by a `200 OK` HTTP status
code. The response contains the data specified in the
`PATCH` request.

```
{ "last": "Jones" }
```

### DELETE - Removing Data


You can delete data with a `DELETE` request:

```
curl -X DELETE \
  'https://[PROJECT_ID].firebaseio.com/users/jack/name/last.json'
```


A successful `DELETE` request is indicated by a
`200 OK` HTTP status code with a response containing JSON
`null`.

### Method Override


If you make REST calls from a browser that does not support the
preceding methods, you can override the request method by making a
`POST` request and setting your method by using
the `X-HTTP-Method-Override` request header.

```
curl -X POST -H "X-HTTP-Method-Override: DELETE" \
  'https://[PROJECT_ID].firebaseio.com/users/jack/name/last.json'
```


You can also use the `x-http-method-override` query parameter.

```
curl -X POST \
  'https://[PROJECT_ID].firebaseio.com/users/jack/name/last.json?x-http-method-override=DELETE'
```

## Conditional Requests

Conditional requests, the REST equivalent of SDK transaction operations, update data according to
a certain condition. See an overview of the workflow and learn more about conditional requests
for REST in [Saving Data](https://firebase.google.com/docs/database/rest/save-data#section-conditional-requests).

### Firebase ETag

The Firebase ETag is the unique identifier for the current data at a specified location. If the
data changes at that location, the ETag changes, too. The Firebase ETag must be specified in the
header for the initial REST request (typically a
`GET`, but can be anything other than `PATCH`).

```
curl -i 'https://[PROJECT_ID].firebaseio.com/posts/12345/upvotes.json' -H 'X-Firebase-ETag: true'
```

### if-match

The `if-match` condition specifies the ETag value for the data you want to update.
If you use the condition, Realtime Database only completes requests where the ETag specified in the
write request matches the ETag of the existing data in the database. Fetch the
ETag at a location with a Firebase ETag request. If you want to overwrite any location that's
null, use `null_etag`.

```
curl -iX PUT -d '11' 'https://[PROJECT_ID].firebaseio.com/posts/12345/upvotes.json' -H 'if-match: [ETAG_VALUE]'
```

### Expected responses

The following table provides an overview of the expected responses for each request type,
based on the ETag match.

| Request Type || 'X-Firebase-ETag: true' | ETag matches `if_match: <matching etag>` | ETag doesn't match `if_match: <no matching etag>` |
| **GET** | **Response Status/Content** | 200: "\<data_at_path\>" | 400: "...not supported.." | 400: "...not supported.." |
| **GET** |
|---|---|---|---|---|
| **Added Headers** | ETag: \<ETag_of_data\> | N/A | N/A |
| **Added Headers** | ETag: \<ETag_of_put_data\> | N/A | ETag: \<database_ETag\> |
| **Added Headers** | ETag: \<ETag_of_post_data\> | N/A | N/A |
| **Added Headers** | N/A | N/A | N/A |
| **Added Headers** | ETag: \<ETag_of_null\> | N/A | ETag: \<database_ETag\> |

## Query Parameters


The Firebase Database REST API accepts the following query parameters and
values:

### access_token


Supported by all request types. Authenticates this request to allow
access to data protected by Firebase Realtime Database Security Rules.
See [the
REST authentication documentation](https://firebase.google.com/docs/reference/rest/database/user-auth) for details.

```
curl 'https://[PROJECT_ID].firebaseio/users/jack/name.json?access_token=CREDENTIAL'
```

### shallow


This is an advanced feature, designed to help you work with large
datasets without needing to download everything. Set this to
`true` to limit the depth of the data returned
at a location. If the data at the location is a JSON primitive
(string, number or boolean), its value will simply be returned. If the
data snapshot at the location is a JSON object, the
values for each key will be truncated to `true`.

| Arguments | REST Methods | Description |
|---|---|---|
| **shallow** | GET | Limit the depth of the response. |

```
curl 'https://[PROJECT_ID].firebaseio/.json?shallow=true'
```


Note that `shallow` cannot be mixed with any other query
parameters.

### print

Formats the data returned in the response from the server.

| Arguments | REST Methods | Description |
|---|---|---|
| **pretty** | GET, PUT, POST, PATCH, DELETE | View the data in a human-readable format. |
| **silent** | GET, PUT, POST, PATCH | Used to suppress the output from the server when writing data. The resulting response will be empty and indicated by a `204 No Content` HTTP status code. |

```
curl 'https://[PROJECT_ID].firebaseio.com/users/jack/name.json?print=pretty'
```

```
curl -X PUT -d '{ "first": "Jack", "last": "Sparrow" }' \
  'https://[PROJECT_ID].firebaseio.com/users/jack/name.json?print=silent'
```

### callback


Supported by `GET` only. To make REST calls from a web browser
across domains, you can use JSONP to wrap the response in a JavaScript
callback function. Add `callback=` to have the REST API wrap
the returned data in the callback function you specify.

```
<script>
  function gotData(data) {
    console.log(data);
  }
</script>
<script src="https://[PROJECT_ID].firebaseio.com/.json?callback=gotData"></script>
```

### format


If set to `export`, the server will encode priorities in the
response.

| Arguments | REST Methods | Description |
|---|---|---|
| **export** | GET | Include priority information in the response. |

```
curl 'https://[PROJECT_ID].firebaseio.com/.json?format=export'
```

### download


Supported by `GET` only. If you would like to trigger a file
download of your data from a web browser, add `download=`.
This causes the REST service to add the appropriate headers so that
browsers know to save the data to a file.

```
curl 'https://[PROJECT_ID].firebaseio/.json?download=myfilename.txt'
```

> [!IMPORTANT]
> **Private Backups** : We do not recommend using the REST API to regularly back up your Realtime Database. Instead, get set up with [Firebase
> Private Backups](https://www.firebase.com/blog/2015-03-05-private-backups-for-firebase-data.html).

### timeout


Use this to limit how long the read takes on the server side. If a read
request doesn't finish within the allotted time, it terminates with an HTTP
400 error. This is particularly useful when you expect a small data transfer
and don't want to wait too long to fetch a potentially huge subtree. Actual
read time might vary based on data size and caching.


Specify `timeouts` using the following format: `3ms`,
`3s`, or `3min`, with a number and a unit. If not
specified, the maximum `timeout` of `15min` will be
applied. If the `timeout` is not positive, or exceeds the maximum,
the request will be rejected with an HTTP 400 error.

### writeSizeLimit


> [!NOTE]
> **Note:** This parameter applies to delete as well as write operations.

To limit the size of a write, you can specify the `writeSizeLimit` query parameter as `tiny` (target=1s), `small` (target=10s), `medium` (target=30s), `large` (target=60s). Realtime Database estimates the size of each write request and aborts requests that will take longer than the target time.

<br />


If you specify `unlimited`, exceptionally large writes (with up to 256MB payload)
are allowed, potentially blocking subsequent requests while the database processes the
current operation. Writes cannot be canceled once they reach the server.

```
curl -X DELETE 'https://docs-examples.firebaseio.com/rest/delete-data.json?writeSizeLimit=medium'
```


You will see the following error message if the write is too big:

```
Error: WRITE_TOO_BIG: Data to write exceeds the maximum size that can be modified with a single request.
```


Additionally, you can set the `defaultWriteSizeLimit` for the whole database
instance using the Firebase CLI. This limit applies to all requests, including those from SDKs.
New databases are created with `defaultWriteSizeLimit`set to `large`.
You can't set `defaultWriteSizeLimit` to `tiny` using the Firebase CLI.

```
firebase database:settings:set defaultWriteSizeLimit large
```

> [!IMPORTANT]
> **Intentional large delete:** To delete a large node, consider using the Firebase CLI, which gracefully performs chunked deletes. Large deletes through the client or Admin SDK may block your database until the delete is completed.
>
> ```
> firebase database:remove /large/path/to/delete
> ```
> See [this blog post](https://firebase.googleblog.com/2019/03/large-deletes-in-realtime-database.html) for more information.

### orderBy


See the section in the guide on
[ordered data](https://firebase.google.com/docs/database/rest/retrieve-data#section-rest-ordered-data)
for more information.

### limitToFirst, limitToLast, startAt, endAt, equalTo


See the section in the guide on
[filtering data](https://firebase.google.com/docs/database/rest/retrieve-data#section-rest-filtering) for
more information.

## Streaming from the REST API


Firebase REST endpoints support the
[EventSource / Server-Sent Events](http://www.w3.org/TR/eventsource/)
protocol. To stream changes to a single location in your Realtime Database,
you need to do a few things:

- Set the client's Accept header to `"text/event-stream"`
- Respect HTTP Redirects, in particular HTTP status code 307
- If the location requires permission to read, you must include the [`auth`](https://firebase.google.com/docs/reference/rest/database#section-param-auth) parameter


In return, the server will send named events as the state of the data at
the requested URL changes. The structure of these messages conforms to
the `EventSource` protocol.

```
event: event name
data: JSON encoded data payload
```

The server may send the following events:

### put


The JSON-encoded data is an object with two keys: **path**
and **data** . The **path** key points to a
location relative to the request URL. The client should replace all of
the data at that location in its cache with **data**.

### patch


The JSON-encoded data is an object with two keys: **path**
and **data** . The **path** key points to a
location relative to the request URL. For each key in
**data**, the client should replace the
corresponding key in its cache with the data for that key in the message.

### keep-alive


The data for this event is `null`. No action is required.

### cancel


Some unexpected errors can send a \`cancel\` event and terminate the connection.
The cause is described in the data provided for this event. Some potential causes are as
follows:

1. The Firebase Realtime Database Security Rules no longer allow a read at the requested location. The
\`data\` description for this cause is "Permission denied."
2. A write triggered an event streamer that sent a large JSON tree that exceeds our limit,
512MB. The \`data\` for this cause is "The specified payload is too large, please request a
location with less data."

### auth_revoked


The data for this event is a string indicating that a the credential
has expired. This event is sent when the supplied `auth`
parameter is no longer valid.


Here's an example set of events that the server may send:

```
// Set your entire cache to {"a": 1, "b": 2}
event: put
data: {"path": "/", "data": {"a": 1, "b": 2}}

// Put the new data in your cache under the key 'c', so that the complete cache now looks like:
// {"a": 1, "b": 2, "c": {"foo": true, "bar": false}}
event: put
data: {"path": "/c", "data": {"foo": true, "bar": false}}

// For each key in the data, update (or add) the corresponding key in your cache at path /c,
// for a final cache of: {"a": 1, "b": 2, "c": {"foo": 3, "bar": false, "baz": 4}}
event: patch
data: {"path": "/c", "data": {"foo": 3, "baz": 4}}
```

## Priorities


Priority information for a location can be referenced with a
"virtual child" named `.priority`. You can read priorities with
`GET` requests and write them with `PUT` requests.
For example, the following request retrieves the priority of the
`users/tom` node:

```
curl 'https://[PROJECT_ID].firebaseio/users/tom/.priority.json'
```


To write priority and data at the same time, you can add a
`.priority` child to the JSON payload:

```
curl -X PUT -d '{"name": {"first": "Tom"}, ".priority": 1.0}' \
  'https://[PROJECT_ID].firebaseio/users/tom.json'
```


To write priority and a primitive value (e.g. a string) at the same time,
you can add a `.priority` child and put the primitive value
in a `.value` child:

```
curl -X PUT -d '{".value": "Tom", ".priority": 1.0}' \
  'https://[PROJECT_ID].firebaseio/users/tom/name/first.json'
```


This writes `"Tom"` with a priority of `1.0`.
Priorities can be included at any depth in the JSON payload.

## Server Values


You can write server values at a location using a placeholder value which
is an object with a single `.sv` key. The value for that key is
the type of server value you wish to set. For example, the following
request sets the node's value to the Firebase server's current
timestamp:

```
curl -X PUT -d '{".sv": "timestamp"}' \
  'https://[PROJECT_ID].firebaseio/users/tom/startedAtTime.json'
```


You can also write priorities using server values, using the
"virtual child" path noted above.


Supported server values include:

| Server Value ||
|---|---|
| **timestamp** | The time since UNIX epoch, in milliseconds. |
| **increment** | Provide an integer or floating point delta value, in the form `{ ".sv": {"increment": <delta_value> }}`, with which to atomically increment the current database value. If the data does not yet exist, the update will set the data to the delta value. If either of the delta value or the existing data are floating point numbers, both values will be interpreted as floating point numbers and applied on the back-end as a double value. Double arithmetic and representation of double values follow IEEE 754 semantics. If there is positive/negative integer overflow, the sum is calculated as a double. |

## Retrieving and Updating Firebase Realtime Database Security Rules


The REST API can also be used to retrieve and update the
[Firebase Realtime Database Security Rules](https://firebase.google.com/docs/database/security) for
your Firebase project. You'll need your Firebase project's secret, which
you can find under the
[**Service Accounts**](https://console.firebase.google.com/project/_/settings/serviceaccounts/databasesecrets) panel of your Firebase project's
setting.

```
curl 'https://[PROJECT_ID].firebaseio/.settings/rules.json?auth=FIREBASE_SECRET'
curl -X PUT -d '{ "rules": { ".read": true } }' 'https://[PROJECT_ID].firebaseio/.settings/rules.json?auth=FIREBASE_SECRET'
```

## Authenticate requests

By default, REST requests are executed with no authentication and will only succeed if the
[Realtime Database Rules](https://firebase.google.com/docs/database/security) allow public read or write access to
the data. To authenticate your request, use the
`access_token=` or `auth=` query parameters.

Learn more about authentication through the REST API in
[Authenticate REST Requests](https://firebase.google.com/docs/database/rest/auth).

## Error Conditions


The Firebase Database REST API can return the following error codes.

| HTTP Status Codes ||
|---|---|
| **400** Bad Request | One of the following error conditions: - Unable to parse `PUT` or `POST` data. - Missing `PUT` or `POST` data. - The request attempts to `PUT` or `POST` data that is too large. - The REST API call contains invalid child names as part of the path. - The REST API call path is too long. - The request contains an unrecognized server value. - The index for the query is not defined in your [Firebase Realtime Database Security Rules](https://firebase.google.com/docs/database/security#section-defining-indexes). - The request does not support one of the query parameters that is specified. - The request mixes query parameters with a shallow `GET` request. |
| **401** Unauthorized | One of the following error conditions: - The auth token has expired. - The auth token used in the request is invalid. - Authenticating with an access_token failed. - The request violates your [Firebase Realtime Database Security Rules.](https://firebase.google.com/docs/database/security) |
| **404** Not Found | The specified Realtime Database was not found. |
| **500** Internal Server Error | The server returned an error. See the error message for further details. |
| **503** Service Unavailable | The specified Firebase Realtime Database is temporarily unavailable, which means the request was not attempted. |
| **412** Precondition Failed | The request's specified ETag value in the if-match header did not match the server's value. |