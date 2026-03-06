# Source: https://northflank.com/docs/v1/application/bring-your-own-cloud/configure-static-egress-ips.md

# Configure static egress IPs

Static egress IPs allow you to configure fixed IP addresses for outbound traffic from pods on private subnets in your BYOC cluster. This is useful when you need to whitelist your cluster's IP in third-party services, meet security requirements, or configure firewall rules for external API access.

This guide covers manual configuration of static egress IPs for AWS and GCP BYOC clusters.

## AWS setup

### Option 1: Using an existing VPC

If you have an existing VPC, follow these steps to configure static egress IPs.

#### 1. Allocate an Elastic IP

1. Navigate to the [AWS EC2 Console - Elastic IPs](https://console.aws.amazon.com/vpcconsole/home#AllocateAddress)

2. Click **Allocate Elastic IP address**

3. Select **Amazon's pool of IPv4 addresses**

4. Click **Allocate**

5. Note the allocated IP address

#### 2. Create a private subnet

The private subnet will host your EKS pods and route egress traffic through a NAT gateway. Use a sufficiently large CIDR range as each pod receives an IP from this subnet.

1. Navigate to the [AWS VPC Console - Subnets](https://console.aws.amazon.com/vpcconsole/home#CreateSubnet:)

2. Click **Create subnet**

3. Select your VPC

4. Configure the subnet:
  
  
  - **Name**: e.g., `northflank-private-subnet`
  
  - **Availability Zone**: Choose an AZ
  
  - **IPv4 CIDR block**: Use at least a `/20` range (4,094 available addresses)

5. Click **Create subnet**

6. After creation, select the subnet and verify **Auto-assign public IPv4 address** is **disabled**

#### 3. Ensure you have a public subnet

Your VPC needs a public subnet to host the NAT gateway.

1. Navigate to the [AWS VPC Console - Subnets](https://console.aws.amazon.com/vpcconsole/home#CreateSubnet:)

2. Check if you have a public subnet. Using the same Availability Zone as your private subnet is recommended for optimal routing, but optional.

3. Create a public subnet (or create a new one for better separation of concerns):
  
  
  - Click **Create subnet**
  
  - Select your VPC
  
  - Configure:
    
    
    - **Name**: e.g., `northflank-public-subnet`
    
    - **Availability Zone**: Same AZ as private subnet (recommended)
    
    - **IPv4 CIDR block**: e.g., `10.0.0.0/24`
  
  - Click **Create subnet**

4. After creation, select the subnet and verify **Auto-assign public IPv4 address** is **enabled**

#### 4. Configure internet gateway

1. Navigate to the [AWS VPC Console - Internet Gateways](https://console.aws.amazon.com/vpcconsole/home)

2. If your VPC doesn't have an internet gateway:
  
  
  - Click **Create internet gateway**
  
  - Provide a name
  
  - Click **Create**
  
  - Select the gateway and click **Actions** → **Attach to VPC**
  
  - Select your VPC and attach

3. Verify the public subnet's route table:
  
  
  - Navigate to [Route Tables](https://console.aws.amazon.com/vpcconsole/home:)
  
  - Find the route table associated with your public subnet
  
  - Ensure it has a route: `0.0.0.0/0` → Internet Gateway

#### 5. Create a NAT gateway

1. Navigate to the [AWS VPC Console - NAT Gateways](https://console.aws.amazon.com/vpcconsole/home#CreateNatGateway)

2. Click **Create NAT gateway**

3. Configure:
  
  
  - **Name**: e.g., `northflank-nat-gateway`
  
  - **Subnet**: Select the **public subnet** from step 3
  
  - **Connectivity type**: **Public**
  
  - **Elastic IP allocation ID**: Select the Elastic IP from step 1

4. Click **Create NAT gateway**

#### 6. Create a route table

1. Navigate to the [AWS VPC Console - Route Tables](https://console.aws.amazon.com/vpcconsole/home#CreateRouteTable:)

2. Click **Create route table**

3. Configure:
  
  
  - **Name**: e.g., `northflank-private-route-table`
  
  - **VPC**: Select your VPC

4. Click **Create**

5. After creation, select the route table:
  
  
  - Click **Routes** tab → **Edit routes**
  
  - Add a route: `0.0.0.0/0` → NAT Gateway (select the NAT from step 5)
  
  - Save routes

6. Click **Subnet associations** tab → **Edit subnet associations**

7. Select the **private subnet** from step 2

8. Save associations

### Option 2: Creating a new VPC

If you're creating a new VPC:

1. Use the [AWS VPC creation wizard](https://console.aws.amazon.com/vpcconsole/home)

2. Select **VPC and more**

3. Configure to include:
  
  
  - At least one **private subnet**
  
  - **NAT Gateway** in a public subnet

4. The wizard will automatically configure routing

5. Note the private subnet ID for use in Northflank

### Configure Northflank cluster

Once your AWS networking is configured:

1. Create a new AWS BYOC cluster in Northflank

2. Select **Custom VPC** mode

3. For each node pool that should use the static egress IP:
  
  
  - Select the **private subnet** you created

4. Deploy the cluster

All egress traffic from pods in the private subnet will route through the NAT gateway using your static Elastic IP.

## GCP setup

### 1. Select a VPC

We recommend using your default VPC, which is pre-configured with the necessary networking settings.

If using a custom VPC, additional configuration (firewall rules, networking settings) may be required beyond this guide. See [GCP VPC documentation](https://cloud.google.com/vpc/docs/vpc) for details.

### 2. Enable Cloud NAT

1. Navigate to the [GCP Cloud NAT Console](https://console.cloud.google.com/net-services/nat/list)

2. Click **Create Cloud NAT gateway**

3. Configure:
  
  
  - **Gateway name**: e.g., `northflank-nat`
  
  - **VPC network**: Select your VPC (default or custom)
  
  - **Region**: Select the region where your cluster will run
  
  - **Cloud Router**: Create a new router or select an existing one
  
  - **NAT mapping**: Select the subnet you want to use
  
  - **NAT IP addresses**: Select **Manual** and choose or create external static IP addresses

4. Click **Create**

The static IP addresses you selected will be used for all egress traffic from the specified subnet.

### 3. Configure Northflank cluster

When creating a new GCP BYOC cluster:

1. If using a custom VPC:
  
  
  - Select **Custom VPC** option
  
  - Choose your VPC and subnet

2. For node pools that should use the static egress IP:
  
  
  - Enable **Private node IPs**
  
  - Ensure the node pool is assigned to the subnet configured with Cloud NAT

All egress traffic from nodes with private IPs will route through Cloud NAT with your static IP addresses.

## Verify your setup

To verify your static egress IP is working:

1. Deploy a test service to your cluster with an image that has `curl` available (e.g., `alpine/curl:latest`)

2. Once the service is running, exec into the workload using:
  
  
  - **Northflank UI**: Navigate to the service → **Terminal** tab
  
  - **Northflank CLI**: Run `northflank exec <service-name>`

3. Run the following command to check your egress IP:

```bash
   curl api.ipify.org
```

1. Compare the returned IP address with your configured static IP:
  
  
  - **AWS**: Should match your Elastic IP from step 1
  
  - **GCP**: Should match one of the external static IPs configured in Cloud NAT

If the IPs match, your static egress configuration is working correctly.

## Troubleshooting

### AWS

**Traffic not routing through static IP:**

- Verify the private subnet is associated with the correct route table

- Check that the route table has `0.0.0.0/0` pointing to the NAT gateway

- Confirm node pools are deployed to the private subnet

**NAT gateway not working:**

- Ensure the NAT gateway is in a **public** subnet

- Verify the public subnet's route table has `0.0.0.0/0` pointing to the internet gateway

- Check that the Elastic IP is properly attached to the NAT gateway

### GCP

**Egress traffic using different IPs:**

- Verify Cloud NAT is configured for the correct VPC and subnet

- Ensure node pools have **private node IPs** enabled

- Check that the subnet matches the one configured in Cloud NAT

## Next steps

- [Deploy node pools: Configure and deploy node pools on a Kubernetes cluster with Northflank.](/v1/application/bring-your-own-cloud/deploy-and-scale-node-pools)
- [Deploy workloads to your cluster: Deploy services, jobs, and addons to your own cluster, and configure workloads to schedule on specific node pools.](/v1/application/bring-your-own-cloud/deploy-workloads-to-your-cluster)
- [Tag your workloads and resources: Create tags to assign to your Northflank workloads and resources to help keep track of them.](/v1/application/release/tag-workloads-and-resources)
- [Configure your Kubernetes cluster: Manage your clusters on other cloud providers using Northflank.](/v1/application/bring-your-own-cloud/configure-your-cluster)
