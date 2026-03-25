# Source: https://docs.gitguardian.com/public-monitoring/remediate/remediate-incidents.md

# Source: https://docs.gitguardian.com/internal-monitoring/remediate/remediate-incidents.md

# Remediate incidents

> Platform features for remediating secret incidents: developer collaboration, workflow customization, and direct secret revocation.

This guide covers GitGuardian's platform features that support your remediation efforts, including collaboration tools, automation capabilities, and integrated secret management.

> **New to remediation?** Start with our [Remediation Overview](./remediation-overview.md) to understand GitGuardian's approach, then choose the appropriate [Remediation Scenario](./remediation-scenarios/overview.md) for your situation.

## Collaborating with developers

Involving developers is crucial for the remediation. Developers also have knowledge about the secret itself, since they are the ones who used it. They also understand the system's architecture and the services that may depend on the secret. They can provide insight into affected services and the best way to mitigate issues. This knowledge is essential in creating an effective and efficient remediation plan.

GitGuardian's goal is to enable easy collaboration with your developers by providing flexible ways to share your incidents.

### Share the incident

You can collaborate by sharing the incident in two ways:

- Internally, with users registered on the dashboard, via the "Grant access" action. This option is only available for Business workspaces.
- Externally, with non-registered users, via the "Public sharing" action.

:::info
When you share an incident, the **entire incident with all its occurrences** is shared, not just individual occurrences. This provides complete context for effective remediation collaboration.
:::

![share button](/img/platform/collaboration-and-sharing/share-button.png)

More details are available in our dedicated [Collaboration and sharing section](../../platform/collaboration-and-sharing/incident-permissions-and-sharing.md).

### Collect the feedback

The feedback form enables you to collect standardized feedback about an incident. To fill out the form, registered users require the "Can edit" incident permission. They can also edit or delete their own feedback.

![Feedback form](/img/internal-monitoring/remediate/incident-detail/feedback-form.png)

Whenever feedback is submitted for an incident, whether by a registered user or a non-registered user, an email notification is sent:
- to the incident assignee, if applicable.
- to all users with access to the incident, if there is no assignee.

Every action taken by the developer will be logged in the incident details timeline.

> The feedback form is not customizable yet.

## Workflow customization

GitGuardian displays a default remediation workflow on each incident's details page to guide remediation efforts. Organizations can customize this workflow to match their specific policies and procedures.

![GitGuardian Remediation section](/img/internal-monitoring/remediate/incident-detail/remediation-section.png)

### Customizing workflows

