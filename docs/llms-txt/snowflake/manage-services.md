# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/services/manage-services.md

# Managing services

Snowpark Container Services enables you to easily deploy, manage, and scale containerized applications.
After you upload your application image to a repository in your account, you run your application containers
as a service or a job. This topic explains working with services.

A service is long-running, like a web service, and does not end on its own. Snowflake manages running services.
For example, if a service container exits, for whatever reason, Snowflake restarts that container so the service
runs uninterrupted. If your service needs more resources, such as more compute power, Snowflake provisions
additional nodes in the compute pool.

For more information about working with container services, see [Snowpark Container Services: Working with services](../../snowpark-container-services/working-with-services.md).

This topic shows how to do the following tasks with services:

* Create a Snowpark Container Services service
* Create and deploy a service from a project definition
* Suspend and resume a service
* Get status information about a service
* List the endpoints in a service
* Set and unset a service’s properties or parameters
* Display logs for a named service
* Upgrade a named service

For common operations, such as listing or dropping, Snowflake CLI uses `snow object` commands as described in [Managing Snowflake objects](../objects/manage-objects.md).

## Create a Snowpark Container Services service

A Snowpark container service requires the following:

* **A compute pool**: Snowflake runs your service in the specified compute pool.
* **A service specification file**: This specification gives Snowflake the information needed to configure and run
  your service.

To create a service, enter a [snow spcs service create](../command-reference/spcs-commands/service-commands/create.md) command similar to the following:

```snowcli
snow spcs service create "job_1" --compute-pool "pool_1" --spec-path "/some-dir/spec_file.yaml"
```

For more information, see [Managing Snowflake objects](../objects/manage-objects.md).

### Create and deploy a service from a project definition

You can create a service from a `snowflake.yml` project definition file and then executing the `snow spcs service deploy` command.

The following shows a sample `snowflake.yml` project definition file:

```yaml
definition_version: 2
entities:
  my_service:
    type: service
    identifier: my_service
    stage: my_stage
    compute_pool: my_compute_pool
    spec_file: spec.yml
    min_instances: 1
    max_instances: 2
    query_warehouse: my_warehouse
    auto_resume: true
    external_access_integrations:
      - my_external_access
    secrets:
        cred: my_cred_name
    artifacts:
      - spec.yml
    comment: "My service"
    tags:
      - name: test_tag
        value: test_value
```

The following table describes the properties of a compute pool project definition.

Compute pool project definition properties

| Property | Definition |
| --- | --- |
| **type**  *required*, *string* | Must be `service`. |
| **stage**  *required*, *string* | Stage where the service specification file is located. |
| **compute_pool**  *required*, *string* | Compute pool where the service runs. |
| **spec_file**  *required*, *string* | Path to service specification file on the stage. |
| **identifier**  *optional*, *string* | Snowflake identifier for the entity. The value can have the following forms:   *String identifier text  ```yaml   identifier: my-service```  Both unquoted and quoted identifiers are supported. To use quoted identifiers, include the surrounding quotes in the YAML value (for example, `’”My Image Repository"`).* Object  ```yaml   identifier:     name: my-service     schema: my-schema # optional     database: my-db # optional```  **Note:** An error occurs if you specify a `schema` or `database` and use a fully qualified name in the `name` property (such as `mydb.schema1.my-app`). |
| **min_instances**  *optional*, *string* | Minimum number of service instances to run.  Default: `1` |
| **max_instances**  *optional*, *string* | Maximum number of service instances to run. |
| **query_warehouse**  *optional*, *string* | Warehouse to use if a service container connects to Snowflake to execute a query without explicitly specifying a warehouse to use. |
| **auto_resume**  *optional*, *string* | Whether to automatically resume when a service function or ingress is called.  Default: `True` |
| **external_access_integrations**  *optional*, *string sequence* | Names of external access integrations needed for this entity to access external networks. |
| **secrets**  *optional*, *dictionary* | Names and values of secrets variables so that you can use the variables to reference the secrets. |
| **artifacts**  *optional*, *string sequence* | List of file source and destination pairs to add to the deploy root. You can use the following artifact properties:   *`src`: Path to the code source file or files* `dest`: Path to the directory to deploy the artifacts.  Destination paths that reference directories must end with a `/`. A glob pattern’s destination that does not end with a `/` results in an error. If omitted, `dest` defaults to the same string as `src`.  You can also pass in a string for each item instead of a `dict`, in which case the value is treated as both `src` and `dest`.   If `src` refers to just one file (not a glob), `dest` can refer to a target `<path>` or a `<path/name>`.  You can also pass in a string for each item instead of a `dict`, in which case the value is treated as both `src` and `dest`. |
| **comment**  *optional*, *string* | Comments to associate with the compute pool. |
| **tags**  *optional*, *Tag sequence* | Tag names and values for the compute pool. For more information, see [Tag quotas](../../../user-guide/object-tagging/introduction.md) |

