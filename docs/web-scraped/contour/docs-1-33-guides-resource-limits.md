# Source: https://projectcontour.io/docs/1.33/guides/resource-limits//

Title: Envoy Resource Limits

URL Source: https://projectcontour.io/docs/1.33/guides/resource-limits/

Markdown Content:
Contour / Envoy Resource Limits
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

[main](https://projectcontour.io/docs/main/guides/resource-limits/)[1.33](https://projectcontour.io/docs/1.33/guides/resource-limits/)[1.32](https://projectcontour.io/docs/1.32/guides/resource-limits/)[1.31](https://projectcontour.io/docs/1.31/guides/resource-limits/)[1.30](https://projectcontour.io/docs/1.30/guides/resource-limits/)[1.29](https://projectcontour.io/docs/1.29/guides/resource-limits/)[1.28](https://projectcontour.io/docs/1.28/guides/resource-limits/)[1.27](https://projectcontour.io/docs/1.27/guides/resource-limits/)[1.26](https://projectcontour.io/docs/1.26/guides/resource-limits/)[1.25](https://projectcontour.io/docs/1.25/guides/resource-limits/)[1.24](https://projectcontour.io/docs/1.24/guides/resource-limits/)[1.23](https://projectcontour.io/docs/1.23/guides/resource-limits/)[1.22](https://projectcontour.io/docs/1.22/guides/resource-limits/)[1.21](https://projectcontour.io/docs/1.21/guides/resource-limits/)[1.20](https://projectcontour.io/docs/1.20/guides/resource-limits/)

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

Performance Testing Contour / Envoy
-----------------------------------

* Cluster Specs
  * Kubernetes
    * Version: v1.12.6
    * Nodes:
      * 5 Worker Nodes
        * 2 CPUs Per Node
        * 8 GB RAM Per Node

      * 10 GB Network

  * Contour
    * Single Instance
      * 4 Instances of Envoy running in a Daemonset
      * Each instance of Envoy is running with HostNetwork

    * Cluster Network Bandwidth

Having a good understanding of the available bandwidth is key when it comes to analyzing performance. It will give you a sense of how many requests per second you can expect to push through the network you are working with.

Use iperf3 to figure out the bandwidth available between two of the kubernetes nodes. The following will deploy an iperf3 server on one node, and an iperf3 client on another node:

```bash
[ ID] Interval           Transfer     Bandwidth       Retr
[  4]   0.00-60.00  sec  34.7 GBytes  4.96 Gbits/sec  479             sender
[  4]   0.00-60.00  sec  34.7 GBytes  4.96 Gbits/sec                  receiver
```

Memory / CPU usage
------------------

Verify the Memory & CPU usage with varying numbers of services, IngressRoute resources, and traffic load into the cluster.

Test Criteria Contour Envoy
# Svc#Ing RPS CC Memory (MB)CPU% / Core Memory (MB)CPU% / Core
0 0 0 0 10 0 15 0
5k 0 0 0 46 2%15 0%
10k 0 0 0 77 3%205 2%
0 5k 0 0 36 1%230 2%
0 10k 0 0 63 1%10 1%
5k 5k 0 0 244 1%221 1%
10k 10k 0 0 2600 6%430 4%
0 0 30k 600 8 1%17 3%
0 0 100k 10k 10 1%118 14%
0 0 200k 20k 9 1%191 31%
0 0 300k 30k 10 1%225 40%

* [Report Issues](https://github.com/projectcontour/contour/issues/new?body=%2A%2AOn+Page%3A%2A%2A+%5BContour+%2F+Envoy+Resource+Limits%5D%28https%3A%2F%2Fprojectcontour.io%2Fdocs%2F1.33%2Fguides%2Fresource-limits%2F%29)
* [![Image 7](https://projectcontour.io/img/github-blue.svg) Edit](https://github.com/projectcontour/contour/edit/main/site/content/docs/1.33/guides/resource-limits.md?description=Signed-off-by%3A+NAME+%3CEMAIL_ADDRESS%3E%0A%0A)

#### On this page

* [Performance Testing Contour / Envoy](https://projectcontour.io/docs/1.33/guides/resource-limits/#performance-testing-contour--envoy)
* [Memory / CPU usage](https://projectcontour.io/docs/1.33/guides/resource-limits/#memory--cpu-usage)

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
