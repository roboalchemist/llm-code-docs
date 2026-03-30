# Source: https://docs.api7.ai/enterprise/getting-started/create-custom-role.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/getting-started/create-custom-role.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/getting-started/create-custom-role.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/getting-started/create-custom-role.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/getting-started/create-custom-role.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/getting-started/create-custom-role.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/getting-started/create-custom-role.md

# Source: https://docs.api7.ai/enterprise/3.8.x/getting-started/create-custom-role.md

# Source: https://docs.api7.ai/enterprise/3.7.x/getting-started/create-custom-role.md

# Source: https://docs.api7.ai/enterprise/3.6.x/getting-started/create-custom-role.md

# Source: https://docs.api7.ai/enterprise/3.5.x/getting-started/create-custom-role.md

# Source: https://docs.api7.ai/enterprise/3.4.x/getting-started/create-custom-role.md

# Source: https://docs.api7.ai/enterprise/3.3.x/getting-started/create-custom-role.md

# Create a Custom Role

API7 Enterprise starts with a locked-down `Super Admin` role and policy granting full access for initial setup. The default `admin` account is permanently tied to this role for emergency recovery.

With [custom roles](https://docs.api7.ai/enterprise/3.3.x/key-concepts/roles-and-permission-policies.md), you can create a granular permission system tailored to your specific needs. This tutorial will guide you through the process of defining custom roles in API7 Enterprise, empowering you to manage access control with greater precision.

This tutorial showcases a custom role with view-only access to production gateway group and full access (view & edit) to test gateway group. You will complete the following steps:

1. Create two [permission policies](https://docs.api7.ai/enterprise/3.3.x/key-concepts/roles-and-permission-policies.md), one to define the view-only permission to production gateway group, and another to define the full access to test gateway group.
2. Create a custom role `Development Team Member` attached to the above two permission policies.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).
2. [Have two gateway groups](https://docs.api7.ai/enterprise/3.3.x/getting-started/add-gateway-group.md) for test and production environments with at least one gateway instance in each group.
3. [Have a published service](https://docs.api7.ai/enterprise/3.3.x/getting-started/launch-your-first-api.md) in both gateway groups for validation use.
4. (Optional) Learn [permission policy examples](https://docs.api7.ai/enterprise/3.3.x/reference/permission-policy-examples.md).

## Create Permission Policies[â](#create-permission-policies "Direct link to Create Permission Policies")

### Create View-only Production Permission Policy[â](#create-view-only-production-permission-policy "Direct link to Create View-only Production Permission Policy")

1. Select **Organization** from the top navigation bar, and then select **Permission Policies**.
2. Click **Add Permission Policy**.
3. From the dialog box, do the following:

* In the **Name** field, enter `production-gateway-group-view-only`.
* In the **Policy Editor** field, enter the JSON:

```
{
  "statement": [
    {
      "resources": [
        "arn:api7:gateway:gatewaygroup/{production gateway group id}" // Use gateway group id to identify
      ],
      "actions": [
        "<.*>Get<.*>"
      ],
      "effect": "allow"
    },
    {
      "resources": [
         "arn:api7:gateway:gatewaygroup/{production gateway group id}/publishedservice/<.*>" // View-only to all published services on these gateway groups
      ],
      "actions": [
        "<.*>Get<.*>"
      ],
      "effect": "allow"
    }
  ]
}
```

* Click **Add**.

### Create Full Access Test Permission Policy[â](#create-full-access-test-permission-policy "Direct link to Create Full Access Test Permission Policy")

1. Select **Organization** from the top navigation bar, and then select **Permission Policies**.
2. Click **Add Permission Policy**.
3. From the dialog box, do the following:

* In the **Name** field, enter `test-gateway-group-full-access`.
* In the **Policy Editor** field, enter the JSON:

```
{
  "statement": [ // Multiple statements within a policy function with an OR relationship.
    {
      "resources": [
        "arn:api7:gateway:gatewaygroup/{test gateway group id}"
      ],
      "actions": [
        "<.*>"
      ],
      "effect": "allow"
    },
    {
      "resources": [
        "arn:api7:gateway:gatewaygroup/{test gateway group id}/publishedservice/<.*>"  // Full access to all published services on this gateway group
      ],
      "actions": [
        "<.*>"
      ],
      "effect": "allow"
    }
  ]
} 
```

* Click **Add**.

## Create Custom Role[â](#create-custom-role "Direct link to Create Custom Role")

1. Select **Organization** from the top navigation bar, and then select **Roles**.
2. Click **Add Custom Role**.
3. From the dialog box, do the following:

* In the **Name** field, enter `Development Team Member`.
* (Optional) In the **Description** field, enter `View-only access to production gateway group and full access (view & edit) to test gateway group.`
* Click **Add**.

4. In the role details page, click **Attach Policy**.
5. Select `production-gateway-group-view-only` and `test-gateway-group-full-access`.
6. Click **Submit**.

## Validate Custom Role[â](#validate-custom-role "Direct link to Validate Custom Role")

1. Follow the tutorial [Update User Roles](https://docs.api7.ai/enterprise/3.3.x/getting-started/rbac.md) and assign the `Development Team Member` to another user, for example `Tom`.
2. Ask Tom to log in and validate his permissions.

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts
  <!-- -->
  * [Roles and Permission Policies](https://docs.api7.ai/enterprise/3.3.x/key-concepts/roles-and-permission-policies.md)

* Getting Started
  <!-- -->
  * [Update User Roles](https://docs.api7.ai/enterprise/3.3.x/getting-started/rbac.md)

* Best Practices
  <!-- -->
  * [Design Custom Role System](https://docs.api7.ai/enterprise/3.3.x/best-practices/design-custom-role-system.md)

* Reference

  <!-- -->

  * [Permission Policy Actions and Resources](https://docs.api7.ai/enterprise/3.3.x/reference/permission-policy-action-and-resource.md)
  * [Permission Policy Examples](https://docs.api7.ai/enterprise/3.3.x/reference/permission-policy-examples.md)
