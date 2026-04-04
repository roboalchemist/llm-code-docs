# Source: https://docs.anyscale.com/get-started.md

# Source: https://docs.anyscale.com/administration/get-started.md

# Get started for admins

[View Markdown](/administration/get-started.md)

# Get started for admins

An administrator or anyone with admin access to your team's cloud provider account typically sets up Anyscale for a team. You need to:

* Create an Anyscale organization.
* Set up the Anyscale cloud.
* Enter billing information.

After you complete these steps, you can invite team members to Anyscale. If your team is already using Anyscale, ask the admin to invite you to the organization.

## 1. Create an Anyscale organization[​](#1-create-an-anyscale-organization "Direct link to 1. Create an Anyscale organization")

Follow the sign-up process at [`console.anyscale.com`](https://console.anyscale.com/register/v2) to create a new organization.

1. Enter your email address.
2. Verify your email.
3. Set a password to sign in.

note

If your email address is already a user of an Anyscale organization, this flow signs into your existing organization.

Contact [Anyscale support](mailto:support@anyscale.com) if you need to create another Anyscale organization.

When you create an Anyscale organization for your team, you become the organization owner by default. As an [organization owner](/administration/organization/permissions.md), you can invite users to join the organization. Organization owners are also responsible for providing a payment method.

## 2. Set up the environment[​](#2-set-up-the-environment "Direct link to 2. Set up the environment")

To programmatically interact with Anyscale outside the console and from your terminal, you need to install the [Anyscale CLI](/reference.md).

* AWS
* Google Cloud

**Step 1: Install the Anyscale CLI and Python client package**

```
pip install -U anyscale
```

**Step 2: Authenticate the CLI**

To access Anyscale's services, you need to obtain a token that verifies your identity. Running the following command fetches and updates the token in the local credential file `~/.anyscale/credentials.json`:

```
anyscale login
```

You can also manually generate your API token [through the console](https://console.anyscale.com/v2/api-keys), and set it in the [`ANYSCALE_CLI_TOKEN` environment variable](/resources/environment-variables.md).

**Step 1: Install the Anyscale CLI and Python client package**

```
pip install -U "anyscale[gcp]"
```

**Step 2: Authenticate the CLI**

To access Anyscale's services, you need to obtain a token that verifies your identity. Running the following command fetches and updates the token in the local credential file `~/.anyscale/credentials.json`:

```
anyscale login
```

You can also manually generate your API token [through the console](https://console.anyscale.com/v2/api-keys), and set it in the [`ANYSCALE_CLI_TOKEN` environment variable](/resources/environment-variables.md).

## 3. Create an Anyscale cloud[​](#create-cloud "Direct link to 3. Create an Anyscale cloud")

An Anyscale cloud abstracts the resources and infrastructure necessary for managing Anyscale clusters. See [Introduction to Anyscale clouds](/admin/cloud.md).

You can request an Anyscale-hosted (or serverless) cloud for your organization. Serverless clouds use infrastructure in Anyscale's account to simplify onboarding and can be helpful during product evaluation.

Configure a self-hosted cloud to unlock all platform features and support production workloads.

### Set up a self-hosted Anyscale cloud[​](#set-up-a-self-hosted-anyscale-cloud "Direct link to Set up a self-hosted Anyscale cloud")

* AWS
* Google Cloud

**Step 1: Configure AWS credentials**

Ensure you have set up AWS credentials on the local machine. See the [AWS configuration guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-methods) for initial setup instructions. Run this command to quickly set and view the credentials:

```
aws configure
```

Verify AWS credentials permissions

* Confirm the credentials can launch EC2 instances in the desired AWS region.
* Check permissions for managing VPC, subnets, Security Group, IAM, S3, and EFS. For detailed requirements, see [Configure AWS resources for an Anyscale cloud](/admin/cloud/configure-aws.md).

**Step 2: Create your Anyscale cloud**

To set up your Anyscale cloud with default settings, run the following command:

```
anyscale cloud setup
```

For troubleshooting and advanced customization, see [Configure AWS resources for an Anyscale cloud](/admin/cloud/configure-aws.md).

**Step 3: Verify the Anyscale cloud**

To verify that the Anyscale cloud satisfies the minimum resource requirements, run the following command to launch a test workspace and service:

```
anyscale cloud verify --name <cloud-name> --functional-verify workspace,service
```

**Step 1: Configure your Google Cloud account**

* Follow the [Google Cloud instructions](https://cloud.google.com/sdk/docs/install-sdk) for installing the `gcloud` CLI.
* Create a Google Cloud project for Anyscale to launch clusters in.

Verify Google Cloud credentials permissions

Confirm you're the owner of the Google Cloud project in which Anyscale operates, by clicking **IAM & Admin** in the [Google Cloud console](https://console.cloud.google.com/).

**Step 2: Create the Anyscale cloud**

To set up the Anyscale cloud with default settings, run the following command:

```
anyscale cloud setup
```

For troubleshooting and advanced customization, see [Configure Google Cloud resources for an Anyscale cloud](/admin/cloud/configure-google-cloud.md).

**Step 3: Verify the Anyscale cloud**

To verify that the Anyscale cloud satisfies the minimum resource requirements, run the following command to launch a test workspace and service:

```
anyscale cloud verify --name <cloud-name> --functional-verify workspace,service
```

## 4. Invite users to your organization[​](#invite-users "Direct link to 4. Invite users to your organization")

You can now invite your team members to join your Anyscale organization. To add team members, click the user icon, select **Organization settings**, then click the **Users** tab.

### Manage roles[​](#manage-roles "Direct link to Manage roles")

You can assign **owner** and **collaborator** roles to users. See [Roles and permissions](/administration/organization/permissions.md).

SSO

Admins can also [configure SSO](/administration/organization/configure-sso.md) for their Anyscale organization.

## 5. Add more Anyscale clouds[​](#add-clouds "Direct link to 5. Add more Anyscale clouds")

Organization owners can add multiple self-hosted clouds to their Anyscale organization. To create a cloud, click the user icon, select **Clouds**, then click **Create**.

What's next?

➡️ **[Overview of Anyscale clouds](/admin/cloud.md)** - Learn more about Anyscale clouds and cloud resource configuration options

➡️ **[Access management](/administration/organization/permissions.md)** - Add users and manage permissions

➡️ **[Resource management](/administration/resource-management/telescope-dashboard.md)** - Track health, performance, and utilization of your workloads

➡️ **[Usage Dashboard](/administration/billing/usage-dashboard.md)** - Track usage of Anyscale Credits across your organization

➡️ **[Budgets](/administration/billing/budgets.md)** - Set cost budgets at different levels to track organization's usage

➡️ **[Resource Quotas](/administration/resource-management/resource-quotas.md)** - Set limits on your organization's resource usage
