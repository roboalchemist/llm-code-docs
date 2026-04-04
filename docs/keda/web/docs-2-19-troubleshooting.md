# Source: https://keda.sh/docs/2.19/troubleshooting/

Title: KEDA | Troubleshooting

URL Source: https://keda.sh/docs/2.19/troubleshooting/

Markdown Content:
Troubleshooting Latest

How to address commonly encountered KEDA issues

If while setting up KEDA, you get an error: `(v1beta1.external.metrics.k8s.io) status FailedDiscoveryCheck` with a message: `failing or missing response from https://POD-IP:6443/apis/external.metrics.k8s.io/v1beta1: Get "https://POD-IP:6443/apis/external.metrics.k8s.io/v1beta1": Address is not allowed`.

One of the reason for this can be due to CNI like Cilium or any other.

### Before you start [](https://keda.sh/docs/2.19/troubleshooting/#before-you-start)

*   Make sure no network policies are blocking traffic and required CIDR’s are added

### Check the status: [](https://keda.sh/docs/2.19/troubleshooting/#check-the-status)

Find the api service name for the service `keda/keda-metrics-apiserver`:

```
kubectl get apiservice --all-namespaces
```

Check for the status of the api service found in previous step:

```
kubectl get apiservice <apiservicename> -o yaml
```

Example:

```
kubectl get apiservice v1beta1.external.metrics.k8s.io -o yaml
```

If the status is `False`, then there seems to be an issue and network might be the primary reason for it.

### Solution for managed Kubernetes services: [](https://keda.sh/docs/2.19/troubleshooting/#solution-for-managed-kubernetes-services)

In managed Kubernetes services you might solve the issue by updating deployment file of metric-apiserver as below.

```
dnsPolicy: ClusterFirst
    hostNetwork: true
```

