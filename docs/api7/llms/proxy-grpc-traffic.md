# Source: https://docs.api7.ai/ingress-controller/proxy-grpc-traffic.md

# Proxy gRPC Traffic

Google Remote Procedure Call (gRPC) is an open-source, high-performance RPC framework built on the HTTP/2 protocol and using Protocol Buffers (protobuf) as its Interface Description Language (IDL).

This guide will show you how to configure the gateway to proxy gRPC traffic using the Ingress Controller.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. Complete [Set Up Ingress Controller and Gateway](https://docs.api7.ai/ingress-controller/set-up-ingress-controller-and-gateway.md).
2. Install [gRPCurl](https://github.com/fullstorydev/grpcurl) to verify gRPC traffic proxying.

## Start an Example Upstream Service[â](#start-an-example-upstream-service "Direct link to Start an Example Upstream Service")

Create a Kubernetes manifest file for the gRPC server deployment and service:

grpc-server.yaml

```
apiVersion: apps/v1
kind: Deployment
metadata:
  namespace: aic
  name: grpc-service
spec:
  replicas: 1
  selector:
    matchLabels:
      app: grpc-service
  template:
    metadata:
      labels:
        app: grpc-service
    spec:
      containers:
        - name: grpc-service
          image: api7/grpc-server-example:1.0.0
          ports:
            - containerPort: 50051
---
apiVersion: v1
kind: Service
metadata:
  namespace: aic
  name: grpc-service
spec:
  type: ClusterIP
  selector:
    app: grpc-service
  ports:
    - name: grpc
      port: 50051
      targetPort: 50051
```

Apply the configuration to your cluster:

```
kubectl apply -f grpc-server.yaml
```

To verify whether the gRPC server is running, first, port forward the gRPC server's service port to your local machine:

```
kubectl port-forward svc/grpc-service 50051:50051 &
```

Send a request to the service to list all available gRPC services and methods:

```
grpcurl -plaintext 127.0.0.1:50051 list
```

If everything is ok, you should see the following response:

```
grpc.reflection.v1alpha.ServerReflection
helloworld.Greeter
helloworld.TestImport
```

List all the available methods for the `helloworld.Greeter` service:

```
grpcurl -plaintext 127.0.0.1:50051 list helloworld.Greeter
```

If everything is ok, you should see the following response:

```
helloworld.Greeter.GetErrResp
helloworld.Greeter.Plus
helloworld.Greeter.SayHello
helloworld.Greeter.SayHelloAfterDelay
helloworld.Greeter.SayHelloBidirectionalStream
helloworld.Greeter.SayHelloClientStream
helloworld.Greeter.SayHelloServerStream
```

## Create a Route[â](#create-a-route "Direct link to Create a Route")

* Gateway API
* APISIX CRD

Create a Kubernetes manifest file to configure a GRPCRoute to the gRPC service:

grpc-route.yaml

```
apiVersion: gateway.networking.k8s.io/v1
kind: GRPCRoute
metadata:
  namespace: aic
  name: grpc-route
spec:
  parentRefs:
  - name: apisix
  rules:
  - matches:
    - method:
        service: helloworld.Greeter
        method: SayHello
    backendRefs:
    - name: grpc-service
      port: 50051
```

Create a Kubernetes manifest file to configure a route to the gRPC service and configure the upstream schema to be `grpc`:

grpc-route.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: aic
  name: grpc-service
spec:
  ingressClassName: apisix
  scheme: grpc
---
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: grpc-route
spec:
  ingressClassName: apisix
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

Apply the configurations to your cluster:

```
kubectl apply -f grpc-route.yaml
```

# Update Gateway Configuration for HTTP/2

By default, the gateway supports TLS-encrypted HTTP/2 on port `9443`. For non-encrypted HTTP/2, you can add a new port to the gateway configuration.

In this section, you will be updating the gateway configuration and deployment to support non-encrypted HTTP/2 on `9081`.

* APISIX Gateway
* API7 Gateway

To update the gateway's HTTP2 configuration, first export all values (including defaults):

```
helm get values -n aic apisix --all > values.yaml
```

In the values file, update the following section values as such:

values.yaml

```
service:
  http:
    containerPort: 9080
    enabled: true
    servicePort: 80
    additionalContainerPorts:
      - port: 9081
        enable_http2: true
```

Upgrade the release:

```
helm upgrade -n aic apisix apisix/apisix -f values.yaml
```

To update the gateway's HTTP2 configuration, first export all values (including defaults):

```
helm get values -n aic api7-ee-3-gateway --all > values.yaml
```

In the values file, update the following section values as such:

values.yaml

```
gateway:
  http:
    enabled: true
    ip: 0.0.0.0
    servicePort: 80
    containerPort: 9080
    additionalContainerPorts:
      - port: 9081
        enable_http2: true
```

Upgrade the release:

```
helm upgrade --install -n aic api7-ee-3-gateway api7/gateway -f values.yaml
```

## Verify[â](#verify "Direct link to Verify")

Download the `helloworld.proto` file [here](https://github.com/api7/grpc_server_example/blob/master/proto/helloworld.proto).

This example uses the `helloworld.proto` file to ensure the gRPCurl CLI tool aligns the request and response format with the gRPC service definition.

Expose the gatewayâs HTTP/2 service port to your local machine:

```
# replace with your gatewayâs service name
kubectl port-forward svc/<gateway-service-name> 9081:9081 &
```

Send a request to the route:

```
grpcurl -plaintext \
  -proto helloworld.proto \
  -d '{"name":"World"}' \
  "127.0.0.1:9081" \
  "helloworld.Greeter.SayHello"
```

You should see the following output:

```
{
  "message": "Hello World"
}
```
