# Source: https://docs.unstructured.io/api-reference/legacy-api/aws.md

# Unstructured API on AWS

> Follow these steps to deploy the Unstructured API service into your AWS account.

<Warning>
  The Unstructured API on AWS is deprecated. It is no longer supported and is not being actively updated.
  Unstructured is now available on the AWS Marketplace as a private offering. To explore supported options
  for running Unstructured within your virtual private cloud (VPC), email Unstructured Sales at
  [sales@unstructured.io](mailto:sales@unstructured.io).

  This page is not being actively updated. It might contain out-of-date information. This page is provided for legacy reference purposes only.
</Warning>

<Warning>
  This article describes how to create several interrelated resources in your AWS account.
  Your AWS account will be charged on an ongoing basis for these resources, even if you are not actively using them.<br /><br />
  Manually stopping or terminating the associated Amazon EC2 instances alone will not reduce these ongoing charges.<br /><br />
  To stop accruing all related ongoing charges, you must delete all of the associated AWS resources.
  To do this, see [Manage related AWS account costs](#manage-related-aws-account-costs).
</Warning>

*Estimated time to complete: 30 minutes*

The requirements are as follows.

1. **An AWS account**:

   * If you have an existing account, log in: [https://aws.amazon.com/](https://aws.amazon.com) > **Sign In to the Console**.

   * If you do not have an existing account, create one: [https://aws.amazon.com/free](https://aws.amazon.com/free) > **Create a Free Account**.

2. **IAM permissions**: In a later step, AWS CloudFormation creates required infrastructure in your account. To learn how to create the associated role, see [Creating IAM Roles with AWS CloudFormation](https://blog.awsfundamentals.com/aws-iam-roles-with-aws-cloudformation#heading-creating-iam-roles-with-aws-cloudformation).

3. **SSH key pair**: For secure access to the Amazon EC2 instance that CloudFormation creates in a later step, create an SSH key pair. To learn how, see [Create a key pair for your Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html).

## Part I: Setting up the Virtual Private Cloud (VPC)

*Note: If you have already configured a Virtual Private Cloud (VPC) for your organization that meets the requirements for deploying the Unstructured API, you may skip this part and proceed to the Part II. Ensure that your existing VPC setup includes the necessary subnets, internet gateway, and route tables as outlined in this guide.*

In Part I, you will construct a resilient and secure infrastructure within AWS by setting up a Virtual Private Cloud (VPC). Your VPC will encompass a dual-tiered subnet model consisting of both **public** and **private** subnets across multiple Availability Zones (AZs).

You will establish the foundational network structure for deploying the Unstructured API by creating two public subnets and one private subnet within your VPC. The public subnets will host resources that require direct access to the internet, such as a load balancer, enabling them to communicate with external users. The private subnet is designed for resources that should not be directly accessible from the internet, like EC2 Compute Engine.

<img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Infrastructure_Diagram.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=6dd574f63ada8a4ea2c1248ec4461536" alt="Infrastructure Diagram" data-og-width="2088" width="2088" data-og-height="1478" height="1478" data-path="img/api/Infrastructure_Diagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Infrastructure_Diagram.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=298b335bce5b6e1faa8121d412d1ac55 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Infrastructure_Diagram.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=965c6d0b2bcfe15d87695a51e1feb140 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Infrastructure_Diagram.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=b9cdd369734cc828e9f8943d1d07eb06 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Infrastructure_Diagram.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=bfb9153e118ba68dcb0c42cb4ca6825b 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Infrastructure_Diagram.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=0a5568932d0d0bc31bcb94e07f28b43a 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Infrastructure_Diagram.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=ebabedb483d15e2bdd969fdec8ae5bf0 2500w" />

1. **Access the VPC dashboard**:

   a.   In the AWS Management Console, in the top menu bar, click **Services > Networking & Content Delivery > VPC**.<br />

   b.   In the sidebar, click **Your VPCs**, and then click **Create VPC**.<br />

2. **Create the VPC**:

   a.   Select **VPC only**.<br />

   b.   Enter a **Name tag** for your VPC.<br />

   c.   Specify the **IPv4 CIDR block** (for example, `10.0.0.0/16`).<br />

   d.   You may leave **IPv6 CIDR block**, **Tenancy**, and **Tags** settings at their defaults.<br />

   e.   Click **Create VPC**.

<img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step2.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=ec11326c56aa24f0838eaaad3604d387" alt="create vpc" data-og-width="1340" width="1340" data-og-height="1698" height="1698" data-path="img/api/VPC_Step2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step2.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=f317928d55d4fca07264c1f48fb35039 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step2.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=9bd7e325d615610ce83257e400694c74 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step2.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=cd06c656301599b621fd40e57237bd54 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step2.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=65f628ddceb01d144f3fb3d5d54f6e3a 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step2.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=c9767dbf0e89f28b848e9d7b3ff080b6 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step2.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=c2e552f6597dc824ed4820cac7595fe8 2500w" />

3. **Create the subnets**:

   a.   After creating the VPC, in the sidebar, click **Subnets**.<br />

   b.   Click **Create subnet**.<br />

   c.   In the **VPC ID** dropdown menu. select the VPC that you just created.<br />

   d.   For the first public subnet:<br />

   * Enter a **Subnet name**.

   * Select an **Availability Zone**.

   * Specify the **IPv4 CIDR block** (for example, `10.0.0.0/16`).

   * Specify the **IPv4 subnet CIDR block** (for example, `10.0.1.0/24`).

   * You may leave the **Tags** setting at its default.

   * Click **Add new subnet**. (Do not click **Create subnet** yet.)

   e.  Repeat the process for the second public subnet with a different **Availability Zone** and **IPv4 subnet CIDR block** (for example, `10.0.2.0/24`).<br />

   * *Note: Each subnet must reside entirely within one Availability Zone and cannot span zones. If you specify the same Availability Zone or IPv4 subnet CIDR block as the first public subnet, AWS CloudFormation might fail in a later step*.

   * To learn more, see [Subnet basics](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html#subnet-basics).

   * Click **Add new subnet**. (Do not click **Create subnet** yet.)

   f.  Repeat the process for the private subnet with a different **Availability Zone** and **IPv4 subnet CIDR block** (for example, `10.0.3.0/24`).<br />

   * *Note: Each subnet must reside entirely within one Availability Zone and cannot span zones. If you specify the same Availability Zone or IPv4 subnet CIDR block as the first or second public subnets, AWS CloudFormation might fail in a later step*.

   g.  Click **Create subnet**.

<img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step3.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=1baf235fd52b412b1a733a0d7b5788ff" alt="create subnet" data-og-width="1340" width="1340" data-og-height="1850" height="1850" data-path="img/api/VPC_Step3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step3.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=bfe8f00995bd3642dbc5cf6c9f89d795 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step3.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=125f69689164792df79118888773acc7 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step3.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=dcbc06f6ec68c0b617fb07c52212fbe5 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step3.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=2598e2744d4733a26e7077b04a7247e1 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step3.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=21faa5f03f0671ce3d986a6ccf264a8e 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step3.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=f0cfa2b855311b69d457425b052cbe91 2500w" />

4. **Create the internet gateway (for the public subnets)**:

   a.   In the sidebar, click **Internet gateways**.<br />

   b.   Click **Create internet gateway**, enter a **Name tag**, and click **Create internet gateway**.<br />

   c.   In the sidebar, click **Internet gateways** again.<br />

   d.   Click the **Internet gateway ID** for the internet gateway that you just created.<br />

   e.   Click **Actions > Attach to VPC**.<br />

   f.   In the **Available VPCs** dropdown list, select the VPC from *Step 2 - Create the VPC*.<br />

   g.   Click **Attach internet gateway**.<br />

<img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step4.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=7e167f41fbed50320e5c4a87777a66ec" alt="create internet gateway" data-og-width="1326" width="1326" data-og-height="944" height="944" data-path="img/api/VPC_Step4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step4.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=af27fa1a7b0fdc2e240585d9ce128dee 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step4.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=4b7a5acf5d8e560842caf3946fa92621 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step4.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=69cd5ee12fe1437362de5e53590a2934 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step4.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=1419674cdc06b3ac8dbf95a05c9f76c9 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step4.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=de76c03570d7a886f1696685a00038e0 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step4.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=73a9829da8f72bd480d28ca079858f25 2500w" />

5. **Set up route tables (for the public subnets)**:

   AWS automatically created a default route table in *Step 3 - Create the subnets*. To tailor your network architecture, you will create a new route table specifically for your public subnets, which will include a route to the internet gateway from *Step 4 - Create the internet gateway (for the public subnets)*.

   a.   In the sidebar, click *Route tables*.

   b.   Click **Create route table**.

   c.   Enter a **Name**.

   d.   Select the **VPC** from *Step 2 - Create the VPC*.

   e.   Click **Create route table**.

<img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step5.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=9d5ddaee0513a9e596cb0a820fb5adae" alt="create route table" data-og-width="1326" width="1326" data-og-height="1062" height="1062" data-path="img/api/VPC_Step5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step5.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=c18deda746ff5d2dcf219147220985a5 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step5.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=914bbad7f28cbe6e866ec6e4d399463c 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step5.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=909f440ff51c8c64d055630d796e745d 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step5.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=426d21437b649615a21a29c66a4ee404 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step5.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=6041c172b3e28e5200c5f937097224e7 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step5.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=2d6bed52dc666962d931dc06ee0a3a0e 2500w" />

6. **Associate public subnets to the route table and internet gateway**:

   a.  Connect the **public subnets** to the **route table** from *Step 5 - Set up route tables (for the public subnets)*:<br />

   * In the sidebar, click **Subnets**.

   * Select the first public subnet from *Step 3 - Create the subnets*.

   * Click **Actions > Edit route table association**.

   * In the **Route table ID** dropdown list, select the route table from *Step 5 - Set up route tables (for the public subnets)*, and then click **Save**.

   * Repeat the process for the second public subnet.

   b.   Now, you’ll ensure that the two public subnets can access the internet by connecting the route table to the internet gateway:<br />

   * In the sidebar, click **Route tables**.

   * Select the route table from *Step 5 - Set up route tables (for the public subnets)*.

   * Click **Actions > Edit routes**.

   * Click **Add route**, in the destination box, enter `0.0.0.0/0`, which represents all IP addresses. In the **Target** dropdown list, select **Internet Gateway**, and select the internet gateway from *Step 4 - Create the internet gateway (for the public subnets)*.

   * Click **Save changes** to establish the route, granting internet access to the first and second public subnets at the same time.

   c.  For the **private subnet**:

   * In the sidebar, click **Subnets**.

   * Select the private subnet from *Step 3 - Create the subnets*.

   * Click **Actions > Edit route table association**.

   * In the **Route table ID** dropdown list, select the main route table, or create and then select a new route table without a route to the internet gateway.

   * Click **Save**.

<img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step6.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=44b90b3777420721b5d502228dd4ed8c" alt="connect public subnet to route table" data-og-width="1334" width="1334" data-og-height="834" height="834" data-path="img/api/VPC_Step6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step6.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=d68aafa51b86619a77128cf8a3c02db1 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step6.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=ecda8e5c7956357209d9e2e2c8747c0a 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step6.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=180e69db53924751b2af2cea456f6354 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step6.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=b59a23a24f4a778f8d13ff993ce9fc41 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step6.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=8e65504ccdc66c72108328bf6b9a77bf 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step6.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=5c3a7a558c997cef4fd937f1e362e1bd 2500w" /> <img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step7.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=160ebfaf0730506745e011ee1a7d2c56" alt="edit routes" data-og-width="3284" width="3284" data-og-height="744" height="744" data-path="img/api/VPC_Step7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step7.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=6a57cfa0ce475043af725aa3c49fb8c7 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step7.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=6c569a7a22b1b4b327d21e289d5d7666 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step7.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=a39262104d7fc2b18a439f5d95f19577 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step7.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=93da0d4e428ae09a3611028d089e84b8 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step7.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=dc7626b09cac4c0aa0e31ee4eb75ecd2 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step7.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=62ca818f5b757b4ffb5f087bc4a4ebaa 2500w" />

7. **Inspect the VPC resource map**:

   You can check the configurations from the resource maps on the VPC details dashboard by clicking **Your VPCs** in the sidebar, clicking the **VPC ID** for your VPC, and then clicking the **Resource map** tab.

<img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step8.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=72bb4ba6007ff4308ce76b1b6690bc7e" alt="VPC Resource Maps" data-og-width="1501" width="1501" data-og-height="935" height="935" data-path="img/api/VPC_Step8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step8.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=9cbb420954d0cb0a890b3b25430a79ca 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step8.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=e8a7bd344403f486374023b5d2a6d73c 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step8.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=dbe6bf2217039fa4d8fa34e62bbc77d4 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step8.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=283356cefe4b05f9a32e7e442066ff64 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step8.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=7d8539b851a0e240ff61c7d65d40a246 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/VPC_Step8.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=8ab95cea25499be809892ca3fea736c0 2500w" />

## Part II: Deploying the Unstructured API from the AWS Marketplace

8. **Go to the Unstructured API page on AWS Marketplace**:

   a.   Leaving the VPC dashboard from Part I open, in a separate web browser tab, go to the [Unstructured API](http://aws.amazon.com/marketplace/pp/prodview-fuvslrofyuato) product page in the AWS Marketplace.

   b.   Click **Continue to Subscribe**.

   c.   Review the terms and conditions.

   d.   Click **Continue to Configuration**.

<img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step8.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=f917128bf235ad278165a22371a1db01" alt="Unstructured API on AWS Marketplace" data-og-width="2688" width="2688" data-og-height="1722" height="1722" data-path="img/api/Marketplace_Step8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step8.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=842ddd37d49dc03570a72206bcca829d 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step8.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=2ac18dc33fb9f575bae3380c6d71a71e 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step8.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=e9204ef02addcadce8dad701982a1bc5 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step8.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=53ee50a48bfce72634a2d80b315ac75e 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step8.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=515565fa94d448d535d01c440dbf4b8d 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step8.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=c7fe3e74bc133216f5348ad854620059 2500w" />

9. **Configure the CloudFormation template**:

   a.   In the **Fulfillment option** dropdown list, select **CloudFormation Template**.

   b.   For **Fulfillment option** and **Software version**, leave the default `UnstructuredAPI` template and software version.

   c.   In the **Region** dropdown list, select the Region that corresponds to the VPC from Part I.

   * *Note: You must select the same Region where you set up the VPC in Part I. To find the Region, on the VPC dashboard tab from Part I that you left open, with your VPC displayed, find the VPC's Region name next to your username in the top navigation bar.*

   d.   Click **Continue to Launch**.

   e.   In the **Choose Action** dropdown list, select **Launch CloudFormation**.

   f.   Click **Launch**.

<img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step9.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=a4ecd07c1df8e06747d3e88e2f31a614" alt="CloudFormation Configuration" data-og-width="1678" width="1678" data-og-height="1728" height="1728" data-path="img/api/Marketplace_Step9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step9.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=2ab7c0fef6e88588249b553d0de27d9d 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step9.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=8d055fd66d48af28c9c74aa2387e6a3b 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step9.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=1c29476ac110afa9cc2152e9ab429ece 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step9.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=f2586baa3040283c00cbeb8d9cec2dd0 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step9.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=301da88a3d88a3395e8aa1b145ea4b58 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step9.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=7c8f0d181bc33616d212f9fdae382afb 2500w" />

10. **Create the CloudFormation stack**:

After you click **Launch**, the **Create stack** page appears in CloudFormation.

**Step 1: Create the stack**

a.   Leave **Choose an existing template** selected.

b.   Leave **Amazon S3 URL** selected and the default **Amazon S3 URL** value unchanged.

c.   Click **Next**.

<img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10a.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=df9dbb66b39813cdc1fca56e6a27f040" alt="Create Stack" data-og-width="2782" width="2782" data-og-height="1196" height="1196" data-path="img/api/Marketplace_Step10a.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10a.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=321e94978b34a415ac1127726c2ee6a9 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10a.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=44fd78cdd9fbd15141908ae13bdc8945 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10a.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=6083acef9241f3608e7ffb95ea9e04b5 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10a.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=6d25e0a24a0343712edb289dcddf7620 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10a.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=b239a366f69e2de22d6d4ab5aaffd29b 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10a.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=86e60b6d8f4150cc9321429c3746ecd9 2500w" />

**Step 2: Specify the stack's details**

a.   Enter some unique **Stack name**.

b.   In the **Parameters** section, in the **InstanceType** drop-down list, select **m5.xlarge**.

c.   In the **KeyName** drop-down list, select the name of the SSH key pair from the beginning of this article.

d.   In the **LoadBalancerScheme** dropdown list, select **internet-facing**.

e.   For **SSHLocation**, enter `0.0.0.0/0`, but only if you allow public access on the internet.

* **Note**: It is generally recommended to limit SSH access to a specific IP range for enhanced security. This can be done by setting the `SSHLocation` to the IP address or range associated with your organization. Please consult your IT department or VPN vendor to obtain the correct IP information for these settings.

* AWS provides `AWS Client VPN`, which is a managed client-based VPN service that enables secure access AWS resources and resources in your on-premises network. To learn more, see [Getting started with AWS Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-getting-started.html).

f.   In the **Subnets** dropdown multiselect list, select the two public subnets and the private subnet from Part I.

g.   In the **VPC** dropdown list, select the VPC from Part I.

h.   You can leave the default values for all of the other **Parameters** fields.

i.   Click **Next**.

<img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10b.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=78c899b28a5c867d8210213152c6206f" alt="Specify stack details" data-og-width="2376" width="2376" data-og-height="1848" height="1848" data-path="img/api/Marketplace_Step10b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10b.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=49b31ba13ddc4f5326fae932910c6b3c 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10b.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=848f8934e3059ae1d2f597ef20a18c26 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10b.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=226a869b90bff97afa9cb7270ee21312 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10b.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=c817a66c3e77ddd7ba0762a6d3b87f0e 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10b.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=814d5d0253759e0bbf4532f7c98a6daf 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10b.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=d4c9a1a0ca146e2e8d526992b0516872 2500w" />

**Step 3: Configure the stack's options**

a.   You can leave the default values, or specify any non-default stack options.

b.   Click **Next**.

<img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10c.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=deeac8275caba0cffda00601572eb8be" alt="Specify stack options" data-og-width="2376" width="2376" data-og-height="1848" height="1848" data-path="img/api/Marketplace_Step10c.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10c.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=7f3f892a5a9538d49cc0afbd9d1915d8 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10c.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=4442dda77bbf14c604cdebf56ebfb156 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10c.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=0487a07fd6d5a9a7e5e7bfc099e4b930 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10c.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=dab2677ebd390441404be78552185fe5 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10c.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=ece043912024317b8aa5bf67947d0f34 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10c.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=a55831e84fe155c737ed1297d2ed8d31 2500w" />

**Step 4: Review**

a.   Review the stack's settings.

b.   Click **Submit**.

<img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10d.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=d520dd22e3b3a4654da461aa05164108" alt="Review stack" data-og-width="2376" width="2376" data-og-height="1848" height="1848" data-path="img/api/Marketplace_Step10d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10d.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=2ebcddc1d77fce816981e0f2c25256ad 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10d.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=77348d02e1944e0c3e0011042d002bfb 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10d.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=3ee3a4bee2a82c7f714271f892b3bda9 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10d.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=3293532d31e83c80084c9b3fb16e8d20 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10d.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=a38b5acd675d92d868b778a10977ac69 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step10d.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=1a8d8a2ffb236820a50dc75532ca23cd 2500w" />

11. **Get the Unstructured API endpoint**:

a.   The CloudFormation details page for the stack appears. If you do not see it, on the sidebar, click **Stacks**, and then click the name of your stack.

b.   Check the status of the CloudFormation stack. A successful deployment will show a **CREATE\_COMPLETE** value for the **Status** field on the **Stack Info** tab on this stack's details page. The deployment can take several minutes.

c.   After a successful deployment, click the **Resources** tab on this stack's details page. Then click the **Physical ID** link next to **ApplicationLoadBalancer** on this tab.

d.   On the **EC2 > Load balancers > (Load balancer ID)** page that appears, copy the **DNS Name** value, which is shown as an **(A Record)** and ends with `.elb.amazonaws.com`.

* Note: You will use this **DNS Name** to replace the `<application-load-balancer-dns-name>` for the following healthcheck and data processing steps.

<img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step11.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=36a0ab8636ec5da6af4ee945ae59ccb3" alt="Unstructured API Endpoint" data-og-width="2786" width="2786" data-og-height="1816" height="1816" data-path="img/api/Marketplace_Step11.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step11.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=63fa26993e9d658059abb1de5737b43b 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step11.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=d8e58c781f0fadfa9f120f945102fa0f 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step11.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=e2987dcbab24f68f4f84bef4dc7b5d00 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step11.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=433f799b0edda669ee82ede0cf9e0c95 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step11.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=964ee0622f5d7b5ed90aedec731eb655 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/Marketplace_Step11.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=1bf43e7bac6e04b3f671bb4440e3342b 2500w" />

## Healthcheck

Perform a health check by running this [curl](https://curl.se/) command from a terminal on your local machine, replacing `<application-load-balancer-dns-name>` with your application load balancer's DNS name. This health check can take several minutes:

```bash  theme={null}
curl http://<application-load-balancer-dns-name>/healthcheck

```

<img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/healthcheck.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=087561beffb043745c3fde43ee00c282" alt="Healthcheck" data-og-width="1666" width="1666" data-og-height="64" height="64" data-path="img/api/healthcheck.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/healthcheck.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=84b1c0ae5b9d1379ce2795247d61676a 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/healthcheck.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=ffc65ca016d60c572cf0fab8e112c1a2 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/healthcheck.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=c4e63c9251131905af60de1d8de82b34 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/healthcheck.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=c3d8efd6d28c0bb171ece27cc4fd2748 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/healthcheck.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=46581ba8675f08b14e0bfa77110cda2e 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/healthcheck.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=9e6c8fcee24c9d6b6d1b04febcff06de 2500w" />

## Data processing

For example, run one of the following, setting the following environment variables to make your code more portable:

* Set `UNSTRUCTURED_API_URL` to `http://`, followed by your load balancer's DNS name, followed by `/general/v0/general`.

  <Info>You can now use this value (`http://`, followed by your load balancer's DNS name, followed by `/general/v0/general`) in place of
  calling the [Unstructured Partition Endpoint](/api-reference/partition/overview) URL as described elsewhere in the Unstructured API documentation.</Info>

* Set `LOCAL_FILE_INPUT_DIR` to the path on your local machine to the files for the Unstructured API to process. If you do not have any input files available, you can download any of the ones from the [example-docs](https://github.com/Unstructured-IO/unstructured-ingest/tree/main/example-docs) folder in GitHub.

* Set `LOCAL_FILE_OUTPUT_DIR` to the path on your local machine for Unstructured API to send the processed output in JSON format:

<AccordionGroup>
  <Accordion title="Ingest CLI">
    You must first [install the Unstructured Ingest CLI](/open-source/ingestion/overview#unstructured-ingest-cli).

    Because you are calling a private API and therefore do not need an Unstructured API key, you can omit the command-line option `--api-key` Or, for better code portability, it is recommended that you first set the environment variable `UNSTRUCTURED_API_KEY` to an empty string and then include the command-line option `--api-key`.

    ```bash CLI theme={null}
    unstructured-ingest \
      local \
        --input-path $LOCAL_FILE_INPUT_DIR \
        --output-dir $LOCAL_FILE_OUTPUT_DIR \
        --partition-by-api \
        --api-key $UNSTRUCTURED_API_KEY \
        --partition-endpoint $UNSTRUCTURED_API_URL \
        --strategy hi_res \
        --additional-partition-args="{\"split_pdf_page\":\"true\", \"split_pdf_allow_failed\":\"true\", \"split_pdf_concurrency_level\": 15}"
    ```
  </Accordion>

  <Accordion title="Ingest Python library">
    You must first [install the Unstructured Ingest Python library](/open-source/ingestion/python-ingest).

    Because you are calling a private API and therefore do not need an Unstructured API key, you can omit the parameter `api_key`. Or, for better code portability, it is recommended that you first set the environment variable `UNSTRUCTURED_API_KEY` to an empty string and then include the parameter `api_key`.

    ```python Python Ingest theme={null}
    import os

    from unstructured_ingest.pipeline.pipeline import Pipeline
    from unstructured_ingest.interfaces import ProcessorConfig
    from unstructured_ingest.processes.connectors.local import (
        LocalIndexerConfig,
        LocalDownloaderConfig,
        LocalConnectionConfig,
        LocalUploaderConfig
    )
    from unstructured_ingest.processes.partitioner import PartitionerConfig

    if __name__ == "__main__":
        Pipeline.from_configs(
            context=ProcessorConfig(),
            indexer_config=LocalIndexerConfig(input_path=os.getenv("LOCAL_FILE_INPUT_DIR")),
            downloader_config=LocalDownloaderConfig(),
            source_connection_config=LocalConnectionConfig(),
            partitioner_config=PartitionerConfig(
                partition_by_api=True,
                api_key=os.getenv("UNSTRUCTURED_API_KEY"),
                partition_endpoint=os.getenv("UNSTRUCTURED_API_URL"),
                strategy="hi_res",
                additional_partition_args={
                    "split_pdf_page": True,
                    "split_pdf_allow_failed": True,
                    "split_pdf_concurrency_level": 15
                }
            ),
            uploader_config=LocalUploaderConfig(output_dir=os.getenv("LOCAL_FILE_OUTPUT_DIR"))
        ).run()
    ```
  </Accordion>
</AccordionGroup>

## Accessing the hosting EC2 instance

If you need to access the Amazon EC2 instance that hosts the Unstructured API, do the following:

1. In the CloudFormation console, open the details page for the stack from Part II. If you do not see it, on the CloudFormation console's sidebar, click **Stacks**, and then click the name of your stack.

2. Click the **Resources** tab on this stack's details page. Then click the **Physical ID** link next to **EC2TargetGroup** on this tab.

3. On the **EC2 > Target groups > (CloudFormation stack name)** page that appears, on the **Targets** tab, click the **Instance ID** link.

4. In the list of instances that appears, click the **Instance ID** link.

5. Click **Connect**, and then follow any of the on-screen options to access the EC2 instance.

## Manage related AWS account costs

After you run the CloudFormation stack that you created in Part II, charges will begin accruing to your AWS account on an ongoing basis for related AWS resources.
The amounts of these charges vary based on where these resource are located, which resources are covered by AWS Free Tier offerings, the extent to
which you customize these resources' settings, how much you use these resources, and other factors. Stopping or terminating
the related Amazon EC2 instances alone will not eliminate these ongoing charges.

To stop these charges from accruing,
[delete the CloudFormation stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.html)
that you created and ran in Part II. This stops and deletes all of the related AWS resources.

Before you delete the stack, note the following:

* You should click the **Resources** tab on the stack's details page to be aware of the associated resources that will be deleted.
* You should note any resource dependencies, resources with deletion protection or termination protection enabled, or nested stacks
  that might prevent stack deletion, and resolve these issues that could prevent stack deletion. To find these kinds of issues:

  * On the **Template** tab on the stack's details page, look for occurences of the `DependsOn` attribute, which are set to the name
    of the resource dependency.
  * On the **Template** tab on the stack's details page, look for occurences of the `DeletionPolicy` attribute set to `Retain` or the
    `UpdateReplacePolicy` attribute set to `Retain`. The associated resources have deletion protection enabled.
  * On the **Stack info** tab on the stack's details page, look for the **Termination protection** field. If it is set to **Activated**,
    termination protection is enabled.
  * On the **Resources** tab on the stack's details page, look for resources with their **Type** set to `AWS::CloudFormation::Stack`. These indicate nested stacks.

After you delete the stack, you should check your [AWS Billing and Cost Management dashboard](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/billinginfo.html) to confirm that associated charges are no longer accruing.
