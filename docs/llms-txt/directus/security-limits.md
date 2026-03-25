# Source: https://directus.io/docs/raw/configuration/security-limits.md

# Security & Limits

> Configuration for access tokens, cookies, CSP, hashing, CORS, rate limiting, and request limits.

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
        SECRET
      </code>
      
      <sup>
        <span>
          1
        </span>
      </sup>
    </td>
    
    <td>
      Secret string for the project. Used for secret signing.
    </td>
    
    <td>
      Random value
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        ACCESS_TOKEN_TTL
      </code>
    </td>
    
    <td>
      The duration that an access token is valid.
    </td>
    
    <td>
      <code>
        15m
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        EMAIL_VERIFICATION_TOKEN_TTL
      </code>
    </td>
    
    <td>
      The duration that an email verification token is valid.
    </td>
    
    <td>
      <code>
        7d
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        REFRESH_TOKEN_TTL
      </code>
    </td>
    
    <td>
      The duration that a refresh token is valid. This value should be higher than <code>
        ACCESS_TOKEN_TTL
      </code>
      
       and <code>
        SESSION_COOKIE_TTL
      </code>
      
      .
    </td>
    
    <td>
      <code>
        7d
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        REFRESH_TOKEN_COOKIE_DOMAIN
      </code>
    </td>
    
    <td>
      Which domain to use for the refresh token cookie. Useful for development mode.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        REFRESH_TOKEN_COOKIE_SECURE
      </code>
    </td>
    
    <td>
      Whether or not to set the <code>
        secure
      </code>
      
       attribute for the refresh token cookie.
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
        REFRESH_TOKEN_COOKIE_SAME_SITE
      </code>
    </td>
    
    <td>
      Value for <code>
        sameSite
      </code>
      
       in the refresh token cookie.
    </td>
    
    <td>
      <code>
        lax
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        REFRESH_TOKEN_COOKIE_NAME
      </code>
    </td>
    
    <td>
      Name of the refresh token cookie.
    </td>
    
    <td>
      <code>
        directus_refresh_token
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        SESSION_COOKIE_TTL
      </code>
    </td>
    
    <td>
      The duration that the session cookie/token is valid, and also how long users stay logged-in to the App.
    </td>
    
    <td>
      <code>
        1d
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        SESSION_COOKIE_DOMAIN
      </code>
    </td>
    
    <td>
      Which domain to use for the session cookie. Useful for development mode.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        SESSION_COOKIE_SECURE
      </code>
    </td>
    
    <td>
      Whether or not to set the <code>
        secure
      </code>
      
       attribute for the session cookie.
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
        SESSION_COOKIE_SAME_SITE
      </code>
    </td>
    
    <td>
      Value for <code>
        sameSite
      </code>
      
       in the session cookie.
    </td>
    
    <td>
      <code>
        lax
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        SESSION_COOKIE_NAME
      </code>
    </td>
    
    <td>
      Name of the session cookie.
    </td>
    
    <td>
      <code>
        directus_session_token
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        SESSION_REFRESH_GRACE_PERIOD
      </code>
    </td>
    
    <td>
      The duration during which a refresh request will permit recently refreshed sessions to be used, thereby preventing race conditions in refresh calls.
    </td>
    
    <td>
      <code>
        10s
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        LOGIN_STALL_TIME
      </code>
    </td>
    
    <td>
      The duration in milliseconds that a login request will be stalled for, and it should be greater than the time taken for a login request with an invalid password.
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
        REGISTER_STALL_TIME
      </code>
    </td>
    
    <td>
      The duration in milliseconds that a registration request will be stalled for, and it should be greater than the time taken for a registration request with an already registered email.
    </td>
    
    <td>
      <code>
        750
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        PASSWORD_RESET_URL_ALLOW_LIST
      </code>
    </td>
    
    <td>
      List of URLs that can be used as <code>
        reset_url
      </code>
      
       in the <code>
        /password/request
      </code>
      
       endpoint.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        USER_INVITE_TOKEN_TTL
      </code>
    </td>
    
    <td>
      The duration that the invite token is valid.
    </td>
    
    <td>
      <code>
        7d
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        USER_INVITE_URL_ALLOW_LIST
      </code>
    </td>
    
    <td>
      List of URLs that can be used as <code>
        invite_url
      </code>
      
       in the <code>
        /users/invite
      </code>
      
       endpoint.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        USER_REGISTER_URL_ALLOW_LIST
      </code>
    </td>
    
    <td>
      List of URLs that can be used as <code>
        verification_url
      </code>
      
       in the <code>
        /users/register
      </code>
      
       endpoint.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        IP_TRUST_PROXY
      </code>
    </td>
    
    <td>
      Settings for the Express.js trust proxy setting.
    </td>
    
    <td>
      true
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        IP_CUSTOM_HEADER
      </code>
    </td>
    
    <td>
      What custom request header to use for the IP address.
    </td>
    
    <td>
      false
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        ASSETS_CONTENT_SECURITY_POLICY
      </code>
    </td>
    
    <td>
      Custom overrides for the Content-Security-Policy header for the /assets endpoint. See <a href="https://helmetjs.github.io" rel="nofollow">
        helmet's documentation on <code>
          helmet.contentSecurityPolicy()
        </code>
      </a>
      
      . Example: <code>
        ASSETS_CONTENT_SECURITY_POLICY_DIRECTIVES__IMG_SRC="'self' https://cdn.example.com data:"
      </code>
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        IMPORT_IP_DENY_LIST
      </code>
      
      <sup>
        <span>
          2
        </span>
      </sup>
    </td>
    
    <td>
      Deny importing files from these IP addresses / IP ranges / CIDR blocks. Use <code>
        0.0.0.0
      </code>
      
       to match any local IP address.
    </td>
    
    <td>
      <code>
        0.0.0.0,169.254.169.254
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        CONTENT_SECURITY_POLICY_*
      </code>
    </td>
    
    <td>
      Custom overrides for the Content-Security-Policy header. See <a href="https://helmetjs.github.io" rel="nofollow">
        helmet's documentation on <code>
          helmet.contentSecurityPolicy()
        </code>
      </a>
      
      . Example: <code>
        CONTENT_SECURITY_POLICY_DIRECTIVES__IMG_SRC="'self' https://images.example.com data:"
      </code>
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        HSTS_ENABLED
      </code>
    </td>
    
    <td>
      Enable the Strict-Transport-Security policy header. When enabled, Directus will send the <code>
        Strict-Transport-Security: max-age=15552000; includeSubDomains
      </code>
      
       header on all responses.
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
        HSTS_*
      </code>
    </td>
    
    <td>
      Custom overrides for the Strict-Transport-Security header. See <a href="https://helmetjs.github.io" rel="nofollow">
        helmet's documentation
      </a>
      
      . Example: <code>
        HSTS_MAX_AGE=63072000
      </code>
    </td>
    
    <td>
      
    </td>
  </tr>
