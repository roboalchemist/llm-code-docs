# Source: https://docs.datadoghq.com/containers/guide/kubernetes-legacy.md

---
title: Legacy Kubernetes versions
description: >-
  Installation instructions and configuration for Datadog Agent on legacy
  Kubernetes versions prior to 1.7.6
breadcrumbs: Docs > Containers > Containers Guides > Legacy Kubernetes versions
---

# Legacy Kubernetes versions

The default configuration targets Kubernetes 1.7.6 and later, as the Agent relies on features and endpoints introduced in this version. More installation steps are required for older versions:

- [RBAC objects](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) (`ClusterRoles` and `ClusterRoleBindings`) are available since Kubernetes 1.6 and OpenShift 3.3, but are available under different `apiVersion` prefixes:

  - `rbac.authorization.k8s.io/v1` in Kubernetes 1.8+ (and OpenShift 3.9+), the default apiVersion

  - `rbac.authorization.k8s.io/v1beta1` in Kubernetes 1.5 to 1.7 (and OpenShift 3.7)

  - `v1` in Openshift 3.3 to 3.6

Apply the Datadog Agent yaml manifests with the following `sed` invocations:

    ```
    sed "s%authorization.k8s.io/v1%authorization.k8s.io/v1beta1%" clusterrole.yaml | kubectl apply -f -
    sed "s%authorization.k8s.io/v1%authorization.k8s.io/v1beta1%" clusterrolebinding.yaml | kubectl apply -f -
    ```

or for Openshift 3.3 to 3.6:

    ```
    sed "s%rbac.authorization.k8s.io/v1%v1%" clusterrole.yaml | oc apply -f -
    sed "s%rbac.authorization.k8s.io/v1%v1%" clusterrolebinding.yaml | oc apply -f -
    ```

- The `kubelet` check retrieves metrics from the Kubernetes 1.7.6+ (OpenShift 3.7.0+) prometheus endpoint. [Enable cAdvisor port mode](https://github.com/DataDog/integrations-core/tree/73b475d0762829a32c70b63da2564eaa15b1d942/kubelet#compatibility) for older versions.

- The default DaemonSet makes use of the [downward API](https://kubernetes.io/docs/tasks/inject-data-application/environment-variable-expose-pod-information) to pass the kubelet's IP to the agent. This only works on versions 1.7 and up. For older versions, here are other ways to enable kubelet connectivity:

  - On version 1.6, use `fieldPath: spec.nodeName` and verify your node name is resolvable and reachable from the pod.
  - If `DD_KUBERNETES_KUBELET_HOST` is unset, the Agent retrieves the node hostname from docker and tries to connect there. See `docker info | grep "Name:"` and verify the name is resolvable and reachable.
  - If the IP of the docker default gateway is constant across your cluster, pass that IP in the `DD_KUBERNETES_KUBELET_HOST` envvar. You can retrieve the IP with the `ip addr show | grep docker0` command.

- The default configuration relies on [bearer token authentication](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#service-account-tokens) to the API server and kubelet. On 1.3, the kubelet does not support bearer token auth, setup client certificates for the `datadog-agent` serviceaccount and pass them to the agent.

## Further Reading{% #further-reading %}

- [Kubernetes DaemonSet Setup](https://docs.datadoghq.com/agent/kubernetes/daemonset_setup/)
- [Kubernetes Host Setup](https://docs.datadoghq.com/agent/kubernetes/host_setup/)
- [Kubernetes Metrics](https://docs.datadoghq.com/agent/kubernetes/metrics/)
