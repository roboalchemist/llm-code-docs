# Source: https://render.com/docs/team-members.md

# Workspaces, Members, and Roles — Create your workspace, add collaborators, and manage access.

Everything you create on Render (services, datastores, and so on) belongs to a *workspace*. Every workspace has an associated [plan](/pricing) that determines available features and how many [team members](#manage-team-members) you can invite.

When you sign up for Render, we automatically create your first workspace on the free *Hobby* plan. You can [create additional workspaces](#create-a-workspace) or [change a workspace's plan](#change-a-workspaces-plan) at any time.

> With an Enterprise plan, you can manage multiple workspaces and team members in a unified [organization](enterprise-orgs).

## Create a workspace

> *You can have up to five Hobby workspaces.*
>
> You can create an unlimited number of paid workspaces.

1. In the [Render Dashboard](https://dashboard.render.com), open the workspace dropdown at the top of the left pane, then click *+ New Workspace*:

   [image: Creating a new workspace in the Render Dashboard]

2. Complete the workspace creation flow, including specifying a plan type and payment method. Then click *Create Workspace*.

You're all set! Render creates your workspace and assigns you the [*Admin* role](#member-roles). You can switch between your different workspaces from the same dropdown.

Now you can start creating services and other resources in your workspace. With a *Professional* workspace or higher, you can also [invite team members](#manage-team-members).

## Change a workspace's plan

You can change your workspace's plan in the [Render Dashboard](https://dashboard.render.com):

1. Open the workspace dropdown in the top-left corner and select *Billing*.
2. Under the *Plan* section, click *Update Plan*.
3. Click the *Choose* button for your desired plan.
   - To switch to an *Enterprise* plan, instead please [contact sales](/contact).
4. Review the details of your plan change, including any reduction in available features if you're downgrading.
5. Click *Confirm*.

Your plan change takes effect immediately. You can view your workspace's current plan from the *Billing* page at any time.

## Manage team members

> *You can't add team members to a *Hobby* workspace.*
>
> First, [upgrade your workspace](#change-a-workspaces-plan) to *Professional* or higher.

Team members with the [*Admin* role](#member-roles) can manage other team members (including other admins):

1. From your workspace's home in the [Render Dashboard](https://dashboard.render.com), click *Settings* in the left pane.

2. Scroll down to the *Team members* section.
   - *To add a team member,* click *+ Invite members*. Provide the member's email address and select a [role](#member-roles) from the dropdown.
   - *To remove a team member,* open the *•••* menu next to that member and click *Remove team member*.
   - *To change a team member's [role](#member-roles),* click their _current_ role and select a new one.

## Member roles

Each member of a workspace has one of the following roles:

------

###### Role

*Admin*

###### Description

- Has full access to the workspace's resources _and_ organizational settings (such as [member management](#manage-team-members), [billing management](https://dashboard.render.com/billing), and [secure login enforcement](login-settings#enforcing-secure-login)).
- Can also designate individual project environments as [protected](projects#protected-environments).
- A workspace's creator is automatically assigned this role.

---

###### Role

*Developer*

###### Description

- Has access to the workspace's resources (services, environment groups, and so on), but _not_ organizational settings.
- Access is limited for resources in a [protected environment.](projects#protected-environments)

---

###### Role

*Contributor*

###### Description

*Requires an Organization plan or higher.* Similar to the *Developer* role, with the following additional restrictions:

- Can't view sensitive fields (billing info, connection strings, environment variables, and so on).
- Can't access running services via SSH or the Shell tab in the [Render Dashboard](https://dashboard.render.com).
- Can't create, modify, or delete most resources.

---

###### Role

*Viewer*

###### Description

*[Enterprise orgs](enterprise-orgs) only.*

- Has _read-only_ access to most of the workspace's resources (services, environment groups, and so on).
- Can't view service logs or sensitive fields (billing info, connection strings, environment variables, and so on).

---

###### Role

*Billing*

###### Description

*[Enterprise orgs](enterprise-orgs) only.*

- Has full access to the workspace's billing settings, including updating payment method. Can also view non-sensitive details of the workspace's resources (such as members and service names).
- Learn more about the [Billing role](enterprise-orgs#the-billing-role).

------

Admins can reassign member roles from the *Workspace Settings* page in the [Render Dashboard](https://dashboard.render.com).

> In an [Enterprise organization](enterprise-orgs) with multiple workspaces, org members can have a different role in each workspace.

## Role permissions

> 🟢 Permitted
>
> ❌ Not permitted
>
> 🟨 Permitted with restrictions (details vary by permission)

### Workspace administration

| Permission | Admin | Developer | Contributor | Viewer | Billing |
| --- | --- | --- | --- | --- | --- |
| *View workspace members* | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 |
| *Edit workspace settings* | 🟢 | ❌ | ❌ | ❌ | 🟨 Billing settings only. |
| *Add/remove workspace members* | 🟢 | ❌ | ❌ | ❌ | ❌ |
| *Export [audit logs](audit-logs)* | 🟢 | ❌ | ❌ | ❌ | ❌ |
| *View billing details* | 🟢 | 🟢 | ❌ | ❌ | 🟢 |
| *Edit payment method* | 🟢 | ❌ | ❌ | ❌ | 🟢 |
| *Leave workspace* | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 |
| *Delete workspace* | 🟢 | ❌ | ❌ | ❌ | ❌ |

### Projects and environments

| Permission | Admin | Developer | Contributor | Viewer | Billing |
| --- | --- | --- | --- | --- | --- |
| *View projects* | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 |
| *Create/modify projects* | 🟢 | 🟢 | ❌ | ❌ | ❌ |
| *Delete projects* | 🟢 | 🟨 Can't delete a project with at least one [protected environment.](projects#protected-environments) | ❌ | ❌ | ❌ |
| *View environments* | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 |
| *Create environments* | 🟢 | 🟢 | ❌ | ❌ | ❌ |
| *Modify/delete environments* | 🟢 | 🟨 Non-[protected environments](projects#protected-environments) only. | ❌ | ❌ | ❌ |
| *Designate an environment as [protected](projects#protected-environments) or [network-isolated](projects#blocking-cross-environment-traffic)* | 🟢 | ❌ | ❌ | ❌ | ❌ |
| *Move resources into or out of an environment* | 🟢 | 🟨 Non-[protected environments](projects#protected-environments) only. | ❌ | ❌ | ❌ |
| *Manage environment secrets* | 🟢 | 🟨 Non-[protected environments](projects#protected-environments) only. | ❌ | ❌ | ❌ |

### Services and datastores

| Permission | Admin | Developer | Contributor | Viewer | Billing |
| --- | --- | --- | --- | --- | --- |
| *View services* | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 |
| *Create services* | 🟢 | 🟨 Non-[protected environments](projects#protected-environments) only. | ❌ | ❌ | ❌ |
| *Modify service configuration* | 🟢 | 🟨 Can't perform potentially destructive modifications to services in a [protected environment.](projects#protected-environments) | ❌ | ❌ | ❌ |
| *Trigger service deploys* | 🟢 | 🟢 | 🟢 | ❌ | ❌ |
| *Trigger [rollbacks](rollbacks)* | 🟢 | 🟢 | 🟢 | ❌ | ❌ |
| *Delete services* | 🟢 | 🟨 Non-[protected environments](projects#protected-environments) only. | ❌ | ❌ | ❌ |
| *View connection strings and credentials for datastores* | 🟢 | 🟨 Non-[protected environments](projects#protected-environments) only. | ❌ | ❌ | ❌ |
| *Modify access control IPs for datastores* | 🟢 | 🟨 Non-[protected environments](projects#protected-environments) only. | ❌ | ❌ | ❌ |
| *Access running services via SSH or the Shell tab* | 🟢 | 🟨 Non-[protected environments](projects#protected-environments) only. | ❌ | ❌ | ❌ |

### Observability

| Permission | Admin | Developer | Contributor | Viewer | Billing |
| --- | --- | --- | --- | --- | --- |
| *View service events* | 🟢 | 🟢 | 🟢 | 🟢 | ❌ |
| *View [service metrics](service-metrics)* | 🟢 | 🟢 | 🟢 | 🟢 | ❌ |
| *View [service logs](logging)* | 🟢 | 🟢 | 🟢 | ❌ | ❌ |

### Integrations

| Permission | Admin | Developer | Contributor | Viewer | Billing |
| --- | --- | --- | --- | --- | --- |
| *Configure [notification settings](notifications)* | 🟢 | ❌ | ❌ | ❌ | ❌ |
| *Create and configure [webhooks](webhooks)* | 🟢 | ❌ | ❌ | ❌ | ❌ |
