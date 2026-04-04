# Reporting configuration settings

View the following statistics for your overall deployment and specific
teams, as well as access server logs, in the System Console by selecting
the **Product** [\|product-list\|](##SUBST##|product-list|) menu,
selecting **System Console**, and then selecting **Reporting**:

- [Site statistics](#site-statistics)
- [Team statistics](#team-statistics)
- [Server logs](#server-logs)
- [Statistics configuration
  settings](#statistics-configuration-settings)

------------------------------------------------------------------------

## Site statistics

+---------------------------------+------------------------------------+
| View statistics on a wide       | - System Config path: **Reporting  |
| variety of activities in        |   \> Site Statistics**             |
| Mattermost, including: users,   | - `config.json setting`: N/A       |
| seats, teams, channels, posts,  | - Environment variable: N/A        |
| calls, sessions, commands,      |                                    |
| webhooks, websocket and         |                                    |
| database connections, and       |                                    |
| collaborative playbooks.        |                                    |
+---------------------------------+------------------------------------+

:::: note
::: title
Note
:::

- Bots, deactivated users, and synthetic users in
  `Microsoft Teams integrations </end-user-guide/collaborate/collaborate-within-connected-microsoft-teams>`{.interpreted-text
  role="doc"} and
  `connected workspaces </administration-guide/onboard/connected-workspaces>`{.interpreted-text
  role="doc"} users aren\'t counted towards the total number of
  activated users.
- For billing purposes, activated guest accounts do consume a licensed
  seat, which is returned when the guest account is deactivated. This
  means that guest accounts count as a paid user in your Mattermost
  `workspace </end-user-guide/end-user-guide-index>`{.interpreted-text
  role="doc"}
::::

------------------------------------------------------------------------

## Team statistics

+----------------------------------+-----------------------------------+
| View statistics per team on      | - System Config path: **Reporting |
| number of activated users,       |   \> Team Statistics**            |
| number of public and private     | - `config.json` setting: N/A      |
| channels, total post count, and  | - Environment variable: N/A       |
| count of paid users (self-hosted |                                   |
| only).                           |                                   |
+----------------------------------+-----------------------------------+

:::: note
::: title
Note
:::

Bots, deactivated users, and synthetic users in
`Microsoft Teams integrations </end-user-guide/collaborate/collaborate-within-connected-microsoft-teams>`{.interpreted-text
role="doc"} and
`connected workspaces </administration-guide/onboard/connected-workspaces>`{.interpreted-text
role="doc"} users aren\'t counted towards the total number of active
users.
::::

------------------------------------------------------------------------

## Server logs

+-----------------------------------+-----------------------------------+
| View logging of server-side       | - System Config path: **Reporting |
| events.                           |   \> Server Logs**                |
|                                   | - `config.json` setting: N/A      |
| Reload data, download the         | - Environment variable: N/A       |
| `mattermost.log` file locally,    |                                   |
| and view full log event details   |                                   |
| for any log entry.                |                                   |
+-----------------------------------+-----------------------------------+

:::: note
::: title
Note
:::

- This setting is applicable to self-hosted deployments only.
- From Mattermost v10.9, you can toggle between JSON and plain text
  server logs in the System Console when console log output is
  configured as
  `JSON <administration-guide/configure/environment-configuration-settings:output console logs as json>`{.interpreted-text
  role="ref"} by specifying the log format as **JSON** or **Plain
  text**. This option is located in the top right corner of the page
  **Server logs** page.
::::

------------------------------------------------------------------------

## Statistics configuration settings

The following self-hosted deployment configuration setting controls
statistics collection behavior. This setting is not available in the
System Console and can only be set in the `config.json` file.

### Maximum users for statistics

This setting is used to maximize performance for large Enterprise
deployments and isn\'t available in the System Console and can only be
set in `config.json`.

+------------------------------+-----------------------------------------------------+
| Set the maximum number of    | - System Config path: N/A                           |
| users on the server before   | - `config.json` setting:                            |
| statistics for total         |   `"AnalyticsSettings.MaxUsersForStatistics": 2500` |
| messages, total hashtag      | - Environment variable: N/A                         |
| messages, total file         |                                                     |
| messages, messages per day,  |                                                     |
| and activated users with     |                                                     |
| messages per day are         |                                                     |
| disabled.                    |                                                     |
|                              |                                                     |
| Numerical input. Default is  |                                                     |
| **2500** users.              |                                                     |
+------------------------------+-----------------------------------------------------+
