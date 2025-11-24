# Source: https://configcat.com/docs/organization.md

# Organization & Roles

An *Organization* represents a collection of preferences that apply to all your *Products* and *Members* in that *Organization*. This includes things like billing information, sign-in methods, and data privacy settings.

The *Manage Organization* menu is only available for *Organization Admins*.

![Organization-menu](/docs/assets/organization-menu.png)

## Organization Admin role[​](#organization-admin-role "Direct link to Organization Admin role")

*Organization Admins* have full access to the entire organization and all products. For example, they can:

* Add or remove members
* Set up security settings
* Change sign-in methods
* Create or delete products, feature flags, and environments

They **do not** have access to billing or subscription settings unless they are also *Billing Managers*.

Only *Organization Admins* can assign or remove the *Organization Admin* role from others.

## Billing Manager role[​](#billing-manager-role "Direct link to Billing Manager role")

Only *Billing Managers* can:

* View and update billing information
* Change the subscription plan
* Assign or remove the *Billing Manager* role from others

*Billing Managers* **cannot** access products, environments, configs, or feature flags, unless they are also *Organization Admins*.
