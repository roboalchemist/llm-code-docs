# Source: https://docs.datadoghq.com/containers/guide/autodiscovery-with-jmx.md

---
title: Autodiscovery with JMX
description: >-
  Configure JMX-based integrations for containerized Java applications using
  Autodiscovery templates
breadcrumbs: Docs > Containers > Containers Guides > Autodiscovery with JMX
---

# Autodiscovery with JMX

In containerized environments there are a few differences in how the Agent connects to the JMX server. Autodiscovery features make it possible to dynamically setup these integrations. Use Datadog's JMX based integrations to collect JMX applications metrics from your pods in Kubernetes.

If you are using the Java tracer for your applications, you can alternatively take advantage of the [Java runtime metrics](https://docs.datadoghq.com/tracing/metrics/runtime_metrics/java/) feature to send these metrics to the Agent.

## Installation{% #installation %}

### Use a JMX-enabled Agent{% #use-a-jmx-enabled-agent %}

JMX utilities are not installed in the Agent by default. To set up a JMX integration, append `-jmx` to your Agent's image tag. For example, `gcr.io/datadoghq/agent:latest-jmx`.

If you are using Datadog Operator or Helm, the following configurations append `-jmx` to your Agent's image tag:

{% tab title="Operator" %}

```yaml
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  #(...)
  override:
    nodeAgent:
      image:
        jmxEnabled: true
```

{% /tab %}

{% tab title="Helm" %}

```yaml
agents:
  image:
    tagSuffix: jmx
```

{% /tab %}

## Configuration{% #configuration %}

Use one of the following methods:

- Autodiscovery annotations (recommended)
- Autodiscovery configuration files: for heavy customization of configuration parameters

### Autodiscovery annotations{% #autodiscovery-annotations %}

In this method, a JMX check configuration is applied using annotations on your Java-based Pods. This allows the Agent to automatically configure the JMX check when a new container starts. Ensure these annotations are on the created Pod, and not on the object (Deployment, DaemonSet, etc.) creating the Pod.

Use the following template for Autodiscovery annotations:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: <POD_NAME>
  annotations:
    ad.datadoghq.com/<CONTAINER_NAME>.checks: |
      {
        "<INTEGRATION_NAME>": {
          "init_config": {
            "is_jmx": true,
            "collect_default_metrics": true
          },
          "instances": [{
            "host": "%%host%%",
            "port": "<JMX_PORT>"
          }]
        }
      }
    # (...)
spec:
  containers:
    - name: '<CONTAINER_NAME>'
      # (...)
      env:
        - name: POD_IP
          valueFrom:
            fieldRef:
              fieldPath: status.podIP
        - name: JAVA_OPTS
          value: >-
            -Dcom.sun.management.jmxremote
            -Dcom.sun.management.jmxremote.authenticate=false
            -Dcom.sun.management.jmxremote.ssl=false
            -Dcom.sun.management.jmxremote.local.only=false
            -Dcom.sun.management.jmxremote.port=<JMX_PORT>
            -Dcom.sun.management.jmxremote.rmi.port=<JMX_PORT>
            -Djava.rmi.server.hostname=$(POD_IP)
```

In this example:

- `<POD_NAME>` is the name of your pod.
- `<CONTAINER_NAME>` matches the desired container within your pod.
- `<INTEGRATION_NAME>` is the name of the desired JMX integration. See the list of available JMX integrations.
- Set `<JMX_PORT>` as desired, as long as it matches between the annotations and `JAVA_OPTS`.

With this configuration, the Datadog Agent discovers this pod and makes a request to the JMX server relative to the `%%host%%` [Autodiscovery template variable](https://docs.datadoghq.com/containers/guide/template_variables/)âthis request resolves to the IP address of the discovered pod. This is why `java.rmi.server.hostname` is set to the `POD_IP` address previously populated with the [Kubernetes downward API](https://kubernetes.io/docs/concepts/workloads/pods/downward-api/).

**Note**: The `JAVA_OPTS` environment variable is commonly used in Java-based container images as a startup parameter (for example, `java $JAVA_OPTS -jar app.jar`). If you are using a custom application, or if your application does not follow this pattern, set these system properties manually.

#### Example annotation: Tomcat{% #example-annotation-tomcat %}

The following configuration runs the [Tomcat](https://docs.datadoghq.com/integrations/tomcat/) JMX integration against port `9012`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: tomcat-test
  annotations:
    ad.datadoghq.com/tomcat.checks: |
      {
        "tomcat": {
          "init_config": {
            "is_jmx": true,
            "collect_default_metrics": true
          },
          "instances": [{
            "host": "%%host%%",
            "port": "9012"
          }]
        }
      }
spec:
  containers:
    - name: tomcat
      image: tomcat:8.0
      imagePullPolicy: Always
      ports:
        - name: jmx-metrics
          containerPort: 9012
      env:
        - name: POD_IP
          valueFrom:
            fieldRef:
              fieldPath: status.podIP
        - name: JAVA_OPTS
          value: >-
            -Dcom.sun.management.jmxremote
            -Dcom.sun.management.jmxremote.authenticate=false
            -Dcom.sun.management.jmxremote.ssl=false
            -Dcom.sun.management.jmxremote.local.only=false
            -Dcom.sun.management.jmxremote.port=9012
            -Dcom.sun.management.jmxremote.rmi.port=9012
            -Djava.rmi.server.hostname=$(POD_IP)
```

#### Custom metric annotation template{% #custom-metric-annotation-template %}

If you need to collect additional metrics from these integrations, add them to the `init_config` section:

```yaml
ad.datadoghq.com/<CONTAINER_NAME>.checks: |
  {
    "<INTEGRATION_NAME>": {
      "init_config": {
        "is_jmx": true,
        "collect_default_metrics": true,
        "conf": [{
          "include": {
            "domain": "java.lang",
            "type": "OperatingSystem",
            "attribute": {
               "FreePhysicalMemorySize": {
                 "metric_type": "gauge",
                 "alias": "jvm.free_physical_memory"
               } 
            }
          }
        }]
      },
      "instances": [{
        "host": "%%host%%",
        "port": "<JMX_PORT>"
      }]
    }
  }
```

See the [JMX integration](https://docs.datadoghq.com/integrations/java/) documentation for more information about the formatting for these metrics.

### Autodiscovery configuration files{% #autodiscovery-configuration-files %}

If you need to pass a more complex custom configuration for your Datadog-JMX integration, you can use [Autodiscovery Container Identifiers](https://docs.datadoghq.com/containers/guide/ad_identifiers/?tab=kubernetes) to pass custom integration configuration files as well as a custom `metrics.yaml` file.

#### 1. Compose configuration file

When using this method, the Agent needs a configuration file and an optional `metrics.yaml` file for the metrics to collect. These files can either be mounted into the Agent pod or built into the container image.

The configuration file naming convention is to first identify your desired integration name from the prerequisite steps of available integrations. Once this is determined, the Agent needs a configuration file named relative to that integrationâ*or* within that integration's config directory.

For example, for the [Tomcat](https://docs.datadoghq.com/integrations/tomcat/) integration, create *either*:

- `/etc/datadog-agent/conf.d/tomcat.yaml`, or
- `/etc/datadog-agent/conf.d/tomcat.d/conf.yaml`

If you are using a custom `metrics.yaml` file, include it in the integration's config directory. (For example: `/etc/datadog-agent/conf.d/tomcat.d/metrics.yaml`.)

This configuration file should include `ad_identifiers`:

```yaml
ad_identifiers:
  - <CONTAINER_IMAGE>

init_config:
  is_jmx: true
  conf:
    <METRICS_TO_COLLECT>

instances:
  - host: "%%host%%"
    port: "<JMX_PORT>"
```

Replace `<CONTAINER_IMAGE>` with the short image name of your desired container. For example, the container image `gcr.io/CompanyName/my-app:latest` has a short image name of `my-app`. As the Datadog Agent discovers that container, it sets up the JMX configuration as described in this file.

You can alternatively reference and specify [custom identifiers to your containers](https://docs.datadoghq.com/containers/guide/ad_identifiers/?tab=kubernetes#custom-autodiscovery-container-identifiers) if you do not want to base this on the short image name.

Like Kubernetes annotations, configuration files can use [Autodiscovery template variables](https://docs.datadoghq.com/containers/guide/template_variables/). In this case, the `host` configuration uses `%%host%%` to resolve to the IP address of the discovered container.

See the [JMX integration](https://docs.datadoghq.com/integrations/java/) documentation (as well as the example configurations for the pre-provided integrations) for more information about structuring your `init_config` and `instances` configuration for the `<METRICS_TO_COLLECT>`.

#### 2. Mount configuration file

{% tab title="Operator" %}
If you are using Datadog Operator, add an override:

```yaml
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  #(...)
  override:
    nodeAgent:
      image:
        jmxEnabled: true
      extraConfd:
        configDataMap:
          <INTEGRATION_NAME>.yaml: |-
            ad_identifiers:
              - <CONTAINER_IMAGE>

            init_config:
              is_jmx: true

            instances:
              - host: "%%host%%"
                port: "<JMX_PORT>"
```

{% /tab %}

{% tab title="Helm" %}
In Helm, use the `datadog.confd` option:

```yaml
datadog:
  confd:
    <INTEGRATION_NAME>.yaml: |
      ad_identifiers:
        - <CONTAINER_IMAGE>

      init_config:
        is_jmx: true

      instances:
        - host: "%%host%%"
          port: "<JMX_PORT>"
```

{% /tab %}

{% tab title="Custom image" %}
If you cannot mount these files in the Agent container (for example, on Amazon ECS) you can build an Agent Docker image containing the desired configuration files.

For example:

```Dockerfile
FROM gcr.io/datadoghq/agent:latest-jmx
COPY <PATH_JMX_CONF_FILE> conf.d/tomcat.d/
COPY <PATH_JMX_METRICS_FILE> conf.d/tomcat.d/
```

Then use this new custom image as your regular containerized Agent.
{% /tab %}

#### 3. Expose JMX server

Set up the JMX server in a way that allows the Agent to access it:

```yaml
spec:
  containers:
    - # (...)
      env:
      - name: POD_IP
        valueFrom:
          fieldRef:
            fieldPath: status.podIP
      - name: JAVA_OPTS
        value: >-
          -Dcom.sun.management.jmxremote
          -Dcom.sun.management.jmxremote.authenticate=false
          -Dcom.sun.management.jmxremote.ssl=false
          -Dcom.sun.management.jmxremote.local.only=false
          -Dcom.sun.management.jmxremote.port=<JMX_PORT>
          -Dcom.sun.management.jmxremote.rmi.port=<JMX_PORT>
          -Djava.rmi.server.hostname=$(POD_IP)   
```

## Available JMX integrations{% #available-jmx-integrations %}

The Datadog Agent comes with several JMX integrations pre-configured.

| Integration Name                                                                  | Metrics file                                                                                                                                    | Configuration file                                                                                                                                        |
| --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [activemq](https://docs.datadoghq.com/integrations/activemq/)                     | [metrics.yaml](https://github.com/DataDog/integrations-core/blob/master/activemq/datadog_checks/activemq/data/metrics.yaml)                     | [conf.yaml.example](https://github.com/DataDog/integrations-core/blob/master/activemq/datadog_checks/activemq/data/conf.yaml.example)                     |
| [cassandra](https://docs.datadoghq.com/integrations/cassandra/)                   | [metrics.yaml](https://github.com/DataDog/integrations-core/blob/master/cassandra/datadog_checks/cassandra/data/metrics.yaml)                   | [conf.yaml.example](https://github.com/DataDog/integrations-core/blob/master/cassandra/datadog_checks/cassandra/data/conf.yaml.example)                   |
| [confluent_platform](https://docs.datadoghq.com/integrations/confluent_platform/) | [metrics.yaml](https://github.com/DataDog/integrations-core/blob/master/confluent_platform/datadog_checks/confluent_platform/data/metrics.yaml) | [conf.yaml.example](https://github.com/DataDog/integrations-core/blob/master/confluent_platform/datadog_checks/confluent_platform/data/conf.yaml.example) |
| [hazelcast](https://docs.datadoghq.com/integrations/hazelcast/)                   | [metrics.yaml](https://github.com/DataDog/integrations-core/blob/master/hazelcast/datadog_checks/hazelcast/data/metrics.yaml)                   | [conf.yaml.example](https://github.com/DataDog/integrations-core/blob/master/hazelcast/datadog_checks/hazelcast/data/conf.yaml.example)                   |
| [hive](https://docs.datadoghq.com/integrations/hive/)                             | [metrics.yaml](https://github.com/DataDog/integrations-core/blob/master/hive/datadog_checks/hive/data/metrics.yaml)                             | [conf.yaml.example](https://github.com/DataDog/integrations-core/blob/master/hive/datadog_checks/hive/data/conf.yaml.example)                             |
| [hivemq](https://docs.datadoghq.com/integrations/hivemq/)                         | [metrics.yaml](https://github.com/DataDog/integrations-core/blob/master/hivemq/datadog_checks/hivemq/data/metrics.yaml)                         | [conf.yaml.example](https://github.com/DataDog/integrations-core/blob/master/hivemq/datadog_checks/hivemq/data/conf.yaml.example)                         |
| [hudi](https://docs.datadoghq.com/integrations/hudi/)                             | [metrics.yaml](https://github.com/DataDog/integrations-core/blob/master/hudi/datadog_checks/hudi/data/metrics.yaml)                             | [conf.yaml.example](https://github.com/DataDog/integrations-core/blob/master/hudi/datadog_checks/hudi/data/conf.yaml.example)                             |
| [ignite](https://docs.datadoghq.com/integrations/ignite/)                         | [metrics.yaml](https://github.com/DataDog/integrations-core/blob/master/ignite/datadog_checks/ignite/data/metrics.yaml)                         | [conf.yaml.example](https://github.com/DataDog/integrations-core/blob/master/ignite/datadog_checks/ignite/data/conf.yaml.example)                         |
| [jboss_wildfly](https://docs.datadoghq.com/integrations/jboss_wildfly/)           | [metrics.yaml](https://github.com/DataDog/integrations-core/blob/master/jboss_wildfly/datadog_checks/jboss_wildfly/data/metrics.yaml)           | [conf.yaml.example](https://github.com/DataDog/integrations-core/blob/master/jboss_wildfly/datadog_checks/jboss_wildfly/data/conf.yaml.example)           |
| [kafka](https://docs.datadoghq.com/integrations/kafka/)                           | [metrics.yaml](https://github.com/DataDog/integrations-core/blob/master/kafka/datadog_checks/kafka/data/metrics.yaml)                           | [conf.yaml.example](https://github.com/DataDog/integrations-core/blob/master/kafka/datadog_checks/kafka/data/conf.yaml.example)                           |
| [presto](https://docs.datadoghq.com/integrations/presto/)                         | [metrics.yaml](https://github.com/DataDog/integrations-core/blob/master/presto/datadog_checks/presto/data/metrics.yaml)                         | [conf.yaml.example](https://github.com/DataDog/integrations-core/blob/master/presto/datadog_checks/presto/data/conf.yaml.example)                         |
| [solr](https://docs.datadoghq.com/integrations/solr/)                             | [metrics.yaml](https://github.com/DataDog/integrations-core/blob/master/solr/datadog_checks/solr/data/metrics.yaml)                             | [conf.yaml.example](https://github.com/DataDog/integrations-core/blob/master/solr/datadog_checks/solr/data/conf.yaml.example)                             |
| [sonarqube](https://docs.datadoghq.com/integrations/sonarqube/)                   | [metrics.yaml](https://github.com/DataDog/integrations-core/blob/master/sonarqube/datadog_checks/sonarqube/data/metrics.yaml)                   | [conf.yaml.example](https://github.com/DataDog/integrations-core/blob/master/sonarqube/datadog_checks/sonarqube/data/conf.yaml.example)                   |
| [tomcat](https://docs.datadoghq.com/integrations/tomcat/)                         | [metrics.yaml](https://github.com/DataDog/integrations-core/blob/master/tomcat/datadog_checks/tomcat/data/metrics.yaml)                         | [conf.yaml.example](https://github.com/DataDog/integrations-core/blob/master/tomcat/datadog_checks/tomcat/data/conf.yaml.example)                         |
| [weblogic](https://docs.datadoghq.com/integrations/weblogic/)                     | [metrics.yaml](https://github.com/DataDog/integrations-core/blob/master/weblogic/datadog_checks/weblogic/data/metrics.yaml)                     | [conf.yaml.example](https://github.com/DataDog/integrations-core/blob/master/weblogic/datadog_checks/weblogic/data/conf.yaml.example)                     |

Each integration in the above table has a `metrics.yaml` file predefined to match the expected pattern of the returned JMX metrics per application. Use the listed integration names as `<INTEGRATION_NAME>` in your Autodiscovery annotations or configuration files.

Alternatively use `jmx` as your `<INTEGRATION_NAME>` to set up a basic JMX integration and collect the default `jvm.*` metrics only.

## Further Reading{% #further-reading %}

- [Create and load an Autodiscovery integration template](https://docs.datadoghq.com/agent/kubernetes/integrations/)
- [Match a container with the corresponding integration template](https://docs.datadoghq.com/agent/guide/ad_identifiers/)
- [Manage which container to include in the Agent Autodiscovery](https://docs.datadoghq.com/agent/guide/autodiscovery-management/)
- [Dynamically assign and collect tags from your application](https://docs.datadoghq.com/agent/kubernetes/tag/)
