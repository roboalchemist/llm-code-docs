# Source: https://planetscale.com/docs/postgres/connecting/private-connections/aws-privatelink.md

# Connect privately with AWS PrivateLink

> When you use AWS PrivateLink, your network traffic between your VPC and PlanetScale stays within the AWS network, without traversing the public internet.

[AWS PrivateLink](https://aws.amazon.com/privatelink/) is a highly available, scalable technology that enables you to privately connect your VPC to supported AWS services, VPC endpoint services, and AWS Marketplace partner services.

### When to use AWS PrivateLink

By default, PlanetScale Postgres databases use secure connections over the public internet with industry-standard TLS encryption. This approach is secure and meets the needs of most customers. However, you may want to consider AWS PrivateLink if:

* **Compliance requirements**: Your organization has stronger regulatory or compliance mandates that require database connections to avoid the public internet entirely
* **Enhanced security posture**: You want an additional layer of network isolation for sensitive data workloads
* **Network architecture**: Your existing AWS infrastructure is designed around private connectivity patterns
* **Reduced network latency**: AWS PrivateLink can help reduce latency by avoiding the extra network hop through a [NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) that's typically required for outbound internet connections from private subnets. While this latency difference is often minimal (typically single-digit milliseconds), it may be noticeable if you're migrating from a database that was previously hosted directly within your VPC

AWS PrivateLink provides these security and compliance benefits by ensuring your database traffic never leaves the AWS backbone network.

<Note>
  Normal PlanetScale Postgres connectivity (as described in our [standard connection documentation](/docs/postgres/connecting)) uses secure TLS encryption over the public internet and is appropriate for most use cases. AWS PrivateLink is primarily beneficial for compliance and enhanced security requirements.
</Note>

### PrivateLink pricing

PlanetScale does not charge any additional fees for AWS PrivateLink connectivity. However, AWS charges standard PrivateLink pricing for VPC endpoints, which includes:

| Charge Type                     | Rate              | Description                                                |
| ------------------------------- | ----------------- | ---------------------------------------------------------- |
| **VPC endpoint hourly charges** | \~\$0.01 per hour | Per VPC endpoint (varies by region)                        |
| **Data processing charges**     | \~\$0.01 per GB   | Data processed through the VPC endpoint (varies by region) |

For current pricing in your region, see the [AWS PrivateLink pricing page](https://aws.amazon.com/privatelink/pricing/).

## Prerequisites

* A PlanetScale Postgres database in an AWS region
* An AWS VPC in the same region where you want to establish the private connection
* Appropriate AWS IAM permissions to create VPC endpoints (see [AWS VPC endpoint permissions documentation](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-iam.html))
* Appropriate AWS IAM permissions to create and modify Security Groups (see [AWS IAM permissions for security groups documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#iam-policies-security-groups))

## Establishing a VPC endpoint

1. **Retrieve the Private Service Name**:
   1. From the PlanetScale organization dashboard, select the desired database
   2. Navigate to **Settings** from the menu on the left
   3. Select **Roles**
   4. Click on a role with permissions to the relevant `Branch`
   5. Copy the `Private Host` and `Private Service Name` from the role details

<img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/aws-private-host-names.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=7f25404edbdd159f28a8b599fc246156" alt="Private connection strings" data-og-width="1842" width="1842" data-og-height="402" height="402" data-path="docs/postgres/connecting/private-connections/aws-private-host-names.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/aws-private-host-names.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=d84ddbd81aac0518f29d647fd0a67a0f 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/aws-private-host-names.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=af6d05832fced533c3a3540ae923c93b 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/aws-private-host-names.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=c231d2702d4b7d5f958464e1cbe83ee5 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/aws-private-host-names.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=70bcb583dc8f822f54fcaeb83638c584 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/aws-private-host-names.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=ab409eae91f99cea5f59b80b97a9964d 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/aws-private-host-names.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=4e7102d24093a9833c3fe5466e3ee3cd 2500w" />

Save these two attributes for your records and the rest of the configuration.

<Note>
  Both the `Private Host` and `Private Service Name` values are the same for all roles for a given PlanetScale database `Branch`. Once enabled, any role can use the PrivateLink endpoint. You do not need to configure this per PlanetScale `Role`.
</Note>

1. **Create a Security Group for the Endpoint**:
   You will need an AWS Security Group configured to allow inbound traffic for the required ports. You can configure access using either the security group ID of your application hosts, your VPC's CIDR configuration, or specific subnet CIDR configurations. Ensure your [security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) allow:

   * **Inbound PostgreSQL (port 5432)**: For direct database connections
   * **Inbound PSBouncer (port 6432)**: For pooled connections via PSBouncer

   An example using the AWS CLI:

   ```bash  theme={null}
   # Create the security group (capture its ID)
   SG_ID=$(aws ec2 create-security-group \
   --group-name PScalePrivateLinkEndpointSG \
   --description "Security group for PlanetScale PrivateLink endpoint" \
   --vpc-id <your-vpc-id> \
   --query 'GroupId' --output text)

   # Option A (preferred): allow only from a client SG (replace sg-CLIENT)
   aws ec2 authorize-security-group-ingress \
      --group-id "$SG_ID" \
      --ip-permissions '[
        {"IpProtocol":"tcp","FromPort":5432,"ToPort":5432,"UserIdGroupPairs":[{"GroupId":"sg-CLIENT"}]},
        {"IpProtocol":"tcp","FromPort":6432,"ToPort":6432,"UserIdGroupPairs":[{"GroupId":"sg-CLIENT"}]}
      ]'

   # Option B: allow from entire VPC CIDR (replace with your actual CIDR)
   #aws ec2 authorize-security-group-ingress \
   #--group-id "$SG_ID" \
   #--ip-permissions '[
   #   {"IpProtocol":"tcp","FromPort":5432,"ToPort":5432,"IpRanges":[{"CidrIp":"10.0.0.0/16"}]},
   #   {"IpProtocol":"tcp","FromPort":6432,"ToPort":6432,"IpRanges":[{"CidrIp":"10.0.0.0/16"}]}
   #]'
   ```

   Replace `<your-vpc-id>` with your actual VPC ID. You can find your VPC ID and its CIDR block using:

   ```bash  theme={null}
   aws ec2 describe-vpcs --query 'Vpcs[*].[VpcId,CidrBlock]' --output table
   ```

2. **Navigate to VPC Endpoints**: In your AWS Console:

   1. Confirm you are in the proper `<aws-region>` from the dropdown on the top right
   2. In the search field at the top left enter "Endpoints".
   3. Click the link listed as a **VPC Feature**.

   <img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/endpoint-search.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=eaef632858754672ef532ff2a2d49c6b" alt="Endpoint search" data-og-width="2598" width="2598" data-og-height="872" height="872" data-path="docs/postgres/connecting/private-connections/endpoint-search.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/endpoint-search.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=841f7ed92b0bdf4888a4f4e91295d808 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/endpoint-search.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=114328369251e66300695dbd59fbc8b1 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/endpoint-search.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=b34c80eec9b07e2bf6e61a1327dff774 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/endpoint-search.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=17d71bdcf19f8120c8095347ec9ab185 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/endpoint-search.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=cdea36621a833694256616ccb955a02d 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/endpoint-search.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=591af4eb9b1108c4ecf96265c5f35b85 2500w" />

3. **Create a new endpoint**: Click "**Create Endpoint**".

   <img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/create-new-endpoint.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=bbc1824a503ec0a5f6b27977f32835da" alt="Create a new endpoint" data-og-width="2598" width="2598" data-og-height="874" height="874" data-path="docs/postgres/connecting/private-connections/create-new-endpoint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/create-new-endpoint.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=7d78a0a6ca4f78baab86663e780ca60e 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/create-new-endpoint.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=0cec45339e7d262577889e0c7a7e16a4 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/create-new-endpoint.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=b38a902b0db5ad77dcca3e7264d7a21f 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/create-new-endpoint.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=b634d07779946ada67a148209aa8c790 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/create-new-endpoint.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=2d8801f44effe53255f0a004d5163736 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/create-new-endpoint.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=4e09c67ca1fd0ad152d7012c515d21a2 2500w" />

4. **Select endpoint type**: Choose "Endpoint services that use NLBs and GWLBs".

   <img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/type-of-endpoint.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=526a744609e2df3a49c21b6e1adc0269" alt="Menu to select endpoint type" data-og-width="2588" width="2588" data-og-height="1280" height="1280" data-path="docs/postgres/connecting/private-connections/type-of-endpoint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/type-of-endpoint.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=d5c5c21c3e775e3f93af1e73cd36c49b 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/type-of-endpoint.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=06e89fc8e1a9ec47629e5d78117f60d7 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/type-of-endpoint.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=15847eee2fd208a4404853e1bf8d7e9d 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/type-of-endpoint.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=d775b4cf91b2dd1b405172eac27de484 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/type-of-endpoint.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=dd9a23e857a5b50c135a3f5f124428dd 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/type-of-endpoint.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=158d23e1223a03a5af1b7cdc96b808bb 2500w" />

5. **Enter service name**: Enter in the "Service name" text box the `Private Service Name` retrieved from the PlanetScale dashboard. Click "**Verify service**" to confirm the service exists.

   <img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/verified-endpoint.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=c94da8e818f0ed9181764b0eb97401d3" alt="Endpoint service name and verification" data-og-width="1994" width="1994" data-og-height="548" height="548" data-path="docs/postgres/connecting/private-connections/verified-endpoint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/verified-endpoint.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=d9cae4bf401c4372fb6d916233ccf47a 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/verified-endpoint.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=e2da51bcfb1d2faeccb06eff4f1693f7 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/verified-endpoint.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=d3e1b9ebf1ac7d4784612527fd001208 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/verified-endpoint.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=34ef6146e0f309be45f282cf7b16cb91 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/verified-endpoint.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=43b430f22f780acc77d324a68a72f87f 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/verified-endpoint.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=8045d22f0d07d13202157897e4497eac 2500w" />

6. **Configure VPCs**: Choose the VPC that should have access to the PlanetScale service endpoint.

7. **Enable DNS names**: Click the "Additional settings" dropdown arrow to reveal DNS configuration options, and select the "**Enable DNS name**" checkbox.

8. **Configure Subnets**: Choose the subnets that should have endpoint interfaces for the PlanetScale service endpoint. It is recommended that you select at least 2. You should select subnets that your application servers have access to.

<img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/network-subnets-config.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=8be0ebbfcc7c356d3a1dbe41fcdc50f1" alt="Subnets" data-og-width="1978" width="1978" data-og-height="1632" height="1632" data-path="docs/postgres/connecting/private-connections/network-subnets-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/network-subnets-config.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=8b4956809072b7129c2892b352cbeb40 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/network-subnets-config.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=a0b9bfaebf8613f1380b49272768888e 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/network-subnets-config.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=f69afdcdef91629204d27596c209b7b3 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/network-subnets-config.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=1341d8303a94f4942416448683727a25 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/network-subnets-config.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=b04e522a752414cdfb2ed424f2879d65 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/network-subnets-config.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=49889780e7ef328a1c87baaae07d74ba 2500w" />

9. **Configure security groups**: Choose the appropriate security group to control which resources can send traffic to the PlanetScale service endpoint. Use the one created earlier if you created one for this purpose.

<img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/security-groups.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=b8de8e5e51d5b772a8b6f32b7a828a6d" alt="Security Groups" data-og-width="2710" width="2710" data-og-height="514" height="514" data-path="docs/postgres/connecting/private-connections/security-groups.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/security-groups.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=0f427f4b9325d146c5484c040d1f7f8c 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/security-groups.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=19a7332357bba7cbde1a9430e6e6fcad 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/security-groups.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=ea83ac732762da72aa6c0f6442885080 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/security-groups.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=c6e3764e42629d11ee2ae8094cdd07c0 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/security-groups.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=482ffdd2b4c1bc06784126de65ef6d86 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/security-groups.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=00cb783f608a6884a0e8a04c80780d92 2500w" />

10. **Create the endpoint**: Click "**Create endpoint**" and wait for the VPC endpoint status to show "Available" (this may take several minutes).

<img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/available-endpoint.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=82cb9829d128862ed2ead700439adad7" alt="Available Endpoint" data-og-width="1602" width="1602" data-og-height="1098" height="1098" data-path="docs/postgres/connecting/private-connections/available-endpoint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/available-endpoint.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=dbb942840764c8a6d89f2fc1b1c06e59 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/available-endpoint.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=d7a1766ab4fce84d2df49cfc75432f7e 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/available-endpoint.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=798f424f2fa386cbaeec169a8396b73b 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/available-endpoint.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=61986496a68eefc47fab4161433ad007 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/available-endpoint.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=746cef0e9d7e0f3528a01748210b141c 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/available-endpoint.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=194992e9506403863fa8950487c313a6 2500w" />

## Verifying your VPC endpoint connectivity

1. **Confirm endpoint status**: In the AWS Console, verify that your endpoint's status shows "Available".

2. **Test DNS resolution**: From an EC2 instance in your configured VPC, run a DNS lookup to confirm resolution to your VPC's IP range. Use the `Private Host` you recorded earlier from the PlanetScale dashboard:

   ```bash  theme={null}
   dig +short <YOUR ENDPOINT>.private-pg.psdb.cloud
   10.0.2.120
   10.0.1.118
   ```

3. **Test your new connection**:

   Once you have confirmed DNS resolution, test the private endpoint:

   ```bash  theme={null}
   psql 'host=<YOUR ENDPOINT>.private-pg.psdb.cloud port=5432 user=postgres.XYZ234 password=pscale_pw_REDACTED dbname=postgres sslnegotiation=direct sslmode=verify-full sslrootcert=system'
   ```

## Update your connection strings

Once your VPC endpoint is established and verified, you're ready to update your application's connection strings to use the private endpoint address instead of the standard public endpoint.

## Security group considerations

Ensure your [security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) allow:

* **Outbound PostgreSQL (port 5432)**: For direct database connections
* **Outbound PSBouncer (port 6432)**: For pooled connections via PSBouncer
* **Inbound - any application-specific ports**: Based on your connection requirements

For more details about connection types and when to use each port, see our [connection documentation](/docs/postgres/connecting) and [PSBouncer guide](/docs/postgres/connecting/pgbouncer).

## Network ACL considerations

VPC [Network ACLs (NACLs)](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) operate at the subnet level and provide an additional layer of security beyond security groups. For AWS PrivateLink connections to PlanetScale, ensure your NACLs allow:

* **Outbound PostgreSQL (ports 5432, 6432)**: For database connections
* **Ephemeral ports (1024-65535)**: For return traffic from AWS PrivateLink endpoints

Most default NACL configurations allow all outbound traffic and are compatible with PrivateLink. If using custom restrictive NACLs, add explicit allow rules for the above ports.

## Troubleshooting

If you're experiencing connectivity issues:

1. **Verify endpoint status**: Ensure your VPC endpoint shows "Available" status
2. **Check security groups**: Confirm your security groups allow the required ports
3. **Check NACLs**: Confirm that your VPC's NACLs are configured to allow the correct network traffic
4. **Test DNS resolution**: Verify DNS is resolving to private IP addresses in your VPC CIDR range
5. **Use AWS Reachability Analyzer**: The [Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html) allows you to inspect the path between two resources (such as a client and your PlanetScale Postgres endpoint) and provides guidance on why connectivity might be failing
6. **Contact support**: If issues persist, contact PlanetScale support with your endpoint configuration details

## Next steps

* [Learn about PostgreSQL roles and permissions](/docs/postgres/connecting/roles)
* [Configure connection pooling with PSBouncer](/docs/postgres/connecting/pgbouncer)
* [Monitor your connections and performance](/docs/postgres/monitoring/query-insights)

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt