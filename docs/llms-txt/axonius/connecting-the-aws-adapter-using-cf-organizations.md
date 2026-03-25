# Source: https://docs.axonius.com/docs/connecting-the-aws-adapter-using-cf-organizations.md

# Connecting the AWS Adapter Using CloudFormation/Organizations

In large AWS deployments it can become difficult to maintain the accounts/roles that are needed by Axonius in order to collect AWS assets. If you are using the AWS Organizations service to manage your AWS accounts then Axonius can integrate with [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) and [AWS CloudFormation](https://docs.aws.amazon.com/cloudformation/) to keep your accounts and asset inventory up to date with much less overhead.

This document is meant to give a high level overview of how the Axonius platform interacts with AWS when customers utilize AWS Organizations in their adapter configuration, as well as simplified instructions on how to set up your AWS accounts to support this configuration.

## Architecture Overview

Throughout this document we will be referring to the following architecture components:

1. **Launch Account** - AWS account used to host an Axonius instance, an entry role, or that contains the IAM user/key Axonius uses to authenticate. The launch account can be any member account in your organization.
2. **Organization Management Account** - AWS account that is the Management account (or delegated administrator) for your AWS Organization.
3. One or more AWS Organizations member accounts.
4. Three distinct IAM entities:

   1. A ReadOnly role that exists in all accounts attached to the organization. This role is used to fetch asset data from each member account.
   2. An Organizations role on the AWS Organizations Management account. This role will have the ability to list the member accounts enrolled within the Organization.
   3. An initial access method which will exist in the **Launch Account** which will be a **Cross-account role**, **Instance Profile**, or **IAM User**. To know which initial access method is appropriate for your deployment, see the **Selecting an Initial Access Method** section below.

## Selecting an Initial Access Method

Axonius is capable of initially accessing your AWS environment in three different ways:

1. Cross-account role - The best option for [Axonius-hosted (SaaS)](/docs/saas-deployment) customers. Axonius will assume a role in the Launch Account directly and use that role for all other operations within your environment.  This role is only available to Axonius hosted customers.
2. Instance profile - The best option for customers who host Axonius within their own AWS account. With this option the initial access method is tied directly to your Axonius Primary Instance, or Compute node.  (Note that this role is not available to Axonius-hosted customers).
3. IAM User - This option should be used when your Axonius instance is neither Axonius-hosted SaaS or self-hosted within AWS, or in any other situation.

Axonius strongly recommends avoiding the use of IAM Users/Keys in cases where using a cross-account role or instance profile are available. For cases where the use of an IAM key is the only option to integrate with AWS, please ensure you review the documentation from AWS regarding [AWS Identity and Access Management Best Practices](https://aws.amazon.com/iam/resources/best-practices/).

## Configuring AWS

In order to deploy Axonius using AWS CloudFormation/Organizations you can utilize the Axonius AWS CloudFormation Template:

[Axonius-CFTemplate.json](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Files/Axonius-CFTemplate.json)

This template is designed to be deployed as a CloudFormation StackSet so that it can be managed by AWS and deployed across your entire organization. Using a StackSet allows the required roles used by Axonius to be automatically deployed to all member accounts, including newly added accounts without the need for additional configuration changes in AWS or Axonius.

<Callout icon="📘" theme="info">
  NOTE

  Before you begin, you should know what [Initial Access Method](/docs/connecting-the-aws-adapter-using-cf-organizations#selecting-an-initial-access-method) will be used to connect to AWS. If you are unsure please reach out to Axonius Support.
</Callout>

### Step 1: Running the StackSet

1. Log in to your [Delegated Administrator](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html) account for your AWS Organization. If you do not have a Delegated Administrator account you will need to log into and perform the following steps from your Organization Management Account.
2. Navigate to **CloudFormation** using the top search bar. Click **StackSets** from the left panel then **Create Stackset**.
3. Select the **Service Managed Permissions** and **Upload a Template file** radio buttons. Upload the CloudFormation template file and click Next to proceed to the **Specify StackSet details** stage of the StackSet deployment.
4. Give the StackSet any name and description of your choice. Expand the appropriate section below depending on what Initial Access method is being used to fill out the Parameters section:

<Accordion title="Cross Account Role Method" icon="fa-info-circle">
  1) **AWSConnectionMethod -** from the dropdown, set this parameter to **role.**
  2) **LaunchAccountID** - a 12 digit AWS Account ID. It can be the account ID of any member account within the organization.
  3) **AWSOrganizationsAccountID** - a 12 digit AWS Account ID. This account ID must be the ID of either your Organizations Delegated Administrator or your Organizations Management account.
  4) **ExternalID** - Copy your Customer ID from your Axonius Instance. To find your Customer ID, log in to your Axonius instance and go to **System Settings → About**.
  5) **SelfHosted -** from the dropdown, set this parameter to **AxoniusHosted**
