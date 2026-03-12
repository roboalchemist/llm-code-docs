# Source: https://clickhouse.ferndocs.com/cloud/guides/sql-console/manage-sql-console-role-assignments.md

---
slug: /cloud/guides/sql-console/manage-sql-console-role-assignments
sidebar_label: Manage SQL console role assignments
title: Configuring SQL console role assignments
description: Guide showing how to manage SQL console role assignments
doc_type: guide
keywords:

- sql console
- role assignments
- access management
- permissions
- security

---

> This guide shows you how to configure SQL console role assignments, which
determine console-wide access permissions and the features that a user can
access within Cloud console.

<Steps headerLevel="h3">

### Access service settings [#access-service-settings]

From the services page, click the menu in the top right corner of the service for which you want to adjust SQL console access settings.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/7868f80c9e486c178a8ebaa776dbcaf010d8370ae4eeec74ebd98e3f45fbdf07/images/cloud/guides/sql_console/service_level_access/1_service_settings.png"/>

Select `settings` from the popup menu.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/dc31c85718981b9706d9adf2c7685aec066e0bd7f3e74f003cd75f7d77e6e3ef/images/cloud/guides/sql_console/service_level_access/2_service_settings.png"/>

### Adjust SQL console access [#adjust-sql-console-access]

Under the "Security" section, find the "SQL console access" area:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/77e51b2023e762a376a58c775396cfab9809719c583db53740d740505e9370ff/images/cloud/guides/sql_console/service_level_access/3_service_settings.png"/>

### Update the settings for Service Admin [#update-settings-for-service-admin]

Select the drop-down menu for Service Admin to change the access control settings for Service Admin roles:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/bef164a3263e3272017f3249279e85e3e3cde72f6e149190362878dc8294f493/images/cloud/guides/sql_console/service_level_access/4_service_settings.png"/>

You can choose from the following roles:

| Role          |
|---------------|
| `No access`   |
| `Read only`   |
| `Full access` |

### Update the settings for Service Read Only [#update-settings-for-service-read-only]

Select the drop-down menu for Service Read Only to change the access control settings for Service Read Only roles:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/5a40ad5c7f807691f2feeb0db6072948255e75eb921cebb1d22e56715701753d/images/cloud/guides/sql_console/service_level_access/5_service_settings.png"/>

You can choose from the following roles:

| Role          |
|---------------|
| `No access`   |
| `Read only`   |
| `Full access` |

### Review users with access [#review-users-with-access]

An overview of users for the service can be viewed by selecting the user count:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/48e1c013c0f84abf70c9ea8a43dbf7dff082c93c09434a6d1a5fe501b4d71449/images/cloud/guides/sql_console/service_level_access/6_service_settings.png"/>

A tab will open to the right of the page showing the total number of users and their roles:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/0f1ba324ebb907967dac6a5249bb63eb155c06ed715ecc0820df037fea1ca6d2/images/cloud/guides/sql_console/service_level_access/7_service_settings.png"/>

</Steps>
