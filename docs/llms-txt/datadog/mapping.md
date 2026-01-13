# Source: https://docs.datadoghq.com/account_management/saml/mapping.md

---
title: SAML Group Mapping
description: >-
  Map SAML identity provider attributes to Datadog roles and teams for automated
  user provisioning and access control management.
breadcrumbs: Docs > Account Management > Single Sign On With SAML > SAML Group Mapping
source_url: https://docs.datadoghq.com/saml/mapping/index.html
---

# SAML Group Mapping

## Overview{% #overview %}

With Datadog, you can map attributes in your Identity Provider (IdP)'s response to Datadog entities.

You can map attributes to the following principals:

- [Datadog roles](https://docs.datadoghq.com/account_management/rbac/)
- [Datadog Teams](https://docs.datadoghq.com/account_management/teams/)

Setting up a mapping from SAML attributes to Datadog entities allows you to manage users solely in your identity provider. The system then provisions users in Datadog according to the mappings you set up.

You can create a maximum of 1000 role mappings and 1000 team mappings in each organization. If your organization needs more mappings, reach out to [Support](https://docs.datadoghq.com/help/).

## Prerequisites{% #prerequisites %}

Users with the Access Management permission can assign or remove Datadog principals based on a user's SAML-assigned attributes.

It's important to understand what is sent in an assertion before turning on mappings, as mappings require correct attributes. Every IdP has specific mappings. For example, Azure works with object IDs, and Okta requires you to set attributes in [Okta settings](https://help.okta.com/en/prod/Content/Topics/users-groups-profiles/usgp-add-custom-user-attributes.htm). Datadog recommends cross-referencing with [built-in browser tooling](https://support.okta.com/help/s/article/How-to-View-a-SAML-Response-in-Your-Browser-for-Troubleshooting?language=en_US) such as Chrome DevTools or browser extensions and [validating your SAML assertions](https://www.samltool.com/validate_response.php) **before** creating mappings.

## Map SAML attributes to Datadog roles{% #map-saml-attributes-to-datadog-roles %}

1. [Cross-reference](https://support.okta.com/help/s/article/How-to-View-a-SAML-Response-in-Your-Browser-for-Troubleshooting?language=en_US) and [validate](https://www.samltool.com/validate_response.php) your SAML assertion to understand your IdP's attributes.

1. Go to **Organization Settings** and click the **SAML Group Mappings** tab.

1. If it is visible, ensure the **Role Mappings** tab is selected.

1. Click **New Mapping**. A dialog box appears.

1. Specify the SAML identity provider `key-value` pair that you want to associate with an existing Datadog role (either default or custom). **Note**: These entries are case-sensitive. For example, if you want all users whose `member_of` attribute has a value of `Development` to be assigned to a custom Datadog role called `Devs`:

   {% image
      source="https://datadog-docs.imgix.net/images/account_management/saml/create_mapping.8a9905c485c106611e1c3ab430e419b8.png?auto=format"
      alt="Creating a SAML mapping to Datadog Role" /%}

**Note**: Every identity provider is different. Some allow you to set your attribute key or label. Others provide one by default. Datadog recommends you use an assertion inspector on your login to view the details of your particular assertion to understand how your Identity Provider is sending your group membership.

1. If you have not already done so, enable mappings by clicking **Enable Mappings**.

When a user logs in who has the specified identity provider attribute, they are automatically assigned the Datadog role. Likewise, if someone has that identity provider attribute removed, they lose access to the role (unless another mapping adds it).

{% alert level="danger" %}
**Important:** If a user does not match any mapping, they lose any roles they had previously and are prevented from logging into the org with SAML. This includes roles that may be set with Just-In-Time provisioning. Double-check your mapping definitions and inspect your own assertions before enabling Mappings to prevent any scenarios where your users are unable to login.
{% /alert %}

Make changes to a mapping by clicking the pencil (**Edit**) icon, or remove a mapping by clicking the garbage (**Delete**) icon. These actions affect only the mapping, not the identity provider attributes or the Datadog roles.

Alternatively, you can create and change mappings of SAML attributes to Datadog roles with the `authn_mappings` endpoint. For more information, see [Federated Authentication to Role Mapping API](https://docs.datadoghq.com/account_management/authn_mapping/).

## Map SAML attributes to Teams{% #map-saml-attributes-to-teams %}

1. Ensure you selected either **SAML** or **All sources** when choosing your [provisioning source](https://docs.datadoghq.com/account_management/teams/#choose-provisioning-source) for team memberships.
1. [Cross-reference](https://support.okta.com/help/s/article/How-to-View-a-SAML-Response-in-Your-Browser-for-Troubleshooting?language=en_US) and [validate](https://www.samltool.com/validate_response.php) your SAML assertion to understand your IdP's attributes.
1. Go to **Organization Settings** and click the **SAML Group Mappings** tab.
1. Ensure the **Team Mappings** tab is selected.
1. Click **New Mapping**. A dialog box appears.
1. Specify the SAML identity provider `key-value` pair that you want to associate with a Datadog Team. **Note**: These entries are case-sensitive. **Note**: Every identity provider is different. Some allow you to set your attribute key or label. Others provide one by default. Datadog recommends you use an assertion inspector on your login to view the details of your particular assertion to understand how your Identity Provider is sending your group membership.
1. Select a **Team** from the dropdown menu.
1. To add an additional mapping, click **Add Row**.
1. When you are done adding mappings, click **Create**.
1. If you have not already done so, enable mappings by clicking **Enable Mappings**.

Make changes to a mapping by clicking the pencil (**Edit**) icon, or remove a mapping by clicking the garbage (**Delete**) icon. These actions affect only the mapping, not the identity provider attributes or the Datadog Team.

**Note:** Unlike Roles, Teams do not affect the login experience in any way. Datadog uses Team mapping purely as a provisioning source. For example, when a user does not belong to any Teams, they can still sign in to Datadog.
