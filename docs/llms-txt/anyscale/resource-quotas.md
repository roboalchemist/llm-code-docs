# Source: https://docs.anyscale.com/reference/resource-quotas.md

# Source: https://docs.anyscale.com/administration/resource-management/resource-quotas.md

# Resource quotas

[View Markdown](/administration/resource-management/resource-quotas.md)

# Resource quotas

Resource quotas enable you to set limits on resource usage within your Anyscale environment. Set resource quotas in the console UI or [CLI](/reference/resource-quotas.md).

## Create a resource quota[​](#create-a-resource-quota "Direct link to Create a resource quota")

To create or manage a quota, navigate to: **User menu > Organization settings > Resource Quota**

![Resource Quota Lists](/assets/images/Resourcequota_List-e9a1cad93c1398e7c4ca82160733ffce.jpg)

### Set quota scope[​](#quota-scope "Direct link to Set quota scope")

You can enforce resource quotas at different levels within your Anyscale infrastructure.

![Setting the resource quota scope](/assets/images/QuotaScope-af91306818a250c97760661bb4eca9ad.jpg)

When creating a resource quota:

* You must specify an Anyscale cloud for quota enforcement.
* You can optionally specify a project or a user.
* If you don't specify a project or user, the quota applies to all projects or users within the specified scope.

info

Keep these points in mind when setting quota scope:

* If you select **All projects**, Anyscale enforces the quota on all current and future projects that you create.
* If you select **All users**, Anyscale enforces the quota on all current and future users added to your organization.
* You can create only one resource quota per cloud-project-user combination.

### Quota limits[​](#quota-limits "Direct link to Quota limits")

![Setting resource quota limits](/assets/images/QuotaLimits-ad267d2572e47d2ea309cae86f514063.jpg)

You can set resource quotas for the following resource dimensions:

* Maximum number of CPUs.
* Maximum number of instances.
* Maximum number of GPUs.
* Maximum number of specific accelerator types.

If the admin sets multiple limits, Anyscale triggers a quota exceed error as soon as any one of the limits is surpassed. Furthermore, the admin can configure notifications for when the quota limit is reached.

**For hard limits:** The admin can keep the "Prevent new nodes from being added after quota limit is reached" option enabled. This setting pauses scaling without terminating the cluster.

**For soft limits:** The admin can disable the "Prevent new nodes from being added after quota limit is reached" option. With this setting, scaling continues, and if you configured notifications, Anyscale will send an alert.

info

Keep these points in mind when setting quota limits:

* Specify at least one limit when creating a quota.
* Use only positive integer values for CPUs, instances, and GPUs.
* Set a value of 0 for specific accelerators to disallow their use.
* Any omitted limit defaults to unlimited for that resource.

### Set notifications[​](#notifications "Direct link to Set notifications")

When any quota limit exceeds, Anyscale can send an alert with an email, Slack notification, or a custom webhook. Configure notification channels as needed.

To send a Slack notification, add a webhook URL to your Slack organization. Set up incoming webhooks by following Slack's [documentation](https://api.slack.com/messaging/webhooks).

![Adding notifications to resource quotas](/assets/images/SetNotifications-d3157100fb2c9b5e3dd48da3e0511761.jpg)

Note: Quota limits don't terminate clusters but can pause scaling if it's a hard limit. Read more about quota exceed and errors below.

## Quota enforcement and exceeded errors[​](#enforcement "Direct link to Quota enforcement and exceeded errors")

Understanding how quota enforcement works is crucial for effective resource management.

**If the admin has created a resource quota with hard limits:**

1. Resource quotas with hard limits affect the ability to start new clusters or scale existing ones within the specified cloud, project, or user scope.
2. If a user attempts to launch a job, service, or workspace that exceeds the set quota limits, Anyscale triggers a "quota exceeded" error. You can find these errors in the event log, which provides information about which quota limit was exceeded. See the screenshot attached below.
3. Enabling a quota does not automatically terminate existing clusters that are already running. However, these clusters may fail to scale up if doing so would exceed the quota limits.
4. Quotas don't affect the ability to scale down resources or terminate existing clusters.

![Quota exceeded error in event logs](/assets/images/HardQuota-exceed-af723aac7b78c3df43c606f82c386147.png)

**If the admin has created a resource quota with soft limits:**

1. Resource quotas with soft limits don't affect the ability to start new clusters or scale existing ones within the specified cloud, project, or user scope.
2. If a user attempts to launch a job, service, or workspace that exceeds the set quota limit, Anyscale displays a "quota exceeded" message in the event logs. See the screenshot attached below.

![Quota exceeded error in event logs](/assets/images/SoftQuota-exceed-6c7763348255a5cb26bb3531d61177e4.png)

By monitoring these quota exceeded errors, you can gain insights into resource usage patterns and adjust your quotas or resource allocation strategies accordingly.

## Manage resource quotas[​](#manage "Direct link to Manage resource quotas")

You can manage resource quotas using the UI or the [CLI](/reference/resource-quotas.md).

* Enable/Disable: Admins may enable or disable quotas.
* Delete: Admins may permanently delete a quota.

![Managing resource quotas](/assets/images/Actions-00895694468e8ef47de6923657b94da7.jpg)

For further assistance, contact [Anyscale Support](mailto:support@anyscale.com).