To create and deploy a service, do the following:

1. Change your current directory to the directory containing the project definition file.
2. Run a `snow spcs service deploy` command similar to the following:

   ```snowcli
   snow spcs service deploy
   ```

   ```output
   +---------------------------------------------------------------------+
   | key    | value                                                      |
   |--------+------------------------------------------------------------|
   | status | Service MY_SERVICE successfully created.                   |
   +---------------------------------------------------------------------+
   ```

## Suspend and resume a service

To suspend a named service, enter a [snow spcs service suspend](../command-reference/spcs-commands/service-commands/suspend.md) command similar to the following:

```snowcli
snow spcs service suspend echo_service
```

```output
+-------------------------------------------+
| key    | value                            |
|--------+----------------------------------|
| status | Statement executed successfully. |
+-------------------------------------------+
```

To resume a suspended service, enter a [snow spcs service resume](../command-reference/spcs-commands/service-commands/resume.md) command similar to the following:

```snowcli
snow spcs service resume echo_service
```

```output
+-------------------------------------------+
| key    | value                            |
|--------+----------------------------------|
| status | Statement executed successfully. |
+-------------------------------------------+
```

## Get status information about a service

> **Note:**
>
> The current role must have MONITOR privilege on the service to get its status.

### List all services

The [snow spcs service list](../command-reference/spcs-commands/service-commands/list.md) command returns an overview of all services, including the runtime state of the services, such as PENDING or RUNNING, and the upgrading status. To get the status of all services, enter a command similar to the following:

```snowcli
snow spcs service list
```

