# Source: https://docs.snowflake.com/en/developer-guide/native-apps/callbacks.md

# Callbacks

This topic describes the callbacks that are available for Snowflake Native Apps.

The Snowflake Native App Framework provides callbacks to help manage the app lifecycle. You can
use these callbacks to enhance your app’s functionality and workflow.

To use callbacks, add them to the `lifecycle_callbacks` section of the manifest file, as
in the following example:

```yaml
lifecycle_callbacks:
    before_configuration_change: app_schema.before_config_change_callback
```

## Types of callbacks

The Snowflake Native App Framework provides synchronous and asynchronous callbacks.

### Synchronous callbacks

Synchronous callbacks are called as part of the triggering SQL command. Synchronous callbacks block the calling SQL command. If the callback returns an error, the command will return an error,
and the callback’s error message is returned as part of the SQL error message of the command.

Synchronous callbacks run in a warehouse, so the calling procedure must have a session warehouse set.

### Asynchronous callbacks

Asynchronous callbacks run in the background, after the calling SQL command completes. Asynchronous callbacks do not block the calling SQL command, and errors in asynchronous callbacks are not returned by the calling command.

To ensure that an asynchronous callback has the most current information, the callback signature doesn’t provide state or status information. Instead, the callback should retrieve the most current information using the appropriate SQL commands, such as [SHOW CONFIGURATIONS](../../sql-reference/sql/show-configurations.md) or [SHOW SPECIFICATIONS](../../sql-reference/sql/show-specifications.md). See the description for each asynchronous callback for more information.

The return value from asynchronous callbacks is ignored.

> **Caution:**
>
> The execution order of asynchronous callbacks is not guaranteed.
> Your app should not rely on the order of asynchronous callbacks to perform its operations.

### Permissions

The callback procedures listed in this topic are not required to be granted to any application role. The procedure can be internal to the app, and does not need to be runnable by the consumer. The Snowflake Native App Framework triggers the callback.

### Specification vs. connection callbacks

Both after_specification_change and
after_server_connection_change are run when
a specification is approved or refused. The differences between the two callbacks are
as follows:

* after_specification_change is part of the
  application specification framework.
  It is only triggered when the consumer approves or refuses a specification request.
* after_server_connection_change is part of the
  inter-app communication framework.
  It is triggered by any operation that directly or indirectly impacts the connection state of application specification, including the following:

  * Approving a specification
  * Refusing an approved specification
  * Dropping an approved specification
  * Dropping the server app

Use after_server_connection_change when your app needs to respond to changes in the connection itself, such as a connection being established, lost, or the server app being deleted. This callback provides better connection tracking because it covers a broader range of events than specification approval alone.

Use after_specification_change when your app only needs to respond to the approval or refusal of a specification request, or when handling application specification types other than `CONNECTION`.

## Callback reference

The following categories of callbacks are provided for Snowflake Native Apps:

* Configuration callbacks
* Connection callbacks
* Specification callbacks

### Configuration callbacks

These callbacks are triggered when a [configuration](app-configuration.md) changes.

* validate_configuration_change
* before_configuration_change
* after_configuration_change

#### validate_configuration_change

This callback is a synchronous callback.

This callback is called as part of `ALTER APPLICATION SET CONFIGURATION VALUE` command.
This callback lets the app perform additional custom validation on the value provided by the
server app. If the callback fails, such as with a syntax error, or if the callback returns and error, the set command fails and the new value is not set.

##### Signature

```sqlexample
validate_configuration_change(configuration_name, configuration_value)
```

##### Parameters

* `configuration_name`: The name of the configuration object.
* `configuration_value`: The value provided by the server app.

##### Return value

The callback must return a string in the following JSON format to indicate a validation success or error.

```json
{
  "type": "SUCCESS | ERROR",
  "payload":{
      "error_message": "Error message indicating the validation failure"
  }
}
```

If the function returns a `type` of `ERROR`, the error message is returned as part of the SQL
error message of the `SET` command. If the function returns a `type` of `SUCCESS`, the
error message is ignored.

#### before_configuration_change

This callback is a synchronous callback.
This callback is called as part of `ALTER APPLICATION SET CONFIGURATION VALUE`
and `ALTER APPLICATION UNSET CONFIGURATION` commands. This callback lets the app
perform further operations based on the configuration value set. The value passed into
the callback is null for the `ALTER APPLICATION UNSET CONFIGURATION` command.

##### Signature

```sqlexample
before_configuration_change(configuration_name, configuration_value)
```

##### Parameters

* `configuration_name`: The name of the configuration object.
* `configuration_value`: The value provided by the server app.

##### Return value

