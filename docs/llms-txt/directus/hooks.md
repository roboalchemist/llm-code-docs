# Source: https://directus.io/docs/raw/guides/extensions/api-extensions/hooks.md

# Event Hooks

> Hooks allow running code when during the Directus lifecycle or database events.

Hooks allow running code when events occur within Directus. Events are triggered on schedules, database events, schedules, or during the Directus application lifecycle.

<partial content="extensions-api">



</partial>

## Hook Entrypoint

The `index.js` or `index.ts` file exports a function that is read by Directus. It contains one or more event listeners.

### Entrypoint Example

```js
export default ({ filter, action }) => {
  filter("items.create", () => {
    console.log("Creating Item!");
  });

  action("items.create", () => {
    console.log("Item created!");
  });
};
```

## Register Function

The register function receives an object containing the type-specific register functions as the first parameter:

<table>
<thead>
  <tr>
    <th>
      Type
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        filter
      </code>
    </td>
    
    <td>
      Happens before the event is emitted. Use to check, modify, or prevent the event from being emitted.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        action
      </code>
    </td>
    
    <td>
      Happens after the event is emitted. Use to execute further logic, enrichment, or automations.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        init
      </code>
    </td>
    
    <td>
      Happens at a defined point within the lifecycle of Directus.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        schedule
      </code>
    </td>
    
    <td>
      Happens on a defined time interval.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        embed
      </code>
    </td>
    
    <td>
      Inject custom JavaScript or CSS in the Data Studio.
    </td>
  </tr>
</tbody>
</table>

The second parameter is a context object with the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        services
      </code>
    </td>
    
    <td>
      All internal Directus services.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        database
      </code>
    </td>
    
    <td>
      Knex instance that is connected to the current database
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        getSchema
      </code>
    </td>
    
    <td>
      Async function that reads the full available schema for use in services
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        env
      </code>
    </td>
    
    <td>
      Parsed environment variables.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        logger
      </code>
    </td>
    
    <td>
      <a href="https://github.com/pinojs/pino" rel="nofollow">
        Pino
      </a>
      
       instance
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        emitter
      </code>
    </td>
    
    <td>
      <a href="https://github.com/directus/directus/blob/main/api/src/emitter.ts" rel="nofollow">
        Event emitter
      </a>
      
       instance that can be used to emit custom events for other extensions
    </td>
  </tr>
</tbody>
</table>

## Filter

Filter events are called before an event is emitted.

```js
export default ({ filter }) => {
  filter("items.create", (payload, meta, context) => {
    console.log("About to create item.");
    return payload;
  });
};
```

The `filter` register function takes an event name and a callback function that receives the modifiable `payload`, an event-specific `meta` object, and a `context` object when the event is emitted.

The `meta` object contains the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        event
      </code>
    </td>
    
    <td>
      The type of event that is being emitted.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        collection
      </code>
    </td>
    
    <td>
      The collection where the event is occuring.
    </td>
  </tr>
</tbody>
</table>

The context object has the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        database
      </code>
    </td>
    
    <td>
      The current database transaction.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        schema
      </code>
    </td>
    
    <td>
      The current API schema in use.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        accountability
      </code>
    </td>
    
    <td>
      Information about the current user.
    </td>
  </tr>
</tbody>
</table>

### Filter Events

