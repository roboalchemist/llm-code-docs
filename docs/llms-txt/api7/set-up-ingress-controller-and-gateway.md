# Source: https://docs.api7.ai/ingress-controller/set-up-ingress-controller-and-gateway.md

# Set Up Ingress Controller and Gateway

This tutorial focuses on setting up APISIX Ingress Controller and APISIX gateway on a Kubernetes cluster for local learning and testing.

for API7 Enterprise users

If you are using API7 Enterprise, the API7 Dashboard will guide you through the setup of API7 Ingress Controller and Gateway, including generating the necessary deployment scripts. Make sure that you:

* Create a new gateway group of type **Ingress Controller**. The Dashboard will then generate deployment steps for the following, based on the **namespace** and **name** you specified:

  <!-- -->

  * Install the Ingress Controller.
  * Deploy the GatewayProxy configuration. Select the **Gateway API** tab if you plan to use Gateway API, or the **Ingress** tab if you plan to use Ingress or APISIX CRDs.

* Deploy a Gateway instance on Kubernetes.

Once completed, skip to the [next tutorial](https://docs.api7.ai/ingress-controller/proxy-requests-to-a-service.md) where you will learn how to create a route that proxies requests to an upstream service on the same cluster.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* Install [Docker](https://docs.docker.com/get-docker/) as a dependency of [kind](https://kind.sigs.k8s.io).
* Install [kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation) and create a local cluster, or use any existing Kubernetes cluster (version 1.26+).
* Install [Helm](https://helm.sh/docs/intro/install/) (version 3.8+).
* Install [kubectl](https://kubernetes.io/docs/tasks/tools/).

## Create a Namespace[â](#create-a-namespace "Direct link to Create a Namespace")

Create a new namespace `aic` (or any name of your choice):

```
kubectl create namespace aic
```

Optionally, you can set the namespace as the preferred namespace:

```
kubectl config set-context --current --namespace=aic
```

## Install APISIX and APISIX Ingress Controller[â](#install-apisix-and-apisix-ingress-controller "Direct link to Install APISIX and APISIX Ingress Controller")

In this section, you will install APISIX and APISIX Ingress Controller in standalone mode on your Kubernetes cluster.

Deployment Mode

The standalone mode is recommended over the traditional etcd-based deployment, as it avoids the stability issues that can occur when running APISIX and etcd together inside Kubernetes.

Install APISIX and APISIX Ingress Controller:

```
helm repo add apisix https://apache.github.io/apisix-helm-chart
helm repo update

helm install apisix \
  --namespace aic \
  --create-namespace \
  --set apisix.deployment.role=traditional \
  --set apisix.deployment.role_traditional.config_provider=yaml \
  --set etcd.enabled=false \
  --set ingress-controller.enabled=true \
  --set ingress-controller.config.provider.type=apisix-standalone \
  --set ingress-controller.apisix.adminService.namespace=aic \
  --set ingress-controller.gatewayProxy.createDefault=true \
  apisix/apisix
```

â¶&â· Start APISIX in [API-driven standalone mode](https://docs.api7.ai/apisix/production/deployment-modes.md#api-driven).

â¸ Disable the etcd deployment.

â¹ Install APISIX Ingress Controller (along with APISIX).

âº Configure the controller to operate in standalone mode, where configuration is pushed directly to the gateway instead of using etcd.

â Configure the namespace of the APISIX Admin Service that the controller will connect to for pushing configurations.

â Automatically creates a GatewayProxy resource that defines the connection information with APISIX.

See the GatewayProxy resource

Find the name of the GatewayProxy:

```
kubectl get gatewayproxy
```

You should see name of the GatewayProxy:

```
NAME            AGE
apisix-config   12s
```

Show the configuration of the GatewayProxy resource in YAML format:

```
kubectl get gatewayproxy apisix-config -o yaml
```

You should see the configuration of the GatewayProxy resource similar to the following:

```
apiVersion: apisix.apache.org/v1alpha1
kind: GatewayProxy
metadata:
  annotations:
    meta.helm.sh/release-name: apisix
    meta.helm.sh/release-namespace: aic
  creationTimestamp: "2025-11-25T10:07:40Z"
  generation: 1
  labels:
    app.kubernetes.io/managed-by: Helm
  name: apisix-config
  namespace: aic
  resourceVersion: "3073"
  uid: 6b0a30db-530c-4f14-b127-024d0507b18e
spec:
  provider:
    controlPlane:
      auth:
        adminKey:
          value: edd1c9f034335f136f87ad84b625c8f1
        type: AdminKey
      service:
        name: apisix-admin
        port: 9180
    type: ControlPlane
```

## Verify Installation[â](#verify-installation "Direct link to Verify Installation")

To verify that APISIX Ingress Controller is installed and running, check the status of the pods:

```
kubectl get pods
```

If everything is ok, you should see that all pods are in the `Running` status:

```
NAME                                        READY   STATUS    RESTARTS   AGE
apisix-bffb459b8-rcqz7                      1/1     Running   0          2m53s
apisix-ingress-controller-ff66c9585-wlxfh   2/2     Running   0          2m53s
```

You can also check the status of the services:

```
kubectl get services
```

If everything is ok, you should see a response similar to the following:

```
NAME                                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
apisix-admin                            ClusterIP   10.96.61.223    <none>        9180/TCP       2m54s
apisix-gateway                          NodePort    10.96.108.211   <none>        80:30834/TCP   2m54s
apisix-ingress-controller               ClusterIP   10.96.249.157   <none>        8080/TCP       2m54s
apisix-ingress-controller-webhook-svc   ClusterIP   10.96.161.96    <none>        443/TCP        2m54s
```

To check the installed APISIX version, first map the gateway service port to the local machine's port:

```
kubectl port-forward svc/apisix-gateway 9080:80 &
```

Then send a request to the gateway:

```
curl -sI "http://127.0.0.1:9080" | grep Server
```

If everything is ok, you should see the APISIX version:

```
Server: APISIX/3.15.0
```

info

If you would like to use a load balancer to expose the service on the kind cluster as an alternative to port forwarding, see [load balancer kind documentation](https://kind.sigs.k8s.io/docs/user/loadbalancer/).

## Define Controller and Gateway[â](#define-controller-and-gateway "Direct link to Define Controller and Gateway")

See the Gateway API tab if you plan to use Gateway API, or the Ingress tab if you plan to use Ingress or APISIX CRDs.

* Gateway API
* Ingress

If you will be using Gateway API, define the GatewayClass and Gateway resources:

gatewayclass-gateway.yaml

```
apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
  name: apisix
spec:
  controllerName: apisix.apache.org/apisix-ingress-controller
---
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  namespace: aic
  name: apisix
spec:
  gatewayClassName: apisix
  listeners:
  - name: http
    protocol: HTTP
    port: 80
  infrastructure:
    parametersRef:
      group: apisix.apache.org
      kind: GatewayProxy
      name: apisix-config
```

Note that the `port` in the Gateway listener is required but ignored. This is due to limitations in the data plane: it cannot dynamically open new ports. Since the Ingress Controller does not manage the data plane deployment, it cannot automatically update the configuration or restart the data plane to apply port changes.

Apply the configuration to your cluster:

```
kubectl apply -f gatewayclass-gateway.yaml
```

If you will be using Ingress or APISIX CRDs, the following IngressClass resource is already applied during installation. You may proceed without any additional configuration.

```
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
  name: apisix
spec:
  controller: apisix.apache.org/apisix-ingress-controller
  parameters:
    apiGroup: apisix.apache.org
    kind: GatewayProxy
    name: apisix-config
    namespace: aic
    scope: Namespace
```

To learn more about these parameters and how to adjust them as needed, see [Define Controller and Gateway](https://docs.api7.ai/ingress-controller/reference/examples.md#define-controller-and-gateway).

## Next Step[â](#next-step "Direct link to Next Step")

In the [next tutorial](https://docs.api7.ai/ingress-controller/proxy-requests-to-a-service.md), you will learn how to create a route that proxies requests to an upstream service on the same cluster.
