# Source: https://clickhouse.ferndocs.com/click-pipes/integrations/clickpipes/mysql/removing_tables.md

# Source: https://clickhouse.ferndocs.com/click-pipes/integrations/clickpipes/mongodb/removing_tables.md

# Source: https://clickhouse.ferndocs.com/click-pipes/integrations/clickpipes/postgres/removing_tables.md

---
title: Removing specific tables from a ClickPipe
description: Removing specific tables from a ClickPipe
sidebar_label: Remove Table
slug: /integrations/clickpipes/postgres/removing_tables
doc_type: guide
keywords:
  - clickpipes
  - postgresql
  - cdc
  - data ingestion
  - real-time sync
---

In some cases, it makes sense to exclude specific tables from a Postgres ClickPipe - for example, if a table isn't needed for your analytics workload, skipping it can reduce storage and replication costs in ClickHouse.

## Steps to remove specific tables [#remove-tables-steps]

The first step is to remove the table from the pipe. This can be done by the following steps:

1. [Pause](/click-pipes/integrations/clickpipes/postgres/pause_and_resume) the pipe.
2. Click on Edit Table Settings.
3. Locate your table - this can be done by searching it in the search bar.
4. Deselect the table by clicking on the selected checkbox.
<br/>

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/1bbb0a63506ad8cd114175907776fd540680ffbcf6c8ff03f6cfcfdd7ee3a8f0/images/integrations/data-ingestion/clickpipes/postgres/remove_table.png"/>

5. Click update.
6. Upon successful update, in the **Metrics** tab the status will be **Running**. This table will no longer be replicated by this ClickPipe.