<table>
<thead>
  <tr>
    <th>
      Name
    </th>
    
    <th>
      Payload
    </th>
    
    <th>
      Meta
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        websocket.authenticate
      </code>
    </td>
    
    <td>
      The default accountability object.
    </td>
    
    <td>
      <code>
        message
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        websocket.message
      </code>
    </td>
    
    <td>
      The message sent over the WebSocket.
    </td>
    
    <td>
      <code>
        client
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        request.not_found
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      <code>
        request
      </code>
      
      , <code>
        response
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        request.error
      </code>
    </td>
    
    <td>
      The request errors.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        database.error
      </code>
    </td>
    
    <td>
      The database error.
    </td>
    
    <td>
      <code>
        client
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        auth.login
      </code>
    </td>
    
    <td>
      The login payload.
    </td>
    
    <td>
      <code>
        status
      </code>
      
      , <code>
        user
      </code>
      
      , <code>
        provider
      </code>
      
      , <code>
        error
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        auth.jwt
      </code>
    </td>
    
    <td>
      The auth token.
    </td>
    
    <td>
      <code>
        status
      </code>
      
      , <code>
        user
      </code>
      
      , <code>
        provider
      </code>
      
      , <code>
        type
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        auth.create
      </code>
      
      <sup>
        <span>
          1
        </span>
      </sup>
    </td>
    
    <td>
      The created user.
    </td>
    
    <td>
      <code>
        identifier
      </code>
      
      , <code>
        provider
      </code>
      
      , <code>
        providerPayload
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        auth.update
      </code>
      
      <sup>
        <span>
          2
        </span>
      </sup>
    </td>
    
    <td>
      The updated auth token<sup>
        <span>
          3
        </span>
      </sup>
      
      .
    </td>
    
    <td>
      <code>
        identifier
      </code>
      
      , <code>
        provider
      </code>
      
      , <code>
        providerPayload
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        authenticate
      </code>
    </td>
    
    <td>
      The default accountability object.
    </td>
    
    <td>
      <code>
        req
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        email.send
      </code>
    </td>
    
    <td>
      The email payload.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        (<collection>.)items.query
      </code>
    </td>
    
    <td>
      The items query.
    </td>
    
    <td>
      <code>
        collection
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        (<collection>.)items.read
      </code>
    </td>
    
    <td>
      The read item.
    </td>
    
    <td>
      <code>
        query
      </code>
      
      , <code>
        collection
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        (<collection>.)items.create
      </code>
    </td>
    
    <td>
      The new item.
    </td>
    
    <td>
      <code>
        collection
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        (<collection>.)items.update
      </code>
    </td>
    
    <td>
      The updated item.
    </td>
    
    <td>
      <code>
        keys
      </code>
      
      , <code>
        collection
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        (<collection>.)items.promote
      </code>
    </td>
    
    <td>
      The promoted item.
    </td>
    
    <td>
      <code>
        collection
      </code>
      
      , <code>
        item
      </code>
      
      , <code>
        version
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        (<collection>.)items.delete
      </code>
    </td>
    
    <td>
      The keys of the item.
    </td>
    
    <td>
      <code>
        collection
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <system-collection>.query
      </code>
    </td>
    
    <td>
      The items query.
    </td>
    
    <td>
      <code>
        collection
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <system-collection>.read
      </code>
    </td>
    
    <td>
      The read item.
    </td>
    
    <td>
      <code>
        query
      </code>
      
      , <code>
        collection
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <system-collection>.create
      </code>
    </td>
    
    <td>
      The new item.
    </td>
    
    <td>
      <code>
        collection
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <system-collection>.update
      </code>
    </td>
    
    <td>
      The updated item.
    </td>
    
    <td>
      <code>
        keys
      </code>
      
      , <code>
        collection
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <system-collection>.delete
      </code>
    </td>
    
    <td>
      The keys of the item.
    </td>
    
    <td>
      <code>
        collection
      </code>
    </td>
  </tr>
</tbody>
</table>

<sup>
<span>

1

</span>
</sup>

 Available for the `ldap`, `oauth2`, `openid` and `saml` driver.

<sup>
<span>

2

</span>
</sup>

 Available for the `ldap`, `oauth2`, and `openid` driver.

<sup>
<span>

3

</span>
</sup>

 Available for the `oauth2`, and `openid` driver if set by provider.

<partial content="extension-hook-footguns">



</partial>

<callout color="warning" icon="material-symbols:warning-rounded">

**Filters are Blocking**
Filters can impact performance if not implemented carefully, especially on `read` events, which can lead to many database reads.

</callout>

<partial content="extension-hook-system-collections">



</partial>

## Action

Action events are called after an event is emitted.

```js
export default ({ action }) => {
  action("items.create", (meta, context) => {
    console.log("Item was just created.");
  });
};
```

The `action` register function takes an event name and a callback function that receives a `meta` object (containing information about the action and the payload) and a `context` object.