```output
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|        |        |        |        |        |        |        |        |        |        |        |         | extern |         |        |         |        |         |        |        |         |        |         |        |
|        |        |        |        |        |        |        |        |        |        |        |         | al_acc |         |        |         |        |         |        |        |         |        | managin | managi |
|        |        | databa |        |        |        |        | curren | target | min_in | max_in |         | ess_in |         |        |         |        | owner_r | query_ |        |         |        | g_objec | ng_obj |
|        |        | se_nam | schema |        | comput | dns_na | t_inst | _insta | stance | stance | auto_re | tegrat | created | update | resumed | commen | ole_typ | wareho |        | spec_di | is_upg | t_domai | ect_na |
| name   | status | e      | _name  | owner  | e_pool | me     | ances  | nces   | s      | s      | sume    | ions   | _on     | d_on   | _on     | t      | e       | use    | is_job | gest    | rading | n       | me     |
|--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+---------+--------+---------+--------+---------+--------+---------+--------+--------+---------+--------+---------+--------|
| ECHO_S | RUNNIN | TEST00 | TEST_S | SYSADM | TUTORI | echo-s | 1      | 1      | 1      | 1      | true    | None   | 2024-10 | 2024-1 | None    | This   | ROLE    | COMPUT | false  | 52e62d1 | false  | None    | None   |
| ERVICE | G      | _DB    | CHEMA  | IN     | AL_COM | ervice |        |        |        |        |         |        | -16     | 0-16   |         | is a   |         | E_WH   |        | f19c720 |        |         |        |
|        |        |        |        |        | PUTE_P | .imhd. |        |        |        |        |         |        | 15:09:3 | 15:09: |         | test   |         |        |        | 6b5f4ef |        |         |        |
|        |        |        |        |        | OOL    | svc.sp |        |        |        |        |         |        | 0.49300 | 31.905 |         | servic |         |        |        | c069557 |        |         |        |
|        |        |        |        |        |        | cs.int |        |        |        |        |         |        | 0-07:00 | 000-07 |         | e      |         |        |        | 8b6c2b3 |        |         |        |
|        |        |        |        |        |        | ernal  |        |        |        |        |         |        |         | :00    |         |        |         |        |        | 806ad76 |        |         |        |
|        |        |        |        |        |        |        |        |        |        |        |         |        |         |        |         |        |         |        |        | 67d78cc |        |         |        |
|        |        |        |        |        |        |        |        |        |        |        |         |        |         |        |         |        |         |        |        | ce8b6ed |        |         |        |
|        |        |        |        |        |        |        |        |        |        |        |         |        |         |        |         |        |         |        |        | 6501a8a |        |         |        |
|        |        |        |        |        |        |        |        |        |        |        |         |        |         |        |         |        |         |        |        | 3       |        |         |        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

### Get the status of a named service

To get the status of an individual service, enter a [snow spcs service describe](../command-reference/spcs-commands/service-commands/describe.md) command similar to the following:

```snowcli
snow spcs service describe echo_service
```

```output
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|        |        |        |        |        |        |        |        |        |        |        |         | extern |         |        |         |        |         |        |        |         |        |         |        |
|        |        |        |        |        |        |        |        |        |        |        |         | al_acc |         |        |         |        |         |        |        |         |        | managin | managi |
|        |        | databa |        |        |        |        | curren | target | min_in | max_in |         | ess_in |         |        |         |        | owner_r | query_ |        |         |        | g_objec | ng_obj |
|        |        | se_nam | schema |        | comput | dns_na | t_inst | _insta | stance | stance | auto_re | tegrat | created | update | resumed | commen | ole_typ | wareho |        | spec_di | is_upg | t_domai | ect_na |
| name   | status | e      | _name  | owner  | e_pool | me     | ances  | nces   | s      | s      | sume    | ions   | _on     | d_on   | _on     | t      | e       | use    | is_job | gest    | rading | n       | me     |
|--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+---------+--------+---------+--------+---------+--------+---------+--------+--------+---------+--------+---------+--------|
| ECHO_S | RUNNIN | TEST00 | TEST_S | SYSADM | TUTORI | echo-s | 1      | 1      | 1      | 1      | true    | None   | 2024-10 | 2024-1 | None    | This   | ROLE    | COMPUT | false  | 52e62d1 | false  | None    | None   |
| ERVICE | G      | _DB    | CHEMA  | IN     | AL_COM | ervice |        |        |        |        |         |        | -16     | 0-16   |         | is a   |         | E_WH   |        | f19c720 |        |         |        |
|        |        |        |        |        | PUTE_P | .imhd. |        |        |        |        |         |        | 15:09:3 | 15:09: |         | test   |         |        |        | 6b5f4ef |        |         |        |
|        |        |        |        |        | OOL    | svc.sp |        |        |        |        |         |        | 0.49300 | 31.905 |         | servic |         |        |        | c069557 |        |         |        |
|        |        |        |        |        |        | cs.int |        |        |        |        |         |        | 0-07:00 | 000-07 |         | e      |         |        |        | 8b6c2b3 |        |         |        |
|        |        |        |        |        |        | ernal  |        |        |        |        |         |        |         | :00    |         |        |         |        |        | 806ad76 |        |         |        |
|        |        |        |        |        |        |        |        |        |        |        |         |        |         |        |         |        |         |        |        | 67d78cc |        |         |        |
|        |        |        |        |        |        |        |        |        |        |        |         |        |         |        |         |        |         |        |        | ce8b6ed |        |         |        |
|        |        |        |        |        |        |        |        |        |        |        |         |        |         |        |         |        |         |        |        | 6501a8a |        |         |        |
|        |        |        |        |        |        |        |        |        |        |        |         |        |         |        |         |        |         |        |        | 3       |        |         |        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

### List instances and containers

You can list service’s instances and containers with the `snow spcs service list-instances` and `snow spcs service list-containers` commands, respectively.

To get the list of instances in the `echo_service` service, enter the following [snow spcs service list-instances](../command-reference/spcs-commands/service-commands/list-instances.md) command:

```snowcli
snow spcs service list-instances echo_service
```

