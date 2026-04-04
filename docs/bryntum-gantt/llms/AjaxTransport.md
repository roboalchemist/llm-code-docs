# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/crud/transport/AjaxTransport.md

# [AjaxTransport](https://bryntum.com/docs/gantt/api/Scheduler/crud/transport/AjaxTransport)

Implements data transferring functional that can be used for [AbstractCrudManager](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManager) super classing. Uses the [Fetch API](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) for transport.

```
// create a new CrudManager using AJAX as a transport system and JSON for encoding
class MyCrudManager extends AjaxTransport(JsonEncode(AbstractCrudManager)) {}
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[transport](https://bryntum.com/docs/gantt/api/Scheduler/crud/transport/AjaxTransport#config-transport)
Configuration of the AJAX requests used by _Crud Manager_ to communicate with a server-side.

```
transport : {
    load : {
        url       : 'http://mycool-server.com/load.php',
        // HTTP request parameter used to pass serialized "load"-requests
        paramName : 'data',
        // pass extra HTTP request parameter
        params    : {
            foo : 'bar'
        }
    },
    sync : {
        url     : 'http://mycool-server.com/sync.php',
        // specify Content-Type for requests
        headers : {
            'Content-Type' : 'application/json'
        }
    }
}
```

Since the class uses Fetch API you can use any of the [Request interface](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/API/Request) options:

```
transport : {
    load : {
        url         : 'http://mycool-server.com/load.php',
        // HTTP request parameter used to pass serialized "load"-requests
        paramName   : 'data',
        // pass few Fetch API options
        method      : 'GET',
        credentials : 'include',
        cache       : 'no-cache'
    },
    sync : {
        url         : 'http://mycool-server.com/sync.php',
        // specify Content-Type for requests
        headers     : {
            'Content-Type' : 'application/json'
        },
        credentials : 'include'
    }
}
```

An object where you can set the following possible properties:

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAjaxTransport](https://bryntum.com/docs/gantt/api/Scheduler/crud/transport/AjaxTransport#property-isAjaxTransport)
Identifies an object as an instance of [AjaxTransport](https://bryntum.com/docs/gantt/api/#Scheduler/crud/transport/AjaxTransport) class, or subclass thereof.

[isAjaxTransport](https://bryntum.com/docs/gantt/api/Scheduler/crud/transport/AjaxTransport#property-isAjaxTransport-static)
Identifies an object as an instance of [AjaxTransport](https://bryntum.com/docs/gantt/api/#Scheduler/crud/transport/AjaxTransport) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[cancelRequest](https://bryntum.com/docs/gantt/api/Scheduler/crud/transport/AjaxTransport#function-cancelRequest)
Cancels an ongoing request.

[sendRequest](https://bryntum.com/docs/gantt/api/Scheduler/crud/transport/AjaxTransport#function-sendRequest)
Sends a _Crud Manager_ request to the server.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeSend](https://bryntum.com/docs/gantt/api/Scheduler/crud/transport/AjaxTransport#event-beforeSend)
Fires before a request is sent to the server.

```
crudManager.on('beforeSend', function ({ params, type }) {
    // let's set "sync" request parameters
    if (type == 'sync') {
        // dynamically depending on "flag" value
        if (flag) {
            params.foo = 'bar';
        }
        else {
            params.foo = 'smth';
        }
    }
});
```
