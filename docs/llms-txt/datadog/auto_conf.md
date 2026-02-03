# Source: https://docs.datadoghq.com/containers/guide/auto_conf.md

---
title: Autodiscovery Auto-Configuration
description: >-
  Manage automatic configuration for popular containerized services using
  Autodiscovery auto-configuration templates
breadcrumbs: Docs > Containers > Containers Guides > Autodiscovery Auto-Configuration
---

# Autodiscovery Auto-Configuration

When the Agent runs as a container, [Autodiscovery](https://docs.datadoghq.com/getting_started/containers/autodiscovery) tries to discover other containers based on default configuration files named `auto_conf.yaml`. You can find these files in the corresponding `conf.d/<INTEGRATION>.d/` folders for the following integrations:

| Integration                                                                                | Auto-configuration file                                                                                                                                       |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Apache](https://docs.datadoghq.com/integrations/apache/)                                  | [auto_conf.yaml](https://github.com/DataDog/integrations-core/tree/master/apache/datadog_checks/apache/data/auto_conf.yaml)                                   |
| [Cilium](https://docs.datadoghq.com/integrations/cilium)                                   | [auto_conf.yaml](https://github.com/DataDog/integrations-core/blob/master/cilium/datadog_checks/cilium/data/auto_conf.yaml)                                   |
| [Consul](https://docs.datadoghq.com/integrations/consul/)                                  | [auto_conf.yaml](https://github.com/DataDog/integrations-core/blob/master/consul/datadog_checks/consul/data/auto_conf.yaml)                                   |
| [Coredns](https://docs.datadoghq.com/integrations/coredns/)                                | [auto_conf.yaml](https://github.com/DataDog/integrations-core/blob/master/coredns/datadog_checks/coredns/data/auto_conf.yaml)                                 |
| [Couch](https://docs.datadoghq.com/integrations/couch/)                                    | [auto_conf.yaml](https://github.com/DataDog/integrations-core/blob/master/couch/datadog_checks/couch/data/auto_conf.yaml)                                     |
| [Couchbase](https://docs.datadoghq.com/integrations/couchbase/)                            | [auto_conf.yaml](https://github.com/DataDog/integrations-core/tree/master/couchbase/datadog_checks/couchbase/data/auto_conf.yaml)                             |
| [Elastic](https://docs.datadoghq.com/integrations/elastic/)                                | [auto_conf.yaml](https://github.com/DataDog/integrations-core/blob/master/elastic/datadog_checks/elastic/data/auto_conf.yaml)                                 |
| [Etcd](https://docs.datadoghq.com/integrations/etcd/)                                      | [auto_conf.yaml](https://github.com/DataDog/integrations-core/blob/master/etcd/datadog_checks/etcd/data/auto_conf.yaml)                                       |
| [External DNS](https://docs.datadoghq.com/integrations/external_dns)                       | [auto_conf.yaml](https://github.com/DataDog/integrations-core/blob/master/external_dns/datadog_checks/external_dns/data/auto_conf.yaml)                       |
| [Harbor](https://docs.datadoghq.com/integrations/harbor/)                                  | [auto_conf.yaml](https://github.com/DataDog/integrations-core/blob/master/harbor/datadog_checks/harbor/data/auto_conf.yaml)                                   |
| [Istio](https://docs.datadoghq.com/integrations/istio)                                     | [auto_conf.yaml](https://github.com/DataDog/integrations-core/blob/master/istio/datadog_checks/istio/data/auto_conf.yaml)                                     |
| [Kube APIserver](https://docs.datadoghq.com/agent/kubernetes/)                             | [auto_conf.yaml](https://github.com/DataDog/integrations-core/blob/master/kube_apiserver_metrics/datadog_checks/kube_apiserver_metrics/data/auto_conf.yaml)   |
| [Kube Controller Manager](https://docs.datadoghq.com/integrations/kube_controller_manager) | [auto_conf.yaml](https://github.com/DataDog/integrations-core/blob/master/kube_controller_manager/datadog_checks/kube_controller_manager/data/auto_conf.yaml) |
| [KubeDNS](https://docs.datadoghq.com/agent/kubernetes/)                                    | [auto_conf.yaml](https://github.com/DataDog/integrations-core/blob/master/kube_dns/datadog_checks/kube_dns/data/auto_conf.yaml)                               |
| [Kube Scheduler](https://docs.datadoghq.com/integrations/kube_scheduler)                   | [auto_conf.yaml](https://github.com/DataDog/integrations-core/blob/master/kube_scheduler/datadog_checks/kube_scheduler/data/auto_conf.yaml)                   |
| [Kubernetes State](https://docs.datadoghq.com/agent/kubernetes/)                           | [auto_conf.yaml](https://github.com/DataDog/integrations-core/blob/master/kubernetes_state/datadog_checks/kubernetes_state/data/auto_conf.yaml)               |
| [Kyototycoon](https://docs.datadoghq.com/integrations/kyototycoon/)                        | [auto_conf.yaml](https://github.com/DataDog/integrations-core/blob/master/kyototycoon/datadog_checks/kyototycoon/data/auto_conf.yaml)                         |
| [MemCached](https://docs.datadoghq.com/integrations/mcache/)                               | [auto_conf.yaml](https://github.com/DataDog/integrations-core/blob/master/mcache/datadog_checks/mcache/data/auto_conf.yaml)                                   |
| [Presto](https://docs.datadoghq.com/integrations/presto/)                                  | [auto_conf.yaml](https://github.com/DataDog/integrations-core/blob/master/presto/datadog_checks/presto/data/auto_conf.yaml)                                   |
| [RabbitMQ](https://docs.datadoghq.com/integrations/rabbitmq/)                              | [auto_conf.yaml](https://github.com/DataDog/integrations-core/blob/master/rabbitmq/datadog_checks/rabbitmq/data/auto_conf.yaml)                               |
| [Redis](https://docs.datadoghq.com/integrations/redisdb/)                                  | [auto_conf.yaml](https://github.com/DataDog/integrations-core/blob/master/redisdb/datadog_checks/redisdb/data/auto_conf.yaml)                                 |
| [Riak](https://docs.datadoghq.com/integrations/riak/)                                      | [auto_conf.yaml](https://github.com/DataDog/integrations-core/blob/master/riak/datadog_checks/riak/data/auto_conf.yaml)                                       |
| [Tomcat](https://docs.datadoghq.com/integrations/tomcat/)                                  | [auto_conf.yaml](https://github.com/DataDog/integrations-core/blob/master/tomcat/datadog_checks/tomcat/data/auto_conf.yaml)                                   |

The `auto_conf.yaml` configuration files cover all required parameters to set up a specific integration, with their corresponding [Autodiscovery Templates Variables](https://docs.datadoghq.com/agent/guide/template_variables/) in place to take into account the containerized environment.

## Override auto-configuration{% #override-auto-configuration %}

Each `auto_conf.yaml` file provides a default configuration. To override this, you can add a custom configuration in [Kubernetes annotations](https://docs.datadoghq.com/containers/kubernetes/integrations/?tab=annotations#configuration) or [Docker Labels](https://docs.datadoghq.com/containers/docker/integrations/).

Kubernetes annotations and Docker Labels take precedence over `auto_conf.yaml` files, but `auto_conf.yaml` files take precedence over Autodiscovery configuration set in the Datadog Operator and Helm charts. To use Datadog Operator or Helm to configure Autodiscovery for an integration in the table on this page, you must disable auto-configuration.

## Disable auto-configuration{% #disable-auto-configuration %}

The following examples disable auto-configuration for the Redis and Istio integrations.

{% tab title="Datadog Operator" %}
In your `datadog-agent.yaml`, use `override.nodeAgent.containers.agent.env` to set the `DD_IGNORE_AUTOCONF` environment variable in the `agent` container.

```yaml
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  global:
    credentials:
      apiKey: <DATADOG_API_KEY>

  override:
    nodeAgent:
      containers: 
        agent:
          env:
            - name: DD_IGNORE_AUTOCONF
              value: "redisdb istio"
```

Then, apply the new configuration.
{% /tab %}

{% tab title="Helm" %}
Add `datadog.ignoreAutoconfig` to your `datadog-values.yaml`:

```yaml
datadog:
  #List of integration(s) to ignore auto_conf.yaml.
  ignoreAutoConfig:
    - redisdb
    - istio
```

{% /tab %}

{% tab title="Containerized Agent" %}
To disable auto configuration integration(s) with your containerized agent (manual DaemonSet, Docker, ECS), add the `DD_IGNORE_AUTOCONF` environment variable:

```yaml
DD_IGNORE_AUTOCONF="redisdb istio"
```

{% /tab %}

## Further Reading{% #further-reading %}

- [Configure integrations with Autodiscovery on Kubernetes](https://docs.datadoghq.com/containers/kubernetes/integrations/)
- [Configure integrations with Autodiscovery on Docker](https://docs.datadoghq.com/containers/docker/integrations/)
- [Container Discovery Management](https://docs.datadoghq.com/containers/guide/container-discovery-management/)
