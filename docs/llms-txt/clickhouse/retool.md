# Source: https://clickhouse.ferndocs.com/integrations/retool.md

---
sidebar_label: Retool
slug: /integrations/retool
keywords:
  - clickhouse
  - retool
  - connect
  - integrate
  - ui
  - admin
  - panel
  - dashboard
  - nocode
  - no-code
description: >-
  Quickly build web and mobile apps with rich user interfaces, automate complex
  tasks, and integrate AI—all powered by your data.
title: Connecting Retool to ClickHouse
doc_type: guide
integration:
  - support_level: partner
  - category: data_integration
---

import {PartnerBadge} from '../../../../../components/Badges/PartnerBadge'

<PartnerBadge/>

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


## 2. Create a ClickHouse resource [#2-create-a-clickhouse-resource]

Login to your Retool account and navigate to the _Resources_ tab. Choose "Create New" -> "Resource":

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/f96507db243dc18cd8a44aa067d1781e3397046e531db959ac48f9262b22dfec/images/integrations/tools/data-integration/retool/retool_01.png" alt="Creating a new resource"/>
<br/>

Select "JDBC" from the list of available connectors:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/1f9c4ace07e4344a55f65710ff590c277810402f4754722bb76e44f0a904709f/images/integrations/tools/data-integration/retool/retool_02.png" alt="Choosing JDBC connector"/>
<br/>

In the setup wizard, make sure you select `com.clickhouse.jdbc.ClickHouseDriver` as the "Driver name":

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/4284c45534e0f8e415ee160ec7af990c5313e6d1bcbcbd92492cb7aa2cf1c4d9/images/integrations/tools/data-integration/retool/retool_03.png" alt="Selecting the right driver"/>
<br/>

Fill in your ClickHouse credentials in the following format: `jdbc:clickhouse://HOST:PORT/DATABASE?user=USERNAME&password=PASSWORD`.
If your instance requires SSL or you are using ClickHouse Cloud, add `&ssl=true` to the connection string, so it looks like `jdbc:clickhouse://HOST:PORT/DATABASE?user=USERNAME&password=PASSWORD&ssl=true`

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/b44d119ae1da31635782a7ece80588b78c2226045aaf9cd2cdd74237aacaf32b/images/integrations/tools/data-integration/retool/retool_04.png" alt="Specifying your credentials"/>
<br/>

After that, test your connection:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/f4f1aaf51a504d415b898470cd484dc998637a5a6ab2c543cd38de938b7a148a/images/integrations/tools/data-integration/retool/retool_05.png" alt="Testing your connection"/>
<br/>

Now, you should be able to proceed to your app using your ClickHouse resource.
