# hapi Documentation
# Source: https://hapi.dev/tutorials/servermethods/?lang=en_US

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



# Server Methods

_This tutorial is compatible with hapi v17 and newer_

##  Overview

Server methods are a useful way of sharing functions by attaching them to your server object rather than requiring a common module everywhere it is needed. Server methods are also used heavily for caching purposes. Since server methods leverage hapi's native caching, they can help reduce your boilerplate to a minimum. See the caching tutorial for more. To register a server method, you call [`server.method()`](/api#server.method\(\)). There are two different ways to call this function. You can call it with the signature `server.method(name, method, [options])`, or you can call it with the signature `server.method(method)`, where `method` is an object with `name`, `method`, and `options` parameters (note that you may also pass an array of these objects).

##  server.method()

The first way to call `server.method()` is with the signature `server.method(name, method, [options])`:
    
    
    const add = function (x, y) {
    
        return x + y;
    };
    
    server.method('add', add, {});
    

Here, you create a function called `add`, which takes two parameters and adds them together. Then you call `server.method()` with the name of the method being `add`, the method you are using, the one we just created called `add`, and no options.

The second way to call `server.method()` is with the signature `server.method(method)`:
    
    
    const add = function (x, y) {
    
        return x + y;
    };
    
    server.method({
        name: 'add',
        method: add,
        options: {}
    });
    

You create the same function again, called `add`. When you register it this time, configure the `method` object. This case, `name` is the name of the method, `method` is the method you are using, and `options` is an object to configure various options.

###  Name

The `name` parameter is a string used to retrieve the method from the server later, via [`server.methods[name]`](#server.methods). Note that if you specify a `name` with a `.` character, it is registered as a nested object rather than the literal string. As in:
    
    
    server.method('math.add', add);
    

This server method can then be called via `server.methods.math.add()`.

###  Method

The `method` parameter is the actual function to call when the method is invoked. It can take any number of arguments. It can be an `async` function, for example:
    
    
    const add = async function (x, y) {
    
        const result = await someLongRunningFunction(x, y);
        return result;
    };
    
    server.method('add', add, {});
    

Your server method function should return a valid result or throw an error if one occurs.

##  Options

When registering `server.method()`, you can configure three `options`: `cache`, `generateKey`, and `bind`.

###  Cache

A major advantage of server methods is that they may leverage hapi's native caching. The default is to not cache, however if a valid configuration is passed when registering the method, the return value will be cached and served from the cache instead of re-running your method every time it is called. The configuration looks like the following:
    
    
    server.method('add', add, {
        cache: {
            expiresIn: 60000,
            expiresAt: '20:30',
            staleIn: 30000,
            staleTimeout: 10000,
            generateTimeout: 100
        }
    });
    

The parameters mean:

  * `expiresIn`: relative expiration expressed in the number of milliseconds since the item was saved in the cache. Cannot be used together with `expiresAt`.
  * `expiresAt`: time of day expressed in 24h notation using the 'HH:MM' format, at which point all cache records for the route expire. Uses local time. Cannot be used together with `expiresIn`.
  * `staleIn`: number of milliseconds to mark an item stored in cache as stale and attempt to regenerate it. Must be less than `expiresIn`.
  * `staleTimeout`: number of milliseconds to wait before returning a stale value while generateFunc is generating a fresh value.
  * `generateTimeout`: number of milliseconds to wait before returning a timeout error when it takes too long to return a value. When the value is eventually returned, it is stored in the cache for future requests.
  * `segment`: an optional segment name used to isolate cache items.
  * `cache`: an optional string with the name of the cache connection configured on your server to use



More information on the caching options can be found in the [API Reference](/api#server.methods) as well as the documentation for [catbox](/module/catbox#policy).

You can override the `ttl` (time-to-live) of a server method result per-invocation by setting the `ttl` flag. Let's see how this works with the earlier example:
    
    
    const add = async function (x, y, flags) {
    
        const result = await someLongRunningFunction(x, y);
    
        flags.ttl = 5 * 60 * 1000; // 5 mins
    
        return result;
    };
    
    server.method('add', add, {
        cache: {
            expiresIn: 2000,
            generateTimeout: 100
        }
    });
    

Here you defined your server method function to have one more parameter than you're expecting to pass to it, the additional `flags` parameter is passed by hapi. You then simply set the `ttl` flag to however long you want the result to be cached for (in milliseconds); if it is set to `0` then the value will never be cached. If you set no flag then the `ttl` will be taken from the cache configuration.

###  Generate a Custom Key

In addition to the above options, you may also define a custom function used to generate a cache key based on the parameters passed to your method. If your method only accepts some combination of string, number, and boolean values hapi will generate a sane key for you. However, if your method accepts an object parameter, you should specify a function that will generate a cache key similar to the following:
    
    
    const sum = function (array) {
    
        let total = 0;
    
        array.forEach((item) => {
    
            total += item;
        });
    
        return total;
    };
    
    server.method('sum', sum, {
        generateKey: (array) => array.join(',')
    });
    

Any arguments that you pass to your method are available to the `generateKey` method.

###  Bind

The last option available to server methods is `bind`. The `bind` option changes the `this` context within the method. It defaults to the current active context when the method is added. This can be useful for passing in a database client without needing to pass it as a parameter and requiring a custom `generateKey` function, as in:
    
    
    const lookup = async function (id) {
    
        // calls myDB.getOne
    
        return await this.getOne({ id });
    };
    
    server.method('lookup', lookup, { bind: myDB });
    

##  server.methods

To call the server methods we registered above, you would use `server.methods()`. Consider our add function:
    
    
    const add = function (x, y) {
    
        return x + y;
    };
    
    server.method({
        name: 'add',
        method: add,
        options: {}
    });
    

To use this method, simply call `server.methods()`
    
    
    server.methods.add(1, 2);  // 3
    

![clipboard](/img/clipboardCheck.png)
