# Source: https://docs.aws.amazon.com/elasticloadbalancing/latest/network/llms.txt

# Elastic Load Balancing Network Load Balancers

> Use Elastic Load Balancing to distribute your incoming application traffic across multiple targets, such as Amazon EC2 instances.

- [What is a Network Load Balancer?](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)
- [Troubleshooting](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-troubleshooting.html)
- [Quotas](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-limits.html)
- [Document history](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/doc-history.html)

## [Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html)

- [Create a load balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-network-load-balancer.html): Learn how to create a Network Load Balancer.
- [Update Availability Zones](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/availability-zones.html): You can enable or disable the Availability Zones for your Network Load Balancer at any time.
- [Update the IP address type](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-ip-address-type.html): Learn how to update the IP address type for your Network Load Balancer.
- [Edit load balancer attributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/edit-load-balancer-attributes.html): Learn how to edit load balancer attributes for your Network Load Balancer.
- [Update the security groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-security-groups.html): Learn how to associate a security group with your Network Load Balancer.
- [Tag a load balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-tags.html): Learn how to update the tags for your Network Load Balancer.
- [Delete a load balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-delete.html): Learn how to delete your Network Load Balancer.
- [View the resource map](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/view-resource-map.html): The Network Load Balancer resource map provides an interactive display of your Network Load Balancers architecture, including its associated listeners, target groups, and targets.
- [CloudWatch logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-cloudwatch-logs.html): Learn how to monitor your Network Load Balancer using logs gathered by CloudWatch.

### [Zonal shift](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/zonal-shift.html)

Learn about the zonal shift function of the Amazon Application Recovery Controller (ARC) and how it works with your Network Load Balancer.

- [Enable zonal shift](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/enable-zonal-shift.html): Zonal shift is disabled by default and must be enabled on each Network Load Balancer.
- [Start a zonal shift](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/start-zonal-shift.html): Zonal shift in ARC enables you to temporarily move traffic for supported resources away from an Availability Zone so that your application can continue to operate normally with other Availability Zones in an AWS Region.
- [Update a zonal shift](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/update-zonal-shift.html): You can update a zonal shift to set a new expiration, or edit or replace the comment for the zonal shift.
- [Cancel a zonal shift](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/cancel-zonal-shift.html): You can cancel a zonal shift any time before it expires.

### [LCU reservations](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/capacity-unit-reservation.html)

Learn about Load Balancer Capacity Unit Reservation for your Network Load Balancer

- [Request reservation](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/request-capacity-unit-reservation.html): Before you use LCU reservation, review the following:
- [Update or cancel reservation](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/update-capacity-unit-reservation.html): If the traffic patterns for your load balancer change, you can update or cancel the LCU reservation for your load balancer.
- [Monitor reservation](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/monitor-capacity-unit-reservation.html)


## [Listeners](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-listeners.html)

- [Create a listener](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-listener.html): Learn how to create a listener for your Network Load Balancer.
- [Server certificates](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/tls-listener-certificates.html): When you create a secure listener for your Network Load Balancer, you must deploy at least one certificate on the load balancer.
- [Security policies](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/describe-ssl-policies.html): When you create a TLS listener, you must select a security policy.
- [Update a listener](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/listener-update-rules.html): Learn how to update a listener for your Network Load Balancer.
- [Update idle timeout](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/update-idle-timeout.html): Learn how to Update the TCP idle timeout for your Network Load Balancer.
- [Update a TLS listener](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/listener-update-certificates.html): Learn how to update the security settings for a TLS listener.
- [Delete a listener](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/delete-listener.html): Learn how to delete a listener for your Network Load Balancer.


## [Target groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html)

- [Create a target group](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-target-group.html): Learn how to create a target group for your Network Load Balancer.
- [Update health settings](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/modify-target-group-health-settings.html): By default, Network Load Balancers monitor the health of targets and route requests to healthy targets.

### [Configure health checks](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/target-group-health-checks.html)

Learn how to configure the health check settings for your Network Load Balancer target groups.

- [Check target health](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/check-target-health.html): You can check the health status of the targets registered with your target groups.
- [Update health check settings](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/modify-health-check-settings.html): You can update the health check settings for your target group at any time.
- [Edit target group attributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/edit-target-group-attributes.html): Learn how to edit target group attributes for your Network Load Balancer.
- [Register targets](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/target-group-register-targets.html): Learn how to add or remove targets from a target group for your Application Load Balancer.
- [Use Application Load Balancers as targets](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/application-load-balancer-target.html): Learn how to use an Application Load Balancer as the target of a Network Load Balancer.
- [Tag a target group](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/target-group-tags.html): Learn how to update the tags for your target groups.
- [Delete a target group](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/delete-target-group.html): Learn how to delete a target group for your Network Load Balancer.


## [Monitor your load balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-monitoring.html)

- [CloudWatch metrics](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-cloudwatch-metrics.html): Learn how to monitor your Network Load Balancer using metrics gathered by CloudWatch.

### [Access logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-access-logs.html)

Learn how to monitor your Network Load Balancer using access logs provided by Elastic Load Balancing.

- [Enable access logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/enable-access-logs.html): When you enable access logging for your load balancer, you must specify the name of the S3 bucket where the load balancer will store the logs.
- [Disable access logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/disable-access-logs.html): You can disable access logging for your load balancer at any time.
