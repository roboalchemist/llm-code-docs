# Source: https://docs.snowflake.com/en/developer-guide/native-apps/connector-sdk/reference/update_warehouse_reference.md

# Update warehouse reference

## Database objects and procedures

The following database objects are created through the `configuration/update_warehouse.sql`.

### PUBLIC.UPDATE_WAREHOUSE(warehouse_name STRING)

Entry point procedure available to the `ADMIN` role. This procedure invokes the Java `UpdateWarehouseHandler.updateWarehouse` handler.

### PUBLIC.UPDATE_WAREHOUSE_INTERNAL(warehouse_name STRING)

Procedure used for providing additional connector specific logic. By default, it returns `'response_code': 'OK'`.
It is invoked by the default `UpdateWarehouseCallback`. Can be overwritten both in SQL and Java.

## Related tables and views

Warehouse update is related to and dependent on the objects from the following files:

* `core.sql` (See [Core SQL reference](core_reference.md))
* `configuration/app_config.sql` (See: [App config SQL reference](app_config_reference.md))
* `configuration/connector_configuration.sql` (See: [Connector configuration reference](connector_configuration_reference.md))

## Related Java objects

The following Java objects from the `com.snowflake.connectors.application.configuration.warehouse` package and some common components are tightly connected with the above procedures:

* `UpdateWarehouseHandler`
* `UpdateWarehouseInputValidator`
* `UpdateWarehouseCallback`
* `UpdateWarehouseSdkCallback`
* `UpdateWarehouseHandlerBuilder`
* `ConnectorStatusService`
* `ConnectorConfigurationService`
* `ConnectorErrorHandler`

## Custom handler

Handler and its internals can be customized using the following two approaches.

### Procedure replacement approach

The following components can be replaced using SQL.

#### Handler

To provide a custom implementation of `UpdateWarehouseHandler` the `PUBLIC.UPDATE_WAREHOUSE` procedure must be replaced. For example:

```sqlexample
CREATE OR REPLACE PROCEDURE PUBLIC.UPDATE_WAREHOUSE(warehouse_name STRING)
  RETURNS VARIANT
  LANGUAGE JAVA
  RUNTIME_VERSION = '11'
  PACKAGES = ('com.snowflake:snowpark:1.11.0')
  IMPORTS = ('/connectors-native-sdk.jar')
  HANDLER = 'com.custom.handler.CustomUpdateWarehouseHandler.updateWarehouse';

GRANT USAGE ON PROCEDURE PUBLIC.UPDATE_WAREHOUSE(STRING) TO APPLICATION ROLE ADMIN;
```

#### Internal procedure

The `INTERNAL` procedure can also be customized through SQL. It can even invoke another Java handler:

```sqlexample
CREATE OR REPLACE PROCEDURE PUBLIC.UPDATE_WAREHOUSE_INTERNAL(warehouse_name STRING)
  RETURNS VARIANT
  LANGUAGE SQL
  EXECUTE AS OWNER
  AS
  BEGIN
    -- SOME CUSTOM LOGIC

    RETURN OBJECT_CONSTRUCT('response_code', 'OK');
  END;
```

```sqlexample
CREATE OR REPLACE PROCEDURE PUBLIC.UPDATE_WAREHOUSE_INTERNAL(warehouse_name STRING)
  RETURNS VARIANT
  LANGUAGE JAVA
  RUNTIME_VERSION = '11'
  PACKAGES = ('com.snowflake:snowpark:1.11.0')
  IMPORTS = ('/connectors-native-sdk.jar')
  HANDLER = 'com.custom.handler.CustomUpdateWarehouseCallback.execute';
```

### Builder approach

`UpdateWarehouseHandler` can be customized using `UpdateWarehouseHandlerBuilder`. This builder allows the developer to provide custom implementations of the following interfaces:

* `UpdateWarehouseInputValidator`
* `UpdateWarehouseCallback`
* `ConnectorErrorHelper`

In case one of them is not provided - the default implementation provided by the SDK will be used.

```java
class CustomUpdateWarehouseInputValidator implements UpdateWarehouseInputValidator {

  @Override
  public ConnectorResponse validate(Identifier warehouse) {
    // CUSTOM VALIDATION LOGIC
    return ConnectorResponse.success();
  }
}

class CustomHandler {

  // Path to this method needs to be specified in the PUBLIC.UPDATE_WAREHOUSE procedure using SQL
  public static Variant updateWarehouse(Session session, String warehouseName) {
    // Using the builder
    var handler = UpdateWarehouseHandler.builder(session)
      .withInputValidator(new CustomUpdateWarehouseInputValidator())
      .build();
    return handler.updateWarehouse(warehouseName).toVariant();
  }
}
```
