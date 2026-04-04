# Source: https://docs.port.io/api-reference/create-a-migration.md

# Create a migration

```
POST 
/v1/migrations
```

This route allows you to create a migration in your Port organization. You can use this to migrate data from one blueprint to another.<br /><br />**Note** that it is not possible to directly change the data type of an existing property via the UI or the API. The type field setting of a property (**number**, **string**, etc.) is permanent and cannot be changed after creation.<br /><br />However, you can create a new property with the desired type and migrate the old values to it. Refer to the [documentation](https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/#change-a-property-type) for more information on how to change a property's type.

## Request[â](#request "Direct link to request")

## Responses[â](#responses "Direct link to Responses")

* 401
* 404
* 413
* 422

Default Response

A resource with the provided identifier was not found

Request body is too large (limit is 1MiB)

The json provided does not match the route's schema
