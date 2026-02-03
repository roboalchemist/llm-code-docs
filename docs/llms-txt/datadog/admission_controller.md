# Source: https://docs.datadoghq.com/containers/cluster_agent/admission_controller.md

---
title: Datadog Admission Controller
description: >-
  Automatically inject environment variables and standard tags into Kubernetes
  pods using the Datadog Admission Controller
breadcrumbs: >-
  Docs > Containers > Cluster Agent for Kubernetes > Datadog Admission
  Controller
---

# Datadog Admission Controller

## Overview{% #overview %}

The Datadog Admission Controller is a component of the Datadog Cluster Agent. The main benefit of the Admission Controller is to simplify your application Pod configuration. For that, it has two main functionalities:

- Inject environment variables (`DD_AGENT_HOST`, `DD_TRACE_AGENT_URL`, `DD_ENTITY_ID` and `DD_EXTERNAL_ENV`) to configure DogStatsD and APM tracer libraries into the user's application containers.
- Inject Datadog standard tags (`env`, `service`, `version`) from application labels into the container environment variables.

Datadog's Admission Controller is `MutatingAdmissionWebhook` type. For more details on admission controllers, see the [Kubernetes guide on admission controllers](https://kubernetes.io/blog/2019/03/21/a-guide-to-kubernetes-admission-controllers/).

## Requirements{% #requirements %}

- Datadog Cluster Agent v7.40+

## Configuration{% #configuration %}

{% tab title="Datadog Operator" %}
The Datadog Operator enables the Datadog Admission Controller by default. No extra configuration is needed to enable the Admission Controller.

If you disabled Admission Controller, you can re-enable it by setting the parameter `features.admissionController.enabled` to `true` in your `DatadogAgent` configuration:

In the `datadog-agent.yaml` file:

```yaml
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  #(...)
  features:
    admissionController:
      enabled: true
      mutateUnlabelled: false
```

{% /tab %}

{% tab title="Helm" %}
Starting from Helm chart v2.35.0, Datadog Admission Controller is enabled by default. No extra configuration is needed to enable the Admission Controller.

To enable the Admission Controller for Helm chart v2.34.6 and earlier, set the parameter `clusterAgent.admissionController.enabled` to `true`:

In the `datadog-values.yaml` file:

```yaml
#(...)
clusterAgent:
  #(...)
  ## @param admissionController - object - required
  ## Enable the admissionController to automatically inject APM and
  ## DogStatsD config and standard tags (env, service, version) into
  ## your pods
  #
  admissionController:
    enabled: true

    ## @param mutateUnlabelled - boolean - optional
    ## Enable injecting config without having the pod label:
    ## admission.datadoghq.com/enabled="true"
    #
    mutateUnlabelled: false
```

{% /tab %}

{% tab title="DaemonSet" %}
To enable the Admission Controller without using Helm or the Datadog operator, add the following to your configuration:

