# Source: https://docs.api7.ai/enterprise/best-practices/configure-grpc.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/best-practices/configure-grpc.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/best-practices/configure-grpc.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/best-practices/configure-grpc.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/best-practices/configure-grpc.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/best-practices/configure-grpc.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/best-practices/configure-grpc.md

# Source: https://docs.api7.ai/enterprise/3.8.x/best-practices/configure-grpc.md

# Source: https://docs.api7.ai/enterprise/3.7.x/best-practices/configure-grpc.md

# Source: https://docs.api7.ai/enterprise/3.6.x/best-practices/configure-grpc.md

# Source: https://docs.api7.ai/enterprise/3.5.x/best-practices/configure-grpc.md

# Source: https://docs.api7.ai/enterprise/3.4.x/best-practices/configure-grpc.md

# Source: https://docs.api7.ai/enterprise/3.3.x/best-practices/configure-grpc.md

# Proxy gRPC Traffic

Google Remote Procedure Call (gRPC) is an open-source high-performance Remote Procedure Call (RPC) framework based on HTTP/2 protocol. It uses Protocol Buffers (protobuf) as the Interface Description Language (IDL). API7 Enterprise provides crucial functionalities such as protocol conversion, load balancing, authentication, and authorization, enhancing the potential of gRPC.

This guide shows how to use API7 Enterprise to proxy traffic for gRPC services.

