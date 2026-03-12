# Source: https://clickhouse.ferndocs.com/reference/sql-reference/functions/overview.md

# Source: https://clickhouse.ferndocs.com/integrations/azure-data-factory/overview.md

# Source: https://clickhouse.ferndocs.com/ch-db/chdb/overview.md

# Source: https://clickhouse.ferndocs.com/click-stack/use-cases/observability/clickstack/ingesting-data/overview.md

# Source: https://clickhouse.ferndocs.com/click-stack/use-cases/observability/clickstack/deployment/overview.md

# Source: https://clickhouse.ferndocs.com/click-stack/use-cases/observability/clickstack/overview.md

# Source: https://clickhouse.ferndocs.com/open-source/operations/backup/overview.md

# Source: https://clickhouse.ferndocs.com/open-source/operations/settings/overview.md

# Source: https://clickhouse.ferndocs.com/cloud/manage/billing/overview.md

# Source: https://clickhouse.ferndocs.com/cloud/reference/byoc/overview.md

# Source: https://clickhouse.ferndocs.com/cloud/manage/backups/overview.md

# Source: https://clickhouse.ferndocs.com/cloud/migrations/postgresql/overview.md

# Source: https://clickhouse.ferndocs.com/cloud/integrations/migration/overview.md

---
sidebar_label: Overview
sidebar_position: 1
slug: /integrations/migration/overview
keywords:

- clickhouse
- migrate
- migration
- migrating
- data
title: Migrating Data into ClickHouse
description: Page describing the options available for migrating data into ClickHouse
doc_type: guide

---

<div class='vimeo-container'>
  <iframe src="https://player.vimeo.com/video/753082620?h=eb566c8c08"
    width="640"
    height="360"
    frameborder="0"
    allow="autoplay;
    fullscreen;
    picture-in-picture"
    allowfullscreen>
  </iframe>
</div>

<br/>

There are several options for migrating data into ClickHouse Cloud, depending on where your data resides now:

- [Self-managed to Cloud](/cloud/migration/clickhouse-to-cloud): use the `remoteSecure` function to transfer data
- [Another DBMS](/cloud/migration/clickhouse-local): use the [clickhouse-local] ETL tool along with the appropriate ClickHouse table function for your current DBMS
- [Anywhere!](/cloud/migration/etl-tool-to-clickhouse): use one of the many popular ETL/ELT tools that connect to all kinds of different data sources
- [Object Storage](/integrations/migration/object-storage-to-clickhouse): easily insert data from S3 into ClickHouse

In the example [Migrate from Redshift](/migrations/redshift/migration-guide), we present three different ways to migrate data to ClickHouse.
