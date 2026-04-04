# Source: https://wafris.org/docs/concepts/operational_modes/

Title: Operational Modes (Managed or Standalone)

URL Source: https://wafris.org/docs/concepts/operational_modes/

Markdown Content:
[](https://wafris.org/docs/concepts/operational_modes/#context) Context
-----------------------------------------------------------------------

Wafris v2 and above firewalls can be deployed in one of two operational modes: `Managed` or `Standalone`. Which mode you choose direclty impacts many aspects of your deployment, including how you deploy, manage, and monitor your WAF.

[](https://wafris.org/docs/concepts/operational_modes/#client-controlled) Client Controlled
-------------------------------------------------------------------------------------------

Each Wafris client instance (e.g. a web server, framework or platform with an deployed Wafis module) controls what operational mode is being used. In most cases, the

[](https://wafris.org/docs/concepts/operational_modes/#features-mode-table) Features Mode Table
-----------------------------------------------------------------------------------------------

| Feature | Managed Mode | Standalone Mode |
| --- | --- | --- |
| Firewall Configuration | Distributed from Wafris Hub | Locally configured |
| Request Reporting | Real-time reports available | No reporting |
| Rule Setting | Sync’d from Wafris Hub | Locally set |
| Monitoring and Alerts | Real-time monitoring and alerts | No monitoring or alerts |
| Data Subscriptions | Geo IP and IP reputation data | No data subscriptions |

[](https://wafris.org/docs/concepts/operational_modes/#standalone-mode) Standalone Mode
---------------------------------------------------------------------------------------

Standalone mode separates the on server firewall blocking from the request reporting, rule setting, monitoring/alerting, and data subscription features that are available in Managed mode.

Conceptually, you’re setting rules by modifying the entries in a SQLite DB which is then deployed alongside your application. The core SQLite DB even with thousands of rules set is smaller that most images on your site making it easy and practical to keep in version control.

To enable standalone mode, refer to the directions in your specific Wafris client documentation.

[](https://wafris.org/docs/concepts/operational_modes/#managed-mode) Managed Mode
---------------------------------------------------------------------------------

Managed Wafris WAFs communicate with [Wafris Hub](https://hub.wafris.org/) to enable:

1. The distribution of firewall configuration rules from Hub to WAF instances.
2. The collection of telemetry request data from the WAF instances.

This is the default operational mode for Wafris WAFs.

#### [](https://wafris.org/docs/concepts/operational_modes/#request-reporting) Request Reporting

Request data sent to Hub from Wafris WAFs is directly tranformed into reports covering the most recent time period.

#### [](https://wafris.org/docs/concepts/operational_modes/#setting-rules) Setting Rules

Rules set from within Wafris Hub are sync’d to Wafris WAFs in seconds.

#### [](https://wafris.org/docs/concepts/operational_modes/#monitoring-and-alerts) Monitoring and Alerts

Usage alerts and real-time monitoring is available for Managed WAFs.

#### [](https://wafris.org/docs/concepts/operational_modes/#data-subscriptions) Data Subscriptions

Geo IP data and IP reputation data are constantly being updated and distributed to Managed WAFs. Standalone WAF (by definition) aren’t updated with this data and can’t take advantage of either feature.

* * *
