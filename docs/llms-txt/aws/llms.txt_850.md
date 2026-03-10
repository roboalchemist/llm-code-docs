# Source: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/llms.txt

# AWS Client VPN Administrator Guide

> Describes key concepts of AWS Client VPN and provides instructions for using the features of Client VPN.

- [Get started with Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-getting-started.html)
- [Quotas](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/limits.html)
- [Document history](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/WhatsNew.html)

## [What is AWS Client VPN?](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html)

- [Rules and best practices](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is-best-practices.html): Learn specific rules and best practices for using Client VPN.


## [How Client VPN works](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/how-it-works.html)

### [Client authentication](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-authentication.html)

Learn how client authentication works in Client VPN.

- [Active Directory authentication](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/ad.html): Learn how Active Directory authentication works in Client VPN.

### [Mutual authentication](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/mutual.html)

Learn how mutual authentication works in Client VPN.

- [Enable mutual authentication](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-auth-mutual-enable.html): Learn how to enable mutual authentication for Client VPN.
- [Renew your server certificate](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/mutual-renew.html): Learn how to renew a server certificate for Client VPN.

### [Single sign-on (SAML 2.0-based federated authentication)](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/federated-authentication.html)

Learn how single sign-on (SAML 2.0-based federated authentication) works in Client VPN.

- [Enable SAML](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-auth-enable-saml.html): Learn how to enable SAML for single sign-on for Client VPN.

### [Client authorization](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-authorization.html)

Learn how client authorization works in Client VPN, and about the supported authorization types.

- [Create an endpoint security group rule](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-auth-rule-create.html): Learn how to create an endpoint security group rule for Client VPN.
- [Connection authorization](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/connection-authorization.html): Configure a client connect handler for your Client VPN endpoint, and use it to run custom logic that authorizes new connections to the Client VPN endpoint.
- [Split-tunnel Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/split-tunnel-vpn.html): Learn about using split-tunnel on Client VPN endpoints to control traffic routing.
- [Connection logging](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/connection-logging.html): Use connection logging to capture information about connection events for your Client VPN endpoint.
- [Scaling considerations](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/scaling-considerations.html): Plan for the number of concurrent connections to your Client VPN endpoint.


## [Work with Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working.html)

- [Self-service portal access](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-self-service-portal.html): Learn how to access the Client VPN self-service portal, and what information to provide to clients.

### [Authorization rules](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-rules.html)

Learn how to add authorization rules to Client VPN to control client access to networks.

- [Add an authorization rule](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-rule-authorize-add.html): Learn how to add an authorization rule to a Client VPN endpoint.
- [Remove an authorization rule](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-rule-remove.html): Learn how to remove an authorization rule from a Client VPN endpoint.
- [View authorization rules](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-rule-view.html): Learn how to view Client VPN endpoint authorization rules.

### [Client certificate revocation lists](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-certificates.html)

Learn how to use Client VPN client certificate revocation lists to revoke access to an endpoint.

- [Generate a client certificate revocation list](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-certificates-generate.html): Learn how to generate a Client VPN client certificate revocation list.
- [Import a client certificate revocation list](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-certificates-import.html): Learn how to import a Client VPN client certificate revocation list.
- [Export a client certificate revocation list](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-certificates-export.html): Learn how to export a Client VPN client certificate revocation list.

### [Client connections](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-connections.html)

Learn about client connections to a Client VPN endpoint.

- [View client connections](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-connections-view.html): Learn how to view Client VPN client connections.
- [Terminate a client connection](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-connections-disassociate.html): Learn how to terminate a Client VPN client connection.

### [Client login banners](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-login-banner.html)

Learn how to display a text banner to Client VPN clients on creation of a VPN session, to meet regulatory and compliance requirements.

