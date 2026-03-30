# Source: https://tyk.io/docs/tyk-multi-data-centre/mdcb-configuration-options.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MDCB Configuration options

> Each of the config options that are available when deploying MDCB.

## Tyk MDCB Configuration

The Tyk MDCB server is configured primarily via the `tyk_sink.conf` file, this file resides in `/opt/tyk-sink` on most systems, but can also live anywhere and be directly targeted with the `-c` flag.

### Environment Variables

Environment variables (env var) can be used to override the settings defined in the configuration file. Where an environment variable is specified, its value will take precedence over the value in the configuration file.

### Environment Variable Type Mapping

When configuring Tyk components using environment variables, it's important to understand how different data types are represented. The type of each variable is based on its definition in the Go source code. This section provides a guide on how to format values for common data types.

| Go Type                  | Environment Variable Format                | Example                                                              |
| ------------------------ | ------------------------------------------ | -------------------------------------------------------------------- |
| `string`                 | A regular string of text.                  | `TYK_GW_SECRET="mysecret"`                                           |
| `int`, `int64`           | A whole number.                            | `TYK_GW_LISTENPORT=8080`                                             |
| `bool`                   | `true` or `false`.                         | `TYK_GW_USEDBAPPCONFIG=true`                                         |
| `[]string`               | A comma-separated list of strings.         | `TYK_PMP_PUMPS_STDOUT_FILTERS_SKIPPEDAPIIDS="api1,api2,api3"`        |
| `map[string]string`      | A comma-separated list of key:value pairs. | `TYK_GW_GLOBALHEADERS="X-Tyk-Test:true,X-Tyk-Version:1.0"`           |
| `map[string]interface{}` | A JSON string representing the object.     | `TYK_GW_POLICIES_POLICYSOURCE_CONFIG='{"connection_string": "..."}'` |

<Note>
  For complex types like `map[string]interface{}`, the value should be a valid JSON string. For `[]string` and `map[string]string`, ensure there are no spaces around the commas unless they are part of the value itself.
</Note>

### Default Ports

| Application         | Port  |
| :------------------ | :---- |
| MongoDB             | 27017 |
| Redis               | 6379  |
| **Tyk Dashboard**   |       |
| Developer Portal    | 3000  |
| Admin Dashboard     | 3000  |
| Admin Dashboard API | 3000  |
| **Tyk Gateway**     |       |
| Management API      | 8080  |
| **MDCB**            |       |
| RPC services        | 9090  |
| HTTP endpoints      | 8181  |

### listen\_port

ENV: <b>TYK\_MDCB\_LISTENPORT</b><br />
Type: `int`<br />

The rpc port which worker gateways will connect to. Open this port to accept connections via your firewall.<br />If this value is not set, the MDCB application will apply a default value of 9091.

### healthcheck\_port

ENV: <b>TYK\_MDCB\_HEALTHCHECKPORT</b><br />
Type: `int`<br />

This port lets MDCB allow standard health checks.<br />If this value is not set, the MDCB component will apply a default value of 8181.
Deprecated: Use `http_port` instead.

### healthcheck

Healthcheck settings

### healthcheck.cache\_renewal\_period

ENV: <b>TYK\_MDCB\_HEALTHCHECK\_CACHERENEWALPERIOD</b><br />
Type: `int`<br />

Specifies the time interval (in seconds) at which the healthchecker refreshes its cached health status information (redis and DB).

### http\_port

ENV: <b>TYK\_MDCB\_HTTPPORT</b><br />
Type: `int`<br />

The HTTP port exposes different endpoints for monitoring and debugging MDCB. The default value is 8181.
Exposed endpoints include:

* /health - Provides the health status of MDCB.
* /dataplanes - Provides information about the dataplanes connected to MDCB (`security.enable_http_secure_endpoints` must be enabled).
* /debug/pprof/\* - Provides profiling information (`enable_http_profiler` must be enabled).

### enable\_http\_profiler

ENV: <b>TYK\_MDCB\_HTTPPROFILE</b><br />
Type: `bool`<br />

Enable debugging of your Tyk MDCB by exposing profiling information.

### server\_options

MDCB gorpc server configuration

### server\_options.use\_ssl

ENV: <b>TYK\_MDCB\_SERVEROPTIONS\_USESSL</b><br />
Type: `bool`<br />

