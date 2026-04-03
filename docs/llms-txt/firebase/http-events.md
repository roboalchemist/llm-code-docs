# Source: https://firebase.google.com/docs/functions/http-events.md.txt

<br />

You can trigger a function through an HTTP request with a request handler. This allows you to invoke a function through the following supported HTTP methods:`GET`,`POST`,`PUT`,`DELETE`, and`OPTIONS`.

## Additional HTTP options

|                  Option                   |                                                                                                 Description                                                                                                  |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `region`                                  | HTTP functions may specify an array of regions as well as a single region. When multiple regions are specified, a separate function instance will be deployed for each region.                               |
| `timeoutSeconds`(`timeout_sec`for Python) | HTTP functions may specify a timeout of up to one hour.                                                                                                                                                      |
| `cors`                                    | HTTP functions may specify CORS policies. You can set this to`true`to allow all origins or a`string`,`regex`, or`array`to specify allowed origins. Defaults to false/no CORS policies if not explicitly set. |

### Configuring CORS (Cross-Origin Resource Sharing)

Use the`cors`option to control which origins can access your function. By default, HTTP functions don't have CORS configured, meaning that any cross-origin request to your function results in this error:  

    request has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.

You can also explicitly disable CORS by setting the`cors`option to`false`for your function.

To allow some cross-origin requests, but not all, you can pass a list of specific domains or regular expressions that should be allowed. For example, if you own the domains`firebase.com`and`flutter.com`, and`firebase.com`can have many subdomains, you might want to set the`cors`option to`[/firebase\.com$/, 'https://flutter.com']`for Node.js or`[r'firebase\.com$', r'https://flutter\.com']`for Python:  

### Node.js

    const { onRequest } = require("firebase-functions/v2/https");

    exports.sayHello = onRequest(
      { cors: [/firebase\.com$/, "https://flutter.com"] },
      (req, res) => {
        res.status(200).send("Hello world!");
      }
    );

### Python

    from firebase_functions import https_fn, options

    @https_fn.on_request(
        cors=options.CorsOptions(
            cors_origins=[r"firebase\.com$", r"https://flutter\.com"],
            cors_methods=["get", "post"],
        )
    )
    def say_hello(req: https_fn.Request) -> https_fn.Response:
        return https_fn.Response("Hello world!")

If your function should be openly available, for example if it's serving a public API or website, set the`cors`policy to`true`.

## Trigger a function with an HTTP request

Use the request handler for your platform ([`onRequest()`](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https#httpsonrequest)or[`on_request`](https://firebase.google.com/docs/reference/functions/python/firebase_functions.https_fn#on_request)) to create a function that handles HTTP events. Examples in this section are based on a "time server" sample that triggers when you send an HTTP`GET`request to the functions endpoint. The sample function retrieves the current server time, formats the time as specified in a URL query parameter, and sends the result in the HTTP response.

### Using request and response objects

The request object gives you access to the properties of the HTTP request sent by the client, and the response object gives you a way to send a response back to the client.  

### Node.js

```javascript
exports.date = onRequest(
    {timeoutSeconds: 1200, region: ["us-west1", "us-east1"]},
    (req, res) => {
// ...
});
```

### Python

    @https_fn.on_request(cors=options.CorsOptions(cors_origins="*", cors_methods=["get", "post"]))
    def date(req: https_fn.Request) -> https_fn.Response:
        """Get the server's local date and time."""  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/https-time-server/functions/main.py#L41-L45

| **Important:** Make sure that all HTTP functions terminate properly. By terminating functions correctly, you can avoid excessive charges from functions that run for too long.

### Using existing Express or Flask apps

Using the app as the argument for the request handler, you can pass a full app to an HTTP function:  

### Node.js

    const { onRequest } = require('firebase-functions/v2/https');

    const express = require('express');
    const app = express();

    // Add middleware to authenticate requests
    app.use(myMiddleware);

    // build multiple CRUD interfaces:
    app.get('/:id', (req, res) => res.send(Widgets.getById(req.params.id)));
    app.post('/', (req, res) => res.send(Widgets.create()));
    app.put('/:id', (req, res) => res.send(Widgets.update(req.params.id, req.body)));
    app.delete('/:id', (req, res) => res.send(Widgets.delete(req.params.id)));
    app.get('/', (req, res) => res.send(Widgets.list()));

    // Expose Express API as a single Cloud Function:
    exports.widgets = onRequest(app);

### Python

    from firebase_admin import initialize_app, db
    from firebase_functions import https_fn
    import flask

    initialize_app()
    app = flask.Flask(__name__)

    # Build multiple CRUD interfaces:


    @app.get("/widgets")
    @app.get("/widgets/<id>")
    def get_widget(id=None):
        if id is not None:
            return db.reference(f"/widgets/{id}").get()
        else:
            return db.reference("/widgets").get()


    @app.post("/widgets")
    def add_widget():
        new_widget = flask.request.get_data(as_text=True)
        db.reference("/widgets").push(new_widget)
        return flask.Response(status=201, response="Added widget")


    # Expose Flask app as a single Cloud Function:


    @https_fn.on_request()
    def httpsflaskexample(req: https_fn.Request) -> https_fn.Response:
        with app.request_context(req.environ):
            return app.full_dispatch_request()  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/http-flask/functions/main.py#L16-L48

## Invoke an HTTP function

After you deploy an HTTP function, you can invoke it through its own unique URL. Use the exact URL output from the CLI after deployment.

For example, the URL to invoke`date()`looks like this:  

    https://us-central1-<project-id>.cloudfunctions.net/date

With Express and Flask app routing, the function name is added as a prefix to the URL paths in the app you define.

## Read values from the request

In the`date()`function example, the function tests both the URL parameter and the body for a`format`value to set the date/time format to use:  

### Node.js

```javascript
let format = req.query.format;
format = req.body.format;https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/https-time-server/functions/index.js#L68-L68
```

### Python

    format = req.args["format"] if "format" in req.args else None  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/https-time-server/functions/main.py#L55-L55

## Terminate HTTP Functions

After retrieving and formatting the server time, the`date()`function concludes by sending the result in the HTTP response:  

### Node.js

Always end an HTTP function with`send()`,`redirect()`, or`end()`. Otherwise, your function might continue to run and be forcibly terminated by the system. See also[Sync, Async and Promises](https://firebase.google.com/docs/functions/terminate-functions).  

```javascript
const formattedDate = moment().format(`${format}`);
logger.log("Sending formatted date:", formattedDate);
res.status(200).send(formattedDate);https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/https-time-server/functions/index.js#L73-L75
```

### Python

    formatted_date = datetime.now().strftime(format)
    print(f"Sending Formatted date: {formatted_date}")
    return https_fn.Response(formatted_date)  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/https-time-server/functions/main.py#L67-L69

## Integrating with Firebase Hosting

You can connect an HTTP function toFirebase Hosting. Requests on yourFirebase Hostingsite can be proxied to specific HTTP functions. This also allows you to use your own custom domain with an HTTP function. Learn more about[connectingCloud FunctionstoFirebase Hosting](https://firebase.google.com/docs/hosting/functions).