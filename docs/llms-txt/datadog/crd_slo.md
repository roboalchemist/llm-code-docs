# Source: https://docs.datadoghq.com/containers/datadog_operator/crd_slo.md

---
title: DatadogSLO CRD
description: >-
  Create and manage Datadog Service Level Objectives (SLOs) using the DatadogSLO
  custom resource definition
breadcrumbs: Docs > Containers > Datadog Operator > DatadogSLO CRD
---

# DatadogSLO CRD

To create a [Service Level Objective](https://docs.datadoghq.com/service_level_objectives/) (SLO), you can use the Datadog Operator and `DatadogSLO` custom resource definition (CRD).

### Prerequisites{% #prerequisites %}

- [Helm](https://helm.sh/)
- [`kubectl` CLI](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [Datadog Operator](https://docs.datadoghq.com/api/latest/service-level-objectives/#create-an-slo-object) v0.6+

### Setup{% #setup %}

1. Create a file with the spec of your `DatadogSLO` deployment configuration.

**Example**: [Monitor-based](https://docs.datadoghq.com/service_level_objectives/monitor/) SLO

In the `datadog-slo.yaml` file:

   ```yaml
      apiVersion: datadoghq.com/v1alpha1
      kind: DatadogSLO
      metadata:
        name: example-slo-monitor3
        namespace: system
      spec:
        name: example-slo-monitor3
        description: "This is an example monitor SLO from datadog-operator"
        monitorIDs:
          - 1234
        tags:
          - "service:example"
          - "env:prod"
        targetThreshold: "99.9"
        timeframe: "7d"
        type: "monitor"

```

**Example**: [Metric-based](https://docs.datadoghq.com/service_level_objectives/metric/) SLO

In the `datadog-slo.yaml` file:

   ```yaml
      apiVersion: datadoghq.com/v1alpha1
      kind: DatadogSLO
      metadata:
        name: example-slo
        namespace: system
      spec:
        name: example-slo
        description: "This is an example metric SLO from datadog-operator"
        query:
          denominator: "sum:requests.total{service:example,env:prod}.as_count()"
          numerator: "sum:requests.success{service:example,env:prod}.as_count()"
        tags:
          - "service:example"
          - "env:prod"
        targetThreshold: "99.9"
        timeframe: "7d"
        type: "metric"

```

For all available configuration options, see the [Create an SLO object API reference](https://docs.datadoghq.com/api/latest/service-level-objectives/#create-an-slo-object).

1. Deploy your `DatadogSLO`:

   ```shell
   kubectl apply -f /path/to/your/datadog-slo.yaml
   ```

### Additional examples{% #additional-examples %}

[Metric-based SLO with Universal Service Monitoring](https://github.com/DataDog/datadog-operator/blob/main/examples/datadogslo/metric-usm-example.yaml)
