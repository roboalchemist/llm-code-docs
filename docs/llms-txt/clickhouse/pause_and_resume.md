# Source: https://clickhouse.ferndocs.com/click-pipes/integrations/clickpipes/mysql/pause_and_resume.md

# Source: https://clickhouse.ferndocs.com/click-pipes/integrations/clickpipes/mongodb/pause_and_resume.md

# Source: https://clickhouse.ferndocs.com/click-pipes/integrations/clickpipes/postgres/pause_and_resume.md

---
title: Pausing and Resuming a Postgres ClickPipe
description: Pausing and Resuming a Postgres ClickPipe
sidebar_label: Pause table
slug: /integrations/clickpipes/postgres/pause_and_resume
doc_type: guide
keywords:
  - clickpipes
  - postgresql
  - cdc
  - data ingestion
  - real-time sync
---

There are scenarios where it would be useful to pause a Postgres ClickPipe. For example, you may want to run some analytics on existing data in a static state. Or, you might be performing upgrades on Postgres. Here is how you can pause and resume a Postgres ClickPipe.

## Steps to pause a Postgres ClickPipe [#pause-clickpipe-steps]

1. In the Data Sources tab, click on the Postgres ClickPipe you wish to pause.
2. Head over to the **Settings** tab.
3. Click on the **Pause** button.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/2ecf6a598fb2f3762ae059645686d4c27c00e3a9abcda9ab8dd593d027fa3769/images/integrations/data-ingestion/clickpipes/postgres/pause_button.png"/>

4. A dialog box should appear for confirmation. Click on Pause again.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/7c170fe7a1a110b4e9e80692b38dd984f127455d38ea647273fa3c2be7f6537d/images/integrations/data-ingestion/clickpipes/postgres/pause_dialog.png"/>

4. Head over to the **Metrics** tab.
5. In around 5 seconds (and also on page refresh), the status of the pipe should be **Paused**.

<Warning>
Pausing a Postgres ClickPipe will not pause the growth of replication slots.
</Warning>

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/1cf954eef8788d4f5bf77079cf90b32f866096bbd9495c7907e6011aae84efe7/images/integrations/data-ingestion/clickpipes/postgres/pause_status.png"/>

## Steps to resume a Postgres ClickPipe [#resume-clickpipe-steps]
1. In the Data Sources tab, click on the Postgres ClickPipe you wish to resume. The status of the mirror should be **Paused** initially.
2. Head over to the **Settings** tab.
3. Click on the **Resume** button.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/e45f5971bb19a468a25df3294c7c79b98de019bb97a9339e3d742c2d4221c1df/images/integrations/data-ingestion/clickpipes/postgres/resume_button.png"/>

4. A dialog box should appear for confirmation. Click on Resume again.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/4f4b51593f724370d3e0652564a89e3cb9f60357f21c6ae2640b1809f5e0ddcf/images/integrations/data-ingestion/clickpipes/postgres/resume_dialog.png"/>

5. Head over to the **Metrics** tab.
6. In around 5 seconds (and also on page refresh), the status of the pipe should be **Running**.
