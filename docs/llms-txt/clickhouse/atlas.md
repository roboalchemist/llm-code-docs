# Source: https://clickhouse.ferndocs.com/click-pipes/integrations/clickpipes/mongodb/source/atlas.md

---
sidebar_label: MongoDB Atlas
description: Step-by-step guide on how to set up MongoDB Atlas as a source for ClickPipes
slug: /integrations/clickpipes/mongodb/source/atlas
title: MongoDB Atlas source setup guide
doc_type: guide
keywords:
  - clickpipes
  - mongodb
  - cdc
  - data ingestion
  - real-time sync
---


## Configure oplog retention [#enable-oplog-retention]

Minimum oplog retention of 24 hours is required for replication. We recommend setting the oplog retention to 72 hours or longer to ensure that the oplog is not truncated before the initial snapshot is completed. To set the oplog retention via UI:

1. Navigate to your cluster's `Overview` tab in the MongoDB Atlas console and click on the `Configuration` tab.
<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/d085b3cd4b68aba84960c29acee3ea218d80d2a1f92ca0607dbe925ef7a869ca/images/integrations/data-ingestion/clickpipes/mongodb/mongo-atlas-cluster-overview-configuration.png" alt="Navigate to cluster configuration"/>

2. Click `Additional Settings` and scroll down to `More Configuration Options`.
<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/6d1ee3dce0572b7668bf17885451925ac6884e6e203f700ec6910cbbb3395025/images/integrations/data-ingestion/clickpipes/mongodb/mongo-atlas-expand-additional-settings.png" alt="Expand additional settings"/>

3. Click `More Configuration Options` and set the minimum oplog window to `72 hours` or longer.
<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/d288df142f6200d100d80a27c164f34561819e9776675a90ecbdcbd8158c8092/images/integrations/data-ingestion/clickpipes/mongodb/mongo-atlas-set-retention-hours.png" alt="Set oplog retention hours"/>

4. Click `Review Changes` to review, and then `Apply Changes` to deploy the changes.

## Configure a database user [#configure-database-user]

Once you are logged in to your MongoDB Atlas console, click `Database Access` under the Security tab in the left navigation bar. Click on "Add New Database User".

ClickPipes requires password authentication:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/ffbcbbc215a3f6b55b234b10273dbb07bc5e09ea9e539bd9cfb70ef9d75c64b0/images/integrations/data-ingestion/clickpipes/mongodb/mongo-atlas-add-new-database-user.png" alt="Add database user"/>

ClickPipes requires a user with the following roles:

- `readAnyDatabase`
- `clusterMonitor`

You can find them in the `Specific Privileges` section:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/1e4daf73e63fe7420315bc0e79c909822a1470a5c94f3f7d7458364126a94723/images/integrations/data-ingestion/clickpipes/mongodb/mongo-atlas-database-user-privilege.png" alt="Configure user roles"/>

You can further specify the cluster(s)/instance(s) you wish to grant access to ClickPipes user:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/e29fa39b43c1fdd6ae9254899212c7c7259e77c37e65414833c4074ddeb47a9b/images/integrations/data-ingestion/clickpipes/mongodb/mongo-atlas-restrict-access.png" alt="Restrict cluster/instance acces"/>

## What's next? [#whats-next]

You can now [create your ClickPipe](/click-pipes/integrations/clickpipes/mongodb) and start ingesting data from your MongoDB instance into ClickHouse Cloud.
Make sure to note down the connection details you used while setting up your MongoDB instance as you will need them during the ClickPipe creation process.
