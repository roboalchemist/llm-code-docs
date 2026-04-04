# Source: https://docs.datadoghq.com/tracing/guide/local_sdk_injection.md

---
title: Local SDK Injection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > APM > Tracing Guides > Local SDK Injection
---

# Local SDK Injection

## Overview{% #overview %}

Use the [Datadog Admission Controller](https://docs.datadoghq.com/containers/cluster_agent/admission_controller/?tab=datadogoperator) to inject APM tracer libraries into Kubernetes workloads using pod-level annotations and labels.

The Datadog Agent uses the Kubernetes Admission Controller to intercept pod creation requests and inject an init container that installs the tracer library before the application starts. This method provides a manual, pod-level alternative to [Single Step Instrumentation (SSI)](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/kubernetes/?tab=agentv764recommended), which uses Helm or the Datadog Operator to configure instrumentation across your cluster.

Use this guide if:

- You want to test library injection on a small number of services before rolling out SSI cluster-wide.
- You're not using Helm or the Datadog Operator, or prefer a lighter-weight integration method.
- You want to control instrumentation directly in your pod specs, rather than through centralized configuration files.

## Requirements{% #requirements %}

- Kubernetes v1.14+
- [Datadog Cluster Agent](https://docs.datadoghq.com/containers/kubernetes/installation/?tab=helm):
  - v7.40+ for Java, Python, and Node.js
  - v7.44+ for .NET and Ruby
- Datadog Admission Controller enabled (enabled by default in Helm chart v2.35.0+)

### Step 1: Enable pod mutation{% #step-1-enable-pod-mutation %}

By default, Datadog Admission controller only mutates pods with the label `admission.datadoghq.com/enabled: "true"`:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    # ...
spec:
  template:
    metadata:
      labels:
        admission.datadoghq.com/enabled: "true"
```

Alternatively, to mutate all pods without requiring the label, do one of the following:

- Configure the Cluster Agent with the following setting:

  ```
  clusterAgent.admissionController.mutateUnlabelled: true
  ```

- Set the environment variable:

  ```gdscript3
  export DD_ADMISSION_CONTROLLER_MUTATE_UNLABELLED=true
  ```

For more details, see the [Datadog Admission Controller documentation](https://docs.datadoghq.com/containers/cluster_agent/admission_controller/?tab=datadogoperator).

### Step 2: Annotate pods for library injection{% #step-2-annotate-pods-for-library-injection %}

#### Specify tracer language and version{% #specify-tracer-language-and-version %}

Use the following pod annotations to specify which language SDK to inject and which version to use:

| Language | Pod annotation                                                        |
| -------- | --------------------------------------------------------------------- |
| Java     | `admission.datadoghq.com/java-lib.version: "<CONTAINER IMAGE TAG>"`   |
| Node.js  | `admission.datadoghq.com/js-lib.version: "<CONTAINER IMAGE TAG>"`     |
| Python   | `admission.datadoghq.com/python-lib.version: "<CONTAINER IMAGE TAG>"` |
| .NET     | `admission.datadoghq.com/dotnet-lib.version: "<CONTAINER IMAGE TAG>"` |
| Ruby     | `admission.datadoghq.com/ruby-lib.version: "<CONTAINER IMAGE TAG>"`   |

Replace `<CONTAINER IMAGE TAG>` with the appropriate value.

For example:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    # (...)
spec:
  template:
    metadata:
      labels:
        admission.datadoghq.com/enabled: "true"
      annotations:
        admission.datadoghq.com/java-lib.version: "v1.12.0"
    spec:
      containers:
        - # (...)
```

To view available library versions, see the tracer repositories for each language:

- [Java](https://github.com/DataDog/dd-trace-java/releases)
- [Node.js](https://github.com/DataDog/dd-trace-js/releases)
- [Python](https://github.com/DataDog/dd-trace-py/releases)
- [.NET](https://github.com/DataDog/dd-trace-dotnet/releases)
- [Ruby](https://github.com/DataDog/dd-trace-rb/releases)
- [PHP](https://github.com/DataDog/dd-trace-php/releases)

**Note:** If a container already includes a manually installed tracer, the injected version takes precedence at runtime.

#### Add Unified Service Tags{% #add-unified-service-tags %}

Use Unified Service Tags (USTs) to apply consistent tags across traces, metrics, and logs, making it easier to navigate and correlate your observability data. See the [UST documentation](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/) to learn how to add USTs to your pods.

### Step 3: Apply your changes and verify injection{% #step-3-apply-your-changes-and-verify-injection %}

After applying your updated pod spec, restart the deployment to trigger injection:

```
kubectl apply -f my-deployment.yaml
```

When injection is successful, the pod includes an init container named `datadog-lib-init`:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_collection/datadog-lib-init.8cb0d7b67ec1868aa1adf81fd601134a.png?auto=format"
   alt="Pod details in Datadog with `datadog-lib-init` listed" /%}

Alternatively, check for `datadog-lib-init` on your pod using:

```
kubectl describe pod <pod-name>
```

You should also see trace data in the [APM](https://app.datadoghq.com/apm/traces) UI shortly after startup.
