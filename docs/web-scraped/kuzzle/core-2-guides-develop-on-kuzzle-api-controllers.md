# Source: https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers

Title: Kuzzle Documentation

URL Source: https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers

Markdown Content:
API Controllers [#](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers#api-controllers)
-----------------------------------------------------------------------------------------------------------

Kuzzle allows to extend its existing API using Controllers. Controllers are **logical containers of actions**.

These actions are then **processed like any other API action** and can be executed through the different mechanisms to secure and normalize requests.

Add a new Controller [#](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers#add-a-new-controller)
---------------------------------------------------------------------------------------------------------------------

Each controller can therefore have several actions. Each of these **actions is associated with a function** called [handler](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers#handler-function).

The syntax of the definition of these actions and the associated handlers is defined by the [ControllerDefinition](https://docs.kuzzle.io/core/2/framework/types/controller-definition) interface.

By convention, a controller action is identified with the name of the controller followed by the action separated by a colon: `<controller>:<action>` (e.g. [document:create](https://docs.kuzzle.io/core/2/api/controllers/document/create)).

Controllers must be added to the application before the application is started with the [Backend.start](https://docs.kuzzle.io/core/2/framework/classes/backend/start) method.

We have chosen to allow developers to add controllers in two different ways in order to best adapt to their needs.

These two ways are very similar and achieve the same goal.

### Register a Controller [#](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers#register-a-controller)

The [Backend.controller.register](https://docs.kuzzle.io/core/2/framework/classes/backend-controller/register) method allows to add a new controller using a **Plain Old Javascript Object (POJO) complying with the [ControllerDefinition](https://docs.kuzzle.io/core/2/framework/types/controller-definition) interface**.

This method takes in parameter the **name** of the controller followed by its **definition**:

```
app.controller.register('greeting', {
  actions: {
    sayHello: {
      handler: async request => /* ... */
    },
    sayGoodbye: {
      handler: async request => /* ... */
    },
  }
});
```

This is faster to develop but maintenance can be costly in the long run for larger applications with many controllers and actions.

### Use a Controller class [#](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers#use-a-controller-class)

The [Backend.controller.use](https://docs.kuzzle.io/core/2/framework/classes/backend-controller/use) method allows to add a new controller using a **class inheriting from the [Controller](https://docs.kuzzle.io/core/2/framework/abstract-classes/controller) class**.

This class must respect the following conventions:

*   extend the `Controller` class
*   call the super constructor with the application instance
*   define the controller actions under the `definition` property

The controller name will be inferred from the class name (unless the `name` property is defined). E.g. `PaymentSolutionController` will become `payment-solution`.

```
import { Controller, KuzzleRequest } from 'kuzzle';

class GreetingController extends Controller {
  constructor (app: Backend) {
    super(app);

    // type ControllerDefinition
    this.definition = {
      actions: {
        sayHello: {
          handler: this.sayHello
        },
        sayGoodbye: {
          handler: this.sayGoodbye
        }
      }
    };
  }

  async sayHello (request: KuzzleRequest) { /* ... */ }

  async sayGoodbye (request: KuzzleRequest) { /* ... */ }
}
```

If the handler function is an instance method of the controller then the context will be automatically bound to the controller instance.

Once you have defined your controller class, you can instantiate it and pass it to the `Backend.controller.use` method:

```
const greetingController = new GreetingController(app);

app.controller.use(greetingController);
```

This way of doing things takes longer to develop but it allows you to have a better code architecture while respecting OOP concepts.

Handler Function [#](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers#handler-function)
-------------------------------------------------------------------------------------------------------------

The handler is the function that will **be called each time our API action is executed**.

This function **takes a [KuzzleRequest](https://docs.kuzzle.io/core/2/framework/classes/kuzzle-request) object** as a parameter and **must return a Promise** resolving on the result to be returned to the client.

This function is defined in the `handler` property of an action. Its signature is: `(request: KuzzleRequest) => Promise<any>`.

```
app.controller.register('greeting', {
  actions: {
    sayHello: {
      // Handler function for the "greeting:sayHello" action
      handler: async (request: KuzzleRequest) => {
        return `Hello, ${request.getString('name')}`;
      }
    }
  }
});
```

The result returned by our `handler` will be **converted to JSON format** and integrated into the standard Kuzzle response in the `result` property.

```
npx wscat -c ws://localhost:7512 --execute '{
  "controller": "greeting",
  "action": "sayHello",
  "name": "Yagmur"
}'

{
  "requestId": "a6f4f5b6-1aa2-4cf9-9724-12b12575c047",
  "status": 200,
  "error": null,
  "controller": "greeting",
  "action": "sayHello",
  "collection": null,
  "index": null,
  "volatile": null,
  "result": "Hello, Yagmur", # <= handler function return value
  "room": "a6f4f5b6-1aa2-4cf9-9724-12b12575c047"
}
```

HTTP routes [#](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers#http-routes)
---------------------------------------------------------------------------------------------------

The execution of an API action through the HTTP protocol is significantly different from other protocols.

Indeed, **the HTTP protocol uses verbs and routes** in order to address an action whereas the other protocols only use the controller and action name in their JSON payloads.

### Define a HTTP route [#](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers#define-a-http-route)

When defining a controller action, it is also possible to **specify one or more HTTP routes** available to execute our action using the `http` property.

This property is at the same level as `handler` and **represents an array of routes**. Each route is an object containing a `verb` and a `path` property.

The following HTTP verbs are available: `get`, `post`, `put`, `delete`, `head`.

When the `path` property starts with a `/` then the route is added as is, otherwise the route will be prefixed with `/_/`.

```
app.controller.register('greeting', {
  actions: {
    sayHello: {
      handler: async (request: KuzzleRequest) => {
        return `Hello, ${request.getString('name')}`;
      },
      http: [
        // generated route: "GET http://<host>:<port>/greeting/hello"
        { verb: 'get', path: '/greeting/hello' },
        // generated route: "POST http://<host>:<port>/_/hello/world"
        { verb: 'post', path: 'hello/world' },
      ]
    }
  }
});
```

It is recommended to let Kuzzle prefix the routes with `/_/` in order to avoid conflict with the existing routes of the standard API.

It is possible to define paths with url parameters. These parameters will be captured and then integrated into the [KuzzleRequest Input](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers#request-input).

```
app.controller.register('greeting', {
  actions: {
    sayHello: {
      handler: async (request: KuzzleRequest) => {
        // "name" comes from the url parameter
        return `Hello, ${request.getString('name')}`;
      },
      http: [
        { verb: 'get', path: '/email/send/:name' },
      ]
    }
  }
});
```

### Default route [#](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers#default-route)

If the `http` property is not set, then Kuzzle will **generate a default route** so that the action can be called from the HTTP protocol.

This default generated route has the following format: `GET http://<host>:<port>/_/<controller-name>/<action-name>`.

The name of the controller and the action will be converted to `kebab-case` format. For example the default route of the `sayHello` action will be: `GET http://<host>:<port>/_/greeting/say-hello`.

It is possible to prevent the generation of a default HTTP route by providing an empty array to the `http` property. By doing this, the action will only be available through the HTTP protocol with the [JSON Query Endpoint](https://docs.kuzzle.io/core/2/guides/main-concepts/api#json-query-endpoint).

OpenAPI Specification [#](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers#openapi-specification)
-----------------------------------------------------------------------------------------------------------------------

The API action [server:openapi](https://docs.kuzzle.io/core/2/api/controllers/server/openapi) returns available API routes OpenAPI v3 specifications.

When used with the `scope` argument to `app`, the API action will returns the OpenAPI specification of custom controllers added by plugins or the application.

Kuzzle generates specifications for custom API actions, although it is possible to customize the OpenAPI specifications for each HTTP route.

To register this custom specification, it must be declared with http routes in an `openapi` property. To write this object, follow the official [openapi specification](https://swagger.io/specification/#paths-object) especially the paths object section.

```
app.controller.register('greeting', {
  actions: {
    sayHello: {
      handler: async (request: KuzzleRequest) => {
        return `Hello, ${request.getString('name')}`;
      },
      http: [{
        verb: 'post',
        path: 'hello/world',
        openapi: {
          description: "Simply say hello",
          parameters: [{
            in: "query",
              name: "name",
              schema: {
                type: "string"
              },
              required: true,
          }],
          responses: {
            200: {
              description: "Custom greeting",
              content: {
                "application/json": {
                  schema: {
                    type: "string",
                  }
                }
              }
            }
          }
        }
      }]
    }
  }
});
```

Then Kuzzle will inject the http route specification as shown in the example below using each property `path`, `verb` and `openapi`.

```
{
  "openapi": "3.0.1",
  "info": {
    "title":"Kuzzle API",
    "description":"The Kuzzle HTTP API",
    "contact": {
      "name":"Kuzzle team",
      "url":"http://kuzzle.io",
      "email":"hello@kuzzle.io"
    },
    "license": {
      "name":"Apache 2",
      "url":"http://opensource.org/licenses/apache2.0"
    },
    "version":"2.4.5"
  },
  "paths": {
    "<path>": {
      "<verb>": {
        // openapi property injected here
      }
    },
  }
}
```

Available since 2.17.0

The complete OpenAPI definition is accessible and customizable with the [Backend.openapi.definition](https://docs.kuzzle.io/core/2/framework/classes/backend-openapi) property.

**Example:**_Register an OpenAPI schema_

```
app.openApi.definition.components.LogisticObjects = {
  Item: {
    type: 'object',
    properties: {
      name: { type: 'string' },
      quantity: { type: 'integer' },
    }
  }
};

// Then you can reference this schema anywhere according to OpenAPI specification "#/components/LogisticObjects/Item"
```

KuzzleRequest Input [#](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers#kuzzlerequest-input)
-------------------------------------------------------------------------------------------------------------------

The `handler` of an API action receives an instance of [KuzzleRequest](https://docs.kuzzle.io/core/2/framework/classes/kuzzle-request) object. This object represents an API request and **contains both the client input and client contextual information**.

The arguments of requests sent to the Kuzzle API are available in the [KuzzleRequest.input](https://docs.kuzzle.io/core/2/framework/classes/request-input) property.

The main available properties are the following:

*   `controller`: API controller name
*   `action`: API action name
*   `args`: Action arguments
*   `body`: Body content

Available since 2.11.0

The request object exposes methods to safely extract parameters from the request in a standardized way.

Each of those methods will check for the parameter presence and type. In case of a validation failure, the corresponding API error will be thrown.

All those methods start with `getXX`: [getString](https://docs.kuzzle.io/core/2/framework/classes/kuzzle-request/get-string), [getBoolean](https://docs.kuzzle.io/core/2/framework/classes/kuzzle-request/get-boolean), [getBodyObject](https://docs.kuzzle.io/core/2/framework/classes/kuzzle-request/get-body-object) etc.

### HTTP [#](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers#http)

With HTTP, there are 3 types of input parameters:

*   URL parameters (**e.g. `/greeting/hello/:name`**)
*   Query arguments (**e.g. `/greeting/hello?name=aschen`**)
*   KuzzleRequest body

URL parameters and query arguments can be found in the `request.input.args` property.

The content of the query body can be found in the `request.input.body` property

The request body must either be in JSON format or submitted as an HTTP form (URL encoded or multipart form data)

For example, with the following request input:

```
# Route: "POST /greeting/hello/:name"
curl \
  -X POST \
  -H  "Content-Type: application/json" \
  "localhost:7512/_/greeting/hello/aschen?_id=JkkZN62jLSA&age=27" \
  --data '{
    "city" : "Antalya"
  }'
```

We can retrieve them in the [KuzzleRequest](https://docs.kuzzle.io/core/2/framework/classes/kuzzle-request) object passed to the `handler`:

```
import assert from 'assert';

app.controller.register('greeting', {
  actions: {
    sayHello: {
      handler: async (request: KuzzleRequest) => {
        assert(request.input.args._id === 'JkkZN62jLSA');
        assert(request.input.args.name === 'aschen');
        assert(request.input.args.age === '27');
        assert(request.input.body.city === 'Antalya');
        // equivalent to
        assert(request.getId() === 'JkkZN62jLSA');
        assert(request.getString('name') === 'aschen');
        assert(request.getInteger('age') === '27');
        assert(request.getBodyString('city') === 'Antalya');
      },
      http: [
        { verb: 'POST', path: 'greeting/hello/:name' }
      ]
    }
  }
});
```

### Other protocols [#](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers#other-protocols)

Other protocols directly **use JSON payloads**.

These payloads contain all the information directly:

```
npx wscat -c ws://localhost:7512 --execute '{
  "controller": "greeting",
  "action": "sayHello",
  "_id": "JkkZN62jLSA",
  "age": 27,
  "name": "aschen",
  "body": {
    "city": "Antalya"
  }
}'
```

We can retrieve them in the [KuzzleRequest](https://docs.kuzzle.io/core/2/framework/classes/kuzzle-request) object passed to the `handler`:

```
import assert from 'assert';

app.controller.register('greeting', {
  actions: {
    sayHello: {
      handler: async (request: KuzzleRequest) => {
        assert(request.input.args._id === 'JkkZN62jLSA');
        assert(request.input.args.name === 'aschen');
        assert(request.input.args.age === '27');
        assert(request.input.body.city === 'Antalya');
        // equivalent to
        assert(request.getId() === 'JkkZN62jLSA');
        assert(request.getString('name') === 'aschen');
        assert(request.getInteger('age') === '27');
        assert(request.getBodyString('city') === 'Antalya');
      },
    }
  }
});
```

KuzzleRequest Context [#](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers#kuzzlerequest-context)
-----------------------------------------------------------------------------------------------------------------------

Information about **the client that executes an API action** are available in the [KuzzleRequest.context](https://docs.kuzzle.io/core/2/framework/classes/request-context) property.

The available properties are as follows:

*   [connection](https://docs.kuzzle.io/core/2/framework/classes/request-context/properties#connection): information about the connection
*   [user](https://docs.kuzzle.io/core/2/framework/classes/request-context/properties#user): information about the user executing the request
*   (optional) [token](https://docs.kuzzle.io/core/2/framework/classes/request-context/properties#token): information about the authentication token

Example:

```
import assert from 'assert';

app.controller.register('greeting', {
  actions: {
    sayHello: {
      handler: async (request: KuzzleRequest) => {
        assert(request.context.connection.protocol === 'http');
        // Unauthenticated users are anonymous
        // and the anonymous user ID is "-1"
        assert(request.context.user._id === '-1');
        // equivalent to
        assert(request.getKuid() === '-1');
      },
    }
  }
});
```

Response format [#](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers#response-format)
-----------------------------------------------------------------------------------------------------------

Kuzzle Response are **standardized**. This format is shared by all API actions, including custom controller actions.

A [ResponsePayload](https://docs.kuzzle.io/core/2/api/payloads/response) is a **JSON object** with the following format:

| Property | Description |
| --- | --- |
| `action` | API action |
| `collection` | Collection name, or `null` if no collection was involved |
| `controller` | API controller |
| `error` | [KuzzleError](https://docs.kuzzle.io/core/2/api/errors/types) object, or `null` if there was no error |
| `index` | Index name, or `null` if no index was involved |
| `requestId` | KuzzleRequest unique identifier |
| `result` | Action result, or `null` if an error occured |
| `status` | Response status, using [HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) |
| `volatile` | Arbitrary data repeated from the initial request |
| The `result` property will contain the return of the action `handler` function. |  |

For example, when calling this controller action:

```
app.controller.register('greeting', {
  actions: {
    sayHello: {
      handler: async (request: KuzzleRequest) => {
        return `Hello, ${request.getString('name')}`;
      }
    }
  }
});
```

The following response will be sent:

```
npx wscat -c ws://localhost:7512 --execute '{
  "controller": "greeting",
  "action": "sayHello",
  "name": "Yagmur"
}'

{
  "requestId": "a6f4f5b6-1aa2-4cf9-9724-12b12575c047",
  "status": 200,
  "error": null,
  "controller": "greeting",
  "action": "sayHello",
  "collection": null,
  "index": null,
  "volatile": null,
  "result": "Hello, Yagmur", # <= handler function return value
  "room": "a6f4f5b6-1aa2-4cf9-9724-12b12575c047"
}
```

#### Return a custom response [#](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers#return-a-custom-response)

In some cases it may be necessary to **return a response that differs** from the standard API response format.

This may be to send a **smaller JSON response** for constrained environments, to **perform HTTP redirection** or to **return another MIME type** such as CSV, an image, a PDF document, etc.

For this it is possible to use the method [request.response.configure](https://docs.kuzzle.io/core/2/framework/classes/request-response/configure) with the `raw` format. This option prevents Kuzzle from standardizing an action's output:

**Example:**_Return a CSV file_

```
app.controller.register('files', {
  actions: {
    csv: {
      handler: async request => {
        const csv = 'name,age\naschen,27\ncaner,28\n';

        request.response.configure({
          format: 'raw',
          headers: {
            'Content-Type': 'text/csv',
            'Content-Disposition': 'attachment; filename="export.csv"'
          }
        });

        return csv;
      }
    }
  }
});
```

The response will only contain the CSV document:

```
curl localhost:7512/_/files/csv

name,age
aschen,27
caner,28
```

You can also change the HTTP status code with the `status` option.

**Example:**_Redirect requests to another website_

```
app.controller.register('redirect', {
  actions: {
    proxy: {
      handler: async request => {
        request.response.configure({
          format: 'raw',
          // HTTP status code for redirection
          status: 302,
          headers: {
            'Location': 'http://kuzzle.io'
          }
        });

        return null;
      }
    }
  }
});
```

#### HTTP Streams [#](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers#http-streams)

Available since 2.17.0

Kuzzle sends response through HTTP using the JSON format. [Kuzzle Response](https://docs.kuzzle.io/core/2/guides/main-concepts/api#response-format) are standardized. This format is shared by all API actions, including custom controller actions.

Kuzzle Response might be heavy when it comes to processing and sending large volumes of data, since the response are sent in one go, this imply that all the processing must be done before sending the response and must be stored in ram until the whole response is sent.

To avoid having to process and store large amount of data before sending it, Kuzzle allow controller's actions to return an [HttpStream](https://docs.kuzzle.io/core/2/framework/classes/http-stream) instead of a JSON object. Kuzzle will then stream the data though the HTTP protocol in chunk until the stream is closed, this way you can process bits of your data at a time and not have everything stored in ram.

Chunks are sent through the HTTP Protocol each time a chunk is emitted through the `data` event of the given stream. It's up to you to implement a buffer mechanism to avoid sending too many small consecutive chunks through the network.

Sending too many small chunks instead of bigger chunks will increase the number of syscall made to the TCP Socket and might decrease performance and throughput.

**Usage:**

All you need to send a stream from any controller's actions is to wrap any [Readable Stream](https://nodejs.org/docs/latest-v14.x/api/stream.html#stream_class_stream_readable) from NodeJS with an [HttpStream](https://docs.kuzzle.io/core/2/framework/classes/http-stream).

**Example: Read a file from the disk and send it.**

```
const fs = require('fs');

app.controller.register('myController', {
  actions: {
    myDownloadAction: {
      handler: async (request: KuzzleRequest) => {
        const readStream = fs.createReadStream('./Document.tar.gz');

        return new HttpStream(readStream);
      }
    }
  }
});
```

Use a custom Controller Action [#](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers#use-a-custom-controller-action)
-----------------------------------------------------------------------------------------------------------------------------------------

As we have seen, controller actions can be executed via different protocols.

We will explore the various possibilities available to execute API actions.

```
app.controller.register('greeting', {
  actions: {
    sayHello: {
      handler: async (request: KuzzleRequest) => {
        return `Hello, ${request.getString('name')}`;
      }
    }
  }
});
```

### HTTP [#](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers#http-1)

Our action can be executed through the HTTP protocol by using an HTTP client (cURL, HTTPie, Postman, ...):

`curl http://localhost:7512/_/greeting/say-hello?name=Yagmur`

### WebSocket [#](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers#websocket)

To execute our action through the WebSocket protocol, we will be using [wscat](https://www.npmjs.com/package/wscat):

```
npx wscat -c ws://localhost:7512 --execute '{
  "controller": "greeting",
  "action": "sayHello",
  "name": "Yagmur"
}'
```

### Kourou [#](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers#kourou)

From a terminal, [Kourou](https://github.com/kuzzleio/kourou), the Kuzzle CLI, can be used to execute an action:

`kourou greeting:sayHello --arg name=Yagmur`

It is possible to pass multiple arguments by repeating the `--arg <arg>=<value>` flag or specify a body with the `--body '{}'` flag.

### SDK [#](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers#sdk)

From one of our [SDKs](https://docs.kuzzle.io/sdk), it is possible to use the `query` method which takes a [KuzzleRequest Payload](https://docs.kuzzle.io/core/2/guides/main-concepts/api#others-protocol) as a parameter.

:::: tabs ::: tab Javascript

Using the Javascript SDK [Kuzzle.query](https://docs.kuzzle.io/sdk/js/7/core-classes/kuzzle/query) method:

```
const response = await kuzzle.query({
  controller: 'greeting',
  action: 'sayHello',
  name: 'Yagmur'
});
```

::: ::: tab Dart

Using the [Dart SDK](https://docs.kuzzle.io/sdk/dart/2/) Kuzzle.query method:

```
final response = await kuzzle.query({
  'controller': 'greeting',
  'action': 'sayHello',
  'name': 'Yagmur'
});
```

:::

::: tab Kotlin

Using the JVM SDK [Kuzzle.query](https://docs.kuzzle.io/sdk/jvm/1/core-classes/kuzzle/query) method:

```
ConcurrentHashMap<String, Object> query = new ConcurrentHashMap<>();
query.put("controller", "greeting");
query.put("action", "sayHello");
query.put("name", "Yagmur");

Response res = kuzzle.query(query).get();
```

:::

::: tab Csharp

Using the Csharp SDK [Kuzzle.query](https://docs.kuzzle.io/sdk/csharp/2/core-classes/kuzzle/query-async/) method:

```
JObject request = JObject.Parse(@"{
  controller: 'greeting',
  action: 'sayHello',
  name: 'Yagmur'
}");

Response response = await kuzzle.QueryAsync(request);
```

:::

::::

Allow access to a custom Controller Action [#](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers#allow-access-to-a-custom-controller-action)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

In the rights management system, **[roles](https://docs.kuzzle.io/core/2/guides/main-concepts/permissions#roles) are managing access to API actions**.

They operate on a whitelist principle by **listing the controllers and actions they give access to**.

So, to allow access to the `greeting:sayHello` action, the following role can be written:

```
kourou security:createRole '{
  controllers: {
    greeting: {
      actions: {
        sayHello: true
      }
    }
  }
}' --id steward
```

It is also possible to use a wildcard (`*`) to give access to all of a controller's actions:

```
kourou security:createRole '{
  controllers: {
    greeting: {
      actions: {
        "*": true
      }
    }
  }
}' --id steward
```
