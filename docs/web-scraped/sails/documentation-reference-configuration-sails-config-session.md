# Source: https://sailsjs.com/documentation/reference/configuration/sails-config-session

Title: sails.config.session

URL Source: https://sailsjs.com/documentation/reference/configuration/sails-config-session

Markdown Content:
sails.config.session
===============

[Edit Page](https://github.com/balderdashy/sails/blob/master/docs/reference/sails.config/sails.config.session.md)
`sails.config.session`
======================

Configuration for Sails' built-in session support.

Sails' default session integration leans heavily on the great work already done by Express and Connect, but also adds a bit of its own special sauce by hooking into the request interpreter. This allows Sails to access and auto-save any changes your code makes to `req.session` when handling a virtual request from Socket.IO. Most importantly, it means you can just write code that uses `req.session` in the way you might be used to from Express or Connect, whether your controller actions are designed to handle HTTP requests, WebSocket messages, or both.

### Properties

| Property | Type | Default | Details |
| --- | --- | --- | --- |
| `adapter` |  | `undefined` | If left unspecified, Sails will use the default memory store bundled in the underlying session middleware. This is fine for development, but in production, you _must_ pass in the name of an installed scalable session store module instead (e.g. `@sailshq/connect-redis`). See [Production config](https://sailsjs.com/documentation/reference/configuration/sails-config-session#?production-config) below for details. |
| `name` |  | `sails.sid` | The name of the session ID cookie to set in the response (and read from in the request) when sessions are enabled (which is the case by default for Sails apps). If you are running multiple different Sails apps from the same shared cookie namespace (i.e. the top-level DNS domain, like `frog-enthusiasts.net`), you must be especially careful to configure separate unique keys for each separate app, otherwise the wrong cookie could be used. |
| `secret` |  | _n/a_ | This session secret is automatically generated when your new app is created. Care should be taken any time this secret is changed in production, as doing so will invalidate the session cookies of your users, forcing them to log in again. Note that this is also used as the "cookie secret" for signed cookies. |
| `cookie` |  | _see [below](https://sailsjs.com/documentation/reference/configuration/sails-config-session#?the-session-id-cookie)_ | Configuration for the session ID cookie, including `maxAge`, `secure`, and more. See [below](https://sailsjs.com/documentation/reference/configuration/sails-config-session#?the-session-id-cookie) for more info. |
| `isSessionDisabled` |  | (see details) | A function to be run for every request which, if it returns a [“truthy” value](https://developer.mozilla.org/en-US/docs/Glossary/Truthy), will cause session support to be disabled for the request (i.e. `req.session` will not exist). By default, this function will check the request path against the [sails.LOOKS_LIKE_ASSET_RX](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-looks-like-asset-rx) regular expression, effectively disabling session support when requesting [assets](https://sailsjs.com/documentation/concepts/assets). |

### Advanced session config

If you are using Redis as a session store in development, additional configuration options are available. Most apps can use Sails' default Redis support as described [here](https://sailsjs.com/documentation/concepts/sessions#?using-redis-as-the-session-store), but some advanced use cases may include the following optional config:

| Property | Type | Default | Details |
| --- | --- | --- | --- |
| `url` |  | `undefined` | The URL of the Redis instance to connect to. This may include one or more of the other settings below, e.g. `redis://:mypass@myredishost.com:1234/5` would indicate a `host` of `myredishost.com`, a `port` of `1234`, a `pass` of `mypass` and a `db` of `5`. In general, you should use either `url` or a combination of the settings below, to avoid confusion. |
| `host` |  | `'127.0.0.1'` | Hostname of your Redis instance. If a `url` setting is configured, this setting will be ignored. |
| `port` |  | `6379` | Port of your Redis instance. If a `url` setting is configured, this setting will be ignored. |
| `pass` |  | `undefined` | The password for your Redis instance. Leave blank if you are not using a password. If a `url` setting is configured that includes a password, this setting will override the password in `url`. |
| `db` |  | `undefined` | The index of the database to use within your Redis instance. If specified, must be an integer. _(On typical Redis setups, this will be a number between 0 and 15.)_ If a `url` setting is configured that includes a db, this setting will override the db in `url`. |
| `client` |  | `undefined` | An already-connected Redis client to use. If provided, any `url`, `host` and `port` settings will be ignored. This setting is useful if you have a Redis Sentinel setup and need to connect using a module like [`ioredis`](https://www.npmjs.com/package/ioredis) |
| `onRedisDisconnect` |  | `undefined` | An optional function for Sails to call if the Redis connection is dropped. Useful for placing your site in a temporary maintenance mode or "panic mode" (see [sails-hook-panic-mode](https://www.npmjs.com/package/sails-hook-panic-mode) for an example). |
| `onRedisReconnect` |  | `undefined` | An optional function for Sails to call if a previously-dropped Redis connection is restored (see `onDisconnect` above). |
| `handleConstructingSessionStore` |  | `undefined` | An optional override function for Sails to call instead of the standard session store construction behavior. To use this setting, please first read and understand the [relevant source code](https://github.com/balderdashy/sails/blob/master/lib/hooks/session/index.js#L415). |

> Note: `onRedisDisconnect` and `onRedisReconnect` will only be called for Redis clients that are created by Sails for you; if you provide your own Redis client (see the `client` option above), these functions will _not_ be called automatically in the case of a disconnect or reconnect.

##### Using other session stores

Any session adapter written for Connect/Express works in Sails, as long as you use a compatible version.

The recommended production session store for Sails.js is Redis... but we realize that, for some apps, that isn't an option. Fortunately, Sails.js supports almost any Connect/Express-compatible session store-- meaning you can store your sessions almost anywhere, whether that's Mongo, on the local filesystem, or even in a relational database. Check out the community session stores for Sails.js, Express, and Connect [available on NPM](https://www.npmjs.com/search?q=connect%20session-).

### The session ID cookie

The built-in session integration in Sails works by using a session ID cookie. This cookie is [HTTP-only](https://www.owasp.org/index.php/HttpOnly) (as safeguard against [XSS exploits](https://sailsjs.com/documentation/concepts/security/xss)), and by default, is set with the name "sails.sid".

##### The "__Host-" prefix

By default, cookies have no integrity against same-site attackers.

In production enviroments, we recommend that you prefix the "name" of your cookie (`sails.config.session.name`) with "__Host-" to limit the scope of your cookie to a single origin.

You can read more about the "__Host-" prefix [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#attributes).

```
session: {
  name: '__Host-sails.sid'
}
```

> Note: Adding this prefix requires the ["secure" flag](https://sailsjs.com/the-secure-flag) to be set to `true`.

##### Expiration

The maximum age / expiration of your app's session ID cookie can be set as a number of milliseconds.

For example, to log users out after 24 hours:

```
session: {
  cookie: {
    maxAge: 24 * 60 * 60 * 1000
  }
}
```

Otherwise, by default, this option is set as `null`, meaning that session ID cookies will not send any kind of ["Expires" or "Max Age" header](https://en.wikipedia.org/wiki/HTTP_cookie) and will last only for as long as a user's web browser is open.

##### The "secure" flag

Whether to set the ["Secure" flag](https://www.owasp.org/index.php/SecureFlag) on the session ID cookie.

```
session: {
  cookie: {
    secure: true
  }
}
```

During development, when you are not using HTTPS, you should leave `sails.config.session.cookie.secure` as undefined (the default).

But in production, you'll want to set it to `true`. This instructs web browsers that they should refuse to send back the session ID cookie _except_ over a secure protocol (`https://`).

> **Note:** If you are using HTTPS behind a proxy/load balancer—for example, on a PaaS like Heroku—then you should still set `secure: true`. But note that, in order for sessions to work with `secure` enabled, you will _also_ need to set another option called [`sails.config.http.trustProxy`](https://sailsjs.com/documentation/reference/configuration/sails-config-http).

##### Do I need an SSL certificate?

In production? Yes.

If you are relying on Sails's built-in session integration, please **always use an SSL certificate in production.** Otherwise, the session ID cookie (or any other secure data) could be transmitted in plain-text, which would make it possible for an attacker in a coffee shop to eavesdrop on one of your authenticated user's HTTP requests, intercept their session ID cookie, then masquerade as them to wreak havoc.

Also realize that, even if you have an SSL certificate, and you always redirect `http://` to `https://`, for _all_ of your subdomains, it is still important to set `secure: true`. (Because without it, even if you redirect all HTTP traffic immediately, that _very first request_ will still have been made over `http://`, and thus would have transmitted the session ID cookie in plain text.)

##### Advanced options

To see other available options (like "[domain](https://stackoverflow.com/a/7887384/486547)") for configuring the session ID cookie in Sails, see [express-session#cookie](https://github.com/expressjs/session/blob/v1.15.6/README.md#cookie).

### Disabling sessions

Sessions are enabled by default in Sails. To disable sessions in your app, disable the `session` hook by changing your `.sailsrc` file. The process for disabling `session` is identical to the process for [disabling the Grunt hook](https://sailsjs.com/documentation/concepts/assets/disabling-grunt) (just type `session: false` instead of `grunt: false`).

> **Note:** If the session hook is disabled, the session secret configured as `sails.config.session.secret` will still be used to support signed cookies, if relevant. If the session hook is disabled _AND_ no session secret configuration exists for your app (e.g. because you deleted `config/session.js`), then signed cookies will not be usable in your application. To make more advanced changes to this behavior, you can customize any of your app's HTTP middleware manually using [`sails.config.http`](https://sailsjs.com/documentation/reference/configuration/sails-config-http).

### Is something missing?

If you notice something we've missed or could be improved on, please follow [this link](https://github.com/balderdashy/sails/blob/master/docs/reference/sails.config/sails.config.session.md) and submit a pull request to the sails repo. Once we merge it, the changes will be reflected on the website the next time it is deployed.

[![Image 2: Sails logo](https://sailsjs.com/images/logo_sails.png)](https://sailsjs.com/)

![Image 3](https://sailsjs.com/images/icon_search_white.png)

* [Home](https://sailsjs.com/)
* [Get started](https://sailsjs.com/get-started)
* [Support](https://sailsjs.com/support)
* [Documentation](https://sailsjs.com/documentation)
* [Documentation](https://sailsjs.com/documentation)[](https://sailsjs.com/documentation/reference/configuration/sails-config-session)

![Image 4](https://sailsjs.com/images/icon_warning.png)For a better experience on sailsjs.com, [update your browser](https://support.microsoft.com/en-us/help/17621/internet-explorer-downloads).

Check out the official Sails [VS Code extension](https://marketplace.visualstudio.com/items?itemName=Sails.sails-vscode)

[Tweet](https://twitter.com/share)[Follow @sailsjs](https://twitter.com/sailsjs)

Documentation
-------------

[Reference](https://sailsjs.com/documentation/reference)[Concepts](https://sailsjs.com/documentation/concepts)[App structure](https://sailsjs.com/documentation/anatomy)|[Upgrading](https://sailsjs.com/documentation/upgrading)[Contribution guide](https://sailsjs.com/documentation/contributing)|[Tutorials](https://sailsjs.com/documentation/tutorials)[More](https://sailsjs.com/support)

#### Reference

* [Application](https://sailsjs.com/documentation/reference/application)
  * [Advanced usage](https://sailsjs.com/documentation/reference/application/advanced-usage)
    * [Lifecycle](https://sailsjs.com/documentation/reference/application/advanced-usage/lifecycle)
    * [sails.LOOKS_LIKE_ASSET_RX](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-looks-like-asset-rx)
    * [sails.getActions()](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-get-actions)
    * [sails.getRouteFor()](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-get-route-for)
    * [sails.lift()](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-lift)
    * [sails.load()](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-load)
    * [sails.lower()](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-lower)
    * [sails.registerAction()](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-register-action)
    * [sails.registerActionMiddleware()](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-register-action-middleware)
    * [sails.reloadActions()](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-reload-actions)
    * [sails.renderView()](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-render-view)
    * [sails.request()](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-request)
    * [sails.getBaseUrl()](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-get-base-url)

  * [sails.config.custom](https://sailsjs.com/documentation/reference/application/sails-config-custom)
  * [sails.getDatastore()](https://sailsjs.com/documentation/reference/application/sails-get-datastore)
  * [sails.getUrlFor()](https://sailsjs.com/documentation/reference/application/sails-get-url-for)
  * [sails.log()](https://sailsjs.com/documentation/reference/application/sails-log)

* [Blueprint API](https://sailsjs.com/documentation/reference/blueprint-api)
  * [add to](https://sailsjs.com/documentation/reference/blueprint-api/add-to)
  * [create](https://sailsjs.com/documentation/reference/blueprint-api/create)
  * [destroy](https://sailsjs.com/documentation/reference/blueprint-api/destroy)
  * [find one](https://sailsjs.com/documentation/reference/blueprint-api/find-one)
  * [find where](https://sailsjs.com/documentation/reference/blueprint-api/find-where)
  * [populate where](https://sailsjs.com/documentation/reference/blueprint-api/populate-where)
  * [remove from](https://sailsjs.com/documentation/reference/blueprint-api/remove-from)
  * [replace](https://sailsjs.com/documentation/reference/blueprint-api/replace)
  * [update](https://sailsjs.com/documentation/reference/blueprint-api/update)

* [Command-line interface](https://sailsjs.com/documentation/reference/command-line-interface)
  * [sails --version](https://sailsjs.com/documentation/reference/command-line-interface/sails-version)
  * [sails console](https://sailsjs.com/documentation/reference/command-line-interface/sails-console)
  * [sails debug](https://sailsjs.com/documentation/reference/command-line-interface/sails-debug)
  * [sails generate](https://sailsjs.com/documentation/reference/command-line-interface/sails-generate)
  * [sails inspect](https://sailsjs.com/documentation/reference/command-line-interface/sails-inspect)
  * [sails lift](https://sailsjs.com/documentation/reference/command-line-interface/sails-lift)
  * [sails new](https://sailsjs.com/documentation/reference/command-line-interface/sails-new)

* [Configuration](https://sailsjs.com/documentation/reference/configuration)
  * [sails.config.*](https://sailsjs.com/documentation/reference/configuration/sails-config)
  * [sails.config.blueprints](https://sailsjs.com/documentation/reference/configuration/sails-config-blueprints)
  * [sails.config.bootstrap()](https://sailsjs.com/documentation/reference/configuration/sails-config-bootstrap)
  * [sails.config.custom](https://sailsjs.com/documentation/reference/configuration/sails-config-custom)
  * [sails.config.datastores](https://sailsjs.com/documentation/reference/configuration/sails-config-datastores)
  * [sails.config.globals](https://sailsjs.com/documentation/reference/configuration/sails-config-globals)
  * [sails.config.http](https://sailsjs.com/documentation/reference/configuration/sails-config-http)
  * [sails.config.i18n](https://sailsjs.com/documentation/reference/configuration/sails-config-i-18-n)
  * [sails.config.log](https://sailsjs.com/documentation/reference/configuration/sails-config-log)
  * [sails.config.models](https://sailsjs.com/documentation/reference/configuration/sails-config-models)
  * [sails.config.policies](https://sailsjs.com/documentation/reference/configuration/sails-config-policies)
  * [sails.config.routes](https://sailsjs.com/documentation/reference/configuration/sails-config-routes)
  * [sails.config.security](https://sailsjs.com/documentation/reference/configuration/sails-config-security)
  * [sails.config.session](https://sailsjs.com/documentation/reference/configuration/sails-config-session)
  * [sails.config.sockets](https://sailsjs.com/documentation/reference/configuration/sails-config-sockets)
  * [sails.config.views](https://sailsjs.com/documentation/reference/configuration/sails-config-views)

* [Request (`req`)](https://sailsjs.com/documentation/reference/request-req)
  * [req._startTime](https://sailsjs.com/documentation/reference/request-req/req-start-time)
  * [req.body](https://sailsjs.com/documentation/reference/request-req/req-body)
  * [req.cookies](https://sailsjs.com/documentation/reference/request-req/req-cookies)
  * [req.fresh](https://sailsjs.com/documentation/reference/request-req/req-fresh)
  * [req.headers](https://sailsjs.com/documentation/reference/request-req/req-headers)
  * [req.hostname](https://sailsjs.com/documentation/reference/request-req/req-hostname)
  * [req.ip](https://sailsjs.com/documentation/reference/request-req/req-ip)
  * [req.ips](https://sailsjs.com/documentation/reference/request-req/req-ips)
  * [req.isSocket](https://sailsjs.com/documentation/reference/request-req/req-is-socket)
  * [req.method](https://sailsjs.com/documentation/reference/request-req/req-method)
  * [req.options](https://sailsjs.com/documentation/reference/request-req/req-options)
  * [req.originalUrl](https://sailsjs.com/documentation/reference/request-req/req-original-url)
  * [req.params](https://sailsjs.com/documentation/reference/request-req/req-params)
  * [req.path](https://sailsjs.com/documentation/reference/request-req/req-path)
  * [req.protocol](https://sailsjs.com/documentation/reference/request-req/req-protocol)
  * [req.query](https://sailsjs.com/documentation/reference/request-req/req-query)
  * [req.secure](https://sailsjs.com/documentation/reference/request-req/req-secure)
  * [req.signedCookies](https://sailsjs.com/documentation/reference/request-req/req-signed-cookies)
  * [req.socket](https://sailsjs.com/documentation/reference/request-req/req-socket)
  * [req.subdomains](https://sailsjs.com/documentation/reference/request-req/req-subdomains)
  * [req.url](https://sailsjs.com/documentation/reference/request-req/req-url)
  * [req.wantsJSON](https://sailsjs.com/documentation/reference/request-req/req-wants-json)
  * [req.xhr](https://sailsjs.com/documentation/reference/request-req/req-xhr)
  * [req.accepts()](https://sailsjs.com/documentation/reference/request-req/req-accepts)
  * [req.acceptsCharsets()](https://sailsjs.com/documentation/reference/request-req/req-accepts-charsets)
  * [req.acceptsLanguages()](https://sailsjs.com/documentation/reference/request-req/req-accepts-languages)
  * [req.allParams()](https://sailsjs.com/documentation/reference/request-req/req-all-params)
  * [req.file()](https://sailsjs.com/documentation/reference/request-req/req-file)
  * [req.get()](https://sailsjs.com/documentation/reference/request-req/req-get)
  * [req.is()](https://sailsjs.com/documentation/reference/request-req/req-is)
  * [req.param()](https://sailsjs.com/documentation/reference/request-req/req-param)
  * [req.setLocale()](https://sailsjs.com/documentation/reference/request-req/req-set-locale)
  * [req.setTimeout()](https://sailsjs.com/documentation/reference/request-req/req-set-timeout)
  * [req.host](https://sailsjs.com/documentation/reference/request-req/req-host)

* [Response (`res`)](https://sailsjs.com/documentation/reference/response-res)
  * [res.attachment()](https://sailsjs.com/documentation/reference/response-res/res-attachment)
  * [res.badRequest()](https://sailsjs.com/documentation/reference/response-res/res-bad-request)
  * [res.clearCookie()](https://sailsjs.com/documentation/reference/response-res/res-clear-cookie)
  * [res.cookie()](https://sailsjs.com/documentation/reference/response-res/res-cookie)
  * [res.forbidden()](https://sailsjs.com/documentation/reference/response-res/res-forbidden)
  * [res.get()](https://sailsjs.com/documentation/reference/response-res/res-get)
  * [res.json()](https://sailsjs.com/documentation/reference/response-res/res-json)
  * [res.jsonp()](https://sailsjs.com/documentation/reference/response-res/res-jsonp)
  * [res.location()](https://sailsjs.com/documentation/reference/response-res/res-location)
  * [res.notFound()](https://sailsjs.com/documentation/reference/response-res/res-not-found)
  * [res.ok()](https://sailsjs.com/documentation/reference/response-res/res-ok)
  * [res.redirect()](https://sailsjs.com/documentation/reference/response-res/res-redirect)
  * [res.send()](https://sailsjs.com/documentation/reference/response-res/res-send)
  * [res.serverError()](https://sailsjs.com/documentation/reference/response-res/res-server-error)
  * [res.set()](https://sailsjs.com/documentation/reference/response-res/res-set)
  * [res.status()](https://sailsjs.com/documentation/reference/response-res/res-status)
  * [res.type()](https://sailsjs.com/documentation/reference/response-res/res-type)
  * [res.view()](https://sailsjs.com/documentation/reference/response-res/res-view)
  * [res.negotiate()](https://sailsjs.com/documentation/reference/response-res/res-negotiate)

* [Waterline (ORM)](https://sailsjs.com/documentation/reference/waterline-orm)
  * [Datastores](https://sailsjs.com/documentation/reference/waterline-orm/datastores)
    * [.driver](https://sailsjs.com/documentation/reference/waterline-orm/datastores/driver)
    * [.manager](https://sailsjs.com/documentation/reference/waterline-orm/datastores/manager)
    * [.leaseConnection()](https://sailsjs.com/documentation/reference/waterline-orm/datastores/lease-connection)
    * [.sendNativeQuery()](https://sailsjs.com/documentation/reference/waterline-orm/datastores/send-native-query)
    * [.transaction()](https://sailsjs.com/documentation/reference/waterline-orm/datastores/transaction)

  * [Models](https://sailsjs.com/documentation/reference/waterline-orm/models)
    * [.addToCollection()](https://sailsjs.com/documentation/reference/waterline-orm/models/add-to-collection)
    * [.archive()](https://sailsjs.com/documentation/reference/waterline-orm/models/archive)
    * [.archiveOne()](https://sailsjs.com/documentation/reference/waterline-orm/models/archive-one)
    * [.avg()](https://sailsjs.com/documentation/reference/waterline-orm/models/avg)
    * [.count()](https://sailsjs.com/documentation/reference/waterline-orm/models/count)
    * [.create()](https://sailsjs.com/documentation/reference/waterline-orm/models/create)
    * [.createEach()](https://sailsjs.com/documentation/reference/waterline-orm/models/create-each)
    * [.destroy()](https://sailsjs.com/documentation/reference/waterline-orm/models/destroy)
    * [.destroyOne()](https://sailsjs.com/documentation/reference/waterline-orm/models/destroy-one)
    * [.find()](https://sailsjs.com/documentation/reference/waterline-orm/models/find)
    * [.findOne()](https://sailsjs.com/documentation/reference/waterline-orm/models/find-one)
    * [.findOrCreate()](https://sailsjs.com/documentation/reference/waterline-orm/models/find-or-create)
    * [.getDatastore()](https://sailsjs.com/documentation/reference/waterline-orm/models/get-datastore)
    * [.removeFromCollection()](https://sailsjs.com/documentation/reference/waterline-orm/models/remove-from-collection)
    * [.replaceCollection()](https://sailsjs.com/documentation/reference/waterline-orm/models/replace-collection)
    * [.stream()](https://sailsjs.com/documentation/reference/waterline-orm/models/stream)
    * [.sum()](https://sailsjs.com/documentation/reference/waterline-orm/models/sum)
    * [.update()](https://sailsjs.com/documentation/reference/waterline-orm/models/update)
    * [.updateOne()](https://sailsjs.com/documentation/reference/waterline-orm/models/update-one)
    * [.validate()](https://sailsjs.com/documentation/reference/waterline-orm/models/validate)
    * [.native()](https://sailsjs.com/documentation/reference/waterline-orm/models/native)
    * [.query()](https://sailsjs.com/documentation/reference/waterline-orm/models/query)

  * [Queries](https://sailsjs.com/documentation/reference/waterline-orm/queries)
    * [.catch()](https://sailsjs.com/documentation/reference/waterline-orm/queries/catch)
    * [.decrypt()](https://sailsjs.com/documentation/reference/waterline-orm/queries/decrypt)
    * [.exec()](https://sailsjs.com/documentation/reference/waterline-orm/queries/exec)
    * [.fetch()](https://sailsjs.com/documentation/reference/waterline-orm/queries/fetch)
    * [.intercept()](https://sailsjs.com/documentation/reference/waterline-orm/queries/intercept)
    * [.limit()](https://sailsjs.com/documentation/reference/waterline-orm/queries/limit)
    * [.meta()](https://sailsjs.com/documentation/reference/waterline-orm/queries/meta)
    * [.populate()](https://sailsjs.com/documentation/reference/waterline-orm/queries/populate)
    * [.skip()](https://sailsjs.com/documentation/reference/waterline-orm/queries/skip)
    * [.sort()](https://sailsjs.com/documentation/reference/waterline-orm/queries/sort)
    * [.then()](https://sailsjs.com/documentation/reference/waterline-orm/queries/then)
    * [.tolerate()](https://sailsjs.com/documentation/reference/waterline-orm/queries/tolerate)
    * [.toPromise()](https://sailsjs.com/documentation/reference/waterline-orm/queries/to-promise)
    * [.usingConnection()](https://sailsjs.com/documentation/reference/waterline-orm/queries/using-connection)
    * [.where()](https://sailsjs.com/documentation/reference/waterline-orm/queries/where)

  * [Records](https://sailsjs.com/documentation/reference/waterline-orm/records)
    * [.toJSON()](https://sailsjs.com/documentation/reference/waterline-orm/records/to-json)

* [WebSockets](https://sailsjs.com/documentation/reference/web-sockets)
  * [Resourceful PubSub](https://sailsjs.com/documentation/reference/web-sockets/resourceful-pub-sub)
    * [.getRoomName()](https://sailsjs.com/documentation/reference/web-sockets/resourceful-pub-sub/get-room-name)
    * [.publish()](https://sailsjs.com/documentation/reference/web-sockets/resourceful-pub-sub/publish)
    * [.subscribe()](https://sailsjs.com/documentation/reference/web-sockets/resourceful-pub-sub/subscribe)
    * [.unsubscribe()](https://sailsjs.com/documentation/reference/web-sockets/resourceful-pub-sub/unsubscribe)

  * [sails.sockets](https://sailsjs.com/documentation/reference/web-sockets/sails-sockets)
    * [.addRoomMembersToRooms()](https://sailsjs.com/documentation/reference/web-sockets/sails-sockets/add-room-members-to-rooms)
    * [.blast()](https://sailsjs.com/documentation/reference/web-sockets/sails-sockets/blast)
    * [.broadcast()](https://sailsjs.com/documentation/reference/web-sockets/sails-sockets/broadcast)
    * [.getId()](https://sailsjs.com/documentation/reference/web-sockets/sails-sockets/get-id)
    * [.join()](https://sailsjs.com/documentation/reference/web-sockets/sails-sockets/join)
    * [.leave()](https://sailsjs.com/documentation/reference/web-sockets/sails-sockets/leave)
    * [.leaveAll()](https://sailsjs.com/documentation/reference/web-sockets/sails-sockets/leave-all)
    * [.removeRoomMembersFromRooms()](https://sailsjs.com/documentation/reference/web-sockets/sails-sockets/remove-room-members-from-rooms)
    * [sails.sockets.id()](https://sailsjs.com/documentation/reference/web-sockets/sails-sockets/sails-sockets-id)

  * [Socket client](https://sailsjs.com/documentation/reference/web-sockets/socket-client)
    * [io.sails](https://sailsjs.com/documentation/reference/web-sockets/socket-client/io-sails)
    * [io.socket](https://sailsjs.com/documentation/reference/web-sockets/socket-client/io-socket)
    * [SailsSocket](https://sailsjs.com/documentation/reference/web-sockets/socket-client/sails-socket)
      * [Methods](https://sailsjs.com/documentation/reference/web-sockets/socket-client/sails-socket/methods)
      * [Properties](https://sailsjs.com/documentation/reference/web-sockets/socket-client/sails-socket/properties)

    * [io.socket.delete()](https://sailsjs.com/documentation/reference/web-sockets/socket-client/io-socket-delete)
    * [io.socket.get()](https://sailsjs.com/documentation/reference/web-sockets/socket-client/io-socket-get)
    * [io.socket.off()](https://sailsjs.com/documentation/reference/web-sockets/socket-client/io-socket-off)
    * [io.socket.on()](https://sailsjs.com/documentation/reference/web-sockets/socket-client/io-socket-on)
    * [io.socket.patch()](https://sailsjs.com/documentation/reference/web-sockets/socket-client/io-socket-patch)
    * [io.socket.post()](https://sailsjs.com/documentation/reference/web-sockets/socket-client/io-socket-post)
    * [io.socket.put()](https://sailsjs.com/documentation/reference/web-sockets/socket-client/io-socket-put)
    * [io.socket.request()](https://sailsjs.com/documentation/reference/web-sockets/socket-client/io-socket-request)

[![Image 5: Sails logo](https://sailsjs.com/images/logo_sails.png)](https://sailsjs.com/)

#### Reference

* [Application](https://sailsjs.com/documentation/reference/application)
  * [Advanced usage](https://sailsjs.com/documentation/reference/application/advanced-usage)
    * [Lifecycle](https://sailsjs.com/documentation/reference/application/advanced-usage/lifecycle)
    * [sails.LOOKS_LIKE_ASSET_RX](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-looks-like-asset-rx)
    * [sails.getActions()](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-get-actions)
    * [sails.getRouteFor()](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-get-route-for)
    * [sails.lift()](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-lift)
    * [sails.load()](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-load)
    * [sails.lower()](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-lower)
    * [sails.registerAction()](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-register-action)
    * [sails.registerActionMiddleware()](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-register-action-middleware)
    * [sails.reloadActions()](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-reload-actions)
    * [sails.renderView()](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-render-view)
    * [sails.request()](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-request)
    * [sails.getBaseUrl()](https://sailsjs.com/documentation/reference/application/advanced-usage/sails-get-base-url)

  * [sails.config.custom](https://sailsjs.com/documentation/reference/application/sails-config-custom)
  * [sails.getDatastore()](https://sailsjs.com/documentation/reference/application/sails-get-datastore)
  * [sails.getUrlFor()](https://sailsjs.com/documentation/reference/application/sails-get-url-for)
  * [sails.log()](https://sailsjs.com/documentation/reference/application/sails-log)

* [Blueprint API](https://sailsjs.com/documentation/reference/blueprint-api)
  * [add to](https://sailsjs.com/documentation/reference/blueprint-api/add-to)
  * [create](https://sailsjs.com/documentation/reference/blueprint-api/create)
  * [destroy](https://sailsjs.com/documentation/reference/blueprint-api/destroy)
  * [find one](https://sailsjs.com/documentation/reference/blueprint-api/find-one)
  * [find where](https://sailsjs.com/documentation/reference/blueprint-api/find-where)
  * [populate where](https://sailsjs.com/documentation/reference/blueprint-api/populate-where)
  * [remove from](https://sailsjs.com/documentation/reference/blueprint-api/remove-from)
  * [replace](https://sailsjs.com/documentation/reference/blueprint-api/replace)
  * [update](https://sailsjs.com/documentation/reference/blueprint-api/update)

* [Command-line interface](https://sailsjs.com/documentation/reference/command-line-interface)
  * [sails --version](https://sailsjs.com/documentation/reference/command-line-interface/sails-version)
  * [sails console](https://sailsjs.com/documentation/reference/command-line-interface/sails-console)
  * [sails debug](https://sailsjs.com/documentation/reference/command-line-interface/sails-debug)
  * [sails generate](https://sailsjs.com/documentation/reference/command-line-interface/sails-generate)
  * [sails inspect](https://sailsjs.com/documentation/reference/command-line-interface/sails-inspect)
  * [sails lift](https://sailsjs.com/documentation/reference/command-line-interface/sails-lift)
  * [sails new](https://sailsjs.com/documentation/reference/command-line-interface/sails-new)

* [Configuration](https://sailsjs.com/documentation/reference/configuration)
  * [sails.config.*](https://sailsjs.com/documentation/reference/configuration/sails-config)
  * [sails.config.blueprints](https://sailsjs.com/documentation/reference/configuration/sails-config-blueprints)
  * [sails.config.bootstrap()](https://sailsjs.com/documentation/reference/configuration/sails-config-bootstrap)
  * [sails.config.custom](https://sailsjs.com/documentation/reference/configuration/sails-config-custom)
  * [sails.config.datastores](https://sailsjs.com/documentation/reference/configuration/sails-config-datastores)
  * [sails.config.globals](https://sailsjs.com/documentation/reference/configuration/sails-config-globals)
  * [sails.config.http](https://sailsjs.com/documentation/reference/configuration/sails-config-http)
  * [sails.config.i18n](https://sailsjs.com/documentation/reference/configuration/sails-config-i-18-n)
  * [sails.config.log](https://sailsjs.com/documentation/reference/configuration/sails-config-log)
  * [sails.config.models](https://sailsjs.com/documentation/reference/configuration/sails-config-models)
  * [sails.config.policies](https://sailsjs.com/documentation/reference/configuration/sails-config-policies)
  * [sails.config.routes](https://sailsjs.com/documentation/reference/configuration/sails-config-routes)
  * [sails.config.security](https://sailsjs.com/documentation/reference/configuration/sails-config-security)
  * [sails.config.session](https://sailsjs.com/documentation/reference/configuration/sails-config-session)
  * [sails.config.sockets](https://sailsjs.com/documentation/reference/configuration/sails-config-sockets)
  * [sails.config.views](https://sailsjs.com/documentation/reference/configuration/sails-config-views)

* [Request (`req`)](https://sailsjs.com/documentation/reference/request-req)
  * [req._startTime](https://sailsjs.com/documentation/reference/request-req/req-start-time)
  * [req.body](https://sailsjs.com/documentation/reference/request-req/req-body)
  * [req.cookies](https://sailsjs.com/documentation/reference/request-req/req-cookies)
  * [req.fresh](https://sailsjs.com/documentation/reference/request-req/req-fresh)
  * [req.headers](https://sailsjs.com/documentation/reference/request-req/req-headers)
  * [req.hostname](https://sailsjs.com/documentation/reference/request-req/req-hostname)
  * [req.ip](https://sailsjs.com/documentation/reference/request-req/req-ip)
  * [req.ips](https://sailsjs.com/documentation/reference/request-req/req-ips)
  * [req.isSocket](https://sailsjs.com/documentation/reference/request-req/req-is-socket)
  * [req.method](https://sailsjs.com/documentation/reference/request-req/req-method)
  * [req.options](https://sailsjs.com/documentation/reference/request-req/req-options)
  * [req.originalUrl](https://sailsjs.com/documentation/reference/request-req/req-original-url)
  * [req.params](https://sailsjs.com/documentation/reference/request-req/req-params)
  * [req.path](https://sailsjs.com/documentation/reference/request-req/req-path)
  * [req.protocol](https://sailsjs.com/documentation/reference/request-req/req-protocol)
  * [req.query](https://sailsjs.com/documentation/reference/request-req/req-query)
  * [req.secure](https://sailsjs.com/documentation/reference/request-req/req-secure)
  * [req.signedCookies](https://sailsjs.com/documentation/reference/request-req/req-signed-cookies)
  * [req.socket](https://sailsjs.com/documentation/reference/request-req/req-socket)
  * [req.subdomains](https://sailsjs.com/documentation/reference/request-req/req-subdomains)
  * [req.url](https://sailsjs.com/documentation/reference/request-req/req-url)
  * [req.wantsJSON](https://sailsjs.com/documentation/reference/request-req/req-wants-json)
  * [req.xhr](https://sailsjs.com/documentation/reference/request-req/req-xhr)
  * [req.accepts()](https://sailsjs.com/documentation/reference/request-req/req-accepts)
  * [req.acceptsCharsets()](https://sailsjs.com/documentation/reference/request-req/req-accepts-charsets)
  * [req.acceptsLanguages()](https://sailsjs.com/documentation/reference/request-req/req-accepts-languages)
  * [req.allParams()](https://sailsjs.com/documentation/reference/request-req/req-all-params)
  * [req.file()](https://sailsjs.com/documentation/reference/request-req/req-file)
  * [req.get()](https://sailsjs.com/documentation/reference/request-req/req-get)
  * [req.is()](https://sailsjs.com/documentation/reference/request-req/req-is)
  * [req.param()](https://sailsjs.com/documentation/reference/request-req/req-param)
  * [req.setLocale()](https://sailsjs.com/documentation/reference/request-req/req-set-locale)
  * [req.setTimeout()](https://sailsjs.com/documentation/reference/request-req/req-set-timeout)
  * [req.host](https://sailsjs.com/documentation/reference/request-req/req-host)

* [Response (`res`)](https://sailsjs.com/documentation/reference/response-res)
  * [res.attachment()](https://sailsjs.com/documentation/reference/response-res/res-attachment)
  * [res.badRequest()](https://sailsjs.com/documentation/reference/response-res/res-bad-request)
  * [res.clearCookie()](https://sailsjs.com/documentation/reference/response-res/res-clear-cookie)
  * [res.cookie()](https://sailsjs.com/documentation/reference/response-res/res-cookie)
  * [res.forbidden()](https://sailsjs.com/documentation/reference/response-res/res-forbidden)
  * [res.get()](https://sailsjs.com/documentation/reference/response-res/res-get)
  * [res.json()](https://sailsjs.com/documentation/reference/response-res/res-json)
  * [res.jsonp()](https://sailsjs.com/documentation/reference/response-res/res-jsonp)
  * [res.location()](https://sailsjs.com/documentation/reference/response-res/res-location)
  * [res.notFound()](https://sailsjs.com/documentation/reference/response-res/res-not-found)
  * [res.ok()](https://sailsjs.com/documentation/reference/response-res/res-ok)
  * [res.redirect()](https://sailsjs.com/documentation/reference/response-res/res-redirect)
  * [res.send()](https://sailsjs.com/documentation/reference/response-res/res-send)
  * [res.serverError()](https://sailsjs.com/documentation/reference/response-res/res-server-error)
  * [res.set()](https://sailsjs.com/documentation/reference/response-res/res-set)
  * [res.status()](https://sailsjs.com/documentation/reference/response-res/res-status)
  * [res.type()](https://sailsjs.com/documentation/reference/response-res/res-type)
  * [res.view()](https://sailsjs.com/documentation/reference/response-res/res-view)
  * [res.negotiate()](https://sailsjs.com/documentation/reference/response-res/res-negotiate)

* [Waterline (ORM)](https://sailsjs.com/documentation/reference/waterline-orm)
  * [Datastores](https://sailsjs.com/documentation/reference/waterline-orm/datastores)
    * [.driver](https://sailsjs.com/documentation/reference/waterline-orm/datastores/driver)
    * [.manager](https://sailsjs.com/documentation/reference/waterline-orm/datastores/manager)
    * [.leaseConnection()](https://sailsjs.com/documentation/reference/waterline-orm/datastores/lease-connection)
    * [.sendNativeQuery()](https://sailsjs.com/documentation/reference/waterline-orm/datastores/send-native-query)
    * [.transaction()](https://sailsjs.com/documentation/reference/waterline-orm/datastores/transaction)

  * [Models](https://sailsjs.com/documentation/reference/waterline-orm/models)
    * [.addToCollection()](https://sailsjs.com/documentation/reference/waterline-orm/models/add-to-collection)
    * [.archive()](https://sailsjs.com/documentation/reference/waterline-orm/models/archive)
    * [.archiveOne()](https://sailsjs.com/documentation/reference/waterline-orm/models/archive-one)
    * [.avg()](https://sailsjs.com/documentation/reference/waterline-orm/models/avg)
    * [.count()](https://sailsjs.com/documentation/reference/waterline-orm/models/count)
    * [.create()](https://sailsjs.com/documentation/reference/waterline-orm/models/create)
    * [.createEach()](https://sailsjs.com/documentation/reference/waterline-orm/models/create-each)
    * [.destroy()](https://sailsjs.com/documentation/reference/waterline-orm/models/destroy)
    * [.destroyOne()](https://sailsjs.com/documentation/reference/waterline-orm/models/destroy-one)
    * [.find()](https://sailsjs.com/documentation/reference/waterline-orm/models/find)
    * [.findOne()](https://sailsjs.com/documentation/reference/waterline-orm/models/find-one)
    * [.findOrCreate()](https://sailsjs.com/documentation/reference/waterline-orm/models/find-or-create)
    * [.getDatastore()](https://sailsjs.com/documentation/reference/waterline-orm/models/get-datastore)
    * [.removeFromCollection()](https://sailsjs.com/documentation/reference/waterline-orm/models/remove-from-collection)
    * [.replaceCollection()](https://sailsjs.com/documentation/reference/waterline-orm/models/replace-collection)
    * [.stream()](https://sailsjs.com/documentation/reference/waterline-orm/models/stream)
    * [.sum()](https://sailsjs.com/documentation/reference/waterline-orm/models/sum)
    * [.update()](https://sailsjs.com/documentation/reference/waterline-orm/models/update)
    * [.updateOne()](https://sailsjs.com/documentation/reference/waterline-orm/models/update-one)
    * [.validate()](https://sailsjs.com/documentation/reference/waterline-orm/models/validate)
    * [.native()](https://sailsjs.com/documentation/reference/waterline-orm/models/native)
    * [.query()](https://sailsjs.com/documentation/reference/waterline-orm/models/query)

  * [Queries](https://sailsjs.com/documentation/reference/waterline-orm/queries)
    * [.catch()](https://sailsjs.com/documentation/reference/waterline-orm/queries/catch)
    * [.decrypt()](https://sailsjs.com/documentation/reference/waterline-orm/queries/decrypt)
    * [.exec()](https://sailsjs.com/documentation/reference/waterline-orm/queries/exec)
    * [.fetch()](https://sailsjs.com/documentation/reference/waterline-orm/queries/fetch)
    * [.intercept()](https://sailsjs.com/documentation/reference/waterline-orm/queries/intercept)
    * [.limit()](https://sailsjs.com/documentation/reference/waterline-orm/queries/limit)
    * [.meta()](https://sailsjs.com/documentation/reference/waterline-orm/queries/meta)
    * [.populate()](https://sailsjs.com/documentation/reference/waterline-orm/queries/populate)
    * [.skip()](https://sailsjs.com/documentation/reference/waterline-orm/queries/skip)
    * [.sort()](https://sailsjs.com/documentation/reference/waterline-orm/queries/sort)
    * [.then()](https://sailsjs.com/documentation/reference/waterline-orm/queries/then)
    * [.tolerate()](https://sailsjs.com/documentation/reference/waterline-orm/queries/tolerate)
    * [.toPromise()](https://sailsjs.com/documentation/reference/waterline-orm/queries/to-promise)
    * [.usingConnection()](https://sailsjs.com/documentation/reference/waterline-orm/queries/using-connection)
    * [.where()](https://sailsjs.com/documentation/reference/waterline-orm/queries/where)

  * [Records](https://sailsjs.com/documentation/reference/waterline-orm/records)
    * [.toJSON()](https://sailsjs.com/documentation/reference/waterline-orm/records/to-json)

* [WebSockets](https://sailsjs.com/documentation/reference/web-sockets)
  * [Resourceful PubSub](https://sailsjs.com/documentation/reference/web-sockets/resourceful-pub-sub)
    * [.getRoomName()](https://sailsjs.com/documentation/reference/web-sockets/resourceful-pub-sub/get-room-name)
    * [.publish()](https://sailsjs.com/documentation/reference/web-sockets/resourceful-pub-sub/publish)
    * [.subscribe()](https://sailsjs.com/documentation/reference/web-sockets/resourceful-pub-sub/subscribe)
    * [.unsubscribe()](https://sailsjs.com/documentation/reference/web-sockets/resourceful-pub-sub/unsubscribe)

  * [sails.sockets](https://sailsjs.com/documentation/reference/web-sockets/sails-sockets)
    * [.addRoomMembersToRooms()](https://sailsjs.com/documentation/reference/web-sockets/sails-sockets/add-room-members-to-rooms)
    * [.blast()](https://sailsjs.com/documentation/reference/web-sockets/sails-sockets/blast)
    * [.broadcast()](https://sailsjs.com/documentation/reference/web-sockets/sails-sockets/broadcast)
    * [.getId()](https://sailsjs.com/documentation/reference/web-sockets/sails-sockets/get-id)
    * [.join()](https://sailsjs.com/documentation/reference/web-sockets/sails-sockets/join)
    * [.leave()](https://sailsjs.com/documentation/reference/web-sockets/sails-sockets/leave)
    * [.leaveAll()](https://sailsjs.com/documentation/reference/web-sockets/sails-sockets/leave-all)
    * [.removeRoomMembersFromRooms()](https://sailsjs.com/documentation/reference/web-sockets/sails-sockets/remove-room-members-from-rooms)
    * [sails.sockets.id()](https://sailsjs.com/documentation/reference/web-sockets/sails-sockets/sails-sockets-id)

  * [Socket client](https://sailsjs.com/documentation/reference/web-sockets/socket-client)
    * [io.sails](https://sailsjs.com/documentation/reference/web-sockets/socket-client/io-sails)
    * [io.socket](https://sailsjs.com/documentation/reference/web-sockets/socket-client/io-socket)
    * [SailsSocket](https://sailsjs.com/documentation/reference/web-sockets/socket-client/sails-socket)
      * [Methods](https://sailsjs.com/documentation/reference/web-sockets/socket-client/sails-socket/methods)
      * [Properties](https://sailsjs.com/documentation/reference/web-sockets/socket-client/sails-socket/properties)

    * [io.socket.delete()](https://sailsjs.com/documentation/reference/web-sockets/socket-client/io-socket-delete)
    * [io.socket.get()](https://sailsjs.com/documentation/reference/web-sockets/socket-client/io-socket-get)
    * [io.socket.off()](https://sailsjs.com/documentation/reference/web-sockets/socket-client/io-socket-off)
    * [io.socket.on()](https://sailsjs.com/documentation/reference/web-sockets/socket-client/io-socket-on)
    * [io.socket.patch()](https://sailsjs.com/documentation/reference/web-sockets/socket-client/io-socket-patch)
    * [io.socket.post()](https://sailsjs.com/documentation/reference/web-sockets/socket-client/io-socket-post)
    * [io.socket.put()](https://sailsjs.com/documentation/reference/web-sockets/socket-client/io-socket-put)
    * [io.socket.request()](https://sailsjs.com/documentation/reference/web-sockets/socket-client/io-socket-request)

![Image 6](https://sailsjs.com/images/logo_sails.png)

#### Built with Love

The Sails framework is built by a [web & mobile shop in Austin, TX](https://sailsjs.com/about), with the help of our contributors. We created Sails in 2012 to assist us on Node.js projects. Naturally we open-sourced it. We hope it makes your life a little bit easier!

##### Sails

* [What is Sails?](https://sailsjs.com/whats-that)
* [Community](https://sailsjs.com/support)
* [News](https://twitter.com/sailsjs)
* [For business](https://sailsjs.com/contact)

##### About

* [Our company](https://sailsjs.com/about)
* [Security](https://sailsjs.com/security)
* [Legal](https://sailsjs.com/legal)
* [Logos/artwork](https://sailsjs.com/resources)

##### Help

* [Get started](https://sailsjs.com/get-started)
* [Documentation](https://sailsjs.com/documentation)
* [Docs](https://sailsjs.com/documentation)
* [Contribute](https://sailsjs.com/documentation/contributing)
* [Take a class](https://courses.platzi.com/courses/sails-js/)

![Image 7](https://sailsjs.com/images/logo_sails.png)
[© 2012-2026 The Sails Company](https://sailsjs.com/about).

 The Sails framework is free and open-source under the MIT License.

 Illustrations by [Edamame](https://www.edamamedesign.com/).

[](https://twitter.com/sailsjs)[](https://www.facebook.com/sailsjs)[](https://github.com/balderdashy/sails)[](https://www.pinterest.com/sailsjs/)[](http://stackoverflow.com/search?q=sails)
