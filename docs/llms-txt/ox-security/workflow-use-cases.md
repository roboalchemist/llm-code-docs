# Source: https://docs.ox.security/automate-with-ox-workflows/creating-a-workflow/workflow-use-cases.md

# Workflow Examples

The following examples illustrate how workflows can be applied to real-world scenarios.\
Each use case shows the trigger, conditions, and resulting actions.

## Use Case 1: Critical secret exposure in public repo

Secrets in code, such as tokens, passwords, or API keys, can expose your organization to immediate risk.

This workflow shows how OX can separate harmless detections from business-critical exposures. Inactive secrets are downgraded and tracked with low severity, while active secrets create alerts and tickets.\
This structure minimizes false alarms while ensuring urgent threats are prioritized immediately.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-ca65995f68b95cbecab27344645694d862c10eb2%2FSecret_in_code_wf.png?alt=media" alt=""><figcaption></figcaption></figure>

The workflow in this scenario contains several branching paths. Each node in the workflow builder represents a condition or an action.

* Secret in Code (Trigger)
* Inactive Secret (Condition)
* Active Secret Exposure (Condition)
* Secret in a Public Repo (Condition)
* Change Severity: Low (Action)
* Change Severity: Apocalypse (Action)
* Slack Message: Security-Alert (Action)
* Jira Ticket: OXDEV (Action)

## Use case 2: SLA violation reminder

The SLA Violation Reminder workflow helps teams stay on top of unresolved issues that exceed their defined Service Level Agreement (SLA).\
Instead of leaving overdue issues unnoticed, the workflow automatically escalates them and ensures visibility across communication and ticketing systems.

SLA management is critical in application security because it ties remediation timelines to business risk. This workflow ensures that high-severity issues do not linger without attention. By sending reminders, alerts, and escalations, it keeps security and development teams accountable.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-bd227715154ec536778e589ec470c642bbf66782%2FSLA_violation_reminder.png?alt=media" alt="" width="399"><figcaption></figcaption></figure>

The workflow in this scenario monitors SLA deadlines and automatically takes action when issues are overdue.

* SLA Breach Detected (Trigger)
* High or Critical Severity (Condition)
* Reminder Email to Issue Owner (Action)
* Slack Alert to Issue-Tracking Channel (Action)
* Escalation for Business-Critical Apps (Action)

## Use case 3: Minor pull request change in critical application

This workflow ensures that even small pull requests in critical applications receive appropriate review.\
By combining PR metadata with business priority, the workflow routes changes for tracking and validation before they reach production.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-8137a736e19a6bfb48bcc1cd050f17928d929ca1%2FMinor%20pull%20request%20change%20in%20critical%20application.png?alt=media" alt="" width="218"><figcaption></figcaption></figure>

* Pull Request Created (Trigger)
* Minor PR Type (Condition)
* Application is Business-Critical (Condition)
* Public Repository (Condition)
* Open PR (Action)
