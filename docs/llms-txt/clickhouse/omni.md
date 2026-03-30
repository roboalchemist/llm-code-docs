# Source: https://clickhouse.ferndocs.com/integrations/omni.md

---
sidebar_label: Omni
slug: /integrations/omni
keywords:
  - clickhouse
  - Omni
  - connect
  - integrate
  - ui
description: >-
  Omni is an enterprise platform for BI, data applications, and embedded
  analytics that helps you explore and share insights in real time.
title: Omni
doc_type: guide
---

import {PartnerBadge} from '../../../../../../components/Badges/PartnerBadge'

<PartnerBadge/>

Omni can connect to ClickHouse Cloud or on-premise deployment via the official ClickHouse data source.

## 1. Gather your connection details [#1-gather-your-connection-details]

To connect to ClickHouse with HTTP(S) you need this information:

| Parameter(s)            | Description                                                                                                   |
|-------------------------|---------------------------------------------------------------------------------------------------------------|
|`HOST` and `PORT`        | Typically, the port is 8443 when using TLS or 8123 when not using TLS.                                        |
|`DATABASE NAME`          | Out of the box, there is a database named `default`, use the name of the database that you want to connect to.|
|`USERNAME` and `PASSWORD`| Out of the box, the username is `default`. Use the username appropriate for your use case.                    |

The details for your ClickHouse Cloud service are available in the ClickHouse Cloud console.
Select a service and click **Connect**:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/9de2a784fe6ef2c5c51be720b96cb4bb7ebd0838901449759f587e0df6d9034a/images/_snippets/cloud-connect-button.png" alt="ClickHouse Cloud service connect button" />

Choose **HTTPS**. Connection details are displayed in an example `curl` command.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/710d528cac4deb00e877550b033fe8d67e19e1a8f825c75889eb0573ab25f7b0/images/_snippets/connection-details-https.png" alt="ClickHouse Cloud HTTPS connection details" />

If you are using self-managed ClickHouse, the connection details are set by your ClickHouse administrator.


## 2. Create a ClickHouse data source [#2-create-a-clickhouse-data-source]

Navigate to Admin -> Connections and click the "Add Connection" button in the top right corner.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/fa1bd52c25d0625550ec74cecd5808fb30c0e405af5ab9e4dcd387861e827303/images/integrations/data-visualization/omni_01.png" alt="Omni admin interface showing the Add Connection button in the Connections section" />
<br/>

Select `ClickHouse`. Enter your credentials in the form.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/76806ad398a3a6547e568133b64ecf7236d776c3a957d2dc335beaca3ca9790c/images/integrations/data-visualization/omni_02.png" alt="Omni connection configuration interface for ClickHouse showing credential form fields" />
<br/>

Now you should can query and visualize data from ClickHouse in Omni.
