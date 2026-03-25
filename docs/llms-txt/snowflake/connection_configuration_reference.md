# Source: https://docs.snowflake.com/en/developer-guide/native-apps/connector-sdk/reference/connection_configuration_reference.md

# Connection configuration reference

## Database objects and procedures

The following database objects are created through the file `configuration/connection_configuration.sql`.

### PUBLIC.SET_CONNECTION_CONFIGURATION (connection_configuration VARIANT)

Entry point procedure available to `ADMIN` role. This procedure invokes the Java function [ConnectionConfigurationHandler.setConnectionConfiguration()](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/application/configuration/connection/ConnectionConfigurationHandler.md).

### PUBLIC.SET_CONNECTION_CONFIGURATION_VALIDATE (connection_configuration VARIANT)

Procedure used for Connector specific validation of the configuration. It can also be used to transform some parts of the configuration.
Transformed configuration needs to be returned as additional `"config"` property. By default, it returns `'response_code': 'OK'`.
It is invoked by the `DefaultConnectionConfigurationInputValidator`. Can be overwritten both in SQL and Java.

### PUBLIC.SET_CONNECTION_CONFIGURATION_INTERNAL (connection_configuration VARIANT)

Procedure used for Connector specific additional connection configuration, for example adding external access integration to other procedures.
By default, it returns `'response_code': 'OK'`. It is invoked by the `InternalConnectionConfigurationCallback`. Can be overwritten both in SQL and Java.

### PUBLIC.GET_CONNECTION_CONFIGURATION()

A procedure to retrieve current connection configuration from the internal table. It is available to `ADMIN` and `VIEWER` users.

## Related tables and views

Connector configuration is related to and dependent on the objects from the following files:

* `core.sql` (See [Core SQL reference](core_reference.md))
* `configuration/app_config.sql` (See: [App config SQL reference](app_config_reference.md))

### PUBLIC.TEST_CONNECTION()

This procedure is not provided by default in any file, but is necessary for the `Connection Configuration` feature.
This procedure will be used as a light weight way to check access to the external source system.

## Related Java objects

The following Java objects from the [com.snowflake.connectors.application.configuration.connector](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/application/configuration/package-summary.md) package and some common components are tightly connected with the above procedures:

* [ConnectionConfigurationHandler](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/application/configuration/connection/ConnectionConfigurationHandler.md)
* [ConnectionConfigurationInputValidator](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/application/configuration/connection/ConnectionConfigurationInputValidator.md)
* [ConnectionValidator](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/application/configuration/connection/ConnectionValidator.md)
* [ConnectorConfigurationService](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/application/configuration/connector/ConnectorConfigurationService.md)
* [ConnectionConfigurationHandlerBuilder](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/application/configuration/connection/ConnectionConfigurationHandlerBuilder.md)
* [ConnectorErrorHelper](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/common/exception/helper/ConnectorErrorHelper.md)

## Custom handler

Handler and its internals can be customized using the following two approaches.

### Procedure replacement approach

The following components can be replaced using SQL.

#### Handler

To provide whole custom implementation of the [ConnectionConfigurationHandler](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/application/configuration/connection/ConnectionConfigurationHandler.md) the PUBLIC.SET_CONNECTION_CONFIGURATION procedure must be replaced. For example:

```sqlexample
CREATE OR REPLACE PROCEDURE PUBLIC.SET_CONNECTION_CONFIGURATION(config VARIANT)
  RETURNS VARIANT
  LANGUAGE JAVA
  RUNTIME_VERSION = '11'
  PACKAGES = ('com.snowflake:snowpark:1.11.0')
  IMPORTS = ('/connectors-native-sdk.jar')
  HANDLER = 'com.custom.handler.CustomConnectionConfigurationHandler.setConnectionConfiguration';

GRANT USAGE ON PROCEDURE PUBLIC.CONFIGURE_CONNECTOR(VARIANT) TO APPLICATION ROLE ADMIN;
```

#### Internal procedures

Internal `VALIDATE` and `INTERNAL` procedures can be also customized through the SQL. They can even invoke another Java handler:

```sqlexample
CREATE OR REPLACE PROCEDURE PUBLIC.SET_CONNECTION_CONFIGURATION_INTERNAL(config VARIANT)
  RETURNS VARIANT
  LANGUAGE SQL
  EXECUTE AS OWNER
  AS
  BEGIN
    -- SOME CUSTOM LOGIC BEGIN
    SELECT sysdate();
    -- SOME CUSTOM LOGIC END

    RETURN OBJECT_CONSTRUCT('response_code', 'OK', '"config"', '"transformed config variant"');
  END;

CREATE OR REPLACE PROCEDURE PUBLIC.SET_CONNECTION_CONFIGURATION_VALIDATE(config VARIANT)
  RETURNS VARIANT
  LANGUAGE JAVA
  RUNTIME_VERSION = '11'
  PACKAGES = ('com.snowflake:snowpark:1.11.0')
  IMPORTS = ('/connectors-native-sdk.jar')
  HANDLER = 'com.custom.handler.CustomConnectionConfigurationValidateHandler.setConnectionConfiguration';
```

### Builder approach

[ConnectionConfigurationHandler](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/application/configuration/connection/ConnectionConfigurationHandler.md) can be customized using [ConnectionConfigurationHandlerBuilder](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/application/configuration/connection/ConnectionConfigurationHandlerBuilder.md). This builder allows user to provide custom implementations of the following interfaces:

* [ConnectionConfigurationInputValidator](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/application/configuration/connection/ConnectionConfigurationInputValidator.md)
* [ConnectionConfigurationCallback](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/application/configuration/connection/ConnectionConfigurationCallback.md)
* [ConnectionValidator](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/application/configuration/connection/ConnectionValidator.md)
* [ConnectorErrorHelper](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/common/exception/helper/ConnectorErrorHelper.md)

In case one of them is not provided the default implementation provided by the SDK will be used.

```java
class CustomConnectionConfigurationInputValidator implements ConnectionConfigurationInputValidator {
  @Override
  public ConnectorResponse validate(Variant config) {
    // CUSTOM LOGIC
    return ConnectorResponse.success();
  }
}

class CustomHandler {

  // Path to this method needs to be specified in the PUBLIC.SET_CONNECTION_CONFIGURATION procedure using SQL
  public static Variant configureConnection(Session session, Variant configuration) {
    //Using builder
    var handler = ConnectionConfigurationHandler.builder(session)
      .withInputValidator(new CustomConnectionConfigurationInputValidator())
      .build();
    return handler.connectionConfiguration(configuration).toVariant();
  }
}
```
