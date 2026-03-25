# Source: https://directus.io/docs/raw/configuration/logging.md

# Logging

> Configuration for general and Realtime logging.

<partial content="config-env-vars">



</partial>

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
        LOG_LEVEL
      </code>
    </td>
    
    <td>
      What level of detail to log. One of <code>
        fatal
      </code>
      
      , <code>
        error
      </code>
      
      , <code>
        warn
      </code>
      
      , <code>
        info
      </code>
      
      , <code>
        debug
      </code>
      
      , <code>
        trace
      </code>
      
       or <code>
        silent
      </code>
      
      .
    </td>
    
    <td>
      <code>
        info
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        LOG_HTTP_IGNORE_PATHS
      </code>
    </td>
    
    <td>
      List of HTTP request paths which should not appear in the log.
    </td>
    
    <td>
      
    </td>
  </tr>
</tbody>
</table>

All `LOGGER_*` environment variables are passed to the `options` configuration of a [`Pino` instance](https://github.com/pinojs/pino/blob/master/docs/api.md#options) and all `LOGGER_HTTP*` environment variables are passed to the `options` configuration of a [`Pino-http` instance](https://github.com/pinojs/pino-http#api).

Based on your project's needs, you can extend the `LOGGER_*` environment variables with any config you need to pass to the logger instance. If a `LOGGER_LEVELS` key is added, these values will be passed to the logger frontmatter, as described [here](https://github.com/pinojs/pino/blob/master/docs/help.md#mapping-pino-log-levels-to-google-cloud-logging-stackdriver-severity-levels). The format for adding `LEVELS` values is: `LOGGER_LEVELS="trace:DEBUG,debug:DEBUG,info:INFO,warn:WARNING,error:ERROR,fatal:CRITICAL"`

## Log Retention

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
        RETENTION_ENABLED
      </code>
    </td>
    
    <td>
      Whether or not to enable custom data retention settings. <code>
        false
      </code>
      
       will not delete data.
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
        RETENTION_SCHEDULE
      </code>
    </td>
    
    <td>
      The cron schedule at which to check for removable records, the default is once a day at 00:00.
    </td>
    
    <td>
      <code>
        0 0 * * *
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        RETENTION_BATCH
      </code>
    </td>
    
    <td>
      The maximum number of records to delete in a single query.
    </td>
    
    <td>
      <code>
        500
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        ACTIVITY_RETENTION
      </code>
    </td>
    
    <td>
      The maximum amount of time to retain <code>
        directus_activity
      </code>
      
       records or <code>
        false
      </code>
      
       to disable. This excludes flow logs.
    </td>
    
    <td>
      <code>
        90d
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        REVISIONS_RETENTION
      </code>
    </td>
    
    <td>
      The maximum amount of time to retain <code>
        directus_revisions
      </code>
      
       records or <code>
        false
      </code>
      
       to disable.
    </td>
    
    <td>
      <code>
        90d
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        FLOW_LOGS_RETENTION
      </code>
    </td>
    
    <td>
      The maximum amount of time to retain flow logs or <code>
        false
      </code>
      
       to disable.
    </td>
    
    <td>
      <code>
        90d
      </code>
    </td>
  </tr>
</tbody>
</table>

## Realtime Logs

![System Logs page with two panes - on the left a set of API calls, on the right the detailed logs for a single selected request.](/img/7abf4ad2-7d08-407d-bfca-67f3bff183d0.webp)

The WebSocket Logs endpoint is accessible at `/websocket/logs`. The method of authentication is limited to `strict` and the connection will be disconnected when the authentication expires.

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
        WEBSOCKETS_LOGS_ENABLED
      </code>
    </td>
    
    <td>
      Whether or not to enable the Logs subscriptions.
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
        WEBSOCKETS_LOGS_LEVEL
      </code>
    </td>
    
    <td>
      What level of detail to stream. One of <code>
        fatal
      </code>
      
      , <code>
        error
      </code>
      
      , <code>
        warn
      </code>
      
      , <code>
        info
      </code>
      
      , <code>
        debug
      </code>
      
      , <code>
        trace
      </code>
      
       or <code>
        silent
      </code>
      
      .
    </td>
    
    <td>
      <code>
        info
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        WEBSOCKETS_LOGS_STYLE
      </code>
    </td>
    
    <td>
      Stream just the message (pretty) or the full JSON log. One of <code>
        pretty
      </code>
      
      , <code>
        raw
      </code>
      
      .
    </td>
    
    <td>
      <code>
        pretty
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        WEBSOCKETS_LOGS_CONN_LIMIT
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
</tbody>
</table>

<callout icon="material-symbols:info-outline">

**Ephemeral Logs**<br />


Realtime system logs are ephemeral and not stored in the database. They are only available while the realtime connection is
active. Refreshing the page will clear the logs.

</callout>

### Enabling Realtime Logs

Realtime system logs rely on WebSockets which are enabled as part of <product-link product="realtime">



</product-link>

. To enable this feature:

1. Ensure the `WEBSOCKETS_ENABLED` environment variable is set to `true`.
2. Verify that the `WEBSOCKETS_LOGS_ENABLED` environment variable is set to `true` (it defaults to `true` if not explicitly configured).

### Log Levels

Under the hood, Directus uses [pino](https://github.com/pinojs/pino) for logging and uses the log levels provided by the
library:

<table>
<thead>
  <tr>
    <th>
      Log Level
    </th>
    
    <th>
      Numeric Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        trace
      </code>
    </td>
    
    <td>
      10
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        debug
      </code>
    </td>
    
    <td>
      20
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        info
      </code>
    </td>
    
    <td>
      30
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        warn
      </code>
    </td>
    
    <td>
      40
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        error
      </code>
    </td>
    
    <td>
      50
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        fatal
      </code>
    </td>
    
    <td>
      60
    </td>
  </tr>
</tbody>
</table>

### Searching & Filtering

If running multiple instances of Directus in a horizontally-scaled setup, you can also filter the logs by instance in
the System Logs pane.

You can also filter the logs by level, or filter by search terms in the `msg` field.
