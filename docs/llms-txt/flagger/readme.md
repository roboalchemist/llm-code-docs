# Source: https://docs.flagger.app/readme.md

# Source: https://docs.flagger.app/main/readme.md

# Introduction

[Flagger](https://github.com/fluxcd/flagger) is a progressive delivery tool that automates the release process for applications running on Kubernetes. It reduces the risk of introducing a new software version in production by gradually shifting traffic to the new version while measuring metrics and running conformance tests.

Flagger implements several deployment strategies (Canary releases, A/B testing, Blue/Green mirroring) using a service mesh or an ingress controller for traffic routing. For release analysis, Flagger can query Prometheus, InfluxDB, Datadog, New Relic, CloudWatch, Stackdriver or Graphite and for alerting it uses Slack, MS Teams, Discord and Rocket.

![Flagger overview diagram](https://raw.githubusercontent.com/fluxcd/flagger/main/docs/diagrams/flagger-overview.png)

Flagger can be configured with Kubernetes custom resources and is compatible with any CI/CD solutions made for Kubernetes. Since Flagger is declarative and reacts to Kubernetes events, it can be used in **GitOps** pipelines together with tools like [Flux CD](https://docs.flagger.app/main/install/flagger-install-with-flux).

Flagger is a [Cloud Native Computing Foundation](https://cncf.io/) graduated project and part of [Flux](https://fluxcd.io) family of GitOps tools.

## Getting started

To get started with Flagger, choose one of the supported routing providers and [install](https://docs.flagger.app/main/install/flagger-install-with-flux) Flagger with Flux CD.

After installing Flagger, you can follow one of these tutorials to get started:

**Service mesh tutorials**

* [Gateway API](https://docs.flagger.app/main/tutorials/gatewayapi-progressive-delivery)
* [Istio](https://docs.flagger.app/main/tutorials/istio-progressive-delivery)
* [Linkerd](https://docs.flagger.app/main/tutorials/linkerd-progressive-delivery)
* [Kuma](https://docs.flagger.app/main/tutorials/kuma-progressive-delivery)

**Ingress controller tutorials**

* [Contour](https://docs.flagger.app/main/tutorials/contour-progressive-delivery)
* [Gloo](https://docs.flagger.app/main/tutorials/gloo-progressive-delivery)
* [NGINX Ingress](https://docs.flagger.app/main/tutorials/nginx-progressive-delivery)
* [Skipper Ingress](https://docs.flagger.app/main/tutorials/skipper-progressive-delivery)
* [Traefik](https://docs.flagger.app/main/tutorials/traefik-progressive-delivery)
* [Apache APISIX](https://docs.flagger.app/main/tutorials/apisix-progressive-delivery)

The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage page](https://www.linuxfoundation.org/legal/trademark-usage).