Eg: [Modify](https://github.com/kedacore/charts/blob/f70e45e9a21e46036d51f8e16c2c63a7de8eea1b/keda/values.yaml#L42) useHostNetwork in values file.

If while setting up KEDA, you get an error: `(v1beta1.external.metrics.k8s.io) status FailedDiscoveryCheck` with a message: `no response from https://ip:443: Get https://ip:443: net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)`.

One of the reason for this can be that you are behind a proxy network.

### Before you start [](https://keda.sh/docs/2.19/troubleshooting/#before-you-start)

*   Make sure no network policies are blocking traffic

### Check the status [](https://keda.sh/docs/2.19/troubleshooting/#check-the-status)

Find the api service name for the service `keda/keda-metrics-apiserver`:

```
kubectl get apiservice --all-namespaces
```

Check for the status of the api service found in previous step:

```
kubectl get apiservice <apiservicename> -o yaml
```

Example:

```
kubectl get apiservice v1beta1.external.metrics.k8s.io -o yaml
```

If the status is `False`, then there seems to be an issue and proxy network might be the primary reason for it.

### Solution for self-managed Kubernetes cluster [](https://keda.sh/docs/2.19/troubleshooting/#solution-for-self-managed-kubernetes-cluster)

Find the cluster IP for the `keda-metrics-apiserver` and `keda-operator-metrics`:

```
kubectl get services --all-namespaces
```

In the `/etc/kubernetes/manifests/kube-apiserver.yaml` - add the cluster IPs found in the previous step in no_proxy variable.

Reload systemd manager configuration:

```
sudo systemctl daemon-reload
```

Restart kubelet:

```
sudo systemctl restart kubelet
```

Check the API service status and the pods now. Should work!

### Solution for managed Kubernetes services [](https://keda.sh/docs/2.19/troubleshooting/#solution-for-managed-kubernetes-services)

In managed Kubernetes services you might solve the issue by updating firewall rules in your cluster.

#### Google Kubernetes Engine (GKE) [](https://keda.sh/docs/2.19/troubleshooting/#google-kubernetes-engine-gke)

E.g. in GKE private cluster [add](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#add_firewall_rules) port 6443 (kube-apiserver) to allowed ports in master node firewall rules.

Also, if you are using Network Policies in your `kube-system` namespace, make sure they don’t block access for the konnectivity agent via port 6443. You can read more about [konnectivity service](https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication/#konnectivity-service).

In that case, you need to add a similar NetworkPolicy in the `kube-system` namespace:

```
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-egress-from-konnectivity-agent-to-keda
  namespace: kube-system
spec:
  egress:
  - ports:
    - port: 6443
      protocol: TCP
    to:
    - ipBlock:
        cidr: ${KUBE_POD_IP_CIDR}
  podSelector:
    matchLabels:
      k8s-app: konnectivity-agent
  policyTypes:
  - Egress
```

#### Amazon Elastic Kubernetes Service (EKS) [](https://keda.sh/docs/2.19/troubleshooting/#amazon-elastic-kubernetes-service-eks)

E.g. Make sure the Cluster Security group can reach the Nodegroups on TCP 6443. For example, using the [terraform eks module](https://registry.terraform.io/modules/terraform-aws-modules/eks/aws/latest), this is achievable through the addtional nodegroup rules

```
module "eks" {
  source                               = "terraform-aws-modules/eks/aws"
  version                              = "19.5.1"
  ...
  create_node_security_group = true
  node_security_group_additional_rules = {
    keda_metrics_server_access = {
      description                   = "Cluster access to keda metrics"
      protocol                      = "tcp"
      from_port                     = 6443
      to_port                       = 6443
      type                          = "ingress"
      source_cluster_security_group = true
    }
  }
```

As of version `19.6.0` of the `terraform-aws-modules/eks/aws` module it is enough to have `node_security_group_enable_recommended_rules` option enabled(default) to get neccessary security group ingress rule.

When KEDA has upstream errors to get scaler source information it will keep the current instance count of the workload unless the `fallback` section is defined.

This behavior might feel like the autoscaling is not happening, but in reality, it is because of problems related to the scaler source.

You can check if this is your case by reviewing the logs from the KEDA pods where you should see errors in both our Operator and Metrics server. You can also check a status of the ScaledObject (`READY` and `ACTIVE` condition) by running following command:

```
$ kubectl get scaledobject MY-SCALED-OBJECT
```

If you’re encountering the following error when trying to apply a `ScaledObject` using the `kubectl apply` command:

```
kubectl apply -f nginx-scaledobject.yaml
```

And receive an error like:

`Error from server (Timeout): error when applying patch:``{"metadata":{"annotations":{"kubectl.kubernetes.io/last-applied-configuration":"{\"apiVersion\":\"keda.sh/v1alpha1\",\"kind\":\"ScaledObject\",\"metadata\":{\"annotations\":{},\"name\":\"nginx-scaledobject\",\"namespace\":\"default\"},\"spec\":{\"cooldownPeriod\":300,\"maxReplicaCount\":2,\"minReplicaCount\":1,\"pollingInterval\":3,\"scaleTargetRef\":{\"name\":\"nginx-deploy\"},\"triggers\":[{\"metadata\":{\"type\":\"Utilization\",\"value\":\"90\"},\"type\":\"cpu\"}]}}\n"}},"spec":{"maxReplicaCount":2}}``to:``Resource: "keda.sh/v1alpha1, Resource=scaledobjects", GroupVersionKind: "keda.sh/v1alpha1, Kind=ScaledObject"``Name: "nginx-scaledobject", Namespace: "default"``for: "nginx-scaledobject.yaml": error when patching "nginx-scaledobject.yaml": Timeout: request did not complete within requested timeout - context deadline exceeded`.

### Root cause [](https://keda.sh/docs/2.19/troubleshooting/#root-cause)

This issue commonly occurs when the KEDA admission webhook is not reachable by the Kubernetes control plane due to a network connectivity issue, typically on port 9443, which the webhook listens on.

### Solution (For Managed Kubernetes Services) [](https://keda.sh/docs/2.19/troubleshooting/#solution-for-managed-kubernetes-services)

**Step 1**: Enable Debug Logging on the Webhook This helps confirm whether the request is reaching the webhook.

**Option A**: If KEDA was installed via Helm:

Update your values.yaml file:

```
webhooks:
  level: debug
```

Then upgrade your Helm release:

```
helm upgrade <release-name> kedacore/keda -n keda -f values.yaml
```

**Option B**: If KEDA was installed manually (without Helm):

Edit the webhook deployment:

```
kubectl edit deployment keda-admission-webhooks -n keda
```

Add or update the arguments to include:

```
args:
  - "--zap-log-level=debug"
```

**Step 2**: Check Webhook Logs To confirm if the webhook is receiving the request:

```
kubectl logs -l app=keda-admission-webhooks -n keda
```

If no logs appear when you run `kubectl apply`, it means the webhook pod is not being reached.

**Step 3**: Check Network Connectivity Ensure port 9443 is open between:

*   The Kubernetes control plane (where `kubectl apply` runs)

*   The nodes hosting the `keda-admission-webhooks` pod

This often involves configuring firewall rules or security groups to allow traffic from the control plane IP range to the node IP range on port 9443.

### Final Test: [](https://keda.sh/docs/2.19/troubleshooting/#final-test)

After opening port `9443`, try applying your ScaledObject again:

```
kubectl apply -f nginx-scaledobject.yaml
```

If the webhook logs now show activity and the resource is created or properly rejected, the issue is resolved.

Troubleshooting KEDA API Server Throttling
------------------------------------------

If you are experiencing messages like “Waited for … due to client-side throttling” in your KEDA operator logs, it might indicate that the KEDA operator is being throttled by the Kubernetes API server. This can happen in environments with a large number of `ScaledObject` resources.

KEDA provides several command-line flags to control its interaction with the Kubernetes API server. Adjusting these flags can help alleviate client-side throttling.

Key Configuration Parameters [](https://keda.sh/docs/2.19/troubleshooting/#key-configuration-parameters)
--------------------------------------------------------------------------------------------------------

The following flags are relevant for tuning KEDA’s API server interaction:

*   `--kube-api-qps` (Default: `20.0`): This flag sets the maximum queries per second (QPS) that the KEDA operator can make to the Kubernetes API server.
*   `--kube-api-burst` (Default: `30`): This flag sets the maximum burst of requests that the KEDA operator can make to the Kubernetes API server.

The following env variable is relevant for tuning KEDA’s API server interaction:

*   `KEDA_SCALEDOBJECT_CTRL_MAX_RECONCILES` (Default: `5`): This environment variable determines the maximum number of `ScaledObject` resources that the KEDA operator will reconcile concurrently.

Recommendation for Adjusting Flags [](https://keda.sh/docs/2.19/troubleshooting/#recommendation-for-adjusting-flags)
--------------------------------------------------------------------------------------------------------------------

In environments with a large number of `ScaledObject` resources (e.g., 400 or more), the default values for these parameters might be too low.

It is recommended to experiment with increasing the values of these parameters:

*   **`--kube-api-qps` and `--kube-api-burst`**: Increasing these values allows the KEDA operator to make more requests to the API server per unit of time. 
    *   Consider starting by doubling the default values (e.g., set `--kube-api-qps=40` and `--kube-api-burst=60`).
    *   Monitor the impact on both KEDA’s performance and the API server’s load.

*   **`KEDA_SCALEDOBJECT_CTRL_MAX_RECONCILES`**: Increasing this value allows KEDA to process more `ScaledObject` resources in parallel. However, this will also increase the overall load on the API server. 
    *   Consider a moderate increase (e.g., to `10`).
    *   Observe the performance and API server load.

Important Considerations [](https://keda.sh/docs/2.19/troubleshooting/#important-considerations)
------------------------------------------------------------------------------------------------

*   **API Server Load:** Increasing these parameters will inevitably increase the load on the Kubernetes API server. It is crucial to monitor the API server’s performance (CPU, memory, request latency) after making these changes to ensure it is not being overwhelmed.
*   **Gradual Adjustments:** Make adjustments to these parameters gradually. Monitor the system’s behavior closely after each change. This iterative approach will help in finding the optimal values for your specific environment.
*   **Throttling vs. Server Overload:** While these adjustments can help with client-side throttling, if the API server itself is overloaded, these changes might exacerbate the problem. Ensure your Kubernetes API server has sufficient resources (CPU, memory) to handle the increased load.

How to Apply Changes [](https://keda.sh/docs/2.19/troubleshooting/#how-to-apply-changes)
----------------------------------------------------------------------------------------

These flags are typically set when deploying the KEDA operator. You will need to update the KEDA operator’s deployment manifest (e.g., its `Deployment` YAML) to include these flags in the `args` section of the operator container.

**Example (partial Deployment YAML):**

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: keda-operator
  namespace: keda # Or your KEDA installation namespace
spec:
  template:
    spec:
      containers:
      - name: keda-operator # Or keda-metrics-apiserver, depending on which component is throttled
        args:
        - "--kube-api-qps=40"
        - "--kube-api-burst=60"
        env:
        - name: KEDA_SCALEDOBJECT_CTRL_MAX_RECONCILES
          value: "10"
        # ... other existing arguments for the KEDA operator
```

Status Update Optimization [](https://keda.sh/docs/2.19/troubleshooting/#status-update-optimization)
----------------------------------------------------------------------------------------------------

As of recent versions of KEDA, the operator includes built-in optimizations to reduce unnecessary ScaledObject status updates. The operator now:

*   **Compares condition states**: Before updating status, KEDA compares the new conditions (Type, Status, Reason, and Message) with existing ones
*   **Skips redundant updates**: Status updates are only performed when conditions have actually changed
*   **Handles edge cases**: Properly distinguishes between empty condition sets and initialized conditions with ‘Unknown’ status

This optimization is particularly beneficial in environments with many ScaledObjects, as it can significantly reduce the number of API calls made by the KEDA operator, helping to prevent API server throttling issues described above.

For the most up-to-date information about this optimization, refer to the [KEDA CHANGELOG](https://github.com/kedacore/keda/blob/main/CHANGELOG.md).

Expected Impact [](https://keda.sh/docs/2.19/troubleshooting/#expected-impact)
------------------------------------------------------------------------------

With proper configuration and built-in optimizations, users typically experience:

*   **Reduced throttling messages**: Fewer “client-side throttling” warnings in KEDA operator logs
*   **Lower API server load**: Decreased request volume from KEDA operations to the Kubernetes API server
*   **Improved performance**: Better responsiveness in environments with 100+ ScaledObjects
*   **More stable scaling**: Consistent autoscaling behavior without throttling-related delays

Additional Troubleshooting [](https://keda.sh/docs/2.19/troubleshooting/#additional-troubleshooting)
----------------------------------------------------------------------------------------------------

By carefully tuning these parameters and leveraging KEDA’s built-in optimizations, you should be able to reduce or eliminate the client-side throttling experienced by the KEDA operator. If throttling persists even after these adjustments, consider:

*   Further investigation into the API server’s capacity and resource allocation
*   Reviewing your ScaledObject configurations for potential optimizations
*   Consulting the KEDA community for environment-specific guidance

If issues continue, potential code-level optimizations within KEDA might be necessary, and feedback to the KEDA project maintainers would be valuable.

Troubleshooting KEDA API Server Throttling
------------------------------------------

If you are experiencing messages like “Waited for … due to client-side throttling” in your KEDA operator logs, it might indicate that the KEDA operator is being throttled by the Kubernetes API server. This can happen in environments with a large number of `ScaledObject` resources.

KEDA provides several command-line flags to control its interaction with the Kubernetes API server. Adjusting these flags can help alleviate client-side throttling.

Key Configuration Parameters [](https://keda.sh/docs/2.19/troubleshooting/#key-configuration-parameters)
--------------------------------------------------------------------------------------------------------

The following flags are relevant for tuning KEDA’s API server interaction:

*   `--kube-api-qps` (Default: `20.0`): This flag sets the maximum queries per second (QPS) that the KEDA operator can make to the Kubernetes API server.
*   `--kube-api-burst` (Default: `30`): This flag sets the maximum burst of requests that the KEDA operator can make to the Kubernetes API server.

The following env variable is relevant for tuning KEDA’s API server interaction:

*   `KEDA_SCALEDOBJECT_CTRL_MAX_RECONCILES` (Default: `5`): This environment variable determines the maximum number of `ScaledObject` resources that the KEDA operator will reconcile concurrently.

Recommendation for Adjusting Flags [](https://keda.sh/docs/2.19/troubleshooting/#recommendation-for-adjusting-flags)
--------------------------------------------------------------------------------------------------------------------

In environments with a large number of `ScaledObject` resources (e.g., 400 or more), the default values for these parameters might be too low.

It is recommended to experiment with increasing the values of these parameters:

*   **`--kube-api-qps` and `--kube-api-burst`**: Increasing these values allows the KEDA operator to make more requests to the API server per unit of time. 
    *   Consider starting by doubling the default values (e.g., set `--kube-api-qps=40` and `--kube-api-burst=60`).
    *   Monitor the impact on both KEDA’s performance and the API server’s load.

*   **`KEDA_SCALEDOBJECT_CTRL_MAX_RECONCILES`**: Increasing this value allows KEDA to process more `ScaledObject` resources in parallel. However, this will also increase the overall load on the API server. 
    *   Consider a moderate increase (e.g., to `10`).
    *   Observe the performance and API server load.

Important Considerations [](https://keda.sh/docs/2.19/troubleshooting/#important-considerations)
------------------------------------------------------------------------------------------------

*   **API Server Load:** Increasing these parameters will inevitably increase the load on the Kubernetes API server. It is crucial to monitor the API server’s performance (CPU, memory, request latency) after making these changes to ensure it is not being overwhelmed.
*   **Gradual Adjustments:** Make adjustments to these parameters gradually. Monitor the system’s behavior closely after each change. This iterative approach will help in finding the optimal values for your specific environment.
*   **Throttling vs. Server Overload:** While these adjustments can help with client-side throttling, if the API server itself is overloaded, these changes might exacerbate the problem. Ensure your Kubernetes API server has sufficient resources (CPU, memory) to handle the increased load.

How to Apply Changes [](https://keda.sh/docs/2.19/troubleshooting/#how-to-apply-changes)
----------------------------------------------------------------------------------------

These flags are typically set when deploying the KEDA operator. You will need to update the KEDA operator’s deployment manifest (e.g., its `Deployment` YAML) to include these flags in the `args` section of the operator container.

**Example (partial Deployment YAML):**

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: keda-operator
  namespace: keda # Or your KEDA installation namespace
spec:
  template:
    spec:
      containers:
      - name: keda-operator # Or keda-metrics-apiserver, depending on which component is throttled
        args:
        - "--kube-api-qps=40"
        - "--kube-api-burst=60"
        env:
        - name: KEDA_SCALEDOBJECT_CTRL_MAX_RECONCILES
          value: "10"
        # ... other existing arguments for the KEDA operator
```

Status Update Optimization [](https://keda.sh/docs/2.19/troubleshooting/#status-update-optimization)
----------------------------------------------------------------------------------------------------

As of recent versions of KEDA, the operator includes built-in optimizations to reduce unnecessary ScaledObject status updates. The operator now:

*   **Compares condition states**: Before updating status, KEDA compares the new conditions (Type, Status, Reason, and Message) with existing ones
*   **Skips redundant updates**: Status updates are only performed when conditions have actually changed
*   **Handles edge cases**: Properly distinguishes between empty condition sets and initialized conditions with ‘Unknown’ status

This optimization is particularly beneficial in environments with many ScaledObjects, as it can significantly reduce the number of API calls made by the KEDA operator, helping to prevent API server throttling issues described above.

For the most up-to-date information about this optimization, refer to the [KEDA CHANGELOG](https://github.com/kedacore/keda/blob/main/CHANGELOG.md).

Expected Impact [](https://keda.sh/docs/2.19/troubleshooting/#expected-impact)
------------------------------------------------------------------------------

With proper configuration and built-in optimizations, users typically experience:

*   **Reduced throttling messages**: Fewer “client-side throttling” warnings in KEDA operator logs
*   **Lower API server load**: Decreased request volume from KEDA operations to the Kubernetes API server
*   **Improved performance**: Better responsiveness in environments with 100+ ScaledObjects
*   **More stable scaling**: Consistent autoscaling behavior without throttling-related delays

Additional Troubleshooting [](https://keda.sh/docs/2.19/troubleshooting/#additional-troubleshooting)
----------------------------------------------------------------------------------------------------

By carefully tuning these parameters and leveraging KEDA’s built-in optimizations, you should be able to reduce or eliminate the client-side throttling experienced by the KEDA operator. If throttling persists even after these adjustments, consider:

*   Further investigation into the API server’s capacity and resource allocation
*   Reviewing your ScaledObject configurations for potential optimizations
*   Consulting the KEDA community for environment-specific guidance

If issues continue, potential code-level optimizations within KEDA might be necessary, and feedback to the KEDA project maintainers would be valuable.

In Golang we have the possibility to profile specific actions in order to determine what causes an issue. For example, if our `keda-operator` pod is keeps getting OOM after a specific time, using profilig we can profile the heap and see what operatios taking all of this space.

Golang support many profiling options like heap, cpu, goroutines and more… (for more info check this site [https://pkg.go.dev/net/http/pprof)](https://pkg.go.dev/net/http/pprof%29).

In KEDA we provide the option to enable profiling on each component separately by enabling it using the Helm chart and providing a port (if not enabled then it won’t work).

```
profiling:
  operator:
    enabled: false
    port: 8082
  metricsServer:
    enabled: false
    port: 8083
  webhooks:
    enabled: false
    port: 8084
```

If not using the Helm chart then you can enable the profiling on each on of components by specifying the following argument in the respective container

```
--profiling-bind-address=":8082"
```

and it will be exposed on the port you specified.

After enabling it you can port-forward or expose the service and use tool like go tool pprof in order to get profiling data.

For more info look at this document [https://go.dev/blog/pprof](https://go.dev/blog/pprof).

If you are running Google Kubernetes Engine (GKE) version 1.16, and are receiving the following error:

```
unable to fetch metrics from external metrics API: <METRIC>.external.metrics.k8s.io is forbidden: User "system:vpa-recommender" cannot list resource "<METRIC>" in API group "external.metrics.k8s.io" in the namespace "<NAMESPACE>": RBAC: clusterrole.rbac.authorization.k8s.io "external-metrics-reader" not found
```

You are almost certainly running into a [known issue](https://issuetracker.google.com/issues/160597676).

The workaround is to recreate the `external-metrics-reader` role using the following YAML:

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: external-metrics-reader
rules:
- apiGroups:
  - "external.metrics.k8s.io"
  resources:
  - "*"
  verbs:
  - list
  - get
  - watch
```

The GKE team is currently working on a fix that they expect to have out in version >= 1.16.13.

If you are running KEDA on AWS using IRSA or KIAM for pod identity and seeing the following error messages:

```
Events:
  Type     Reason                      Age                From           Message
  ----     ------                      ----               ----           -------
  Normal   KEDAScalersStarted          31s                keda-operator  Started scalers watch
  Normal   KEDAScaleTargetDeactivated  31s                keda-operator  Deactivated apps/v1.Deployment default/my-event-based-deployment from 1 to 0
  Normal   ScaledObjectReady           13s (x2 over 31s)  keda-operator  ScaledObject is ready for scaling
  Warning  KEDAScalerFailed            1s (x2 over 31s)   keda-operator  NoCredentialProviders: no valid providers in chain. Deprecated.
           For verbose messaging see aws.Config.CredentialsChainVerboseErrors
```

And the operator logs:

```
2021-11-02T23:50:29.688Z    ERROR    controller    Reconciler error    {"reconcilerGroup": "keda.sh", "reconcilerKind": "ScaledObject", "controller": "scaledobject", "name": "my-event-based-deployment-scaledobject", "namespace": "default"
, "error": "error getting scaler for trigger #0: error parsing SQS queue metadata: awsAccessKeyID not found"}
```

This means hat the KEDA operator is not receiving valid credentials, even before attempting to assume the IAM role associated with the `scaleTargetRef`.

Some things to check:

*   Ensure the `keda-operator` deployment has the `iam.amazonaws.com/role` annotation under `deployment.spec.template.metadata` not `deployment.metadata` - if using KIAM
*   Ensure the `keda-operator` serviceAccount is annotated `eks.amazonaws.com/role-arn` - if using IRSA
*   Check `kiam-server` logs, successful provisioning of credentials looks like: `kube-system kiam-server-6bb67587bd-2f47p kiam-server {"level":"info","msg":"found role","pod.iam.role":"arn:aws:iam::1234567890:role/my-service-role","pod.ip":"100.64.7.52","time":"2021-11-05T03:13:34Z"}`. 
    *   Use `grep` to filter the `kiam-server` logs, searching for the `keda-operator` pod ip.

Our initial approach to manage CRDs through Helm was not ideal given it didn’t update existing CRDs.

This is a [known limitation of Helm](https://helm.sh/docs/chart_best_practices/custom_resource_definitions/#install-a-crd-declaration-before-using-the-resource):

> There is no support at this time for upgrading or deleting CRDs using Helm. This was an explicit decision after much community discussion due to the danger for unintentional data loss. Furthermore, there is currently no community consensus around how to handle CRDs and their lifecycle. As this evolves, Helm will add support for those use cases.

As of [v2.2.1](https://github.com/kedacore/charts/releases/tag/v2.2.1) of our Helm chart, we have changed our approach so that we automatically managing the CRDs through our Helm chart.

Due to this transition, it can cause upgrade failures if you started using KEDA before v2.2.1 and will cause errors during upgrades such as the following:

> Error: UPGRADE FAILED: rendered manifests contain a resource that already exists. Unable to continue with update: CustomResourceDefinition “scaledobjects.keda.sh” in namespace "" exists and cannot be imported into the current release: invalid ownership metadata; label validation error: missing key “app.kubernetes.io/managed-by”: must be set to “Helm”; annotation validation error: missing key “meta.helm.sh/release-name”: must be set to “keda”; annotation validation error: missing key “meta.helm.sh/release-namespace”: must be set to “keda”

In order to fix this, you will need to manually add the following attributes to our CRDs:

*   `app.kubernetes.io/managed-by: Helm` label
*   `meta.helm.sh/release-name: keda` annotation
*   `meta.helm.sh/release-namespace: keda` annotation

Future upgrades should work seamlessly.

While setting up KEDA, you get an error: `(v1beta1.external.metrics.k8s.io) status FailedDiscoveryCheck` and you have [Istio](https://istio.io/) installed as service mesh in your cluster.

This can lead to side effects like not being able to delete namespaces in your cluster. You will see an error like:

`NamespaceDeletionDiscoveryFailure - Discovery failed for some groups, 1 failing: unable to retrieve the complete list of server APIs: external.metrics.k8s.io/v1beta1: the server is currently unable to handle the request`

### Check the setup [](https://keda.sh/docs/2.19/troubleshooting/#check-the-setup)

In the following we assume that KEDA is installed in the namespace `keda`.

#### Check the KEDA API service status [](https://keda.sh/docs/2.19/troubleshooting/#check-the-keda-api-service-status)

Find the api service name for the service `keda/keda-metrics-apiserver`:

```
kubectl get apiservice --all-namespaces
```

Check for the status of the api service found in previous step:

```
kubectl get apiservice <apiservicename> -o yaml
```

Example:

```
kubectl get apiservice v1beta1.external.metrics.k8s.io -o yaml
```

If the status is `False`, then there seems to be an issue with the KEDA installation.

#### Check Istio installation [](https://keda.sh/docs/2.19/troubleshooting/#check-istio-installation)

Check if Istio is installed in your cluster:

```
kubectl get svc -n istio-system
```

If Istio is installed you get a result like:

```
NAME                   TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)                                      AGE
istio-ingressgateway   LoadBalancer   100.65.18.245    34.159.50.243   15021:31585/TCP,80:31669/TCP,443:30464/TCP   3d
istiod                 ClusterIP      100.65.146.141   <none>          15010/TCP,15012/TCP,443/TCP,15014/TCP        3d
```

#### Check KEDA namespace labels [](https://keda.sh/docs/2.19/troubleshooting/#check-keda-namespace-labels)

Check the KEDA namespace labels:

```
kubectl describe ns keda
```

If Istio injection is enabled there is **no** label stating `istio-injection=disabled`.

In this setup the sidecar injection of Istio prevents the api service of KEDA to work properly.

### Solution [](https://keda.sh/docs/2.19/troubleshooting/#solution)

To prevent the side-car injection of Istio we must label the namespace accordingly. This can be achieved via setting the label `istio-injection=disabled` to the namespace:

```
kubectl label namespace keda istio-injection=disabled
```

Check that the label is set via `kubectl describe ns keda`

Install KEDA into the namespace `keda` and re-check the status of the api service which should now have the status `True`.
