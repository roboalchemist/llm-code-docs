# Source: https://docs.gitguardian.com/platform/collaboration-and-sharing/incident-permissions-and-sharing.md

# Incident permissions and sharing

> Configure incident access permissions and share incidents externally with developers who are not workspace members.

GitGuardian is designed to be super collaborative yet very secure. Learn how to use incident permission levels and our sharing capability to do so, so users only access and do what you want them to access and do.

## What are incident permissions

Incident permissions define the set of actions that users can perform on the incident in question:

- **Can view**: they can view the incident and be assigned to it.
- **Can edit**: they have the "Can edit" permissions, plus the ability to resolve, ignore, change severity and custom tags, comment and provide feedback on an incident.
- **Full access**: they have the "Can edit" permissions, plus the ability to share the incident within the workspace or publicly.

Any time you manually grant someone access to an incident, you will need to set their incident permissions. The default incident permission is `Can edit`.

![Incident permissions dropdown in the share modal](/img/platform/collaboration-and-sharing/incident-permissions-dropdown-share-modal.png)

Those advanced granular incident permissions are only allowed in the Business plan, thus:

- **any workspace under the Free plan works as if only the `Full access` incident permission was present**.
- when switching from the Business plan to the Free plan (eg: end of contract or end of business trial), **all people who do not have `Full access` incident permission are considered deactivated**.

## Granting access to incidents

GitGuardian has a sharing capability internal to the workspace: this is called the "Grant Access" feature. This makes it possible to share an incident with a person registered on the workspace or even a team.

:::info
The "Grant access" capability is a feature reserved for workspaces under the Business plan.
Only people with `Full access` incident permissions can use the "Grant access" feature.
:::

### Granting access to individuals

Sometimes you will want to share an incident only with certain other members of your workspace to gain their expertise or knowledge.

1. Click on **Share** at the top-right-hand corner of the incident you want to share.
2. Search for the people you want by typing in their name or email address.
   Since workspace Managers have access to all incidents of the workspaces, **only Members and Restricted are eligible to be selected**.
3. You can set their incident permission from the dropdown in the input.
4. Click on **Grant access**.
5. An email is then sent to these people to notify them of their new access.

![Grant access to individuals](/img/platform/collaboration-and-sharing/grant-access-to-individuals.png)

By default, users with `Member` or `Restricted` access level and `Full access` incident permission can enter the email address of someone who is not yet registered in the workspace.
This behavior can be deactivated via a workspace setting. Please refer to [this page](../enterprise-administration/workspace-settings.md) for more details.

#### How can I automate this incident workflow?

If you are under our Business plan (or in Business trial), you can automate this entire process with our [Auto-access granting playbook](../automate-with-playbooks/available-playbooks.md#auto-grant-access-to-involved-developer-in-app)

### Granting access to entire teams

Sometimes you will want to share an incident with an entire team to better collaborate on an incident.

1. Click on **Share** at the top-right-hand corner of the incident you want to share.
2. Search for the teams you want by typing in their name.
3. You can set the incident permission of those teams from the dropdown in the input.
4. Click on **Grant access**.
5. An email is then sent to all teammates belonging to the teams to notify them of their new access.

![Grant access to teams](/img/platform/collaboration-and-sharing/grant-access-to-teams.png)

## Revoking access

If you want to revoke access to the incident for a specific person or team.

1. Click on **Share** at the top-right-hand corner of the incident.
2. To the right of the team's name or the individual's name, click on the bin icon.You can use the search bar at the top of the modal if needed.

![Revoke access](/img/platform/collaboration-and-sharing/revoke-access.png)

If a team has access to an incident because it occurred on their perimeter, access cannot be revoked.

![Revoke access not Authorized for team with perimeter involved](/img/platform/collaboration-and-sharing/revoke-access-not-authorize-for-team-with-perimeter-involved.png)

If a user is assigned to an incident, access cannot be revoked. The assignment needs to be changed first for access to be revoked.

## Sharing incidents publicly

GitGuardian has a sharing capability external to the workspace. This allows you to share an incident on the web via a single link accessible to everyone, even those who are not registered in your workspace.

Public sharing can be deactivated via a workspace setting. Please refer to [this page](../enterprise-administration/workspace-settings.md) for more details.

:::info
Under Business plan, only people with `Full access` incident permissions can share the incident publicly.
Under Free plan, every user can share the incident publicly.
:::

### Creating the public share link

You can share any incident by turning on the sharing switch. Such action will **generate a unique link** containing by default:

- the **incident** with the secret visible,
- its **occurrences** with links to their locations on the VCS and the resulting check of their presence in the git history,
- the resulting check of the secret's **validity**,
- **"How to remediate"** guidelines.

This link will automatically expire either 30 days after its creation or 5 days after the incident is closed, whichever of the two dates is earlier. A new link can be generated at any time after the expiration of the previous one.

![Incident public sharing](/img/platform/collaboration-and-sharing/public-sharing.png)

The publicly accessible page of the incident via the unique share link looks like this:

![Public share page](/img/platform/collaboration-and-sharing/public-share-page.png)

### Enabling feedback collection

The feedback collection process can be achieved via this link. The sharing link of an incident has a **"Feedback collection" option**.
When this option is on, an entire section becomes available in the shared page where **the person having access to it can submit their feedback**.

![Public share page feedback panel](/img/platform/collaboration-and-sharing/public-share-page-feedback-panel.png)

When the feedback is submitted, it will be **directly visible on the incident page of your GitGuardian dashboard** under the **"Feedback" section**.

![Incident feedback panel](/img/internal-monitoring/remediate/incident-detail/feedback-panel.png)

:::info
This "Feedback collection" option is ON by default whenever a share link is generated manually.
The feedback form is not customizable yet.
:::

### Allowing auto-healing

The share link also provides a **"Resolve or ignore via link" option**. 
When turned on, you enable the **auto-healing of the incident**: the person who has access to the link can close the incident themselves. An entire section becomes accessible within the shared page to enable "Resolve" and "Ignore" actions.

![Public share page auto healing panel](/img/platform/collaboration-and-sharing/public-share-page-auto-healing-panel.png)

This is particularly useful if **you want to reduce your workload and if you trust members of your team external to your dashboard**, namely the developer responsible for the leak, to properly remediate the incident.

:::info
This "Auto-healing" option is OFF by default whenever a share link is generated manually as GitGuardian considers closing an incident as a sensitive action.
:::
