# Source: https://docs.snowflake.com/en/developer-guide/native-apps/connector-sdk/reference/connector_configuration_reference.md

# Connector configuration reference

## Database objects and procedures

The following database objects are created through the file `configuration/connector_configuration.sql`.

### PUBLIC.CONFIGURE_CONNECTOR (config VARIANT)

Entry point procedure available to the `ADMIN` role. This procedure invokes the Java function [ConfigureConnectorHandler.configureConnector](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/application/configuration/connector/ConfigureConnectorHandler.md).

### PUBLIC.CONFIGURE_CONNECTOR_VALIDATE (config VARIANT)

Procedure used for connector specific validation of the configuration. By default, it returns `'response_code': 'OK'`.
It is invoked by the `DefaultConfigureConnectorInputValidator` function. Can be overwritten both in SQL and Java.

### PUBLIC.CONFIGURE_CONNECTOR_INTERNAL (config VARIANT)

Procedure used for connector specific additional configuration. By default, it returns `'response_code': 'OK'`.
It is invoked by the `InternalConfigureConnectorCallback`. Can be overwritten both in SQL and Java.

## Related tables and views

Connector configuration is related to and dependent on the objects from the following files:

* `core.sql` (See [Core SQL reference](core_reference.md))
* `configuration/app_config.sql` (See: [App config SQL reference](app_config_reference.md))

## Related Java objects

The following Java objects from the `com.snowflake.connectors.application.configuration.connector` package and some common components are tightly connected with the above procedures:

* [ConfigureConnectorHandler](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/application/configuration/connector/ConfigureConnectorHandler.md)
* [ConfigureConnectorInputValidator](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/application/configuration/connector/ConfigureConnectorInputValidator.md)
* [ConfigureConnectorCallback](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/application/configuration/connector/ConfigureConnectorCallback.md)
* [ConnectorConfigurationService](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/application/configuration/connector/ConnectorConfigurationService.md)
* [ConfigureConnectorHandlerBuilder](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/application/configuration/connector/ConfigureConnectorHandlerBuilder.md)
* [ConnectorErrorHelper](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/common/exception/helper/ConnectorErrorHelper.md)

## Custom handler

Handler and its internals can be customized using the following two approaches.

### Procedure replacement approach

The following components can be replaced using SQL.

#### Handler

To provide whole custom implementation of the [ConfigureConnectorHandler](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/application/configuration/connector/ConfigureConnectorHandler.md) the PUBLIC.CONFIGURE_CONNECTOR procedure must be replaced. For example:

```sqlexample
CREATE OR REPLACE PROCEDURE PUBLIC.CONFIGURE_CONNECTOR(config VARIANT)
RETURNS VARIANT
LANGUAGE JAVA
RUNTIME_VERSION = '11'
PACKAGES = ('com.snowflake:snowpark:1.11.0')
IMPORTS = ('/connectors-native-sdk.jar')
HANDLER = 'com.custom.handler.CustomConfigureConnectorHandler.configureConnector';

GRANT USAGE ON PROCEDURE PUBLIC.CONFIGURE_CONNECTOR(VARIANT) TO APPLICATION ROLE ADMIN;
```

#### Internal procedures

Internal `VALIDATE` and `INTERNAL` procedures can be also customized through the SQL. They can even invoke another Java handler:

```sqlexample
CREATE OR REPLACE PROCEDURE PUBLIC.CONFIGURE_CONNECTOR_INTERNAL(config VARIANT)
RETURNS VARIANT
LANGUAGE SQL
EXECUTE AS OWNER
AS
BEGIN
    -- SOME CUSTOM LOGIC BEGIN
    SELECT sysdate();
    -- SOME CUSTOM LOGIC END

    RETURN OBJECT_CONSTRUCT('response_code', 'OK');
END;

CREATE OR REPLACE PROCEDURE PUBLIC.CONFIGURE_CONNECTOR_VALIDATE(config VARIANT)
    RETURNS VARIANT
    LANGUAGE JAVA
    RUNTIME_VERSION = '11'
    PACKAGES = ('com.snowflake:snowpark:1.11.0')
    IMPORTS = ('/connectors-native-sdk.jar')
    HANDLER = 'com.custom.handler.CustomConfigureConnectorInternalHandler.configureConnector';
```

### Builder approach

[ConfigureConnectorHandler](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/application/configuration/connector/ConfigureConnectorHandler.md) can be customized using [ConfigureConnectorHandlerBuilder](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/application/configuration/connector/ConfigureConnectorHandlerBuilder.md). This builder allows user to provide custom implementations of the following interfaces:

* [ConfigureConnectorInputValidator](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/application/configuration/connector/ConfigureConnectorInputValidator.md)
* [ConfigureConnectorCallback](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/application/configuration/connector/ConfigureConnectorCallback.md)
* [ConnectorErrorHelper](/developer-guide/native-apps/connector-sdk/java/com/snowflake/connectors/common/exception/helper/ConnectorErrorHelper.md)

In case one of them is not provided the default implementation provided by the SDK will be used.

```java
class CustomConfigureConnectorInputValidator implements ConfigureConnectorInputValidator {
    @Override
    public ConnectorResponse validate(Variant config) {
        // CUSTOM LOGIC
        return ConnectorResponse.success();
    }
}

class CustomHandler {

    // Path to this method needs to be specified in the PUBLIC.CONFIGURE_CONNECTOR procedure using SQL
    public static Variant configureConnector(Session session, Variant configuration) {
            //Using builder
        var handler = ConfigureConnectorHandler.builder(session)
            .withInputValidator(new CustomConfigureConnectorInputValidator())
            .build();
        return handler.configureConnector(configuration).toVariant();
    }
}
```
