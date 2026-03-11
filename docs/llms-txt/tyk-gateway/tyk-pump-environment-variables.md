# Source: https://tyk.io/docs/tyk-pump/tyk-pump-configuration/tyk-pump-environment-variables.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tyk Pump Environment Variables

> Using Environment Variables to configure your Tyk Pump

export const HOST_0 = undefined

export const PORT_0 = undefined

You can use environment variables to override the config file for the Tyk Pump. Environment variables are created from the dot notation versions of the JSON objects contained with the config files.
To understand how the environment variables notation works, see [Environment Variables](/tyk-oss-gateway/configuration).

All the Pump environment variables have the prefix `TYK_PMP_`. The environment variables will take precedence over the values in the configuration file.

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

### purge\_chunk

ENV: <b>TYK\_PMP\_PURGECHUNK</b><br />
Type: `int64`<br />

The maximum number of records to pull from Redis at a time. If it's unset or `0`, all the
analytics records in Redis are pulled. If it's set, `storage_expiration_time` is used to
reset the analytics record TTL.

### storage\_expiration\_time

ENV: <b>TYK\_PMP\_STORAGEEXPIRATIONTIME</b><br />
Type: `int64`<br />

The number of seconds for the analytics records TTL. It only works if `purge_chunk` is
enabled. Defaults to `60` seconds.

### uptime\_pump\_config

Example Uptime Pump configuration:

````{.json}  theme={null}
"uptime_pump_config": {
  "uptime_type": "mongo",
  "mongo_url": "mongodb://localhost:27017",
  "collection_name": "tyk_uptime_analytics"
},

### SQL Uptime Pump
*Supported in Tyk Pump v1.5.0+*

In `uptime_pump_config` you can configure a SQL uptime pump. To do that, you need to add the
field `uptime_type` with `sql` value. You can also use different types of SQL Uptime pumps,
like `postgres` using the `type` field.

An example of a SQL Postgres uptime pump would be:
```{.json}
"uptime_pump_config": {
    "uptime_type": "sql",
    "type": "postgres",
    "connection_string": "host=sql_host port=sql_port user=sql_usr dbname=dbname password=sql_pw",
    "table_sharding": false
},
````

Take into account that you can also set `log_level` field into the `uptime_pump_config` to `debug`,
`info` or `warning`. By default, the SQL logger verbosity is `silent`.

### uptime\_pump\_config.EnvPrefix

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_ENVPREFIX</b><br />
Type: `string`<br />

The prefix for the environment variables that will be used to override the configuration.
Defaults to `TYK_PMP_PUMPS_SQL_META`

### uptime\_pump\_config.mongo\_url

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_MONGOURL</b><br />
Type: `string`<br />

The full URL to your MongoDB instance, this can be a clustered instance if necessary and
should include the database and username / password data.

### uptime\_pump\_config.mongo\_use\_ssl

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_MONGOUSESSL</b><br />
Type: `bool`<br />

Set to true to enable Mongo SSL connection.

### uptime\_pump\_config.mongo\_ssl\_insecure\_skip\_verify

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_MONGOSSLINSECURESKIPVERIFY</b><br />
Type: `bool`<br />

Allows the use of self-signed certificates when connecting to an encrypted MongoDB database.

### uptime\_pump\_config.mongo\_ssl\_allow\_invalid\_hostnames

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_MONGOSSLALLOWINVALIDHOSTNAMES</b><br />
Type: `bool`<br />

Ignore hostname check when it differs from the original (for example with SSH tunneling).
The rest of the TLS verification will still be performed.

### uptime\_pump\_config.mongo\_ssl\_ca\_file

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_MONGOSSLCAFILE</b><br />
Type: `string`<br />

Path to the PEM file with trusted root certificates

### uptime\_pump\_config.mongo\_ssl\_pem\_keyfile

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_MONGOSSLPEMKEYFILE</b><br />
Type: `string`<br />

Path to the PEM file which contains both client certificate and private key. This is
required for Mutual TLS.

### uptime\_pump\_config.mongo\_db\_type

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_MONGODBTYPE</b><br />
Type: `int`<br />

Specifies the mongo DB Type. If it's 0, it means that you are using standard mongo db. If it's 1 it means you are using AWS Document DB. If it's 2, it means you are using CosmosDB.
Defaults to Standard mongo (0).

### uptime\_pump\_config.omit\_index\_creation

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_OMITINDEXCREATION</b><br />
Type: `bool`<br />

Set to true to disable the default tyk index creation.

### uptime\_pump\_config.mongo\_session\_consistency

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_MONGOSESSIONCONSISTENCY</b><br />
Type: `string`<br />

Set the consistency mode for the session, it defaults to `Strong`. The valid values are: strong, monotonic, eventual.

### uptime\_pump\_config.driver

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_MONGODRIVERTYPE</b><br />
Type: `string`<br />

MongoDriverType is the type of the driver (library) to use. The valid values are: “mongo-go” and “mgo”.
Since v1.9, the default driver is "mongo-go". Check out this guide to [learn about MongoDB drivers supported by Tyk Pump](https://github.com/TykTechnologies/tyk-pump#driver-type).

### uptime\_pump\_config.mongo\_direct\_connection

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_MONGODIRECTCONNECTION</b><br />
Type: `bool`<br />

MongoDirectConnection informs whether to establish connections only with the specified seed servers,
or to obtain information for the whole cluster and establish connections with further servers too.
If true, the client will only connect to the host provided in the ConnectionString
and won't attempt to discover other hosts in the cluster. Useful when network restrictions
prevent discovery, such as with SSH tunneling. Default is false.

### uptime\_pump\_config.collection\_name

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_COLLECTIONNAME</b><br />
Type: `string`<br />

Specifies the mongo collection name.

### uptime\_pump\_config.max\_insert\_batch\_size\_bytes

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_MAXINSERTBATCHSIZEBYTES</b><br />
Type: `int`<br />

Maximum insert batch size for mongo selective pump. If the batch we are writing surpasses this value, it will be sent in multiple batches.
Defaults to 10Mb.

### uptime\_pump\_config.max\_document\_size\_bytes

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_MAXDOCUMENTSIZEBYTES</b><br />
Type: `int`<br />

Maximum document size. If the document exceed this value, it will be skipped.
Defaults to 10Mb.

### uptime\_pump\_config.collection\_cap\_max\_size\_bytes

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_COLLECTIONCAPMAXSIZEBYTES</b><br />
Type: `int`<br />

Amount of bytes of the capped collection in 64bits architectures.
Defaults to 5GB.

### uptime\_pump\_config.collection\_cap\_enable

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_COLLECTIONCAPENABLE</b><br />
Type: `bool`<br />

Enable collection capping. It's used to set a maximum size of the collection.

### uptime\_pump\_config.type

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_TYPE</b><br />
Type: `string`<br />

The only supported and tested types are `postgres` and `mysql`.
From v1.12.0, we no longer support `sqlite` as a storage type.

### uptime\_pump\_config.connection\_string

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_CONNECTIONSTRING</b><br />
Type: `string`<br />

Specifies the connection string to the database.

### uptime\_pump\_config.postgres

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_POSTGRES</b><br />
Type: `PostgresConfig`<br />

Postgres configurations.

### uptime\_pump\_config.postgres.prefer\_simple\_protocol

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_POSTGRES\_PREFERSIMPLEPROTOCOL</b><br />
Type: `bool`<br />

Disables implicit prepared statement usage.

### uptime\_pump\_config.mysql

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_MYSQL</b><br />
Type: `MysqlConfig`<br />

Mysql configurations.

### uptime\_pump\_config.mysql.default\_string\_size

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_MYSQL\_DEFAULTSTRINGSIZE</b><br />
Type: `uint`<br />

Default size for string fields. Defaults to `256`.

### uptime\_pump\_config.mysql.disable\_datetime\_precision

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_MYSQL\_DISABLEDATETIMEPRECISION</b><br />
Type: `bool`<br />

Disable datetime precision, which not supported before MySQL 5.6.

### uptime\_pump\_config.mysql.dont\_support\_rename\_index

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_MYSQL\_DONTSUPPORTRENAMEINDEX</b><br />
Type: `bool`<br />

Drop & create when rename index, rename index not supported before MySQL 5.7, MariaDB.

### uptime\_pump\_config.mysql.dont\_support\_rename\_column

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_MYSQL\_DONTSUPPORTRENAMECOLUMN</b><br />
Type: `bool`<br />

`change` when rename column, rename column not supported before MySQL 8, MariaDB.

### uptime\_pump\_config.mysql.skip\_initialize\_with\_version

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_MYSQL\_SKIPINITIALIZEWITHVERSION</b><br />
Type: `bool`<br />

Auto configure based on currently MySQL version.

### uptime\_pump\_config.table\_sharding

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_TABLESHARDING</b><br />
Type: `bool`<br />

Specifies if all the analytics records are going to be stored in one table or in multiple
tables (one per day). By default, `false`. If `false`, all the records are going to be
stored in `tyk_aggregated` table. Instead, if it's `true`, all the records of the day are
going to be stored in `tyk_aggregated_YYYYMMDD` table, where `YYYYMMDD` is going to change
depending on the date.

### uptime\_pump\_config.log\_level

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_LOGLEVEL</b><br />
Type: `string`<br />

Specifies the SQL log verbosity. The possible values are: `info`,`error` and `warning`. By
default, the value is `silent`, which means that it won't log any SQL query.

### uptime\_pump\_config.batch\_size

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_BATCHSIZE</b><br />
Type: `int`<br />

Specifies the amount of records that are going to be written each batch. Type int. By
default, it writes 1000 records max per batch.

### uptime\_pump\_config.migrate\_sharded\_tables

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_MIGRATESHARDEDTABLES</b><br />
Type: `bool`<br />

Specifies whether to migrate all existing sharded tables to latest schema during Pump initialization (default: false).
When true, on initialization Pump will scan and migrate all sharded tables to the latest schema.
When false, existing tables will not be migrated and may miss columns included in the latest schema.
If there are a large number of existing tables, or those tables are in use by other services, there may be a performance impact from the migration. We recommend testing carefully.

### uptime\_pump\_config.uptime\_type

ENV: <b>TYK\_PMP\_UPTIMEPUMPCONFIG\_UPTIMETYPE</b><br />
Type: `string`<br />

Determines the uptime type. Options are `mongo` and `sql`. Defaults to `mongo`.

### pumps

The default environment variable prefix for each pump follows this format:
`TYK_PMP_PUMPS_{PUMP-NAME}_`, for example `TYK_PMP_PUMPS_KAFKA_`.

You can also set custom names for each pump specifying the pump type. For example, if you
want a Kafka pump which is called `PROD` you need to create `TYK_PMP_PUMPS_PROD_TYPE=kafka`
and configure it using the `TYK_PMP_PUMPS_PROD_` prefix.

### pumps.csv.name

ENV: <b>TYK\_PMP\_PUMPS\_CSV\_NAME</b><br />
Type: `string`<br />

The name of the pump. This is used to identify the pump in the logs.
Deprecated, use `type` instead.

### pumps.csv.type

ENV: <b>TYK\_PMP\_PUMPS\_CSV\_TYPE</b><br />
Type: `string`<br />

Sets the pump type. This is needed when the pump key does not equal to the pump name type.
Current valid types are: `mongo`, `mongo-pump-selective`, `mongo-pump-aggregate`, `csv`,
`elasticsearch`, `influx`, `influx2`, `moesif`, `statsd`, `segment`, `graylog`, `splunk`, `hybrid`, `prometheus`,
`logzio`, `dogstatsd`, `kafka`, `syslog`, `sql`, `sql_aggregate`, `stdout`, `timestream`, `mongo-graph`,
`sql-graph`, `sql-graph-aggregate`, `resurfaceio`.

### pumps.csv.filters

This feature adds a new configuration field in each pump called filters and its structure is
the following:

```{.json}  theme={null}
"filters":{
  "api_ids":[],
  "org_ids":[],
  "response_codes":[],
  "skip_api_ids":[],
  "skip_org_ids":[],
  "skip_response_codes":[]
}
```

The fields api\_ids, org\_ids and response\_codes works as allow list (APIs and orgs where we
want to send the analytics records) and the fields skip\_api\_ids, skip\_org\_ids and
skip\_response\_codes works as block list.

The priority is always block list configurations over allow list.

An example of configuration would be:

```{.json}  theme={null}
"csv": {
 "type": "csv",
 "filters": {
   "org_ids": ["org1","org2"]
 },
 "meta": {
   "csv_dir": "./bar"
 }
}
```

### pumps.csv.filters.org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_CSV\_FILTERS\_ORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of org\_ids.

### pumps.csv.filters.api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_CSV\_FILTERS\_APIIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of api\_ids.

### pumps.csv.filters.response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_CSV\_FILTERS\_RESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by an allow list of response\_codes.

### pumps.csv.filters.skip\_org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_CSV\_FILTERS\_SKIPPEDORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of org\_ids.

### pumps.csv.filters.skip\_api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_CSV\_FILTERS\_SKIPPEDAPIIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of api\_ids.

### pumps.csv.filters.skip\_response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_CSV\_FILTERS\_SKIPPEDRESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by a block list of response\_codes.

### pumps.csv.timeout

ENV: <b>TYK\_PMP\_PUMPS\_CSV\_TIMEOUT</b><br />
Type: `int`<br />

By default, a pump will wait forever for each write operation to complete; you can configure an optional timeout by setting the configuration option `timeout`.
If you have deployed multiple pumps, then you can configure each timeout independently. The timeout is in seconds and defaults to 0.

The timeout is configured within the main pump config as shown here; note that this example would configure a 5 second timeout:

```{.json}  theme={null}
"pump_name": {
  ...
  "timeout":5,
  "meta": {...}
}
```

Tyk will inform you if the pump's write operation is taking longer than the purging loop (configured via `purge_delay`) as this will mean that data is purged before being written to the target data sink.

If there is no timeout configured and pump's write operation is taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try to set a timeout for this pump.`

If there is a timeout configured, but pump's write operation is still taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try lowering the timeout configured for this pump.`.

### pumps.csv.omit\_detailed\_recording

ENV: <b>TYK\_PMP\_PUMPS\_CSV\_OMITDETAILEDRECORDING</b><br />
Type: `bool`<br />

Reduce the size of the traffic logs generated for each request by setting this to true. Tyk Pump will
then not include the `raw_request` and `raw_response` in the logs. Defaults to `false`.

### pumps.csv.max\_record\_size

ENV: <b>TYK\_PMP\_PUMPS\_CSV\_MAXRECORDSIZE</b><br />
Type: `int`<br />

Defines maximum size (in bytes) for Raw Request and Raw Response logs, this value defaults
to 0. If it is not set then tyk-pump will not trim any data and will store the full
information. This can also be set at a pump level. For example:

```{.json}  theme={null}
"csv": {
  "type": "csv",
  "max_record_size":1000,
  "meta": {
    "csv_dir": "./"
  }
}
```

### pumps.csv.ignore\_fields

ENV: <b>TYK\_PMP\_PUMPS\_CSV\_IGNOREFIELDS</b><br />
Type: `[]string`<br />

IgnoreFields defines a list of analytics fields that will be ignored when writing to the pump.
This can be used to avoid writing sensitive information to the Database, or data that you don't really need to have.
The field names must be the same as the JSON tags of the analytics record fields.
For example: `["api_key", "api_version"]`.

### pumps.csv.meta.EnvPrefix

ENV: <b>TYK\_PMP\_PUMPS\_CSV\_META\_ENVPREFIX</b><br />
Type: `string`<br />

The prefix for the environment variables that will be used to override the configuration.
Defaults to `TYK_PMP_PUMPS_CSV_META`

### pumps.csv.meta.csv\_dir

ENV: <b>TYK\_PMP\_PUMPS\_CSV\_META\_CSVDIR</b><br />
Type: `string`<br />

The directory and the filename where the CSV data will be stored.

### pumps.dogstatsd.name

ENV: <b>TYK\_PMP\_PUMPS\_DOGSTATSD\_NAME</b><br />
Type: `string`<br />

The name of the pump. This is used to identify the pump in the logs.
Deprecated, use `type` instead.

### pumps.dogstatsd.type

ENV: <b>TYK\_PMP\_PUMPS\_DOGSTATSD\_TYPE</b><br />
Type: `string`<br />

Sets the pump type. This is needed when the pump key does not equal to the pump name type.
Current valid types are: `mongo`, `mongo-pump-selective`, `mongo-pump-aggregate`, `csv`,
`elasticsearch`, `influx`, `influx2`, `moesif`, `statsd`, `segment`, `graylog`, `splunk`, `hybrid`, `prometheus`,
`logzio`, `dogstatsd`, `kafka`, `syslog`, `sql`, `sql_aggregate`, `stdout`, `timestream`, `mongo-graph`,
`sql-graph`, `sql-graph-aggregate`, `resurfaceio`.

### pumps.dogstatsd.filters

This feature adds a new configuration field in each pump called filters and its structure is
the following:

```{.json}  theme={null}
"filters":{
  "api_ids":[],
  "org_ids":[],
  "response_codes":[],
  "skip_api_ids":[],
  "skip_org_ids":[],
  "skip_response_codes":[]
}
```

The fields api\_ids, org\_ids and response\_codes works as allow list (APIs and orgs where we
want to send the analytics records) and the fields skip\_api\_ids, skip\_org\_ids and
skip\_response\_codes works as block list.

The priority is always block list configurations over allow list.

An example of configuration would be:

```{.json}  theme={null}
"csv": {
 "type": "csv",
 "filters": {
   "org_ids": ["org1","org2"]
 },
 "meta": {
   "csv_dir": "./bar"
 }
}
```

### pumps.dogstatsd.filters.org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_DOGSTATSD\_FILTERS\_ORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of org\_ids.

### pumps.dogstatsd.filters.api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_DOGSTATSD\_FILTERS\_APIIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of api\_ids.

### pumps.dogstatsd.filters.response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_DOGSTATSD\_FILTERS\_RESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by an allow list of response\_codes.

### pumps.dogstatsd.filters.skip\_org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_DOGSTATSD\_FILTERS\_SKIPPEDORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of org\_ids.

### pumps.dogstatsd.filters.skip\_api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_DOGSTATSD\_FILTERS\_SKIPPEDAPIIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of api\_ids.

### pumps.dogstatsd.filters.skip\_response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_DOGSTATSD\_FILTERS\_SKIPPEDRESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by a block list of response\_codes.

### pumps.dogstatsd.timeout

ENV: <b>TYK\_PMP\_PUMPS\_DOGSTATSD\_TIMEOUT</b><br />
Type: `int`<br />

By default, a pump will wait forever for each write operation to complete; you can configure an optional timeout by setting the configuration option `timeout`.
If you have deployed multiple pumps, then you can configure each timeout independently. The timeout is in seconds and defaults to 0.

The timeout is configured within the main pump config as shown here; note that this example would configure a 5 second timeout:

```{.json}  theme={null}
"pump_name": {
  ...
  "timeout":5,
  "meta": {...}
}
```

Tyk will inform you if the pump's write operation is taking longer than the purging loop (configured via `purge_delay`) as this will mean that data is purged before being written to the target data sink.

If there is no timeout configured and pump's write operation is taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try to set a timeout for this pump.`

If there is a timeout configured, but pump's write operation is still taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try lowering the timeout configured for this pump.`.

### pumps.dogstatsd.omit\_detailed\_recording

ENV: <b>TYK\_PMP\_PUMPS\_DOGSTATSD\_OMITDETAILEDRECORDING</b><br />
Type: `bool`<br />

Reduce the size of the traffic logs generated for each request by setting this to true. Tyk Pump will
then not include the `raw_request` and `raw_response` in the logs. Defaults to `false`.

### pumps.dogstatsd.max\_record\_size

ENV: <b>TYK\_PMP\_PUMPS\_DOGSTATSD\_MAXRECORDSIZE</b><br />
Type: `int`<br />

Defines maximum size (in bytes) for Raw Request and Raw Response logs, this value defaults
to 0. If it is not set then tyk-pump will not trim any data and will store the full
information. This can also be set at a pump level. For example:

```{.json}  theme={null}
"csv": {
  "type": "csv",
  "max_record_size":1000,
  "meta": {
    "csv_dir": "./"
  }
}
```

### pumps.dogstatsd.ignore\_fields

ENV: <b>TYK\_PMP\_PUMPS\_DOGSTATSD\_IGNOREFIELDS</b><br />
Type: `[]string`<br />

IgnoreFields defines a list of analytics fields that will be ignored when writing to the pump.
This can be used to avoid writing sensitive information to the Database, or data that you don't really need to have.
The field names must be the same as the JSON tags of the analytics record fields.
For example: `["api_key", "api_version"]`.

### pumps.dogstatsd.meta.EnvPrefix

ENV: <b>TYK\_PMP\_PUMPS\_DOGSTATSD\_META\_ENVPREFIX</b><br />
Type: `string`<br />

The prefix for the environment variables that will be used to override the configuration.
Defaults to `TYK_PMP_PUMPS_DOGSTATSD_META`

### pumps.dogstatsd.meta.namespace

ENV: <b>TYK\_PMP\_PUMPS\_DOGSTATSD\_META\_NAMESPACE</b><br />
Type: `string`<br />

Prefix for your metrics to datadog.

### pumps.dogstatsd.meta.address

ENV: <b>TYK\_PMP\_PUMPS\_DOGSTATSD\_META\_ADDRESS</b><br />
Type: `string`<br />

Address of the datadog agent including host & port.

### pumps.dogstatsd.meta.sample\_rate

ENV: <b>TYK\_PMP\_PUMPS\_DOGSTATSD\_META\_SAMPLERATE</b><br />
Type: `float64`<br />

Defaults to `1` which equates to `100%` of requests. To sample at `50%`, set to `0.5`.

### pumps.dogstatsd.meta.async\_uds

ENV: <b>TYK\_PMP\_PUMPS\_DOGSTATSD\_META\_ASYNCUDS</b><br />
Type: `bool`<br />

