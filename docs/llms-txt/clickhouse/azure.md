# Source: https://clickhouse.ferndocs.com/open-source/operations/backup/azure.md

---
description: Details backup/restore to or from an Azure Blob Storage endpoint
sidebar_label: AzureBlobStorage
slug: /operations/backup/azure
title: Backup and restore to/from Azure Blob Storage
doc_type: guide
---

## Syntax [#syntax]

```sql
-- core commands
BACKUP | RESTORE [ASYNC]
--- what to backup/restore (or exclude)
TABLE [db.]table_name           [AS [db.]table_name_in_backup] |
DICTIONARY [db.]dictionary_name [AS [db.]name_in_backup] |
DATABASE database_name          [AS database_name_in_backup] |
TEMPORARY TABLE table_name      [AS table_name_in_backup] |
VIEW view_name                  [AS view_name_in_backup] |
[EXCEPT TABLES ...] |
ALL [EXCEPT {TABLES|DATABASES}...] } [,...]
--- 
[ON CLUSTER 'cluster_name']
--- where to backup or restore to or from
TO|FROM 
File('<path>/<filename>') | 
Disk('<disk_name>', '<path>/') | 
S3('<S3 endpoint>/<path>', '<Access key ID>', '<Secret access key>', '<extra_credentials>') |
AzureBlobStorage('<connection string>/<url>', '<container>', '<path>', '<account name>', '<account key>')
--- additional settings
[SETTINGS ...]
```

**See ["command summary"](/operations/backup/overview/#command-summary) for more details
of each command.**

## Configuring BACKUP / RESTORE to use an AzureBlobStorage endpoint [#configuring-backuprestore-to-use-an-azureblobstorage-endpoint]

To write backups to an AzureBlobStorage container you need the following pieces of information:
- AzureBlobStorage endpoint connection string / url,
- Container,
- Path,
- Account name (if url is specified)
- Account Key (if url is specified)

The destination for a backup will be specified as:

```sql
AzureBlobStorage('<connection string>/<url>', '<container>', '<path>', '<account name>', '<account key>')
```

```sql
BACKUP TABLE data TO AzureBlobStorage('DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://azurite1:10000/devstoreaccount1/;',
    'testcontainer', 'data_backup');
RESTORE TABLE data AS data_restored FROM AzureBlobStorage('DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://azurite1:10000/devstoreaccount1/;',
    'testcontainer', 'data_backup');
```