Below is an interactive demo that provides a hands-on introduction to proxying gRPC traffic using API7 Enterprise.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).
2. Complete [Deploy with API7 Ingress Controller on Kubernetes](https://docs.api7.ai/enterprise/3.3.x/deployment/ingress-controller.md) if needed.
3. Install [gRPCurl](https://github.com/fullstorydev/grpcurl) to send requests to gRPC services for validation.

## Deploy an Example gRPC Server[â](#deploy-an-example-grpc-server "Direct link to Deploy an Example gRPC Server")

API7 provides an example gRPC service for testing. You can start the service in Docker or Kubernetes, depending on your API7 installation.

### Start a Server[â](#start-a-server "Direct link to Start a Server")

* Docker
* Kubernetes

Start an example gRPC server in Docker listening on port `50051`:

```
docker run -d \
  --name grpc-service \
  --network=api7-ee_api7 \
  -p 50051:50051 \
  --restart always api7/grpc-server-example:1.0.0
```

Start an example gRPC server listening on port `50051`:

```
kubectl run grpc-service \
  --image=api7/grpc-server-example:1.0.0 \
  --port=50051 \
  --restart=Always
```

You should see a `pod/grpc-service created` response.

### Verify Installation[â](#verify-installation "Direct link to Verify Installation")

* Docker
* Kubernetes

Expose the application's port `50051` through a service:

```
kubectl expose pod grpc-service --port 50051
```

You should see a `service/grpc-service exposed` response.

Port forward `50051` of the service to localhost:

```
kubectl port-forward svc/grpc-service 50051:50051 &
```

Verify whether the gRPC server starts successfully by listing all available gRPC services and methods:

```
grpcurl -plaintext 127.0.0.1:50051 list
```

You should see the following output:

```
grpc.reflection.v1alpha.ServerReflection
helloworld.Greeter
helloworld.TestImport
```

List all the available methods for the `helloworld.Greeter` service:

```
grpcurl -plaintext 127.0.0.1:50051 list helloworld.Greeter
```

You should see the following output:

```
helloworld.Greeter.GetErrResp
helloworld.Greeter.Plus
helloworld.Greeter.SayHello
helloworld.Greeter.SayHelloAfterDelay
helloworld.Greeter.SayHelloBidirectionalStream
helloworld.Greeter.SayHelloClientStream
helloworld.Greeter.SayHelloServerStream
```

## Create a Service and a Route[â](#create-a-service-and-a-route "Direct link to Create a Service and a Route")

In this section, you will be creating a service with a route that proxies traffic to the example gRPC service.

* Dashboard
* ADC
* Ingress Controller

### Create a Service

1. Select **Published Services** of your gateway group from the side navigation bar, then click **Add Service**.
2. Select **Add Manually**.
3. From the dialog box, do the following:

* In the **Name** field, enter `grpc-example`.

* In the **Service Type** field, choose `HTTP(Layer 7 Proxy)`.

* In the **Upstream Scheme** field, choose `gRPC`.

* In the **How to find the upstream** field, choose `Use Nodes`.

* Click **Add Node**.

* From the **Add Node** dialog box, do the following:

  <!-- -->

  * In the **Host** field, enter your private IP address, such as `192.168.2.103`. \*In the **Port** field, enter `50051`.
  * In the **Port** field, enter `50051`.

* Click **Add**.

### Create a Route

1. Inside the service that you just created in the previous step and then click **Add Route**.
2. From the dialog box, do the following:

* In the **Name** field, enter `helloworld.Greeter`.
* In the **Path** field, enter `helloworld.Greeter/SayHello`.
* In the **Methods** field, choose `GET` and `POST`.
* Click **Add**.

Create an ADC configuration file to configure a route to the gRPC service:

adc.yaml

```
services:
  - name: grpc-example
    upstream:
      name: gRPC Upstream
      scheme: grpc
      type: roundrobin
      nodes:
        - host: 192.168.2.103
          port: 50051
          weight: 100
    routes:
      - uris:
          - /helloworld.Greeter/SayHello
        name: helloworld.Greeter
        methods:
          - GET
          - POST
```

Synchronize the configuration to API7 Gateway:

```
adc sync -f adc.yaml
```

Create a Kubernetes manifest file to configure a route to the gRPC service using the ApisixRoute custom resource:

grpc-route.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  name: grpc-route
  # namespace: api7    # replace with your namespace
spec:
  http:
    - name: helloworld-greeter
      match:
        paths:
          - /helloworld.Greeter/SayHello
        methods:
          - GET
          - POST
      backends:
        - serviceName: grpc-service
          servicePort: 50051
```

Create another Kubernetes manifest file to configure the upstream scheme to `grpc` using the ApisixUpstream custom resource:

grpc-upstream.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  name: grpc-service
# namespace: api7    # replace with your namespace
spec:
  scheme: grpc
```

Apply the configurations to your cluster:

```
kubectl apply -f grpc-route.yaml -f grpc-upstream.yaml
```

## Update API7 Gateway to Allow HTTP/2[â](#update-api7-gateway-to-allow-http2 "Direct link to Update API7 Gateway to Allow HTTP/2")

By default, API7 gateway instance supports TLS-encrypted HTTP/2 on port `9443`. For non-encrypted HTTP/2, you can add a new port to the gateway configuration.

In this section, you will be updating the API7 Gateway configuration and deployment to support non-encrypted HTTP/2 on `9081`.

* Docker
* Kubernetes

Since Docker does not support updating port mappings while the container is running, first remove the `api7-ee-gateway-1` gateway container [started with the installation](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md#install-api7-enterprise).

Next, [start a new gateway instance in Docker](https://docs.api7.ai/enterprise/3.3.x/getting-started/add-gateway-instance.md). Before running the generated deployment command, add the `-p 9081:9081` flag. Your command after modification should look similar to:

```
docker run -d -e API7_CONTROL_PLANE_ENDPOINTS='["https://<YOUR_IP_ADDR>:7943"]' \
  -e API7_GATEWAY_GROUP_SHORT_ID=default \
  -e API7_CONTROL_PLANE_CERT="-----BEGIN CERTIFICATE-----
  <CERT_CONTENT>
  -----END CERTIFICATE-----
  " \
  -e API7_CONTROL_PLANE_KEY="-----BEGIN PRIVATE KEY-----
  <PRIVATE_KEY_VALUE>
  -----END PRIVATE KEY-----
  " \
  -e API7_CONTROL_PLANE_CA="-----BEGIN CERTIFICATE-----
  <CERT_CONTENT>
  -----END CERTIFICATE-----
  " \
  -e API7_CONTROL_PLANE_SNI="api7ee3-dp-manager" \
  -p 9080:9080 \
  -p 9081:9081 \
  -p 9443:9443 \
  api7/api7-ee-3-gateway:<VERSION>
```

Run the command to start the gateway.

Once the gateway is running, update the gateway configuration to allow HTTP/2 on port `9081`:

```
docker exec <api7-ee-gateway-container-name> /bin/sh -c "echo '
nginx_config:
  error_log_level: warn

apisix:
  node_listen:
    - port: 9080
      enable_http2: true
    - port: 9081
      enable_http2: true
' > /usr/local/apisix/conf/config.yaml"
```

Reload the container for configuration changes to take effect:

```
docker exec <api7-ee-gateway-container-name> apisix reload
```

Edit the gateway ConfigMap:

```
kubectl edit cm api7-ee-3-gateway
```

Add the configuration to allow HTTP/2 on `9081` in the ConfigMap:

```
apisix:
  node_listen:
    - port: 9080
      enable_http2: false
    - port: 9081
      enable_http2: true
```

Save the ConfigMap and restart the deployment:

```
kubectl rollout restart deployment api7-ee-3-gateway
```

To add `9081` as a service port, edit the service:

```
kubectl edit svc/api7-ee-3-gateway-gateway
```

Add the following configuration to `ports`:

```
spec:
  ports:
    ...
    - name: http2-non-tls
      port: 9081
      protocol: TCP
      targetPort: 9081
    ...
```

Save the service manifest for changes to take effect.

## Verify Configurations[â](#verify-configurations "Direct link to Verify Configurations")

Download the `helloworld.proto` file [here](https://github.com/api7/grpc_server_example/blob/master/proto/helloworld.proto).

This example uses the `helloworld.proto` file to ensure the gRPCurl CLI tool aligns the request and response format with the gRPC service definition.

* Docker
* Kubernetes

If you have installed the gateway instance in Docker and use Dashboard or ADC for configurations, send a request to the route:

If you have installed the gateway instance on Kubernetes and use Ingress Controller for configurations, first expose the service port to your local machine by port forwarding:

```
kubectl port-forward svc/api7-ee-3-gateway-gateway 9081:9081 &
```

Send a request to the route:

```
grpcurl -plaintext \
  -proto helloworld.proto \
  -d '{"name":"API7"}' \
  "127.0.0.1:9081" \
  "helloworld.Greeter.SayHello"
```

You should see the following output:

```
{
  "message": "Hello API7"
}
```

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts

  <!-- -->

  * [Services](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md)
  * [Routes](https://docs.api7.ai/enterprise/3.3.x/key-concepts/routes.md)
  * [Plugins](https://docs.api7.ai/enterprise/3.3.x/key-concepts/plugins.md)
