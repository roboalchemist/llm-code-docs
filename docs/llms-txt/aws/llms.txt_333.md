# Source: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/llms.txt

# Elastic Load Balancing Application Load Balancers

> Use Elastic Load Balancing to distribute your incoming application traffic across multiple targets, such as EC2 instances.

- [What is an Application Load Balancer?](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)
- [Troubleshoot your load balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-troubleshooting.html)
- [Quotas](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-limits.html)
- [Document history](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/doc-history.html)

## [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html)

- [Create a load balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-application-load-balancer.html): Learn how to create an Application Load Balancer.
- [Update Availability Zones](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-subnets.html): Learn how to enable or disable the Availability Zones for your Application Load Balancer.
- [Update security groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-update-security-groups.html): Learn how to update the security groups for your Application Load Balancer.
- [Update the IP address type](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-ip-address-type.html): Learn how to update the IP address type for your Application Load Balancer.
- [Update the IPAM IP address pools](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-ip-pools.html): Learn how to update the IPAM IP address pool for your Application Load Balancer.
- [Edit load balancer attributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/edit-load-balancer-attributes.html): Learn how to edit load balancer attributes for your Application Load Balancer.
- [Tag a load balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-tags.html): Learn how to update the tags for your Application Load Balancer.
- [Delete a load balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-delete.html): Learn how to delete your Application Load Balancer.
- [View the resource map](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/view-resource-map.html): The Application Load Balancer resource map provides an interactive display of your load balancer's architecture, including its associated listeners, rules, target groups, and targets.

### [Zonal shift](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/zonal-shift.html)

Learn about the zonal shift function of the Amazon Application Recovery Controller (ARC) and how it works with your Application Load Balancer.

- [Enable zonal shift](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/enable-zonal-shift.html): Zonal shift is disabled by default and must be enabled on each Application Load Balancer.
- [Start a zonal shift](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/start-zonal-shift.html): Zonal shift in ARC enables you to temporarily move traffic for supported resources away from an Availability Zone so that your application can continue to operate normally with other Availability Zones in an AWS Region.
- [Update a zonal shift](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/update-zonal-shift.html): You can update a zonal shift to set a new expiration, or edit or replace the comment for the zonal shift.
- [Cancel a zonal shift](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/cancel-zonal-shift.html): You can cancel a zonal shift any time before it expires.

### [LCU reservations](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/capacity-unit-reservation.html)

Learn about Load Balancer Capacity Unit Reservation for your Application Load Balancer

- [Request reservation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/request-capacity-unit-reservation.html): Before you use LCU reservation, review the following:
- [Update or cancel reservation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/update-capacity-unit-reservation.html): If the traffic patterns for your load balancer change, you can update or cancel the LCU reservation for your load balancer.
- [Monitor reservation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/monitor-capacity-unit-reservation.html)
- [Load balancer integrations](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-integrations.html): Learn about integrations for your Application Load Balancer.


## [Listeners and rules](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html)

- [Create an HTTP listener](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-listener.html): Learn how to create an HTTP listener for your Application Load Balancer.
- [SSL certificates](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/https-listener-certificates.html): When you create a secure listener for your Application Load Balancer, you must deploy at least one certificate on the load balancer.
- [Security policies](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/describe-ssl-policies.html): Elastic Load Balancing uses a Secure Socket Layer (SSL) negotiation configuration, known as a security policy, to negotiate SSL connections between a client and the load balancer.
- [Create an HTTPS listener](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html): Learn about HTTPS listeners for your Application Load Balancer.
- [Update an HTTPS listener](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-update-certificates.html): Learn how to update the security settings for an HTTPS listener.

### [Listener rules](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-rules.html)

Understand the key concepts and requirements for listener rules.

