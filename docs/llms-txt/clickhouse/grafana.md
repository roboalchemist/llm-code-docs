# Source: https://clickhouse.ferndocs.com/integrations/grafana.md

---
sidebar_label: Quick Start
sidebar_position: 1
slug: /integrations/grafana
description: Introduction to using ClickHouse with Grafana
title: ClickHouse data source plugin for Grafana
show_related_blogs: true
doc_type: guide
integration:
  - support_level: partner
  - category: data_visualization
  - website: 'https://grafana.com/grafana/plugins/grafana-clickhouse-datasource/'
keywords:
  - Grafana
  - data visualization
  - dashboard
  - plugin
  - data source
---

import {ClickHouseSupportedBadge} from '../../../../../../../components/Badges/ClickHouseSupported'

<ClickHouseSupportedBadge/>

With Grafana you can explore and share all of your data through dashboards.
Grafana requires a plugin to connect to ClickHouse, which is easily installed within their UI.

<div class='vimeo-container'>
  <iframe src="//www.youtube.com/embed/bRce9xWiqQM"
    width="640"
    height="360"
    frameborder="0"
    allow="autoplay;
    fullscreen;
    picture-in-picture"
    allowfullscreen>
  </iframe>
</div>

## 1. Gather your connection details [#1-gather-your-connection-details]

To connect to ClickHouse with native TCP you need this information:

| Parameter(s)              | Description                                                                                                   |
|---------------------------|---------------------------------------------------------------------------------------------------------------|
| `HOST` and `PORT`         | Typically, the port is 9440 when using TLS, or 9000 when not using TLS.                                       |
| `DATABASE NAME`           | Out of the box there is a database named `default`, use the name of the database that you want to connect to. |
| `USERNAME` and `PASSWORD` | Out of the box the username is `default`. Use the username appropriate for your use case.                     |

The details for your ClickHouse Cloud service are available in the ClickHouse Cloud console.
Select the service that you will connect to and click **Connect**:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/9de2a784fe6ef2c5c51be720b96cb4bb7ebd0838901449759f587e0df6d9034a/images/_snippets/cloud-connect-button.png" alt="ClickHouse Cloud service connect button"/>

Choose **Native**, and the details are available in an example `clickhouse-client` command.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/1ee67fa3dad36e2eae368f91c239fb2fcb17f9486a89e29b7347c0267fa1ceb7/images/_snippets/connection-details-native.png" alt="ClickHouse Cloud Native TCP connection details"/>

If you are using self-managed ClickHouse, the connection details are set by your ClickHouse administrator.


## 2. Making a read-only user [#2-making-a-read-only-user]

When connecting ClickHouse to a data visualization tool like Grafana, it is recommended to make a read-only user to protect your data from unwanted modifications.

Grafana does not validate that queries are safe. Queries can contain any SQL statement, including `DELETE` and `INSERT`.

To configure a read-only user, follow these steps:
1. Create a `readonly` user profile following the [Creating Users and Roles in ClickHouse](/operations/access-rights) guide.
2. Ensure the `readonly` user has enough permission to modify the `max_execution_time` setting required by the underlying [clickhouse-go client](https://github.com/ClickHouse/clickhouse-go).
3. If you're using a public ClickHouse instance, it is not recommended to set `readonly=2` in the `readonly` profile. Instead, leave `readonly=1` and set the constraint type of `max_execution_time` to [changeable_in_readonly](/operations/settings/constraints-on-settings) to allow modification of this setting.

## 3.  Install the ClickHouse plugin for Grafana [#3--install-the-clickhouse-plugin-for-grafana]

Before Grafana can connect to ClickHouse, you need to install the appropriate Grafana plugin. Assuming you are logged in to Grafana, follow these steps:

1. From the **Connections** page in the sidebar, select the **Add new connection** tab.

2. Search for **ClickHouse** and click on the signed plugin by Grafana Labs:

    <Image size="md" img={search} alt="Select the ClickHouse plugin on the connections page" border />

3. On the next screen, click the **Install** button:

    <Image size="md" img={install} alt="Install the ClickHouse plugin" border />

## 4. Define a ClickHouse data source [#4-define-a-clickhouse-data-source]

1. Once the installation is complete, click the **Add new data source** button. (You can also add a data source from the **Data sources** tab on the **Connections** page.)

    <Image size="md" img={add_new_ds} alt="Create a ClickHouse data source" border />

2. Either scroll down and find the **ClickHouse** data source type, or you can search for it in the search bar of the **Add data source** page. Select the **ClickHouse** data source and the following page will appear:

  <Image size="md" img={quick_config} alt="Connection configuration page" border />

3. Enter your server settings and credentials. The key settings are:

- **Server host address:** the hostname of your ClickHouse service.
- **Server port:** the port for your ClickHouse service. Will be different depending on server configuration and protocol.
- **Protocol** the protocol used to connect to your ClickHouse service.
- **Secure connection** enable if your server requires a secure connection.
- **Username** and **Password**: enter your ClickHouse user credentials. If you have not configured any users, try `default` for the username. It is recommended to [configure a read-only user](#2-making-a-read-only-user).

For more settings, check the [plugin configuration](/integrations/grafana/config) documentation.

4. Click the **Save & test** button to verify that Grafana can connect to your ClickHouse service. If successful, you will see a **Data source is working** message:

    <Image size="md" img={valid_ds} alt="Select Save & test" border />

## 5. Next steps [#5-next-steps]

Your data source is now ready to use! Learn more about how to build queries with the [query builder](/integrations/grafana/query-builder).

For more details on configuration, check the [plugin configuration](/integrations/grafana/config) documentation.

If you're looking for more information that is not included in these docs, check the [plugin repository on GitHub](https://github.com/grafana/clickhouse-datasource).

## Upgrading plugin versions [#upgrading-plugin-versions]

Starting with v4, configurations and queries are able to be upgraded as new versions are released.

Configurations and queries from v3 are migrated to v4 as they are opened. While the old configurations and dashboards will load in v4, the migration is not persisted until they are saved again in the new version. If you notice any issues when opening an old configuration/query, discard your changes and [report the issue on GitHub](https://github.com/grafana/clickhouse-datasource/issues).

The plugin cannot downgrade to previous versions if the configuration/query was created with a newer version.
