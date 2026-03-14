# Source: https://projectcontour.io/docs/1.33/guides/deploy-aws-nlb//

Title: Deploying Contour on AWS with NLB

URL Source: https://projectcontour.io/docs/1.33/guides/deploy-aws-nlb/

Markdown Content:
Deploying Contour on AWS with NLB
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

[main](https://projectcontour.io/docs/main/guides/deploy-aws-nlb/)[1.33](https://projectcontour.io/docs/1.33/guides/deploy-aws-nlb/)[1.32](https://projectcontour.io/docs/1.32/guides/deploy-aws-nlb/)[1.31](https://projectcontour.io/docs/1.31/guides/deploy-aws-nlb/)[1.30](https://projectcontour.io/docs/1.30/guides/deploy-aws-nlb/)[1.29](https://projectcontour.io/docs/1.29/guides/deploy-aws-nlb/)[1.28](https://projectcontour.io/docs/1.28/guides/deploy-aws-nlb/)[1.27](https://projectcontour.io/docs/1.27/guides/deploy-aws-nlb/)[1.26](https://projectcontour.io/docs/1.26/guides/deploy-aws-nlb/)[1.25](https://projectcontour.io/docs/1.25/guides/deploy-aws-nlb/)[1.24](https://projectcontour.io/docs/1.24/guides/deploy-aws-nlb/)[1.23](https://projectcontour.io/docs/1.23/guides/deploy-aws-nlb/)[1.22](https://projectcontour.io/docs/1.22/guides/deploy-aws-nlb/)[1.21](https://projectcontour.io/docs/1.21/guides/deploy-aws-nlb/)[1.20](https://projectcontour.io/docs/1.20/guides/deploy-aws-nlb/)

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

This is an advanced deployment guide to configure Contour on AWS with the [Network Load Balancer (NLB)](https://aws.amazon.com/blogs/aws/new-network-load-balancer-effortless-scaling-to-millions-of-requests-per-second/). This configuration has several advantages:

1. NLBs are often cheaper. This is especially true for development. Idle LBs do not cost money.
2. There are no extra network hops. Traffic goes to the NLB, to the node hosting Contour, and then to the target pod.
3. Source IP addresses are retained. Envoy (running as part of Contour) sees the native source IP address and records this with an `X-Forwarded-For` header.

Moving parts
------------

* We run Envoy as a DaemonSet across the cluster and Contour as a deployment
* The Envoy pod runs on host ports 80 and 443 on the node
* Host networking means that traffic hits Envoy without transitioning through any other fancy networking hops
* Contour also binds to 8001 for Envoy->Contour config traffic.

Deploying Contour
-----------------

1. [Clone the Contour repository](https://github.com/projectcontour/contour/tree/release-1.33) and cd into the repo
2. Edit the Envoy service (`02-service-envoy.yaml`) in the `examples/contour` directory:
    *Remove the existing annotation: `service.beta.kubernetes.io/aws-load-balancer-backend-protocol: tcp`
    *   Add the following annotation: `service.beta.kubernetes.io/aws-load-balancer-type: nlb`

3. Run `kubectl apply -f examples/contour`

This creates the `projectcontour` Namespace along with a ServiceAccount, RBAC rules, Contour Deployment and an Envoy DaemonSet. It also creates the NLB based loadbalancer for you.

You can get the address of your NLB via:

```
kubectl get service envoy --namespace=projectcontour -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'
```

Test
----

You can now test your NLB.

1. Install a workload (see the kuard example in the [main deployment guide](https://projectcontour.io/docs/1.33/deploy-options/#testing-your-installation)).
2. Look up the address for your NLB in the AWS console and enter it in your browser.

* Notice that Envoy fills out `X-Forwarded-For`, because it was the first to see the traffic directly from the browser.

* [Report Issues](https://github.com/projectcontour/contour/issues/new?body=%2A%2AOn+Page%3A%2A%2A+%5BDeploying+Contour+on+AWS+with+NLB%5D%28https%3A%2F%2Fprojectcontour.io%2Fdocs%2F1.33%2Fguides%2Fdeploy-aws-nlb%2F%29)
* [![Image 7](https://projectcontour.io/img/github-blue.svg) Edit](https://github.com/projectcontour/contour/edit/main/site/content/docs/1.33/guides/deploy-aws-nlb.md?description=Signed-off-by%3A+NAME+%3CEMAIL_ADDRESS%3E%0A%0A)

#### On this page

* [Moving parts](https://projectcontour.io/docs/1.33/guides/deploy-aws-nlb/#moving-parts)
* [Deploying Contour](https://projectcontour.io/docs/1.33/guides/deploy-aws-nlb/#deploying-contour)
* [Test](https://projectcontour.io/docs/1.33/guides/deploy-aws-nlb/#test)

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
