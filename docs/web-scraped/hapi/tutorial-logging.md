# hapi Documentation
# Source: https://hapi.dev/tutorials/logging/?lang=en_US

Tutorials

Languages:

en-US pt-BR ko-KR tr-TR zh-CN

  * [Getting Started](/tutorials/gettingstarted/?lang=en_US)

* * *

  * [Express Migration](/tutorials/expresstohapi/?lang=en_US)

* * *

  * [Authentication](/tutorials/auth/?lang=en_US)

* * *

  * [Caching](/tutorials/caching/?lang=en_US)

* * *

  * [Cookies](/tutorials/cookies/?lang=en_US)

* * *

  * [Logging](/tutorials/logging/?lang=en_US)

* * *

  * [Plugins](/tutorials/plugins/?lang=en_US)

* * *

  * [Routing](/tutorials/routing/?lang=en_US)

* * *

  * [Server Methods](/tutorials/servermethods/?lang=en_US)

* * *

  * [Serving Static Files](/tutorials/servingfiles/?lang=en_US)

* * *

  * [Testing](/tutorials/testing/?lang=en_US)

* * *

  * [Validation](/tutorials/validation/?lang=en_US)

* * *

  * [Views](/tutorials/views/?lang=en_US)

* * *

  * [Community Tutorials](/tutorials/community/?lang=en_US)



# Logging

_This tutorial is compatible with hapi v17 and newer_

##  Overview

As with any server software, logging is very important. hapi has some built in logging methods, as well as some basic capabilities for displaying these logs.

##  Built-in Methods

There are two nearly identical logging methods, `server.log(tags, [data, [timestamp]])`, and `request.log(tags, [data])`, which are to be called whenever you want to log an event in your application.

###  request.log()

You want to call `request.log()` whenever you want to log something in the context of a request, such as a route handler, request lifecycle extension, or authentication scheme. The method takes two argument:

`tags`: a string or an array of strings (e.g. `['error', 'database', 'read']`) used to identify the event. Tags are used instead of log levels and provide a much more expressive mechanism for describing and filtering events.

`data`: (optional) a message string or object with the application data being logged. If data is a function, the function signature is `function()` and it called once to generate (return value) the actual data emitted to the listeners.

For example:
    
    
    server.route({
        method: 'GET',
        path: '/',
        handler: function (request, h) {
    
            request.log('error', 'Event error');
            return 'Hello World';
        }
    });
    

In this example, if there is a request-specific event with a tag of `error`, the event will get logged. You also send a `data` parameter of `Event error`. This can be anything you want, such as an error message or any other details.

###  server.log()

`server.log()` is used when you have no specific request in scope, for instance, just after your server has started or inside a plugin's `register()` method.

`server.log()` takes three parameters, `(tags, data, timestamp)`. The `tags` and `data` parameters are exactly the same as in `request.logs()`. The `timestamp` parameter defaults to `Date.now()` and should only be passed in if you need to override the default for some reason.
    
    
    const Hapi = require('@hapi/hapi');
    const server = Hapi.server({ port: 80 });
    
    server.log(['test', 'error'], 'Test event');
    

In this example, you'll see that server will log an event with `tags` `'test'` and `'error'`. Since there is no specific request in scope in this example, you use `server.log()`.

##  Retrieving and Displaying Logs

The hapi server object emits events for each log event. You can use the standard EventEmitter API to listen for such events and display them however you wish.
    
    
    server.events.on('log', (event, tags) => {
    
        if (tags.error) {
            console.log(`Server error: ${event.error ? event.error.message : 'unknown'}`);
        }
    });
    

In this example, you call `server.events.on()` to listen for any `log` event, in this case anything logged with `server.log()`. Events logged with `server.log()` will emit a `log` event and events logged with `request.log()` will emit a `request` event.

You can retrieve all logs for a particular request at once via `request.logs`. This will be an array containing all the logged request events. You must first set the `log.collect` option to `true` on the route, otherwise this array will be empty.
    
    
    server.route({
        method: 'GET',
        path: '/',
        options: {
            log: {
                collect: true
            }
        },
        handler: function (request, h) {
    
            return 'hello';
        }
    });
    

##  Debug Mode (development only)

hapi has a debug mode, which is a pain-free way to have your log events printed to the console, without configuring additional plugins or writing logging code yourself.

By default, the only errors debug mode will print to console are uncaught errors in user code, and runtime errors from incorrect implementation of hapi's API. You can configure your server to print request events based on tag, however. For example, if you wanted to print any error in a request you would configure your server as follows:

`const server = Hapi.server({ debug: { request: ['error'] } });`

You can find more information on debug mode in the [API documentation](/api#server.options.debug).

## Logging Plugins

The built-in methods provided by hapi for retrieving and printing logs are fairly minimal. For a more feature-rich logging experience, you can look into using a plugin like [hapi-pino](https://www.npmjs.com/package/hapi-pino), [New Relic](https://newrelic.com/instant-observability/hapi/2124da5b-0174-457a-be5a-e0068673b2b5) or any of the other [hapi logging plugins](/plugins#logging).

![clipboard](/img/clipboardCheck.png)
