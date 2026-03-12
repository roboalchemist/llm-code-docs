# Source: https://docs.statsig.com/access-management/guide.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Initial Setup Guide of your Workspace

<Info>
  Organizations and their related features are for Enterprise contracts only. Please reach out to our support team, your sales contact, or our [Slack channel](https://statsig.com/slack) if you need to enable Enterprise features as you use Statsig.
</Info>

## Overview

This initial setup guide aims to provide a **step-by-step guide** for a set of essential configurations that you would need to get started with Statsig on an Enterprise plan.

This guide is primarily written for **organization admins** who need to set up the initial environment and put the guardrails in place for the broader teams to start using Statsig.
It also includes some **best practices** to increase your operational efficiency and set your team up for success in the long run.

### Statsig Workspace Structure

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/N-GBxJsWYP5W8YJB/images/access_management_structure_diagram.png?fit=max&auto=format&n=N-GBxJsWYP5W8YJB&q=85&s=f9d4bdb57bd51f2863e6f04aab4244c2" alt="Statsig structure diagram" width="2156" height="832" data-path="images/access_management_structure_diagram.png" />
</Frame>

In Statsig, we have three constructs to help you organize your workspace and scale it out more broadly within your organization.

**Organization** is an enterprise-level environment that allows companies to create project(s) and bring members to work inside the project.

**Project** is a workspace within the organization where the configs (e.g., feature gates, experiments, layers, etc.), metrics, and SDK keys you and your team created lives.

**Team** is a group of members at the project level that can help your organization manage the permissions and ownership of resources.

#### Our Recommendation

In Statsig, each project within the organization is isolated from one another.
This means that **none** of the resources or data is shared among different projects, even if they are part of the same organization.

The Statsig team believe that the **sensible default structure** for most customers is having an organization with a **single project** where multiple teams contribute and collaborate inside.

We believe that different teams and functions across your organization can stay well-organized within a single project by leveraging features such as **[teams](/access-management/teams), [roles](/access-management/projects#roles), [tags](/access-management/tags),** and **[templates](/experiments/templates/templates)**.
This also removes the risk of costly migrations if some projects ever need to be consolidated in the future for cross-functional collaborations.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/N-GBxJsWYP5W8YJB/images/access_management_structure_anti_pattern.png?fit=max&auto=format&n=N-GBxJsWYP5W8YJB&q=85&s=10e6cff68692483bc3d7e6ed811dc052" alt="Statsig structure diagram anti pattern" width="2006" height="1332" data-path="images/access_management_structure_anti_pattern.png" />
</Frame>

Note that Statsig has rich support for **environments** within our resources.
We consider it an *anti-pattern* to create multiple projects just to manage lower environments separately from production.

### Setup Guide

#### Step 1: Setting up the Organization

When you sign an enterprise contract with Statsig, we will provision your existing Statsig account into an enterprise account.

Once provisioned, you will see that the [tab for Organization](https://console.statsig.com/settings?tab=organization) is now added to your account along with additional security and governance settings.

#### Step 2: Setting up SSO

We recommend configuring [**SSO**](/access-management/sso/overview) (Single Sign-On) for your Statsig organization to simplify the user experience while improving your security.

Statsig supports any Identity Provider that implements the **OIDC protocol** for SSO, such as [Okta](/access-management/sso/okta_sso), [Microsoft Entra ID](/access-management/sso/azuread), [Google](/access-management/sso/google), and more.
Additionally, consider integrating [**SCIM**](/access-management/scim/overview) (System for Cross-domain Identity Management) if you are using Okta as your identity provider.

New users who are provisioned via SSO will be assigned the *Member* Role unless you're using SCIM.

#### Step 3: Creating your Project

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/ozN4u5Ool0qeSBaN/images/access_management_project_view.png?fit=max&auto=format&n=ozN4u5Ool0qeSBaN&q=85&s=52f3aebc05544293fbcf7295fe4d729b" alt="Organization project administration interface" width="2432" height="1026" data-path="images/access_management_project_view.png" />
</Frame>

A project in Statsig serves as a workspace that contains everything you and your team will create. This includes configs (e.g., feature gates, experiments, dynamic configs, layers), metrics, integrations, and more.

When creating a new project, you can set its type to *Open* which would allow anyone in the organization to join freely, or to *Closed* which would allow people to join only by invitation or request.

#### Step 4: Setting up Roles

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/N-GBxJsWYP5W8YJB/images/access_management_roles.png?fit=max&auto=format&n=N-GBxJsWYP5W8YJB&q=85&s=4651f3e3ebc21bc4d59ce0e071b7e490" alt="Project roles interface" width="1788" height="1294" data-path="images/access_management_roles.png" />
</Frame>

Each person is assigned a role that defines their level of access within the project and organization.
We recommend reviewing the permissions set for each predefined roles so you can [assign the appropriate roles](/access-management/organizations#organization-members) or create a custom role that aligns with your organization's needs.

Common examples of custom roles include a *Metrics Admin* (responsible for managing metrics) and a *Data Warehouse Admin* (in Warehouse Native projects, responsible for managing warehouse connections).

#### Step 5: Inviting your team to the Organization

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/N-GBxJsWYP5W8YJB/images/access_management_invite.png?fit=max&auto=format&n=N-GBxJsWYP5W8YJB&q=85&s=2ca0d3b0f96a30d5fd9d5ee9c3276956" alt="Project invite interface" width="2004" height="1178" data-path="images/access_management_invite.png" />
</Frame>

If you’ve successfully configured SSO, your teams can now join the Statsig organization by signing in from the console and going through the request flow within your identity provider.

If you haven’t set up SSO yet, you can invite individual members to your organization and/or project in the console.

#### Step 6: Creating Teams within the Project

[Teams](/access-management/teams) can be created within the project to help with organization and ownership.

Once a team is configured and users are added to team, any configs created will be associated with the team that the user belongs to.
And these configs will automatically inherit all the default settings and templates from the team when they are created.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/N-GBxJsWYP5W8YJB/images/access_management_team_filter.png?fit=max&auto=format&n=N-GBxJsWYP5W8YJB&q=85&s=defd06c9aadf5ac3b4c1e87ec4c08e2d" alt="Team filter in experiments" width="2362" height="1258" data-path="images/access_management_team_filter.png" />
</Frame>

Team becomes extremely useful as multiple teams begin to use Statsig, as it helps with organization and governance, as well as onboarding of new users as it provides a set of defaults to work from.

As a best practice, you can require all resource creations to be attached to a team and have team admins (e.g., tech leads, engineering managers, etc.) add people to their corresponding teams, enabling them to start creating configs and metrics.

### Best practices

#### Setting up Review Policies

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/N-GBxJsWYP5W8YJB/images/access_management_reviews.png?fit=max&auto=format&n=N-GBxJsWYP5W8YJB&q=85&s=890645cd6b620946a771ab4f75ab30bc" alt="Review setting interface" width="2028" height="792" data-path="images/access_management_reviews.png" />
</Frame>

Within Statsig, you can enable [reviews](/guides/setting-up-reviews) for any changes to config and metric, requiring a second pair of eyes to review the change before they get deployed to production.

Note that you can **customize** your review policies to align with your organization’s needs.
For example, you can set up a team of reviewers by giving their roles a permission to approve the reviews.
You can also give certain roles (e.g., oncalls) the ability to self-approve or require reviews for production environment only to allow for agility when needed.

Each **team** also has team-level **review settings** that can require reviews for configs and metrics owned by specific team and allow only members and/or admins (with roles that permit approving reviews) of that specific team to be able to approve the reviews.

#### Setting up your API Keys

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/N-GBxJsWYP5W8YJB/images/access_management_sdk_env.png?fit=max&auto=format&n=N-GBxJsWYP5W8YJB&q=85&s=1d76e35483a757043c69c23e8d23eba4" alt="SDK environment interface" width="2344" height="1400" data-path="images/access_management_sdk_env.png" />
</Frame>

In Statsig, you have **Client API Keys** to initialize all Statsig [client SDKs](/client/introduction) and **Server Secret Keys** to initialize all Statsig [server SDKs](/server/introduction).

We believe there is a **"Crawl, Walk, Run"** phase when it comes to configuring your API keys:

* **Crawl:** Begin by creating API keys that are scoped to specific environment within Statsig for [environment-based evaluation](/guides/using-environments#1-environment-specific-sdk-keys).

* **Walk:** Next, create different API keys for each of the frontend clients (e.g., iOS, Android, and Web).

* **Run:** At scale, consider having different API keys at the service level where each backend service and its environments have their own keys.

This setup integrates seamlessly with [Target Apps](/sdks/target-apps) that can unlock additional performance and security.

#### Configuring Target Apps for API keys

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/N-GBxJsWYP5W8YJB/images/access_management_target_apps.png?fit=max&auto=format&n=N-GBxJsWYP5W8YJB&q=85&s=529ccfbf5e77d4263f8b228ecbb9f8a4" alt="Target apps interface" width="2010" height="978" data-path="images/access_management_target_apps.png" />
</Frame>

[Target app](/sdks/target-apps) is an attribute you can associate to your SDK keys and configs.
Through target apps, you can precisely set the scope of configs that will be accessed from each SDK key (which can also reduce the size of your payloads).

We highly recommend setting up target apps as you scale the usage of Statsig for [additional performance and security](/sdks/target-apps#motivation).

#### Setting up Notifications

Statsig has an integration with [Slack](/integrations/slack) that you can set up, so you can receive real-time notifications about the activities, status changes, and other useful alerts directly in your Slack workspace.

Additionally, you can configure to receive notifications in your [email](https://www.statsig.com/updates/update/email-notifs) as well for any alerts, reviews, reports, and more.


Built with [Mintlify](https://mintlify.com).