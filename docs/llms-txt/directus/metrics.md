# Source: https://directus.io/docs/raw/configuration/metrics.md

# Metrics

> Configuration for metrics.

To enable performance and error measurement of connected services, Directus can provide Prometheus metrics.

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
        METRICS_ENABLED
      </code>
    </td>
    
    <td>
      Whether or not to enable metrics.
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
        METRICS_SCHEDULE
      </code>
    </td>
    
    <td>
      The cron schedule at which to generate the metrics, the default is every minute
    </td>
    
    <td>
      <code>
        */1 * * * *
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        METRICS_TOKENS
      </code>
    </td>
    
    <td>
      A CSV of tokens to allow access to via a <code>
        Authorization: Metrics <token>
      </code>
      
       header. By default it is restricted to admins
    </td>
    
    <td>
      --
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        METRICS_SERVICES
      </code>
    </td>
    
    <td>
      A CSV of directus services to observe metrics for. Currently <code>
        database
      </code>
      
      , <code>
        cache
      </code>
      
      , <code>
        redis
      </code>
      
       and <code>
        storage
      </code>
      
       are supported
    </td>
    
    <td>
      <code>
        database,cache,redis,storage
      </code>
    </td>
  </tr>
</tbody>
</table>

<callout color="warning" icon="material-symbols:warning-rounded">

**Metric Aggregation**
If Directus is running within a PM2 context, then metrics will be aggregated on a per scheduled job frequency. Ensure
Prometheus' scrape frequency takes that into account.

</callout>
