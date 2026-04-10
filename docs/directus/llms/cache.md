# Source: https://directus.io/docs/raw/configuration/cache.md

# Cache

> Configuration for internal and output caching.

<partial content="config-env-vars">



</partial>

Directus has a built-in data-caching option. Enabling this will cache the output of requests (based on the current user
and exact query parameters used) into configured cache storage location. This drastically improves API performance, as
subsequent requests are served straight from this cache. Enabling cache will also make Directus return accurate
cache-control headers. Depending on your setup, this will further improve performance by caching the request in
middleman servers (like CDNs) and even the browser.

<callout icon="material-symbols:info-outline">

**Internal Caching**
In addition to data-caching, Directus also does some internal caching. Note `CACHE_SCHEMA` which is enabled by default.
This speed up the overall performance of Directus, as we don't want to introspect the whole database on every request.

</callout>

<callout icon="material-symbols:warning-rounded" color="warning">

These settings are shared across all cache drivers. If `CACHE_ENABLED` is disabled, settings marked with **superscript 5** may be used by Directus's caching system. This behavior cannot be turned off.

</callout>

<callout icon="material-symbols:info-outline">

**Assets Cache**`Cache-Control` and `Last-Modified` headers for the `/assets` endpoint are separate from the regular data-cache.
`Last-Modified` comes from `modified_on` DB field. This is useful as it's often possible to cache assets for far longer
than you would cache database content. To learn more, see [Files](/configuration/files).

</callout>

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
        CACHE_ENABLED
      </code>
    </td>
    
    <td>
      Whether or not data caching is enabled.
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
        CACHE_TTL
      </code>
      
      <sup>
        <span>
          1
        </span>
      </sup>
    </td>
    
    <td>
      How long the data cache is persisted.
    </td>
    
    <td>
      <code>
        5m
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        CACHE_CONTROL_S_MAXAGE
      </code>
    </td>
    
    <td>
      Whether to not to add the <code>
        s-maxage
      </code>
      
       expiration flag. Set to a number for a custom value.
    </td>
    
    <td>
      <code>
        0
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        CACHE_AUTO_PURGE
      </code>
      
      <sup>
        <span>
          2
        </span>
      </sup>
    </td>
    
    <td>
      Automatically purge the data cache on actions that manipulate the data.
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
        CACHE_AUTO_PURGE_IGNORE_LIST
      </code>
      
      <sup>
        <span>
          3
        </span>
      </sup>
    </td>
    
    <td>
      List of collections that prevent cache purging when <code>
        CACHE_AUTO_PURGE
      </code>
      
       is enabled.
    </td>
    
    <td>
      <code>
        directus_activity,directus_presets
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        CACHE_SYSTEM_TTL
      </code>
      
      <sup>
        <span>
          4
        </span>
      </sup>
      
      <sup>
        <span>
          5
        </span>
      </sup>
    </td>
    
    <td>
      How long <code>
        CACHE_SCHEMA
      </code>
      
       is persisted.
    </td>
    
    <td>
      --
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        CACHE_SCHEMA
      </code>
      
      <sup>
        <span>
          4
        </span>
      </sup>
    </td>
    
    <td>
      Whether or not the database schema is cached. One of <code>
        false
      </code>
      
      , <code>
        true
      </code>
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
        CACHE_SCHEMA_MAX_ITERATIONS
      </code>
      
      <sup>
        <span>
          4
        </span>
      </sup>
    </td>
    
    <td>
      Safe value to limit max iterations on get schema cache. This value should only be adjusted for high scaling applications.
    </td>
    
    <td>
      <code>
        100
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        CACHE_SCHEMA_SYNC_TIMEOUT
      </code>
    </td>
    
    <td>
      How long to wait for other containers to message before trying again
    </td>
    
    <td>
      <code>
        10000
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        CACHE_SCHEMA_FREEZE_ENABLED
      </code>
    </td>
    
    <td>
      Whether or not to freeze the schema to improve memory efficiency
    </td>
    
    <td>
      false
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        CACHE_NAMESPACE
      </code>
      
      <sup>
        <span>
          5
        </span>
      </sup>
    </td>
    
    <td>
      How to scope the cache data.
    </td>
    
    <td>
      <code>
        system-cache
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        CACHE_STORE
      </code>
      
      <sup>
        <span>
          5
        </span>
      </sup>
    </td>
    
    <td>
      Where to store the cache data. Either <code>
        memory
      </code>
      
      , <code>
        redis
      </code>
      
      .
    </td>
    
    <td>
      <code>
        memory
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        CACHE_STATUS_HEADER
      </code>
    </td>
    
    <td>
      If set, returns the cache status in the configured header. One of <code>
        HIT
      </code>
      
      , <code>
        MISS
      </code>
      
      .
    </td>
    
    <td>
      --
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        CACHE_VALUE_MAX_SIZE
      </code>
    </td>
    
    <td>
      Maximum size of values that will be cached. Accepts number of bytes, or human readable string. Use <code>
        false
      </code>
      
       for no limit
    </td>
    
    <td>
      false
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        CACHE_SKIP_ALLOWED
      </code>
    </td>
    
    <td>
      Whether requests can use the Cache-Control header with <code>
        no-store
      </code>
      
       to skip data caching.
    </td>
    
    <td>
      false
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        CACHE_HEALTHCHECK_THRESHOLD
      </code>
    </td>
    
    <td>
      Healthcheck timeout threshold in ms.
    </td>
    
    <td>
      <code>
        150
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

 `CACHE_TTL` Based on your project's needs, you might be able to aggressively cache your data, only
requiring new data to be fetched every hour or so. This allows you to squeeze the most performance out of your Directus
instance. This can be incredibly useful for applications where you have a lot of (public) read-access and where updates
aren't real-time (for example a website). `CACHE_TTL` uses [`ms`](https://www.npmjs.com/package/ms) to parse the value,
so you configure it using human readable values (like `2 days`, `7 hrs`, `5m`).

<sup>
<span>

2

</span>
</sup>

 `CACHE_AUTO_PURGE` allows you to keep the Directus API real-time, while still getting the performance
benefits on quick subsequent reads.

<sup>
<span>

3

</span>
</sup>

 The cache has to be manually cleared when requiring to access updated results for collections in
`CACHE_AUTO_PURGE_IGNORE_LIST`.

<sup>
<span>

4

</span>
</sup>

 Not affected by the `CACHE_ENABLED` value.

<sup>
<span>

5

</span>
</sup>

 `CACHE_STORE` For larger projects, you most likely don't want to rely on local memory for caching.
Instead, you can use the above `CACHE_STORE` environment variable to use `redis` as the cache store.
