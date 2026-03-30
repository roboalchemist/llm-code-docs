# Source: https://www.apollographql.com/docs/graphos/routing/self-hosted/containerization/kubernetes/extensibility.md

# Router Extensibility Features in Kubernetes

The Apollo Router Core source code and all its distributions are made available under the [Elastic License v2.0 (ELv2) license](https://www.apollographql.com/docs/resources/elastic-license-v2-faq/#can-i-extend-or-modify-the-gateway-or-router-by-creating-plugins).

The router supports two extensibility options to customize the router's behavior. The extensibility features are:

* [Rhai scripting](https://www.apollographql.com/docs/graphos/routing/customization/rhai)
* [External coprocessors](https://www.apollographql.com/docs/router/customizations/coprocessor)

This guide shows how to deploy a router with these features in Kubernetes.

## Deploy with Rhai scripts

The router supports [Rhai scripting](https://www.apollographql.com/docs/graphos/routing/customization/rhai) to add custom functionality.

Enabling Rhai scripts in your deployed router requires mounting an extra volume for your Rhai scripts and getting your scripts onto the volume. That can be done by following steps in [a separate example for creating a custom in-house router chart](https://github.com/apollographql/in-house-router-example). The example creates a new (in-house) chart that depends on the released router chart, and the new chart has templates that add the necessary configuration to allow Rhai scripts for a deployed router.

## Deploying with a coprocessor

You have two options to consider when deploying a coprocessor.

* [Deploy as a sidecar container](https://www.apollographql.com/docs/graphos/routing/self-hosted/containerization/kubernetes/extensibility.md#deploy-as-a-sidecar-container)
* [Deploy as a separate Kubernetes `Deployment`](https://www.apollographql.com/docs/graphos/routing/self-hosted/containerization/kubernetes/extensibility.md#deploying-using-a-separate-deployment)

Consider the following when deciding which option to use:

* The sidecar container option is the simplest and most common way to deploy a coprocessor. It allows you to run the coprocessor in the same pod as the router, which can simplify networking and configuration.
* The separate `Deployment` option allows you to run the coprocessor in a different pod, which can be useful if you want to scale the coprocessor independently of the router.

### Deploy as a sidecar container

The router supports [external coprocessing](https://www.apollographql.com/docs/router/customizations/coprocessor) to run custom logic on requests throughout the [router's request-handling lifecycle](https://www.apollographql.com/docs/graphos/routing/customization/rhai/#router-request-lifecycle).

A deployed coprocessor can have its own application image and container in the router pod.

To configure a coprocessor and its container for your deployed router through a YAML configuration file:

1. Create a YAML file, `coprocessor_values.yaml`, to contain additional values that override default values.
2. Edit `coprocessor_values.yaml` to configure a coprocessor for the router. For reference, follow the [typical](https://www.apollographql.com/docs/router/customizations/coprocessor#typical-configuration) and [minimal](https://www.apollographql.com/docs/router/customizations/coprocessor#minimal-configuration)  configuration examples, and apply them to `router.configuration.coprocessor`.

```yaml title=router.yaml
coprocessor:
  url: http://127.0.0.1:8081 # Required. Replace with the URL of your coprocessor's HTTP endpoint.
  # The timeout for all coprocessor requests. Defaults to 1 second (1s)
  # Supported formats: https://docs.rs/humantime/latest/humantime/fn.parse_duration.html
  timeout: 2s
  router: # This coprocessor hooks into the `RouterService`
    request: # By including this key, the `RouterService` sends a coprocessor request whenever it first receives a client request.
      headers: true # These boolean properties indicate which request data to include in the coprocessor request. All are optional and false by default.
      body: false
      context: false
      sdl: false
      path: false
      method: false
    response: # By including this key, the `RouterService` sends a coprocessor request whenever it's about to send response data to a client (including incremental data via @defer).
      headers: true
      body: false
      context: false
      sdl: false
      status_code: false
  supergraph: # This coprocessor hooks into the `SupergraphService`
    request: # By including this key, the `SupergraphService` sends a coprocessor request whenever it first receives a client request.
      headers: true # These boolean properties indicate which request data to include in the coprocessor request. All are optional and false by default.
      body: false
      context: false
      sdl: false
      method: false
    response: # By including this key, the `SupergraphService` sends a coprocessor request whenever it's about to send response data to a client (including incremental data via @defer).
      headers: true
      body: false
      context: false
      sdl: false
      status_code: false
  subgraph:
    all:
      request: # By including this key, the `SubgraphService` sends a coprocessor request whenever it is about to make a request to a subgraph.
        headers: true # These boolean properties indicate which request data to include in the coprocessor request. All are optional and false by default.
        body: false
        context: false
        uri: false
        method: false
        service_name: false
        subgraph_request_id: false
      response: # By including this key, the `SubgraphService` sends a coprocessor request whenever receives a subgraph response.
        headers: true
        body: false
        context: false
        service_name: false
        status_code: false
        subgraph_request_id: false
  connector: # This coprocessor hooks into connector HTTP requests.
    all:
      request: # By including this key, the coprocessor sends a request before each connector HTTP call.
        headers: true # These boolean properties indicate which request data to include in the coprocessor request. All are optional and false by default.
        body: false
        context: false
        uri: false
        method: false
        service_name: false
      response: # By including this key, the coprocessor sends a request after each connector HTTP call.
        headers: true
        body: false
        context: false
        service_name: false
        status_code: false
```

1. Edit `coprocessor_values.yaml` to add a container for the coprocessor.

```yaml title=coprocessor_values.yaml
extraContainers:
  - name: <coprocessor-deployed-name> # name of deployed container
    image: <coprocessor-app-image> # name of application image
    ports:
      - containerPort: <coprocessor-container-port> # must match port of router.configuration.coprocessor.url
    env: [] # array of environment variables
```

1. Deploy the router with the additional YAML configuration file. For example, starting with the `helm install` command from the basic deployment step, append `--values coprocessor_values.yaml`:

```bash
helm install --namespace <router-namespace> --set managedFederation.apiKey="<graph-api-key>" --set managedFederation.graphRef="<graph-ref>"  oci://ghcr.io/apollographql/helm-charts/router --version <router-version> --values router/values.yaml --values coprocessor_values.yaml
```

### Deploying using a separate `Deployment`

Deploying as a separate `Deployment` can take shape in two ways:

* Using an entirely separate Helm chart.
* Using the router's Helm chart as a dependency and adding a new `Deployment` template
  * This option is more complex but allows you to customize the router's Helm chart and add your own templates whilst keeping the coporcessor's deployment alongside the router's.

#### Separate Helm chart

In the case of using a separate Helm chart, a `coprocessor` chart would be deployed independently of the router. This chart would contain the configuration for the coprocessor's deployment. An example folder structure might look like:

```text
charts/
├── coprocessor/
│   ├── Chart.yaml
│   ├── values.yaml
│   ├── templates/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   └── ...
│   └── ...
├── router/
│   ├── values.yaml
│   └── ...
```

The `router` chart would be the router's Helm chart, which you can deploy as described in the [Kubernetes deployment guide](https://www.apollographql.com/docs/graphos/routing/self-hosted/containerization/kubernetes/quickstart).

#### Using the router's Helm chart as a dependency

In the case of using the router's Helm chart as a dependency, you can create a new  template in the `templates` folder of the `router` Helm chart. This template would contain the configuration for the coprocessor's deployment.

The `Chart.yaml` file for the router would include:

```yaml
dependencies:
  - name: router
    version: 2.3.0
    repository: oci://ghcr.io/apollographql/helm-charts
```

An example folder structure might look like:

```text
charts/
├── router/
│   ├── Chart.yaml
│   ├── values.yaml
│   ├── templates/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   └── ...
│   └── ...
```

In the above example, the `router` chart would be the router's Helm chart, which you can deploy as described in the [Kubernetes deployment guide](https://www.apollographql.com/docs/graphos/routing/self-hosted/containerization/kubernetes/quickstart). The `templates` folder would contain the configuration for the coprocessor's deployment. Within the `values.yaml` you can then nest the necessary configuration under the `router` key, such as:

```values.yaml
router:
  configuration:
    coprocessor:
      url: http://<coprocessor-service-name>:<coprocessor-container-port>
```
