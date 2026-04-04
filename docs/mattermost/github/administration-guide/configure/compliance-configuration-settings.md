# Compliance configuration settings

Review and manage the following compliance configuration options in the
System Console by selecting the **Product**
[\|product-list\|](##SUBST##|product-list|) menu, selecting **System
Console**, and then selecting **Compliance**:

- [Data Retention Policies](#data-retention-policies)
- [Compliance Export](#administration-guide/comply/compliance-export)
- [Compliance Monitoring](#compliance-monitoring)
- [Custom Terms of Service](#custom-terms-of-service)

:::: tip
::: title
Tip
:::

System admins managing a self-hosted Mattermost deployment can edit the
`config.json` file as described in the following tables. Each
configuration value below includes a JSON path to access the value
programmatically in the `config.json` file using a JSON-aware tool. For
example, the `MessageRetentionHours` value is under
`DataRetentionSettings`.

- If using a tool such as [jq](https://stedolan.github.io/jq/), you\'d
  enter:
  `cat config/config.json | jq '.DataRetentionSettings.MessageRetentionHours'`
- When working with the `config.json` file manually, look for an object
  such as `DataRetentionSettings`, then within that object, find the key
  `MessageRetentionHours`.
::::

------------------------------------------------------------------------

## Data retention policies

Changes to properties in this section require a server restart before
taking effect.

:::: warning
::: title
Warning
:::

- Once a message or a file is deleted, the action is irreversible.
  Please be careful when setting up a custom data retention policy.
- From Mattermost v9.5, data retention removes Elasticsearch indexes
  based on the day of the retention cut-off time.
::::

Access the following configuration settings in the System Console by
going to **Compliance \> Data Retention Policies**.

### Global retention policy for messages

Set how long Mattermost keeps messages across all teams and channels.
This value is not used for any teams and channels that have a custom
retention policy applied . Requires the
`global retention policy for messages <administration-guide/configure/compliance-configuration-settings:global retention policy for messages>`{.interpreted-text
role="ref"} configuration setting to be set to `true`.

By default, messages are kept forever. If **Hours**, **Days**, or
**Years** is chosen, set how many hours, days, or years messages are
kept in Mattermost. Messages older than the duration you set will be
deleted nightly. The minimum message retention time is one hour.

The global retention time for messages can be superseded on a team or
channel level by creating custom policies with unique post retention
times See the [Custom retention policy](#custom-retention-policy)
section below for details.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is `"MessageRetentionHours": 1`
  with numerical input.

  -----------------------------------------------------------------------

:::: note
::: title
Note
:::

From Mattermost v9.5, `MessageRetentionDays` has been deprecated in
favor of `MessageRetentionHours`. See
`deprecated configuration settings </administration-guide/configure/deprecated-configuration-settings>`{.interpreted-text
role="doc"} for details.
::::

### Global retention policy for files

Set how long Mattermost keeps files across all teams and channels.
Custom policies on team and channel level don\'t apply to file
attachments. The global retention time for files will be used even if a
custom policy for messages is in place. Requires the
`global retention policy for files <administration-guide/configure/compliance-configuration-settings:global retention policy for files>`{.interpreted-text
role="ref"} configuration setting to be set to `true`.

By default, files are kept forever. If **Hours**, **Days**, or **Years**
is chosen, set how many hours, days, or years files are kept in
Mattermost. Files older than the duration you set will be deleted
nightly. The minimum file retention time is one hour.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is `"FileRetentionHours": 1` with
  numerical input.

  -----------------------------------------------------------------------

:::: note
::: title
Note
:::

From Mattermost v9.5, `FileRetentionDays` has been deprecated in favor
of `FileRetentionHours`. See
`deprecated configuration settings </administration-guide/configure/deprecated-configuration-settings>`{.interpreted-text
role="doc"} for details.
::::

### Preserve pinned posts

From Mattermost v10.10, controls whether pinned posts are preserved when
data retention policies delete messages. When enabled, pinned posts
won\'t be deleted by data retention policies, even if they exceed the
configured retention period.

**True**: Pinned posts are preserved and won\'t be deleted by data
retention policies.

**False**: **(Default)** Pinned posts are deleted according to the
configured data retention policy.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is
  `"DataRetentionSettings.PreservePinnedPosts": false` with options
  `true` and `false`.

  -----------------------------------------------------------------------

:::: note
::: title
Note
:::

- This global configuration setting must be enabled with mmctl using the
  `mmctl config set <administration-guide/manage/mmctl-command-line-tool:mmctl config set>`{.interpreted-text
  role="ref"} command.
- This configuration setting applies to team and channel policies as
  well as data retention, and can\'t be overridden in those more
  granular team or channel policies.
- Files attached to the pinned message aren\'t preserved.
- Only the pinned post is preserved. If it\'s attached to a thread or if
  it\'s the root post of a thread, the other threaded messages aren\'t
  preserved.
::::

### Custom retention policy

Set how long Mattermost keeps messages across specific teams and
channels by specifying a name for the custom retention policy, setting a
duration value in days or years, and specifying the teams and channels
that will follow this policy. The attachment retention time cannot be
set on custom policy levels and the global retention time for
attachments is always applied.

### Data deletion time

Set the start time of the daily scheduled data retention job. Choose a
time when fewer people are using your system. Must be a 24-hour time
stamp in the form `HH:MM`.

This setting is based on the local time of the server.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is
  `"DeletionJobStartTime": "02:00"` with 24-hour timestamp input in the
  form `"HH:MM"`.

  -----------------------------------------------------------------------

### Run deletion job now

Start a Data Retention deletion job immediately. You can monitor the
status of the job in the data deletion job table within the Policy Log
section.

------------------------------------------------------------------------

## Compliance export

Access the following configuration settings in the System Console by
going to **Compliance \> Compliance Export**.

### Enable compliance export

**True**: Mattermost will generate a compliance export file that
contains all messages that were posted in the last 24 hours. The export
task is scheduled to run once per day. See the
`documentation to learn more </administration-guide/comply/compliance-export>`{.interpreted-text
role="doc"}.

**False**: Mattermost doesn\'t generate a compliance export file.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is `"EnableExport": false` with
  options `true` and `false`.

  -----------------------------------------------------------------------

### Compliance export time

Set the start time of the daily scheduled compliance export job. Choose
a time when fewer people are using your system. Must be a 24-hour time
stamp in the form `HH:MM`.

This setting is based on the local time of the server.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is `"DailyRunTime": 01:00` with
  24-hour timestamp input in the form `"HH:MM"`.

  -----------------------------------------------------------------------

### Export file format

File format of the compliance export. Corresponds to the system that you
want to import the data into.

Currently supported formats are CSV, Actiance XML, and Global Relay EML.

If Global Relay is chosen, the following options will be presented:

### Global Relay customer account

Type of Global Relay customer account your organization has. Can be one
of: `A9/Type 9`, `A10/Type 10`, or `Custom`.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is `"CustomerType": "A9"` with
  options `"A9`, `"A10"`, and `CUSTOM`.

  -----------------------------------------------------------------------

### Global Relay SMTP username

The username for authenticating to the Global Relay SMTP server.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is `"SmtpUsername": ""` with
  string input.

  -----------------------------------------------------------------------

### Global Relay SMTP password

The password associated with the Global Relay SMTP username.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is `"SmtpPassword": ""` with
  string input.

  -----------------------------------------------------------------------

### Global Relay email address

The email address your Global Relay server monitors for incoming
compliance exports.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is `"EmailAddress": ""` with
  string input.

  -----------------------------------------------------------------------

### SMTP server name

The SMTP server name URL that will receive your Global Relay EML file
when a [custom customer account type](#global-relay-customer-account) is
configured.

  -------------------------------------------------------------------------
  This feature\'s `config.json` setting is
  `".MessageExportSettings.GlobalRelaySettings.CustomSMTPServerName": ""`
  with string input.

  -------------------------------------------------------------------------

### SMTP server port

The SMTP server port that will receive your Global Relay EML file when a
[custom customer account type](#global-relay-customer-account) is
configured. Default is `"25"`.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is
  `".MessageExportSettings.GlobalRelaySettings.CustomSMTPPort": "25"`
  with string input.

  -----------------------------------------------------------------------

### Message export batch size

This setting isn\'t available in the System Console and can only be set
in `config.json`.

Determines how many new posts are batched together to a compliance
export file.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is `"BatchSize": 10000` with
  numerical input.

  -----------------------------------------------------------------------

### Run compliance export job now

This button initiates a compliance export job immediately. You can
monitor the status of the job in the compliance export job table.

------------------------------------------------------------------------

## Compliance monitoring

Settings used to enable and configure Mattermost compliance reports.

Access the following configuration settings in the System Console by
going to **Compliance \> Compliance Monitoring**.

### Enable compliance reporting

**True**: Compliance reporting is enabled in Mattermost.

**False**: Compliance reporting is disabled.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is `"Enable": false` with options
  `true` and `false`.

  -----------------------------------------------------------------------

### Compliance report directory

Sets the directory where compliance reports are written.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is `"Directory": "./data/"` with
  string input.

  -----------------------------------------------------------------------

### Enable daily report

**True**: Mattermost generates a daily compliance report.

**False**: Daily reports are not generated.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is `"EnableDaily": false` with
  options `true` and `false`.

  -----------------------------------------------------------------------

### Batch size

Set the size of the batches in which posts will be read from the
database to generate the compliance report. This setting is currently
not available in the System Console and can only be set in
`config.json`.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is `"BatchSize": 30000` with
  default value `30000`.

  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Custom terms of service

Access the following configuration settings in the System Console by
going to **Compliance \> Custom Terms of Service**.

### Enable custom terms of service

:::: note
::: title
Note
:::

This configuration setting can only be modified using the System Console
user interface.
::::

**True**: New users must accept the Terms of Service before accessing
any Mattermost teams on desktop, web, or mobile. Existing users must
accept them after login or a page refresh. To update the Terms of
Service link displayed in account creation and login pages, go to
**System Console \> Legal and Support \> Terms of Service Link**.

**False**: During account creation or login, users can review Terms of
Service by accessing the link configured via **System Console \> Legal
and Support \> Terms of Service link**.

### Custom terms of service text

Text that will appear in your custom Terms of Service. Supports
Markdown-formatted text.

### Re-acceptance period

The number of days before Terms of Service acceptance expires, and the
terms must be re-accepted.

Defaults to 365 days. 0 indicates the terms do not expire.
