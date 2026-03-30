# Source: https://sailsjs.com/documentation/reference/blueprint-api/replace

Title: replace

URL Source: https://sailsjs.com/documentation/reference/blueprint-api/replace

Markdown Content:
replace
===============

[Edit Page](https://github.com/balderdashy/sails/blob/master/docs/reference/blueprint-api/Replace.md)
Replace (blueprint)
===================

Replace all of the foreign records in one of this record's collections (e.g. "comments").

```
PUT /:model/:id/:association
```

This action resets references to "foreign", or "child" records that are members of a particular collection of _this_ record (the "primary", or "parent" record), replacing any existing references in the collection.

* If the specified `:id` does not correspond with a primary record that exists in the database, this responds using `res.notFound()`.
* Note that, if the association is "2-way" (meaning it has `via`), then the foreign key or collection on the foreign record(s) will also be updated.

### Parameters

[#](https://sailsjs.com/documentation/reference/blueprint-api/replace#?parameters)

| Parameter | Type | Details |
| --- | --- | --- |
| model | String | The [identity](https://sailsjs.com/documentation/concepts/models-and-orm/model-settings#?identity) of the containing model for the parent record. e.g. `'employee'` (in `/employee/7/involvedinPurchases`) |
| id | String | The desired parent record's primary key value. e.g. `'7'` (in `/employee/7/involvedInPurchases`) |
| association | String | The name of the collection attribute. e.g. `'involvedInPurchases'` |
| fks | Array | The primary key values (usually ids) of the child records to use as the new members of this collection. e.g. `[47, 65]` |

> _The `fks` parameter should be sent in the PUT request body, unless you are making this request using a development-only [shortcut blueprint route](https://sailsjs.com/documentation/concepts/blueprints/blueprint-routes#?shortcut-routes), in which case you can simply include it in the query string as `?fks=[47,65]`._

### Example

[#](https://sailsjs.com/documentation/reference/blueprint-api/replace#?example)
Suppose you are in charge of keeping records for a large chain of grocery stores, and Dolly the cashier (employee #7) had been taking credit for being involved in a large number of purchases, when really she had only checked out two customers. Since the owner of the grocery store chain is very forgiving, Dolly gets to keep her job, but now you have to update Dolly's `involvedInPurchases` collection so that it _only_ contains purchases #47 and #65:

`PUT /employee/7/involvedInPurchases`

```
[47, 65]
```

[![Image 3: Run in Postman](https://s3.amazonaws.com/postman-static/run-button.png)](https://www.getpostman.com/run-collection/96217d0d747e536e49a4)

##### Expected response

[#](https://sailsjs.com/documentation/reference/blueprint-api/replace#?expected-response)
This returns Dolly, the parent record. Notice that her record only shows her being involved in purchases #47 and #65:

```
{
  "id": 7,
  "name": "Dolly",
  "createdAt": 1485462079725,
  "updatedAt": 1485476060873,
  "involvedInPurchases": [
    {
      "amount": 10000,
      "createdAt": 1485551132315,
      "updatedAt": 1486355134239,
      "id": 47,
      "cashier": 7
    },
    {
      "amount": 5667,
      "createdAt": 1483551158349,
      "updatedAt": 1485355134284,
      "id": 65,
      "cashier": 7
    }
  ]
}
```

### Socket notifications

[#](https://sailsjs.com/documentation/reference/blueprint-api/replace#?socket-notifications)
If you have WebSockets enabled for your app, then every client [subscribed](https://sailsjs.com/documentation/reference/web-sockets/resourceful-pub-sub) to the parent record will receive one [`addedTo` notification](https://sailsjs.com/documentation/reference/blueprint-api/add-to#?socket-notifications) for each child record in the new collection (if any).

For instance, continuing the example above, let's assume that Dolly's previous `involvedInPurchases` included purchases #65, #42, and #33. All clients subscribed to Dolly's employee record (_except_ for the client making the request) would receive two kinds of notifications: `addedTo` for the purchase she was not previously involved in (#47), and `removedFrom` for the purchases she is no longer involved in (#42 and #33).

```
{
  id: 7,
  verb: 'addedTo',
  attribute: 'involvedInPurchases',
  addedIds: [ 47 ]
}
```

and

```
{
  id: 7,
  verb: 'removedFrom',
  attribute: 'involvedInPurchases',
  removedIds: [ 42, 33 ]
}
```

> Note that purchase #65 is not included in the `addedTo` notification, since it was in Dolly's previous list of `involvedInPurchases`.

**Clients subscribed to the child records receive additional notifications:**

Assuming `involvedInPurchases` had a `via`, then either `updated` or `addedTo`/`removedFrom` notifications would also be sent to clients who were [subscribed](https://sailsjs.com/documentation/reference/web-sockets/resourceful-pub-sub) to any of the purchases we just linked or unlinked.

> If the `via`-linked attribute on the other side (Purchase) is [also plural](https://sailsjs.com/documentation/concepts/models-and-orm/associations/many-to-many) (e.g. `cashiers`), then an `addedTo` or `removedFrom` notification will be sent. Otherwise, if the `via`[points at a singular attribute](https://sailsjs.com/documentation/concepts/models-and-orm/associations/one-to-many) (e.g. `cashier`) then the [`updated` notification](https://sailsjs.com/documentation/reference/blueprint-api/update#?socket-notifications) will be sent.

**Finally, a third kind of notification might be sent:**

If giving Dolly this new collection of Purchases would "steal" any of them from other employees' `involvedInPurchases`, then any clients subscribed to those other, stolen-from employee records (e.g. Motoki, employee #12 and Timothy, employee #4) would receive `removedFrom` notifications. (See [**Blueprints > remove from**](https://sailsjs.com/documentation/reference/blueprint-api/remove-from#?socket-notifications)).

### Notes

[#](https://sailsjs.com/documentation/reference/blueprint-api/replace#?notes)
>
> * Remember, this blueprint replaces the _entire_ set of associated records for the given attribute. To add or remove a single associated record from the collection, leaving the rest of the collection unchanged, use the "add" or "remove" blueprint actions. (See [**Blueprints > add to**](https://sailsjs.com/documentation/reference/blueprint-api/add-to) and [**Blueprints > remove from**](https://sailsjs.com/documentation/reference/blueprint-api/remove-from)).

### Is something missing?

If you notice something we've missed or could be improved on, please follow [this link](https://github.com/balderdashy/sails/blob/master/docs/reference/blueprint-api/Replace.md) and submit a pull request to the sails repo. Once we merge it, the changes will be reflected on the website the next time it is deployed.

[![Image 4: Sails logo](https://sailsjs.com/images/logo_sails.png)](https://sailsjs.com/)

* Version:
* v1.x
* v0.12

v1.x

![Image 5](https://sailsjs.com/images/icon_search_white.png)

* [Home](https://sailsjs.com/)
* [Get started](https://sailsjs.com/get-started)
* [Support](https://sailsjs.com/support)
* [Documentation](https://sailsjs.com/documentation)
* [* Reference * Concepts * App structure * Upgrading * Contribution guide * Tutorials * Our story Documentation](https://sailsjs.com/documentation/reference/blueprint-api/replace)

![Image 6](https://sailsjs.com/images/icon_warning.png)For a better experience on sailsjs.com, [update your browser](https://support.microsoft.com/en-us/help/17621/internet-explorer-downloads).

Check out the official Sails [VS Code extension](https://marketplace.visualstudio.com/items?itemName=Sails.sails-vscode)

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

[![Image 7: ads via Carbon](https://srv.carbonads.net/static/30242/bb0b2a898008ba2d4ba0898af490dde617c4c7bb)](https://srv.carbonads.net/ads/click/x/GTND427UCK7D427JCABLYKQUCA7I5KJJCY7IVZ3JCASIC53MCVADP23KC6SDCK7ICEYD62JLFTAIEK3YCE7D55QMHEYI527ICV7IT23ECTNCYBZ52K)[Get the APM insights you need without enterprise price tags. Built for dev teams, not Fortune 500s](https://srv.carbonads.net/ads/click/x/GTND427UCK7D427JCABLYKQUCA7I5KJJCY7IVZ3JCASIC53MCVADP23KC6SDCK7ICEYD62JLFTAIEK3YCE7D55QMHEYI527ICV7IT23ECTNCYBZ52K)[ads via Carbon](http://carbonads.net/?utm_source=sailsjsorg&utm_medium=ad_via_link&utm_campaign=in_unit&utm_term=carbon)

[![Image 8: Sails logo](https://sailsjs.com/images/logo_sails.png)](https://sailsjs.com/)

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

![Image 9](https://sailsjs.com/images/logo_sails.png)

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

![Image 10](https://sailsjs.com/images/logo_sails.png)
[© 2012-2026 The Sails Company](https://sailsjs.com/about).

 The Sails framework is free and open-source under the MIT License.

 Illustrations by [Edamame](https://www.edamamedesign.com/).

[](https://twitter.com/sailsjs)[](https://www.facebook.com/sailsjs)[](https://github.com/balderdashy/sails)[](https://www.pinterest.com/sailsjs/)[](http://stackoverflow.com/search?q=sails)
