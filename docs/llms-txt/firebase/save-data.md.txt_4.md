# Source: https://firebase.google.com/docs/database/rest/save-data.md.txt

| ## Ways to Save Data ||
|---|---|
| PUT | Write or replace data to a **defined path** , like `fireblog/users/user1/<data>` |
| PATCH | Update some of the keys for a defined path without replacing all of the data. |
| POST | **Add to a list of data** in our Firebase database. Every time we send a `POST` request, the Firebase client generates a unique key, like `fireblog/users/<unique-id>/<data>` |
| DELETE | Remove data from the specified Firebase database reference. |

> [!WARNING]
> Note that all examples use a read-only Firebase Realtime Database, `docs-example.firebaseio.com`. Replace this Realtime Database URL with one from the [Firebase console](https://console.firebase.google.com/) you have access to.

## Writing Data with PUT


The basic write operation through the REST API is `PUT`. To
demonstrate saving data, we'll build a blogging application with posts and users. All of the
data for our application will be stored under the path of \`fireblog\`, at the Firebase database URL
\`https://docs-examples.firebaseio.com/fireblog\`.

> [!IMPORTANT]
> If we are making REST calls from a browser that does not support some of the above methods, Firebase supports the **X-HTTP-Method-Override** header.


Let's start by saving some user data to our Firebase database. We'll store each user by a unique
username, and we'll also store their full name and date of birth. Since each user will have a
unique username, it makes sense to use `PUT` here instead of `POST` since
we already have the key and don't need to create one.


Using `PUT`, we can write a string, number, boolean, array or any JSON object to
our Firebase database. In this case we'll pass it an object:

```
curl -X PUT -d '{
  "alanisawesome": {
    "name": "Alan Turing",
    "birthday": "June 23, 1912"
  }
}' 'https://docs-examples.firebaseio.com/fireblog/users.json'
```


When a JSON object is saved to the database, the object properties are
automatically mapped to child locations in a nested fashion. If we navigate
to the newly created node, we'll see the value "Alan Turing". We can also
save data directly to a
child location:

```
curl -X PUT -d '"Alan Turing"' \
  'https://docs-examples.firebaseio.com/fireblog/users/alanisawesome/name.json'
```

```
curl -X PUT -d '"June 23, 1912"' \
  'https://docs-examples.firebaseio.com/fireblog/users/alanisawesome/birthday.json'
```


The above two examples---writing the value at the same time as an object and writing them
separately to child locations---will result in the same data being saved to our Firebase
database:

```
{
  "users": {
    "alanisawesome": {
      "date_of_birth": "June 23, 1912",
      "full_name": "Alan Turing"
    }
  }
}
```


A successful request will be indicated by a `200 OK` HTTP status code, and the
response will contain the data we wrote to the database. The first example will only
trigger one event on clients that are watching the data, whereas the second example will trigger
two. It is important to note that if data already existed at the users path, the first approach
would overwrite it, but the second method would only modify the value of each separate child
node while leaving other children unchanged. `PUT` is equivalent to
[`set()`](https://firebase.google.com/docs/reference/js/database#set) in our JavaScript SDK.

> [!IMPORTANT]
> Using **PUT** will overwrite the data at the specified location, including any child nodes.

## Updating Data with PATCH


Using a `PATCH` request, we can update specific children at a location without
overwriting existing data. Let's add Turing's nickname to his user data with a `PATCH`
request:

```
curl -X PATCH -d '{
  "nickname": "Alan The Machine"
}' \
  'https://docs-examples.firebaseio.com/fireblog/users/alanisawesome.json'
```


The above request will write `nickname` to our `alanisawesome` object
without deleting the `name` or `birthday` children. Note that if we had
issued a `PUT` request here instead, `name` and `birthday`
would have been deleted since they were not included in the request. The data in our Firebase
database now looks like this:

```
{
  "users": {
    "alanisawesome": {
      "date_of_birth": "June 23, 1912",
      "full_name": "Alan Turing",
      "nickname": "Alan The Machine"
    }
  }
}
```


A successful request will be indicated by a `200 OK` HTTP status code, and the
response will contain the updated data written to the database.


Firebase also supports multi-path updates. This means that `PATCH` can now update values at multiple locations in your Firebase database at the same time, a powerful feature which allows helps you
[denormalize your data](https://firebase.googleblog.com/2013/04/denormalizing-your-data-is-normal.html). Using multi-path updates, we can add nicknames to both Alan and Grace at the same time:

```
curl -X PATCH -d '{
  "alanisawesome/nickname": "Alan The Machine",
  "gracehopper/nickname": "Amazing Grace"
}' \
  'https://docs-examples.firebaseio.com/fireblog/users.json'
