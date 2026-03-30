# Source: https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/llms.txt

# Elastic Load Balancing Classic Load Balancers

> Use Elastic Load Balancing to distribute your incoming application traffic across multiple EC2 instances.

- [What is a Classic Load Balancer?](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/introduction.html)
- [Quotas](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-limits.html)
- [Document history](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/DocumentHistory.html)

## [Internet-facing load balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-internet-facing-load-balancers.html)

- [Create an internet-facing load balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-getting-started.html): Get started with basic load balancing tasks using a Classic Load Balancer with Elastic Load Balancing.


## [Internal load balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-internal-load-balancers.html)

- [Create an internal load balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-create-internal-load-balancer.html): Create a Classic Load Balancer that is internal to your VPC.


## [Configure your load balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-configure-load-balancer.html)

- [Idle connection timeout](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-idle-timeout.html): Configure the idle connection timeout for your Classic Load Balancer.
- [Cross-zone load balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html): Enable or disable cross-zone load balancing for your Classic Load Balancer.
- [Connection draining](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html): Learn about the connection draining setting for your Classic Load Balancer.
- [Sticky sessions](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html): Create a sticky session, also known as session affinity, to bind a user's session to a specific application.
- [Desync mitigation mode](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-desync-mitigation-mode.html): Desync mitigation mode protects your application from issues due to HTTP Desync.
- [Proxy protocol](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-proxy-protocol.html): Enable or disable support for proxy protocol, a human-readable header, for your Classic Load Balancer.
- [Tags](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/add-remove-tags.html): Learn how to use tags to help you categorize your Classic Load Balancers in different ways, for example, by purpose, owner, or environment.
- [Subnets and zones](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-manage-subnets.html): Learn how to add or remove subnets for your Classic Load Balancer.
- [Security groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-vpc-security-groups.html): Control the traffic allowed to reach your Classic Load Balancer using security groups.
- [Network ACLs](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-vpc-network-acls.html): Control the traffic allowed to reach your Classic Load Balancer using network ACLs.
- [Custom domain name](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/using-domain-names-with-elb.html): Configure a custom domain name for your Classic Load Balancer that is easy for customers to remember.


## [Listeners](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html)

- [Listener configurations](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/using-elb-listenerconfig-quickref.html): A summary of the listener settings you can use to configure your Classic Load Balancer.
- [X-forwarded headers](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/x-forwarded-headers.html): Learn about the X-Forwarded request headers for Elastic Load Balancing.


## [HTTPS listeners](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-https-load-balancers.html)

- [SSL/TLS certificates](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ssl-server-cert.html): Deploy SSL/TLS certificates on your Classic Load Balancers.
- [SSL negotiation configurations](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-ssl-security-policy.html): Negotiate SSL connections between a client and your Classic Load Balancer using a predefined SSL.
- [Predefined SSL security policies](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html): Describes the predefined security policies for SSL negotiation for SSL/HTTP listeners.
- [Create an HTTPS load balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-create-https-ssl-load-balancer.html): Learn how to create a HTTPS listener for your Classic Load Balancer with SSL cipher settings and back-end instance authentication.
- [Configure an HTTPS listener](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-add-or-delete-listeners.html): Add a listener to or remove a listener from your Classic Load Balancer.
- [Replace the SSL certificate](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-update-ssl-cert.html): Update the SSL server certificate that is deployed on your Classic Load Balancer.
- [Update the SSL negotiation configuration](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ssl-config-update.html): Update the SSL negotiation configuration of your Classic Load Balancer.


## [Registered instances](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-backend-instances.html)

- [Register instances with your load balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-deregister-register-instances.html): Register and deregister your EC2 instances with your Classic Load Balancer.
- [Health checks](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-healthchecks.html): Learn how to configure health checks for your Classic Load Balancer.
- [Security groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-instances-security-groups.html): Control the traffic allowed to reach instances using security groups.
- [Network ACLs](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-instances-network-acls.html): Control the traffic allowed to reach instances using network ACLs.


## [Monitor your load balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-monitor-logs.html)

- [CloudWatch metrics](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-cloudwatch-metrics.html): Monitor your Classic Load Balancer with metrics published to Amazon CloudWatch.

### [Access logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/access-log-collection.html)

Learn how to manage access logs for your Classic Load Balancer.

- [Enable access logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html): Learn how to enable access logs.
- [Disable access logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/disable-access-logs.html): Learn how to disable access logs.


## [Troubleshoot your load balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-troubleshooting.html)

- [API errors](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ts-elb-error-api-response.html): Troubleshoot the error messages returned by Elastic Load Balancing API.
- [HTTP errors](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ts-elb-error-message.html): Troubleshoot the error messages returned for your Classic Load Balancer.
- [Response code metrics](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ts-elb-http-errors.html): Troubleshoot the HTTP response codes returned for your Classic Load Balancer.
- [Health checks](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ts-elb-healthcheck.html): Troubleshoot failed health checks for your Classic Load Balancer.
- [Client connectivity](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ts-elb-connection-failed.html): Troubleshoot issues you might encounter when your Classic Load Balancer does not respond to requests.
- [Instance registration](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ts-elb-register-instance.html): Troubleshoot issues you might encounter when registering your instance with your Classic Load Balancer.
