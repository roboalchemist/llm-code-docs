# Source: https://docs.datadoghq.com/agent/guide/private-link.md

---
title: Connect to Datadog over AWS PrivateLink
description: >-
  Configure AWS PrivateLink endpoints to send telemetry data to Datadog securely
  through internal VPC connections, including cross-region setups.
breadcrumbs: Docs > Agent > Agent Guides > Connect to Datadog over AWS PrivateLink
---

# Connect to Datadog over AWS PrivateLink

{% callout %}
# Important note for users on the following Datadog sites: us3.datadoghq.com, us5.datadoghq.com, app.datadoghq.eu, app.ddog-gov.com

{% alert level="danger" %}
Datadog PrivateLink does not support the selected Datadog site.
{% /alert %}

{% /callout %}

{% callout %}
# Important note for users on the following Datadog sites: app.datadoghq.com, ap1.datadoghq.com, ap2.datadoghq.com

## Overview{% #overview %}

This guide walks you through configuring [AWS PrivateLink](https://aws.amazon.com/privatelink/) for use with Datadog. The overall process consists of configuring an internal endpoint in your VPC that local Datadog Agents can send data to. Your VPC endpoint is then peered with the endpoint within Datadog's VPC.

{% image
   source="https://datadog-docs.imgix.net/images/agent/guide/private_link/vpc_diagram_schema.6dd705df72be71ce37f28283a1761e62.png?auto=format"
   alt="VPC diagram Schema" /%}

Datadog exposes AWS PrivateLink endpoints in ****.

- If you need to route Datadog traffic in the same region, follow the steps in Connect from the same region to set up your endpoint.
- To route traffic to Datadog's PrivateLink offering in  from other regions, Datadog recommends cross-region PrivateLink endpoints. [Cross-region PrivateLink](https://aws.amazon.com/privatelink/) enables you to establish connections between VPCs across different AWS regions. This allows VPC resources in different regions to communicate with each other using private IP addresses. Alternatively, use VPC Peering.

## Connect from the same region{% #connect-from-the-same-region %}

1. Connect the AWS Management Console to the region of your choice.

1. From the VPC Dashboard, under **PrivateLink and Lattice**, select **Endpoints**.

1. Click **Create Endpoint**:

   {% image
      source="https://datadog-docs.imgix.net/images/agent/guide/private-link-vpc.4c27a714182fc4afd90d49f8e6edb95a.png?auto=format"
      alt="The endpoints page on the VPC dashboard" /%}

1. Select **Find service by name**.

1. Fill the *Service Name* text box according to which service you want to establish AWS PrivateLink for:

   {% image
      source="https://datadog-docs.imgix.net/images/agent/guide/private_link/vpc_service_name.bdbcaf7807ebf1d0d3f79e6e1f4640b4.png?auto=format"
      alt="VPC service name" /%}

| Datadog                  | PrivateLink service name | Private DNS name |
| ------------------------ | ------------------------ | ---------------- |
| Logs (Agent HTTP intake) |                          |                  |
| Logs (User HTTP intake)  |                          |                  |
| API                      |                          |                  |
| Metrics                  |                          |                  |
| Containers               |                          |                  |
| Process                  |                          |                  |
| Profiling                |                          |                  |
| Traces                   |                          |                  |
| Database Monitoring      |                          |                  |
| Remote Configuration     |                          |                  |

Click **Verify**. If this does not return *Service name found*, reach out to [Datadog support](https://docs.datadoghq.com/help/).

Choose the VPC and subnets that should be peered with the Datadog VPC service endpoint.

Make sure that for **Enable DNS name**, *Enable for this endpoint* is checked:

{% image
   source="https://datadog-docs.imgix.net/images/agent/guide/private_link/enabled_dns_private.eaed3b0d637a73dba106155e4c759bc5.png?auto=format"
   alt="Enable DNS private" /%}

Choose the security group of your choice to control what can send traffic to this VPC endpoint.

**Note**: **The security group must accept inbound traffic on TCP port `443`**.

Click **Create endpoint** at the bottom of the screen. If successful, the following is displayed:

{% image
   source="https://datadog-docs.imgix.net/images/agent/guide/private_link/vpc_endpoint_created.96216f676440c8b68dd16f7be58416d4.png?auto=format"
   alt="VPC endpoint created" /%}

Click on the VPC endpoint ID to check its status.

Wait for the status to move from *Pending* to *Available*. This can take up to 10 minutes. Once it shows *Available*, you can use AWS PrivateLink.

{% image
   source="https://datadog-docs.imgix.net/images/agent/guide/private_link/vpc_status.8da158d01e8dc429dbc846a185e9d266.png?auto=format"
   alt="VPC status" /%}

If you are running a Datadog Agent version older than v6.19 or v7.19, to collect logs data, ensure your Agent is configured to send logs over HTTPS. If the data is not already there, add the following to the [Agent `datadog.yaml` configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/#agent-main-configuration-file):

```yaml
logs_config:
    force_use_http: true
```

If you are using the container Agent, set the following environment variable instead:

```
DD_LOGS_CONFIG_FORCE_USE_HTTP=true
```

This configuration is required when sending logs to Datadog with AWS PrivateLink and the Datadog Agent, and is not required for the Lambda Extension. For more details, see [Agent log collection](https://docs.datadoghq.com/agent/logs/?tab=tailexistingfiles#send-logs-over-https).

If your Lambda Extension loads the Datadog API Key from AWS Secrets Manager using the ARN specified by the environment variable `DD_API_KEY_SECRET_ARN`, you need to [create a VPC endpoint for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/vpc-endpoint-overview.html).

[Restart your Agent](https://docs.datadoghq.com/agent/configuration/agent-commands/#restart-the-agent) to send data to Datadog through AWS PrivateLink.

## Connect from other regions{% #connect-from-other-regions %}

{% tab title="Cross-region PrivateLink endpoints" %}

1. Connect the AWS Management Console to the region of your choice.

1. From the VPC Dashboard, under **PrivateLink and Lattice**, select **Endpoints**.

1. Click **Create Endpoint**:

   {% image
      source="https://datadog-docs.imgix.net/images/agent/guide/private-link-vpc.4c27a714182fc4afd90d49f8e6edb95a.png?auto=format"
      alt="The endpoints page on the VPC dashboard" /%}

1. Configure the VPC interface endpoint settings

   1. Optionally, fill in the **Name tag**.
   1. Under **Type**, select **PrivateLink Ready partner services**.

1. Discover and configure the interface endpoint with cross-region support:

   1. Under **Service name**, fill in the service name with a valid PrivateLink service name from the table below.
   1. Under **Service region**, click **Enable Cross Region endpoint** and select ****.
   1. Click **Verify service** and wait for a *Service name verified* notification. **Note:** If you aren't able to verify the service after completing the steps above, reach out to [Datadog Support](https://docs.datadoghq.com/help/).

1. Under **Network Settings**, select a VPC to deploy the VPC Interface endpoint with.

1. Ensure the option to **Enable DNS name** is checked.

1. Under **Subnets**, select one or more subnets in your VPC for the interface endpoint.

1. Under **Security Groups**, select a security group to control what can send traffic to the VPC endpoint.

**Note**: The security group must accept inbound traffic on TCP port 443.

1. Optionally, provide a **Name tag** and click **Create endpoint**.

1. Allow a few minutes for the endpoint status to update from **Pending** to **Available**. This may take up to 10 minutes. If it is taking longer than expected, reach out to [Datadog Support](https://docs.datadoghq.com/help/).

After the endpoint status is updated to **Available**, you can use this endpoint to send telemetry to Datadog using the cross-region AWS PrivateLink endpoint.

## PrivateLink service names{% #privatelink-service-names %}

| Datadog                  | PrivateLink service name | Private DNS name |
| ------------------------ | ------------------------ | ---------------- |
| Logs (Agent HTTP intake) |                          |                  |
| Logs (User HTTP intake)  |                          |                  |
| API                      |                          |                  |
| Metrics                  |                          |                  |
| Containers               |                          |                  |
| Process                  |                          |                  |
| Profiling                |                          |                  |
| Traces                   |                          |                  |
| Database Monitoring      |                          |                  |
| Remote Configuration     |                          |                  |

**Note**: Cross-region PrivateLink doesn't emit CloudWatch metrics. See [CloudWatch metrics for AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-cloudwatch-metrics.html) for more information.
{% /tab %}

{% tab title="VPC Peering" %}

1. Connect the AWS Console to region **** and create a VPC endpoint.

{% image
   source="https://datadog-docs.imgix.net/images/agent/guide/private_link/create_vpc_endpoint.609d6832d368847f22d3769ab50f6814.png?auto=format"
   alt="Create VPC endpoint" /%}
Select **Find service by name**.Fill the *Service Name* text box according to the service you want to establish AWS PrivateLink for:
{% image
   source="https://datadog-docs.imgix.net/images/agent/guide/private_link/vpc_service_name.bdbcaf7807ebf1d0d3f79e6e1f4640b4.png?auto=format"
   alt="VPC service name" /%}

| Datadog                  | PrivateLink service name |
| ------------------------ | ------------------------ |
| Logs (Agent HTTP intake) |                          |
| Logs (User HTTP intake)  |                          |
| API                      |                          |
| Metrics                  |                          |
| Containers               |                          |
| Process                  |                          |
| Profiling                |                          |
| Traces                   |                          |
| Database Monitoring      |                          |
| Remote Configuration     |                          |

Click **Verify**. If this does not return *Service name found*, reach out to [Datadog support](https://docs.datadoghq.com/help/).

Next, choose the VPC and subnets that should be peered with the Datadog VPC service endpoint. Do not select **Enable DNS name** as VPC peering requires DNS to be manually configured.

Choose the security group of your choice to control what can send traffic to this VPC endpoint.

**Note**: **The security group must accept inbound traffic on TCP port `443`**.

Click **Create endpoint** at the bottom of the screen. If successful, the following is displayed:

{% image
   source="https://datadog-docs.imgix.net/images/agent/guide/private_link/vpc_endpoint_created.96216f676440c8b68dd16f7be58416d4.png?auto=format"
   alt="VPC endpoint created" /%}
Click on the VPC endpoint ID to check its status.Wait for the status to move from *Pending* to *Available*. This can take up to 10 minutes.After creating the endpoint, use VPC peering to make the PrivateLink endpoint available in another region to send telemetry to Datadog over PrivateLink. For more information, read the [Work With VPC Peering connections](https://docs.aws.amazon.com/vpc/latest/peering/working-with-vpc-peering.html) page in AWS.
{% image
   source="https://datadog-docs.imgix.net/images/agent/guide/private_link/vpc_status.8da158d01e8dc429dbc846a185e9d266.png?auto=format"
   alt="VPC status" /%}

### Amazon Route53{% #amazon-route53 %}

1. Create a [Route53 private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html) for each service you have created an AWS PrivateLink endpoint for. Attach the private hosted zone to the VPC in .

{% image
   source="https://datadog-docs.imgix.net/images/agent/guide/private_link/create-a-route53-private-hosted-zone.b5895b38dde45b63d3ef57a08d38bd92.png?auto=format"
   alt="Create a Route53 private hosted zone" /%}

Use the list below to map service and DNS name to different parts of Datadog:

| Datadog                  | PrivateLink service name | Private DNS name |
| ------------------------ | ------------------------ | ---------------- |
| Logs (Agent HTTP intake) |                          |                  |
| Logs (User HTTP intake)  |                          |                  |
| API                      |                          |                  |
| Metrics                  |                          |                  |
| Containers               |                          |                  |
| Process                  |                          |                  |
| Profiling                |                          |                  |
| Traces                   |                          |                  |
| Database Monitoring      |                          |                  |
| Remote Configuration     |                          |                  |

You can also find this information by interrogating the AWS API, `DescribeVpcEndpointServices`, or by using the following command:

```bash
aws ec2 describe-vpc-endpoint-services --service-names <service-name>`
```

For example, in the case of the Datadog metrics endpoint for :

```bash
aws ec2 describe-vpc-endpoint-services --service-names  | jq '.ServiceDetails[0].PrivateDnsName'
```

This returns `metrics.agent.`, the private hosted zone name that you need in order to associate with the VPC which the Agent traffic originates in. Overriding this record grabs all Metrics-related intake hostnames.

Within each new Route53 private hosted zone, create an A record with the same name. Toggle the **Alias** option, then under **Route traffic to**, choose **Alias to VPC endpoint**, ****, and enter the DNS name of the VPC endpoint associated with the DNS name.

**Notes**:

- To retrieve your DNS name, see the [View endpoint service private DNS name configuration documentation.](https://docs.aws.amazon.com/vpc/latest/privatelink/view-vpc-endpoint-service-dns-name.html)
- The Agent sends telemetry to versioned endpoints, for example, `[version]-app.agent.` which resolves to `metrics.agent.` through a CNAME alias. Therefore, you only need to set up a private hosted zone for `metrics.agent.`.

{% image
   source="https://datadog-docs.imgix.net/images/agent/guide/private_link/create-an-a-record.2953b919477a0675e2b3158de7a7e195.png?auto=format"
   alt="Create an A record" /%}

Configure VPC peering and routing between the VPC in  that contains the Datadog PrivateLink endpoints and the VPC in the region where the Datadog Agents run.

If the VPCs are in different AWS accounts, the VPC containing the Datadog Agent must be authorized to associate with the Route53 private hosted zones before continuing. Create a [VPC association authorization](https://docs.amazonaws.cn/en_us/Route53/latest/DeveloperGuide/hosted-zone-private-associate-vpcs-different-accounts.html) for each Route53 private hosted zone using the region and VPC ID of the VPC where the Datadog Agent runs. This option is not available in the AWS Console. It must be configured using the AWS CLI, SDK, or API.

Edit the Route53 hosted zone to add VPCs for other regions.

{% image
   source="https://datadog-docs.imgix.net/images/agent/guide/private_link/edit-route53-hosted-zone.c291ce0824598540370bf36a8abb0b73.png?auto=format"
   alt="Edit a Route53 private hosted zone" /%}

VPCs that have the Private Hosted Zone (PHZ) attached need to have certain settings toggled on, specifically `enableDnsHostnames` and `enableDnsSupport` in the VPCs that the PHZ is associated with. See [Considerations when working with a private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-considerations.html#hosted-zone-private-considerations-vpc-settings).

[Restart the Agent](https://docs.datadoghq.com/agent/configuration/agent-commands/?tab=agentv6v7#restart-the-agent) to send data to Datadog through AWS PrivateLink.

#### Troubleshooting DNS resolution and connectivity{% #troubleshooting-dns-resolution-and-connectivity %}

The DNS names should resolve to IP addresses contained within the CIDR block of the VPC in , and connections to `port 443` should succeed.

{% image
   source="https://datadog-docs.imgix.net/images/agent/guide/private_link/successful-setup.29e5d307829595cbda1942cc6f754e11.png?auto=format"
   alt="Connection to port 443 should be successful" /%}

If DNS is resolving to public IP addresses, then the Route53 zone has **not** been associated with the VPC in the alternate region, or the A record does not exist.

If DNS resolves correctly, but connections to `port 443` are failing, then VPC peering or routing may be misconfigured, or port 443 may not be allowed outbound to the CIDR block of the VPC in .

The VPCs with Private Hosted Zone (PHZ) attached need to have a couple of settings toggled on. Specifically, `enableDnsHostnames` and `enableDnsSupport` need to be turned on in the VPCs that the PHZ is associated with. See [Amazon VPC settings](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-considerations.html#hosted-zone-private-considerations-vpc-settings).

### Datadog Agent{% #datadog-agent %}

1. If you are collecting logs data, ensure your Agent is configured to send logs over HTTPS. If the data is not already there, add the following to the [Agent `datadog.yaml` configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/#agent-main-configuration-file):

   ```yaml
   logs_config:
       force_use_http: true
   ```

If you are using the container Agent, set the following environment variable instead:

   ```
   DD_LOGS_CONFIG_FORCE_USE_HTTP=true
   ```

This configuration is required when sending logs to Datadog with AWS PrivateLink and the Datadog Agent, and is not required for the Lambda Extension. For more details, see [Agent log collection](https://docs.datadoghq.com/agent/logs/?tab=tailexistingfiles#send-logs-over-https).

1. If your Lambda Extension loads the Datadog API Key from AWS Secrets Manager using the ARN specified by the environment variable `DD_API_KEY_SECRET_ARN`, you need to [create a VPC endpoint for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/vpc-endpoint-overview.html).

1. [Restart the Agent](https://docs.datadoghq.com/agent/configuration/agent-commands/?tab=agentv6v7#restart-the-agent).

{% /tab %}

{% /callout %}

## Verify that data is being sent using PrivateLink{% #verify-that-data-is-being-sent-using-privatelink %}

After setting up PrivateLink, to verify that data is getting sent using PrivateLink, run the `dig` command on a machine that is on that VPC. For example, run this command if you had set up a PrivateLink for the endpoint `http-intake.logs.datadoghq.com`:

```
dig http-intake.logs.datadoghq.com
```

If logs are being sent over PrivateLink, the `ANSWER Section` section of the output shows `http-intake.logs.datadoghq.com` like in the following example. **Note**: The IP addresses you get back should be in [private IP space](https://en.wikipedia.org/wiki/Private_network#Private_IPv4_addresses).

```
;; ANSWER SECTION:
http-intake.logs.datadoghq.com.	60 IN	A	172.31.57.3
http-intake.logs.datadoghq.com.	60 IN	A	172.31.3.10
http-intake.logs.datadoghq.com.	60 IN	A	172.31.20.174
http-intake.logs.datadoghq.com.	60 IN	A	172.31.34.135
```

If logs are not being sent over PrivateLink, the `ANSWER SECTION` of the output shows the load balancer (`4-logs-http-s1-e721f9c2a0e65948.elb.us-east-1.amazonaws.com`) to which the logs are getting sent.

```
;; ANSWER SECTION:
http-intake.logs.datadoghq.com.	177 IN	CNAME	http-intake-l4.logs.datadoghq.com.
http-intake-l4.logs.datadoghq.com. 173 IN CNAME	l4-logs-http-s1-e721f9c2a0e65948.elb.us-east-1.amazonaws.com.
l4-logs-http-s1-e721f9c2a0e65948.elb.us-east-1.amazonaws.com. 42 IN A 3.233.158.48
l4-logs-http-s1-e721f9c2a0e65948.elb.us-east-1.amazonaws.com. 42 IN A 3.233.158.49
l4-logs-http-s1-e721f9c2a0e65948.elb.us-east-1.amazonaws.com. 42 IN A 3.233.158.50
```

## Further reading{% #further-reading %}

- [Using Cross-Region AWS PrivateLink to Send Telemetry to Datadog](https://www.datadoghq.com/architecture/using-cross-region-aws-privatelink-to-send-telemetry-to-datadog/)
- [Enable log collection with the Agent](https://docs.datadoghq.com/agent/logs)
- [Collect logs from your AWS services](https://docs.datadoghq.com/integrations/amazon_web_services/#log-collection)
- [Connect to Datadog over AWS PrivateLink](https://www.datadoghq.com/architecture/connect-to-datadog-over-aws-privatelink/)
- [Connect to Datadog over AWS PrivateLink using AWS Transit Gateway](https://www.datadoghq.com/architecture/connect-to-datadog-over-aws-privatelink-using-aws-transit-gateway/)
- [Connect to Datadog over AWS PrivateLink using AWS VPC peering](https://www.datadoghq.com/architecture/connect-to-datadog-over-aws-privatelink-using-aws-vpc-peering/)
- [Reduce costs and enhance security with cross-region Datadog connectivity using AWS PrivateLink](https://www.datadoghq.com/blog/datadog-aws-cross-region-privatelink/)