Enable async UDS over UDP [https://github.com/Datadog/datadog-go#unix-domain-sockets-client](https://github.com/Datadog/datadog-go#unix-domain-sockets-client).

### pumps.dogstatsd.meta.async\_uds\_write\_timeout\_seconds

ENV: <b>TYK\_PMP\_PUMPS\_DOGSTATSD\_META\_ASYNCUDSWRITETIMEOUT</b><br />
Type: `int`<br />

Integer write timeout in seconds if `async_uds: true`.

### pumps.dogstatsd.meta.buffered

ENV: <b>TYK\_PMP\_PUMPS\_DOGSTATSD\_META\_BUFFERED</b><br />
Type: `bool`<br />

Enable buffering of messages.

### pumps.dogstatsd.meta.buffered\_max\_messages

ENV: <b>TYK\_PMP\_PUMPS\_DOGSTATSD\_META\_BUFFEREDMAXMESSAGES</b><br />
Type: `int`<br />

Max messages in single datagram if `buffered: true`. Default 16.

### pumps.dogstatsd.meta.tags

ENV: <b>TYK\_PMP\_PUMPS\_DOGSTATSD\_META\_TAGS</b><br />
Type: `[]string`<br />

List of tags to be added to the metric. The possible options are listed in the below example.

If no tag is specified the fallback behavior is to use the below tags:

* `path`
* `method`
* `response_code`
* `api_version`
* `api_name`
* `api_id`
* `org_id`
* `tracked`
* `oauth_id`

Note that this configuration can generate significant charges due to the unbound nature of
the `path` tag.

```{.json}  theme={null}
"dogstatsd": {
  "type": "dogstatsd",
  "meta": {
    "address": "localhost:8125",
    "namespace": "pump",
    "async_uds": true,
    "async_uds_write_timeout_seconds": 2,
    "buffered": true,
    "buffered_max_messages": 32,
    "sample_rate": 0.5,
    "tags": [
      "method",
      "response_code",
      "api_version",
      "api_name",
      "api_id",
      "org_id",
      "tracked",
      "path",
      "oauth_id"
    ]
  }
},
```

On startup, you should see the loaded configs when initializing the dogstatsd pump

```
[May 10 15:23:44]  INFO dogstatsd: initializing pump
[May 10 15:23:44]  INFO dogstatsd: namespace: pump.
[May 10 15:23:44]  INFO dogstatsd: sample_rate: 50%
[May 10 15:23:44]  INFO dogstatsd: buffered: true, max_messages: 32
[May 10 15:23:44]  INFO dogstatsd: async_uds: true, write_timeout: 2s
```

### pumps.elasticsearch.name

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_NAME</b><br />
Type: `string`<br />

The name of the pump. This is used to identify the pump in the logs.
Deprecated, use `type` instead.

### pumps.elasticsearch.type

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_TYPE</b><br />
Type: `string`<br />

Sets the pump type. This is needed when the pump key does not equal to the pump name type.
Current valid types are: `mongo`, `mongo-pump-selective`, `mongo-pump-aggregate`, `csv`,
`elasticsearch`, `influx`, `influx2`, `moesif`, `statsd`, `segment`, `graylog`, `splunk`, `hybrid`, `prometheus`,
`logzio`, `dogstatsd`, `kafka`, `syslog`, `sql`, `sql_aggregate`, `stdout`, `timestream`, `mongo-graph`,
`sql-graph`, `sql-graph-aggregate`, `resurfaceio`.

### pumps.elasticsearch.filters

This feature adds a new configuration field in each pump called filters and its structure is
the following:

```{.json}  theme={null}
"filters":{
  "api_ids":[],
  "org_ids":[],
  "response_codes":[],
  "skip_api_ids":[],
  "skip_org_ids":[],
  "skip_response_codes":[]
}
```

The fields api\_ids, org\_ids and response\_codes works as allow list (APIs and orgs where we
want to send the analytics records) and the fields skip\_api\_ids, skip\_org\_ids and
skip\_response\_codes works as block list.

The priority is always block list configurations over allow list.

An example of configuration would be:

```{.json}  theme={null}
"csv": {
 "type": "csv",
 "filters": {
   "org_ids": ["org1","org2"]
 },
 "meta": {
   "csv_dir": "./bar"
 }
}
```

### pumps.elasticsearch.filters.org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_FILTERS\_ORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of org\_ids.

### pumps.elasticsearch.filters.api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_FILTERS\_APIIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of api\_ids.

### pumps.elasticsearch.filters.response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_FILTERS\_RESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by an allow list of response\_codes.

### pumps.elasticsearch.filters.skip\_org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_FILTERS\_SKIPPEDORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of org\_ids.

### pumps.elasticsearch.filters.skip\_api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_FILTERS\_SKIPPEDAPIIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of api\_ids.

### pumps.elasticsearch.filters.skip\_response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_FILTERS\_SKIPPEDRESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by a block list of response\_codes.

### pumps.elasticsearch.timeout

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_TIMEOUT</b><br />
Type: `int`<br />

By default, a pump will wait forever for each write operation to complete; you can configure an optional timeout by setting the configuration option `timeout`.
If you have deployed multiple pumps, then you can configure each timeout independently. The timeout is in seconds and defaults to 0.

The timeout is configured within the main pump config as shown here; note that this example would configure a 5 second timeout:

```{.json}  theme={null}
"pump_name": {
  ...
  "timeout":5,
  "meta": {...}
}
```

Tyk will inform you if the pump's write operation is taking longer than the purging loop (configured via `purge_delay`) as this will mean that data is purged before being written to the target data sink.

If there is no timeout configured and pump's write operation is taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try to set a timeout for this pump.`

If there is a timeout configured, but pump's write operation is still taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try lowering the timeout configured for this pump.`.

### pumps.elasticsearch.omit\_detailed\_recording

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_OMITDETAILEDRECORDING</b><br />
Type: `bool`<br />

Reduce the size of the traffic logs generated for each request by setting this to true. Tyk Pump will
then not include the `raw_request` and `raw_response` in the logs. Defaults to `false`.

### pumps.elasticsearch.max\_record\_size

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_MAXRECORDSIZE</b><br />
Type: `int`<br />

Defines maximum size (in bytes) for Raw Request and Raw Response logs, this value defaults
to 0. If it is not set then tyk-pump will not trim any data and will store the full
information. This can also be set at a pump level. For example:

```{.json}  theme={null}
"csv": {
  "type": "csv",
  "max_record_size":1000,
  "meta": {
    "csv_dir": "./"
  }
}
```

### pumps.elasticsearch.ignore\_fields

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_IGNOREFIELDS</b><br />
Type: `[]string`<br />

IgnoreFields defines a list of analytics fields that will be ignored when writing to the pump.
This can be used to avoid writing sensitive information to the Database, or data that you don't really need to have.
The field names must be the same as the JSON tags of the analytics record fields.
For example: `["api_key", "api_version"]`.

### pumps.elasticsearch.meta.EnvPrefix

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_META\_ENVPREFIX</b><br />
Type: `string`<br />

The prefix for the environment variables that will be used to override the configuration.
Defaults to `TYK_PMP_PUMPS_ELASTICSEARCH_META`

### pumps.elasticsearch.meta.index\_name

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_META\_INDEXNAME</b><br />
Type: `string`<br />

The name of the index that all the analytics data will be placed in. Defaults to
"tyk\_analytics".

### pumps.elasticsearch.meta.elasticsearch\_url

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_META\_ELASTICSEARCHURL</b><br />
Type: `string`<br />

If sniffing is disabled, the URL that all data will be sent to. Defaults to
"[http://localhost:9200](http://localhost:9200)".

### pumps.elasticsearch.meta.use\_sniffing

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_META\_ENABLESNIFFING</b><br />
Type: `bool`<br />

If sniffing is enabled, the "elasticsearch\_url" will be used to make a request to get a
list of all the nodes in the cluster, the returned addresses will then be used. Defaults to
`false`.

### pumps.elasticsearch.meta.document\_type

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_META\_DOCUMENTTYPE</b><br />
Type: `string`<br />

The type of the document that is created in ES. Defaults to "tyk\_analytics".

### pumps.elasticsearch.meta.rolling\_index

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_META\_ROLLINGINDEX</b><br />
Type: `bool`<br />

Appends the date to the end of the index name, so each days data is split into a different
index name. E.g. tyk\_analytics-2016.02.28. Defaults to `false`.

### pumps.elasticsearch.meta.extended\_stats

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_META\_EXTENDEDSTATISTICS</b><br />
Type: `bool`<br />

If set to `true` will include the following additional fields: Raw Request, Raw Response and
User Agent.

### pumps.elasticsearch.meta.generate\_id

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_META\_GENERATEID</b><br />
Type: `bool`<br />

When enabled, generate \_id for outgoing records. This prevents duplicate records when
retrying ES.

### pumps.elasticsearch.meta.decode\_base64

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_META\_DECODEBASE64</b><br />
Type: `bool`<br />

Allows for the base64 bits to be decode before being passed to ES.

### pumps.elasticsearch.meta.version

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_META\_VERSION</b><br />
Type: `string`<br />

Specifies the ES version. Use "3" for ES 3.X, "5" for ES 5.X, "6" for ES 6.X, "7" for ES
7.X . Defaults to "3".

### pumps.elasticsearch.meta.disable\_bulk

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_META\_DISABLEBULK</b><br />
Type: `bool`<br />

Disable batch writing. Defaults to false.

### pumps.elasticsearch.meta.bulk\_config

Batch writing trigger configuration. Each option is an OR with eachother:

### pumps.elasticsearch.meta.bulk\_config.workers

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_META\_BULKCONFIG\_WORKERS</b><br />
Type: `int`<br />

Number of workers. Defaults to 1.

### pumps.elasticsearch.meta.bulk\_config.flush\_interval

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_META\_BULKCONFIG\_FLUSHINTERVAL</b><br />
Type: `int`<br />

Specifies the time in seconds to flush the data and send it to ES. Default disabled.

### pumps.elasticsearch.meta.bulk\_config.bulk\_actions

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_META\_BULKCONFIG\_BULKACTIONS</b><br />
Type: `int`<br />

Specifies the number of requests needed to flush the data and send it to ES. Defaults to
1000 requests. If it is needed, can be disabled with -1.

### pumps.elasticsearch.meta.bulk\_config.bulk\_size

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_META\_BULKCONFIG\_BULKSIZE</b><br />
Type: `int`<br />

Specifies the size (in bytes) needed to flush the data and send it to ES. Defaults to 5MB.
If it is needed, can be disabled with -1.

### pumps.elasticsearch.meta.auth\_api\_key\_id

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_META\_AUTHAPIKEYID</b><br />
Type: `string`<br />

API Key ID used for APIKey auth in ES. It's send to ES in the Authorization header as ApiKey base64(auth\_api\_key\_id:auth\_api\_key)

### pumps.elasticsearch.meta.auth\_api\_key

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_META\_AUTHAPIKEY</b><br />
Type: `string`<br />

API Key used for APIKey auth in ES. It's send to ES in the Authorization header as ApiKey base64(auth\_api\_key\_id:auth\_api\_key)

### pumps.elasticsearch.meta.auth\_basic\_username

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_META\_USERNAME</b><br />
Type: `string`<br />

Basic auth username. It's send to ES in the Authorization header as username:password encoded in base64.

### pumps.elasticsearch.meta.auth\_basic\_password

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_META\_PASSWORD</b><br />
Type: `string`<br />

Basic auth password. It's send to ES in the Authorization header as username:password encoded in base64.

### pumps.elasticsearch.meta.use\_ssl

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_META\_USESSL</b><br />
Type: `bool`<br />

Enables SSL connection.

### pumps.elasticsearch.meta.ssl\_insecure\_skip\_verify

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_META\_SSLINSECURESKIPVERIFY</b><br />
Type: `bool`<br />

Controls whether the pump client verifies the Elastic Search server's certificate chain and hostname.

### pumps.elasticsearch.meta.ssl\_cert\_file

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_META\_SSLCERTFILE</b><br />
Type: `string`<br />

Can be used to set custom certificate file for authentication with Elastic Search.

### pumps.elasticsearch.meta.ssl\_key\_file

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_META\_SSLKEYFILE</b><br />
Type: `string`<br />

Can be used to set custom key file for authentication with Elastic Search.

### pumps.elasticsearch.meta.ssl\_ca\_file

ENV: <b>TYK\_PMP\_PUMPS\_ELASTICSEARCH\_META\_SSLCAFILE</b><br />
Type: `string`<br />

Path to the PEM file with trusted CA certificates that will be used to verify the Elasticsearch server's certificate.

### pumps.graylog.name

ENV: <b>TYK\_PMP\_PUMPS\_GRAYLOG\_NAME</b><br />
Type: `string`<br />

The name of the pump. This is used to identify the pump in the logs.
Deprecated, use `type` instead.

### pumps.graylog.type

ENV: <b>TYK\_PMP\_PUMPS\_GRAYLOG\_TYPE</b><br />
Type: `string`<br />

Sets the pump type. This is needed when the pump key does not equal to the pump name type.
Current valid types are: `mongo`, `mongo-pump-selective`, `mongo-pump-aggregate`, `csv`,
`elasticsearch`, `influx`, `influx2`, `moesif`, `statsd`, `segment`, `graylog`, `splunk`, `hybrid`, `prometheus`,
`logzio`, `dogstatsd`, `kafka`, `syslog`, `sql`, `sql_aggregate`, `stdout`, `timestream`, `mongo-graph`,
`sql-graph`, `sql-graph-aggregate`, `resurfaceio`.

### pumps.graylog.filters

This feature adds a new configuration field in each pump called filters and its structure is
the following:

```{.json}  theme={null}
"filters":{
  "api_ids":[],
  "org_ids":[],
  "response_codes":[],
  "skip_api_ids":[],
  "skip_org_ids":[],
  "skip_response_codes":[]
}
```

The fields api\_ids, org\_ids and response\_codes works as allow list (APIs and orgs where we
want to send the analytics records) and the fields skip\_api\_ids, skip\_org\_ids and
skip\_response\_codes works as block list.

The priority is always block list configurations over allow list.

An example of configuration would be:

```{.json}  theme={null}
"csv": {
 "type": "csv",
 "filters": {
   "org_ids": ["org1","org2"]
 },
 "meta": {
   "csv_dir": "./bar"
 }
}
```

### pumps.graylog.filters.org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_GRAYLOG\_FILTERS\_ORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of org\_ids.

### pumps.graylog.filters.api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_GRAYLOG\_FILTERS\_APIIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of api\_ids.

### pumps.graylog.filters.response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_GRAYLOG\_FILTERS\_RESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by an allow list of response\_codes.

### pumps.graylog.filters.skip\_org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_GRAYLOG\_FILTERS\_SKIPPEDORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of org\_ids.

### pumps.graylog.filters.skip\_api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_GRAYLOG\_FILTERS\_SKIPPEDAPIIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of api\_ids.

### pumps.graylog.filters.skip\_response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_GRAYLOG\_FILTERS\_SKIPPEDRESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by a block list of response\_codes.

### pumps.graylog.timeout

ENV: <b>TYK\_PMP\_PUMPS\_GRAYLOG\_TIMEOUT</b><br />
Type: `int`<br />

By default, a pump will wait forever for each write operation to complete; you can configure an optional timeout by setting the configuration option `timeout`.
If you have deployed multiple pumps, then you can configure each timeout independently. The timeout is in seconds and defaults to 0.

The timeout is configured within the main pump config as shown here; note that this example would configure a 5 second timeout:

```{.json}  theme={null}
"pump_name": {
  ...
  "timeout":5,
  "meta": {...}
}
```

Tyk will inform you if the pump's write operation is taking longer than the purging loop (configured via `purge_delay`) as this will mean that data is purged before being written to the target data sink.

If there is no timeout configured and pump's write operation is taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try to set a timeout for this pump.`

If there is a timeout configured, but pump's write operation is still taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try lowering the timeout configured for this pump.`.

### pumps.graylog.omit\_detailed\_recording

ENV: <b>TYK\_PMP\_PUMPS\_GRAYLOG\_OMITDETAILEDRECORDING</b><br />
Type: `bool`<br />

Reduce the size of the traffic logs generated for each request by setting this to true. Tyk Pump will
then not include the `raw_request` and `raw_response` in the logs. Defaults to `false`.

### pumps.graylog.max\_record\_size

ENV: <b>TYK\_PMP\_PUMPS\_GRAYLOG\_MAXRECORDSIZE</b><br />
Type: `int`<br />

Defines maximum size (in bytes) for Raw Request and Raw Response logs, this value defaults
to 0. If it is not set then tyk-pump will not trim any data and will store the full
information. This can also be set at a pump level. For example:

```{.json}  theme={null}
"csv": {
  "type": "csv",
  "max_record_size":1000,
  "meta": {
    "csv_dir": "./"
  }
}
```

### pumps.graylog.ignore\_fields

ENV: <b>TYK\_PMP\_PUMPS\_GRAYLOG\_IGNOREFIELDS</b><br />
Type: `[]string`<br />

IgnoreFields defines a list of analytics fields that will be ignored when writing to the pump.
This can be used to avoid writing sensitive information to the Database, or data that you don't really need to have.
The field names must be the same as the JSON tags of the analytics record fields.
For example: `["api_key", "api_version"]`.

### pumps.graylog.meta.EnvPrefix

ENV: <b>TYK\_PMP\_PUMPS\_GRAYLOG\_META\_ENVPREFIX</b><br />
Type: `string`<br />

The prefix for the environment variables that will be used to override the configuration.
Defaults to `TYK_PMP_PUMPS_GRAYLOG_META`

### pumps.graylog.meta.host

ENV: <b>TYK\_PMP\_PUMPS\_GRAYLOG\_META\_GRAYLOGHOST</b><br />
Type: `string`<br />

Graylog host.

### pumps.graylog.meta.port

ENV: <b>TYK\_PMP\_PUMPS\_GRAYLOG\_META\_GRAYLOGPORT</b><br />
Type: `int`<br />

Graylog port.

### pumps.graylog.meta.tags

ENV: <b>TYK\_PMP\_PUMPS\_GRAYLOG\_META\_TAGS</b><br />
Type: `[]string`<br />

List of tags to be added to the metric. The possible options are listed in the below example.

If no tag is specified the fallback behaviour is to don't send anything.
The possible values are:

* `path`
* `method`
* `response_code`
* `api_version`
* `api_name`
* `api_id`
* `org_id`
* `tracked`
* `oauth_id`
* `raw_request`
* `raw_response`
* `request_time`
* `ip_address`

### pumps.hybrid.name

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_NAME</b><br />
Type: `string`<br />

The name of the pump. This is used to identify the pump in the logs.
Deprecated, use `type` instead.

### pumps.hybrid.type

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_TYPE</b><br />
Type: `string`<br />

Sets the pump type. This is needed when the pump key does not equal to the pump name type.
Current valid types are: `mongo`, `mongo-pump-selective`, `mongo-pump-aggregate`, `csv`,
`elasticsearch`, `influx`, `influx2`, `moesif`, `statsd`, `segment`, `graylog`, `splunk`, `hybrid`, `prometheus`,
`logzio`, `dogstatsd`, `kafka`, `syslog`, `sql`, `sql_aggregate`, `stdout`, `timestream`, `mongo-graph`,
`sql-graph`, `sql-graph-aggregate`, `resurfaceio`.

### pumps.hybrid.filters

This feature adds a new configuration field in each pump called filters and its structure is
the following:

```{.json}  theme={null}
"filters":{
  "api_ids":[],
  "org_ids":[],
  "response_codes":[],
  "skip_api_ids":[],
  "skip_org_ids":[],
  "skip_response_codes":[]
}
```

The fields api\_ids, org\_ids and response\_codes works as allow list (APIs and orgs where we
want to send the analytics records) and the fields skip\_api\_ids, skip\_org\_ids and
skip\_response\_codes works as block list.

The priority is always block list configurations over allow list.

An example of configuration would be:

```{.json}  theme={null}
"csv": {
 "type": "csv",
 "filters": {
   "org_ids": ["org1","org2"]
 },
 "meta": {
   "csv_dir": "./bar"
 }
}
```

### pumps.hybrid.filters.org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_FILTERS\_ORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of org\_ids.

### pumps.hybrid.filters.api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_FILTERS\_APIIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of api\_ids.

### pumps.hybrid.filters.response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_FILTERS\_RESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by an allow list of response\_codes.

### pumps.hybrid.filters.skip\_org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_FILTERS\_SKIPPEDORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of org\_ids.

### pumps.hybrid.filters.skip\_api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_FILTERS\_SKIPPEDAPIIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of api\_ids.

### pumps.hybrid.filters.skip\_response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_FILTERS\_SKIPPEDRESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by a block list of response\_codes.

### pumps.hybrid.timeout

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_TIMEOUT</b><br />
Type: `int`<br />

By default, a pump will wait forever for each write operation to complete; you can configure an optional timeout by setting the configuration option `timeout`.
If you have deployed multiple pumps, then you can configure each timeout independently. The timeout is in seconds and defaults to 0.

The timeout is configured within the main pump config as shown here; note that this example would configure a 5 second timeout:

```{.json}  theme={null}
"pump_name": {
  ...
  "timeout":5,
  "meta": {...}
}
```

Tyk will inform you if the pump's write operation is taking longer than the purging loop (configured via `purge_delay`) as this will mean that data is purged before being written to the target data sink.

If there is no timeout configured and pump's write operation is taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try to set a timeout for this pump.`

If there is a timeout configured, but pump's write operation is still taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try lowering the timeout configured for this pump.`.

### pumps.hybrid.omit\_detailed\_recording

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_OMITDETAILEDRECORDING</b><br />
Type: `bool`<br />

Reduce the size of the traffic logs generated for each request by setting this to true. Tyk Pump will
then not include the `raw_request` and `raw_response` in the logs. Defaults to `false`.

### pumps.hybrid.max\_record\_size

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_MAXRECORDSIZE</b><br />
Type: `int`<br />

Defines maximum size (in bytes) for Raw Request and Raw Response logs, this value defaults
to 0. If it is not set then tyk-pump will not trim any data and will store the full
information. This can also be set at a pump level. For example:

```{.json}  theme={null}
"csv": {
  "type": "csv",
  "max_record_size":1000,
  "meta": {
    "csv_dir": "./"
  }
}
```

### pumps.hybrid.ignore\_fields

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_IGNOREFIELDS</b><br />
Type: `[]string`<br />

IgnoreFields defines a list of analytics fields that will be ignored when writing to the pump.
This can be used to avoid writing sensitive information to the Database, or data that you don't really need to have.
The field names must be the same as the JSON tags of the analytics record fields.
For example: `["api_key", "api_version"]`.

### pumps.hybrid.meta.EnvPrefix

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_META\_ENVPREFIX</b><br />
Type: `string`<br />

The prefix for the environment variables that will be used to override the configuration.
Defaults to `TYK_PMP_PUMPS_HYBRID_META`

### pumps.hybrid.meta.ConnectionString

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_META\_CONNECTIONSTRING</b><br />
Type: `string`<br />

MDCB URL connection string

### pumps.hybrid.meta.RPCKey

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_META\_RPCKEY</b><br />
Type: `string`<br />

Your organization ID to connect to the MDCB installation.

### pumps.hybrid.meta.APIKey

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_META\_APIKEY</b><br />
Type: `string`<br />

This the API key of a user used to authenticate and authorize the Hybrid Pump access through MDCB.
The user should be a standard Dashboard user with minimal privileges so as to reduce any risk if the user is compromised.

### pumps.hybrid.meta.ignore\_tag\_prefix\_list

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_META\_IGNORETAGPREFIXLIST</b><br />
Type: `[]string`<br />

Specifies prefixes of tags that should be ignored if `aggregated` is set to `true`.

### pumps.hybrid.meta.CallTimeout

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_META\_CALLTIMEOUT</b><br />
Type: `int`<br />

Hybrid pump RPC calls timeout in seconds. Defaults to `10` seconds.

### pumps.hybrid.meta.RPCPoolSize

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_META\_RPCPOOLSIZE</b><br />
Type: `int`<br />

Hybrid pump connection pool size. Defaults to `5`.

### pumps.hybrid.meta.aggregationTime

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_META\_AGGREGATIONTIME</b><br />
Type: `int`<br />

aggregationTime is to specify the frequency of the aggregation in minutes if `aggregated` is set to `true`.

### pumps.hybrid.meta.Aggregated

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_META\_AGGREGATED</b><br />
Type: `bool`<br />

Send aggregated analytics data to Tyk MDCB

### pumps.hybrid.meta.TrackAllPaths

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_META\_TRACKALLPATHS</b><br />
Type: `bool`<br />

Specifies if it should store aggregated data for all the endpoints if `aggregated` is set to `true`. By default, `false`
which means that only store aggregated data for `tracked endpoints`.

### pumps.hybrid.meta.store\_analytics\_per\_minute

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_META\_STOREANALYTICSPERMINUTE</b><br />
Type: `bool`<br />

Determines if the aggregations should be made per minute (true) or per hour (false) if `aggregated` is set to `true`.

### pumps.hybrid.meta.UseSSL

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_META\_USESSL</b><br />
Type: `bool`<br />

Use SSL to connect to Tyk MDCB

### pumps.hybrid.meta.SSLInsecureSkipVerify

ENV: <b>TYK\_PMP\_PUMPS\_HYBRID\_META\_SSLINSECURESKIPVERIFY</b><br />
Type: `bool`<br />

Skip SSL verification

### pumps.influx.name

ENV: <b>TYK\_PMP\_PUMPS\_INFLUX\_NAME</b><br />
Type: `string`<br />

The name of the pump. This is used to identify the pump in the logs.
Deprecated, use `type` instead.

### pumps.influx.type

ENV: <b>TYK\_PMP\_PUMPS\_INFLUX\_TYPE</b><br />
Type: `string`<br />

Sets the pump type. This is needed when the pump key does not equal to the pump name type.
Current valid types are: `mongo`, `mongo-pump-selective`, `mongo-pump-aggregate`, `csv`,
`elasticsearch`, `influx`, `influx2`, `moesif`, `statsd`, `segment`, `graylog`, `splunk`, `hybrid`, `prometheus`,
`logzio`, `dogstatsd`, `kafka`, `syslog`, `sql`, `sql_aggregate`, `stdout`, `timestream`, `mongo-graph`,
`sql-graph`, `sql-graph-aggregate`, `resurfaceio`.

### pumps.influx.filters

This feature adds a new configuration field in each pump called filters and its structure is
the following:

```{.json}  theme={null}
"filters":{
  "api_ids":[],
  "org_ids":[],
  "response_codes":[],
  "skip_api_ids":[],
  "skip_org_ids":[],
  "skip_response_codes":[]
}
```

The fields api\_ids, org\_ids and response\_codes works as allow list (APIs and orgs where we
want to send the analytics records) and the fields skip\_api\_ids, skip\_org\_ids and
skip\_response\_codes works as block list.

The priority is always block list configurations over allow list.

An example of configuration would be:

```{.json}  theme={null}
"csv": {
 "type": "csv",
 "filters": {
   "org_ids": ["org1","org2"]
 },
 "meta": {
   "csv_dir": "./bar"
 }
}
```

### pumps.influx.filters.org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_INFLUX\_FILTERS\_ORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of org\_ids.

### pumps.influx.filters.api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_INFLUX\_FILTERS\_APIIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of api\_ids.

### pumps.influx.filters.response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_INFLUX\_FILTERS\_RESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by an allow list of response\_codes.

### pumps.influx.filters.skip\_org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_INFLUX\_FILTERS\_SKIPPEDORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of org\_ids.

### pumps.influx.filters.skip\_api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_INFLUX\_FILTERS\_SKIPPEDAPIIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of api\_ids.

### pumps.influx.filters.skip\_response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_INFLUX\_FILTERS\_SKIPPEDRESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by a block list of response\_codes.

### pumps.influx.timeout

ENV: <b>TYK\_PMP\_PUMPS\_INFLUX\_TIMEOUT</b><br />
Type: `int`<br />

By default, a pump will wait forever for each write operation to complete; you can configure an optional timeout by setting the configuration option `timeout`.
If you have deployed multiple pumps, then you can configure each timeout independently. The timeout is in seconds and defaults to 0.

The timeout is configured within the main pump config as shown here; note that this example would configure a 5 second timeout:

```{.json}  theme={null}
"pump_name": {
  ...
  "timeout":5,
  "meta": {...}
}
```

Tyk will inform you if the pump's write operation is taking longer than the purging loop (configured via `purge_delay`) as this will mean that data is purged before being written to the target data sink.

If there is no timeout configured and pump's write operation is taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try to set a timeout for this pump.`

If there is a timeout configured, but pump's write operation is still taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try lowering the timeout configured for this pump.`.

### pumps.influx.omit\_detailed\_recording

ENV: <b>TYK\_PMP\_PUMPS\_INFLUX\_OMITDETAILEDRECORDING</b><br />
Type: `bool`<br />

Reduce the size of the traffic logs generated for each request by setting this to true. Tyk Pump will
then not include the `raw_request` and `raw_response` in the logs. Defaults to `false`.

### pumps.influx.max\_record\_size

ENV: <b>TYK\_PMP\_PUMPS\_INFLUX\_MAXRECORDSIZE</b><br />
Type: `int`<br />

Defines maximum size (in bytes) for Raw Request and Raw Response logs, this value defaults
to 0. If it is not set then tyk-pump will not trim any data and will store the full
information. This can also be set at a pump level. For example:

```{.json}  theme={null}
"csv": {
  "type": "csv",
  "max_record_size":1000,
  "meta": {
    "csv_dir": "./"
  }
}
```

### pumps.influx.ignore\_fields

ENV: <b>TYK\_PMP\_PUMPS\_INFLUX\_IGNOREFIELDS</b><br />
Type: `[]string`<br />

IgnoreFields defines a list of analytics fields that will be ignored when writing to the pump.
This can be used to avoid writing sensitive information to the Database, or data that you don't really need to have.
The field names must be the same as the JSON tags of the analytics record fields.
For example: `["api_key", "api_version"]`.

### pumps.influx.meta.EnvPrefix

ENV: <b>TYK\_PMP\_PUMPS\_INFLUX\_META\_ENVPREFIX</b><br />
Type: `string`<br />

The prefix for the environment variables that will be used to override the configuration.
Defaults to `TYK_PMP_PUMPS_INFLUX_META`

### pumps.influx.meta.database\_name

ENV: <b>TYK\_PMP\_PUMPS\_INFLUX\_META\_DATABASENAME</b><br />
Type: `string`<br />

InfluxDB pump database name.

### pumps.influx.meta.address

ENV: <b>TYK\_PMP\_PUMPS\_INFLUX\_META\_ADDR</b><br />
Type: `string`<br />

InfluxDB pump host.

### pumps.influx.meta.username

ENV: <b>TYK\_PMP\_PUMPS\_INFLUX\_META\_USERNAME</b><br />
Type: `string`<br />

InfluxDB pump database username.

### pumps.influx.meta.password

ENV: <b>TYK\_PMP\_PUMPS\_INFLUX\_META\_PASSWORD</b><br />
Type: `string`<br />

InfluxDB pump database password.

### pumps.influx.meta.fields

ENV: <b>TYK\_PMP\_PUMPS\_INFLUX\_META\_FIELDS</b><br />
Type: `[]string`<br />

Define which Analytics fields should be sent to InfluxDB. Check the available
fields in the example below. Default value is `["method",
"path", "response_code", "api_key", "time_stamp", "api_version", "api_name", "api_id",
"org_id", "oauth_id", "raw_request", "request_time", "raw_response", "ip_address"]`.

### pumps.influx.meta.tags

ENV: <b>TYK\_PMP\_PUMPS\_INFLUX\_META\_TAGS</b><br />
Type: `[]string`<br />

List of tags to be added to the metric.

### pumps.kafka.name

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_NAME</b><br />
Type: `string`<br />

The name of the pump. This is used to identify the pump in the logs.
Deprecated, use `type` instead.

### pumps.kafka.type

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_TYPE</b><br />
Type: `string`<br />

Sets the pump type. This is needed when the pump key does not equal to the pump name type.
Current valid types are: `mongo`, `mongo-pump-selective`, `mongo-pump-aggregate`, `csv`,
`elasticsearch`, `influx`, `influx2`, `moesif`, `statsd`, `segment`, `graylog`, `splunk`, `hybrid`, `prometheus`,
`logzio`, `dogstatsd`, `kafka`, `syslog`, `sql`, `sql_aggregate`, `stdout`, `timestream`, `mongo-graph`,
`sql-graph`, `sql-graph-aggregate`, `resurfaceio`.

### pumps.kafka.filters

This feature adds a new configuration field in each pump called filters and its structure is
the following:

```{.json}  theme={null}
"filters":{
  "api_ids":[],
  "org_ids":[],
  "response_codes":[],
  "skip_api_ids":[],
  "skip_org_ids":[],
  "skip_response_codes":[]
}
```

The fields api\_ids, org\_ids and response\_codes works as allow list (APIs and orgs where we
want to send the analytics records) and the fields skip\_api\_ids, skip\_org\_ids and
skip\_response\_codes works as block list.

The priority is always block list configurations over allow list.

An example of configuration would be:

```{.json}  theme={null}
"csv": {
 "type": "csv",
 "filters": {
   "org_ids": ["org1","org2"]
 },
 "meta": {
   "csv_dir": "./bar"
 }
}
```

### pumps.kafka.filters.org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_FILTERS\_ORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of org\_ids.

### pumps.kafka.filters.api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_FILTERS\_APIIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of api\_ids.

### pumps.kafka.filters.response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_FILTERS\_RESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by an allow list of response\_codes.

### pumps.kafka.filters.skip\_org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_FILTERS\_SKIPPEDORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of org\_ids.

### pumps.kafka.filters.skip\_api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_FILTERS\_SKIPPEDAPIIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of api\_ids.

### pumps.kafka.filters.skip\_response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_FILTERS\_SKIPPEDRESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by a block list of response\_codes.

### pumps.kafka.timeout

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_TIMEOUT</b><br />
Type: `int`<br />

By default, a pump will wait forever for each write operation to complete; you can configure an optional timeout by setting the configuration option `timeout`.
If you have deployed multiple pumps, then you can configure each timeout independently. The timeout is in seconds and defaults to 0.

The timeout is configured within the main pump config as shown here; note that this example would configure a 5 second timeout:

```{.json}  theme={null}
"pump_name": {
  ...
  "timeout":5,
  "meta": {...}
}
```

Tyk will inform you if the pump's write operation is taking longer than the purging loop (configured via `purge_delay`) as this will mean that data is purged before being written to the target data sink.

If there is no timeout configured and pump's write operation is taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try to set a timeout for this pump.`

If there is a timeout configured, but pump's write operation is still taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try lowering the timeout configured for this pump.`.

### pumps.kafka.omit\_detailed\_recording

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_OMITDETAILEDRECORDING</b><br />
Type: `bool`<br />

Reduce the size of the traffic logs generated for each request by setting this to true. Tyk Pump will
then not include the `raw_request` and `raw_response` in the logs. Defaults to `false`.

### pumps.kafka.max\_record\_size

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_MAXRECORDSIZE</b><br />
Type: `int`<br />

Defines maximum size (in bytes) for Raw Request and Raw Response logs, this value defaults
to 0. If it is not set then tyk-pump will not trim any data and will store the full
information. This can also be set at a pump level. For example:

```{.json}  theme={null}
"csv": {
  "type": "csv",
  "max_record_size":1000,
  "meta": {
    "csv_dir": "./"
  }
}
```

### pumps.kafka.ignore\_fields

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_IGNOREFIELDS</b><br />
Type: `[]string`<br />

IgnoreFields defines a list of analytics fields that will be ignored when writing to the pump.
This can be used to avoid writing sensitive information to the Database, or data that you don't really need to have.
The field names must be the same as the JSON tags of the analytics record fields.
For example: `["api_key", "api_version"]`.

### pumps.kafka.meta.EnvPrefix

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_META\_ENVPREFIX</b><br />
Type: `string`<br />

The prefix for the environment variables that will be used to override the configuration.
Defaults to `TYK_PMP_PUMPS_KAFKA_META`

### pumps.kafka.meta.broker

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_META\_BROKER</b><br />
Type: `[]string`<br />

The list of brokers used to discover the partitions available on the kafka cluster. E.g.
"localhost:9092".

### pumps.kafka.meta.client\_id

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_META\_CLIENTID</b><br />
Type: `string`<br />

Unique identifier for client connections established with Kafka.

### pumps.kafka.meta.topic

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_META\_TOPIC</b><br />
Type: `string`<br />

The topic that the writer will produce messages to.

### pumps.kafka.meta.timeout

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_META\_TIMEOUT</b><br />
Type: `interface{}`<br />

Timeout is the maximum amount of seconds to wait for a connect or write to complete.

### pumps.kafka.meta.compressed

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_META\_COMPRESSED</b><br />
Type: `bool`<br />

Enable "github.com/golang/snappy" codec to be used to compress Kafka messages. By default
is `false`.

### pumps.kafka.meta.meta\_data

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_META\_METADATA</b><br />
Type: `map[string]string`<br />

Can be used to set custom metadata inside the kafka message.

### pumps.kafka.meta.use\_ssl

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_META\_USESSL</b><br />
Type: `bool`<br />

Enables SSL connection.

### pumps.kafka.meta.ssl\_insecure\_skip\_verify

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_META\_SSLINSECURESKIPVERIFY</b><br />
Type: `bool`<br />

Controls whether the pump client verifies the kafka server's certificate chain and host
name.

### pumps.kafka.meta.ssl\_cert\_file

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_META\_SSLCERTFILE</b><br />
Type: `string`<br />

Can be used to set custom certificate file for authentication with kafka.

### pumps.kafka.meta.ssl\_key\_file

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_META\_SSLKEYFILE</b><br />
Type: `string`<br />

Can be used to set custom key file for authentication with kafka.

### pumps.kafka.meta.ssl\_ca\_file

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_META\_SSLCAFILE</b><br />
Type: `string`<br />

Path to the PEM file with trusted CA certificates that will be used to verify the Kafka server's certificate.

### pumps.kafka.meta.sasl\_mechanism

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_META\_SASLMECHANISM</b><br />
Type: `string`<br />

SASL mechanism configuration. Only "plain" and "scram" are supported.

### pumps.kafka.meta.sasl\_username

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_META\_USERNAME</b><br />
Type: `string`<br />

SASL username.

### pumps.kafka.meta.sasl\_password

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_META\_PASSWORD</b><br />
Type: `string`<br />

SASL password.

### pumps.kafka.meta.sasl\_algorithm

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_META\_ALGORITHM</b><br />
Type: `string`<br />

SASL algorithm. It's the algorithm specified for scram mechanism. It could be sha-512 or sha-256.
Defaults to "sha-256".

### pumps.kafka.meta.batch\_bytes

ENV: <b>TYK\_PMP\_PUMPS\_KAFKA\_META\_BATCHBYTES</b><br />
Type: `int`<br />

BatchBytes controls the maximum size of a request in bytes before it's sent to a partition.
If the value is 0, the writer will use the default value from kafka-go library (1MB).

### pumps.kinesis.name

ENV: <b>TYK\_PMP\_PUMPS\_KINESIS\_NAME</b><br />
Type: `string`<br />

The name of the pump. This is used to identify the pump in the logs.
Deprecated, use `type` instead.

### pumps.kinesis.type

ENV: <b>TYK\_PMP\_PUMPS\_KINESIS\_TYPE</b><br />
Type: `string`<br />

Sets the pump type. This is needed when the pump key does not equal to the pump name type.
Current valid types are: `mongo`, `mongo-pump-selective`, `mongo-pump-aggregate`, `csv`,
`elasticsearch`, `influx`, `influx2`, `moesif`, `statsd`, `segment`, `graylog`, `splunk`, `hybrid`, `prometheus`,
`logzio`, `dogstatsd`, `kafka`, `syslog`, `sql`, `sql_aggregate`, `stdout`, `timestream`, `mongo-graph`,
`sql-graph`, `sql-graph-aggregate`, `resurfaceio`.

### pumps.kinesis.filters

This feature adds a new configuration field in each pump called filters and its structure is
the following:

```{.json}  theme={null}
"filters":{
  "api_ids":[],
  "org_ids":[],
  "response_codes":[],
  "skip_api_ids":[],
  "skip_org_ids":[],
  "skip_response_codes":[]
}
```

The fields api\_ids, org\_ids and response\_codes works as allow list (APIs and orgs where we
want to send the analytics records) and the fields skip\_api\_ids, skip\_org\_ids and
skip\_response\_codes works as block list.

The priority is always block list configurations over allow list.

An example of configuration would be:

```{.json}  theme={null}
"csv": {
 "type": "csv",
 "filters": {
   "org_ids": ["org1","org2"]
 },
 "meta": {
   "csv_dir": "./bar"
 }
}
```

### pumps.kinesis.filters.org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_KINESIS\_FILTERS\_ORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of org\_ids.

### pumps.kinesis.filters.api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_KINESIS\_FILTERS\_APIIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of api\_ids.

### pumps.kinesis.filters.response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_KINESIS\_FILTERS\_RESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by an allow list of response\_codes.

### pumps.kinesis.filters.skip\_org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_KINESIS\_FILTERS\_SKIPPEDORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of org\_ids.

### pumps.kinesis.filters.skip\_api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_KINESIS\_FILTERS\_SKIPPEDAPIIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of api\_ids.

### pumps.kinesis.filters.skip\_response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_KINESIS\_FILTERS\_SKIPPEDRESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by a block list of response\_codes.

### pumps.kinesis.timeout

ENV: <b>TYK\_PMP\_PUMPS\_KINESIS\_TIMEOUT</b><br />
Type: `int`<br />

By default, a pump will wait forever for each write operation to complete; you can configure an optional timeout by setting the configuration option `timeout`.
If you have deployed multiple pumps, then you can configure each timeout independently. The timeout is in seconds and defaults to 0.

The timeout is configured within the main pump config as shown here; note that this example would configure a 5 second timeout:

```{.json}  theme={null}
"pump_name": {
  ...
  "timeout":5,
  "meta": {...}
}
```

Tyk will inform you if the pump's write operation is taking longer than the purging loop (configured via `purge_delay`) as this will mean that data is purged before being written to the target data sink.

If there is no timeout configured and pump's write operation is taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try to set a timeout for this pump.`

If there is a timeout configured, but pump's write operation is still taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try lowering the timeout configured for this pump.`.

### pumps.kinesis.omit\_detailed\_recording

ENV: <b>TYK\_PMP\_PUMPS\_KINESIS\_OMITDETAILEDRECORDING</b><br />
Type: `bool`<br />

Reduce the size of the traffic logs generated for each request by setting this to true. Tyk Pump will
then not include the `raw_request` and `raw_response` in the logs. Defaults to `false`.

### pumps.kinesis.max\_record\_size

ENV: <b>TYK\_PMP\_PUMPS\_KINESIS\_MAXRECORDSIZE</b><br />
Type: `int`<br />

Defines maximum size (in bytes) for Raw Request and Raw Response logs, this value defaults
to 0. If it is not set then tyk-pump will not trim any data and will store the full
information. This can also be set at a pump level. For example:

```{.json}  theme={null}
"csv": {
  "type": "csv",
  "max_record_size":1000,
  "meta": {
    "csv_dir": "./"
  }
}
```

### pumps.kinesis.ignore\_fields

ENV: <b>TYK\_PMP\_PUMPS\_KINESIS\_IGNOREFIELDS</b><br />
Type: `[]string`<br />

IgnoreFields defines a list of analytics fields that will be ignored when writing to the pump.
This can be used to avoid writing sensitive information to the Database, or data that you don't really need to have.
The field names must be the same as the JSON tags of the analytics record fields.
For example: `["api_key", "api_version"]`.

### pumps.kinesis.meta.EnvPrefix

ENV: <b>TYK\_PMP\_PUMPS\_KINESIS\_META\_ENVPREFIX</b><br />
Type: `string`<br />

The prefix for the environment variables that will be used to override the configuration.
Defaults to `TYK_PMP_PUMPS_KINESIS_META`

### pumps.kinesis.meta.StreamName

ENV: <b>TYK\_PMP\_PUMPS\_KINESIS\_META\_STREAMNAME</b><br />
Type: `string`<br />

A name to identify the stream. The stream name is scoped to the AWS account used by the application
that creates the stream. It is also scoped by AWS Region.
That is, two streams in two different AWS accounts can have the same name.
Two streams in the same AWS account but in two different Regions can also have the same name.

### pumps.kinesis.meta.Region

ENV: <b>TYK\_PMP\_PUMPS\_KINESIS\_META\_REGION</b><br />
Type: `string`<br />

AWS Region the Kinesis stream targets

### pumps.kinesis.meta.BatchSize

ENV: <b>TYK\_PMP\_PUMPS\_KINESIS\_META\_BATCHSIZE</b><br />
Type: `int`<br />

Each PutRecords (the function used in this pump)request can support up to 500 records.
Each record in the request can be as large as 1 MiB, up to a limit of 5 MiB for the entire request, including partition keys.
Each shard can support writes up to 1,000 records per second, up to a maximum data write total of 1 MiB per second.

### pumps.kinesis.meta.KMSKeyID

ENV: <b>TYK\_PMP\_PUMPS\_KINESIS\_META\_KMSKEYID</b><br />
Type: `string`<br />

The KMS Key ID used for server-side encryption of the Kinesis stream.
Defaults to an empty string if not provided.

### pumps.logzio.name

ENV: <b>TYK\_PMP\_PUMPS\_LOGZIO\_NAME</b><br />
Type: `string`<br />

The name of the pump. This is used to identify the pump in the logs.
Deprecated, use `type` instead.

### pumps.logzio.type

ENV: <b>TYK\_PMP\_PUMPS\_LOGZIO\_TYPE</b><br />
Type: `string`<br />

Sets the pump type. This is needed when the pump key does not equal to the pump name type.
Current valid types are: `mongo`, `mongo-pump-selective`, `mongo-pump-aggregate`, `csv`,
`elasticsearch`, `influx`, `influx2`, `moesif`, `statsd`, `segment`, `graylog`, `splunk`, `hybrid`, `prometheus`,
`logzio`, `dogstatsd`, `kafka`, `syslog`, `sql`, `sql_aggregate`, `stdout`, `timestream`, `mongo-graph`,
`sql-graph`, `sql-graph-aggregate`, `resurfaceio`.

### pumps.logzio.filters

This feature adds a new configuration field in each pump called filters and its structure is
the following:

```{.json}  theme={null}
"filters":{
  "api_ids":[],
  "org_ids":[],
  "response_codes":[],
  "skip_api_ids":[],
  "skip_org_ids":[],
  "skip_response_codes":[]
}
```

The fields api\_ids, org\_ids and response\_codes works as allow list (APIs and orgs where we
want to send the analytics records) and the fields skip\_api\_ids, skip\_org\_ids and
skip\_response\_codes works as block list.

The priority is always block list configurations over allow list.

An example of configuration would be:

```{.json}  theme={null}
"csv": {
 "type": "csv",
 "filters": {
   "org_ids": ["org1","org2"]
 },
 "meta": {
   "csv_dir": "./bar"
 }
}
```

### pumps.logzio.filters.org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_LOGZIO\_FILTERS\_ORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of org\_ids.

### pumps.logzio.filters.api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_LOGZIO\_FILTERS\_APIIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of api\_ids.

### pumps.logzio.filters.response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_LOGZIO\_FILTERS\_RESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by an allow list of response\_codes.

### pumps.logzio.filters.skip\_org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_LOGZIO\_FILTERS\_SKIPPEDORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of org\_ids.

### pumps.logzio.filters.skip\_api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_LOGZIO\_FILTERS\_SKIPPEDAPIIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of api\_ids.

### pumps.logzio.filters.skip\_response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_LOGZIO\_FILTERS\_SKIPPEDRESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by a block list of response\_codes.

### pumps.logzio.timeout

ENV: <b>TYK\_PMP\_PUMPS\_LOGZIO\_TIMEOUT</b><br />
Type: `int`<br />

By default, a pump will wait forever for each write operation to complete; you can configure an optional timeout by setting the configuration option `timeout`.
If you have deployed multiple pumps, then you can configure each timeout independently. The timeout is in seconds and defaults to 0.

The timeout is configured within the main pump config as shown here; note that this example would configure a 5 second timeout:

```{.json}  theme={null}
"pump_name": {
  ...
  "timeout":5,
  "meta": {...}
}
```

Tyk will inform you if the pump's write operation is taking longer than the purging loop (configured via `purge_delay`) as this will mean that data is purged before being written to the target data sink.

If there is no timeout configured and pump's write operation is taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try to set a timeout for this pump.`

If there is a timeout configured, but pump's write operation is still taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try lowering the timeout configured for this pump.`.

### pumps.logzio.omit\_detailed\_recording

ENV: <b>TYK\_PMP\_PUMPS\_LOGZIO\_OMITDETAILEDRECORDING</b><br />
Type: `bool`<br />

Reduce the size of the traffic logs generated for each request by setting this to true. Tyk Pump will
then not include the `raw_request` and `raw_response` in the logs. Defaults to `false`.

### pumps.logzio.max\_record\_size

ENV: <b>TYK\_PMP\_PUMPS\_LOGZIO\_MAXRECORDSIZE</b><br />
Type: `int`<br />

Defines maximum size (in bytes) for Raw Request and Raw Response logs, this value defaults
to 0. If it is not set then tyk-pump will not trim any data and will store the full
information. This can also be set at a pump level. For example:

```{.json}  theme={null}
"csv": {
  "type": "csv",
  "max_record_size":1000,
  "meta": {
    "csv_dir": "./"
  }
}
```

### pumps.logzio.ignore\_fields

ENV: <b>TYK\_PMP\_PUMPS\_LOGZIO\_IGNOREFIELDS</b><br />
Type: `[]string`<br />

IgnoreFields defines a list of analytics fields that will be ignored when writing to the pump.
This can be used to avoid writing sensitive information to the Database, or data that you don't really need to have.
The field names must be the same as the JSON tags of the analytics record fields.
For example: `["api_key", "api_version"]`.

### pumps.logzio.meta.EnvPrefix

ENV: <b>TYK\_PMP\_PUMPS\_LOGZIO\_META\_ENVPREFIX</b><br />
Type: `string`<br />

The prefix for the environment variables that will be used to override the configuration.
Defaults to `TYK_PMP_PUMPS_LOGZIO_META`

### pumps.logzio.meta.check\_disk\_space

ENV: <b>TYK\_PMP\_PUMPS\_LOGZIO\_META\_CHECKDISKSPACE</b><br />
Type: `bool`<br />

Set the sender to check if it crosses the maximum allowed disk usage. Default value is
`true`.

### pumps.logzio.meta.disk\_threshold

ENV: <b>TYK\_PMP\_PUMPS\_LOGZIO\_META\_DISKTHRESHOLD</b><br />
Type: `int`<br />

Set disk queue threshold, once the threshold is crossed the sender will not enqueue the
received logs. Default value is `98` (percentage of disk).

### pumps.logzio.meta.drain\_duration

ENV: <b>TYK\_PMP\_PUMPS\_LOGZIO\_META\_DRAINDURATION</b><br />
Type: `string`<br />

Set drain duration (flush logs on disk). Default value is `3s`.

### pumps.logzio.meta.queue\_dir

ENV: <b>TYK\_PMP\_PUMPS\_LOGZIO\_META\_QUEUEDIR</b><br />
Type: `string`<br />

The directory for the queue.

### pumps.logzio.meta.token

ENV: <b>TYK\_PMP\_PUMPS\_LOGZIO\_META\_TOKEN</b><br />
Type: `string`<br />

Token for sending data to your logzio account.

### pumps.logzio.meta.url

ENV: <b>TYK\_PMP\_PUMPS\_LOGZIO\_META\_URL</b><br />
Type: `string`<br />

If you do not want to use the default Logzio url i.e. when using a proxy. Default is
`https://listener.logz.io:8071`.

### pumps.moesif.name

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_NAME</b><br />
Type: `string`<br />

The name of the pump. This is used to identify the pump in the logs.
Deprecated, use `type` instead.

### pumps.moesif.type

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_TYPE</b><br />
Type: `string`<br />

Sets the pump type. This is needed when the pump key does not equal to the pump name type.
Current valid types are: `mongo`, `mongo-pump-selective`, `mongo-pump-aggregate`, `csv`,
`elasticsearch`, `influx`, `influx2`, `moesif`, `statsd`, `segment`, `graylog`, `splunk`, `hybrid`, `prometheus`,
`logzio`, `dogstatsd`, `kafka`, `syslog`, `sql`, `sql_aggregate`, `stdout`, `timestream`, `mongo-graph`,
`sql-graph`, `sql-graph-aggregate`, `resurfaceio`.

### pumps.moesif.filters

This feature adds a new configuration field in each pump called filters and its structure is
the following:

```{.json}  theme={null}
"filters":{
  "api_ids":[],
  "org_ids":[],
  "response_codes":[],
  "skip_api_ids":[],
  "skip_org_ids":[],
  "skip_response_codes":[]
}
```

The fields api\_ids, org\_ids and response\_codes works as allow list (APIs and orgs where we
want to send the analytics records) and the fields skip\_api\_ids, skip\_org\_ids and
skip\_response\_codes works as block list.

The priority is always block list configurations over allow list.

An example of configuration would be:

```{.json}  theme={null}
"csv": {
 "type": "csv",
 "filters": {
   "org_ids": ["org1","org2"]
 },
 "meta": {
   "csv_dir": "./bar"
 }
}
```

### pumps.moesif.filters.org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_FILTERS\_ORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of org\_ids.

### pumps.moesif.filters.api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_FILTERS\_APIIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of api\_ids.

### pumps.moesif.filters.response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_FILTERS\_RESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by an allow list of response\_codes.

### pumps.moesif.filters.skip\_org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_FILTERS\_SKIPPEDORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of org\_ids.

### pumps.moesif.filters.skip\_api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_FILTERS\_SKIPPEDAPIIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of api\_ids.

### pumps.moesif.filters.skip\_response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_FILTERS\_SKIPPEDRESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by a block list of response\_codes.

### pumps.moesif.timeout

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_TIMEOUT</b><br />
Type: `int`<br />

By default, a pump will wait forever for each write operation to complete; you can configure an optional timeout by setting the configuration option `timeout`.
If you have deployed multiple pumps, then you can configure each timeout independently. The timeout is in seconds and defaults to 0.

The timeout is configured within the main pump config as shown here; note that this example would configure a 5 second timeout:

```{.json}  theme={null}
"pump_name": {
  ...
  "timeout":5,
  "meta": {...}
}
```

Tyk will inform you if the pump's write operation is taking longer than the purging loop (configured via `purge_delay`) as this will mean that data is purged before being written to the target data sink.

If there is no timeout configured and pump's write operation is taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try to set a timeout for this pump.`

If there is a timeout configured, but pump's write operation is still taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try lowering the timeout configured for this pump.`.

### pumps.moesif.omit\_detailed\_recording

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_OMITDETAILEDRECORDING</b><br />
Type: `bool`<br />

Reduce the size of the traffic logs generated for each request by setting this to true. Tyk Pump will
then not include the `raw_request` and `raw_response` in the logs. Defaults to `false`.

### pumps.moesif.max\_record\_size

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_MAXRECORDSIZE</b><br />
Type: `int`<br />

Defines maximum size (in bytes) for Raw Request and Raw Response logs, this value defaults
to 0. If it is not set then tyk-pump will not trim any data and will store the full
information. This can also be set at a pump level. For example:

```{.json}  theme={null}
"csv": {
  "type": "csv",
  "max_record_size":1000,
  "meta": {
    "csv_dir": "./"
  }
}
```

### pumps.moesif.ignore\_fields

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_IGNOREFIELDS</b><br />
Type: `[]string`<br />

IgnoreFields defines a list of analytics fields that will be ignored when writing to the pump.
This can be used to avoid writing sensitive information to the Database, or data that you don't really need to have.
The field names must be the same as the JSON tags of the analytics record fields.
For example: `["api_key", "api_version"]`.

### pumps.moesif.meta.EnvPrefix

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_META\_ENVPREFIX</b><br />
Type: `string`<br />

The prefix for the environment variables that will be used to override the configuration.
Defaults to `TYK_PMP_PUMPS_MOESIF_META`

### pumps.moesif.meta.application\_id

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_META\_APPLICATIONID</b><br />
Type: `string`<br />

Moesif Application Id. You can find your Moesif Application Id from
[*Moesif Dashboard*](https://www.moesif.com/) -> *Top Right Menu* -> *API Keys* . Moesif
recommends creating separate Application Ids for each environment such as Production,
Staging, and Development to keep data isolated.

### pumps.moesif.meta.request\_header\_masks

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_META\_REQUESTHEADERMASKS</b><br />
Type: `[]string`<br />

An option to mask a specific request header field.

### pumps.moesif.meta.response\_header\_masks

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_META\_RESPONSEHEADERMASKS</b><br />
Type: `[]string`<br />

An option to mask a specific response header field.

### pumps.moesif.meta.request\_body\_masks

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_META\_REQUESTBODYMASKS</b><br />
Type: `[]string`<br />

An option to mask a specific - request body field.

### pumps.moesif.meta.response\_body\_masks

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_META\_RESPONSEBODYMASKS</b><br />
Type: `[]string`<br />

An option to mask a specific response body field.

### pumps.moesif.meta.disable\_capture\_request\_body

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_META\_DISABLECAPTUREREQUESTBODY</b><br />
Type: `bool`<br />

An option to disable logging of request body. Default value is `false`.

### pumps.moesif.meta.disable\_capture\_response\_body

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_META\_DISABLECAPTURERESPONSEBODY</b><br />
Type: `bool`<br />

An option to disable logging of response body. Default value is `false`.

### pumps.moesif.meta.user\_id\_header

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_META\_USERIDHEADER</b><br />
Type: `string`<br />

An optional field name to identify User from a request or response header.

### pumps.moesif.meta.company\_id\_header

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_META\_COMPANYIDHEADER</b><br />
Type: `string`<br />

An optional field name to identify Company (Account) from a request or response header.

### pumps.moesif.meta.enable\_bulk

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_META\_ENABLEBULK</b><br />
Type: `bool`<br />

Set this to `true` to enable `bulk_config`.

### pumps.moesif.meta.bulk\_config

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_META\_BULKCONFIG</b><br />
Type: `map[string]interface{}`<br />

Batch writing trigger configuration.

* `"event_queue_size"` - (optional) An optional field name which specify the maximum
  number of events to hold in queue before sending to Moesif. In case of network issues when
  not able to connect/send event to Moesif, skips adding new events to the queue to prevent
  memory overflow. Type: int. Default value is `10000`.
* `"batch_size"` - (optional) An optional field name which specify the maximum batch size
  when sending to Moesif. Type: int. Default value is `200`.
* `"timer_wake_up_seconds"` - (optional) An optional field which specifies a time (every n
  seconds) how often background thread runs to send events to moesif. Type: int. Default value
  is `2` seconds.

### pumps.moesif.meta.authorization\_header\_name

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_META\_AUTHORIZATIONHEADERNAME</b><br />
Type: `string`<br />

An optional request header field name to used to identify the User in Moesif. Default value
is `authorization`.

### pumps.moesif.meta.authorization\_user\_id\_field

ENV: <b>TYK\_PMP\_PUMPS\_MOESIF\_META\_AUTHORIZATIONUSERIDFIELD</b><br />
Type: `string`<br />

An optional field name use to parse the User from authorization header in Moesif. Default
value is `sub`.

### pumps.mongo.name

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_NAME</b><br />
Type: `string`<br />

The name of the pump. This is used to identify the pump in the logs.
Deprecated, use `type` instead.

### pumps.mongo.type

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_TYPE</b><br />
Type: `string`<br />

Sets the pump type. This is needed when the pump key does not equal to the pump name type.
Current valid types are: `mongo`, `mongo-pump-selective`, `mongo-pump-aggregate`, `csv`,
`elasticsearch`, `influx`, `influx2`, `moesif`, `statsd`, `segment`, `graylog`, `splunk`, `hybrid`, `prometheus`,
`logzio`, `dogstatsd`, `kafka`, `syslog`, `sql`, `sql_aggregate`, `stdout`, `timestream`, `mongo-graph`,
`sql-graph`, `sql-graph-aggregate`, `resurfaceio`.

### pumps.mongo.filters

This feature adds a new configuration field in each pump called filters and its structure is
the following:

```{.json}  theme={null}
"filters":{
  "api_ids":[],
  "org_ids":[],
  "response_codes":[],
  "skip_api_ids":[],
  "skip_org_ids":[],
  "skip_response_codes":[]
}
```

The fields api\_ids, org\_ids and response\_codes works as allow list (APIs and orgs where we
want to send the analytics records) and the fields skip\_api\_ids, skip\_org\_ids and
skip\_response\_codes works as block list.

The priority is always block list configurations over allow list.

An example of configuration would be:

```{.json}  theme={null}
"csv": {
 "type": "csv",
 "filters": {
   "org_ids": ["org1","org2"]
 },
 "meta": {
   "csv_dir": "./bar"
 }
}
```

### pumps.mongo.filters.org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_FILTERS\_ORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of org\_ids.

### pumps.mongo.filters.api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_FILTERS\_APIIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of api\_ids.

### pumps.mongo.filters.response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_FILTERS\_RESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by an allow list of response\_codes.

### pumps.mongo.filters.skip\_org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_FILTERS\_SKIPPEDORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of org\_ids.

### pumps.mongo.filters.skip\_api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_FILTERS\_SKIPPEDAPIIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of api\_ids.

### pumps.mongo.filters.skip\_response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_FILTERS\_SKIPPEDRESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by a block list of response\_codes.

### pumps.mongo.timeout

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_TIMEOUT</b><br />
Type: `int`<br />

By default, a pump will wait forever for each write operation to complete; you can configure an optional timeout by setting the configuration option `timeout`.
If you have deployed multiple pumps, then you can configure each timeout independently. The timeout is in seconds and defaults to 0.

The timeout is configured within the main pump config as shown here; note that this example would configure a 5 second timeout:

```{.json}  theme={null}
"pump_name": {
  ...
  "timeout":5,
  "meta": {...}
}
```

Tyk will inform you if the pump's write operation is taking longer than the purging loop (configured via `purge_delay`) as this will mean that data is purged before being written to the target data sink.

If there is no timeout configured and pump's write operation is taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try to set a timeout for this pump.`

If there is a timeout configured, but pump's write operation is still taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try lowering the timeout configured for this pump.`.

### pumps.mongo.omit\_detailed\_recording

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_OMITDETAILEDRECORDING</b><br />
Type: `bool`<br />

Reduce the size of the traffic logs generated for each request by setting this to true. Tyk Pump will
then not include the `raw_request` and `raw_response` in the logs. Defaults to `false`.

### pumps.mongo.max\_record\_size

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_MAXRECORDSIZE</b><br />
Type: `int`<br />

Defines maximum size (in bytes) for Raw Request and Raw Response logs, this value defaults
to 0. If it is not set then tyk-pump will not trim any data and will store the full
information. This can also be set at a pump level. For example:

```{.json}  theme={null}
"csv": {
  "type": "csv",
  "max_record_size":1000,
  "meta": {
    "csv_dir": "./"
  }
}
```

### pumps.mongo.ignore\_fields

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_IGNOREFIELDS</b><br />
Type: `[]string`<br />

IgnoreFields defines a list of analytics fields that will be ignored when writing to the pump.
This can be used to avoid writing sensitive information to the Database, or data that you don't really need to have.
The field names must be the same as the JSON tags of the analytics record fields.
For example: `["api_key", "api_version"]`.

### pumps.mongo.meta.EnvPrefix

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_META\_ENVPREFIX</b><br />
Type: `string`<br />

Prefix for the environment variables that will be used to override the configuration.
Defaults to `TYK_PMP_PUMPS_MONGO_META` for Mongo Pump
`TYK_PMP_PUMPS_UPTIME_META` for Uptime Pump
`TYK_PMP_PUMPS_MONGOAGGREGATE_META` for Mongo Aggregate Pump
`TYK_PMP_PUMPS_MONGOSELECTIVE_META` for Mongo Selective Pump
`TYK_PMP_PUMPS_MONGOGRAPH_META` for Mongo Graph Pump.

### pumps.mongo.meta.mongo\_url

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_META\_MONGOURL</b><br />
Type: `string`<br />

The full URL to your MongoDB instance, this can be a clustered instance if necessary and
should include the database and username / password data.

### pumps.mongo.meta.mongo\_use\_ssl

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_META\_MONGOUSESSL</b><br />
Type: `bool`<br />

Set to true to enable Mongo SSL connection.

### pumps.mongo.meta.mongo\_ssl\_insecure\_skip\_verify

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_META\_MONGOSSLINSECURESKIPVERIFY</b><br />
Type: `bool`<br />

Allows the use of self-signed certificates when connecting to an encrypted MongoDB database.

### pumps.mongo.meta.mongo\_ssl\_allow\_invalid\_hostnames

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_META\_MONGOSSLALLOWINVALIDHOSTNAMES</b><br />
Type: `bool`<br />

Ignore hostname check when it differs from the original (for example with SSH tunneling).
The rest of the TLS verification will still be performed.

### pumps.mongo.meta.mongo\_ssl\_ca\_file

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_META\_MONGOSSLCAFILE</b><br />
Type: `string`<br />

Path to the PEM file with trusted root certificates

### pumps.mongo.meta.mongo\_ssl\_pem\_keyfile

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_META\_MONGOSSLPEMKEYFILE</b><br />
Type: `string`<br />

Path to the PEM file which contains both client certificate and private key. This is
required for Mutual TLS.

### pumps.mongo.meta.mongo\_db\_type

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_META\_MONGODBTYPE</b><br />
Type: `int`<br />

Specifies the mongo DB Type. If it's 0, it means that you are using standard mongo db. If it's 1 it means you are using AWS Document DB. If it's 2, it means you are using CosmosDB.
Defaults to Standard mongo (0).

### pumps.mongo.meta.omit\_index\_creation

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_META\_OMITINDEXCREATION</b><br />
Type: `bool`<br />

Set to true to disable the default tyk index creation.

### pumps.mongo.meta.mongo\_session\_consistency

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_META\_MONGOSESSIONCONSISTENCY</b><br />
Type: `string`<br />

Set the consistency mode for the session, it defaults to `Strong`. The valid values are: strong, monotonic, eventual.

### pumps.mongo.meta.driver

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_META\_MONGODRIVERTYPE</b><br />
Type: `string`<br />

MongoDriverType is the type of the driver (library) to use. The valid values are: “mongo-go” and “mgo”.
Since v1.9, the default driver is "mongo-go". Check out this guide to [learn about MongoDB drivers supported by Tyk Pump](https://github.com/TykTechnologies/tyk-pump#driver-type).

### pumps.mongo.meta.mongo\_direct\_connection

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_META\_MONGODIRECTCONNECTION</b><br />
Type: `bool`<br />

MongoDirectConnection informs whether to establish connections only with the specified seed servers,
or to obtain information for the whole cluster and establish connections with further servers too.
If true, the client will only connect to the host provided in the ConnectionString
and won't attempt to discover other hosts in the cluster. Useful when network restrictions
prevent discovery, such as with SSH tunneling. Default is false.

### pumps.mongo.meta.collection\_name

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_META\_COLLECTIONNAME</b><br />
Type: `string`<br />

Specifies the mongo collection name.

### pumps.mongo.meta.max\_insert\_batch\_size\_bytes

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_META\_MAXINSERTBATCHSIZEBYTES</b><br />
Type: `int`<br />

Maximum insert batch size for mongo selective pump. If the batch we are writing surpasses this value, it will be sent in multiple batches.
Defaults to 10Mb.

### pumps.mongo.meta.max\_document\_size\_bytes

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_META\_MAXDOCUMENTSIZEBYTES</b><br />
Type: `int`<br />

Maximum document size. If the document exceed this value, it will be skipped.
Defaults to 10Mb.

### pumps.mongo.meta.collection\_cap\_max\_size\_bytes

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_META\_COLLECTIONCAPMAXSIZEBYTES</b><br />
Type: `int`<br />

Amount of bytes of the capped collection in 64bits architectures.
Defaults to 5GB.

### pumps.mongo.meta.collection\_cap\_enable

ENV: <b>TYK\_PMP\_PUMPS\_MONGO\_META\_COLLECTIONCAPENABLE</b><br />
Type: `bool`<br />

Enable collection capping. It's used to set a maximum size of the collection.

### pumps.mongoaggregate.name

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_NAME</b><br />
Type: `string`<br />

The name of the pump. This is used to identify the pump in the logs.
Deprecated, use `type` instead.

### pumps.mongoaggregate.type

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_TYPE</b><br />
Type: `string`<br />

Sets the pump type. This is needed when the pump key does not equal to the pump name type.
Current valid types are: `mongo`, `mongo-pump-selective`, `mongo-pump-aggregate`, `csv`,
`elasticsearch`, `influx`, `influx2`, `moesif`, `statsd`, `segment`, `graylog`, `splunk`, `hybrid`, `prometheus`,
`logzio`, `dogstatsd`, `kafka`, `syslog`, `sql`, `sql_aggregate`, `stdout`, `timestream`, `mongo-graph`,
`sql-graph`, `sql-graph-aggregate`, `resurfaceio`.

### pumps.mongoaggregate.filters

This feature adds a new configuration field in each pump called filters and its structure is
the following:

```{.json}  theme={null}
"filters":{
  "api_ids":[],
  "org_ids":[],
  "response_codes":[],
  "skip_api_ids":[],
  "skip_org_ids":[],
  "skip_response_codes":[]
}
```

The fields api\_ids, org\_ids and response\_codes works as allow list (APIs and orgs where we
want to send the analytics records) and the fields skip\_api\_ids, skip\_org\_ids and
skip\_response\_codes works as block list.

The priority is always block list configurations over allow list.

An example of configuration would be:

```{.json}  theme={null}
"csv": {
 "type": "csv",
 "filters": {
   "org_ids": ["org1","org2"]
 },
 "meta": {
   "csv_dir": "./bar"
 }
}
```

### pumps.mongoaggregate.filters.org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_FILTERS\_ORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of org\_ids.

### pumps.mongoaggregate.filters.api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_FILTERS\_APIIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of api\_ids.

### pumps.mongoaggregate.filters.response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_FILTERS\_RESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by an allow list of response\_codes.

### pumps.mongoaggregate.filters.skip\_org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_FILTERS\_SKIPPEDORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of org\_ids.

### pumps.mongoaggregate.filters.skip\_api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_FILTERS\_SKIPPEDAPIIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of api\_ids.

### pumps.mongoaggregate.filters.skip\_response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_FILTERS\_SKIPPEDRESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by a block list of response\_codes.

### pumps.mongoaggregate.timeout

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_TIMEOUT</b><br />
Type: `int`<br />

By default, a pump will wait forever for each write operation to complete; you can configure an optional timeout by setting the configuration option `timeout`.
If you have deployed multiple pumps, then you can configure each timeout independently. The timeout is in seconds and defaults to 0.

The timeout is configured within the main pump config as shown here; note that this example would configure a 5 second timeout:

```{.json}  theme={null}
"pump_name": {
  ...
  "timeout":5,
  "meta": {...}
}
```

Tyk will inform you if the pump's write operation is taking longer than the purging loop (configured via `purge_delay`) as this will mean that data is purged before being written to the target data sink.

If there is no timeout configured and pump's write operation is taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try to set a timeout for this pump.`

If there is a timeout configured, but pump's write operation is still taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try lowering the timeout configured for this pump.`.

### pumps.mongoaggregate.omit\_detailed\_recording

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_OMITDETAILEDRECORDING</b><br />
Type: `bool`<br />

Reduce the size of the traffic logs generated for each request by setting this to true. Tyk Pump will
then not include the `raw_request` and `raw_response` in the logs. Defaults to `false`.

### pumps.mongoaggregate.max\_record\_size

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_MAXRECORDSIZE</b><br />
Type: `int`<br />

Defines maximum size (in bytes) for Raw Request and Raw Response logs, this value defaults
to 0. If it is not set then tyk-pump will not trim any data and will store the full
information. This can also be set at a pump level. For example:

```{.json}  theme={null}
"csv": {
  "type": "csv",
  "max_record_size":1000,
  "meta": {
    "csv_dir": "./"
  }
}
```

### pumps.mongoaggregate.ignore\_fields

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_IGNOREFIELDS</b><br />
Type: `[]string`<br />

IgnoreFields defines a list of analytics fields that will be ignored when writing to the pump.
This can be used to avoid writing sensitive information to the Database, or data that you don't really need to have.
The field names must be the same as the JSON tags of the analytics record fields.
For example: `["api_key", "api_version"]`.

### pumps.mongoaggregate.meta.EnvPrefix

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_META\_ENVPREFIX</b><br />
Type: `string`<br />

Prefix for the environment variables that will be used to override the configuration.
Defaults to `TYK_PMP_PUMPS_MONGO_META` for Mongo Pump
`TYK_PMP_PUMPS_UPTIME_META` for Uptime Pump
`TYK_PMP_PUMPS_MONGOAGGREGATE_META` for Mongo Aggregate Pump
`TYK_PMP_PUMPS_MONGOSELECTIVE_META` for Mongo Selective Pump
`TYK_PMP_PUMPS_MONGOGRAPH_META` for Mongo Graph Pump.

### pumps.mongoaggregate.meta.mongo\_url

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_META\_MONGOURL</b><br />
Type: `string`<br />

The full URL to your MongoDB instance, this can be a clustered instance if necessary and
should include the database and username / password data.

### pumps.mongoaggregate.meta.mongo\_use\_ssl

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_META\_MONGOUSESSL</b><br />
Type: `bool`<br />

Set to true to enable Mongo SSL connection.

### pumps.mongoaggregate.meta.mongo\_ssl\_insecure\_skip\_verify

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_META\_MONGOSSLINSECURESKIPVERIFY</b><br />
Type: `bool`<br />

Allows the use of self-signed certificates when connecting to an encrypted MongoDB database.

### pumps.mongoaggregate.meta.mongo\_ssl\_allow\_invalid\_hostnames

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_META\_MONGOSSLALLOWINVALIDHOSTNAMES</b><br />
Type: `bool`<br />

Ignore hostname check when it differs from the original (for example with SSH tunneling).
The rest of the TLS verification will still be performed.

### pumps.mongoaggregate.meta.mongo\_ssl\_ca\_file

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_META\_MONGOSSLCAFILE</b><br />
Type: `string`<br />

Path to the PEM file with trusted root certificates

### pumps.mongoaggregate.meta.mongo\_ssl\_pem\_keyfile

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_META\_MONGOSSLPEMKEYFILE</b><br />
Type: `string`<br />

Path to the PEM file which contains both client certificate and private key. This is
required for Mutual TLS.

### pumps.mongoaggregate.meta.mongo\_db\_type

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_META\_MONGODBTYPE</b><br />
Type: `int`<br />

Specifies the mongo DB Type. If it's 0, it means that you are using standard mongo db. If it's 1 it means you are using AWS Document DB. If it's 2, it means you are using CosmosDB.
Defaults to Standard mongo (0).

### pumps.mongoaggregate.meta.omit\_index\_creation

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_META\_OMITINDEXCREATION</b><br />
Type: `bool`<br />

Set to true to disable the default tyk index creation.

### pumps.mongoaggregate.meta.mongo\_session\_consistency

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_META\_MONGOSESSIONCONSISTENCY</b><br />
Type: `string`<br />

Set the consistency mode for the session, it defaults to `Strong`. The valid values are: strong, monotonic, eventual.

### pumps.mongoaggregate.meta.driver

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_META\_MONGODRIVERTYPE</b><br />
Type: `string`<br />

MongoDriverType is the type of the driver (library) to use. The valid values are: “mongo-go” and “mgo”.
Since v1.9, the default driver is "mongo-go". Check out this guide to [learn about MongoDB drivers supported by Tyk Pump](https://github.com/TykTechnologies/tyk-pump#driver-type).

### pumps.mongoaggregate.meta.mongo\_direct\_connection

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_META\_MONGODIRECTCONNECTION</b><br />
Type: `bool`<br />

MongoDirectConnection informs whether to establish connections only with the specified seed servers,
or to obtain information for the whole cluster and establish connections with further servers too.
If true, the client will only connect to the host provided in the ConnectionString
and won't attempt to discover other hosts in the cluster. Useful when network restrictions
prevent discovery, such as with SSH tunneling. Default is false.

### pumps.mongoaggregate.meta.use\_mixed\_collection

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_META\_USEMIXEDCOLLECTION</b><br />
Type: `bool`<br />

If set to `true` the Mongo Aggregate pump will send analytics to two collections:

* `z_tyk_analyticz_aggregate_{ORG ID}`
* `tyk_analytics_aggregates`
  When set to 'false' your pump will only store analytics to `z_tyk_analyticz_aggregate_{ORG ID}`.

### pumps.mongoaggregate.meta.track\_all\_paths

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_META\_TRACKALLPATHS</b><br />
Type: `bool`<br />

Specifies if it should store aggregated data for all the endpoints. By default, `false`
which means that only store aggregated data for `tracked endpoints`.

### pumps.mongoaggregate.meta.ignore\_tag\_prefix\_list

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_META\_IGNORETAGPREFIXLIST</b><br />
Type: `[]string`<br />

Specifies prefixes of tags that should be ignored.

### pumps.mongoaggregate.meta.threshold\_len\_tag\_list

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_META\_THRESHOLDLENTAGLIST</b><br />
Type: `int`<br />

Determines the threshold of amount of tags of an aggregation. If the amount of tags is superior to the threshold,
it will print an alert.
Defaults to 1000.

### pumps.mongoaggregate.meta.store\_analytics\_per\_minute

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_META\_STOREANALYTICSPERMINUTE</b><br />
Type: `bool`<br />

Determines if the aggregations should be made per minute (true) or per hour (false).

### pumps.mongoaggregate.meta.aggregation\_time

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_META\_AGGREGATIONTIME</b><br />
Type: `int`<br />

Determines the amount of time the aggregations should be made (in minutes). It defaults to the max value is 60 and the minimum is 1.
If StoreAnalyticsPerMinute is set to true, this field will be skipped.

### pumps.mongoaggregate.meta.enable\_aggregate\_self\_healing

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_META\_ENABLEAGGREGATESELFHEALING</b><br />
Type: `bool`<br />

Determines if the self healing will be activated or not.
Self Healing allows pump to handle Mongo document's max-size errors by creating a new document when the max-size is reached.
It also divide by 2 the AggregationTime field to avoid the same error in the future.

### pumps.mongoaggregate.meta.ignore\_aggregations

ENV: <b>TYK\_PMP\_PUMPS\_MONGOAGGREGATE\_META\_IGNOREAGGREGATIONSLIST</b><br />
Type: `[]string`<br />

This list determines which aggregations are going to be dropped and not stored in the collection.
Posible values are: "APIID","errors","versions","apikeys","oauthids","geo","tags","endpoints","keyendpoints",
"oauthendpoints", and "apiendpoints".

### pumps.mongoselective.name

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_NAME</b><br />
Type: `string`<br />

The name of the pump. This is used to identify the pump in the logs.
Deprecated, use `type` instead.

### pumps.mongoselective.type

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_TYPE</b><br />
Type: `string`<br />

Sets the pump type. This is needed when the pump key does not equal to the pump name type.
Current valid types are: `mongo`, `mongo-pump-selective`, `mongo-pump-aggregate`, `csv`,
`elasticsearch`, `influx`, `influx2`, `moesif`, `statsd`, `segment`, `graylog`, `splunk`, `hybrid`, `prometheus`,
`logzio`, `dogstatsd`, `kafka`, `syslog`, `sql`, `sql_aggregate`, `stdout`, `timestream`, `mongo-graph`,
`sql-graph`, `sql-graph-aggregate`, `resurfaceio`.

### pumps.mongoselective.filters

This feature adds a new configuration field in each pump called filters and its structure is
the following:

```{.json}  theme={null}
"filters":{
  "api_ids":[],
  "org_ids":[],
  "response_codes":[],
  "skip_api_ids":[],
  "skip_org_ids":[],
  "skip_response_codes":[]
}
```

The fields api\_ids, org\_ids and response\_codes works as allow list (APIs and orgs where we
want to send the analytics records) and the fields skip\_api\_ids, skip\_org\_ids and
skip\_response\_codes works as block list.

The priority is always block list configurations over allow list.

An example of configuration would be:

```{.json}  theme={null}
"csv": {
 "type": "csv",
 "filters": {
   "org_ids": ["org1","org2"]
 },
 "meta": {
   "csv_dir": "./bar"
 }
}
```

### pumps.mongoselective.filters.org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_FILTERS\_ORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of org\_ids.

### pumps.mongoselective.filters.api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_FILTERS\_APIIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of api\_ids.

### pumps.mongoselective.filters.response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_FILTERS\_RESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by an allow list of response\_codes.

### pumps.mongoselective.filters.skip\_org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_FILTERS\_SKIPPEDORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of org\_ids.

### pumps.mongoselective.filters.skip\_api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_FILTERS\_SKIPPEDAPIIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of api\_ids.

### pumps.mongoselective.filters.skip\_response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_FILTERS\_SKIPPEDRESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by a block list of response\_codes.

### pumps.mongoselective.timeout

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_TIMEOUT</b><br />
Type: `int`<br />

By default, a pump will wait forever for each write operation to complete; you can configure an optional timeout by setting the configuration option `timeout`.
If you have deployed multiple pumps, then you can configure each timeout independently. The timeout is in seconds and defaults to 0.

The timeout is configured within the main pump config as shown here; note that this example would configure a 5 second timeout:

```{.json}  theme={null}
"pump_name": {
  ...
  "timeout":5,
  "meta": {...}
}
```

Tyk will inform you if the pump's write operation is taking longer than the purging loop (configured via `purge_delay`) as this will mean that data is purged before being written to the target data sink.

If there is no timeout configured and pump's write operation is taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try to set a timeout for this pump.`

If there is a timeout configured, but pump's write operation is still taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try lowering the timeout configured for this pump.`.

### pumps.mongoselective.omit\_detailed\_recording

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_OMITDETAILEDRECORDING</b><br />
Type: `bool`<br />

Reduce the size of the traffic logs generated for each request by setting this to true. Tyk Pump will
then not include the `raw_request` and `raw_response` in the logs. Defaults to `false`.

### pumps.mongoselective.max\_record\_size

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_MAXRECORDSIZE</b><br />
Type: `int`<br />

Defines maximum size (in bytes) for Raw Request and Raw Response logs, this value defaults
to 0. If it is not set then tyk-pump will not trim any data and will store the full
information. This can also be set at a pump level. For example:

```{.json}  theme={null}
"csv": {
  "type": "csv",
  "max_record_size":1000,
  "meta": {
    "csv_dir": "./"
  }
}
```

### pumps.mongoselective.ignore\_fields

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_IGNOREFIELDS</b><br />
Type: `[]string`<br />

IgnoreFields defines a list of analytics fields that will be ignored when writing to the pump.
This can be used to avoid writing sensitive information to the Database, or data that you don't really need to have.
The field names must be the same as the JSON tags of the analytics record fields.
For example: `["api_key", "api_version"]`.

### pumps.mongoselective.meta.EnvPrefix

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_META\_ENVPREFIX</b><br />
Type: `string`<br />

Prefix for the environment variables that will be used to override the configuration.
Defaults to `TYK_PMP_PUMPS_MONGO_META` for Mongo Pump
`TYK_PMP_PUMPS_UPTIME_META` for Uptime Pump
`TYK_PMP_PUMPS_MONGOAGGREGATE_META` for Mongo Aggregate Pump
`TYK_PMP_PUMPS_MONGOSELECTIVE_META` for Mongo Selective Pump
`TYK_PMP_PUMPS_MONGOGRAPH_META` for Mongo Graph Pump.

### pumps.mongoselective.meta.mongo\_url

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_META\_MONGOURL</b><br />
Type: `string`<br />

The full URL to your MongoDB instance, this can be a clustered instance if necessary and
should include the database and username / password data.

### pumps.mongoselective.meta.mongo\_use\_ssl

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_META\_MONGOUSESSL</b><br />
Type: `bool`<br />

Set to true to enable Mongo SSL connection.

### pumps.mongoselective.meta.mongo\_ssl\_insecure\_skip\_verify

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_META\_MONGOSSLINSECURESKIPVERIFY</b><br />
Type: `bool`<br />

Allows the use of self-signed certificates when connecting to an encrypted MongoDB database.

### pumps.mongoselective.meta.mongo\_ssl\_allow\_invalid\_hostnames

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_META\_MONGOSSLALLOWINVALIDHOSTNAMES</b><br />
Type: `bool`<br />

Ignore hostname check when it differs from the original (for example with SSH tunneling).
The rest of the TLS verification will still be performed.

### pumps.mongoselective.meta.mongo\_ssl\_ca\_file

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_META\_MONGOSSLCAFILE</b><br />
Type: `string`<br />

Path to the PEM file with trusted root certificates

### pumps.mongoselective.meta.mongo\_ssl\_pem\_keyfile

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_META\_MONGOSSLPEMKEYFILE</b><br />
Type: `string`<br />

Path to the PEM file which contains both client certificate and private key. This is
required for Mutual TLS.

### pumps.mongoselective.meta.mongo\_db\_type

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_META\_MONGODBTYPE</b><br />
Type: `int`<br />

Specifies the mongo DB Type. If it's 0, it means that you are using standard mongo db. If it's 1 it means you are using AWS Document DB. If it's 2, it means you are using CosmosDB.
Defaults to Standard mongo (0).

### pumps.mongoselective.meta.omit\_index\_creation

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_META\_OMITINDEXCREATION</b><br />
Type: `bool`<br />

Set to true to disable the default tyk index creation.

### pumps.mongoselective.meta.mongo\_session\_consistency

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_META\_MONGOSESSIONCONSISTENCY</b><br />
Type: `string`<br />

Set the consistency mode for the session, it defaults to `Strong`. The valid values are: strong, monotonic, eventual.

### pumps.mongoselective.meta.driver

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_META\_MONGODRIVERTYPE</b><br />
Type: `string`<br />

MongoDriverType is the type of the driver (library) to use. The valid values are: “mongo-go” and “mgo”.
Since v1.9, the default driver is "mongo-go". Check out this guide to [learn about MongoDB drivers supported by Tyk Pump](https://github.com/TykTechnologies/tyk-pump#driver-type).

### pumps.mongoselective.meta.mongo\_direct\_connection

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_META\_MONGODIRECTCONNECTION</b><br />
Type: `bool`<br />

MongoDirectConnection informs whether to establish connections only with the specified seed servers,
or to obtain information for the whole cluster and establish connections with further servers too.
If true, the client will only connect to the host provided in the ConnectionString
and won't attempt to discover other hosts in the cluster. Useful when network restrictions
prevent discovery, such as with SSH tunneling. Default is false.

### pumps.mongoselective.meta.max\_insert\_batch\_size\_bytes

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_META\_MAXINSERTBATCHSIZEBYTES</b><br />
Type: `int`<br />

Maximum insert batch size for mongo selective pump. If the batch we are writing surpass this value, it will be send in multiple batchs.
Defaults to 10Mb.

### pumps.mongoselective.meta.max\_document\_size\_bytes

ENV: <b>TYK\_PMP\_PUMPS\_MONGOSELECTIVE\_META\_MAXDOCUMENTSIZEBYTES</b><br />
Type: `int`<br />

Maximum document size. If the document exceed this value, it will be skipped.
Defaults to 10Mb.

### pumps.prometheus.name

ENV: <b>TYK\_PMP\_PUMPS\_PROMETHEUS\_NAME</b><br />
Type: `string`<br />

The name of the pump. This is used to identify the pump in the logs.
Deprecated, use `type` instead.

### pumps.prometheus.type

ENV: <b>TYK\_PMP\_PUMPS\_PROMETHEUS\_TYPE</b><br />
Type: `string`<br />

Sets the pump type. This is needed when the pump key does not equal to the pump name type.
Current valid types are: `mongo`, `mongo-pump-selective`, `mongo-pump-aggregate`, `csv`,
`elasticsearch`, `influx`, `influx2`, `moesif`, `statsd`, `segment`, `graylog`, `splunk`, `hybrid`, `prometheus`,
`logzio`, `dogstatsd`, `kafka`, `syslog`, `sql`, `sql_aggregate`, `stdout`, `timestream`, `mongo-graph`,
`sql-graph`, `sql-graph-aggregate`, `resurfaceio`.

### pumps.prometheus.filters

This feature adds a new configuration field in each pump called filters and its structure is
the following:

```{.json}  theme={null}
"filters":{
  "api_ids":[],
  "org_ids":[],
  "response_codes":[],
  "skip_api_ids":[],
  "skip_org_ids":[],
  "skip_response_codes":[]
}
```

The fields api\_ids, org\_ids and response\_codes works as allow list (APIs and orgs where we
want to send the analytics records) and the fields skip\_api\_ids, skip\_org\_ids and
skip\_response\_codes works as block list.

The priority is always block list configurations over allow list.

An example of configuration would be:

```{.json}  theme={null}
"csv": {
 "type": "csv",
 "filters": {
   "org_ids": ["org1","org2"]
 },
 "meta": {
   "csv_dir": "./bar"
 }
}
```

### pumps.prometheus.filters.org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_PROMETHEUS\_FILTERS\_ORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of org\_ids.

### pumps.prometheus.filters.api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_PROMETHEUS\_FILTERS\_APIIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of api\_ids.

### pumps.prometheus.filters.response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_PROMETHEUS\_FILTERS\_RESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by an allow list of response\_codes.

### pumps.prometheus.filters.skip\_org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_PROMETHEUS\_FILTERS\_SKIPPEDORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of org\_ids.

### pumps.prometheus.filters.skip\_api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_PROMETHEUS\_FILTERS\_SKIPPEDAPIIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of api\_ids.

### pumps.prometheus.filters.skip\_response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_PROMETHEUS\_FILTERS\_SKIPPEDRESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by a block list of response\_codes.

### pumps.prometheus.timeout

ENV: <b>TYK\_PMP\_PUMPS\_PROMETHEUS\_TIMEOUT</b><br />
Type: `int`<br />

By default, a pump will wait forever for each write operation to complete; you can configure an optional timeout by setting the configuration option `timeout`.
If you have deployed multiple pumps, then you can configure each timeout independently. The timeout is in seconds and defaults to 0.

The timeout is configured within the main pump config as shown here; note that this example would configure a 5 second timeout:

```{.json}  theme={null}
"pump_name": {
  ...
  "timeout":5,
  "meta": {...}
}
```

Tyk will inform you if the pump's write operation is taking longer than the purging loop (configured via `purge_delay`) as this will mean that data is purged before being written to the target data sink.

If there is no timeout configured and pump's write operation is taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try to set a timeout for this pump.`

If there is a timeout configured, but pump's write operation is still taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try lowering the timeout configured for this pump.`.

### pumps.prometheus.omit\_detailed\_recording

ENV: <b>TYK\_PMP\_PUMPS\_PROMETHEUS\_OMITDETAILEDRECORDING</b><br />
Type: `bool`<br />

Reduce the size of the traffic logs generated for each request by setting this to true. Tyk Pump will
then not include the `raw_request` and `raw_response` in the logs. Defaults to `false`.

### pumps.prometheus.max\_record\_size

ENV: <b>TYK\_PMP\_PUMPS\_PROMETHEUS\_MAXRECORDSIZE</b><br />
Type: `int`<br />

Defines maximum size (in bytes) for Raw Request and Raw Response logs, this value defaults
to 0. If it is not set then tyk-pump will not trim any data and will store the full
information. This can also be set at a pump level. For example:

```{.json}  theme={null}
"csv": {
  "type": "csv",
  "max_record_size":1000,
  "meta": {
    "csv_dir": "./"
  }
}
```

### pumps.prometheus.ignore\_fields

ENV: <b>TYK\_PMP\_PUMPS\_PROMETHEUS\_IGNOREFIELDS</b><br />
Type: `[]string`<br />

IgnoreFields defines a list of analytics fields that will be ignored when writing to the pump.
This can be used to avoid writing sensitive information to the Database, or data that you don't really need to have.
The field names must be the same as the JSON tags of the analytics record fields.
For example: `["api_key", "api_version"]`.

### pumps.prometheus.meta.EnvPrefix

ENV: <b>TYK\_PMP\_PUMPS\_PROMETHEUS\_META\_ENVPREFIX</b><br />
Type: `string`<br />

Prefix for the environment variables that will be used to override the configuration.
Defaults to `TYK_PMP_PUMPS_PROMETHEUS_META`

### pumps.prometheus.meta.listen\_address

ENV: <b>TYK\_PMP\_PUMPS\_PROMETHEUS\_META\_ADDR</b><br />
Type: `string`<br />

The full URL to your Prometheus instance, {HOST_0}:{PORT_0}. For example `localhost:9090`.

### pumps.prometheus.meta.path

ENV: <b>TYK\_PMP\_PUMPS\_PROMETHEUS\_META\_PATH</b><br />
Type: `string`<br />

The path to the Prometheus collection. For example `/metrics`.

### pumps.prometheus.meta.aggregate\_observations

ENV: <b>TYK\_PMP\_PUMPS\_PROMETHEUS\_META\_AGGREGATEOBSERVATIONS</b><br />
Type: `bool`<br />

This will enable an experimental feature that will aggregate the histogram metrics request time values before exposing them to prometheus.
Enabling this will reduce the CPU usage of your prometheus pump but you will loose histogram precision. Experimental.

### pumps.prometheus.meta.disabled\_metrics

ENV: <b>TYK\_PMP\_PUMPS\_PROMETHEUS\_META\_DISABLEDMETRICS</b><br />
Type: `[]string`<br />

Metrics to exclude from exposition. Currently, excludes only the base metrics.

### pumps.prometheus.meta.track\_all\_paths

ENV: <b>TYK\_PMP\_PUMPS\_PROMETHEUS\_META\_TRACKALLPATHS</b><br />
Type: `bool`<br />

Specifies if it should expose aggregated metrics for all the endpoints. By default, `false`
which means that all APIs endpoints will be counted as 'unknown' unless the API uses the track endpoint plugin.

### pumps.prometheus.meta.custom\_metrics

ENV: <b>TYK\_PMP\_PUMPS\_PROMETHEUS\_META\_CUSTOMMETRICS</b><br />
Type: `CustomMetrics`<br />

Custom Prometheus metrics.

### pumps.splunk.name

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_NAME</b><br />
Type: `string`<br />

The name of the pump. This is used to identify the pump in the logs.
Deprecated, use `type` instead.

### pumps.splunk.type

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_TYPE</b><br />
Type: `string`<br />

Sets the pump type. This is needed when the pump key does not equal to the pump name type.
Current valid types are: `mongo`, `mongo-pump-selective`, `mongo-pump-aggregate`, `csv`,
`elasticsearch`, `influx`, `influx2`, `moesif`, `statsd`, `segment`, `graylog`, `splunk`, `hybrid`, `prometheus`,
`logzio`, `dogstatsd`, `kafka`, `syslog`, `sql`, `sql_aggregate`, `stdout`, `timestream`, `mongo-graph`,
`sql-graph`, `sql-graph-aggregate`, `resurfaceio`.

### pumps.splunk.filters

This feature adds a new configuration field in each pump called filters and its structure is
the following:

```{.json}  theme={null}
"filters":{
  "api_ids":[],
  "org_ids":[],
  "response_codes":[],
  "skip_api_ids":[],
  "skip_org_ids":[],
  "skip_response_codes":[]
}
```

The fields api\_ids, org\_ids and response\_codes works as allow list (APIs and orgs where we
want to send the analytics records) and the fields skip\_api\_ids, skip\_org\_ids and
skip\_response\_codes works as block list.

The priority is always block list configurations over allow list.

An example of configuration would be:

```{.json}  theme={null}
"csv": {
 "type": "csv",
 "filters": {
   "org_ids": ["org1","org2"]
 },
 "meta": {
   "csv_dir": "./bar"
 }
}
```

### pumps.splunk.filters.org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_FILTERS\_ORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of org\_ids.

### pumps.splunk.filters.api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_FILTERS\_APIIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of api\_ids.

### pumps.splunk.filters.response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_FILTERS\_RESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by an allow list of response\_codes.

### pumps.splunk.filters.skip\_org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_FILTERS\_SKIPPEDORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of org\_ids.

### pumps.splunk.filters.skip\_api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_FILTERS\_SKIPPEDAPIIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of api\_ids.

### pumps.splunk.filters.skip\_response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_FILTERS\_SKIPPEDRESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by a block list of response\_codes.

### pumps.splunk.timeout

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_TIMEOUT</b><br />
Type: `int`<br />

By default, a pump will wait forever for each write operation to complete; you can configure an optional timeout by setting the configuration option `timeout`.
If you have deployed multiple pumps, then you can configure each timeout independently. The timeout is in seconds and defaults to 0.

The timeout is configured within the main pump config as shown here; note that this example would configure a 5 second timeout:

```{.json}  theme={null}
"pump_name": {
  ...
  "timeout":5,
  "meta": {...}
}
```

Tyk will inform you if the pump's write operation is taking longer than the purging loop (configured via `purge_delay`) as this will mean that data is purged before being written to the target data sink.

If there is no timeout configured and pump's write operation is taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try to set a timeout for this pump.`

If there is a timeout configured, but pump's write operation is still taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try lowering the timeout configured for this pump.`.

### pumps.splunk.omit\_detailed\_recording

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_OMITDETAILEDRECORDING</b><br />
Type: `bool`<br />

Reduce the size of the traffic logs generated for each request by setting this to true. Tyk Pump will
then not include the `raw_request` and `raw_response` in the logs. Defaults to `false`.

### pumps.splunk.max\_record\_size

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_MAXRECORDSIZE</b><br />
Type: `int`<br />

Defines maximum size (in bytes) for Raw Request and Raw Response logs, this value defaults
to 0. If it is not set then tyk-pump will not trim any data and will store the full
information. This can also be set at a pump level. For example:

```{.json}  theme={null}
"csv": {
  "type": "csv",
  "max_record_size":1000,
  "meta": {
    "csv_dir": "./"
  }
}
```

### pumps.splunk.ignore\_fields

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_IGNOREFIELDS</b><br />
Type: `[]string`<br />

IgnoreFields defines a list of analytics fields that will be ignored when writing to the pump.
This can be used to avoid writing sensitive information to the Database, or data that you don't really need to have.
The field names must be the same as the JSON tags of the analytics record fields.
For example: `["api_key", "api_version"]`.

### pumps.splunk.meta.EnvPrefix

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_META\_ENVPREFIX</b><br />
Type: `string`<br />

The prefix for the environment variables that will be used to override the configuration.
Defaults to `TYK_PMP_PUMPS_SPLUNK_META`

### pumps.splunk.meta.collector\_token

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_META\_COLLECTORTOKEN</b><br />
Type: `string`<br />

Address of the datadog agent including host & port.

### pumps.splunk.meta.collector\_url

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_META\_COLLECTORURL</b><br />
Type: `string`<br />

Endpoint the Pump will send analytics too.  Should look something like:
`https://splunk:8088/services/collector/event`.

### pumps.splunk.meta.ssl\_insecure\_skip\_verify

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_META\_SSLINSECURESKIPVERIFY</b><br />
Type: `bool`<br />

Controls whether the pump client verifies the Splunk server's certificate chain and host name.

### pumps.splunk.meta.ssl\_cert\_file

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_META\_SSLCERTFILE</b><br />
Type: `string`<br />

SSL cert file location.

### pumps.splunk.meta.ssl\_key\_file

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_META\_SSLKEYFILE</b><br />
Type: `string`<br />

SSL cert key location.

### pumps.splunk.meta.ssl\_ca\_file

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_META\_SSLCAFILE</b><br />
Type: `string`<br />

Path to the PEM file with trusted CA certificates that will be used to verify the Splunk server's certificate.

### pumps.splunk.meta.ssl\_server\_name

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_META\_SSLSERVERNAME</b><br />
Type: `string`<br />

SSL Server name used in the TLS connection.

### pumps.splunk.meta.obfuscate\_api\_keys

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_META\_OBFUSCATEAPIKEYS</b><br />
Type: `bool`<br />

Controls whether the pump client should hide the API key. In case you still need substring
of the value, check the next option. Default value is `false`.

### pumps.splunk.meta.obfuscate\_api\_keys\_length

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_META\_OBFUSCATEAPIKEYSLENGTH</b><br />
Type: `int`<br />

Define the number of the characters from the end of the API key. The `obfuscate_api_keys`
should be set to `true`. Default value is `0`.

### pumps.splunk.meta.fields

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_META\_FIELDS</b><br />
Type: `[]string`<br />

Define which Analytics fields should participate in the Splunk event. Check the available
fields in the example below. Default value is `["method",
"path", "response_code", "api_key", "time_stamp", "api_version", "api_name", "api_id",
"org_id", "oauth_id", "raw_request", "request_time", "raw_response", "ip_address"]`.

### pumps.splunk.meta.ignore\_tag\_prefix\_list

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_META\_IGNORETAGPREFIXLIST</b><br />
Type: `[]string`<br />

Choose which tags to be ignored by the Splunk Pump. Keep in mind that the tag name and value
are hyphenated. Default value is `[]`.

### pumps.splunk.meta.enable\_batch

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_META\_ENABLEBATCH</b><br />
Type: `bool`<br />

If this is set to `true`, pump is going to send the analytics records in batch to Splunk.
Default value is `false`.

### pumps.splunk.meta.batch\_max\_content\_length

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_META\_BATCHMAXCONTENTLENGTH</b><br />
Type: `int`<br />

Max content length in bytes to be sent in batch requests. It should match the
`max_content_length` configured in Splunk. If the purged analytics records size don't reach
the amount of bytes, they're send anyways in each `purge_loop`. Default value is 838860800
(\~ 800 MB), the same default value as Splunk config.

### pumps.splunk.meta.max\_retries

ENV: <b>TYK\_PMP\_PUMPS\_SPLUNK\_META\_MAXRETRIES</b><br />
Type: `uint64`<br />

MaxRetries represents the maximum amount of retries to attempt if failed to send requests to splunk HEC.
Default value is `0`

### pumps.sql.name

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_NAME</b><br />
Type: `string`<br />

The name of the pump. This is used to identify the pump in the logs.
Deprecated, use `type` instead.

### pumps.sql.type

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_TYPE</b><br />
Type: `string`<br />

Sets the pump type. This is needed when the pump key does not equal to the pump name type.
Current valid types are: `mongo`, `mongo-pump-selective`, `mongo-pump-aggregate`, `csv`,
`elasticsearch`, `influx`, `influx2`, `moesif`, `statsd`, `segment`, `graylog`, `splunk`, `hybrid`, `prometheus`,
`logzio`, `dogstatsd`, `kafka`, `syslog`, `sql`, `sql_aggregate`, `stdout`, `timestream`, `mongo-graph`,
`sql-graph`, `sql-graph-aggregate`, `resurfaceio`.

### pumps.sql.filters

This feature adds a new configuration field in each pump called filters and its structure is
the following:

```{.json}  theme={null}
"filters":{
  "api_ids":[],
  "org_ids":[],
  "response_codes":[],
  "skip_api_ids":[],
  "skip_org_ids":[],
  "skip_response_codes":[]
}
```

The fields api\_ids, org\_ids and response\_codes works as allow list (APIs and orgs where we
want to send the analytics records) and the fields skip\_api\_ids, skip\_org\_ids and
skip\_response\_codes works as block list.

The priority is always block list configurations over allow list.

An example of configuration would be:

```{.json}  theme={null}
"csv": {
 "type": "csv",
 "filters": {
   "org_ids": ["org1","org2"]
 },
 "meta": {
   "csv_dir": "./bar"
 }
}
```

### pumps.sql.filters.org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_FILTERS\_ORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of org\_ids.

### pumps.sql.filters.api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_FILTERS\_APIIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of api\_ids.

### pumps.sql.filters.response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_FILTERS\_RESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by an allow list of response\_codes.

### pumps.sql.filters.skip\_org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_FILTERS\_SKIPPEDORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of org\_ids.

### pumps.sql.filters.skip\_api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_FILTERS\_SKIPPEDAPIIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of api\_ids.

### pumps.sql.filters.skip\_response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_FILTERS\_SKIPPEDRESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by a block list of response\_codes.

### pumps.sql.timeout

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_TIMEOUT</b><br />
Type: `int`<br />

By default, a pump will wait forever for each write operation to complete; you can configure an optional timeout by setting the configuration option `timeout`.
If you have deployed multiple pumps, then you can configure each timeout independently. The timeout is in seconds and defaults to 0.

The timeout is configured within the main pump config as shown here; note that this example would configure a 5 second timeout:

```{.json}  theme={null}
"pump_name": {
  ...
  "timeout":5,
  "meta": {...}
}
```

Tyk will inform you if the pump's write operation is taking longer than the purging loop (configured via `purge_delay`) as this will mean that data is purged before being written to the target data sink.

If there is no timeout configured and pump's write operation is taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try to set a timeout for this pump.`

If there is a timeout configured, but pump's write operation is still taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try lowering the timeout configured for this pump.`.

### pumps.sql.omit\_detailed\_recording

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_OMITDETAILEDRECORDING</b><br />
Type: `bool`<br />

Reduce the size of the traffic logs generated for each request by setting this to true. Tyk Pump will
then not include the `raw_request` and `raw_response` in the logs. Defaults to `false`.

### pumps.sql.max\_record\_size

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_MAXRECORDSIZE</b><br />
Type: `int`<br />

Defines maximum size (in bytes) for Raw Request and Raw Response logs, this value defaults
to 0. If it is not set then tyk-pump will not trim any data and will store the full
information. This can also be set at a pump level. For example:

```{.json}  theme={null}
"csv": {
  "type": "csv",
  "max_record_size":1000,
  "meta": {
    "csv_dir": "./"
  }
}
```

### pumps.sql.ignore\_fields

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_IGNOREFIELDS</b><br />
Type: `[]string`<br />

IgnoreFields defines a list of analytics fields that will be ignored when writing to the pump.
This can be used to avoid writing sensitive information to the Database, or data that you don't really need to have.
The field names must be the same as the JSON tags of the analytics record fields.
For example: `["api_key", "api_version"]`.

### pumps.sql.meta.EnvPrefix

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_META\_ENVPREFIX</b><br />
Type: `string`<br />

The prefix for the environment variables that will be used to override the configuration.
Defaults to `TYK_PMP_PUMPS_SQL_META`

### pumps.sql.meta.type

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_META\_TYPE</b><br />
Type: `string`<br />

The only supported and tested types are `postgres` and `mysql`.
From v1.12.0, we no longer support `sqlite` as a storage type.

### pumps.sql.meta.connection\_string

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_META\_CONNECTIONSTRING</b><br />
Type: `string`<br />

Specifies the connection string to the database.

### pumps.sql.meta.postgres

Postgres configurations.

### pumps.sql.meta.postgres.prefer\_simple\_protocol

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_META\_POSTGRES\_PREFERSIMPLEPROTOCOL</b><br />
Type: `bool`<br />

Disables implicit prepared statement usage.

### pumps.sql.meta.mysql

Mysql configurations.

### pumps.sql.meta.mysql.default\_string\_size

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_META\_MYSQL\_DEFAULTSTRINGSIZE</b><br />
Type: `uint`<br />

Default size for string fields. Defaults to `256`.

### pumps.sql.meta.mysql.disable\_datetime\_precision

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_META\_MYSQL\_DISABLEDATETIMEPRECISION</b><br />
Type: `bool`<br />

Disable datetime precision, which not supported before MySQL 5.6.

### pumps.sql.meta.mysql.dont\_support\_rename\_index

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_META\_MYSQL\_DONTSUPPORTRENAMEINDEX</b><br />
Type: `bool`<br />

Drop & create when rename index, rename index not supported before MySQL 5.7, MariaDB.

### pumps.sql.meta.mysql.dont\_support\_rename\_column

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_META\_MYSQL\_DONTSUPPORTRENAMECOLUMN</b><br />
Type: `bool`<br />

`change` when rename column, rename column not supported before MySQL 8, MariaDB.

### pumps.sql.meta.mysql.skip\_initialize\_with\_version

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_META\_MYSQL\_SKIPINITIALIZEWITHVERSION</b><br />
Type: `bool`<br />

Auto configure based on currently MySQL version.

### pumps.sql.meta.table\_sharding

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_META\_TABLESHARDING</b><br />
Type: `bool`<br />

Specifies if all the analytics records are going to be stored in one table or in multiple
tables (one per day). By default, `false`. If `false`, all the records are going to be
stored in `tyk_aggregated` table. Instead, if it's `true`, all the records of the day are
going to be stored in `tyk_aggregated_YYYYMMDD` table, where `YYYYMMDD` is going to change
depending on the date.

### pumps.sql.meta.log\_level

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_META\_LOGLEVEL</b><br />
Type: `string`<br />

Specifies the SQL log verbosity. The possible values are: `info`,`error` and `warning`. By
default, the value is `silent`, which means that it won't log any SQL query.

### pumps.sql.meta.batch\_size

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_META\_BATCHSIZE</b><br />
Type: `int`<br />

Specifies the amount of records that are going to be written each batch. Type int. By
default, it writes 1000 records max per batch.

### pumps.sql.meta.migrate\_sharded\_tables

ENV: <b>TYK\_PMP\_PUMPS\_SQL\_META\_MIGRATESHARDEDTABLES</b><br />
Type: `bool`<br />

Specifies whether to migrate all existing sharded tables to latest schema during Pump initialization (default: false).
When true, on initialization Pump will scan and migrate all sharded tables to the latest schema.
When false, existing tables will not be migrated and may miss columns included in the latest schema.
If there are a large number of existing tables, or those tables are in use by other services, there may be a performance impact from the migration. We recommend testing carefully.

### pumps.sqlaggregate.name

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_NAME</b><br />
Type: `string`<br />

The name of the pump. This is used to identify the pump in the logs.
Deprecated, use `type` instead.

### pumps.sqlaggregate.type

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_TYPE</b><br />
Type: `string`<br />

Sets the pump type. This is needed when the pump key does not equal to the pump name type.
Current valid types are: `mongo`, `mongo-pump-selective`, `mongo-pump-aggregate`, `csv`,
`elasticsearch`, `influx`, `influx2`, `moesif`, `statsd`, `segment`, `graylog`, `splunk`, `hybrid`, `prometheus`,
`logzio`, `dogstatsd`, `kafka`, `syslog`, `sql`, `sql_aggregate`, `stdout`, `timestream`, `mongo-graph`,
`sql-graph`, `sql-graph-aggregate`, `resurfaceio`.

### pumps.sqlaggregate.filters

This feature adds a new configuration field in each pump called filters and its structure is
the following:

```{.json}  theme={null}
"filters":{
  "api_ids":[],
  "org_ids":[],
  "response_codes":[],
  "skip_api_ids":[],
  "skip_org_ids":[],
  "skip_response_codes":[]
}
```

The fields api\_ids, org\_ids and response\_codes works as allow list (APIs and orgs where we
want to send the analytics records) and the fields skip\_api\_ids, skip\_org\_ids and
skip\_response\_codes works as block list.

The priority is always block list configurations over allow list.

An example of configuration would be:

```{.json}  theme={null}
"csv": {
 "type": "csv",
 "filters": {
   "org_ids": ["org1","org2"]
 },
 "meta": {
   "csv_dir": "./bar"
 }
}
```

### pumps.sqlaggregate.filters.org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_FILTERS\_ORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of org\_ids.

### pumps.sqlaggregate.filters.api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_FILTERS\_APIIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of api\_ids.

### pumps.sqlaggregate.filters.response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_FILTERS\_RESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by an allow list of response\_codes.

### pumps.sqlaggregate.filters.skip\_org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_FILTERS\_SKIPPEDORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of org\_ids.

### pumps.sqlaggregate.filters.skip\_api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_FILTERS\_SKIPPEDAPIIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of api\_ids.

### pumps.sqlaggregate.filters.skip\_response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_FILTERS\_SKIPPEDRESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by a block list of response\_codes.

### pumps.sqlaggregate.timeout

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_TIMEOUT</b><br />
Type: `int`<br />

By default, a pump will wait forever for each write operation to complete; you can configure an optional timeout by setting the configuration option `timeout`.
If you have deployed multiple pumps, then you can configure each timeout independently. The timeout is in seconds and defaults to 0.

The timeout is configured within the main pump config as shown here; note that this example would configure a 5 second timeout:

```{.json}  theme={null}
"pump_name": {
  ...
  "timeout":5,
  "meta": {...}
}
```

Tyk will inform you if the pump's write operation is taking longer than the purging loop (configured via `purge_delay`) as this will mean that data is purged before being written to the target data sink.

If there is no timeout configured and pump's write operation is taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try to set a timeout for this pump.`

If there is a timeout configured, but pump's write operation is still taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try lowering the timeout configured for this pump.`.

### pumps.sqlaggregate.omit\_detailed\_recording

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_OMITDETAILEDRECORDING</b><br />
Type: `bool`<br />

Reduce the size of the traffic logs generated for each request by setting this to true. Tyk Pump will
then not include the `raw_request` and `raw_response` in the logs. Defaults to `false`.

### pumps.sqlaggregate.max\_record\_size

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_MAXRECORDSIZE</b><br />
Type: `int`<br />

Defines maximum size (in bytes) for Raw Request and Raw Response logs, this value defaults
to 0. If it is not set then tyk-pump will not trim any data and will store the full
information. This can also be set at a pump level. For example:

```{.json}  theme={null}
"csv": {
  "type": "csv",
  "max_record_size":1000,
  "meta": {
    "csv_dir": "./"
  }
}
```

### pumps.sqlaggregate.ignore\_fields

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_IGNOREFIELDS</b><br />
Type: `[]string`<br />

IgnoreFields defines a list of analytics fields that will be ignored when writing to the pump.
This can be used to avoid writing sensitive information to the Database, or data that you don't really need to have.
The field names must be the same as the JSON tags of the analytics record fields.
For example: `["api_key", "api_version"]`.

### pumps.sqlaggregate.meta.EnvPrefix

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_META\_ENVPREFIX</b><br />
Type: `string`<br />

The prefix for the environment variables that will be used to override the configuration.
Defaults to `TYK_PMP_PUMPS_SQLAGGREGATE_META`

### pumps.sqlaggregate.meta.type

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_META\_TYPE</b><br />
Type: `string`<br />

The only supported and tested types are `postgres` and `mysql`.
From v1.12.0, we no longer support `sqlite` as a storage type.

### pumps.sqlaggregate.meta.connection\_string

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_META\_CONNECTIONSTRING</b><br />
Type: `string`<br />

Specifies the connection string to the database.

### pumps.sqlaggregate.meta.postgres

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_META\_POSTGRES</b><br />
Type: `PostgresConfig`<br />

Postgres configurations.

### pumps.sqlaggregate.meta.postgres.prefer\_simple\_protocol

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_META\_POSTGRES\_PREFERSIMPLEPROTOCOL</b><br />
Type: `bool`<br />

Disables implicit prepared statement usage.

### pumps.sqlaggregate.meta.mysql

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_META\_MYSQL</b><br />
Type: `MysqlConfig`<br />

Mysql configurations.

### pumps.sqlaggregate.meta.mysql.default\_string\_size

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_META\_MYSQL\_DEFAULTSTRINGSIZE</b><br />
Type: `uint`<br />

Default size for string fields. Defaults to `256`.

### pumps.sqlaggregate.meta.mysql.disable\_datetime\_precision

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_META\_MYSQL\_DISABLEDATETIMEPRECISION</b><br />
Type: `bool`<br />

Disable datetime precision, which not supported before MySQL 5.6.

### pumps.sqlaggregate.meta.mysql.dont\_support\_rename\_index

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_META\_MYSQL\_DONTSUPPORTRENAMEINDEX</b><br />
Type: `bool`<br />

Drop & create when rename index, rename index not supported before MySQL 5.7, MariaDB.

### pumps.sqlaggregate.meta.mysql.dont\_support\_rename\_column

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_META\_MYSQL\_DONTSUPPORTRENAMECOLUMN</b><br />
Type: `bool`<br />

`change` when rename column, rename column not supported before MySQL 8, MariaDB.

### pumps.sqlaggregate.meta.mysql.skip\_initialize\_with\_version

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_META\_MYSQL\_SKIPINITIALIZEWITHVERSION</b><br />
Type: `bool`<br />

Auto configure based on currently MySQL version.

### pumps.sqlaggregate.meta.table\_sharding

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_META\_TABLESHARDING</b><br />
Type: `bool`<br />

Specifies if all the analytics records are going to be stored in one table or in multiple
tables (one per day). By default, `false`. If `false`, all the records are going to be
stored in `tyk_aggregated` table. Instead, if it's `true`, all the records of the day are
going to be stored in `tyk_aggregated_YYYYMMDD` table, where `YYYYMMDD` is going to change
depending on the date.

### pumps.sqlaggregate.meta.log\_level

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_META\_LOGLEVEL</b><br />
Type: `string`<br />

Specifies the SQL log verbosity. The possible values are: `info`,`error` and `warning`. By
default, the value is `silent`, which means that it won't log any SQL query.

### pumps.sqlaggregate.meta.batch\_size

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_META\_BATCHSIZE</b><br />
Type: `int`<br />

Specifies the amount of records that are going to be written each batch. Type int. By
default, it writes 1000 records max per batch.

### pumps.sqlaggregate.meta.migrate\_sharded\_tables

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_META\_MIGRATESHARDEDTABLES</b><br />
Type: `bool`<br />

Specifies whether to migrate all existing sharded tables to latest schema during Pump initialization (default: false).
When true, on initialization Pump will scan and migrate all sharded tables to the latest schema.
When false, existing tables will not be migrated and may miss columns included in the latest schema.
If there are a large number of existing tables, or those tables are in use by other services, there may be a performance impact from the migration. We recommend testing carefully.

### pumps.sqlaggregate.meta.track\_all\_paths

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_META\_TRACKALLPATHS</b><br />
Type: `bool`<br />

Specifies if it should store aggregated data for all the endpoints. By default, `false`
which means that only store aggregated data for `tracked endpoints`.

### pumps.sqlaggregate.meta.ignore\_tag\_prefix\_list

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_META\_IGNORETAGPREFIXLIST</b><br />
Type: `[]string`<br />

Specifies prefixes of tags that should be ignored.

### pumps.sqlaggregate.meta.store\_analytics\_per\_minute

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_META\_STOREANALYTICSPERMINUTE</b><br />
Type: `bool`<br />

Determines if the aggregations should be made per minute instead of per hour.

### pumps.sqlaggregate.meta.omit\_index\_creation

ENV: <b>TYK\_PMP\_PUMPS\_SQLAGGREGATE\_META\_OMITINDEXCREATION</b><br />
Type: `bool`<br />

Set to true to disable the default tyk index creation.

### pumps.statsd.name

ENV: <b>TYK\_PMP\_PUMPS\_STATSD\_NAME</b><br />
Type: `string`<br />

The name of the pump. This is used to identify the pump in the logs.
Deprecated, use `type` instead.

### pumps.statsd.type

ENV: <b>TYK\_PMP\_PUMPS\_STATSD\_TYPE</b><br />
Type: `string`<br />

Sets the pump type. This is needed when the pump key does not equal to the pump name type.
Current valid types are: `mongo`, `mongo-pump-selective`, `mongo-pump-aggregate`, `csv`,
`elasticsearch`, `influx`, `influx2`, `moesif`, `statsd`, `segment`, `graylog`, `splunk`, `hybrid`, `prometheus`,
`logzio`, `dogstatsd`, `kafka`, `syslog`, `sql`, `sql_aggregate`, `stdout`, `timestream`, `mongo-graph`,
`sql-graph`, `sql-graph-aggregate`, `resurfaceio`.

### pumps.statsd.filters

This feature adds a new configuration field in each pump called filters and its structure is
the following:

```{.json}  theme={null}
"filters":{
  "api_ids":[],
  "org_ids":[],
  "response_codes":[],
  "skip_api_ids":[],
  "skip_org_ids":[],
  "skip_response_codes":[]
}
```

The fields api\_ids, org\_ids and response\_codes works as allow list (APIs and orgs where we
want to send the analytics records) and the fields skip\_api\_ids, skip\_org\_ids and
skip\_response\_codes works as block list.

The priority is always block list configurations over allow list.

An example of configuration would be:

```{.json}  theme={null}
"csv": {
 "type": "csv",
 "filters": {
   "org_ids": ["org1","org2"]
 },
 "meta": {
   "csv_dir": "./bar"
 }
}
```

### pumps.statsd.filters.org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_STATSD\_FILTERS\_ORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of org\_ids.

### pumps.statsd.filters.api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_STATSD\_FILTERS\_APIIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of api\_ids.

### pumps.statsd.filters.response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_STATSD\_FILTERS\_RESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by an allow list of response\_codes.

### pumps.statsd.filters.skip\_org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_STATSD\_FILTERS\_SKIPPEDORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of org\_ids.

### pumps.statsd.filters.skip\_api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_STATSD\_FILTERS\_SKIPPEDAPIIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of api\_ids.

### pumps.statsd.filters.skip\_response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_STATSD\_FILTERS\_SKIPPEDRESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by a block list of response\_codes.

### pumps.statsd.timeout

ENV: <b>TYK\_PMP\_PUMPS\_STATSD\_TIMEOUT</b><br />
Type: `int`<br />

By default, a pump will wait forever for each write operation to complete; you can configure an optional timeout by setting the configuration option `timeout`.
If you have deployed multiple pumps, then you can configure each timeout independently. The timeout is in seconds and defaults to 0.

The timeout is configured within the main pump config as shown here; note that this example would configure a 5 second timeout:

```{.json}  theme={null}
"pump_name": {
  ...
  "timeout":5,
  "meta": {...}
}
```

Tyk will inform you if the pump's write operation is taking longer than the purging loop (configured via `purge_delay`) as this will mean that data is purged before being written to the target data sink.

If there is no timeout configured and pump's write operation is taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try to set a timeout for this pump.`

If there is a timeout configured, but pump's write operation is still taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try lowering the timeout configured for this pump.`.

### pumps.statsd.omit\_detailed\_recording

ENV: <b>TYK\_PMP\_PUMPS\_STATSD\_OMITDETAILEDRECORDING</b><br />
Type: `bool`<br />

Reduce the size of the traffic logs generated for each request by setting this to true. Tyk Pump will
then not include the `raw_request` and `raw_response` in the logs. Defaults to `false`.

### pumps.statsd.max\_record\_size

ENV: <b>TYK\_PMP\_PUMPS\_STATSD\_MAXRECORDSIZE</b><br />
Type: `int`<br />

Defines maximum size (in bytes) for Raw Request and Raw Response logs, this value defaults
to 0. If it is not set then tyk-pump will not trim any data and will store the full
information. This can also be set at a pump level. For example:

```{.json}  theme={null}
"csv": {
  "type": "csv",
  "max_record_size":1000,
  "meta": {
    "csv_dir": "./"
  }
}
```

### pumps.statsd.ignore\_fields

ENV: <b>TYK\_PMP\_PUMPS\_STATSD\_IGNOREFIELDS</b><br />
Type: `[]string`<br />

IgnoreFields defines a list of analytics fields that will be ignored when writing to the pump.
This can be used to avoid writing sensitive information to the Database, or data that you don't really need to have.
The field names must be the same as the JSON tags of the analytics record fields.
For example: `["api_key", "api_version"]`.

### pumps.statsd.meta.EnvPrefix

ENV: <b>TYK\_PMP\_PUMPS\_STATSD\_META\_ENVPREFIX</b><br />
Type: `string`<br />

The prefix for the environment variables that will be used to override the configuration.
Defaults to `TYK_PMP_PUMPS_STATSD_META`

### pumps.statsd.meta.address

ENV: <b>TYK\_PMP\_PUMPS\_STATSD\_META\_ADDRESS</b><br />
Type: `string`<br />

Address of statsd including host & port.

### pumps.statsd.meta.fields

ENV: <b>TYK\_PMP\_PUMPS\_STATSD\_META\_FIELDS</b><br />
Type: `[]string`<br />

Define which Analytics fields should have its own metric calculation.

### pumps.statsd.meta.tags

ENV: <b>TYK\_PMP\_PUMPS\_STATSD\_META\_TAGS</b><br />
Type: `[]string`<br />

List of tags to be added to the metric.

### pumps.statsd.meta.separated\_method

ENV: <b>TYK\_PMP\_PUMPS\_STATSD\_META\_SEPARATEDMETHOD</b><br />
Type: `bool`<br />

Allows to have a separated method field instead of having it embedded in the path field.

### pumps.stdout.name

ENV: <b>TYK\_PMP\_PUMPS\_STDOUT\_NAME</b><br />
Type: `string`<br />

The name of the pump. This is used to identify the pump in the logs.
Deprecated, use `type` instead.

### pumps.stdout.type

ENV: <b>TYK\_PMP\_PUMPS\_STDOUT\_TYPE</b><br />
Type: `string`<br />

Sets the pump type. This is needed when the pump key does not equal to the pump name type.
Current valid types are: `mongo`, `mongo-pump-selective`, `mongo-pump-aggregate`, `csv`,
`elasticsearch`, `influx`, `influx2`, `moesif`, `statsd`, `segment`, `graylog`, `splunk`, `hybrid`, `prometheus`,
`logzio`, `dogstatsd`, `kafka`, `syslog`, `sql`, `sql_aggregate`, `stdout`, `timestream`, `mongo-graph`,
`sql-graph`, `sql-graph-aggregate`, `resurfaceio`.

### pumps.stdout.filters

This feature adds a new configuration field in each pump called filters and its structure is
the following:

```{.json}  theme={null}
"filters":{
  "api_ids":[],
  "org_ids":[],
  "response_codes":[],
  "skip_api_ids":[],
  "skip_org_ids":[],
  "skip_response_codes":[]
}
```

The fields api\_ids, org\_ids and response\_codes works as allow list (APIs and orgs where we
want to send the analytics records) and the fields skip\_api\_ids, skip\_org\_ids and
skip\_response\_codes works as block list.

The priority is always block list configurations over allow list.

An example of configuration would be:

```{.json}  theme={null}
"csv": {
 "type": "csv",
 "filters": {
   "org_ids": ["org1","org2"]
 },
 "meta": {
   "csv_dir": "./bar"
 }
}
```

### pumps.stdout.filters.org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_STDOUT\_FILTERS\_ORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of org\_ids.

### pumps.stdout.filters.api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_STDOUT\_FILTERS\_APIIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of api\_ids.

### pumps.stdout.filters.response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_STDOUT\_FILTERS\_RESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by an allow list of response\_codes.

### pumps.stdout.filters.skip\_org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_STDOUT\_FILTERS\_SKIPPEDORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of org\_ids.

### pumps.stdout.filters.skip\_api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_STDOUT\_FILTERS\_SKIPPEDAPIIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of api\_ids.

### pumps.stdout.filters.skip\_response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_STDOUT\_FILTERS\_SKIPPEDRESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by a block list of response\_codes.

### pumps.stdout.timeout

ENV: <b>TYK\_PMP\_PUMPS\_STDOUT\_TIMEOUT</b><br />
Type: `int`<br />

By default, a pump will wait forever for each write operation to complete; you can configure an optional timeout by setting the configuration option `timeout`.
If you have deployed multiple pumps, then you can configure each timeout independently. The timeout is in seconds and defaults to 0.

The timeout is configured within the main pump config as shown here; note that this example would configure a 5 second timeout:

```{.json}  theme={null}
"pump_name": {
  ...
  "timeout":5,
  "meta": {...}
}
```

Tyk will inform you if the pump's write operation is taking longer than the purging loop (configured via `purge_delay`) as this will mean that data is purged before being written to the target data sink.

If there is no timeout configured and pump's write operation is taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try to set a timeout for this pump.`

If there is a timeout configured, but pump's write operation is still taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try lowering the timeout configured for this pump.`.

### pumps.stdout.omit\_detailed\_recording

ENV: <b>TYK\_PMP\_PUMPS\_STDOUT\_OMITDETAILEDRECORDING</b><br />
Type: `bool`<br />

Reduce the size of the traffic logs generated for each request by setting this to true. Tyk Pump will
then not include the `raw_request` and `raw_response` in the logs. Defaults to `false`.

### pumps.stdout.max\_record\_size

ENV: <b>TYK\_PMP\_PUMPS\_STDOUT\_MAXRECORDSIZE</b><br />
Type: `int`<br />

Defines maximum size (in bytes) for Raw Request and Raw Response logs, this value defaults
to 0. If it is not set then tyk-pump will not trim any data and will store the full
information. This can also be set at a pump level. For example:

```{.json}  theme={null}
"csv": {
  "type": "csv",
  "max_record_size":1000,
  "meta": {
    "csv_dir": "./"
  }
}
```

### pumps.stdout.ignore\_fields

ENV: <b>TYK\_PMP\_PUMPS\_STDOUT\_IGNOREFIELDS</b><br />
Type: `[]string`<br />

IgnoreFields defines a list of analytics fields that will be ignored when writing to the pump.
This can be used to avoid writing sensitive information to the Database, or data that you don't really need to have.
The field names must be the same as the JSON tags of the analytics record fields.
For example: `["api_key", "api_version"]`.

### pumps.stdout.meta.EnvPrefix

ENV: <b>TYK\_PMP\_PUMPS\_STDOUT\_META\_ENVPREFIX</b><br />
Type: `string`<br />

The prefix for the environment variables that will be used to override the configuration.
Defaults to `TYK_PMP_PUMPS_STDOUT_META`

### pumps.stdout.meta.format

ENV: <b>TYK\_PMP\_PUMPS\_STDOUT\_META\_FORMAT</b><br />
Type: `string`<br />

Format of the analytics logs. Default is `text` if `json` is not explicitly specified. When
JSON logging is used all pump logs to stdout will be JSON.

### pumps.stdout.meta.log\_field\_name

ENV: <b>TYK\_PMP\_PUMPS\_STDOUT\_META\_LOGFIELDNAME</b><br />
Type: `string`<br />

Root name of the JSON object the analytics record is nested in.

### pumps.syslog.name

ENV: <b>TYK\_PMP\_PUMPS\_SYSLOG\_NAME</b><br />
Type: `string`<br />

The name of the pump. This is used to identify the pump in the logs.
Deprecated, use `type` instead.

### pumps.syslog.type

ENV: <b>TYK\_PMP\_PUMPS\_SYSLOG\_TYPE</b><br />
Type: `string`<br />

Sets the pump type. This is needed when the pump key does not equal to the pump name type.
Current valid types are: `mongo`, `mongo-pump-selective`, `mongo-pump-aggregate`, `csv`,
`elasticsearch`, `influx`, `influx2`, `moesif`, `statsd`, `segment`, `graylog`, `splunk`, `hybrid`, `prometheus`,
`logzio`, `dogstatsd`, `kafka`, `syslog`, `sql`, `sql_aggregate`, `stdout`, `timestream`, `mongo-graph`,
`sql-graph`, `sql-graph-aggregate`, `resurfaceio`.

### pumps.syslog.filters

This feature adds a new configuration field in each pump called filters and its structure is
the following:

```{.json}  theme={null}
"filters":{
  "api_ids":[],
  "org_ids":[],
  "response_codes":[],
  "skip_api_ids":[],
  "skip_org_ids":[],
  "skip_response_codes":[]
}
```

The fields api\_ids, org\_ids and response\_codes works as allow list (APIs and orgs where we
want to send the analytics records) and the fields skip\_api\_ids, skip\_org\_ids and
skip\_response\_codes works as block list.

The priority is always block list configurations over allow list.

An example of configuration would be:

```{.json}  theme={null}
"csv": {
 "type": "csv",
 "filters": {
   "org_ids": ["org1","org2"]
 },
 "meta": {
   "csv_dir": "./bar"
 }
}
```

### pumps.syslog.filters.org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_SYSLOG\_FILTERS\_ORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of org\_ids.

### pumps.syslog.filters.api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_SYSLOG\_FILTERS\_APIIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of api\_ids.

### pumps.syslog.filters.response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_SYSLOG\_FILTERS\_RESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by an allow list of response\_codes.

### pumps.syslog.filters.skip\_org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_SYSLOG\_FILTERS\_SKIPPEDORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of org\_ids.

### pumps.syslog.filters.skip\_api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_SYSLOG\_FILTERS\_SKIPPEDAPIIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of api\_ids.

### pumps.syslog.filters.skip\_response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_SYSLOG\_FILTERS\_SKIPPEDRESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by a block list of response\_codes.

### pumps.syslog.timeout

ENV: <b>TYK\_PMP\_PUMPS\_SYSLOG\_TIMEOUT</b><br />
Type: `int`<br />

By default, a pump will wait forever for each write operation to complete; you can configure an optional timeout by setting the configuration option `timeout`.
If you have deployed multiple pumps, then you can configure each timeout independently. The timeout is in seconds and defaults to 0.

The timeout is configured within the main pump config as shown here; note that this example would configure a 5 second timeout:

```{.json}  theme={null}
"pump_name": {
  ...
  "timeout":5,
  "meta": {...}
}
```

Tyk will inform you if the pump's write operation is taking longer than the purging loop (configured via `purge_delay`) as this will mean that data is purged before being written to the target data sink.

If there is no timeout configured and pump's write operation is taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try to set a timeout for this pump.`

If there is a timeout configured, but pump's write operation is still taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try lowering the timeout configured for this pump.`.

### pumps.syslog.omit\_detailed\_recording

ENV: <b>TYK\_PMP\_PUMPS\_SYSLOG\_OMITDETAILEDRECORDING</b><br />
Type: `bool`<br />

Reduce the size of the traffic logs generated for each request by setting this to true. Tyk Pump will
then not include the `raw_request` and `raw_response` in the logs. Defaults to `false`.

### pumps.syslog.max\_record\_size

ENV: <b>TYK\_PMP\_PUMPS\_SYSLOG\_MAXRECORDSIZE</b><br />
Type: `int`<br />

Defines maximum size (in bytes) for Raw Request and Raw Response logs, this value defaults
to 0. If it is not set then tyk-pump will not trim any data and will store the full
information. This can also be set at a pump level. For example:

```{.json}  theme={null}
"csv": {
  "type": "csv",
  "max_record_size":1000,
  "meta": {
    "csv_dir": "./"
  }
}
```

### pumps.syslog.ignore\_fields

ENV: <b>TYK\_PMP\_PUMPS\_SYSLOG\_IGNOREFIELDS</b><br />
Type: `[]string`<br />

IgnoreFields defines a list of analytics fields that will be ignored when writing to the pump.
This can be used to avoid writing sensitive information to the Database, or data that you don't really need to have.
The field names must be the same as the JSON tags of the analytics record fields.
For example: `["api_key", "api_version"]`.

### pumps.syslog.meta.meta\_env\_prefix

ENV: <b>TYK\_PMP\_PUMPS\_SYSLOG\_META\_ENVPREFIX</b><br />
Type: `string`<br />

The prefix for the environment variables that will be used to override the configuration.
Defaults to `TYK_PMP_PUMPS_SYSLOG_META`

### pumps.syslog.meta.transport

ENV: <b>TYK\_PMP\_PUMPS\_SYSLOG\_META\_TRANSPORT</b><br />
Type: `string`<br />

Possible values are `udp, tcp, tls` in string form.

### pumps.syslog.meta.network\_addr

ENV: <b>TYK\_PMP\_PUMPS\_SYSLOG\_META\_NETWORKADDR</b><br />
Type: `string`<br />

Host & Port combination of your syslog daemon ie: `"localhost:5140"`.

### pumps.syslog.meta.log\_level

ENV: <b>TYK\_PMP\_PUMPS\_SYSLOG\_META\_LOGLEVEL</b><br />
Type: `int`<br />

The severity level, an integer from 0-7, based off the Standard:
[Syslog Severity Levels](https://en.wikipedia.org/wiki/Syslog#Severity_level).

### pumps.syslog.meta.tag

ENV: <b>TYK\_PMP\_PUMPS\_SYSLOG\_META\_TAG</b><br />
Type: `string`<br />

Prefix tag

When working with FluentD, you should provide a
[FluentD Parser](https://docs.fluentd.org/input/syslog) based on the OS you are using so
that FluentD can correctly read the logs.

```{.json}  theme={null}
"syslog": {
  "name": "syslog",
  "meta": {
    "transport": "udp",
    "network_addr": "localhost:5140",
    "log_level": 6,
    "tag": "syslog-pump"
  }
```

### pumps.timestream.name

ENV: <b>TYK\_PMP\_PUMPS\_TIMESTREAM\_NAME</b><br />
Type: `string`<br />

The name of the pump. This is used to identify the pump in the logs.
Deprecated, use `type` instead.

### pumps.timestream.type

ENV: <b>TYK\_PMP\_PUMPS\_TIMESTREAM\_TYPE</b><br />
Type: `string`<br />

Sets the pump type. This is needed when the pump key does not equal to the pump name type.
Current valid types are: `mongo`, `mongo-pump-selective`, `mongo-pump-aggregate`, `csv`,
`elasticsearch`, `influx`, `influx2`, `moesif`, `statsd`, `segment`, `graylog`, `splunk`, `hybrid`, `prometheus`,
`logzio`, `dogstatsd`, `kafka`, `syslog`, `sql`, `sql_aggregate`, `stdout`, `timestream`, `mongo-graph`,
`sql-graph`, `sql-graph-aggregate`, `resurfaceio`.

### pumps.timestream.filters

This feature adds a new configuration field in each pump called filters and its structure is
the following:

```{.json}  theme={null}
"filters":{
  "api_ids":[],
  "org_ids":[],
  "response_codes":[],
  "skip_api_ids":[],
  "skip_org_ids":[],
  "skip_response_codes":[]
}
```

The fields api\_ids, org\_ids and response\_codes works as allow list (APIs and orgs where we
want to send the analytics records) and the fields skip\_api\_ids, skip\_org\_ids and
skip\_response\_codes works as block list.

The priority is always block list configurations over allow list.

An example of configuration would be:

```{.json}  theme={null}
"csv": {
 "type": "csv",
 "filters": {
   "org_ids": ["org1","org2"]
 },
 "meta": {
   "csv_dir": "./bar"
 }
}
```

### pumps.timestream.filters.org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_TIMESTREAM\_FILTERS\_ORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of org\_ids.

### pumps.timestream.filters.api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_TIMESTREAM\_FILTERS\_APIIDS</b><br />
Type: `[]string`<br />

Filters pump data by an allow list of api\_ids.

### pumps.timestream.filters.response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_TIMESTREAM\_FILTERS\_RESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by an allow list of response\_codes.

### pumps.timestream.filters.skip\_org\_ids

ENV: <b>TYK\_PMP\_PUMPS\_TIMESTREAM\_FILTERS\_SKIPPEDORGSIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of org\_ids.

### pumps.timestream.filters.skip\_api\_ids

ENV: <b>TYK\_PMP\_PUMPS\_TIMESTREAM\_FILTERS\_SKIPPEDAPIIDS</b><br />
Type: `[]string`<br />

Filters pump data by a block list of api\_ids.

### pumps.timestream.filters.skip\_response\_codes

ENV: <b>TYK\_PMP\_PUMPS\_TIMESTREAM\_FILTERS\_SKIPPEDRESPONSECODES</b><br />
Type: `[]int`<br />

Filters pump data by a block list of response\_codes.

### pumps.timestream.timeout

ENV: <b>TYK\_PMP\_PUMPS\_TIMESTREAM\_TIMEOUT</b><br />
Type: `int`<br />

By default, a pump will wait forever for each write operation to complete; you can configure an optional timeout by setting the configuration option `timeout`.
If you have deployed multiple pumps, then you can configure each timeout independently. The timeout is in seconds and defaults to 0.

The timeout is configured within the main pump config as shown here; note that this example would configure a 5 second timeout:

```{.json}  theme={null}
"pump_name": {
  ...
  "timeout":5,
  "meta": {...}
}
```

Tyk will inform you if the pump's write operation is taking longer than the purging loop (configured via `purge_delay`) as this will mean that data is purged before being written to the target data sink.

If there is no timeout configured and pump's write operation is taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try to set a timeout for this pump.`

If there is a timeout configured, but pump's write operation is still taking longer than the purging loop, the following warning log will be generated:
`Pump {pump_name} is taking more time than the value configured of purge_delay. You should try lowering the timeout configured for this pump.`.

### pumps.timestream.omit\_detailed\_recording

ENV: <b>TYK\_PMP\_PUMPS\_TIMESTREAM\_OMITDETAILEDRECORDING</b><br />
Type: `bool`<br />

Reduce the size of the traffic logs generated for each request by setting this to true. Tyk Pump will
then not include the `raw_request` and `raw_response` in the logs. Defaults to `false`.

### pumps.timestream.max\_record\_size

ENV: <b>TYK\_PMP\_PUMPS\_TIMESTREAM\_MAXRECORDSIZE</b><br />
Type: `int`<br />

Defines maximum size (in bytes) for Raw Request and Raw Response logs, this value defaults
to 0. If it is not set then tyk-pump will not trim any data and will store the full
information. This can also be set at a pump level. For example:

```{.json}  theme={null}
"csv": {
  "type": "csv",
  "max_record_size":1000,
  "meta": {
    "csv_dir": "./"
  }
}
```

### pumps.timestream.ignore\_fields

ENV: <b>TYK\_PMP\_PUMPS\_TIMESTREAM\_IGNOREFIELDS</b><br />
Type: `[]string`<br />

IgnoreFields defines a list of analytics fields that will be ignored when writing to the pump.
This can be used to avoid writing sensitive information to the Database, or data that you don't really need to have.
The field names must be the same as the JSON tags of the analytics record fields.
For example: `["api_key", "api_version"]`.

### pumps.timestream.meta.EnvPrefix

ENV: <b>TYK\_PMP\_PUMPS\_TIMESTREAM\_META\_ENVPREFIX</b><br />
Type: `string`<br />

The prefix for the environment variables that will be used to override the configuration.
Defaults to `TYK_PMP_PUMPS_TIMESTREAM_META`

### pumps.timestream.meta.AWSRegion

ENV: <b>TYK\_PMP\_PUMPS\_TIMESTREAM\_META\_AWSREGION</b><br />
Type: `string`<br />

The aws region that contains the timestream database

### pumps.timestream.meta.TableName

ENV: <b>TYK\_PMP\_PUMPS\_TIMESTREAM\_META\_TABLENAME</b><br />
Type: `string`<br />

The table name where the data is going to be written

### pumps.timestream.meta.DatabaseName

ENV: <b>TYK\_PMP\_PUMPS\_TIMESTREAM\_META\_DATABASENAME</b><br />
Type: `string`<br />

The timestream database name that contains the table being written to

### pumps.timestream.meta.Dimensions

ENV: <b>TYK\_PMP\_PUMPS\_TIMESTREAM\_META\_DIMENSIONS</b><br />
Type: `[]string`<br />

A filter of all the dimensions that will be written to the table. The possible options are
\["Method","Host","Path","RawPath","APIKey","APIVersion","APIName","APIID","OrgID","OauthID"]

### pumps.timestream.meta.Measures

ENV: <b>TYK\_PMP\_PUMPS\_TIMESTREAM\_META\_MEASURES</b><br />
Type: `[]string`<br />

A filter of all the measures that will be written to the table. The possible options are
\["ContentLength","ResponseCode","RequestTime","NetworkStats.OpenConnections",
"NetworkStats.ClosedConnection","NetworkStats.BytesIn","NetworkStats.BytesOut",
"Latency.Total","Latency.Upstream","GeoData.City.GeoNameID","IPAddress",
"GeoData.Location.Latitude","GeoData.Location.Longitude","UserAgent","RawRequest","RawResponse",
"RateLimit.Limit","Ratelimit.Remaining","Ratelimit.Reset",
"GeoData.Country.ISOCode","GeoData.City.Names","GeoData.Location.TimeZone"]

### pumps.timestream.meta.WriteRateLimit

ENV: <b>TYK\_PMP\_PUMPS\_TIMESTREAM\_META\_WRITERATELIMIT</b><br />
Type: `bool`<br />

Set to true in order to save any of the `RateLimit` measures. Default value is `false`.

### pumps.timestream.meta.ReadGeoFromRequest

ENV: <b>TYK\_PMP\_PUMPS\_TIMESTREAM\_META\_READGEOFROMREQUEST</b><br />
Type: `bool`<br />

If set true, we will try to read geo information from the headers if
values aren't found on the analytic record . Default value is `false`.

### pumps.timestream.meta.WriteZeroValues

ENV: <b>TYK\_PMP\_PUMPS\_TIMESTREAM\_META\_WRITEZEROVALUES</b><br />
Type: `bool`<br />

Set to true, in order to save numerical values with value zero. Default value is `false`.

### pumps.timestream.meta.NameMappings

ENV: <b>TYK\_PMP\_PUMPS\_TIMESTREAM\_META\_NAMEMAPPINGS</b><br />
Type: `map[string]string`<br />

A name mapping for both Dimensions and Measures names. It's not required

### analytics\_storage\_config

Example Temporal storage configuration:

```{.json}  theme={null}
  "analytics_storage_config": {
    "type": "redis",
    "host": "localhost",
    "port": 6379,
    "hosts": null,
    "username": "",
    "password": "",
    "database": 0,
    "optimisation_max_idle": 100,
    "optimisation_max_active": 0,
    "enable_cluster": false,
    "use_ssl": false,
    "ssl_insecure_skip_verify": false
  },
```

### analytics\_storage\_config.type

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_TYPE</b><br />
Type: `string`<br />

Deprecated.

### analytics\_storage\_config.host

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_HOST</b><br />
Type: `string`<br />

Host value. For example: "localhost".

### analytics\_storage\_config.port

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_PORT</b><br />
Type: `int`<br />

Port value. For example: 6379.

### analytics\_storage\_config.hosts

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_HOSTS</b><br />
Type: `map[string]string`<br />

Deprecated: use Addrs instead.

### analytics\_storage\_config.addrs

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_ADDRS</b><br />
Type: `[]string`<br />

Use instead of the host value if you're running a Redis cluster with multiple instances.

### analytics\_storage\_config.master\_name

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_MASTERNAME</b><br />
Type: `string`<br />

Sentinel master name.

### analytics\_storage\_config.sentinel\_password

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_SENTINELPASSWORD</b><br />
Type: `string`<br />

Sentinel password.

### analytics\_storage\_config.username

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_USERNAME</b><br />
Type: `string`<br />

Database username.

### analytics\_storage\_config.password

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_PASSWORD</b><br />
Type: `string`<br />

Database password.

### analytics\_storage\_config.database

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_DATABASE</b><br />
Type: `int`<br />

Database name.

### analytics\_storage\_config.timeout

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_TIMEOUT</b><br />
Type: `int`<br />

How long to allow for new connections to be established (in milliseconds). Defaults to 5sec.

### analytics\_storage\_config.optimisation\_max\_idle

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_MAXIDLE</b><br />
Type: `int`<br />

Maximum number of idle connections in the pool.

### analytics\_storage\_config.optimisation\_max\_active

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_MAXACTIVE</b><br />
Type: `int`<br />

Maximum number of connections allocated by the pool at a given time. When zero, there is no
limit on the number of connections in the pool. Defaults to 500.

### analytics\_storage\_config.enable\_cluster

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_ENABLECLUSTER</b><br />
Type: `bool`<br />

Enable this option if you are using a cluster instance. Default is `false`.

### analytics\_storage\_config.redis\_key\_prefix

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_REDISKEYPREFIX</b><br />
Type: `string`<br />

Prefix the key names. Defaults to "analytics-".
Deprecated: use KeyPrefix instead.

### analytics\_storage\_config.key\_prefix

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_KEYPREFIX</b><br />
Type: `string`<br />

Prefix the key names. Defaults to "analytics-".

### analytics\_storage\_config.use\_ssl

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_USESSL</b><br />
Type: `bool`<br />

Setting this to true to use SSL when connecting to the DB.

### analytics\_storage\_config.ssl\_insecure\_skip\_verify

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_SSLINSECURESKIPVERIFY</b><br />
Type: `bool`<br />

Set this to `true` to tell Pump to ignore database's cert validation.

### analytics\_storage\_config.ssl\_ca\_file

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_SSLCAFILE</b><br />
Type: `string`<br />

Path to the CA file.

### analytics\_storage\_config.ssl\_cert\_file

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_SSLCERTFILE</b><br />
Type: `string`<br />

Path to the cert file.

### analytics\_storage\_config.ssl\_key\_file

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_SSLKEYFILE</b><br />
Type: `string`<br />

Path to the key file.

### analytics\_storage\_config.ssl\_max\_version

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_SSLMAXVERSION</b><br />
Type: `string`<br />

Maximum supported TLS version. Defaults to TLS 1.3, valid values are TLS 1.0, 1.1, 1.2, 1.3.

### analytics\_storage\_config.ssl\_min\_version

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_SSLMINVERSION</b><br />
Type: `string`<br />

Minimum supported TLS version. Defaults to TLS 1.2, valid values are TLS 1.0, 1.1, 1.2, 1.3.

### analytics\_storage\_config.redis\_use\_ssl

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_REDISUSESSL</b><br />
Type: `bool`<br />

Setting this to true to use SSL when connecting to the DB.
Deprecated: use UseSSL instead.

### analytics\_storage\_config.redis\_ssl\_insecure\_skip\_verify

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGECONFIG\_REDISSSLINSECURESKIPVERIFY</b><br />
Type: `bool`<br />

Set this to `true` to tell Pump to ignore database's cert validation.
Deprecated: use SSLInsecureSkipVerify instead.

### analytics\_storage\_type

ENV: <b>TYK\_PMP\_ANALYTICSSTORAGETYPE</b><br />
Type: `string`<br />

Sets the type of storage from which the Pump will fetch data.
The supported value is `redis`, which covers both Redis and the Redis-compatible Valkey.
Pump will default to assume Redis if no alternative is provided, so this configuration can be ignored at present.

### statsd\_connection\_string

ENV: <b>TYK\_PMP\_STATSDCONNECTIONSTRING</b><br />
Type: `string`<br />

Connection string for StatsD monitoring for information please see the
[Instrumentation docs](/api-management/logs-metrics).

### statsd\_prefix

ENV: <b>TYK\_PMP\_STATSDPREFIX</b><br />
Type: `string`<br />

Custom prefix value. For example separate settings for production and staging.

### log\_level

ENV: <b>TYK\_PMP\_LOGLEVEL</b><br />
Type: `string`<br />

Set the logger details for tyk-pump. The posible values are: `info`,`debug`,`error` and
`warn`. By default, the log level is `info`.

### log\_format

ENV: <b>TYK\_PMP\_LOGFORMAT</b><br />
Type: `string`<br />

Set the logger format. The possible values are: `text` and `json`. By default, the log
format is `text`.

### Health Check

From v2.9.4, we have introduced a `/health` endpoint to confirm the Pump is running. You
need to configure the following settings. This returns a HTTP 200 OK response if the Pump is
running.

### health\_check\_endpoint\_name

ENV: <b>TYK\_PMP\_HEALTHCHECKENDPOINTNAME</b><br />
Type: `string`<br />

The default is "hello".

### purge\_delay

ENV: <b>TYK\_PMP\_PURGEDELAY</b><br />
Type: `int`<br />

Controls the frequency at which Tyk Pump should perform regular collection and purge
of traffic logs from the temporal storage (typically Redis). Set the time between purges (in seconds).
Be careful to ensure that this is long enough for the transfer of records to the target data sink (e.g.
persistent storage or external APM) to complete to avoid data loss, but short enough to optimise
your temporal storage size.

### health\_check\_endpoint\_port

ENV: <b>TYK\_PMP\_HEALTHCHECKENDPOINTPORT</b><br />
Type: `int`<br />

The default port is 8083.

### max\_record\_size

ENV: <b>TYK\_PMP\_MAXRECORDSIZE</b><br />
Type: `int`<br />

Defines maximum size (in bytes) for Raw Request and Raw Response logs, this value defaults
to 0. If it is not set then tyk-pump will not trim any data and will store the full
information. This can also be set at a pump level. For example:

```{.json}  theme={null}
"csv": {
  "type": "csv",
  "max_record_size":1000,
  "meta": {
    "csv_dir": "./"
  }
}
```

### dont\_purge\_uptime\_data

ENV: <b>TYK\_PMP\_DONTPURGEUPTIMEDATA</b><br />
Type: `bool`<br />

A default Uptime Pump will transfer uptime metrics which are used by Tyk Dashboard.
If this is not required, you can disable that Pump by setting this option to `true`.

### omit\_detailed\_recording

ENV: <b>TYK\_PMP\_OMITDETAILEDRECORDING</b><br />
Type: `bool`<br />

Reduce the size of the traffic logs generated for each request by setting this to true. Tyk Pump will
then not include the `raw_request` and `raw_response` in the logs. Defaults to false.

### omit\_config\_file

ENV: <b>TYK\_PMP\_OMITCONFIGFILE</b><br />
Type: `bool`<br />

Defines if tyk-pump should ignore all the values in configuration file. Specially useful when setting all configurations in environment variables.

### enable\_http\_profiler

ENV: <b>TYK\_PMP\_HTTPPROFILE</b><br />
Type: `bool`<br />

Expose profiling information to support debugging of Tyk Pump. This operates in the same way as for Tyk Gateway, as explained [here](api-management/troubleshooting-debugging).

### raw\_request\_decoded

ENV: <b>TYK\_PMP\_DECODERAWREQUEST</b><br />
Type: `bool`<br />

This option was intended to decode raw request payloads from base64 for all Pumps. However, it was never implemented and therefore has no functional effect. It has now been deprecated.
for all pumps. This is set to false by default.
Deprecated: Use pump level raw\_request\_decoded configuration instead.

### raw\_response\_decoded

ENV: <b>TYK\_PMP\_DECODERAWRESPONSE</b><br />
Type: `bool`<br />

This option was intended to decode raw response payloads from base64 for all Pumps. However, it was never implemented and therefore has no functional effect. It has now been deprecated.
Deprecated: Use pump level raw\_response\_decoded configuration instead.

Built with [Mintlify](https://mintlify.com).
