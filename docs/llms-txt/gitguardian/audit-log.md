# Source: https://docs.gitguardian.com/platform/enterprise-administration/audit-log.md

# Audit log

> Review the centralized stream of user activity on your GitGuardian workspace to investigate suspicious behavior and security issues.

The audit log is **the centralized stream of user activity which occurs on your workspace**.
It allows the workspace Managers to investigate for potential suspicious behavior and security issues by reviewing the actions performed by users of their workspace.

The following information is included in each event recorded:

- **Actor**: the GitGuardian user who performed the event.
- **Event**: the event recorded.
- **Date**: the date when the event happened.
- **IP address**: the IP address of the actor who performed the event.

### Accessing the audit log

1. Navigate to Settings > Workspace > [Audit log](https://dashboard.gitguardian.com/settings/workspace/audit-logs).
2. Search for logs.

![Audit log table](/img/platform/enterprise-administration/audit-log-table.png)

:::info
Only the Owner and Managers have access to the workspace's audit log.
:::

### Email Alerts for Audit Log Failures

For self-hosted, owners and managers can receive email alerts for audit log failures. These alerts will provide details about the issue. To enable this feature, run the following command:

```bash
kubectl exec --namespace <namespace> deployments/webapp-internal-api -c app -- python manage.py set_preferences --general__is_audit_log_failure_triggers_mail=True
```

If needed, specify the Kubernetes namespace with `--namespace` (default namespace is used if not specified).
