<!-- Source: https://namespace.so/docs/architecture/networking/security -->

# Network Security

Our network architecture is designed to securely support diverse customer workloads on our compute platform.
It provides full isolation by default, with flexible controls to enable cross-instance communication when desired.

## Security Commitment

Network security is only one aspect of Namespace's commitment to security and compliance.
All our security measures are continuously monitored and regularly audited by external security experts as part of our SOC 2 certification.

For complete transparency into our security practices and certifications, customers can access our [Trust Center](https://trust.namespace.so),
where our SOC 2 reports and security controls are available for review.
You can also read more about our [Security & Compliance](/docs/workspaces/security) beyond networking.

[![SOC 2 Type II Badge](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fsoc2.e68a19e5.png&w=640&q=75)](https://trust.namespace.so)

## Private Networking

Different customer environments are always fully isolated from each other, ensuring workloads remain separate and secure.

Workloads within a workspace are also isolated by default, but can be configured to allow communication over a private network.
Instances configured to participate in a Virtual Private Cloud (VPC) are able to securely communicate with other instances on that same network.

## Stable IP Ranges

Namespace provides stable egress IP ranges that make it possible to whitelist traffic in firewalls and other security systems,
providing an additional layer of control and monitoring capability.

Each workspace is assigned specific IP ranges that are documented on the Namespace dashboard under [Networking](https://cloud.namespace.so/workspace/networking).

Namespace provides advance notification of any planned changes to these IP ranges.
Reach out to [support@namespace.so](mailto:support@namespace.so) to subscribe to these updates.

Dedicated egress pools (multi-homed and multi-site) using unique IP addresses are available to enterprise customers.
Using dedicated egress pools you can apply fine-grained network routing policies to your instances.

## Connection Monitoring and Telemetry

Namespace provides connection telemetry and monitoring capabilities,
giving customers visibility into their network traffic patterns and security posture.
This telemetry data can be used for security analysis, compliance reporting, and troubleshooting network connectivity issues.

## Related Topics

- [Federation →](/docs/federation) Enable secure access between Namespace and your cloud infrastructure.
- [Data Residency →](/docs/workspaces/data-residency) Control where your data lives with customizable data residency support.

Last updated October 6, 2025
