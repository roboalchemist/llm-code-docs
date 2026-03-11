# Source: https://projectcontour.io/docs/1.33/guides/kind/

Title: Creating a Contour-compatible kind cluster

URL Source: https://projectcontour.io/docs/1.33/guides/kind/

Markdown Content:
Creating a Contour-compatible kind cluster
===============

[![Image 1: Contour logo](https://projectcontour.io/img/Contour.svg)](https://projectcontour.io/)

* [Getting Started](https://projectcontour.io/getting-started/)
* [Documentation](https://projectcontour.io/docs/1.33)
* [Community](https://projectcontour.io/community/)
* [Resources](https://projectcontour.io/resources/)

![Image 2: Mobile nav icon](https://projectcontour.io/img/hamburger.svg)![Image 3: Mobile nav icon](https://projectcontour.io/img/close.svg)

* [Getting Started](https://projectcontour.io/getting-started/)
* [Documentation](https://projectcontour.io/docs/1.33)
* [Community](https://projectcontour.io/community/)
* [Resources](https://projectcontour.io/resources/)

[![Image 4: Twitter logo](https://projectcontour.io/img/twitter.png)Twitter](https://twitter.com/projectcontour)[![Image 5: Slack logo](https://projectcontour.io/img/slack.png)Slack](https://kubernetes.slack.com/?redir=%2Fmessages%2Fcontour)[![Image 6: GitHub logo](https://projectcontour.io/img/github.svg)GitHub](https://github.com/projectcontour/contour)

Documentation
=============

 1.33

[main](https://projectcontour.io/docs/main/guides/kind/)[1.33](https://projectcontour.io/docs/1.33/guides/kind/)[1.32](https://projectcontour.io/docs/1.32/guides/kind/)[1.31](https://projectcontour.io/docs/1.31/guides/kind/)[1.30](https://projectcontour.io/docs/1.30/guides/kind/)[1.29](https://projectcontour.io/docs/1.29/guides/kind/)[1.28](https://projectcontour.io/docs/1.28/guides/kind/)[1.27](https://projectcontour.io/docs/1.27/guides/kind/)[1.26](https://projectcontour.io/docs/1.26/guides/kind/)[1.25](https://projectcontour.io/docs/1.25/guides/kind/)[1.24](https://projectcontour.io/docs/1.24/guides/kind/)[1.23](https://projectcontour.io/docs/1.23/guides/kind/)[1.22](https://projectcontour.io/docs/1.22/guides/kind/)[1.21](https://projectcontour.io/docs/1.21/guides/kind/)[1.20](https://projectcontour.io/docs/1.20/guides/kind/)

Search

#### Introduction

* [Contour Architecture](https://projectcontour.io/docs/1.33/architecture/)
* [Contour Philosophy](https://projectcontour.io/resources/philosophy)

#### Configuration

* [HTTPProxy Fundamentals](https://projectcontour.io/docs/1.33/config/fundamentals/)
* [Gateway API Support](https://projectcontour.io/docs/1.33/config/gateway-api/)
* [Ingress v1 Support](https://projectcontour.io/docs/1.33/config/ingress/)
* [Virtual Hosts](https://projectcontour.io/docs/1.33/config/virtual-hosts/)
* [Inclusion and Delegation](https://projectcontour.io/docs/1.33/config/inclusion-delegation/)
* [TLS Termination](https://projectcontour.io/docs/1.33/config/tls-termination/)
* [Upstream TLS](https://projectcontour.io/docs/1.33/config/upstream-tls/)
* [Request Routing](https://projectcontour.io/docs/1.33/config/request-routing/)
* [External Service Routing](https://projectcontour.io/docs/1.33/config/external-service-routing/)
* [Request Rewriting](https://projectcontour.io/docs/1.33/config/request-rewriting/)
* [CORS](https://projectcontour.io/docs/1.33/config/cors/)
* [Websockets](https://projectcontour.io/docs/1.33/config/websockets/)
* [Upstream Health Checks](https://projectcontour.io/docs/1.33/config/health-checks/)
* [Client Authorization](https://projectcontour.io/docs/1.33/config/client-authorization/)
* [TLS Delegation](https://projectcontour.io/docs/1.33/config/tls-delegation/)
* [Rate Limiting](https://projectcontour.io/docs/1.33/config/rate-limiting/)
* [Access logging](https://projectcontour.io/docs/1.33/config/access-logging/)
* [Cookie Rewriting](https://projectcontour.io/docs/1.33/config/cookie-rewriting/)
* [Overload Manager](https://projectcontour.io/docs/1.33/config/overload-manager/)
* [JWT Verification](https://projectcontour.io/docs/1.33/config/jwt-verification/)
* [IP Filtering](https://projectcontour.io/docs/1.33/config/ip-filtering/)
* [Annotations Reference](https://projectcontour.io/docs/1.33/config/annotations/)
* [Slow Start Mode](https://projectcontour.io/docs/1.33/config/slow-start/)
* [Tracing Support](https://projectcontour.io/docs/1.33/config/tracing/)
* [API Reference](https://projectcontour.io/docs/1.33/config/api/)

#### Deployment

* [Deployment Options](https://projectcontour.io/docs/1.33/deploy-options/)
* [Contour Configuration](https://projectcontour.io/docs/1.33/configuration/)
* [Upgrading Contour](https://projectcontour.io/resources/upgrading)
* [Enabling TLS between Envoy and Contour](https://projectcontour.io/docs/1.33/grpc-tls-howto/)
* [Redeploy Envoy](https://projectcontour.io/docs/1.33/redeploy-envoy/)

#### Guides

* [Deploying Contour on AWS with NLB](https://projectcontour.io/docs/1.33/guides/deploy-aws-nlb//)
* [AWS Network Load Balancer TLS Termination with Contour](https://projectcontour.io/docs/1.33/guides/deploy-aws-tls-nlb//)
* [Deploying HTTPS services with Contour and cert-manager](https://projectcontour.io/docs/1.33/guides/cert-manager//)
* [External Authorization Support](https://projectcontour.io/docs/1.33/guides/external-authorization//)
* [FIPS 140-2 in Contour](https://projectcontour.io/docs/1.33/guides/fips/)
* [Using Gatekeeper with Contour](https://projectcontour.io/docs/1.33/guides/gatekeeper/)
* [Using Gateway API with Contour](https://projectcontour.io/docs/1.33/guides/gateway-api/)
* [Global Rate Limiting](https://projectcontour.io/docs/1.33/guides/global-rate-limiting/)
* [Configuring ingress to gRPC services with Contour](https://projectcontour.io/docs/1.33/guides/grpc/)
* [Health Checking](https://projectcontour.io/docs/1.33/guides/health-checking/)
* [Creating a Contour-compatible kind cluster](https://projectcontour.io/docs/1.33/guides/kind/)
* [Collecting Metrics with Prometheus](https://projectcontour.io/docs/1.33/guides/prometheus//)
* [How to Configure PROXY Protocol v1/v2 Support](https://projectcontour.io/docs/1.33/guides/proxy-proto//)
* [Contour/Envoy Resource Limits](https://projectcontour.io/docs/1.33/guides/resource-limits//)

#### Troubleshooting

* [Troubleshooting Common Proxy Errors](https://projectcontour.io/docs/1.33/troubleshooting/common-proxy-errors/)
* [Envoy Administration Access](https://projectcontour.io/docs/1.33/troubleshooting/envoy-admin-interface/)
* [Contour Debug Logging](https://projectcontour.io/docs/1.33/troubleshooting/contour-debug-log/)
* [Envoy Debug Logging](https://projectcontour.io/docs/1.33/troubleshooting/envoy-debug-log/)
* [Visualize the Contour Graph](https://projectcontour.io/docs/1.33/troubleshooting/contour-graph/)
* [Show Contour xDS Resources](https://projectcontour.io/docs/1.33/troubleshooting/contour-xds-resources/)
* [Profiling Contour](https://projectcontour.io/docs/1.33/troubleshooting/profiling-contour/)
* [Envoy Container Stuck in Unready State](https://projectcontour.io/docs/1.33/troubleshooting/envoy-container-draining/)

#### Resources

* [Support Policy](https://projectcontour.io/resources/support)
* [Compatibility Matrix](https://projectcontour.io/resources/compatibility-matrix)
* [Contour Deprecation Policy](https://projectcontour.io/resources/deprecation-policy)
* [Release Process](https://projectcontour.io/resources/release-process)
* [Frequently Asked Questions](https://projectcontour.io/resources/faq)
* [Tagging](https://projectcontour.io/resources/tagging)
* [Adopters](https://projectcontour.io/resources/adopters)
* [Ecosystem](https://projectcontour.io/resources/ecosystem)

#### Security

* [Threat Model and Security Posture](https://projectcontour.io/resources/security-threat-model)
* [Security Report Process](https://projectcontour.io/resources/security-process)
* [Security Fix Checklist](https://projectcontour.io/resources/security-checklist)

#### Contribute

* [Start Contributing](https://projectcontour.io/docs/1.33/start-contributing/)
* [How We Work](https://projectcontour.io/resources/how-we-work)

This guide walks through creating a kind (Kubernetes in Docker) cluster on your local machine that can be used for developing and testing Contour.

Prerequisites
=============

Download & install Docker and kind:

* Docker [installation information](https://docs.docker.com/desktop/#download-and-install)
* kind [download and install instructions](https://kind.sigs.k8s.io/docs/user/quick-start/)

Kind configuration file
=======================

Create a kind configuration file locally. This file will instruct kind to create a cluster with one control plane node and one worker node, and to map ports 80 and 443 on your local machine to ports 80 and 443 on the worker node container. This will allow us to easily get traffic to Contour/Envoy running inside the kind cluster from our local machine.

Copy the text below into the local yaml file `kind-config.yaml`:

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
- role: worker
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    listenAddress: "0.0.0.0"  
  - containerPort: 443
    hostPort: 443
    listenAddress: "0.0.0.0"
```

Kubernetes cluster using kind
=============================

Create a kind cluster using the config file from above:

```yaml
kind create cluster --config kind-config.yaml
```

Verify the nodes are ready by running:

```yaml
kubectl get nodes
```

You should see 2 nodes listed with status **Ready**:

* kind-control-plane
* kind-worker

Congratulations, you have created your cluster environment. You’re ready to install Contour.

_Note:_ When you are done with the cluster, you can delete it by running:

```yaml
kind delete cluster
```

Next Steps
==========

See [https://projectcontour.io/getting-started/](https://projectcontour.io/getting-started/) for how to install Contour into your kind cluster.

* [Report Issues](https://github.com/projectcontour/contour/issues/new?body=%2A%2AOn+Page%3A%2A%2A+%5BCreating+a+Contour-compatible+kind+cluster%5D%28https%3A%2F%2Fprojectcontour.io%2Fdocs%2F1.33%2Fguides%2Fkind%2F%29)
* [![Image 7](https://projectcontour.io/img/github-blue.svg) Edit](https://github.com/projectcontour/contour/edit/main/site/content/docs/1.33/guides/kind.md?description=Signed-off-by%3A+NAME+%3CEMAIL_ADDRESS%3E%0A%0A)

Ready to try Contour?
---------------------

Read our getting started documentation.

[Getting Started](https://projectcontour.io/getting-started)

* [![Image 8: Twitter logo](https://projectcontour.io/img/twitter.png)Twitter](https://twitter.com/projectcontour)
* [![Image 9: Slack logo](https://projectcontour.io/img/slack.png)#Slack Slack](https://kubernetes.slack.com/messages/contour)
* [![Image 10: GitHub logo](https://projectcontour.io/img/github.svg)GitHub](https://github.com/projectcontour/contour)

[![Image 11: Contour logo](https://projectcontour.io/img/Contour.svg)](https://projectcontour.io/)

© Project Contour Authors

© 2026 [The Linux Foundation](https://linuxfoundation.org/). All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage](https://linuxfoundation.org/trademark-usage) page.
