# Source: https://docs.axonius.com/docs/varonis-csv.md

# Varonis CSV

Varonis helps prioritize risks around sensitive repositories, monitor the use of personal accounts, and identify costly misconfigurations.

The adapter parameters are as same as the [CSV Legacy Remote File Configuration](/docs/legacy-remote-file-configuration-csv), except for the following parameters:

* **File contains users information**
* **File contains installed software information**
* **Custom prefix for dynamic fields**
* **Multi-value fields delimiter**

These fields aren't part of the Varonis CSV File adapter configuration, as the adapter provides devices data only, without any information on the installed software.

When uploading a CSV file exported from Varonis, you need to ensure that this file contains the `file_server` field (column), as the adapter expects to get a CSV file where each row is an alert relevant to a specific file server. Any other field (listed below) is optional.

#### Optional Fields

* file\_server
* Alert ID
* Alert Severity
* Threat Model Name
* User Name
* Device Name
* Asset
* Status
* Alert Category
* Close Reason
* State
* Country
* Abnormal Location
* Aggregated External IP Threat Types
* Privileged Account Type
* Department
* Manager
* SAM Account Name
* Blacklisted Location
* No. of Alerted Events
* Contains Malicious External IPs
* User Has Follow-Up Indicators
* Sensitive Data Exposed
* Flagged data exposed
* Alert Time