```


After this update, both Alan and Grace have had their nicknames added:

```
{
  "users": {
    "alanisawesome": {
      "date_of_birth": "June 23, 1912",
      "full_name": "Alan Turing",
      "nickname": "Alan The Machine"
    },
    "gracehop": {
      "date_of_birth": "December 9, 1906",
      "full_name": "Grace Hopper",
      "nickname": "Amazing Grace"
    }
  }
}
```


Note that trying to update objects by writing objects with the paths included will result in different behavior. Let's take a look at what happens if we instead try to update Grace and Alan this way:

```
curl -X PATCH -d '{
  "alanisawesome": {"nickname": "Alan The Machine"},
  "gracehopper": {"nickname": "Amazing Grace"}
}' \
  'https://docs-examples.firebaseio.com/fireblog/users.json'
```


This results in different behavior, namely overwriting the entire `/fireblog/users` node:

```
{
  "users": {
    "alanisawesome": {
      "nickname": "Alan The Machine"
    },
    "gracehop": {
      "nickname": "Amazing Grace"
    }
  }
}
```

## Updating Data with Conditional Requests

You can use conditional requests, the REST equivalent to transactions, to update data according to its existing state. For example, if you want to increase an upvote counter, and want to make sure the count accurately reflects multiple, simultaneous upvotes, use a conditional request to write the new value to the counter. Instead of two writes that change the counter to the same number, one of the write requests fails and you can then retry the request with the new value.

1. To perform a conditional request at a location, get the unique identifier for the current data at that location, or the ETag. If the data changes at that location, the ETag changes, too. You can request an ETag with any method other than `PATCH`. The following example uses a `GET` request.

   ```
   curl -i 'https://test.example.com/posts/12345/upvotes.json' -H 'X-Firebase-ETag: true'
   ```
   Specifically calling the ETag in the header returns the ETag of the specified location in the HTTP response.

   ```
   HTTP/1.1 200 OK
   Content-Length: 6
   Content-Type: application/json; charset=utf-8
   Access-Control-Allow-Origin: *
   ETag: [ETAG_VALUE]
   Cache-Control: no-cache

   10 // Current value of the data at the specified location
   ```
2. Include the returned ETag in your next `PUT` or `DELETE` request to update data that specifically matches that ETag value. Following our example, to update the counter to 11, or 1 larger than the initial fetched value of 10, and fail the request if the value no longer matches, use the following code:

   ```
   curl -iX PUT -d '11' 'https://[PROJECT_ID].firebaseio.com/posts/12345/upvotes.json' -H 'if-match:[ETAG_VALUE]'
   ```
   If the value of the data at the specified location is still 10, the ETag in the `PUT` request matches, and the request succeeds, writing 11 to the database.

   ```
   HTTP/1.1 200 OK
   Content-Length: 6
   Content-Type: application/json; charset=utf-8
   Access-Control-Allow-Origin: *
   Cache-Control: no-cache

   11 // New value of the data at the specified location, written by the conditional request
   ```
   If the location no longer matches the ETag, which might occur if another user wrote a new value to the database, the request fails without writing to the location. The return response includes the new value and ETag.

   ```
   HTTP/1.1 412 Precondition Failed
   Content-Length: 6
   Content-Type: application/json; charset=utf-8
   Access-Control-Allow-Origin: *
   ETag: [ETAG_VALUE]
   Cache-Control: no-cache

   12 // New value of the data at the specified location
   ```
3. Use the new information if you decide to retry the request. Realtime Database does not automatically retry conditional requests that have failed. However, you can use the new value and ETag to build a new conditional request with the information returned by the fail response.

REST-based conditional requests implement the HTTP
[if-match](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match)
standard. However, they differ from the standard in the following ways:

- You can only supply one ETag value for each if-match request, not multiple.
- While the standard suggests that ETags be returned with all requests, Realtime Database only returns ETags with requests including the `X-Firebase-ETag` header. This reduces billing costs for standard requests.

Conditional requests might also be slower than typical REST requests.

## Saving Lists of Data


To generate a unique, timestamp-based key for every child added to a Firebase database reference
we can send a `POST` request. For our `users` path, it made sense to
define our own keys since each user has a unique username. But when users add blog posts to the
app, we'll use a `POST` request to auto-generate a key for each blog post:

```
curl -X POST -d '{
  "author": "alanisawesome",
  "title": "The Turing Machine"
}' 'https://docs-examples.firebaseio.com/fireblog/posts.json'
```


Our `posts` path now has the following data:

```
{
  "posts": {
    "-JSOpn9ZC54A4P4RoqVa": {
      "author": "alanisawesome",
      "title": "The Turing Machine"
    }
  }
}
```


Notice that the key `-JSOpn9ZC54A4P4RoqVa` was automatically generated for us because
we used a `POST` request. A successful request will be indicated by a `200 OK`
HTTP status code, and the response will contain the key of the new data that was added:

```
{"name":"-JSOpn9ZC54A4P4RoqVa"}
```

> [!NOTE]
> Interested in learning more about how push keys are generated? Check out [this blog post](https://firebase.googleblog.com/2015/02/the-2120-ways-to-ensure-unique_68.html).

## Removing Data


To remove data from the database, we can send a `DELETE` request with the
URL of the path from which we'd like to delete data. The following would delete Alan from our
`users` path:

```
curl -X DELETE \
  'https://docs-examples.firebaseio.com/fireblog/users/alanisawesome.json'
