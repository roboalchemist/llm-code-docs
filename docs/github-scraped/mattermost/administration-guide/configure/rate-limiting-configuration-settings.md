orphan

:

nosearch

:

With self-hosted deployments, rate limiting prevents your Mattermost
server from being overloaded with too many requests, and decreases the
risk and impact of third-party applications or malicious attacks on your
server.

Configure rate limiting settings by going to **System Console \>
Environment \> Rate Limiting**, or by editing the `config.json` file as
described in the following tables. Changes to configuration settings in
this section require a server restart before taking effect.

:::: important
::: title
Important
:::

Mattermost rate limiting configuration settings are intended for small
deployments of Mattermost up to a few hundred users, and is not intended
for larger, Enterprise-scale deployments.
::::

# Enable rate limiting

+----------------------------------------+--------------------------------------+
| Enable or disable rate limiting to     | - System Config path: **Environment  |
| throttle APIs to a specified number of |   \> Rate Limiting**                 |
| requests per second.                   | - `config.json` setting:             |
|                                        |   `RateLimitSettings` \> `Enable` \> |
| - **true**: APIs are throttled at the  |   `false`                            |
|   rate specified by the [Maximum       | - Environment variable:              |
|   queries per                          |   `MM_RATELIMITSETTINGS_ENABLE`      |
|   second](#maximum-queries-per-second) |                                      |
|   configuration setting.               |                                      |
| - **false**: **(Default)** API access  |                                      |
|   isn't throttled.                     |                                      |
+----------------------------------------+--------------------------------------+

# Maximum queries per second

+----------------------------------+-------------------------------------+
| Throttle the API at this number  | - System Config path: **Environment |
| of requests per second when      |   \> Rate Limiting**                |
| [rate                            | - `config.json` setting:            |
| limiting](#enable-rate-limiting) |   `RateLimitSettings` \> `PerSec`   |
| is enabled.                      |   \> `10`                           |
|                                  | - Environment variable:             |
| Numerical input. Default is      |   `MM_RATELIMITSETTINGS_PERSEC`     |
| **10**.                          |                                     |
|                                  |                                     |
| Increase this value to accept    |                                     |
| more requests each second, and   |                                     |
| decrease this value to allow     |                                     |
| fewer requests.                  |                                     |
+----------------------------------+-------------------------------------+

# Maximum burst size

+----------------------------------+--------------------------------------+
| The maximum number of requests   | - System Config path: **Environment  |
| allowed beyond the per second    |   \> Rate Limiting**                 |
| query limit when [rate           | - `config.json` setting:             |
| limiting](#enable-rate-limiting) |   `RateLimitSettings` \> `MaxBurst`  |
| is enabled.                      |   \> `100`                           |
|                                  | - Environment variable:              |
| Numerical input. Default is      |   `MM_RATELIMITSETTINGS_MAXBURST`    |
| **100**.                         |                                      |
|                                  |                                      |
| Increase this value to allow for |                                      |
| more concurrent requests to be   |                                      |
| handled, and decrease this value |                                      |
| to limit this capacity.          |                                      |
+----------------------------------+--------------------------------------+

# Memory store size

+----------------------------------+------------------------------------------+
| The maximum number of user       | - System Config path: **Environment \>   |
| sessions connected to the system |   Rate Limiting**                        |
| as determined by vary rate limit | - `config.json` setting:                 |
| settings when [rate              |   `RateLimitSettings` \>                 |
| limiting](#enable-rate-limiting) |   `MemoryStoreSize` \> `10000`           |
| is enabled.                      | - Environment variable:                  |
|                                  |   `MM_RATELIMITSETTINGS_MEMORYSTORESIZE` |
| Numerical input. Default is      |                                          |
| **10000**. Typically set to the  |                                          |
| number of users in the system.   |                                          |
|                                  |                                          |
| We recommend setting this value  |                                          |
| to the expected number of users. |                                          |
| A higher value may result in     |                                          |
| underutilized resources, and a   |                                          |
| lower value may result in user   |                                          |
| sessions/tokens expiring too     |                                          |
| frequently.                      |                                          |
+----------------------------------+------------------------------------------+

# Vary rate limit by remote address

+----------------------------------+-------------------------------------------+
| Configure Mattermost to rate     | - System Config path: **Environment \>    |
| limit API access by IP address   |   Rate Limiting**                         |
| when [rate                       | - `config.json` setting:                  |
| limiting](#enable-rate-limiting) |   `RateLimitSettings` \>                  |
| is enabled.                      |   `VaryByRemoteAddr` \> `true`            |
|                                  | - Environment variable:                   |
| - **true**: **(Default)** Rate   |   `MM_RATELIMITSETTINGS_VARYBYREMOTEADDR` |
|   limit API access by IP         |                                           |
|   address. Recommended when      |                                           |
|   using a proxy.                 |                                           |
| - **false**: Rate limiting does  |                                           |
|   not vary by IP address.        |                                           |
+----------------------------------+-------------------------------------------+

# Vary rate limit by user

+----------------------------------+--------------------------------------+
| Configure Mattermost to rate     | - System Config path: **Environment  |
| limit API access by              |   \> Rate Limiting**                 |
| authentication token or not when | - `config.json` setting:             |
| [rate                            |   `RateLimitSettings` \>             |
| limiting](#enable-rate-limiting) |   `VaryByUser` \> `false`            |
| is enabled.                      | - Environment variable:              |
|                                  |   `MM_RATELIMITSETTINGS_VARYBYUSER`  |
| - **true**: Rate limit API       |                                      |
|   access by user authentication  |                                      |
|   token. Recommended when using  |                                      |
|   a proxy.                       |                                      |
| - **false**: **(Default)** Rate  |                                      |
|   limiting does not vary by user |                                      |
|   authentication token.          |                                      |
+----------------------------------+--------------------------------------+

# Vary rate limit by HTTP header

+-------------------------------+---------------------------------------+
| Configure Mattermost to vary  | - System Config path: **Environment   |
| rate limiting API access by   |   \> Rate Limiting**                  |
| the HTTP header field         | - `config.json` setting:              |
| specified. Recommended when   |   `RateLimitSettings` \>              |
| you're using a proxy.         |   `VaryByHeader` \> `""`              |
|                               | - Environment variable:               |
| - When configuring NGINX, set |   `MM_RATELIMITSETTINGS_VARYBYHEADER` |
|   this to **X-Real-IP**.      |                                       |
| - When configuring AmazonELB, |                                       |
|   set this to                 |                                       |
|   **X-Forwarded-For**.        |                                       |
+-------------------------------+---------------------------------------+
