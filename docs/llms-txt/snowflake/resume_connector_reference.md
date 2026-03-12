# Source: https://docs.snowflake.com/en/developer-guide/native-apps/connector-sdk/reference/resume_connector_reference.md

# Resume connector reference

## Database objects and procedures

The following database objects are created through the file `lifecycle/resume.sql`.

### PUBLIC.RESUME_CONNECTOR()

The entry point procedure available to the `ADMIN` role. This procedure invokes the Java function `ResumeConnectorHandler.resumeConnector`

### PUBLIC.RESUME_CONNECTOR_VALIDATE()

The procedure used for connector specific validation of pausing process. By default, it returns `'response_code': 'OK'`.
It is invoked by `DefaultResumeConnectorStateValidator`. Can be overwritten both in SQL and Java.

### PUBLIC.RESUME_CONNECTOR_INTERNAL()

The procedure used for connector specific additional pausing duties. By default, it returns `'response_code': 'OK'`.
It is invoked by the `InternalResumeConnectorCallback`. Can be overwritten both in SQL and Java.

## Related tables and views

Resume connector is related to and dependent on the objects from the following files:

* `core.sql` (See [Core SQL reference](core_reference.md))
* `configuration/app_config.sql` (See: [App config SQL reference](app_config_reference.md))
* `configuration/finalize_configuration.sql` (See [Finalize configuration reference](finalize_configuration_reference.md))
* `lifecycle/pause.sql` (See [Pause connector reference](pause_connector_reference.md))

### Related Java objects

The following Java objects from the `com.snowflake.connectors.application.lifecycle` package and some common components are tightly connected with the above procedures:

* `ResumeConnectorHandler`
* `ResumeConnectorStateValidator`
* `ResumeConnectorCallback`
* `ConnectorStatusService`
* `LifecycleService`
* `ConnectorErrorHelper`

## Custom handler

The handler and its internals can be customized using the following two approaches.

### Procedure replacement approach

The following components can be replaced using SQL.

#### Handler

To provide whole custom implementation of the `ResumeConnectorHandler` the `PUBLIC.RESUME_CONNECTOR` procedure must be replaced. For example:

```sqlexample
CREATE OR REPLACE PROCEDURE PUBLIC.RESUME_CONNECTOR()
RETURNS VARIANT
LANGUAGE JAVA
RUNTIME_VERSION = '11'
PACKAGES = ('com.snowflake:snowpark:1.11.0')
IMPORTS = ('/connectors-native-sdk.jar')
HANDLER = 'com.custom.handler.CustomResumeConnectorHandler.resumeConnector';

GRANT USAGE ON PROCEDURE PUBLIC.RESUME_CONNECTOR() TO APPLICATION ROLE ADMIN;
```

#### Internal procedures

The internal `VALIDATE` and `INTERNAL` procedures can be also customized through the SQL. They can even invoke another Java handler:

```sqlexample
CREATE OR REPLACE PROCEDURE PUBLIC.RESUME_CONNECTOR_INTERNAL()
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

CREATE OR REPLACE PROCEDURE PUBLIC.RESUME_CONNECTOR_VALIDATE()
RETURNS VARIANT
LANGUAGE JAVA
RUNTIME_VERSION = '11'
PACKAGES = ('com.snowflake:snowpark:1.11.0')
IMPORTS = ('/connectors-native-sdk.jar')
HANDLER = 'com.custom.handler.CustomResumeConnectorInternalHandler.resumeConnector';
```

### Builder approach

`ResumeConnectorHandler` can be customized using `ResumeConnectorHandlerBuilder`. This builder allows user to provide custom implementations of the following interfaces:

* `ResumeConnectorStateValidator`
* `ResumeConnectorCallback`
* `ConnectorErrorHelper`

In case one is not provided, the default implementation provided by the SDK will be used.

```java
class CustomResumeConnectorStateValidator implements ResumeConnectorStateValidator {
    @Override
    public ConnectorResponse validate() {
        // CUSTOM LOGIC
        return ConnectorResponse.success();
    }
}

class CustomHandler {

    // Path to this method needs to be specified in the PUBLIC.RESUME_CONNECTOR procedure using SQL
    public static Variant resumeConnector(Session session) {
            //Using builder
        var handler = ResumeConnectorHandlerBuilder.builder(session)
            .withStateValidator(new CustomResumeConnectorStateValidator())
            .build();
        return handler.resumeConnector().toVariant();
    }
}
```
