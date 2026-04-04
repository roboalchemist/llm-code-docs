# Source: https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/

Title: Kubernetes Monitoring Helm tutorial | Grafana Loki documentation

URL Source: https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/

Markdown Content:
Kubernetes Monitoring Helm tutorial | Grafana Loki documentation
===============

![Image 5: GrafanaCON 2026](https://grafana.com/media/events/grafanacon/2026/banners/logo-gcon2026-horiz-banner-centered.svg)![Image 6: GrafanaCON 2026](https://grafana.com/media/events/grafanacon/2026/banners/logo-gcon2026-horiz-banner-left.svg)

Save the Date!

Sign up to get the latest GrafanaCON 2026 updates, agenda drops, and first access to early-bird tickets when they’re first available.

[Sign up](https://grafana.com/events/grafanacon/)

![Image 7: GrafanaCON 2026](https://grafana.com/media/events/grafanacon/2026/banners/logo-gcon2026-horiz-banner-centered.svg)![Image 8: GrafanaCON 2026](https://grafana.com/media/events/grafanacon/2026/banners/logo-gcon2026-horiz-banner-left.svg)

We have our sights

on Barcelona

[Save the Date](https://grafana.com/events/grafanacon/)

![Image 9: ObservabilityCON 2025](https://a-us.storyblok.com/f/1022730/280x40/b0872b99f9/grafana-logo-observabilitycon-2025-black.svg/m/)

 Watch the keynote again and signup for more on-demand sessions. 

[Watch keynote](https://grafana.com/events/observabilitycon/?plcmt=obscon2025-post-event-banner)![Image 10](https://grafana.com/media/events/grafanacon/2025/icon-close-x.svg)

![Image 11: ObservabilityCON 2025](https://grafana.com/media/events/obscon/2025/grafana-obscon2025-promo-logo-black.svg)

📢 Registration + agenda now live  Explore the latest Grafana Cloud and AI solutions, learn tips & tricks from demos and hands-on workshops, and get actionable advice to advance your observability strategy. Register now and get 50% off - limited tickets available (while they last!).

[Register now](https://grafana.com/events/observabilitycon/?tech=target&plcmt=top-banner&aud=default)

Path:

![Image 12: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)

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

![Image 13: Grafana Cloud](https://grafana.com/media/menus/products/grafana-menu-icon-grafana-cloud.svg)

[Grafana Cloud overview](https://grafana.com/products/cloud)

LGTM+ Stack

[![Image 14: Grafana Cloud Logs](https://grafana.com/media/menus/products/grafana-menu-icon-logs.svg) Logs powered by Grafana Loki](https://grafana.com/products/cloud/logs/?plcmt=products-nav)

[![Image 15: Grafana](https://grafana.com/media/menus/products/grafana-menu-icon.svg) Grafana for visualization](https://grafana.com/grafana/?plcmt=products-nav)

[![Image 16: Grafana Cloud Traces](https://grafana.com/media/menus/products/grafana-menu-icon-traces.svg) Traces powered by Grafana Tempo](https://grafana.com/products/cloud/traces/?plcmt=products-nav)

[![Image 17: Grafana Cloud Metrics](https://grafana.com/media/menus/products/grafana-menu-icon-metrics.svg) Metrics powered by Grafana Mimir and Prometheus](https://grafana.com/products/cloud/metrics/?plcmt=products-nav)

Key Capabilities

[![Image 18: AI/ML](https://grafana.com/media/menus/products/grafana-menu-icon-ai-ml.svg) AI/ML insights Identify anomalies and reduce toil](https://grafana.com/products/cloud/ai-tools-for-observability/?plcmt=products-nav)

[![Image 19: Grafana Cloud Asserts](https://grafana.com/media/menus/products/grafana-menu-icon-asserts-v1.svg) Contextual root cause analysis Automated anomaly correlation](https://grafana.com/products/cloud/asserts/?plcmt=products-nav)

[![Image 20: Grafana SLO](https://grafana.com/media/menus/products/grafana-menu-icon-slo.svg) SLO management Create SLOs and error budget alerts](https://grafana.com/products/cloud/slo/?plcmt=products-nav)

[![Image 21: Grafana Alerting](https://grafana.com/media/menus/products/grafana-menu-icon-alerting.svg) Alerting Trigger alerts from any data source](https://grafana.com/products/cloud/alerting/?plcmt=products-nav)

[![Image 22: Plugins](https://grafana.com/media/menus/products/grafana-menu-icon-plugins.svg) Plugins Connect Grafana to data sources, apps, and more](https://grafana.com/grafana/plugins/?plcmt=products-nav)

Observability Solutions

[![Image 23: Application Observability](https://grafana.com/media/menus/products/grafana-menu-icon-app-o11y.svg) Application Observability Monitor application performance](https://grafana.com/products/cloud/application-observability/?plcmt=products-nav)

[![Image 24: Infrastructure Observability](https://grafana.com/media/menus/products/grafana-menu-icon-infra-o11y.svg) Infrastructure observability Ensure infrastructure health and performance](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/?plcmt=products-nav)

Testing

[![Image 25: Grafana Cloud k6](https://grafana.com/media/menus/products/grafana-menu-icon-k6.svg) Performance testing Powered by Grafana k6](https://grafana.com/products/cloud/k6/?plcmt=products-nav)

[![Image 26: Synthetic Monitoring](https://grafana.com/media/menus/products/grafana-menu-icon-synthetic-monitoring.svg) Synthetic Monitoring powered by Grafana k6](https://grafana.com/products/cloud/synthetic-monitoring/?plcmt=products-nav)

IRM

[![Image 27: Incident](https://grafana.com/media/menus/products/grafana-menu-icon-incident.svg) Incident response Routine task automation for incidents](https://grafana.com/products/cloud/incident/?plcmt=products-nav)

[![Image 28: OnCall](https://grafana.com/media/menus/products/grafana-menu-icon-oncall.svg) On-call management Flexible on-call management](https://grafana.com/products/cloud/oncall/?plcmt=products-nav)

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

![Image 29: linux server logo](https://grafana.com/static/img/logos/logo-linux.svg)

[Linux](https://grafana.com/integrations/linux-node/monitor/?plcmt=solutions-nav)

![Image 30: windows logo](https://grafana.com/media/solutions/windows-monitor/windows-icon.png)

[Windows](https://grafana.com/integrations/windows/monitor/?plcmt=solutions-nav)

![Image 31: docker logo](https://grafana.com/static/img/logos/icon-docker.svg)

[Docker](https://grafana.com/integrations/docker/monitor/?plcmt=solutions-nav)

![Image 32: postgresql logo](https://grafana.com/static/img/logos/postgresql_elephant_icon.svg)

[Postgres](https://grafana.com/integrations/postgresql/monitor/?plcmt=solutions-nav)

![Image 33: mysql logo](https://grafana.com/static/img/logos/mysql_logo_menu.svg)

[MySQL](https://grafana.com/integrations/mysql/monitor/?plcmt=solutions-nav)

![Image 34: aws logo](https://grafana.com/media/images/logos/aws-logo-light.svg)

[AWS](https://grafana.com/integrations/cloud-monitoring-aws/?plcmt=solutions-nav)

![Image 35: kafka logo](https://grafana.com/static/img/logos/kafka.svg)

[Kafka](https://grafana.com/integrations/kafka/monitor/?plcmt=solutions-nav)

![Image 36: jenkins logo](https://grafana.com/static/img/logos/jenkins-logo.svg)

[Jenkins](https://grafana.com/integrations/jenkins/monitor/?plcmt=solutions-nav)

![Image 37: rabbitmq logo](https://grafana.com/media/solutions/rabbitmq-monitor/rabbitmq-icon.png)

[RabbitMQ](https://grafana.com/integrations/rabbitmq/monitor/?plcmt=solutions-nav)

![Image 38: mongodb logo](https://grafana.com/media/images/logos/logo-mongodb.svg)

[MongoDB](https://grafana.com/integrations/mongodb/monitor/?plcmt=solutions-nav)

![Image 39: microsoft azure observability logo](https://grafana.com/media/solutions/azure-metrics-monitor/microsoft-azure-icon.svg)

[Microsoft Azure](https://grafana.com/integrations/cloud-monitoring-microsoft-azure/?plcmt=solutions-nav)

![Image 40: google cloud observability with grafana cloud logo](https://grafana.com/media/images/logos/google-cloud-logo-60x48.svg)

[Google Cloud](https://grafana.com/integrations/cloud-monitoring-google-cloud/?plcmt=solutions-nav)

[All monitoring integrations](https://grafana.com/integrations/monitoring/?plcmt=nav-solutions-cta2)

visualize any data

Instantly connect all your data sources to Grafana

![Image 41: mongodb logo](https://grafana.com/media/images/logos/logo-mongodb.svg)

[MongoDB](https://grafana.com/integrations/mongodb/visualize/?plcmt=solutions-nav)

![Image 42: appdynamics logo](https://grafana.com/static/img/logos/appDynamics-white.svg)

[AppDynamics](https://grafana.com/integrations/appdynamics/visualize/?plcmt=solutions-nav)

![Image 43: oracle database logo](https://grafana.com/static/img/logos/oracle-logo.png)

[Oracle](https://grafana.com/integrations/oracle-database/visualize/?plcmt=solutions-nav)

![Image 44: gitlab logo](https://grafana.com/static/img/logos/gitlab.svg)

[GitLab](https://grafana.com/integrations/gitlab/visualize/?plcmt=solutions-nav)

![Image 45: jira logo](https://grafana.com/static/img/diagram/jira-small.svg)

[Jira](https://grafana.com/integrations/jira/visualize/?plcmt=solutions-nav)

![Image 46: salesforce logo](https://grafana.com/static/img/logos/salesforce.com_logo.svg)

[Salesforce](https://grafana.com/integrations/salesforce/visualize/?plcmt=solutions-nav)

![Image 47: splunk logo](https://grafana.com/static/img/logos/splunk-menu.svg)

[Splunk](https://grafana.com/integrations/splunk/visualize/?plcmt=solutions-nav)

![Image 48: datadog logo](https://grafana.com/static/img/logos/icon-datadog.svg)

[Datadog](https://grafana.com/integrations/datadog/visualize/?plcmt=solutions-nav)

![Image 49: new relic logo](https://grafana.com/static/img/logos/newrelic.svg)

[New Relic](https://grafana.com/integrations/new-relic/visualize/?plcmt=solutions-nav)

![Image 50: snowflake logo](https://grafana.com/static/img/logos/snowflake-logo-lg.png)

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

![Image 51: Grafana Cloud](https://grafana.com/media/menus/products/grafana-menu-icon-grafana-cloud.svg)

[Grafana Cloud overview](https://grafana.com/products/cloud/?plcmt=products-nav)

LGTM+ Stack

[![Image 52: Grafana Cloud Logs](https://grafana.com/media/menus/products/grafana-menu-icon-logs.svg) Logs](https://grafana.com/products/cloud/logs/?plcmt=products-nav "powered by Grafana Loki")[![Image 53: Grafana](https://grafana.com/media/menus/products/grafana-menu-icon.svg) Grafana](https://grafana.com/grafana/?plcmt=products-nav "for visualization")[![Image 54: Grafana Cloud Traces](https://grafana.com/media/menus/products/grafana-menu-icon-traces.svg) Traces](https://grafana.com/products/cloud/traces/?plcmt=products-nav "powered by Grafana Tempo")[![Image 55: Grafana Cloud Metrics](https://grafana.com/media/menus/products/grafana-menu-icon-metrics.svg) Metrics](https://grafana.com/products/cloud/metrics/?plcmt=products-nav "powered by Grafana Mimir and Prometheus")

Key Capabilities

[![Image 56: AI/ML](https://grafana.com/media/menus/products/grafana-menu-icon-ai-ml.svg) AI/ML insights](https://grafana.com/products/cloud/ai-tools-for-observability/?plcmt=products-nav "Identify anomalies and reduce toil")[![Image 57: Grafana Cloud Asserts](https://grafana.com/media/menus/products/grafana-menu-icon-asserts-v1.svg) Contextual root cause analysis](https://grafana.com/products/cloud/asserts/?plcmt=products-nav "Automated anomaly correlation")[![Image 58: Grafana SLO](https://grafana.com/media/menus/products/grafana-menu-icon-slo.svg) SLO management](https://grafana.com/products/cloud/slo/?plcmt=products-nav "Create SLOs and error budget alerts")[![Image 59: Grafana Alerting](https://grafana.com/media/menus/products/grafana-menu-icon-alerting.svg) Alerting](https://grafana.com/products/cloud/alerting/?plcmt=products-nav "Trigger alerts from any data source")[![Image 60: Plugins](https://grafana.com/media/menus/products/grafana-menu-icon-plugins.svg) Plugins](https://grafana.com/grafana/plugins/?plcmt=products-nav "Connect Grafana to data sources, apps, and more")

Observability Solutions

[![Image 61: Application Observability](https://grafana.com/media/menus/products/grafana-menu-icon-app-o11y.svg) Application Observability](https://grafana.com/products/cloud/application-observability/?plcmt=products-nav "Monitor application performance")[![Image 62: Infrastructure Observability](https://grafana.com/media/menus/products/grafana-menu-icon-infra-o11y.svg) Infrastructure observability](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/?plcmt=products-nav "Ensure infrastructure health and performance")

Testing

[![Image 63: Grafana Cloud k6](https://grafana.com/media/menus/products/grafana-menu-icon-k6.svg) Performance testing](https://grafana.com/products/cloud/k6/?plcmt=products-nav "Powered by Grafana k6")[![Image 64: Synthetic Monitoring](https://grafana.com/media/menus/products/grafana-menu-icon-synthetic-monitoring.svg) Synthetic Monitoring](https://grafana.com/products/cloud/synthetic-monitoring/?plcmt=products-nav "powered by Grafana k6")

IRM

[![Image 65: Incident](https://grafana.com/media/menus/products/grafana-menu-icon-incident.svg) Incident response](https://grafana.com/products/cloud/incident/?plcmt=products-nav "Routine task automation for incidents")[![Image 66: OnCall](https://grafana.com/media/menus/products/grafana-menu-icon-oncall.svg) On-call management](https://grafana.com/products/cloud/oncall/?plcmt=products-nav "Flexible on-call management")

The actually useful free plan

Grafana Cloud Free Tier

![Image 67: check](https://grafana.com/media/images/icons/grafana-icon-bullet-light-green.svg)
10k series Prometheus metrics

![Image 68: check](https://grafana.com/media/images/icons/grafana-icon-bullet-light-green.svg)
50GB logs, 50GB traces, 50GB profiles

![Image 69: check](https://grafana.com/media/images/icons/grafana-icon-bullet-light-green.svg)
500VUh k6 testing

![Image 70: check](https://grafana.com/media/images/icons/grafana-icon-bullet-light-green.svg)
20+ Enterprise data source plugins

![Image 71: check](https://grafana.com/media/images/icons/grafana-icon-bullet-light-green.svg)
100+ pre-built solutions

![Image 72: check](https://grafana.com/media/images/icons/grafana-icon-bullet-light-green.svg)
3 active AI users

[Create account](https://grafana.com/auth/sign-up/create-user/?plcmt=products-nav)

[![Image 73: Grafana Cloud Logs](https://grafana.com/media/menus/products/grafana-menu-icon-logs.svg) Grafana Loki Multi-tenant log aggregation system](https://grafana.com/oss/loki/?plcmt=oss-nav)[![Image 74: Grafana](https://grafana.com/media/menus/products/grafana-menu-icon.svg) Grafana Query, visualize, and alert on data](https://grafana.com/oss/grafana/?plcmt=oss-nav)[![Image 75: Grafana Cloud Traces](https://grafana.com/media/menus/products/grafana-menu-icon-traces.svg) Grafana Tempo High-scale distributed tracing backend](https://grafana.com/oss/tempo/?plcmt=oss-nav)[![Image 76: Grafana Cloud Metrics](https://grafana.com/media/menus/products/grafana-menu-icon-metrics.svg) Grafana Mimir Scalable and performant metrics backend](https://grafana.com/oss/mimir/?plcmt=oss-nav)

[![Image 77: Grafana Cloud Profiles](https://grafana.com/media/menus/products/grafana-menu-icon-profiles.svg) Grafana Pyroscope Scalable continuous profiling backend](https://grafana.com/oss/pyroscope/?plcmt=oss-nav)[![Image 78](https://grafana.com/static/img/logos/beyla-logo.svg) Grafana Beyla eBPF auto-instrumentation](https://grafana.com/oss/beyla-ebpf/?plcmt=oss-nav)[![Image 79: Frontend Observability](https://grafana.com/media/menus/products/grafana-menu-icon-faro.svg) Grafana Faro Frontend application observability web SDK](https://grafana.com/oss/faro/?plcmt=oss-nav)[![Image 80: Grafana Alloy](https://grafana.com/media/oss/alloy/alloy-logo.svg) Grafana Alloy OpenTelemetry Collector distribution with Prometheus pipelines](https://grafana.com/oss/alloy-opentelemetry-collector/?plcmt=oss-nav)

[![Image 81: Grafana Cloud k6](https://grafana.com/media/menus/products/grafana-menu-icon-k6.svg) Grafana k6 Load testing for engineering teams](https://grafana.com/oss/k6/?plcmt=oss-nav)[![Image 82: Prometheus](https://grafana.com/static/img/menu/prometheus.svg) Prometheus Monitor Kubernetes and cloud native](https://grafana.com/oss/prometheus/?plcmt=oss-nav)[![Image 83: OpenTelemetry](https://grafana.com/static/img/menu/opentelemetry.svg) OpenTelemetry Instrument and collect telemetry data](https://grafana.com/oss/opentelemetry/?plcmt=oss-nav)[![Image 84: Graphite](https://grafana.com/static/img/menu/graphite.svg) Graphite Scalable monitoring for time series data](https://grafana.com/oss/graphite/?plcmt=oss-nav)[](https://grafana.com/oss/?plcmt=oss-nav)

[](https://grafana.com/oss/?plcmt=oss-nav)[All](https://grafana.com/oss/?plcmt=oss-nav)

Community resources

[Dashboard templates Try out and share prebuilt visualizations](https://grafana.com/grafana/dashboards/?plcmt=oss-nav)[Prometheus exporters Get your metrics into Prometheus quickly](https://grafana.com/oss/prometheus/exporters/?plcmt=oss-nav)

end-to-end integrations

Opinionated integrations that help you get there easier and faster

[![Image 85: Kubernetes Monitoring](https://grafana.com/static/img/logos/logo-kubernetes.svg) Kubernetes Monitoring Get K8s health, performance, and cost monitoring from cluster to container](https://grafana.com/solutions/kubernetes/?plcmt=solutions-nav)[![Image 86: Application Observability](https://grafana.com/media/menus/products/grafana-menu-icon-app-o11y.svg) Application Observability Monitor application performance](https://grafana.com/products/cloud/application-observability/?plcmt=solutions-nav)[![Image 87: Frontend Observability](https://grafana.com/media/menus/products/grafana-menu-icon-faro.svg) Frontend Observability Gain real user monitoring insights](https://grafana.com/products/cloud/frontend-observability-for-real-user-monitoring/?plcmt=solutions-nav)[![Image 88: Incident Response & Management](https://grafana.com/static/img/menu/incident-icon.svg) Incident Response & Management Detect and respond to incidents with a simplified workflow](https://grafana.com/products/cloud/irm/?plcmt=solutions-nav)

monitor infrastructure

Out-of-the-box KPIs, dashboards, and alerts for observability

[![Image 89: linux server logo](https://grafana.com/static/img/logos/logo-linux.svg)Linux](https://grafana.com/integrations/linux-node/monitor/?plcmt=solutions-nav)

[![Image 90: windows logo](https://grafana.com/media/solutions/windows-monitor/windows-icon.png)Windows](https://grafana.com/integrations/windows/monitor/?plcmt=solutions-nav)

[![Image 91: docker logo](https://grafana.com/static/img/logos/icon-docker.svg)Docker](https://grafana.com/integrations/docker/monitor/?plcmt=solutions-nav)

[![Image 92: postgresql logo](https://grafana.com/static/img/logos/postgresql_elephant_icon.svg)Postgres](https://grafana.com/integrations/postgresql/monitor/?plcmt=solutions-nav)

[![Image 93: mysql logo](https://grafana.com/static/img/logos/mysql_logo_menu.svg)MySQL](https://grafana.com/integrations/mysql/monitor/?plcmt=solutions-nav)

[![Image 94: aws logo](https://grafana.com/media/images/logos/aws-logo-light.svg)AWS](https://grafana.com/integrations/cloud-monitoring-aws/?plcmt=solutions-nav)

[![Image 95: kafka logo](https://grafana.com/static/img/logos/kafka.svg)Kafka](https://grafana.com/integrations/kafka/monitor/?plcmt=solutions-nav)

[![Image 96: jenkins logo](https://grafana.com/static/img/logos/jenkins-logo.svg)Jenkins](https://grafana.com/integrations/jenkins/monitor/?plcmt=solutions-nav)

[![Image 97: rabbitmq logo](https://grafana.com/media/solutions/rabbitmq-monitor/rabbitmq-icon.png)RabbitMQ](https://grafana.com/integrations/rabbitmq/monitor/?plcmt=solutions-nav)

[![Image 98: mongodb logo](https://grafana.com/media/images/logos/logo-mongodb.svg)MongoDB](https://grafana.com/integrations/mongodb/monitor/?plcmt=solutions-nav)

[![Image 99: microsoft azure observability logo](https://grafana.com/media/solutions/azure-metrics-monitor/microsoft-azure-icon.svg)Microsoft Azure](https://grafana.com/integrations/cloud-monitoring-microsoft-azure/?plcmt=solutions-nav)

[![Image 100: google cloud observability with grafana cloud logo](https://grafana.com/media/images/logos/google-cloud-logo-60x48.svg)Google Cloud](https://grafana.com/integrations/cloud-monitoring-google-cloud/?plcmt=solutions-nav)

visualize any data

Instantly connect all your data sources to Grafana

[![Image 101: mongodb logo](https://grafana.com/media/images/logos/logo-mongodb.svg)MongoDB](https://grafana.com/integrations/mongodb/visualize/?plcmt=solutions-nav)

[![Image 102: appdynamics logo](https://grafana.com/static/img/logos/appDynamics-white.svg)AppDynamics](https://grafana.com/integrations/appdynamics/visualize/?plcmt=solutions-nav)

[![Image 103: oracle database logo](https://grafana.com/static/img/logos/oracle-logo.png)Oracle](https://grafana.com/integrations/oracle-database/visualize/?plcmt=solutions-nav)

[![Image 104: gitlab logo](https://grafana.com/static/img/logos/gitlab.svg)GitLab](https://grafana.com/integrations/gitlab/visualize/?plcmt=solutions-nav)

[![Image 105: jira logo](https://grafana.com/static/img/diagram/jira-small.svg)Jira](https://grafana.com/integrations/jira/visualize/?plcmt=solutions-nav)

[![Image 106: salesforce logo](https://grafana.com/static/img/logos/salesforce.com_logo.svg)Salesforce](https://grafana.com/integrations/salesforce/visualize/?plcmt=solutions-nav)

[![Image 107: splunk logo](https://grafana.com/static/img/logos/splunk-menu.svg)Splunk](https://grafana.com/integrations/splunk/visualize/?plcmt=solutions-nav)

[![Image 108: datadog logo](https://grafana.com/static/img/logos/icon-datadog.svg)Datadog](https://grafana.com/integrations/datadog/visualize/?plcmt=solutions-nav)

[![Image 109: new relic logo](https://grafana.com/static/img/logos/newrelic.svg)New Relic](https://grafana.com/integrations/new-relic/visualize/?plcmt=solutions-nav)

[![Image 110: snowflake logo](https://grafana.com/static/img/logos/snowflake-logo-lg.png)Snowflake](https://grafana.com/integrations/snowflake/visualize/?plcmt=solutions-nav)

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

[![Image 111: Getting started with grafana LGTM stack](https://grafana.com/static/assets/featured/getting-started-with-grafana-lgtm-stack-amer_featured.png?w=500)](https://grafana.com/go/webinar/getting-started-with-grafana-lgtm-stack/?plcmt=learn-nav-featured?plcmt=learn-nav)

Getting started with managing your metrics, logs, and traces using Grafana

Learn how to unify, correlate, and visualize data with dashboards using Grafana.

[Learn more →](https://grafana.com/go/webinar/getting-started-with-grafana-lgtm-stack/?plcmt=learn-nav-featured)

 Site search  Ask Grot AI

[Try using ![Image 112: Grot AI](https://grafana.com/static/img/grot-chat.svg)**Grot AI** for this query ->](https://grafana.com/grot/?chat=&from=/search)

All

Docs

[](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/)

[View all results](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/)

No results.

There was an error with your request.

![Image 113: close nav](https://grafana.com/static/assets/img/icons/grafana-icon-mobile-nav-close-white.svg)![Image 114: close nav](https://grafana.com/static/assets/img/icons/grafana-icon-mobile-nav-close-white.svg)![Image 115: open nav](https://grafana.com/static/assets/img/icons/grafana-icon-mobile-nav-open-white.svg)

Kubernetes Monitoring Helm tutorial

![Image 116: close table of contents](https://grafana.com/static/assets/img/icons/grafana-icon-mobile-toc-close-white.svg)![Image 117: open table of contents](https://grafana.com/static/assets/img/icons/grafana-icon-mobile-toc-open-white.svg)![Image 118: open table of contents](https://grafana.com/static/assets/img/icons/grafana-icon-mobile-toc-open-white.svg)

![Image 119](https://grafana.com/static/assets/img/icons/grafana-icon-docs-search.svg)

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

[Documentation](https://grafana.com/docs/)![Image 120: breadcrumb arrow](https://grafana.com/static/assets/img/icons/grafana-icon-breadcrumb-arrow-gray.svg)[Grafana Loki](https://grafana.com/docs/loki/latest/)![Image 121: breadcrumb arrow](https://grafana.com/static/assets/img/icons/grafana-icon-breadcrumb-arrow-gray.svg)[Send data](https://grafana.com/docs/loki/latest/send-data/)![Image 122: breadcrumb arrow](https://grafana.com/static/assets/img/icons/grafana-icon-breadcrumb-arrow-gray.svg)Kubernetes Monitoring Helm

Open source 

Kubernetes Monitoring Helm tutorial[](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#kubernetes-monitoring-helm-tutorial)
==============================================================================================================================================

One of the primary use cases for Loki is to collect and store logs from your [Kubernetes cluster](https://kubernetes.io/docs/concepts/overview/). These logs fall into three categories:

1.   [**Pod logs**](https://kubernetes.io/docs/concepts/cluster-administration/logging/#basic-logging-in-kubernetes): Logs generated by pods running in your cluster.
2.   [**Kubernetes Events**](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/event-v1/): Logs generated by the Kubernetes API server.
3.   [**Node logs**](https://kubernetes.io/docs/concepts/cluster-administration/logging/#using-a-node-logging-agent): Logs generated by the nodes in your cluster.

[![Image 123: Scraping Kubernetes Logs](https://grafana.com/media/docs/loki/loki-k8s-logs.png) Scraping Kubernetes Logs](https://grafana.com/media/docs/loki/loki-k8s-logs.png)
In this tutorial, we will deploy [Loki](https://grafana.com/docs/loki/latest/get-started/overview/) and the [Kubernetes Monitoring Helm chart](https://grafana.com/docs/grafana-cloud/monitor-infrastructure/kubernetes-monitoring/) to collect two of these log types: Pod logs and Kubernetes events. We will also deploy [Grafana](https://grafana.com/docs/grafana/latest/) to visualize these logs.

Things to know[](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#things-to-know)
----------------------------------------------------------------------------------------------------

Before you begin, here are some things you should know:

*   **Loki**: Loki can run in a single binary mode or as a distributed system. In this tutorial, we will deploy Loki as a single binary, otherwise known as monolithic mode. Loki can be vertically scaled in this mode depending on the number of logs you are collecting. Grafana Labs recommends running Loki in a distributed/microservice mode for production use cases to monitor high volumes of logs.
*   **Deployment**: You will deploy Loki, Grafana, and Alloy (as part of the Kubernetes Monitoring Helm chart) in the `meta` namespace of your Kubernetes cluster. Make sure you have the necessary permissions to create resources in this namespace. These pods will also require resources to run, so consider the amount of capacity your nodes have available. It also possible to just deploy the Kubernetes monitoring Helm chart (since it has a minimal resource footprint) within your cluster and write logs to an external Loki instance or Grafana Cloud.
*   **Storage**: In this tutorial, Loki will use the default object storage backend provided in the Loki Helm chart; [MinIO](https://min.io/docs/minio/kubernetes/upstream/index.html). You should migrate to a more production-ready storage backend like [S3](https://aws.amazon.com/s3/getting-started/), [GCS](https://cloud.google.com/storage/docs), [Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/) or a MinIO Cluster for production use cases.

Prerequisites[](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#prerequisites)
--------------------------------------------------------------------------------------------------

Before you begin, you will need the following:

*   A Kubernetes cluster running version `1.23` or later.
*   [kubectl](https://kubernetes.io/docs/tasks/tools/) installed on your local machine.
*   [Helm](https://helm.sh/docs/intro/install/) installed on your local machine.

> Tip
> 
> 
> Alternatively, you can try out this example in our interactive learning environment: [Kubernetes Monitoring with Loki](https://killercoda.com/grafana-labs/course/loki/k8s-monitoring-helm).
> 
> 
> It’s a fully configured environment with all the dependencies already installed.
> 
> 
> ![Image 125: Interactive](https://grafana.com/media/docs/loki/loki-ile.svg)
> 
> 
> Provide feedback, report bugs, and raise issues in the [Grafana Killercoda repository](https://github.com/grafana/killercoda).

Create the `meta` and `prod` namespaces[](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#create-the-meta-and-prod-namespaces)
--------------------------------------------------------------------------------------------------------------------------------------------------

The K8s Monitoring Helm chart will monitor two namespaces: `meta` and `prod`:

*   `meta` namespace: This namespace will be used to deploy Loki, Grafana, and Alloy.
*   `prod` namespace: This namespace will be used to deploy the sample application that will generate logs.

Create the `meta` and `prod` namespaces by running the following command:

Bash![Image 126: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy

```bash
kubectl create namespace meta && kubectl create namespace prod
```

Add the Grafana Helm repository[](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#add-the-grafana-helm-repository)
--------------------------------------------------------------------------------------------------------------------------------------

All three Helm charts (Loki, Grafana, and the Kubernetes Monitoring Helm) are available in the Grafana Helm repository. Add the Grafana Helm repository by running the following command:

Bash![Image 127: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy

```bash
helm repo add grafana https://grafana.github.io/helm-charts && helm repo update
```

As well as adding the repo to your local helm list, you should also run `helm repo update` to ensure you have the latest version of the charts.

Clone the tutorial repository[](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#clone-the-tutorial-repository)
----------------------------------------------------------------------------------------------------------------------------------

Clone the tutorial repository by running the following command:

Bash![Image 128: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy

```bash
git clone https://github.com/grafana/alloy-scenarios.git
```

Then change directories to the `alloy-scenarios/k8s/logs` directory:

Bash![Image 129: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy

```bash
cd alloy-scenarios/k8s/logs
```

**The rest of this tutorial assumes you are in the `alloy-scenarios/k8s/logs` directory.**

Deploy Loki[](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#deploy-loki)
----------------------------------------------------------------------------------------------

Grafana Loki will be used to store our collected logs. In this tutorial we will deploy Loki with a minimal footprint and use the default storage backend provided by the Loki Helm chart, MinIO.

To deploy Loki run the following command:

Bash![Image 130: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy

```bash
helm install --values loki-values.yml loki grafana/loki -n meta
```

This command will deploy Loki in the `meta` namespace. The command also includes a `values` file that specifies the configuration for Loki. For more details on how to configure the Loki Helm chart refer to the Loki Helm [documentation](https://grafana.com/docs/loki/latest/setup/install/helm/).

Deploy Grafana[](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#deploy-grafana)
----------------------------------------------------------------------------------------------------

Next we will deploy Grafana to the `meta` namespace. You will use Grafana to visualize the logs stored in Loki. To deploy Grafana run the following command:

Bash![Image 131: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy

```bash
helm install --values grafana-values.yml grafana grafana/grafana --namespace meta
```

As before, the command also includes a `values` file that specifies the configuration for Grafana. There are two important configuration attributes to take note of:

1.   `adminUser` and `adminPassword`: These are the credentials you will use to log in to Grafana. The values are `admin` and `adminadminadmin` respectively. The recommended practice is to either use a Kubernetes secret or allow Grafana to generate a password for you. For more details on how to configure the Grafana Helm chart, refer to the Grafana Helm [documentation](https://grafana.com/docs/grafana/latest/installation/helm/).

2.   `datasources`: This section of the configuration lets you define the data sources that Grafana should use. In this tutorial, you will define a Loki data source. The data source is defined as follows:

YAML![Image 132: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy  ```yaml
datasources:
   datasources.yaml:
         apiVersion: 1
         datasources:
         - name: Loki
           type: loki
           access: proxy
           orgId: 1
           url: http://loki-gateway.meta.svc.cluster.local:80
           basicAuth: false
           isDefault: false
           version: 1
           editable: false
```  

This configuration defines a data source named `Loki` that Grafana will use to query logs stored in Loki. The `url` attribute specifies the URL of the Loki gateway. The Loki gateway is a service that sits in front of the Loki API and provides a single endpoint for ingesting and querying logs. The URL is in the format `http://loki-gateway.<NAMESPACE>.svc.cluster.local:80`. The `loki-gateway` service is created by the Loki Helm chart and is used to query logs stored in Loki. **If you choose to deploy Loki in a different namespace or with a different name, you will need to update the `url` attribute accordingly.**

Deploy the Kubernetes Monitoring Helm chart[](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#deploy-the-kubernetes-monitoring-helm-chart)
--------------------------------------------------------------------------------------------------------------------------------------------------------------

The Kubernetes Monitoring Helm chart is used for gathering, scraping, and forwarding Kubernetes telemetry data to a Grafana stack. This includes the ability to collect metrics, logs, traces, and continuous profiling data. The scope of this tutorial is to deploy the Kubernetes Monitoring Helm chart to collect pod logs and Kubernetes events.

To deploy the Kubernetes Monitoring Helm chart run the following command:

Bash![Image 133: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy

```bash
helm install --values ./k8s-monitoring-values.yml k8s grafana/k8s-monitoring -n meta
```

Within the configuration file `k8s-monitoring-values.yml` we have defined the following:

YAML![Image 134: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy

Expand code

```yaml
---
cluster:
  name: meta-monitoring-tutorial

destinations:
  - name: loki
    type: loki
    url: http://loki-gateway.meta.svc.cluster.local/loki/api/v1/push

clusterEvents:
  enabled: true
  collector: alloy-logs
  namespaces:
    - meta
    - prod

nodeLogs:
  enabled: false

podLogs:
  enabled: true
  gatherMethod: kubernetesApi
  collector: alloy-logs
  labelsToKeep: ["app_kubernetes_io_name","container","instance","job","level","namespace","service_name","service_namespace","deployment_environment","deployment_environment_name"]
  structuredMetadata:
    pod: pod  # Set structured metadata "pod" from label "pod"
  namespaces:
    - meta
    - prod

# Collectors
alloy-singleton:
  enabled: false

alloy-metrics:
  enabled: false

alloy-logs:
  enabled: true
  # Required when using the Kubernetes API to pod logs
  alloy:
    mounts:
      varlog: false
    clustering:
      enabled: true

alloy-profiles:
  enabled: false

alloy-receiver:
  enabled: false
```

To break down the configuration file:

*   Define the cluster name as `meta-monitoring-tutorial`. This a static label that will be attached to all logs collected by the Kubernetes Monitoring Helm chart.
*   Define a destination named `loki` that will be used to forward logs to Loki. The `url` attribute specifies the URL of the Loki gateway. **If you choose to deploy Loki in a different namespace or in a different location entirely, you will need to update the `url` attribute accordingly.**
*   Enable the collection of cluster events and pod logs:
    *   `collector`: specifies which collector to use to collect logs. In this case, we are using the `alloy-logs` collector.
    *   `labelsToKeep`: specifies the labels to keep when collecting logs. Note this does not drop logs. This is useful when you do not want to apply a high cardanility label. In this case we have removed `pod` from the labels to keep.
    *   `structuredMetadata`: specifies the structured metadata to collect. In this case, we are setting the structured metadata `pod` so we can retain the pod name for querying. Though it does not need to be indexed as a label.zw
    *   `namespaces`: specifies the namespaces to collect logs from. In this case, we are collecting logs from the `meta` and `prod` namespaces.

*   Disable the collection of node logs for the purpose of this tutorial as it requires the mounting of `/var/log/journal`. This is out of scope for this tutorial.
*   Lastly, define the role of the collector. The Kubernetes Monitoring Helm chart will deploy only what you need and nothing more. In this case, we are telling the Helm chart to only deploy Alloy with the capability to collect logs. If you need to collect K8s metrics, traces, or continuous profiling data, you can enable the respective collectors.

Accessing Grafana[](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#accessing-grafana)
----------------------------------------------------------------------------------------------------------

To access Grafana, you will need to port-forward the Grafana service to your local machine. To do this, run the following command:

Bash![Image 135: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy

```bash
export POD_NAME=$(kubectl get pods --namespace meta -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=grafana" -o jsonpath="{.items[0].metadata.name}") && \
kubectl --namespace meta port-forward $POD_NAME 3000 --address 0.0.0.0
```

> Tip
> 
> 
> This will make your terminal unusable until you stop the port-forwarding process. To stop the process, press `Ctrl + C`.

This command will port-forward the Grafana service to your local machine on port `3000`.

You can now access Grafana by navigating to [http://localhost:3000](http://localhost:3000/) in your browser. The default credentials are `admin` and `adminadminadmin`.

One of the first places you should visit is Logs Drilldown which lets you automatically visualize and explore your logs without having to write queries: [http://localhost:3000/a/grafana-lokiexplore-app](http://localhost:3000/a/grafana-lokiexplore-app)

[![Image 136: Logs Drilldown view of K8s logs](https://grafana.com/media/docs/loki/k8s-logs-explore-logs.png) Logs Drilldown view of K8s logs](https://grafana.com/media/docs/loki/k8s-logs-explore-logs.png)
(Optional) View the Alloy UI[](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#optional-view-the-alloy-ui)
------------------------------------------------------------------------------------------------------------------------------

The Kubernetes Monitoring Helm chart deploys Grafana Alloy to collect and forward telemetry data from the Kubernetes cluster. The Helm chart is designed to abstract you away from creating an Alloy configuration file. However if you would like to understand the pipeline you can view the Alloy UI. To access the Alloy UI, you will need to port-forward the Alloy service to your local machine. To do this, run the following command:

Bash![Image 138: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy

```bash
export POD_NAME=$(kubectl get pods --namespace meta -l "app.kubernetes.io/name=alloy-logs,app.kubernetes.io/instance=k8s-alloy-logs" -o jsonpath="{.items[0].metadata.name}") && \
kubectl --namespace meta port-forward $POD_NAME 12345 --address 0.0.0.0
```

> Tip
> 
> 
> This will make your terminal unusable until you stop the port-forwarding process. To stop the process, press `Ctrl + C`.

This command will port-forward the Alloy service to your local machine on port `12345`. You can access the Alloy UI by navigating to [http://localhost:12345](http://localhost:12345/) in your browser.

[![Image 139: Grafana Alloy UI](https://grafana.com/media/docs/loki/k8s-logs-alloy-ui.png) Grafana Alloy UI](https://grafana.com/media/docs/loki/k8s-logs-alloy-ui.png)
Adding a sample application to `prod`[](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#adding-a-sample-application-to-prod)
------------------------------------------------------------------------------------------------------------------------------------------------

Finally, lets deploy a sample application to the `prod` namespace that will generate some logs. To deploy the sample application run the following command:

Bash![Image 141: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy

```bash
helm install tempo grafana/tempo-distributed -n prod
```

This will deploy a default version of Grafana Tempo to the `prod` namespace. Tempo is a distributed tracing backend that is used to store and query traces. Normally Tempo would sit alongside Loki and Grafana in the `meta` namespace, but for the purpose of this tutorial, we will pretend this is the primary application generating logs.

Once deployed lets expose Grafana once more:

Bash![Image 142: Copy code to clipboard](https://grafana.com/media/images/icons/icon-copy-small-2.svg)Copy

```bash
export POD_NAME=$(kubectl get pods --namespace meta -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=grafana" -o jsonpath="{.items[0].metadata.name}") && \
kubectl --namespace meta port-forward $POD_NAME 3000 --address 0.0.0.0
```

and navigate to [http://localhost:3000/a/grafana-lokiexplore-app](http://localhost:3000/a/grafana-lokiexplore-app) to view Grafana Tempo logs.

[![Image 143: Label view of Tempo logs](https://grafana.com/media/docs/loki/k8s-logs-tempo.png) Label view of Tempo logs](https://grafana.com/media/docs/loki/k8s-logs-tempo.png)
Conclusion[](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#conclusion)
--------------------------------------------------------------------------------------------

In this tutorial, you learned how to deploy Loki, Grafana, and the Kubernetes Monitoring Helm chart to collect and store logs from a Kubernetes cluster. We have deployed a minimal test version of each of these Helm charts to demonstrate how quickly you can get started with Loki. It is now worth exploring each of these Helm charts in more detail to understand how to scale them to meet your production needs:

*   [Loki Helm chart](https://grafana.com/docs/loki/latest/setup/install/helm/)
*   [Grafana Helm chart](https://grafana.com/docs/grafana/latest/installation/helm/)
*   [Kubernetes Monitoring Helm chart](https://grafana.com/docs/grafana-cloud/monitor-infrastructure/kubernetes-monitoring/)

Was this page helpful?
----------------------

![Image 145: 👎](https://grafana.com/media/images/svg/thumbs-up.svg) Yes![Image 146: 👎](https://grafana.com/media/images/svg/thumbs-up.svg) No

[Suggest an edit in GitHub](https://github.com/grafana/loki/edit/main/docs/sources/send-data/k8s-monitoring-helm/_index.md)[Create a GitHub issue](https://github.com/grafana/loki/issues/new?title=Documentation%20feedback:%20/docs/sources/send-data/k8s-monitoring-helm/_index.md)[Email docs@grafana.com](mailto:docs@grafana.com)[Help and support](https://grafana.com/help/)[Community](https://grafana.com/community/)

Related resources from Grafana Labs
-----------------------------------

Additional helpful documentation, links, and articles:

[![Image 147: video icon](https://grafana.com/static/assets/img/icons/grafana-icon-card-video.svg) Video ![Image 148: Getting started with logging and Grafana Loki](blob:http://localhost/63adff11dad904a1878c568edbadacdf) Getting started with logging and Grafana Loki See a demo of the updated features in Loki, and how to create metrics from logs and alert on your logs with powerful Prometheus-style alerting rules.](https://grafana.com/go/webinar/getting-started-with-logging-and-grafana-loki/?pg=docs-loki-latest-send-data-k8s-monitoring-helm&plcmt=related)[![Image 149: video icon](https://grafana.com/static/assets/img/icons/grafana-icon-card-video.svg) Video ![Image 150: Essential Grafana Loki configuration settings](blob:http://localhost/63adff11dad904a1878c568edbadacdf) Essential Grafana Loki configuration settings This webinar focuses on Grafana Loki configuration including agents Promtail and Docker; the Loki server; and Loki storage for popular backends.](https://grafana.com/go/webinar/logging-with-loki-essential-configuration-settings/?pg=docs-loki-latest-send-data-k8s-monitoring-helm&plcmt=related-2)[![Image 151: webinar icon](https://grafana.com/static/assets/img/icons/grafana-icon-card-webinar.svg) Video ![Image 152: Scaling and securing your logs with Grafana Loki](blob:http://localhost/63adff11dad904a1878c568edbadacdf) Scaling and securing your logs with Grafana Loki This webinar covers the challenges of scaling and securing logs, and how Grafana Cloud Logs powered by Grafana Loki can help, cost-effectively.](https://grafana.com/go/webinar/scaling-and-securing-your-logs-with-grafana-loki/?pg=docs-loki-latest-send-data-k8s-monitoring-helm&plcmt=related-3)

Is this page helpful?

![Image 153: 👎](https://grafana.com/media/images/svg/thumbs-up.svg) Yes![Image 154: 👎](https://grafana.com/media/images/svg/thumbs-up.svg) No

On this page

*   [Things to know](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#things-to-know)
*   [Prerequisites](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#prerequisites)
*   [Create the meta and prod namespaces](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#create-the-meta-and-prod-namespaces)
*   [Add the Grafana Helm repository](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#add-the-grafana-helm-repository)
*   [Clone the tutorial repository](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#clone-the-tutorial-repository)
*   [Deploy Loki](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#deploy-loki)
*   [Deploy Grafana](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#deploy-grafana)
*   [Deploy the Kubernetes Monitoring Helm chart](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#deploy-the-kubernetes-monitoring-helm-chart)
*   [Accessing Grafana](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#accessing-grafana)
*   [(Optional) View the Alloy UI](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#optional-view-the-alloy-ui)
*   [Adding a sample application to prod](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#adding-a-sample-application-to-prod)
*   [Conclusion](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/#conclusion)

Scroll for more

![Image 155: GrafanaCON 2026](https://grafana.com/media/events/grafanacon/2026/banners/logo-gcon2026-vert-banner-dark.svg)

Save the Date!Sign up to get the latest GrafanaCON 2026 updates, agenda drops, and first access to early-bird tickets when they’re first available.

[Sign Up](https://grafana.com/events/grafanacon/)

![Image 156: ObservabilityCON 2025](https://grafana.com/media/events/obscon/2025/logo-obscon25-simple.svg)

7-9 OCT LONDON

Learn how to leverage new AI features and observability tools, attend technical deep dives, & leave with tips for growing your observability strategy.

[Sign up to save the date](https://grafana.com/events/observabilitycon/?tech=target&pg=docs&plcmt=sidebar)

![Image 157](https://grafana.com/media/images/icons/grafana-banner-close-btn-light.svg)

![Image 158: ObservabilityCON 2025](https://grafana.com/media/banners/observabilitycon/2025/logo-ocr2025-banner.svg)

We're coming to the Bay Area FEB 25

[Join Us](https://grafana.com/events/observabilitycon-on-the-road/2025/san-francisco-bay-area/?plcmt=sidebar-banner&pg=docs-loki-latest-send-data-k8s-monitoring-helm&tech=target)

![Image 159: GrafanaCON 2025](https://grafana.com/media/events/grafanacon/2025/logo-gcon2025-banner-vertical.svg)

Bring your crew &

 save up to 20%  Don’t miss out—be the first to dive into Grafana 12, Prometheus 3.0, and our nearly sold-out hands-on labs on Grafana as Code, OpenTelemetry, and more.

[Register](https://grafana.com/events/grafanacon/?tech=target&plcmt=footer-banner&aud=default#register)

![Image 160: orange cloud icon](https://grafana.com/media/banners/images/cloud-banner-dashboards-bg.png)

×

###### The fastest way to get started is with the Grafana Cloud free tier which includes:

*   ![Image 161: checkmark](https://grafana.com/media/banners/images/metrics-log-yellow.svg) 10k metrics 
*   ![Image 162: checkmark](https://grafana.com/media/banners/images/logs-orange.svg) 50GB logs 
*   ![Image 163: checkmark](https://grafana.com/media/banners/images/traces-red.svg) 50GB traces 
*   ![Image 164: checkmark](https://grafana.com/media/banners/images/pink-grafana.svg) 3 active users 
*   ![Image 165: checkmark](https://grafana.com/media/banners/images/retention-purple.svg) 14-day retention 

[Create free account](https://grafana.com/auth/sign-up/create-user?plcmt=sidebar&pg=docs-loki-latest-send-data-k8s-monitoring-helm)

![Image 166: orange cloud icon](https://grafana.com/media/banners/images/cloud-banner-bg-icons.png)

###### The fastest way to get started is with the Grafana Cloud free tier which includes:

*   10k metrics
*    50GB logs
*   50GB traces
*   3 active users
*   14-day rentention

[Start Free](https://grafana.com/auth/sign-up/create-user?plcmt=sidebar&pg=docs-loki-latest-send-data-k8s-monitoring-helm)

![Image 167: Grafana 10](https://grafana.com/media/banners/images/grafana-cloud-logo.svg)

 Introducing 

 Frontend Observability 

 Our hosted service for real user monitoring. Gain precise, end-to-end user insights. 

[Sign up for free](https://grafana.com/auth/sign-up/create-user?tech=target&pg=docs&plcmt=sidebar&aud=non-cloud-frontend-observability-default)[Read the blog](https://grafana.com/blog/2023/05/02/gain-real-user-monitoring-insights-with-grafana-cloud-frontend-observability/?tech=target&pg=docs&plcmt=sidebar&aud=non-cloud-frontend-observability-default)

![Image 168: k6 cloud icon](https://grafana.com/media/products/k6-cloud/k6-sidebar-banner.svg)![Image 169](https://grafana.com/media/products/k6-cloud/k6-sidebar-banner-dark.png?w=500)
The best developer experience for performance testing

[Learn more](https://grafana.com/products/cloud/k6/?pg=docs-loki-latest-send-data-k8s-monitoring-helm&plcmt=sidebar)

![Image 170: k6 cloud icon](https://grafana.com/media/products/k6-cloud/k6-sidebar-banner.svg)![Image 171](https://grafana.com/media/products/k6-cloud/k6-sidebar-banner-dark.png?w=500)
Introducing Grafana Cloud k6, a new offering empowers teams to prevent system failures and deliver fast and reliable applications.

[Learn more](https://grafana.com/products/cloud/k6/?pg=docs-loki-latest-send-data-k8s-monitoring-helm&plcmt=sidebar)

![Image 172: Grafana Cloud Adaptive Metrics](https://grafana.com/media/images/logos/adaptive-metrics-banner-logo-2.svg)
*   Reduce metric cardinality by 30-50%
*   Pay only for metrics you use
*   Centralize control over your data in Grafana Cloud

[Create free account](https://grafana.com/auth/sign-up/create-user?pg=docs-loki-latest-send-data-k8s-monitoring-helm&plcmt=sidebar)[Read the blog post](https://grafana.com/blog/?pg=docs-loki-latest-send-data-k8s-monitoring-helm&plcmt=sidebar)

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

[Ask Grafana Assistant](https://grafana.com/docs/loki/latest/send-data/k8s-monitoring-helm/)
