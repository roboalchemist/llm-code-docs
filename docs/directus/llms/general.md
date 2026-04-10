# Source: https://directus.io/docs/raw/configuration/general.md

# General

> Configuration for the general system, server, first admin user, and telemetry.

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
        CONFIG_PATH
      </code>
    </td>
    
    <td>
      Where your config file is located. See <a href="/self-hosting/deploying">
        Deploying Directus
      </a>
      
      .
    </td>
    
    <td>
      <code>
        .env
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        HOST
      </code>
    </td>
    
    <td>
      IP or host the API listens on.
    </td>
    
    <td>
      <code>
        0.0.0.0
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        PORT
      </code>
    </td>
    
    <td>
      What port to run the API under.
    </td>
    
    <td>
      <code>
        8055
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        UNIX_SOCKET_PATH
      </code>
    </td>
    
    <td>
      The Unix socket the API listens on, <code>
        PORT
      </code>
      
       and <code>
        HOST
      </code>
      
       will be ignored if this is provided.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        PUBLIC_URL
      </code>
    </td>
    
    <td>
      URL where your API can be reached on the web. used for things like OAuth redirects, forgot-password emails, and publicly-accessible logos.
    </td>
    
    <td>
      <code>
        /
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        ROOT_REDIRECT
      </code>
    </td>
    
    <td>
      Redirect the root of the application <code>
        /
      </code>
      
       to a specific route. Accepts a relative path, absolute URL, or <code>
        false
      </code>
      
       to disable.
    </td>
    
    <td>
      <code>
        ./admin
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        SERVE_APP
      </code>
    </td>
    
    <td>
      Whether or not to serve the Data Studio web application.
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
        GRAPHQL_INTROSPECTION
      </code>
    </td>
    
    <td>
      Whether or not to enable GraphQL Introspection.
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
        GRAPHQL_SCHEMA_CACHE_CAPACITY
      </code>
    </td>
    
    <td>
      How many user GraphQL schemas to store in memory.
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
        GRAPHQL_SCHEMA_GENERATION_MAX_CONCURRENT
      </code>
    </td>
    
    <td>
      How many GraphQL schemas can be generated simultaneously.
    </td>
    
    <td>
      <code>
        5
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        ROBOTS_TXT
      </code>
    </td>
    
    <td>
      What the <code>
        /robots.txt
      </code>
      
       endpoint should return.
    </td>
    
    <td>
      <code>
        User-agent: *\nDisallow: /
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        TEMP_PATH
      </code>
    </td>
    
    <td>
      Where Directus' temporary files should be managed.
    </td>
    
    <td>
      <code>
        ./node_modules/.directus
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        ACCEPT_TERMS
      </code>
    </td>
    
    <td>
      Confirm acknowledgement of the <a href="https://directus.io/bsl" rel="nofollow">
        Directus BSL License 1.1
      </a>
      
       and disable the license welcome banner.
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
        PROJECT_OWNER
      </code>
    </td>
    
    <td>
      Registered owner and primary contact responsible for your Directus instance. We need this to ensure compliance with our <a href="https://directus.io/bsl" rel="nofollow">
        BSL 1.1 license
      </a>
      
      .
    </td>
    
    <td>
      
    </td>
  </tr>
</tbody>
</table>

## Server

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
        SERVER_KEEP_ALIVE_TIMEOUT
      </code>
    </td>
    
    <td>
      Timeout in milliseconds for socket to be destroyed.
    </td>
    
    <td>
      <a href="https://github.com/nodejs/node/blob/master/doc/api/http.md#serverkeepalivetimeout" rel="nofollow">
        server.keepAliveTimeout
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        SERVER_HEADERS_TIMEOUT
      </code>
    </td>
    
    <td>
      Timeout in milliseconds to parse HTTP headers.
    </td>
    
    <td>
      <a href="https://github.com/nodejs/node/blob/master/doc/api/http.md#serverheaderstimeout" rel="nofollow">
        server.headersTimeout
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        SERVER_SHUTDOWN_TIMEOUT
      </code>
    </td>
    
    <td>
      Timeout in milliseconds before the server is forcefully shut down.
    </td>
    
    <td>
      1000
    </td>
  </tr>
</tbody>
</table>

### Additional Server Variables

All `SERVER_*` environment variables are merged with `server` instance properties created from [http.Server](https://github.com/nodejs/node/blob/master/doc/api/http.md#class-httpserver). This allows to configure server behind a proxy, a load balancer, etc. Be careful to not override methods of this instance otherwise you may incur into unexpected behaviors.

## First Admin User

The following commands set details for the first admin user created when the project is bootstrapped.

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
        ADMIN_EMAIL
      </code>
    </td>
    
    <td>
      The email address of the first user that's automatically created during bootstrapping.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        ADMIN_PASSWORD
      </code>
    </td>
    
    <td>
      The password of the first user that's automatically created during bootstrapping.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        ADMIN_TOKEN
      </code>
    </td>
    
    <td>
      The API token of the first user that's automatically created during bootstrapping.
    </td>
    
    <td>
      
    </td>
  </tr>
</tbody>
</table>

## Telemetry

To more accurately gauge the frequency of installation, version fragmentation, and general size of the user base, Directus collects little and anonymized data about your environment.

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
        TELEMETRY
      </code>
    </td>
    
    <td>
      Allow Directus to collect anonymized data about your environment.
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
        TELEMETRY_URL
      </code>
    </td>
    
    <td>
      URL that the usage report is submitted to.
    </td>
    
    <td>
      <code>
        https://telemetry.directus.io/
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        TELEMETRY_AUTHORIZATION
      </code>
    </td>
    
    <td>
      Optional authorization header value.
    </td>
    
    <td>
      
    </td>
  </tr>
</tbody>
</table>
