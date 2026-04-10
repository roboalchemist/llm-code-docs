# Source: https://directus.io/docs/raw/configuration/synchronization.md

# Synchronization

> Configuration around synchronization and Redis.

<partial content="config-env-vars">



</partial>

Synchronization in Directus refers to the process of coordinating actions across multiple instances or containers. This is crucial for ensuring consistency and reliability in distributed environments. Directus supports two synchronization stores: `memory` and `redis`. The `memory` store is the default and suitable for single-container deployments, while `redis` is recommended for multi-container deployments to ensure synchronization across all instances.

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
        SYNCHRONIZATION_STORE
      </code>
    </td>
    
    <td>
      One of <code>
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
        SYNCHRONIZATION_NAMESPACE
      </code>
    </td>
    
    <td>
      How to scope the channels in Redis.
    </td>
    
    <td>
      <code>
        directus-sync
      </code>
    </td>
  </tr>
</tbody>
</table>

## Redis

Redis is a critical component for Directus in multi-container deployments. It enables features like caching, rate-limiting, and WebSockets to function reliably across all instances of Directus. To use Redis, you can configure the following variables:

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
        REDIS_ENABLED
      </code>
    </td>
    
    <td>
      Whether or not Redis should be used. Defaults to whether or not you have any of the vars below configured.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        REDIS
      </code>
    </td>
    
    <td>
      Redis connection string. Using this will ignore the other Redis connection parameter environment variables.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        REDIS_HOST
      </code>
    </td>
    
    <td>
      Hostname of the Redis instance.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        REDIS_PORT
      </code>
    </td>
    
    <td>
      Port of the Redis instance.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        REDIS_USERNAME
      </code>
    </td>
    
    <td>
      Username for the Redis instance.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        REDIS_PASSWORD
      </code>
    </td>
    
    <td>
      Password for the Redis instance.
    </td>
    
    <td>
      
    </td>
  </tr>
</tbody>
</table>
