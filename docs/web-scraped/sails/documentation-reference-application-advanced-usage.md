# Source: https://sailsjs.com/documentation/reference/application/advanced-usage

Title: Advanced usage

URL Source: https://sailsjs.com/documentation/reference/application/advanced-usage

Markdown Content:
Advanced usage
===============

[Edit Page](https://github.com/balderdashy/sails/blob/master/docs/reference/application/advanced-usage/advanced-usage.md)
Advanced usage
==============

Most users of the Sails framework will never need to access more than a few basic methods of the `sails` application object. However, if you have an advanced use case or are considering [contributing to Sails](https://sailsjs.com/documentation/contributing), you may need to delve into some of these lesser-used methods or reference the [loading order of Sails core](https://sailsjs.com/documentation/reference/application/advanced-usage/lifecycle).

### Disabling the `sails` global

We recommended using the `sails` global with Sails.

However, the auto-globalization of `sails`[can be disabled](https://sailsjs.com/documentation/reference/configuration/sails-config-globals). Disabling the `sails` global might be a good idea for use cases where multiple Sails app instances need to exist at once, or where globals are not an option.

If the `sails` global is disabled, then you'll need another way to reference the application instance. Luckily, this is possible from almost anywhere in your app:

* in the `fn` of an [action](https://sailsjs.com/documentation/concepts/actions-and-controllers) (`this.sails`)
* in the `fn` of a [helper](https://sailsjs.com/documentation/concepts/helpers) (`this.sails`).
* on an incoming request (`req._sails`)

### Properties (advanced)

##### sails.hooks

A dictionary of all loaded [Sails hooks](https://sailsjs.com/documentation/concepts/extending-sails/hooks), indexed by their _identity_. Use `sails.hooks` to access properties and methods of hooks you've installed to extend Sails—for example, by calling `sails.hooks.email.send()`. You can also use this dictionary to access the Sails [core hooks](https://sailsjs.com/documentation/concepts/extending-sails/hooks#?types-of-hooks), for advanced usage.

By default, a hook's identity is the lowercased version of its folder name, with any `sails-hook-` prefix removed. For example, the default identity for a hook loaded from `node_modules/sails-hook-email` would be `email`, and the hook would be accessible via `sails.hooks.email`. An installed hook's identity can be changed via the [`installedHooks` config property](https://sailsjs.com/documentation/concepts/extending-sails/hooks/using-hooks#?changing-the-way-sails-loads-an-installable-hook).

See the [hooks concept documentation](https://sailsjs.com/documentation/concepts/extending-sails/hooks) for more information about hooks.

##### `sails.io`

The API exposed by the [`sails.sockets.*` methods](https://sailsjs.com/documentation/reference/web-sockets/sails-sockets) is flexible enough out of the box to cover the requirements of most applications, and using them will future-proof your app against possible changes in the underlying implementation. However, if you are working on bringing some legacy code from a vanilla Socket.io app into your Sails app, it can be useful to talk to Socket.io directly. To accomplish this, Sails provides raw access to the underlying [socket.io](http://socket.io/) server instance (`io`) as `sails.io`. See the [Socket.io docs](http://socket.io/docs/) for more information. If you decide to use Socket.io directly, please proceed with care.

> Sails bundles `socket.io` as a dependency of [sails-hook-sockets](https://sailsjs.com/documentation/reference/application/github.com/balderdashy/sails-hook-sockets), a core hook.

### Where does the application object come from?

An application instance automatically created _the first time_ you `require('sails')`.

This is what is happening in the generated `app.js` file:

```
var sails = require('sails');
```

Note that any subsequent calls to `require('sails')` return the same app instance. (This is why you might sometimes hear the Sails app instance referred to as a "singleton".)

### Creating a new application object (advanced)

If you are implementing something unconventional (e.g. writing tests for Sails core) where you need to create more than one Sails application instance in a process, you _should not_ use the instance returned by `require('sails')`, as this can cause unexpected behavior. Instead, you should obtain application instances by using the Sails constructor:

```
var Sails = require('sails').constructor;
var sails0 = new Sails();
var sails1 = new Sails();
var sails2 = new Sails();
```

Each app instance (`sails0`, `sails1`, `sails2`) can be loaded/lifted separately, using different configuration.

For more on using Sails programatically, see the conceptual overview on [programmatic usage in Sails](https://sailsjs.com/documentation/concepts/programmatic-usage).

### Is something missing?

If you notice something we've missed or could be improved on, please follow [this link](https://github.com/balderdashy/sails/blob/master/docs/reference/application/advanced-usage/advanced-usage.md) and submit a pull request to the sails repo. Once we merge it, the changes will be reflected on the website the next time it is deployed.

[![Image 2: Sails logo](https://sailsjs.com/images/logo_sails.png)](https://sailsjs.com/)

![Image 3](https://sailsjs.com/images/icon_search_white.png)

* [Home](https://sailsjs.com/)
* [Get started](https://sailsjs.com/get-started)
* [Support](https://sailsjs.com/support)
* [Documentation](https://sailsjs.com/documentation)
* [Documentation](https://sailsjs.com/documentation)[](https://sailsjs.com/documentation/reference/application/advanced-usage)

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
