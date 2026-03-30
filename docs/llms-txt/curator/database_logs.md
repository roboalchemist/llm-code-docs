# Source: https://docs.curator.interworks.com/site_administration/logging/database_logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Backend Logs

> Database-stored logs accessible through the Curator backend including Usage Log, Event Log, Access Log, and Alert Log.

export const BackendNavPath = ({levelOne, levelTwo, levelThree, tab, section}) => {
  const levels = [levelOne, levelTwo, levelThree].filter(Boolean);
  const lastLevel = levels.length ? levels[levels.length - 1] : '';
  return <span>
      In the <a href="/setup/installation/linux_installation">backend of Curator</a> using the left-hand navigation,
      navigate to the
      {levelOne && <strong>{" " + levelOne}</strong>}
      {levelOne && levelTwo && " > "}
      {levelTwo && <strong>{levelTwo}</strong>}
      {levelTwo && levelThree && " > "}
      {levelThree && <strong>{levelThree}</strong>} page.
      {(tab || section) && <>
          {" "}On the {lastLevel} page
          {tab && <> click the <strong>{tab}</strong> tab</>}
          {tab && section && " and"}
          {section && <> expand the <strong>{section}</strong> section</>}.
        </>}
    </span>;
};

Backend logs are stored in the Curator database and can be viewed through the Curator backend interface. These
logs are designed for day-to-day monitoring and auditing by administrators who may not have direct server access.

## Usage Log

The Usage Log serves as an audit trail for your Curator instance, tracking who made what changes and when.
This includes configuration changes, content modifications, user management actions, and administrative
operations. The Usage Log is essential for compliance, security auditing, and troubleshooting issues
caused by configuration changes.

### Viewing the Usage Log

1. <BackendNavPath levelOne="Settings" levelTwo="Curator" levelThree="Usage Log" />
2. Use the filters to search for specific users, date ranges, or action types.

### Usage Log Retention

The Usage Log retention period can be configured in Portal Settings:

1. <BackendNavPath levelOne="Settings" levelTwo="Curator" levelThree="Portal Settings" tab="General" section="Security" />
2. Find the **Usage Log Retention** setting.
3. Select the desired retention period (1 Month, 3 Months, 6 Months, or 12 Months).
4. Click **Save**.

Older usage log entries will be automatically purged based on this setting.

## Event Log

The Event Log records system events including errors, warnings, informational messages, and debug output.
This is the primary log for troubleshooting issues with your Curator instance.

<Tip>
  The Event Log is stored in the database and mirrors the file-based System Log. In rare cases where
  event log entries appear to be missing, the [System Log](/site_administration/logging/file_based_logs#system-log)
  may contain additional information.
</Tip>

### Debug Modes

Curator provides several debug modes that can drastically increase the amount of logging in the Event Log.
These modes are useful for troubleshooting specific integrations or features:

* [Tableau Debug Mode](/creating_integrations/tableau_connection/tableau_connection_troubleshooting#how-to-enable-debug-mode) - Detailed logging for Tableau Server/Cloud communication
* [Power BI Debug Mode](/creating_integrations/power_bi_connection/troubleshooting_power_bi_access#enable-debug-mode) - Detailed logging for Power BI integration
* **Cron Debug Mode** - Detailed logging for scheduled tasks
* And others depending on your enabled features

Debug modes should typically only be turned on temporarily while troubleshooting, as they can
significantly increase the volume of log entries.

### Viewing the Event Log

1. <BackendNavPath levelOne="Settings" levelTwo="Logs" levelThree="Event Log" />
2. Click on any entry to view its details, including the full message and any associated context data.

### Download Debug Package

The Event Log page includes a **Download Debug Package** button that bundles various logs and system
information into a single downloadable archive. This package is useful when reporting issues to
InterWorks Support, as it includes:

* Recent event log entries
* System log files
* System configuration information

To download the debug package, click the **Download Debug Package** button in the toolbar on the Event Log page.

### Event Log Retention

The Event Log retention period can be configured in Portal Settings:

1. <BackendNavPath levelOne="Settings" levelTwo="Curator" levelThree="Portal Settings" tab="General" section="Security" />
2. Find the **Event Log Retention** setting.
3. Select the desired retention period:
   * **Never (Manual)** - Logs are not automatically purged; use the Event Log interface to manually clear entries
   * **1 Week** - Entries older than 7 days are automatically purged
   * **2 Weeks** - Entries older than 14 days are automatically purged
   * **1 Month** - Entries older than 30 days are automatically purged
   * **3 Months** - Entries older than 90 days are automatically purged
4. Click **Save**.

When automatic purging is enabled, old event log entries are removed daily at 2:00 AM (server timezone).

## Access Log

The Access Log tracks backend administrator logins and activity. This is useful for security auditing and
compliance purposes.

### Viewing the Access Log

1. <BackendNavPath levelOne="Settings" levelTwo="Logs" levelThree="Access Log" />
2. Review administrator access history including login times and IP addresses.

## Alert Log

The Alert Log aggregates recurring system alerts into a single, manageable view. Rather than creating
duplicate event log entries for the same recurring issue, the Alert Log consolidates these alerts and
tracks how many times they have occurred.

### Viewing the Alert Log

Alert Log entries are displayed in two locations:

1. **Status Page** - <BackendNavPath levelOne="Settings" levelTwo="Curator" levelThree="Status" /> Here you can see active alerts alongside other system health information.

2. **Alert Log List** - <BackendNavPath levelOne="Settings" levelTwo="Logs" levelThree="Alert Log" /> This provides a detailed view where you can:
   * View all active, resolved, and suppressed alerts
   * See occurrence counts and timestamps
   * Mark alerts as resolved or suppressed
   * Clear alerts in bulk

### Alert Statuses

* **Active** - The alert is current and requires attention
* **Resolved** - The underlying issue has been addressed
* **Suppressed** - The alert has been acknowledged but hidden from the active view