- [Configure a client login banner for an existing endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/configure-login-banner-existing-endpoint.html): Learn how to configure a Client VPN login banner for an existing endpoint.
- [Deactivate a client login banner for an endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/disable-login-banner.html): Learn how to deactivate a Client VPN client login banner.
- [Modify existing banner text](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/modify-banner-text.html): Learn how to modify the text of an existing Client VPN client login banner.
- [View a currently configured login banner](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/display-login-banner.html): Learn how to view the currently configured Client VPN login banner.

### [Client Route Enforcement](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-cre.html)

Monitor routes of connected clients.

- [Activate Client Route Enforcement](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/activate-cre.html): Activate client route enforcement for client vpn
- [Deactivate Client Route Enforcement](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/deactivate-cre.html): Deactivate client route enforcement for client vpn
- [Troubleshoot IPv6 Client Route Enforcement](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cre-ipv6-troubleshooting.html): Troubleshoot client route enforcement for client vpn

### [Endpoints](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoints.html)

Learn how to create, modify, add, and delete Client VPN endpoints.

- [Create an endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoint-create.html): Learn how to create a Client VPN endpoint.
- [View endpoints](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoint-view.html): Learn how to view Client VPN endpoints.
- [Modify an endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoint-modify.html): Learn how to modify a Client VPN endpoint.
- [Delete an endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoint-delete.html): Learn how to delete a Client VPN endpoint.

### [Connection logs](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-with-connection-logs.html)

Learn how to work with connection logs for your Client VPN endpoint.

- [Enable connection logging for a new endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/create-connection-log-new.html): Learn how to enable connection logging for a new Client VPN endpoint.
- [Enable connection logging for an existing endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/create-connection-log-existing.html): Learn how to enable connection logging for an existing Client VPN endpoint.
- [View connection logs](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/view-connection-logs.html): Learn how to view Client VPN connection logs.
- [Turn off connection logging](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/disable-connection-logs.html): Learn how to turn off connection logging for a Client VPN endpoint.

### [Client configuration file export](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoint-export.html)

Learn how to configure the Client VPN endpoint configuration file, and export it for clients who need access to the VPN.

- [Export the client configuration file](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/export-client-config-file.html): Learn how to export a Client VPN client configuration file.
- [Add the client certificate and key information for mutual authentication](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/add-config-file-cert-key.html): Learn how to add a Client VPN client certificate file and key information to a configuration file for mutual authentication.

### [Routes](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-routes.html)

Learn how route tables are used for routing traffic to Client VPN endpoints.

- [Create an endpoint route](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-routes-create.html): Learn how to create a Client VPN endpoint route.
- [View endpoint routes](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-routes-view.html): Learn how to view Client VPN endpoint routes.
- [Delete an endpoint route](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-routes-delete.html): Learn how to delete a Client VPN endpoint route.

### [Target networks](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-target.html)

Learn how target networks are used to enable Client VPN clients to establish a VPN connection.

- [Associate a target network with an endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-target-associate.html): Learn how to associate a target network with an endpoint in Client VPN.
- [Apply a security group to a target network](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-target-apply.html): Learn how to apply a security group to a target network in Client VPN.
- [View target networks](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-target-view.html): Learn how to view Client VPN target networks.
- [Disassociate a target network from an endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-target-disassociate.html): Learn how to disassociate a target network from a Client VPN endpoint.

### [Maximum VPN session duration](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-max-duration.html)

Learn how to configure Client VPN timeout for maximum VPN session duration to meet security and compliance requirements.

- [View current maximum VPN session duration](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/display-max-duration.html): Learn how to view the current maximum Client VPN session duration.
- [Modify the maximum VPN session duration](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/modify-max-timeout.html): Learn how to modify the current Client VPN maximum session duration.


## [Security](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/security.html)

