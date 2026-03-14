# Source: https://sailsjs.com/documentation/reference/blueprint-api/add-to

Title: add to

URL Source: https://sailsjs.com/documentation/reference/blueprint-api/add-to

Markdown Content:
add to
===============

[Edit Page](https://github.com/balderdashy/sails/blob/master/docs/reference/blueprint-api/Add.md)
Add (blueprint)
===============

Add a foreign record (e.g. a comment) to one of this record's collections (e.g. "comments").

```
PUT /:model/:id/:association/:fk
```

This action adds a reference to some other record (the "foreign", or "child" record) onto a particular collection of this record (the "primary", or "parent" record).

* If the specified `:id` does not correspond with a primary record that exists in the database, this responds using `res.notFound()`.
* If the specified `:fk` does not correspond with a foreign record that exists in the database, this responds using `res.notFound()`.
* If the primary record is already associated with this foreign record, this action will not modify any records. (Note that currently, in the case of a many-to-many association, it _will_ add duplicate junction records! To resolve this, add a multi-column index at the database layer, if possible. We are currently working on a friendlier solution/default for users of MongoDB, sails-disk, and other NoSQL databases.)
* Note that if the association is "2-way" (meaning it has `via`), then the foreign key or collection it points to with that `via` will also be updated on the foreign record.

### Parameters

[#](https://sailsjs.com/documentation/reference/blueprint-api/add-to#?parameters)

| Parameter | Type | Details |
| --- | --- | --- |
| model | String | The [identity](https://sailsjs.com/documentation/concepts/models-and-orm/model-settings#?identity) of the containing model for the parent record. e.g. `'employee'` (in `/employee/7/involvedinPurchases/47`) |
| id | String | The desired parent record's primary key value. e.g. `'7'` (in `/employee/7/involvedInPurchases/47`) |
| association | String | The name of the collection attribute. e.g. `'involvedInPurchases'` |
| fk | String | The primary key value (usually id) of the child record to add to this collection. e.g. `'47'` |

### Example

[#](https://sailsjs.com/documentation/reference/blueprint-api/add-to#?example)
Add purchase #47 to the list of purchases that Dolly (employee #7) has been involved in:

```
PUT /employee/7/involvedInPurchases/47
```

[![Image 3: Run in Postman](https://s3.amazonaws.com/postman-static/run-button.png)](https://www.getpostman.com/run-collection/96217d0d747e536e49a4)

##### Expected response

[#](https://sailsjs.com/documentation/reference/blueprint-api/add-to#?expected-response)
This returns "Dolly", the parent record. Notice she is now involved in purchase #47:

```
{
  "id": 7,
  "name": "Dolly",
  "createdAt": 1485462079725,
  "updatedAt": 1485476060873,
  "involvedInPurchases": [
    {
      "amount": 10000,
      "createdAt": 1485476060873,
      "updatedAt": 1485476060873,
      "id": 47,
      "cashier": 7
    }
  ]
}
```

##### Using jQuery

[#](https://sailsjs.com/documentation/reference/blueprint-api/add-to#?using-jquery)

```
$.put('/employee/7/involvedInPurchases/47', function (purchases) {
  console.log(purchases);
});
```

##### Using Angular

[#](https://sailsjs.com/documentation/reference/blueprint-api/add-to#?using-angular)

```
$http.put('/employee/7/involvedInPurchases/47')
.then(function (purchases) {
  console.log(purchases);
});
```

##### Using sails.io.js

[#](https://sailsjs.com/documentation/reference/blueprint-api/add-to#?using-sailsiojs)

```
io.socket.put('/employee/7/involvedInPurchases/47', function (purchases) {
  console.log(purchases);
});
```

##### Using [cURL](https://en.wikipedia.org/wiki/CURL)

[#](https://sailsjs.com/documentation/reference/blueprint-api/add-to#?using-curl)

```
curl http://localhost:1337/employee/7/involvedInPurchases/47 -X "PUT"
```

### Socket notifications

[#](https://sailsjs.com/documentation/reference/blueprint-api/add-to#?socket-notifications)
If you have WebSockets enabled for your app, then every client [subscribed](https://sailsjs.com/documentation/reference/web-sockets/resourceful-pub-sub) to the primary record will receive a notification in which the notification event name is the primary model identity (e.g. `'employee'`), and the message has the following format:

```
id: <the parent record primary key value>,
verb: 'addedTo',
attribute: <the parent record collection attribute name>,
addedIds: <the now-added child records' primary key values>
```

For instance, continuing the example above, all clients subscribed to Dolly, aka employee #7, (_except_ for the client making the request) would receive the following message:

```
{
  id: 7,
  verb: 'addedTo',
  attribute: 'involvedInPurchases',
  addedIds: [ 47 ]
}
```

**Clients subscribed to the child record receive an additional notification:**

Assuming `involvedInPurchases` had a `via`, then either `updated` or `addedTo` notifications would also be sent to any clients who were [subscribed](https://sailsjs.com/documentation/reference/web-sockets/resourceful-pub-sub) to purchase #47, the child record we just added.

> If the `via`-linked attribute on the other side is [also plural](https://sailsjs.com/documentation/concepts/models-and-orm/associations/many-to-many) (e.g. `cashiers`), then another `addedTo` notification will be sent. Otherwise, if the `via`[points at a singular attribute](https://sailsjs.com/documentation/concepts/models-and-orm/associations/one-to-many) (e.g. `cashier`) then the [`updated` notification](https://sailsjs.com/documentation/reference/blueprint-api/update#?socket-notifications) will be sent.

**Finally, a third notification might be sent:**

If adding this purchase to Dolly's collection would "steal" it from another employee's `involvedInPurchases`, then any clients subscribed to that other, stolen-from employee record (e.g. Motoki, employee #12) would receive a `removedFrom` notification (see [**Blueprints > remove from**](https://sailsjs.com/documentation/reference/blueprint-api/remove-from#?socket-notifications).

### Notes

[#](https://sailsjs.com/documentation/reference/blueprint-api/add-to#?notes)
>
> * If you'd like to spend some more time with Dolly, a more detailed walkthrough related to the example above is available [here](https://gist.github.com/mikermcneil/e5a20b03be5aa4e0459b).
> * This action is for dealing with _plural_ ("collection") attributes. If you want to set or unset a _singular_ ("model") attribute, just use [update](https://sailsjs.com/documentation/reference/blueprint-api/update) and set the foreign key to the id of the new foreign record (or `null` to clear the association). If you want to completely _replace_ the set of records in the collection with another set, use the [replace](https://sailsjs.com/documentation/reference/blueprint-api/replace) blueprint.
> * The example above assumes "rest" blueprints are enabled, and that your project contains at least an 'Employee' model with attribute: `involvedInPurchases: {collection: 'Purchase', via: 'cashier'}` as well as a `Purchase` model with attribute: `cashier: {model: 'Employee'}`. You can quickly achieve this by running:
>
>
> ```
> sails new foo
> cd foo
> sails generate model purchase
> sails generate model employee
> ```
>
>
> ...then editing `api/models/Purchase.js` and `api/models/Employee.js`.

### Is something missing?

If you notice something we've missed or could be improved on, please follow [this link](https://github.com/balderdashy/sails/blob/master/docs/reference/blueprint-api/Add.md) and submit a pull request to the sails repo. Once we merge it, the changes will be reflected on the website the next time it is deployed.

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
* [* Reference * Concepts * App structure * Upgrading * Contribution guide * Tutorials * Our story Documentation](https://sailsjs.com/documentation/reference/blueprint-api/add-to)

![Image 6](https://sailsjs.com/images/icon_warning.png)For a better experience on sailsjs.com, [update your browser](https://support.microsoft.com/en-us/help/17621/internet-explorer-downloads).

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

[![Image 7: ads via Carbon](https://srv.carbonads.net/static/30242/d58937c1b39ab9c35fd7abeaa7895417951bdf14)](https://srv.carbonads.net/ads/click/x/GTND427UCK7D427JCABLYKQUCA7IK27UCWAIKZ3JCASIC53EFTSIPK3KCESDCK7IFT7DPKJNCTSITK3LCVSD62QKC6SI5K7LCKYDVK3EHJNCLSIZ)[Join Beta and get 6 months of free AI integration for your ecommerce, no replatforming. Sign up!](https://srv.carbonads.net/ads/click/x/GTND427UCK7D427JCABLYKQUCA7IK27UCWAIKZ3JCASIC53EFTSIPK3KCESDCK7IFT7DPKJNCTSITK3LCVSD62QKC6SI5K7LCKYDVK3EHJNCLSIZ)[ads via Carbon](http://carbonads.net/?utm_source=sailsjsorg&utm_medium=ad_via_link&utm_campaign=in_unit&utm_term=carbon)

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