If use\_ssl is set to true, you need to enter the cert\_file and key\_file path names for certificate.

### server\_options.certificate

cert data to expose the http server

### server\_options.certificate.cert\_file

ENV: <b>TYK\_MDCB\_SERVEROPTIONS\_CERTIFICATE\_CERTFILE</b><br />
Type: `string`<br />

Filesystem location for pem encoded certificate

### server\_options.certificate.key\_file

ENV: <b>TYK\_MDCB\_SERVEROPTIONS\_CERTIFICATE\_KEYFILE</b><br />
Type: `string`<br />

Filesystem location for pem encoded private key

### server\_options.min\_version

ENV: <b>TYK\_MDCB\_SERVEROPTIONS\_MINVERSION</b><br />
Type: `uint16`<br />

The `min_version` setting should be the minimum TLS protocol version required from the client.<br /> For TLS 1.0 use 769<br />For TLS 1.1 use 770<br />For TLS 1.2 use 771<br />For TLS 1.3 use 772

### server\_options.ssl\_ciphers

ENV: <b>TYK\_MDCB\_SERVEROPTIONS\_CIPHERS</b><br />
Type: `[]string`<br />

Is the list of names supported cipher suites (IANA) for TLS versions up to TLS 1.2. This defaults to a list of secure cipher suites.

### server\_options.ssl\_certificates

ENV: <b>TYK\_MDCB\_SERVEROPTIONS\_SSLCERTIFICATES</b><br />
Type: `[]string`<br />

SSL certificates used by your MDCB server. A list of certificate IDs or path to files.

### http\_server\_options

HTTPServerOptions configures SSL/TLS for the HTTP server, affecting security settings.
It applies to endpoints like /health for health checks, /dataplanes for node information
and /debug/pprof/ for performance profiling.

### http\_server\_options.use\_ssl

ENV: <b>TYK\_MDCB\_HTTPSERVEROPTIONS\_USESSL</b><br />
Type: `bool`<br />

If use\_ssl is set to true, you need to enter the cert\_file and key\_file path names for certificate.

### http\_server\_options.certificate

cert data to expose the http server

### http\_server\_options.certificate.cert\_file

ENV: <b>TYK\_MDCB\_HTTPSERVEROPTIONS\_CERTIFICATE\_CERTFILE</b><br />
Type: `string`<br />

Filesystem location for pem encoded certificate

### http\_server\_options.certificate.key\_file

ENV: <b>TYK\_MDCB\_HTTPSERVEROPTIONS\_CERTIFICATE\_KEYFILE</b><br />
Type: `string`<br />

Filesystem location for pem encoded private key

### http\_server\_options.min\_version

ENV: <b>TYK\_MDCB\_HTTPSERVEROPTIONS\_MINVERSION</b><br />
Type: `uint16`<br />

The `min_version` setting should be the minimum TLS protocol version required from the client.<br /> For TLS 1.0 use 769<br />For TLS 1.1 use 770<br />For TLS 1.2 use 771<br />For TLS 1.3 use 772

### http\_server\_options.ssl\_ciphers

ENV: <b>TYK\_MDCB\_HTTPSERVEROPTIONS\_CIPHERS</b><br />
Type: `[]string`<br />

Is the list of names supported cipher suites (IANA) for TLS versions up to TLS 1.2. This defaults to a list of secure cipher suites.

### http\_server\_options.ssl\_certificates

ENV: <b>TYK\_MDCB\_HTTPSERVEROPTIONS\_SSLCERTIFICATES</b><br />
Type: `[]string`<br />

SSL certificates used by your MDCB server. A list of certificate IDs or path to files.

### security.private\_certificate\_encoding\_secret

ENV: <b>TYK\_MDCB\_SECURITY\_PRIVATECERTIFICATEENCODINGSECRET</b><br />
Type: `string`<br />

Allows MDCB to use Mutual TLS. This requires to set `server_options.use_ssl` to true. See [Mutual TLS](/basic-config-and-security/security/mutual-tls/client-mtls) for more details.

### storage

This section describes your centralised Redis DB. This will act as your main key store for all of your clusters.

### storage.type

ENV: <b>TYK\_MDCB\_STORAGE\_TYPE</b><br />
Type: `string`<br />

Currently, the only storage type supported is Redis.

