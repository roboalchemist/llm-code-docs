# Source: https://projectcontour.io/docs/1.33/guides/proxy-proto//

Title: How to Configure PROXY v1/v2 Support

URL Source: https://projectcontour.io/docs/1.33/guides/proxy-proto/

Markdown Content:
How to Configure PROXY v1/v2 Support
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

[main](https://projectcontour.io/docs/main/guides/proxy-proto/)[1.33](https://projectcontour.io/docs/1.33/guides/proxy-proto/)[1.32](https://projectcontour.io/docs/1.32/guides/proxy-proto/)[1.31](https://projectcontour.io/docs/1.31/guides/proxy-proto/)[1.30](https://projectcontour.io/docs/1.30/guides/proxy-proto/)[1.29](https://projectcontour.io/docs/1.29/guides/proxy-proto/)[1.28](https://projectcontour.io/docs/1.28/guides/proxy-proto/)[1.27](https://projectcontour.io/docs/1.27/guides/proxy-proto/)[1.26](https://projectcontour.io/docs/1.26/guides/proxy-proto/)[1.25](https://projectcontour.io/docs/1.25/guides/proxy-proto/)[1.24](https://projectcontour.io/docs/1.24/guides/proxy-proto/)[1.23](https://projectcontour.io/docs/1.23/guides/proxy-proto/)[1.22](https://projectcontour.io/docs/1.22/guides/proxy-proto/)[1.21](https://projectcontour.io/docs/1.21/guides/proxy-proto/)[1.20](https://projectcontour.io/docs/1.20/guides/proxy-proto/)

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

If you deploy Contour as a Deployment or Daemonset, you will likely use a `type: LoadBalancer` Service to request an [external load balancer](https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer) from your hosting provider. If you use the Elastic Load Balancer (ELB) service from Amazon’s EC2, you need to perform a couple of additional steps to enable the [PROXY](http://www.haproxy.org/download/1.8/doc/proxy-protocol.txt) protocol. Here’s why:

External load balancers typically operate in one of two modes: a layer 7 HTTP proxy, or a layer 4 TCP proxy. The former cannot be used to load balance TLS traffic, because your cloud provider attempts HTTP negotiation on port 443. So the latter must be used when Contour handles HTTP and HTTPS traffic.

However this leads to a situation where the remote IP address of the client is reported as the inside address of your cloud provider’s load balancer. To rectify the situation, you can add annotations to your service and flags to your Contour Deployment or DaemonSet to enable the [PROXY](http://www.haproxy.org/download/1.8/doc/proxy-protocol.txt) protocol which forwards the original client IP details to Envoy.

Enable PROXY protocol on your service in GKE
--------------------------------------------

In GKE clusters a `type: LoadBalancer` Service is provisioned as a Network Load Balancer and will forward traffic to your Envoy instances with their client addresses intact. Your services should see the addresses in the `X-Forwarded-For` or `X-Envoy-External-Address` headers without having to enable a PROXY protocol.

Enable PROXY protocol on your service in AWS
--------------------------------------------

To instruct EC2 to place the ELB into `tcp`+`PROXY` mode, add the following annotations to the `contour` Service:

```
apiVersion: v1
kind: Service
metadata:
  annotations:
      service.beta.kubernetes.io/aws-load-balancer-backend-protocol: tcp
      service.beta.kubernetes.io/aws-load-balancer-proxy-protocol: '*'
    name: contour
    namespace: projectcontour
spec:
  type: LoadBalancer
...
```

Enable PROXY protocol support for all Envoy listening ports
-----------------------------------------------------------

```
...
spec:
  containers:
  - image: ghcr.io/projectcontour/contour:<version>
    imagePullPolicy: Always
    name: contour
    command: ["contour"]
    args: ["serve", "--incluster", "--use-proxy-protocol"]
...
```

* [Report Issues](https://github.com/projectcontour/contour/issues/new?body=%2A%2AOn+Page%3A%2A%2A+%5BHow+to+Configure+PROXY+v1%2Fv2+Support%5D%28https%3A%2F%2Fprojectcontour.io%2Fdocs%2F1.33%2Fguides%2Fproxy-proto%2F%29)
* [![Image 7](https://projectcontour.io/img/github-blue.svg) Edit](https://github.com/projectcontour/contour/edit/main/site/content/docs/1.33/guides/proxy-proto.md?description=Signed-off-by%3A+NAME+%3CEMAIL_ADDRESS%3E%0A%0A)

#### On this page

* [Enable PROXY protocol on your service in GKE](https://projectcontour.io/docs/1.33/guides/proxy-proto/#enable-proxy-protocol-on-your-service-in-gke)
* [Enable PROXY protocol on your service in AWS](https://projectcontour.io/docs/1.33/guides/proxy-proto/#enable-proxy-protocol-on-your-service-in-aws)
* [Enable PROXY protocol support for all Envoy listening ports](https://projectcontour.io/docs/1.33/guides/proxy-proto/#enable-proxy-protocol-support-for-all-envoy-listening-ports)

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
