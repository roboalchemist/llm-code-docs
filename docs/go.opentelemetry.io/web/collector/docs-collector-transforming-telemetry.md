# Source: https://opentelemetry.io/docs/collector/transforming-telemetry/

Title: Transforming telemetry

URL Source: https://opentelemetry.io/docs/collector/transforming-telemetry/

Markdown Content:
Transforming telemetry | OpenTelemetry
===============

[OpenTelemetry](https://opentelemetry.io/)

*   [Docs](https://opentelemetry.io/docs/)
*   [Ecosystem](https://opentelemetry.io/ecosystem/)
*   [Status](https://opentelemetry.io/status/)
*   [Community](https://opentelemetry.io/community/)
*   [Training](https://opentelemetry.io/training/)
*   [Blog](https://opentelemetry.io/blog/)
*   
[English EN](https://opentelemetry.io/docs/collector/transforming-telemetry/#)
    *   [বাংলা (Bengali)](https://opentelemetry.io/bn/docs/collector/transforming-telemetry/)
    *   English
    *   [Español](https://opentelemetry.io/es/docs/collector/transforming-telemetry/)
    *   [Français](https://opentelemetry.io/fr/docs/collector/transforming-telemetry/)
    *   [日本語 (Japanese)](https://opentelemetry.io/ja/docs/collector/transforming-telemetry/)
    *   [Português](https://opentelemetry.io/pt/docs/collector/transforming-telemetry/)
    *   [Română (Romanian)](https://opentelemetry.io/ro/docs/collector/transforming-telemetry/)
    *   [Українська (Ukrainian)](https://opentelemetry.io/uk/docs/collector/transforming-telemetry/)
    *   [中文 (Chinese)](https://opentelemetry.io/zh/docs/collector/transforming-telemetry/)

*   
    *    Light 
    *    Dark 
    *    Auto 

*   [Collector](https://opentelemetry.io/docs/collector/)
    *   - [x] [Quick start](https://opentelemetry.io/docs/collector/quick-start/) 
    *   - [x] [Install](https://opentelemetry.io/docs/collector/install/ "Install the Collector") 
        *   - [x] [Docker](https://opentelemetry.io/docs/collector/install/docker/ "Install the Collector with Docker") 
        *   - [x] [Kubernetes](https://opentelemetry.io/docs/collector/install/kubernetes/ "Install the Collector with Kubernetes") 
        *   - [x] [Binary](https://opentelemetry.io/docs/collector/install/binary/ "Install from a Collector binary") 
            *   - [x] [Linux](https://opentelemetry.io/docs/collector/install/binary/linux/ "Install the Collector on Linux") 
            *   - [x] [macOS](https://opentelemetry.io/docs/collector/install/binary/macos/ "Install the Collector on macOS") 
            *   - [x] [Windows](https://opentelemetry.io/docs/collector/install/binary/windows/ "Install the Collector on Windows") 

    *   - [x] [Deploy](https://opentelemetry.io/docs/collector/deploy/ "Deploy the Collector") 
        *   - [x] [Agent pattern](https://opentelemetry.io/docs/collector/deploy/agent/ "Agent deployment pattern") 
        *   - [x] [Gateway pattern](https://opentelemetry.io/docs/collector/deploy/gateway/ "Gateway deployment pattern") 
        *   - [x] [Other patterns](https://opentelemetry.io/docs/collector/deploy/other/ "Other deployment patterns") 
            *   - [x] [No Collector](https://opentelemetry.io/docs/collector/deploy/other/no-collector/) 

    *   - [x] [Configuration](https://opentelemetry.io/docs/collector/configuration/) 
    *   - [x] [Components](https://opentelemetry.io/docs/collector/components/) 
        *   - [x] [Receivers](https://opentelemetry.io/docs/collector/components/receiver/) 
        *   - [x] [Processors](https://opentelemetry.io/docs/collector/components/processor/) 
        *   - [x] [Exporters](https://opentelemetry.io/docs/collector/components/exporter/) 
        *   - [x] [Connectors](https://opentelemetry.io/docs/collector/components/connector/) 
        *   - [x] [Extensions](https://opentelemetry.io/docs/collector/components/extension/) 

    *   - [x] [Management](https://opentelemetry.io/docs/collector/management/) 
    *   - [x] [Distributions](https://opentelemetry.io/docs/collector/distributions/) 
    *   - [x] [Internal telemetry](https://opentelemetry.io/docs/collector/internal-telemetry/) 
    *   - [x] [Troubleshooting](https://opentelemetry.io/docs/collector/troubleshooting/) 
    *   - [x] [Scaling the Collector](https://opentelemetry.io/docs/collector/scaling/) 
    *   - [x] [Transforming telemetry](https://opentelemetry.io/docs/collector/transforming-telemetry/) 
    *   - [x] [Architecture](https://opentelemetry.io/docs/collector/architecture/) 
    *   - [x] [Extend](https://opentelemetry.io/docs/collector/extend/ "Extend the Collector") 
        *   - [x] [Build from source](https://opentelemetry.io/docs/collector/extend/build-from-source/) 
        *   - [x] [Build a custom Collector](https://opentelemetry.io/docs/collector/extend/ocb/ "Build a custom Collector with OpenTelemetry Collector Builder") 
        *   - [x] [Build custom components](https://opentelemetry.io/docs/collector/extend/custom-component/) 
            *   - [x] [Receivers](https://opentelemetry.io/docs/collector/extend/custom-component/receiver/ "Build a receiver") 
            *   - [x] [Connectors](https://opentelemetry.io/docs/collector/extend/custom-component/connector/ "Build a connector") 
            *   - [x] [Extensions](https://opentelemetry.io/docs/collector/extend/custom-component/extension/ "Build an extension") 
                *   - [x] [Authenticator](https://opentelemetry.io/docs/collector/extend/custom-component/extension/authenticator/ "Build an authenticator extension") 

    *   - [x] [Benchmarks](https://opentelemetry.io/docs/collector/benchmarks/) 
    *   - [x] [Registry](https://opentelemetry.io/docs/collector/registry/) 
    *   - [x] [Resiliency](https://opentelemetry.io/docs/collector/resiliency/) 

[View page source](https://github.com/open-telemetry/opentelemetry.io/tree/main/content/en/docs/collector/transforming-telemetry.md)[Edit this page](https://github.com/open-telemetry/opentelemetry.io/edit/main/content/en/docs/collector/transforming-telemetry.md)[Create child page](https://github.com/open-telemetry/opentelemetry.io/new/main/content/en/docs/collector?filename=change-me.md&value=---%0Atitle%3A+%22Long+Page+Title%22%0AlinkTitle%3A+%22Short+Nav+Title%22%0Aweight%3A+100%0Adescription%3A+%3E-%0A+++++Page+description+for+heading+and+indexes.%0A---%0A%0A%23%23+Heading%0A%0AEdit+this+template+to+create+your+new+page.%0A%0A%2A+Give+it+a+good+name%2C+ending+in+%60.md%60+-+e.g.+%60get-started.md%60%0A%2A+Edit+the+%22front+matter%22+section+at+the+top+of+the+page+%28weight+controls+how+its+ordered+amongst+other+pages+in+the+same+directory%3B+lowest+number+first%29.%0A%2A+Add+a+good+commit+message+at+the+bottom+of+the+page+%28%3C80+characters%3B+use+the+extended+description+field+for+more+detail%29.%0A%2A+Create+a+new+branch+so+you+can+preview+your+new+file+and+request+a+review+via+Pull+Request.%0A)[Create documentation issue](https://github.com/open-telemetry/opentelemetry.io/issues/new?title=Transforming%20telemetry)

On this page[](https://opentelemetry.io/docs/collector/transforming-telemetry/# "Top of page")

*   [Basic filtering](https://opentelemetry.io/docs/collector/transforming-telemetry/#basic-filtering)
*   [Adding or Deleting Attributes](https://opentelemetry.io/docs/collector/transforming-telemetry/#adding-or-deleting-attributes)
*   [Renaming Metrics or Metric Labels](https://opentelemetry.io/docs/collector/transforming-telemetry/#renaming-metrics-or-metric-labels)
*   [Enriching Telemetry with Resource Attributes](https://opentelemetry.io/docs/collector/transforming-telemetry/#enriching-telemetry-with-resource-attributes)
*   [Setting a span status](https://opentelemetry.io/docs/collector/transforming-telemetry/#setting-a-span-status)
*   [Advanced Transformations](https://opentelemetry.io/docs/collector/transforming-telemetry/#advanced-transformations)

1.   [Docs](https://opentelemetry.io/docs/)
2.   [Collector](https://opentelemetry.io/docs/collector/)
3.   Transforming telemetry

Transforming telemetry
======================

The OpenTelemetry Collector is a convenient place to transform data before sending it to a vendor or other systems. This is frequently done for data quality, governance, cost, and security reasons.

Processors available from the [Collector Contrib repository](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor) support dozens of different transformations on metric, span and log data. The following sections provide some basic examples on getting started with a few frequently-used processors.

The configuration of processors, particularly advanced transformations, may have a significant impact on collector performance.

Basic filtering[](https://opentelemetry.io/docs/collector/transforming-telemetry/#basic-filtering)
--------------------------------------------------------------------------------------------------

**Processor**: [filter processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/filterprocessor)

The filter processor allows users to filter telemetry using [OTTL](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/pkg/ottl/README.md). Telemetry that matches any condition is dropped.

For example, to _only_ allow span data from services app1, app2, and app3 and drop data from all other services:

```yaml
processors:
  filter/ottl:
    error_mode: ignore
    traces:
      span:
        - |
        resource.attributes["service.name"] != "app1" and
        resource.attributes["service.name"] != "app2" and
        resource.attributes["service.name"] != "app3"
```

To only drop spans from a service called `service1` while keeping all other spans:

```yaml
processors:
  filter/ottl:
    error_mode: ignore
    traces:
      span:
        - resource.attributes["service.name"] == "service1"
```

The [filter processor docs](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/filterprocessor) have more examples, including filtering on logs and metrics.

Adding or Deleting Attributes[](https://opentelemetry.io/docs/collector/transforming-telemetry/#adding-or-deleting-attributes)
------------------------------------------------------------------------------------------------------------------------------

**Processor**: [attributes processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/attributesprocessor) or [resource processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/resourceprocessor)

The attributes processor can be used to update, insert, delete, or replace existing attributes on metrics or traces. For example, here’s a configuration that adds an attribute called account_id to all spans:

```yaml
processors:
  attributes/accountid:
    actions:
      - key: account_id
        value: 2245
        action: insert
```

The resource processor has an identical configuration, but applies only to [resource attributes](https://opentelemetry.io/docs/specs/semconv/resource/). Use the resource processor to modify infrastructure metadata related to telemetry. For example, this inserts the Kubernetes cluster name:

```yaml
processors:
  resource/k8s:
    attributes:
      - key: k8s.cluster.name
        from_attribute: k8s-cluster
        action: insert
```

Renaming Metrics or Metric Labels[](https://opentelemetry.io/docs/collector/transforming-telemetry/#renaming-metrics-or-metric-labels)
--------------------------------------------------------------------------------------------------------------------------------------

**Processor:**[metrics transform processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/metricstransformprocessor)

The [metrics transform processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/metricstransformprocessor) shares some functionality with the [attributes processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/attributesprocessor), but also supports renaming and other metric-specific functionality.

```yaml
processors:
  metricstransform/rename:
    transforms:
      - include: system.cpu.usage
        action: update
        new_name: system.cpu.usage_time
```

The [metrics transform processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/metricstransformprocessor) also supports regular expressions to apply transform rules to multiple metric names or metric labels at the same time. This example renames cluster_name to cluster-name for all metrics:

```yaml
processors:
  metricstransform/clustername:
    transforms:
      - include: ^.*$
        match_type: regexp
        action: update
        operations:
          - action: update_label
            label: cluster_name
            new_label: cluster-name
```

Enriching Telemetry with Resource Attributes[](https://opentelemetry.io/docs/collector/transforming-telemetry/#enriching-telemetry-with-resource-attributes)
------------------------------------------------------------------------------------------------------------------------------------------------------------

**Processor**: [resource detection processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/resourcedetectionprocessor) and [k8sattributes processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/k8sattributesprocessor)

These processors can be used for enriching telemetry with relevant infrastructure metadata to help teams quickly identify when underlying infrastructure is impacting service health or performance.

The resource detection processor adds relevant cloud or host-level information to telemetry:

```yaml
processors:
  resourcedetection/system:
    # Modify the list of detectors to match the cloud environment
    detectors: [env, system, gcp, ec2, azure]
    timeout: 2s
    override: false
```

Similarly, the K8s processor enriches telemetry with relevant Kubernetes metadata like pod name, node name, or workload name. The collector pod must be configured to have [read access to certain Kubernetes RBAC APIs](https://pkg.go.dev/github.com/open-telemetry/opentelemetry-collector-contrib/processor/k8sattributesprocessor#readme-role-based-access-control). To use the default options, it can be configured with an empty block:

```yaml
processors:
  k8sattributes/default:
```

Setting a span status[](https://opentelemetry.io/docs/collector/transforming-telemetry/#setting-a-span-status)
--------------------------------------------------------------------------------------------------------------

**Processor**: [transform processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/transformprocessor)

Use the transform processor to set a span’s status. The following example sets the span status to `Ok` when the `http.request.status_code` attribute is 400:

```yaml
transform:
  error_mode: ignore
  trace_statements:
    - set(span.status.code, STATUS_CODE_OK) where span.attributes["http.request.status_code"] == 400
```

You can also use the transform processor to modify the span name based on its attributes or extract span attributes from the span name. For examples, see an example [config file](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/9b28f76c02c18f7479d10e4b6a95a21467fd85d6/processor/transformprocessor/testdata/config.yaml) file for the transform processor.

Advanced Transformations[](https://opentelemetry.io/docs/collector/transforming-telemetry/#advanced-transformations)
--------------------------------------------------------------------------------------------------------------------

More advanced attribute transformations are also available in the [transform processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/transformprocessor). The transform processor allows end-users to specify transformations on metrics, logs, and traces using the [OpenTelemetry Transformation Language](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/pkg/ottl).

Feedback
--------

Was this page helpful?

Yes No
Thank you. Your feedback is appreciated!

Please let us know [how we can improve this page](https://github.com/open-telemetry/opentelemetry.io/issues/new?template=PAGE_FEEDBACK.yml&title=[Page+feedback]%3A+ADD+A+SUMMARY+OF+YOUR+FEEDBACK+HERE). Your feedback is appreciated!

Last modified May 22, 2025: [[chore] Accessible links 1 (#6049) (801233d0)](https://github.com/open-telemetry/opentelemetry.io/commit/801233d066e99c97408663e5dbc6971fa38e94d3)

*   [](https://github.com/open-telemetry/community#mailing-lists)
*   [](https://bsky.app/profile/opentelemetry.io)
*   [](https://fosstodon.org/@opentelemetry)
*   [](https://stackoverflow.com/questions/tagged/open-telemetry)
*   [](https://github.com/cncf/artwork/tree/master/projects/opentelemetry)
*   [](https://docs.google.com/spreadsheets/d/1SYKfjYhZdm2Wh2Cl6KVQalKg_m4NhTPZqq-8SzEVO6s)
*   [](https://lookerstudio.google.com/s/tSTKxK1ECeU)

*   [](https://github.com/open-telemetry)
*   [](https://cloud-native.slack.com/archives/CJFCJHG4Q)
*   [](https://opentelemetry.devstats.cncf.io/d/8/dashboards?orgId=1&refresh=15m)
*   [](https://www.linuxfoundation.org/legal/privacy-policy)
*   [](https://www.linuxfoundation.org/legal/trademark-usage)
*   [](https://opentelemetry.io/community/marketing-guidelines/)
*   [](https://opentelemetry.io/site/)

© 2019–present OpenTelemetry Authors | Docs [CC BY 4.0](https://creativecommons.org/licenses/by/4.0)All Rights Reserved