### storage.host

ENV: <b>TYK\_MDCB\_STORAGE\_HOST</b><br />
Type: `string`<br />

Hostname of your Redis server

### storage.port

ENV: <b>TYK\_MDCB\_STORAGE\_PORT</b><br />
Type: `int`<br />

The port the Redis server is listening on.

### storage.master\_name

ENV: <b>TYK\_MDCB\_STORAGE\_MASTERNAME</b><br />
Type: `string`<br />

It defines the sentinel master name

### storage.sentinel\_password

ENV: <b>TYK\_MDCB\_STORAGE\_SENTINELPASSWORD</b><br />
Type: `string`<br />

If set, redis sentinel will authenticate using this password.

### storage.username

ENV: <b>TYK\_MDCB\_STORAGE\_USERNAME</b><br />
Type: `string`<br />

If set, a redis connection will be established with this user. If not set then it will defaults to the default redis user

### storage.password

ENV: <b>TYK\_MDCB\_STORAGE\_PASSWORD</b><br />
Type: `string`<br />

Optional auth password for Redis db

### storage.database

ENV: <b>TYK\_MDCB\_STORAGE\_DATABASE</b><br />
Type: `int`<br />

By default, the database is 0. Setting the database is not supported with redis cluster. As such, if you have `storage.redis_cluster:true`, then this value should be omitted or explicitly set to 0.

### storage.optimisation\_max\_idle

ENV: <b>TYK\_MDCB\_STORAGE\_MAXIDLE</b><br />
Type: `int`<br />

MDCB will open a pool of connections to Redis. This setting will configure how many connections are maintained in the pool when idle (no traffic). Set the `max_idle` value to something large, we usually leave it at around 2000 for HA deployments.

### storage.optimisation\_max\_active

ENV: <b>TYK\_MDCB\_STORAGE\_MAXACTIVE</b><br />
Type: `int`<br />

In order to not over commit connections to the Redis server, we may limit the total number of active connections to Redis. We recommend for production use to set this to around 4000.

### storage.enable\_cluster

ENV: <b>TYK\_MDCB\_STORAGE\_ENABLECLUSTER</b><br />
Type: `bool`<br />

If you are using Redis cluster, enable it here to enable the slots mode.

### storage.hosts

ENV: <b>TYK\_MDCB\_STORAGE\_HOSTS</b><br />
Type: `map[string]string`<br />

Add your Redis hosts here as a map of hostname:port. This field is required when storage.enable\_cluster is set to true. example:<br />`{`<br />  `"server1": "6379",`<br />  `"server2": "6380",`<br />  `"server3": "6381"`<br />`}`

### storage.addrs

ENV: <b>TYK\_MDCB\_STORAGE\_ADDRS</b><br />
Type: `[]string`<br />

It can be either a single address or a seed list of host:port addresses of cluster/sentinel nodes. It overrides the value of hosts.

### storage.redis\_use\_ssl

ENV: <b>TYK\_MDCB\_STORAGE\_REDISUSESSL</b><br />
Type: `bool`<br />

If set, MDCB will assume the connection to Redis is encrypted. (use with Redis providers that support in-transit encryption).
Deprecated. Use `use_ssl` instead.

### storage.redis\_ssl\_insecure\_skip\_verify

ENV: <b>TYK\_MDCB\_STORAGE\_REDISSSLINSECURESKIPVERIFY</b><br />
Type: `bool`<br />

Allows usage of self-signed certificates when connecting to an encrypted Redis database.
Deprecated. Use `ssl_insecure_skip_verify` instead.

### storage.timeout

ENV: <b>TYK\_MDCB\_STORAGE\_TIMEOUT</b><br />
Type: `int`<br />

Set a custom timeout for Redis network operations. Default value is 5 seconds.

### storage.use\_ssl

ENV: <b>TYK\_MDCB\_STORAGE\_USESSL</b><br />
Type: `bool`<br />

Enable SSL/TLS connection between Tyk MDCB & Redis.

### storage.ssl\_insecure\_skip\_verify

ENV: <b>TYK\_MDCB\_STORAGE\_SSLINSECURESKIPVERIFY</b><br />
Type: `bool`<br />

Disable TLS verification.

### storage.ca\_file

