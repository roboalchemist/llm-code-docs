# Source: https://docs.airbyte.com/integrations/enterprise-connectors/source-service-now.md

![]()

# Source ServiceNow

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Enterprise](/integrations/connector-support-levels.md)

* Connector Version

  0.1.1

* Enterprise Connector

  **This premium connector is available to Enterprise customers at an additional cost**.

  <!-- -->

  [Talk to Sales](https://airbyte.com/company/talk-to-sales)

  <!-- -->

  [ ](https://airbyte.com/company/talk-to-sales).

* Definition ID

  `23867633-144a-4d7f-845a-a8bd9b9b9e5d`

Airbyte’s incubating ServiceNow enterprise source connector currently offers Full Refresh syncs for streams that are part of Software Asset Management and Configuration Management Database applications.

## Features[​](#features "Direct link to Features")

| Feature           | Supported?(Yes/No) | Notes |
| ----------------- | ------------------ | ----- |
| Full Refresh Sync | Yes                |       |
| Incremental Sync  | No                 |       |

## Setup Guide[​](#setup-guide "Direct link to Setup Guide")

1. Enter your ServiceNow environment as the Base URL.
2. Enter the username and password for a ServiceNow user account that has access to all tables that you want to include in the connection.

![ServiceNow Connector setup with credentials](/assets/images/service-now-setup-78f5686734f40604519a969ca5af8588.png)

## Supported streams[​](#supported-streams "Direct link to Supported streams")

### Configuration Management Database (CMDB)[​](#configuration-management-database-cmdb "Direct link to Configuration Management Database (CMDB)")

* cmdb\_ci\_wap\_network
* cmdb\_ci\_ip\_router
* cmdb\_ci\_ip\_switch
* cmdb\_ci\_lb\_bigip
* cmdb\_ci\_ip\_firewall
* cmdb\_ci\_printer
* cmdb\_ci\_scanner
* cmdb\_ci\_linux\_server
* cmdb\_ci\_comm
* cmdb\_ci\_win\_server
* cmdb\_ci\_ucs\_chassis
* cmdb\_ci\_storage\_switch
* cmdb\_ci\_pc\_hardware
* cmdb\_ci\_esx\_server
* cmdb\_ci\_aix\_server
* cmdb\_ci\_solaris\_server
* cmdb\_ci\_chassis\_server
* cmdb\_ci\_server
* cmdb\_ci\_net\_app\_server

### Software Asset Management (SAM)[​](#software-asset-management-sam "Direct link to Software Asset Management (SAM)")

* cmdb\_model\_category
* sam\_sw\_product\_lifecycle
* alm\_license

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

The connector is still incubating; this section exists to satisfy Airbyte's QA checks.

* 0.1.0
