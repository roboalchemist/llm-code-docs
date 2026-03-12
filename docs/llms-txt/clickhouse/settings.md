# Source: https://clickhouse.ferndocs.com/reference/operations/system-tables/settings.md

# Source: https://clickhouse.ferndocs.com/reference/operations/settings/settings.md

# Source: https://clickhouse.ferndocs.com/reference/operations/server-configuration-parameters/settings.md

# Source: https://clickhouse.ferndocs.com/cloud/manage/settings.md

---
sidebar_label: Configuring settings
slug: /manage/settings
title: Configuring settings
description: >-
  How to configure settings for your ClickHouse Cloud service for a specific
  user or role
keywords:

- ClickHouse Cloud
- settings configuration
- cloud settings
- user settings
- role settings
doc_type: guide

---

# Configuring settings

To specify settings for your ClickHouse Cloud service for a specific [user](/operations/access-rights#user-account-management) or [role](/operations/access-rights#role-management), you must use [SQL-driven Settings Profiles](/operations/access-rights#settings-profiles-management). Applying Settings Profiles ensures that the settings you configure persist, even when your services stop, idle, and upgrade. To learn more about Settings Profiles, please see [this page](/operations/settings/settings-profiles.md).

Please note that XML-based Settings Profiles and [configuration files](/operations/configuration-files.md) are currently not supported for ClickHouse Cloud.

To learn more about the settings you can specify for your ClickHouse Cloud service, please see all possible settings by category in [our docs](/operations/settings).

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/9a1f64ef440cac3e95b03fc403ce8b41ec130fdaf53d9f6fdaeb378ca726e079/images/cloud/manage/cloud-settings-sidebar.png" alt="Cloud settings sidebar"/>