The `meta` object contains the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        event
      </code>
    </td>
    
    <td>
      The type of event that was emitted.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        payload
      </code>
    </td>
    
    <td>
      The data associated with the event.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        key
      </code>
    </td>
    
    <td>
      The primary key of the item.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        collection
      </code>
    </td>
    
    <td>
      The collection where the event occurred.
    </td>
  </tr>
</tbody>
</table>

The context object has the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        database
      </code>
    </td>
    
    <td>
      The current database transaction.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        schema
      </code>
    </td>
    
    <td>
      The current API schema in use.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        accountability
      </code>
    </td>
    
    <td>
      Information about the current user.
    </td>
  </tr>
</tbody>
</table>

### Action Events

<table>
<thead>
  <tr>
    <th>
      Name
    </th>
    
    <th>
      Meta
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        websocket.message
      </code>
    </td>
    
    <td>
      <code>
        message
      </code>
      
      , <code>
        client
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        websocket.error
      </code>
    </td>
    
    <td>
      <code>
        client
      </code>
      
      , <code>
        event
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        websocket.close
      </code>
    </td>
    
    <td>
      <code>
        client
      </code>
      
      , <code>
        event
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        websocket.connect
      </code>
    </td>
    
    <td>
      <code>
        client
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        websocket.auth.success
      </code>
    </td>
    
    <td>
      <code>
        client
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        websocket.auth.failure
      </code>
    </td>
    
    <td>
      <code>
        client
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        server.start
      </code>
    </td>
    
    <td>
      <code>
        server
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        server.stop
      </code>
    </td>
    
    <td>
      <code>
        server
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        response
      </code>
    </td>
    
    <td>
      <code>
        request
      </code>
      
      , <code>
        response
      </code>
      
      , <code>
        ip
      </code>
      
      , <code>
        duration
      </code>
      
      , <code>
        finished
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        auth.login
      </code>
    </td>
    
    <td>
      <code>
        payload
      </code>
      
      , <code>
        status
      </code>
      
      , <code>
        user
      </code>
      
      , <code>
        provider
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        files.upload
      </code>
    </td>
    
    <td>
      <code>
        payload
      </code>
      
      , <code>
        key
      </code>
      
      , <code>
        collection
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        extensions.load
      </code>
    </td>
    
    <td>
      <code>
        extensions
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        extensions.unload
      </code>
    </td>
    
    <td>
      <code>
        extensions
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        extensions.reload
      </code>
    </td>
    
    <td>
      <code>
        extensions
      </code>
      
      , <code>
        added
      </code>
      
       , <code>
        removed
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        extensions.installed
      </code>
    </td>
    
    <td>
      <code>
        extensions
      </code>
      
      , <code>
        versionId
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        extensions.uninstalled
      </code>
    </td>
    
    <td>
      <code>
        extensions
      </code>
      
      , <code>
        folder
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        (<collection>.)items.read
      </code>
    </td>
    
    <td>
      <code>
        payload
      </code>
      
      , <code>
        query
      </code>
      
      , <code>
        collection
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        (<collection>.)items.create
      </code>
    </td>
    
    <td>
      <code>
        payload
      </code>
      
      , <code>
        key
      </code>
      
      , <code>
        collection
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        (<collection>.)items.update
      </code>
    </td>
    
    <td>
      <code>
        payload
      </code>
      
      , <code>
        keys
      </code>
      
      , <code>
        collection
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        (<collection>.)items.promote
      </code>
    </td>
    
    <td>
      <code>
        payload
      </code>
      
      , <code>
        collection
      </code>
      
      , <code>
        item
      </code>
      
      , <code>
        version
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        (<collection>.)items.delete
      </code>
    </td>
    
    <td>
      <code>
        keys
      </code>
      
      , <code>
        collection
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        (<collection>.)items.sort
      </code>
    </td>
    
    <td>
      <code>
        collection
      </code>
      
      , <code>
        item
      </code>
      
      , <code>
        to
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <system-collection>.read
      </code>
    </td>
    
    <td>
      <code>
        payload
      </code>
      
      , <code>
        query
      </code>
      
      , <code>
        collection
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <system-collection>.create
      </code>
    </td>
    
    <td>
      <code>
        payload
      </code>
      
      , <code>
        key
      </code>
      
      , <code>
        collection
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <system-collection>.update
      </code>
    </td>
    
    <td>
      <code>
        payload
      </code>
      
      , <code>
        keys
      </code>
      
      , <code>
        collection
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <system-collection>.delete
      </code>
    </td>
    
    <td>
      <code>
        keys
      </code>
      
      , <code>
        collection
      </code>
    </td>
  </tr>
