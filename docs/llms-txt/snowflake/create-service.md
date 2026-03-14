# Source: https://docs.snowflake.com/en/sql-reference/sql/create-service.md

# CREATE SERVICE

Creates a new [Snowpark Container Services service](../../developer-guide/snowpark-container-services/working-with-services.md)
in the current schema. If a service with that name already exists, use the [DROP SERVICE](drop-service.md) command to delete the previously
created service.

You can run more than one instance of your service. Each service instance is a collection of containers, as defined in the
service specification file, that run together on a node in your compute pool. If you run multiple instances of a service, a load
balancer manages incoming traffic.

Note that the command parameters must be specified in specific order. For more information, see the Usage Notes section.

See also:
:   [ALTER SERVICE](alter-service.md) , [DESCRIBE SERVICE](desc-service.md), [DROP SERVICE](drop-service.md) , [SHOW SERVICES](show-services.md)

## Syntax

```sqlsyntax
CREATE SERVICE [ IF NOT EXISTS ] <name>
  IN COMPUTE POOL <compute_pool_name>
  {
     fromSpecification
     | fromSpecificationTemplate
  }
  [ AUTO_SUSPEND_SECS = <num> ]
  [ EXTERNAL_ACCESS_INTEGRATIONS = ( <EAI_name> [ , ... ] ) ]
  [ AUTO_RESUME = { TRUE | FALSE } ]
  [ MIN_INSTANCES = <num> ]
  [ MIN_READY_INSTANCES = <num> ]
  [ MAX_INSTANCES = <num> ]
  [ LOG_LEVEL = '<log_level>' ]
  [ QUERY_WAREHOUSE = <warehouse_name> ]
  [ [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' , ... ] ) ]
  [ COMMENT = '{string_literal}']
```

Where:

> ```sqlsyntax
> fromSpecification ::=
>   {
>     FROM SPECIFICATION_FILE = '<yaml_file_path>' -- for native app service.
>     | FROM @<stage> SPECIFICATION_FILE = '<yaml_file_path>' -- for non-native app service.
>     | FROM SPECIFICATION <specification_text>
>   }
> ```
>
> ```sqlsyntax
> fromSpecificationTemplate ::=
>   {
>     FROM SPECIFICATION_TEMPLATE_FILE = '<yaml_file_stage_path>' -- for native app service.
>     | FROM @<stage> SPECIFICATION_TEMPLATE_FILE = '<yaml_file_stage_path>' -- for non-native app service.
>     | FROM SPECIFICATION_TEMPLATE <specification_text>
>   }
>   USING ( <key> => <value> [ , <key> => <value> [ , ... ] ]  )
> ```

## Required parameters

`name`
:   String that specifies the identifier (that is, the name) for the service; it must be unique for the schema in which the service
    is created.

    Quoted names for special characters or case-sensitive names are not supported. The same constraint also applies to database
    and schema names where you create a service. That is, database and schema names without quotes are valid when creating a
    service.

`IN COMPUTE POOL compute_pool_name`
:   Specifies the name of the compute pool in your account on which to run the service.

`FROM ...`
:   Identifies the [specification](../../developer-guide/snowpark-container-services/specification-reference.md) or
    the [template](../../developer-guide/snowpark-container-services/working-with-services.md) specification for the service.

    **Using a service specification**

    You can either define the specification either [inline or in a separate file](../../developer-guide/snowpark-container-services/working-with-services.md).

    `SPECIFICATION_FILE = 'yaml_file_path'` or . `@stage SPECIFICATION_FILE = 'yaml_file_path'` or . `SPECIFICATION specification_text`
    :   Specifies the file containing the service specification or the service specification inline. If your service specification is in a file, use SPECIFICATION_FILE. For services created in a Snowflake Native App, omit `@stage`, and specify a path relative to the app root directory. For services created in other contexts, specify the Snowflake internal stage and path to the service specification file.

    **Using a service specification template**

    You can either define the [template specification](../../developer-guide/snowpark-container-services/working-with-services.md) either [inline or in a separate file](../../developer-guide/snowpark-container-services/working-with-services.md).

    `SPECIFICATION_TEMPLATE_FILE = 'yaml_file_path'` or . `@stage SPECIFICATION_TEMPLATE_FILE = 'yaml_file_path'` or . `SPECIFICATION_TEMPLATE specification_text`
    :   Specifies the file containing the service specification template or the service specification template inline. If your service specification template is in a file, use SPECIFICATION_TEMPLATE_FILE. For services created in a Snowflake Native App, omit `@stage`, and specify a path relative to the app root directory. For services created in other contexts, specify the Snowflake internal stage and path to the service specification file. When using template specification, you should also include the `USING` parameter.

    `USING ( key => value [ , key => value [ , ... ] ]  )`
    :   Specifies the template variables and the values of those variables.

        * `key` is the name of the template variable. The template variable name can optionally be enclosed in double quotes
          (`"`).
        * `value` is the value to assign to the variable in the template. String values must be enclosed in `'` or
          `$$`. The value must either be alphanumeric or valid JSON.

        Use a comma between each key-value pair.

