# Source: https://docs.api7.ai/enterprise/getting-started/publish-service.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/getting-started/publish-service.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/getting-started/publish-service.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/getting-started/publish-service.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/getting-started/publish-service.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/getting-started/publish-service.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/getting-started/publish-service.md

# Source: https://docs.api7.ai/enterprise/3.8.x/getting-started/publish-service.md

# Source: https://docs.api7.ai/enterprise/3.7.x/getting-started/publish-service.md

# Source: https://docs.api7.ai/enterprise/3.6.x/getting-started/publish-service.md

# Source: https://docs.api7.ai/enterprise/3.5.x/getting-started/publish-service.md

# Source: https://docs.api7.ai/enterprise/3.4.x/getting-started/publish-service.md

# Source: https://docs.api7.ai/enterprise/3.3.x/getting-started/publish-service.md

# Publish Service Version

For version control of deployed APIs, leverage API7 Gateway for publishing service versions to different [gateway groups](https://docs.api7.ai/enterprise/3.3.x/key-concepts/gateway-groups.md), instead of in-place gateway group edits.

Typically, an API version is published first in test and staging environments before publishing in production environments. API7 Gateway manages this environmental separation through [Gateway Groups](https://docs.api7.ai/enterprise/3.3.x/key-concepts/gateway-groups.md), where an API belongs to a single [Published Service](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md) with a shared [Upstream](https://docs.api7.ai/enterprise/3.3.x/key-concepts/upstreams.md).

This tutorial guides you in publishing the [httpbin](https://httpbin.org/) service to a gateway group on API7 Gateway. You will learn how to:

1. Create a service manually and through an OpenAPI Specification file.
2. Publish services by configuring upstream nodes and by using service discovery mechanisms.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).
2. [Have at least one gateway instance](https://docs.api7.ai/enterprise/3.3.x/getting-started/add-gateway-instance.md) in your gateway group.

## Add a Service Template with Routes[â](#add-a-service-template-with-routes "Direct link to Add a Service Template with Routes")

### Add Manually[â](#add-manually "Direct link to Add Manually")

* Dashboard
* ADC

1. Select **Service Hub** from the side navigation bar, then click **Add Service**.
2. Select **Add Manually**.
3. From the dialog box, do the following:

* In the **Name** field, enter `httpbin`.
* In the **Service Type** field, choose `HTTP(Layer 7 Proxy)`.
* In the **Upstream Scheme** field, choose `HTTP`.
* Click **Add**.

4. Inside the service, click **Add Route**.
5. From the **Add Route** dialog box, do the following:

* In the **Name** field, enter `getting-started-anything`.
* In the **Path** field, enter `/anything/*`.
* In the **Methods** field, choose `GET`.
* Click **Add**.

Create an ADC configuration file with the service, its upstream, and route configuration:

adc.yaml

```
services:
  - name: httpbin
    upstream:
      name: httpbin upstream
      scheme: http
      nodes:
        - host: httpbin.org
          port: 80
          weight: 100
    routes:
      - uris:
          - /anything/*
        name: getting-started-anything
        methods:
          - GET
```

### Import OpenAPI Specification[â](#import-openapi-specification "Direct link to Import OpenAPI Specification")

Both the dashboard and ADC support importing an [OpenAPI v3.0](https://swagger.io/specification/) Specification.

Define your API in a YAML/JSON file as shown below:

OpenAPI.yaml

```
openapi: 3.1.0
info:
  title: httpbin
  description: "httpbin for the API7 Enterprise Getting Started guides."
  version: 1.0.0
paths:
  "/anything/*":
    get:
      tags:
        - Anything
      summary: Returns anything that is passed into the request.
      operationId: getting-started-anything
      responses:
        "200":
          description: Successful Response
          content:
            application/json:
              schema:
                type: string
tags:
  - name: Anything
    description: Return anything that is passed in on the request.
```

Then, use it in API7 Gateway:

* Dashboard
* ADC

1. Select **Service Hub** from the side navigation bar, then click **Add Service**.
2. Select **Import OpenAPI**.
3. From the dialog box, do the following:

* Upload your YAML/JSON file.
* In the **Upstream Scheme** field, choose `HTTP`.
* Click **Next**.

4. Confirm the following information:

* **Name**: the `title` field in OpenAPI Specification.
* **Labels**: the `tag` field in OpenAPI Specification.
* **Description**: the `description` field in OpenAPI Specification.
* **Name**: the `title` field in the OpenAPI Specification.
* Click **Add**.

Use ADC to convert the OpenAPI Specification to an ADC configuration file:

```
adc convert openapi -f openapi.yaml -o adc.yaml
```

## Publish Single Service to Gateway Group[â](#publish-single-service-to-gateway-group "Direct link to Publish Single Service to Gateway Group")

* Dashboard
* ADC

1. Select **Service Hub** from the side navigation bar and then select `httpbin`.
2. Click **Publish New Version**.
3. Select your target gateway group, for example, `default`, and then click **Next**.
4. From the dialog box, do the following:

* In the **New Version** field, enter `1.0.0`.

* In the **How to find the upstream** field, choose `Use Nodes`.

* Click **Add Node**. From the dialog box, do the following:

  <!-- -->

  * In the **Host** and **Port** fields, enter `httpbin.org` as the host and `80` as the port.
  * In the **Weight** field, use the default value `100`.
  * Click **Add**.

* Confirm the service information and then click **Publish**.

Synchronize the configuration file created in the previous step to your target gateway group, for example, `default`:

```
adc sync -f adc.yaml --gateway-group default
```

## Publish Multiple Services to Gateway Group[â](#publish-multiple-services-to-gateway-group "Direct link to Publish Multiple Services to Gateway Group")

* Dashboard
* ADC

1. Select **Service Hub** from the side navigation bar and then click **Batch Publish Services**.
2. Select your target gateway group, for example, `default`, and then click **Next**.
3. Click **Add Service**.
4. From the dialog box, do the following:

* In the **Service** dropdown, select the service you want to publish.
* In the **New Version** field, enter `1.0.0`.
* Click **Add**.

5. Repeat the above steps to add more services.
6. Click **Next** to continue publishing the services.
7. In the new window, do the following for each service:

* In the **How to find the upstream** field, choose `Use Nodes`.

* Click **Add Node**. From the dialog box, do the following:

  <!-- -->

  * In the **Host** and **Port** fields, enter `httpbin.org` as the host and `80` as the port.
  * In the **Weight** field, use the default value `100`.
  * Click **Add**.

8. Confirm the information and then click **Publish**.

To publish multiple services, you can either update your ADC configuration file to include other services or use multiple configuration files and synchronize them to your target gateway group, for example, `default`, as shown below:

```
adc sync -f adc-1.yaml -f adc-2.yaml
```

Below is an interactive demo that provides a hands-on introduction to publishing versioned services. You will gain a better understanding of how to use it in API7 Enterprise by clicking and following the steps.

## Validate the API[â](#validate-the-api "Direct link to Validate the API")

```
curl "http://127.0.0.1:9080/anything/publish"
```

You should see the following output:

```
{
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Host": "localhost",
    "User-Agent": "curl/7.88.1",
    "X-Amzn-Trace-Id": "Root=1-664cc6d6-10fe9f740ab1629e19cf85a2",
    "X-Forwarded-Host": "localhost"
  },
  "json": null,
  "method": "GET",
  "origin": "152.15.0.1, 116.212.249.196",
  "url": "http://localhost/anything/publish"
}
```

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts
  <!-- -->
  * [Services](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md)

* Getting Started

  <!-- -->

  * [Synchronize Published Service Version between Gateway Groups](https://docs.api7.ai/enterprise/3.3.x/getting-started/sync-service.md)
  * [Rollback a Published Service](https://docs.api7.ai/enterprise/3.3.x/getting-started/rollback-service.md)

* Best Practices
  <!-- -->
  * [API Version Control](https://docs.api7.ai/enterprise/3.3.x/best-practices/api-version-control.md)
