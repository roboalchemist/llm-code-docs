# Source: https://firebase.google.com/docs/database/rest/retrieve-data.md.txt

## Reading Data with GET


We can read data from our Firebase database by issuing a `GET` request to its URL
endpoint. Let's continue with our blog example from the previous section and read all of our
blog post data:

```
curl 'https://docs-examples.firebaseio.com/fireblog/posts.json?print=pretty'
```


A successful request will be indicated by a `200 OK` HTTP status code, and the
response will contain the data we're retrieving.

## Adding URI Parameters


The REST API accepts several query parameters when reading data from our Firebase database.
Listed below are the most commonly used parameters. For a full list, refer to the
[REST API Reference](https://firebase.google.com/docs/reference/rest/database#section-query-parameters).

### auth


The `auth` request parameter allows access to data protected by
[Firebase Realtime Database Security Rules](https://firebase.google.com/docs/database/security/rules-conditions), and is
supported by all request types. The argument can either be your Firebase app's secret or an
authentication token, as described in the [Users in Firebase Projects](https://firebase.google.com/docs/auth/users). In the following example we send a `GET` request with an `auth`
parameter, where `CREDENTIAL` is either your Firebase app's secret or an
authentication token:

```
curl 'https://docs-examples.firebaseio.com/auth-example.json?auth=CREDENTIAL'
```

> [!IMPORTANT]
> If the token's `debug` flag is set, debug information can be found in the **X-Firebase-Auth-Debug** header of the response.

### print


Specifying `print=pretty` returns the data in a human-readable format.

```
curl 'https://docs-examples.firebaseio.com/fireblog/posts.json?print=pretty'
```


Specifying `print=silent` returns a `204 No Content` on success.

```
curl 'https://docs-examples.firebaseio.com/fireblog/posts.json?print=silent'
```

### callback


To make REST calls from a web browser across domains you can use
[JSONP](https://en.wikipedia.org/wiki/JSONP) to wrap the response in a JavaScript
callback function. Add `callback=` to have the REST API wrap the returned data in the
callback function you specify. For example:

```
<script>
  function gotData(data) {
    console.log(data);
  }
</script>
<script src="https://docs-examples.firebaseio.com/fireblog/posts.json?callback=gotData">
```

### shallow


This is an advanced feature, designed to help you work with large datasets without needing to
download everything. To use it, add `shallow=true` as a parameter. This will limit
the depth of the data returned. If the data at the location is a JSON primitive (string, number,
or boolean) its value will simply be returned. If the data snapshot at the location is a JSON
object, the values for each key will be truncated to **true**. For example, using
the data below:

```
{
  "message": {
    "user": {
      "name": "Chris"
    },
    "body": "Hello!"
  }
}

// A request to /message.json?shallow=true
// would return the following:
{
  "user": true,
  "body": true
}

// A request to /message/body.json?shallow=true
// would simply return:
"Hello!"
```


Try it out with this `curl` request:

```
curl 'https://docs-examples.firebaseio.com/rest/retrieving-data.json?shallow=true&print=pretty'
```

> [!WARNING]
> `shallow` cannot be used with any of the "filtering data" query parameters.

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
In the following example, the `GET` request includes a
`timeout` of 10 seconds.

```
curl 'https://docs-examples.firebaseio.com/rest/retrieving-data.json?timeout=10s'
```

## Filtering Data


We can construct queries to filter data based on various factors. To start, you specify how you want your data to be filtered using the `orderBy`
parameter. Then, you combine `orderBy` with any of the other five parameters:
`limitToFirst`, `limitToLast`, `startAt`, `endAt`,
and `equalTo`.

> [!WARNING]
> **Filtered data is returned unordered**: When using the REST API, the filtered results are returned in an undefined order since JSON interpreters don't enforce any ordering. If the order of your data is important you should sort the results in your application after they are returned from Firebase.


Since all of us at Firebase think dinosaurs are pretty cool, we'll use
a snippet from a sample database of dinosaur facts to demonstrate how
you can filter data:

```
{
  "lambeosaurus": {
    "height": 2.1,
    "length": 12.5,
    "weight": 5000
  },
  "stegosaurus": {
    "height": 4,
    "length": 9,
    "weight": 2500
  }
}
```


We can filter data in one of three ways: by **child key** , by **key** , or by
**value** . A query starts with one of these parameters, and then must be combined with one or more of the following parameters: `startAt`, `endAt`, `limitToFirst`, `limitToLast`, or `equalTo`.

### Filtering by a specified child key


We can filter nodes by a common child key by passing that key to the `orderBy`
parameter. For example, to retrieve all dinosaurs with a height greater than 3, we can do the following:

```
curl 'https://dinosaur-facts.firebaseio.com/dinosaurs.json?orderBy="height"&startAt=3&print=pretty'
```


Any node that does not have the child key we're filtering on will be sorted with a value of
`null`. For details on how data is
ordered, see [How Data is Ordered](https://firebase.google.com/docs/database/rest/retrieve-data#section-rest-ordered-data).


Firebase also supports queries ordered by deeply nested children, rather than only children one level down. This is useful if you have deeply nested data like this:

```
{
  "lambeosaurus": {
    "dimensions": {
      "height" : 2.1,
      "length" : 12.5,
      "weight": 5000
    }
  },
  "stegosaurus": {
    "dimensions": {
      "height" : 4,
      "length" : 9,
      "weight" : 2500
    }
  }
}
```


To query the height now, we use the full path to the object rather than a single key:

```
curl 'https://dinosaur-facts.firebaseio.com/dinosaurs.json?orderBy="dimensions/height"&startAt=3&print=pretty'
```


Queries can only filter by one key at a time. Using the `orderBy` parameter multiple
times on the same request throws an error.

> [!WARNING]
> **Add Indexing to your Firebase Realtime Database Security Rules** : If you're using `orderBy` in your app, you need to define the keys you will be indexing on via the `.indexOn` rule in your Firebase Realtime Database Security Rules. [Read the documentation](https://firebase.google.com/docs/database/security/indexing-data) on the `.indexOn` rule for more information.

### Filtering by key


We can also filter nodes by their keys using the `orderBy="$key"` parameter. The
following example retrieves all dinosaurs with a name starting with the letter `a` through `m`:

```
curl 'https://dinosaur-facts.firebaseio.com/dinosaurs.json?orderBy="$key"&startAt="a"&endAt="m"&print=pretty'
```

### Filtering by value


We can filter nodes by the value of their child keys using the `orderBy="$value"`
parameter. Let's say the dinosaurs are having a dino sports competition and we're keeping
track of their scores in the following format:

```
{
  "scores": {
    "bruhathkayosaurus": 55,
    "lambeosaurus": 21,
    "linhenykus": 80,
    "pterodactyl": 93,
    "stegosaurus": 5,
    "triceratops": 22
  }
}
```


To retrieve all dinosaurs with a score higher than 50, we could make the following request:

```
curl 'https://dinosaur-facts.firebaseio.com/scores.json?orderBy="$value"&startAt=50&print=pretty'
```


See [How Data is Ordered](https://firebase.google.com/docs/database/rest/retrieve-data#section-rest-ordered-data) for an explanation on
how `null`, boolean, string, and object values are sorted when using
`orderBy="$value"`.

> [!WARNING]
> **Add Indexing to your Firebase Realtime Database Security Rules** : If you're using `orderBy="$value"` in your app, you need to add `.value` to your rules at the appropriate index. [Read the documentation](https://firebase.google.com/docs/database/security/indexing-data) on the `.indexOn` rule for more information.

## Complex Filtering


We can combine multiple parameters to construct more complex queries.

### Limit Queries


The `limitToFirst` and `limitToLast` parameters are used to set a
maximum number of children for which to receive data. If we set a limit of 100, we will only
receive up to 100 matching children. If we have less than 100 messages stored in our
database, we will receive every child. However, if we have over 100 messages, we will only
receive data for 100 of those messages. These will be the first 100 ordered messages if we are
using `limitToFirst` or the last 100 ordered messages if we are using
`limitToLast`.


Using our dinosaur facts database and `orderBy`, we can find the two
heaviest dinosaurs:

```
curl 'https://dinosaur-facts.firebaseio.com/dinosaurs.json?orderBy="weight"&limitToLast=2&print=pretty'
```


Similarly, we can find the two shortest dinosaurs by using `limitToFirst`:

```
curl 'https://dinosaur-facts.firebaseio.com/dinosaurs.json?orderBy="height"&limitToFirst=2&print=pretty'
```


We can also conduct limit queries with `orderBy="$value"`. If we want to create a
leaderboard with the top three highest scoring dino sports competitors, we could do the
following:

```
curl 'https://dinosaur-facts.firebaseio.com/scores.json?orderBy="$value"&limitToLast=3&print=pretty'
```

### Range Queries


Using `startAt`, `endAt`, and `equalTo` allows us to choose
arbitrary starting and ending points for our queries. For example, if we wanted to find all
dinosaurs that are at least three meters tall, we can combine `orderBy` and
`startAt`:

```
curl 'https://dinosaur-facts.firebaseio.com/dinosaurs.json?orderBy="height"&startAt=3&print=pretty'
```


We can use `endAt` to find all dinosaurs whose names come before Pterodactyl
lexicographically:

```
curl 'https://dinosaur-facts.firebaseio.com/dinosaurs.json?orderBy="$key"&endAt="pterodactyl"&print=pretty'
```

> [!NOTE]
> `startAt` and `endAt` are inclusive, meaning "pterodactyl" will match the query above.


We can combine `startAt` and `endAt` to limit both ends of our query.
The following example finds all dinosaurs whose name starts with the letter "b":

```
curl 'https://dinosaur-facts.firebaseio.com/dinosaurs.json?orderBy="$key"&startAt="b"&endAt="b\uf8ff"&print=pretty'
```

> [!NOTE]
> The `\uf8ff` character used in the query above is a very high code point in the Unicode range. Because it is after most regular characters in Unicode, the query matches all values that start with a b.


Range queries are also useful when you need to paginate your data.

### Putting it all together


We can combine all of these techniques to create complex queries. For example, maybe you want
to find the name of all dinosaurs that are shorter than or equal in height to our favorite
kind, Stegosaurus:

```
MY_FAV_DINO_HEIGHT=`curl "https://dinosaur-facts.firebaseio.com/dinosaurs/stegosaurus/height.json"`
curl "https://dinosaur-facts.firebaseio.com/dinosaurs.json?orderBy=\"height\"&endAt=${MY_FAV_DINO_HEIGHT}&print=pretty"
```

## How Data is Ordered


This section explains how your data is ordered when using each of the three filtering parameters.

> [!WARNING]
> **The REST API Returns Unsorted Results** : JSON interpreters do not enforce any ordering on the result set. While `orderBy` can be used in combination with `startAt`, `endAt`, `limitToFirst`, or `limitToLast` to return a subset of the data, the returned results will not be sorted. Therefore, it may be necessary to manually sort the results if ordering is important.

### orderBy


When using `orderBy` with the name of a child key, data that contains the specified
child key will be ordered as follows:

1. Children with a `null` value for the specified child key come first.
2. Children with a value of `false` for the specified child key come next. If multiple children have a value of `false`, they are sorted [lexicographically](http://en.wikipedia.org/wiki/Lexicographical_order) by key.
3. Children with a value of `true` for the specified child key come next. If multiple children have a value of `true`, they are sorted lexicographically by key.
4. Children with a numeric value come next, sorted in ascending order. If multiple children have the same numerical value for the specified child node, they are sorted by key.
5. Strings come after numbers, and are sorted lexicographically in ascending order. If multiple children have the same value for the specified child node, they are ordered lexicographically by key.
6. Objects come last, and sorted lexicographically by key in ascending order.

The filtered results are returned unordered. If the order of your data is important you should sort the results in your application after they are returned from Firebase.

### orderBy="$key"


When using the `orderBy="$key"` parameter to sort your data, data will be returned
in ascending order by key as follows. Keep in mind that keys can only be strings.

1. Children with a key that can be parsed as a 32-bit integer come first, sorted in ascending order.
2. Children with a string value as their key come next, sorted lexicographically in ascending order.

### orderBy="$value"


When using the `orderBy="$value"` parameter to sort your data, children will be
ordered by their value. The ordering criteria is the same as data ordered by a child key,
except the value of the node is used instead of the value of a specified child key.

### orderBy="$priority"


When using the `orderBy="$priority"` parameter to sort your data, the ordering of
children is determined by their priority and key as follows. Keep in mind that priority values
can only be numbers or strings.

> [!IMPORTANT]
> Numeric priorities are stored and ordered as IEEE 754 double-precision floating-point numbers. Keys are always stored as strings and are treated as numeric only when they can be parsed as a 32-bit integer.

1. Children with no priority (the default) come first.
2. Children with a number as their priority come next. They are sorted numerically by priority, small to large.
3. Children with a string as their priority come last. They are sorted lexicographically by priority.
4. Whenever two children have the same priority (including no priority), they are sorted by key. Numeric keys come first (sorted numerically), followed by the remaining keys (sorted lexicographically).


For more information on priorities, see the
[API reference](https://firebase.google.com/docs/reference/rest#section-priorities).

## Streaming from the REST API


Firebase REST endpoints support the [EventSource /
Server-Sent Events](http://www.w3.org/TR/eventsource/) protocol, making it easy to stream changes to a single location in our
Firebase database.

<br />


To get started with streaming, we will need to do the following:

<br />

<br />

1. Set the client's Accept header to `text/event-stream`
2. Respect HTTP Redirects, in particular HTTP status code 307
3. Include the `auth` query parameter if the Firebase database location requires permission to read

<br />

<br />


In return, the server will send named events as the state of the data at the requested URL
changes. The structure of these messages conforms to the EventSource protocol:

<br />

```
event: event name
data: JSON encoded data payload
```

<br />


The server may send the following events:

<br />

|---|---|
| put | The JSON-encoded data will be an object with two keys: path and data The path points to a location relative to the request URL The client should replace all of the data at that location in its cache with the data given in the message |
| patch | The JSON-encoded data will be an object with two keys: path and data The path points to a location relative to the request URL For each key in the data, the client should replace the corresponding key in its cache with the data for that key in the message |
| keep-alive | The data for this event is null, no action is required |
| cancel | The data for this event is null This event will be sent if the Firebase Realtime Database Security Rules cause a read at the requested location to no longer be allowed |
| auth_revoked | The data for this event is a string indicating that a the credential has expired This event will be sent when the supplied auth parameter is no longer valid |

<br />


Below is an example of a set of events that the server may send:

<br />

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

<br />


If you're using Go, check out [Firego](https://github.com/CloudCom/firego), a
third-party wrapper around the Firebase REST and Streaming APIs.

<br />