</Accordion>

<Accordion title="Instance Profile Method" icon="fa-info-circle">
  1. **AWSConnectionMethod -** from the dropdown, set this parameter to **role.**

  2. **LaunchAccountID** - a 12 digit AWS Account ID. **This must be the account in which Axonius (or a compute node for your Axonius platform) is currently running.**

  3. **AWSOrganizationsAccountID** - a 12 digit AWS Account ID. This account ID must be the ID of either your Organizations Delegated Administrator or your Organizations Management account.

  4. **SelfHosted -** from the dropdown, set this parameter to **SelfHosted**
</Accordion>

<Accordion title="IAM User Method" icon="fa-info-circle">
  1. **AWSConnectionMethod** - from the dropdown, set this parameter to **user.**

  2. **LaunchAccountID** - a 12 digit AWS Account ID. It can be the account ID of any member account within the organization.

  3. **AWSOrganizationsAccountID** - a 12 digit AWS Account ID. This account ID must be the ID of either your Organizations Delegated Administrator or your Organizations Management account.

  4. Once the parameters have been filled out click Next to proceed to the **Configure Stackset Options**stage of the deployment.
</Accordion>

5. Check the Acknowledgement box at the bottom of the page, then click Next.
6. In the **Specify regions** section, add **us-east-1**. If you are integrating a US GovCloud organization, use **us-gov-east-1.**  Optionally, you can choose to deploy to and have Axonius retrieve asset data from a subset of your organization using the **Deploy to organizational units (OUs)** radio button. If selected, enter the OU(s) that contain your desired accounts. If you want Axonius to retrieve asset data from all Organization member accounts then leave the **Deploy to organization** radio button selected. Click Next.
7. The **Review** stage will summarize the configuration from the previous steps. Click **Submit** to initialize the StackSet.

### Step 2: Running a Stack in the Organizations Management Account

