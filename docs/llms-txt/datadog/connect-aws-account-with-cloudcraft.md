# Source: https://docs.datadoghq.com/cloudcraft/getting-started/connect-aws-account-with-cloudcraft.md

---
title: Connect your AWS Account to Cloudcraft
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Cloudcraft (Standalone) > Getting started > Connect your AWS Account to
  Cloudcraft
---

# Connect your AWS Account to Cloudcraft

Connecting your AWS accounts to Cloudcraft allows you to visualize your infrastructure by reverse-engineering the live environment's service relationships into a system architecture diagram. In addition to automatically generating diagrams, a budget model will also be created, and your imported components will display live status data directly in your diagrams. There is no limit on the number of AWS accounts you can connect to Cloudcraft.

**Note**: For AWS organizations, you must manually add the Cloudcraft role to each individual account in the organization.

This article walks you through connecting your AWS account to Cloudcraft.

{% alert level="info" %}
Datadog users can bypass this process by connecting their Datadog account to Cloudcraft. For more information, see [Datadog Integration](https://docs.datadoghq.com/cloudcraft/getting-started/datadog-integration/ "Datadog Integration").
{% /alert %}

## Requirements{% #requirements %}

- A Cloudcraft user with the [Owner or Administrator role](https://docs.datadoghq.com/cloudcraft/account-management/roles-and-permissions/).
- An active [Cloudcraft Pro subscription](https://www.cloudcraft.co/pricing).
- An AWS account with permission to create IAM roles.

## How the live AWS sync works{% #how-the-live-aws-sync-works %}

Cloudcraft uses a [cross-account role to securely access your AWS environment](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html). As a result, you need to create a Cloudcraft-specific, read-only role in your AWS account. This role can be revoked at any time.

If having a read-only role with access to all components isn't permissible or violates your company's policies, you also have the option to [attach a stricter minimal access policy](https://docs.datadoghq.com/cloudcraft/advanced/minimal-iam-policy/), only giving read-only access to the resources you want to use with Cloudcraft, further minimizing the amount of data the role can access.

Cloudcraft doesn't keep any of the live data from your AWS environment. Instead, it stores ARNs, which are unique identifiers for resources in AWS. This allows the application to link live data to components at runtime.

The data from your AWS environment is streamed in real-time to your browser via Cloudcraft's own AWS environment via role-based access, and is only stored client-side while you are using the application. When you close the application, the live data is deleted.

While not having write access to your account prevents Cloudcraft from offering certain featuresâlike deleting an EC2 instance on both the diagram and your accountâit's simply a more secure approach.

Cloudcraft implements rigorous security processes and controls for the SOC2 compliance program. You can read more about Cloudcraft's security program and controls on [the security page](https://www.cloudcraft.co/security).

## Manage AWS accounts{% #manage-aws-accounts %}

### Add account{% #add-account %}

1. In Cloudcraft, navigate to **User** > **AWS accounts**.
1. At the bottom of the modal, click **Add AWS Account**.
1. The next page provides step-by-step instructions. Click **Open the AWS IAM Console to the Create Role page** to configures the read-only IAM role in AWS.

{% alert level="info" %}
If you can't access the **Create Role** page, you may lack **AdministrativeAccess** or sufficient IAM permissions to create a new IAM role. If this is the case, contact your AWS account's administrator and have them complete the following steps.
{% /alert %}
On the **Create role** page in AWS, leave **Require MFA** unchecked, and click **Next**.
{% alert level="info" %}
**Require MFA** must be disabled as it's not applicable for system-to-system access where there is no human involved. Access is instead protected by being limited to access from the Cloucraft AWS account.
{% /alert %}

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/connect-aws-account-with-cloudcraft/create-iam-role.8b531874e5394106de23a7d8ebd467d1.png?auto=format"
   alt="AWS Identity and Access Management console screen showing options for selecting trusted entities for role configuration." /%}
Next, add permissions policies to your role. Type **ReadOnlyAccess** in the search box and press **Enter** to filter policies by name.Select the **ReadOnlyAccess** policy that provides read-only access to AWS services and resources, then click **Next**.
{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/connect-aws-account-with-cloudcraft/read-only-role.bbf67b7d7f1d42e524afe3df4a6a4644.png?auto=format"
   alt="AWS management console page with the 'ReadOnlyAccess' policy highlighted and selected." /%}
Enter a name and description for the IAM role. You can also add tags to organize, track, or control access for the role. Tagging your role is optional. For tagging best practices, see [Best Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html).Click **Create role**.Select the `cloudcraft` role from the list of roles. On the **Summary** page, copy the **Role ARN**.
{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/connect-aws-account-with-cloudcraft/role-summary.3fcd2f28c1cc4623131baf66efd7910c.png?auto=format"
   alt="AWS IAM role configuration screen showing Role ARN for Cloudcraft integration." /%}
In Cloudcraft, paste the ARN in the **Role ARN** field, and enter a name for your account.Optionally, configure team access by clicking the blue button beneath **Team access** and selecting the teams you want to share access to the AWS account with.
{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/connect-aws-account-with-cloudcraft/team-access.543a0f4f2d62dfef5161c4a911a80a4d.png?auto=format"
   alt="Cloudcraft interface showing Team access options with Cloudcraft, Team Demo, and Cloudcraft Sales + Support team tags." /%}
Click **Save Account**.
### Edit account{% #edit-account %}

To edit an account, click the gray pencil icon to the left of the account you want to edit. You can change details of the account, such as the name, ARN, and team access.

When you are done, click **Save Account**.

### Remove account{% #remove-account %}

To remove an account, click the trash can icon to the right of the account you want to remove, then click **Remove**.
