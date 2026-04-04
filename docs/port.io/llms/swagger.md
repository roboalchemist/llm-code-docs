# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/swagger.md

# Swagger UI

The `Swagger UI` property is used to import and display [OpenAPI](https://www.openapis.org/) and/or [AsyncAPI](https://www.asyncapi.com/) specification files within an [entity]() in Port.

Using this property will automatically create an additional tab in each [entity page](/customize-pages-dashboards-and-plugins/page/entity-page.md), displaying the specification files in [Swagger UI](https://swagger.io/) format. Within this tab, you will be able to perform HTTP calls to the spec target directly from Port.

The following is an example of a `Swagger UI` tab in an entity page:

![](/img/software-catalog/blueprint/swaggerUiExample.png)

## OpenAPI[â](#openapi "Direct link to OpenAPI")

### Definition[â](#definition "Direct link to Definition")

* URL
* JSON
* YAML

When using the URL format, Port will query the provided URL for the OpenAPI spec and expects a JSON OpenAPI spec

CORS configuration

When using URL for the `open-api` display, make sure that your server allows cross-origin (CORS) requests from Port:

* EU region: `app.getport.io`
* US region: `app.us.port.io`

To serve the OpenAPI spec from an AWS S3 bucket, add a CORS policy to the bucket that allows requests from both `app.getport.io` and `app.us.port.io`. Check out the [AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enabling-cors-examples.html?icmpid=docs_amazons3_console) for more information.

* API
* Terraform

```
{
  "myOpenApi": {
    "title": "My Open API",
    "type": "string",
    "format": "url",
    "spec": "open-api",
    "description": "Open-API Prop"
  }
}
```

```
resource "port_blueprint" "myBlueprint" {
  # ...blueprint properties
  properties {
    identifier = "myOpenApi"
    title      = "My Open Api"
    required   = false
    type       = "string"
    format     = "url"
    spec       = "open-api"
  }
}
```

When using the JSON type, you will need to provide the full JSON OpenAPI spec as an object to the entity:

* API
* Terraform

```
{
  "myOpenApi": {
    "title": "My Open API",
    "type": "object",
    "spec": "open-api",
    "description": "Open-API Prop"
  }
}
```

```
resource "port_blueprint" "myBlueprint" {
  # ...blueprint properties
  properties = {
    props_object = {
      myOpenApi = {
        title      = "My Open Api"
        required   = false
        spec       = "open-api"
      }
    }
  }
}
```

When using the YAML type, you will need to provide the full YAML OpenAPI spec to the entity:

* API
* Terraform

```
{
  "myOpenApi": {
    "title": "My Open API",
    "type": "string",
    "format": "yaml",
    "spec": "open-api",
    "description": "Open-API Prop"
  }
}
```

```
resource "port_blueprint" "myBlueprint" {
  # ...blueprint properties
  properties = {
    string_props = {
      "myYamlProp" = {
        title      = "My yaml"
        required   = false
        format     = "yaml"
      }
    }
  }
}
```

***

### Example[â](#example "Direct link to Example")

Here is how the Swagger tab in the specific entity page appears when an OpenAPI spec is provided:

![OpenAPI Example](/assets/images/openAPI-857c5da7fcb1706a064d474de929b43b.png)

## AsyncAPI[â](#asyncapi "Direct link to AsyncAPI")

### Definition[â](#definition-1 "Direct link to Definition")

* URL
* JSON
* YAML

When using the URL format, Port will query the provided URL for the AsyncAPI spec and expects a JSON AsyncAPI spec

CORS configuration

When using URL for the `async-api` display, make sure that your server allows cross-origin (CORS) requests from Port:

* EU region: `app.getport.io`
* US region: `app.us.port.io`

To serve the AsyncAPI spec from an AWS S3 bucket, add a CORS policy to the bucket that allows requests from both `app.getport.io` and `app.us.port.io`. Check out the [AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enabling-cors-examples.html?icmpid=docs_amazons3_console) for more information.

* API
* Terraform

```
{
  "myAsyncApi": {
    "title": "My Async API",
    "type": "string",
    "format": "url",
    "spec": "async-api",
    "description": "async-api Prop"
  }
}
```

```
resource "port_blueprint" "myBlueprint" {
  # ...blueprint properties
  properties {
    identifier = "myAsyncApi"
    title      = "My Async API"
    required   = false
    type       = "string"
    format     = "url"
    spec       = "async-api"
  }
}
```

When using the JSON type, you will need to provide the full JSON AsyncAPI spec as an object to the Entity:

* API
* Terraform

```
{
  "myAsyncApi": {
    "title": "My Async API",
    "type": "object",
    "spec": "async-api",
    "description": "async-api Prop"
  }
}
```

```
resource "port_blueprint" "myBlueprint" {
  # ...blueprint properties
  properties = {
    props_object = {
      myAsyncApi = {
        title      = "My Async Api"
        required   = false
        spec       = "async-api"
      }
    }
  }
}
```

When using the YAML type, you will need to provide the full YAML AsyncAPI spec to the entity:

* API
* Terraform

```
{
  "myOpenApi": {
    "title": "My Async API",
    "type": "string",
    "format": "yaml",
    "spec": "async-api",
    "description": "Async-API Prop"
  }
}
```

```
resource "port_blueprint" "myBlueprint" {
  # ...blueprint properties
  properties = {
    string_props = {
      "myYamlProp" = {
        title      = "My yaml"
        required   = false
        format     = "yaml"
      }
    }
  }
}
```

***

### Example[â](#example-1 "Direct link to Example")

Here is how the Swagger tab in the specific entity page appears when an AsyncAPI spec is provided:

![AsyncAPI Example](/assets/images/asyncAPI-3a894f3617e7b21be9e7da9cfa3d9f4b.png)
