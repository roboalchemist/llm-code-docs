# Source: https://docs.gitguardian.com/platform/configure-alerting/notifiers-integrations/email-alerting.md

# Email alerting

> Configure email notification preferences for GitGuardian secrets incidents and workspace alerts.

GitGuardian sends an email to all members of the affected team anytime it detects an incident. To prevent alert
fatigue, only one email is sent for multiple occurrences of the same incident.

The members of a team will only receive emails for incidents within their team(s). If you want to receive emails for all the incidents of your workspace, make sure you're a member of the `all-incidents` team.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/vw3moD8iaL8?controls=0&modestbranding=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Email alerts

Email alerts include:

- Details of the incident (secret detector, repository and commit involved)
- Date of the incident
- A link to view the offending file directly on the source
- A link to the incident in the GitGuardian dashboard

> You can configure your email alerts in your [personal settings](https://dashboard.gitguardian.com/settings/personal/notifications). Read [our dedicated documentation on email preferences](../../user-account/email-preferences.md).

## FAQ

<!-- Why do we include the developer?-->

<!-- GitGuardian strongly believes that including the developer involved in the incident gives the greatest opportunity to remediate the leak quickly and efficiently.-->

**I just received an alert email on which I did not install GitGuardian. Why did this happen?**

**Public Alerts** are another type of GitGuardian alert that you may encounter.
They originate from our pro-bono public alerting service, which is not related to this application.

When GitGuardian detects a secret on a public GitHub repository, it alerts the developer responsible for the incident
through their commit email.

If you have received an alert email, please see our [remediation guide for leaks on public GitHub](../../../secrets-detection/secrets-detection-engine/leaks_remediation.mdx)
