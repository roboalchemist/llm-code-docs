# Environment configuration settings

Review and manage the following environmental configuration options in
the System Console by selecting the **Product**
[\|product-list\|](##SUBST##|product-list|) menu, selecting **System
Console**, and then selecting **Environment**:

- [Web server](#web-server)
- [Database](#database)
- [Enterprise search](#enterprise-search)
- [File storage](#file-storage)
- [Image proxy](#image-proxy)
- [SMTP](#smtp)
- [Push notification server](#push-notification-server)
- [High availability](#high-availability)
- [Rate limiting](#rate-limiting)
- [Logging](#logging)
- [Session lengths](#session-lengths)
- [Performance monitoring](#performance-monitoring)
- [Developer](#developer)
- [Mobile security](#mobile-security)
- [config.json-only settings](#config-json-only-settings)

:::: tip
::: title
Tip
:::

System admins managing a self-hosted Mattermost deployment can edit the
`config.json` file as described in the following tables. Each
configuration value below includes a JSON path to access the value
programmatically in the `config.json` file using a JSON-aware tool. For
example, the `SiteURL` value is under `ServiceSettings`.

- If using a tool such as [jq](https://stedolan.github.io/jq/), you\'d
  enter: `cat config/config.json | jq '.ServiceSettings.SiteURL'`
- When working with the `config.json` file manually, look for an object
  such as `ServiceSettings`, then within that object, find the key
  `SiteURL`.
::::

## Web server

With self-hosted deployments, you can configure the network environment
in which Mattermost is deployed by going to **System Console \>
Environment \> Web Server**, or by updating the `config.json` file as
described in the following tables. Changes to configuration settings in
this section require a server restart before taking effect.

### Site URL

+-----------------------------------+-----------------------------------+
| The URL that users use to access  | - System Config path:             |
| Mattermost. The port number is    |   **Environment \> Web Server**   |
| required if it's not a standard   | - `config.json` setting:          |
| port, such as 80 or 443. This     |   `ServiceSettings` \> `SiteURL`  |
| field is required.                | - Environment variable:           |
|                                   |   `MM_SERVICESETTINGS_SITEURL`    |
| Select the **Test Live URL**      |                                   |
| button in the System Console to   |                                   |
| validate the Site URL.            |                                   |
+-----------------------------------+-----------------------------------+

:::: note
::: title
Note
:::

- The URL may contain a subpath, such as
  `https://example.com/company/mattermost`.
- If you change the Site URL value, log out of the Desktop App, and sign
  back in using the new domain.
- If Site URL is not set:
  - Email notifications will contain broken links, and email batching
    will not work.
  - Authentication via OAuth 2.0, including GitLab, Google, and Entra
    ID, will fail.
  - Plugins may not work as expected.
::::

### Maximum URL length

+------------------------------+-----------------------------------------+
| The longest URL, in          | - System Config path: N/A               |
| characters, including query  | - `config.json` setting:                |
| parameters, accepted by the  |   `ServiceSettings` \>                  |
| Mattermost server. Longer    |   `MaximumURLLength` \> `2048`          |
| URLs are rejected, and API   | - Environment variable:                 |
| calls fail with an error.    |   `MM_SERVICESETTINGS_MAXIMUMURLLENGTH` |
|                              |                                         |
| Numeric value. Default is    |                                         |
| **2048** characters.         |                                         |
+------------------------------+-----------------------------------------+

### Web server listen address

+---------------------------------+--------------------------------------+
| The address and port to which   | - System Config path: **Environment  |
| to bind and listen. Specifying  |   \> Web Server**                    |
| `:8065` will bind to all        | - `config.json` setting:             |
| network interfaces. Specifying  |   `ServiceSettings` \>               |
| `127.0.0.1:8065` will only bind |   `ListenAddress`                    |
| to the network interface having | - Environment variable:              |
| that IP address.                |   `MM_SERVICESETTINGS_LISTENADDRESS` |
|                                 |                                      |
| If you choose a port of a lower |                                      |
| level (called "system ports" or |                                      |
| "well-known ports", in the      |                                      |
| range of 0-1023), you must have |                                      |
| permissions to bind to that     |                                      |
| port.                           |                                      |
+---------------------------------+--------------------------------------+

:::: note
::: title
Note
:::

Web server uses `address:port` (e.g., `":8065"`), while
`Metrics <administration-guide/configure/environment-configuration-settings:listen address>`{.interpreted-text
role="ref"} uses a port number only (e.g., `8067`).
::::

### Forward port 80 to 443

+------------------------------+---------------------------------------+
| Forward insecure traffic     | - System Config path: **Environment   |
| from port 80 to port 443.    |   \> Web Server**                     |
|                              | - `config.json` setting:              |
| - **true**: Forwards all     |   `ServiceSettings` \>                |
|   insecure traffic from port |   `Forward80To443` \> `false`         |
|   80 to secure port 443.     | - Environment variable:               |
| - **false**: **(Default)**   |   `MM_SERVICESETTINGS_FORWARD80TO443` |
|   When using a proxy such as |                                       |
|   NGINX in front of          |                                       |
|   Mattermost this setting is |                                       |
|   unnecessary and should be  |                                       |
|   set to false.              |                                       |
+------------------------------+---------------------------------------+

### Web server connection security

+----------------------------------+-------------------------------------------+
| Connection security between      | - System Config path: **Environment \>    |
| Mattermost clients and the       |   Web Server**                            |
| server.                          | - `config.json` setting:                  |
|                                  |   `ServiceSettings` \>                    |
| - **Not specified**: Mattermost  |   `ConnectionSecurity`                    |
|   will connect over an unsecure  | - Environment variable:                   |
|   connection.                    |   `MM_SERVICESETTINGS_CONNECTIONSECURITY` |
| - **TLS**: Encrypts the          |                                           |
|   communication between          |                                           |
|   Mattermost clients and your    |                                           |
|   server.                        |                                           |
+----------------------------------+-------------------------------------------+

See the
`setting up TLS for Mattermost </deployment-guide/server/setup-tls>`{.interpreted-text
role="doc"} for details.

### TLS certificate file

+-------------------------------+--------------------------------------+
| The path to the certificate   | - System Config path: **Environment  |
| file to use for TLS           |   \> Web Server**                    |
| connection security.          | - `config.json` setting:             |
|                               |   `ServiceSettings` \> `TLSCertFile` |
| String input.                 | - Environment variable:              |
|                               |   `MM_SERVICESETTINGS_TLSCERTFILE`   |
+-------------------------------+--------------------------------------+

### TLS key file

+--------------------------------+-------------------------------------+
| The path to the TLS key file   | - System Config path: **Environment |
| to use for TLS connection      |   \> Web Server**                   |
| security.                      | - `config.json` setting:            |
|                                |   `ServiceSettings` \> `TLSKeyFile` |
| String input.                  | - Environment variable:             |
|                                |   `MM_SERVICESETTINGS_TLSKEYFILE`   |
+--------------------------------+-------------------------------------+

### Use Let\'s Encrypt

+----------------------------------+---------------------------------------+
| Enable the automatic retrieval   | - System Config path: **Environment   |
| of certificates from Let's       |   \> Web Server**                     |
| Encrypt.                         | - `config.json` setting:              |
|                                  |   `ServiceSettings` \>                |
| - **true**: The certificate will |   `UseLetsEncrypt` \> `false`         |
|   be retrieved when a client     | - Environment variable:               |
|   attempts to connect from a new |   `MM_SERVICESETTINGS_USELETSENCRYPT` |
|   domain. This will work with    |                                       |
|   multiple domains.              |                                       |
| - **false**: **(Default)**       |                                       |
|   Manual certificate             |                                       |
|   specification based on the TLS |                                       |
|   Certificate File and TLS Key   |                                       |
|   File specified above.          |                                       |
+----------------------------------+---------------------------------------+

See the
`setting up TLS for Mattermost </deployment-guide/server/setup-tls>`{.interpreted-text
role="doc"} for details on setting up Let\'s Encrypt.

### Let\'s Encrypt certificate cache file

+---------------------------+--------------------------------------------------------+
| The path to the file      | - System Config path: **Environment \> Web Server**    |
| where certificates and    | - `config.json` setting: `ServiceSettings` \>          |
| other data about the      |   `LetsEncryptCertificateCacheFile`                    |
| Let's Encrypt service     | - Environment variable:                                |
| will be stored.           |   `MM_SERVICESETTINGS_LETSENCRYPTCERTIFICATECACHEFILE` |
|                           |                                                        |
| File path input.          |                                                        |
+---------------------------+--------------------------------------------------------+

### Read timeout

+-----------------------------+----------------------------------------+
| Maximum time allowed from   | - System Config path: **Environment \> |
| when the connection is      |   Web Server**                         |
| accepted to when the        | - `config.json` setting:               |
| request body is fully read. |   `ServiceSettings` \> `ReadTimeout`   |
|                             |   \> `300`                             |
| Numerical input in seconds. | - Environment variable:                |
| Default is **300** seconds. |   `MM_SERVICESETTINGS_READTIMEOUT`     |
+-----------------------------+----------------------------------------+

### Write timeout

+------------------------------+---------------------------------------+
| - If using HTTP (insecure),  | - System Config path: **Environment   |
|   this is the maximum time   |   \> Web Server**                     |
|   allowed from the end of    | - `config.json` setting:              |
|   reading the request        |   `ServiceSettings` \> `WriteTimeout` |
|   headers until the response |   \> `300`                            |
|   is written.                | - Environment variable:               |
| - If using HTTPS, it\'s the  |   `MM_SERVICESETTINGS_WRITETIMEOUT`   |
|   total time from when the   |                                       |
|   connection is accepted     |                                       |
|   until the response is      |                                       |
|   written.                   |                                       |
|                              |                                       |
| Numerical input in seconds.  |                                       |
| Default is **300** seconds.  |                                       |
+------------------------------+---------------------------------------+

### Idle timeout

+-----------------------------+----------------------------------------+
| Set an explicit idle        | - System Config path: **Environment \> |
| timeout in the HTTP server. |   Web Server**                         |
| This is the maximum time    | - `config.json` setting:               |
| allowed before an idle      |   `ServiceSettings` \> `IdleTimeout`   |
| connection is disconnected. |   \> `300`                             |
|                             | - Environment variable:                |
| Numerical input in seconds. |   `MM_SERVICESETTINGS_IDLETIMEOUT`     |
| Default is **300** seconds. |                                        |
+-----------------------------+----------------------------------------+

### Webserver mode

+--------------------------------+--------------------------------------+
| We recommend gzip to improve   | - System Config path: **Environment  |
| performance unless your        |   \> Web Server**                    |
| environment has specific       | - `config.json` setting:             |
| restrictions, such as a web    |   `ServiceSettings` \>               |
| proxy that distributes gzip    |   `WebserverMode` \> `"gzip"`        |
| files poorly.                  | - Environment variable:              |
|                                |   `MM_SERVICESETTINGS_WEBSERVERMODE` |
| - **gzip**: **(Default)** The  |                                      |
|   Mattermost server will serve |                                      |
|   static files compressed with |                                      |
|   gzip to improve performance. |                                      |
|   gzip compression applies to  |                                      |
|   the HTML, CSS, Javascript,   |                                      |
|   and other static content     |                                      |
|   files that make up the       |                                      |
|   Mattermost web client.       |                                      |
| - **Uncompressed**: The        |                                      |
|   Mattermost server will serve |                                      |
|   static files uncompressed.   |                                      |
| - **Disabled**: The Mattermost |                                      |
|   server will not serve static |                                      |
|   files.                       |                                      |
+--------------------------------+--------------------------------------+

### Enable insecure outgoing connections

+--------------------------+----------------------------------------------------------+
| Configure Mattermost to  | - System Config path: **Environment \> Web Server**      |
| allow insecure outgoing  | - `config.json` setting: `ServiceSettings` \>            |
| connections.             |   `EnableInsecureOutgoingConnections` \> `false`         |
|                          | - Environment variable:                                  |
| - **true**: Outgoing     |   `MM_SERVICESETTINGS_ENABLEINSECUREOUTGOINGCONNECTIONS` |
|   HTTPS requests,        |                                                          |
|   including S3 clients,  |                                                          |
|   can accept unverified, |                                                          |
|   self-signed            |                                                          |
|   certificates. For      |                                                          |
|   example, outgoing      |                                                          |
|   webhooks to a server   |                                                          |
|   with a self-signed TLS |                                                          |
|   certificate, using any |                                                          |
|   domain, will be        |                                                          |
|   allowed, and will skip |                                                          |
|   TLS verification.      |                                                          |
| - **false**:             |                                                          |
|   **(Default)** Only     |                                                          |
|   secure HTTPS requests  |                                                          |
|   are allowed.           |                                                          |
+--------------------------+----------------------------------------------------------+

:::: warning
::: title
Warning
:::

Enabling this feature makes these connections susceptible to
man-in-the-middle attacks.
::::

### Managed resource paths

+---------------------------------------+---------------------------------------------+
| A comma-separated list of paths       | - System Config path: **Environment \> Web  |
| within the Mattermost domain that are |   Server**                                  |
| managed by a third party service      | - `config.json` setting: `ServiceSettings`  |
| instead of Mattermost itself.         |   \> `ManagedResourcePaths`                 |
|                                       | - Environment variable:                     |
| Links to these paths will be opened   |   `MM_SERVICESETTINGS_MANAGEDRESOURCEPATHS` |
| in a new tab/window by Mattermost     |                                             |
| apps.                                 |                                             |
|                                       |                                             |
| For example, if Mattermost is running |                                             |
| on `https://mymattermost.com`,        |                                             |
| setting this to conference will cause |                                             |
| links such as                         |                                             |
| `https://mymattermost.com/conference` |                                             |
| to open in a new window.              |                                             |
+---------------------------------------+---------------------------------------------+

:::: note
::: title
Note
:::

When using the Mattermost Desktop App, additional configuration is
required to open the link within the Desktop App instead of in a
browser. See the
`desktop managed resources </deployment-guide/desktop/desktop-app-managed-resources>`{.interpreted-text
role="doc"} documentation for details.
::::

### Reload configuration from disk

+---------------------------------+------------------------------------+
| You must change the database    | - System Config path:              |
| line in the `config.json` file, |   **Environment \> Web Server**    |
| and then reload configuration   | - `config.json` setting: N/A       |
| to fail over without taking the | - Environment variable: N/A        |
| server down.                    |                                    |
|                                 |                                    |
| Select the **Reload             |                                    |
| configuration from disk**       |                                    |
| button in the System Console    |                                    |
| after changing your database    |                                    |
| configuration. Then, go to      |                                    |
| **Environment \> Database** and |                                    |
| select **Recycle Database       |                                    |
| Connections** to complete the   |                                    |
| reload.                         |                                    |
+---------------------------------+------------------------------------+

### Purge all caches

+---------------------------------+------------------------------------+
| Purge all in-memory caches for  | - System Config path:              |
| sessions, accounts, and         |   **Environment \> Web Server**    |
| channels.                       | - `config.json` setting: N/A       |
|                                 | - Environment variable: N/A        |
| Select the **Purge All Caches** |                                    |
| button in the System Console to |                                    |
| purge all caches.               |                                    |
+---------------------------------+------------------------------------+

:::: note
::: title
Note
:::

Purging the caches may adversely impact performance.
`high availability cluster-based deployments </administration-guide/scale/high-availability-cluster-based-deployment>`{.interpreted-text
role="doc"} will attempt to purge all the servers in the cluster.
::::

### Websocket URL

+-----------------------------+----------------------------------------+
| You can configure the       | - System Config path: N/A              |
| server to instruct clients  | - `config.json` setting:               |
| on where they should try to |   `ServiceSettings` \> `WebsocketURL`  |
| connect websockets to.      |   \> `""`                              |
|                             | - Environment variable:                |
| String input.               |   `MM_SERVICESETTINGS_WEBSOCKETURL`    |
+-----------------------------+----------------------------------------+

:::: note
::: title
Note
:::

We strongly recommend configuring a single websocket URL that matches
the [Site URL](#site-url) configuration setting.
::::

### License file location

+---------------------------+--------------------------------------------+
| The path and filename of  | - System Config path: N/A                  |
| the license file on disk. | - `config.json` setting: `ServiceSettings` |
| On startup, if Mattermost |   \> `LicenseFileLocation` \> `""`         |
| can\'t find a valid       | - Environment variable:                    |
| license in the database   |   `MM_SERVICESETTINGS_LICENSEFILELOCATION` |
| from a previous upload,   |                                            |
| it looks in this path for |                                            |
| the license file.         |                                            |
|                           |                                            |
| String input. Can be an   |                                            |
| absolute path or a path   |                                            |
| relative to the           |                                            |
| `mattermost` directory.   |                                            |
+---------------------------+--------------------------------------------+

### TLS minimum version

+-----------------------------+----------------------------------------+
| The minimum TLS version     | - System Config path: N/A              |
| used by the Mattermost      | - `config.json` setting:               |
| server.                     |   `ServiceSettings` \> `TLSMinVer` \>  |
|                             |   `1.2`                                |
| String input. Default is    | - Environment variable:                |
| **1.2**.                    |   `MM_SERVICESETTINGS_TLSMINVER`       |
+-----------------------------+----------------------------------------+

:::: note
::: title
Note
:::

This setting only takes effect if you are using the built-in server
binary directly, and not using a reverse proxy layer, such as NGINX.
::::

### Trusted proxy IP header

+-------------------------------------+---------------------------------------------+
| Specified headers that will be      | - System Config path: N/A                   |
| checked, one by one, for IP         | - `config.json` setting: `ServiceSettings`  |
| addresses (order is important). All |   \> `TrustedProxyIPHeader` \> `[]`         |
| other headers are ignored.          | - Environment variable:                     |
|                                     |   `MM_SERVICESETTINGS_TRUSTEDPROXYIPHEADER` |
| String array input consisting of    |                                             |
| header names, such as               |                                             |
| `["X-Forwarded-For", "X-Real-Ip"]`. |                                             |
+-------------------------------------+---------------------------------------------+

:::: note
::: title
Note
:::

- The default value of `[]` means that no header will be trusted.
- We recommend keeping the default setting when Mattermost is running
  without a proxy to avoid the client sending the headers and bypassing
  rate limiting and/or the audit log.
- For environments that use a reverse proxy, this issue does not exist,
  provided that the headers are set by the reverse proxy. In those
  environments, only explicitly whitelist the header set by the reverse
  proxy and no additional values.
::::

### Enable Strict Transport Security (HSTS)

+---------------------------+-------------------------------------------+
| - **true**: Adds the      | - System Config path: N/A                 |
|   Strict Transport        | - `config.json` setting:                  |
|   Security (HSTS) header  |   `ServiceSettings` \>                    |
|   to all responses,       |   `TLSStrictTransport` \> `false`         |
|   forcing the browser to  | - Environment variable:                   |
|   request all resources   |   `MM_SERVICESETTINGS_TLSSTRICTTRANSPORT` |
|   via HTTPS.              |                                           |
| - **false**:              |                                           |
|   **(Default)** No        |                                           |
|   restrictions on TLS     |                                           |
|   transport. Strict       |                                           |
|   Transport Security      |                                           |
|   (HSTS) header isn\'t    |                                           |
|   added to responses.     |                                           |
+---------------------------+-------------------------------------------+

See the
[Strict-Transport-Security](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security)
documentation for details.

### Secure TLS transport expiry

+-------------------------+-------------------------------------------------+
| The time, in seconds,   | - System Config path: N/A                       |
| that the browser        | - `config.json` setting: `ServiceSettings` \>   |
| remembers a site is     |   `TLSStrictTransportMaxAge` \> `63072000`      |
| only to be accessed     | - Environment variable:                         |
| using HTTPS. After this |   `MM_SERVICESETTINGS_TLSSTRICTTRANSPORTMAXAGE` |
| period, a site can\'t   |                                                 |
| be accessed using HTTP  |                                                 |
| unless                  |                                                 |
| `TLSStrictTransport` is |                                                 |
| set to `true`.          |                                                 |
|                         |                                                 |
| Numerical input.        |                                                 |
| Default is **63072000** |                                                 |
| (2 years).              |                                                 |
+-------------------------+-------------------------------------------------+

See the
[Strict-Transport-Security](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security)
documentation for details.

### TLS cipher overwrites

+---------------------------+--------------------------------------------+
| Set TLS ciphers           | - System Config path: N/A                  |
| overwrites to meet        | - `config.json` setting: `ServiceSettings` |
| requirements from legacy  |   \> `TLSOverwriteCiphers` \> `[]`         |
| clients which don\'t      | - Environment variable:                    |
| support modern ciphers,   |   `MM_SERVICESETTINGS_TLSOVERWRITECIPHERS` |
| or to limit the types of  |                                            |
| accepted ciphers.         |                                            |
|                           |                                            |
| If none specified, the    |                                            |
| Mattermost server assumes |                                            |
| a set of currently        |                                            |
| considered secure         |                                            |
| ciphers, and allows       |                                            |
| overwrites in the edge    |                                            |
| case.                     |                                            |
|                           |                                            |
| String array input.       |                                            |
+---------------------------+--------------------------------------------+

:::: note
::: title
Note
:::

- This setting only takes effect if you are using the built-in server
  binary directly and not using a reverse proxy layer, such as NGINX.
- See the `ServerTLSSupportedCiphers` variable in
  [/model/config.go](https://github.com/mattermost/mattermost/blob/master/server/public/model/config.go)
  for a list of ciphers considered secure.
::::

### Goroutine health threshold

+--------------------------+-------------------------------------------------+
| Set a threshold on the   | - System Config path: N/A                       |
| number of goroutines     | - `config.json` setting: `ServiceSettings` \>   |
| when the Mattermost      |   `GoroutineHealthThreshold` \> `-1`            |
| system is considered to  | - Environment variable:                         |
| be in a healthy state.   |   `MM_SERVICESETTINGS_GOROUTINEHEALTHTHRESHOLD` |
|                          |                                                 |
| When goroutines exceed   |                                                 |
| this limit, a warning is |                                                 |
| returned in the server   |                                                 |
| logs.                    |                                                 |
|                          |                                                 |
| Numeric input. Default   |                                                 |
| is **-1** which turns    |                                                 |
| off checking for the     |                                                 |
| threshold.               |                                                 |
+--------------------------+-------------------------------------------------+

### Allow cookies for subdomains

+--------------------------+--------------------------------------------------+
| - **true**:              | - System Config path: N/A                        |
|   **(Default)** Allows   | - `config.json` setting: `ServiceSettings` \>    |
|   cookies for subdomains |   `AllowCookiesForSubdomains` \> `true`          |
|   by setting the domain  | - Environment variable:                          |
|   parameter on           |   `MM_SERVICESETTINGS_ALLOWCOOKIESFORSUBDOMAINS` |
|   Mattermost cookies.    |                                                  |
| - **false**: Cookies     |                                                  |
|   aren\'t allowed for    |                                                  |
|   subdomains.            |                                                  |
+--------------------------+--------------------------------------------------+

### Cluster log timeout

+-------------------------+------------------------------------------------------+
| Define the frequency,   | - System Config path: N/A                            |
| in milliseconds, of     | - `config.json` setting: `ServiceSettings` \>        |
| cluster request time    |   `ClusterLogTimeoutMilliseconds` \> `2000`          |
| logging for performance | - Environment variable:                              |
| monitoring.             |   `MM_SERVICESETTINGS_CLUSTERLOGTIMEOUTMILLISECONDS` |
|                         |                                                      |
| Numerical input.        |                                                      |
| Default is **2000**     |                                                      |
| milliseconds (2         |                                                      |
| seconds).               |                                                      |
+-------------------------+------------------------------------------------------+

See the
`performance monitoring </administration-guide/scale/deploy-prometheus-grafana-for-performance-monitoring>`{.interpreted-text
role="doc"} documentation for details.

### Maximum payload size

+---------------------------+------------------------------------------------+
| The maximum payload size  | - System Config path: N/A                      |
| in bytes for all APIs     | - `config.json` setting: `ServiceSettings` \>  |
| except APIs that receive  |   `MaximumPayloadSizeBytes` \> `300000`        |
| a file as an input.       | - Environment variable:                        |
|                           |   `MM_SERVICESETTINGS_MAXIMUMPAYLOADSIZEBYTES` |
| For example, the upload   |                                                |
| attachment API or the API |                                                |
| to upload a custom emoji. |                                                |
|                           |                                                |
| Numerical value. Default  |                                                |
| is **300000** (300 kB).   |                                                |
+---------------------------+------------------------------------------------+

------------------------------------------------------------------------

## Database

With self-hosted deployments, you can configure the database environment
in which Mattermost is deployed by going to **System Console \>
Environment \> Database**, or by editing the `config.json` file as
described in the following tables. Changes to configuration settings in
this section require a server restart before taking effect.

### Driver name

+--------------------------------+-------------------------------------+
| The type of database. Can be   | - System Config path: N/A           |
| either:                        | - `config.json` setting:            |
|                                |   `SqlSettings` \> `DriverName`     |
| - **mysql**: **(Default)**     | - Environment variable:             |
|   Enables driver to MySQL      |   `MM_SQLSETTINGS_DRIVERNAME`       |
|   database.                    |                                     |
| - **postgres**: Enables driver |                                     |
|   to PostgreSQL database.      |                                     |
+--------------------------------+-------------------------------------+

### Data source

+--------------------------------+-------------------------------------+
| The connection string to the   | - System Config path: N/A           |
| master database.               | - `config.json` setting:            |
|                                |   `SqlSettings` \> `DataSource`     |
| String input.                  | - Environment variable:             |
|                                |   `MM_SQLSETTINGS_DATASOURCE`       |
+--------------------------------+-------------------------------------+

#### PostgreSQL databases

When **Driver Name** is set to postgres, use a connection string in the
form of:
`postgres://mmuser:password@hostname_or_IP:5432/mattermost_test?sslmode=disable&connect_timeout=10`

**To use TLS with PostgreSQL databases**

The parameter to encrypt connection against a PostgreSQL server is
sslmode. The library used to interact with PostgreSQL server is
[pq](https://pkg.go.dev/github.com/lib/pq). Currently, it\'s not
possible to use all the values that you could pass to a standard
PostgreSQL Client `psql "sslmode=value"` See the [SSL Mode
Descriptions](https://www.postgresql.org/docs/current/libpq-ssl.html)
documentation for details.

Your database admin must configure the functionality according to the
supported values described below.

+--------------------+---------------+----------------------------------------------------------------------------------------------------------+
| Short description  | Value         | Example of a data source name                                                                            |
| of the `sslmode`   |               |                                                                                                          |
| parameter          |               |                                                                                                          |
+====================+===============+==========================================================================================================+
| Don\'t use TLS /   | `disable`     | `postgres://mmuser:password@hostname_or_IP:5432/mattermost_test ?sslmode=disable&connect_timeout=10`     |
| SSL encryption     |               |                                                                                                          |
| against the        |               |                                                                                                          |
| PostgreSQL server. |               |                                                                                                          |
|                    |               |                                                                                                          |
| Default value in   |               |                                                                                                          |
| file `config.json` |               |                                                                                                          |
+--------------------+---------------+----------------------------------------------------------------------------------------------------------+
| The data is        | `require`     | `postgres://mmuser:password@hostname_or_IP:5432/mattermost_test ?sslmode=require&connect_timeout=10`     |
| encrypted and the  |               |                                                                                                          |
| network is         |               |                                                                                                          |
| trusted.           |               |                                                                                                          |
|                    |               |                                                                                                          |
| Default value is   |               |                                                                                                          |
| `sslmode` when     |               |                                                                                                          |
| omitted.           |               |                                                                                                          |
+--------------------+---------------+----------------------------------------------------------------------------------------------------------+
| The data is        | `verify-ca`   | `postgres://mmuser:password@hostname_or_IP:5432/mattermost_test ?sslmode=verify-ca&connect_timeout=10`   |
| encrypted when     |               |                                                                                                          |
| connecting to a    |               |                                                                                                          |
| trusted server.    |               |                                                                                                          |
+--------------------+---------------+----------------------------------------------------------------------------------------------------------+
| The data is        | `verify-full` | `postgres://mmuser:password@hostname_or_IP:5432/mattermost_test ?sslmode=verify-full&connect_timeout=10` |
| encrypted when     |               |                                                                                                          |
| connecting to a    |               |                                                                                                          |
| trusted server.    |               |                                                                                                          |
+--------------------+---------------+----------------------------------------------------------------------------------------------------------+

#### MySQL Databases

When Driver Name is set to mysql, we recommend using collation over
using charset.

To specify collation:

``` text
"SqlSettings": {
    "DataSource": "<mmuser:password>@tcp(hostname or IP:3306)/mattermost?charset=utf8mb4,utf8&collation=utf8mb4_general_ci",
    [...]
}
```

If collation is omitted, the default collation, `utf8mb4_general_ci` is
used:

``` text
"SqlSettings": {
  "DataSource": "<mmuser:password>@tcp(hostname or IP:3306)/mattermost?charset=utf8mb4,utf8",
  [...]
}
```

:::: note
::: title
Note
:::

If you're using MySQL 8.0 or later, the default collation has changed to
`utf8mb4_0900_ai_ci`. See our
`Database Software Requirements </deployment-guide/software-hardware-requirements>`{.interpreted-text
role="doc"} documentation for details on MySQL 8.0 support.
::::

**To use TLS with MySQL Databases**

The parameter to encrypt connection against a MySQL server is `tls`.

The library used to interact with MySQL is
[Go-MySQL-Driver](https://pkg.go.dev/github.com/go-sql-driver/mysql).

For the moment, it\'s not possible to use all the values that you could
pass to a standard MySQL Client `mysql --ssl-mode=value`. See
[Connection-Encryption Option
Summary](https://dev.mysql.com/doc/refman/8.0/en/connection-options.html#option_general_ssl-mode)
documentation for a version 8.0 example.

Your database admin must configure the functionality according to
supported values described below.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------
  Short description of    Value           Example of a data source name
  the `tls` parameter
  ----------------------- --------------- -----------------------------------------------------------------------------------------------------------------------
  Don\'t use TLS / SSL    `false`         `"<mmuser:password>@tcp(hostname or IP:3306)/mattermost_test ?charset=utf8mb4,utf8&writeTimeout=30s&tls=false"`
  encryption against
  MySQL server.

  Use TLS / SSL           `true`          `"<mmuser:password>@tcp(hostname or IP:3306)/mattermost_test ?charset=utf8mb4,utf8&writeTimeout=30s&tls=true"`
  encryption against
  MySQL server.

  Use TLS / SSL           `skip-verify`   `"<mmuser:password>@tcp(hostname or IP:3306)/mattermost_test ?charset=utf8mb4,utf8&writeTimeout=30s&tls=skip-verify"`
  encryption with a
  self-signed certificate
  against MySQL server.

Use TLS / SSL           `preferred`     `"<mmuser:password>@tcp(hostname or IP:3306)/mattermost_test ?charset=utf8mb4,utf8&writeTimeout=30s&tls=preferred"`
  encryption if server
  advertises a possible
  fallback; unencrypted
  if it\'s not
  advertised
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------

#### AWS High Availablity RDS cluster deployments

For an AWS High Availability RDS cluster deployment, point this
configuration setting to the write/read endpoint at the **cluster**
level to benefit from the AWS failover handling. AWS takes care of
promoting different database nodes to be the writer node. Mattermost
doesn\'t need to manage this. See the
`high availablility database configuration <administration-guide/scale/high-availability-cluster-based-deployment:database configuration>`{.interpreted-text
role="ref"} documentation for details.

### Maximum open connections

+------------------------------+---------------------------------------+
| The maximum number of open   | - System Config path: **Environment   |
| connections to the database. |   \> Database**                       |
|                              | - `config.json` setting:              |
| Numerical input. Default is  |   `SqlSettings` \> `MaxOpenConns` \>  |
| **100**.                     |   `100`                               |
|                              | - Environment variable:               |
|                              |   `MM_SQLSETTINGS_MAXOPENCONNS`       |
+------------------------------+---------------------------------------+

### Maximum idle connections

+------------------------------+---------------------------------------+
| The maximum number of idle   | - System Config path: **Environment   |
| connections held open to the |   \> Database**                       |
| database.                    | - `config.json` setting:              |
|                              |   `SqlSettings` \> `MaxIdleConns` \>  |
| Numerical input. Default is  |   `50`                                |
| **50**. A 2:1 ratio with     | - Environment variable:               |
| MaxOpenConns is recommended. |   `MM_SQLSETTINGS_MAXIDLECONNS`       |
+------------------------------+---------------------------------------+

### Query timeout

+------------------------------+---------------------------------------+
| The amount of time to wait,  | - System Config path: **Environment   |
| in seconds, for a response   |   \> Database**                       |
| from the database after      | - `config.json` setting:              |
| opening a connection and     |   `SqlSettings` \> `QueryTimeout` \>  |
| sending the query.           |   `30`                                |
|                              | - Environment variable:               |
| Numerical input in seconds.  |   `MM_SQLSETTINGS_QUERYTIMEOUT`       |
| Default is **30** seconds.   |                                       |
+------------------------------+---------------------------------------+

### Maximum connection lifetime

+--------------------------+------------------------------------------------+
| Maximum lifetime for a   | - System Config path: **Environment \>         |
| connection to the        |   Database**                                   |
| database, in             | - `config.json` setting: `SqlSettings` \>      |
| milliseconds. Use this   |   `ConnMaxLifetimeMilliseconds` \> `3600000`   |
| setting to configure the | - Environment variable:                        |
| maximum amount of time a |   `MM_SQLSETTINGS_CONNMAXLIFETIMEMILLISECONDS` |
| connection to the        |                                                |
| database may be reused   |                                                |
|                          |                                                |
| Numerical input in       |                                                |
| milliseconds. Default is |                                                |
| **3600000** milliseconds |                                                |
| (1 hour).                |                                                |
+--------------------------+------------------------------------------------+

### Maximum connection idle timeout

+--------------------------+------------------------------------------------+
| Maximum time a database  | - System Config path: **Environment \>         |
| connection can remain    |   Database**                                   |
| idle, in milliseconds.   | - `config.json` setting: `SqlSettings` \>      |
|                          |   `ConnMaxIdleTimeMilliseconds` \> `300000`    |
| Numerical input in       | - Environment variable:                        |
| milliseconds. Default is |   `MM_SQLSETTINGS_CONNMAXIDLETIMEMILLISECONDS` |
| **300000** (5 minutes).  |                                                |
+--------------------------+------------------------------------------------+

### Minimum hashtag length

+--------------------------------+-----------------------------------------+
| Minimum number of characters   | - System Config path: **Environment \>  |
| in a hashtag. This value must  |   Database**                            |
| be greater than or equal to    | - `config.json` setting: `SqlSettings`  |
| **2**.                         |   \> `MinimumHashtagLength` \> `3`      |
|                                | - Environment variable:                 |
|                                |   `MM_SQLSETTINGS_MINIMUMHASHTAGLENGTH` |
+--------------------------------+-----------------------------------------+

:::: note
::: title
Note
:::

MySQL databases must be configured to support searching strings shorter
than three characters. See the [MySQL
documentation](https://dev.mysql.com/doc/refman/8.0/en/fulltext-fine-tuning.html)
for details.
::::

### SQL statement logging

+--------------------------------+-------------------------------------+
| Executed SQL statements can be | - System Config path: **Environment |
| written to the log for         |   \> Database**                     |
| development.                   | - `config.json` setting:            |
|                                |   `SqlSettings` \> `Trace` \>       |
| - **true**: Executing SQL      |   `false`                           |
|   statements are written to    | - Environment variable:             |
|   the log.                     |   `MM_SQLSETTINGS_TRACE`            |
| - **false**: **(Default)** SQL |                                     |
|   statements aren\'t written   |                                     |
|   to the log.                  |                                     |
+--------------------------------+-------------------------------------+

### Recycle database connections

+--------------------------------+-------------------------------------+
| Select the **Recycle Database  | - System Config path: **Environment |
| Connections** button to        |   \> Database**                     |
| manually recycle the           | - `config.json` setting: N/A        |
| connection pool by closing the | - Environment variable: N/A         |
| current set of open            |                                     |
| connections to the database    |                                     |
| within 20 seconds, and then    |                                     |
| creating a new set of          |                                     |
| connections.                   |                                     |
|                                |                                     |
| To fail over without stopping  |                                     |
| the server, change the         |                                     |
| database line in the           |                                     |
| `config.json` file, select     |                                     |
| **Reload Configuration from    |                                     |
| Disk** via **Environment \>    |                                     |
| Web Server**, then select      |                                     |
| **Recycle Database             |                                     |
| Connections**.                 |                                     |
+--------------------------------+-------------------------------------+

### Disable database search

+---------------------------------------------------------------------------------------------+------------------------------------------+
| When                                                                                        | - System Config path: **Environment \>   |
| `enterprise-scale search </administration-guide/scale/enterprise-search>`{.interpreted-text |   Database**                             |
| role="doc"}, database search can be disabled from performing searches.                      | - `config.json` setting: `SqlSettings`   |
|                                                                                             |   \> `DisableDatabaseSearch` \> `false`  |
| - **true**: Disables the use of the database to perform searches. If another search engine  | - Environment variable:                  |
|   isn\'t configured, setting this value to `true` will result in empty search results.      |   `MM_SQLSETTINGS_DISABLEDATABASESEARCH` |
| - **false**: **(Default)** Database search isn\'t disabled.                                 |                                          |
+---------------------------------------------------------------------------------------------+------------------------------------------+

Search behavior in Mattermost depends on which search engines are
enabled:

- When
  `Elasticsearch </administration-guide/scale/elasticsearch-setup>`{.interpreted-text
  role="doc"} or
  `AWS OpenSearch </administration-guide/scale/opensearch-setup>`{.interpreted-text
  role="doc"} is enabled, Mattermost will try to use it first.
- If Elasticsearch fails or is disabled, Mattermost will attempt to use
  Bleve search, if enabled. Bleve search has been deprecated in
  Mattermost v11.0. We recommend using Elasticsearch or OpenSearch for
  enterprise search capabilities.
- If these fail or are disabled, Mattermost tries to search the database
  directly, if this is enabled.
- If all of the above methods fail or are disabled, the search results
  will be empty.

:::: note
::: title
Note
:::

Disabling this configuration setting in larger deployments may improve
server performance in the following areas:

- **Reduced Database Load**: When database search is enabled, every
  search query executed by users needs to interact with the database,
  leading to additional load on the database server. By disabling
  database search, you can avoid these queries, thereby reducing the
  database load.
- **Improved Response Time**: Database searches can be time-consuming,
  especially with large datasets. Disabling database search can result
  in faster response times because the system no longer spends time
  fetching and processing search results from the database.
- **Offloading Search to Indexing Services**: Disabling database search
  often means that searches are offloaded to specialized indexing
  services like Elasticsearch, which are optimized for search
  operations. These services can provide faster and more efficient
  search capabilities compared to traditional database searches.
- **Lower Resource Consumption**: Running search queries directly
  against the database can be resource-intensive (using CPU and memory).
  With database search disabled, these resources can be allocated to
  other critical functions, improving overall system performance.
- **Enhanced Scalability**: As the number of users and data volume grow,
  database search can become less efficient. Specialized search services
  are designed to scale more effectively, enhancing overall system
  scalability and performance.

However, the ability to perform database searches in Mattermost is a
critical feature for many users, particularly when other search engines
aren\'t enabled. Disabling this feature will result in users seeing an
error if they attempt to use the Mattermost Search box. It's important
to balance performance improvements with the needs of your organization
and users.
::::

### Applied schema migrations

A list of all migrations that have been applied to the data store based
on the version information available in the `db_migrations` table.
Select **About Mattermost** from the Product
[\|product-list\|](##SUBST##|product-list|) menu to review the current
database schema version applied to your deployment.

### Active search backend

Read-only display of the currently active backend used for search.
Values can include `none`, `database`, `elasticsearch`, or `bleve`.

### Read replicas

+----------------------------+-----------------------------------------+
| Specifies the connection   | - System Config path: N/A               |
| strings for the read       | - `config.json` setting: `SqlSettings`  |
| replica databases.         |   \> `DataSourceReplicas` \> `[]`       |
|                            | - Environment variable:                 |
|                            |   `MM_SQLSETTINGS_DATASOURCEREPLICAS`   |
+----------------------------+-----------------------------------------+

:::: note
::: title
Note
:::

- Each database connection string in the array must be in the same form
  used for the [Data source](#data-source) setting.
- Space separate multiple read replicas in the array to allow Mattermost
  to load balance read queries across multiple database instances. For
  example, `MM_SQLSETTINGS_DATASOURCEREPLICAS=dc-1 dc-2`
::::

#### AWS High Availability RDS cluster deployments

For an AWS High Availability RDS cluster deployment, point this
configuration setting directly to the underlying read-only node endpoint
within the RDS cluster to circumvent the failover/load balancing that
AWS/RDS takes care of (except for the write traffic). Mattermost has its
own method of balancing the read-only connections and can also balance
those queries to the data source/write+read connection should those
nodes fail. See the
`high availablility database configuration <administration-guide/scale/high-availability-cluster-based-deployment:database configuration>`{.interpreted-text
role="ref"} documentation for details.

### Search replicas

+---------------------------+---------------------------------------------+
| Specifies the connection  | - System Config path: N/A                   |
| strings for the search    | - `config.json` setting: `SqlSettings` \>   |
| replica databases. A      |   `DataSourceSearchReplicas` \> `[]`        |
| search replica is similar | - Environment variable:                     |
| to a read replica, but is |   `MM_SQLSETTINGS_DATASOURCESEARCHREPLICAS` |
| used only for handling    |                                             |
| search queries.           |                                             |
+---------------------------+---------------------------------------------+

:::: note
::: title
Note
:::

Each database connection string in the array must be in the same form
used for the [Data source](#data-source) setting.
::::

#### AWS High Availability RDS cluster deployments

For an AWS High Availability RDS cluster deployment, point this
configuration setting directly to the underlying read-only node endpoint
within the RDS cluster to circumvent the failover/load balancing that
AWS/RDS takes care of (except for the write traffic). Mattermost has its
own method of balancing the read-only connections and can also balance
those queries to the data source/write+read connection should those
nodes fail. See the
`high availablility database configuration <administration-guide/scale/high-availability-cluster-based-deployment:database configuration>`{.interpreted-text
role="ref"} documentation for details.

### Replica lag settings

+----------------------------+-----------------------------------------+
| String array input         | - System Config path: N/A               |
| specifies a connection     | - `config.json` setting: `SqlSettings`  |
| string and user-defined    |   \> `ReplicaLagSettings` \> `[]`       |
| SQL queries on the         | - Environment variable:                 |
| database to measure        |   `MM_SQLSETTINGS_REPLICALAGSETTINGS`   |
| replica lag for a single   |                                         |
| replica instance.          |                                         |
|                            |                                         |
| These settings monitor     |                                         |
| absolute lag based on      |                                         |
| binlog                     |                                         |
| distance/transaction queue |                                         |
| length, and the time taken |                                         |
| for the replica to catch   |                                         |
| up.                        |                                         |
|                            |                                         |
| String array input         |                                         |
| consists of:               |                                         |
|                            |                                         |
| - `DataSource`: The        |                                         |
|   database credentials to  |                                         |
|   connect to the database  |                                         |
|   instance.                |                                         |
| - `QueryAbsoluteLag`: A    |                                         |
|   plain SQL query that     |                                         |
|   must return a single     |                                         |
|   row. The first column    |                                         |
|   must be the node value   |                                         |
|   of the Prometheus        |                                         |
|   metric, and the second   |                                         |
|   column must be the value |                                         |
|   of the lag used to       |                                         |
|   measure absolute lag.    |                                         |
| - `QueryTimeLag`: A plain  |                                         |
|   SQL query that must      |                                         |
|   return a single row. The |                                         |
|   first column must be the |                                         |
|   node value of the        |                                         |
|   Prometheus metric, and   |                                         |
|   the second column must   |                                         |
|   be the value of the lag  |                                         |
|   used to measure the time |                                         |
|   lag.                     |                                         |
+----------------------------+-----------------------------------------+

:::: note
::: title
Note
:::

- The `QueryAbsoluteLag` and `QueryTimeLag` queries must return a single
  row.
- To properly monitor this, you must set up
  `performance monitoring </administration-guide/scale/deploy-prometheus-grafana-for-performance-monitoring>`{.interpreted-text
  role="doc"} for Mattermost.
::::

1. Configure the replica lag metric based on your database type. See
    the following tabs for details on configuring this for each database
    type.

> ::: tab
> AWS Aurora
>
> Add the configuration highlighted below to your
> `SqlSettings.ReplicaLagSettings` array. You only need to add this once
> because replication statistics for AWS Aurora nodes are visible across
> all server instances that are members of the cluster. Be sure to
> change the `DataSource` to point to a single node in the group.
>
> For more information on Aurora replication stats, see the [AWS Aurora
> documentaion](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_global_db_instance_status.html).
>
> Example
>
> ``` {.json emphasize-lines="4,5,6,7,8"}
> {
>   "SqlSettings": {
>       "ReplicaLagSettings": [
>         {
>             "DataSource": "replica-1",
>             "QueryAbsoluteLag": "select server_id, highest_lsn_rcvd-durable_lsn as bindiff from aurora_global_db_instance_status() where server_id=<>",
>             "QueryTimeLag": "select server_id, visibility_lag_in_msec from aurora_global_db_instance_status() where server_id=<>"
>         }
>       ]
>   }
> }
> ```
>
> :::
>
> ::: tab
> MySQL Group Replication
>
> Add the configuration highlighted below to your
> `SqlSettings.ReplicaLagSettings` array. You only need to add this once
> because replication statistics for all nodes are shared across all
> server instances that are members of the MySQL replication group. Be
> sure to change the `DataSource` to point to a single node in the
> group.
>
> For more information on group replication stats, see the [MySQL
> documentation](https://dev.mysql.com/doc/refman/8.0/en/group-replication-replication-group-member-stats.html).
>
> Example
>
> ``` {.json emphasize-lines="4,5,6,7,8"}
> {
>   "SqlSettings": {
>       "ReplicaLagSettings": [
>         {
>             "DataSource": "replica-1",
>             "QueryAbsoluteLag": "select member_id, count_transactions_remote_in_applier_queue FROM performance_schema.replication_group_member_stats where member_id=<>",
>             "QueryTimeLag": ""
>         }
>       ]
>   }
> }
> ```
>
> :::
>
> ::: tab
> PostgreSQL replication slots
>
> 1. Add the configuration highlighted below to your
>     `SqlSettings.ReplicaLagSettings` array. This query should run
>     against the **primary** node in your cluster, to do this change
>     the `DataSource` to match the
>     [SqlSettings.DataSource](#data-source) setting you have
>     configured.
>
> For more information on pg_stat_replication, see the [PostgreSQL
> documentation](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-REPLICATION-VIEW).
>
> > **Example:**
> >
> > ``` {.json emphasize-lines="4,5,6,7,8"}
> > {
> >   "SqlSettings": {
> >       "ReplicaLagSettings": [
> >         {
> >             "DataSource": "postgres://mmuser:password@localhost:5432/mattermost_test?sslmode=disable&connect_timeout=10.",
> >             "QueryAbsoluteLag": "select usename, pg_wal_lsn_diff(pg_current_wal_lsn(),replay_lsn) as metric from pg_stat_replication;",
> >             "QueryTimeLag": ""
> >         }
> >       ]
> >   }
> > }
> > ```
>
> 1. Grant permissions to the database user for `pg_monitor`. This user
>     should be the same user configured above in the `DataSource`
>     string.
>
> > For more information on roles, see the [PostgreSQL
> > documentation](https://www.postgresql.org/docs/10/default-roles.html).
> >
> > ``` sh
> > sudo -u postgres psql
> > postgres=# GRANT pg_monitor TO mmuser;
> > ```
> >
> :::

1. Save the config and restart all Mattermost nodes.
2. Navigate to your Grafana instance monitoring Mattermost and open the
    [Mattermost Performance Monitoring
    v2](https://grafana.com/grafana/dashboards/15582-mattermost-performance-monitoring-v2/)
    dashboard.
3. The `QueryTimeLag` chart is already setup for you utilizing the
    existing `Replica Lag` chart. If using `QueryAbsoluteLag` metric
    clone the `Replica Lag` chart and edit the query to use the below
    absolute lag metrics and modify the title to be
    `Replica Lag Absolute`.

> ``` text
> mattermost_db_replica_lag_abs{instance=~"$server"}
> ```
>
> ![A screenshot showing how to clone a chart within Grafana](../../images/database-configuration-settings-replica-lag-grafana-1.jpg)
>
> ![A screenshot showing the specific edits to make to the cloned grafana chart.](../../images/database-configuration-settings-replica-lag-grafana-2.jpg)

### Replica monitor interval (seconds)

+--------------------------+--------------------------------------------------+
| Specifies how frequently | - System Config path: N/A                        |
| unhealthy replicas will  | - `config.json` setting: `SqlSettings` \>        |
| be monitored for         |   `ReplicaMonitorIntervalSeconds` \> `5`         |
| liveness check.          | - Environment variable:                          |
| Mattermost will          |   `MM_SQLSETTINGS_REPLICAMONITORINTERVALSECONDS` |
| dynamically choose a     |                                                  |
| replica if it\'s alive.  |                                                  |
|                          |                                                  |
| Numerical input. Default |                                                  |
| is 5 seconds.            |                                                  |
+--------------------------+--------------------------------------------------+

:::: note
::: title
Note
:::

This configuration setting is applicable to self-hosted deployments
only.
::::

------------------------------------------------------------------------

## Enterprise search

Core database search happens in a relational database and is intended
for deployments under about 2--3 million posts and file entries. Beyond
that scale, enabling enterprise search with Elasticsearch or AWS
OpenSearch is highly recommended for optimum search performance before
reaching 3 million posts.

For self-hosted deployments with over 3 million posts, Elasticsearch or
AWS OpenSearch is required to avoid significant performance issues, such
as timeouts, with
`message searches </end-user-guide/collaborate/search-for-messages>`{.interpreted-text
role="doc"} and
`@mentions </end-user-guide/collaborate/mention-people>`{.interpreted-text
role="doc"}.

You can configure Mattermost enterprise search by going to **System
Console \> Environment \> Elasticsearch**. The following configuration
settings apply to both Elasticsearch and AWS OpenSearch. You can also
edit the `config.json` file as described in the following tables.
Changes to configuration settings in this section require a server
restart before taking effect.

### Enable Elasticsearch indexing

+-----------------------------+---------------------------------------------+
| Configure Mattermost to     | - System Config path: **Environment \>      |
| index new posts             |   Elasticsearch**                           |
| automatically.              | - `config.json` setting:                    |
|                             |   `ElasticsearchSettings` \>                |
| - **true**: Indexing of new |   `EnableIndexing` \> `false`               |
|   messages occurs           | - Environment variable:                     |
|   automatically.            |   `MM_ELASTICSEARCHSETTINGS_ENABLEINDEXING` |
| - **false**: **(Default)**  |                                             |
|   Indexing of new messages  |                                             |
|   is disabled, and new      |                                             |
|   messages aren\'t indexed. |                                             |
+-----------------------------+---------------------------------------------+

:::: note
::: title
Note
:::

If indexing is disabled and then re-enabled after an index is created,
purge and rebuild the index to ensure complete search results.
::::

### Backend type

Both
`Elasticsearch </administration-guide/scale/elasticsearch-setup>`{.interpreted-text
role="doc"} and
`AWS OpenSearch </administration-guide/scale/opensearch-setup>`{.interpreted-text
role="doc"} provide enterprise-scale deployments with optimized search
performance and prevents performance degradation and timeouts. Learn
more about
`enterprise search </administration-guide/scale/enterprise-search>`{.interpreted-text
role="doc"} in our product documentation.

+-------------------------+--------------------------------------------+
| The type of search      | - System Config path: **Environment \>     |
| backend.                |   Elasticsearch**                          |
|                         | - `config.json` setting:                   |
| - `elasticsearch` -     |   `ElasticsearchSettings` \> `Backend` \>  |
|   (**Default**)         |   `"elasticsearch"`                        |
| - `opensearch` -        | - Environment variable:                    |
|   Required for AWS      |   `MM_ELASTICSEARCHSETTINGS_BACKEND`       |
|   OpenSearch.           |                                            |
+-------------------------+--------------------------------------------+

Learn more about
`enterprise search version support <administration-guide/scale/enterprise-search:supported paths>`{.interpreted-text
role="ref"}.

### Server connection address

+----------------------------+--------------------------------------------+
| The address of the         | - System Config path: **Environment \>     |
| Elasticsearch or AWS       |   Elasticsearch**                          |
| OpenSearch server.         | - `config.json` setting:                   |
|                            |   `ElasticsearchSettings` \>               |
|                            |   `ConnectionUrl`                          |
|                            | - Environment variable:                    |
|                            |   `MM_ELASTICSEARCHSETTINGS_CONNECTIONURL` |
+----------------------------+--------------------------------------------+

### CA path

+----------------------------+-----------------------------------------+
| Optional path to the       | - System Config path: **Environment \>  |
| Custom Certificate         |   Elasticsearch**                       |
| Authority certificates for | - `config.json` setting:                |
| the Elasticsearch or AWS   |   `ElasticsearchSettings` \> `CA`       |
| OpenSearch server.         | - Environment variable:                 |
|                            |   `MM_ELASTICSEARCHSETTINGS_CA`         |
+----------------------------+-----------------------------------------+

:::: note
::: title
Note
:::

- Available from Mattermost v7.8. The certificate path should be
  `/opt/mattermost/data/elasticsearch/` or
  `/opt/mattermost/data/opensearch` and configured in the System Console
  as `./elasticsearch/cert.pem` or `./opensearch/cert.pem`.
- Can be used in conjunction with basic authentication credentials or
  can replace them. Leave this setting blank to use the default
  Certificate Authority certificates for the operating system.
::::

### Client certificate path

Available from Mattermost v7.8. Can be used in conjunction with basic
auth credentials or to replace them.

+----------------------------+-----------------------------------------+
| Optional client            | - System Config path: **Environment \>  |
| certificate for the        |   Elasticsearch**                       |
| connection to the          | - `config.json` setting:                |
| Elasticsearch or AWS       |   `ElasticsearchSettings` \>            |
| OpenSearch server in the   |   `ClientCert`                          |
| PEM format.                | - Environment variable:                 |
|                            |   `MM_ELASTICSEARCHSETTINGS_CLIENTCERT` |
+----------------------------+-----------------------------------------+

### Client certificate key path

Available from Mattermost v7.8. Can be used in conjunction with basic
auth credentials or to replace them.

+----------------------------+-----------------------------------------+
| Optional key for the       | - System Config path: **Environment \>  |
| client certificate in the  |   Elasticsearch**                       |
| PEM format.                | - `config.json` setting:                |
|                            |   `ElasticsearchSettings` \>            |
|                            |   `ClientKey`                           |
|                            | - Environment variable:                 |
|                            |   `MM_ELASTICSEARCHSETTINGS_CLIENTKEY`  |
+----------------------------+-----------------------------------------+

### Skip TLS verification

+----------------------------+--------------------------------------------------+
| The certificate step for   | - System Config path: **Environment \>           |
| TLS connections can be     |   Elasticsearch**                                |
| skipped.                   | - `config.json` setting: `ElasticsearchSettings` |
|                            |   \> `SkipTLSVerification` \> `false`            |
| - **true**: Skips the      | - Environment variable:                          |
|   certificate verification |   `MM_ELASTICSEARCHSETTINGS_SKIPTLSVERIFICATION` |
|   step for TLS             |                                                  |
|   connections.             |                                                  |
| - **false**: **(Default)** |                                                  |
|   Mattermost requires      |                                                  |
|   certificate              |                                                  |
|   verification.            |                                                  |
+----------------------------+--------------------------------------------------+

### Server username

+--------------------------------+---------------------------------------+
| (Optional) The username to     | - System Config path: **Environment   |
| authenticate to the            |   \> Elasticsearch**                  |
| Elasticsearch or AWS           | - `config.json` setting:              |
| OpenSearch server.             |   `ElasticsearchSettings` \>          |
|                                |   `UserName`                          |
| String input.                  | - Environment variable:               |
|                                |   `MM_ELASTICSEARCHSETTINGS_USERNAME` |
+--------------------------------+---------------------------------------+

### Server password

+--------------------------------+---------------------------------------+
| (Optional) The password to     | - System Config path: **Environment   |
| authenticate to the            |   \> Elasticsearch**                  |
| Elasticsearch or AWS           | - `config.json` setting:              |
| OpenSearch server.             |   `ElasticsearchSettings` \>          |
|                                |   `Password`                          |
| String input.                  | - Environment variable:               |
|                                |   `MM_ELASTICSEARCHSETTINGS_PASSWORD` |
+--------------------------------+---------------------------------------+

### Enable cluster sniffing

+------------------------------+---------------------------------------+
| Configure Mattermost to      | - System Config path: **Environment   |
| automatically find and       |   \> Elasticsearch**                  |
| connect to all data nodes in | - `config.json` setting:              |
| a cluster.                   |   `ElasticsearchSettings` \> `Sniff`  |
|                              |   \> `false`                          |
| - **true**: Sniffing finds   | - Environment variable:               |
|   and connects to all data   |   `MM_ELASTICSEARCHSETTINGS_SNIFF`    |
|   nodes in your cluster      |                                       |
|   automatically.             |                                       |
| - **false**: **(Default)**   |                                       |
|   Cluster sniffing is        |                                       |
|   disabled.                  |                                       |
+------------------------------+---------------------------------------+

Select the **Test Connection** button in the System Console to validate
the connection between Mattermost and the Elasticsearch or AWS
OpenSearch server.

### Bulk indexing

+--------------------------------+-------------------------------------+
| Configure Mattermost to start  | - System Config path: **Environment |
| a bulk index of all existing   |   \> Elasticsearch**                |
| posts in the database, from    | - `config.json` setting: N/A        |
| oldest to newest.              | - Environment variable: N/A         |
+--------------------------------+-------------------------------------+

:::: note
::: title
Note
:::

- Always [purge indexes](#purge-indexes) before bulk indexing.
- Select the **Index Now** button in the System Console to start a bulk
  index of all posts, and review all index jobs in progress.
- Elasticsearch or AWS OpenSearch is available during indexing, but
  search results may be incomplete until the indexing job is complete.
- If an in-progress indexing job is canceled, the index and search
  results will be incomplete.
::::

### Rebuild channels index

+-----------------------------------+-----------------------------------+
| Purge the channels index adn      | - System Config path:             |
| re-index all channels in the      |   **Environment \>                |
| database, from oldest to newest.  |   Elasticsearch**                 |
|                                   | - `config.json` setting: N/A      |
|                                   | - Environment variable: N/A       |
+-----------------------------------+-----------------------------------+

Select the **Rebuild Channels Index** button in the System Console to
purge the channels index. Ensure no other indexing jobs are in progress
via the **Bulk Indexing** table before starting this process. During
indexing, channel auto-complete is available, but search results may be
incomplete until the indexing job is complete.

### Purge indexes

+----------------------------+-----------------------------------------+
| Purge the entire           | - System Config path: **Environment \>  |
| Elasticsearch index.       |   Elasticsearch**                       |
|                            | - `config.json` setting: N/A            |
|                            | - Environment variable: N/A             |
+----------------------------+-----------------------------------------+

Select the **Purge Indexes** button in the System Console to purge the
index. After purging the index, create a new index by selecting the
**Index Now** button.

### Indexes to skip while purging

+------------------------------+--------------------------------------------------+
| Specify index names to       | - System Config path: **Environment \>           |
| ignore while purging         |   Elasticsearch**                                |
| indexes. Separate multiple   | - `config.json` setting: `ElasticsearchSettings` |
| index names with commas.     |   \> `IgnoredPurgeIndexes`                       |
|                              | - Environment variable:                          |
| Use an asterisk (\*) to      |   `MM_ELASTICSEARCHSETTINGS_IGNOREDPURGEINDEXES` |
| match a sequence of index    |                                                  |
| name characters.             |                                                  |
+------------------------------+--------------------------------------------------+

### Enable Elasticsearch for search queries

+-----------------------------+----------------------------------------------+
| Configure Mattermost to use | - System Config path: **Environment \>       |
| Elasticsearch or AWS        |   Elasticsearch**                            |
| OpenSearch for all search   | - `config.json` setting:                     |
| queries using the latest    |   `ElasticsearchSettings` \>                 |
| index.                      |   `EnableSearching` \> `false`               |
|                             | - Environment variable:                      |
| - **true**: Elasticsearch   |   `MM_ELASTICSEARCHSETTINGS_ENABLESEARCHING` |
|   or AWS OpenSearch is used |                                              |
|   for all search queries    |                                              |
|   using the latest index.   |                                              |
|   Search results may be     |                                              |
|   incomplete until a bulk   |                                              |
|   index of the existing     |                                              |
|   message database is       |                                              |
|   completed.                |                                              |
| - **false**: **(Default)**  |                                              |
|   Database search is used   |                                              |
|   for search queries.       |                                              |
+-----------------------------+----------------------------------------------+

If indexing is disabled and then re-enabled after an index is created,
purge and rebuild the index to ensure complete search results.

### Enable Elasticsearch for autocomplete queries

+----------------------------+-------------------------------------------------+
| Configure Mattermost to    | - System Config path: **Environment \>          |
| use Elasticsearch or AWS   |   Elasticsearch**                               |
| OpenSearch for all         | - `config.json` setting:                        |
| autocompletion queries on  |   `ElasticsearchSettings` \>                    |
| users and channels using   |   `EnableAutocomplete` \> `false`               |
| the latest index.          | - Environment variable:                         |
|                            |   `MM_ELASTICSEARCHSETTINGS_ENABLEAUTOCOMPLETE` |
| - **true**: Elasticsearch  |                                                 |
|   or AWS OpenSearch will   |                                                 |
|   be used for all          |                                                 |
|   autocompletion queries   |                                                 |
|   on users and channels    |                                                 |
|   using the latest index.  |                                                 |
| - **false**: **(Default)** |                                                 |
|   Database autocomplete is |                                                 |
|   used.                    |                                                 |
+----------------------------+-------------------------------------------------+

Autocompletion results may be incomplete until a bulk index of the
existing users and channels database is finished.

### Post index replicas

+-----------------------------+------------------------------------------------+
| The number of replicas to   | - System Config path: N/A                      |
| use for each post index.    | - `config.json` setting:                       |
|                             |   `ElasticsearchSettings` \>                   |
| Numerical input. Default is |   `PostIndexReplicas` \> `1`                   |
| **1**.                      | - Environment variable:                        |
|                             |   `MM_ELASTICSEARCHSETTINGS_POSTINDEXREPLICAS` |
+-----------------------------+------------------------------------------------+

:::: note
::: title
Note
:::

- If this setting is changed, the changed configuration only applies to
  newly-created indexes. To apply the change to existing indexes, purge
  and rebuild the index after changing this setting.
- If there are `n` data nodes, the number of replicas per shard for each
  index should be `n-1`.
- If the number of nodes in an Elasticsearch or AWS OpenSearch cluster
  changes, this configuration setting, as well as [Channel Index
  Replicas](#channel-index-replicas) and [User Index
  Replicas](#user-index-replicas) must also be updated accordingly.
::::

### Post index shards

+-----------------------------+----------------------------------------------+
| The number of shards to use | - System Config path: N/A                    |
| for each post index.        | - `config.json` setting:                     |
|                             |   `ElasticsearchSettings` \>                 |
| Numerical input. Default is |   `PostIndexShards` \> `1`                   |
| **1**.                      | - Environment variable:                      |
|                             |   `MM_ELASTICSEARCHSETTINGS_POSTINDEXSHARDS` |
+-----------------------------+----------------------------------------------+

:::: note
::: title
Note
:::

If this configuration setting is changed, the changed configuration only
applies to newly-created indexes. To apply the change to existing
indexes, purge and rebuild the index after changing this setting.
::::

### Channel index replicas

+----------------------------+---------------------------------------------------+
| The number of replicas to  | - System Config path: N/A                         |
| use for each channel       | - `config.json` setting: `ElasticsearchSettings`  |
| index.                     |   \> `ChannelIndexReplicas` \> `1`                |
|                            | - Environment variable:                           |
| Numerical input. Default   |   `MM_ELASTICSEARCHSETTINGS_CHANNELINDEXREPLICAS` |
| is **1**.                  |                                                   |
+----------------------------+---------------------------------------------------+

:::: note
::: title
Note
:::

If there are `n` data nodes, the number of replicas per shard for each
index should be `n-1`. If the number of nodes in an Elasticsearch or AWS
OpenSearch cluster changes, this configuration setting, as well as [Post
Index Replicas](#post-index-shards) and [User Index
Replicas](#user-index-replicas) must also be updated accordingly.
::::

### Channel index shards

+----------------------------+-------------------------------------------------+
| The number of shards to    | - System Config path: N/A                       |
| use for each channel       | - `config.json` setting:                        |
| index.                     |   `ElasticsearchSettings` \>                    |
|                            |   `ChannelIndexShards` \> `1`                   |
| Numerical input. Default   | - Environment variable:                         |
| is **1**.                  |   `MM_ELASTICSEARCHSETTINGS_CHANNELINDEXSHARDS` |
+----------------------------+-------------------------------------------------+

### User index replicas

+-----------------------------+------------------------------------------------+
| The number of replicas to   | - System Config path: N/A                      |
| use for each user index.    | - `config.json` setting:                       |
|                             |   `ElasticsearchSettings` \>                   |
| Numerical input. Default is |   `UserIndexReplicas` \> `1`                   |
| **1**.                      | - Environment variable:                        |
|                             |   `MM_ELASTICSEARCHSETTINGS_USERINDEXREPLICAS` |
+-----------------------------+------------------------------------------------+

:::: note
::: title
Note
:::

If there are `n` data nodes, the number of replicas per shard for each
index should be `n-1`. If the number of nodes in an Elasticsearch or AWS
OpenSearch cluster changes, this configuration setting, as well as [Post
Index Replicas](#post-index-shards) and [User Index
Replicas](#user-index-replicas) must also be updated accordingly.
::::

### User index shards

+-----------------------------+----------------------------------------------+
| The number of shards to use | - System Config path: N/A                    |
| for each user index.        | - `config.json` setting:                     |
|                             |   `ElasticsearchSettings` \>                 |
| Numerical input. Default is |   `UserIndexShards` \> `1`                   |
| **1**.                      | - Environment variable:                      |
|                             |   `MM_ELASTICSEARCHSETTINGS_USERINDEXSHARDS` |
+-----------------------------+----------------------------------------------+

### Aggregate search indexes

+---------------------------+------------------------------------------------------+
| Elasticsearch or AWS      | - System Config path: N/A                            |
| OpenSearch indexes older  | - `config.json` setting: `ElasticsearchSettings` \>  |
| than the age specified by |   `AggregatePostsAfterDays` \> `365`                 |
| this setting, in days,    | - Environment variable:                              |
| will be aggregated during |   `MM_ELASTICSEARCHSETTINGS_AGGREGATEPOSTSAFTERDAYS` |
| the daily scheduled job.  |                                                      |
|                           |                                                      |
| Numerical input. Default  |                                                      |
| is **365** days.          |                                                      |
+---------------------------+------------------------------------------------------+

:::: note
::: title
Note
:::

If you're using
`data retention </administration-guide/comply/data-retention-policy>`{.interpreted-text
role="doc"} and
`enterprise search </administration-guide/scale/enterprise-search>`{.interpreted-text
role="doc"}, configure this with a value greater than your data
retention policy.
::::

### Post aggregator start time

+--------------------------+----------------------------------------------------------+
| The start time of the    | - System Config path: N/A                                |
| daily scheduled          | - `config.json` setting: `ElasticsearchSettings` \>      |
| aggregator job.          |   `PostsAggregatorJobStartTime` \> `"03:00"`             |
|                          | - Environment variable:                                  |
| Must be a 24-hour time   |   `MM_ELASTICSEARCHSETTINGS_POSTSAGGREGATORJOBSTARTTIME` |
| stamp in the form        |                                                          |
| `HH:MM` based on the     |                                                          |
| local time of the        |                                                          |
| server.                  |                                                          |
|                          |                                                          |
| Default is **03:00** (3  |                                                          |
| AM)                      |                                                          |
+--------------------------+----------------------------------------------------------+

### Index prefix

+--------------------------------+------------------------------------------+
| The prefix added to the        | - System Config path: N/A                |
| Elasticsearch or AWS           | - `config.json` setting:                 |
| OpenSearch index name.         |   `ElasticsearchSettings` \>             |
|                                |   `IndexPrefix`                          |
|                                | - Environment variable:                  |
|                                |   `MM_ELASTICSEARCHSETTINGS_INDEXPREFIX` |
+--------------------------------+------------------------------------------+

:::: note
::: title
Note
:::

When this setting is used, all Elasticsearch or AWS OpenSearch indexes
created by Mattermost are given this prefix. You can set different
prefixes so that multiple Mattermost deployments can share an
Elasticsearch or AWS OpenSearch cluster without the index names
colliding.
::::

### Global search prefix

+-------------------------------+-------------------------------------------------+
| Enable global search across   | - System Config path: N/A                       |
| multiple Elasticsearch        | - `config.json` setting:                        |
| indices with the same [index  |   `ElasticsearchSettings` \>                    |
| prefix](#index-prefix).       |   `GlobalSearchPrefix`                          |
|                               | - Environment variable:                         |
| This is helpful for setups    |   `MM_ELASTICSEARCHSETTINGS_GLOBALSEARCHPREFIX` |
| with multiple data centers    |                                                 |
| where Elasticsearch instances |                                                 |
| share data using              |                                                 |
| cross-cluster replication. It |                                                 |
| allows for easier and unified |                                                 |
| searching across distributed  |                                                 |
| indices.                      |                                                 |
|                               |                                                 |
| Value must be a prefix of     |                                                 |
| `IndexPrefix`.                |                                                 |
+-------------------------------+-------------------------------------------------+

### Live indexing batch size

+----------------------------+----------------------------------------------------+
| The number of new posts    | - System Config path: N/A                          |
| needed before those posts  | - `config.json` setting: `ElasticsearchSettings`   |
| are added to the           |   \> `LiveIndexingBatchSize` \> `1`                |
| Elasticsearch or AWS       | - Environment variable:                            |
| OpenSearch index. Once     |   `MM_ELASTICSEARCHSETTINGS_LIVEINDEXINGBATCHSIZE` |
| added to the index, the    |                                                    |
| post becomes searchable.   |                                                    |
|                            |                                                    |
| On servers with more than  |                                                    |
| 1 post per second, we      |                                                    |
| suggest setting this value |                                                    |
| to the average number of   |                                                    |
| posts over a 20 second     |                                                    |
| period of time.            |                                                    |
|                            |                                                    |
| Numerical input. Default   |                                                    |
| is **1**. Every post is    |                                                    |
| indexed synchronously as   |                                                    |
| they are created.          |                                                    |
+----------------------------+----------------------------------------------------+

:::: note
::: title
Note
:::

It may be necessary to increase this value to avoid hitting the rate
limit or resource limit of your Elasticsearch or AWS OpenSearch cluster
on installs handling more than 1 post per second.
::::

**What exactly happens when I increase this value?**

The primary impact is that a post will be indexed into Elasticsearch or
AWS OpenSearch after the threshold of posts is met, which then makes the
posts searchable within Mattermost. So, if you set this based on
recommendations for larger servers, and you make a post, you cannot find
it via search for \~10--20 seconds, on average. Realistically, no users
should see or feel this impact due to the limited number of users who
are actively **searching** for a post this quickly. You can set this
value to a lower or higher average depending on your Elasticsearch or
AWS OpenSearch server specifications.

During busy periods, this delay will be faster as more traffic is
occurring, causing more posts and a quicker time to hit the index
number. During slower periods, expect the reverse.

**How to find the right number for your server**

1. You must understand how many posts your server makes every minute.
    Run the query below to calculate your server\'s average posts per
    minute.

    > Note that this query can be heavy, so we recommend that you run it
    > during non-peak hours. Additionally, you can adjust the `WHERE`
    > clause to see the posts per minute over a different time period.
    > Right now `31536000000` represents the number of milliseconds in a
    > year.
    >
    > ``` SQL
    > SELECT
    >   AVG(postsPerMinute) as averagePostsPerMinute
    > FROM (
    >   SELECT
    >     count(*) as postsPerMinute,
    >     date_trunc('minute', to_timestamp(createat/1000))
    >   FROM posts
    >   WHERE createAt > ( (extract(epoch from now()) * 1000 )  - 31536000000)
    >   GROUP BY date_trunc('minute', to_timestamp(createat/1000))
    > ) as ppm;
    > ```

2. Decide the acceptable index window for your environment, and divide
    your average posts per minute by that. We suggest 10-20 seconds.
    Assuming you have `600` posts per minute on average, and you want to
    index every 20 seconds (`60 seconds / 20 seconds = 3`[) you would
    calculate ]{.title-ref}[600 / 3]{.title-ref}[ to come to the number
    ]{.title-ref}[200]{.title-ref}\`. After 200 posts, Mattermost will
    index the posts into Elasticsearch or AWS OpenSearch. So, on
    average, there would be a 20-second delay in searchability.

3. Edit the `config.json` or run mmctl to modify the
    `LiveIndexingBatchSize` setting

    > **In the \`\`config.json\`\`**
    >
    > ``` JSON
    > {
    >   "ElasticsearchSettings": {
    >     "LiveIndexingBatchSize": 200
    >   }
    > }
    > ```
    >
    > **Via mmctl**
    >
    > ``` sh
    > mmctl config set ElasticsearchSettings.LiveIndexingBatchSize 200
    > ```
    >
    > **Via an environment variable**
    >
    > ``` sh
    > MM_ELASTICSEARCHSETTINGS_LIVEINDEXINGBATCHSIZE = 200
    > ```

4. Restart the Mattermost server.

### Batch size

+-----------------------+----------------------------------------------+
| The number of posts   | - System Config path: N/A                    |
| for a single batch    | - `config.json` setting:                     |
| during a bulk         |   `ElasticsearchSettings` \> `BatchSize` \>  |
| indexing job.         |   `10000`                                    |
|                       | - Environment variable:                      |
| Numerical input.      |   `MM_ELASTICSEARCHSETTINGS_BATCHSIZE`       |
| Default is **10000**. |                                              |
+-----------------------+----------------------------------------------+

### Request timeout

+----------------------------+----------------------------------------------------+
| The timeout, in seconds,   | - System Config path: N/A                          |
| for Elasticsearch or AWS   | - `config.json` setting: `ElasticsearchSettings`   |
| OpenSearch calls.          |   \> `RequestTimeoutSeconds` \> `30`               |
|                            | - Environment variable:                            |
| Numerical input in         |   `MM_ELASTICSEARCHSETTINGS_REQUESTTIMEOUTSECONDS` |
| seconds. Default is **30** |                                                    |
| seconds.                   |                                                    |
+----------------------------+----------------------------------------------------+

### Trace

+---------------------------------+------------------------------------+
| Options for printing            | - System Config path: N/A          |
| Elasticsearch or AWS OpenSearch | - `config.json` setting:           |
| trace errors.                   |   `ElasticsearchSettings` \>       |
|                                 |   `Trace`                          |
| - **error**: Creates the error  | - Environment variable:            |
|   trace when initializing the   |   `MM_ELASTICSEARCHSETTINGS_TRACE` |
|   Elasticsearch or AWS          |                                    |
|   OpenSearch client and prints  |                                    |
|   any template creation or      |                                    |
|   search query that returns an  |                                    |
|   error as part of the error    |                                    |
|   message.                      |                                    |
| - **all**: Creates the three    |                                    |
|   traces (error, trace and      |                                    |
|   info) for the driver and      |                                    |
|   doesn't print the queries     |                                    |
|   because they will be part of  |                                    |
|   the trace log level of the    |                                    |
|   driver.                       |                                    |
| - **not specified**:            |                                    |
|   **(Default)** No error trace  |                                    |
|   is created.                   |                                    |
+---------------------------------+------------------------------------+

------------------------------------------------------------------------

## File storage

With self-hosted deployments, you can configure file storage settings by
going to **System Console \> Environment \> File Storage**, or by
editing the `config.json` file as described in the following tables.

:::: note
::: title
Note
:::

Mattermost currently supports storing files on the local filesystem and
Amazon S3 or S3-compatible containers. We have tested Mattermost with
[Digital Ocean Spaces](https://docs.digitalocean.com/products/spaces/),
but not all S3-compatible containers on the market. If you are looking
to use other S3-compatible containers, we recommend completing your own
testing. You can also use local storage or a network drive using NFS.
::::

### File storage system

+-------------------------------+--------------------------------------+
| The type of file storage      | - System Config path: **Environment  |
| system used. Can be either    |   \> File Storage**                  |
| Local File System or Amazon   | - `config.json` setting:             |
| S3.                           |   `FileSettings` \> `DriverName` \>  |
|                               |   `"local"`                          |
| - **local**: **(Default)**    | - Environment variable:              |
|   Files and images are stored |   `MM_FILESETTINGS_DRIVERNAME`       |
|   in the specified local file |                                      |
|   directory.                  |                                      |
| - **amazons3**: Files and     |                                      |
|   images are stored on Amazon |                                      |
|   S3 based on the access key, |                                      |
|   bucket, and region fields   |                                      |
|   provided. The driver is     |                                      |
|   compatible with other       |                                      |
|   S3-compatible services,     |                                      |
|   such as Digital Ocean       |                                      |
|   Spaces.                     |                                      |
+-------------------------------+--------------------------------------+

### Local storage directory

+--------------------------------+-------------------------------------+
| The local directory to which   | - System Config path: **Environment |
| files are written when the     |   \> File Storage**                 |
| **File storage system** is set | - `config.json` setting:            |
| to **local**. Can be any       |   `FileSettings` \> `Directory`     |
| directory writable by the user | - Environment variable:             |
| Mattermost is running as, and  |   `MM_FILESETTINGS_DIRECTORY`       |
| is relative to the directory   |                                     |
| where Mattermost is installed. |                                     |
|                                |                                     |
| Defaults to **./data/**.       |                                     |
+--------------------------------+-------------------------------------+

When **File storage system** is set to **amazons3**, this setting has no
effect.

### Maximum file size

+-------------------------------+--------------------------------------+
| The maximum file size for     | - System Config path: **Environment  |
| message attachments and       |   \> File Storage**                  |
| plugin uploads. This value    | - `config.json` setting:             |
| must be specified in          |   `FileSettings` \> `MaxFileSize` \> |
| mebibytes in the System       |   `104857600`                        |
| Console, and in bytes in the  | - Environment variable:              |
| `config.json` file.           |   `MM_FILESETTINGS_MAXFILESIZE`      |
|                               |                                      |
| The default is `104857600`    |                                      |
| bytes (**100** mebibytes).    |                                      |
+-------------------------------+--------------------------------------+

:::: note
::: title
Note
:::

- Verify server memory can support your setting choice. Large file sizes
  increase the risk of server crashes and failed uploads due to network
  disruptions.
- When
  `uploading plugin files <administration-guide/configure/plugins-configuration-settings:upload plugin>`{.interpreted-text
  role="ref"}, a `Received invalid response from the server` error
  typically indicates that `MaxFileSize` isn\'t large enough to support
  the plugin file upload, and/or that proxy settings may not be
  sufficient.
- If you use a proxy or load balancer in front of Mattermost, the
  following proxy settings must be adjusted accordingly:
  - For NGINX, use `client_max_body_size`.
  - For Apache, use `LimitRequestBody`.
::::

### Enable document search by content

+-----------------------------+----------------------------------------+
| Enable users to search the  | - System Config path: **Environment \> |
| contents of documents       |   File Storage**                       |
| attached to messages.       | - `config.json` setting:               |
|                             |   `FileSettings` \> `ExtractContent`   |
| - **true**: **(Default)**   |   \> `true`                            |
|   Documents are searchable  | - Environment variable:                |
|   by their content.         |   `MM_FILESETTINGS_EXTRACTCONTENT`     |
| - **false**: Documents      |                                        |
|   aren't searchable by      |                                        |
|   their content. When       |                                        |
|   document content search   |                                        |
|   is disabled, users can    |                                        |
|   search for files by file  |                                        |
|   name only.                |                                        |
+-----------------------------+----------------------------------------+

:::: note
::: title
Note
:::

Enabling document search by content is required when extracting content
from files. Both Mattermost
`file search </end-user-guide/collaborate/search-for-messages>`{.interpreted-text
role="doc"} and
`Mattermost Agents </end-user-guide/agents>`{.interpreted-text
role="doc"} can access files and their content, when enabled with the
necessary dependencies. Document content search results for files shared
before upgrading to Mattermost Server v5.35 may be incomplete until an
extraction command is executed using the
`mmctl <administration-guide/manage/mmctl-command-line-tool:mmctl extract>`{.interpreted-text
role="ref"}. If this command is not run, users can search older files
based on file name only.

You can optionally install the following
[dependencies](https://github.com/sajari/docconv#dependencies) to extend
content searching support in Mattermost to include file formats beyond
PDF, DOCX, and ODT, such as DOC, RTF, XML, and HTML:

- **tidy**: Used to search the contents of HTML documents.
- **wv**: Used to search the contents of DOC documents.
- **poppler-utils**: Used to significantly improve server performance
  when extracting the contents of PDF documents.
- **unrtf**: Used to search the contents of RTF documents.
- **JusText**: Used to search HTML documents. See the [JusText Python
  package](https://pypi.org/project/jusText/) for deployment
  information.

If you choose not to install these dependencies, you'll see log entries
for documents that couldn't be extracted. Any documents that can't be
extracted are skipped and logged so that content extraction can proceed.
::::

### Enable searching content of documents within ZIP files

+-----------------------------+----------------------------------------+
| Enables users to search the | - System Config path: **Environment \> |
| contents of compressed ZIP  |   File Storage**                       |
| files attached to messages. | - `config.json` setting:               |
|                             |   `FileSettings` \> `ArchiveRecursion` |
| - **true**: Contents of     |   \> `false`                           |
|   documents within ZIP      | - Environment variable:                |
|   files are returned in     |   `MM_FILESETTINGS_ARCHIVERECURSION`   |
|   search results. This may  |                                        |
|   have an impact on server  |                                        |
|   performance for large     |                                        |
|   files. the specified      |                                        |
|   local file directory.     |                                        |
| - **false**: **(Default)**  |                                        |
|   The contents of documents |                                        |
|   within ZIP files aren't   |                                        |
|   returned in search        |                                        |
|   results.                  |                                        |
+-----------------------------+----------------------------------------+

:::: note
::: title
Note
:::

- You can search for document content within ZIP files when using
  Mattermost in a web browser or the desktop app.
- Searching document contents adds load to your server.
- For large deployments, or teams that share many large, text-heavy
  documents, we recommend you review our
  `hardware requirements <deployment-guide/software-hardware-requirements:hardware requirements>`{.interpreted-text
  role="ref"}, and test enabling this feature in a staging environment
  before enabling it in a production environment.
::::

### Amazon S3 bucket

+--------------------------------+-------------------------------------+
| The name of the bucket for     | - System Config path: **Environment |
| your S3-compatible object      |   \> File Storage**                 |
| storage instance.              | - `config.json` setting:            |
|                                |   `FileSettings` \>                 |
| A string with the              |   `AmazonS3Bucket`                  |
| S3-compatible bucket name.     | - Environment variable:             |
|                                |   `MM_FILESETTINGS_AMAZONS3BUCKET`  |
+--------------------------------+-------------------------------------+

### Amazon S3 path prefix

+--------------------------------+----------------------------------------+
| The prefix you selected for    | - System Config path: N/A              |
| your **Amazon S3 bucket** in   | - `config.json` setting:               |
| AWS.                           |   `FileSettings` \>                    |
|                                |   `AmazonS3PathPrefix`                 |
| A string containing the path   | - Environment variable:                |
| prefix.                        |   `MM_FILESETTINGS_AMAZONS3PATHPREFIX` |
+--------------------------------+----------------------------------------+

### Amazon S3 region

+--------------------------------+------------------------------------------+
| The AWS region you selected    | - System Config path: **Environment \>   |
| when creating your **Amazon S3 |   File Storage**                         |
| bucket** in AWS.               | - `config.json` setting:                 |
|                                |   `` `".FileSettings.AmazonS3Region", `` |
| A string with the AWS region   | - Environment variable:                  |
| containing the bucket. If no   |   `MM_FILESETTINGS_AMAZONS3REGION`       |
| region is set, Mattermost      |                                          |
| attempts to get the            |                                          |
| appropriate region from AWS,   |                                          |
| and sets it to **us-east-1**   |                                          |
| if none found.                 |                                          |
+--------------------------------+------------------------------------------+

For Digital Ocean Spaces or other S3-compatible services, leave this
setting empty.

### Amazon S3 access key ID

+--------------------------------+-----------------------------------------+
| A string with the access key   | - System Config path: **Environment \>  |
| for the S3-compatible storage  |   File Storage**                        |
| instance. Your EC2             | - `config.json` setting: `FileSettings` |
| administrator can supply you   |   \> `AmazonS3AccessKeyId`              |
| with the Access Key ID.        | - Environment variable:                 |
|                                |   `MM_FILESETTINGS_AMAZONS3ACCESSKEYID` |
+--------------------------------+-----------------------------------------+

:::: note
::: title
Note
:::

This is required for access unless you are using an [Amazon S3 IAM
Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html)
with Amazon S3.
::::

### Amazon S3 endpoint

+----------------------------+-----------------------------------------+
| The hostname of your       | - System Config path: **Environment \>  |
| S3-compatible instance.    |   File Storage**                        |
|                            | - `config.json` setting: `FileSettings` |
| A string with the hostname |   \> `AmazonS3Endpoint` \>              |
| of the S3-compatible       |   `"s3.amazonaws.com"`                  |
| storage instance. Defaults | - Environment variable:                 |
| to **s3.amazonaws.com**.   |   `MM_FILESETTINGS_AMAZONS3ENDPOINT`    |
+----------------------------+-----------------------------------------+

:::: note
::: title
Note
:::

For Digital Ocean Spaces, the hostname should be set to
**\<region\>.digitaloceanspaces.com**, where **\<region\>** is the
abbreviation for the region you selected when setting up the Space. It
can be **nyc3**, **ams3**, or **sgp1**.
::::

### Amazon S3 secret access key

+-------------------------------+---------------------------------------------+
| The secret access key         | - System Config path: **Environment \> File |
| associated with your Amazon   |   Storage**                                 |
| S3 Access Key ID.             | - `config.json` setting: `FileSettings` \>  |
|                               |   `AmazonS3SecretAccessKey`                 |
| A string with the secret      | - Environment variable:                     |
| access key for the            |   `MM_FILESETTINGS_AMAZONS3SECRETACCESSKEY` |
| S3-compatible storage         |                                             |
| instance.                     |                                             |
+-------------------------------+---------------------------------------------+

### Enable secure Amazon S3 connections

+--------------------------------+-------------------------------------+
| Enable or disable secure       | - System Config path: **Environment |
| Amazon S3 connections.         |   \> File Storage**                 |
|                                | - `config.json` setting:            |
| - **true**: **(Default)**      |   `FileSettings` \> `AmazonS3SSL`   |
|   Enables only secure Amazon   |   \> `true`                         |
|   S3 connections.              | - Environment variable:             |
| - **false**: Allows insecure   |   `MM_FILESETTINGS_AMAZONS3SSL`     |
|   connections to Amazon S3.    |                                     |
+--------------------------------+-------------------------------------+

### Amazon S3 signature v2

+-------------------------------+--------------------------------------+
| By default, Mattermost uses   | - System Config path: N/A            |
| Signature v4 to sign API      | - `config.json` setting:             |
| calls to AWS, but under some  |   `FileSettings` \> `AmazonS3SignV2` |
| circumstances, v2 is          |   \> `false`                         |
| required.                     | - Environment variable:              |
|                               |   `MM_FILESETTINGS_AMAZONS3SIGNV2`   |
| - **true**: Use Signature v2  |                                      |
|   signing process.            |                                      |
| - **false**: **(Default)**    |                                      |
|   Use Signature v4 signing    |                                      |
|   process.                    |                                      |
+-------------------------------+--------------------------------------+

See the
[AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html)
documentation for information about when to use the Signature v2 signing
process.

### Enable server-side encryption for Amazon S3

+-------------------------------+--------------------------------------+
| Enable server-side encryption | - System Config path: **Environment  |
| for Amazon S3.                |   \> File Storage**                  |
|                               | - `config.json` setting:             |
| - **true**: Encrypts files in |   `FileSettings` \> `AmazonS3SSE` \> |
|   Amazon S3 using server-side |   `false`                            |
|   encryption with Amazon      | - Environment variable:              |
|   S3-managed keys.            |   `MM_FILESETTINGS_AMAZONS3SSE`      |
| - **false**: **(Default)**    |                                      |
|   Doesn't encrypt files in    |                                      |
|   Amazon S3.                  |                                      |
+-------------------------------+--------------------------------------+

:::: note
::: title
Note
:::

This configuration setting is available for self-hosted deployments
only.
::::

### Enable Amazon S3 debugging

+-------------------------------+--------------------------------------+
| Enable or disable Amazon S3   | - System Config path: **Environment  |
| debugging to capture          |   \> File Storage**                  |
| additional debugging          | - `config.json` setting:             |
| information in system logs.   |   `FileSettings` \> `AmazonS3Trace`  |
|                               |   \> `false`                         |
| - **true**: Log additional    | - Environment variable:              |
|   debugging information is    |   `MM_FILESETTINGS_AMAZONS3TRACE`    |
|   logged to the system logs.  |                                      |
| - **false**: **(Default)** No |                                      |
|   Amazon S3 debugging         |                                      |
|   information is included in  |                                      |
|   the system logs. Typically  |                                      |
|   set to **false** in         |                                      |
|   production.                 |                                      |
+-------------------------------+--------------------------------------+

Select the **Test Connection** button in the System Console to validate
the settings and ensure the user can access the server.

### Amazon S3 storage class

Some Amazon S3-compatible storage solutions require the storage class
parameter to be present in upload requests, otherwise they will be
rejected. Configure this storage class as the storage class required by
your S3-compatible solution.

+-----------------------------+------------------------------------------+
| The storage class to use    | - System Config path: **Environment \>   |
| for uploads to              |   File Storage**                         |
| S3-compatible storage       | - `config.json` setting: `FileSettings`  |
| solutions.                  |   \> `AmazonS3StorageClass` \> `""`,     |
|                             | - Environment variable:                  |
| String input. Default is an |   `MM_FILESETTINGS_AMAZONS3STORAGECLASS` |
| empty string `""`. Select   |                                          |
| **Test Connection** to test |                                          |
| the configured connection.  |                                          |
+-----------------------------+------------------------------------------+

:::: note
::: title
Note
:::

Most Amazon S3-compatible storage solutions assign a default storage
class of `STANDARD` when no storage class is provided. See the [Amazon
S3 storage
class](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html#AmazonS3-PutObject-request-header-StorageClass)
documentation for details about supported storage classes.
::::

### Export Amazon S3 storage class

+-----------------------------+------------------------------------------------+
| The storage class to use    | - System Config path: N/A                      |
| for exports to              | - `config.json` setting: `FileSettings` \>     |
| S3-compatible storage       |   `ExportAmazonS3StorageClass` \> `""`         |
| solutions.                  | - Environment variable:                        |
|                             |   `MM_FILESETTINGS_EXPORTAMAZONS3STORAGECLASS` |
| String input. Default is an |                                                |
| empty string `""`.          |                                                |
+-----------------------------+------------------------------------------------+

:::: note
::: title
Note
:::

Most Amazon S3-compatible storage solutions assign a default storage
class of `STANDARD` when no storage class is provided. See the [Amazon
S3 storage
class](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html#AmazonS3-PutObject-request-header-StorageClass)
documentation for details about supported storage classes.
::::

### Amazon S3 request timeout

+---------------------------+--------------------------------------------------------+
| The amount of time, in    | - System Config path: N/A                              |
| milliseconds, before      | - `config.json` setting: `FileSettings` \>             |
| requests to Amazon S3     |   `AmazonS3RequestTimeoutMilliseconds` \> `30000`      |
| storage time out.         | - Environment variable:                                |
|                           |   `MM_FILESETTINGS_AMAZONS3REQUESTTIMEOUTMILLISECONDS` |
| Default is 30000 (30      |                                                        |
| seconds).                 |                                                        |
+---------------------------+--------------------------------------------------------+

### Amazon S3 upload part size

+---------------------------+-------------------------------------------------+
| The size, in bytes, of    | - System Config path: N/A                       |
| each part in a multi-part | - `config.json` setting: `FileSettings` \>      |
| upload to Amazon S3.      |   `AmazonS3UploadPartSizeBytes` \> `5242880`    |
|                           | - Environment variable:                         |
| Numeric value. Default is |   `MM_FILESETTINGS_AMAZONS3UPLOADPARTSIZEBYTES` |
| 5242880 (5MB).            |                                                 |
+---------------------------+-------------------------------------------------+

:::: note
::: title
Note
:::

A smaller part size can result in more requests and an increase in
latency, while a larger part size can result in more memory being
allocated.
::::

### Amazon S3 exported upload part size

+--------------------------+-------------------------------------------------------+
| The size, in bytes, of   | - System Config path: N/A                             |
| each part in a           | - `config.json` setting: `FileSettings` \>            |
| multi-part exported to   |   `ExportAmazonS3UploadPartSizeBytes` \> `104857600`  |
| Amazon S3.               | - Environment variable:                               |
|                          |   `MM_FILESETTINGS_EXPORTAMAZONS3UPLOADPARTSIZEBYTES` |
| Numeric value. Default   |                                                       |
| is 104857600 (100MB).    |                                                       |
+--------------------------+-------------------------------------------------------+

:::: note
::: title
Note
:::

A smaller part size can result in more requests and an increase in
latency, while a larger part size can result in more memory being
allocated.
::::

### Amazon S3 request timeout

+---------------------------+--------------------------------------------------------+
| The amount of time, in    | - System Config path: N/A                              |
| milliseconds, before      | - `config.json` setting: `FileSettings` \>             |
| requests to Amazon S3     |   `AmazonS3RequestTimeoutMilliseconds` \> `30000`      |
| storage time out.         | - Environment variable:                                |
|                           |   `MM_FILESETTINGS_AMAZONS3REQUESTTIMEOUTMILLISECONDS` |
| Default is 30000 (30      |                                                        |
| seconds).                 |                                                        |
+---------------------------+--------------------------------------------------------+

### Initial font

+----------------------------+-----------------------------------------+
| The font used in           | - System Config path: N/A               |
| auto-generated profile     | - `config.json` setting: `FileSettings` |
| pictures with colored      |   \> `InitialFont` \>                   |
| backgrounds and username   |   `"nunito-bold.ttf"`                   |
| initials.                  | - Environment variable:                 |
|                            |   `MM_FILESETTINGS_INITIALFONT`         |
| A string with the font     |                                         |
| file name. Default is      |                                         |
| **nunito-bold.ttf**.       |                                         |
+----------------------------+-----------------------------------------+

------------------------------------------------------------------------

## Image proxy

With self-hosted deployments, an image proxy can be used by Mattermost
apps to prevent them from connecting directly to remote self-hosted
servers. Configure an image proxy by going to **System Console \>
Environment \> Image Proxy**, or by editing the `config.json` file as
described in the following tables.

### Enable image proxy

+-------------------------------+--------------------------------------+
| An image proxy anonymizes     | - System Config path: **Environment  |
| Mattermost app connections    |   \> Image Proxy**                   |
| and prevents them from        | - `config.json` setting:             |
| accessing insecure content.   |   `ImageProxySettings` \> `Enable`   |
|                               |   \> `true`                          |
| - **true**: Enables an image  | - Environment variable:              |
|   proxy for loading external  |   `MM_IMAGEPROXYSETTINGS_ENABLE`     |
|   images.                     |                                      |
| - **false**: **(Default)**    |                                      |
|   Disables the image proxy.   |                                      |
+-------------------------------+--------------------------------------+

See the
`image proxy </deployment-guide/server/image-proxy>`{.interpreted-text
role="doc"} documentation to learn more.

### Image proxy type

+-----------------------------+------------------------------------------+
| The type of image proxy     | - System Config path: **Environment \>   |
| used by Mattermost.         |   Image Proxy**                          |
|                             | - `config.json` setting:                 |
| - **local**: **(Default)**  |   `ImageProxySettings` \>                |
|   The Mattermost server     |   `ImageProxyType` \> `"local"`          |
|   itself acts as the image  | - Environment variable:                  |
|   proxy.                    |   `MM_IMAGEPROXYSETTINGS_IMAGEPROXYTYPE` |
| - **atmos/camo**: An        |                                          |
|   external atmos/camo image |                                          |
|   proxy is used.            |                                          |
+-----------------------------+------------------------------------------+

See the
`image proxy </deployment-guide/server/image-proxy>`{.interpreted-text
role="doc"} documentation to learn more.

### Remote image proxy URL

+-------------------------------+-----------------------------------------------+
| The URL of the atmos/camo     | - System Config path: **Environment \> Image  |
| proxy. This setting isn\'t    |   Proxy**                                     |
| needed when using the         | - `config.json` setting: `ImageProxySettings` |
| **local** image proxy.        |   \> `RemoteImageProxyURL`                    |
|                               | - Environment variable:                       |
|                               |   `MM_IMAGEPROXYSETTINGS_REMOTEIMAGEPROXYURL` |
+-------------------------------+-----------------------------------------------+

### Remote image proxy options

+------------------------------+---------------------------------------------------+
| The URL signing key passed   | - System Config path: **Environment \> Image      |
| to an atmos/camo image       |   Proxy**                                         |
| proxy. This setting isn\'t   | - `config.json` setting: `ImageProxySettings` \>  |
| needed when using the        |   `RemoteImageProxyOptions`                       |
| **local** image proxy type.  | - Environment variable:                           |
|                              |   `MM_IMAGEPROXYSETTINGS_REMOTEIMAGEPROXYOPTIONS` |
+------------------------------+---------------------------------------------------+

See the
`image proxy </deployment-guide/server/image-proxy>`{.interpreted-text
role="doc"} documentation to learn more.

------------------------------------------------------------------------

## SMTP

With self-hosted deployments, you can configure SMTP email server
settings by going to **System Console \> Environment \> SMTP**, or by
editing the `config.json` file as described in the following tables.

### SMTP server

+-----------------------------------+-----------------------------------+
| The location of the SMTP email    | - System Config path:             |
| server used for email             |   **Environment \> SMTP**         |
| notifications.                    | - `config.json` setting:          |
|                                   |   `EmailSettings` \> `SMTPServer` |
|                                   | - Environment variable:           |
|                                   |   `MM_EMAILSETTINGS_SMTPSERVER`   |
+-----------------------------------+-----------------------------------+

### SMTP server port

+-----------------------------------+-----------------------------------+
| The port of SMTP email server.    | - System Config path:             |
|                                   |   **Environment \> SMTP**         |
| String input.                     | - `config.json` setting:          |
|                                   |   `EmailSettings` \> `"SMTPPort"` |
|                                   | - Environment variable:           |
|                                   |   `MM_EMAILSETTINGS_SMTPPORT`     |
+-----------------------------------+-----------------------------------+

### Enable SMTP authentication

+-------------------------------+--------------------------------------+
| Enable or disable SMTP        | - System Config path: **Environment  |
| authentication.               |   \> SMTP**                          |
|                               | - `config.json` setting:             |
| - **true**: SMTP username and |   `EmailSettings` \>                 |
|   password are used for       |   `EnableSMTPAuth` \> `false`        |
|   authenticating to the SMTP  | - Environment variable:              |
|   server.                     |   `MM_EMAILSETTINGS_ENABLESMTPAUTH`  |
| - **false**: **(Default)**    |                                      |
|   Mattermost doesn't attempt  |                                      |
|   to authenticate to the SMTP |                                      |
|   server.                     |                                      |
+-------------------------------+--------------------------------------+

### SMTP server username

+-----------------------------------+-----------------------------------+
| The username for authenticating   | - System Config path:             |
| to the SMTP server.               |   **Environment \> SMTP**         |
|                                   | - `config.json` setting:          |
| String input.                     |   `EmailSettings` \>              |
|                                   |   `SMTPUsername`                  |
|                                   | - Environment variable:           |
|                                   |   `MM_EMAILSETTINGS_SMTPUSERNAME` |
+-----------------------------------+-----------------------------------+

### SMTP server password

+-----------------------------------+-----------------------------------+
| The password associated with the  | - System Config path:             |
| SMTP username.                    |   **Environment \> SMTP**         |
|                                   | - `config.json` setting:          |
| String input.                     |   `EmailSettings` \>              |
|                                   |   `SMTPPassword`                  |
|                                   | - Environment variable:           |
|                                   |   `MM_EMAILSETTINGS_SMTPPASSWORD` |
+-----------------------------------+-----------------------------------+

### SMTP connection security

+---------------------------------+-----------------------------------------+
| Specify connection security for | - System Config path: **Environment \>  |
| emails sent using SMTP.         |   SMTP**                                |
|                                 | - `config.json` setting:                |
| - **Not specified**:            |   `EmailSettings` \>                    |
|   **(Default)** Send email over |   `ConnectionSecurity`                  |
|   an unsecure connection.       | - Environment variable:                 |
| - **TLS**: Communication        |   `MM_EMAILSETTINGS_CONNECTIONSECURITY` |
|   between Mattermost and your   |                                         |
|   email server is encrypted.    |                                         |
| - **STARTTLS**: Attempts to     |                                         |
|   upgrade an existing insecure  |                                         |
|   connection to a secure        |                                         |
|   connection using TLS.         |                                         |
+---------------------------------+-----------------------------------------+

### Skip server certificate verification

+----------------------------+--------------------------------------------------------+
| Configure Mattermost to    | - System Config path: **Environment \> SMTP**          |
| skip the verification of   | - `config.json` setting: `EmailSettings` \>            |
| the email server           |   `SkipServerCertificateVerification` \> `false`       |
| certificate.               | - Environment variable:                                |
|                            |   `MM_EMAILSETTINGS_SKIPSERVERCERTIFICATEVERIFICATION` |
| - **true**: Mattermost     |                                                        |
|   won\'t verify the email  |                                                        |
|   server certificate.      |                                                        |
| - **false**: **(Default)** |                                                        |
|   Mattermost verifies the  |                                                        |
|   email server             |                                                        |
|   certificate.             |                                                        |
+----------------------------+--------------------------------------------------------+

### Enable security alerts

+-----------------------------+-----------------------------------------------+
| Enable or disable security  | - System Config path: **Environment \> SMTP** |
| alerts.                     | - `config.json` setting: `ServiceSettings` \> |
|                             |   `EnableSecurityFixAlert` \> `true`          |
| - **true**: **(Default)**   | - Environment variable:                       |
|   System admins are         |   `MM_SERVICESETTINGS_ENABLESECURITYFIXALERT` |
|   notified by email if a    |                                               |
|   relevant security fix     |                                               |
|   alert is announced.       |                                               |
|   Requires email to be      |                                               |
|   enabled.                  |                                               |
| - **false**: Security       |                                               |
|   alerts are disabled.      |                                               |
+-----------------------------+-----------------------------------------------+

See the
`Telemetry <administration-guide/manage/telemetry:security update check feature>`{.interpreted-text
role="ref"} documentation to learn more.

### SMTP server timeout

+---------------------------------+----------------------------------------+
| The maximum amount of time, in  | - System Config path: **Environment \> |
| seconds, allowed for            |   SMTP**                               |
| establishing a TCP connection   | - `config.json` setting:               |
| between Mattermost and the SMTP |   `EmailSettings` \>                   |
| server.                         |   `SMTPServerTimeout`                  |
|                                 | - Environment variable:                |
| Numerical value in seconds.     |   `MM_EMAILSETTINGS_SMTPSERVERTIMEOUT` |
+---------------------------------+----------------------------------------+

------------------------------------------------------------------------

## Push notification server

With self-hosted deployments, you can configure mobile push
notifications for Mattermost by going to **System Console \> Environment
\> Push Notification Server**, or by editing the `config.json` file as
described in the following tables. Changes to configuration settings in
this section require a server restart before taking effect.

### Enable push notifications

+-------------------------------+--------------------------------------------+
| Enable or disable Mattermost  | - System Config path: **Environment \>     |
| push notifications.           |   Push Notification Server**               |
|                               | - `config.json` setting: `EmailSettings`   |
| - **Do not send push          |   \> `SendPushNotifications`               |
|   notifications**: Mobile     | - Environment variable:                    |
|   push notifications are      |   `MM_EMAILSETTINGS_SENDPUSHNOTIFICATIONS` |
|   disabled.                   |                                            |
| - **Use HPNS connection with  |                                            |
|   uptime SLA to send          |                                            |
|   notifications to iOS and    |                                            |
|   Android apps**:             |                                            |
|   **(Default)** Use           |                                            |
|   Mattermost\'s hosted push   |                                            |
|   notification service.       |                                            |
| - **Use TPNS connection to    |                                            |
|   send notifications to iOS   |                                            |
|   and Android apps**: Use     |                                            |
|   Mattermost\'s test push     |                                            |
|   notification service.       |                                            |
| - **Manually enter Push       |                                            |
|   Notification Service        |                                            |
|   location**: When building   |                                            |
|   your own custom mobile      |                                            |
|   apps, you must host your    |                                            |
|   own mobile push proxy       |                                            |
|   service, and specify that   |                                            |
|   URL in the **Push           |                                            |
|   Notification Server**       |                                            |
|   field.                      |                                            |
+-------------------------------+--------------------------------------------+

#### Hosted Push Notifications Service (HPNS)

Mattermost Enterprise, Professional, and Cloud customers can use
Mattermost\'s Hosted Push Notification Service (HPNS). The HPNS offers:

- Access to a publicly-hosted Mattermost Push Notification Service
  (MPNS) [available on
  GitHub.](https://github.com/mattermost/mattermost-push-proxy)
- An explicit [privacy
  policy](https://mattermost.com/data-processing-addendum/) for the
  contents of unencrypted messages.
- Encrypted TLS connections:
  - Between HPNS and Apple Push Notification Services
  - Between HPNS and Google's Firebase Cloud Messaging Service
  - HPNS and your Mattermost Server
- Production-level uptime expectations.
- Out-of-box configuration for new servers means nothing is required to
  enable HPNS for new deployments. HPNS can be [enabled for existing
  deployments](#enable-hpns-for-existing-deployments).

:::: note
::: title
Note
:::

\- The HPNS only works with pre-built apps Mattermost deploys through
the [Apple App Store](https://www.apple.com/app-store/) and [Google Play
Store](https://play.google.com/store/games?hl=en). If you build your own
mobile apps, you must also [host your own Mattermost push proxy
server](#host-your-own-push-proxy-service). - You must ensure that the
push proxy can be reached on the correct port. For HPNS, it\'s port 443
from the Mattermost server. - Mattermost doesn\'t store any notification
data. Any data being stored is at the server level only, such as the
`device_id`, since the HPNS needs to know which device the notification
must be sent to.
::::

#### Test Push Notifications Service (TPNS)

Non-commercial self-hosted customers can use Mattermost\'s free, basic
Test Push Notifications Service (TPNS).

:::: note
::: title
Note
:::

\- The TPNS isn't recommended for use in production environments, and
doesn't offer production-level update service level agreements (SLAs). -
The TPNS isn\'t available for Mattermost Cloud deployments. - The TPNS
only works with the pre-built mobile apps that Mattermost deploys
through the [Apple App Store](https://www.apple.com/app-store/) and
[Google Play Store](https://play.google.com/store/games?hl=en). If you
have built your own mobile apps, you must also [host your own Mattermost
push proxy service](#host-your-own-push-proxy-service). - You must
ensure that the push proxy can be reached on the correct port. For TPNS,
it\'s port 80 from the Mattermost server. - If you don\'t need or want
Mattermost to send mobile push notifications, disabling this
configuration setting in larger deployments may improve server
performance in the following areas:

- Reduced Processing Load: Generating and sending push notifications
  requires processing power and resources. By disabling them, the server
  can allocate those resources to other tasks.
- Decreased Network Traffic: Push notifications involve network
  communication. Disabling them reduces the amount of data being
  transferred, which can enhance overall network performance.
- Lower Database Load: Each push notification may involve reading from
  and writing to the database. Reducing these operations decreases the
  load on the database, improving response times for other queries.
- Faster Response Times: With fewer tasks to handle related to
  notifications, the system can respond faster to other requests from
  users, leading to a better user experience.
- Simplified Error Handling: Push notification services can sometimes
  fail or have latency issues, requiring additional error handling.
  Disabling these notifications simplifies the system\'s operations.
- However, disabling push notifications can negatively impact user
  experience, communication efficiency, and overall productivity. It's
  important to balance performance improvements with the needs of your
  organization and users.
::::

#### ID-only push notifications

Admins can enable mobile notifications to be fully private to protect a
Mattermost customer against breaches in iOS and Android notification
infrastructure by limiting the data sent to Apple and Google through a
Mattermost configuration setting.

The standard way to send notifications to iOS and Android applications
requires sending clear text messages to Apple or Google so they can be
forwarded to a user's phone and displayed on iOS or Android. While Apple
or Google assure the data is not collected or stored, should the
organizations be breached or coerced, all standard mobile notifications
on the platform could be compromised.

To avoid this risk, Mattermost can be configured to replace mobile
notification text with message ID numbers that pass no information to
Apple of Google. When received by the Mattermost mobile application on a
user's phone, the message IDs are used to privately communicate with
their Mattermost server and to retrieve mobile notification messages
over an encrypted channel. This means that, at no time, is the message
text visible to Apple or Google's message relay system. The contents of
the message also won\'t reach Mattermost.

:::: note
::: title
Note
:::

Because of the extra steps to retrieve the notifications messages under
Mattermost's private mobility capability with ID-only push
notifications, end users may experience a slight delay before the mobile
notification is fully displayed compared to sending clear text through
Apple and Google's platform.
::::

See our
`configuration settings <administration-guide/configure/site-configuration-settings:push notification contents>`{.interpreted-text
role="ref"} documentation to learn more about the ID-only push
notifications configuration setting. See our
`Mobile Apps FAQ documentation <deployment-guide/mobile/mobile-faq:how can i use id-only push notifications to protect notification content from being exposed to third-party services?>`{.interpreted-text
role="ref"} for details on using ID-only push notifications for data
privacy.

### Push notification server location

+-------------------------------+---------------------------------------------+
| The physical location of the  | - System Config path: **Environment \> Push |
| Mattermost Hosted Push        |   Notification Server**                     |
| Notification Service (HPNS)   | - `config.json` setting: `EmailSettings` \> |
| server.                       |   `PushNotificationServer`                  |
|                               | - Environment variable:                     |
| Select from **US**            |   `MM_EMAILSETTINGS_PUSHNOTIFICATIONSERVER` |
| **(Default)** or **Germany**  |                                             |
| to automatically populate the |                                             |
| **Push Notification Server**  |                                             |
| field server URL.             |                                             |
+-------------------------------+---------------------------------------------+

### Maximum notifications per channel

+----------------------------+-------------------------------------------------+
| The maximum total number   | - System Config path: **Environment \> Push     |
| of users in a channel      |   Notification Server**                         |
| before \@all, \@here, and  | - `config.json` setting: `TeamSettings` \>      |
| \@channel no longer send   |   `MaxNotificationsPerChannel` \> `1000`        |
| desktop, email, or mobile  | - Environment variable:                         |
| push notifications to      |   `MM_EMAILSETTINGS_MAXNOTIFICATIONSPERCHANNEL` |
| maximize performance.      |                                                 |
|                            |                                                 |
| Numerical input. Default   |                                                 |
| is **1000**.               |                                                 |
+----------------------------+-------------------------------------------------+

:::: note
::: title
Note
:::

- We recommend increasing this value a little at a time, monitoring
  system health by tracking
  `performance monitoring metrics </administration-guide/scale/deploy-prometheus-grafana-for-performance-monitoring>`{.interpreted-text
  role="doc"}, and only increasing this value if large channels have
  restricted permissions controlling who can post to the channel, such
  as a
  `read-only channel <administration-guide/onboard/advanced-permissions:read-only channels>`{.interpreted-text
  role="ref"}.
- Reducing this configuration setting value to **10** in larger
  deployments may improve server performance in the following areas:
  - **Reduced Load on Notification System**: Each notification generates
    a certain amount of computational and network load. By limiting the
    number of notifications per channel, the system processes fewer
    notifications, thereby reducing the load on servers.
  - **Database Efficiency**: Notifications are typically stored in a
    database. Fewer notifications mean less frequent database writes and
    reads, leading to quicker database operations and reduced latency.
  - **Minimized Client Processing**: Users\' clients (e.g., desktop and
    mobile apps) have to fetch and process notifications. With fewer
    notifications, clients can operate more efficiently, reducing memory
    and CPU usage on users\' devices.
  - **Improved User Experience**: An overload of notifications can lead
    to performance lags and a cluttered experience for users. Limiting
    the number ensures that users receive only the most important
    notifications, which can enhance usability and response times.
  - **Network Bandwidth**: High numbers of notifications can consume a
    lot of bandwidth, particularly if they are being sent to many users.
    Fewer notifications can lead to lower overall network usage and
    potentially faster delivery of critical messages.
  - **Server Load Balancing**: By reducing the number of notifications,
    the workload can be more evenly distributed across the servers,
    leading to better load balancing and preventing any single server
    from becoming a bottleneck.
::::

------------------------------------------------------------------------

## High availability

With self-hosted deployments, you can configure Mattermost as a
`high availability cluster-based deployment </administration-guide/scale/high-availability-cluster-based-deployment>`{.interpreted-text
role="doc"} by going to **System Console \> Environment \> High
Availability**, or by editing the `config.json` file as described in the
following tables. Changes to configuration settings in this section
require a server restart before taking effect.

In a Mattermost high availability cluster-based deployment, the System
Console is set to read-only, and settings can only be changed by editing
the `config.json` file directly. However, to test a high availability
cluster-based environment, you can disable
`ClusterSettings.ReadOnlyConfig` in the `config.json` file by setting it
to `false`. This allows changes applied using the System Console to be
saved back to the configuration file.

### Enable high availability mode

+--------------------------------+-------------------------------------+
| You can enable high            | - System Config path: **Environment |
| availability mode.             |   \> High Availability**            |
|                                | - `config.json` setting:            |
| - **true**: The Mattermost     |   `ClusterSettings` \> `Enable` \>  |
|   server will attempt          |   `false`                           |
|   inter-node communication     | - Environment variable:             |
|   with the other servers in    |   `MM_CLUSTERSETTINGS_ENABLE`       |
|   the cluster that have the    |                                     |
|   same cluster name. This sets |                                     |
|   the System Console to        |                                     |
|   read-only mode to keep the   |                                     |
|   servers\' `config.json`      |                                     |
|   files in sync.               |                                     |
| - **false**: **(Default)**     |                                     |
|   Mattermost high availability |                                     |
|   mode is disabled.            |                                     |
+--------------------------------+-------------------------------------+

### Cluster name

+-----------------------------------+------------------------------------+
| The cluster to join by name in a  | - System Config path:              |
| high availability cluster-based   |   **Environment \> High            |
| deployment.                       |   Availability**                   |
|                                   | - `config.json` setting:           |
| Only nodes with the same cluster  |   `ClusterSettings` \>             |
| name will join together. This is  |   `ClusterName`                    |
| to support blue-green deployments | - Environment variable:            |
| or staging pointing to the same   |   `MM_CLUSTERSETTINGS_CLUSTERNAME` |
| database.                         |                                    |
+-----------------------------------+------------------------------------+

### Override hostname

+-------------------------------+-----------------------------------------+
| You can override the hostname | - System Config path: **Environment \>  |
| of this server.               |   High Availability**                   |
|                               | - `config.json` setting:                |
| - This property can be set to |   `ClusterSettings` \>                  |
|   a specific IP address if    |   `OverrideHostname`                    |
|   needed; however, we don't   | - Environment variable:                 |
|   recommend overriding the    |   `MM_CLUSTERSETTINGS_OVERRIDEHOSTNAME` |
|   hostname unless it\'s       |                                         |
|   necessary.                  |                                         |
| - If left blank, Mattermost   |                                         |
|   attempts to get the         |                                         |
|   hostname from the operating |                                         |
|   system or uses the IP       |                                         |
|   address.                    |                                         |
+-------------------------------+-----------------------------------------+

See the
`high availability cluster-based deployment </administration-guide/scale/high-availability-cluster-based-deployment>`{.interpreted-text
role="doc"} documentation for details.

### Use IP address

+----------------------------------+-------------------------------------+
| You can configure your high      | - System Config path: **Environment |
| availability cluster-based       |   \> High Availability**            |
| deployment to communicate using  | - `config.json` setting:            |
| the hostname instead of the IP   |   `ClusterSettings` \>              |
| address.                         |   `UseIPAddress` \> `true`          |
|                                  | - Environment variable:             |
| - **true**: **(Default)** The    |   `MM_CLUSTERSETTINGS_USEIPADDRESS` |
|   cluster attempts to            |                                     |
|   communicate using the IP       |                                     |
|   address specified.             |                                     |
| - **false**: The cluster         |                                     |
|   attempts to communicate using  |                                     |
|   the hostname.                  |                                     |
+----------------------------------+-------------------------------------+

### Enable gossip encryption

+-----------------------------+-----------------------------------------------+
| Gossip encryption uses      | - System Config path: **Environment \> High   |
| AES-256 by default, and     |   Availability**                              |
| this value isn\'t           | - `config.json` setting: `ClusterSettings` \> |
| configurable by design.     |   `EnableGossipEncryption` \> `true`          |
|                             | - Environment variable:                       |
| - **true**: **(Default)**   |   `MM_CLUSTERSETTINGS_ENABLEGOSSIPENCRYPTION` |
|   The server attempts to    |                                               |
|   communicate via the       |                                               |
|   gossip protocol over the  |                                               |
|   gossip port specified.    |                                               |
| - **false**: The server     |                                               |
|   attempts to communicate   |                                               |
|   over the streaming port.  |                                               |
+-----------------------------+-----------------------------------------------+

:::: note
::: title
Note
:::

- The Gossip protocol is based on principles outlined in the [SWIM
  protocol developed by researchers at Cornell
  University](https://www.cs.cornell.edu/projects/Quicksilver/public_pdfs/SWIM.pdf).
  The gossip protocol is a communication mechanism in distributed
  systems where nodes randomly exchange information to ensure data
  consistency across the network. It is decentralized, scalable, and
  fault-tolerant, making it ideal for systems with numerous nodes.
  Information is spread in a manner similar to social gossip, with nodes
  periodically \"gossiping\" updates to random peers until the network
  converges to a consistent state. Widely used in distributed databases,
  blockchain networks, and peer-to-peer systems, the protocol is simple
  to implement and resilient to node failures. However, it can suffer
  from redundancy and propagation delays in large networks.
- Alternatively, you can manually set the `ClusterEncryptionKey` row
  value in the **Systems** table. A key is a byte array converted to
  base64. Set this value to either 16, 24, or 32 bytes to select
  AES-128, AES-192, or AES-256 respectively.
- From Mattermost v10.11, gossip encryption is enabled by default for
  all new deployments. For existing deployments, all communication using
  the gossip protocol remains unencrypted unless you manually enable
  encryption. Prior to v10.11, gossip encryption is enabled by default
  for Cloud deployments and disabled by default for self-hosted
  deployments.
::::

### Enable gossip compression

+-----------------------------+------------------------------------------------+
| We recommend that you       | - System Config path: **Environment \> High    |
| disable this configuration  |   Availability**                               |
| setting for better          | - `config.json` setting: `ClusterSettings` \>  |
| performance.                |   `EnableGossipCompression` \> `true`          |
|                             | - Environment variable:                        |
| - **true**: **(Default for  |   `MM_CLUSTERSETTINGS_ENABLEGOSSIPCOMPRESSION` |
|   self-hosted               |                                                |
|   deployments)** All        |                                                |
|   communication through the |                                                |
|   cluster uses gossip       |                                                |
|   compression. This setting |                                                |
|   is enabled by default to  |                                                |
|   maintain compatibility    |                                                |
|   with older servers.       |                                                |
| - **false**: **(Default for |                                                |
|   Cloud deployments)** All  |                                                |
|   communication using the   |                                                |
|   gossip protocol remains   |                                                |
|   uncompressed.             |                                                |
+-----------------------------+------------------------------------------------+

### Gossip port

+--------------------------------+-------------------------------------+
| The port used for the gossip   | - System Config path: **Environment |
| protocol. Both UDP and TCP     |   \> High Availability**            |
| should be allowed on this      | - `config.json` setting:            |
| port.                          |   `ClusterSettings` \> `GossipPort` |
|                                |   \> `8074`                         |
| Numerical input. Default is    | - Environment variable:             |
| **8074**.                      |   `MM_CLUSTERSETTINGS_GOSSIPPORT`   |
+--------------------------------+-------------------------------------+

### Read only config

+-------------------------------+---------------------------------------+
| - **true**: **(Default)**     | - System Config path: N/A             |
|   Changes made to settings in | - `config.json` setting:              |
|   the System Console are      |   `ClusterSettings` \>                |
|   ignored.                    |   `ReadOnlyConfig` \> `true`          |
| - **false**: Changes made to  | - Environment variable:               |
|   settings in the System      |   `MM_CLUSTERSETTINGS_READONLYCONFIG` |
|   Console are written to      |                                       |
|   `config.json`.              |                                       |
+-------------------------------+---------------------------------------+

### Network interface

+-------------------------------+-----------------------------------------+
| An IP address used to         | - System Config path: N/A               |
| identify the device that does | - `config.json` setting:                |
| automatic IP detection in     |   `ClusterSettings` \>                  |
| high availability             |   `NetworkInterface` \> `""`            |
| cluster-based deployments.    | - Environment variable:                 |
|                               |   `MM_CLUSTERSETTINGS_NETWORKINTERFACE` |
| String input.                 |                                         |
+-------------------------------+-----------------------------------------+

### Bind address

+--------------------------------+-------------------------------------+
| An IP address used to bind     | - System Config path: N/A           |
| cluster traffic to a specific  | - `config.json` setting:            |
| network device.                |   `ClusterSettings` \>              |
|                                |   `BindAddress` \> `""`             |
| This setting is used primarily | - Environment variable:             |
| for servers with multiple      |   `MM_CLUSTERSETTINGS_BINDADDRESS`  |
| network devices or different   |                                     |
| Bind Address and Advertise     |                                     |
| Address like in deployments    |                                     |
| that involve NAT (Network      |                                     |
| Address Translation).          |                                     |
|                                |                                     |
| String input.                  |                                     |
+--------------------------------+-------------------------------------+

### Advertise address

+-------------------------------+-----------------------------------------+
| The IP address used to access | - System Config path: N/A               |
| the server from other nodes.  | - `config.json` setting:                |
| This settings is used primary |   `ClusterSettings` \>                  |
| when cluster nodes are not in |   `AdvertiseAddress` \> `""`            |
| the same network and involve  | - Environment variable:                 |
| NAT (Network Address          |   `MM_CLUSTERSETTINGS_ADVERTISEADDRESS` |
| Translation).                 |                                         |
|                               |                                         |
| String input.                 |                                         |
+-------------------------------+-----------------------------------------+

------------------------------------------------------------------------

## Rate limiting

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

### Enable rate limiting

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

### Maximum queries per second

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

### Maximum burst size

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

### Memory store size

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

### Vary rate limit by remote address

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

### Vary rate limit by user

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

### Vary rate limit by HTTP header

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

------------------------------------------------------------------------

## Logging

Mattermost provides 3 independent logging systems for self-hosted
deployments that can be configured separately with separate log files
and rotation policies to meet different operational and compliance
needs:

- [Log Settings](#log-settings)
- [Notification Log Settings](#notification-logging)
- [Audit Log Settings](#audit-logging)

By default, all Mattermost editions write logs to both the console and
to the `mattermost.log` file in a machine-readable JSON format.
Mattermost Enterprise and Professional customers can additionally log
directly to syslog and TCP socket destination targets.

### Log settings

Configure general logging by going to **System Console \> Environment \>
Logging**, or by editing the `config.json` file as described in the
following tables. Changes to configuration settings in this section
require a server restart before taking effect.

#### Output logs to console

+------------------------------+-------------------------------------------+
| Configure Mattermost to      | - System Config path: **Environment \>    |
| output general logs to the   |   Logging**                               |
| console.                     | - `config.json` setting: `LogSettings` \> |
|                              |   `EnableConsole` \> `true`               |
| - **true**: **(Default)**    | - Environment variable:                   |
|   Output log messages are    |   `MM_LOGSETTINGS_ENABLECONSOLE`          |
|   written to the console     |                                           |
|   based on the [console log  |                                           |
|   level](#console-log-level) |                                           |
|   configuration. The server  |                                           |
|   writes messages to the     |                                           |
|   standard output stream     |                                           |
|   (stdout).                  |                                           |
| - **false**: Output log      |                                           |
|   messages aren't written to |                                           |
|   the console.               |                                           |
+------------------------------+-------------------------------------------+

:::: note
::: title
Note
:::

From Mattermost v11.0, notification logs are automatically included in
the main console logs.
::::

#### Console log level

+--------------------------+-------------------------------------------+
| The level of detail in   | - System Config path: **Environment \>    |
| general log events       |   Logging**                               |
| written when Mattermost  | - `config.json` setting: `LogSettings` \> |
| outputs log messages to  |   `ConsoleLevel` \> `"DEBUG"`             |
| the console.             | - Environment variable:                   |
|                          |   `MM_LOGSETTINGS_CONSOLELEVEL`           |
| - **DEBUG**:             |                                           |
|   **(Default)** Outputs  |                                           |
|   verbose detail for     |                                           |
|   developers debugging   |                                           |
|   issues.                |                                           |
| - **ERROR**: Outputs     |                                           |
|   only error messages.   |                                           |
| - **INFO**: Outputs      |                                           |
|   error messages and     |                                           |
|   information around     |                                           |
|   startup and            |                                           |
|   initialization.        |                                           |
+--------------------------+-------------------------------------------+

#### Output console logs as JSON

+--------------------------+-------------------------------------------+
| Configure Mattermost to  | - System Config path: **Environment \>    |
| output general console   |   Logging**                               |
| logs as JSON.            | - `config.json` setting: `LogSettings` \> |
|                          |   `ConsoleJson` \> `true`                 |
| - **true**:              | - Environment variable:                   |
|   **(Default)** Logged   |   `MM_LOGSETTINGS_CONSOLEJSON`            |
|   events are written in  |                                           |
|   a machine-readable     |                                           |
|   JSON format.           |                                           |
| - **false**: Logged      |                                           |
|   events are written in  |                                           |
|   plain text.            |                                           |
+--------------------------+-------------------------------------------+

Typically set to **true** in a production environment.

#### Colorize plain text console logs

+--------------------------+-------------------------------------------+
| Enables system admins to | - System Config path: N/A                 |
| display plain text       | - `config.json` setting: `LogSettings` \> |
| general log level        |   `EnableColor` \> `false`                |
| details in color.        | - Environment variable:                   |
|                          |   `MM_LOGSETTINGS_ENABLECOLOR`            |
| - **true**: When logged  |                                           |
|   events are output to   |                                           |
|   the console as plain   |                                           |
|   text, colorize log     |                                           |
|   levels details.        |                                           |
| - **false**:             |                                           |
|   **(Default)** Plain    |                                           |
|   text log details       |                                           |
|   aren\'t colorized in   |                                           |
|   the console.           |                                           |
+--------------------------+-------------------------------------------+

#### Output logs to file

+---------------------------+-------------------------------------------+
| Configure Mattermost to   | - System Config path: **Environment \>    |
| output general console    |   Logging**                               |
| logs to a file.           | - `config.json` setting: `LogSettings` \> |
|                           |   `EnableFile` \> `true`                  |
| - **true**: **(Default)** | - Environment variable:                   |
|   Logged events are       |   `MM_LOGSETTINGS_ENABLEFILE`             |
|   written based on the    |                                           |
|   [file log               |                                           |
|   level](#file-log-level) |                                           |
|   configuration to a      |                                           |
|   `mattermost.log` file   |                                           |
|   located in the          |                                           |
|   directory configured    |                                           |
|   via `file location`.    |                                           |
| - **false**: Logged       |                                           |
|   events aren't written   |                                           |
|   to a file.              |                                           |
+---------------------------+-------------------------------------------+

:::: note
::: title
Note
:::

- From Mattermost v11.0, notification logs are automatically included in
  the main file logs.
- This setting is typically set to **true** in a production environment.
  When enabled, you can download the `mattermost.log` file locally by
  going to **System Console \> Reporting \> Server Logs**, and selecting
  **Download Logs**.
::::

#### File log directory

+--------------------------+-------------------------------------------+
| The location of the      | - System Config path: **Environment \>    |
| general log files.       |   Logging**                               |
|                          | - `config.json` setting: `LogSettings` \> |
| String input. If left    |   `FileLocation` \> `""`                  |
| blank, log files are     | - Environment variable:                   |
| stored in the `./logs`   |   `MM_LOGSETTINGS_FILELOCATION`           |
| directory.               |                                           |
+--------------------------+-------------------------------------------+

:::: note
::: title
Note
:::

- The path you configure must exist, and Mattermost must have write
  permissions for this directory.
- From Mattermost v11.4, you can use the `MM_LOG_PATH` environment
  variable to restrict log file locations to a designated root
  directory. This security enhancement ensures that all log files
  configured via `LogSettings.FileLocation` or
  `LogSettings.AdvancedLoggingJSON` remain within an authorized logging
  directory.
  - If `MM_LOG_PATH` isn\'t set, the default `logs` directory is used.
    Paths outside the root directory generate error logs and are
    excluded from
    `support packet </administration-guide/manage/admin/generating-support-packet>`{.interpreted-text
    role="doc"} downloads. See the
    `log path restrictions <administration-guide/manage/logging:log path restrictions>`{.interpreted-text
    role="ref"} documentation for details.
::::

#### File log level

+----------------------------+-----------------------------------------+
| The level of detail in     | - System Config path: **Environment \>  |
| general log events when    |   Logging**                             |
| when Mattermost outputs    | - `config.json` setting: `LogSettings`  |
| log messages to a file.    |   \> `FileLevel` \> `"INFO"`            |
|                            | - Environment variable:                 |
| - **DEBUG**: Outputs       |   `MM_LOGSETTINGS_FILELEVEL`            |
|   verbose detail for       |                                         |
|   developers debugging     |                                         |
|   issues.                  |                                         |
| - **ERROR**: Outputs only  |                                         |
|   error messages.          |                                         |
| - **INFO**: **(Default)**  |                                         |
|   Outputs error messages   |                                         |
|   and information around   |                                         |
|   startup and              |                                         |
|   initialization.          |                                         |
+----------------------------+-----------------------------------------+

#### Output file logs as JSON

+---------------------------+------------------------------------------+
| Configure Mattermost to   | - System Config path: **Environment \>   |
| output general file logs  |   Logging**                              |
| as JSON.                  | - `config.json` setting: `LogSettings`   |
|                           |   \> `FileJson` \> `true`                |
| - **true**: **(Default)** | - Environment variable:                  |
|   Logged events are       |   `MM_LOGSETTINGS_FILEJSON`              |
|   written in a            |                                          |
|   machine-readable JSON   |                                          |
|   format.                 |                                          |
| - **false**: Logged       |                                          |
|   events are written in   |                                          |
|   plain text.             |                                          |
+---------------------------+------------------------------------------+

Typically set to **true** in a production environment.

#### Enable webhook debugging

+------------------------+---------------------------------------------+
| Configure Mattermost   | - System Config path: **Environment \>      |
| to capture the         |   Logging**                                 |
| contents of general    | - `config.json` setting: `LogSettings` \>   |
| incoming webhooks to   |   `EnableWebhookDebugging` \> `true`        |
| console and/or file    | - Environment variable:                     |
| logs for debugging.    |   `MM_LOGSETTINGS_ENABLEWEBHOOKDEBUGGING`   |
|                        |                                             |
| - **true**:            |                                             |
|   **(Default)** The    |                                             |
|   contents of incoming |                                             |
|   webhooks are printed |                                             |
|   to log files for     |                                             |
|   debugging.           |                                             |
| - **false**: The       |                                             |
|   contents of incoming |                                             |
|   webhooks aren't      |                                             |
|   printed to log       |                                             |
|   files.               |                                             |
+------------------------+---------------------------------------------+

:::: note
::: title
Note
:::

Enable debug logs by changing the [file log level](#file-log-level) to
`DEBUG` to include the request body of incoming webhooks in logs.
::::

#### Output logs to multiple targets

+------------------------+---------------------------------------------+
| Configure Mattermost   | - System Config path: **Environment \>      |
| to allow any           |   Logging**                                 |
| combination of         | - `config.json` setting: `LogSettings` \>   |
| console, local file,   |   `AdvancedLoggingJSON` \> `": ""`          |
| syslog, and TCP socket | - Environment variable:                     |
| targets, and send      |   `MM_LOGSETTINGS_ADVANCEDLOGGINGJSON`      |
| general log records to |                                             |
| multiple targets.      |                                             |
|                        |                                             |
| String input can       |                                             |
| contain a filespec to  |                                             |
| another configuration  |                                             |
| file, a database DSN,  |                                             |
| or JSON.               |                                             |
+------------------------+---------------------------------------------+

:::: note
::: title
Note
:::

- See the
  `Mattermost logging </administration-guide/manage/logging>`{.interpreted-text
  role="doc"} documentation for details. These targets have been chosen
  as they support the vast majority of log aggregators, and other log
  analysis tools, without needing additional software installed.
- Logs are recorded asynchronously to reduce latency to the caller.
- Advanced logging supports hot-reloading of logger configuration.
- From Mattermost v11.4, file paths specified in `AdvancedLoggingJSON`
  configurations should be within the directory specified by the
  `MM_LOG_PATH` environment variable. See
  `log path restrictions <administration-guide/manage/logging:log path restrictions>`{.interpreted-text
  role="ref"} for details.
::::

#### Maximum field size

+--------------------------+-------------------------------------------+
| Enables system admins to | - System Config path: N/A                 |
| limit the size of        | - `config.json` setting: `LogSettings` \> |
| general log fields       |   `MaxFieldSize` \> `2048`                |
| during logging.          | - Environment variable:                   |
|                          |   `MM_LOGSETTINGS_MAXFIELDSIZE`           |
| Numerical value. Default |                                           |
| is **2048**.             |                                           |
+--------------------------+-------------------------------------------+

#### Enable diagnostics and error reporting

+-------------------------+--------------------------------------------+
| Whether or not general  | - System Config path: **Environment \>     |
| diagnostics and error   |   Logging**                                |
| reports are sent to     | - `config.json` setting: `LogSettings` \>  |
| Mattermost, Inc.        |   `EnableDiagnostics` \> `""`              |
|                         | - Environment variable:                    |
| - **true**:             |   `MM_LOGSETTINGS_ENABLEDIAGNOSTICS`       |
|   **(Default)** Send    |                                            |
|   diagnostics and error |                                            |
|   reports.              |                                            |
| - **false**:            |                                            |
|   Diagnostics and error |                                            |
|   reports aren\'t sent. |                                            |
+-------------------------+--------------------------------------------+

:::: note
::: title
Note
:::

See the
`telemetry <administration-guide/manage/telemetry:error and diagnostics reporting feature>`{.interpreted-text
role="ref"} docummentation for details on the information Mattermost
collects.
::::

#### Enable verbose diagnostics

+-------------------------+--------------------------------------------+
| Whether or not verbose  | - System Config path: N/A                  |
| general diagnostics     | - `config.json` setting: `LogSettings` \>  |
| information is sent.    |   `VerboseDiagnostics` \> `false`          |
|                         | - Environment variable:                    |
| - **true**: Send        |   `MM_LOGSETTINGS_VERBOSEDIAGNOSTICS`      |
|   verbose diagnostics   |                                            |
|   information.          |                                            |
| - **false**:            |                                            |
|   **(Default)** Verbose |                                            |
|   diagnostics           |                                            |
|   information isn\'t    |                                            |
|   sent.                 |                                            |
+-------------------------+--------------------------------------------+

#### Enable Sentry reporting

+-------------------------+--------------------------------------------+
| Whether or not general  | - System Config path: N/A                  |
| error reports are sent  | - `config.json` setting: `LogSettings` \>  |
| to Sentry.              |   `EnableSentry` \> `true`                 |
|                         | - Environment variable:                    |
| - **true**:             |   `MM_LOGSETTINGS_ENABLESENTRY`            |
|   **(Default)** Send    |                                            |
|   error reports to      |                                            |
|   Sentry. Default       |                                            |
|   matches the           |                                            |
|   EnableDiagnostics     |                                            |
|   setting.              |                                            |
| - **false**: Error      |                                            |
|   reports are not sent  |                                            |
|   to Sentry.            |                                            |
+-------------------------+--------------------------------------------+

------------------------------------------------------------------------

### Notification logging

:::: important
::: title
Important
:::

**From Mattermost v11, notification log settings have been consolidated
into the standard console logs and mattermost.log file**. You can no
longer disable notification logging without using advanced logging
settings, as the main log level setting now controls both server and
notification logs.

You can use the `AdvancedLoggingJSON` configuration with discrete
notification log levels: `NotificationError`, `NotificationWarn`,
`NotificationInfo`, `NotificationDebug`, and `NotificationTrace` to
split notification logs into separate files and reduce troubleshooting
noise. See
`Advanced Logging <administration-guide/manage/logging:advanced logging>`{.interpreted-text
role="ref"} for details.
::::

The following configuration settings apply only to Mattermost server
versions prior to v11.0.

You can configure logging specifically for Mattermost notifications by
editing the `config.json` file as described in the following tables.
These settings operate independently from the main `LogSettings` and
allow you to customize logging behavior specifically for the
notification subsystem. Changes to these configuration settings require
a server restart before taking effect.

#### Output logs to console

+------------------------------+----------------------------------------------+
| Configure Mattermost to      | - System Config path: N/A                    |
| output notification logs to  | - `config.json` setting:                     |
| the console.                 |   `NotificationLogSettings` \>               |
|                              |   `EnableConsole` \> `true`                  |
| - **true**: **(Default)**    | - Environment variable:                      |
|   Output log messages are    |   `MM_NOTIFICATIONLOGSETTINGS_ENABLECONSOLE` |
|   written to the console     |                                              |
|   based on the [console log  |                                              |
|   level](#console-log-level) |                                              |
|   configuration. The server  |                                              |
|   writes messages to the     |                                              |
|   standard output stream     |                                              |
|   (stdout).                  |                                              |
| - **false**: Output log      |                                              |
|   messages aren\'t written   |                                              |
|   to the console.            |                                              |
+------------------------------+----------------------------------------------+

#### Console log level

+------------------------+---------------------------------------------+
| The level of detail in | - System Config path: N/A                   |
| notification log       | - `config.json` setting:                    |
| events written when    |   `NotificationLogSettings` \>              |
| Mattermost outputs log |   `ConsoleLevel` \> `"DEBUG"`               |
| messages to the        | - Environment variable:                     |
| console.               |   `MM_NOTIFICATIONLOGSETTINGS_CONSOLELEVEL` |
|                        |                                             |
| - **DEBUG**:           |                                             |
|   **(Default)**        |                                             |
|   Outputs verbose      |                                             |
|   detail for           |                                             |
|   developers debugging |                                             |
|   issues.              |                                             |
| - **ERROR**: Outputs   |                                             |
|   only error messages. |                                             |
| - **INFO**: Outputs    |                                             |
|   error messages and   |                                             |
|   information around   |                                             |
|   startup and          |                                             |
|   initialization.      |                                             |
+------------------------+---------------------------------------------+

#### Output console logs as JSON

+------------------------+---------------------------------------------+
| Configure Mattermost   | - System Config path: N/A                   |
| to output notification | - `config.json` setting:                    |
| console logs as JSON.  |   `NotificationLogSettings` \>              |
|                        |   `ConsoleJson` \> `true`                   |
| - **true**:            | - Environment variable:                     |
|   **(Default)** Logged |   `MM_NOTIFICATIONLOGSETTINGS_CONSOLEJSON`  |
|   events are written   |                                             |
|   in a                 |                                             |
|   machine-readable     |                                             |
|   JSON format.         |                                             |
| - **false**: Logged    |                                             |
|   events are written   |                                             |
|   in plain text.       |                                             |
+------------------------+---------------------------------------------+

Typically set to **true** in a production environment.

#### Colorize plain text console logs

+------------------------+---------------------------------------------+
| Enables system admins  | - System Config path: N/A                   |
| to display plain text  | - `config.json` setting:                    |
| notification log level |   `NotificationLogSettings` \>              |
| details in color.      |   `EnableColor` \> `false`                  |
|                        | - Environment variable:                     |
| - **true**: When       |   `MM_NOTIFICATIONLOGSETTINGS_ENABLECOLOR`  |
|   logged events are    |                                             |
|   output to the        |                                             |
|   console as plain     |                                             |
|   text, colorize log   |                                             |
|   levels details.      |                                             |
| - **false**:           |                                             |
|   **(Default)** Plain  |                                             |
|   text log details     |                                             |
|   aren\'t colorized in |                                             |
|   the console.         |                                             |
+------------------------+---------------------------------------------+

#### Output logs to file

+---------------------------+---------------------------------------------+
| Configure Mattermost to   | - System Config path: N/A                   |
| output notification       | - `config.json` setting:                    |
| console logs to a file.   |   `NotificationLogSettings` \> `EnableFile` |
|                           |   \> `true`                                 |
| - **true**: **(Default)** | - Environment variable:                     |
|   Logged events are       |   `MM_NOTIFICATIONLOGSETTINGS_ENABLEFILE`   |
|   written based on the    |                                             |
|   [file log               |                                             |
|   level](#file-log-level) |                                             |
|   configuration to a      |                                             |
|   `notifications.log`     |                                             |
|   file located in the     |                                             |
|   directory configured    |                                             |
|   via `file location`.    |                                             |
| - **false**: Logged       |                                             |
|   events aren\'t written  |                                             |
|   to a file.              |                                             |
+---------------------------+---------------------------------------------+

#### File log directory

+------------------------+---------------------------------------------+
| The location of the    | - System Config path: N/A                   |
| notification log       | - `config.json` setting:                    |
| files.                 |   `NotificationLogSettings` \>              |
|                        |   `FileLocation` \> `""`                    |
| String input. If left  | - Environment variable:                     |
| blank, log files are   |   `MM_NOTIFICATIONLOGSETTINGS_FILELOCATION` |
| stored in the `./logs` |                                             |
| directory.             |                                             |
+------------------------+---------------------------------------------+

:::: note
::: title
Note
:::

The path you configure must exist, and Mattermost must have write
permissions for this directory.
::::

#### File log level

+-------------------------+--------------------------------------------+
| The level of detail in  | - System Config path: N/A                  |
| notification log events | - `config.json` setting:                   |
| when Mattermost outputs |   `NotificationLogSettings` \> `FileLevel` |
| log messages to a file. |   \> `"INFO"`                              |
|                         | - Environment variable:                    |
| - **DEBUG**: Outputs    |   `MM_NOTIFICATIONLOGSETTINGS_FILELEVEL`   |
|   verbose detail for    |                                            |
|   developers debugging  |                                            |
|   issues.               |                                            |
| - **ERROR**: Outputs    |                                            |
|   only error messages.  |                                            |
| - **INFO**:             |                                            |
|   **(Default)** Outputs |                                            |
|   error messages and    |                                            |
|   information around    |                                            |
|   startup and           |                                            |
|   initialization.       |                                            |
+-------------------------+--------------------------------------------+

#### Output file logs as JSON

+------------------------+---------------------------------------------+
| Configure Mattermost   | - System Config path: N/A                   |
| to output notification | - `config.json` setting:                    |
| file logs as JSON.     |   `NotificationLogSettings` \> `FileJson`   |
|                        |   \> `true`                                 |
| - **true**:            | - Environment variable:                     |
|   **(Default)** Logged |   `MM_NOTIFICATIONLOGSETTINGS_FILEJSON`     |
|   events are written   |                                             |
|   in a                 |                                             |
|   machine-readable     |                                             |
|   JSON format.         |                                             |
| - **false**: Logged    |                                             |
|   events are written   |                                             |
|   in plain text.       |                                             |
+------------------------+---------------------------------------------+

#### Output logs to multiple targets

+-----------------------+----------------------------------------------------+
| Configure Mattermost  | - System Config path: N/A                          |
| to allow any          | - `config.json` setting: `NotificationLogSettings` |
| combination of        |   \> `AdvancedLoggingJSON` \> `": ""`              |
| console, local file,  | - Environment variable:                            |
| syslog, and TCP       |   `MM_NOTIFICATIONLOGSETTINGS_ADVANCEDLOGGINGJSON` |
| socket targets, and   |                                                    |
| send notification log |                                                    |
| records to multiple   |                                                    |
| targets.              |                                                    |
|                       |                                                    |
| String input can      |                                                    |
| contain a filespec to |                                                    |
| another configuration |                                                    |
| file, a database DSN, |                                                    |
| or JSON.              |                                                    |
+-----------------------+----------------------------------------------------+

------------------------------------------------------------------------

### Audit logging

Configure audit logging by going to **System Console \> Compliance \>
Audit Logging**, or by editing the `config.json` file as described in
the following tables. These settings operate independently from the main
`LogSettings` and allow you to customize logging behavior specifically
for the audit subsystem. Changes to these configuration settings require
a server restart before taking effect.

#### Output audit logs to file

+-------------------------+----------------------------------------------+
| Whether to write audit  | - System Config path: **Compliance \> Audit  |
| log files to disk.      |   Logging**                                  |
|                         | - `config.json` setting:                     |
| - **true**: Logged      |   `ExperimentalAuditSettings` \>             |
|   events are written to |   `FileEnabled` \> `false`                   |
|   the file specified by | - Environment variable:                      |
|   the audit file name   |   `MM_EXPERIMENTALAUDITSETTINGS_FILEENABLED` |
|   configuration         |                                              |
|   setting.              |                                              |
| - **false**:            |                                              |
|   **(Default)** Audit   |                                              |
|   log files aren\'t     |                                              |
|   written.              |                                              |
+-------------------------+----------------------------------------------+

:::: note
::: title
Note
:::

When `FileEnabled` is set to **true**, then the [audit file
name](#auditlog-filename) must be set.
::::

#### Audit file name

+---------------------------------+-------------------------------------------+
| The name of the audit log       | - System Config path: **Compliance \>     |
| files.                          |   Audit Logging**                         |
|                                 | - `config.json` setting:                  |
| The path that you set to the    |   `ExperimentalAuditSettings` \>          |
| audit file must exist and       |   `FileName` \> `""`                      |
| Mattermost must have write      | - Environment variable:                   |
| permissions in it.              |   `MM_EXPERIMENTALAUDITSETTINGS_FILENAME` |
|                                 |                                           |
| **Example:**                    |                                           |
| `/var/log/mattermost_audit.log` |                                           |
+---------------------------------+-------------------------------------------+

:::: note
::: title
Note
:::

The file name must be set to [enable](#auditlog-fileenabled) audit
logging.
::::

#### Maximum file size

+-------------------------+------------------------------------------------+
| The maximum size in     | - System Config path: **Compliance \> Audit    |
| megabytes for audit log |   Logging**                                    |
| files before they are   | - `config.json` setting:                       |
| rotated.                |   `ExperimentalAuditSettings` \>               |
|                         |   `FileMaxSizeMB` \> `100`                     |
| Numerical input.        | - Environment variable:                        |
| Default is **100** MB.  |   `MM_EXPERIMENTALAUDITSETTINGS_FILEMAXSIZEMB` |
+-------------------------+------------------------------------------------+

#### Maximum file age

+-------------------------+-------------------------------------------------+
| The maximum age in days | - System Config path: **Compliance \> Audit     |
| for audit log files     |   Logging**                                     |
| before they are         | - `config.json` setting:                        |
| deleted.                |   `ExperimentalAuditSettings` \>                |
|                         |   `FileMaxAgeDays` \> `0`                       |
| Numerical input.        | - Environment variable:                         |
| Default is **0** (no    |   `MM_EXPERIMENTALAUDITSETTINGS_FILEMAXAGEDAYS` |
| limit).                 |                                                 |
+-------------------------+-------------------------------------------------+

#### Maximum file backups

+-------------------------+-------------------------------------------------+
| The maximum number of   | - System Config path: **Compliance \> Audit     |
| audit log file backups  |   Logging**                                     |
| to retain.              | - `config.json` setting:                        |
|                         |   `ExperimentalAuditSettings` \>                |
| Numerical input.        |   `FileMaxBackups` \> `0`                       |
| Default is **0** (no    | - Environment variable:                         |
| limit).                 |   `MM_EXPERIMENTALAUDITSETTINGS_FILEMAXBACKUPS` |
+-------------------------+-------------------------------------------------+

#### Compress audit log files

+------------------------+-----------------------------------------------+
| Whether to compress    | - System Config path: **Compliance \> Audit   |
| rotated audit log      |   Logging**                                   |
| files.                 | - `config.json` setting:                      |
|                        |   `ExperimentalAuditSettings` \>              |
| - **true**: Rotated    |   `FileCompress` \> `false`                   |
|   audit log files are  | - Environment variable:                       |
|   compressed.          |   `MM_EXPERIMENTALAUDITSETTINGS_FILECOMPRESS` |
| - **false**:           |                                               |
|   **(Default)**        |                                               |
|   Rotated audit log    |                                               |
|   files aren\'t        |                                               |
|   compressed.          |                                               |
+------------------------+-----------------------------------------------+

#### Audit log queue size

+------------------------+---------------------------------------------------+
| The maximum number of  | - System Config path: **Compliance \> Audit       |
| audit log entries that |   Logging**                                       |
| can be queued.         | - `config.json` setting:                          |
|                        |   `ExperimentalAuditSettings` \>                  |
| Numerical input.       |   `FileMaxQueueSize` \> `1000`                    |
| Default is **1000**.   | - Environment variable:                           |
|                        |   `MM_EXPERIMENTALAUDITSETTINGS_FILEMAXQUEUESIZE` |
+------------------------+---------------------------------------------------+

#### Audit log certificate

+------------------------+----------------------------------------------+
| Certificate            | - System Config path: N/A                    |
| configuration for      | - `config.json` setting:                     |
| audit logging.         |   `ExperimentalAuditSettings` \>             |
|                        |   `Certificate` \> `""`                      |
| String input. Default  | - Environment variable:                      |
| is blank.              |   `MM_EXPERIMENTALAUDITSETTINGS_CERTIFICATE` |
+------------------------+----------------------------------------------+

#### Output audit logs to multiple targets

+------------------------+------------------------------------------------------+
| Configures Mattermost  | - System Config path: **Compliance \> Audit          |
| to output audit log    |   Logging**                                          |
| records to multiple    | - `config.json` setting: `ExperimentalAuditSettings` |
| targets.               |   \> `AdvancedLoggingJSON` \> `{}`                   |
|                        | - Environment variable:                              |
|                        |   `MM_EXPERIMENTALAUDITSETTINGS_ADVANCEDLOGGINGJSON` |
+------------------------+------------------------------------------------------+

:::: note
::: title
Note
:::

- See the
  `Mattermost logging </administration-guide/manage/logging>`{.interpreted-text
  role="doc"} documentation for details on advanced logging
  configuration. These targets have been chosen as they support the vast
  majority of log aggregators, and other log analysis tools, without
  needing additional software installed.
- Audit logs are recorded asynchronously to reduce latency to the
  caller.
- Advanced audit logging supports hot-reloading of logger configuration.
::::

------------------------------------------------------------------------

## Session lengths

With self-hosted deployments, user sessions are cleared when a user
tries to log in, and sessions are cleared every 24 hours from the
sessions database table. Configure session lengths by going to **System
Console \> Environment \> Session Lengths**, or by editing the
`config.json` file as described in the following tables. Changes to
configuration settings in this section require a server restart before
taking effect.

### Extend session length with activity

+-----------------------------------+--------------------------------------------------------+
| Improves the user experience by   | - System Config path: **Environment \> Session         |
| extending sessions and keeping    |   Lengths**                                            |
| users logged in if they are       | - `config.json` setting: `ServiceSettings` \>          |
| active in their Mattermost apps.  |   `ExtendSessionLengthWithActivity` \> `true`          |
|                                   | - Environment variable:                                |
| - **true**: **(Default)**         |   `MM_SERVICESETTINGS_EXTENDSESSIONLENGTHWITHACTIVITY` |
|   Sessions are automatically      |                                                        |
|   extended when users are active  |                                                        |
|   in their Mattermost client.     |                                                        |
|   User sessions only expire when  |                                                        |
|   users aren't active in their    |                                                        |
|   Mattermost client for the       |                                                        |
|   entire duration of the session  |                                                        |
|   lengths defined.                |                                                        |
| - **false**: Sessions won\'t      |                                                        |
|   extend with activity in         |                                                        |
|   Mattermost. User sessions       |                                                        |
|   immediately expire at the end   |                                                        |
|   of the session length or based  |                                                        |
|   on the [session idle            |                                                        |
|   timeout](#session-idle-timeout) |                                                        |
|   configured.                     |                                                        |
+-----------------------------------+--------------------------------------------------------+

### Terminate sessions on password change

+---------------------------+----------------------------------------------------------+
| Enable or disable session | - System Config path: **Environment \> Session Lengths** |
| revocation when a user\'s | - `config.json` setting: `ServiceSettings` \>            |
| password changes.         |   `TerminateSessionsOnPasswordChange` \> `true`          |
|                           | - Environment variable:                                  |
| - **true**: **(Default    |   `MM_SERVICESETTINGS_TERMINATESESSIONSONPASSWORDCHANGE` |
|   for new deployments)**  |                                                          |
|   Session revocation is   |                                                          |
|   enabled. All sessions   |                                                          |
|   of a user expire if     |                                                          |
|   their password is       |                                                          |
|   changed (by themselves  |                                                          |
|   or by a system admin).  |                                                          |
|   If the password change  |                                                          |
|   is initiated by the     |                                                          |
|   user, their current     |                                                          |
|   session isn\'t          |                                                          |
|   terminated.             |                                                          |
| - **false**: **(Default   |                                                          |
|   for existing            |                                                          |
|   deployments)** Session  |                                                          |
|   revocation is disabled. |                                                          |
|   When users change their |                                                          |
|   password, only the      |                                                          |
|   user\'s current session |                                                          |
|   is revoked. When a      |                                                          |
|   system admin changes    |                                                          |
|   the user\'s password,   |                                                          |
|   none of the user\'s     |                                                          |
|   sessions are revoked.   |                                                          |
+---------------------------+----------------------------------------------------------+

### Session length for AD/LDAP and email

+-----------------------------+------------------------------------------------+
| Set the number of hours     | - System Config path: **Environment \> Session |
| counted from the last time  |   Lengths**                                    |
| a user entered their        | - `config.json` setting: `ServiceSettings` \>  |
| credentials into the web    |   `SessionLengthWebInHours` \> `720`           |
| app or the desktop app to   | - Environment variable:                        |
| the expiry of the user's    |   `MM_SERVICESETTINGS_SESSIONLENGTHWEBINHOURS` |
| session on email and        |                                                |
| AD/LDAP authentication.     |                                                |
|                             |                                                |
| Numerical input in hours.   |                                                |
| Default is **720** hours.   |                                                |
+-----------------------------+------------------------------------------------+

:::: note
::: title
Note
:::

After changing this setting, the new session length takes effect after
the next time the user enters their credentials.
::::

### Session length for mobile

+----------------------------+---------------------------------------------------+
| Set the number of hours    | - System Config path: **Environment \> Session    |
| counted from the last time |   Lengths**                                       |
| a user entered their       | - `config.json` setting: `ServiceSettings` \>     |
| credential into the mobile |   `SessionLengthMobileInHours` \> `720`           |
| app to the expiry of the   | - Environment variable:                           |
| user's session.            |   `MM_SERVICESETTINGS_SESSIONLENGTHMOBILEINHOURS` |
|                            |                                                   |
| Numerical input in hours.  |                                                   |
| Default is **720** hours.  |                                                   |
+----------------------------+---------------------------------------------------+

:::: note
::: title
Note
:::

After changing this setting, the new session length takes effect after
the next time the user enters their credentials.
::::

### Session length for SSO

+-----------------------------+------------------------------------------------+
| Set the number of hours     | - System Config path: **Environment \> Session |
| from the last time a user   |   Lengths**                                    |
| entered their SSO           | - `config.json` setting: `ServiceSettings` \>  |
| credentials to the expiry   |   `SessionLengthSSOInHours` \> `720`           |
| of the user's session. This | - Environment variable:                        |
| setting defines the session |   `MM_SERVICESETTINGS_SESSIONLENGTHSSOINHOURS` |
| length for SSO              |                                                |
| authentication, such as     |                                                |
| SAML, GitLab, and OAuth     |                                                |
| 2.0.                        |                                                |
|                             |                                                |
| Numerical input in hours.   |                                                |
| Default is **720** hours.   |                                                |
| Numbers as decimals are     |                                                |
| also valid values for this  |                                                |
| configuration setting.      |                                                |
+-----------------------------+------------------------------------------------+

:::: note
::: title
Note
:::

- After changing this setting, the new session length takes effect after
  the next time the user enters their credentials.
- If the authentication method is SAML, GitLab, or OAuth 2.0, users may
  automatically be logged back in to Mattermost if they are already
  logged in to SAML, GitLab, or with OAuth 2.0.
::::

### Session cache

+-----------------------------+----------------------------------------------+
| Set the number of minutes   | - System Config path: **Environment \>       |
| to cache a session in       |   Session Lengths**                          |
| memory.                     | - `config.json` setting: `ServiceSettings`   |
|                             |   \> `SessionCacheInMinutes` \> `10`         |
| Numerical input in minutes. | - Environment variable:                      |
| Default is **10** minutes.  |   `MM_SERVICESETTINGS_SESSIONCACHEINMINUTES` |
+-----------------------------+----------------------------------------------+

### Session idle timeout

+----------------------------+----------------------------------------------------+
| The number of minutes from | - System Config path: N/A                          |
| the last time a user was   | - `config.json` setting: `ServiceSettings` \>      |
| active on the system to    |   `SessionIdleTimeoutInMinutes` \> `43200`         |
| the expiry of the user's   | - Environment variable:                            |
| session. Once expired, the |   `MM_SERVICESETTINGS_SESSIONIDLETIMEOUTINMINUTES` |
| user will need to log in   |                                                    |
| to continue.               |                                                    |
|                            |                                                    |
| Numerical input in         |                                                    |
| minutes. Default is        |                                                    |
| **43200** (30 days).       |                                                    |
| Minimum value is **5**     |                                                    |
| minutes, and a value of    |                                                    |
| **0** sets the time as     |                                                    |
| unlimited.                 |                                                    |
+----------------------------+----------------------------------------------------+

:::: note
::: title
Note
:::

- This setting has no effect when [extend session length with
  activity](#extend-session-length-with-activity) is set to **true**.
- This setting applies to the webapp and the desktop app. For mobile
  apps, use an
  `EMM provider </deployment-guide/mobile/deploy-mobile-apps-using-emm-provider>`{.interpreted-text
  role="doc"} to lock the app when not in use. \|
- In
  `high availability mode </administration-guide/scale/high-availability-cluster-based-deployment>`{.interpreted-text
  role="doc"}, enable IP hash load balancing for reliable timeout
  measurement.
::::

------------------------------------------------------------------------

## Performance monitoring

With self-hosted deployments, you can configure performance monitoring
by going to **System Console \> Environment \> Performance Monitoring**,
or by editing the `config.json` file as described in the following
tables.

``` json
{
  "MetricsSettings": {
    "Enable": false,
    "BlockProfileRate": 0,
    "ListenAddress": :8067,
    "EnableClientMetrics": false,
    "EnableNotificationMetrics": true,
    "ClientSideUserIds": ""
  }
}
```

Changes to configuration settings in this section require a server
restart before taking effect.

See the
`performance monitoring </administration-guide/scale/deploy-prometheus-grafana-for-performance-monitoring>`{.interpreted-text
role="doc"} documentation to learn more about setting up performance
monitoring with Prometheus and Grafana. See the
`collect performance metrics </administration-guide/scale/collect-performance-metrics>`{.interpreted-text
role="doc"} documentation to learn more about using the Mattermost
Metrics plugin.

### Enable performance monitoring

+--------------------------+-------------------------------------------+
| Enable or disable        | - System Config path: **Environment \>    |
| performance monitoring.  |   Performance Monitoring**                |
|                          | - `config.json` setting:                  |
| - **true**: Performance  |   `MetricsSettings` \> `Enable` \>        |
|   monitoring data        |   `false`                                 |
|   collection and         | - Environment variable:                   |
|   profiling is enabled.  |   `MM_METRICSSETTINGS_ENABLE`             |
| - **false**:             |                                           |
|   **(Default)**          |                                           |
|   Mattermost performance |                                           |
|   monitoring is          |                                           |
|   disabled.              |                                           |
+--------------------------+-------------------------------------------+

See the
`performance monitoring </administration-guide/scale/deploy-prometheus-grafana-for-performance-monitoring>`{.interpreted-text
role="doc"} documentation to learn more.

### Enable client performance monitoring

+--------------------------+--------------------------------------------+
| Enable or disable client | - System Config path: **Environment \>     |
| performance monitoring.  |   Performance Monitoring**                 |
|                          | - `config.json` setting: `MetricsSettings` |
| - **true**: Client       |   \> `EnableClientMetrics` \> `false`      |
|   performance monitoring | - Environment variable:                    |
|   data collection and    |   `MM_METRICSSETTINGS_ENABLECLIENTMETRICS` |
|   profiling is enabled.  |                                            |
| - **false**:             |                                            |
|   **(Default)**          |                                            |
|   Mattermost client      |                                            |
|   performance monitoring |                                            |
|   is disabled.           |                                            |
+--------------------------+--------------------------------------------+

### Client side user ids

+--------------------------------+------------------------------------------+
| A list of comma-separated user | - System Config path: **Environment \>   |
| IDs you want to track for      |   Performance Monitoring**               |
| client-side webapp metrics.    | - `config.json` setting:                 |
|                                |   `MetricsSettings` \>                   |
| Limited to 5 user IDs. Blank   |   `ClientSideUserIds`                    |
| by default.                    | - Environment variable:                  |
|                                |   `MM_METRICSSETTINGS_CLIENTSIDEUSERIDS` |
+--------------------------------+------------------------------------------+

:::: note
::: title
Note
:::

- This setting only applies when `EnableClientMetrics` is set to `true`.
- Each user ID should correspond to a valid user in the Mattermost
  system. For example,
  `MM_METRICSSETTINGS_CLIENTSIDEUSERIDS="user1,user2,user3"`.
- The total number of user IDs is limited to 5 to ensure performance.
  Adding more IDs can overwhelm Prometheus due to high label
  cardinality. To avoid performance issues, we recommend minimizing
  changes to this list.
::::

### Listen address

+-------------------------------+---------------------------------------+
| The port the Mattermost       | - System Config path: **Environment   |
| server will listen on to      |   \> Performance Monitoring**         |
| expose performance metrics,   | - `config.json` setting:              |
| when enabled.                 |   `MetricsSettings` \>                |
|                               |   `ListenAddress` \> `8067`           |
| Numerical input. Default is   | - Environment variable:               |
| **8067**.                     |   `MM_METRICSSETTINGS_LISTENADDRESS`  |
+-------------------------------+---------------------------------------+

:::: note
::: title
Note
:::

- `ListenAddress` accepts a port only. It doesn't take an IP/host. If
  you need to restrict interfaces, do so via your OS firewall or reverse
  proxy.
- The address uses a `host:port` format. Use `:8067` to listen on all
  interfaces on port **8067**, or use `localhost:8067` to restrict to
  **localhost** only.
::::

### Block profile rate

+-------------------------------+-----------------------------------------+
| Control how often Mattermost  | - System Config path: **N/A**           |
| collects data about delays    | - `config.json` setting:                |
| caused by blocking operations |   `MetricsSettings` \>                  |
| within Mattermost (such as    |   `BlockProfileRate` \> `0`             |
| when one part of the program  | - Environment variable:                 |
| has to wait for another).     |   `MM_METRICSSETTINGS_BLOCKPROFILERATE` |
| Default is **0** (profiling   |                                         |
| is disabled).                 |                                         |
|                               |                                         |
| The profiler aims to sample   |                                         |
| an average of one blocking    |                                         |
| event per rate nanoseconds    |                                         |
| spent blocked.                |                                         |
|                               |                                         |
| Default is **0**.             |                                         |
+-------------------------------+-----------------------------------------+

:::: note
::: title
Note
:::

- This setting isn\'t available in the System Console and can only be
  set in `config.json`.
- Only adjust this if you're diagnosing performance issues and know how
  to analyze profiling data. The value represents how frequently
  Mattermost records blocking events in its performance profile:
  - Set to 0 to record no blocking events (profiling is disabled).
  - Set to 1 to record every blocking event (profiling is fully
    enabled).
  - Set to a higher number to record only a fraction of events (useful
    for sampling instead of full profiling).
::::

### Enable notification monitoring

+----------------------+--------------------------------------------------+
| Enable or disable    | - System Config path: **Site Configuration \>    |
| notification metrics |   Notifications**                                |
| data collection.     | - `config.json` setting: `MetricsSettings` \>    |
|                      |   `EnableNotificationMetrics` \> `true`          |
| - **true**:          | - Environment variable:                          |
|   **(Default)**      |   `MM_METRICSSETTINGS_ENABLENOTIFICATIONMETRICS` |
|   Mattermost         |                                                  |
|   notification data  |                                                  |
|   collection is      |                                                  |
|   enabled for        |                                                  |
|   client-side web    |                                                  |
|   and desktop app    |                                                  |
|   users.             |                                                  |
| - **false**:         |                                                  |
|   Mattermost         |                                                  |
|   notification data  |                                                  |
|   collection is      |                                                  |
|   disabled.          |                                                  |
+----------------------+--------------------------------------------------+

:::: note
::: title
Note
:::

- `MetricsSettings.Enable` must be set to `true`
- The `NotificationMonitoring` feature flag must be set to `true`
::::

See the
`performance monitoring <administration-guide/scale/deploy-prometheus-grafana-for-performance-monitoring:getting started>`{.interpreted-text
role="ref"} documentation to learn more about Mattermost Notification
Health metrics.

------------------------------------------------------------------------

## Developer

With self-hosted deployments, you can configure developer mode by going
to **System Console \> Environment \> Developer**, or by editing the
`config.json` file as described in the following tables. Changes to
configuration settings in this section require a server restart before
taking effect.

### Enable testing commands

+---------------------------+------------------------------------------+
| Enable or disable the     | - System Config path: **Environment \>   |
| `/test` slash command.    |   Developer**                            |
|                           | - `config.json` setting:                 |
| - **true**: **(Default)** |   `ServiceSettings` \> `EnableTesting`   |
|   The `/test` slash       |   \> `true`                              |
|   command is enabled to   | - Environment variable:                  |
|   load test accounts and  |   `MM_SERVICESETTINGS_ENABLETESTING`     |
|   test data.              |                                          |
| - **false**: The `/test`  |                                          |
|   slash command is        |                                          |
|   disabled.               |                                          |
+---------------------------+------------------------------------------+

### Enable developer mode

+-------------------------+--------------------------------------------+
| Enable or disable       | - System Config path: **Environment \>     |
| developer mode.         |   Developer**                              |
|                         | - `config.json` setting: `ServiceSettings` |
| - **true**:             |   \> `EnableDeveloper` \> `true`           |
|   **(Default)**         | - Environment variable:                    |
|   Javascript errors are |   `MM_SERVICESETTINGS_ENABLEDEVELOPER`     |
|   shown in a banner at  |                                            |
|   the top of Mattermost |                                            |
|   the user interface.   |                                            |
|   Not recommended for   |                                            |
|   use in production.    |                                            |
| - **false**: Users are  |                                            |
|   not alerted to        |                                            |
|   Javascript errors.    |                                            |
+-------------------------+--------------------------------------------+

### Enable client debugging

+-----------------------+---------------------------------------------------------+
| Enable or disable     | - System Config path: **Environment \> Developer**      |
| client-side debugging | - `config.json` setting: `ServiceSettings` \>           |
| settings found in     |   `EnableClientPerformanceDebugging` \> `false`         |
| **Settings \>         | - Environment variable:                                 |
| Advanced \>           |   `MM_SERVICESETTINGS_ENABLECLIENTPERFORMANCEDEBUGGING` |
| Debugging** for       |                                                         |
| individual users.     |                                                         |
|                       |                                                         |
| - **true**: Those     |                                                         |
|   settings are        |                                                         |
|   visible and can be  |                                                         |
|   enabled by users.   |                                                         |
| - **false**:          |                                                         |
|   **(Default)** Those |                                                         |
|   settings are hidden |                                                         |
|   and disabled.       |                                                         |
+-----------------------+---------------------------------------------------------+

See the
`client debugging <end-user-guide/preferences/manage-advanced-options:performance debugging>`{.interpreted-text
role="ref"} documentation to learn more.

### Allow untrusted internal connections

:::: warning
::: title
Warning
:::

This setting is intended to prevent users located outside your local
network from using the Mattermost server to request confidential data
from inside your network. Care should be used when configuring this
setting to prevent unintended access to your local network.
::::

+----------------------+------------------------------------------------------------+
| Limit the ability    | - System Config path: **Environment \> Developer**         |
| for the Mattermost   | - `config.json` setting: `ServiceSettings` \>              |
| server to make       |   `AllowedUntrustedInternalConnections` \> `""`            |
| untrusted requests   | - Environment variable:                                    |
| within its local     |   `MM_SERVICESETTINGS_ALLOWEDUNTRUSTEDINTERNALCONNECTIONS` |
| network. A request   |                                                            |
| is considered        |                                                            |
| "untrusted" when     |                                                            |
| it's made on behalf  |                                                            |
| of a client.         |                                                            |
+----------------------+------------------------------------------------------------+

This setting is a whitelist of local network addresses that can be
requested by the Mattermost server. It's configured as a
whitespace-separated list of hostnames, IP addresses, and CIDR ranges
that can be accessed.

Requests that can only be configured by system admins are considered
trusted and won\'t be affected by this setting. Trusted URLs include
ones used for OAuth login or for sending push notifications.

The following features make untrusted requests and are affected by this
setting:

- Integrations using webhooks, slash commands, or message actions. This
  prevents them from requesting endpoints within the local network.
- Link previews. When a link to a local network address is posted in a
  chat message, this prevents a link preview from being displayed.
- The local
  `image proxy </deployment-guide/server/image-proxy>`{.interpreted-text
  role="doc"}. If the local image proxy is enabled, images located on
  the local network cannot be used by integrations or posted in chat
  messages.

Some examples of when you may want to modify this setting include:

- When installing a plugin that includes its own images, such as
  [Matterpoll](https://github.com/matterpoll/matterpoll), you\'ll need
  to add the Mattermost server's domain name to this list.
- When running a bot or webhook-based integration on your local network,
  you'll need to add the hostname of the bot/integration to this list.
- If your network is configured in such a way that publicly-accessible
  web pages or images are accessed by the Mattermost server using their
  internal IP address, the hostnames for those servers must be added to
  this list.

:::: note
::: title
Note
:::

- The public IP of the Mattermost application server itself is also
  considered a reserved IP.
- Use whitespaces instead of commas to list the hostnames, IP addresses,
  or CIDR ranges. For example: `webhooks.internal.example.com`,
  `127.0.0.1`, or `10.0.16.0/28`.
- IP address and domain name rules are applied before host resolution.
- CIDR rules are applied after host resolution, and only CIDR rules
  require DNS resolution.
- Mattermost attempts to match IP addresses and hostnames without even
  resolving. If that fails, Mattermost resolve using the local resolver
  (by reading the `/etc/hosts` file first), then checking for matching
  CIDR rules. For example, if the domain "webhooks.internal.example.com"
  resolves to the IP address `10.0.16.20`, a webhook with the URL
  `https://webhooks.internal.example.com/webhook` can be whitelisted
  using `webhooks.internal.example.com`, or `10.0.16.16/28`, but not
  `10.0.16.20`.
::::

## Mobile security

From Mattermost v10.7 and mobile app v2.27, you can configure biometric
authentication, prevent Mattermost use on jailbroken or rooted devices,
and can block screen captures without relying on an EMM Provider.
Configure these options by going to **System Console \> Environment \>
Mobile Security**, or by editing the `config.json` file as described in
the following tables. Changes to configuration settings in this section
require a server restart and require users to restart their mobile app
or log out and back in before taking effect.

### Enable biometric authentication

+-----------------------+-------------------------------------------------+
| Enforce biometric     | - System Config path: **Environment \> Mobile   |
| authentication, with  |   Security**                                    |
| PIN/passcode          | - `config.json` setting: `NativeAppSettings` \> |
| fallback, before      |   `MobileEnableBiometrics` \> `false`           |
| accessing the app.    | - Environment variable:                         |
| Users will be         |   `MM_NATIVEAPPSETTINGS_MOBILEENABLEBIOMETRICS` |
| prompted based on     |                                                 |
| session activity and  |                                                 |
| server switching      |                                                 |
| rules.                |                                                 |
|                       |                                                 |
| - **true**: Biometric |                                                 |
|   authentication is   |                                                 |
|   enabled.            |                                                 |
| - **false**:          |                                                 |
|   **(Default)**       |                                                 |
|   Biometric           |                                                 |
|   authentication is   |                                                 |
|   disabled.           |                                                 |
+-----------------------+-------------------------------------------------+

:::: note
::: title
Note
:::

- Changing this configuration setting takes effect when mobile users
  restart their Mattermost mobile app or log out and log back in.
- Users must authenticate in the following situations:
  - Adding a new server: When a new server is added to the mobile app
    and biometric authentication is enabled.
  - Opening the mobile app: At app launch when the active server
    requires authentication.
  - Returning after background use: After the app has been in the
    background for 5 minutes or more and the active server requires
    authentication.
  - Using multiple servers: When accessing a server for the first time,
    after 5 minutes of inactivity on a server, and when the last
    authentication attempt fails.
::::

### Enable jailbreak/root protection

+-----------------------+----------------------------------------------------+
| Prevent access to the | - System Config path: **Environment \> Mobile      |
| app on devices        |   Security**                                       |
| detected as           | - `config.json` setting: `NativeAppSettings` \>    |
| jailbroken or rooted. |   `MobileJailbreakProtection` \> `false`           |
| If a device fails the | - Environment variable:                            |
| security check, users |   `MM_NATIVEAPPSETTINGS_MOBILEJAILBREAKPROTECTION` |
| will be denied access |                                                    |
| or prompted to switch |                                                    |
| to a compliant        |                                                    |
| server.               |                                                    |
|                       |                                                    |
| - **true**:           |                                                    |
|   Jailbreak/Root      |                                                    |
|   protection is       |                                                    |
|   enabled.            |                                                    |
| - **false**:          |                                                    |
|   **(Default)**       |                                                    |
|   Jailbreak/Root      |                                                    |
|   protection is       |                                                    |
|   disabled.           |                                                    |
+-----------------------+----------------------------------------------------+

:::: note
::: title
Note
:::

- Changing this configuration setting takes effect when mobile users
  restart their Mattermost mobile app or log out and log back in.
- See the [Expo SDK
  documentation](https://docs.expo.dev/versions/latest/sdk/device/#deviceisrootedexperimentalasync)
  to learn more about how checks are performed for this functionality.
::::

### Prevent screen capture

+-----------------------+-----------------------------------------------------+
| Block screenshots and | - System Config path: **Environment \> Mobile       |
| screen recordings     |   Security**                                        |
| when using the mobile | - `config.json` setting: `NativeAppSettings` \>     |
| app. Screenshots will |   `MobilePreventScreenCapture` \> `false`           |
| appear blank, and     | - Environment variable:                             |
| screen recordings     |   `MM_NATIVEAPPSETTINGS_MOBILEPREVENTSCREENCAPTURE` |
| will blur (iOS) or    |                                                     |
| show a black screen   |                                                     |
| (Android). Also       |                                                     |
| applies when          |                                                     |
| switching apps.       |                                                     |
|                       |                                                     |
| - **true**: Screen    |                                                     |
|   capture blocking is |                                                     |
|   enabled.            |                                                     |
| - **false**:          |                                                     |
|   **(Default)**       |                                                     |
|   Screen capture      |                                                     |
|   blocking is         |                                                     |
|   disabled.           |                                                     |
+-----------------------+-----------------------------------------------------+

:::: note
::: title
Note
:::

Changing this configuration setting takes effect when mobile users
restart their Mattermost mobile app or log out and log back in.
::::

### Enable secure file preview on mobile

This setting improves an organization\'s mobile security posture by
restricting file access while still allowing essential file viewing
capabilities.

+--------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| - **true**: Prevents file downloads, previews, and sharing for most file types, even when the                                                    | - System Config path: **Site Configuration \>     |
|   `Allow file downloads on mobile <administration-guide/configure/site-configuration-settings:allow file downloads on mobile>`{.interpreted-text |   File sharing and downloads**                    |
|   role="ref"} configuration setting is enabled. Allows in-app previews for PDFs, videos, and images only. Files are stored temporarily in the    | - `config.json` setting: `FileSettings` \>        |
|   app\'s cache and cannot be exported or shared.                                                                                                 |   `MobileEnableSecureFilePreview` \> `false`      |
| - **false**: **(Default)** Secure file preview mode is disabled.                                                                                 | - Environment variable:                           |
|                                                                                                                                                  |   `MM_FILESETTINGS_MOBILEENABLESECUREFILEPREVIEW` |
+--------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+

:::: note
::: title
Note
:::

Changing this configuration setting takes effect when mobile users
restart their Mattermost mobile app or log out and log back in.
::::

### Allow PDF link navigation on mobile

+------------------------------+--------------------------------------------------+
| - **true**: **(Default)**    | - System Config path: **Site Configuration \>    |
|   Enables tapping links      |   File sharing and downloads**                   |
|   inside PDFs on mobile when | - `config.json` setting: `FileSettings` \>       |
|   Secure File Preview Mode   |   `MobileAllowPdfLinkNavigation` \> `true`       |
|   is active. Links will open | - Environment variable:                          |
|   in the device browser or   |   `MM_FILESETTINGS_MOBILEALLOWPDFLINKNAVIGATION` |
|   supported app.             |                                                  |
| - **false**: Disables link   |                                                  |
|   navigation in PDFs when    |                                                  |
|   Secure File Preview Mode   |                                                  |
|   is active.                 |                                                  |
+------------------------------+--------------------------------------------------+

:::: note
::: title
Note
:::

- Changing this configuration setting takes effect when mobile users
  restart their Mattermost mobile app or log out and log back in.
- This setting has no effect when the [Secure file preview on
  mobile](#enable-secure-file-preview-on-mobile) configuration setting
  is disabled.
::::

------------------------------------------------------------------------

## config.json-only settings

The following self-hosted deployment settings are only configurable in
the `config.json` file and are not available in the System Console.

### Disable Customer Portal requests

+--------------------------+-------------------------------------------+
| Enable or disable        | - System Config path: **N/A**             |
| customer portal          | - `config.json` setting: `CloudSettings`  |
| requests.                |   \> `Disable` \> `true,`                 |
|                          | - Environment variable:                   |
| - **true**:              |   `MM_CLOUDSETTINGS_DISABLE`              |
|   **(Default)**          |                                           |
|   Server-side requests   |                                           |
|   made to the customer   |                                           |
|   portal are disabled.   |                                           |
| - **false**: Server-side |                                           |
|   requests made to the   |                                           |
|   Mattermost Customer    |                                           |
|   Portal are enabled,    |                                           |
|   but will always fail   |                                           |
|   in air-gapped and      |                                           |
|   restricted deployment  |                                           |
|   environments.          |                                           |
+--------------------------+-------------------------------------------+

:::: note
::: title
Note
:::

Cloud admins can't modify this configuration setting.
::::

### Enable API team deletion

+------------------------------------------+----------------------------------------+
| Allow permanent team deletion via API.   | - System Config path: N/A              |
|                                          | - `config.json` setting:               |
| - **true**: Team and system admins (or   |   `ServiceSettings` \>                 |
|   users with appropriate permissions)    |   `EnableAPITeamDeletion` \> `false`   |
|   can call                               | - Environment variable: N/A            |
|   `api/v4/teams/{teamid}?permanent=true` |                                        |
|   or use `mmctl team delete` to          |                                        |
|   permanently delete a team.             |                                        |
| - **false**: **(Default)** Endpoint not  |                                        |
|   available; `api/v4/teams/{teamid}`     |                                        |
|   still soft deletes a team.             |                                        |
+------------------------------------------+----------------------------------------+

:::: note
::: title
Note
:::

This setting isn't available in the System Console and can only be set
in `config.json`.
::::

### Enable API user deletion

+------------------------------------------+----------------------------------------+
| Allow permanent user deletion via API.   | - System Config path: N/A              |
|                                          | - `config.json` setting:               |
| - **true**: System admins (or users with |   `ServiceSettings` \>                 |
|   appropriate permissions) can call      |   `EnableAPIUserDeletion` \> `false`   |
|   `api/v4/users/{userid}?permanent=true` | - Environment variable: N/A            |
|   or use `mmctl user delete` to          |                                        |
|   permanently delete a user.             |                                        |
| - **false**: **(Default)** Endpoint not  |                                        |
|   available; `api/v4/users/{userid}`     |                                        |
|   still soft deletes a user.             |                                        |
+------------------------------------------+----------------------------------------+

:::: note
::: title
Note
:::

This setting isn't available in the System Console and can only be set
in `config.json`.
::::

### Enable API channel deletion

+------------------------------------------------+----------------------------------------+
| Allow permanent channel deletion via API.      | - System Config path: N/A              |
|                                                | - `config.json` setting:               |
| - **true**: System admins (or users with       |   `ServiceSettings` \>                 |
|   appropriate permissions) can call            |   `EnableAPIChannelDeletion` \>        |
|   `api/v4/channels/{channelid}?permanent=true` |   `false`                              |
|   or use `mmctl channel delete` to permanently | - Environment variable: N/A            |
|   delete a channel.                            |                                        |
| - **false**: **(Default)** Endpoint not        |                                        |
|   available; `api/v4/channels/{channelid}`     |                                        |
|   still soft deletes a channel.                |                                        |
+------------------------------------------------+----------------------------------------+

:::: note
::: title
Note
:::

This setting isn't available in the System Console and can only be set
in `config.json`.
::::

### Enable desktop app developer mode

From Desktop App v5.10, this setting enables developer debugging options
available by going to the **View \> Developer Tools** menu in the
Mattermost desktop app.

This setting isn\'t available in the System Console and can only be
enabled in `config.json` by setting the environment variable
`MM_DESKTOP_DEVELOPER_MODE` to `true`. This setting is disabled by
default.

- **True**: Unlocks the following options in the Desktop App for the
  purposes of troubleshooting and debugging. You should only enable this
  setting if instructed to by a Mattermost developer:
  - **Browser Mode Only**: Completely disables the preload script and
    stops web app components from knowing they\'re in the desktop app.
    This option should be the best indicator of whether a web app
    component is causing performance and/or memory retention issues.
    This option disables notifications, cross-tab navigation,
    unread/mentions badges, the calls widget, and breaks resizing on
    macOS.
  - **Disable Notification Storage**: Turns off maps that hold
    references to unread notifications until they\'ve been selected &
    read. This option is good for debugging in cases where Mattermost is
    holding onto too many references to unused notifications.
  - **Disable User Activity Monitor**: Turns off the interval that
    checks whether the user is away or not. This option is good for
    debugging whether a user\'s availability status is causing
    unexpected desktop app behavior.
  - **Disable Context Menu**: Turns off the context menu attached to the
    BrowserViews. This option is good as a library santity check.
  - **Force Legacy Messaging API**: Forces the app to revert back to the
    old messaging API instead of the newer contextBridge API. This
    option is a good santity check to confirm whether the new API is
    responsible for holding onto memory.
  - **Force New Messaging API**: Forces the app to use the contextBridge
    API and completely disables the legacy one. This option forces off
    listeners for the legacy API.
- **False**: **(Default)** Developer debugging options are locked and
  unavailable in the Desktop App.

### Redis cache backend

From Mattermost v10.4, Mattermost Enterprise customers with self-hosted
deployments can configure [Redis](https://redis.io/) (Remote Dictionary
Server) as an alternative cache backend. Redis is an open-source,
in-memory data structure store that can be used as a database, cache,
and message broker. It supports various data structures and is a top
choice for its performance because its able to store data in memory and
provide very quick data access.

Using Redis as a caching solution can help ensure that Mattermost for
enterprise-level deployments with high concurrency and large user bases
remains performant and efficient, even under heavy usage.

Configure a Redis cache by editing the `config.json` file as described
in the following tables. Changes to configuration settings in this
section require a server restart before taking effect.

#### Cache type

+--------------------------+-------------------------------------------+
| Define the cache type.   | - System Config path: **N/A**             |
|                          | - `config.json` setting: `CacheSettings`  |
| - **lru**: **(Default)** |   \> `CacheType,` \> `lru`                |
|   Mattermost uses the    | - Environment variable:                   |
|   in-memory cache store. |   `MM_CACHESETTINGS_CACHETYPE`            |
| - **redis**: Mattermost  |                                           |
|   uses the configured    |                                           |
|   Redis cache store.     |                                           |
+--------------------------+-------------------------------------------+

#### Redis address

+--------------------------+-------------------------------------------+
| The hostname of the      | - System Config path: **N/A**             |
| Redis host.              | - `config.json` setting: `CacheSettings`  |
|                          |   \> `RedisAddress,`                      |
| String input.            | - Environment variable:                   |
|                          |   `MM_CACHESETTINGS_REDISADDRESS`         |
+--------------------------+-------------------------------------------+

#### Redis password

+--------------------------+-------------------------------------------+
| The password of the      | - System Config path: **N/A**             |
| Redis host.              | - `config.json` setting: `CacheSettings`  |
|                          |   \> `RedisPassword,`                     |
| String input. Leave      | - Environment variable:                   |
| blank if there is no     |   `MM_CACHESETTINGS_REDISPASSWORD`        |
| password.                |                                           |
+--------------------------+-------------------------------------------+

#### Redis database

+--------------------------+-------------------------------------------+
| The database of the      | - System Config path: **N/A**             |
| Redis host.              | - `config.json` setting: `CacheSettings`  |
|                          |   \> `RedisDB,`                           |
| Zero-indexed number up   | - Environment variable:                   |
| to 15. Typically set to  |   `MM_CACHESETTINGS_REDISDB`              |
| `0`. Redis allows a      |                                           |
| maximum of 16 databases. |                                           |
+--------------------------+-------------------------------------------+

#### Disable client cache

+------------------------+---------------------------------------------+
| Disables the           | - System Config path: **N/A**               |
| client-side cache of   | - `config.json` setting: `CacheSettings` \> |
| Redis.                 |   `DisableClientCache,` \> `false`          |
|                        | - Environment variable:                     |
| - **true**:            |   `MM_CACHESETTINGS_REDISDB`                |
|   Client-side cache of |                                             |
|   Redis is disabled.   |                                             |
|   Typically used as a  |                                             |
|   test option, and not |                                             |
|   in production        |                                             |
|   environments.        |                                             |
| - **false**:           |                                             |
|   **(Default)**        |                                             |
|   Client-side cache of |                                             |
|   Redis is enabled.    |                                             |
+------------------------+---------------------------------------------+

#### Redis cache prefix

+------------------------+---------------------------------------------+
| Adds a prefix to all   | - System Config path: **N/A**               |
| Redis cache keys.      | - `config.json` setting: `CacheSettings` \> |
|                        |   `RedisCachePrefix`                        |
|                        | - Environment variable:                     |
|                        |   `MM_CACHESETTINGS_REDISCACHEPREFIX`       |
+------------------------+---------------------------------------------+

:::: tip
::: title
Tip
:::

Adding a prefix to all Redis cache keys reduces key collisions,
simplifies debugging, isolates data, and provides a clear structure for
managing and scaling Redis-based systems. In environments where multiple
systems or tenants use the same Redis instance, prefixes become critical
for maintaining data integrity and operational efficiency.
::::

### Enable webhub channel iteration

+------------------------+-----------------------------------------------------+
| Control the            | - System Config path: **N/A**                       |
| performance of         | - `config.json` setting: `ServiceSettings` \>       |
| websocket broadcasting |   `EnableWebHubChannelIteration,` \> `false`        |
| in channels.           | - Environment variable:                             |
|                        |   `MM_SERVICESETTINGS_ENABLEWEBHUBCHANNELITERATION` |
| When enabled, improves |                                                     |
| websocket broadcasting |                                                     |
| performance; however,  |                                                     |
| performance may        |                                                     |
| decrease when users    |                                                     |
| join or leave a        |                                                     |
| channel.               |                                                     |
|                        |                                                     |
| Not recommended unless |                                                     |
| you have at least      |                                                     |
| 200,000 concurrent     |                                                     |
| users actively using   |                                                     |
| Mattermost.            |                                                     |
|                        |                                                     |
| Disabled by default.   |                                                     |
+------------------------+-----------------------------------------------------+

### Enable dedicated export filestore target

+-------------------------------------------------------------------------------------------------------+------------------------------------------+
| Enables the ability to specify an alternate filestore target for Mattermost                           | - System Config path: **N/A**            |
| `bulk exports </administration-guide/manage/bulk-export-tool>`{.interpreted-text role="doc"} and      | - `config.json` setting: `FileSettings`  |
| `compliance exports </administration-guide/comply/compliance-export>`{.interpreted-text role="doc"}.  |   \> `DedicatedExportStore`              |
|                                                                                                       | - Environment variable:                  |
| - **True**: A new `ExportFileBackend()` is generated under `FileSettings` using new configuration     |   `MM_FILESETTINGS_DEDICATEDEXPORTSTORE` |
|   values for the following configuration settings:                                                    |                                          |
|                                                                                                       |                                          |
| > - `ExportDriverName`                                                                                |                                          |
| > - `ExportDirectory`                                                                                 |                                          |
| > - `ExportAmazonS3AccessKeyId`                                                                       |                                          |
| > - `ExportAmazonS3SecretAccessKey`                                                                   |                                          |
| > - `ExportAmazonS3Bucket`                                                                            |                                          |
| > - `ExportAmazonS3PathPrefix`                                                                        |                                          |
| > - `ExportAmazonS3Region`                                                                            |                                          |
| > - `ExportAmazonS3Endpoint`                                                                          |                                          |
| > - `ExportAmazonS3SSL`                                                                               |                                          |
| > - `ExportAmazonS3SignV2`                                                                            |                                          |
| > - `ExportAmazonS3SSE`                                                                               |                                          |
| > - `ExportAmazonS3Trace`                                                                             |                                          |
| > - `ExportAmazonS3RequestTimeoutMilliseconds`                                                        |                                          |
| > - `ExportAmazonS3PresignExpiresSeconds`                                                             |                                          |
|                                                                                                       |                                          |
| - **False**: (**Default**) Standard `file storage                                                     |                                          |
|   <administration-guide/configure/environment-configuration-settings:file storage>`{.interpreted-text |                                          |
|   role="ref"} is used. Standard file storage will also be used when the configuration setting or      |                                          |
|   value is omitted.                                                                                   |                                          |
+-------------------------------------------------------------------------------------------------------+------------------------------------------+

:::: note
::: title
Note
:::

- When an alternate filestore target is configured, Mattermost Cloud
  admins can generate an S3 presigned URL for exports using the
  `/exportlink [job-id|zip file|latest]` slash command. See the
  `Mattermost data migration <administration-guide/manage/cloud-data-export:create the export>`{.interpreted-text
  role="ref"} documentation for details. Alternatively, Cloud and
  self-hosted admins can use the
  `mmctl export generate-presigned-url <administration-guide/manage/mmctl-command-line-tool:mmctl export generate-presigned-url>`{.interpreted-text
  role="ref"} command to generate a presigned URL directly from mmctl.
- Generating an S3 presigned URL requires the feature flag
  `EnableExportDirectDownload` to be set to `true`, the storage must be
  compatible with generating an S3 link, and this experimental
  configuration setting must be set to `true`. Presigned URLs for
  exports aren\'t supported for systems with shared storage.
::::
