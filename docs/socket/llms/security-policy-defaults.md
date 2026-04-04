# Source: https://docs.socket.dev/docs/security-policy-defaults.md

# Alert Actions

| Alert Action | Shows up in Dashboard | Developers see it (e.g., GitHub comment, CLI prints a warning) | Developers blocked (GitHub PR fails, CLI errors) |
| ------------ | --------------------- | -------------------------------------------------------------- | ------------------------------------------------ |
| Block 🚫     | ✅                     | ✅                                                              | ✅                                                |
| Warn ❗       | ✅                     | ✅                                                              | ❌                                                |
| Monitor 👁️  | ✅                     | ❌                                                              | ❌                                                |
| Ignore ➖     | ❌                     | ❌                                                              | ❌                                                |

### Legend

* **Block 🚫**: This action will fail the Socket CI/CD check, preventing the merge or deployment process until the issue is resolved. All related alerts will appear in the dashboard, developers will be notified, and further actions will be blocked.
* **Warn ❗**: This action indicates a potential issue that should be reviewed. It will appear in the dashboard and notify developers through comments or warnings, but it will not block the development process.
* **Monitor 👁️**: This action is used for tracking alerts that require monitoring over time. Alerts will be visible in the dashboard, but no notifications will be sent to developers, and it won't block any processes.
* **Ignore ➖**: This action is set for low-priority alerts or informational notifications. The alerts will not show up in the dashboard, and there will be no notifications or blocks applied.

## Ignore

Set alerts to "Ignore" if you don't want to see these alerts at all. This is great for cutting out noise and focusing on what matters in your project or organization. Alerts set to “Ignore” won't pop up in your pull requests (PRs) or merge requests (MRs), nor anywhere in the Socket platform, including in the Socket Dashboard (including Organization Alerts and Report Runs).

## Monitor

Choose "Monitor" for alerts you're still evaluating. You'll see these in the Socket Dashboard, including in the organization-wide alert page and report summaries. This way, you can keep an eye on them without alerting developers or cluttering your PRs or MRs with potential false alarms.

Alerts in Monitor mode display findings in:

* Socket Dashboard (including Organization Alerts and Report Runs)

## Warn

Switch to "Warn" for alerts you trust and need to act on. These will show up in your PRs or MRs, the Socket Dashboard, and through any integrations you've set up, like Slack notifications or security incident and event management (SIEM) systems. It's for when you're ready to take findings seriously but not let them stop developer work.

Alerts in Warn mode display findings in:

* Developers' PRs or MRs
* Socket CLI (e.g. `socket ci` , `socket report create` , and safe-npm)
* Socket Dashboard (including Organization Alerts and Report Runs)
* Integrations (e.g. Slack alerts, Vanta, SIEM integrations)

## Block

"Block" is for the highest confidence and severity issues. Using this will fail the Socket CI/CD check effectively blocking the PR or MR until the issue is resolved. This level is strict: if a Socket scan fails, so does your PR or MR. To prevent developers bypassing these alerts, GitHub users, for example, can enable branch protection and set the PR to fail if the Socket scan fails.

Alerts in Block mode display findings in:

* Developers' PRs or MRs
* Socket CLI (e.g. `socket ci` , `socket report create` , and safe-npm)
* Socket Dashboard (including Organization Alerts and Report Runs)
* Integrations (e.g. Slack alerts, Vanta, SIEM integrations)