# Source: https://render.com/docs/private-link.md

# Private Link Connections — Securely connect your Render infrastructure to AWS-hosted cloud services.


> *Private links require a Professional workspace or higher.* [See pricing.](/pricing)

You can create *private links* in your workspace to securely connect your infrastructure to non-Render providers hosted on AWS:

[image: Diagram of a private link connection]

Use a private link to connect to:

- AWS-hosted providers like Snowflake or MongoDB Atlas
- Resources in your own AWS VPC, such as an EC2 instance or an Aurora database

You create _same-region_ private links (e.g., Virginia-to-Virginia) directly in the Render Dashboard.

## Setup

Creating a private link requires setup both in the Render Dashboard _and_ with the provider you're linking to:

### 1. Render

1. Open the [Render Dashboard](https://dashboard.render.com).

2. From your workspace home, select *Private Links* in the left pane.

   [image: Creating a private link in the Render Dashboard]

3. Click *Create Private Link*. The creation form appears:

   [image: The private link creation form in the Render Dashboard]

4. Copy the value of the *ARN Principal* field.
   - Some systems use this value to authorize the incoming private link connection.

### 2. External provider

1. Open your provider's dashboard.

2. Create a *VPC endpoint service* in the same region as the resource you're linking to.

   *This process varies by provider.* See guidance for popular providers in the tabs below:

**MongoDB Atlas**

#### MongoDB Atlas

> *Your MongoDB Atlas cluster must be hosted on AWS.*

1. In the [Atlas UI](https://cloud.mongodb.com), select the project containing your cluster and open its *Network Access* page.

2. Select the *Private Endpoint* tab:

   [image: The Private Endpoint tab in the Atlas UI]

3. Click *Add Private Endpoint*.

   The endpoint creation dialog appears.

4. Under *Cloud Provider*:

   - Select *AWS*.
   - Select the same region where your cluster is hosted.

5. Under *Interface Endpoint*, wait for your endpoint service to become ready:

   [image: The Interface Endpoint tab in the Atlas UI]

6. Close the endpoint creation dialog (you'll finish configuring the endpoint later).

   Your new endpoint appears in the *Private Endpoint* tab:

   [image: The Private Endpoint tab in the Atlas UI]

7. Copy your new endpoint's *Atlas Endpoint Service* value.

   You'll provide this value to Render in the next step.

**Snowflake**

#### Snowflake

As described in the [Snowflake documentation](https://docs.snowflake.com/en/user-guide/admin-security-privatelink#enabling-aws-privatelink), authorizing a managed cloud service like Render first requires contacting Snowflake support.

In your message to Snowflake support:

- Request a *VPC endpoint service* in the same AWS region as your Snowflake database.
- Provide the *ARN Principal* value you copied in the Render Dashboard.
- Request the name of the created VPC endpoint service. The service name resembles the following:

  ```
  com.amazonaws.vpce.us-east-1.vpce-svc-abc123...
  ```

You'll provide the endpoint service name to Render in the next step.

Also complete any additional actions indicated by Snowflake support.

**Self-managed VPC (EC2, Aurora, etc.)**

#### Self-managed VPC (EC2, Aurora, etc.)

1. Follow the steps in the AWS documentation to [create an endpoint service](https://docs.aws.amazon.com/vpc/latest/privatelink/create-endpoint-service.html#create-endpoint-service-nlb) in your VPC.

   - To simplify connecting later, disable the *Require acceptance for endpoint* option.
   - Your private link will only be able to access resources that are registered to the network load balancer (NLB) you apply to your endpoint service.

2. Follow the steps in the AWS documentation to [allow a principal](https://docs.aws.amazon.com/vpc/latest/privatelink/configure-endpoint-service.html) for your endpoint service.

   - Provide the *ARN Principal* value you copied in the Render Dashboard.
   - By adding an allowed principal this way, your endpoint service rejects connections from other principals.

3. Copy the name of your new endpoint service. This value resembles the following:

   ```
   com.amazonaws.vpce.us-east-1.vpce-svc-abc123...
   ```

You'll provide this value to Render in the next step.

### 3. Render

1. Return to the private link creation form in the [Render Dashboard](https://dashboard.render.com):

   [image: The private link creation form in the Render Dashboard]

2. Provide a *Name* and *Description* for your private link.

   - These values are for your team's reference only.

3. Provide the *VPC Endpoint Service Name* you obtained from your provider.

   This value resembles the following:

   ```
   com.amazonaws.vpce.us-east-1.vpce-svc-abc123...
   ```

   The *Region* field automatically populates based on the provided value.

4. Under *Access Policy*, choose either *Allow All* or *Limit to Selected Environments*:

------

###### Access Policy

*Allow All*

###### Description

All of your services hosted in the same region as the private link can access it.

---

###### Access Policy

*Limit to Selected Environments*

###### Description

You specify which of your [project environments](projects) can access the private link. A service can access the private link if _both_ of the following are true:

   - The service belongs to one of the selected environments.
   - The service is hosted in the same region as your private link.

------

5. Click *Create Private Link*.

   Your browser redirects to your private link's details page:

   [image: The private link creation form in the Render Dashboard]

   For now, your private link has the status *Pending Acceptance*.

6. Copy your private link's *AWS ID*.

   You might need to provide this value to your provider in the next step.

### 4. External provider

1. Return to your provider's dashboard.

2. Finalize your connection according to your provider:

**MongoDB Atlas**

#### MongoDB Atlas

1. In the [Atlas UI](https://cloud.mongodb.com), return to the *Private Endpoint* tab for your project.

2. Click the *Edit* button for your endpoint. The in-progress endpoint creation dialog appears.

3. Advance to the *Finalize Endpoint Connection* tab:

   [image: The Finalize Endpoint Connection tab in the Atlas UI]

4. In the *Your VPC Endpoint ID* field, provide the *AWS ID* value you copied in the Render Dashboard.

5. Click *Create*.

MongoDB Atlas begins deploying your finalized endpoint. When the deploy completes, your endpoint's status updates to available in both the Atlas UI and the Render Dashboard:

[image: A MongoDB Atlas endpoint with status "Available"]

You're ready to start [connecting](#connecting-from-your-render-services) from your Render infrastructure.

**Snowflake**

#### Snowflake

If required, contact Snowflake support to finalize your connection (such as by authorizing Render's incoming private link connection).

When the connection is finalized, your private link's status updates to *Available* in the Render Dashboard:

[image: A private link with status "Available"]

You're ready to start [connecting](#connecting-from-your-render-services) from your Render infrastructure.

**Self-managed VPC (EC2, Aurora, etc.)**

#### Self-managed VPC (EC2, Aurora, etc.)

If your endpoint service requires accepting incoming connections, follow the steps in the AWS documentation to [accept the incoming connection](https://docs.aws.amazon.com/vpc/latest/privatelink/configure-endpoint-service.html#accept-reject-connection-requests) from Render.

When the connection is finalized, your private link's status updates to *Available* in the Render Dashboard:

[image: A private link with status "Available"]

You're ready to start [connecting](#connecting-from-your-render-services) from your Render infrastructure.

## Connecting from your Render services

After your private link is fully established, you can start connecting to your provider from your Render infrastructure.

To connect to a particular resource, use its private connection URL from your provider:

**MongoDB Atlas**

#### MongoDB Atlas

1. In the [Atlas UI](https://cloud.mongodb.com), select your cluster and open its *Connect* dialog:

   [image: Selecting a connection method in the Atlas UI]

2. Select the *Private Endpoint* connection type.

3. Select whichever connection method your Render service will use (usually a language-specific driver). All displayed methods will use the private connection URL accessible via your private link.

4. Apply the corresponding changes to your Render service and deploy.

**Snowflake**

#### Snowflake

Your Render services can connect to Snowflake using your Snowflake *private connectivity URL*. For details, see the [Snowflake docs.](https://docs.snowflake.com/en/user-guide/organizations-connect#private-connectivity-urls)

**Self-managed VPC (EC2, Aurora, etc.)**

#### Self-managed VPC (EC2, Aurora, etc.)

To connect to a particular resource (such as an EC2 instance or Aurora cluster):

1. In the AWS console, find the private DNS name or IP address of the resource, as registered with your endpoint service’s network load balancer (NLB).
2. Update your Render service’s configuration to use this private DNS name or IP address.
3. Deploy your Render service.

## Limitations

- Private links require a *Professional* workspace or higher.
- By default, a workspace can have up to three private links.
  - If you require additional private links, please [contact us](/contact).
- Private links support connections initiated _from_ your Render infrastructure _to_ an external provider, but not the reverse.
- Your external provider must be hosted in an AWS VPC.
- Your external provider must support creating a VPC endpoint service.
- Certain Render customers might not be able to create private links in the Oregon region.
  - If you encounter this issue, please reach out to support in the [Render Dashboard](https://dashboard.render.com?contact-support).
- You can currently only create private links in the same region as the VPC endpoint service you're linking to.

  - Your services in other regions cannot access the private link:

    [image: Diagram of a private link connection]

