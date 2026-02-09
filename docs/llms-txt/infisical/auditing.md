# Source: https://infisical.com/docs/documentation/platform/pam/product-reference/auditing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Auditing

> Learn how Infisical audits all actions across your PAM project.

## What's Audited

Infisical logs a wide range of actions to provide a complete audit trail for your PAM project. These actions include:

* Session Start and End
* Fetching session credentials
* Creating, updating, or deleting resources, accounts, folders, and sessions

<Info>
  Please note: Audit logs track metadata about sessions (e.g., start/end times), but not the specific commands executed *within* them. For detailed in-session activity, check out [Session Recording](/documentation/platform/pam/product-reference/session-recording).
</Info>

## Viewing Audit Logs

You can view, search, and filter all events from the **Audit Logs** page within your PAM project.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/pam/product-reference/auditing/audit-logs.png" alt="Audit Logs" />
