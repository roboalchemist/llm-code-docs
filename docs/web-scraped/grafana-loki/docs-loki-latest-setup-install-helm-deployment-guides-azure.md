# Source: https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/

Title: Deploy the Loki Helm chart on Azure | Grafana Loki documentation

URL Source: https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/

Markdown Content:
Deploy the Loki Helm chart on Azure | Grafana Loki documentation
===============

![Image 1: GrafanaCON 2026](https://grafana.com/media/events/grafanacon/2026/banners/logo-gcon2026-horiz-banner-centered.svg)![Image 2: GrafanaCON 2026](https://grafana.com/media/events/grafanacon/2026/banners/logo-gcon2026-horiz-banner-left.svg)

Save the Date!

Sign up to get the latest GrafanaCON 2026 updates, agenda drops, and first access to early-bird tickets when they’re first available.

[Sign up](https://grafana.com/events/grafanacon/)

![Image 3: GrafanaCON 2026](https://grafana.com/media/events/grafanacon/2026/banners/logo-gcon2026-horiz-banner-centered.svg)![Image 4: GrafanaCON 2026](https://grafana.com/media/events/grafanacon/2026/banners/logo-gcon2026-horiz-banner-left.svg)

We have our sights

on Barcelona

[Save the Date](https://grafana.com/events/grafanacon/)

![Image 5: ObservabilityCON 2025](https://a-us.storyblok.com/f/1022730/280x40/b0872b99f9/grafana-logo-observabilitycon-2025-black.svg/m/)

 Watch the keynote again and signup for more on-demand sessions. 

[Watch keynote](https://grafana.com/events/observabilitycon/?plcmt=obscon2025-post-event-banner)![Image 6](https://grafana.com/media/events/grafanacon/2025/icon-close-x.svg)

![Image 7: ObservabilityCON 2025](https://grafana.com/media/events/obscon/2025/grafana-obscon2025-promo-logo-black.svg)

📢 Registration + agenda now live  Explore the latest Grafana Cloud and AI solutions, learn tips & tricks from demos and hands-on workshops, and get actionable advice to advance your observability strategy. Register now and get 50% off - limited tickets available (while they last!).

[Register now](https://grafana.com/events/observabilitycon/?tech=target&plcmt=top-banner&aud=default)

Path:

![Image 8: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)

Copied!

[](https://grafana.com/)

*   [Products](https://grafana.com/products/cloud/)[Open Source](https://grafana.com/oss/)[Solutions](https://grafana.com/integrations/)[Learn](https://grafana.com/blog/)[Docs](https://grafana.com/docs/)[Pricing](https://grafana.com/pricing/)

*    [Downloads](https://grafana.com/get/)[Contact us](https://grafana.com/contact/)[Sign in](https://grafana.com/auth/sign-in/)

[Create free account](https://grafana.com/auth/sign-up/create-user?plcmt=mobile-nav&cta=create-free-account)[Contact us](https://grafana.com/contact/?plcmt=mobile-nav&cta=myaccount)

Products

All

Products

Grafana Cloud

Monitor, analyze, and act faster with AI-powered observability.

![Image 9: Grafana Cloud](https://grafana.com/media/menus/products/grafana-menu-icon-grafana-cloud.svg)

[Grafana Cloud overview](https://grafana.com/products/cloud)

LGTM+ Stack

[![Image 10: Grafana Cloud Logs](https://grafana.com/media/menus/products/grafana-menu-icon-logs.svg) Logs powered by Grafana Loki](https://grafana.com/products/cloud/logs/?plcmt=products-nav)

[![Image 11: Grafana](https://grafana.com/media/menus/products/grafana-menu-icon.svg) Grafana for visualization](https://grafana.com/grafana/?plcmt=products-nav)

[![Image 12: Grafana Cloud Traces](https://grafana.com/media/menus/products/grafana-menu-icon-traces.svg) Traces powered by Grafana Tempo](https://grafana.com/products/cloud/traces/?plcmt=products-nav)

[![Image 13: Grafana Cloud Metrics](https://grafana.com/media/menus/products/grafana-menu-icon-metrics.svg) Metrics powered by Grafana Mimir and Prometheus](https://grafana.com/products/cloud/metrics/?plcmt=products-nav)

Key Capabilities

[![Image 14: AI/ML](https://grafana.com/media/menus/products/grafana-menu-icon-ai-ml.svg) AI/ML insights Identify anomalies and reduce toil](https://grafana.com/products/cloud/ai-tools-for-observability/?plcmt=products-nav)

[![Image 15: Grafana Cloud Asserts](https://grafana.com/media/menus/products/grafana-menu-icon-asserts-v1.svg) Contextual root cause analysis Automated anomaly correlation](https://grafana.com/products/cloud/asserts/?plcmt=products-nav)

[![Image 16: Grafana SLO](https://grafana.com/media/menus/products/grafana-menu-icon-slo.svg) SLO management Create SLOs and error budget alerts](https://grafana.com/products/cloud/slo/?plcmt=products-nav)

[![Image 17: Grafana Alerting](https://grafana.com/media/menus/products/grafana-menu-icon-alerting.svg) Alerting Trigger alerts from any data source](https://grafana.com/products/cloud/alerting/?plcmt=products-nav)

[![Image 18: Plugins](https://grafana.com/media/menus/products/grafana-menu-icon-plugins.svg) Plugins Connect Grafana to data sources, apps, and more](https://grafana.com/grafana/plugins/?plcmt=products-nav)

Observability Solutions

[![Image 19: Application Observability](https://grafana.com/media/menus/products/grafana-menu-icon-app-o11y.svg) Application Observability Monitor application performance](https://grafana.com/products/cloud/application-observability/?plcmt=products-nav)

[![Image 20: Infrastructure Observability](https://grafana.com/media/menus/products/grafana-menu-icon-infra-o11y.svg) Infrastructure observability Ensure infrastructure health and performance](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/?plcmt=products-nav)

Testing

[![Image 21: Grafana Cloud k6](https://grafana.com/media/menus/products/grafana-menu-icon-k6.svg) Performance testing Powered by Grafana k6](https://grafana.com/products/cloud/k6/?plcmt=products-nav)

[![Image 22: Synthetic Monitoring](https://grafana.com/media/menus/products/grafana-menu-icon-synthetic-monitoring.svg) Synthetic Monitoring powered by Grafana k6](https://grafana.com/products/cloud/synthetic-monitoring/?plcmt=products-nav)

IRM

[![Image 23: Incident](https://grafana.com/media/menus/products/grafana-menu-icon-incident.svg) Incident response Routine task automation for incidents](https://grafana.com/products/cloud/incident/?plcmt=products-nav)

[![Image 24: OnCall](https://grafana.com/media/menus/products/grafana-menu-icon-oncall.svg) On-call management Flexible on-call management](https://grafana.com/products/cloud/oncall/?plcmt=products-nav)

Open Source

All

Open Source

[Grafana Loki Multi-tenant log aggregation system](https://grafana.com/oss/loki/?plcmt=oss-nav)

[Grafana Query, visualize, and alert on data](https://grafana.com/oss/grafana/?plcmt=oss-nav)

[Grafana Tempo High-scale distributed tracing backend](https://grafana.com/oss/tempo/?plcmt=oss-nav)

[Grafana Mimir Scalable and performant metrics backend](https://grafana.com/oss/mimir/?plcmt=oss-nav)

[Grafana Pyroscope Scalable continuous profiling backend](https://grafana.com/oss/pyroscope/?plcmt=oss-nav)

[Grafana Beyla eBPF auto-instrumentation](https://grafana.com/oss/beyla-ebpf/?plcmt=oss-nav)

[Grafana Faro Frontend application observability web SDK](https://grafana.com/oss/faro/?plcmt=oss-nav)

[Grafana Alloy OpenTelemetry Collector distribution with Prometheus pipelines](https://grafana.com/oss/alloy-opentelemetry-collector/?plcmt=oss-nav)

[Grafana k6 Load testing for engineering teams](https://grafana.com/oss/k6/?plcmt=oss-nav)

[Prometheus Monitor Kubernetes and cloud native](https://grafana.com/oss/prometheus/?plcmt=oss-nav)

[OpenTelemetry Instrument and collect telemetry data](https://grafana.com/oss/opentelemetry/?plcmt=oss-nav)

[Graphite Scalable monitoring for time series data](https://grafana.com/oss/graphite/?plcmt=oss-nav)

[All](https://grafana.com/oss/?plcmt=oss-nav)

Community resources

[Dashboard templates Try out and share prebuilt visualizations](https://grafana.com/grafana/dashboards/?plcmt=oss-nav)[Prometheus exporters Get your metrics into Prometheus quickly](https://grafana.com/oss/prometheus/exporters/?plcmt=oss-nav)

Solutions

All

end-to-end integrations

Opinionated integrations that help you get there easier and faster

[Kubernetes Monitoring Get K8s health, performance, and cost monitoring from cluster to container](https://grafana.com/solutions/kubernetes/?plcmt=solutions-nav)

[Application Observability Monitor application performance](https://grafana.com/products/cloud/application-observability/?plcmt=solutions-nav)

[Frontend Observability Gain real user monitoring insights](https://grafana.com/products/cloud/frontend-observability-for-real-user-monitoring/?plcmt=solutions-nav)

[Incident Response & Management Detect and respond to incidents with a simplified workflow](https://grafana.com/products/cloud/irm/?plcmt=solutions-nav)

[All monitoring and visualization integrations](https://grafana.com/integrations/?plcmt=nav-solutions-cta1)

monitor infrastructure

Out-of-the-box KPIs, dashboards, and alerts for observability

![Image 25: linux server logo](https://grafana.com/static/img/logos/logo-linux.svg)

[Linux](https://grafana.com/integrations/linux-node/monitor/?plcmt=solutions-nav)

![Image 26: windows logo](https://grafana.com/media/solutions/windows-monitor/windows-icon.png)

[Windows](https://grafana.com/integrations/windows/monitor/?plcmt=solutions-nav)

![Image 27: docker logo](https://grafana.com/static/img/logos/icon-docker.svg)

[Docker](https://grafana.com/integrations/docker/monitor/?plcmt=solutions-nav)

![Image 28: postgresql logo](https://grafana.com/static/img/logos/postgresql_elephant_icon.svg)

[Postgres](https://grafana.com/integrations/postgresql/monitor/?plcmt=solutions-nav)

![Image 29: mysql logo](https://grafana.com/static/img/logos/mysql_logo_menu.svg)

[MySQL](https://grafana.com/integrations/mysql/monitor/?plcmt=solutions-nav)

![Image 30: aws logo](https://grafana.com/media/images/logos/aws-logo-light.svg)

[AWS](https://grafana.com/integrations/cloud-monitoring-aws/?plcmt=solutions-nav)

![Image 31: kafka logo](https://grafana.com/static/img/logos/kafka.svg)

[Kafka](https://grafana.com/integrations/kafka/monitor/?plcmt=solutions-nav)

![Image 32: jenkins logo](https://grafana.com/static/img/logos/jenkins-logo.svg)

[Jenkins](https://grafana.com/integrations/jenkins/monitor/?plcmt=solutions-nav)

![Image 33: rabbitmq logo](https://grafana.com/media/solutions/rabbitmq-monitor/rabbitmq-icon.png)

[RabbitMQ](https://grafana.com/integrations/rabbitmq/monitor/?plcmt=solutions-nav)

![Image 34: mongodb logo](https://grafana.com/media/images/logos/logo-mongodb.svg)

[MongoDB](https://grafana.com/integrations/mongodb/monitor/?plcmt=solutions-nav)

![Image 35: microsoft azure observability logo](https://grafana.com/media/solutions/azure-metrics-monitor/microsoft-azure-icon.svg)

[Microsoft Azure](https://grafana.com/integrations/cloud-monitoring-microsoft-azure/?plcmt=solutions-nav)

![Image 36: google cloud observability with grafana cloud logo](https://grafana.com/media/images/logos/google-cloud-logo-60x48.svg)

[Google Cloud](https://grafana.com/integrations/cloud-monitoring-google-cloud/?plcmt=solutions-nav)

[All monitoring integrations](https://grafana.com/integrations/monitoring/?plcmt=nav-solutions-cta2)

visualize any data

Instantly connect all your data sources to Grafana

![Image 37: mongodb logo](https://grafana.com/media/images/logos/logo-mongodb.svg)

[MongoDB](https://grafana.com/integrations/mongodb/visualize/?plcmt=solutions-nav)

![Image 38: appdynamics logo](https://grafana.com/static/img/logos/appDynamics-white.svg)

[AppDynamics](https://grafana.com/integrations/appdynamics/visualize/?plcmt=solutions-nav)

![Image 39: oracle database logo](https://grafana.com/static/img/logos/oracle-logo.png)

[Oracle](https://grafana.com/integrations/oracle-database/visualize/?plcmt=solutions-nav)

![Image 40: gitlab logo](https://grafana.com/static/img/logos/gitlab.svg)

[GitLab](https://grafana.com/integrations/gitlab/visualize/?plcmt=solutions-nav)

![Image 41: jira logo](https://grafana.com/static/img/diagram/jira-small.svg)

[Jira](https://grafana.com/integrations/jira/visualize/?plcmt=solutions-nav)

![Image 42: salesforce logo](https://grafana.com/static/img/logos/salesforce.com_logo.svg)

[Salesforce](https://grafana.com/integrations/salesforce/visualize/?plcmt=solutions-nav)

![Image 43: splunk logo](https://grafana.com/static/img/logos/splunk-menu.svg)

[Splunk](https://grafana.com/integrations/splunk/visualize/?plcmt=solutions-nav)

![Image 44: datadog logo](https://grafana.com/static/img/logos/icon-datadog.svg)

[Datadog](https://grafana.com/integrations/datadog/visualize/?plcmt=solutions-nav)

![Image 45: new relic logo](https://grafana.com/static/img/logos/newrelic.svg)

[New Relic](https://grafana.com/integrations/new-relic/visualize/?plcmt=solutions-nav)

![Image 46: snowflake logo](https://grafana.com/static/img/logos/snowflake-logo-lg.png)

[Snowflake](https://grafana.com/integrations/snowflake/visualize/?plcmt=solutions-nav)

[All visualization integrations](https://grafana.com/integrations/visualization/?plcmt=nav-solutions-cta3)

Learn

All

Learn

Community and events

[Events Upcoming in-person and virtual events](https://grafana.com/events/?plcmt=learn-nav)

[ObservabilityCON 2025 Our flagship observability event](https://grafana.com/events/observabilitycon/?plcmt=learn-nav)

[GrafanaCON 2026 Our annual OSS community conference](https://grafana.com/events/grafanacon/?plcmt=learn-nav)

[ObservabilityCON on the Road Our observability conference on the road](https://grafana.com/events/observabilitycon-on-the-road/?plcmt=learn-nav)

[Community Join the Grafana community](https://grafana.com/community/?plcmt=learn-nav)

[Community forums Ask the community for help](https://community.grafana.com/?plcmt=learn-nav)

Resources

[Blog News, releases, cool stories, and more](https://grafana.com/blog/?plcmt=learn-nav)

[4th annual Observability Survey Share your thoughts on the state of observability](https://grafana.com/observability-survey/?plcmt=learn-nav)

[Benefits of Observability New research, reports, and insights](https://grafana.com/observability-benefits-for-business/?plcmt=learn-nav)

[Success stories By use case, product, and industry](https://grafana.com/success/?plcmt=learn-nav)

How-to

[Documentation All the docs](https://grafana.com/docs/?plcmt=learn-nav)

[Webinars and videos Demos, webinars, and feature tours](https://grafana.com/videos/?plcmt=learn-nav)

[Tutorials Step-by-step guides](https://grafana.com/tutorials/?plcmt=learn-nav)

[Workshops Free, in-person or online](https://grafana.com/workshops/?plcmt=learn-nav)

[Learning Paths Expert guidance for mastering our platform](https://grafana.com/docs/learning-paths/?plcmt=learn-nav)

[Professional Services Expert guidance and training](https://grafana.com/professional-services/?plcmt=learn-nav)

[Docs](https://grafana.com/docs/)

[Pricing](https://grafana.com/pricing/?plcmt=mobile-nav)

Help build the future of open source observability software [Open positions](https://grafana.com/about/careers/?plcmt=mobile-nav&cta=career)

Check out the open source projects we support [Downloads](https://grafana.com/get/?plcmt=mobile-nav&cta=downloads)

[Sign in](https://grafana.com/auth/sign-in?plcmt=mobile-nav&cta=myaccount)

Grafana Cloud

Monitor, analyze, and act faster with AI-powered observability.

![Image 47: Grafana Cloud](https://grafana.com/media/menus/products/grafana-menu-icon-grafana-cloud.svg)

[Grafana Cloud overview](https://grafana.com/products/cloud/?plcmt=products-nav)

LGTM+ Stack

[![Image 48: Grafana Cloud Logs](https://grafana.com/media/menus/products/grafana-menu-icon-logs.svg) Logs](https://grafana.com/products/cloud/logs/?plcmt=products-nav "powered by Grafana Loki")[![Image 49: Grafana](https://grafana.com/media/menus/products/grafana-menu-icon.svg) Grafana](https://grafana.com/grafana/?plcmt=products-nav "for visualization")[![Image 50: Grafana Cloud Traces](https://grafana.com/media/menus/products/grafana-menu-icon-traces.svg) Traces](https://grafana.com/products/cloud/traces/?plcmt=products-nav "powered by Grafana Tempo")[![Image 51: Grafana Cloud Metrics](https://grafana.com/media/menus/products/grafana-menu-icon-metrics.svg) Metrics](https://grafana.com/products/cloud/metrics/?plcmt=products-nav "powered by Grafana Mimir and Prometheus")

Key Capabilities

[![Image 52: AI/ML](https://grafana.com/media/menus/products/grafana-menu-icon-ai-ml.svg) AI/ML insights](https://grafana.com/products/cloud/ai-tools-for-observability/?plcmt=products-nav "Identify anomalies and reduce toil")[![Image 53: Grafana Cloud Asserts](https://grafana.com/media/menus/products/grafana-menu-icon-asserts-v1.svg) Contextual root cause analysis](https://grafana.com/products/cloud/asserts/?plcmt=products-nav "Automated anomaly correlation")[![Image 54: Grafana SLO](https://grafana.com/media/menus/products/grafana-menu-icon-slo.svg) SLO management](https://grafana.com/products/cloud/slo/?plcmt=products-nav "Create SLOs and error budget alerts")[![Image 55: Grafana Alerting](https://grafana.com/media/menus/products/grafana-menu-icon-alerting.svg) Alerting](https://grafana.com/products/cloud/alerting/?plcmt=products-nav "Trigger alerts from any data source")[![Image 56: Plugins](https://grafana.com/media/menus/products/grafana-menu-icon-plugins.svg) Plugins](https://grafana.com/grafana/plugins/?plcmt=products-nav "Connect Grafana to data sources, apps, and more")

Observability Solutions

[![Image 57: Application Observability](https://grafana.com/media/menus/products/grafana-menu-icon-app-o11y.svg) Application Observability](https://grafana.com/products/cloud/application-observability/?plcmt=products-nav "Monitor application performance")[![Image 58: Infrastructure Observability](https://grafana.com/media/menus/products/grafana-menu-icon-infra-o11y.svg) Infrastructure observability](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/?plcmt=products-nav "Ensure infrastructure health and performance")

Testing

[![Image 59: Grafana Cloud k6](https://grafana.com/media/menus/products/grafana-menu-icon-k6.svg) Performance testing](https://grafana.com/products/cloud/k6/?plcmt=products-nav "Powered by Grafana k6")[![Image 60: Synthetic Monitoring](https://grafana.com/media/menus/products/grafana-menu-icon-synthetic-monitoring.svg) Synthetic Monitoring](https://grafana.com/products/cloud/synthetic-monitoring/?plcmt=products-nav "powered by Grafana k6")

IRM

[![Image 61: Incident](https://grafana.com/media/menus/products/grafana-menu-icon-incident.svg) Incident response](https://grafana.com/products/cloud/incident/?plcmt=products-nav "Routine task automation for incidents")[![Image 62: OnCall](https://grafana.com/media/menus/products/grafana-menu-icon-oncall.svg) On-call management](https://grafana.com/products/cloud/oncall/?plcmt=products-nav "Flexible on-call management")

The actually useful free plan

Grafana Cloud Free Tier

![Image 63: check](https://grafana.com/media/images/icons/grafana-icon-bullet-light-green.svg)
10k series Prometheus metrics

![Image 64: check](https://grafana.com/media/images/icons/grafana-icon-bullet-light-green.svg)
50GB logs, 50GB traces, 50GB profiles

![Image 65: check](https://grafana.com/media/images/icons/grafana-icon-bullet-light-green.svg)
500VUh k6 testing

![Image 66: check](https://grafana.com/media/images/icons/grafana-icon-bullet-light-green.svg)
20+ Enterprise data source plugins

![Image 67: check](https://grafana.com/media/images/icons/grafana-icon-bullet-light-green.svg)
100+ pre-built solutions

![Image 68: check](https://grafana.com/media/images/icons/grafana-icon-bullet-light-green.svg)
3 active AI users

[Create account](https://grafana.com/auth/sign-up/create-user/?plcmt=products-nav)

[![Image 69: Grafana Cloud Logs](https://grafana.com/media/menus/products/grafana-menu-icon-logs.svg) Grafana Loki Multi-tenant log aggregation system](https://grafana.com/oss/loki/?plcmt=oss-nav)[![Image 70: Grafana](https://grafana.com/media/menus/products/grafana-menu-icon.svg) Grafana Query, visualize, and alert on data](https://grafana.com/oss/grafana/?plcmt=oss-nav)[![Image 71: Grafana Cloud Traces](https://grafana.com/media/menus/products/grafana-menu-icon-traces.svg) Grafana Tempo High-scale distributed tracing backend](https://grafana.com/oss/tempo/?plcmt=oss-nav)[![Image 72: Grafana Cloud Metrics](https://grafana.com/media/menus/products/grafana-menu-icon-metrics.svg) Grafana Mimir Scalable and performant metrics backend](https://grafana.com/oss/mimir/?plcmt=oss-nav)

[![Image 73: Grafana Cloud Profiles](https://grafana.com/media/menus/products/grafana-menu-icon-profiles.svg) Grafana Pyroscope Scalable continuous profiling backend](https://grafana.com/oss/pyroscope/?plcmt=oss-nav)[![Image 74](https://grafana.com/static/img/logos/beyla-logo.svg) Grafana Beyla eBPF auto-instrumentation](https://grafana.com/oss/beyla-ebpf/?plcmt=oss-nav)[![Image 75: Frontend Observability](https://grafana.com/media/menus/products/grafana-menu-icon-faro.svg) Grafana Faro Frontend application observability web SDK](https://grafana.com/oss/faro/?plcmt=oss-nav)[![Image 76: Grafana Alloy](https://grafana.com/media/oss/alloy/alloy-logo.svg) Grafana Alloy OpenTelemetry Collector distribution with Prometheus pipelines](https://grafana.com/oss/alloy-opentelemetry-collector/?plcmt=oss-nav)

[![Image 77: Grafana Cloud k6](https://grafana.com/media/menus/products/grafana-menu-icon-k6.svg) Grafana k6 Load testing for engineering teams](https://grafana.com/oss/k6/?plcmt=oss-nav)[![Image 78: Prometheus](https://grafana.com/static/img/menu/prometheus.svg) Prometheus Monitor Kubernetes and cloud native](https://grafana.com/oss/prometheus/?plcmt=oss-nav)[![Image 79: OpenTelemetry](https://grafana.com/static/img/menu/opentelemetry.svg) OpenTelemetry Instrument and collect telemetry data](https://grafana.com/oss/opentelemetry/?plcmt=oss-nav)[![Image 80: Graphite](https://grafana.com/static/img/menu/graphite.svg) Graphite Scalable monitoring for time series data](https://grafana.com/oss/graphite/?plcmt=oss-nav)[](https://grafana.com/oss/?plcmt=oss-nav)

[](https://grafana.com/oss/?plcmt=oss-nav)[All](https://grafana.com/oss/?plcmt=oss-nav)

Community resources

[Dashboard templates Try out and share prebuilt visualizations](https://grafana.com/grafana/dashboards/?plcmt=oss-nav)[Prometheus exporters Get your metrics into Prometheus quickly](https://grafana.com/oss/prometheus/exporters/?plcmt=oss-nav)

end-to-end integrations

Opinionated integrations that help you get there easier and faster

[![Image 81: Kubernetes Monitoring](https://grafana.com/static/img/logos/logo-kubernetes.svg) Kubernetes Monitoring Get K8s health, performance, and cost monitoring from cluster to container](https://grafana.com/solutions/kubernetes/?plcmt=solutions-nav)[![Image 82: Application Observability](https://grafana.com/media/menus/products/grafana-menu-icon-app-o11y.svg) Application Observability Monitor application performance](https://grafana.com/products/cloud/application-observability/?plcmt=solutions-nav)[![Image 83: Frontend Observability](https://grafana.com/media/menus/products/grafana-menu-icon-faro.svg) Frontend Observability Gain real user monitoring insights](https://grafana.com/products/cloud/frontend-observability-for-real-user-monitoring/?plcmt=solutions-nav)[![Image 84: Incident Response & Management](https://grafana.com/static/img/menu/incident-icon.svg) Incident Response & Management Detect and respond to incidents with a simplified workflow](https://grafana.com/products/cloud/irm/?plcmt=solutions-nav)

monitor infrastructure

Out-of-the-box KPIs, dashboards, and alerts for observability

[![Image 85: linux server logo](https://grafana.com/static/img/logos/logo-linux.svg)Linux](https://grafana.com/integrations/linux-node/monitor/?plcmt=solutions-nav)

[![Image 86: windows logo](https://grafana.com/media/solutions/windows-monitor/windows-icon.png)Windows](https://grafana.com/integrations/windows/monitor/?plcmt=solutions-nav)

[![Image 87: docker logo](https://grafana.com/static/img/logos/icon-docker.svg)Docker](https://grafana.com/integrations/docker/monitor/?plcmt=solutions-nav)

[![Image 88: postgresql logo](https://grafana.com/static/img/logos/postgresql_elephant_icon.svg)Postgres](https://grafana.com/integrations/postgresql/monitor/?plcmt=solutions-nav)

[![Image 89: mysql logo](https://grafana.com/static/img/logos/mysql_logo_menu.svg)MySQL](https://grafana.com/integrations/mysql/monitor/?plcmt=solutions-nav)

[![Image 90: aws logo](https://grafana.com/media/images/logos/aws-logo-light.svg)AWS](https://grafana.com/integrations/cloud-monitoring-aws/?plcmt=solutions-nav)

[![Image 91: kafka logo](https://grafana.com/static/img/logos/kafka.svg)Kafka](https://grafana.com/integrations/kafka/monitor/?plcmt=solutions-nav)

[![Image 92: jenkins logo](https://grafana.com/static/img/logos/jenkins-logo.svg)Jenkins](https://grafana.com/integrations/jenkins/monitor/?plcmt=solutions-nav)

[![Image 93: rabbitmq logo](https://grafana.com/media/solutions/rabbitmq-monitor/rabbitmq-icon.png)RabbitMQ](https://grafana.com/integrations/rabbitmq/monitor/?plcmt=solutions-nav)

[![Image 94: mongodb logo](https://grafana.com/media/images/logos/logo-mongodb.svg)MongoDB](https://grafana.com/integrations/mongodb/monitor/?plcmt=solutions-nav)

[![Image 95: microsoft azure observability logo](https://grafana.com/media/solutions/azure-metrics-monitor/microsoft-azure-icon.svg)Microsoft Azure](https://grafana.com/integrations/cloud-monitoring-microsoft-azure/?plcmt=solutions-nav)

[![Image 96: google cloud observability with grafana cloud logo](https://grafana.com/media/images/logos/google-cloud-logo-60x48.svg)Google Cloud](https://grafana.com/integrations/cloud-monitoring-google-cloud/?plcmt=solutions-nav)

visualize any data

Instantly connect all your data sources to Grafana

[![Image 97: mongodb logo](https://grafana.com/media/images/logos/logo-mongodb.svg)MongoDB](https://grafana.com/integrations/mongodb/visualize/?plcmt=solutions-nav)

[![Image 98: appdynamics logo](https://grafana.com/static/img/logos/appDynamics-white.svg)AppDynamics](https://grafana.com/integrations/appdynamics/visualize/?plcmt=solutions-nav)

[![Image 99: oracle database logo](https://grafana.com/static/img/logos/oracle-logo.png)Oracle](https://grafana.com/integrations/oracle-database/visualize/?plcmt=solutions-nav)

[![Image 100: gitlab logo](https://grafana.com/static/img/logos/gitlab.svg)GitLab](https://grafana.com/integrations/gitlab/visualize/?plcmt=solutions-nav)

[![Image 101: jira logo](https://grafana.com/static/img/diagram/jira-small.svg)Jira](https://grafana.com/integrations/jira/visualize/?plcmt=solutions-nav)

[![Image 102: salesforce logo](https://grafana.com/static/img/logos/salesforce.com_logo.svg)Salesforce](https://grafana.com/integrations/salesforce/visualize/?plcmt=solutions-nav)

[![Image 103: splunk logo](https://grafana.com/static/img/logos/splunk-menu.svg)Splunk](https://grafana.com/integrations/splunk/visualize/?plcmt=solutions-nav)

[![Image 104: datadog logo](https://grafana.com/static/img/logos/icon-datadog.svg)Datadog](https://grafana.com/integrations/datadog/visualize/?plcmt=solutions-nav)

[![Image 105: new relic logo](https://grafana.com/static/img/logos/newrelic.svg)New Relic](https://grafana.com/integrations/new-relic/visualize/?plcmt=solutions-nav)

[![Image 106: snowflake logo](https://grafana.com/static/img/logos/snowflake-logo-lg.png)Snowflake](https://grafana.com/integrations/snowflake/visualize/?plcmt=solutions-nav)

[All monitoring and visualization integrations](https://grafana.com/integrations/?plcmt=nav-solutions-cta1)

Community and events

[Events](https://grafana.com/events/?plcmt=learn-nav "Upcoming in-person and virtual events")

[ObservabilityCON 2025](https://grafana.com/events/observabilitycon/?plcmt=learn-nav "Our flagship observability event")

[GrafanaCON 2026](https://grafana.com/events/grafanacon/?plcmt=learn-nav "Our annual OSS community conference")

[ObservabilityCON on the Road](https://grafana.com/events/observabilitycon-on-the-road/?plcmt=learn-nav "Our observability conference on the road")

[Community](https://grafana.com/community/?plcmt=learn-nav "Join the Grafana community")

[Community forums](https://community.grafana.com/?plcmt=learn-nav "Ask the community for help")

Resources

[Blog](https://grafana.com/blog/?plcmt=learn-nav "News, releases, cool stories, and more")

[4th annual Observability Survey](https://grafana.com/observability-survey/?plcmt=learn-nav "Share your thoughts on the state of observability")

[Benefits of Observability](https://grafana.com/observability-benefits-for-business/?plcmt=learn-nav "New research, reports, and insights")

[Success stories](https://grafana.com/success/?plcmt=learn-nav "By use case, product, and industry")

How-to

[Documentation](https://grafana.com/docs/?plcmt=learn-nav "All the docs")

[Webinars and videos](https://grafana.com/videos/?plcmt=learn-nav "Demos, webinars, and feature tours")

[Tutorials](https://grafana.com/tutorials/?plcmt=learn-nav "Step-by-step guides")

[Workshops](https://grafana.com/workshops/?plcmt=learn-nav "Free, in-person or online")

[Learning Paths](https://grafana.com/docs/learning-paths/?plcmt=learn-nav "Expert guidance for mastering our platform")

[Professional Services](https://grafana.com/professional-services/?plcmt=learn-nav "Expert guidance and training")

Featured webinar

[![Image 107: Getting started with grafana LGTM stack](https://grafana.com/static/assets/featured/getting-started-with-grafana-lgtm-stack-amer_featured.png?w=500)](https://grafana.com/go/webinar/getting-started-with-grafana-lgtm-stack/?plcmt=learn-nav-featured?plcmt=learn-nav)

Getting started with managing your metrics, logs, and traces using Grafana

Learn how to unify, correlate, and visualize data with dashboards using Grafana.

[Learn more →](https://grafana.com/go/webinar/getting-started-with-grafana-lgtm-stack/?plcmt=learn-nav-featured)

 Site search  Ask Grot AI

[Try using ![Image 108: Grot AI](https://grafana.com/static/img/grot-chat.svg)**Grot AI** for this query ->](https://grafana.com/grot/?chat=&from=/search)

All

Docs

[](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/)

[View all results](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/)

No results.

There was an error with your request.

![Image 109: close nav](https://grafana.com/static/assets/img/icons/grafana-icon-mobile-nav-close-white.svg)![Image 110: close nav](https://grafana.com/static/assets/img/icons/grafana-icon-mobile-nav-close-white.svg)![Image 111: open nav](https://grafana.com/static/assets/img/icons/grafana-icon-mobile-nav-open-white.svg)

Deploy the Loki Helm chart on Azure

![Image 112: close table of contents](https://grafana.com/static/assets/img/icons/grafana-icon-mobile-toc-close-white.svg)![Image 113: open table of contents](https://grafana.com/static/assets/img/icons/grafana-icon-mobile-toc-open-white.svg)![Image 114: open table of contents](https://grafana.com/static/assets/img/icons/grafana-icon-mobile-toc-open-white.svg)

![Image 115](https://grafana.com/static/assets/img/icons/grafana-icon-docs-search.svg)

[Technical documentation](https://grafana.com/docs/)[Plugin catalog](https://grafana.com/grafana/plugins/)

Choose a product

Viewing: v3.6.x (latest)[Find another version](https://grafana.com/docs/versions/?project=/docs/loki/)

*   [Grafana Loki](https://grafana.com/docs/loki/latest/)

*   [Release notes](https://grafana.com/docs/loki/latest/release-notes/)

    

    *   [Release cadence](https://grafana.com/docs/loki/latest/release-notes/cadence/)

    

    *   [v3.6](https://grafana.com/docs/loki/latest/release-notes/v3-6/)

    

    *   [v3.5](https://grafana.com/docs/loki/latest/release-notes/v3-5/)

    

    *   [v3.4](https://grafana.com/docs/loki/latest/release-notes/v3-4/)

    

    *   [v3.3](https://grafana.com/docs/loki/latest/release-notes/v3-3/)

    

    *   [v3.2](https://grafana.com/docs/loki/latest/release-notes/v3-2/)

    

    *   [v3.1](https://grafana.com/docs/loki/latest/release-notes/v3-1/)

    

    *   [v3.0](https://grafana.com/docs/loki/latest/release-notes/v3-0/)

    

    *   [V2.9](https://grafana.com/docs/loki/latest/release-notes/v2-9/)

    

    *   [V2.8](https://grafana.com/docs/loki/latest/release-notes/v2-8/)

    

    *   [V2.7](https://grafana.com/docs/loki/latest/release-notes/v2-7/)

    

    *   [V2.6](https://grafana.com/docs/loki/latest/release-notes/v2-6/)

    

    *   [V2.5](https://grafana.com/docs/loki/latest/release-notes/v2-5/)

    

    *   [V2.4](https://grafana.com/docs/loki/latest/release-notes/v2-4/)

    

    *   [V2.3](https://grafana.com/docs/loki/latest/release-notes/v2-3/)

*   [Get started](https://grafana.com/docs/loki/latest/get-started/)

    

    *   [Loki overview](https://grafana.com/docs/loki/latest/get-started/overview/)

    

    *   [Quick Start](https://grafana.com/docs/loki/latest/get-started/quick-start/)

        

        *   [Loki quickstart](https://grafana.com/docs/loki/latest/get-started/quick-start/quick-start/)

        

        *   [Loki Tutorial](https://grafana.com/docs/loki/latest/get-started/quick-start/tutorial/)

    

    *   [Architecture](https://grafana.com/docs/loki/latest/get-started/architecture/)

    

    *   [Components](https://grafana.com/docs/loki/latest/get-started/components/)

    

    *   [Deployment modes](https://grafana.com/docs/loki/latest/get-started/deployment-modes/)

    

    *   [Labels](https://grafana.com/docs/loki/latest/get-started/labels/)

        

        *   [Label best practices](https://grafana.com/docs/loki/latest/get-started/labels/bp-labels/)

        

        *   [Cardinality](https://grafana.com/docs/loki/latest/get-started/labels/cardinality/)

        

        *   [Structured metadata](https://grafana.com/docs/loki/latest/get-started/labels/structured-metadata/)

        

        *   [Modify default labels](https://grafana.com/docs/loki/latest/get-started/labels/modify-default-labels/)

    

    *   [Hash rings](https://grafana.com/docs/loki/latest/get-started/hash-rings/)

*   [Set up](https://grafana.com/docs/loki/latest/setup/)

    

    *   [Size the cluster](https://grafana.com/docs/loki/latest/setup/size/)

    

    *   [Install](https://grafana.com/docs/loki/latest/setup/install/)

        

        *   [Install using Helm](https://grafana.com/docs/loki/latest/setup/install/helm/)

            

            *   [Helm chart components](https://grafana.com/docs/loki/latest/setup/install/helm/concepts/)

            

            *   [Install monolithic Loki](https://grafana.com/docs/loki/latest/setup/install/helm/install-monolithic/)

            

            *   [Install microservice Loki](https://grafana.com/docs/loki/latest/setup/install/helm/install-microservices/)

            

            *   [Install scalable Loki](https://grafana.com/docs/loki/latest/setup/install/helm/install-scalable/)

            

            *   [Cloud Deployment Guides](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/)

                

                *   [Deploy on AWS](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/aws/)

                

                *   [Deploy on Azure](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/)

                

                *   [Deploy on GCP](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/gcp/)

            

            *   [Configure storage](https://grafana.com/docs/loki/latest/setup/install/helm/configure-storage/)

            

            *   [Helm chart values](https://grafana.com/docs/loki/latest/setup/install/helm/reference/)

            

            *   [Monitoring](https://grafana.com/docs/loki/latest/setup/install/helm/monitor-and-alert/)

                

                *   [Monitor Loki using a local LGTM stack](https://grafana.com/docs/loki/latest/setup/install/helm/monitor-and-alert/with-local-monitoring/)

                

                *   [Monitor Loki with Grafana Cloud](https://grafana.com/docs/loki/latest/setup/install/helm/monitor-and-alert/with-grafana-cloud/)

        

        *   [Install using Tanka](https://grafana.com/docs/loki/latest/setup/install/tanka/)

        

        *   [Install using Docker](https://grafana.com/docs/loki/latest/setup/install/docker/)

        

        *   [Install locally](https://grafana.com/docs/loki/latest/setup/install/local/)

        

        *   [Install on Istio](https://grafana.com/docs/loki/latest/setup/install/istio/)

        

        *   [Install from source](https://grafana.com/docs/loki/latest/setup/install/install-from-source/)

    

    *   [Migrate](https://grafana.com/docs/loki/latest/setup/migrate/)

        

        *   [Migrate to Alloy](https://grafana.com/docs/loki/latest/setup/migrate/migrate-to-alloy/)

        

        *   [Migrate from SSD to distributed](https://grafana.com/docs/loki/latest/setup/migrate/ssd-to-distributed/)

        

        *   [Migrate to TSDB](https://grafana.com/docs/loki/latest/setup/migrate/migrate-to-tsdb/)

        

        *   [Migrate from `loki-distributed`](https://grafana.com/docs/loki/latest/setup/migrate/migrate-from-distributed/)

        

        *   [Migrate to three targets](https://grafana.com/docs/loki/latest/setup/migrate/migrate-to-three-scalable-targets/)

        

        *   [Migrate to Thanos storage clients](https://grafana.com/docs/loki/latest/setup/migrate/migrate-storage-clients/)

    

    *   [Upgrade](https://grafana.com/docs/loki/latest/setup/upgrade/)

        

        *   [Upgrade the Helm chart to 3.0](https://grafana.com/docs/loki/latest/setup/upgrade/upgrade-from-2x/)

        

        *   [Upgrade the Helm chart to 6.0](https://grafana.com/docs/loki/latest/setup/upgrade/upgrade-to-6x/)

*   [Configure](https://grafana.com/docs/loki/latest/configure/)

    

    *   [Best practices](https://grafana.com/docs/loki/latest/configure/bp-configure/)

    

    *   [Storage](https://grafana.com/docs/loki/latest/configure/storage/)

    

    *   [Examples](https://grafana.com/docs/loki/latest/configure/examples/)

        

        *   [Configuration](https://grafana.com/docs/loki/latest/configure/examples/configuration-examples/)

        

        *   [Thanos storage examples](https://grafana.com/docs/loki/latest/configure/examples/thanos-storage-configs/)

        

        *   [Query frontend example](https://grafana.com/docs/loki/latest/configure/examples/query-frontend/)

*   [Send data](https://grafana.com/docs/loki/latest/send-data/)

    

    *   [Grafana Alloy](https://grafana.com/docs/loki/latest/send-data/alloy/)

        

        *   [Sending Logs to Loki via Kafka using Alloy](https://grafana.com/docs/loki/latest/send-data/alloy/examples/alloy-kafka-logs/)

        

        *   [Sending OpenTelemetry logs to Loki using Alloy](https://grafana.com/docs/loki/latest/send-data/alloy/examples/alloy-otel-logs/)

    

    *   [OpenTelemetry](https://grafana.com/docs/loki/latest/send-data/otel/)

        

        *   [Native OTLP endpoint vs Loki Exporter](https://grafana.com/docs/loki/latest/send-data/otel/native_otlp_vs_loki_exporter/)

        

        *   [OTel Collector tutorial](https://grafana.com/docs/loki/latest/send-data/otel/otel-collector-getting-started/)

    

    *   [Kubernetes Monitoring Helm](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/)

    

    *   [Promtail](https://grafana.com/docs/loki/latest/send-data/promtail/)

        

        *   [Install Promtail](https://grafana.com/docs/loki/latest/send-data/promtail/installation/)

        

        *   [Configuration reference](https://grafana.com/docs/loki/latest/send-data/promtail/configuration/)

        

        *   [Configure for cloud](https://grafana.com/docs/loki/latest/send-data/promtail/cloud/)

            

            *   [Promtail on EC2](https://grafana.com/docs/loki/latest/send-data/promtail/cloud/ec2/)

            

            *   [Promtail on ECS](https://grafana.com/docs/loki/latest/send-data/promtail/cloud/ecs/)

            

            *   [Promtail on EKS](https://grafana.com/docs/loki/latest/send-data/promtail/cloud/eks/)

            

            *   [Promtail on GCP](https://grafana.com/docs/loki/latest/send-data/promtail/cloud/gcp/)

        

        *   [Configure service discovery](https://grafana.com/docs/loki/latest/send-data/promtail/scraping/)

        

        *   [Configure log rotation](https://grafana.com/docs/loki/latest/send-data/promtail/logrotation/)

        

        *   [Pipelines](https://grafana.com/docs/loki/latest/send-data/promtail/pipelines/)

        

        *   [Pipeline stages](https://grafana.com/docs/loki/latest/send-data/promtail/stages/)

            

            *   [cri](https://grafana.com/docs/loki/latest/send-data/promtail/stages/cri/)

            

            *   [decolorize](https://grafana.com/docs/loki/latest/send-data/promtail/stages/decolorize/)

            

            *   [docker](https://grafana.com/docs/loki/latest/send-data/promtail/stages/docker/)

            

            *   [drop](https://grafana.com/docs/loki/latest/send-data/promtail/stages/drop/)

            

            *   [eventlogmessage](https://grafana.com/docs/loki/latest/send-data/promtail/stages/eventlogmessage/)

            

            *   [geoip](https://grafana.com/docs/loki/latest/send-data/promtail/stages/geoip/)

            

            *   [json](https://grafana.com/docs/loki/latest/send-data/promtail/stages/json/)

            

            *   [labelallow](https://grafana.com/docs/loki/latest/send-data/promtail/stages/labelallow/)

            

            *   [labeldrop](https://grafana.com/docs/loki/latest/send-data/promtail/stages/labeldrop/)

            

            *   [labels](https://grafana.com/docs/loki/latest/send-data/promtail/stages/labels/)

            

            *   [limit](https://grafana.com/docs/loki/latest/send-data/promtail/stages/limit/)

            

            *   [logfmt](https://grafana.com/docs/loki/latest/send-data/promtail/stages/logfmt/)

            

            *   [match](https://grafana.com/docs/loki/latest/send-data/promtail/stages/match/)

            

            *   [metrics](https://grafana.com/docs/loki/latest/send-data/promtail/stages/metrics/)

            

            *   [multiline](https://grafana.com/docs/loki/latest/send-data/promtail/stages/multiline/)

            

            *   [output](https://grafana.com/docs/loki/latest/send-data/promtail/stages/output/)

            

            *   [pack](https://grafana.com/docs/loki/latest/send-data/promtail/stages/pack/)

            

            *   [regex](https://grafana.com/docs/loki/latest/send-data/promtail/stages/regex/)

            

            *   [replace](https://grafana.com/docs/loki/latest/send-data/promtail/stages/replace/)

            

            *   [sampling](https://grafana.com/docs/loki/latest/send-data/promtail/stages/sampling/)

            

            *   [static_labels](https://grafana.com/docs/loki/latest/send-data/promtail/stages/static_labels/)

            

            *   [structured_metadata](https://grafana.com/docs/loki/latest/send-data/promtail/stages/structured_metadata/)

            

            *   [template](https://grafana.com/docs/loki/latest/send-data/promtail/stages/template/)

            

            *   [tenant](https://grafana.com/docs/loki/latest/send-data/promtail/stages/tenant/)

            

            *   [timestamp](https://grafana.com/docs/loki/latest/send-data/promtail/stages/timestamp/)

        

        *   [Troubleshooting](https://grafana.com/docs/loki/latest/send-data/promtail/troubleshooting/)

    

    *   [Docker driver](https://grafana.com/docs/loki/latest/send-data/docker-driver/)

        

        *   [Configure Docker driver](https://grafana.com/docs/loki/latest/send-data/docker-driver/configuration/)

    

    *   [Fluent Bit](https://grafana.com/docs/loki/latest/send-data/fluentbit/)

        

        *   [Fluent Bit tutorial](https://grafana.com/docs/loki/latest/send-data/fluentbit/fluent-bit-loki-tutorial/)

        

        *   [Fluent Bit Community Plugin](https://grafana.com/docs/loki/latest/send-data/fluentbit/community-plugin/)

        

        *   [Fluent Bit](https://grafana.com/docs/loki/latest/send-data/fluentbit/fluent-bit-plugin/)

    

    *   [Fluentd](https://grafana.com/docs/loki/latest/send-data/fluentd/)

    

    *   [Lambda Promtail](https://grafana.com/docs/loki/latest/send-data/lambda-promtail/)

    

    *   [Logstash plugin](https://grafana.com/docs/loki/latest/send-data/logstash/)

    

    *   [k6 load testing](https://grafana.com/docs/loki/latest/send-data/k6/)

        

        *   [Log generation](https://grafana.com/docs/loki/latest/send-data/k6/log-generation/)

        

        *   [Write path testing](https://grafana.com/docs/loki/latest/send-data/k6/write-scenario/)

        

        *   [Query testing](https://grafana.com/docs/loki/latest/send-data/k6/query-scenario/)

*   [Query](https://grafana.com/docs/loki/latest/query/)

    

    *   [Query best practices](https://grafana.com/docs/loki/latest/query/bp-query/)

    

    *   [LogQL simulator](https://grafana.com/docs/loki/latest/query/analyzer/)

    

    *   [Log queries](https://grafana.com/docs/loki/latest/query/log_queries/)

    

    *   [Metric queries](https://grafana.com/docs/loki/latest/query/metric_queries/)

    

    *   [Template functions](https://grafana.com/docs/loki/latest/query/template_functions/)

    

    *   [LogCLI](https://grafana.com/docs/loki/latest/query/logcli/)

        

        *   [Getting started](https://grafana.com/docs/loki/latest/query/logcli/getting-started/)

        

        *   [LogCLI tutorial](https://grafana.com/docs/loki/latest/query/logcli/logcli-tutorial/)

    

    *   [Matching IP addresses](https://grafana.com/docs/loki/latest/query/ip/)

    

    *   [Query examples](https://grafana.com/docs/loki/latest/query/query_examples/)

    

    *   [Query acceleration](https://grafana.com/docs/loki/latest/query/query_acceleration/)

    

    *   [Query Reference](https://grafana.com/docs/loki/latest/query/query_reference/)

    

    *   [Troubleshoot queries](https://grafana.com/docs/loki/latest/query/troubleshoot-query/)

*   [Visualize](https://grafana.com/docs/loki/latest/visualize/grafana/)

*   [Alert](https://grafana.com/docs/loki/latest/alert/)

*   [Manage](https://grafana.com/docs/loki/latest/operations/)

    

    *   [Loki Canary](https://grafana.com/docs/loki/latest/operations/loki-canary/)

    

    *   [Unwanted queries](https://grafana.com/docs/loki/latest/operations/blocking-queries/)

    

    *   [Caching](https://grafana.com/docs/loki/latest/operations/caching/)

    

    *   [Rate limits](https://grafana.com/docs/loki/latest/operations/request-validation-rate-limits/)

    

    *   [Query fairness](https://grafana.com/docs/loki/latest/operations/query-fairness/)

    

    *   [Shuffle sharding](https://grafana.com/docs/loki/latest/operations/shuffle-sharding/)

    

    *   [Monitor Loki](https://grafana.com/docs/loki/latest/operations/meta-monitoring/)

        

        *   [Deploy Loki Meta Monitoring](https://grafana.com/docs/loki/latest/operations/meta-monitoring/deploy/)

        

        *   [Install Mixins](https://grafana.com/docs/loki/latest/operations/meta-monitoring/mixins/)

    

    *   [Troubleshooting](https://grafana.com/docs/loki/latest/operations/troubleshooting/)

        

        *   [Troubleshoot operations](https://grafana.com/docs/loki/latest/operations/troubleshooting/troubleshoot-operations/)

        

        *   [Troubleshoot drilldown](https://grafana.com/docs/loki/latest/operations/troubleshooting/troubleshoot-drilldown/)

        

        *   [Troubleshoot ingestion](https://grafana.com/docs/loki/latest/operations/troubleshooting/troubleshoot-ingest/)

        

        *   [Troubleshoot queries](https://grafana.com/docs/loki/latest/operations/troubleshooting/troubleshoot-query/)

    

    *   [Authentication](https://grafana.com/docs/loki/latest/operations/authentication/)

    

    *   [Bloom filters](https://grafana.com/docs/loki/latest/operations/bloom-filters/)

    

    *   [Automatic stream sharding](https://grafana.com/docs/loki/latest/operations/automatic-stream-sharding/)

    

    *   [Scale Loki](https://grafana.com/docs/loki/latest/operations/scalability/)

    

    *   [Recording rules](https://grafana.com/docs/loki/latest/operations/recording-rules/)

    

    *   [Storage](https://grafana.com/docs/loki/latest/operations/storage/)

        

        *   [TSDB](https://grafana.com/docs/loki/latest/operations/storage/tsdb/)

        

        *   [BoltDB Shipper](https://grafana.com/docs/loki/latest/operations/storage/boltdb-shipper/)

        

        *   [Filesystem object store](https://grafana.com/docs/loki/latest/operations/storage/filesystem/)

        

        *   [Storage schema](https://grafana.com/docs/loki/latest/operations/storage/schema/)

        

        *   [Write Ahead Log](https://grafana.com/docs/loki/latest/operations/storage/wal/)

        

        *   [Log retention](https://grafana.com/docs/loki/latest/operations/storage/retention/)

        

        *   [Log entry deletion](https://grafana.com/docs/loki/latest/operations/storage/logs-deletion/)

        

        *   [Horizontal scaling of Compactor](https://grafana.com/docs/loki/latest/operations/storage/compactor-horizontal-scaling/)

        

        *   [Legacy storage](https://grafana.com/docs/loki/latest/operations/storage/legacy-storage/)

        

        *   [Table manager](https://grafana.com/docs/loki/latest/operations/storage/table-manager/)

    

    *   [Multi-tenancy](https://grafana.com/docs/loki/latest/operations/multi-tenancy/)

    

    *   [Autoscaling queriers](https://grafana.com/docs/loki/latest/operations/autoscaling_queriers/)

    

    *   [Upgrade](https://grafana.com/docs/loki/latest/operations/upgrade/)

    

    *   [Overrides Exporter](https://grafana.com/docs/loki/latest/operations/overrides-exporter/)

    

    *   [Zone aware ingesters](https://grafana.com/docs/loki/latest/operations/zone-ingesters/)

*   [Reference](https://grafana.com/docs/loki/latest/reference/)

    

    *   [Loki configuration reference](https://grafana.com/docs/loki/latest/reference/loki-config-ref/)

    

    *   [Loki HTTP API](https://grafana.com/docs/loki/latest/reference/loki-http-api/)

*   [Community](https://grafana.com/docs/loki/latest/community/)

    

    *   [Contacting the Loki Team](https://grafana.com/docs/loki/latest/community/getting-in-touch/)

    

    *   [Contributing to Loki](https://grafana.com/docs/loki/latest/community/contributing/)

    

    *   [Governance](https://grafana.com/docs/loki/latest/community/governance/)

    

    *   [Maintaining](https://grafana.com/docs/loki/latest/community/maintaining/)

        

        *   [Releasing Grafana Loki](https://grafana.com/docs/loki/latest/community/maintaining/release/)

            

            *   [Backport commits](https://grafana.com/docs/loki/latest/community/maintaining/release/backport-commits/)

            

            *   [Create Release Branch](https://grafana.com/docs/loki/latest/community/maintaining/release/create-release-branch/)

            

            *   [Document metrics and configurations changes](https://grafana.com/docs/loki/latest/community/maintaining/release/document-metrics-configurations-changes/)

            

            *   [Merge Release PR](https://grafana.com/docs/loki/latest/community/maintaining/release/merge-release-pr/)

            

            *   [Patch Go version](https://grafana.com/docs/loki/latest/community/maintaining/release/patch-go-version/)

            

            *   [Patch vulnerabilities](https://grafana.com/docs/loki/latest/community/maintaining/release/patch-vulnerabilities/)

            

            *   [Prepare Major Release](https://grafana.com/docs/loki/latest/community/maintaining/release/major-release/)

            

            *   [Prepare Release](https://grafana.com/docs/loki/latest/community/maintaining/release/prepare-release/)

            

            *   [Prepare Upgrade guide](https://grafana.com/docs/loki/latest/community/maintaining/release/prepare-upgrade-guide/)

            

            *   [Update version numbers](https://grafana.com/docs/loki/latest/community/maintaining/release/update-version-numbers/)

            

            *   [Version](https://grafana.com/docs/loki/latest/community/maintaining/release/concepts/version/)

        

        *   [Releasing Loki Build Image](https://grafana.com/docs/loki/latest/community/maintaining/release-loki-build-image/)

    

    *   [Loki Improvement Documents (LIDs)](https://grafana.com/docs/loki/latest/community/lids/)

        

        *   [0001: Introducing LIDs](https://grafana.com/docs/loki/latest/community/lids/0001-introduction/)

        

        *   [0002: Remote Rule Evaluation](https://grafana.com/docs/loki/latest/community/lids/0002-remoteruleevaluation/)

        

        *   [0003: Query fairness across users within tenants](https://grafana.com/docs/loki/latest/community/lids/0003-queryfairnessinscheduler/)

        

        *   [0004: Index Gateway Sharding](https://grafana.com/docs/loki/latest/community/lids/0004-indexgatewaysharding/)

        

        *   [0005: Loki mixin configuration improvements](https://grafana.com/docs/loki/latest/community/lids/0005-loki-mixin-configuration-improvements/)

        

        *   [0006: Expose Split Logic in API](https://grafana.com/docs/loki/latest/community/lids/0006-api-expose-split/)

    

    *   [Design documents](https://grafana.com/docs/loki/latest/community/design-documents/)

        

        *   [Labels](https://grafana.com/docs/loki/latest/community/design-documents/labels/)

        

        *   [Promtail Push API](https://grafana.com/docs/loki/latest/community/design-documents/2020-02-promtail-push-api/)

        

        *   [Write-Ahead Logs](https://grafana.com/docs/loki/latest/community/design-documents/2020-09-write-ahead-log/)

        

        *   [Ordering Constraint Removal](https://grafana.com/docs/loki/latest/community/design-documents/2021-01-ordering-constraint-removal/)

*   [Copyright notice](https://grafana.com/docs/copyright-notice/)

Scroll for more

[Documentation](https://grafana.com/docs/)![Image 116: breadcrumb arrow](https://grafana.com/static/assets/img/icons/grafana-icon-breadcrumb-arrow-gray.svg)[Grafana Loki](https://grafana.com/docs/loki/latest/)![Image 117: breadcrumb arrow](https://grafana.com/static/assets/img/icons/grafana-icon-breadcrumb-arrow-gray.svg)[Set up](https://grafana.com/docs/loki/latest/setup/)![Image 118: breadcrumb arrow](https://grafana.com/static/assets/img/icons/grafana-icon-breadcrumb-arrow-gray.svg)[Install](https://grafana.com/docs/loki/latest/setup/install/)![Image 119: breadcrumb arrow](https://grafana.com/static/assets/img/icons/grafana-icon-breadcrumb-arrow-gray.svg)[Install using Helm](https://grafana.com/docs/loki/latest/setup/install/helm/)![Image 120: breadcrumb arrow](https://grafana.com/static/assets/img/icons/grafana-icon-breadcrumb-arrow-gray.svg)[Cloud Deployment Guides](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/)![Image 121: breadcrumb arrow](https://grafana.com/static/assets/img/icons/grafana-icon-breadcrumb-arrow-gray.svg)Deploy on Azure

Open source 

Deploy the Loki Helm chart on Azure[](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/#deploy-the-loki-helm-chart-on-azure)
===========================================================================================================================================================

This guide shows how to deploy a minimally viable Loki in **microservice** mode on Azure using the Helm chart. In order to successfully complete this guide, you must have the necessary tools and permissions to deploy resources on Azure, such as:

*   Full access to AKS (Azure Kubernetes Service)
*   Full access to Azure Blob Storage
*   Sufficient permissions to create federated credentials and roles in Azure AD (Active Directory)

There are four primary ways to authenticate Loki with Azure:

*   Hard coding a connection string - this is the simplest method but is not recommended for production environments.
*   Service principal
*   Managed identity
*   Federated token

In this guide, we will use the federated token method to deploy Loki on Azure. This method is more secure than hard coding a connection string and is more suitable for production environments.

Considerations[](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/#considerations)
-----------------------------------------------------------------------------------------------------------------

> Caution
> 
> 
> This guide was accurate at the time it was last updated on **6th of February, 2026**. As cloud providers frequently update their services and offerings, as a best practice, you should refer to the [Azure documentation](https://learn.microsoft.com/en-us/azure/) before creating your storage account and assigning roles.

*   **AD Role:** In this tutorial we will create a role in Azure Active Directory (Azure AD) to allow Loki to read and write from Azure Blob Storage. This role will be assigned to the Loki service account. You may want to adjust the permissions based on your requirements.

*   **Authentication:** Grafana Loki comes with a basic authentication layer. The Loki gateway (NGINX) is exposed to the internet using basic authentication in this example. NGINX can also be replaced with other open-source reverse proxies. Refer to [Authentication](https://grafana.com/docs/loki/latest/operations/authentication/) for more information.

*   **Retention:** The retention period is set to 28 days in the `values.yaml` file. You may wish to adjust this based on your requirements.

*   **Costs:** Running Loki on Azure will incur costs. Make sure to monitor your usage and costs to avoid any unexpected bills. In this guide we have used a simple AKS cluster with 3 nodes and `Standard_E2ds_v5` instances. You may wish to adjust the instance types and number of nodes based on your workload.

Prerequisites[](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/#prerequisites)
---------------------------------------------------------------------------------------------------------------

*   Helm 3 or above. Refer to [Installing Helm](https://helm.sh/docs/intro/install/). This should be installed on your local machine.
*   Kubectl installed on your local machine. Refer to [Install and Set Up kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/).
*   Azure CLI installed on your local machine. Refer to [Installing the Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli). This is a requirement for following this guide as all resources will be created using the Azure CLI.

### AKS minimum requirements[](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/#aks-minimum-requirements)

Before creating an AKS cluster in Azure you need to create a resource group. You can create a resource group using the Azure CLI:

Bash![Image 122: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy

```bash
az group create --name <INSERT-NAME> -location <INSERT-AZURE-REGION>
```

> Caution
> 
> 
> These AKS requirements are the minimum specification needed to deploy Loki using this guide. You may wish to adjust the instance types based on your Azure environment and workload. **If you choose to do so, we cannot guarantee that this sample configuration will still meet your needs.**
> 
> 
> In this guide, we deploy Loki using `Standard_E2ds_v5` instances. This is to make sure we remain within the free tier limits for Azure. Which allows us to deploy up to 10 vCPUs within a region. We recommend for large production workloads to scale these nodes up to `Standard_D4_v5`.

The minimum requirements for deploying Loki on AKS are:

*   Kubernetes version `1.30` or above.
*   `3` nodes for the AKS cluster.
*   Instance type depends on your workload. A good starting point for a production cluster in the free tier is `Standard_E2ds_v5` instances and for large production workloads `Standard_D4_v5` instances.

Here is how to create an AKS cluster with the minimum requirements:

Bash![Image 123: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy

```bash
az aks create \
  --resource-group <MY_RESOURCE_GROUP_NAME> \
  --name <MY_AKS_CLUSTER_NAME> \
  --node-count 3 \
  --node-vm-size Standard_E2ds_v5 \
  --generate-ssh-keys \
  --enable-workload-identity \
  --enable-oidc-issuer
```

Note in the above command we have enabled workload identity and OIDC issuer. This is required for the Loki service account to authenticate with Azure AD. If you have already created an AKS cluster, you can enable these features using the following command:

Bash![Image 124: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy

```bash
az aks update \
  --resource-group <MY_RESOURCE_GROUP_NAME> \
  --name <MY_AKS_CLUSTER_NAME> \
  --enable-workload-identity \
  --enable-oidc-issuer
```

The Azure CLI also lets you bind the AKS cluster to kubectl. You can do this by running the following command:

Bash![Image 125: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy

```bash
az aks get-credentials --resource-group <MY_RESOURCE_GROUP_NAME> --name <MY_AKS_CLUSTER_NAME>
```

Configuring Azure Blob Storage[](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/#configuring-azure-blob-storage)
-------------------------------------------------------------------------------------------------------------------------------------------------

> Tip
> 
> 
> Consider using unique bucket names rather than: `chunk`, `ruler`, and `admin`. Although Azure Blog Storage is not directly affected by this [security update](https://grafana.com/blog/2024/06/27/grafana-security-update-grafana-loki-and-unintended-data-write-attempts-to-amazon-s3-buckets/) it is a best practice to use unique container names for buckets.

Before deploying Loki, you need to create two Azure storage containers; one to store logs (chunks), the second to store alert rules. You can create the containers using the Azure CLI. Containers must exist inside a storage account.

> Note
> 
> 
> GEL customers will require a third container to store the admin data. This container is not required for OSS users.

1.   Create a storage account:

Bash![Image 126: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy  ```bash
az storage account create \
--name <NAME> \
--location <REGION> \
--sku Standard_ZRS \
--encryption-services blob \
--resource-group <MY_RESOURCE_GROUP_NAME>
```  
Replace the placeholders with your desired values.

2.   Create the containers for chunks and ruler:

Bash![Image 127: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy  ```bash
az storage container create --account-name <STORAGE-ACCOUNT-NAME> --name <CHUNK-BUCKET-NAME> --auth-mode login && \
az storage container create --account-name <STORAGE-ACCOUNT-NAME> --name <RULER-BUCKET-NAME> --auth-mode login
```  
Make sure `--account-name` matches the account you just created

With the storage account and containers created, you can now proceed to creating the Azure AD role and federated credentials.

Creating the Azure AD role and federated credentials[](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/#creating-the-azure-ad-role-and-federated-credentials)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The recommended way to authenticate Loki with Azure Blob Storage is to use federated credentials. This method is more secure than hard coding a connection string directly into the Loki configuration. In this next section, we will create an Azure AD role and federated credentials for Loki to allow it to read and write from Azure Blob Storage:

1.   Locate the OpenID Connect (OIDC) issuer URL:

Bash![Image 128: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy  ```bash
az aks show \
--resource-group <MY_RESOURCE_GROUP_NAME> \
--name <MY_AKS_CLUSTER_NAME> \
--query "oidcIssuerProfile.issuerUrl" \
-o tsv
```  
This command will return the OIDC issuer URL. You will need this URL to create the federated credentials.

2.   Generate a `credentials.json` file with the following content:

JSON![Image 129: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy  ```json
{
    "name": "LokiFederatedIdentity",
    "issuer": "<OIDC-ISSUER-URL>",
    "subject": "system:serviceaccount:loki:loki",
    "description": "Federated identity for Loki accessing Azure resources",
    "audiences": [
      "api://AzureADTokenExchange"
    ]
}
```  
Replace `<OIDC-ISSUER-URL>` with the OIDC issuer URL you found in the previous step.

3.   Make sure you to save the `credentials.json` file before continuing.

4.   Next generate an Azure directory `app`. We will use this to assign our federated credentials to:

Bash![Image 130: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy  ```bash
az ad app create \
 --display-name loki \
 --query appId \
 -o tsv
```  
This will return the app ID. Save this for later use. If you need to find the app ID later you can run the following command:

Bash![Image 131: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy  ```bash
az ad app list --display-name loki --query "[].appId" -o tsv
```  
5.   The app requires a service principal to authenticate with Azure AD. Create a service principal for the app:

Bash![Image 132: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy  ```bash
az ad sp create --id <APP-ID>
```  
Replace `<APP-ID>` with the app ID you generated in the previous step.

6.   Next assign the federated credentials to the app:

Bash![Image 133: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy  ```bash
az ad app federated-credential create \
  --id <APP-ID> \
  --parameters credentials.json
```  
Replace `<APP-ID>` with the app ID you generated in the previous step.

7.   Lastly add a role assignment to the app:

Bash![Image 134: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy  ```bash
az role assignment create \
  --role "Storage Blob Data Contributor" \
  --assignee <APP-ID> \
  --scope /subscriptions/<SUBSCRIPTION-ID>/resourceGroups/<RESOURCE-GROUP>/providers/Microsoft.Storage/storageAccounts/<STORAGE-ACCOUNT-NAME>
```  
Replace the placeholders with your actual values.

Now that you have created the Azure AD role and federated credentials, you can proceed to deploying Loki using the Helm chart.

Deploying the Helm chart[](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/#deploying-the-helm-chart)
-------------------------------------------------------------------------------------------------------------------------------------

The following steps require the use of `helm` and `kubectl`. Make sure you have run the `az` command to bind your AKS cluster to `kubectl`:

Bash![Image 135: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy

```bash
az aks get-credentials --resource-group <MY_RESOURCE_GROUP_NAME> --name <MY_AKS_CLUSTER_NAME>
```

Before we can deploy the Loki Helm chart, we need to add the Grafana chart repository to Helm. This repository contains the Loki Helm chart.

1.   Add the Grafana chart repository to Helm:

Bash![Image 136: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy  ```bash
helm repo add grafana https://grafana.github.io/helm-charts
```  
2.   Update the chart repository:

Bash![Image 137: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy  ```bash
helm repo update
```  
3.   Create a new namespace for Loki:

Bash![Image 138: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy  ```bash
kubectl create namespace loki
```  

### Loki basic authentication[](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/#loki-basic-authentication)

Loki by default does not come with any authentication. Since we will be deploying Loki to Azure and exposing the gateway to the internet, we recommend adding at least basic authentication. In this guide we will give Loki a username and password:

1.   To start we will need create a `.htpasswd` file with the username and password. You can use the `htpasswd` command to create the file:

> Tip
> 
> 
> If you don’t have the `htpasswd` command installed, you can install it using `brew` or `apt-get` or `yum` depending on your OS. Bash![Image 139: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy  ```bash
htpasswd -c .htpasswd <username>
```  
This will create a file called `auth` with the username `loki`. You will be prompted to enter a password.

2.   Create a Kubernetes secret with the `.htpasswd` file:

Bash![Image 140: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy  ```bash
kubectl create secret generic loki-basic-auth --from-file=.htpasswd -n loki
```  
This will create a secret called `loki-basic-auth` in the `loki` namespace. We will reference this secret in the Loki Helm chart configuration.

3.   Create a `canary-basic-auth` secret for the canary:

Bash![Image 141: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy  ```bash
kubectl create secret generic canary-basic-auth \
  --from-literal=username=<USERNAME> \
  --from-literal=password=<PASSWORD> \
  -n loki
```  
We create a literal secret with the username and password for Loki canary to authenticate with the Loki gateway. Make sure to replace the placeholders with your desired username and password.

### Loki Helm chart configuration[](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/#loki-helm-chart-configuration)

Create a `values.yaml` file choosing the configuration options that best suit your requirements. Below there is an example of `values.yaml` files for the Loki Helm chart in [microservices](https://grafana.com/docs/loki/latest/get-started/deployment-modes/#microservices-mode) mode.

YAML![Image 142: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy

Expand code

```yaml
loki:
   podLabels:
    "azure.workload.identity/use": "true" # Add this label to the Loki pods to enable workload identity
   schemaConfig:
     configs:
       - from: "2024-04-01"
         store: tsdb
         object_store: azure
         schema: v13
         index:
           prefix: loki_index_
           period: 24h
   storage:
     type: azure
     bucketNames:
       chunks: "<CHUNK-CONTAINER-NAME>" # Your actual Azure Blob Storage container name (loki-azure-dev-chunks)
       ruler: "<RULER-CONTAINER-NAME>" # Your actual Azure Blob Storage container name (loki-azure-dev-ruler)
       # admin: "admin-loki-devrel" # Your actual Azure Blob Storage container name (loki-azure-dev-admin)
     azure:
       accountName: <INSERT-STORAGE-ACCOUNT-NAME>
       useFederatedToken: true # Use federated token for authentication
   ingester:
     chunk_encoding: snappy
   pattern_ingester:
     enabled: true
   limits_config:
     allow_structured_metadata: true
     volume_enabled: true
     retention_period: 672h # 28 days retention
   compactor:
     retention_enabled: true 
     delete_request_store: azure
   ruler:
     enable_api: true
     alertmanager_url: http://prom:9093 # The URL of the Alertmanager to send alerts (Prometheus, Mimir, etc.)

   querier:
     max_concurrent: 4

# Define the Azure workload identity
serviceAccount:
  name: loki
  annotations:
    "azure.workload.identity/client-id": "<APP-ID>" # The app ID of the Azure AD app
  labels:
    "azure.workload.identity/use": "true"

deploymentMode: Distributed

ingester:
 replicas: 3
 zoneAwareReplication:
  enabled: false

querier:
  replicas: 3
  maxUnavailable: 2

queryFrontend:
  replicas: 2
  maxUnavailable: 1

queryScheduler:
  replicas: 2

distributor:
  replicas: 3
  maxUnavailable: 2

compactor:
  replicas: 1

indexGateway:
  replicas: 2
  maxUnavailable: 1

ruler:
  replicas: 1
  maxUnavailable: 1

# This exposes the Loki gateway so it can be written to and queried externaly
gateway:
  service:
    type: LoadBalancer
  basicAuth: 
    enabled: true
    existingSecret: loki-basic-auth

# Since we are using basic auth, we need to pass the username and password to the canary
lokiCanary:
  extraArgs:
    - -pass=$(LOKI_PASS)
    - -user=$(LOKI_USER)
  extraEnv:
    - name: LOKI_PASS
      valueFrom:
        secretKeyRef:
          name: canary-basic-auth
          key: password
    - name: LOKI_USER
      valueFrom:
        secretKeyRef:
          name: canary-basic-auth
          key: username

# Enable minio for storage
minio:
  enabled: false

backend:
  replicas: 0
read:
  replicas: 0
write:
  replicas: 0

singleBinary:
  replicas: 0
```

> Caution
> 
> 
> Make sure to replace the placeholders with your actual values.

It is critical to define a valid `values.yaml` file for the Loki deployment. To remove the risk of misconfiguration, let’s break down the configuration options to keep in mind when deploying to Azure:

*   **Loki Config vs. Values Config:**

    *   The `values.yaml` file contains a section called `loki`, which contains a direct representation of the Loki configuration file.
    *   This section defines the Loki configuration, including the schema, storage, and querier configuration.
    *   The key configuration to focus on for chunks is the `storage` section, where you define the Azure container name and storage account. This tells Loki where to store the chunks.
    *   The `ruler` section defines the configuration for the ruler, including the Azure container name and storage account. This tells Loki where to store the alert and recording rules.
    *   For the full Loki configuration, refer to the [Loki Configuration](https://grafana.com/docs/loki/latest/configure/) documentation.

*   **Storage:**

    *   Defines where the Helm chart stores data.
    *   Set the type to `azure` since we are using Azure Blob Storage.
    *   Configure the container names for the chunks and ruler to match the containers created earlier.
    *   The `azure` section specifies the storage account name and also sets `useFederatedToken` to `true`. This tells Loki to use federated credentials for authentication.

*   **Service Account:**

    *   The `serviceAccount` section is used to define the federated workload identity Loki will use to authenticate with Azure AD.
    *   We set the `azure.workload.identity/client-id` annotation to the app ID of the Azure AD app.

*   **Gateway:**

    *   Defines how the Loki gateway will be exposed.
    *   We are using a `LoadBalancer` service type in this configuration.

### Deploy Loki[](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/#deploy-loki)

Now that you have created the `values.yaml` file, you can deploy Loki using the Helm chart.

1.   Deploy using the newly created `values.yaml` file:

Bash![Image 143: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy  ```bash
helm install --values values.yaml loki grafana/loki -n loki --create-namespace
```  
It is important to create a namespace called `loki` as our federated credentials were generated with the value `system:serviceaccount:loki:loki`. This translates to the `loki` service account in the `loki` namespace. This is configurable but make sure to update the federated credentials file first.

2.   Verify the deployment:

Bash![Image 144: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy  ```bash
kubectl get pods -n loki
```  
You should see the Loki pods running.

console![Image 145: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy  Expand code 
```console
NAME                                    READY   STATUS    RESTARTS   AGE
loki-canary-crqpg                       1/1     Running   0          10m
loki-canary-hm26p                       1/1     Running   0          10m
loki-canary-v9wv9                       1/1     Running   0          10m
loki-chunks-cache-0                     2/2     Running   0          10m
loki-compactor-0                        1/1     Running   0          10m
loki-distributor-78ccdcc9b4-9wlhl       1/1     Running   0          10m
loki-distributor-78ccdcc9b4-km6j2       1/1     Running   0          10m
loki-distributor-78ccdcc9b4-ptwrb       1/1     Running   0          10m
loki-gateway-5f97f78755-hm6mx           1/1     Running   0          10m
loki-index-gateway-0                    1/1     Running   0          10m
loki-index-gateway-1                    1/1     Running   0          10m
loki-ingester-zone-a-0                  1/1     Running   0          10m
loki-ingester-zone-b-0                  1/1     Running   0          10m
loki-ingester-zone-c-0                  1/1     Running   0          10m
loki-querier-89d4ff448-4vr9b            1/1     Running   0          10m
loki-querier-89d4ff448-7nvrf            1/1     Running   0          10m
loki-querier-89d4ff448-q89kh            1/1     Running   0          10m
loki-query-frontend-678899db5-n5wc4     1/1     Running   0          10m
loki-query-frontend-678899db5-tf69b     1/1     Running   0          10m
loki-query-scheduler-7d666bf759-9xqb5   1/1     Running   0          10m
loki-query-scheduler-7d666bf759-kpb5q   1/1     Running   0          10m
loki-results-cache-0                    2/2     Running   0          10m
loki-ruler-0                            1/1     Running   0          10m
```  

### Find the Loki gateway service[](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/#find-the-loki-gateway-service)

The Loki gateway service is a load balancer service that exposes the Loki gateway to the internet. This is where you will write logs to and query logs from. By default NGINX is used as the gateway.

> Caution
> 
> 
> The Loki gateway service is exposed to the internet. We provide basic authentication using a username and password in this tutorial. Refer to the [Authentication](https://grafana.com/docs/loki/latest/operations/authentication/) documentation for more information.

To find the Loki gateway service, run the following command:

Bash![Image 146: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy

```bash
kubectl get svc -n loki
```

You should see the Loki gateway service with an external IP address. This is the address you will use to write to and query Loki.

console![Image 147: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy

```console
NAME                             TYPE           CLUSTER-IP       EXTERNAL-IP    PORT(S)              AGE
loki-gateway                     LoadBalancer   10.100.201.74     134.236.21.145  80:30707/TCP         46m
```

Congratulations! You have successfully deployed Loki on Azure using the Helm chart. Before we finish, let’s test the deployment.

Testing Your Loki Deployment[](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/#testing-your-loki-deployment)
---------------------------------------------------------------------------------------------------------------------------------------------

k6 is one of the fastest ways to test your Loki deployment. This will allow you to both write and query logs to Loki. To get started with k6, follow the steps below:

1.   Install k6 with the Loki extension on your local machine. Refer to [Installing k6 and the xk6-loki extension](https://grafana.com/docs/loki/latest/send-data/k6/).

2.   Create a `azure-test.js` file with the following content:

JavaScript![Image 148: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy  Expand code 
```javascript
import {sleep, check} from 'k6';
 import loki from 'k6/x/loki';

 /**
 * URL used for push and query requests
 * Path is automatically appended by the client
 * @constant {string}
 */

 const username = '<USERNAME>';
 const password = '<PASSWORD>';
 const external_ip = '<EXTERNAL-IP>';

 const credentials = `${username}:${password}`;

 const BASE_URL = `http://${credentials}@${external_ip}`;

 /**
 * Helper constant for byte values
 * @constant {number}
 */
 const KB = 1024;

 /**
 * Helper constant for byte values
 * @constant {number}
 */
 const MB = KB * KB;

 /**
 * Instantiate config and Loki client
 */

 const conf = new loki.Config(BASE_URL);
 const client = new loki.Client(conf);

 /**
 * Define test scenario
 */
 export const options = {
   vus: 10,
   iterations: 10,
 };

 export default () => {
   // Push request with 10 streams and uncompressed logs between 800KB and 2MB
   var res = client.pushParameterized(10, 800 * KB, 2 * MB);
   // Check for successful write
   check(res, { 'successful write': (res) => res.status == 204 });

   // Pick a random log format from label pool
   let format = randomChoice(conf.labels["format"]);

   // Execute instant query with limit 1
   res = client.instantQuery(`count_over_time({format="${format}"}[1m])`, 1)
   // Check for successful read
   check(res, { 'successful instant query': (res) => res.status == 200 });

   // Execute range query over last 5m and limit 1000
   res = client.rangeQuery(`{format="${format}"}`, "5m", 1000)
   // Check for successful read
   check(res, { 'successful range query': (res) => res.status == 200 });

   // Wait before next iteration
   sleep(1);
 }

 /**
 * Helper function to get random item from array
 */
 function randomChoice(items) {
   return items[Math.floor(Math.random() * items.length)];
 }
```  
Replace `<EXTERNAL-IP>` with the external IP address of the Loki Gateway service.

This script will write logs to Loki and query logs from Loki. It will write logs in a random format between 800KB and 2MB and query logs in a random format over the last 5 minutes.

3.   Run the test:

Bash![Image 149: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy  ```bash
./k6 run azure-test.js
```  
This will run the test and output the results. You should see the test writing logs to Loki and querying logs from Loki.

Now that you have successfully deployed Loki in microservices mode on Microsoft Azure, you may wish to explore the following:

*   [Sending data to Loki](https://grafana.com/docs/loki/latest/send-data/)
*   [Querying Loki](https://grafana.com/docs/loki/latest/query/)
*   [Manage Loki](https://grafana.com/docs/loki/latest/operations/)

Was this page helpful?
----------------------

![Image 150: 👎](https://grafana.com/media/images/svg/thumbs-up.svg) Yes![Image 151: 👎](https://grafana.com/media/images/svg/thumbs-up.svg) No

[Suggest an edit in GitHub](https://github.com/grafana/loki/edit/main/docs/sources/setup/install/helm/deployment-guides/azure.md)[Create a GitHub issue](https://github.com/grafana/loki/issues/new?title=Documentation%20feedback:%20/docs/sources/setup/install/helm/deployment-guides/azure.md)[Email docs@grafana.com](mailto:docs@grafana.com)[Help and support](https://grafana.com/help/)[Community](https://grafana.com/community/)

Related resources from Grafana Labs
-----------------------------------

Additional helpful documentation, links, and articles:

[![Image 152: video icon](https://grafana.com/static/assets/img/icons/grafana-icon-card-video.svg) Video ![Image 153: Getting started with logging and Grafana Loki](blob:http://localhost/63adff11dad904a1878c568edbadacdf) Getting started with logging and Grafana Loki See a demo of the updated features in Loki, and how to create metrics from logs and alert on your logs with powerful Prometheus-style alerting rules.](https://grafana.com/go/webinar/getting-started-with-logging-and-grafana-loki/?pg=docs-loki-latest-setup-install-helm-deployment-guides-azure&plcmt=related)[![Image 154: video icon](https://grafana.com/static/assets/img/icons/grafana-icon-card-video.svg) Video ![Image 155: Essential Grafana Loki configuration settings](blob:http://localhost/63adff11dad904a1878c568edbadacdf) Essential Grafana Loki configuration settings This webinar focuses on Grafana Loki configuration including agents Promtail and Docker; the Loki server; and Loki storage for popular backends.](https://grafana.com/go/webinar/logging-with-loki-essential-configuration-settings/?pg=docs-loki-latest-setup-install-helm-deployment-guides-azure&plcmt=related-2)[![Image 156: webinar icon](https://grafana.com/static/assets/img/icons/grafana-icon-card-webinar.svg) Video ![Image 157: Scaling and securing your logs with Grafana Loki](blob:http://localhost/63adff11dad904a1878c568edbadacdf) Scaling and securing your logs with Grafana Loki This webinar covers the challenges of scaling and securing logs, and how Grafana Cloud Logs powered by Grafana Loki can help, cost-effectively.](https://grafana.com/go/webinar/scaling-and-securing-your-logs-with-grafana-loki/?pg=docs-loki-latest-setup-install-helm-deployment-guides-azure&plcmt=related-3)

Is this page helpful?

![Image 158: 👎](https://grafana.com/media/images/svg/thumbs-up.svg) Yes![Image 159: 👎](https://grafana.com/media/images/svg/thumbs-up.svg) No

On this page

*   [Considerations](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/#considerations)
*   [Prerequisites](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/#prerequisites)
*   [AKS minimum requirements](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/#aks-minimum-requirements)
*   [Configuring Azure Blob Storage](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/#configuring-azure-blob-storage)
*   [Creating the Azure AD role and federated credentials](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/#creating-the-azure-ad-role-and-federated-credentials)
*   [Deploying the Helm chart](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/#deploying-the-helm-chart)
*   [Loki basic authentication](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/#loki-basic-authentication)
*   [Loki Helm chart configuration](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/#loki-helm-chart-configuration)
*   [Deploy Loki](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/#deploy-loki)
*   [Find the Loki gateway service](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/#find-the-loki-gateway-service)
*   [Testing Your Loki Deployment](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/#testing-your-loki-deployment)

Scroll for more

![Image 160: GrafanaCON 2026](https://grafana.com/media/events/grafanacon/2026/banners/logo-gcon2026-vert-banner-dark.svg)

Save the Date!Sign up to get the latest GrafanaCON 2026 updates, agenda drops, and first access to early-bird tickets when they’re first available.

[Sign Up](https://grafana.com/events/grafanacon/)

![Image 161: ObservabilityCON 2025](https://grafana.com/media/events/obscon/2025/logo-obscon25-simple.svg)

7-9 OCT LONDON

Learn how to leverage new AI features and observability tools, attend technical deep dives, & leave with tips for growing your observability strategy.

[Sign up to save the date](https://grafana.com/events/observabilitycon/?tech=target&pg=docs&plcmt=sidebar)

![Image 162](https://grafana.com/media/images/icons/grafana-banner-close-btn-light.svg)

![Image 163: ObservabilityCON 2025](https://grafana.com/media/banners/observabilitycon/2025/logo-ocr2025-banner.svg)

We're coming to the Bay Area FEB 25

[Join Us](https://grafana.com/events/observabilitycon-on-the-road/2025/san-francisco-bay-area/?plcmt=sidebar-banner&pg=docs-loki-latest-setup-install-helm-deployment-guides-azure&tech=target)

![Image 164: GrafanaCON 2025](https://grafana.com/media/events/grafanacon/2025/logo-gcon2025-banner-vertical.svg)

Bring your crew &

 save up to 20%  Don’t miss out—be the first to dive into Grafana 12, Prometheus 3.0, and our nearly sold-out hands-on labs on Grafana as Code, OpenTelemetry, and more.

[Register](https://grafana.com/events/grafanacon/?tech=target&plcmt=footer-banner&aud=default#register)

![Image 165: orange cloud icon](https://grafana.com/media/banners/images/cloud-banner-dashboards-bg.png)

×

###### The fastest way to get started is with the Grafana Cloud free tier which includes:

*   ![Image 166: checkmark](https://grafana.com/media/banners/images/metrics-log-yellow.svg) 10k metrics 
*   ![Image 167: checkmark](https://grafana.com/media/banners/images/logs-orange.svg) 50GB logs 
*   ![Image 168: checkmark](https://grafana.com/media/banners/images/traces-red.svg) 50GB traces 
*   ![Image 169: checkmark](https://grafana.com/media/banners/images/pink-grafana.svg) 3 active users 
*   ![Image 170: checkmark](https://grafana.com/media/banners/images/retention-purple.svg) 14-day retention 

[Create free account](https://grafana.com/auth/sign-up/create-user?plcmt=sidebar&pg=docs-loki-latest-setup-install-helm-deployment-guides-azure)

![Image 171: orange cloud icon](https://grafana.com/media/banners/images/cloud-banner-bg-icons.png)

###### The fastest way to get started is with the Grafana Cloud free tier which includes:

*   10k metrics
*    50GB logs
*   50GB traces
*   3 active users
*   14-day rentention

[Start Free](https://grafana.com/auth/sign-up/create-user?plcmt=sidebar&pg=docs-loki-latest-setup-install-helm-deployment-guides-azure)

![Image 172: Grafana 10](https://grafana.com/media/banners/images/grafana-cloud-logo.svg)

 Introducing 

 Frontend Observability 

 Our hosted service for real user monitoring. Gain precise, end-to-end user insights. 

[Sign up for free](https://grafana.com/auth/sign-up/create-user?tech=target&pg=docs&plcmt=sidebar&aud=non-cloud-frontend-observability-default)[Read the blog](https://grafana.com/blog/2023/05/02/gain-real-user-monitoring-insights-with-grafana-cloud-frontend-observability/?tech=target&pg=docs&plcmt=sidebar&aud=non-cloud-frontend-observability-default)

![Image 173: k6 cloud icon](https://grafana.com/media/products/k6-cloud/k6-sidebar-banner.svg)![Image 174](https://grafana.com/media/products/k6-cloud/k6-sidebar-banner-dark.png?w=500)
The best developer experience for performance testing

[Learn more](https://grafana.com/products/cloud/k6/?pg=docs-loki-latest-setup-install-helm-deployment-guides-azure&plcmt=sidebar)

![Image 175: k6 cloud icon](https://grafana.com/media/products/k6-cloud/k6-sidebar-banner.svg)![Image 176](https://grafana.com/media/products/k6-cloud/k6-sidebar-banner-dark.png?w=500)
Introducing Grafana Cloud k6, a new offering empowers teams to prevent system failures and deliver fast and reliable applications.

[Learn more](https://grafana.com/products/cloud/k6/?pg=docs-loki-latest-setup-install-helm-deployment-guides-azure&plcmt=sidebar)

![Image 177: Grafana Cloud Adaptive Metrics](https://grafana.com/media/images/logos/adaptive-metrics-banner-logo-2.svg)
*   Reduce metric cardinality by 30-50%
*   Pay only for metrics you use
*   Centralize control over your data in Grafana Cloud

[Create free account](https://grafana.com/auth/sign-up/create-user?pg=docs-loki-latest-setup-install-helm-deployment-guides-azure&plcmt=sidebar)[Read the blog post](https://grafana.com/blog/?pg=docs-loki-latest-setup-install-helm-deployment-guides-azure&plcmt=sidebar)

Sign up for Grafana stack updates

Subscribe

Subscribe

Email* 

Subscribe Subscribe

Sorry, an error occurred. Email [update@grafana.com](mailto:update@grafana.com) for help.

Note: By signing up, you agree to be emailed related product-level information.

* * *

[](https://grafana.com/)

[](https://www.facebook.com/grafana/)[](https://twitter.com/grafana)[](https://www.linkedin.com/company/grafana-labs/)[](https://github.com/grafana/)[](https://www.youtube.com/channel/UCYCwgQAMm9sTJv0rgwQLCxw)[](https://www.reddit.com/r/grafana/)

* * *

**Products**

*   [Grafana Cloud](https://grafana.com/products/cloud/)
*   [Grafana Enterprise Stack](https://grafana.com/products/enterprise/)
*   [Grafana visualizations](https://grafana.com/grafana/)
*   [Plugins](https://grafana.com/grafana/plugins/)
*   [Grafana Cloud Logs](https://grafana.com/products/cloud/logs/)
*   [Grafana Cloud Metrics](https://grafana.com/products/cloud/metrics/)
*   [Grafana Cloud Traces](https://grafana.com/products/cloud/traces/)
*   [Grafana Cloud Profiles](https://grafana.com/products/cloud/profiles-for-continuous-profiling/)
*   [AI/ML tools for observability](https://grafana.com/products/cloud/ai-tools-for-observability/)
*   [Application Observability](https://grafana.com/products/cloud/application-observability/)
*   [Frontend Observability](https://grafana.com/products/cloud/frontend-observability-for-real-user-monitoring/)
*   [Grafana Cloud Asserts](https://grafana.com/products/cloud/asserts/)
*   [Grafana IRM](https://grafana.com/products/cloud/irm/)
*   [Grafana k6](https://grafana.com/products/cloud/k6/)
*   [Grafana SLO](https://grafana.com/products/cloud/slo/)
*   [Synthetic Monitoring](https://grafana.com/products/cloud/synthetic-monitoring/)
*   [Integrations](https://grafana.com/integrations/)
*   [Pricing](https://grafana.com/pricing/)

**Open Source**

*   [Grafana](https://grafana.com/oss/grafana/)
*   [Grafana Alloy](https://grafana.com/oss/alloy-opentelemetry-collector/)
*   [Grafana Beyla](https://grafana.com/oss/beyla-ebpf/)
*   [Grafana Faro](https://grafana.com/oss/faro/)
*   [Grafana k6](https://grafana.com/oss/k6/)
*   [Grafana Loki](https://grafana.com/oss/loki/)
*   [Grafana Mimir](https://grafana.com/oss/mimir/)
*   [Grafana OnCall](https://grafana.com/oss/oncall/)
*   [Grafana Pyroscope](https://grafana.com/oss/pyroscope/)
*   [Grafana Tanka](https://grafana.com/oss/tanka/)
*   [Grafana Tempo](https://grafana.com/oss/tempo/)
*   [Graphite](https://grafana.com/oss/graphite/)
*   [OpenTelemetry](https://grafana.com/oss/opentelemetry/)
*   [Prometheus](https://grafana.com/oss/prometheus/)
*   [Dashboard templates](https://grafana.com/grafana/dashboards/)
*   [Downloads](https://grafana.com/get/)
*   [GitHub](https://github.com/grafana/)

**Learn**

*   [Documentation](https://grafana.com/docs/)
*   [Grafana Labs blog](https://grafana.com/blog/)
*   [Webinars and videos](https://grafana.com/videos/)
*   [Tutorials](https://grafana.com/tutorials/)
*   [Workshops](https://grafana.com/workshops/)
*   [Events](https://grafana.com/events/)
*   [Community](https://grafana.com/community/)
*   [Professional Services](https://grafana.com/professional-services/)
*   [Community forums](https://community.grafana.com/)
*   [Community Slack](https://slack.grafana.com/)
*   [Grafana Champions](https://grafana.com/community/champions/)
*   [Community organizers](https://grafana.com/community/meetups/)
*   [Observability Survey Report 2025](https://grafana.com/observability-survey/)
*   [OSS vs Cloud](https://grafana.com/oss-vs-cloud/)
*   [Writers' Toolkit](https://grafana.com/docs/writers-toolkit/)
*   [Plugin development](https://grafana.com/developers/)
*   [Load testing](https://grafana.com/load-testing/)
*   [OpenTelemetry Report](https://grafana.com/opentelemetry-report/)
*   [Log monitoring](https://grafana.com/resources/log-monitoring/)

**Company**

*   [Partnerships](https://grafana.com/partnerships/)
*   [Our team](https://grafana.com/about/team/)
*   [Careers](https://grafana.com/about/careers/)
*   [Success stories](https://grafana.com/success/)
*   [Newsroom](https://grafana.com/about/press/)
*   [Contact us](https://grafana.com/contact/)
*   [Getting help](https://grafana.com/help/)
*   [Merch](https://grafana.com/community/merch/)
*   [Open positions](https://grafana.com/about/careers/open-positions/)
We're hiring

*   [The Story of Grafana](https://grafana.com/story-of-grafana/)

**Compare**

*   [Grafana vs. Datadog](https://grafana.com/compare/grafana-vs-datadog/)

**Localized content**

*   [Japanese pages](https://grafana.com/ja/content/)
*   [German pages](https://grafana.com/de/content/)
*   [French pages](https://grafana.com/fr/content/)
*   [Spanish pages](https://grafana.com/es/content/)
*   [Portuguese pages](https://grafana.com/pt-br/content/)

* * *

*   [Grafana Cloud status](https://status.grafana.com/)

*   Your cookie preferences
*   [Legal and Security](https://grafana.com/legal/)
*   [Terms of Service](https://grafana.com/legal/terms/)
*   [Privacy Policy](https://grafana.com/legal/privacy-policy/)
*   [Trademark Policy](https://grafana.com/trademark-policy/)

Copyright 2026 © Grafana Labs

Grafana Labs uses cookies for the normal operation of this website. [**Learn more.**](https://grafana.com/terms#cookie-policy)

Got it!

[Ask Grafana Assistant](https://grafana.com/docs/loki/latest/setup/install/helm/deployment-guides/azure/)