</tbody>
</table>

<callout color="primary" icon="material-symbols:menu-book-outline" to="/guides/realtime/custom-handlers">

Learn how to build custom WebSocket handlers with practical examples using these hooks.

</callout>

<partial content="extension-hook-footguns">



</partial>

<partial content="extension-hook-system-collections">



</partial>

## Init

Init events are called during the Directus application lifecycle.

```js
export default ({ init }) => {
  init("routes.before", (meta) => {
    console.log(meta);
  });
};
```

The `init` register function takes an event name and a callback function that receives `meta`. `meta` contains either `program` or `app` (the full underlying Express application) depending on the lifecycle event.

### Init Events

<table>
<thead>
  <tr>
    <th>
      Name
    </th>
    
    <th>
      Meta
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        cli.before
      </code>
    </td>
    
    <td>
      <code>
        program
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        cli.after
      </code>
    </td>
    
    <td>
      <code>
        program
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        app.before
      </code>
    </td>
    
    <td>
      <code>
        app
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        app.after
      </code>
    </td>
    
    <td>
      <code>
        app
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        routes.before
      </code>
    </td>
    
    <td>
      <code>
        app
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        routes.after
      </code>
    </td>
    
    <td>
      <code>
        app
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        routes.custom.before
      </code>
    </td>
    
    <td>
      <code>
        app
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        routes.custom.after
      </code>
    </td>
    
    <td>
      <code>
        app
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        middlewares.before
      </code>
    </td>
    
    <td>
      <code>
        app
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        middlewares.after
      </code>
    </td>
    
    <td>
      <code>
        app
      </code>
    </td>
  </tr>
</tbody>
</table>

## Schedule

Schedule events are called on a defined time interval.

```js
export default ({ schedule }) => {
  schedule("*/15 * * * *", () => {
    console.log("15 minutes have passed.");
  });
};
```

The `schedule` event takes a cron string as the first argument and a callback function as the second argument. The cron string follows the following format:

```text
*    *    *    *    *    *
┬    ┬    ┬    ┬    ┬    ┬
│    │    │    │    │    │
│    │    │    │    │    └ day of week (0 - 7) (0 or 7 is Sun)
│    │    │    │    └───── month (1 - 12)
│    │    │    └────────── day of month (1 - 31)
│    │    └─────────────── hour (0 - 23)
│    └──────────────────── minute (0 - 59)
└───────────────────────── second (0 - 59, OPTIONAL)
```

## Embed

The embed hook injects custom JavaScript or CSS into the `<head>` and `<body>` tags within the Data Studio.

```js
export default ({ embed }) => {
  embed("body", '<script>console.log("Hello World")</script>');
};
```

The embed register function requires two parameters - the position of the embed (either `head` or `body`), and a value to embed (either a string or a function that returns a string).

## Sandboxed Hooks

When using the sandbox, you have access to `filter` and `action` events only. Callback functions recieve the `payload` object as the only parameter.

### TypeScript

You can import the `SandboxHookRegisterContext` type from `directus:api` to type the register function's `context` object:

```ts
/// <reference types="@directus/extensions/api.d.ts" />
import type { SandboxHookRegisterContext } from "directus:api";

export default ({ filter, action }: SandboxHookRegisterContext) => {};
```

<callout color="primary" icon="material-symbols:menu-book-outline" to="/guides/extensions/api-extensions/sandbox">

Learn more about the Directus sandbox for API extensions.

</callout>

<partial content="extensions-api-internals">



</partial>