## Optional parameters

`AUTO_SUSPEND_SECS = num`
:   Specifies the number of seconds of inactivity (service is idle) after which Snowflake automatically suspends the service. Inactivity means no queries (that invoke a service function) executed for the time period specified by AUTO_SUSPEND_SECS. You can configure this value to 300 seconds or more to enable auto-suspension. For more information, see [Suspending a service](../../developer-guide/snowpark-container-services/working-with-services.md).

    Default: 0 seconds, which indicates Snowflake does not suspend the service automatically.

    [Preview Feature](../../release-notes/preview-features.md) — Open

    Configuring the automatic suspension of a Snowpark Container Services service using the AUTO_SUSPEND_SECS property is a [preview feature](../../release-notes/preview-features.md).

`EXTERNAL_ACCESS_INTEGRATIONS = ( EAI_name [ , ... ] )`
:   Specifies the names of the [external access integrations](../../developer-guide/external-network-access/creating-using-external-network-access.md) that allow your service to access external sites.
    The names in this list are case-sensitive. By default, application containers don’t have
    permission to access the internet. If you want to allow your service to access an external site, create an External Access Integration
    (EAI), and configure your service to use that integration. For more
    information, see [Configure service egress](../../developer-guide/snowpark-container-services/service-network-communications.md).

`AUTO_RESUME = { TRUE | FALSE }`
:   Specifies whether to automatically resume a service when user performs one of the following actions that depend on the service:

    * Executing a query is that uses a [service function](../../developer-guide/snowpark-container-services/working-with-services.md).
    * Sending a request to the public endpoint exposed by the service ([ingress](../../developer-guide/snowpark-container-services/working-with-services.md)).

    If AUTO_RESUME is FALSE, you need to explicitly resume the service (using [ALTER SERVICE … RESUME](alter-service.md)).

    Default: TRUE.

`MIN_INSTANCES = num`
:   Specifies the minimum number of service instances to run.

    Default: 1.

`MIN_READY_INSTANCES = num`
:   Indicates the minimum service instances that must be ready for Snowflake to consider the service is ready to process requests.
    MIN_READY_INSTANCES must be equal to or less than MIN_INSTANCES. For more information, see [Scaling services](../../developer-guide/snowpark-container-services/working-with-services.md).

    Default: The value of the MIN_INSTANCES property.

`MAX_INSTANCES = num`
:   Specifies the maximum number of service instances to run.

    Default: The value of the MIN_INSTANCES property.

`LOG_LEVEL = 'log_level'`
:   Specifies the severity level of messages that should be ingested and made available in the active event table. Messages at
    the specified level (and at more severe levels) are ingested.
    Currently, LOG_LEVEL is supported only for [platform events](../../developer-guide/snowpark-container-services/monitoring-services.md), Changing LOG_LEVEL for [container logs](../../developer-guide/snowpark-container-services/monitoring-services.md) is not supported.

    For more information about levels, see [LOG_LEVEL](../parameters.md). For information about setting the log level, see
    [Setting levels for logging, metrics, and tracing](../../developer-guide/logging-tracing/telemetry-levels.md).

`QUERY_WAREHOUSE = warehouse_name`
:   Warehouse to use if a service container connects to Snowflake to execute a query but does not explicitly specify a warehouse
    to use. This parameter also supports object references in Native Apps. For more information, see [Request references and object-level privileges from consumers](../../developer-guide/native-apps/requesting-refs.md).

    Default: none.

`TAG ( tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ] )`
:   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

    The tag value is always a string, and the maximum number of characters for the tag value is 256.

    For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

`COMMENT = 'string_literal'`
:   Specifies a comment for the service.

    Default: No value

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE SERVICE | Schema |  |
| USAGE | Compute pool |  |
| READ | Stage | This is the stage where the specification is stored. |
| READ | Image repository | Repository of images referenced by the specification. |
| BIND SERVICE ENDPOINT | Account | A role must have this privilege to create a service with public endpoints. This allows the service access through the public endpoints. If the service’s owner role loses this privilege, the public endpoints will not be accessible. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* When calling CREATE SERVICE, the parameters should be provided in this order: specify compute pool, followed by the service specification (either provider specification file on stage or inline specification), and then other properties.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

Create a service with two service instances running:

```sqlexample
CREATE SERVICE echo_service
  IN COMPUTE POOL tutorial_compute_pool
  FROM @tutorial_stage
  SPECIFICATION_FILE='echo_spec.yaml'
  MIN_INSTANCES=2
  MAX_INSTANCES=2
```