</tbody>
</table>

<sup>
<span>

1

</span>
</sup>

 When `SECRET` is not set, a random value will be used. This means sessions won't persist across system
restarts or horizontally scaled deployments. Must be explicitly set to a secure random value in production.

<sup>
<span>

2

</span>
</sup>

 localhost can get resolved to `::1` as well as `127.0.0.1` depending on the system - ensure to include
both if you want to specifically block localhost.

Browser are pretty strict when it comes to third-party cookies. If you're running into unexpected problems when running your project and API on different domains, make sure to verify your configuration for `REFRESH_TOKEN_COOKIE_NAME`, `REFRESH_TOKEN_COOKIE_SECURE`, and `REFRESH_TOKEN_COOKIE_SAME_SITE`.

## Hashing

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
        HASH_MEMORY_COST
      </code>
    </td>
    
    <td>
      How much memory to use when generating hashes, in KiB.
    </td>
    
    <td>
      <code>
        4096
      </code>
      
       (4 MiB)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        HASH_LENGTH
      </code>
    </td>
    
    <td>
      The length of the hash function output in bytes.
    </td>
    
    <td>
      <code>
        32
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        HASH_TIME_COST
      </code>
    </td>
    
    <td>
      The amount of passes (iterations) used by the hash function. It increases hash strength at the cost of time required to compute.
    </td>
    
    <td>
      <code>
        3
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        HASH_PARALLELISM
      </code>
    </td>
    
    <td>
      The amount of threads to compute the hash on. Each thread has a memory pool with <code>
        HASH_MEMORY_COST
      </code>
      
       size.
    </td>
    
    <td>
      <code>
        1
      </code>
      
       (single thread)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        HASH_TYPE
      </code>
    </td>
    
    <td>
      The variant of the hash function (<code>
        0
      </code>
      
      : argon2d, <code>
        1
      </code>
      
      : argon2i, or <code>
        2
      </code>
      
      : argon2id).
    </td>
    
    <td>
      <code>
        2
      </code>
      
       (argon2id)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        HASH_ASSOCIATED_DATA
      </code>
    </td>
    
    <td>
      An extra and optional non-secret value. The value will be included Base64 encoded in the parameters portion of the digest.
    </td>
    
    <td>
      
    </td>
  </tr>
