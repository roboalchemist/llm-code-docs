# Source: https://kubescape.io/docs/operator/telemetry/

Title: Telemetry - Kubescape

URL Source: https://kubescape.io/docs/operator/telemetry/

Markdown Content:
Telemetry - Kubescape
===============
- [x] - [x] 

[Skip to content](https://kubescape.io/docs/operator/telemetry/#setting-up-telemetry)

[![Image 1: logo](https://kubescape.io/assets/kubescape-lockup.svg)](https://kubescape.io/ "Kubescape")

 Kubescape 

 Telemetry 

Type to start searching

[GitHub * v4.0.2 * 11.2k * 900](https://github.com/kubescape/kubescape "Go to repository")

*   [Home](https://kubescape.io/)
*   [Docs](https://kubescape.io/docs/)
*   [Project](https://kubescape.io/project/about/)
*   [Blog](https://kubescape.io/blog/)
*   [GitHub](https://github.com/kubescape/kubescape)

[![Image 2: logo](https://kubescape.io/assets/kubescape-lockup.svg)](https://kubescape.io/ "Kubescape") Kubescape  

[GitHub * v4.0.2 * 11.2k * 900](https://github.com/kubescape/kubescape "Go to repository")

*   [Home](https://kubescape.io/)
*   - [x]  Docs   Docs  
    *   [Documentation overview](https://kubescape.io/docs/)
    *   [Getting Started](https://kubescape.io/docs/getting-started/)
    *   [Installing the client](https://kubescape.io/docs/install-cli/)
    *   [Installing in your cluster](https://kubescape.io/docs/install-operator/)
    *   [Scanning your environment](https://kubescape.io/docs/scanning/)
    *   [Accepting risk](https://kubescape.io/docs/accepting-risk/)
    *   [Connecting to providers](https://kubescape.io/docs/providers/)
    *   [MCP Server](https://kubescape.io/docs/mcp-server/)
    *   - [x]  Kubescape Operator   Kubescape Operator  
        *   [Overview](https://kubescape.io/docs/operator/)
        *   [Vulnerability scanning](https://kubescape.io/docs/operator/vulnerabilities/)
        *   [Relevancy](https://kubescape.io/docs/operator/relevancy/)
        *   [Runtime Threat Detection](https://kubescape.io/docs/operator/runtime-threat-detection/)
        *   [Generate Network Policies](https://kubescape.io/docs/operator/network-policy-generation/)
        *   [Scheduled scans](https://kubescape.io/docs/operator/scheduled-scans/)
        *   [Continuous scanning](https://kubescape.io/docs/operator/continuous-scanning/)
        *   [Prometheus Integrations](https://kubescape.io/docs/operator/prometheus-integration/)
        *   [UI with Headlamp](https://kubescape.io/docs/operator/ui-with-headlamp/)
        *   [Automatic upgrades](https://kubescape.io/docs/operator/automatic-release-upgrades/)
        *   [VEX document generation (experimental)](https://kubescape.io/docs/operator/generating-vex/)
        *   - [x]  Telemetry  [Telemetry](https://kubescape.io/docs/operator/telemetry/) Table of contents  
            *   [Host metrics collection](https://kubescape.io/docs/operator/telemetry/#host-metrics-collection)
                *   [Example: exporting to uptrace running inside docker-compose](https://kubescape.io/docs/operator/telemetry/#example-exporting-to-uptrace-running-inside-docker-compose)

        *   [Node Agents per Node Pool](https://kubescape.io/docs/operator/multiple-node-agent-per-node-pool/)

    *   - [x]  Integrations   Integrations  
        *   [Overview](https://kubescape.io/docs/integrations/)
        *   [GitHub](https://kubescape.io/docs/integrations/github/)
        *   [Lens](https://kubescape.io/docs/integrations/lens/)
        *   [VS Code](https://kubescape.io/docs/integrations/vscode/)

    *   - [x]  Frameworks and Controls   Frameworks and Controls  
        *   [Overview](https://kubescape.io/docs/frameworks-and-controls/)
        *   [Frameworks](https://kubescape.io/docs/frameworks-and-controls/frameworks/)
        *   [Control library](https://kubescape.io/docs/controls/)
        *   [Configuring controls](https://kubescape.io/docs/frameworks-and-controls/configuring-controls/)

    *   - [x]  Guides   Guides  
        *   [Configure checks on a GitHub repository](https://kubescape.io/docs/guides/kubescape-gha/)
        *   [Harden a cluster](https://kubescape.io/docs/guides/kubescape-cli/)
        *   [Deploying on OpenShift](https://kubescape.io/docs/guides/deploying-on-openshift/)
        *   [Kubescape for teenagers](https://kubescape.io/docs/guides/kubescape-for-teenagers/kubescape-for-teenagers/)

*   - [x]  Project   Project  
    *   [About the Kubescape project](https://kubescape.io/project/about/)
    *   [License](https://kubescape.io/project/license/)
    *   [Releases](https://github.com/kubescape/helm-charts/releases)
    *   [Community](https://kubescape.io/project/community/)
    *   [Contributing](https://github.com/kubescape/kubescape/blob/master/CONTRIBUTING.md)

*   - [x]  Blog   Blog  
    *   [Kubescape Blog](https://kubescape.io/blog/)
    *   - [x]  Archive   Archive  
        *   [May 2025](https://kubescape.io/blog/archive/2025/05/)
        *   [April 2025](https://kubescape.io/blog/archive/2025/04/)
        *   [March 2025](https://kubescape.io/blog/archive/2025/03/)
        *   [February 2025](https://kubescape.io/blog/archive/2025/02/)
        *   [August 2024](https://kubescape.io/blog/archive/2024/08/)
        *   [July 2024](https://kubescape.io/blog/archive/2024/07/)
        *   [December 2023](https://kubescape.io/blog/archive/2023/12/)
        *   [November 2023](https://kubescape.io/blog/archive/2023/11/)
        *   [October 2023](https://kubescape.io/blog/archive/2023/10/)
        *   [September 2023](https://kubescape.io/blog/archive/2023/09/)

    *   - [x]  Categories   Categories  
        *   [Announcements](https://kubescape.io/blog/category/announcements/)
        *   [Project](https://kubescape.io/blog/category/project/)
        *   [Study](https://kubescape.io/blog/category/study/)

*   [GitHub](https://github.com/kubescape/kubescape)

 Table of contents  
*   [Host metrics collection](https://kubescape.io/docs/operator/telemetry/#host-metrics-collection)
    *   [Example: exporting to uptrace running inside docker-compose](https://kubescape.io/docs/operator/telemetry/#example-exporting-to-uptrace-running-inside-docker-compose)

Setting up Telemetry
====================

Several of Kubescape's in-cluster components implement telemetry data using [OpenTelemetry](https://opentelemetry.io/) (otel).\ You can optionally install an Otel [collector](https://opentelemetry.io/docs/collector/) to your cluster to aggregate all metrics and send them to your own tracing tool.

You simply have to fill in this information before [installing kubescape operator](https://kubescape.io/install-operator.md):\ you need to edit the property below at [values.yaml](https://github.com/kubescape/helm-charts/blob/main/charts/kubescape-operator/values.yaml) OR using --set while installing the helm chart\

```
configurations:
  otelUrl: # Default is empty. Add your Open Telemetry URL here.

..
..
..

otelCollector:
  name: otel-collector
  endpoint: 
    insecure: true # configurable
    headers:
      uptrace-dsn: "" # configurable
```

If you don't have an otel distribution, we suggest you try either [Uptrace](https://github.com/uptrace/uptrace/tree/master/example/docker) or [SigNoz](https://signoz.io/docs/install/docker/) as they are free, opensource and can be quickly deployed using docker-compose.

Host metrics collection
-----------------------

The OpenTelemetry collector is configured with the [`hostmetrics`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/hostmetricsreceiver/README.md) receiver to collect CPU and memory utilization metrics.

Note that the hostmetrics receiver is disabled by default. If you wish to enable it, simply install the operator with `--set otelCollector.hostmetrics.enabled=true`

#### Example: exporting to uptrace running inside docker-compose

1.   Download the example using Git:

```
git clone https://github.com/uptrace/uptrace.git
cd uptrace/example/docker
```

1.   Start the services using Docker:

```
docker-compose pull
docker-compose up -d
```

1.   Make sure Uptrace is running:

```
docker-compose logs uptrace
```

1.   Follow the [instructions above](https://kubescape.io/docs/operator/telemetry/#installing-kubescape-operator-in-a-kubernetes-cluster-using-helm), add the OTEL collector configuration and install the operator as follows:

```
--set configurations.otelUrl=<collector host>:14317 --set otelCollector.endpoint.insecure=false
```

1.   Open Uptrace UI at [http://localhost:14318/overview/2](http://localhost:14318/overview/2)

[Previous VEX document generation (experimental)](https://kubescape.io/docs/operator/generating-vex/)[Next Node Agents per Node Pool](https://kubescape.io/docs/operator/multiple-node-agent-per-node-pool/)

 Copyright &copy; 2021 - 2026 [The Kubescape Authors](https://kubescape.devstats.cncf.io/d/66/developer-activity-counts-by-companies?orgId=1)

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) and hosted by [Netlify](https://netlify.com/)

[](https://twitter.com/@kubescape "twitter.com")[](https://github.com/kubescape/kubescape "github.com")

[Do not sell or share my personal information](https://kubescape.io/docs/operator/telemetry/#)