Workspace Managers can customize remediation workflows in the [Secrets detection settings](https://dashboard.gitguardian.com/settings/secrets/general):

- **Create custom workflows** - Define up to 20 custom steps with titles, descriptions, and links
- **Switch between workflows** - Choose between default GitGuardian workflow and custom versions  
- **Edit existing workflows** - Add, modify, delete, or reorder steps as needed
- **Apply organization-wide** - Custom workflows appear on all incident pages and shared incidents

This customization helps ensure remediation follows your organization's established security procedures and compliance requirements.

### Custom messages when using GitGuardian CLI (ggshield)

When GitGuardian CLI detects secrets in developers' code, whether in pre-commit or other stages, it is highly beneficial to provide them with clear instructions on using secrets in their code according to company standards (Vaults, Environment variables, ..).

Security teams have the ability to customize these messages, which will be disseminated through the CLI at different stages of the Software Development Life Cycle such as pre-commit, pre-push, and pre-receive.

[Learn more here](../../ggshield-docs/reference/secret/custom-remediation-messages.md)

## Secret Manager integration

GitGuardian integrates with Secret Managers through **[ggscout](/ggscout-docs/home)** to streamline the remediation process:

### Key capabilities

- **Push-to-vault** - Move exposed secrets directly to your Secret Manager from the GitGuardian dashboard
- **Secret identification** - Automatically tag incidents when secrets are already vaulted
- **Remediation tracking** - Monitor progress from detection through secure storage implementation

### Supported integrations

GitGuardian works with major Secret Manager platforms to provide seamless remediation workflows. The integration helps identify which secrets need to be moved to secure storage and facilitates the transition process.

**[Learn more about Secret Manager integrations](/internal-monitoring/integrate-sources/secrets-managers-integrations/overview.md)**

## Secret revocation from GitGuardian

GitGuardian's integrated secret revocation feature enables you to revoke valid secrets directly from the platform for supported providers, drastically reducing the time secrets remain exposed and accelerating your incident response workflows.

This feature eliminates the need to switch between multiple tools and platforms during remediation, providing a streamlined path from detection to resolution.

:::success Pre-requisites
- The secret shall have aÂ **Valid**Â status.
- You shall have `Full Access` permissions on the incident.
- The secret revocation is supported by the provider. 
:::

### Supported providers

Secret revocation is currently available for the following providers:

- **GitHub**Â personal access tokens and fine-grained tokens.
- **GitLab**Â personal access tokens.
- **OpenAI**Â API keys.

:::info
GitGuardian actively advocates with service providers to adopt programmatic revocation capabilities and implement standardized revocation endpoints, making secret management more secure across the ecosystem.
Additional providers are being added regularly. Check back for updates or contact support to request specific provider support.
:::

### Enabling secret revocation

The secret revocation feature can be toggled on or off in your workspace settings: 

1. Navigate to [**Settings > Secrets > General**](https://dashboard.gitguardian.com/settings/secrets/general).
2. Locate the **Secret Revocation** toggle. 
3. Toggle the feature on or off as needed. 

:::info
Workspace Managers and Owners can control this setting. When disabled, the revoke button will not appear on incident details pages.
:::

### Filtering for revocable incidents

Focus your team's efforts on these high-impact, actionable incidents that can be immediately revoked:

1. Navigate to your incidents list. 
2. Filter secrets `Valid` secrets using `Secret Validity`.  
3. Filter revocable secrets using `Revocable by GitGuardian` GitGuardian tag. 

![Filter Revocable Secrets](/img/internal-monitoring/remediate/revoking-secrets/filtering-revocable-secrets.png)

### Revoking a secret

:::warning Assess Revocation Impact
Revoking a secret may have dramatic side effects on your systems, applications, or workflows. Therefore, you should always consider checking what the revocation will impact before proceeding.

GitGuardian provides you with a lot of context and insights to [assess the impact of the exposure](/internal-monitoring/remediate/investigate-incidents), but more importantly, [measure the impact of the revocation](/nhi-governance/discover-your-nhis#exploration-map), thanks to the identification of the workloads using these credentials. 
:::

To revoke a secret directly from GitGuardian:

1. **Navigate to the incident**: Open the incident details page for the secret you want to revoke.
2. **Locate the revoke button**: Find the **Revoke** button in the secret details right-panel section.

![Revoke Secret](/img/internal-monitoring/remediate/revoking-secrets/revoke-action.png)

3. **Initiate revocation**: Click **Revoke** to open the confirmation dialog. 
4. **Confirm the action**: Confirm the revocation by inserting `revoke` in the modal dialog. 

![Confirm Revoke Secret](/img/internal-monitoring/remediate/revoking-secrets/confirm-revocation.png)

5. **Monitor the timeline**: The revocation action will be automatically logged in the incident timeline. 

### After revocation

Once a secret is revoked, GitGuardian automatically re-runs the validity checker. If successful: 
- The secret status changes from `Valid` to `Invalid`.
- The linked incident status changes to `Resolved` assuming Playbook [Automatically resolves incidents when valid secrets are revoked](../../platform/automate-with-playbooks/available-playbooks.md#auto-resolve-revoked-secrets) is enabled. 

All revocation activities are logged in the incident timeline for audit and compliance purposes.

:::info Provider limitations
Most revocation APIs do not explicitly confirm successful revocation. GitGuardian relies on subsequent validity checks to determine if the revocation was successful.
:::

## Automate remediation with playbooks

GitGuardian playbooks can automate many remediation tasks for internal incidents, reducing manual work and accelerating response times.

Learn more about [configuring playbooks](../../platform/automate-with-playbooks/playbooks-overview.md) for your workspace.

The playbooks relevant to Internal Monitoring are:
- Auto-share incident access to the author of the leak (link by email)
- Auto-grant incident access to author of the leak (in-app)
- Auto-resolve incident when valid secret is revoked
- Auto-ignore incidents when secrets are tagged as false positive
- Auto-ignore incidents when secrets are directly marked as invalid

See the complete detail of [available playbooks](../../platform/automate-with-playbooks/available-playbooks.md).
