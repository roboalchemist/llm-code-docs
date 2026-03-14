# Source: https://docs.fiddler.ai/reference/settings/aws-vpl-setup.md

# AWS Virtual PrivateLink Setup

{% hint style="info" %}
**Automated Setup Available**: We now provide an automated script that simplifies the VPC endpoint creation process. For most users, we recommend using the [AWS VPC Endpoint Automation Script](https://docs.fiddler.ai/reference/settings/aws-vpc-endpoint-setup) instead of this manual process. This guide remains available for reference, troubleshooting, and those who prefer manual configuration.
{% endhint %}

This guide illustrates configuring an AWS Virtual PrivateLink (VPL) between your company VPC and Fiddler Cloud environment to establish secure communication channels.

{% hint style="info" %}
Fiddler Customers must complete these steps only after the Fiddler team has completed the customer's private-link-based environment deployment.
{% endhint %}

{% hint style="warning" %}
Your Fiddler environment will use the private DNS name: `<customer-subdomain>.cloud.fiddler.ai`, where `<customer-subdomain>` is typically your company name. If you have specific subdomain requirements or restrictions, notify your Fiddler representative before VPL configuration.
{% endhint %}

## Prerequisites

* AWS account with VPC access
* Fiddler-provided service name
* Fiddler-provided DNS name
* VPC CIDR range information
* Appropriate AWS IAM permissions to create VPC endpoints

## Step 1: Navigate to the AWS VPC Console

1. Log in to your AWS Management Console
2. Navigate to the VPC service
3. In the left navigation panel, click on "Endpoints"
4. Click the Create endpoint button

![Create an endpoint](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-0d4a43775d32075ca6a9e57bba66ba037cd3216d%2Fvpl-step1.png?alt=media)

## Step 2: Configure the Fiddler Endpoint Service

1. Enter a descriptive name tag for your endpoint
2. Select "PrivateLink Ready partner services" from the service categories
3. Enter the Fiddler-provided service name
4. Click Verify Service to confirm the service details

{% hint style="warning" %}
Fiddler will provide the service name before you proceed with this step. Contact your Fiddler representative if you haven't received this information.
{% endhint %}

![Provide the endpoint service name](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-6824843bc3d36b13298e0fb15f20d4ce4fd8b120%2Fvpl-step2.png?alt=media)

## Step 3: Select VPC and Subnets

1. Select your VPC from the dropdown
2. Choose all subnets where your client applications are running
3. Ensure the selected subnets have appropriate routing within your VPC to the endpoint

![Select the VPC](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-facde798ccd3d5d0fc12851a1abc44585abeec20%2Fvpl-step3.png?alt=media)

## Step 4: Configure Security Group

1. Create a new security group if one doesn't exist
2. Add an inbound rule to allow:
   * Port: 443 (HTTPS)
   * Source: Your VPC CIDR range
3. Select the security group ID to associate with the endpoint

### Example security group configuration:

* Inbound rule: TCP 443 from VPC CIDR
* Outbound rule: All traffic (default)

![Create a new security group](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-2565f02f39c6b00f017169d6a5e2647af00ed45e%2Fvpl-step4.png?alt=media)

## Step 5: Create the Endpoint

1. Review all configuration settings
2. Click Create endpoint to initiate the endpoint creation
3. Wait for the endpoint status to change to "Available"

## Step 6: Configure Private DNS

1. Select the newly created endpoint
2. From the Actions menu, choose "Modify private DNS name"
3. Enable private DNS names by checking the "Enable for this endpoint" checkbox
4. **Important**: The private DNS name will be in the format: `<customer-subdomain>.cloud.fiddler.ai`
   * Example: If your company name is "acme", the DNS name would be `acme.cloud.fiddler.ai`
5. Click Save changes

{% hint style="info" %}
Once enabled, AWS will automatically configure DNS resolution for your assigned Fiddler subdomain in the format `<customer-subdomain>.cloud.fiddler.ai`.
{% endhint %}

![Select action "Modify the private DNS name"](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-8808bc020ce8f3d6a19a0b08dc44627f298d8c3a%2Fvpl-step6.png?alt=media)

![Modify the private DNS name](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-85077220cee0bbd0b9bfb9873761eda2ff20f2b0%2Fvpl-step7.png?alt=media)

## Step 7: Verify Configuration

1. Wait for the endpoint status to show as "Available"
2. Verify that the private DNS name is enabled
3. Confirm the security group rules are properly configured

## Step 8: Access Fiddler

Once the configuration is complete, you can access the Fiddler UI within your VPC using the configured DNS name:

`https://<customer-subdomain>.cloud.fiddler.ai`

## Troubleshooting

If you encounter issues:

* Verify the endpoint status in the AWS console
* Check security group rules and network ACLs
* Confirm DNS resolution within your VPC
* Contact Fiddler support with your endpoint ID and any error messages

## Next Steps

* For automated setup, see the [AWS VPC Endpoint Automation Script](https://docs.fiddler.ai/reference/settings/aws-vpc-endpoint-setup)
* [Configure your applications to use the private endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html)
* [Set up monitoring for the VPL connection](https://docs.aws.amazon.com/vpc/latest/userguide/monitoring.html)
* [Review security best practices](https://docs.aws.amazon.com/vpc/latest/userguide/security.html)
