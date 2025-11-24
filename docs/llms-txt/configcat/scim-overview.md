# Source: https://configcat.com/docs/advanced/team-management/scim/scim-overview.md

# (Beta) User provisioning (SCIM) Overview

info

**Beta Feature**: SCIM provisioning is in public beta. It has been thoroughly tested with various Identity Providers. We're now collecting feedback from real-world usage to fine-tune the experience. Share your feedback [here](https://configcat.com/support).

This section describes how to configure *User provisioning (SCIM)* for your Organization in ConfigCat.

User provisioning (SCIM) allows you to synchronize users and groups from your Identity Provider into a ConfigCat Organization. ConfigCat permissions then can be assigned to each synchronized Identity Provider (IdP) group, which puts their members to the selected *ConfigCat permission groups* upon a user provisioning process.

Go to the **User provisioning (SCIM)** section on the [Authentication & Provisioning](https://app.configcat.com/organization/authentication/) page to set up User provisioning. You need to be an Organization Admin to do this.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* [Verified domain](https://configcat.com/docs/docs/advanced/team-management/domain-verification/.md): You must verify your company's email domain before you can set up User provisioning (SCIM).
* Identity Provider that supports SCIM 2.0.

## Supported SCIM 2.0 endpoints[​](#supported-scim-20-endpoints "Direct link to Supported SCIM 2.0 endpoints")

Check our User Provisioning (SCIM) API documentation [here](https://configcat.com/docs/docs/api/scim/configcat-user-provisioning-scim-api/.md).

## 1. Connect your Identity Provider[​](#connect "Direct link to 1. Connect your Identity Provider")

To enable SCIM in your Identity Provider, you have to let it know where ConfigCat accepts SCIM endpoint calls and how these calls are authorized. Configcat displays this information on its [Authentication & Provisioning](https://app.configcat.com/organization/authentication/) page, where you'll find:

* The **SCIM URL**: this points your Identity Provider to ConfigCat's SCIM endpoint.
* The **Token**: use this to authorize requests with the `Bearer:` scheme.

To get the bearer token, go to the **1. Connect your Identity Provider** section and click the **+ GENERATE** button.

![ConfigCat SCIM token generate](/docs/assets/scim/dashboard/token_generate.png)

A dialog will open. Copy the *token* and save it somewhere safe - you'll need it when setting up your Identity Provider.

![ConfigCat SCIM token](/docs/assets/scim/dashboard/token.png)

Go to your Identity Provider, and connect it to ConfigCat. To help, we prepared specific Identity Provider-specific instructions for a few providers. These instructions are tested and validated:

* [Entra ID (Azure AD)](https://configcat.com/docs/docs/advanced/team-management/scim/identity-providers/entra-id/.md)
* [Okta](https://configcat.com/docs/docs/advanced/team-management/scim/identity-providers/okta/.md)
* [OneLogin](https://configcat.com/docs/docs/advanced/team-management/scim/identity-providers/onelogin/.md)

info

Other Identity Providers might also work with ConfigCat, if they support the SCIM 2.0 protocol.

info

Connecting your Identity Provider and starting to sync users and groups is safe. It won't affect your current ConfigCat users or permissions until you click the `START PROVISIONING` button later.

## 2. Assign ConfigCat permissions to Identity Provider groups[​](#groups "Direct link to 2. Assign ConfigCat permissions to Identity Provider groups")

After the first successful sync, your Identity Provider groups will show up in ConfigCat. You will find them in the **2. Assign ConfigCat permissions to Identity Provider groups** section of the [Authentication & Provisioning](https://app.configcat.com/organization/authentication/) page. For each Identity Provider group, you can assign ConfigCat permissions by clicking their gear icon.

![ConfigCat SCIM assign permissions](/docs/assets/scim/dashboard/assign_permissions.png)

A dialog will appear. Choose which ConfigCat permissions should be assigned to the members of the given *Identity Provider group*.

![ConfigCat SCIM select permissions](/docs/assets/scim/dashboard/select_permissions.png)

### How permission conflicts are resolved[​](#how-permission-conflicts-are-resolved "Direct link to How permission conflicts are resolved")

An Identity Provider user can be a member of multiple Identity Provider groups. ConfigCat's user provisioning merges the associated permissions using the following rules:

* If a user is in an Identity Provider group linked to ConfigCat's Organization Admin role, they get Organization Admin access in ConfigCat.
* If a user is in an Identity Provider group linked to ConfigCat's Billing Manager role, they get Billing Manager access in ConfigCat.
* If none of the groups have the Organization Admin role, ConfigCat merges the product-level permissions from each Identity Provider group.

If there's a conflict, the group with a higher priority (listed first) wins. You can change the Identity Provider group priorities by clicking the **Set priority** button above the **Identity Provider groups** table.

![ConfigCat SCIM set group priority](/docs/assets/scim/dashboard/set_priority.png)

You can change the group order by dragging and dropping items in the list.

![ConfigCat SCIM change group priority](/docs/assets/scim/dashboard/change_priority.png)

### Example[​](#example "Direct link to Example")

A ConfigCat Organization has 2 *products*. Each product has its own *permission groups*:

| Product   | Permission groups                   |
| --------- | ----------------------------------- |
| Product A | Readers, Writers, Developers        |
| Product B | Readers, Product owners, Developers |

There are 5 *Identity Provider groups* that are marked for synchronization with the following permissions:

| Priority | Identity Provider group | Associated ConfigCat Permissions           |
| -------- | ----------------------- | ------------------------------------------ |
| 1.       | Owners                  | Organziation Admin, Billing Manager        |
| 2.       | Billing Managers        | Organziation Admin                         |
| 3.       | Developers              | Product A/Developers, Product B/Developers |
| 4.       | Product owners          | Product B/Product owners                   |
| 5.       | Readers                 | Product A/Readers, Product B/Readers       |

Based on their *Identity Provider groups*, users will get the following *ConfigCat permissions*:

| Identity Provider user | Identity Provider groups  | Calculated ConfigCat Permissions                      | Explanation                                                                                                                                                                                                                                                                   |
| ---------------------- | ------------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| John                   | Owners, Readers           | Organization Admin, Billing Manager                   | John is in the Owners group (IdP), which gives him the Organization Admin role in ConfigCat. Product-level permissions from the Readers group (IdP) are skipped because ConfigCat's Organization Admin role automatically grants all permissions in all *ConfigCat products*. |
| Jane                   | Readers, Billing Managers | Billing Manager, Product A/Readers, Product B/Readers | Jane gets both Billing Manager and product-level permissions. These are merged from her groups.                                                                                                                                                                               |
| Peter                  | Readers, Developers       | Product A/Developers, Product B/Developers            | As both the Readers and Developers Identity Provider groups have associated permissions to the same Products, the permissions will be merged based on the Identity Provider group's priority.                                                                                 |

## 3. Start and stop provisioning for Identity Provider users[​](#users "Direct link to 3. Start and stop provisioning for Identity Provider users")

After successful synchronization, Identity Provider users will appear in ConfigCat. You can find them in the **3. Start and stop provisioning for Identity Provider users** section of the [Authentication & Provisioning](https://app.configcat.com/organization/authentication/) page. You can see and control their provisioning state there.

Some of those users are new to ConfigCat, and they do not yet have a ConfigCat account under your Organization. When they are synced from your Identity Provider, ConfigCat does not create accounts for them right away.

Other users might already have a ConfigCat account in your Organization - either because they joined earlier or accepted a previous invite. For them, ConfigCat permissions won't change automatically. You must start provisioning manually to apply the permissions linked to their Identity Provider groups.

![Start/Stop provisioning](/docs/assets/scim/dashboard/start_stop_provisioning.png)

### What is managed by the provisioning?[​](#what-is-managed-by-the-provisioning "Direct link to What is managed by the provisioning?")

After you start provisioning an Identity Provider user, the following user-related attributes are managed:

* **ConfigCat permissions**: with a fine-tuned provisioning configuration, you can manage your team members' *ConfigCat permissions* through your Identity Provider.
* **ConfigCat account's email address**: if an *Identity Provider user*'s email address has been changed in the Identity Provider, the associated *ConfigCat user*'s email address will be changed too. The *ConfigCat user* will be able to log in with the new email address only.
* **ConfigCat account's full name**: the *Identity Provider user*'s full name is synchronized from the Identity Provider and overwrites the *ConfigCat user*'s full name property.
* **Soft delete**: if an *Identity Provider user* is soft deleted in the Identity Provider, the *ConfigCat account* will be disabled and cannot be used.
* **Hard delete**: if an *Identity Provider user* is hard deleted in the Identity Provider, the *ConfigCat account* will be removed from your ConfigCat Organization entirely, but the *ConfigCat account* will not be deleted for a while.

### Start/stop provisioning[​](#startstop-provisioning "Direct link to Start/stop provisioning")

In the **Identity Provider users** table, the last column has a start/stop button. This indicates whether an *Identity Provider user*'s provisioning is active or not. As long as the provisioning is not started, you can adjust your Identity Provider groups' provisioning configurations till the permissions for your Identity Provider users match the expected permissions without having to worry about changing existing users' permissions. The provisioning status column can give you an overview what will happen if you start the provisioning for the *Identity Provider user*.

If you start the provisioning for an *Identity Provider user* who already has a *ConfigCat account*, the provisioning will overwrite the account's current *ConfigCat permissions*. If you start the provisioning for an *Identity Provider user* who doesn't have a *ConfigCat account yet*, their *ConfigCat permissions* will be set based on the permissions you see in the **Identity Provider user** table after they sign up for a *ConfigCat account*.

info

After you start provisioning an *Identity Provider user*, you won't be able to set their ConfigCat permissions manually on the [Team Members](https://app.configcat.com/product/members/) or [Members & Roles](https://app.configcat.com/organization/members/) pages. Their *ConfigCat permissions* can only be changed by modifying their group memberships in your Identity Provider, or by changing the *ConfigCat permissions* associated with those groups in the **Identity Provider groups table** in ConfigCat.

If you stop provisioning an Identity Provider user, it will disconnect that user's *ConfigCat permissions* from their *Identity Provider group memberships*. Modifying provisioning permissions or changing the user's *Identity Provider groups* will not change their *ConfigCat permissions*. If you want to manage the *ConfigCat permissions* of that user, you should use ConfigCat's [Team Members](https://app.configcat.com/product/members/) and [Members & Roles](https://app.configcat.com/organization/members/) pages.<br /><!-- -->After starting the provisioning again, *ConfigCat permissions* may change according to the actual provisioning configurations.

### Provisioning status[​](#provisioning-status "Direct link to Provisioning status")

The **Provisioning status** column in the **Identity Provider users** table shows important information about the provisioning state.

#### Identity Provider user with an unverified email domain[​](#identity-provider-user-with-an-unverified-email-domain "Direct link to Identity Provider user with an unverified email domain")

User Provisioning synchronizes all *Identity Provider users* from your Identity Provider regardless of whether the *Identity Provider user*'s email domain is a verified email domain in ConfigCat. **Provisioning status** displays an error message if the Identity Provider user's email address is not from a *verified domain*. You will not be able to start provisioning for that Identity Provider user until you verify the email domain in ConfigCat.

#### Identity Provider user without a ConfigCat account[​](#identity-provider-user-without-a-configcat-account "Direct link to Identity Provider user without a ConfigCat account")

The Provisioning status shows you information about what permissions will be assigned and what will happen to the Identity Provider user after a successful sign up.<br />**Provisioning status** displays a warning if an Identity Provider user will have no permissions in ConfigCat after signup. This allows you to fine-tune your provisioning configuration.

#### Identity Provider user with an already existing ConfigCat account[​](#identity-provider-user-with-an-already-existing-configcat-account "Direct link to Identity Provider user with an already existing ConfigCat account")

If the provisioning of the *Identity Provider user* is stopped, the **provisioning status** shows what will happen to the *ConfigCat account* when you start provisioning again. After the provisioning is started again, the **provisioning status** can take the following values:

* **Provisioning is active**: all permissions and user properties match your Identity Provider configuration for the *Identity Provider user*.
* **Provisioning is in progress**: the provisioning process is running in the background. For a short time, you can see the **provisioning is in progress** status. This happens when your Identity Provider sends updates to ConfigCat about the *Identity Provider user*, or when you modify your *Identity Provider group*'s provisioning permissions.

## 4. Provision future users automatically[​](#auto-provisioning "Direct link to 4. Provision future users automatically")

By default, after the Identity Provider synchronizes a new Identity Provider user to ConfigCat, the Identity Provider user will be in the **provisioning stopped** state. This allows you time to verify your configuration/permissions and adjust your settings if needed.<br /><!-- -->After you are confident that the provisioning works as expected, you can turn ON the **Provision future users automatically** toggle. This will immediately start the provisioning for newly synchronized Identity Provider users.

![Auto provisioning for new users](/docs/assets/scim/dashboard/auto_provisioning.png)

### Disable Domain Auto-assign[​](#disable-domain-auto-assign "Direct link to Disable Domain Auto-assign")

ConfigCat has a few other features that might interfere with *User provisioning*:

* **Domain verification**: after verifying your domain name in ConfigCat, all users signing up with that domain will be added to your Organization.
* **Auto-assign**: the *auto-assign feature* assigns initial permissions to those users automatically.

If you want to allow only provisioned users into your ConfigCat Organization, you should deactivate the auto-assign feature in **Domain verification & Auto-assign users** panel.

![Disable domain auto-assign](/docs/assets/scim/dashboard/disable_auto_assign.png)

## 5. Review ConfigCat users who are not managed by user provisioning[​](#not-managed "Direct link to 5. Review ConfigCat users who are not managed by user provisioning")

Even after configuring *user provisioning* and synchronizing *Identity Provider users* from your Identity Provider, there might be *ConfigCat accounts* in your Organization that are not managed by *user provisioning*.

There can always be exceptions, but in most cases:

* Either they no longer need access to ConfigCat - you may want to delete them.
* Or you want to manage them through your Identity Provider - in this case, go to your Identity Provider and set up sync for them.
* Or you want to keep them this way - in this case, you need to manage their ConfigCat permissions on the [Team Members](https://app.configcat.com/product/members/) or [Members & Roles](https://app.configcat.com/organization/members/) page.