The return value of the callback is ignored.

#### after_configuration_change

This callback is an asynchronous callback.
This callback is called after the `ALTER APPLICATION SET CONFIGURATION VALUE`
and `ALTER APPLICATION UNSET CONFIGURATION` commands complete. This callback lets the
client app be notified when a value is provided by the server app.

##### Signature

```sqlexample
after_configuration_change(configuration_name)
```

##### Parameters

* `configuration_name`: The name of the configuration object.

##### Retrieving the latest state

In the callback, the following code snippet can be used to retrieve the current status and value of the configuration:

```python
session.sql(f"""
  SHOW CONFIGURATIONS ->>
      SELECT "status", "value"
      FROM $1
      WHERE "name" = '{configuration_name}';
  """);
```

### Connection callbacks

These callbacks are triggered when a connection’s status changes.

* after_server_connection_change
* after_client_connection_change
* after_server_version_change

#### after_server_connection_change

This callback is an asynchronous callback.
This callback is triggered by any operation that directly or indirectly impacts the connection state of application specification, including the following:

* Approving a specification
* Refusing an approved specification
* Dropping an approved specification
* Dropping the server app

##### Signature

```sqlexample
after_server_connection_change(server_name)
```

##### Parameters

* `server_name`: The name of the server app for which the connection has been changed.

##### Retrieving the latest state

In the callback, the following code snippet retrieves the current
connection status to the server app:

```python
session.sql(f"""
  SHOW SPECIFICATIONS ->>
  SELECT "status"
  FROM $1
  WHERE PARSE_JSON("definition"):"SERVER_APPLICATION"::STRING = '{server_name}';
  """);
```

#### after_client_connection_change

This callback is an asynchronous callback.
This callback is triggered by any operation that directly or indirectly impacts the connection state of application specification, including the following:

* Approving a specification
* Refusing an approved specification
* Dropping an approved specification
* Dropping the client app

##### Signature

```sqlexample
after_client_connection_change(client_name)
```

##### Parameters

* `client_name`: The name of the client app for which the connection has been changed.

##### Retrieving the latest state

In the callback, the following code snippet retrieves what roles, if any,
have been granted to the client app:

```python
session.sql(f"""
  SHOW GRANTS TO APPLICATION {client_name} ->>
  SELECT "name"
  FROM $1
  WHERE "granted_on" = 'APPLICATION_ROLE'
      AND STARTSWITH("name", CURRENT_DATABASE())
  """);
```

#### after_server_version_change

This callback is an asynchronous callback.
This callback is called after the server app’s version or patch number changes.
This lets the client app react to the upgrade or downgrade.

##### Signature

```sqlexample
after_server_version_change(server_name)
```

##### Parameters

* `server_name`: The name of the server app for which the version has changed.

##### Retrieving the latest state

In the callback, the following code snippet can be used to retrieve the current
version of the server app:

```python
session.sql(f"""
  SHOW APPLICATIONS ->>
  SELECT "version", "patch"
  FROM $1
  WHERE "name" = {server_name}
  """);
```

### Specification callbacks

The callback is triggered when a specification of any type has a status change

* `after_specification_change`

#### after_specification_change

This callback is an asynchronous callback.
This callback is called after the `ALTER APPLICATION APPROVE SPECIFICATION` or `ALTER APPLICATION DECLINE SPECIFICATION` commands complete. This callback
lets the app be notified when its specification status is changed.

This callback replaces the functionality of the `specification_action` callback.
You can only specify one of `after_specification_change` or `specification_action` in the manifest file.
For information about the `specification_action` callback, see [Using callback functions with app specifications](requesting-app-specs.md).

##### Signature

```sqlexample
after_specification_change(spec_name)
```

##### Parameters

* `spec_name`: The name of the application specification that has been approved or refused.

##### Retrieving the latest state

In the callback, the following code snippet can be used to retrieve the current
status of the specification:

```python
session.sql(f"""
  SHOW SPECIFICATIONS ->>
      SELECT "status"
      FROM $1
      WHERE "name" = '{spec_name}';
  """);
```

## Callback history

Use the following SQL function and Account Usage view to monitor callback invocations for your Snowflake Native Apps:

* [APPLICATION_CALLBACK_HISTORY](../../sql-reference/functions/application_callback_history.md) (Information Schema table function): Returns the history of callback invocations for applications in the current account. Use this table function to query callback history for a specific application or callback.
* [APPLICATION_CALLBACK_HISTORY view](../../sql-reference/account-usage/application_callback_history.md) (Account Usage view): Provides a history of callback invocations for applications in the account. Use this view to analyze callback activity across all applications in the account.