First, download the [Cluster Agent RBAC permissions](https://raw.githubusercontent.com/DataDog/datadog-agent/master/Dockerfiles/manifests/cluster-agent/cluster-agent-rbac.yaml) manifest, and add the following under `rules`:

In the `cluster-agent-rbac.yaml` file:

```yaml
- apiGroups:
  - admissionregistration.k8s.io
  resources:
  - mutatingwebhookconfigurations
  verbs: ["get", "list", "watch", "update", "create"]
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get", "list", "watch", "update", "create"]
- apiGroups: ["batch"]
  resources: ["jobs", "cronjobs"]
  verbs: ["get"]
- apiGroups: ["apps"]
  resources: ["statefulsets", "replicasets", "deployments"]
  verbs: ["get"]
```

Add the following to the bottom of `agent-services.yaml`:

In the `agent-services.yaml` file:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: datadog-cluster-agent-admission-controller
  labels:
    app: "datadog"
    app.kubernetes.io/name: "datadog"
spec:
  selector:
    app: datadog-cluster-agent
  ports:
  - port: 443
    targetPort: 8000
```

Add environment variables to the Cluster Agent deployment which enable the Admission Controller:

In the `cluster-agent-deployment.yaml` file:

```yaml
- name: DD_ADMISSION_CONTROLLER_ENABLED
  value: "true"
- name: DD_ADMISSION_CONTROLLER_SERVICE_NAME
  value: "datadog-cluster-agent-admission-controller"

# Uncomment this to configure APM tracers automatically (see below)
# - name: DD_ADMISSION_CONTROLLER_MUTATE_UNLABELLED
#   value: "true"
```

Finally, run the following commands:

- `kubectl apply -f cluster-agent-rbac.yaml`
- `kubectl apply -f agent-services.yaml`
- `kubectl apply -f cluster-agent-deployment.yaml`

{% /tab %}

### APM Instrumentation library injection{% #apm-instrumentation-library-injection %}

You can configure the Cluster Agent (version 7.39 and higher) to inject instrumentation libraries using Single Step Instrumentation. Read [Single Step APM Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/) for more information.

If you do not want to use Single Step Instrumentation, the Datadog Admission Controller can be used to inject APM tracer libraries directly as a manual, pod-level alternative. Read [Local SDK Injection](https://docs.datadoghq.com/tracing/guide/local_sdk_injection/) for more information.

### APM and DogStatsD environment variable injection{% #apm-and-dogstatsd-environment-variable-injection %}

To configure DogStatsD clients or other APM libraries that do not support library injection, inject the environment variables `DD_AGENT_HOST` and `DD_ENTITY_ID` by doing one of the following:

- Add the label `admission.datadoghq.com/enabled: "true"` to your Pod.
- Configure the Cluster Agent admission controller by setting `mutateUnlabelled` (or `DD_ADMISSION_CONTROLLER_MUTATE_UNLABELLED`, depending on your configuration method) to `true`.

Adding a `mutateUnlabelled: true` Agent config in the Helm chart causes the Cluster Agent to attempt to intercept every unlabelled Pod.

To prevent Pods from receiving environment variables, add the label `admission.datadoghq.com/enabled: "false"`. This works even if you set `mutateUnlabelled: true`.

If `mutateUnlabelled` is set to `false`, the Pod label must be set to `admission.datadoghq.com/enabled: "true"`.

Possible options:

| mutateUnlabelled | Pod label                               | Injection |
| ---------------- | --------------------------------------- | --------- |
| `true`           | No label                                | Yes       |
| `true`           | `admission.datadoghq.com/enabled=true`  | Yes       |
| `true`           | `admission.datadoghq.com/enabled=false` | No        |
| `false`          | No label                                | No        |
| `false`          | `admission.datadoghq.com/enabled=true`  | Yes       |
| `false`          | `admission.datadoghq.com/enabled=false` | No        |

#### Order of priority{% #order-of-priority %}

The Datadog Admission Controller does not inject the environment variables `DD_VERSION`, `DD_ENV`, or `DD_SERVICE` if they already exist.

When these environment variables are not set, the Admission Controller uses standard tags value in the following order (highest first):

- Labels on the Pod
- Labels on the `ownerReference` (ReplicaSets, DaemonSets, Deployments, etc.)

#### Configure APM and DogstatsD communication mode{% #configure-apm-and-dogstatsd-communication-mode %}

Starting from Datadog Cluster Agent v1.20.0, the Datadog Admission Controller can be configured to inject different modes of communication between the application and Datadog agent.

This feature can be configured by setting `admission_controller.inject_config.mode` or by defining a Pod-specific mode using the `admission.datadoghq.com/config.mode` Pod label.

Starting from Helm chart v3.22.0 and Datadog Operator v1.1.0, the communication mode is automatically set to `socket` if either APM socket or DSD socket is enabled.

Possible options:

| Mode               | Description                                                                                                                                                                                                                            |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `hostip` (Default) | Inject the host IP in `DD_AGENT_HOST` environment variable                                                                                                                                                                             |
| `service`          | Inject Datadog's local-service DNS name in `DD_AGENT_HOST` environment variable (available with Kubernetes v1.22+)                                                                                                                     |
| `socket`           | Inject Unix Domain Socket path in `DD_TRACE_AGENT_URL` environment variable and the volume definition to access the corresponding path. Inject URL to use to connect the Datadog Agent for DogStatsD metrics in `DD_DOGSTATSD_URL`.    |
| `csi`              | Inject Unix Domain Socket paths in `DD_TRACE_AGENT_URL` and `DD_DOGSTATSD_URL` environment variables and the Datadog CSI volume definition to access the corresponding paths. This mode is available for Datadog Cluster Agent v7.67+. |

**Note**: Pod-specific mode takes precedence over the global mode defined at the Admission Controller level.

## Troubleshooting{% #troubleshooting %}

See [Admission Controller Troubleshooting](https://docs.datadoghq.com/containers/troubleshooting/admission-controller).

## Further Reading{% #further-reading %}

- [Troubleshooting the Datadog Cluster Agent](https://docs.datadoghq.com/agent/cluster_agent/troubleshooting/)
- [Troubleshooting the Admission Controller](https://docs.datadoghq.com/containers/troubleshooting/admission-controller)
- [Use library injection to auto-instrument tracing for Kubernetes applications with Datadog APM](https://www.datadoghq.com/blog/auto-instrument-kubernetes-tracing-with-datadog/)
- [Bring high-performance observability to secure Kubernetes environments with Datadog's CSI driver](https://www.datadoghq.com/blog/datadog-csi-driver/)
- [Instrument your app using the Datadog Operator and Admission Controller](https://www.datadoghq.com/architecture/instrument-your-app-using-the-datadog-operator-and-admission-controller/)
- [Disable the Datadog Admission Controller with the Cluster Agent](https://docs.datadoghq.com/containers/guide/cluster_agent_disable_admission_controller)
