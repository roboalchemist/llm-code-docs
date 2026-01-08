# Alerts and notifications

Source: https://semgrep.dev/docs/semgrep-appsec-platform/notifications

- [](/docs/)- [Scan](/docs/getting-started/quickstart)- Set up and deploy scans- Notifications**On this page- [Deployment](/docs/tags/deployment)- [Semgrep AppSec Platform](/docs/tags/semgrep-app-sec-platform)Alerts and notifications
You can receive notifications for Semgrep findings in the following channels:

ChannelSemgrep CodeSemgrep Supply ChainSemgrep Secrets[Slack](/docs/semgrep-appsec-platform/slack-notifications)Integrate with Semgrep through **Settings &gt; Integrations**. Customize through rule modes in [Policies page](/docs/semgrep-code/policies).Integrate with Semgrep through **Settings &gt; Integrations**. Limited customizability; configured by default to send notifications on **reachable** findingsIntegrate with Semgrep through **Settings &gt; Integrations**. Customize through policies in [Policies page](/docs/semgrep-secrets/policies) [Email](/docs/semgrep-appsec-platform/email-notifications)Not availableNot available[Webhooks](/docs/semgrep-appsec-platform/webhooks)Not availableNot available
Setting up notifications involves the following steps:

- Integrating the notification channel, such as Slack, with Semgrep.
- Customizing the conditions under which a notification is sent to that channel. Available conditions and how they are set up varies depending on the Semgrep product; see the following table.

Semgrep Code **rule modes** define workflow actions (**Monitor**, **Comment**, or **Block**) that Semgrep Code performs when a rule detects a finding. In addition to these workflow actions, you can also configure Semgrep to send notifications on any rule mode.

Click to expand table of rule modesRule modeDescriptionMonitorRules in **Monitor mode** display findings only in: - Semgrep AppSec Platform- **For Semgrep Code and Supply Chain**: User-defined notificationsSet rules to this mode to evaluate their true positive rate and other criteria you may have. By keeping rules in Monitor, developers do not receive potentially noisy findings in their PRs or MRs.CommentRules in **Comment mode** display findings in:- Developers&#x27; PRs or MRs- Semgrep AppSec Platform- **For Semgrep Code and Supply Chain**: User-defined notificationsSet rules that have met your performance criteria to this mode when you are ready to display findings to developers.BlockRules in **Block mode** cause the scan job to fail with an exit code of `1` if Semgrep Secrets detects a finding from these rules. You can use this result to enforce a block on the PR or MR. For example, GitHub users can enable branch protection and set the PR to fail if the Semgrep step fails. These rules display findings in:- Developers&#x27; PRs or MRs- Semgrep AppSec Platform- **For Semgrep Code and Supply Chain**: User-defined notificationsThese are typically high-confidence, high-severity rules.
## View integrations[​](#view-integrations)
To view all integrations available to you in Semgrep AppSec Platform, follow these steps:

- Sign in to your [Semgrep AppSec Platform ](https://semgrep.dev/orgs/-/settings/integrations) account.
- Click **Settings &gt; Integrations**.

***Figure***. The integrations available in Semgrep AppSec Platform.

## Next steps[​](#next-steps)
Refer to the specific documentation page for the notification channel you want to set up.

Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Deployment](/docs/tags/deployment)- [Semgrep AppSec Platform](/docs/tags/semgrep-app-sec-platform)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/semgrep-appsec-platform/notifications.md)Last updated on **Jul 28, 2025**