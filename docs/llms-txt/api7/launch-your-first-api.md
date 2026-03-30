# Source: https://docs.api7.ai/enterprise/getting-started/launch-your-first-api.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/getting-started/launch-your-first-api.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/getting-started/launch-your-first-api.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/getting-started/launch-your-first-api.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/getting-started/launch-your-first-api.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/getting-started/launch-your-first-api.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/getting-started/launch-your-first-api.md

# Source: https://docs.api7.ai/enterprise/3.8.x/getting-started/launch-your-first-api.md

# Source: https://docs.api7.ai/enterprise/3.7.x/getting-started/launch-your-first-api.md

# Source: https://docs.api7.ai/enterprise/3.6.x/getting-started/launch-your-first-api.md

# Source: https://docs.api7.ai/enterprise/3.5.x/getting-started/launch-your-first-api.md

# Source: https://docs.api7.ai/enterprise/3.4.x/getting-started/launch-your-first-api.md

# Source: https://docs.api7.ai/enterprise/3.3.x/getting-started/launch-your-first-api.md

# Launch Your First API

This tutorial describes launching and validating a simple API on API7 Gateway. You will complete the following steps:

1. Create a [Published Service](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md) with a [Route](https://docs.api7.ai/enterprise/3.3.x/key-concepts/routes.md) and an [Upstream](https://docs.api7.ai/enterprise/3.3.x/key-concepts/upstreams.md) that points to `httpbin` upstream.
2. Validate the created API by sending a request.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).
2. [Have at least one gateway instance in your gateway group](https://docs.api7.ai/enterprise/3.3.x/getting-started/add-gateway-instance.md).

## Start a Sample Upstream Service[â](#start-a-sample-upstream-service "Direct link to Start a Sample Upstream Service")

If you are running API7 on Kubernetes, you will be deploying an [httpbin](https://hub.docker.com/r/kennethreitz/httpbin/) application to your cluster in this section as the sample upstream service. Otherwise, skip to the [next section](#create-service-and-route) where you will be using the hosted [httpbin](https://httpbin.org) application as the upstream.

Start a sample [httpbin](https://hub.docker.com/r/kennethreitz/httpbin/) application:

```
kubectl run httpbin --image kennethreitz/httpbin --port 80
```

You should see a `pod/httpbin created` response.

Expose the application's port `80` through a service:

```
kubectl expose pod httpbin --port 80
```

You should see a `service/httpbin exposed` response.

## Create Service and Route[â](#create-service-and-route "Direct link to Create Service and Route")

* Dashboard
* ADC
* Ingress Controller

### Create a Service

1. Select **Published Services** under your gateway group from the side navigation bar and then click **Add Service**.

2. Select **Add Manually**.

3. From the **Add Service** dialog box, do the following:

   <!-- -->

   * In the **Name** field, enter `httpbin`.

   * In the **Service Type** field, choose `HTTP (Layer 7 Proxy)`.

   * In the **Upstream Scheme** field, choose `HTTP`.

   * In the **How to find the upstream** field, choose `Use Nodes`.

   * Click **Add Node**.

   * From the **Add Node** dialog box, do the following:

     <!-- -->

     * In the **Host** field, enter `httpbin.org`.
     * In the **Port** field, enter `80`.
     * In the **Weight** field, enter `100`.

4. Click **Add**. This will create a new service in the 'No Version' state.

### Create a Route

1. Click the service that you just created in the previous step, and then click **Add Route**.

2. From the **Add Route** dialog box, do the following:

   <!-- -->

   * In the **Name** field, enter `get-ip`.
   * In the **Path** field, enter `/ip`.
   * In the **Methods** field, choose `GET`.
   * Click **Add**.

Below is an interactive demo that provides a hands-on introduction to creating no-version services. You will better understand how to use it in API7 Enterprise by clicking and following the steps.

Create the following configuration file:

adc.yaml

```
services:
  - name: httpbin
    upstream:
      name: default
      scheme: http
      nodes:
        - host: httpbin.org
          port: 80
          weight: 100
    routes:
      - uris:
          - /ip
        name: get-ip
        methods:
          - GET
```

Synchronize the configuration to API7 Enterprise:

```
adc sync -f adc.yaml
```

Create a configuration file containing the API7 Ingress Controller custom resource of a route:

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  name: get-ip
  namespace: api7
spec:
  http:
    - name: get-ip
      match:
        paths:
          - /ip
      backends:
        - serviceName: httpbin
          servicePort: 80
```

Apply the configuration to your cluster:

```
kubectl apply -f httpbin-route.yaml
```

You should see a response of the following:

```
apisixroute.apisix.apache.org/httpbin-route created
```

## Validate the API[â](#validate-the-api "Direct link to Validate the API")

* Dashboard
* ADC
* Ingress Controller

Send a request to the route:

```
curl "http://127.0.0.1:9080/ip"
```

You should see the following response:

```
{
  "origin": "127.0.0.1"
}
```

Send a request to the route:

```
curl "http://127.0.0.1:9080/ip"
```

You should see the following response:

```
{
  "origin": "127.0.0.1"
}
```

In the dashboard, you should see a service called `api7_httpbin_80` under the **Published Services**.

First, expose the service port to your local machine by port forwarding:

```
kubectl port-forward svc/api7-ee-3-gateway-gateway 9080:80 &
```

The command above runs in the background and maps port `80` of the `api7-ee-3-gateway-gateway` service to port `9080` on the local machine.

Send a request to the route:

```
curl "http://127.0.0.1:9080/ip"
```

You should see a response similar to the following:

```
{
  "origin": "127.0.0.1"
}
```

And thatâs it. You have your first API running now.

## Add APIs by Importing OpenAPI[â](#add-apis-by-importing-openapi "Direct link to Add APIs by Importing OpenAPI")

You can also add APIs by importing an OpenAPI 3.0 specification.

**Create a Service**

1. Select **Published Services** under your gateway group from the side navigation bar and then click **Add Service**.

2. Select **Import OpenAPI**.

3. From the **Add Service** dialog box, do the following:

   <!-- -->

   * In the **OpenAPI 3.0 Specification** field, upload the `httpbin.yaml` file.

   * In the **Upstream Scheme** and **Service Type** fields, keep the default settings `HTTP`.

   * In the **How to find the upstream** field, keep the default setting `Use Nodes`.

   * Click **Add Node**.

   * From the **Add Node** dialog box, do the following:

     <!-- -->

     * In the **Host** field, enter `httpbin.org`.
     * In the **Port** field, enter `80`.
     * In the **Weight** field, enter `100`.

   * Click **Next**.

4. Click **Add**. This will create a new service in the 'No Version' state. The basic information and labels are imported, and **all paths in the OpenAPI file are transformed to routes in the service**.

Below is an interactive demo that provides a hands-on introduction to adding services by importing OpenAPI. You will better understand how to use it in API7 Enterprise by clicking and following the steps.

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Getting Started
  <!-- -->
  * [Publish Service Version](https://docs.api7.ai/enterprise/3.3.x/getting-started/publish-service.md)
* Best Practices
  <!-- -->
  * [API Version Control](https://docs.api7.ai/enterprise/3.3.x/best-practices/api-version-control.md)