- [Action types](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/rule-action-types.html): Understand the types of actions for listener rules and the information required for each action type.
- [Condition types](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/rule-condition-types.html): Understand the types of conditions for listener rules and the information required for each condition type.
- [Transforms](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/rule-transforms.html): Understand the transforms that you can apply to your listener rules and how each transform works.
- [Add a rule](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/add-rule.html): Learn how to add a listener rule to your load balancer listener.
- [Edit a rule](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/edit-rule.html): Learn how to edit a listener rule.
- [Delete a rule](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/delete-rule.html): Learn how to delete a listener rule from your load balancer listener.

### [Mutual TLS authentication](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/mutual-authentication.html)

Learn how to configure mutual authentication for your Application Load Balancer.

- [Configure mutual TLS](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/configuring-mtls-with-elb.html): To use mutual TLS passthrough mode, you need only configure the listener to accept any certificates from clients.
- [Share a trust store](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/trust-store-sharing.html): Describes how to use shared trust stores in Elastic Load Balancing.
- [User authentication](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-authenticate-users.html): Learn how to configure an Application Load Balancer to authenticate users of your applications using their corporate or social identities before routing requests.
- [JWT verification](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-verify-jwt.html): You can configure an Application Load Balancer (ALB) to verify JSON Web Tokens (JWT) provided by clients for secure service-to-service (S2S) or machine-to-machine (M2M) communications.
- [X-forwarded headers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/x-forwarded-headers.html): Learn about the X-Forwarded request headers for Elastic Load Balancing.

### [HTTP header modification](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/header-modification.html)

HTTP header modification is supported by Application Load Balancers, for both request and response headers.

- [Enable header modification](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/enable-header-modification.html): Header modification is turned off by default and must be enabled on each listener.
- [Delete a listener](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/delete-listener.html): Learn how to delete a listener for your Application Load Balancer.


## [Target groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html)

- [Create a target group](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-target-group.html): Learn how to create a target group for your Application Load Balancer.

### [Configure health checks](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html)

Learn how to configure the health check settings for your target groups.

- [Check target health](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/check-target-health.html): You can check the health status of the targets registered with your target groups.
- [Update health check settings](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/modify-health-check-settings.html): You can update the health check settings for your target group at any time.
- [Edit target group attributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/edit-target-group-attributes.html): Learn how to edit target group attributes for your Application Load Balancer.
- [Register targets](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-register-targets.html): Learn how to add or remove targets from a target group for your Application Load Balancer.
- [Use Lambda functions as targets](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html): Learn how to register a Lambda function as a target with an Application Load Balancer.
- [Tag a target group](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-tags.html): Learn how to update the tags for your target groups.
- [Delete a target group](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/delete-target-group.html): Learn how to delete a target group for your Application Load Balancer.


## [Monitor your load balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-monitoring.html)

- [CloudWatch metrics](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-cloudwatch-metrics.html): Learn how to monitor your Application Load Balancer using metrics gathered by CloudWatch.

### [Access logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html)

Learn how to monitor your Application Load Balancer using access logs provided by Elastic Load Balancing.

- [Enable access logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/enable-access-logging.html): When you enable access logs for your load balancer, you must specify the name of the S3 bucket where the load balancer will store the logs.
- [Disable access logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/disable-access-logging.html): You can disable access logs for your load balancer at any time.

### [Connection logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-connection-logs.html)

Learn how to monitor your Application Load Balancer using connection logs provided by Elastic Load Balancing.

- [Enable connection logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/enable-connection-logging.html): When you enable connection logs for your load balancer, you must specify the name of the S3 bucket where the load balancer will store the logs.
- [Disable connection logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/disable-connection-logging.html): You can disable connection logs for your load balancer at any time.

### [Health check logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-health-check-logs.html)

Learn how you can access health check logs for your Application Load Balancer

- [Enable health check logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/enable-health-check-logging.html): When you enable health check logs for your load balancer, you must specify the name of the S3 bucket where the load balancer will store the logs.
- [Disable health check logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/disable-health-check-logging.html): You can disable health check logs for your load balancer at any time.
- [Request tracing](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-request-tracing.html): Learn how you can trace a client request to your application.