ENV: <b>TYK\_MDCB\_STORAGE\_CAFILE</b><br />
Type: `string`<br />

Path to the CA file.

### storage.cert\_file

ENV: <b>TYK\_MDCB\_STORAGE\_CERTFILE</b><br />
Type: `string`<br />

Path to the cert file.

### storage.key\_file

ENV: <b>TYK\_MDCB\_STORAGE\_KEYFILE</b><br />
Type: `string`<br />

Path to the key file.

### storage.max\_version

ENV: <b>TYK\_MDCB\_STORAGE\_MAXVERSION</b><br />
Type: `string`<br />

Maximum TLS version that is supported.
Options: \["1.0", "1.1", "1.2", "1.3"].
Defaults to "1.3".

### storage.min\_version

ENV: <b>TYK\_MDCB\_STORAGE\_MINVERSION</b><br />
Type: `string`<br />

Minimum TLS version that is supported.
Options: \["1.0", "1.1", "1.2", "1.3"].
Defaults to "1.2".

### analytics

configuration of the store of analytics

### analytics.type

ENV: <b>TYK\_MDCB\_ANALYTICSCONFIG\_TYPE</b><br />
Type: `DBType`<br />

Determines the storage type. It could be `mongo` or `postgres`. By default, the value is `mongo`.

### analytics.connection\_string

ENV: <b>TYK\_MDCB\_ANALYTICSCONFIG\_CONNECTIONSTRING</b><br />
Type: `string`<br />

This is used to configure the conenction string for the storage.

### analytics.table\_sharding

ENV: <b>TYK\_MDCB\_ANALYTICSCONFIG\_TABLESHARDING</b><br />
Type: `bool`<br />

Enable table sharding for SQL Analytics

### analytics.batch\_size

ENV: <b>TYK\_MDCB\_ANALYTICSCONFIG\_BATCHSIZE</b><br />
Type: `int`<br />

Max Batch size for SQL Analytics

### analytics.postgres.prefer\_simple\_protocol

ENV: <b>TYK\_MDCB\_ANALYTICSCONFIG\_POSTGRES\_PREFERSIMPLEPROTOCOL</b><br />
Type: `bool`<br />

disables implicit prepared statement usage

### analytics.mysql.default\_string\_size

ENV: <b>TYK\_MDCB\_ANALYTICSCONFIG\_MYSQL\_DEFAULTSTRINGSIZE</b><br />
Type: `uint`<br />

default size for string fields. By default set to: 256

### analytics.mysql.disable\_datetime\_precision

ENV: <b>TYK\_MDCB\_ANALYTICSCONFIG\_MYSQL\_DISABLEDATETIMEPRECISION</b><br />
Type: `bool`<br />

disable datetime precision, which not supported before MySQL 5.6

### analytics.mysql.dont\_support\_rename\_index

ENV: <b>TYK\_MDCB\_ANALYTICSCONFIG\_MYSQL\_DONTSUPPORTRENAMEINDEX</b><br />
Type: `bool`<br />

drop & create when rename index, rename index not supported before MySQL 5.7, MariaDB

### analytics.mysql.dont\_support\_rename\_column

ENV: <b>TYK\_MDCB\_ANALYTICSCONFIG\_MYSQL\_DONTSUPPORTRENAMECOLUMN</b><br />
Type: `bool`<br />

`change` when rename column, rename column not supported before MySQL 8, MariaDB

### analytics.mysql.skip\_initialize\_with\_version

ENV: <b>TYK\_MDCB\_ANALYTICSCONFIG\_MYSQL\_SKIPINITIALIZEWITHVERSION</b><br />
Type: `bool`<br />

auto configure based on currently MySQL version

### analytics.mongo\_url

ENV: <b>TYK\_MDCB\_ANALYTICSCONFIG\_MONGOURL</b><br />
Type: `string`<br />

Connection string for MongoDB.

### analytics.mongo\_use\_ssl

ENV: <b>TYK\_MDCB\_ANALYTICSCONFIG\_MONGOUSESSL</b><br />
Type: `bool`<br />

A Boolean setting for Mongo SSL support. Set to true to enable SSL.

### analytics.mongo\_ssl\_insecure\_skip\_verify

ENV: <b>TYK\_MDCB\_ANALYTICSCONFIG\_MONGOSSLINSECURESKIPVERIFY</b><br />
Type: `bool`<br />