```output
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| database_name | schema_name | service_name | instance_id | status | spec_digest                                                      | creation_time        | start_time           |
|---------------+-------------+--------------+-------------+--------+------------------------------------------------------------------+----------------------+----------------------|
| TEST00_DB     | TEST_SCHEMA | ECHO_SERVICE | 0           | READY  | 336c065739dd2b96e770f01804affdc7810e6df68a23b23052d851627abfbdf9 | 2024-10-10T06:06:30Z | 2024-10-10T06:06:30Z |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

To get the list of containers in the `echo_service` service, enter the following [snow spcs service list-containers](../command-reference/spcs-commands/service-commands/list-containers.md) command:

```snowcli
snow spcs service list-containers echo_service
```

```output
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| database_name | schema_name | service_name | instance_id | container_name | status | message | image_name                                | image_digest                              | restart_count | start_time           |
|---------------+-------------+--------------+-------------+----------------+--------+---------+-------------------------------------------+-------------------------------------------+---------------+----------------------|
| TEST00_DB     | TEST_SCHEMA | ECHO_SERVICE | 0           | main           | READY  | Running | org-test-account-00.registry.registry.sno | sha256:06c3d54edc24925abe398eda70d37eb6b8 | 0             | 2024-10-16T22:09:35Z |
|               |             |              |             |                |        |         | wflakecomputing.com/test00_db/test_schema | 7b1c4dd6211317592764e1e7d94498            |               |                      |
|               |             |              |             |                |        |         | /test00_repo/echo_service:latest          |                                           |               |                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

### List the endpoints in a service

To list the endpoints a named service, enter a [snow spcs service list-endpoints](../command-reference/spcs-commands/service-commands/list-endpoints.md) command similar to the following:

```snowcli
snow spcs service list-endpoints echo_service
```

```output
+--------------+------+----------+-----------------+-----------------------------------------+
| name         | port | protocol | ingress_enabled | ingress_url                             |
|--------------+------+----------+-----------------+-----------------------------------------|
| echoendpoint | 8000 | TCP      | true            | org-id-acct-id.snowflakecomputing.app   |
+--------------+------+----------+-----------------+-----------------------------------------+
```

### List the service roles associated with a service

You can manage access to individual endpoints exposed by a service by defining service roles and permissions in the service specification. For more information about how to use service roles, see [GRANT SERVICE ROLE](../../../sql-reference/sql/grant-service-role.md).

To get a list of service roles created for a service, use the [snow spcs service list-roles](../command-reference/spcs-commands/service-commands/list-roles.md) command, as shown:

```snowcli
snow spcs service list-roles my_service
```

```output
+------------------------------------------------------------------+
| created_on                       | name                | comment |
|----------------------------------+---------------------+---------|
| 2024-10-09 16:48:52.980000-07:00 | ALL_ENDPOINTS_USAGE | None    |
+------------------------------------------------------------------+
```

## Set and unset a service’s properties or parameters

> **Note:**
>
> The current role must have OPERATE privilege on the service to set properties.

To set a service’s property or parameter, enter a [snow spcs service set](../command-reference/spcs-commands/service-commands/set.md) command similar to the following:

```snowcli
snow spcs service set echo_service --min-instances 2 --max-instances 4
```

```output
+-------------------------------------------+
| key    | value                            |
|--------+----------------------------------|
| status | Statement executed successfully. |
+-------------------------------------------+
```

To reset a service’s property or parameter to its default value, enter a command similar to the following:

```snowcli
snow spcs compute-pool unset tutorial_compute_pool --auto-resume
```

```output
+-------------------------------------------+
| key    | value                            |
|--------+----------------------------------|
| status | Statement executed successfully. |
+-------------------------------------------+
```

## Display logs for a named service

> **Note:**
>
> The current role must have MONITOR privilege on the service to display logs.

To display local logs for a named service, enter a [snow spcs service logs](../command-reference/spcs-commands/service-commands/logs.md) command similar to the following:

```snowcli
snow spcs service logs "service_1" --container-name "container_1" --instance-id "0"
```

## Upgrade a named service

> **Note:**
>
> The current role must have OPERATE privilege on the service to upgrade it.

To upgrade a named service, enter a [snow spcs service upgrade](../command-reference/spcs-commands/service-commands/upgrade.md) command similar to the following:

```snowcli
snow spcs service upgrade echo_service --spec-path spec.yml
```

```output
+-------------------------------------------+
| key    | value                            |
|--------+----------------------------------|
| status | Statement executed successfully. |
+-------------------------------------------+
```
