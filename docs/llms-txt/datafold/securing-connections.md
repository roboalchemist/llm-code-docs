# Source: https://docs.datafold.com/security/securing-connections.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Securing Connections

> Datafold supports multiple options to secure connections between your resources (e.g., databases and BI tools) and Datafold.

## Encryption

When you connect to Datafold to query your data in a database (e.g., BigQuery), communications are secured using HTTPS encryption.

## IP whitelisting

If access to your data connection is restricted to IP addresses on an allowlist, you will need to manually add Datafold's addresses in order to use our product. Otherwise, you will receive a connection error when setting up your data connection.

For SaaS (app.datafold.com) deployments, whitelist the following IP addresses:

* `23.23.71.47`
* `35.166.223.86`
* `52.11.132.23`
* `54.71.177.163`
* `54.185.25.103`
* `54.210.34.216`

Note that at any given time, you will only see one of these addresses in use. However, the active IP address can change, so you should add them all to your IP whitelist to ensure no interruptions in service.

## Private Link

<Tabs>
  <Tab title="AWS">
    ### AWS PrivateLink

    AWS PrivateLink allows you to connect Datafold to your databases without exposing data to the internet. This option is available for both Datafold SaaS Cloud and all Datafold Dedicated Cloud options.

    The following diagram shows the architecture for a customer with a High Availability RDS setup:

    <Frame caption="SaaS with PrivateLink">
      <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saas_with_privatelink-1294c819a7e75474a9eb736bfac2cc95.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=65b88c7ff34cc84894b60d27691bbe88" data-og-width="2480" width="2480" data-og-height="1296" height="1296" data-path="images/saas_with_privatelink-1294c819a7e75474a9eb736bfac2cc95.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saas_with_privatelink-1294c819a7e75474a9eb736bfac2cc95.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ce35baacdc5cdfd99ecca2350df43249 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saas_with_privatelink-1294c819a7e75474a9eb736bfac2cc95.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=01d156c2eff63bdb78b10e4109d86b67 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saas_with_privatelink-1294c819a7e75474a9eb736bfac2cc95.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=f569417d66283f168b84c4cb23ea92a9 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saas_with_privatelink-1294c819a7e75474a9eb736bfac2cc95.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=b6529b2dd6158a729dd4185760904f76 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saas_with_privatelink-1294c819a7e75474a9eb736bfac2cc95.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=73881be7675758882f8de1ef81698b14 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saas_with_privatelink-1294c819a7e75474a9eb736bfac2cc95.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=892c9b54e12f3de7dc08df77a01ebfae 2500w" />
    </Frame>

    ### Setup

    <Info>
      Supported databases

      The following setup assumes you have an RDS/Aurora database you want to connect to. Datafold also supports PrivateLink connections to other databases such as Snowflake, which should only be accessed from your VPC. Please contact [support@datafold.com](mailto:support@datafold.com) to get assistance with connecting to your specific database.
    </Info>

    Our support team will send you the following:

    * The role ARN to establish the PrivateLink connection.
    * Datafold SaaS Cloud VPC CIDR range.

    You need to do the following steps:

    1. Send us the region(s) where your database(s) are located.
    2. Create a VPC Endpoint Service and NLB.
       * The core concepts of this setup are described in this AWS blog: [Access Amazon RDS across VPCs using AWS PrivateLink and Network Load Balancer](https://aws.amazon.com/blogs/database/access-amazon-rds-across-vpcs-using-aws-privatelink-and-network-load-balancer/).
       * If your databases are HA, please implement the failover mechanics described in the blog.
         * A CloudFormation template for inspiration can be found [here](https://github.com/aws-samples/amazon-rds-crossaccount-access/blob/main/CrossAccountRDSAccess.yml).
       * You'll need to create a Network Load Balancer that points to your database and a VPC Endpoint Service that exposes the NLB.
       * Configure security groups to allow traffic from Datafold's VPC to your database.
       * If your databases are HA (High Availability), implement automatic failover mechanics to ensure the NLB routes to the active database instance.
       * For detailed step-by-step instructions, see our [**AWS PrivateLink Setup Guide**](/security/aws_privatelink_setup).
    3. Add the provided role ARN as 'Allowed Principal' on the VPC Endpoint Service.
    4. Allow ingress from the Datafold SaaS Cloud VPC.
    5. Send us the:
       * Service name(s), e.g. `com.amazonaws.vpce.us-west-2.vpce-svc-0cfd2f258c4395ad6`.
       * Availability Zone ID(s) used in the VPCE Service(s), e.g. `use1-az6` or `usw2-az3`.
       * RDS/Aurora hostname(s), e.g. `datafold.c2zezoge6btk.us-west-2.rds.amazonaws.com`.

    At the end, the database hostname used to configure the data source will be the original RDS/Aurora hostname. But with private DNS resolution, we will resolve the hostname to the VPC Endpoint. Our support team will let you know when everything is set up and you can accept the PrivateLink connection and start configuring the data source.

    <Tip>
      **Detailed Instructions**

      For comprehensive step-by-step instructions including security group configuration, target group setup, Lambda-based automatic failover for HA setups, and troubleshooting, see our [**AWS PrivateLink Setup Guide**](/security/aws_privatelink_setup).
    </Tip>

    ### Cross-Region PrivateLink

    Datafold SaaS Cloud supports cross-region PrivateLink for all North American regions. Datafold SaaS Cloud is located in `us-west-2`. Datafold manages the cross-region networking, allowing you to connect to a VPC Endpoint in the same region as your VPC Endpoint Service. For Datafold Dedicated Cloud customers, deployment occurs in your chosen region. If you need to connect to databases in multiple regions, Datafold also supports this through cross-region PrivateLink.

    The setup will be similar to the regular PrivateLink setup.
  </Tab>

  <Tab title="GCP">
    ### Private Service Connect

    Google Cloud's Private Service Connect is only available if both parties are in the same cloud region. This option is only available for Datafold Dedicated Cloud customers. The diagram below illustrates how the solution works:

    <Frame>
      <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcp-psc-endpoint-overview-codelabs-b94101869413df5385a0a6406b9ff859.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=38c439b9f588193c87956ef53895a424" data-og-width="1008" width="1008" data-og-height="586" height="586" data-path="images/gcp-psc-endpoint-overview-codelabs-b94101869413df5385a0a6406b9ff859.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcp-psc-endpoint-overview-codelabs-b94101869413df5385a0a6406b9ff859.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=be06d8ff89a08b4df409ecfede8a683b 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcp-psc-endpoint-overview-codelabs-b94101869413df5385a0a6406b9ff859.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=0b583f6cb0578ee985d1195d03834a21 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcp-psc-endpoint-overview-codelabs-b94101869413df5385a0a6406b9ff859.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=ccf8914007440e0cb88fe9839abd2f89 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcp-psc-endpoint-overview-codelabs-b94101869413df5385a0a6406b9ff859.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=2753bd770bb50ff04c7bc89d428df1f9 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcp-psc-endpoint-overview-codelabs-b94101869413df5385a0a6406b9ff859.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4f33eb651737d66fef59dd4c929f52b0 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gcp-psc-endpoint-overview-codelabs-b94101869413df5385a0a6406b9ff859.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=d94d78eb8007a0a5b49ecb36ddbc2711 2500w" />
    </Frame>

    The basics of Private Service Connect are available [here](https://cloud.google.com/vpc/docs/private-service-connect).
  </Tab>

  <Tab title="Azure">
    ### Azure Private Link

    Azure Private Link is only available if both parties are in the same cloud region. This option is only available for Datafold Dedicated Cloud customers. The diagram below illustrates how the solution works:

    <Frame>
      <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure-cross-tenant-secure-access-private-endpoints-architecture-bcf92a6fe7e8007d278b3256c1ef666d.svg?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e8a1369ee4fd7f7866ec7550337f0c23" data-og-width="1140" width="1140" data-og-height="729" height="729" data-path="images/azure-cross-tenant-secure-access-private-endpoints-architecture-bcf92a6fe7e8007d278b3256c1ef666d.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure-cross-tenant-secure-access-private-endpoints-architecture-bcf92a6fe7e8007d278b3256c1ef666d.svg?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=0cdc802a43333d995b7161feb6021374 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure-cross-tenant-secure-access-private-endpoints-architecture-bcf92a6fe7e8007d278b3256c1ef666d.svg?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=05bbed6ba750dbb4538db193265bf181 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure-cross-tenant-secure-access-private-endpoints-architecture-bcf92a6fe7e8007d278b3256c1ef666d.svg?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d01a70b96bf8e75b3a26cf6ae91c9e45 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure-cross-tenant-secure-access-private-endpoints-architecture-bcf92a6fe7e8007d278b3256c1ef666d.svg?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=315e8750c5cda55724d638efa3f5c899 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure-cross-tenant-secure-access-private-endpoints-architecture-bcf92a6fe7e8007d278b3256c1ef666d.svg?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=b8d4907b690435efb419d259574260af 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/azure-cross-tenant-secure-access-private-endpoints-architecture-bcf92a6fe7e8007d278b3256c1ef666d.svg?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f788286a9ffaa42293d3ea1e22f03742 2500w" />
    </Frame>

    The basics of Private Link are available [here](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview).

    For Customer-Hosted Dedicated Cloud, achieving cross-tenant access requires using Private Link. The documentation can be accessed [here](https://learn.microsoft.com/en-us/azure/architecture/guide/networking/cross-tenant-secure-access-private-endpoints).
  </Tab>
</Tabs>

## VPC Peering (SaaS)

VPC Peering is easier to set up than Private Link, but a drawback is that both networks are joined and the IP ranges must not overlap. For Datafold SaaS Cloud, this setup is an AWS-only option.

The basics of VPC peering are covered [here](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html).

To set up VPC peering, please contact [support@datafold.com](mailto:support@datafold.com) and provide us with the following information:

* AWS region where your database is hosted.
* ID of the VPC that you would like to connect.
* CIDR of the VPC.

If there are no address collisions, we'll send you a peering request and CIDR that we use on our end, and whitelist the CIDR range for your organization. You'll need to set up routing to this CIDR through the peering connection.

If you activate DNS on your side of the peering connection, you can use the private DNS hostname to connect. Otherwise, you need to use the IP.

## VPC Peering (Dedicated Cloud)

VPC Peering is a supported option for all cloud providers, both for Datafold-hosted and customer-hosted deployments. Basic information for each cloud provider can be found here:

* [AWS](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html)
* [GCP](https://cloud.google.com/vpc/docs/vpc-peering)
* [Azure](https://learn.microsoft.com/en-us/azure/virtual-network/create-peering-different-subscriptions?tabs=create-peering-portal)

<Tip>
  **VPC vs VNet**

  We use the term VPC across all major cloud providers. However, Azure calls this concept a Virtual Network (VNet).
</Tip>

## SSH Tunnel

To set up a tunnel, please contact our team at [support@datafold.com](mailto:support@datafold.com) and provide the following information:

* Hostname of your bastion host and port number used for SSH service.
* Hostname of and port number of your database.
* SSH fingerprint of the bastion host (optional).

We'll get back to you with:

* SSH public key that you need to add to `~/.ssh/authorized_hosts`.
* IP address and port to use for data connection configuration in the Datafold application.

## IPSec tunnel

Please contact our team at [support@datafold.com](mailto:support@datafold.com) for more information.