This setting allows the use of self-signed certificates when connecting to an encrypted MongoDB database.

### analytics.mongo\_ssl\_allow\_invalid\_hostnames

ENV: <b>TYK\_MDCB\_ANALYTICSCONFIG\_MONGOSSLALLOWINVALIDHOSTNAMES</b><br />
Type: `bool`<br />

Ignore hostname check when it differs from the original (for example with SSH tunneling). The rest of the TLS verification will still be performed

### analytics.mongo\_ssl\_ca\_file

ENV: <b>TYK\_MDCB\_ANALYTICSCONFIG\_MONGOSSLCAFILE</b><br />
Type: `string`<br />

Path to the PEM file with trusted root certificates

### analytics.mongo\_ssl\_pem\_keyfile

ENV: <b>TYK\_MDCB\_ANALYTICSCONFIG\_MONGOSSLPEMKEYFILE</b><br />
Type: `string`<br />

Path to the PEM file which contains both client certificate and private key. This is required for Mutual TLS.

### analytics.mongo\_session\_consistency

ENV: <b>TYK\_MDCB\_ANALYTICSCONFIG\_MONGOSESSIONCONSISTENCY</b><br />
Type: `string`<br />

Set the consistency mode for the session, it defaults to `Strong`. The valid values are:

* eventual
  monotonic

### analytics.mongo\_batch\_size

ENV: <b>TYK\_MDCB\_ANALYTICSCONFIG\_MONGOBATCHSIZE</b><br />
Type: `int`<br />

Sets the batch size for mongo results.

### analytics.driver

ENV: <b>TYK\_MDCB\_ANALYTICSCONFIG\_DRIVER</b><br />
Type: `string`<br />

Use `mongo-go` to use the official mongo driver. Alternatively, use `mgo` to use the old driver.
Since v2.4.3, the default driver is `mongo-go`.

### analytics.mongo\_direct\_connection

ENV: <b>TYK\_MDCB\_ANALYTICSCONFIG\_MONGODIRECTCONNECTION</b><br />
Type: `bool`<br />

MongoDirectConnection informs whether to establish connections only with the specified seed servers,
or to discover and establish connections with further servers within the cluster.
If true, the client will only connect to the host provided in the ConnectionString
and won't attempt to discover other servers within the cluster. Useful when network
restrictions prevent discovery, such as with SSH tunneling. Default is false.

### hash\_keys

ENV: <b>TYK\_MDCB\_HASHKEYS</b><br />
Type: `bool`<br />

Set to true if you are using a hashed configuration installation of Tyk, otherwise set to false.

### session\_timeout

ENV: <b>TYK\_MDCB\_SESSIONTIMEOUT</b><br />
Type: `int64`<br />

Number of seconds before the gateways are forced to re-login. Default is 86400 (24 hours).

### forward\_analytics\_to\_pump

ENV: <b>TYK\_MDCB\_FORWARDANALYTICSTOPUMP</b><br />
Type: `bool`<br />

