# Source: https://directus.io/docs/raw/configuration/realtime.md

# Realtime

> Configuration for WebSockets and GraphQL Subscriptions.

<partial content="config-env-vars">



</partial>

Directus Realtime provides WebSockets and GraphQL Subscriptions.

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        WEBSOCKETS_ENABLED
      </code>
    </td>
    
    <td>
      Whether or not to enable all WebSocket functionality.
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        WEBSOCKETS_HEARTBEAT_ENABLED
      </code>
    </td>
    
    <td>
      Whether or not to enable the heartbeat ping signal.
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        WEBSOCKETS_HEARTBEAT_PERIOD
      </code>
    </td>
    
    <td>
      The period in seconds at which to send the ping. This period doubles as the timeout used for closing an unresponsive connection.
    </td>
    
    <td>
      30
    </td>
  </tr>
</tbody>
</table>

It's recommended to keep the `WEBSOCKETS_HEARTBEAT_PERIOD` between 30 and 120 seconds, otherwise the connections could be considered idle by other parties and therefore terminated.

## WebSockets

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        WEBSOCKETS_REST_ENABLED
      </code>
    </td>
    
    <td>
      Whether or not to enable the WebSocket message handlers.
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        WEBSOCKETS_REST_PATH
      </code>
    </td>
    
    <td>
      The URL path at which the WebSocket endpoint will be available.
    </td>
    
    <td>
      <code>
        /websocket
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        WEBSOCKETS_REST_CONN_LIMIT
      </code>
    </td>
    
    <td>
      How many simultaneous connections are allowed.
    </td>
    
    <td>
      <code>
        Infinity
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        WEBSOCKETS_REST_AUTH
      </code>
    </td>
    
    <td>
      The method of authentication to require for this connection. One of <code>
        public
      </code>
      
      , <code>
        handshake
      </code>
      
       or <code>
        strict
      </code>
      
      .
    </td>
    
    <td>
      <code>
        handshake
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        WEBSOCKETS_REST_AUTH_TIMEOUT
      </code>
    </td>
    
    <td>
      The amount of time in seconds to wait before closing an unauthenticated connection.
    </td>
    
    <td>
      30
    </td>
  </tr>
</tbody>
</table>

<callout icon="material-symbols:menu-book-outline" color="primary" to="/guides/realtime/authentication">

Read more about different authentication methods with Directus Realtime.

</callout>

## GraphQL

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        WEBSOCKETS_GRAPHQL_ENABLED
      </code>
    </td>
    
    <td>
      Whether or not to enable GraphQL Subscriptions.
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        WEBSOCKETS_GRAPHQL_PATH
      </code>
    </td>
    
    <td>
      The URL path at which the GraphQL Subscriptions endpoint will be available.
    </td>
    
    <td>
      <code>
        /graphql
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        WEBSOCKETS_GRAPHQL_CONN_LIMIT
      </code>
    </td>
    
    <td>
      How many simultaneous connections are allowed.
    </td>
    
    <td>
      <code>
        Infinity
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        WEBSOCKETS_GRAPHQL_AUTH
      </code>
    </td>
    
    <td>
      The method of authentication to require for this connection. One of <code>
        public
      </code>
      
      , <code>
        handshake
      </code>
      
       or <code>
        strict
      </code>
      
      .
    </td>
    
    <td>
      <code>
        handshake
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        WEBSOCKETS_GRAPHQL_AUTH_TIMEOUT
      </code>
    </td>
    
    <td>
      The amount of time in seconds to wait before closing an unauthenticated connection.
    </td>
    
    <td>
      30
    </td>
  </tr>
</tbody>
</table>

<callout icon="material-symbols:menu-book-outline" color="primary" to="/guides/realtime/authentication">

Read more about different authentication methods with Directus Realtime.

</callout>

## Collaborative Editing

<callout icon="material-symbols:info-outline">

Multi-instance collaboration requires a shared Redis instance for coordination.

</callout>

<table>
<thead>
  <tr>
    <th align="left">
      Variable
    </th>
    
    <th align="left">
      Description
    </th>
    
    <th align="left">
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td align="left">
      <code>
        WEBSOCKETS_COLLAB_ENABLED
      </code>
    </td>
    
    <td align="left">
      Toggle collaborative editing functionality specifically (when WebSockets are enabled).
    </td>
    
    <td align="left">
      <code>
        true
      </code>
    </td>
  </tr>
  
  <tr>
    <td align="left">
      <code>
        WEBSOCKETS_COLLAB_INSTANCE_TIMEOUT
      </code>
    </td>
    
    <td align="left">
      Duration in milliseconds before a silent node is considered dead.
    </td>
    
    <td align="left">
      <code>
        10000
      </code>
    </td>
  </tr>
  
  <tr>
    <td align="left">
      <code>
        WEBSOCKETS_COLLAB_CLUSTER_CLEANUP_CRON
      </code>
    </td>
    
    <td align="left">
      Cron expression for how often to garbage-collect empty rooms.
    </td>
    
    <td align="left">
      <code>
        */1 * * * *
      </code>
    </td>
  </tr>
  
  <tr>
    <td align="left">
      <code>
        WEBSOCKETS_COLLAB_LOCAL_CLEANUP_INTERVAL
      </code>
    </td>
    
    <td align="left">
      Duration in milliseconds between local cleanup sweeps.
    </td>
    
    <td align="left">
      <code>
        60000
      </code>
    </td>
  </tr>
  
  <tr>
    <td align="left">
      <code>
        WEBSOCKETS_COLLAB_PERMISSIONS_CACHE_CAPACITY
      </code>
    </td>
    
    <td align="left">
      LRU cache size for permission checks.
    </td>
    
    <td align="left">
      <code>
        2000
      </code>
    </td>
  </tr>
  
  <tr>
    <td align="left">
      <code>
        WEBSOCKETS_COLLAB_STORE_NAMESPACE
      </code>
    </td>
    
    <td align="left">
      The namespace used for Redis storage.
    </td>
    
    <td align="left">
      <code>
        collab
      </code>
    </td>
  </tr>
</tbody>
</table>

## Logging

Read more about logging with Directus Realtime in the [logging configuration](/configuration/logging).
