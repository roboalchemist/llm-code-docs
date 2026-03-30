# Source: https://docs.parseplatform.org/rest/guide/

Title: Parse

URL Source: https://docs.parseplatform.org/rest/guide/

Published Time: Sat, 07 Feb 2026 17:30:01 GMT

Markdown Content:
[](https://docs.parseplatform.org/rest/guide/#your-configuration)Your Configuration
-----------------------------------------------------------------------------------

Customize our docs with your server configuration.

Note: `masterKey` overrides all permissions. Keep this secret.

Protocol:

 Domain: Mount Path: App Id: Master Key: Client Key: Rest API Key:

*   serverUrl: `https://YOUR.PARSE-SERVER.HERE/parse/`
*   appId: `APPLICATION_ID`
*   masterKey: `MASTER_KEY`
*   clientKey: `CLIENT_KEY`
*   restApiKey: `REST_API_KEY`

[](https://docs.parseplatform.org/rest/guide/#getting-started)Getting Started
-----------------------------------------------------------------------------

The REST API lets you interact with Parse Server from anything that can send an HTTP request. There are many things you can do with the REST API. For example:

*   A mobile website can access Parse Server data from JavaScript.
*   A web server can show data from Parse Server on a website.
*   You can upload large amounts of data that will later be consumed in a mobile app.
*   You can download recent data to run your own custom analytics.
*   Applications written in any programming language can interact with data on Parse Server.

[](https://docs.parseplatform.org/rest/guide/#quick-reference)Quick Reference
-----------------------------------------------------------------------------

For your convenience you can customize [your configuration](https://docs.parseplatform.org/rest/guide/#your-configuration) to change the default server url, mount path and additional values to match your personal setup.

All API access is provided via the domain to your parse server instance. In cases where a domain is used to access the API we will reference `YOUR.PARSE-SERVER.HERE`, which should be set to your domain in [your configuration](https://docs.parseplatform.org/rest/guide/#your-configuration).

The relative path prefix `/parse/` is the default mount path for most installations. If you are using a different mount path be sure to change this to accommodate for your instance. If you are using a hosted service this may be something other than the expected `/parse/`, be sure to check before you proceed. For the following examples we will be using `/parse/`, which can be set in [your configuration](https://docs.parseplatform.org/rest/guide/#your-configuration).

API access can be provided over **HTTPS** and **HTTP**. We recommend utilizing **HTTPS** for anything other than local development. If you are using a hosted service you will almost certainly be accessing your API exclusively over **HTTPS**.

[](https://docs.parseplatform.org/rest/guide/#objects-api)Objects API
---------------------------------------------------------------------

| URL | HTTP Verb | Functionality |
| --- | --- | --- |
| `/parse/classes/<className>` | POST | [Creating Objects](https://docs.parseplatform.org/rest/guide/#creating-objects) |
| `/parse/classes/<className>/<objectId>` | GET | [Retrieving Objects](https://docs.parseplatform.org/rest/guide/#retrieving-objects) |
| `/parse/classes/<className>/<objectId>` | PUT | [Updating Objects](https://docs.parseplatform.org/rest/guide/#updating-objects) |
| `/parse/classes/<className>` | GET | [Queries](https://docs.parseplatform.org/rest/guide/#queries) |
| `/parse/classes/<className>/<objectId>` | DELETE | [Deleting Objects](https://docs.parseplatform.org/rest/guide/#deleting-objects) |

[](https://docs.parseplatform.org/rest/guide/#users-api)Users API
-----------------------------------------------------------------

| URL | HTTP Verb | Functionality |
| --- | --- | --- |
| `/parse/users` | POST | [Signing Up](https://docs.parseplatform.org/rest/guide/#signing-up) [Linking Users](https://docs.parseplatform.org/rest/guide/#linking-users) |
| `/parse/login` | GET | [Logging In](https://docs.parseplatform.org/rest/guide/#logging-in) |
| `/parse/logout` | POST | [Logging Out](https://docs.parseplatform.org/rest/guide/#deleting-sessions) |
| `/parse/users/<objectId>` | GET | [Retrieving Users](https://docs.parseplatform.org/rest/guide/#retrieving-users) |
| `/parse/users/me` | GET | [Validating Session Tokens](https://docs.parseplatform.org/rest/guide/#validating-session-tokens--retrieving-current-user) [Retrieving Current User](https://docs.parseplatform.org/rest/guide/#retrieving-users) |
| `/parse/users/<objectId>` | PUT | [Updating Users](https://docs.parseplatform.org/rest/guide/#updating-users) [Linking Users](https://docs.parseplatform.org/rest/guide/#linking-users) [Verifying Emails](https://docs.parseplatform.org/rest/guide/#verifying-emails) |
| `/parse/users` | GET | [Querying Users](https://docs.parseplatform.org/rest/guide/#querying) |
| `/parse/users/<objectId>` | DELETE | [Deleting Users](https://docs.parseplatform.org/rest/guide/#deleting-users) |
| `/parse/requestPasswordReset` | POST | [Requesting A Password Reset](https://docs.parseplatform.org/rest/guide/#requesting-a-password-reset) |

[](https://docs.parseplatform.org/rest/guide/#sessions-api)Sessions API
-----------------------------------------------------------------------

| URL | HTTP Verb | Functionality |
| --- | --- | --- |
| `/parse/sessions` | POST | [Creating Restricted Sessions](https://docs.parseplatform.org/rest/guide/#creating-sessions) |
| `/parse/sessions/<objectId>` | GET | [Retrieving Sessions](https://docs.parseplatform.org/rest/guide/#retrieving-sessions) |
| `/parse/sessions/me` | GET | [Retrieving Current Session](https://docs.parseplatform.org/rest/guide/#retrieving-sessions) |
| `/parse/sessions/<objectId>` | PUT | [Updating Sessions](https://docs.parseplatform.org/rest/guide/#updating-sessions) |
| `/parse/sessions` | GET | [Querying Sessions](https://docs.parseplatform.org/rest/guide/#querying-sessions) |
| `/parse/sessions/<objectId>` | DELETE | [Deleting Sessions](https://docs.parseplatform.org/rest/guide/#deleting-sessions) |
| `/parse/sessions/me` | PUT | [Pairing with Installation](https://docs.parseplatform.org/rest/guide/#pairing-session-with-installation) |

[](https://docs.parseplatform.org/rest/guide/#roles-api)Roles API
-----------------------------------------------------------------

| URL | HTTP Verb | Functionality |
| --- | --- | --- |
| `/parse/roles` | POST | [Creating Roles](https://docs.parseplatform.org/rest/guide/#creating-roles) |
| `/parse/roles/<objectId>` | GET | [Retrieving Roles](https://docs.parseplatform.org/rest/guide/#retrieving-roles) |
| `/parse/roles/<objectId>` | PUT | [Updating Roles](https://docs.parseplatform.org/rest/guide/#updating-roles) |
| `/parse/roles/<objectId>` | DELETE | [Deleting Roles](https://docs.parseplatform.org/rest/guide/#deleting-roles) |

[](https://docs.parseplatform.org/rest/guide/#files-api)Files API
-----------------------------------------------------------------

| URL | HTTP Verb | Functionality |
| --- | --- | --- |
| `/parse/files/<fileName>` | POST | [Uploading Files](https://docs.parseplatform.org/rest/guide/#uploading-files) |

[](https://docs.parseplatform.org/rest/guide/#analytics-api)Analytics API
-------------------------------------------------------------------------

| URL | HTTP Verb | Functionality |
| --- | --- | --- |
| `/parse/events/AppOpened` | POST | [Analytics](https://docs.parseplatform.org/rest/guide/#app-open-analytics) |
| `/parse/events/<eventName>` | POST | [Custom Analytics](https://docs.parseplatform.org/rest/guide/#custom-analytics) |

[](https://docs.parseplatform.org/rest/guide/#push-notifications-api)Push Notifications API
-------------------------------------------------------------------------------------------

| URL | HTTP Verb | Functionality |
| --- | --- | --- |
| `/parse/push` | POST | [Push Notifications](https://docs.parseplatform.org/rest/guide/#push-notifications) |

[](https://docs.parseplatform.org/rest/guide/#installations-api)Installations API
---------------------------------------------------------------------------------

| URL | HTTP Verb | Functionality |
| --- | --- | --- |
| `/parse/installations` | POST | [Uploading Installation Data](https://docs.parseplatform.org/rest/guide/#uploading-installation-data) |
| `/parse/installations/<objectId>` | GET | [Retrieving Installations](https://docs.parseplatform.org/rest/guide/#retrieving-installations) |
| `/parse/installations/<objectId>` | PUT | [Updating Installations](https://docs.parseplatform.org/rest/guide/#updating-installations) |
| `/parse/installations` | GET | [Querying Installations](https://docs.parseplatform.org/rest/guide/#querying-installations) |
| `/parse/installations/<objectId>` | DELETE | [Deleting Installations](https://docs.parseplatform.org/rest/guide/#deleting-installations) |

[](https://docs.parseplatform.org/rest/guide/#cloud-functions-api)Cloud Functions API
-------------------------------------------------------------------------------------

| URL | HTTP Verb | Functionality |
| --- | --- | --- |
| `/parse/functions/<name>` | POST | [Calling Cloud Functions](https://docs.parseplatform.org/rest/guide/#calling-cloud-functions) |
| `/parse/jobs/<name>` | POST | [Triggering Background Jobs](https://docs.parseplatform.org/rest/guide/#triggering-background-jobs) |

[](https://docs.parseplatform.org/rest/guide/#schemas-api)Schemas API
---------------------------------------------------------------------

| URL | HTTP Verb | Functionality |
| --- | --- | --- |
| `/parse/schemas/` | GET | [Fetch All Schemas](https://docs.parseplatform.org/rest/guide/#fetch-the-schema) |
| `/parse/schemas/<className>` | GET | [Fetch Schema](https://docs.parseplatform.org/rest/guide/#fetch-the-schema) |
| `/parse/schemas/<className>` | POST | [Create Schema](https://docs.parseplatform.org/rest/guide/#adding-a-schema) |
| `/parse/schemas/<className>` | PUT | [Modify Schema](https://docs.parseplatform.org/rest/guide/#modifying-the-schema) |
| `/parse/schemas/<className>` | DELETE | [Delete Schema](https://docs.parseplatform.org/rest/guide/#removing-a-schema) |

[](https://docs.parseplatform.org/rest/guide/#function-hooks-api)Function Hooks API
-----------------------------------------------------------------------------------

| URL | HTTP Verb | Functionality |
| --- | --- | --- |
| `/parse/hooks/functions/<functionName>` | GET | [Fetch Cloud Functions](https://docs.parseplatform.org/rest/guide/#fetch-functions) |
| `/parse/hooks/functions/` | POST | [Create Cloud Function](https://docs.parseplatform.org/rest/guide/#create-function-webhook) |
| `/parse/hooks/functions/<functionName>` | PUT | [Edit Cloud Function](https://docs.parseplatform.org/rest/guide/#edit-function-webhook) |
| `/parse/hooks/functions/<functionName>` | DELETE | [Delete Cloud Function](https://docs.parseplatform.org/rest/guide/#delete-function-webhook) |

[](https://docs.parseplatform.org/rest/guide/#trigger-hooks-api)Trigger Hooks API
---------------------------------------------------------------------------------

| URL | HTTP Verb | Functionality |
| --- | --- | --- |
| `/parse/hooks/triggers/<className>/<triggerName>` | GET | [Fetch Cloud Trigger](https://docs.parseplatform.org/rest/guide/#fetch-triggers) |
| `/parse/hooks/triggers/` | POST | [Create Cloud Trigger](https://docs.parseplatform.org/rest/guide/#create-trigger-webhook) |
| `/parse/hooks/triggers/<className>/<triggerName>` | PUT | [Edit Cloud Trigger](https://docs.parseplatform.org/rest/guide/#edit-trigger-webhook) |
| `/parse/hooks/triggers/<className>/<triggerName>` | DELETE | [Delete Cloud Trigger](https://docs.parseplatform.org/rest/guide/#delete-trigger-webhook) |

[](https://docs.parseplatform.org/rest/guide/#request-format)Request Format
---------------------------------------------------------------------------

For POST and PUT requests, the request body must be JSON, with the `Content-Type` header set to `application/json`.

Authentication is done via HTTP headers. The `X-Parse-Application-Id` header identifies which application you are accessing, and the `X-Parse-REST-API-Key` header authenticates the endpoint.

In the examples that follow, the keys for your app are included in the command. You can use the drop-down to construct example code for other apps.

You may also authenticate your REST API requests using basic HTTP authentication. For example, to retrieve an object you could set the URL using your Parse credentials in the following format:

```
https://myAppID:javascript-key=myJavaScriptKey@YOUR.PARSE-SERVER.HERE/parse/classes/GameScore/Ed1nuqPvcm
```

For JavaScript usage, the Parse Cloud supports [cross-origin resource sharing](https://en.wikipedia.org/wiki/Cross-Origin_Resource_Sharing), so that you can use these headers in conjunction with XMLHttpRequest.

[](https://docs.parseplatform.org/rest/guide/#response-format)Response Format
-----------------------------------------------------------------------------

The response format for all requests is a JSON object.

Whether a request succeeded is indicated by the HTTP status code. A 2xx status code indicates success, whereas a 4xx status code indicates failure. When a request fails, the response body is still JSON, but always contains the fields `code` and `error` which you can inspect to use for debugging. For example, trying to save an object with invalid keys will return the message:

```
{
  "code": 105,
  "error": "invalid field name: bl!ng"
}
```

[](https://docs.parseplatform.org/rest/guide/#calling-from-client-apps)Calling from Client Apps
-----------------------------------------------------------------------------------------------

You should not use the REST API Key in client apps (i.e. code you distribute to your customers). If the Parse SDK is available for your client platform, we recommend using our SDK instead of the REST API. If you must call the REST API directly from the client, you should use the corresponding client-side Parse key for that plaform (e.g. Client Key for iOS/Android, or .NET Key for Windows/Xamarin/Unity).

If there is no Parse SDK for your client platform, please use your app’s Client Key to call the REST API. Requests made with the Client Key, JavaScript Key, or Windows Key are restricted by client-side app settings that you configure in your Parse Dashboard app dashboard. These settings make your app more secure. For example, we recommend that all production apps turn off the “Client Push Enabled” setting to prevent push notifications from being sent from any device using the Client Key, JavaScript Key, or .NET Key, but not the REST API Key. Therefore, if you plan on registering installations to enable Push Notifications for your app, you should not distribute any app code with the REST API key embedded in it.

The JavaScript Key cannot be used to make requests directly against the REST API from JavaScript. The JavaScript Key is meant to be used with the Parse JavaScript SDK, which makes its posts through a Cross Origin-friendly format without HTTP headers.

[](https://docs.parseplatform.org/rest/guide/#objects)Objects
-------------------------------------------------------------

[](https://docs.parseplatform.org/rest/guide/#object-format)Object Format
-------------------------------------------------------------------------

Storing data through the Parse REST API is built around a JSON encoding of the object’s data. This data is schemaless, which means that you don’t need to specify ahead of time what keys exist on each object. You simply set whatever key-value pairs you want, and the backend will store it.

For example, let’s say you’re tracking high scores for a game. A single object could contain:

```
{
  "score": 1337,
  "playerName": "Sean Plott",
  "cheatMode": false
}
```

Keys must be alphanumeric strings. Values can be anything that can be JSON-encoded.

Each object has a class name that you can use to distinguish different sorts of data. For example, we could call the high score object a `GameScore`. We recommend that you NameYourClassesLikeThis and nameYourKeysLikeThis, just to keep your code looking pretty.

When you retrieve objects from Parse, some fields are automatically added: `createdAt`, `updatedAt`, and `objectId`. These field names are reserved, so you cannot set them yourself. The object above could look like this when retrieved:

```
{
  "score": 1337,
  "playerName": "Sean Plott",
  "cheatMode": false,
  "createdAt": "2022-01-01T12:23:45.678Z",
  "updatedAt": "2022-01-01T12:23:45.678Z",
  "objectId": "Ed1nuqPvcm"
}
```

`createdAt` and `updatedAt` are UTC timestamps stored in ISO 8601 format with millisecond precision: `YYYY-MM-DDTHH:MM:SS.MMMZ`. `objectId` is a string unique to this class that identifies this object.

In the REST API, the class-level operations operate on a resource based on just the class name. For example, if the class name is `GameScore`, the class URL is:

```
https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore
```

Users have a special class-level url:

```
https://YOUR.PARSE-SERVER.HERE/parse/users
```

The operations specific to a single object are available as a nested URL. For example, operations specific to the `GameScore` above with `objectId` equal to `Ed1nuqPvcm` would use the object URL:

```
https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore/Ed1nuqPvcm
```

[](https://docs.parseplatform.org/rest/guide/#creating-objects)Creating Objects
-------------------------------------------------------------------------------

To create a new object on Parse, send a POST request to the class URL containing the contents of the object. For example, to create the object described above:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"score":1337,"playerName":"Sean Plott","cheatMode":false}' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore
```

When the creation is successful, the HTTP response is a `201 Created` and the `Location` header contains the object URL for the new object:

```
Status: 201 Created
Location: https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore/Ed1nuqPvcm
```

The response body is a JSON object containing the `objectId` and the `createdAt` timestamp of the newly-created object:

```
{
  "createdAt": "2022-01-01T12:23:45.678Z",
  "objectId": "Ed1nuqPvcm"
}
```

[](https://docs.parseplatform.org/rest/guide/#retrieving-objects)Retrieving Objects
-----------------------------------------------------------------------------------

Once you’ve created an object, you can retrieve its contents by sending a GET request to the object URL returned in the location header. For example, to retrieve the object we created above:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore/Ed1nuqPvcm
```

The response body is a JSON object containing all the user-provided fields, plus the `createdAt`, `updatedAt`, and `objectId` fields:

```
{
  "score": 1337,
  "playerName": "Sean Plott",
  "cheatMode": false,
  "skills": [
    "pwnage",
    "flying"
  ],
  "createdAt": "2022-01-01T12:23:45.678Z",
  "updatedAt": "2022-01-01T12:23:45.678Z",
  "objectId": "Ed1nuqPvcm"
}
```

When retrieving objects that have pointers to children, **you can fetch child objects** by using the `include` option. For instance, to fetch the object pointed to by the “game” key:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'include=game' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore/Ed1nuqPvcm
```

When using a MongoDB replica set, you can use the `readPreference` option to choose from which replica the object will be retrieved. You can also use the `includeReadPreference` option to choose from which replica the included pointers will be retrieved. The possible values for both options are `PRIMARY` (default), `PRIMARY_PREFERRED`, `SECONDARY`, `SECONDARY_PREFERRED`, or `NEAREST`. If the `includeReadPreference` option is not set, the same replica chosen for `readPreference` will be also used for the includes.

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'include=game' \
  --data-urlencode 'readPreference=SECONDARY' \
  --data-urlencode 'includeReadPreference=SECONDARY_PREFERRED' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore/Ed1nuqPvcm
```

[](https://docs.parseplatform.org/rest/guide/#updating-objects)Updating Objects
-------------------------------------------------------------------------------

To change the data on an object that already exists, send a PUT request to the object URL. Any keys you don’t specify will remain unchanged, so you can update just a subset of the object’s data. For example, if we wanted to change the score field of our object:

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"score":73453}' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore/Ed1nuqPvcm
```

The response body is a JSON object containing just an `updatedAt` field with the timestamp of the update.

```
{
  "updatedAt": "2022-01-01T12:23:45.678Z"
}
```

### [](https://docs.parseplatform.org/rest/guide/#counters)Counters

To help with storing counter-type data, Parse provides the ability to atomically increment (or decrement) any number field. So, we can increment the score field like so:

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"score":{"__op":"Increment","amount":1}}' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore/Ed1nuqPvcm
```

To decrement the counter, use the `Increment` operator with a negative number:

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"score":{"__op":"Increment","amount":-1}}' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore/Ed1nuqPvcm
```

### [](https://docs.parseplatform.org/rest/guide/#arrays)Arrays

To help with storing array data, there are three operations that can be used to atomically change an array field:

*   `Add` appends the given array of objects to the end of an array field.
*   `AddUnique` adds only the given objects which aren’t already contained in an array field to that field. The position of the insert is not guaranteed.
*   `Remove` removes all instances of each given object from an array field.

Each method takes an array of objects to add or remove in the “objects” key. For example, we can add items to the set-like “skills” field like so:

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"skills":{"__op":"AddUnique","objects":["flying","kungfu"]}}' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore/Ed1nuqPvcm
```

### [](https://docs.parseplatform.org/rest/guide/#relations)Relations

In order to update `Relation` types, Parse provides special operators to atomically add and remove objects to a relation. So, we can add an object to a relation like so:

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"opponents":{"__op":"AddRelation","objects":[{"__type":"Pointer","className":"Player","objectId":"Vx4nudeWn"}]}}' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore/Ed1nuqPvcm
```

To remove an object from a relation, you can do:

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"opponents":{"__op":"RemoveRelation","objects":[{"__type":"Pointer","className":"Player","objectId":"Vx4nudeWn"}]}}' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore/Ed1nuqPvcm
```

[](https://docs.parseplatform.org/rest/guide/#deleting-objects)Deleting Objects
-------------------------------------------------------------------------------

To delete an object from the Parse Cloud, send a DELETE request to its object URL. For example:

```
curl -X DELETE \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore/Ed1nuqPvcm
```

You can delete a single field from an object by using the `Delete` operation:

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"opponents":{"__op":"Delete"}}' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore/Ed1nuqPvcm
```

[](https://docs.parseplatform.org/rest/guide/#batch-operations)Batch Operations
-------------------------------------------------------------------------------

To reduce the amount of time spent on network round trips, you can create, update, or delete using the batch endpoint. The batch size can be customized, the default batch size is 20.

Each command in a batch has `method`, `path`, and `body` parameters that specify the HTTP command that would normally be used for that command. The commands are run in the order they are given. For example, to create a couple of `GameScore` objects:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "requests": [
          {
            "method": "POST",
            "path": "/parse/classes/GameScore",
            "body": {
              "score": 1337,
              "playerName": "Sean Plott"
            }
          },
          {
            "method": "POST",
            "path": "/parse/classes/GameScore",
            "body": {
              "score": 1338,
              "playerName": "ZeroCool"
            }
          }
        ]
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/batch
```

The response from batch will be a list with the same number of elements as the input list. Each item in the list with be a dictionary with either the `success` or `error` field set. The value of `success` will be the normal response to the equivalent REST command:

```
{
  "success": {
    "createdAt": "2022-01-01T12:23:45.678Z",
    "objectId": "YAfSAWwXbL"
  }
}
```

The value of `error` will be an object with a numeric `code` and `error` string:

```
{
  "error": {
    "code": 101,
    "error": "object not found for delete"
  }
}
```

Other commands that work in a batch are `update` and `delete`.

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "requests": [
          {
            "method": "PUT",
            "path": "/parse/classes/GameScore/Ed1nuqPvcm",
            "body": {
              "score": 999999
            }
          },
          {
            "method": "DELETE",
            "path": "/parse/classes/GameScore/Cpl9lrueY5"
          }
        ]
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/batch
```

Note that N requests sent in a batch will still count toward your request limit as N requests.

[](https://docs.parseplatform.org/rest/guide/#data-types)Data Types
-------------------------------------------------------------------

So far we have only used values that can be encoded with standard JSON. The Parse mobile client libraries also support dates, geolocations, and relational data. In the REST API, these values are encoded as JSON hashes with the `__type` field set to indicate their type, so you can read or write these fields if you use the correct encoding. Overall, the following types are allowed for each field in your object:

*   String
*   Number
*   Boolean
*   Arrays
*   JSON Objects
*   DateTime
*   File
*   Pointer to another Parse Object
*   Relation to another Parse Class
*   Null

The `Date` type contains a field `iso` which contains a UTC timestamp stored in ISO 8601 format with millisecond precision: `YYYY-MM-DDTHH:MM:SS.MMMZ`.

```
{
  "__type": "Date",
  "iso": "2022-01-01T12:23:45.678Z"
}
```

Dates are useful in combination with the built-in `createdAt` and `updatedAt` fields. For example, to retrieve objects created since a particular time, just encode a Date in a comparison query:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={"createdAt":{"$gte":{"__type":"Date","iso":"2022-01-01T12:23:45.678Z"}}}' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore
```

The `Pointer` type is used when mobile code sets another Parse `Object` as the value of another object. It contains the `className` and `objectId` of the referred-to value.

```
{
  "__type": "Pointer",
  "className": "GameScore",
  "objectId": "Ed1nuqPvc"
}
```

Note that the built-in `User`, `Role`, and `Installation` classes are prefixed by an underscore. For example, pointers to user objects have a `className` of `_User`. Prefixing with an underscore is forbidden for developer-defined classes as it signifies the class is a special built-in.

The `Relation` type is used for many-to-many relations. It has a `className` that is the class name of the target objects.

```
{
  "__type": "Relation",
  "className": "GameScore"
}
```

When querying, `Relation` objects behave like arrays of Pointers. Any operation that is valid for arrays of pointers (other than `include`) works for `Relation` objects.

We do not recommend storing large pieces of binary data like images or documents on a Parse object. To store more, we recommend you use `File`. You may associate a [previously uploaded file](https://docs.parseplatform.org/rest/guide/#files) using the `File` type.

```
{
  "__type": "File",
  "name": "...profile.png"
}
```

When more data types are added, they will also be represented as hashes with a `__type` field set, so you may not use this field yourself on JSON objects. For more information about how Parse handles data, check out our documentation on [Data](https://docs.parseplatform.org/rest/guide/#data).

[](https://docs.parseplatform.org/rest/guide/#queries)Queries
-------------------------------------------------------------

[](https://docs.parseplatform.org/rest/guide/#basic-queries)Basic Queries
-------------------------------------------------------------------------

You can retrieve multiple objects at once by sending a GET request to the class URL. Without any URL parameters, this simply lists objects in the class:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore
```

The return value is a JSON object that contains a `results` field with a JSON array that lists the objects.

```
{
  "results": [
    {
      "playerName": "Jang Min Chul",
      "updatedAt": "2022-01-01T12:23:45.678Z",
      "cheatMode": false,
      "createdAt": "2022-01-01T12:23:45.678Z",
      "objectId": "A22v5zRAgd",
      "score": 80075
    },
    {
      "playerName": "Sean Plott",
      "updatedAt": "2022-01-01T12:23:45.678Z",
      "cheatMode": false,
      "createdAt": "2022-01-01T12:23:45.678Z",
      "objectId": "Ed1nuqPvcm",
      "score": 73453
    }
  ]
}
```

[](https://docs.parseplatform.org/rest/guide/#query-constraints)Query Constraints
---------------------------------------------------------------------------------

There are several ways to put constraints on the objects found, using the `where` URL parameter. The value of the `where` parameter should be encoded JSON. Thus, if you look at the actual URL requested, it would be JSON-encoded, then URL-encoded. The simplest use of the `where` parameter is constraining the value for keys. For example, if we wanted to retrieve Sean Plott’s scores that were not in cheat mode, we could do:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={"playerName":"Sean Plott","cheatMode":false}' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore
```

The values of the `where` parameter also support comparisons besides exact matching. Instead of an exact value, provide a hash with keys corresponding to the comparisons to do. The `where` parameter supports these options:

| Key | Operation |
| --- | --- |
| $lt | Less Than |
| $lte | Less Than Or Equal To |
| $gt | Greater Than |
| $gte | Greater Than Or Equal To |
| $ne | Not Equal To |
| $in | Contained In |
| $nin | Not Contained in |
| $exists | A value is set for the key |
| $select | This matches a value for a key in the result of a different query |
| $dontSelect | Requires that a key’s value not match a value for a key in the result of a different query |
| $all | Contains all of the given values |
| $regex | Requires that a key’s value match a regular expression |
| $text | Performs a full text search on indexed fields |

For example, to retrieve scores between 1000 and 3000, including the endpoints, we could issue:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={"score":{"$gte":1000,"$lte":3000}}' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore
```

To retrieve scores equal to an odd number below 10, we could issue:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={"score":{"$in":[1,3,5,7,9]}}' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore
```

To retrieve scores not by a given list of players we could issue:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={
   "playerName": {
     "$nin": [
       "Jonathan Walsh",
       "Dario Wunsch",
       "Shawn Simon"
     ]
   }
  }' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore
```

To retrieve documents with the score set, we could issue:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={"score":{"$exists":true}}' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore
```

To retrieve documents without the score set, we could issue:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={"score":{"$exists":false}}' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore
```

If you have a class containing sports teams and you store a user’s hometown in the user class, you can issue one query to find the list of users whose hometown teams have winning records. The query would look like:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={"hometown":{"$select":{"query":{"className":"Team","where":{"winPct":{"$gt":0.5}}},"key":"city"}}}' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/_User
```

In addition to `where`, there are several parameters you can use to configure what types of results are returned by the query.

| Parameter | Use |
| --- | --- |
| order | Specify a field to sort by |
| limit | Limit the number of objects returned by the query |
| skip | Use with limit to paginate through results |
| keys | Restrict the fields returned by the query |
| excludeKeys | Exclude specific fields from the returned query |
| include | Use on Pointer columns to return the full object |

You can use the `order` parameter to specify a field to sort by. Prefixing with a negative sign reverses the order. Thus, to retrieve scores in ascending order:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'order=score' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore
```

And to retrieve scores in descending order:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'order=-score' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore
```

You can sort by multiple fields by passing `order` a comma-separated list. To retrieve documents that are ordered by scores in ascending order and the names in descending order:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'order=score,-name' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore
```

You can use the `limit` and `skip` parameters for pagination.`limit` defaults to 100. In the old Parse hosted backend, the maximum limit was 1,000, but Parse Server removed that constraint. Thus, to retrieve 200 objects after skipping the first 400:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'limit=200' \
  --data-urlencode 'skip=400' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore
```

You can restrict the fields returned by passing `keys` or `excludeKeys` as an [array](https://docs.parseplatform.org/rest/guide/#arrays). To retrieve documents that contain only the `score` and `playerName` fields (and also special built-in fields such as `objectId`, `createdAt`, and `updatedAt`):

*   On Parse Server <5.0.0 pass a comma-delimited string, e.g. `"score,playerName"` instead of an array for `keys` and `excludeKeys`.

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'keys=score,playerName' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore
```

Or you may use `excludeKeys` to fetch everything except `playerName`:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'excludeKeys=playerName' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore/Ed1nuqPvcm
```

All of these parameters can be used in combination with each other. For example:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={
   "playerName": {
     "$nin": [
       "Jonathan Walsh",
       "Dario Wunsch",
       "Shawn Simon"
     ]
   }
  }' \
  --data-urlencode 'order=score,-name' \
  --data-urlencode 'limit=200' \
  --data-urlencode 'skip=400' \
  --data-urlencode 'keys=score,playerName' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore
```

[](https://docs.parseplatform.org/rest/guide/#queries-on-array-values)Queries on Array Values
---------------------------------------------------------------------------------------------

For keys with an array type, you can find objects where the key’s array value contains 2 by:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={"arrayKey":2}' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/RandomObject
```

You can also use the `$all` operator to find objects with an array field which contains each of the values 2, 3, and 4 by:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={"arrayKey":{"$all":[2,3,4]}}' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/RandomObject
```

[](https://docs.parseplatform.org/rest/guide/#queries-on-string-values)Queries on String Values
-----------------------------------------------------------------------------------------------

Use the `$regex` operator to restrict to string values that match a regular expression. Most regular expression queries in Parse are heavily throttled due to performance considerations. Use case sensitive, anchored queries where possible. Similar to a MySQL LIKE operator, anchored queries are indexed so they are efficient for large datasets. For example:

```
# Finds barbecue sauces that start with "Big Daddy"
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={"name":{"$regex":"^Big Daddy"}}' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/BarbecueSauce
```

The above example will match any `BarbecueSauce` objects where the value in the “name” String key starts with “Big Daddy”. For example, both “Big Daddy” and “Big Daddy’s” will match, but “big daddy” or “BBQ Sauce: Big Daddy’s” will not.

Queries that have regular expression constraints are very expensive, especially for classes with over 100,000 records. Parse restricts how many such operations can be run on a particular app at any given time.

*   Starting with Parse-Server 2.5.0

For efficient search capabilities use the `$text` operator. By creating indexes on one or more columns your strings are turned into tokens for full text search functionality.

The format `{"$text": {"$search": {parameters}}}`

| Parameter | Use |
| --- | --- |
| $term | Specify a field to search (Required) |
| $language | Determines the list of stop words and the rules for tokenizer. |
| $caseSensitive | Enable or disable case sensitive search. |
| $diacriticSensitive | Enable or disable diacritic sensitive search |

Please refer to your database documentation on Full Text Search to setup your indexes, weights and limitations.

[Mongo 3.2 Full Text Search](https://docs.mongodb.com/v3.2/text-search/)

[Mongo 3.4 Full Text Search](https://docs.mongodb.com/manual/reference/operator/query/text/)

[Postgres 9.5 Full Text Search](https://www.postgresql.org/docs/9.5/static/textsearch.html)

Note: Postgres doesn’t support `$caseSensitive` for Full Text Search, please use `$regex` above or create a lowercase column in your DB. Postgres supports `$diacriticSensitive: true` by default but `$diacriticSensitive: false` is not supported. To use false automatically, please install Postgres Unaccent Extension and update your text search configuration.

```
# Finds strings that contains "Daddy"
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={"name":{"$text":{"$search":{"$term":"Daddy"}}}}' \
  https://api.parse.com/1/classes/BarbecueSauce
```

`$text` allows for sorting by `$score`. The text score signifies how well the string matched the search term(s) based on weights.

```
# Finds strings that contains "Daddy" ordered by relevance
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={"name":{"$text":{"$search":{"$term":"Daddy"}}}}' \
  --data-urlencode 'order="$score"' \
  --data-urlencode 'key="$score"' \
  https://api.parse.com/1/classes/BarbecueSauce
```

Note: Both keys and order are required to sort by `$score`. You have to manually set weights on Postgres to use `$score`.

[](https://docs.parseplatform.org/rest/guide/#relational-queries)Relational Queries
-----------------------------------------------------------------------------------

There are several ways to issue queries for relational data. If you want to retrieve objects where a field matches a particular object, you can use a `where` clause with a `Pointer` encoded with `__type` just like you would use other data types. For example, if each `Comment` has a `Post` object in its `post` field, you can fetch comments for a particular `Post`:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={"post":{"__type":"Pointer","className":"Post","objectId":"8TOXdXf3tz"}}' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/Comment
```

If you want to retrieve objects where a field contains an object that matches another query, you can use the `$inQuery` operator. For example, imagine you have Post class and a Comment class, where each Comment has a pointer to its parent Post. You can find comments on posts with images by doing:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={"post":{"$inQuery":{"where":{"image":{"$exists":true}},"className":"Post"}}}' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/Comment
```

If you want to retrieve objects where a field contains an object that does not match another query, you can use the `$notInQuery` operator. Imagine you have Post class and a Comment class, where each Comment has a pointer to its parent Post. You can find comments on posts without images by doing:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={"post":{"$notInQuery":{"where":{"image":{"$exists":true}},"className":"Post"}}}' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/Comment
```

If you want to retrieve objects that are members of `Relation` field of a parent object, you can use the `$relatedTo` operator. Imagine you have a Post class and User class, where each Post can be liked by many users. If the Users that liked a Post were stored in a `Relation` on the post under the key “likes”, you can find the users that liked a particular post by:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={"$relatedTo":{"object":{"__type":"Pointer","className":"Post","objectId":"8TOXdXf3tz"},"key":"likes"}}' \
  https://YOUR.PARSE-SERVER.HERE/parse/users
```

In some situations, you want to return multiple types of related objects in one query. You can do this by passing the field to include in the `include` parameter. For example, let’s say you are retrieving the last ten comments, and you want to retrieve their related posts at the same time:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'order=-createdAt' \
  --data-urlencode 'limit=10' \
  --data-urlencode 'include=post' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/Comment
```

Instead of being represented as a `Pointer`, the `post` field is now expanded into the whole object. `__type` is set to `Object` and `className` is provided as well. For example, a `Pointer` to a `Post` could be represented as:

```
{
  "__type": "Pointer",
  "className": "Post",
  "objectId": "8TOXdXf3tz"
}
```

When the query is issued with an `include` parameter for the key holding this pointer, the pointer will be expanded to:

```
{
  "__type": "Object",
  "className": "Post",
  "objectId": "8TOXdXf3tz",
  "createdAt": "2022-01-01T12:23:45.678Z",
  "updatedAt": "2022-01-01T12:23:45.678Z",
  "otherFields": "willAlsoBeIncluded"
}
```

You can also do multi level includes using dot notation. If you wanted to include the post for a comment and the post’s author as well you can do:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'order=-createdAt' \
  --data-urlencode 'limit=10' \
  --data-urlencode 'include=post.author' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/Comment
```

You can issue a query with multiple fields included by passing a comma-separated list of keys as the `include` parameter.

[](https://docs.parseplatform.org/rest/guide/#counting-objects)Counting Objects
-------------------------------------------------------------------------------

Note: In the old Parse hosted backend, count queries were rate limited to a maximum of 160 requests per minute. They also returned inaccurate results for classes with more than 1,000 objects. But, Parse Server has removed both constraints and can count objects well above 1,000.

If you are limiting your query, or if there are a very large number of results, and you want to know how many total results there are without returning them all, you can use the `count` parameter. For example, if you only care about the number of games played by a particular player:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={"playerName":"Jonathan Walsh"}' \
  --data-urlencode 'count=1' \
  --data-urlencode 'limit=0' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/GameScore
```

Since this requests a count as well as limiting to zero results, there will be a count but no results in the response.

```
{
  "results": [],
  "count": 1337
}
```

With a nonzero limit, that request would return results as well as the count.

[](https://docs.parseplatform.org/rest/guide/#compound-queries)Compound Queries
-------------------------------------------------------------------------------

If you want to find objects that match one of several queries, you can use `$or` operator, with a JSONArray as its value. For instance, if you want to find players with either have a lot of wins or a few wins, you can do:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={"$or":[{"wins":{"$gt":150}},{"wins":{"$lt":5}}]}' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/Player
```

Any other constraints on the query are also applied to the object returned, so you can add other constraints to queries with `$or`.

Note that we do not, however, support GeoPoint or non-filtering constraints (e.g. nearSphere, within, limit, skip, sort, include) in the subqueries of the compound query.

[](https://docs.parseplatform.org/rest/guide/#distinct-queries)Distinct Queries
-------------------------------------------------------------------------------

*   Starting with Parse-Server 2.7.0 (requires masterKey)

Finds unique values for a specified field.

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'distinct=score' \
  https://YOUR.PARSE-SERVER.HERE/parse/aggregate/GameScore
```

Can be used with `where` parameter for constraining the value for keys.

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={"playerName":"Sean Plott"},distinct=score' \
  https://YOUR.PARSE-SERVER.HERE/parse/aggregate/GameScore
```

[](https://docs.parseplatform.org/rest/guide/#aggregate-queries)Aggregate Queries
---------------------------------------------------------------------------------

*   Starting with Parse-Server 2.7.0 (requires masterKey)

You can find objects using aggregate functions. This will compute result(s) for a set of input values.

For a list of available operators please refer to Mongo Aggregate Documentation.

[Mongo 3.2 Aggregate Operators](https://docs.mongodb.com/v3.2/reference/operator/aggregation/)

[Mongo 3.4 Aggregate Operators](https://docs.mongodb.com/manual/reference/operator/aggregation/#aggregation-expression-operators)

You can group the objects and apply an accumulator operator such as `$sum`, `$avg`, `$max`, `$min`. `group` is similar to `distinct`.

Note: `_id` does not exist in parse-server. Please replace with `objectId`.

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'group={"objectId":null,"total":{"$sum":"$score"}}' \
  https://YOUR.PARSE-SERVER.HERE/parse/aggregate/Player
```

You can add or remove existing fields with `project` parameter. `project` is similar to `keys`.

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'project={"score":1}' \
  https://YOUR.PARSE-SERVER.HERE/parse/aggregate/Player
```

You can filter out objects with `match` parameter. `match` is similar to `$eq`.

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'match={"score":{"$gt":15}}' \
  https://YOUR.PARSE-SERVER.HERE/parse/aggregate/Player
```

You can also constraint by `limit`, `skip`, `sort`.

[](https://docs.parseplatform.org/rest/guide/#read-preference)Read Preference
-----------------------------------------------------------------------------

When using a MongoDB replica set, you can use the `readPreference` option to choose from which replica the objects will be retrieved. You can also use the `includeReadPreference` option to choose from which replica the included pointers will be retrieved and the `subqueryReadPreference` option to choose in which replica the subqueries will run. The possible values these options are `PRIMARY` (default), `PRIMARY_PREFERRED`, `SECONDARY`, `SECONDARY_PREFERRED`, or `NEAREST`. If the `includeReadPreference` option is not set, the same replica chosen for `readPreference` will be also used for the includes. The same rule applies for the `subqueryReadPreference` option.

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={"post":{"$inQuery":{"where":{"image":{"$exists":true}},"className":"Post"}}}' \
  --data-urlencode 'include=post' \
  --data-urlencode 'readPreference=SECONDARY' \
  --data-urlencode 'includeReadPreference=SECONDARY_PREFERRED' \
  --data-urlencode 'subqueryReadPreference=NEAREST' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/Comment
```

[](https://docs.parseplatform.org/rest/guide/#users)Users
---------------------------------------------------------

Many apps have a unified login that works across the mobile app and other systems. Accessing user accounts through the REST API lets you build this functionality on top of Parse.

In general, users have the same features as other objects, such as the flexible schema. The differences are that user objects must have a username and password, the password is automatically encrypted and stored securely, and Parse enforces the uniqueness of the `username` and `email` fields.

[](https://docs.parseplatform.org/rest/guide/#signing-up)Signing Up
-------------------------------------------------------------------

Signing up a new user differs from creating a generic object in that the `username` and `password` fields are required. The password field is handled differently than the others; it is encrypted with bcrypt when stored in the Parse Cloud and never returned to any client request.

You can ask Parse to verify user email addresses in your application settings page. With this setting enabled, all new user registrations with an `email` field will generate an email confirmation at that address. You can check whether the user has verified their `email` with the `emailVerified` field.

To sign up a new user, send a POST request to the users root. You may add any additional fields. For example, to create a user with a specific phone number:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "X-Parse-Revocable-Session: 1" \
  -H "Content-Type: application/json" \
  -d '{"username":"cooldude6","password":"p_n7!-e8","phone":"415-392-0202"}' \
  https://YOUR.PARSE-SERVER.HERE/parse/users
```

When the creation is successful, the HTTP response is a `201 Created` and the `Location` header contains the URL for the new user:

```
Status: 201 Created
Location: https://YOUR.PARSE-SERVER.HERE/parse/users/g7y9tkhB7O
```

The response body is a JSON object containing the `objectId`, the `createdAt` timestamp of the newly-created object, and the `sessionToken` which can be used to authenticate subsequent requests as this user:

```
{
  "createdAt": "2022-01-01T12:23:45.678Z",
  "objectId": "g7y9tkhB7O",
  "sessionToken": "r:pnktnjyb996sj4p156gjtp4im"
}
```

[](https://docs.parseplatform.org/rest/guide/#logging-in)Logging In
-------------------------------------------------------------------

After you allow users to sign up, you need to let them log in to their account with a username and password in the future. To do this, send a POST request to the `/parse/login` endpoint with `username` and `password` as parameters in the body:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "X-Parse-Revocable-Session: 1" \
  -H "Content-Type: application/json" \
  -d '{"username":"cooldude6","password":"p_n7!-e8"}' \
  https://YOUR.PARSE-SERVER.HERE/parse/login
```

The response body is a JSON object containing all the user-provided fields except `password`. It also contains the `createdAt`, `updatedAt`, `objectId`, and `sessionToken` fields:

```
{
  "username": "cooldude6",
  "phone": "415-392-0202",
  "createdAt": "2022-01-01T12:23:45.678Z",
  "updatedAt": "2022-01-01T12:23:45.678Z",
  "objectId": "g7y9tkhB7O",
  "sessionToken": "r:pnktnjyb996sj4p156gjtp4im"
}
```

[](https://docs.parseplatform.org/rest/guide/#verifying-emails)Verifying Emails
-------------------------------------------------------------------------------

Enabling email verification in an application’s settings allows the application to reserve part of its experience for users with confirmed email addresses. Email verification adds the `emailVerified` field to the `User` object. When a `User`’s `email` is set or modified, `emailVerified` is set to `false`. Parse then emails the user a link which will set `emailVerified` to `true`.

There are three `emailVerified` states to consider:

1.   `true` - the user confirmed his or her email address by clicking on the link Parse emailed them. `Users` can never have a `true` value when the user account is first created.
2.   `false` - at the time the `User` object was last refreshed, the user had not confirmed his or her email address. If `emailVerified` is `false`, consider refreshing the `User` object.
3.   _missing_ - the `User` was created when email verification was off or the `User` does not have an `email`.

You can request a verification email to be sent by sending a POST request to `/parse/verificationEmailRequest` with `email` in the body of the request:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"email":"email@example.com"}' \
  https://YOUR.PARSE-SERVER.HERE/parse/verificationEmailRequest
```

Note that a verification email will not be sent if the email has already been successfully verified.

[](https://docs.parseplatform.org/rest/guide/#requesting-a-password-reset)Requesting A Password Reset
-----------------------------------------------------------------------------------------------------

You can initiate password resets for users who have emails associated with their account. To do this, send a POST request to `/parse/requestPasswordReset` endpoint with `email` in the body of the request:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"email":"coolguy@iloveapps.com"}' \
  https://YOUR.PARSE-SERVER.HERE/parse/requestPasswordReset
```

If successful, the response body is an empty JSON object.

You can use the [`beforePasswordResetRequest`](https://docs.parseplatform.org/cloudcode/guide/#beforepasswordresetrequest) Cloud Code trigger to add custom validation logic before the password reset email is sent.

[](https://docs.parseplatform.org/rest/guide/#retrieving-users)Retrieving Users
-------------------------------------------------------------------------------

You can also retrieve the contents of a user object by sending a GET request to the URL returned in the location header when it was created. For example, to retrieve the user created above:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  https://YOUR.PARSE-SERVER.HERE/parse/users/g7y9tkhB7O
```

The response body is a JSON object containing all the user-provided fields except `password`. It also contains the `createdAt`, `updatedAt`, and `objectId` fields:

```
{
  "username": "cooldude6",
  "phone": "415-392-0202",
  "createdAt": "2022-01-01T12:23:45.678Z",
  "updatedAt": "2022-01-01T12:23:45.678Z",
  "objectId": "g7y9tkhB7O"
}
```

[](https://docs.parseplatform.org/rest/guide/#validating-session-tokens--retrieving-current-user)Validating Session Tokens / Retrieving Current User
----------------------------------------------------------------------------------------------------------------------------------------------------

With a valid session token, you can send a GET request to the `/parse/users/me` endpoint to retrieve the user associated with that session token:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "X-Parse-Session-Token: r:pnktnjyb996sj4p156gjtp4im" \
  https://YOUR.PARSE-SERVER.HERE/parse/users/me
```

The response matches the JSON object above for retrieving users. If the session token is not valid, an error object is returned:

```
{
  "code": 209,
  "error": "invalid session token"
}
```

[](https://docs.parseplatform.org/rest/guide/#updating-users)Updating Users
---------------------------------------------------------------------------

In normal usage, nobody except the user is allowed to modify their own data. To authenticate themselves, the user must add a `X-Parse-Session-Token` header to the request with the session token provided by the signup or login method.

To change the data on a user that already exists, send a PUT request to the user URL. Any keys you don’t specify will remain unchanged, so you can update just a subset of the user’s data. `username` and `password` may be changed, but the new username must not already be in use.

For example, if we wanted to change the phone number for `cooldude6`:

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "X-Parse-Session-Token: r:pnktnjyb996sj4p156gjtp4im" \
  -H "Content-Type: application/json" \
  -d '{"phone":"415-369-6201"}' \
  https://YOUR.PARSE-SERVER.HERE/parse/users/g7y9tkhB7O
```

The response body is a JSON object containing just an `updatedAt` field with the timestamp of the update.

```
{
  "updatedAt": "2022-01-01T12:23:45.678Z"
}
```

[](https://docs.parseplatform.org/rest/guide/#querying)Querying
---------------------------------------------------------------

You can retrieve multiple users at once by sending a GET request to the root users URL. Without any URL parameters, this simply lists users:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  https://YOUR.PARSE-SERVER.HERE/parse/users
```

The return value is a JSON object that contains a `results` field with a JSON array that lists the objects.

```
{
  "results": [
    {
      "username": "bigglesworth",
      "phone": "650-253-0000",
      "createdAt": "2022-01-01T12:23:45.678Z",
      "updatedAt": "2022-01-01T12:23:45.678Z",
      "objectId": "3KmCvT7Zsb"
    },
    {
      "username": "cooldude6",
      "phone": "415-369-6201",
      "createdAt": "2022-01-01T12:23:45.678Z",
      "updatedAt": "2022-01-01T12:23:45.678Z",
      "objectId": "g7y9tkhB7O"
    }
  ]
}
```

All of the options for queries that work for regular objects also work for user objects, so check the section on [Querying Objects](https://docs.parseplatform.org/rest/guide/#basic-queries) for more details.

[](https://docs.parseplatform.org/rest/guide/#deleting-users)Deleting Users
---------------------------------------------------------------------------

To delete a user from the Parse Cloud, send a DELETE request to its URL. You must provide the `X-Parse-Session-Token` header to authenticate. For example:

```
curl -X DELETE \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "X-Parse-Session-Token: r:pnktnjyb996sj4p156gjtp4im" \
  https://YOUR.PARSE-SERVER.HERE/parse/users/g7y9tkhB7O
```

[](https://docs.parseplatform.org/rest/guide/#linking-users)Linking Users
-------------------------------------------------------------------------

Parse allows you to link your users with services like Twitter and Facebook, enabling your users to sign up or log into your application using their existing identities. This is accomplished through the sign-up and update REST endpoints by providing authentication data for the service you wish to link to a user in the `authData` field. Once your user is associated with a service, the `authData` for the service will be stored with the user and is retrievable by logging in.

`authData` is a JSON object with keys for each linked service containing the data below. In each case, you are responsible for completing the authentication flow (e.g. OAuth 1.0a) to obtain the information the the service requires for linking.

### [](https://docs.parseplatform.org/rest/guide/#facebook-authdata)Facebook `authData`

```
{
  "facebook": {
    "id": "user's Facebook id number as a string",
    "access_token": "an authorized Facebook access token for the user",
    "expiration_date": "token expiration date of the format: yyyy-MM-dd'T'HH:mm:ss.SSS'Z'"
  }
}
```

Learn more about [Facebook login](https://developers.facebook.com/docs/authentication/).

### [](https://docs.parseplatform.org/rest/guide/#twitter-authdata)Twitter `authData`

```
{
  "twitter": {
    "id": "user's Twitter id number as a string",
    "screen_name": "user's Twitter screen name",
    "consumer_key": "your application's consumer key",
    "consumer_secret": "your application's consumer secret",
    "auth_token": "an authorized Twitter token for the user with your application",
    "auth_token_secret": "the secret associated with the auth_token"
  }
}
```

Learn more about [Twitter login](https://dev.twitter.com/docs/auth/implementing-sign-twitter).

### [](https://docs.parseplatform.org/rest/guide/#anonymous-user-authdata)Anonymous user `authData`

```
{
  "anonymous": {
    "id": "random UUID with lowercase hexadecimal digits"
  }
}
```

### [](https://docs.parseplatform.org/rest/guide/#signing-up-and-logging-in)Signing Up and Logging In

Signing a user up with a linked service and logging them in with that service uses the same POST request, in which the `authData` for the user is specified. For example, to sign up or log in with a user’s Twitter account:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "X-Parse-Revocable-Session: 1" \
  -H "Content-Type: application/json" \
  -d '{
        "authData": {
          "twitter": {
            "id": "12345678",
            "screen_name": "ParseIt",
            "consumer_key": "SaMpLeId3X7eLjjLgWEw",
            "consumer_secret": "SaMpLew55QbMR0vTdtOACfPXa5UdO2THX1JrxZ9s3c",
            "auth_token": "12345678-SaMpLeTuo3m2avZxh5cjJmIrAfx4ZYyamdofM7IjU",
            "auth_token_secret": "SaMpLeEb13SpRzQ4DAIzutEkCE2LBIm2ZQDsP3WUU"
          }
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/users
```

Parse then verifies that the provided `authData` is valid and checks to see if a user is already associated with this data. If so, it returns a status code of `200 OK` and the details (including a `sessionToken` for the user):

```
Status: 200 OK
Location: https://YOUR.PARSE-SERVER.HERE/parse/users/uMz0YZeAqc
```

With a response body like:

```
{
  "username": "Parse",
  "createdAt": "2022-01-01T12:23:45.678Z",
  "updatedAt": "2022-01-01T12:23:45.678Z",
  "objectId": "uMz0YZeAqc",
  "sessionToken": "r:samplei3l83eerhnln0ecxgy5",
  "authData": {
    "twitter": {
      "id": "12345678",
      "screen_name": "ParseIt",
      "consumer_key": "SaMpLeId3X7eLjjLgWEw",
      "consumer_secret": "SaMpLew55QbMR0vTdtOACfPXa5UdO2THX1JrxZ9s3c",
      "auth_token": "12345678-SaMpLeTuo3m2avZxh5cjJmIrAfx4ZYyamdofM7IjU",
      "auth_token_secret": "SaMpLeEb13SpRzQ4DAIzutEkCE2LBIm2ZQDsP3WUU"
    }
  }
}
```

If the user has never been linked with this account, you will instead receive a status code of `201 Created`, indicating that a new user was created:

```
Status: 201 Created
Location: https://YOUR.PARSE-SERVER.HERE/parse/users/uMz0YZeAqc
```

The body of the response will contain the `objectId`, `createdAt`, `sessionToken`, and an automatically-generated unique `username`. For example:

```
{
  "username": "iwz8sna7sug28v4eyu7t89fij",
  "createdAt": "2022-01-01T12:23:45.678Z",
  "objectId": "uMz0YZeAqc",
  "sessionToken": "r:samplei3l83eerhnln0ecxgy5"
}
```

### [](https://docs.parseplatform.org/rest/guide/#linking)Linking

Linking an existing user with a service like Facebook or Twitter uses a PUT request to associate `authData` with the user. For example, linking a user with a Facebook account would use a request like this:

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "X-Parse-Session-Token: r:samplei3l83eerhnln0ecxgy5" \
  -H "Content-Type: application/json" \
  -d '{
        "authData": {
          "facebook": {
            "id": "123456789",
            "access_token": "SaMpLeAAibS7Q55FSzcERWIEmzn6rosftAr7pmDME10008bWgyZAmv7mziwfacNOhWkgxDaBf8a2a2FCc9Hbk9wAsqLYZBLR995wxBvSGNoTrEaL",
            "expiration_date": "2022-01-01T12:23:45.678Z"
          }
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/users/uMz0YZeAqc
```

After linking your user to a service, you can authenticate them using matching `authData`.

### [](https://docs.parseplatform.org/rest/guide/#unlinking)Unlinking

Unlinking an existing user with a service also uses a PUT request to clear `authData` from the user by setting the `authData` for the service to `null`. For example, unlinking a user with a Facebook account would use a request like this:

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "X-Parse-Session-Token: r:samplei3l83eerhnln0ecxgy5" \
  -H "Content-Type: application/json" \
  -d '{
        "authData": {
          "facebook": null
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/users/uMz0YZeAqc
```

[](https://docs.parseplatform.org/rest/guide/#user-security)`User` Security
---------------------------------------------------------------------------

When you access Parse via the REST API key, access can be restricted by ACL just like in the iOS and Android SDKs. You can still read and modify acls via the REST API, just by accessing the `"ACL"` key of an object.

The ACL is formatted as a JSON object where the keys are either object ids or the special key `"*"` to indicate public access permissions. The values of the ACL are “permission objects”, JSON objects whose keys are the permission names and whose values are always `true`.

For example, if you want the user with id `"3KmCvT7Zsb"` to have read and write access to an object, plus the object should be publicly readable, that corresponds to an ACL of:

```
"ACL": {
  "3KmCvT7Zsb": {
    "read": true,
    "write": true
  },
  "*": {
    "read": true
  }
}
```

If you want to access your data ignoring all ACLs, you can use the master key provided on the Dashboard. Instead of the `X-Parse-REST-API-Key` header, set the `X-Parse-Master-Key` header. For backward compatibility, you can also do master-level authentication using HTTP Basic Auth, passing the application id as the username and the master key as the password. For security, the master key should not be distributed to end users, but if you are running code in a trusted environment, feel free to use the master key for authentication.

[](https://docs.parseplatform.org/rest/guide/#user-impersonation)User Impersonation
-----------------------------------------------------------------------------------

An application may allow a user to take action on behalf of another user, without having access to the other user’s login credentials. The Parse REST API provides the `/loginAs` endpoint which takes a `userId` parameter, that is the `objectId` of the user for which a session should be created. A session that has been created this way can be identified by its `createdWith` property:

```
"createdWith": {
  "action": "login",
  "authProvider": "masterkey"
}
```

Calling the endpoint requires the master key and it returns the same response format as the `/login` endpoint.

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "X-Parse-Revocable-Session: 1" \
  -G \
  --data-urlencode 'userId=abc123' \
  https://YOUR.PARSE-SERVER.HERE/parse/loginAs
```

Calling this endpoint does not invoke [session triggers](https://docs.parseplatform.org/cloudcode/guide/#session-triggers) such as `beforeLogin` and `afterLogin`. This action will always succeed if the supplied user exists in the database, regardless of whether the user is currently locked out.

[](https://docs.parseplatform.org/rest/guide/#sessions)Sessions
---------------------------------------------------------------

Sessions represent an instance of a user logged into a device. Sessions are automatically created when users log in or sign up. They are automatically deleted when users log out. There is one distinct `Session` object for each user-installation pair; if a user issues a login request from a device they’re already logged into, that user’s previous `Session` object for that Installation is automatically deleted. `Session` objects are stored on Parse in the Session class, and you can view them on the Parse Dashboard Data Browser. We provide a set of APIs to manage `Session` objects in your app.

A `Session` is a subclass of a Parse `Object`, so you can query, update, and delete sessions in the same way that you manipulate normal objects on Parse. Because the Parse Cloud automatically creates sessions when you log in or sign up users, you should not manually create `Session` objects unless you are building an IoT app (e.g. Arduino or Embedded C). Deleting a `Session` will log the user out of the device that is currently using this session’s token.

Unlike other Parse objects, the `Session` class does not have Cloud Code triggers. So you cannot register a `beforeSave` or `afterSave` handler for the Session class.

[](https://docs.parseplatform.org/rest/guide/#session-properties)`Session` Properties
-------------------------------------------------------------------------------------

The `Session` object has these special fields:

*   `sessionToken` (readonly): String token for authentication on Parse API requests. In the response of `Session` queries, only your current `Session` object will contain a session token.
*   `user`: (readonly) Pointer to the `User` object that this session is for.
*   `createdWith` (readonly): Information about how this session was created (e.g. `{ "action": "login", "authProvider": "password"}`). 
    *   `action` could have values: `login`, `signup`, `create`, or `upgrade`. The `create` action is when the developer manually creates the session by saving a `Session` object. The `upgrade` action is when the user is upgraded to revocable session from a legacy session token.
    *   `authProvider` could have values: `password`, `anonymous`, `facebook`, or `twitter`.

*   `restricted` (readonly): Boolean for whether this session is restricted. 
    *   Restricted sessions do not have write permissions on `User`, `Session`, and `Role` classes on Parse. Restricted sessions also cannot read unrestricted sessions.
    *   All sessions that the Parse Cloud automatically creates during user login/signup will be unrestricted. All sessions that the developer manually creates by saving a new `Session` object from the client (only needed for IoT apps) will be restricted.

*   `expiresAt` (readonly): Approximate UTC date when this `Session` object will be automatically deleted. You can configure session expiration settings (either 1-year inactivity expiration or no expiration) in your app’s Parse Dashboard settings page.
*   `installationId` (can be set only once): String referring to the `Installation` where the session is logged in from. For the REST API, you can set this by passing the `X-Parse-Installation-Id` header on login and signup requests. All special fields except `installationId` can only be set automatically by the Parse Cloud. You can add custom fields onto `Session` objects, but please keep in mind that any logged-in device (with session token) can read other sessions that belong to the same user (unless you disable Class-Level Permissions, see below).

[](https://docs.parseplatform.org/rest/guide/#handling-invalid-session-token-error)Handling Invalid Session Token Error
-----------------------------------------------------------------------------------------------------------------------

Apps created before March 25, 2015 use legacy session tokens until you migrate them to use the new revocable sessions. On API requests with legacy tokens, if the token is invalid (e.g. User object was deleted), then the request is executed as a non-logged in user and no error was returned. On API requests with revocable session tokens, an invalid session token will always fail with the “invalid session token” error. This new behavior lets you know when you need to ask the user to log in again.

With revocable sessions, your current session token could become invalid if its corresponding `Session` object is deleted from the Parse Cloud. This could happen if you implement a Session Manager UI that lets users log out of other devices, or if you manually delete the session via Cloud Code, REST API, or Data Browser. Sessions could also be deleted due to automatic expiration (if configured in app settings). When a device’s session token no longer corresponds to a `Session` object on the Parse Cloud, all API requests from that device will fail with “Error 209: invalid session token”.

[](https://docs.parseplatform.org/rest/guide/#creating-sessions)Creating Sessions
---------------------------------------------------------------------------------

For mobile apps and websites, you should not create `Session` objects manually. Instead, you should call `GET /parse/login` and `POST /parse/users` (signup), which will automatically generate a `Session` object in the Parse Cloud. The session token for this automatically-created session will be sent back on the login and signup response. Same for Facebook/Twitter login and signup requests.

[](https://docs.parseplatform.org/rest/guide/#retrieving-sessions)Retrieving Sessions
-------------------------------------------------------------------------------------

If you have the session’s objectId, you fetch the `Session` object as long as it belongs to the same user as your current session:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "X-Parse-Session-Token: r:pnktnjyb996sj4p156gjtp4im" \
  https://YOUR.PARSE-SERVER.HERE/parse/sessions/Axy98kq1B09
```

If you only have the session’s token (from previous login or session create), you can validate and fetch the corresponding session by:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "X-Parse-Session-Token: r:pnktnjyb996sj4p156gjtp4im" \
  https://YOUR.PARSE-SERVER.HERE/parse/sessions/me
```

[](https://docs.parseplatform.org/rest/guide/#updating-sessions)Updating Sessions
---------------------------------------------------------------------------------

Updating a session is analogous to updating a Parse object.

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "X-Parse-Session-Token: r:pnktnjyb996sj4p156gjtp4im" \
  -H "Content-Type: application/json" \
  -d '{"customField":"value"}' \
  https://YOUR.PARSE-SERVER.HERE/parse/sessions/Axy98kq1B09
```

[](https://docs.parseplatform.org/rest/guide/#querying-sessions)Querying Sessions
---------------------------------------------------------------------------------

Querying for `Session` objects will only return objects belonging to the same user as your current session (due to the Session ACL). You can also add a where clause to your query, just like normal Parse objects.

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "X-Parse-Session-Token: r:pnktnjyb996sj4p156gjtp4im" \
  https://YOUR.PARSE-SERVER.HERE/parse/sessions
```

[](https://docs.parseplatform.org/rest/guide/#deleting-sessions)Deleting Sessions
---------------------------------------------------------------------------------

Deleting the Session object will revoke its session token and cause the user to be logged out on the device that’s currently using this session token. When you have the session token, then you can delete its `Session` object by calling the logout endpoint:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "X-Parse-Session-Token: r:pnktnjyb996sj4p156gjtp4im" \
  https://YOUR.PARSE-SERVER.HERE/parse/logout
```

If you want to delete another `Session` object for your user, and you have its `objectId`, you can delete it (but not log yourself out) by:

```
curl -X DELETE \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "X-Parse-Session-Token: r:pnktnjyb996sj4p156gjtp4im" \
  https://YOUR.PARSE-SERVER.HERE/parse/sessions/Axy98kq1B09
```

`X-Parse-Session-Token` authenticates the request as the user that also owns session `Axy98kq1B09`, which may have a different session token. You can only delete other sessions that belong to the same user.

[](https://docs.parseplatform.org/rest/guide/#pairing-session-with-installation)Pairing Session with Installation
-----------------------------------------------------------------------------------------------------------------

For normal user login with the `/parse/login` endpoint, the Parse Cloud will set the automatically-created `Session` object’s `installationId` to the `X-Parse-Installation-Id` header passed on the login or signup request. Therefore, for these scenarios, you don’t need to manually associate the `Session` object with an installation.

The following API is most useful for IoT apps (e.g. Arduino or Embedded C). During IoT device provisioning, the phone typically does not know the `installationId` of the IoT device. The provisioning process typically goes like this:

1.   Phone creates a restricted session (with blank `installationId`) for the device.
2.   IoT device acts as a Wi-Fi software access point. Phone passes this newly-created session’s token, along with the Wi-Fi password, to the IoT device.
3.   IoT device connects to Internet via Wi-Fi, saves its `Installation` object.
4.   IoT device calls the following endpoint to associate the its `installationId` with its session. This endpoint only works with session tokens from restricted sessions. Please note that REST API calls from an IoT device should use the Client Key, not the REST API Key.

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Client-Key: ${CLIENT_KEY}" \
  -H "X-Parse-Session-Token: r:aVrtljyb7E8xKo9256gfvp4n2" \
  -H "X-Parse-Installation-Id: 2d3777a5-f5fc-4caf-80be-73c766235afb" \
  -H "Content-Type: application/json" \
  -d '{}' \
  https://YOUR.PARSE-SERVER.HERE/parse/sessions/me
```

[](https://docs.parseplatform.org/rest/guide/#session-security)Session Security
-------------------------------------------------------------------------------

`Session` objects can only be accessed by the user specified in the user field. All `Session` objects have an ACL that is read and write by that user only. You cannot change this ACL. This means querying for sessions will only return objects that match the current logged-in user.

When you log in a user via `/parse/login`, Parse will automatically create a new unrestricted `Session` object in the Parse Cloud. Same for signups and Facebook/Twitter logins.

Session objects manually created from `POST /parse/sessions` are always restricted. You cannot manually create an unrestricted sessions using the object creation API.

Restricted sessions are prohibited from creating, modifying, or deleting any data in the `User`, `Session`, and `Role` classes. Restricted session also cannot read unrestricted sessions. Restricted Sessions are useful for IoT devices (e.g Arduino or Embedded C) that may run in a less-trusted physical environment than mobile apps. However, please keep in mind that restricted sessions can still read data on `User`, `Session`, and `Role` classes, and can read/write data in any other class just like a normal session. So it is still important for IoT devices to be in a safe physical environment and ideally use encrypted storage to store the session token.

If you want to prevent restricted Sessions from modifying classes other than `User`, `Session`, or `Role`, you can write a Cloud Code `beforeSave` handler for that class:

```
Parse.Cloud.beforeSave("MyClass", async request => {
  const user = request.user;
  const token = user.getSessionToken(); 
  const query = new Parse.Query(Parse.Session);
  query.equalTo('sessionToken', token);
  const session = await q.first({ useMasterKey: true });
  if (session.get('restricted')) {
      throw 'write operation not allowed';
  }
});
```

You can configure Class-Level Permissions (CLPs) for the Session class just like other classes on Parse. CLPs restrict reading/writing of sessions via the `/parse/sessions` API, but do not restrict Parse Cloud’s automatic session creation/deletion when users log in, sign up, and log out. We recommend that you disable all CLPs not needed by your app. Here are some common use cases for Session CLPs:

*   **Find**, **Delete** — Useful for building a UI screen that allows users to see their active session on all devices, and log out of sessions on other devices. If your app does not have this feature, you should disable these permissions.
*   **Create** — Useful for IoT apps (e.g. Arduino or Embedded C) that provision restricted user sessions for other devices from the phone app. You should disable this permission when building apps for mobile and web. For IoT apps, you should check whether your IoT device actually needs to access user-specific data. If not, then your IoT device does not need a user session, and you should disable this permission.
*   **Get**, **Update**, **Add Field** — Unless you need these operations, you should disable these permissions.

[](https://docs.parseplatform.org/rest/guide/#roles)Roles
---------------------------------------------------------

As your app grows in scope and user-base, you may find yourself needing more coarse-grained control over access to pieces of your data than user-linked ACLs can provide. To address this requirement, Parse supports a form of [Role-based Access Control](https://en.wikipedia.org/wiki/Role-based_access_control). Roles provide a logical way of grouping users with common access privileges to your Parse data. Roles are named objects that contain users and other roles. Any permission granted to a role is implicitly granted to its users as well as to the users of any roles that it contains.

For example, in your application with curated content, you may have a number of users that are considered “Moderators” and can modify and delete content created by other users. You may also have a set of users that are “Administrators” and are allowed all of the same privileges as Moderators, but can also modify the global settings for the application. By adding users to these roles, you can ensure that new users can be made moderators or administrators, without having to manually grant permission to every resource for each user.

We provide a specialized role class to represent these groupings of users for the purposes of assigning permissions. Roles have a few special fields that set them apart from other objects.

*   name: The name for the role. This value is required, and can only be set once as a role is being created. The name must consist of alphanumeric characters, spaces, -, or _. This name will be used to identify the Role without needing its objectId.
*   users: A [relation](https://docs.parseplatform.org/rest/guide/#updating-objects) to the set of users that will inherit permissions granted to the containing role.
*   roles: A [relation](https://docs.parseplatform.org/rest/guide/#updating-objects) to the set of child roles whose users and roles will inherit permissions granted to the containing role.

Often, in order to keep these roles secure, your mobile apps won’t be directly responsible for managing creation and membership of your roles. Instead, roles may be managed by a separate interface on the web or manually managed by an administrator. Our REST API allows you to manage your roles without requiring a mobile client.

[](https://docs.parseplatform.org/rest/guide/#creating-roles)Creating Roles
---------------------------------------------------------------------------

Creating a new role differs from creating a generic object in that the `name` field is required. Roles must also specify an [`ACL`](https://docs.parseplatform.org/rest/guide/#access-control-lists), which should be as restrictive as possible to avoid allowing the wrong users to modify a role.

To create a new role, send a POST request to the roles root:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "name": "Moderators",
        "ACL": {
          "*": {
            "read": true
          }
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/roles
```

You can create a role with child roles or users by adding existing objects to the `roles` and `users`[relations](https://docs.parseplatform.org/rest/guide/#updating-objects):

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "name": "Moderators",
        "ACL": {
          "*": {
            "read": true
          }
        },
        "roles": {
          "__op": "AddRelation",
          "objects": [
            {
              "__type": "Pointer",
              "className": "_Role",
              "objectId": "Ed1nuqPvc"
            }
          ]
        },
        "users": {
          "__op": "AddRelation",
          "objects": [
            {
              "__type": "Pointer",
              "className": "_User",
              "objectId": "8TOXdXf3tz"
            }
          ]
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/roles
```

When the creation is successful, the HTTP response is a `201 Created` and the Location header contains the object URL for the new object:

```
Status: 201 Created
Location: https://YOUR.PARSE-SERVER.HERE/parse/roles/mrmBZvsErB
```

The response body is a JSON object containing the `objectId` and `createdAt` timestamp of the newly-created object:

```
{
  "createdAt": "2022-01-01T12:23:45.678Z",
  "objectId": "mrmBZvsErB"
}
```

[](https://docs.parseplatform.org/rest/guide/#retrieving-roles)Retrieving Roles
-------------------------------------------------------------------------------

You can also retrieve the contents of a role object by sending a GET request to the URL returned in the location header when it was created. For example, to retrieve the role created above:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  https://YOUR.PARSE-SERVER.HERE/parse/roles/mrmBZvsErB
```

The response body is a JSON object containing all of the fields on the role:

```
{
  "createdAt": "2022-01-01T12:23:45.678Z",
  "objectId": "mrmBZvsErB",
  "updatedAt": "2022-01-01T12:23:45.678Z",
  "ACL": {
    "*": {
      "read": true
    },
    "role:Administrators": {
      "write": true
    }
  },
  "name": "Moderators"
}
```

Note that the `users` and `roles` relations will not be visible in this JSON. Instead, you must [query](https://docs.parseplatform.org/rest/guide/#relational-queries) for the roles and users that belong to a given role using the `$relatedTo` operator.

[](https://docs.parseplatform.org/rest/guide/#updating-roles)Updating Roles
---------------------------------------------------------------------------

Updating a role generally works like [updating any other object](https://docs.parseplatform.org/rest/guide/#updating-objects), but the `name` field on the role cannot be changed. Adding and removing users and roles to the `users` and `roles` relations can be accomplished by using the `AddRelation` and `RemoveRelation` operators.

For example, we can add two users to the “Moderators” role created above like so:

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "users": {
          "__op": "AddRelation",
          "objects": [
            {
              "__type": "Pointer",
              "className": "_User",
              "objectId": "8TOXdXf3tz"
            },
            {
              "__type": "Pointer",
              "className": "_User",
              "objectId": "g7y9tkhB7O"
            }
          ]
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/roles/mrmBZvsErB
```

Similarly, we can remove a child role from the “Moderators” role created above like so:

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "roles": {
          "__op": "RemoveRelation",
          "objects": [
            {
              "__type": "Pointer",
              "className": "_Role",
              "objectId": "Ed1nuqPvc"
            }
          ]
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/roles/mrmBZvsErB
```

Note that we’ve included the master key in the query above because the “Moderators” role has an ACL that restricts modification by the public.

[](https://docs.parseplatform.org/rest/guide/#deleting-roles)Deleting Roles
---------------------------------------------------------------------------

To delete a role from the Parse Cloud, send a DELETE request to its URL. For example:

```
curl -X DELETE \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  https://YOUR.PARSE-SERVER.HERE/parse/roles/mrmBZvsErB
```

Again, we pass the master key in order to bypass the ACL on the role itself. Alternatively, we could pass an X-Parse-Session-Token for a user that has write access to the Role object (e.g. an Administrator). For example:

```
curl -X DELETE \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "X-Parse-Session-Token: pnktnjyb996sj4p156gjtp4im" \
  https://YOUR.PARSE-SERVER.HERE/parse/roles/mrmBZvsErB
```

[](https://docs.parseplatform.org/rest/guide/#security-with-role)Security with Role
-----------------------------------------------------------------------------------

When you access Parse via the REST API key, access can be restricted by ACL just like in the iOS and Android SDKs. You can still read and modify ACLs via the REST API, just by accessing the `"ACL"` key of an object. In addition to per-user permissions [as described above](https://docs.parseplatform.org/rest/guide/#access-control-lists), you can also specify role-level permissions to your Parse objects. Instead of specifying an `objectId` as the key for a permission object as you do for users, you can instead specify a role’s name with a `"role:"` prefix as the key for a permission object. You can use role-level permissions alongside user-level permissions to provide fine-grained control over user access.

For example, to restrict an object to be readable by anyone in the “Members” role and writable by its creator and anyone in the “Moderators” role, you would specify an ACL like this:

```
{
  "8TOXdXf3tz": {
    "write": true
  },
  "role:Members": {
    "read": true
  },
  "role:Moderators": {
    "write": true
  }
}
```

You are not required to specify read permissions for the user or the “Moderators” role if the user and role are already children of the “Members” role, since they will inherit read permissions granted to “Members”.

[](https://docs.parseplatform.org/rest/guide/#role-hierarchy)Role Hierarchy
---------------------------------------------------------------------------

As described above, one role can contain another, establishing a parent-child relationship between the two roles. The consequence of this relationship is that any permission granted to the parent role is implicitly granted to all of its child roles.

These types of relationships are commonly found in applications with user-managed content, such as forums. Some small subset of users are “Administrators”, with the highest level of access to tweaking the application’s settings, creating new forums, setting global messages, and so on. Another set of users are “Moderators”, who are responsible for ensuring that the content created by users remains appropriate. Any user with Administrator privileges should also be granted the permissions of any Moderator. To establish this relationship, you would make your “Administrators” role a child role of “Moderators” by adding the “Administrators” role to the `roles` relation on your “Moderators” object like this:

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "roles": {
          "__op": "AddRelation",
          "objects": [
            {
              "__type": "Pointer",
              "className": "_Role",
              "objectId": "<AdministratorsRoleObjectId>"
            }
          ]
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/roles/<ModeratorsRoleObjectId>
```

[](https://docs.parseplatform.org/rest/guide/#files)Files
---------------------------------------------------------

[](https://docs.parseplatform.org/rest/guide/#uploading-files)Uploading Files
-----------------------------------------------------------------------------

To upload a file to Parse, send a POST request to the files URL, postfixed with the name of the file. The request must contain the `Content-Type` header associated with the file. Keep in mind that files are limited to 10 megabytes. Here’s a simple example that’ll create a file named `hello.txt` containing a string:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: text/plain" \
  -d 'Hello, World!' \
  https://YOUR.PARSE-SERVER.HERE/parse/files/hello.txt
```

When the file upload is successful, the HTTP response is a `201 Created` and the `Location` header which contains the URL for the file:

```
Status: 201 Created
Location: http://files.parsetfss.com/bc9f32df-2957-4bb1-93c9-ec47d9870a05/tfss-db295fb2-8a8b-49f3-aad3-dd911142f64f-hello.txt
```

The response body is a JSON object containing the `name` of the file, which is the original file name prefixed with a unique identifier in order to prevent name collisions. This means you can save files with the same name, and the files will not overwrite one another.

```
{
  "url": "http://files.parsetfss.com/bc9f32df-2957-4bb1-93c9-ec47d9870a05/tfss-db295fb2-8a8b-49f3-aad3-dd911142f64f-hello.txt",
  "name": "db295fb2-8a8b-49f3-aad3-dd911142f64f-hello.txt"
}
```

To upload an image, the syntax is a little bit different. Here’s an example that will upload the image `myPicture.jpg` from the current directory.

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: image/jpeg" \
  --data-binary '@myPicture.jpg' \
  https://YOUR.PARSE-SERVER.HERE/parse/files/pic.jpg
```

[](https://docs.parseplatform.org/rest/guide/#associating-with-objects)Associating with Objects
-----------------------------------------------------------------------------------------------

After files are uploaded, you can associate them with Parse objects:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "name": "Andrew",
        "picture": {
          "name": "...profile.png",
          "url": "...profile.png",
          "__type": "File"
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/PlayerProfile
```

Note that the name of the file in the request is not the local file name, but the name in the response of the previous upload operation. It is also important to add the `url` from the previous upload operation to the request.

[](https://docs.parseplatform.org/rest/guide/#deleting-files)Deleting Files
---------------------------------------------------------------------------

Users holding the master key are allowed to delete files using the REST API. To delete a file, send a DELETE request to the files URL, postfixed with the name of the file. Note that the name of the file must be the name in the response of the upload operation, rather than the original filename. Note that the `X-Parse-Master-Key` must be provided in headers.

```
curl -X DELETE \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  https://YOUR.PARSE-SERVER.HERE/parse/files/...profile.png
```

Note that deleting a PFObject with a file associated with it will not delete the file. All files stored on Parse should be deleted by using the above explained API.

[](https://docs.parseplatform.org/rest/guide/#geopoints)GeoPoints
-----------------------------------------------------------------

Parse allows you to associate real-world latitude and longitude coordinates with an object. Adding a `GeoPoint` data type to a class allows queries to take into account the proximity of an object to a reference point. This allows you to easily do things like find out what user is closest to another user or which places are closest to a user.

[](https://docs.parseplatform.org/rest/guide/#geopoint)GeoPoint
---------------------------------------------------------------

To associate a point with an object you will need to embed a `GeoPoint` data type into your object. This is done by using a JSON object with `__type` set to the string `GeoPoint` and numeric values being set for the `latitude` and `longitude` keys. For example, to create an object containing a point under the “location” key with a latitude of 40.0 degrees and -30.0 degrees longitude:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "location": {
          "__type": "GeoPoint",
          "latitude": 40.0,
          "longitude": -30.0
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/PlaceObject
```

[](https://docs.parseplatform.org/rest/guide/#geo-queries)Geo Queries
---------------------------------------------------------------------

Now that you have a bunch of objects with spatial coordinates, it would be nice to find out which objects are closest to a point. This can be done by using a `GeoPoint` data type with query on the field using `$nearSphere`. Getting a list of ten places that are closest to a user may look something like:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'limit=10' \
  --data-urlencode 'where={
        "location": {
          "$nearSphere": {
            "__type": "GeoPoint",
            "latitude": 30.0,
            "longitude": -20.0
          }
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/PlaceObject
```

This will return a list of results ordered by distance from 30.0 latitude and -20.0 longitude. The first result will be the nearest object. (Note that if an explicit `order` parameter is supplied, it will take precedence over the distance ordering.) For example, here are two results returned for the above query:

```
{
  "results": [
    {
      "location": {
        "latitude": 40.0,
        "__type": "GeoPoint",
        "longitude": -30.0
      },
      "updatedAt": "2022-01-01T12:23:45.678Z",
      "createdAt": "2022-01-01T12:23:45.678Z",
      "objectId": "iFEPN5Gwoz"
    },
    {
      "location": {
        "latitude": 60.0,
        "__type": "GeoPoint",
        "longitude": -20.0
      },
      "updatedAt": "2022-01-01T12:23:45.678Z",
      "createdAt": "2022-01-01T12:23:45.678Z",
      "objectId": "LAyNKSNTHT"
    }
  ]
}
```

To limit the search to a maximum distance add a `$maxDistanceInMiles` (for miles), `$maxDistanceInKilometers` (for kms), or `$maxDistanceInRadians` (for radian angle), term to the key constraint. For example, the following limits the radius to 10 miles:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={
        "location": {
          "$nearSphere": {
            "__type": "GeoPoint",
            "latitude": 30.0,
            "longitude": -20.0
          },
          "$maxDistanceInMiles": 10.0
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/PlaceObject
```

It’s also possible to query for the set of objects that are contained within a particular area. To find the objects in a rectangular bounding box, add a clause to the key constraint with the format `{"$within": {"$box": {[southwestGeoPoint, northeastGeoPoint]}}}`.

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={
        "location": {
          "$within": {
            "$box": [
              {
                "__type": "GeoPoint",
                "latitude": 37.71,
                "longitude": -122.53
              },
              {
                "__type": "GeoPoint",
                "latitude": 30.82,
                "longitude": -122.37
              }
            ]
          }
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/classes/PizzaPlaceObject
```

*   Starting with Parse-Server 2.5.0

It’s also possible to query for the set of objects that are contained within or on the bounds of a polygon. `$polygon` allows for opened or closed paths, minimum of 3 `GeoPoint`’s.

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -G \
  --data-urlencode 'where={
        "location": {
          "$geoWithin": {
            "$polygon": [
              {
                "__type": "GeoPoint",
                "latitude": 25.774,
                "longitude": -80.190
              },
              {
                "__type": "GeoPoint",
                "latitude": 18.466,
                "longitude": -66.118
              },
              {
                "__type": "GeoPoint",
                "latitude": 32.321,
                "longitude": -64.757
              }
            ]
          }
        }
      }' \
  https://api.parse.com/1/classes/PizzaPlaceObject
```

[](https://docs.parseplatform.org/rest/guide/#caveats)Caveats
-------------------------------------------------------------

At the moment there are a couple of things to watch out for:

1.   Each PFObject class may only have one key with a PFGeoPoint object.
2.   Using the `$nearSphere` constraint will also limit results to within 100 miles.
3.   Points should not equal or exceed the extreme ends of the ranges. Latitude should not be -90.0 or 90.0. Longitude should not be -180.0 or 180.0. Attempting to use `GeoPoint`’s with latitude and/or longitude outside these ranges will cause an error.

[](https://docs.parseplatform.org/rest/guide/#data)Data
-------------------------------------------------------

We’ve designed the Parse SDKs so that you typically don’t need to worry about how data is saved while using the client SDKs. Simply add data to the Parse `Object`, and it’ll be saved correctly.

Nevertheless, there are some cases where it’s useful to be aware of how data is stored on the Parse platform.

[](https://docs.parseplatform.org/rest/guide/#data-storage)Data Storage
-----------------------------------------------------------------------

Internally, Parse stores data as JSON, so any datatype that can be converted to JSON can be stored on Parse. Refer to the [Data Types in Objects](https://docs.parseplatform.org/rest/guide/#data-types) section of this guide to see platform-specific examples.

Keys including the characters `$` or `.`, along with the key `__type` key, are reserved for the framework to handle additional types, so don’t use those yourself. Key names must contain only numbers, letters, and underscore, and must start with a letter. Values can be anything that can be JSON-encoded.

[](https://docs.parseplatform.org/rest/guide/#data-type-lock-in)Data Type Lock-in
---------------------------------------------------------------------------------

When a class is initially created, it doesn’t have an inherent schema defined. This means that for the first object, it could have any types of fields you want.

However, after a field has been set at least once, that field is locked into the particular type that was saved. For example, if a `User` object is saved with field `name` of type `String`, that field will be restricted to the `String` type only (the server will return an error if you try to save anything else).

One special case is that any field can be set to `null`, no matter what type it is.

[](https://docs.parseplatform.org/rest/guide/#the-data-browser)The Data Browser
-------------------------------------------------------------------------------

The Data Browser is the web UI where you can update and create objects in each of your apps. Here, you can see the raw JSON values that are saved that represents each object in your class.

When using the interface, keep in mind the following:

*   The `objectId`, `createdAt`, `updatedAt` fields cannot be edited (these are set automatically).
*   The value “(empty)” denotes that the field has not been set for that particular object (this is different than `null`).
*   You can remove a field’s value by hitting your Delete key while the value is selected.

The Data Browser is also a great place to test the Cloud Code validations contained in your Cloud Code functions (such as `beforeSave`). These are run whenever a value is changed or object is deleted from the Data Browser, just as they would be if the value was changed or deleted from your client code.

[](https://docs.parseplatform.org/rest/guide/#importing-data)Importing Data
---------------------------------------------------------------------------

You may import data into your Parse app by using CSV or JSON files. To create a new class with data from a CSV or JSON file, go to the Data Browser and click the “Import” button on the left hand column.

The JSON format is an array of objects in our REST format or a JSON object with a `results` that contains an array of objects. It must adhere to the [JSON standard](http://json.org/). A file containing regular objects could look like:

```
{ "results": [
  {
    "score": 1337,
    "playerName": "Sean Plott",
    "cheatMode": false,
    "createdAt": "2022-01-01T12:23:45.678Z",
    "updatedAt": "2022-01-01T12:23:45.678Z",
    "objectId": "fchpZwSuGG"
  }]
}
```

Objects in either format should contain keys and values that also satisfy the following:

*   Key names must contain only numbers, letters, and underscore, and must start with a letter.
*   No value may contain a hard newline ‘`\n`’.

Normally, when objects are saved to Parse, they are automatically assigned a unique identifier through the `objectId` field, as well as a `createdAt` field and `updatedAt` field which represent the time that the object was created and last modified in your Parse Server. These fields can be manually set when data is imported from a JSON file. Please keep in mind the following:

*   Use a unique 10 character alphanumeric string as the value of your `objectId` fields.
*   Use a UTC timestamp in the ISO 8601 format when setting a value for the `createdAt` field or the `updatedAt` field.

In addition to the exposed fields, objects in the Parse User class can also have the `bcryptPassword` field set. The value of this field is a `String` that is the bcrypt hashed password + salt in the modular crypt format described in this [StackOverflow answer](http://stackoverflow.com/a/5882472/1351961). Most OpenSSL based bcrypt implementations should have built-in methods to produce these strings.

A file containing a `User` object could look like:

```
{ "results":
  [{
    "username": "cooldude",
    "createdAt": "1983-09-13T22:42:30.548Z",
    "updatedAt": "2015-09-04T10:12:42.137Z",
    "objectId": "ttttSEpfXm",
    "sessionToken": "dfwfq3dh0zwe5y2sqv514p4ib",
    "bcryptPassword": "$2a$10$ICV5UeEf3lICfnE9W9pN9.O9Ved/ozNo7G83Qbdk5rmyvY8l16MIK"
  }]
}
```

Note that in CSV the import field types are limited to `String`, `Boolean`, and `Number`.

[](https://docs.parseplatform.org/rest/guide/#exporting-your-data)Exporting your Data
-------------------------------------------------------------------------------------

You can request an export of your data at any time from your app’s Settings page. The data export runs at a lower priority than production queries, so if your app is still serving queries, production traffic will always be given a higher priority, which may slow down the delivery of your data export.

### [](https://docs.parseplatform.org/rest/guide/#export-formats)Export Formats

Each collection will be exported in the same JSON format used by our REST API and delivered in a single zipped file. Since data is stored internally as JSON, this allows us to ensure that the export closely matches how the data is saved to Parse. Other formats such as CSV cannot represent all of the data types supported by Parse without losing information. If you’d like to work with your data in CSV format, you can use any of the JSON-to-CSV converters available widely on the web.

### [](https://docs.parseplatform.org/rest/guide/#offline-analysis)Offline Analysis

For offline analysis of your data, we highly recommend using alternate ways to access your data that do not require extracting the entire collection at once. For example, you can try exporting only the data that has changed since your last export. Here are some ways of achieving this:

*   Use the JavaScript SDK in a node app. `Parse.Query.each()` will allow you to extract every single object that matches a query. You can use date constraints to make sure the query only matches data that has been updated since you last ran this app. Your node app can write this data to disk for offline analysis.

*   Use the REST API in a script. You can run queries against your class and use skip/limit to page through results, which can then be written to disk for offline analysis. You can again use date constraints to make sure only newly updated data is extracted.

*   If the above two options do not fit your needs, you can try using the Data Browser to export data selectively. Use the Funnel icon to create a filter for the specific data that you need to export, such as newly updated objects. Once the filter has been applied, click on the Export data icon on the upper right of your Data Browser. This type of export will only include the objects that match your criteria.

[](https://docs.parseplatform.org/rest/guide/#push-notifications)Push Notifications
-----------------------------------------------------------------------------------

Push Notifications are a great way to keep your users engaged and informed about your app. You can reach your entire user base quickly and effectively. This guide will help you through the setup process and the general usage of Parse to send push notifications.

If you haven’t installed the SDK yet, please [head over to the Push QuickStart](https://docs.parseplatform.org/parse-server/guide/#push-notifications-quick-start) to get our SDK up and running.

[](https://docs.parseplatform.org/rest/guide/#installations)Installations
-------------------------------------------------------------------------

### [](https://docs.parseplatform.org/rest/guide/#uploading-installation-data)Uploading Installation Data

An installation object represents an instance of your app being installed on a device. These objects are used to store subscription data for installations which have subscribed to one or more push notification channels. Installations have a flexible schema, except that the special fields below have special type and validation requirements:

*   **`badge`**: is a number field representing the last known application badge for iOS installations.
*   **`channels`**: An array of the channels to which a device is currently subscribed.
*   **`timeZone`**: The current time zone where the target device is located. This should be an [IANA time zone identifier](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
*   **`deviceType`**: The type of device, “ios”, “android”, “winrt”, “winphone”, or “dotnet”_(readonly)_.
*   **`pushType`**: This field is reserved for directing Parse to the push delivery network to be used. If the device is registered to receive pushes via FCM, this field will be marked “gcm”. If this device is not using FCM, and is using Parse’s push notification service, it will be blank _(readonly)_.
*   **`installationId`**: Universally Unique Identifier (UUID) for the device used by Parse. It must be unique across all of an app’s installations. _(readonly)_.
*   **`deviceToken`**: The Apple or Google generated token used to deliver messages to the APNs or FCM push networks respectively.
*   **`channelUris`**: The Microsoft-generated push URIs for Windows devices.
*   **`appName`**: The display name of the client application to which this installation belongs.
*   **`appVersion`**: The version string of the client application to which this installation belongs.
*   **`parseVersion`**: The version of the Parse SDK which this installation uses.
*   **`appIdentifier`**: A unique identifier for this installation’s client application. In iOS, this is the Bundle Identifier.

Most of the time, installation data is modified by push-related methods in the client SDK. For example, calling `subscribeToChannel` or `unsubscribeFromChannel` from the client SDK will create an object for that installation if it doesn’t yet exist and update its channels, and calling `getSubscribedChannels` from the client SDK will read subscription data from that installation’s object. The REST methods can be used to mimic these operations. For instance, if you have an iOS device token then you can subscribe it to push notifications by creating an installation object for it with the desired `channels` list. You can also perform operations which aren’t possible through the client SDK, like using a query over installations to find the set of subscribers to a given channel.

Creating an installation object is similar to creating a generic object, but the special installation fields listed above must pass validation. For example, if you have a device token provided by the Apple Push Notification service and would like to subscribe it to the broadcast channel `""`, you can use the following command:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "deviceType": "ios",
        "deviceToken": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
        "channels": [
          ""
        ]
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/installations
```

When the creation is successful, the HTTP response is a `201 Created` and the `Location` header contains the URL for the new installation:

```
Status: 201 Created
Location: https://YOUR.PARSE-SERVER.HERE/parse/installations/mrmBZvsErB
```

The response body is a JSON object containing the `objectId` and the `createdAt` timestamp of the newly-created installation:

```
{
  "createdAt": "2022-01-01T12:23:45.678Z",
  "objectId": "mrmBZvsErB"
}
```

When creating Android installation objects containing FCM (Firebase Cloud Messaging) credentials, you must have at least the following fields in your installation object:

*   A `deviceType` set to `android`.
*   A `pushType` set to `gcm`.
*   A FCM registration token in the `deviceToken` field.

You could create and object with these fields using a command like this:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "deviceType": "android",
        "pushType": "gcm",
        "deviceToken": "APA91bFMvbrGg4cp3KUV_7dhU1gmwE_...",
        "channels": [
          ""
        ]
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/installations
```

### [](https://docs.parseplatform.org/rest/guide/#retrieving-installations)Retrieving Installations

You can retrieve the contents of an installation object by sending a GET request to the URL returned in the location header when it was created. For example, to retrieve the installation created above:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  https://YOUR.PARSE-SERVER.HERE/parse/installations/mrmBZvsErB
```

The response body is a JSON object containing all the user-provided fields, plus the `createdAt`, `updatedAt`, and `objectId` fields:

```
{
  "deviceType": "ios",
  "deviceToken": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
  "channels": [
    ""
  ],
  "createdAt": "2022-01-01T12:23:45.678Z",
  "updatedAt": "2022-01-01T12:23:45.678Z",
  "objectId": "mrmBZvsErB"
}
```

### [](https://docs.parseplatform.org/rest/guide/#updating-installations)Updating Installations

Installation objects can be updated by sending a PUT request to the installation URL. For example, to subscribe the installation above to the “foo” push channel:

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "deviceType": "ios",
        "deviceToken": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
        "channels": [
          "",
          "foo"
        ]
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/installations/mrmBZvsErB
```

Note that there is a restriction on updating the `deviceToken` field of Installation objects. You can only update the `deviceToken` field of an Installation object if contains a non-nil `installationId` field.

### [](https://docs.parseplatform.org/rest/guide/#querying-installations)Querying Installations

You can retrieve multiple installations at once by sending a GET request to the root installations URL. This functionality is not available in the SDKs, so you must authenticate this method using the `X-Parse-Master-Key` header in your request instead of the `X-Parse-REST-API-Key` header. Your master key allows you to bypass ACLs and should only be used from within a trusted environment.

Without any URL parameters, a GET request simply lists installations:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  https://YOUR.PARSE-SERVER.HERE/parse/installations
```

The return value is a JSON object that contains a results field with a JSON array that lists the users.

```
{
  "results": [
    {
      "deviceType": "ios",
      "deviceToken": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
      "channels": [
        ""
      ],
      "createdAt": "2022-01-01T12:23:45.678Z",
      "updatedAt": "2022-01-01T12:23:45.678Z",
      "objectId": "mrmBZvsErB"
    },
    {
      "deviceType": "ios",
      "deviceToken": "fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210",
      "channels": [
        ""
      ],
      "createdAt": "2022-01-01T12:23:45.678Z",
      "updatedAt": "2022-01-01T12:23:45.678Z",
      "objectId": "sGlvypFQcO"
    }
  ]
}
```

All of the options for queries that work for regular objects also work for installation objects, so check the section on [Querying Objects](https://docs.parseplatform.org/rest/guide/#basic-queries) for more details. By doing an array query over `channels`, for example, you can find the set of devices subscribed to a given push channel.

### [](https://docs.parseplatform.org/rest/guide/#deleting-installations)Deleting Installations

To delete an installation from the Parse Cloud, send a DELETE request to its URL. This functionality is not available in the client SDKs, so you must authenticate this method using the `X-Parse-Master-Key` header in your request instead of the `X-Parse-REST-API-Key` header. Your master key allows you to bypass ACLs and should only be used from within a trusted environment. For example:

```
curl -X DELETE \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  https://YOUR.PARSE-SERVER.HERE/parse/installations/mrmBZvsErB
```

[](https://docs.parseplatform.org/rest/guide/#sending-pushes)Sending Pushes
---------------------------------------------------------------------------

There are two ways to send push notifications using Parse: [channels](https://docs.parseplatform.org/rest/guide/#using-channels) and [advanced targeting](https://docs.parseplatform.org/rest/guide/#using-advanced-targeting). Channels offer a simple and easy to use model for sending pushes, while advanced targeting offers a more powerful and flexible model. Both are fully compatible with each other and will be covered in this section.

You can view your past push notifications on the Parse Dashboard push console for up to 30 days after creating your push. For pushes scheduled in the future, you can delete the push on the push console as long as no sends have happened yet. After you send the push, the push console shows push analytics graphs.

### [](https://docs.parseplatform.org/rest/guide/#using-channels)Using Channels

The simplest way to start sending notifications is using channels. This allows you to use a publisher-subscriber model for sending pushes. Devices start by subscribing to one or more channels, and notifications can later be sent to these subscribers. The channels subscribed to by a given `Installation` are stored in the `channels` field of the `Installation` object.

#### [](https://docs.parseplatform.org/rest/guide/#subscribing-to-channels)Subscribing to Channels

A channel is identified by a string that starts with a letter and consists of alphanumeric characters, underscores, and dashes. It doesn’t need to be explicitly created before it can be used and each `Installation` can subscribe to any number of channels at a time.

Subscribing to a channel via the REST API can be done by updating the `Installation` object. We send a PUT request to the `Installation` URL and update the `channels` field. For example, in a baseball score app, we could do:

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "channels": [
          "Giants"
        ]
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/installations/mrmBZvsErB
```

Once subscribed to the “Giants” channel, your `Installation` object should have an updated `channels` field.

![Image 1](https://docs.parseplatform.org/assets/images/installation_channel.png)

To unsubscribe from a channel you would need to update the `channels` array and remove the unsubscribed channel.

#### [](https://docs.parseplatform.org/rest/guide/#sending-pushes-to-channels)Sending Pushes to Channels

With the REST API, the following code can be used to alert all subscribers of the “Giants” and “Mets” channels about the results of the game. This will display a notification center alert to iOS users and a system tray notification to Android users.

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "channels": [
          "Giants",
          "Mets"
        ],
        "data": {
          "alert": "The Giants won against the Mets 2-3."
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/push
```

### [](https://docs.parseplatform.org/rest/guide/#using-advanced-targeting)Using Advanced Targeting

While channels are great for many applications, sometimes you need more precision when targeting the recipients of your pushes. Parse allows you to write a query for any subset of your `Installation` objects using the [querying API](https://docs.parseplatform.org/rest/guide/#queries) and to send them a push.

Since `Installation` objects are just like any other object stored in Parse, you can save any data you want and even create relationships between `Installation` objects and your other objects. This allows you to send pushes to a very customized and dynamic segment of your user base.

#### [](https://docs.parseplatform.org/rest/guide/#saving-installation-data)Saving Installation Data

Storing arbitrary data on an `Installation` object is done in the same way we store data on [any other object](https://docs.parseplatform.org/rest/guide/#objects) on Parse. In our Baseball app, we could allow users to get pushes about game results, scores and injury reports.

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "scores": true,
        "gameResults": true,
        "injuryReports": true
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/installations/mrmBZvsErB
```

You can even create relationships between your `Installation` objects and other classes saved on Parse. To associate an Installation with a particular user, for example, you can use a pointer to the `_User` class on the `Installation`.

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "user": {
          "__type": "Pointer",
          "className": "_User",
          "objectId": "vmRZXZ1Dvo"
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/installations/mrmBZvsErB
```

#### [](https://docs.parseplatform.org/rest/guide/#sending-pushes-to-queries)Sending Pushes to Queries

Once you have your data stored on your `Installation` objects, you can use a query to target a subset of these devices. `Installation` queries work just like any other [Parse query](https://docs.parseplatform.org/rest/guide/#queries).

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "where": {
          "injuryReports": true
        },
        "data": {
          "alert": "Willie Hayes injured by own pop fly."
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/push
```

We can even use channels with our query. To send a push to all subscribers of the “Giants” channel but filtered by those who want score update, we can do the following:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "where": {
          "channels": "Giants",
          "scores": true
        },
        "data": {
          "alert": "The Giants scored a run! The score is now 2-2."
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/push
```

If we store relationships to other objects in our `Installation` class, we can also use those in our query. For example, we could send a push notification to all users near a given location like this.

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "where": {
          "user": {
            "$inQuery": {
              "location": {
                "$nearSphere": {
                  "__type": "GeoPoint",
                  "latitude": 30.0,
                  "longitude": -20.0
                },
                "$maxDistanceInMiles": 1.0
              }
            }
          }
        },
        "data": {
          "alert": "Free hotdogs at the Parse concession stand!"
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/push
```

An in depth look at the `Installation` end point can be found in the [REST guide](https://docs.parseplatform.org/rest/guide/#installations).

[](https://docs.parseplatform.org/rest/guide/#sending-options)Sending Options
-----------------------------------------------------------------------------

Push notifications can do more than just send a message. In iOS, pushes can also include the sound to be played, the badge number to display as well as any custom data you wish to send. In Android, it is even possible to specify an `Intent` to be fired upon receipt of a notification. An expiration date can also be set for the notification in case it is time sensitive.

### [](https://docs.parseplatform.org/rest/guide/#customizing-your-notifications)Customizing your Notifications

If you want to send more than just a message, you can set other fields in the `data` dictionary. There are some reserved fields that have a special meaning.

*   **`alert`**: the notification’s message.
*   **`badge`**: _(iOS only)_ the value indicated in the top right corner of the app icon. This can be set to a value or to `Increment` in order to increment the current value by 1.
*   **`sound`**: _(iOS only)_ the name of a sound file in the application bundle.
*   **`content-available`**: _(iOS only)_ If you are a writing an app using the Remote Notification Background Mode [introduced in iOS7](https://developer.apple.com/library/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS7.html#//apple_ref/doc/uid/TP40013162-SW10) (a.k.a. “Background Push”), set this value to 1 to trigger a background download. You also have to set `push_type` starting iOS 13 and watchOS 6.
*   **`push_type`**: _(iOS only)_ The type of the notification. The value is `alert` or `background`. Specify `alert` when the delivery of your notification displays an alert, plays a sound, or badges your app’s icon. Specify `background` for silent notifications that do not interact with the user. Defaults to `alert` if no value is set. Required when delivering notifications to devices running iOS 13 and later, or watchOS 6 and later.
*   **`priority`**: _(iOS only)_ The priority of the notification. Specify 10 to send the notification immediately. Specify 5 to send the notification based on power considerations on the user’s device. ([More detailed documentation](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns))
*   **`category`**: _(iOS only)_ the identifier of the [`UNNotification​Category`](https://developer.apple.com/reference/usernotifications/unnotificationcategory) for this push notification.
*   **`uri`**: _(Android only)_ an optional field that contains a URI. When the notification is opened, an `Activity` associated with opening the URI is launched.
*   **`title`**: _(Android only)_ the value displayed in the Android system tray notification.

For example, to send a notification that increases the current badge number by 1 and plays a custom sound for iOS devices, and displays a particular title for Android users, you can do the following:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "channels": [
          "Mets"
        ],
        "data": {
          "alert": "The Mets scored! The game is now tied 1-1.",
          "badge": "Increment",
          "sound": "cheering.caf",
          "title": "Mets Score!"
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/push
```

It is also possible to specify your own data in this dictionary. As explained in the Receiving Notifications section for [iOS](https://docs.parseplatform.org/ios/guide/#receiving-pushes) and [Android](https://docs.parseplatform.org/android/guide/#receiving-pushes), iOS will give you access to this data only when the user opens your app via the notification and Android will provide you this data in the `Intent` if one is specified.

### [](https://docs.parseplatform.org/rest/guide/#setting-an-expiration-date)Setting an Expiration Date

When a user’s device is turned off or not connected to the internet, push notifications cannot be delivered. If you have a time sensitive notification that is not worth delivering late, you can set an expiration date. This avoids needlessly alerting users of information that may no longer be relevant.

There are two parameters provided by Parse to allow setting an expiration date for your notification. The first is `expiration_time` which takes a date (in ISO 8601 format or Unix epoch time) specifying when Parse should stop trying to send the notification. To expire the notification exactly 1 week from now, you can use the following command.

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "expiration_time": "2015-03-19T22:05:08Z",
        "data": {
          "alert": "Season tickets on sale until March 19, 2015"
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/push
```

Alternatively, you can use the `expiration_interval` parameter to specify a duration of time before your notification expired. This value is relative to the `push_time` parameter used to [schedule notifications](https://docs.parseplatform.org/rest/guide/#scheduling-pushes). This means that a push notification scheduled to be sent out in 1 day and an expiration interval of 6 days can be received up to a week from March 16th, 2015.

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "push_time": "2015-03-13T22:05:08Z",
        "expiration_interval": 518400,
        "data": {
          "alert": "Season tickets on sale until March 19, 2015"
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/push
```

### [](https://docs.parseplatform.org/rest/guide/#targeting-by-platform)Targeting by Platform

If you build a cross platform app, it is possible you may only want to target iOS or Android devices. There are two methods provided to filter which of these devices are targeted. Note that both platforms are targeted by default.

The following examples would send a different notification to Android, iOS, and Windows users.

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "where": {
          "deviceType": "android"
        },
        "data": {
          "alert": "Your suitcase has been filled with tiny robots!"
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/push
```

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "where": {
          "deviceType": "ios"
        },
        "data": {
          "alert": "Your suitcase has been filled with tiny apples!"
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/push
```

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "where": {
          "deviceType": "winrt"
        },
        "data": {
          "alert": "Your suitcase has been filled with tiny glass!"
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/push
```

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "where": {
          "deviceType": "winphone"
        },
        "data": {
          "alert": "Your suitcase is very hip; very metro."
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/push
```

[](https://docs.parseplatform.org/rest/guide/#scheduling-pushes)Scheduling Pushes
---------------------------------------------------------------------------------

You can schedule a push in advance by specifying a `push_time`. For example, if a user schedules a game reminder for a game on March 19th, 2015 at noon UTC, you can schedule the push notification by sending:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "where": {
          "user_id": "user_123"
        },
        "push_time": "2015-03-19T12:00:00Z",
        "data": {
          "alert": "You previously created a reminder for the game today"
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/push
```

If you also specify an `expiration_interval`, it will be calculated from the scheduled push time, not from the time the push is submitted. This means a push scheduled to be sent in a week with an expiration interval of a day will expire 8 days after the request is sent.

The scheduled time cannot be in the past, and can be up to two weeks in the future. It can be an ISO 8601 date with a date, time, and timezone, as in the example above, or it can be a numeric value representing a UNIX epoch time in seconds (UTC). To schedule an alert for 08/22/2015 at noon UTC time, you can set the `push_time` to either `2015-08-022T12:00:00.000Z` or `1440226800000`.

### [](https://docs.parseplatform.org/rest/guide/#local-push-scheduling)Local Push Scheduling

The `push_time` parameter can schedule a push to be delivered to each device according to its time zone. This technique delivers a push to all `Installation` objects with a `timeZone` member when that time zone would match the push time. For example, if an app had a device in timezone `America/New_York` and another in `America/Los_Angeles`, the first would receive the push three hours before the latter.

To schedule a push according to each device’s local time, the `push_time` parameter should be an ISO 8601 date without a time zone, i.e. `2015-03-19T12:00:00`. Note that Installations without a `timeZone` will be excluded from this localized push.

[](https://docs.parseplatform.org/rest/guide/#localizing-push)Localizing Push
-----------------------------------------------------------------------------

Starting parse-server version 2.6.1, it is possible to localize the push notifications messages according to the _Installation’s `localeIdentifier`.

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "data": {
          "alert": "The default alert for all languages",
          "alert-fr": "Une alerte en français"
        }
      }' \
  https://api.parse.com/1/push
```

When setting the `alert-[lang|locale]` in the data, parse-server will find all installations that have that language or locale set. The language is usually the first part of the locale. This will have no impact on the query planning, as the localizations will be resolved just before the push is sent.

If a custom localization is found, the `alert` value is replaced by the provided alert and all the localized keys are stripped out of the `data` part of the body.

[](https://docs.parseplatform.org/rest/guide/#config)Config
-----------------------------------------------------------

`Parse Config` is a way to configure your applications remotely by storing a single configuration object on Parse. It enables you to add things like feature gating or a simple “Message of the day”. To start using `Parse Config` you need to add a few key/value pairs (parameters) to your app on the Parse Config Dashboard.

![Image 2](https://docs.parseplatform.org/assets/images/config_editor.png)

After that you will be able to fetch the config on the client by sending a `GET` request to config URL. Here is a simple example that will fetch the `Parse.Config`:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  https://YOUR.PARSE-SERVER.HERE/parse/config
```

The response body is a JSON object containing all the configuration parameters in the `params` field.

```
{
  "params": {
    "welcomeMessage": "Welcome to The Internet!",
    "winningNumber": 42
  }
}
```

You can also update the config by sending a `PUT` request to config URL. Here is a simple example that will update the `Parse.Config` (requires `masterKey`):

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -d "{\"params\":{\"winningNumber\":43}}"
  https://YOUR.PARSE-SERVER.HERE/parse/config
```

```
var request = require('request');
return request({
  method: 'PUT',
  url: Parse.serverURL + '/config',
  headers: {
    'X-Parse-Application-Id': Parse.applicationId,
    'X-Parse-Master-Key': Parse.masterKey
  },
  json: true,
  body: {
    params: { winningNumber: 43 }
  }
})
```

The response body is a JSON object containing a simple boolean value in the `result` field.

```
{
  "result": true
}
```

If you want to make any changes to configs without sending the `masterkey`, you will need to create a Cloud Function that makes those changes.

[](https://docs.parseplatform.org/rest/guide/#analytics)Analytics
-----------------------------------------------------------------

Parse provides a number of hooks for you to get a glimpse into the ticking heart of your app. We understand that it’s important to understand what your app is doing, how frequently, and when.

While this section will cover different ways to instrument your app to best take advantage of Parse’s analytics backend, developers using Parse to store and retrieve data can already take advantage of metrics on Parse.

Without having to implement any client-side logic, you can view real-time graphs and breakdowns (by device type, Parse class name, or REST verb) of your API Requests in your app’s dashboard and save these graph filters to quickly access just the data you’re interested in.

The current server time will be used for all analytics requests. To explicitly set the time associated with a given event, an optional `at` parameter can be provided in ISO 8601 format.

```
-d '{
    "at": {
      "__type": "Date",
      "iso": "2015-03-01T15:59:11-07:00"
    }
  }'
```

[](https://docs.parseplatform.org/rest/guide/#app-open-analytics)App-Open Analytics
-----------------------------------------------------------------------------------

Our analytics hook allows you to track your application being launched. By making a POST request to our REST API, you’ll begin to collect data on when and how often your application is opened.

In the example below, the `at` parameter is optional. If omitted, the current server time will be used instead.

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/events/AppOpened
```

Graphs and breakdowns of your statistics are accessible from your app’s Dashboard.

[](https://docs.parseplatform.org/rest/guide/#custom-analytics)Custom Analytics
-------------------------------------------------------------------------------

Parse Analytics also allows you to track free-form events, with a handful of string keys and values. These extra dimensions allow segmentation of your custom events via your app’s Dashboard.

Say your app offers search functionality for apartment listings, and you want to track how often the feature is used, with some additional metadata.

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "dimensions": {
          "priceRange": "1000-1500",
          "source": "craigslist",
          "dayType": "weekday"
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/events/Search
```

Parse Analytics can even be used as a lightweight error tracker — simply invoke the following and you’ll have access to an overview of the rate and frequency of errors, broken down by error code, in your application:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
        "dimensions": {
          "code": "404"
        }
      }' \
  https://YOUR.PARSE-SERVER.HERE/parse/events/Error
```

Note that Parse currently only stores the first eight dimension pairs per call to `/parse/events/<eventName>`.

[](https://docs.parseplatform.org/rest/guide/#cloud-code)Cloud Code
-------------------------------------------------------------------

[](https://docs.parseplatform.org/rest/guide/#calling-cloud-functions)Calling Cloud Functions
---------------------------------------------------------------------------------------------

Cloud Functions can be called using the REST API. For example, to call the Cloud Function named `hello`:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-REST-API-Key: ${REST_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{}' \
  https://YOUR.PARSE-SERVER.HERE/parse/functions/hello
```

[](https://docs.parseplatform.org/rest/guide/#triggering-background-jobs)Triggering Background Jobs
---------------------------------------------------------------------------------------------------

Similarly, you can trigger a background job from the REST API. For example, to trigger the job named `userMigration`:

Take a look at the [Cloud Code Guide](https://docs.parseplatform.org/cloudcode/guide/#cloud-functions) to learn more about Cloud Functions and Background Jobs.

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"plan":"paid"}' \
  https://YOUR.PARSE-SERVER.HERE/parse/jobs/userMigration
```

[](https://docs.parseplatform.org/rest/guide/#schema)Schema
-----------------------------------------------------------

Schema is the structure representing classes in your app. You can use the schema of an app to verify operations in a unit test, generate test data, generate test classes and then clean up after tests. The schema API can also be used to create custom views of your data. We use the schema API to display columns names and types in the databrowser.

This API allows you to access the schemas of your app. Note: This API can be only accessed using the `master key`.

*   Starting with Parse Server 2.7.1 Index support added.

[](https://docs.parseplatform.org/rest/guide/#fetch-the-schema)Fetch the schema
-------------------------------------------------------------------------------

To fetch the Schema for all the classes of your app, run:

Note: `createdAt` and `updatedAt` are of type `Date` but they are represented as strings in object representation. This is a special case for the Parse API.

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  https://YOUR.PARSE-SERVER.HERE/parse/schemas
```

The response body is JSON containing all the schema information of the app.

```
{
  "results": [
    {
      "className": "Game",
      "fields": {
        "ACL": {
          "type": "ACL"
        },
        "createdAt": {
          "type": "Date"
        },
        "objectId": {
          "type": "String"
        },
        "name": {
          "type": "String"
        },
        "score": {
          "type": "Number"
        },
        "updatedAt": {
          "type": "Date"
        }
      }
    },
    /*...*/
  ]
}
```

To fetch schema of a single class, run:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  https://YOUR.PARSE-SERVER.HERE/parse/schemas/Game
```

[](https://docs.parseplatform.org/rest/guide/#adding-a-schema)Adding a schema
-----------------------------------------------------------------------------

When you add a new schema to your app, it creates an empty class with the provided fields and some default fields applicable to the class. To add the schema, run:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  -d '
    {
      "className": "City",
      "fields": {
        "name": {
          "type": "String"
        }
      }
    }' \
  https://YOUR.PARSE-SERVER.HERE/parse/schemas/City
```

You may also add indexes to your fields. You need to use the format you need to use `{"index_name" : { field_name: index } }`. The fields must exist when you add indexes.

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  -d '
    {
      "className": "City",
      "fields": {
        "name": {
          "type": "String"
        }
      },
      "indexes": {
        "indexName": {
          "name": 1
        }
      }
    }' \
  https://YOUR.PARSE-SERVER.HERE/parse/schemas/City
```

[](https://docs.parseplatform.org/rest/guide/#modifying-the-schema)Modifying the schema
---------------------------------------------------------------------------------------

You can add or delete columns to a schema. To do so, run:

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  -d '
    {
      "className": "City",
      "fields": {
        "population": {
          "type": "Number"
        }
      },
      "indexes": {
        "population_index": {
          "population": 1
        }
      }
    }' \
  https://YOUR.PARSE-SERVER.HERE/parse/schemas/City
```

To delete a particular field or index, you need to use `{"__op" : "Delete" }`

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  -d '
    {
      "className": "City",
      "fields": {
        "population": {
          "__op": "Delete"
        }
      },
      "indexes": {
        "population_index": {
          "__op": "Delete"
        }
      }
    }' \
  https://YOUR.PARSE-SERVER.HERE/parse/schemas/City
```

[](https://docs.parseplatform.org/rest/guide/#removing-a-schema)Removing a schema
---------------------------------------------------------------------------------

You can only remove a schema from your app if it is empty (has 0 objects). To do that, run:

```
curl -X DELETE\
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  https://YOUR.PARSE-SERVER.HERE/parse/schemas/City
```

[](https://docs.parseplatform.org/rest/guide/#hooks)Hooks
---------------------------------------------------------

You can create, update, list or delete all your cloud code webhooks via the Hooks API, in addition to being able to do so through the parse website.

Hooks API requires the users to provide `Application-Id` and `Master-Key` in the request headers.

There are two kinds of cloud code webhooks: function webhooks and trigger webhooks.

Cloud functions are functions that run in the cloud and allow you to build functions common to all platforms. For more details please read [cloud code functions](https://docs.parseplatform.org/cloudcode/guide/#cloud-functions).

Cloud triggers are invoked whenever you save or delete a parse object. Triggers are commonly used to validate your objects before saving them. For more details please read [cloud code triggers](https://docs.parseplatform.org/cloudcode/guide/#beforesave-triggers).

Lets establish some basic terminology used throughout the rest of this section.

`Cloud Code Webhooks` consist of `function webhooks` and `trigger webhooks`. This is code that runs on your servers.

`Cloud Code` has `cloud code functions` and `cloud code triggers`. This is code that runs on the Parse servers.

These are the generic concepts encapsulating both use cases:

`Cloud Function` is either a `cloud code function` or a `function webhook`. `Cloud Trigger` is either a `cloud code trigger` or a `trigger webhook`.

A function webhook has a name and a url. Hence, its JSON response looks like:

```
{"functionName": "foo", "url": "https://api.example.com/foo"}
```

JSON reponse for a cloud code function just contains the function name.

```
{"functionName": "foo"}
```

A trigger webhook belongs to a class, has a trigger name and a url. Hence, its JSON response looks like:

```
{"className": "score", "triggerName": "beforeSave", "url": "https://api.example.com/score/beforeSave"}
```

JSON response for a cloud code trigger contains the class name and the trigger name.

```
{"className": "score", "triggerName": "beforeSave"}
```

Note that trigger name can only be one of `beforeSave`, `afterSave`, `beforeDelete` and `afterDelete`.

[](https://docs.parseplatform.org/rest/guide/#fetch-functions)Fetch functions
-----------------------------------------------------------------------------

To fetch the list of all cloud functions you deployed or created, use:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  https://YOUR.PARSE-SERVER.HERE/parse/hooks/functions
```

The output is a json object with one key: “results” whose value is a list of cloud functions.

```
{
  "results": [
    { "functionName": "sendMessage", "url": "https://api.example.com/sendMessage" },
    { "functionName": "sendMessage" },
    { "functionName": "foo", "url": "https://api.example.com/foo" },
    { "functionName": "bar" }
  ]
}
```

To fetch a single cloud function with a given name, use:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  https://YOUR.PARSE-SERVER.HERE/parse/hooks/functions/sendMessage
```

The output is a json object with one key: “results” whose value is a list of cloud functions with the given name.

```
{
  "results": [
    { "functionName": "sendMessage", "url": "https://api.example.com/sendMessage" },
    { "functionName": "sendMessage" }
  ]
}
```

[](https://docs.parseplatform.org/rest/guide/#fetch-triggers)Fetch triggers
---------------------------------------------------------------------------

To fetch the list of all cloud triggers you deployed or created, use:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  https://YOUR.PARSE-SERVER.HERE/parse/hooks/triggers
```

The output is a json object with one key: “results” whose value is a list of cloud triggers.

```
{
  "results": [
    { "className": "Scores", "triggerName": "beforeSave" },
    {
      "className": "Scores",
      "triggerName": "beforeSave",
      "url": "https://api.example.com/Scores/beforeSave"
    },
    {
      "className": "Game",
      "triggerName": "afterSave",
      "url": "https://api.example.com/Game/afterSave"
    },
    { "className": "Tournament", "triggerName": "beforeDelete" }
  ]
}
```

To fetch a single cloud trigger, use:

```
curl -X GET \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  https://YOUR.PARSE-SERVER.HERE/parse/hooks/triggers/Scores/beforeSave
```

The path looks like `/hooks/triggers/className/triggerName` where `triggerName` can be one of `beforeSave`, `afterSave`, `beforeDelete`, `afterDelete`.

The output may look like this:

```
{
  "results": [
    { "className": "Scores", "triggerName": "beforeSave" },
    {
      "className": "Scores",
      "triggerName": "beforeSave",
      "url": "https://api.example.com/Scores/beforeSave"
    }
  ]
}
```

The output is a json object with one key: “results” whose value is a list of all cloud triggers with given name for a given class.

Note that POST, PUT and DELETE only work on function or trigger webhooks. To create cloud code functions or cloud code triggers you can modify your cloud code javascript files and perform a `parse deploy` the usual way.

[](https://docs.parseplatform.org/rest/guide/#create-function-webhook)Create function webhook
---------------------------------------------------------------------------------------------

To create a new function webhook post to `/parse/hooks/functions` with payload in the format

```
{
  "functionName": "foo", 
  "url": "https://api.example.com/foo"
}
```

Post example:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"functionName":"baz","url":"https://api.example.com/baz"}' \
  https://YOUR.PARSE-SERVER.HERE/parse/hooks/functions
```

The output may look like this:

```
{"functionName": "baz", "url": "https://api.example.com/baz"}'
```

It returns the function name and url of the created webhook.

If you try to create a function webhook and a cloud code function with the same name already exists, upon successful creation the response json has an additional `warning` field informing about the name conflict. Note that, function webhooks takes precedence over cloud code functions.

For example:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"functionName":"bar","url":"https://api.example.com/bar"}' \
  https://YOUR.PARSE-SERVER.HERE/parse/hooks/functions
```

The output may look like this:

```
{
  "functionName": "bar",
  "url": "https://api.example.com/bar",
  "warning": "a cloudcode function with name: bar already exists"
}
```

[](https://docs.parseplatform.org/rest/guide/#create-trigger-webhook)Create trigger webhook
-------------------------------------------------------------------------------------------

To create a new function webhook post to `/parse/hooks/triggers` with payload in the format:

```
{"className": x, "triggerName": y, "url": z}
```

Post example:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"className": "Game", "triggerName": "beforeSave", "url": "https://api.example.com/Game/beforeSave"}' \
https://YOUR.PARSE-SERVER.HERE/parse/hooks/triggers
```

The output may look like this:

```
{
  "className": "Game",
  "triggerName": "beforeSave",
  "url": "https://api.example.com/Game/beforeSave"
}
```

It returns the class name, trigger name and url of the created trigger webhook.

If you try to create a trigger webhook and a cloud code trigger with the same name already exists, upon successful creation the response json has an additional `warning` field informing about the name conflict. Note that, trigger webhooks takes precedence over cloud code triggers.

For example:

```
curl -X POST \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"className": "Tournament", "triggerName": "beforeDelete", "url": "https://api.example.com/Scores/beforeDelete"}' \
https://YOUR.PARSE-SERVER.HERE/parse/hooks/triggers
```

The output may look like this:

```
{
  "className": "Tournament",
  "triggerName": "beforeDelete",
  "url": "https://api.example.com/Tournament/beforeDelete",
  "warning": "beforeDelete trigger already defined for class Tournament in cloud code"
}
```

[](https://docs.parseplatform.org/rest/guide/#edit-function-webhook)Edit function webhook
-----------------------------------------------------------------------------------------

To edit the url of a function webhook that was already created use the put method.

Put example:

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"url":"https://api.example.com/_baz"}' \
  https://YOUR.PARSE-SERVER.HERE/parse/hooks/functions/baz
```

The output may look like this:

```
{"functionName": "baz", "url": "https://api.example.com/baz"}'
```

It returns the function name and url of the modified webhook.

If you try to update a function webhook and a cloud code function with the same name already exists, upon successful update the response json has an additional `warning` field informing about the name conflict. Note that, function webhooks takes precedence over cloud code functions.

For example:

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"url":"https://api.example.com/_bar"}' \
  https://YOUR.PARSE-SERVER.HERE/parse/hooks/functions/bar
```

The output may look like this:

```
{
  "functionName": "bar",
  "url": "https://api.example.com/_bar",
  "warning": "a cloudcode function with name: bar already exists"
}
```

[](https://docs.parseplatform.org/rest/guide/#edit-trigger-webhook)Edit trigger webhook
---------------------------------------------------------------------------------------

To edit the url of a trigger webhook that was already crated use the put method.

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://api.example.com/Game/_beforeSave"}' \
https://YOUR.PARSE-SERVER.HERE/parse/hooks/triggers/Game/beforeSave
```

The output may look like this:

```
{
  "className": "Game",
  "triggerName": "beforeSave",
  "url": "https://api.example.com/Game/_beforeSave"
}
```

It returns the class name, trigger name and url of the modified trigger webhook.

If you try to update a trigger webhook and a cloud code trigger with the same name already exists, upon successful update the response json has an additional `warning` field informing about the name conflict. Note that, trigger webhooks takes precedence over cloud code triggers.

For example:

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://api.example.com/Scores/beforeDelete"}' \
https://YOUR.PARSE-SERVER.HERE/parse/hooks/triggers/Tournament/beforeDelete
```

The output may look like this:

```
{
  "className": "Tournament",
  "triggerName": "beforeDelete",
  "url": "https://api.example.com/Tournament/beforeDelete",
  "warning": "beforeDelete trigger already defined for class Tournament in cloud code"
}
```

[](https://docs.parseplatform.org/rest/guide/#delete-function-webhook)Delete function webhook
---------------------------------------------------------------------------------------------

To delete a function webhook use the put method.

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"__op": "Delete"}' \
https://YOUR.PARSE-SERVER.HERE/parse/hooks/functions/foo
```

The output may look like this:

```
{}
```

If a cloud code function with the same name already exists then it is returned as the result. Since the overriding webhook was just deleted, this cloud code function will be run the next time sendMessage is called.

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  -d '{ "__op": "Delete" }' \
https://YOUR.PARSE-SERVER.HERE/parse/hooks/functions/sendMessage
```

The output may look like this:

```
{ "functionName": "sendMessage" }
```

[](https://docs.parseplatform.org/rest/guide/#delete-trigger-webhook)Delete trigger webhook
-------------------------------------------------------------------------------------------

To delete a trigger webhook use the put method.

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  -d '{ "__op": "Delete" }' \
https://YOUR.PARSE-SERVER.HERE/parse/hooks/triggers/Game/beforeSave
```

The output may look like this:

```
{}
```

If a cloud code trigger with the same name already exists then the it is returned as the result. Since the overriding webhook was just deleted, this cloud code trigger will be run the next time a Tournament object is saved.

```
curl -X PUT \
  -H "X-Parse-Application-Id: ${APPLICATION_ID}" \
  -H "X-Parse-Master-Key: ${MASTER_KEY}" \
  -H "Content-Type: application/json" \
  -d '{ "__op": "Delete" }' \
https://YOUR.PARSE-SERVER.HERE/parse/hooks/triggers/Tournament/beforeDelete
```

The output may look like this:

```
{
  "className": "Tournament",
  "triggerName": "beforeDelete"
}
```

[](https://docs.parseplatform.org/rest/guide/#security)Security
---------------------------------------------------------------

As your app development progresses, you will want to use Parse’s security features in order to safeguard data. This document explains the ways in which you can secure your apps.

If your app is compromised, it’s not only you as the developer who suffers, but potentially the users of your app as well. Continue reading for our suggestions for sensible defaults and precautions to take before releasing your app into the wild.

[](https://docs.parseplatform.org/rest/guide/#client-vs-server)Client vs. Server
--------------------------------------------------------------------------------

When an app first connects to Parse, it identifies itself with an Application ID and a Client key (or REST Key, or .NET Key, or JavaScript Key, depending on which platform you’re using). These are not secret and by themselves they do not secure an app. These keys are shipped as a part of your app, and anyone can decompile your app or proxy network traffic from their device to find your client key. This exploit is even easier with JavaScript — one can simply “view source” in the browser and immediately find your client key.

This is why Parse has many other security features to help you secure your data. The client key is given out to your users, so anything that can be done with just the client key is doable by the general public, even malicious hackers.

The master key, on the other hand, is definitely a security mechanism. Using the master key allows you to bypass all of your app’s security mechanisms, such as [class-level permissions](https://docs.parseplatform.org/rest/guide/#class-level-permissions) and [ACLs](https://docs.parseplatform.org/rest/guide/#object-level-access-control). Having the master key is like having root access to your app’s servers, and you should guard your master key with the same zeal with which you would guard your production machines’ root password.

The overall philosophy is to limit the power of your clients (using client keys), and to perform any sensitive actions requiring the master key in Cloud Code. You’ll learn how to best wield this power in the section titled [Implementing Business Logic in Cloud Code](https://docs.parseplatform.org/rest/guide/#implementing-business-logic-in-cloud-code).

A final note: It is recommended to setup HTTPS and SSL in your server, to avoid man-in-the-middle attacks, but Parse works fine as well with non-HTTPS connections.

[](https://docs.parseplatform.org/rest/guide/#class-level-permissions)Class-Level Permissions
---------------------------------------------------------------------------------------------

The second level of security is at the schema and data level. Enforcing security measures at this level will restrict how and when client applications can access and create data on Parse. When you first begin developing your Parse application, all of the defaults are set so that you can be a more productive developer. For example:

*   A client application can create new classes on Parse
*   A client application can add fields to classes
*   A client application can modify or query for objects on Parse

You can configure any of these permissions to apply to everyone, no one, or to specific users or roles in your app. Roles are groups that contain users or other roles, which you can assign to an object to restrict its use. Any permission granted to a role is also granted to any of its children, whether they are users or other roles, enabling you to create an access hierarchy for your apps. Each of [the Parse guides](https://docs.parseplatform.org/) includes a detailed description of employing Roles in your apps.

Once you are confident that you have the right classes and relationships between classes in your app, you should begin to lock it down by doing the following:

Almost every class that you create should have these permissions tweaked to some degree. For classes where every object has the same permissions, class-level settings will be most effective. For example, one common use case entails having a class of static data that can be read by anyone but written by no one.

### [](https://docs.parseplatform.org/rest/guide/#restricting-class-creation)Restricting class creation

As a start, you can configure your application so that clients cannot create new classes on Parse. This is done by setting the key `allowClientClassCreation` to `false` in your ParseServer configuration. See the project Readme for an overview of [Configuring your ParseServer](https://github.com/parse-community/parse-server#configuration). Once restricted, classes may only be created from the Data Browser or with a the `masterKey`. This will prevent attackers from filling your database with unlimited, arbitrary new classes.

### [](https://docs.parseplatform.org/rest/guide/#enforcing-private-users)Enforcing Private Users

_Requires Parse Server 5.0.0+_

By default, Parse Server creates Users with public read access. This allows other users, and un-authenticated users, to read data such as `email`. When moving to production, set the key `enforcePrivateUsers` to `true`, as this will remove the public read access to new users.

### [](https://docs.parseplatform.org/rest/guide/#configuring-class-level-permissions)Configuring Class-Level Permissions

Parse lets you specify what operations are allowed per class. This lets you restrict the ways in which clients can access or modify your classes. To change these settings, go to the Data Browser, select a class, and click the “Security” button.

You can configure the client’s ability to perform each of the following operations for the selected class:

*   **Read**:

    *   **Get**: With Get permission, users can fetch objects in this table if they know their objectIds.

    *   **Find**: Anyone with Find permission can query all of the objects in the table, even if they don’t know their objectIds. Any table with public Find permission will be completely readable by the public, unless you put an ACL on each object.

*   **Write**:

    *   **Update**: Anyone with Update permission can modify the fields of any object in the table that doesn’t have an ACL. For publicly readable data, such as game levels or assets, you should disable this permission.

    *   **Create**: Like Update, anyone with Create permission can create new objects of a class. As with the Update permission, you’ll probably want to turn this off for publicly readable data.

    *   **Delete**: With this permission, people can delete any object in the table that doesn’t have an ACL. All they need is its objectId.

*   **Add fields**: Parse classes have schemas that are inferred when objects are created. While you’re developing your app, this is great, because you can add a new field to your object without having to make any changes on the backend. But once you ship your app, it’s very rare to need to add new fields to your classes automatically. You should pretty much always turn off this permission for all of your classes when you submit your app to the public.

For each of the above actions, you can grant permission to all users (which is the default), or lock permissions down to a list of roles and users. For example, a class that should be available to all users would be set to read-only by only enabling get and find. A logging class could be set to write-only by only allowing creates. You could enable moderation of user-generated content by providing update and delete access to a particular set of users or roles.

[](https://docs.parseplatform.org/rest/guide/#object-level-access-control)Object-Level Access Control
-----------------------------------------------------------------------------------------------------

Once you’ve locked down your schema and class-level permissions, it’s time to think about how data is accessed by your users. Object-level access control enables one user’s data to be kept separate from another’s, because sometimes different objects in a class need to be accessible by different people. For example, a user’s private personal data should be accessible only to them.

Parse also supports the notion of anonymous users for those apps that want to store and protect user-specific data without requiring explicit login.

When a user logs into an app, they initiate a session with Parse. Through this session they can add and modify their own data but are prevented from modifying other users’ data.

### [](https://docs.parseplatform.org/rest/guide/#access-control-lists)Access Control Lists

The easiest way to control who can access which data is through access control lists, commonly known as ACLs. The idea behind an ACL is that each object has a list of users and roles along with what permissions that user or role has. A user needs read permissions (or must belong to a role that has read permissions) in order to retrieve an object’s data, and a user needs write permissions (or must belong to a role that has write permissions) in order to update or delete that object.

Once you have a User, you can start using ACLs. Remember: Users can be created through traditional username/password sign up, through a third-party login system like Facebook or Twitter, or even by using Parse’s [automatic anonymous users](https://docs.parseplatform.org/ios/guide/#anonymous-users) functionality. To set an ACL on the current user’s data to not be publicly readable, all you have to do is:

Most apps should do this. If you store any sensitive user data, such as email addresses or phone numbers, you need to set an ACL like this so that the user’s private information isn’t visible to other users. If an object doesn’t have an ACL, it’s readable and writeable by everyone. The only exception is the `_User` class. We never allow users to write each other’s data, but they can read it by default. (If you as the developer need to update other `_User` objects, remember that your master key can provide the power to do this.)

To make it super easy to create user-private ACLs for every object, we have a way to set a default ACL that will be used for every new object you create:

If you want the user to have some data that is public and some that is private, it’s best to have two separate objects. You can add a pointer to the private data from the public one.

Of course, you can set different read and write permissions on an object. For example, this is how you would create an ACL for a public post by a user, where anyone can read it:

Sometimes it’s inconvenient to manage permissions on a per-user basis, and you want to have groups of users who get treated the same (like a set of admins with special powers). Roles are a special kind of object that let you create a group of users that can all be assigned to the ACL. The best thing about roles is that you can add and remove users from a role without having to update every single object that is restricted to that role. To create an object that is writeable only by admins:

Of course, this snippet assumes you’ve already created a role named “admins”. This is often reasonable when you have a small set of special roles set up while developing your app. Roles can also be created and updated on the fly — for example, adding new friends to a “friendOf___” role after each connection is made.

All this is just the beginning. Applications can enforce all sorts of complex access patterns through ACLs and class-level permissions. For example:

*   For private data, read and write access can be restricted to the owner.
*   For a post on a message board, the author and members of the “Moderators” role can have “write” access, and the general public can have “read” access.
*   For logging data that will only be accessed by the developer through the REST API using the master key, the ACL can deny all permissions.
*   Data created by a privileged group of users or the developer, like a global message of the day, can have public read access but restrict write access to an “Administrators” role.
*   A message sent from one user to another can give “read” and “write” access just to those users.

For the curious, here’s the format for an ACL that restricts read and write permissions to the owner (whose `objectId` is identified by `"aSaMpLeUsErId"`) and enables other users to read the object:

```
{
    "*": { "read":true },
    "aSaMpLeUsErId": { "read" :true, "write": true }
}
```

And here’s another example of the format of an ACL that uses a Role:

```
{
    "role:RoleName": { "read": true },
    "aSaMpLeUsErId": { "read": true, "write": true }
}
```

### [](https://docs.parseplatform.org/rest/guide/#pointer-permissions)Pointer Permissions

Pointer permissions are a special type of class-level permission that create a virtual ACL on every object in a class, based on users stored in pointer fields on those objects. For example, given a class with an `owner` field, setting a read pointer permission on `owner` will make each object in the class only readable by the user in that object’s `owner` field. For a class with a `sender` and a `reciever` field, a read pointer permission on the `receiver` field and a read and write pointer permission on the `sender` field will make each object in the class readable by the user in the `sender` and `receiver` field, and writable only by the user in the `sender` field.

Given that objects often already have pointers to the user(s) that should have permissions on the object, pointer permissions provide a simple and fast solution for securing your app using data which is already there, that doesn’t require writing any client code or cloud code.

Pointer permissions are like virtual ACLs. They don’t appear in the ACL column, but if you are familiar with how ACLs work, you can think of them like ACLs. In the above example with the `sender` and `receiver`, each object will act as if it has an ACL of:

```
{
    "<SENDER_USER_ID>": {
        "read": true,
        "write": true
    },
    "<RECEIVER_USER_ID>": {
        "read": true
    }
}
```

Note that this ACL is not actually created on each object. Any existing ACLs will not be modified when you add or remove pointer permissions, and any user attempting to interact with an object can only interact with the object if both the virtual ACL created by the pointer permissions, and the real ACL already on the object allow the interaction. For this reason, it can sometimes be confusing to combine pointer permissions and ACLs, so we recommend using pointer permissions for classes that don’t have many ACLs set. Fortunately, it’s easy to remove pointer permissions if you later decide to use Cloud Code or ACLs to secure your app.

### [](https://docs.parseplatform.org/rest/guide/#requires-authentication-permission-requires-parse-server---230)Requires Authentication permission (requires parse-server >= 2.3.0)

Starting version 2.3.0, parse-server introduces a new Class Level Permission `requiresAuthentication`. This CLP prevents any non authenticated user from performing the action protected by the CLP.

For example, you want to allow your **authenticated users** to `find` and `get``Announcement`’s from your application and your **admin role** to have all privileged, you would set the CLP:

```
// POST http://my-parse-server.com/schemas/Announcement
// Set the X-Parse-Application-Id and X-Parse-Master-Key header
// body:
{
  classLevelPermissions:
  {
    "find": {
      "requiresAuthentication": true,
      "role:admin": true
    },
    "get": {
      "requiresAuthentication": true,
      "role:admin": true
    },
    "create": { "role:admin": true },
    "update": { "role:admin": true },
    "delete": { "role:admin": true }
  }
}
```

Effects:

*   Non authenticated users won’t be able to do anything.
*   Authenticated users (any user with a valid sessionToken) will be able to read all the objects in that class
*   Users belonging to the admin role, will be able to perform all operations.

:warning: Note that this is in no way securing your content, if you allow anyone to login to your server, every client will still be able to query this object.

### [](https://docs.parseplatform.org/rest/guide/#clp-and-acl-interaction)CLP and ACL interaction

Class-Level Permissions (CLPs) and Access Control Lists (ACLs) are both powerful tools for securing your app, but they don’t always interact exactly how you might expect. They actually represent two separate layers of security that each request has to pass through to return the correct information or make the intended change. These layers, one at the class level, and one at the object level, are shown below. A request must pass through BOTH layers of checks in order to be authorized. Note that despite acting similarly to ACLs, [Pointer Permissions](https://docs.parseplatform.org/rest/guide/#pointer-permissions) are a type of class level permission, so a request must pass the pointer permission check in order to pass the CLP check.

![Image 3: CLP vs ACL Diagram](https://docs.parseplatform.org/assets/images/clp_vs_acl_diagram.png)

As you can see, whether a user is authorized to make a request can become complicated when you use both CLPs and ACLs. Let’s look at an example to get a better sense of how CLPs and ACLs can interact. Say we have a `Photo` class, with an object, `photoObject`. There are 2 users in our app, `user1` and `user2`. Now lets say we set a Get CLP on the `Photo` class, disabling public Get, but allowing `user1` to perform Get. Now let’s also set an ACL on `photoObject` to allow Read - which includes GET - for only `user2`.

You may expect this will allow both `user1` and `user2` to Get `photoObject`, but because the CLP layer of authentication and the ACL layer are both in effect at all times, it actually makes it so _neither_`user1` nor `user2` can Get `photoObject`. If `user1` tries to Get `photoObject`, it will get through the CLP layer of authentication, but then will be rejected because it does not pass the ACL layer. In the same way, if `user2` tries to Get `photoObject`, it will also be rejected at the CLP layer of authentication.

Now lets look at example that uses Pointer Permissions. Say we have a `Post` class, with an object, `myPost`. There are 2 users in our app, `poster`, and `viewer`. Lets say we add a pointer permission that gives anyone in the `Creator` field of the `Post` class read and write access to the object, and for the `myPost` object, `poster` is the user in that field. There is also an ACL on the object that gives read access to `viewer`. You may expect that this will allow `poster` to read and edit `myPost`, and `viewer` to read it, but `viewer` will be rejected by the Pointer Permission, and `poster` will be rejected by the ACL, so again, neither user will be able to access the object.

Because of the complex interaction between CLPs, Pointer Permissions, and ACLs, we recommend being careful when using them together. Often it can be useful to use CLPs only to disable all permissions for a certain request type, and then using Pointer Permissions or ACLs for other request types. For example, you may want to disable Delete for a `Photo` class, but then put a Pointer Permission on `Photo` so the user who created it can edit it, just not delete it. Because of the especially complex way that Pointer Permissions and ACLs interact, we usually recommend only using one of those two types of security mechanisms.

### [](https://docs.parseplatform.org/rest/guide/#security-edge-cases)Security Edge Cases

There are some special classes in Parse that don’t follow all of the same security rules as every other class. Not all classes follow [Class-Level Permissions (CLPs)](https://docs.parseplatform.org/rest/guide/#class-level-permissions) or [Access Control Lists (ACLs)](https://docs.parseplatform.org/rest/guide/#object-level-access-control) exactly how they are defined, and here those exceptions are documented. Here “normal behavior” refers to CLPs and ACLs working normally, while any other special behaviors are described in the footnotes.

|  | `_User` | `_Installation` |
| --- | --- | --- |
| Get | normal behaviour [1, 2, 3] | ignores CLP, but not ACL |
| Find | normal behavior [3] | master key only [6] |
| Create | normal behavior [4] | ignores CLP |
| Update | normal behavior [5] | ignores CLP, but not ACL [7] |
| Delete | normal behavior [5] | master key only [7] |
| Add Field | normal behavior | normal behavior |

1.   Logging in, or `/parse/login` in the REST API, does not respect the Get CLP on the user class. Login works just based on username and password, and cannot be disabled using CLPs.

2.   Retrieving the current user, or becoming a User based on a session token, which are both `/parse/users/me` in the REST API, do not respect the Get CLP on the user class.

3.   Read ACLs do not apply to the logged in user. For example, if all users have ACLs with Read disabled, then doing a find query over users will still return the logged in user. However, if the Find CLP is disabled, then trying to perform a find on users will still return an error.

4.   Create CLPs also apply to signing up. So disabling Create CLPs on the user class also disables people from signing up without the master key.

5.   Users can only Update and Delete themselves. Public CLPs for Update and Delete may still apply. For example, if you disable public Update for the user class, then users cannot edit themselves. But no matter what the write ACL on a user is, that user can still Update or Delete itself, and no other user can Update or Delete that user. As always, however, using the master key allows users to update other users, independent of CLPs or ACLs.

6.   Get requests on installations follow ACLs normally. Find requests without master key is not allowed unless you supply the `installationId` as a constraint.

7.   Update requests on installations do adhere to the ACL defined on the installation, but Delete requests are master-key-only. For more information about how installations work, check out the [installations section of the REST guide](https://docs.parseplatform.org/rest/guide/#installations).

[](https://docs.parseplatform.org/rest/guide/#data-integrity-in-cloud-code)Data Integrity in Cloud Code
-------------------------------------------------------------------------------------------------------

For most apps, care around keys, class-level permissions, and object-level ACLs are all you need to keep your app and your users’ data safe. Sometimes, though, you’ll run into an edge case where they aren’t quite enough. For everything else, there’s [Cloud Code](https://docs.parseplatform.org/cloudcode/guide/).

Cloud Code allows you to upload JavaScript to Parse’s servers, where we will run it for you. Unlike client code running on users’ devices that may have been tampered with, Cloud Code is guaranteed to be the code that you’ve written, so it can be trusted with more responsibility.

One particularly common use case for Cloud Code is preventing invalid data from being stored. For this sort of situation, it’s particularly important that a malicious client not be able to bypass the validation logic.

To create validation functions, Cloud Code allows you to implement a `beforeSave` trigger for your class. These triggers are run whenever an object is saved, and allow you to modify the object or completely reject a save. For example, this is how you create a [Cloud Code beforeSave trigger](https://docs.parseplatform.org/cloudcode/guide/#beforesave-triggers) to make sure every user has an email address set:

```
Parse.Cloud.beforeSave(Parse.User, request => {
  const user = request.object;
  if (!user.get("email")) {
    throw "Every user must have an email address.";
  }
});
```

Validations can lock down your app so that only certain values are acceptable. You can also use `afterSave` validations to normalize your data (e.g. formatting all phone numbers or currency identically). You get to retain most of the productivity benefits of accessing Parse data directly from your client applications, but you can also enforce certain invariants for your data on the fly.

Common scenarios that warrant validation include:

*   Making sure phone numbers have the right format
*   Sanitizing data so that its format is normalized
*   Making sure that an email address looks like a real email address
*   Requiring that every user specifies an age within a particular range
*   Not letting users directly change a calculated field
*   Not letting users delete specific objects unless certain conditions are met

[](https://docs.parseplatform.org/rest/guide/#implementing-business-logic-in-cloud-code)Implementing Business Logic in Cloud Code
---------------------------------------------------------------------------------------------------------------------------------

While validation often makes sense in Cloud Code, there are likely certain actions that are particularly sensitive, and should be as carefully guarded as possible. In these cases, you can remove permissions or the logic from clients entirely and instead funnel all such operations to Cloud Code functions.

When a Cloud Code function is called, it can use the optional `{useMasterKey:true}` parameter to gain the ability to modify user data. With the master key, your Cloud Code function can override any ACLs and write data. This means that it’ll bypass all the security mechanisms you’ve put in place in the previous sections.

Say you want to allow a user to “like” a `Post` object without giving them full write permissions on the object. You can do this by having the client call a Cloud Code function instead of modifying the Post itself:

The master key should be used carefully. setting `useMasterKey` to `true` only in the individual API function calls that need that security override:

```
Parse.Cloud.define("like", async request => {
  var post = new Parse.Object("Post");
  post.id = request.params.postId;
  post.increment("likes");
  await post.save(null, { useMasterKey: true })
});
```

One very common use case for Cloud Code is sending push notifications to particular users. In general, clients can’t be trusted to send push notifications directly, because they could modify the alert text, or push to people they shouldn’t be able to. Your app’s settings will allow you to set whether “client push” is enabled or not; we recommend that you make sure it’s disabled. Instead, you should write Cloud Code functions that validate the data to be pushed and sent before sending a push.

[](https://docs.parseplatform.org/rest/guide/#rate-limiting)Rate Limiting
-------------------------------------------------------------------------

*   Available on Parse Server >=6.0.0 *

It’s important to restrict how often a client can call the Parse Server API. This prevents malicious attacks that could:

*   overwhelm server resources by exceeding expected API traffic
*   collect large amounts of data (“data scraping”)
*   repeatedly guess passwords, object IDs, installation IDs or other data (“brute force”)

Parse Sever offers a mechanism to enforce rate limits by setting the Parse Server option `rateLimit`, or by specifying a `rateLimit` object on a Cloud Function validator.

The valid options for a rate limit are:

*   `requestPath`: The path of the API route to be rate limited.
*   `requestMethods`: Optional, the HTTP request methods to be rate limited.
*   `requestTimeWindow`: The window of time in milliseconds within which the number of requests set in `requestCount` can be made before the rate limit is applied.
*   `requestCount`: The number of requests that can be made per IP address within the time window set in `requestTimeWindow` before the rate limit is applied.
*   `errorResponseMessage`: The error message that should be returned in the body of the HTTP 429 response when the rate limit is hit. Default is `Too many requests.`.
*   `includeInternalRequests`: Optional, whether the rate limit will also apply to requests that are made in by Cloud Code.
*   `includeMasterKey`: Optional, whether the rate limit will also apply to requests using the `masterKey`
*   `redisUrl` Optional, the URL of the Redis server to store rate limit data.

To specify a server-wide rate limit of 200 requests per 15 minute window:

```
const parseServer = new ParseServer({
  rateLimit: {
    requestPath: '*',
    requestTimeWindow: 15 * 60 * 1000,
    requestCount: 200,
  },
});
```

To specify a cloud function specific rate limit of 3 request per hour:

```
Parse.Cloud.define('someFunction', () => {
  return 'Hello world';
}, {
  rateLimit: {
    requestTimeWindow: 60 * 60 * 1000,
    requestCount: 3,
  }
});
```

Rate limits can also be applied to `beforeSave` triggers to restrict how often a given class is written to:

```
Parse.Cloud.beforeSave('TestObject', () => {}, {
  rateLimit: {
    requestTimeWindow: 1 * 60 * 1000 // one write per minute,,
    requestCount: 1,
    errorResponseMessage: 'Too many requests!',
  },
});
```

> ⚠️ Rate limits should be enforced as far away from Parse Server as possible to mitigate possible impacts on resource costs, availability and integrity. While Parse Server offers a rate limiting mechanism as a conveniently available security feature without requiring a deep level of expertise, it is _not considered best practice_ to enforce rate limits only after requests already reached the server. For better protection we advice to examine your network architecture an consider enforcing rate limits on the outer edge of the cloud if using a content delivery network, or at least before requests reach the server resource. Consult your cloud service provider for recommended rate limit and firewall solutions for your resources.

[](https://docs.parseplatform.org/rest/guide/#parse-security-summary)Parse Security Summary
-------------------------------------------------------------------------------------------

Parse provides a number of ways for you to secure data in your app. As you build your app and evaluate the kinds of data you will be storing, you can make the decision about which implementation to choose.

It is worth repeating that that the Parse User object is readable by all other users by default. You will want to set the ACL on your User object accordingly if you wish to prevent data contained in the User object (for example, the user’s email address) from being visible by other users.

Most classes in your app will fall into one of a couple of easy-to-secure categories. For fully public data, you can use class-level permissions to lock down the table to put publicly readable and writeable by no one. For fully private data, you can use ACLs to make sure that only the user who owns the data can read it. But occasionally, you’ll run into situations where you don’t want data that’s fully public or fully private. For example, you may have a social app, where you have data for a user that should be readable only to friends whom they’ve approved. For this you’ll need to a combination of the techniques discussed in this guide to enable exactly the sharing rules you desire.

We hope that you’ll use these tools to do everything you can to keep your app’s data and your users’ data secure. Together, we can make the web a safer place.

[](https://docs.parseplatform.org/rest/guide/#error-codes)Error Codes
---------------------------------------------------------------------

The following is a list of all the error codes that can be returned by the Parse API. You may also refer to [RFC2616](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) for a list of http error codes. Make sure to check the error message for more details.

[](https://docs.parseplatform.org/rest/guide/#api-issues)API Issues
-------------------------------------------------------------------

| Name | Code | Description |
| --- | --- | --- |
| `UserInvalidLoginParams` | 101 | Invalid login parameters. Check error message for more details. |
| `ObjectNotFound` | 101 | The specified object or session doesn’t exist or could not be found. Can also indicate that you do not have the necessary permissions to read or write this object. Check error message for more details. |
| `InvalidQuery` | 102 | There is a problem with the parameters used to construct this query. This could be an invalid field name or an invalid field type for a specific constraint. Check error message for more details. |
| `InvalidClassName` | 103 | Missing or invalid classname. Classnames are case-sensitive. They must start with a letter, and a-zA-Z0-9_ are the only valid characters. |
| `MissingObjectId` | 104 | An unspecified object id. |
| `InvalidFieldName` | 105 | An invalid field name. Keys are case-sensitive. They must start with a letter, and a-zA-Z0-9_ are the only valid characters. Some field names may be reserved. Check error message for more details. |
| `InvalidPointer` | 106 | A malformed pointer was used. You would typically only see this if you have modified a client SDK. |
| `InvalidJSON` | 107 | Badly formed JSON was received upstream. This either indicates you have done something unusual with modifying how things encode to JSON, or the network is failing badly. Can also indicate an invalid utf-8 string or use of multiple form encoded values. Check error message for more details. |
| `CommandUnavailable` | 108 | The feature you tried to access is only available internally for testing purposes. |
| `NotInitialized` | 109 | You must call Parse.initialize before using the Parse library. Check the Quick Start guide for your platform. |
| `ObjectTooLarge` | 116 | The object is too large. |
| `ExceededConfigParamsError` | 116 | You have reached the limit of 100 config parameters. |
| `InvalidLimitError` | 117 | An invalid value was set for the limit. Check error message for more details. |
| `InvalidSkipError` | 118 | An invalid value was set for skip. Check error message for more details. |
| `OperationForbidden` | 119 | The operation isn’t allowed for clients due to class-level permissions. Check error message for more details. |
| `CacheMiss` | 120 | The result was not found in the cache. |
| `InvalidNestedKey` | 121 | An invalid key was used in a nested JSONObject. Check error message for more details. |
| `InvalidACL` | 123 | An invalid ACL was provided. |
| `InvalidEmailAddress` | 125 | The email address was invalid. |
| `DuplicateValue` | 137 | Unique field was given a value that is already taken. |
| `InvalidRoleName` | 139 | Role’s name is invalid. |
| `ReservedValue` | 139 | Field value is reserved. |
| `ExceededCollectionQuota` | 140 | You have reached the quota on the number of classes in your app. Please delete some classes if you need to add a new class. |
| `ScriptFailed` | 141 | Cloud Code script failed. Usually points to a JavaScript error. Check error message for more details. |
| `FunctionNotFound` | 141 | Cloud function not found. Check that the specified Cloud function is present in your Cloud Code script and has been deployed. |
| `JobNotFound` | 141 | Background job not found. Check that the specified job is present in your Cloud Code script and has been deployed. |
| `ValidationFailed` | 142 | Cloud Code validation failed. |
| `WebhookError` | 143 | Webhook error. |
| `InvalidImageData` | 150 | Invalid image data. |
| `UnsavedFileError` | 151 | An unsaved file. |
| `InvalidPushTimeError` | 152 | An invalid push time was specified. |
| `HostingError` | 158 | Hosting error. |
| `InvalidEventName` | 160 | The provided analytics event name is invalid. |
| `ClassNotEmpty` | 255 | Class is not empty and cannot be dropped. |
| `AppNameInvalid` | 256 | App name is invalid. |
| `MissingAPIKeyError` | 902 | The request is missing an API key. |
| `InvalidAPIKeyError` | 903 | The request is using an invalid API key. |

| Name | Code | Description |
| --- | --- | --- |
| `IncorrectType` | 111 | A field was set to an inconsistent type. Check error message for more details. |
| `InvalidChannelName` | 112 | Invalid channel name. A channel name is either an empty string (the broadcast channel) or contains only a-zA-Z0-9_ characters and starts with a letter. |
| `InvalidSubscriptionType` | 113 | Bad subscription type. Check error message for more details. |
| `InvalidDeviceToken` | 114 | The provided device token is invalid. |
| `PushMisconfigured` | 115 | Push is misconfigured in your app. Check error message for more details. |
| `PushWhereAndChannels` | 115 | Can’t set channels for a query-targeted push. You can fix this by moving the channels into your push query constraints. |
| `PushWhereAndType` | 115 | Can’t set device type for a query-targeted push. You can fix this by incorporating the device type constraints into your push query. |
| `PushMissingData` | 115 | Push is missing a ‘data’ field. |
| `PushMissingChannels` | 115 | Non-query push is missing a ‘channels’ field. Fix by passing a ‘channels’ or ‘query’ field. |
| `ClientPushDisabled` | 115 | Client-initiated push is not enabled. Check your Parse app’s push notification settings. |
| `RestPushDisabled` | 115 | REST-initiated push is not enabled. Check your Parse app’s push notification settings. |
| `ClientPushWithURI` | 115 | Client-initiated push cannot use the “uri” option. |
| `PushQueryOrPayloadTooLarge` | 115 | Your push query or data payload is too large. Check error message for more details. |
| `InvalidExpirationError` | 138 | Invalid expiration value. |
| `MissingPushIdError` | 156 | A push id is missing. Deprecated. |
| `MissingDeviceTypeError` | 157 | The device type field is missing. Deprecated. |

| Name | Code | Description |
| --- | --- | --- |
| `InvalidFileName` | 122 | An invalid filename was used for Parse File. A valid file name contains only a-zA-Z0-9_. characters and is between 1 and 128 characters. |
| `MissingContentType` | 126 | Missing content type. |
| `MissingContentLength` | 127 | Missing content length. |
| `InvalidContentLength` | 128 | Invalid content length. |
| `FileTooLarge` | 129 | File size exceeds maximum allowed. |
| `FileSaveError` | 130 | Error saving a file. |
| `FileDeleteError` | 153 | File could not be deleted. |
| `FileDeleteUnnamedError` | 161 | Unnamed file could not be deleted. |

| Name | Code | Description |
| --- | --- | --- |
| `InvalidInstallationIdError` | 132 | Invalid installation id. |
| `InvalidDeviceTypeError` | 133 | Invalid device type. |
| `InvalidChannelsArrayError` | 134 | Invalid channels array value. |
| `MissingRequiredFieldError` | 135 | Required field is missing. |
| `ChangedImmutableFieldError` | 136 | An immutable field was changed. |

| Name | Code | Description |
| --- | --- | --- |
| `ReceiptMissing` | 143 | Product purchase receipt is missing. |
| `InvalidPurchaseReceipt` | 144 | Product purchase receipt is invalid. |
| `PaymentDisabled` | 145 | Payment is disabled on this device. |
| `InvalidProductIdentifier` | 146 | The product identifier is invalid. |
| `ProductNotFoundInAppStore` | 147 | The product is not found in the App Store. |
| `InvalidServerResponse` | 148 | The Apple server response is not valid. |
| `ProductDownloadFilesystemError` | 149 | The product fails to download due to file system error. |

| Name | Code | Description |
| --- | --- | --- |
| `UsernameMissing` | 200 | The username is missing or empty. |
| `PasswordMissing` | 201 | The password is missing or empty. |
| `UsernameTaken` | 202 | The username has already been taken. |
| `UserEmailTaken` | 203 | Email has already been used. |
| `UserEmailMissing` | 204 | The email is missing, and must be specified. |
| `UserWithEmailNotFound` | 205 | A user with the specified email was not found. |
| `SessionMissing` | 206 | A user object without a valid session could not be altered. |
| `MustCreateUserThroughSignup` | 207 | A user can only be created through signup. |
| `AccountAlreadyLinked` | 208 | An account being linked is already linked to another user. |
| `InvalidSessionToken` | 209 | The device’s session token is no longer valid. The application should ask the user to log in again. |

[](https://docs.parseplatform.org/rest/guide/#linked-services-errors)Linked services errors
-------------------------------------------------------------------------------------------

| Name | Code | Description |
| --- | --- | --- |
| `LinkedIdMissing` | 250 | A user cannot be linked to an account because that account’s id could not be found. |
| `InvalidLinkedSession` | 251 | A user with a linked (e.g. Facebook or Twitter) account has an invalid session. Check error message for more details. |
| `InvalidGeneralAuthData` | 251 | Invalid auth data value used. |
| `BadAnonymousID` | 251 | Anonymous id is not a valid lowercase UUID. |
| `FacebookBadToken` | 251 | The supplied Facebook session token is expired or invalid. |
| `FacebookBadID` | 251 | A user with a linked Facebook account has an invalid session. |
| `FacebookWrongAppID` | 251 | Unacceptable Facebook application id. |
| `TwitterVerificationFailed` | 251 | Twitter credential verification failed. |
| `TwitterWrongID` | 251 | Submitted Twitter id does not match the id associated with the submitted access token. |
| `TwitterWrongScreenName` | 251 | Submitted Twitter handle does not match the handle associated with the submitted access token. |
| `TwitterConnectFailure` | 251 | Twitter credentials could not be verified due to problems accessing the Twitter API. |
| `UnsupportedService` | 252 | A service being linked (e.g. Facebook or Twitter) is unsupported. Check error message for more details. |
| `UsernameSigninDisabled` | 252 | Authentication by username and password is not supported for this application. Check your Parse app’s authentication settings. |
| `AnonymousSigninDisabled` | 252 | Anonymous users are not supported for this application. Check your Parse app’s authentication settings. |
| `FacebookSigninDisabled` | 252 | Authentication by Facebook is not supported for this application. Check your Parse app’s authentication settings. |
| `TwitterSigninDisabled` | 252 | Authentication by Twitter is not supported for this application. Check your Parse app’s authentication settings. |
| `InvalidAuthDataError` | 253 | An invalid authData value was passed. Check error message for more details. |
| `LinkingNotSupportedError` | 999 | Linking to an external account not supported yet with signup_or_login. Use update instead. |

[](https://docs.parseplatform.org/rest/guide/#client-only-errors)Client-only errors
-----------------------------------------------------------------------------------

| Name | Code | Description |
| --- | --- | --- |
| `ConnectionFailed` | 100 | The connection to the Parse servers failed. |
| `AggregateError` | 600 | There were multiple errors. Aggregate errors have an “errors” property, which is an array of error objects with more detail about each error that occurred. |
| `FileReadError` | 601 | Unable to read input for a Parse File on the client. |
| `XDomainRequest` | 602 | A real error code is unavailable because we had to use an XDomainRequest object to allow CORS requests in Internet Explorer, which strips the body from HTTP responses that have a non-2XX status code. |

[](https://docs.parseplatform.org/rest/guide/#operational-issues)Operational issues
-----------------------------------------------------------------------------------

| Name | Code | Description |
| --- | --- | --- |
| `RequestTimeout` | 124 | The request was slow and timed out. Typically this indicates that the request is too expensive to run. You may see this when a Cloud function did not finish before timing out, or when a `Parse.Cloud.httpRequest` connection times out. |
| `InefficientQueryError` | 154 | An inefficient query was rejected by the server. Refer to the Performance Guide and slow query log. |

[](https://docs.parseplatform.org/rest/guide/#other-issues)Other issues
-----------------------------------------------------------------------

| Name | Code | Description |
| --- | --- | --- |
| `OtherCause` | -1 | An unknown error or an error unrelated to Parse occurred. |
| `InternalServerError` | 1 | Internal server error. No information available. |
| `ServiceUnavailable` | 2 | The service is currently unavailable. |
| `ClientDisconnected` | 4 | Connection failure. |

[](https://docs.parseplatform.org/rest/guide/#error-code-ranges)Error Code Ranges
---------------------------------------------------------------------------------

In order to provide better organization and avoid conflicts with Parse Platform’s built-in `Parse.Error` codes, the following ranges are defined:

### [](https://docs.parseplatform.org/rest/guide/#parse-server-and-related-modules)Parse Server and Related Modules

*   Error code range: `<= 4999` (including negative numbers)
*   This range is reserved exclusively for errors generated by Parse Server and its directly related modules. It includes all predefined errors listed in the documentation.

### [](https://docs.parseplatform.org/rest/guide/#reserved)Reserved

*   Error code range: `>= 5000 and <= 8999`
*   This range is currently reserved for future use and should not be used by anyone.

### [](https://docs.parseplatform.org/rest/guide/#app-developers-custom-app-errors)App Developers (Custom App Errors)

*   Error code range: `>= 9000 and <= 9999`
*   Developers may use this range for defining custom errors specific to their applications. This range is reserved to ensure that custom application errors do not conflict with those defined by Parse Server and its modules.

### [](https://docs.parseplatform.org/rest/guide/#3rd-party-providers-of-parse-platform-components)3rd Party Providers of Parse Platform Components

*   We discourage from introducing new custom error codes in 3rd party components, as they may conflict with either of the reserved ranges mentioned above. Instead, use the general internal Parse Server error code `1` and add any specific information in the error message, or use another pre-defined error code of Parse Platform.
