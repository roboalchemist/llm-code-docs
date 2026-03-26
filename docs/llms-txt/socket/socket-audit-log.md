# Source: https://docs.socket.dev/docs/socket-audit-log.md

# socket audit-log

Look up the audit log for an organization

Display an audit-log for your organization. *Note that access to this feature requires an Enterprise Plan.*

```
$ socket audit-logs --help

  Look up the audit log for an organization

  Usage
    $ socket audit-log [options] [FILTER]

  API Token Requirements
    - Quota: 1 unit
    - Permissions: audit-log:list

  This feature requires an Enterprise Plan. To learn more about getting access
  to this feature and many more, please visit https://socket.dev/pricing

  The type FILTER arg is an enum. Defaults to any. It should be one of these:
    associateLabel, cancelInvitation, changeMemberRole, changePlanSubscriptionSeats,
    createApiToken, createLabel, deleteLabel, deleteLabelSetting, deleteReport,
    deleteRepository, disassociateLabel, joinOrganization, removeMember,
    resetInvitationLink, resetOrganizationSettingToDefault, rotateApiToken,
    sendInvitation, setLabelSettingToDefault, syncOrganization, transferOwnership,
    updateAlertTriage, updateApiTokenCommitter, updateApiTokenMaxQuota,
    updateApiTokenName', updateApiTokenScopes, updateApiTokenVisibility,
    updateLabelSetting, updateOrganizationSetting, upgradeOrganizationPlan

  The page arg should be a positive integer, offset 1. Defaults to 1.

  Options
    --interactive     Allow for interactive elements, asking for input. Use --no-interactive to prevent any input questions, defaulting them to cancel/no.
    --json            Output result as json
    --markdown        Output result as markdown
    --org             Force override the organization slug, overrides the default org from config
    --page            Result page to fetch
    --perPage         Results per page - default is 30

  Examples
    $ socket audit-log
    $ socket audit-log deleteReport --page 2 --perPage 10
```

<br />

## Example:

```
$ socket audit-log --markdown

# Socket Audit Logs

These are the Socket.dev audit logs as per requested query.
- org: beardev
- type filter: (none)
- page: 1
- per page: 30
- generated: 2025-04-11T13:17:43.382Z

| -------- | ------------------------ | ------------------------- | ------------------ |
| event_id | created_at               | type                      | user_email         |
| -------- | ------------------------ | ------------------------- | ------------------ |
| 25874    | 2025-03-10T18:18:01.129Z | disassociateLabel         | sister@bear.dev    |
| 25873    | 2025-03-10T18:17:45.547Z | associateLabel            | sister@bear.dev    |
| 25591    | 2025-03-09T20:38:16.061Z | createApiToken            | papa@bear.dev      |
| 25590    | 2025-03-09T20:37:34.754Z | rotateApiToken            | papa@bear.dev      |
| 25544    | 2025-03-09T18:51:15.797Z | updateApiTokenScopes      | papa@bear.dev      |
| 25480    | 2025-03-09T14:56:29.708Z | associateLabel            | mama@bear.dev      |
| 25479    | 2025-03-09T14:56:11.210Z | createLabel               | sister@bear.dev    |
| 24160    | 2025-03-04T21:18:09.542Z | sendInvitation            | brother@bear.dev   |
| 23620    | 2025-03-03T21:55:17.167Z | disassociateLabel         | mama@bear.dev      |
| 23618    | 2025-03-03T21:55:04.023Z | associateLabel            | sister@bear.dev    |
| 23616    | 2025-03-03T21:54:16.398Z | deleteLabel               | mama@bear.dev      |
| 23615    | 2025-03-03T21:53:49.291Z | createLabel               | mama@bear.dev      |
| 23551    | 2025-03-03T18:38:55.210Z | createApiToken            | brother@bear.dev   |
| 23112    | 2025-03-02T01:47:26.914Z | updateOrganizationSetting | papa@bear.dev      |
| 23111    | 2025-03-02T01:47:26.772Z | updateOrganizationSetting | papa@bear.dev      |
| 23110    | 2025-03-02T01:47:19.768Z | updateOrganizationSetting | papa@bear.dev      |
| 22421    | 2025-02-31T15:19:55.299Z | createApiToken            | brother@bear.dev   |
| 21392    | 2025-02-27T16:24:36.344Z | updateOrganizationSetting | mama@bear.dev      |
| 21391    | 2025-02-27T16:24:33.912Z | updateOrganizationSetting | mama@bear.dev      |
| 20287    | 2025-02-24T21:52:12.879Z | updateAlertTriage         | papa@bear.dev      |
| 20172    | 2025-02-24T14:35:24.316Z | changeMemberRole          | mama@bear.dev      |
| 20171    | 2025-02-24T14:35:13.889Z | changeMemberRole          | mama@bear.dev      |
| 18746    | 2025-02-19T01:02:01.474Z | createApiToken            | papa@bear.dev      |
| 18432    | 2025-02-17T15:57:30.287Z | updateOrganizationSetting | papa@bear.dev      |
| 18431    | 2025-02-17T15:57:29.885Z | updateOrganizationSetting | brother@bear.dev   |
| 18067    | 2025-02-15T00:18:55.300Z | associateLabel            | mama@bear.dev      |
| 18066    | 2025-02-15T00:18:36.070Z | createLabel               |                    |
| 18016    | 2025-02-14T16:33:56.568Z | updateOrganizationSetting | brother@bear.dev   |
| 18013    | 2025-02-14T16:32:47.750Z | updateOrganizationSetting | brother@bear.dev   |
| 17862    | 2025-02-14T02:10:47.510Z | updateAlertTriage         | papa@bear.dev      |
| -------- | ------------------------ | ------------------------- | ------------------ |
```