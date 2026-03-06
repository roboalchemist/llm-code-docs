# Source: https://northflank.com/docs/v1/application/network/load-balancing.md

# Select a load balancing strategy

Northflank routes external traffic to your instances using scalable, secure, and highly performant load balancers.

By default, traffic will be distributed using the least-connection strategy. You can select the load-balancing strategy for a combined or deployment service in the networking section when creating it, or change it on the networking page of an existing service. Changes will take effect immediately and do not require redeployment.

If an instance is replaced then requests will be routed to a new instance using the same strategy.

## Least connection

Least-connection selects the pod with the least current open connections. This approach helps ensure even distribution of traffic across your instances, especially when requests can vary in duration and resource usage.

## Consistent hashing

Consistent hashing can be used to create "sticky sessions", consistent connections between users and a specific instance.

You can choose different hash modes depending on your requirements:

Client IP address mode will use the IP address of the request to route requests to the same instances.

Custom header allows you to set the [HTTP header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers) to use, for example `X-Sticky-Session`. The value of this header will be hashed to consistently route to the same instance. This also allows for multiple different users to be routed to the same instance.

## Round robin

Round-robin balances requests by routing each request to the next instance in turn. This strategy is best if requests are fairly uniform in resource usage.

For example, with 2 instances: request 1 is routed to instance 1, request 2 is routed to instance 2, and request 3 is routed to instance 1.

## Next steps

- [Expose ports in your application: Expose ports in your application to make it available for networking.](/v1/application/network/expose-your-application)
- [Add public ports: Configure ports to expose your services on the internet.](/v1/application/network/configure-ports#public-ports)
- [Set IP policies: Allow or deny access to services based on IP addresses.](/v1/application/network/add-security-policies-for-ports#set-ip-policies)
- [Configure basic authentication: Require users to enter a username and password to access your site.](/v1/application/network/add-security-policies-for-ports#require-credentials)
