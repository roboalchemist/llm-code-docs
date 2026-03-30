# Source: https://docs.gitguardian.com/internal-monitoring/remediate/remediation-scenarios/realtime-incidents.md

# Real-time incidents

> How to establish remediation processes for real-time secret incidents by involving developers through external sharing or workspace membership.

After adding automated secrets detection to your repositories, you need to establish precise remediation processes for the real-time incidents that the GitGuardian Internal Monitoring platform will raise.

At this stage, you will have to determine:

- Which team/role is responsible for remediating the incidents. Which team/role will be held accountable for the open incidents.
- Which team/role to consult during the remediation process (e.g. DevOps engineers might have to intervene to avoid service outages while rotating secrets).
- How much autonomy/trust you are willing to give developers for incident remediation.

At GitGuardian, we believe developers should be front-and-center when it comes to remediating incidents they are responsible for. To bring your security teams and developers together, GitGuardian Internal Monitoring suggests two options:

- The first one is to provide external access to incidents a developer is involved in.
- The second one requires the developer to sign up to GitGuardian and join your workspace to view their incidents in-app.
  Both options can be automated with what we call [Playbooks](../../../platform/automate-with-playbooks/playbooks-overview.md). These are process flows running a series of automated jobs without the manual intervention of your security or software engineers.

### Option 1. Using the dev-in-the-loop feature to provide external access

You can automate the incident sharing process with the developers involved using the "Auto-share incident access to the author of the leak" playbook. Whenever a new incident is detected, GitGuardian will send an email with a unique link to the developer to view the incident details on a standalone (external) page.

You can also choose which options to apply to the sharing link:

- Feedback collection option: the ability for the developer to submit feedback on the incident on the external page.
- Resolution capability option: the ability for the developer to resolve or ignore the incident on the external page.

In the early stages of the rollout, security teams will likely have to go all out when it comes to verifying the progress of developers on remediation â the feedback collection option is helpful here. This option provides security teams with more context about incidents but leaves taking care of the resolution to their members.

As both teams advance and become more comfortable with their collaboration and remediation processes, we recommend security teams embrace the trust but verify principle. In the long run, we advise that developers are empowered to resolve their incidents with as little intervention as possible from security teams â the auto-share with resolution capability option is useful here.

### Option 2. Inviting developers to join your workspace

:::caution
[SSO authentication](../../../platform/enterprise-administration/saml-sso-configuration.md) needs to be activated on your workspace for this scenario to function. You are also responsible for sending the SSO login URL to your team members ahead of the rollout.
:::

You can automate the process of giving access to incident details in the GitGuardian dashboard for members with a Restricted access level (usually reserved for developers) thanks to the auto-access granting playbook.

GitGuardian will automatically give the Restricted user access to the incident details page in the dashboard by matching
the commit author email against the dashboard user email. To abide by the principle of least privileges, Restricted users
can only get access to their incidents in the dashboard. Restricted users cannot view the incidents of their teammates unless
they are given access by a workspace Manager (usually reserved for technical security leads or development leads).

Going with one or another depends on how close you want to pull your developers towards the remediation process. You can start with the external access option to explore how security and development teams should work together. Over time, you should consider migrating to the second option, where developers are part of your GitGuardian workspace.

We believe this option is more valuable for the following reasons:

- The auto-access granting playbook is not only for real-time incidents. It also applies to all historical incidents the developer committed before implementing GitGuardian. This playbook will be practical for Step 3. Remediating historical incidents (see below).
- Technical Security Leads will be able to track the progress of each developer on their incidentsâ remediation and notify them directly in the dashboard when needed.
- Developers with access to the dashboard can generate Personal Access Tokens to use ggshield CLI and implement secret scanning at the pre-commit level.
