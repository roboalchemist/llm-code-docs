# Source: https://firebase.google.com/docs/functions/1st-gen/http-events-1st.md.txt

<br />

| **Note:** The 1st-gen functionality described in this page is also supported inCloud Functions(2nd gen) with improved features and performance. For more information about 2nd gen, see the[version comparison](https://firebase.google.com/docs/functions/version-comparison). To go directly to the 2nd gen guide for this feature, see[Call functions via HTTP requests](https://firebase.google.com/docs/functions/http-events).

You can trigger a function through an HTTP request by using`functions.https`. This allows you to invoke a synchronous function through the following supported HTTP methods:`GET`,`POST`,`PUT`,`DELETE`, and`OPTIONS`.

Examples in this page are based on a[sample function](https://github.com/firebase/functions-samples/tree/main/Node-1st-gen/quickstarts/https-time-server)that triggers when you send an HTTP`GET`request to the functions endpoint. The sample function retrieves the current server time, formats the time as specified in a URL query parameter, and sends the result in the HTTP response.

## Trigger a function with an HTTP request

Use[`functions.https`](https://firebase.google.com/docs/reference/functions/firebase-functions.https)to create a function that handles HTTP events. The event handler for an HTTP function listens for the[`onRequest()`](https://firebase.google.com/docs/reference/functions/firebase-functions.https#httpsonrequest)event, which supports routers and apps managed by the[Express](https://expressjs.com/)web framework.

### Using Express request and response objects

Used as arguments for`onRequest()`, the[Request](http://expressjs.com/en/4x/api.html#req)object gives you access to the properties of the HTTP request sent by the client, and the[Response](http://expressjs.com/en/4x/api.html#res)object gives you a way to send a response back to the client.

<br />

```gdscript
exports.date = functions.https.onRequest((req, res) => {
  // ...
});
```

<br />

| **Important:** Make sure that all HTTP functions terminate properly. By terminating functions correctly, you can avoid excessive charges from functions that run for too long. Terminate**HTTP functions** with`res.redirect()`,`res.send()`, or`res.end()`.

### Using existing Express apps

Using[App](http://expressjs.com/en/4x/api.html#req.app)as the argument for`onRequest()`, you can pass a full Express app to an HTTP function. Boilerplate code can be moved to middleware as shown:  

    const express = require('express');
    const cors = require('cors');

    const app = express();

    // Automatically allow cross-origin requests
    app.use(cors({ origin: true }));

    // Add middleware to authenticate requests
    app.use(myMiddleware);

    // build multiple CRUD interfaces:
    app.get('/:id', (req, res) => res.send(Widgets.getById(req.params.id)));
    app.post('/', (req, res) => res.send(Widgets.create()));
    app.put('/:id', (req, res) => res.send(Widgets.update(req.params.id, req.body)));
    app.delete('/:id', (req, res) => res.send(Widgets.delete(req.params.id)));
    app.get('/', (req, res) => res.send(Widgets.list()));

    // Expose Express API as a single Cloud Function:
    exports.widgets = functions.https.onRequest(app);

## Invoke an HTTP function

After you deploy an HTTP function, you can invoke it through its own unique URL. The URL includes the following, in order:

- The region (or regions) to which you deployed your function. Some production functions may need to explicitly set the[location](https://firebase.google.com/docs/functions/locations)to minimize network latency.
- Your Firebase project ID
- `cloudfunctions.net`
- The name of your function

For example, the URL to invoke`date()`looks like this:  

    https://us-central1-<project-id>.cloudfunctions.net/date

If you encounter permissions errors when deploying functions, make sure that the appropriate[IAM roles](https://firebase.google.com/docs/projects/iam/permissions#functions)are assigned to the user running the deployment commands.

With Express app routing, the function name is added as a prefix to the URL paths in the app you define. For example, the URL to invoke the getter in the Express app example above looks like this:  

    https://us-central1-<project-id>.cloudfunctions.net/widgets/<id>

If you invoke HTTP functions behind a firewall or IP filter, you can[look up](https://cloud.google.com/compute/docs/faq#find_ip_range)the IP addresses that Google uses to serve HTTP functions.

## Use middleware modules withCloud Functions

If you need to inject middleware dependencies for things like cookie support or CORS, call these within the function. For example, to enable CORS support, add the following block:

<br />

```mysql
// Enable CORS using the `cors` express middleware.
cors(req, res, () => {
  // ...
});
```

<br />

## Read values from the request

The following table lists some common scenarios:

<br />

|            Content Type             |    Request Body     |                                                                    Behavior                                                                     |
|-------------------------------------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| `application/json`                  | `'{"name":"John"}'` | `request.body.name`equals 'John'                                                                                                                |
| `application/octet-stream`          | 'my text'           | `request.body`equals '6d792074657874' (the raw bytes of the request; see the[Node.js Buffer documentation](https://nodejs.org/api/buffer.html)) |
| `text/plain`                        | 'my text'           | `request.body`equals 'my text'                                                                                                                  |
| `application/x-www-form-urlencoded` | 'name=John'         | `request.body.name`equals 'John'                                                                                                                |

This parsing is done by the following body parsers:

- [JSON body parser](https://www.npmjs.com/package/body-parser#bodyparserjsonoptions)
- [Raw body parser](https://www.npmjs.com/package/body-parser#bodyparserrawoptions)
- [Text body parser](https://www.npmjs.com/package/body-parser#bodyparsertextoptions)
- [URL-encoded form body parser](https://www.npmjs.com/package/body-parser#bodyparserurlencodedoptions)

Suppose your function is called with the following request:  

```bash
curl -X POST -H "Content-Type:application/json" -H "X-MyHeader: 123" YOUR_HTTP_TRIGGER_ENDPOINT?foo=baz -d '{"text":"something"}'
```

then the sent data would be materialized under:

|     Property/Method     |                  Value                  |
|-------------------------|-----------------------------------------|
| `req.method`            | "POST"                                  |
| `req.get('x-myheader')` | "123"                                   |
| `req.query.foo`         | "baz"                                   |
| `req.body.text`         | "something"                             |
| `req.rawBody`           | The raw (unparsed) bytes of the request |

In the`date()`function example, the function tests both the URL parameter and the body for a`format`value to set the date/time format to use:

<br />

```text
let format = req.query.format;
format = req.body.format;https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/https-time-server/functions/index.js#L69-L69
```

<br />

## Terminate HTTP Functions

Always end an HTTP function with`send()`,`redirect()`, or`end()`. Otherwise, your function might continue to run and be forcibly terminated by the system. See also[Sync, Async and Promises](https://firebase.google.com/docs/functions/terminate-functions).

After retrieving and formatting the server time using the Node.js[`moment`](https://www.npmjs.com/package/moment)module, the`date()`function concludes by sending the result in the HTTP response:

<br />

```gdscript
const formattedDate = moment().format(`${format}`);
functions.logger.log('Sending Formatted date:', formattedDate);
res.status(200).send(formattedDate);https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/https-time-server/functions/index.js#L73-L75
```

<br />

## Connecting HTTP Functions toFirebase Hosting

You can connect an HTTP function toFirebase Hosting. Requests on yourFirebase Hostingsite can be proxied to specific HTTP functions. This also allows you to use your own custom domain with an HTTP function. Learn more about[connectingCloud FunctionstoFirebase Hosting](https://firebase.google.com/docs/hosting/functions).
| **Note:** If you're using a web framework like Angular Universal or Next.js to develop dynamic web apps, try out the public preview of the[framework-awareFirebaseCLI](https://firebase.google.com/docs/hosting/frameworks-overview). This early preview supports both static site generation and server-side rendering.