1. Log in to your AWS Organizations Management account.
2. Click the region drop down at the top right of the AWS Console and select the **us-east-1** region. If you are integrating with a US GovCloud organization, select **us-gov-east-1**.
3. Navigate to **CloudFormation** using the top search bar.
4. Click **Stacks** from the left panel then **Create Stack**. From the dropdown, select **With new resources (standard).**
5. Select the **Upload a template file** radio button. Upload the CloudFormation template file and click Next.
6. Give the Stack any name and description of your choice. **Enter the parameters exactly as they were done within**  [Step 1](/docs/connecting-the-aws-adapter-using-cf-organizations#step-1-running-the-stackset), then click Next.
7. Check the Acknowledgement box at the bottom of the page, then click Next.
8. The **Review** stage will summarize the configuration from the previous steps. Click **Submit** to initialize the Stack.

### Step 3: Attaching an Instance Profile/Generating Access Keys

<Callout icon="📘" theme="info">
  NOTE

  This step is only required for customers who are using an IAM user/Instance Profile initial access method. If using an cross-account role then the configuration with AWS is already complete and you can proceed to [Configuring the AWS Adapter in Axonius](/docs/connecting-the-aws-adapter-using-cf-organizations#configuring-the-aws-adapter-in-axonius).
</Callout>

1. Expand the appropriate section below depending on what Initial Access method is being used:

<Accordion title="Instance Profile Method" icon="fa-info-circle">
  1) Log into the AWS Account ID that was indicated as the **LaunchAccountID** in [Step 1](/docs/connecting-the-aws-adapter-using-cf-organizations#step-1-running-the-stackset).
  2) Navigate to **EC2** using the top search bar.
  3) Click the region drop down at the top right of the AWS Console and select whichever region your Axonius system (or compute node) is hosted in.
  4) Select the your Axonius instance from the EC2 instances list, then click Actions → Security → Modify IAM Role.
  5) Choose the instance profile name that was indicated in [Step 1](/docs/connecting-the-aws-adapter-using-cf-organizations#step-1-running-the-stackset) in the **AccessName** parameter. By default the name of the instance profile will be **Axonius-Access**. Click **Update IAM role**.
</Accordion>

<Accordion title="IAM User Method" icon="fa-info-circle">
  1. Log into the AWS Account ID that was indicated as the **LaunchAccountID** in [Step 1](/docs/connecting-the-aws-adapter-using-cf-organizations#step-1-running-the-stackset).
  2. Navigate to **IAM** using the top search bar.
  3. From the left menu, click **Users**.
  4. Click the user name that was indicated in [Step 1](/docs/connecting-the-aws-adapter-using-cf-organizations#step-1-running-the-stackset) in the **AccessName** parameter. By default the name of the IAM user will be **Axonius-Access**.
  5. Click the **Security Credentials** tab.
  6. Under **Access keys**, click **Create access key**.
  7. From the list of radio buttons, choose **Application running outside AWS** and click next.
  8. Add a description of your choice, then click **Create access key**.
  9. The AWS Access Key ID and Secret will be displayed and downloadable as a CSV file. Save these in a secure location. They will be used in the [Configuring the AWS Adapter in Axonius](/docs/connecting-the-aws-adapter-using-cf-organizations#configuring-the-aws-adapter-in-axonius) section.
</Accordion>

## Configuring the AWS Adapter in Axonius

At this point the work in AWS is complete. Let’s move on to configuring the connection within Axonius. How the connection is configured will again depend on your initial access method. In order to configure the connection we will be referencing many of the same values that were used within your StackSet parameters. If you can’t remember what parameters you used you can always look at them after deployment by going to **CloudFormation → StackSets → \[My StackSet Name] → Parameters.**

Axonius uses an advanced configuration file to configure the AWS adapter. This is simply a JSON formatted document. Samples will be included in the documentation below, but be sure to replace any items with their respective values from your StackSet configuration. Each value that needs to be replaced will be enclosed in square brackets. Replace the entire item, including the brackets themselves. For instance, assuming the default role names are used \[AccessName] would be replaced with Axonius-Access.

1. Expand the appropriate section below depending on what Initial Access method is being used:

<Accordion title="Cross-account role Method" icon="fa-info-circle">
  1) Using notepad or a simple text editor of your choice, update the following JSON with your relevant parameter values and save the file to your workstation as **Advanced-Config.json**. Make sure to replace ALL values within square brackets.

  ```json
  {
  "fetch_roles_from_organization": {
  "organization_role_for_discovery": "arn:aws:iam::[AWSOrganizationsAccountID]:role/[OrganizationsRole]",
  "role_name": "[ReadOnlyRole]"
  },
  "entry_point_role_arn": "arn:aws:iam::[AWSLaunchAccountID]:role/[AccessName]",
  "entry_point_external_id": "[ExternalID]",
  "skip_ec2_verification": true
  }
  ```

  2. Log in to Axonius and from the left ribbon click Adapters, then AWS. Click the blue **Add Connection** button at the top right of the page.
  3. In the connection details, check the box for **Use instance profile (attached role)**, check the box for **Get all regions**, and upload the Advanced-Config.json file under the **Advanced Configuration file** section. Optionally, add any connection label you wish. Click Save and Fetch.

  <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-L3FYEHW0.png" width="433px" height="604px" />
</Accordion>

<Accordion title="Instance Profile Method" icon="fa-info-circle">
  1. Using notepad or a simple text editor of your choice, update the following JSON with your relevant parameter values and save the file to your workstation as **Advanced-Config.json**. Make sure to replace ALL values within square brackets.

  ```json
  {
  "fetch_roles_from_organization": {
  "organization_role_for_discovery": "arn:aws:iam::[AWSOrganizationsAccountID]:role/[OrganizationsRole]",
  "role_name": "[ReadOnlyRole]"
  },
  "skip_ec2_verification": true
  }
  ```

  2. Log in to Axonius and from the left ribbon click Adapters, then AWS. Click the blue **Add Connection** button at the top right of the page.
  3. In the connection details, check the box for **Use instance profile (attached role)**, check the box for **Get all regions**, and upload the Advanced-Config.json file under the **Advanced Configuration file** section. Optionally, add any connection label you wish. Click Save and Fetch.

  <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-L3FYEHW0.png" width="433px" height="604px" />
</Accordion>

<Accordion title="IAM User Method" icon="fa-info-circle">
  1. Using notepad or a simple text editor of your choice, update the following JSON with your relevant parameter values and save the file to your workstation as **Advanced-Config.json**. Make sure to replace ALL values within square brackets.

  ```json
  {
  "fetch_roles_from_organization": {
  "organization_role_for_discovery": "arn:aws:iam::[AWSOrganizationsAccountID]:role/[OrganizationsRole]",
  "role_name": "[ReadOnlyRole]"
  },
  "skip_ec2_verification": true
  }
  ```

  2. Log in to Axonius and from the left ribbon click Adapters, then AWS. Click the blue **Add Connection** button at the top right of the page.
  3. In the connection details enter the AWS Access Key ID and AWS Access Key Secret from [Step 3](/docs/connecting-the-aws-adapter-using-cf-organizations#step-3-attaching-an-instance-profilegenerating-access-keys) of the previous section. Check the box for **Get all regions**, and upload the Advanced-Config.json file under the **Advanced Configuration file** section. Optionally, add any connection label you wish. Click Save and Fetch!

  <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-00L9MVM2.png" width="439px" height="604px" />
</Accordion>