```


A successful `DELETE` request will be indicated by a `200 OK` HTTP status code with a response containing JSON `null`.

## URI Parameters


The REST API accepts the following URI parameters when writing data to the database:

### auth


The `auth` request parameter allows access to data protected by
[Firebase Realtime Database Security Rules](https://firebase.google.com/docs/database/security/rules-conditions), and is
supported by all request types. The argument can either be our Firebase app secret or an
authentication token, which we'll cover in the [user authorization
section](https://firebase.google.com/docs/auth/users). In the following example we send a `POST` request with an
`auth` parameter, where `CREDENTIAL` is either our Firebase app secret or
an authentication token:

```
curl -X POST -d '{"Authenticated POST request"}' \
  'https://docs-examples.firebaseio.com/auth-example.json?auth=CREDENTIAL'
```

> [!NOTE]
> If the token `debug` flag is set, debug information can be found in the **X-Firebase-Auth-Debug** header of the response.

### print


The `print` parameter lets us specify the format of our response from the
database. Adding `print=pretty` to our request will return the data in a
human-readable format. `print=pretty` is supported by `GET`,
`PUT`, `POST`, `PATCH`, and `DELETE` requests.


To suppress the output from the server when writing data, we can add
`print=silent` to our request. The resulting response will be empty and indicated by
a `204 No Content` HTTP status code if the request is successful.
The `print=silent` is supported by `GET`, `PUT`,
`POST`, and `PATCH` requests.

## Writing Server Values


Server values can be written at a location using a placeholder value, which is an object with a
single `".sv"` key. The value for that key is the type of server value we wish to set.
For example, to set a timestamp when a user is created we could do the following:

```
curl -X PUT -d '{".sv": "timestamp"}' \
  'https://docs-examples.firebaseio.com/alanisawesome/createdAt.json'
```


`"timestamp"` is the only supported server value, and is the time since the UNIX
epoch in milliseconds.

## Improving Write Performance


If we're writing large amounts of data to the database, we can use the
`print=silent` parameter to improve our write performance and decrease bandwidth
usage. In the normal write behavior, the server responds with the JSON data that was written.
When `print=silent` is specified, the server immediately
closes the connection once the data is received, reducing bandwidth usage.


In cases where we're making many requests to the database, we can re-use the HTTPS
connection by sending a `Keep-Alive` request in the HTTP header.

## Error Conditions


The REST API will return error codes under these circumstances:

| HTTP Status Codes ||
|---|---|
| **400** Bad Request | One of the following error conditions: - Unable to parse `PUT` or `POST` data. - Missing `PUT` or `POST` data. - The request attempts to `PUT` or `POST` data that is too large. - The REST API call contains invalid child names as part of the path. - The REST API call path is too long. - The request contains an unrecognized server value. - The index for the query is not defined in your [Firebase Realtime Database Security Rules](https://firebase.google.com/docs/database/security/indexing-data). - The request does not support one of the query parameters that is specified. - The request mixes query parameters with a shallow `GET` request. |
| **401** Unauthorized | One of the following error conditions: - The auth token has expired. - The auth token used in the request is invalid. - Authenticating with an access_token failed. - The request violates your [Firebase Realtime Database Security Rules.](https://firebase.google.com/docs/database/security) |
| **404** Not Found | The specified Firebase database was not found. |
| **500** Internal Server Error | The server returned an error. See the error message for further details. |
| **503** Service Unavailable | The specified Firebase Realtime Database is temporarily unavailable, which means the request was not attempted. |

## Securing Data


Firebase has a security language that lets us define which users have read and write access to
different nodes of our data. You can read more about it in
[Realtime Database Security Rules](https://firebase.google.com/docs/database/security).


Now that we've covered saving data, we can learn how to retrieve our data from the Firebase
database through the REST API in the next section.