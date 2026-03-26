# Source: https://docs.api7.ai/enterprise/3.2.16.7/deployment/ingress-controller.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/deployment/ingress-controller.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/deployment/ingress-controller.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/deployment/ingress-controller.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/deployment/ingress-controller.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/deployment/ingress-controller.md

# Source: https://docs.api7.ai/enterprise/3.8.x/deployment/ingress-controller.md

# Source: https://docs.api7.ai/enterprise/3.7.x/deployment/ingress-controller.md

# Source: https://docs.api7.ai/enterprise/3.6.x/deployment/ingress-controller.md

# Source: https://docs.api7.ai/enterprise/3.5.x/deployment/ingress-controller.md

# Source: https://docs.api7.ai/enterprise/3.4.x/deployment/ingress-controller.md

# Source: https://docs.api7.ai/enterprise/3.3.x/deployment/ingress-controller.md

# Deploy with API7 Ingress Controller on Kubernetes

This tutorial will show you how to deploy API7 Gateway and Ingress Controller on Kubernetes. API7 Ingress Controller allows you to configure API7 Gateway declaratively in Kubernetes. If you do not wish to work with Kubernetes and API7 Ingress Controller, you may skip this tutorial and start with [Launch Your First API](https://docs.api7.ai/enterprise/3.3.x/getting-started/launch-your-first-api.md).

Below is an interactive demo providing a hands-on introduction to this tutorial.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).
2. Have a running Kubernetes cluster.
3. Have [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl) installed.

## Create and Set Namespace[â](#create-and-set-namespace "Direct link to Create and Set Namespace")

You can optionally create a new namespace for the resources and set it as the preferred namespace, so that you do not need to explicitly specify the namespace in every command.

Create a new namespace `api7`:

```
kubectl create namespace api7
```

You should see the namespace has been set:

```
namespace/api7 created
```

## Add a New Gateway Group[â](#add-a-new-gateway-group "Direct link to Add a New Gateway Group")

Navigate to the Dashboard:

1. Select **Gateway Groups** from the side navigation bar and then click **Add Gateway Group**.
2. Select **Ingress Controller** as **Type**.
3. Enter `api7-ingress` in the **Name** field.
4. Click **Add**.

## Install Ingress Controller[â](#install-ingress-controller "Direct link to Install Ingress Controller")

Copy the deployment script generated and run it in the terminal. If deployed successfully, you should see a response similar to the following:

```
NAME: api7-ingress
LAST DEPLOYED: Wed Jun 19 17:20:24 2024
NAMESPACE: api7
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

## Install Gateway Instance[â](#install-gateway-instance "Direct link to Install Gateway Instance")

Navigate to the Dashboard:

1. Select **Gateway Instances** from the side navigation bar and then click **Add Gateway Instance**.
2. Switch to the **Kubernetes** tab.
3. Fill out the namespace and other parameters, and click **Generate** to see the deployment script.
4. Run the deployment script in the terminal.

info

When [installing API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md), a gateway group `default` is initialized with one gateway instance. To avoid port conflicts, you can modify the listening ports of the new gateway instance, or remove the unused instance in the `default` gateway group.

## Verify[â](#verify "Direct link to Verify")

Check the pod status:

```
kubectl get pods
```

You should see all pods in the `Running` status:

```
NAME                                                  READY   STATUS    RESTARTS      AGE
api7-ee-3-gateway-698f85d98b-jxrwp                    1/1     Running      0          6m
api7-ingress-api7-ingress-controller-b4487c7c-p5qzk   1/1     Running      0          10m
```

Check the services:

```
kubectl get services
```

You should see a response similar to the following:

```
NAME                                                  TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)                      AGE
api7-ee-3-gateway-gateway                             NodePort    10.96.106.11   <none>        80:32469/TCP                 6m
api7-ingress-api7-ingress-controller                  ClusterIP   10.96.61.45    <none>        80/TCP                       10m
api7-ingress-api7-ingress-controller-apisix-gateway   NodePort    10.96.85.233   <none>        80:32160/TCP,443:31815/TCP   10m
kubernetes                                            ClusterIP   10.96.0.1      <none>        443/TCP                      10m
```

Navigate back to the Dashboard and select **Gateway Instances**, you should see a gateway instance in `healthy` status. Note that resources created with API7 Ingress Controller will be read-only in the Dashboard.

## Next Steps[â](#next-steps "Direct link to Next Steps")

1. Learn how to create a [gateway instance](https://docs.api7.ai/enterprise/3.3.x/getting-started/add-gateway-instance.md) in the gateway group.
2. Follow the [getting started tutorials](https://docs.api7.ai/enterprise/3.3.x/getting-started/launch-your-first-api.md) to learn more about using API7 Ingress Controller in API7 Enterprise.
