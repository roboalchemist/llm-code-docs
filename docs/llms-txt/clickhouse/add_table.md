# Source: https://clickhouse.ferndocs.com/click-pipes/integrations/clickpipes/mysql/add_table.md

# Source: https://clickhouse.ferndocs.com/click-pipes/integrations/clickpipes/mongodb/add_table.md

# Source: https://clickhouse.ferndocs.com/click-pipes/integrations/clickpipes/postgres/add_table.md

---
title: Adding specific tables to a ClickPipe
description: Describes the steps need to add specific tables to a ClickPipe.
sidebar_label: Add table
slug: /integrations/clickpipes/postgres/add_table
show_title: false
keywords:
  - clickpipes postgres
  - add table
  - table configuration
  - initial load
  - snapshot
doc_type: guide
---

There are scenarios where it would be useful to add specific tables to a pipe. This becomes a common necessity as your transactional or analytical workload scales.

## Steps to add specific tables to a ClickPipe [#add-tables-steps]

This can be done by the following steps:
1. [Pause](/click-pipes/integrations/clickpipes/postgres/pause_and_resume) the pipe.
2. Click on Edit Table settings.
3. Locate your table - this can be done by searching it in the search bar.
4. Select the table by clicking on the checkbox.
<br/>
<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/977330de6e051295bd9ddeb67405aef15c864a121d82be4b1861bf57b7d5c80d/images/integrations/data-ingestion/clickpipes/postgres/add_table.png"/>

5. Click update.
6. Upon successful update, the pipe will have statuses `Setup`, `Snapshot` and `Running` in that order. The table's initial load can be tracked in the **Tables** tab.

<Note>
CDC for existing tables resumes automatically after the new table’s snapshot completes.
</Note>
