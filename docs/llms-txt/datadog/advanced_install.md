# Source: https://docs.datadoghq.com/containers/datadog_operator/advanced_install.md

---
title: Installing the Datadog Operator
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Container Monitoring > Datadog Operator > Installing the Datadog
  Operator
source_url: https://docs.datadoghq.com/datadog_operator/advanced_install/index.html
---

# Installing the Datadog Operator

This document contains detailed information about installing the Datadog Operator. For basic installation instructions for the Datadog Agent on Kubernetes, see [Install the Datadog Agent on Kubernetes](https://docs.datadoghq.com/containers/kubernetes/installation).

## Prerequisites{% #prerequisites %}

- **Kubernetes Cluster version >= v1.20.X**: Tests were performed on Kubernetes versions >= `1.20.0`. It is expected to work on versions `>= v1.11.0`, but for earlier versions the Operator may not work as expected because of limited CRD support.
- **[Helm](https://helm.sh)** for deploying the Datadog Operator
- **[`kubectl` CLI](https://kubernetes.io/docs/tasks/tools/install-kubectl/)** for installing the Datadog Agent

## Install the Datadog Operator with Helm{% #install-the-datadog-operator-with-helm %}

You can deploy the Datadog Operator in your cluster using the [Datadog Operator Helm chart](https://artifacthub.io/packages/helm/datadog/datadog-operator):

```shell
helm repo add datadog https://helm.datadoghq.com
helm install my-datadog-operator datadog/datadog-operator
```

To customize the Operator configuration, create a `values.yaml` file that can override the default Helm chart values.

For instance:

```yaml
image:
  tag: 1.2.0
clusterName: my-cluster
datadogMonitor:
  enabled: true
```

Then, to update the Helm release, run:

```shell
helm upgrade my-datadog-operator datadog/datadog-operator -f values.yaml
```

### Add credentials{% #add-credentials %}

1. Create a Kubernetes Secret that contains your API and application keys.

   ```gdscript3
   export DD_API_KEY=<YOUR_API_KEY>
   export DD_APP_KEY=<YOUR_APP_KEY>
   
   kubectl create secret generic datadog-operator-secret --from-literal api-key=$DD_API_KEY --from-literal app-key=$DD_APP_KEY
   ```

1. Reference this Secret in your `values.yaml` file.

   ```yaml
   apiKeyExistingSecret: datadog-operator-secret
   appKeyExistingSecret: datadog-operator-secret
   image:
     tag: 1.2.0
   datadogMonitor:
     enabled: true
   ```

1. Update the Helm release.

   ```shell
   helm upgrade my-datadog-operator datadog/datadog-operator -f values.yaml
   ```

### Configure cluster name (optional){% #configure-cluster-name-optional %}

Setting a cluster name is optional but recommended. The cluster name can be configured in the following ways:

- **Helm chart `clusterName` value** (sets `DD_CLUSTER_NAME` environment variable on the Operator):

  ```yaml
  clusterName: my-cluster
  ```

- **DatadogAgent CRD `spec.global.clusterName`**:

  ```yaml
  apiVersion: datadoghq.com/v2alpha1
  kind: DatadogAgent
  metadata:
    name: datadog
  spec:
    global:
      clusterName: my-cluster
  ```

## Install the Datadog Operator with Operator Lifecycle Manager{% #install-the-datadog-operator-with-operator-lifecycle-manager %}

Instructions for deploying the Datadog Operator with [Operator Lifecycle Manager](https://olm.operatorframework.io/) (OLM) are available at [operatorhub.io](https://operatorhub.io/operator/datadog-operator).

### Override the default Operator configuration with OLM{% #override-the-default-operator-configuration-with-olm %}

The [Operator Lifecycle Manager](https://olm.operatorframework.io/) framework allows overriding the default Operator configuration. See [Subscription Config](https://github.com/operator-framework/operator-lifecycle-manager/blob/master/doc/design/subscription-config.md) for a list of the supported installation configuration parameters.

For example, the following [Operator Lifecycle Manager](https://olm.operatorframework.io/) `Subscription` changes the Datadog Operator's Pod resources:

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: my-datadog-operator
  namespace: operators
spec:
  channel: stable
  name: datadog-operator
  source: operatorhubio-catalog
  sourceNamespace: olm
  config:
    resources:
      requests:
        memory: "250Mi"
        cpu: "250m"
      limits:
        memory: "250Mi"
        cpu: "500m"
```

### Add credentials{% #add-credentials-1 %}

1. Create a Kubernetes Secret that contains your API and application keys.

   ```gdscript3
   export DD_API_KEY=<YOUR_API_KEY>
   export DD_APP_KEY=<YOUR_APP_KEY>
   
   kubectl create secret generic datadog-operator-secret --from-literal api-key=$DD_API_KEY --from-literal app-key=$DD_APP_KEY
   ```

1. Add references to the Secret in the Datadog Operator `Subscription` resource instance.

   ```yaml
   apiVersion: operators.coreos.com/v1alpha1
   kind: Subscription
   metadata:
     name: my-datadog-operator
     namespace: operators
   spec:
     channel: stable
     name: datadog-operator
     source: operatorhubio-catalog
     sourceNamespace: olm
     config:
       env:
         - name: DD_API_KEY
           valueFrom:
             secretKeyRef: 
                key: api-key
                name: datadog-operator-secret
         - name: DD_APP_KEY
           valueFrom:
             secretKeyRef: 
               key: app-key
               name: datadog-operator-secret
   ```

## Deploy the DatadogAgent custom resource managed by the Operator{% #deploy-the-datadogagent-custom-resource-managed-by-the-operator %}

After deploying the Datadog Operator, create the `DatadogAgent` resource that triggers the deployment of the Datadog Agent, Cluster Agent, and Cluster Checks Runners (if used) in your Kubernetes cluster. The Datadog Agent is deployed as a DaemonSet, running a pod on every node of your cluster.

1. Create a Kubernetes secret with your API and application keys.

   ```gdscript3
   export DD_API_KEY=<YOUR_API_KEY>
   export DD_APP_KEY=<YOUR_APP_KEY>
   
   kubectl create secret generic datadog-secret --from-literal api-key=<DATADOG_API_KEY> --from-literal app-key=<DATADOG_APP_KEY>
   ```

1. Create a file with the spec of your `DatadogAgent` deployment configuration. The simplest configuration is:

   ```yaml
   apiVersion: datadoghq.com/v1alpha1
   kind: DatadogAgent
   metadata:
     name: datadog
   spec:
     credentials:
       apiSecret:
         secretName: datadog-secret
         keyName: api-key
       appSecret:
         secretName: datadog-secret
         keyName: app-key
   ```

1. Deploy the Datadog Agent with the above configuration file:

   ```shell
   kubectl apply -f /path/to/your/datadog-agent.yaml
   ```

In a cluster with two worker nodes, you should see the Agent Pods created on each node.

```console
$ kubectl get daemonset
NAME            DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
datadog-agent   2         2         2       2            2           <none>          5m30s

$ kubectl get pod -owide
NAME                                         READY   STATUS    RESTARTS   AGE     IP            NODE
agent-datadog-operator-d897fc9b-7wbsf        1/1     Running   0          1h      10.244.2.11   kind-worker
datadog-agent-k26tp                          1/1     Running   0          5m59s   10.244.2.13   kind-worker
datadog-agent-zcxx7                          1/1     Running   0          5m59s   10.244.1.7    kind-worker2
```

### Tolerations{% #tolerations %}

Update your [`datadog-agent.yaml` file](https://github.com/DataDog/datadog-operator/blob/main/examples/datadogagent/datadog-agent-with-tolerations.yaml) with the following configuration to add tolerations in the `Daemonset.spec.template` of your DaemonSet:

```yaml
apiVersion: datadoghq.com/v1alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  credentials:
    apiSecret:
      secretName: datadog-secret
      keyName: api-key
    appSecret:
      secretName: datadog-secret
      keyName: app-key
  agent:
    config:
      tolerations:
       - operator: Exists
```

Apply this new configuration:

```console
$ kubectl apply -f datadog-agent.yaml
datadogagent.datadoghq.com/datadog updated
```

Validate the DaemonSet update by looking at the new `desired` Pod value:

```console
$ kubectl get daemonset
NAME            DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
datadog-agent   3         3         3       3            3           <none>          7m31s

$ kubectl get pod
NAME                                         READY   STATUS     RESTARTS   AGE
agent-datadog-operator-d897fc9b-7wbsf        1/1     Running    0          15h
datadog-agent-5ctrq                          1/1     Running    0          7m43s
datadog-agent-lkfqt                          0/1     Running    0          15s
datadog-agent-zvdbw                          1/1     Running    0          8m1s
```

## Configuration{% #configuration %}

For a full list of configuration options, see the [configuration spec](https://github.com/DataDog/datadog-operator/blob/main/docs/configuration.v2alpha1.md).

## Install the kubectl plugin{% #install-the-kubectl-plugin %}

See the [`kubectl` plugin documentation](https://github.com/DataDog/datadog-operator/blob/main/docs/kubectl-plugin.md).

## Use a custom Datadog Operator image{% #use-a-custom-datadog-operator-image %}

See instructions to build a Datadog Operator custom container image based on an official release in [Custom Operator container images](https://github.com/DataDog/datadog-operator/blob/main/docs/custom-operator-image.md).

### Datadog Operator images with Helm charts{% #datadog-operator-images-with-helm-charts %}

To install a custom Datadog Operator image using the Helm chart, run the following:

```shell
helm install my-datadog-operator --set image.repository=<custom-image-repository> --set image.tag=<custom-image-tag> datadog/datadog-operator
```

## Cleanup{% #cleanup %}

The following command deletes all the Kubernetes resources created by the Datadog Operator and the linked `DatadogAgent` `datadog`.

```shell
kubectl delete datadogagent datadog
```

This command outputs `datadogagent.datadoghq.com/datadog deleted`.

You can then remove the Datadog Operator with the `helm delete` command:

```shell
helm delete my-datadog-operator
```