- [Data protection](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS Client VPN.

### [Identity and access management](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/security-iam.html)

Learn how to authenticate requests and manage access to your Client VPN resources.

- [How AWS Client VPN works with IAM](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/security_iam_service-with-iam.html): Learn about the IAM features that Client VPN supports.
- [Identity-based policy examples](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/security_iam_id-based-policy-examples.html): Learn how to use identity-based policies to grant users and roles access to Client VPN.
- [Troubleshooting](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/security_iam_troubleshoot.html): Troubleshoot common issues with IAM in Client VPN.

### [Using service-linked roles](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/using-service-linked-roles.html)

Learn how to grant Client VPN access to resources in your account by using service-linked roles.

- [Client VPN usage](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/using-service-linked-roles-cvpn-slr.html): How to use service-linked roles to give Client VPN access to resources in your AWS account.
- [Connection authorization](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/using-service-linked-roles-client-connect-handler.html): How to use service-linked roles to give Client VPN access to resources in your AWS account.
- [Resilience](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Client VPN features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/infrastructure-security.html): Learn how AWS Client VPN isolates service traffic.
- [Best practices](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/security-best-practices.html): Learn about security best practices for AWS Client VPN.
- [IPv6 considerations](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/ipv6-considerations.html): Learn about IPv6 considerations for using Client VPN.


## [Monitoring Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/monitoring-overview.html)

### [CloudWatch metrics](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/monitoring-cloudwatch.html)

Learn about the metrics that Client VPN sends to Amazon CloudWatch.

- [View CloudWatch metrics](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/viewing-metrics.html): Learn how you can view Client VPN endpoint metrics in Amazon CloudWatch.


## [Troubleshooting](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/troubleshooting.html)

- [Unable to resolve the Client VPN endpoint DNS name](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/resolve-host-name.html): This information helps troubleshoot when a Client VPN endpoint doesn't resolve.
- [Traffic is not being split between subnets](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/split-traffic.html): This information helps troubleshoot when Client VPN traffic is not being split between subnets.
- [Authorization rules for Active Directory groups not working as expected](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/ad-group-auth-rules.html): This information helps troubleshoot a Client VPN error about Active Directory groups.
- [Clients can't access a peered VPC, Amazon S3, or the internet](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/no-internet-access.html): This information helps troubleshoot a Client VPN error where a client can't access a peered VPC, Amazon S3 or the internet.
- [Access to a peered VPC, Amazon S3, or the internet is intermittent](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/intermittent-access.html): This information helps troubleshoot Client VPN intermittent access problems with a peered VPC, Amazon S3 or the internet.
- [Client software returns TLS error](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-cannot-connect.html): This information helps troubleshoot a Client VPN issue around a TLS error.
- [Client software returns user name and password errors â Active Directory authentication](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-user-name-password-mfa.html): This information helps troubleshoot a Client VPN user name or password error when using Active Directory authentication.
- [Client software returns user name and password errors â federated authentication](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/missing-attribute.html): This information helps troubleshoot a Client VPN error about user name or password errors when using federated authentication.
- [Clients cannot connect â mutual authentication](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-cannot-connect-mutual.html): This information helps troubleshoot a Client VPN error about clients not connecting when you're using mutual authentication.
- [Client returns a credentials exceed max size error â federated authentication](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-credentials-exceeded.html): This information helps troubleshoot a Client VPN error about max size for credentials when you're using federated authentication.
- [Client does not open browser â federated authentication](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-no-browser.html): This information helps troubleshoot a Client VPN error where the client does not open a browser window when you're using federated authentication.
- [Client returns no available ports error â federated authentication](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-no-port.html): This information helps troubleshoot a Client VPN error that no ports are available, when you're using federated authentication.
- [VPN connection terminated due to IP mismatch](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/server-ip-mismatch.html): This information helps troubleshoot a Client VPN error about an IP mismatch.
- [Routing traffic to LAN not working as expected](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/routing-to-lan.html): This information helps troubleshoot a Client VPN error that routing traffic to the LAN is not working.
- [Verify the bandwidth limit for an endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/test-throughput.html): This information helps you check the bandwidth limit for a Client VPN endpoint.
- [Client VPN tunnel connectivity](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/VPNTunnelConnectivityTroubleshooting.html): Learn how to systematically troubleshoot connectivity issues between AWS Client VPN clients and your Amazon VPC resources.