</tbody>
</table>

Argon2's hashing function is used by Directus to hash user passwords, generate hashes for the `Hash` field type in collections, and for use in the `/utils/hash/generate` endpoint.

All `HASH_*` environment variable parameters are passed to the `argon2.hash` function. See the [node-argon2 library options page](https://github.com/ranisalt/node-argon2/wiki/Options) for reference.

<callout icon="material-symbols:info-outline">

**Memory Usage**<br />


Modifying `HASH_MEMORY_COST` and/or `HASH_PARALLELISM` will affect the amount of memory directus uses when computing hashes; each thread gets `HASH_MEMORY_COST` amount of memory, so the total additional memory will be these two values multiplied. This may cause out of memory errors, especially when running in containerized environments.

</callout>

## CORS

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
        CORS_ENABLED
      </code>
    </td>
    
    <td>
      Whether or not to enable the CORS headers.
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
        CORS_ORIGIN
      </code>
    </td>
    
    <td>
      Value for the <code>
        Access-Control-Allow-Origin
      </code>
      
       header. Use <code>
        true
      </code>
      
       to match the Origin header, or provide a domain or a CSV of domains for specific access.
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
        CORS_METHODS
      </code>
    </td>
    
    <td>
      Value for the <code>
        Access-Control-Allow-Methods
      </code>
      
       header.
    </td>
    
    <td>
      <code>
        GET,POST,PATCH,DELETE
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        CORS_ALLOWED_HEADERS
      </code>
    </td>
    
    <td>
      Value for the <code>
        Access-Control-Allow-Headers
      </code>
      
       header.
    </td>
    
    <td>
      <code>
        Content-Type,Authorization
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        CORS_EXPOSED_HEADERS
      </code>
    </td>
    
    <td>
      Value for the <code>
        Access-Control-Expose-Headers
      </code>
      
       header.
    </td>
    
    <td>
      <code>
        Content-Range
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        CORS_CREDENTIALS
      </code>
    </td>
    
    <td>
      Whether or not to send the <code>
        Access-Control-Allow-Credentials
      </code>
      
       header.
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
        CORS_MAX_AGE
      </code>
    </td>
    
    <td>
      Value for the <code>
        Access-Control-Max-Age
      </code>
      
       header.
    </td>
    
    <td>
      <code>
        18000
      </code>
    </td>
  </tr>
</tbody>
</table>

For more details about each configuration variable, please see the [CORS package documentation](https://www.npmjs.com/package/cors#configuration-options).

## Rate Limiting

You can use the built-in rate-limiter to prevent users from hitting the API too much.

Enabling the rate-limiter with no other options will set a default maximum of 50 requests per second, tracked in memory.

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
        RATE_LIMITER_ENABLED
      </code>
    </td>
    
    <td>
      Whether or not to enable rate limiting per IP on the API.
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
        RATE_LIMITER_POINTS
      </code>
    </td>
    
    <td>
      The amount of allowed hits per duration.
    </td>
    
    <td>
      <code>
        50
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        RATE_LIMITER_DURATION
      </code>
    </td>
    
    <td>
      The time window in seconds in which the points are counted.
    </td>
    
    <td>
      <code>
        1
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        RATE_LIMITER_STORE
      </code>
    </td>
    
    <td>
      Where to store the rate limiter counts. One of <code>
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
        RATE_LIMITER_HEALTHCHECK_THRESHOLD
      </code>
    </td>
    
    <td>
      Healthcheck timeout threshold in milliseconds.
    </td>
    
    <td>
      <code>
        150
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        RATE_LIMITER_GLOBAL_ENABLED
      </code>
    </td>
    
    <td>
      Whether or not to enable global rate limiting on the API.
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
        RATE_LIMITER_GLOBAL_POINTS
      </code>
    </td>
    
    <td>
      The total amount of allowed hits per duration.
    </td>
    
    <td>
      <code>
        1000
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        RATE_LIMITER_GLOBAL_DURATION
      </code>
    </td>
    
    <td>
      The time window in seconds in which the points are counted.
    </td>
    
    <td>
      <code>
        1
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        RATE_LIMITER_GLOBAL_HEALTHCHECK_THRESHOLD
      </code>
    </td>
    
    <td>
      Healthcheck timeout threshold in milliseconds.
    </td>
    
    <td>
      <code>
        150
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        RATE_LIMITER_REGISTRATION_ENABLED
      </code>
    </td>
    
    <td>
      Whether or not to enable rate limiting per IP on the user registration.
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
        RATE_LIMITER_REGISTRATION_POINTS
      </code>
    </td>
    
    <td>
      The amount of allowed hits per duration.
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
        RATE_LIMITER_REGISTRATION_DURATION
      </code>
    </td>
    
    <td>
      The time window in seconds in which the points are counted.
    </td>
    
    <td>
      <code>
        60
      </code>
    </td>
  </tr>
</tbody>
</table>

### Pressure-Based Rate Limiter

This rate-limiter prevents the API from accepting new requests while the server is experiencing high load. This continuously monitors the current event loop and memory usage, and error with a 503 early when the system is overloaded.

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
        PRESSURE_LIMITER_ENABLED
      </code>
    </td>
    
    <td>
      Whether or not to enable pressure-based rate limiting on the API.
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
        PRESSURE_LIMITER_SAMPLE_INTERVAL
      </code>
    </td>
    
    <td>
      The time window for measuring pressure in milliseconds.
    </td>
    
    <td>
      <code>
        250
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        PRESSURE_LIMITER_MAX_EVENT_LOOP_UTILIZATION
      </code>
    </td>
    
    <td>
      The maximum allowed utilization where <code>
        1
      </code>
      
       is 100% loop utilization.
    </td>
    
    <td>
      <code>
        0.99
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        PRESSURE_LIMITER_MAX_EVENT_LOOP_DELAY
      </code>
    </td>
    
    <td>
      The maximum amount of time the current loop can be delayed in milliseconds.
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
        PRESSURE_LIMITER_MAX_MEMORY_RSS
      </code>
    </td>
    
    <td>
      The maximum allowed memory Resident Set Size (RSS) in bytes.
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
        PRESSURE_LIMITER_MAX_MEMORY_HEAP_USED
      </code>
    </td>
    
    <td>
      The maximum allowed heap usage in bytes.
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
        PRESSURE_LIMITER_RETRY_AFTER
      </code>
    </td>
    
    <td>
      Sets the <code>
        Retry-After
      </code>
      
       header when the rate limiter is triggered.
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
  </tr>
</tbody>
</table>

### Email Rate Limiting

You can use the built-in email rate-limiter. This rate limiter has a queue to prevent mails from being dropped if a short burst happens to hit the limit.

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
        RATE_LIMITER_EMAIL_ENABLED
      </code>
    </td>
    
    <td>
      Whether or not to enable rate limiting for emails.
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
        RATE_LIMITER_EMAIL_POINTS
      </code>
    </td>
    
    <td>
      The amount of allowed emails per duration.
    </td>
    
    <td>
      <code>
        60
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        RATE_LIMITER_EMAIL_DURATION
      </code>
    </td>
    
    <td>
      The time window in seconds in which the points are counted.
    </td>
    
    <td>
      <code>
        60
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        RATE_LIMITER_EMAIL_QUEUE_SIZE
      </code>
    </td>
    
    <td>
      The amount of items that will be queued before erroring.
    </td>
    
    <td>
      <code>
        1000000
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        RATE_LIMITER_EMAIL_ERROR_MESSAGE
      </code>
    </td>
    
    <td>
      A custom error message which is appended to the rate limit error.
    </td>
    
    <td>
      <code>
        ''
      </code>
    </td>
  </tr>
</tbody>
</table>

### Email Flows Operation Rate Limiting

You can use the built-in email rate-limiter. works the same as the api rate limiter, if you hit the limit then the flow operation starts erroring and dropping the mails.

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
        RATE_LIMITER_EMAIL_FLOWS_ENABLED
      </code>
    </td>
    
    <td>
      Whether or not to enable rate limiting for the <code>
        Send Email
      </code>
      
       operation.
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
        RATE_LIMITER_EMAIL_FLOWS_POINTS
      </code>
    </td>
    
    <td>
      The amount of allowed hits per duration.
    </td>
    
    <td>
      <code>
        1
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        RATE_LIMITER_EMAIL_FLOWS_DURATION
      </code>
    </td>
    
    <td>
      The time window in seconds in which the points are counted.
    </td>
    
    <td>
      <code>
        60
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        RATE_LIMITER_EMAIL_FLOWS_ERROR_MESSAGE
      </code>
    </td>
    
    <td>
      A custom error message which is appended to the rate limit error.
    </td>
    
    <td>
      <code>
        ''
      </code>
    </td>
  </tr>
</tbody>
</table>

## Limits & Optimizations

Allows you to configure hard technical limits, to prevent abuse and optimize for your particular server environment.

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
        RELATIONAL_BATCH_SIZE
      </code>
    </td>
    
    <td>
      How many rows are read into memory at a time when constructing nested relational datasets.
    </td>
    
    <td>
      25000
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        EXPORT_BATCH_SIZE
      </code>
    </td>
    
    <td>
      How many rows are read into memory at a time when constructing exports.
    </td>
    
    <td>
      5000
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        USERS_ADMIN_ACCESS_LIMIT
      </code>
    </td>
    
    <td>
      How many active users with admin privilege are allowed.
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
        USERS_APP_ACCESS_LIMIT
      </code>
    </td>
    
    <td>
      How many active users with access to the Data Studio are allowed.
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
        USERS_API_ACCESS_LIMIT
      </code>
    </td>
    
    <td>
      How many active API access users are allowed.
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
        GRAPHQL_QUERY_TOKEN_LIMIT
      </code>
    </td>
    
    <td>
      How many GraphQL query tokens will be parsed.
    </td>
    
    <td>
      5000
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        MAX_PAYLOAD_SIZE
      </code>
    </td>
    
    <td>
      Controls the maximum request body size. Accepts number of bytes, or human readable string.
    </td>
    
    <td>
      <code>
        1mb
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        MAX_BATCH_MUTATION
      </code>
    </td>
    
    <td>
      The maximum number of items for batch mutations when creating, updating and deleting.
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
        MAX_RELATIONAL_DEPTH
      </code>
    </td>
    
    <td>
      The maximum depth when filtering / querying relational fields, with a minimum value of <code>
        2
      </code>
      
      .
    </td>
    
    <td>
      <code>
        10
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        MAX_JSON_QUERY_DEPTH
      </code>
    </td>
    
    <td>
      The maximum json path depth when querying JSON fields.
    </td>
    
    <td>
      <code>
        10
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        QUERY_LIMIT_DEFAULT
      </code>
    </td>
    
    <td>
      The default query limit used when not defined in the API request.
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
        QUERY_LIMIT_MAX
      </code>
    </td>
    
    <td>
      The maximum query limit accepted on API requests.
    </td>
    
    <td>
      <code>
        -1
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        QUERYSTRING_MAX_PARSE_DEPTH
      </code>
    </td>
    
    <td>
      The maximum object depth when parsing URL query parameters using the querystring format
    </td>
    
    <td>
      <code>
        10
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        QUERYSTRING_ARRAY_LIMIT
      </code>
    </td>
    
    <td>
      The array limit when parsing URL query parameters using the querystring format
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
        MAX_IMPORT_ERRORS
      </code>
    </td>
    
    <td>
      The maximum number of validation errors permitted while importing records before the process is cancelled and the errors returned.
    </td>
    
    <td>
      <code>
        1000
      </code>
    </td>
  </tr>
</tbody>
</table>