Instead of sending analytics directly to MongoDB, MDCB can send analytics to Redis. This will allow \[tyk-pump] ([https://github.com/TykTechnologies/tyk-pump](https://github.com/TykTechnologies/tyk-pump)) to pull analytics from Redis and send to your own data sinks.

### enable\_multiple\_analytics\_keys

ENV: <b>TYK\_MDCB\_ENABLEMULTIPLEANALYTICSKEYS</b><br />
Type: `bool`<br />

Instead of saving all the analytics in one key, this will enable to save the analytics in multiple keys. It's specially useful when you are using Redis cluster. This will work only if `forward_analytics_to_pump` is true and tyk-pump is v1.2.1+ .

### dont\_store\_selective

ENV: <b>TYK\_MDCB\_DONTSTORESELECTIVE</b><br />
Type: `bool`<br />

set to true if you don't want to store selective analytics

### dont\_store\_aggregate

ENV: <b>TYK\_MDCB\_DONTSTOREAGGREGATES</b><br />
Type: `bool`<br />

Set to true to don't store aggregate analytics

### org\_session\_expiration

ENV: <b>TYK\_MDCB\_ORGCACHEEXPIRATION</b><br />
Type: `int`<br />

Sets the organization cache expiration in minutes. By default, 60 minutes. This will only work with tyk-sink 1.9+

### org\_session\_cleanup

ENV: <b>TYK\_MDCB\_ORGCACHECLEANUP</b><br />
Type: `int`<br />

Sets the organization cache cleanup interval in minutes. By default, 60 minutes. This will only work with tyk-sink 1.9+.

### license

ENV: <b>TYK\_MDCB\_LICENSE</b><br />
Type: `string`<br />

Enter your license in this section so MDCB can start.

### track\_all\_paths

ENV: <b>TYK\_MDCB\_TRACKALLPATHS</b><br />
Type: `bool`<br />

Currently, analytics for an endpoint is stored only if Track Endpoint plugin is enabled on that endpoint. If `track_all_paths` is enabled, it will store analytics for all the endpoints, irrespective of Track Endpoint plugin.

### store\_analytics\_per\_minute

ENV: <b>TYK\_MDCB\_STOREANALYTICSPERMINUTE</b><br />
Type: `bool`<br />

Enable to generate aggregated per minute. By default it will generate aggregate data per hour. If this option is enabled, aggregate data will be generated per minute.

### ignore\_tag\_prefix\_list

ENV: <b>TYK\_MDCB\_IGNORETAGPREFIXLIST</b><br />
Type: `[]string`<br />

if set to true then it will not store analytics for tags having prefix specified in the list. **Note**: Prefix “key-” is added in the list by default. This tag is added by gateway for keys.

### threshold\_len\_tag\_list

ENV: <b>TYK\_MDCB\_THRESHOLDLENTAGLIST</b><br />
Type: `int`<br />

If number of tags in a document grows beyond `threshold_len_tag_list`, pump will throw a warning, it works for mongo aggregate pump. The warning will print top 5 common tag prefix. Default value is 1000. To disable alerts set it to -1.

### omit\_analytics\_index\_creation

ENV: <b>TYK\_MDCB\_OMITANALYTICSINDEXCREATION</b><br />
Type: `bool`<br />

Set to true to disable the Mongo storages default index creation. More detailed behavior explained at [https://tyk.io/docs/tyk-pump/tyk-pump-configuration/tyk-pump-dashboard-config/#omitting-indexes](https://tyk.io/docs/tyk-pump/tyk-pump-configuration/tyk-pump-dashboard-config/#omitting-indexes).

### enable\_separate\_analytics\_store

ENV: <b>TYK\_MDCB\_ENABLESEPERATEANALYTICSSTORE</b><br />
Type: `bool`<br />

Set it to true if you are using a separated analytic storage in the Control Plane Gateway. If `forward_analytics_to_pump` is true, it will forward the analytics to the separated storage specified in `analytics_storage`.

### analytics\_storage

This section describes your separated analytic Redis DB. It has the same fields as `storage`. It requires `enable_separate_analytics_store` set to true.

### analytics\_storage.type

ENV: <b>TYK\_MDCB\_ANALYTICSSTORAGE\_TYPE</b><br />
Type: `string`<br />

Currently, the only storage type supported is Redis.

### analytics\_storage.host

ENV: <b>TYK\_MDCB\_ANALYTICSSTORAGE\_HOST</b><br />
Type: `string`<br />

Hostname of your Redis server

### analytics\_storage.port

ENV: <b>TYK\_MDCB\_ANALYTICSSTORAGE\_PORT</b><br />
Type: `int`<br />

The port the Redis server is listening on.

### analytics\_storage.master\_name

ENV: <b>TYK\_MDCB\_ANALYTICSSTORAGE\_MASTERNAME</b><br />
Type: `string`<br />

It defines the sentinel master name

### analytics\_storage.sentinel\_password

ENV: <b>TYK\_MDCB\_ANALYTICSSTORAGE\_SENTINELPASSWORD</b><br />
Type: `string`<br />

If set, redis sentinel will authenticate using this password.

### analytics\_storage.username

ENV: <b>TYK\_MDCB\_ANALYTICSSTORAGE\_USERNAME</b><br />
Type: `string`<br />

If set, a redis connection will be established with this user. If not set then it will defaults to the default redis user

### analytics\_storage.password

ENV: <b>TYK\_MDCB\_ANALYTICSSTORAGE\_PASSWORD</b><br />
Type: `string`<br />

Optional auth password for Redis db

### analytics\_storage.database

ENV: <b>TYK\_MDCB\_ANALYTICSSTORAGE\_DATABASE</b><br />
Type: `int`<br />

By default, the database is 0. Setting the database is not supported with redis cluster. As such, if you have `storage.redis_cluster:true`, then this value should be omitted or explicitly set to 0.

### analytics\_storage.optimisation\_max\_idle

ENV: <b>TYK\_MDCB\_ANALYTICSSTORAGE\_MAXIDLE</b><br />
Type: `int`<br />

MDCB will open a pool of connections to Redis. This setting will configure how many connections are maintained in the pool when idle (no traffic). Set the `max_idle` value to something large, we usually leave it at around 2000 for HA deployments.

### analytics\_storage.optimisation\_max\_active

ENV: <b>TYK\_MDCB\_ANALYTICSSTORAGE\_MAXACTIVE</b><br />
Type: `int`<br />

In order to not over commit connections to the Redis server, we may limit the total number of active connections to Redis. We recommend for production use to set this to around 4000.

### analytics\_storage.enable\_cluster

ENV: <b>TYK\_MDCB\_ANALYTICSSTORAGE\_ENABLECLUSTER</b><br />
Type: `bool`<br />

If you are using Redis cluster, enable it here to enable the slots mode.

### analytics\_storage.hosts

ENV: <b>TYK\_MDCB\_ANALYTICSSTORAGE\_HOSTS</b><br />
Type: `map[string]string`<br />

Add your Redis hosts here as a map of hostname:port. This field is required when storage.enable\_cluster is set to true. example:<br />`{`<br />  `"server1": "6379",`<br />  `"server2": "6380",`<br />  `"server3": "6381"`<br />`}`

### analytics\_storage.addrs

ENV: <b>TYK\_MDCB\_ANALYTICSSTORAGE\_ADDRS</b><br />
Type: `[]string`<br />

It can be either a single address or a seed list of host:port addresses of cluster/sentinel nodes. It overrides the value of hosts.

### analytics\_storage.redis\_use\_ssl

ENV: <b>TYK\_MDCB\_ANALYTICSSTORAGE\_REDISUSESSL</b><br />
Type: `bool`<br />

If set, MDCB will assume the connection to Redis is encrypted. (use with Redis providers that support in-transit encryption).
Deprecated. Use `use_ssl` instead.

### analytics\_storage.redis\_ssl\_insecure\_skip\_verify

ENV: <b>TYK\_MDCB\_ANALYTICSSTORAGE\_REDISSSLINSECURESKIPVERIFY</b><br />
Type: `bool`<br />

Allows usage of self-signed certificates when connecting to an encrypted Redis database.
Deprecated. Use `ssl_insecure_skip_verify` instead.

### analytics\_storage.timeout

ENV: <b>TYK\_MDCB\_ANALYTICSSTORAGE\_TIMEOUT</b><br />
Type: `int`<br />

Set a custom timeout for Redis network operations. Default value is 5 seconds.

### analytics\_storage.use\_ssl

ENV: <b>TYK\_MDCB\_ANALYTICSSTORAGE\_USESSL</b><br />
Type: `bool`<br />

Enable SSL/TLS connection between Tyk MDCB & Redis.

### analytics\_storage.ssl\_insecure\_skip\_verify

ENV: <b>TYK\_MDCB\_ANALYTICSSTORAGE\_SSLINSECURESKIPVERIFY</b><br />
Type: `bool`<br />

Disable TLS verification.

### analytics\_storage.ca\_file

ENV: <b>TYK\_MDCB\_ANALYTICSSTORAGE\_CAFILE</b><br />
Type: `string`<br />

Path to the CA file.

### analytics\_storage.cert\_file

ENV: <b>TYK\_MDCB\_ANALYTICSSTORAGE\_CERTFILE</b><br />
Type: `string`<br />

Path to the cert file.

### analytics\_storage.key\_file

ENV: <b>TYK\_MDCB\_ANALYTICSSTORAGE\_KEYFILE</b><br />
Type: `string`<br />

Path to the key file.

### analytics\_storage.max\_version

ENV: <b>TYK\_MDCB\_ANALYTICSSTORAGE\_MAXVERSION</b><br />
Type: `string`<br />

Maximum TLS version that is supported.
Options: \["1.0", "1.1", "1.2", "1.3"].
Defaults to "1.3".

### analytics\_storage.min\_version

ENV: <b>TYK\_MDCB\_ANALYTICSSTORAGE\_MINVERSION</b><br />
Type: `string`<br />

Minimum TLS version that is supported.
Options: \["1.0", "1.1", "1.2", "1.3"].
Defaults to "1.2".

### log\_level

ENV: <b>TYK\_MDCB\_LOGLEVEL</b><br />
Type: `string`<br />

You can now set a logging level (log\_level). The following levels can be set: debug, info, warn, error.
If not set or left empty, it will default to `info`.

### enable\_key\_logging

ENV: <b>TYK\_MDCB\_ENABLEKEYLOGGING</b><br />
Type: `bool`<br />

EnableKeyLogging prints the unhashed keys without obfuscating them in the logs

### sync\_worker\_config

Configuration of the MDCB Synchroniser functionality introduced in MDCB v2.0.0

### sync\_worker\_config.enabled

ENV: <b>TYK\_MDCB\_SYNCWORKER\_ENABLED</b><br />
Type: `bool`<br />

Enable the MDCB Synchroniser

### sync\_worker\_config.hash\_keys

ENV: <b>TYK\_MDCB\_SYNCWORKER\_HASHKEYS</b><br />
Type: `bool`<br />

Allows the worker to synchronize hashed API keys. Set this to true if `hash_keys` is true in dashboard and gateway configuration.

### sync\_worker\_config.max\_batch\_size

ENV: <b>TYK\_MDCB\_SYNCWORKER\_MAXBATCHSIZE</b><br />
Type: `int`<br />

The maximum number of keys that we can fetch per batch. Default value: 1000 keys per batch.

### sync\_worker\_config.time\_between\_batches

ENV: <b>TYK\_MDCB\_SYNCWORKER\_TIMEBETWEENBATCHES</b><br />
Type: `int`<br />

Specifies a cooldown time between batches in seconds. 0 / disabled by default.

### sync\_worker\_config.max\_workers

ENV: <b>TYK\_MDCB\_SYNCWORKER\_MAXWORKERS</b><br />
Type: `int`<br />

Specifies the maximum number of Groups (worker GW clusters) that can be synchronised by MDCB at the same time. Increasing this value can affect the operation of MDCB so it is recommended that you only modify this value if you need to synchronise a higher number of datacenters. Default value: 1000.

### sync\_worker\_config.warmup\_time

ENV: <b>TYK\_MDCB\_SYNCWORKER\_WARMUPTIME</b><br />
Type: `int`<br />

Specifies the time (in seconds) that MDCB should wait before starting to synchronise workers with the controller. This is to allow the worker nodes to load APIs and policies from local Redis before synchronising the other resources. Default value: 2 seconds.

### sync\_worker\_config.group\_key\_ttl

ENV: <b>TYK\_MDCB\_SYNCWORKER\_GROUPKEYTTL</b><br />
Type: `int`<br />

Specifies the group key TTL in seconds. This key is used to prevent a group of gateways from re-syncing when is not required. On login (GroupLogin call), if the key doesn't exist then the sync process is triggered. If the key exists then the TTL just gets renewed. In case the cluster of gateways is down, the key will expire and get removed and if they connect again a sync process will be triggered. Default value: 180 seconds. Min value: 30 seconds.

### enable\_ownership

ENV: <b>TYK\_MDCB\_ENABLEOWNERSHIP</b><br />
Type: `bool`<br />

Enables [API Ownership](/api-management/user-management#enabling-api-ownership) in MDCB. It allows the gateways in the data plane cluster to load only APIs that are accessible by the user and user group associated with the `slave_options.api_key` that is used to connect to MDCB (defined in `tyk.config` of the gateway).
This will be enforced if `enable_ownership` is also enabled in the Dashboard and your API definition has been associated with a user or user\_group
Defaults to `false`.

### escape\_dots\_in\_oas\_paths

ENV: <b>TYK\_MDCB\_ESCAPEDOTSINOASPATHS</b><br />
Type: `bool`<br />

When enabled, dots in OAS field names will be escaped (to \u002e ) and unescaped when required for compatibility with specific databases.
Defaults to `false`.

Built with [Mintlify](https://mintlify.com).
