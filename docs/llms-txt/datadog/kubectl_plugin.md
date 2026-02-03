# Source: https://docs.datadoghq.com/containers/kubernetes/kubectl_plugin.md

---
title: Datadog Plugin for kubectl
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Containers > Kubernetes > Datadog Plugin for kubectl
---

# Datadog Plugin for kubectl

Datadog provides a `kubectl` plugin with helper utilities that gives visibility into internal components. You can use the plugin with Operator installations or with the Datadog [Helm chart](https://github.com/DataDog/helm-charts/tree/main/charts/datadog).

## Install the plugin{% #install-the-plugin %}

Run:

```shell
kubectl krew install datadog
```

This uses the [Krew plugin manager](https://krew.sigs.k8s.io/).

```console
$ kubectl krew install datadog
Installing plugin: datadog
Installed plugin: datadog
\
 | Use this plugin:
 | 	kubectl datadog
 | Documentation:
 | 	https://github.com/DataDog/datadog-operator
/
```

## Available commands{% #available-commands %}

```console
$ kubectl datadog --help
Usage:
  datadog [command]

Available Commands:
  agent
  clusteragent
  flare        Collect a Datadog's Operator flare and send it to Datadog
  get          Get DatadogAgent deployment(s)
  help         Help about any command
  validate
```

### Agent sub-commands{% #agent-sub-commands %}

```console
$ kubectl datadog agent --help
Usage:
  datadog agent [command]

Available Commands:
  check       Find check errors
  find        Find datadog agent pod monitoring a given pod
  upgrade     Upgrade the Datadog Agent version
```

### Cluster Agent sub-commands{% #cluster-agent-sub-commands %}

```console
$ kubectl datadog clusteragent --help
Usage:
  datadog clusteragent [command]

Available Commands:
  leader      Get Datadog Cluster Agent leader
  upgrade     Upgrade the Datadog Cluster Agent version
```

### Validate sub-commands{% #validate-sub-commands %}

```console
$ kubectl datadog validate ad --help
Usage:
  datadog validate ad [command]

Available Commands:
  pod         Validate the autodiscovery annotations for a pod
  service     Validate the autodiscovery annotations for a service
```
