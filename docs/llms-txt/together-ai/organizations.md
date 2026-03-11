# Source: https://docs.together.ai/docs/organizations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Organizations

## What is an Organization?

<Note>
  Organizations are in early access. To participate in our early access program, contact our [support team](https://portal.usepylon.com/together-ai/forms/support-request) or reach out to your Account Executive.
</Note>

Organizations let you collaborate with other users in a shared Together account. Once enabled, you can invite members by email, manage access to resources via Projects, and govern all usage under a single billing account.

## Organization Membership

There are two ways to manage who belongs to your Organization.

### Organization Membership via Single Sign-On (SSO)

With SSO, membership is managed automatically through your Identity Provider (IdP) like Okta or Google Workspace. Upon authentication with SSO, a user account is created and membership is automatically granted to the Organization. Access is revoked when a user is removed from your IdP — no manual management required.

<Warning>
  SSO and invitation-based membership cannot be used together. If your Organization uses SSO, inviting members via email is not supported. Contact our [support team](https://portal.usepylon.com/together-ai/forms/support-request) if you need to change your membership approach.
</Warning>

For setup and configuration, see [Single Sign-On (SSO)](/docs/sso).

### Managing Members With Invitations

Invitation-based membership lets you add and remove members manually by email. Members authenticate with one of our provided authentication methods (Google or GitHub OAuth).

#### How do I invite someone to my Organization?

Only Organization members with the "admin" role may send invitations. From your [Organization settings](https://api.together.ai/settings/organization), enter the email address of the user you want to invite and send the invitation. They'll receive an email with a link to accept.

Invitations can be sent to any email address — there are no domain restrictions.

#### Will people who share my email domain automatically join my Organization?

No. Sharing a domain (e.g., `@yourcompany.com`) does not automatically add anyone to your Organization. Every member must be explicitly invited.

#### Do Invitations Expire?

Invitations expire after **7 days**. If a user has not accepted a pending invitation within that window, a new invitation will need to be sent from your Organization settings.

#### Does a user need an existing Together account to accept an invite?

The user will be prompted to create a new Together account. Once their user account is set up and the invitation accepted, their user will be linked to your Organization and they'll have access to all shared resources. If they already have an existing Together account they'd like to migrate, reach out to our [support team](https://portal.usepylon.com/together-ai/forms/support-request).

#### Can I remove a member from my Organization?

Yes. Members with the "admin" role can remove any member at any time from the Organization settings. Removed members immediately lose their Project membership, which revokes their access to shared resources.

Any resources they created — fine-tuned models, endpoints, files — are not lost. Those resources remain inside the Project they were created within, so they persist even after a member is removed.

## Organization Role-based Access Control (RBAC)

Today, there are two roles — **Member** and **Admin** — with nearly identical permissions. Granular role-based access controls (RBAC) will roll out over time.

<Note>
  Fine-grained role-based access controls are on our roadmap and will be added in a future release.
</Note>

## Organization Projects

All members are automatically added to your Organization's default Project when they join the Organization. Through this Project, they have access to shared resources, including:

* Fine-tuned models
* Dedicated endpoints
* Serverless inference history
* Evaluations
* Instant clusters

Members can take any action on shared resources — including starting or stopping dedicated endpoints, which incurs costs.

### Multi-Project Support (early access)

Today, all resources and API keys belong to your Organization's default Project. Multi-Project support lets you create multiple Projects to segment resource access, spending, and workloads into isolated workspaces tailored to your team's structure.

Common ways to organize Projects:

* **By team:** Give your engineering, data science, and ops teams their own Projects with separate resource access
* **By environment:** Separate development, staging, and production workloads
* **By workload:** Isolate fine-tuning jobs from inference endpoints

Multi-Project support and Project-level membership management are in early access. Contact our [support team](https://portal.usepylon.com/together-ai/forms/support-request) to learn more.

### Project API Keys

Project members jointly manage the Project's API keys. API keys are project-scoped — customers who do not have multi-project support have API keys that belong to their default Project, where all resources currently exist.

When creating a new key, **copy it immediately** — it's only shown once. If you lose it, you'll need to create a new one.

Existing API keys are not affected when someone joins an organization — all prior keys continue to work.

## Billing

Usage across all Organization members is consolidated and billed to the Organization. Members are not billed separately.

All members can purchase credits and spend them. Keep in mind that member spending counts against the organization's shared balance. See [Credits & Billing](/docs/billing-credits) for details.


Built with [Mintlify](https://mintlify.com).