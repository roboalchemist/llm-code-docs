# Source: https://code.kx.com/kdbai/latest/use/delete-data.html

Title: How To Delete Data in KDB.AI

URL Source: https://code.kx.com/kdbai/latest/use/delete-data.html

Markdown Content:
How To Delete Data in KDB.AI - KDB.AI Documentation
===============
- [x] - [x] 

[Skip to content](https://code.kx.com/kdbai/latest/use/delete-data.html#how-to-delete-data-in-kdbai)

[](https://code.kx.com/kdbai/latest/index.html "KDB.AI Homepage")

 KDB.AI Documentation 

1.9.0
*   [1.9.0](https://code.kx.com/kdbai/1.9.0/)
*   [1.8.0](https://code.kx.com/kdbai/1.8.0/)
*   [1.7.0](https://code.kx.com/kdbai/1.7.0/)
*   [1.6.0](https://code.kx.com/kdbai/1.6.0/)
*   [1.5.0](https://code.kx.com/kdbai/1.5.0/)
*   [1.4.0](https://code.kx.com/kdbai/1.4.0/)
*   [1.3.0](https://code.kx.com/kdbai/1.3.0/)
*   [1.2.0](https://code.kx.com/kdbai/1.2.0/)
*   [1.1.0](https://code.kx.com/kdbai/1.1.0/)
*   [1.0.0](https://code.kx.com/kdbai/1.0.0/)

 How To Delete Data in KDB.AI 

Type to start searching

*   [Home](https://code.kx.com/kdbai/latest/index.html)
*   [Learn](https://code.kx.com/kdbai/latest/reference/authentication.html)
*   [How To](https://code.kx.com/kdbai/latest/use/database.html)
*   [API Reference](https://code.kx.com/kdbai/latest/reference/python-client.html)
*   [Integrations](https://code.kx.com/kdbai/latest/integrations/allintegrations.html)
*   [Examples](https://github.com/KxSystems/kdbai-samples/)
*   [Releases](https://code.kx.com/kdbai/latest/releaseNotes/release-notes-latest.html)
*   [Help and Support](https://code.kx.com/kdbai/latest/support/known-issues.html)

[](https://code.kx.com/kdbai/latest/ "KDB.AI Documentation") KDB.AI Documentation  
*   - [x]  Home   Home  
    *   [About KDB.AI](https://code.kx.com/kdbai/latest/index.html)
    *   - [x]  Get Started   Get Started  
        *   [Prerequisites](https://code.kx.com/kdbai/latest/gettingStarted/pre-requisites.html)
        *   [KDB.AI Server Setup](https://code.kx.com/kdbai/latest/gettingStarted/kdb-ai-server-setup.html)
        *   [Quick Start](https://code.kx.com/kdbai/latest/gettingStarted/quickstart.html)
        *   [Versioning and Upgrade](https://code.kx.com/kdbai/latest/versioning.html)

*   - [x]  Learn   Learn  
    *   [Authentication and Authorization (New)](https://code.kx.com/kdbai/latest/reference/authentication.html)
    *   [Database](https://code.kx.com/kdbai/latest/reference/database.html)
    *   [Table](https://code.kx.com/kdbai/latest/reference/table.html)
    *   [Data Types](https://code.kx.com/kdbai/latest/reference/supported-types.html)
    *   [Index](https://code.kx.com/kdbai/latest/reference/index.html)
    *   [Similarity Metrics](https://code.kx.com/kdbai/latest/reference/metrics.html)
    *   [Hybrid Search](https://code.kx.com/kdbai/latest/reference/hybrid.html)
    *   [Transformed TSS](https://code.kx.com/kdbai/latest/reference/transformed-tss.html)
    *   [Non-Transformed TSS](https://code.kx.com/kdbai/latest/reference/non-transformed-tss.html)
    *   [Dynamic Time Warping](https://code.kx.com/kdbai/latest/reference/dynamic-time-warping.html)
    *   [Filters](https://code.kx.com/kdbai/latest/reference/filters.html)
    *   [Partitioning](https://code.kx.com/kdbai/latest/reference/partition.html)
    *   [Reranking](https://code.kx.com/kdbai/latest/reference/reranking.html)
    *   [Parallel Processing](https://code.kx.com/kdbai/latest/reference/multithreading.html)
    *   [Learning Hub](https://kdb.ai/learning-hub)

*   - [x]  How To   How To  
    *   [Use Databases](https://code.kx.com/kdbai/latest/use/database.html)
    *   [Manage Tables](https://code.kx.com/kdbai/latest/use/manage-tables.html)
    *   [Ingest Data](https://code.kx.com/kdbai/latest/use/ingestion.html)
    *   [Query Data](https://code.kx.com/kdbai/latest/use/query.html)
    *   - [x]  Delete Data  [Delete Data](https://code.kx.com/kdbai/latest/use/delete-data.html) On this page  
        *   [Supported table types](https://code.kx.com/kdbai/latest/use/delete-data.html#supported-table-types)
        *   [Key considerations before deleting data](https://code.kx.com/kdbai/latest/use/delete-data.html#key-considerations-before-deleting-data)
            *   [1. Performance](https://code.kx.com/kdbai/latest/use/delete-data.html#1-performance)
            *   [2. Timing](https://code.kx.com/kdbai/latest/use/delete-data.html#2-timing)
            *   [3. Data safety](https://code.kx.com/kdbai/latest/use/delete-data.html#3-data-safety)
            *   [4. Use of filters](https://code.kx.com/kdbai/latest/use/delete-data.html#4-use-of-filters)
            *   [5. Disk and memory requirements](https://code.kx.com/kdbai/latest/use/delete-data.html#5-disk-and-memory-requirements)

        *   [Best practices](https://code.kx.com/kdbai/latest/use/delete-data.html#best-practices)
        *   [Backup and rollback behavior](https://code.kx.com/kdbai/latest/use/delete-data.html#backup-and-rollback-behavior)
        *   [Example: delete rows](https://code.kx.com/kdbai/latest/use/delete-data.html#example-delete-rows)
        *   [Next steps](https://code.kx.com/kdbai/latest/use/delete-data.html#next-steps)

    *   [Use Indexes](https://code.kx.com/kdbai/latest/use/supported-indexes.html)
    *   - [x]  Search   Search  
        *   [Similarity Search](https://code.kx.com/kdbai/latest/use/search.html)
        *   [Hybrid Search](https://code.kx.com/kdbai/latest/use/hybrid-search.html)
        *   [Transformed TSS](https://code.kx.com/kdbai/latest/use/transformed-tss.html)
        *   [Non-Transformed TSS](https://code.kx.com/kdbai/latest/use/non-transformed-tss.html)
        *   [Dynamic Time Warping (DTW)](https://code.kx.com/kdbai/latest/use/dynamic-time-warping-dtw.html)

    *   [Customize Filters](https://code.kx.com/kdbai/latest/use/filter.html)
    *   [Partition](https://code.kx.com/kdbai/latest/use/partitioning.html)
    *   [Rerank](https://code.kx.com/kdbai/latest/use/rerank.html)
    *   - [x]  Set Up Authentication   Set Up Authentication  
        *   [Static Authentication](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html)
        *   [OAuth 2.0](https://code.kx.com/kdbai/latest/use/set-up-oauth2-authentication.html)

    *   [Get System Usage Info](https://code.kx.com/kdbai/latest/use/get-system-usage-info.html)

*   - [x]  API Reference   API Reference  
    *   [Python API](https://code.kx.com/kdbai/latest/reference/python-client.html)
    *   [q API](https://code.kx.com/kdbai/latest/reference/qAPI.html)
    *   [REST API](https://code.kx.com/kdbai/latest/reference/rest-api.html)
    *   [Naming and Reserved Words](https://code.kx.com/kdbai/latest/reference/naming-convention-reserved-words.html)
    *   [Glossary](https://code.kx.com/kdbai/latest/reference/glossary.html)

*   - [x]  Integrations   Integrations  
    *   [All integrations](https://code.kx.com/kdbai/latest/integrations/allintegrations.html)
    *   [kdb+](https://code.kx.com/kdbai/latest/integrations/kdb.html)
    *   [OpenAI](https://code.kx.com/kdbai/latest/integrations/openai.html)
    *   [LangChain](https://code.kx.com/kdbai/latest/integrations/langchain.html)
    *   [LlamaIndex](https://code.kx.com/kdbai/latest/integrations/llamaindex.html)
    *   [Vector IO](https://code.kx.com/kdbai/latest/integrations/vector-io.html)
    *   [Azure AI](https://code.kx.com/kdbai/latest/integrations/azureml.html)
    *   [Hugging Face](https://code.kx.com/kdbai/latest/integrations/hugging-face.html)
    *   [Unstructured](https://code.kx.com/kdbai/latest/integrations/unstructured-io.html)
    *   [Cohere](https://code.kx.com/kdbai/latest/use/rerank.html)
    *   [Jina AI](https://code.kx.com/kdbai/latest/use/rerank.html)
    *   [Voyage AI](https://code.kx.com/kdbai/latest/use/rerank.html)
    *   [Model Context Protocol (MCP) Server](https://code.kx.com/kdbai/latest/integrations/mcp-server.html)

*   - [x]  Examples   Examples  
    *   [GitHub Samples](https://github.com/KxSystems/kdbai-samples/)

*   - [x]  Releases   Releases  
    *   [Latest](https://code.kx.com/kdbai/latest/releaseNotes/release-notes-latest.html)
    *   [Previous](https://code.kx.com/kdbai/latest/releaseNotes/release-notes-previous.html)

*   - [x]  Help and Support   Help and Support  
    *   [Known Issues](https://code.kx.com/kdbai/latest/support/known-issues.html)
    *   [FAQs and Troubleshooting](https://code.kx.com/kdbai/latest/support/FAQ-troubleshooting.html)
    *   [Slack Community](http://kx.com/slack)

 On this page  
*   [Supported table types](https://code.kx.com/kdbai/latest/use/delete-data.html#supported-table-types)
*   [Key considerations before deleting data](https://code.kx.com/kdbai/latest/use/delete-data.html#key-considerations-before-deleting-data)
    *   [1. Performance](https://code.kx.com/kdbai/latest/use/delete-data.html#1-performance)
    *   [2. Timing](https://code.kx.com/kdbai/latest/use/delete-data.html#2-timing)
    *   [3. Data safety](https://code.kx.com/kdbai/latest/use/delete-data.html#3-data-safety)
    *   [4. Use of filters](https://code.kx.com/kdbai/latest/use/delete-data.html#4-use-of-filters)
    *   [5. Disk and memory requirements](https://code.kx.com/kdbai/latest/use/delete-data.html#5-disk-and-memory-requirements)

*   [Best practices](https://code.kx.com/kdbai/latest/use/delete-data.html#best-practices)
*   [Backup and rollback behavior](https://code.kx.com/kdbai/latest/use/delete-data.html#backup-and-rollback-behavior)
*   [Example: delete rows](https://code.kx.com/kdbai/latest/use/delete-data.html#example-delete-rows)
*   [Next steps](https://code.kx.com/kdbai/latest/use/delete-data.html#next-steps)

How To Delete Data in KDB.AI
============================

_This page explains how to delete data from your KDB.AI tables._

Because KDB.AI is optimized for append-only streaming workloads, delete operations behave differently from traditional databases. They can be slow on large datasets and should be planned carefully. This page covers supported table types, performance tips, safe deletion practices, and rollback mechanisms. Follow the recommendations here to minimize risk and ensure correct behavior during deletions.

Supported table types
---------------------

KDB.AI supports the delete operation only on specific table index configurations. Before attempting a delete, confirm that your table meets one of the following criteria:

*   It has **no index**

*   It uses **a flat index**

*   It uses **a qFlat index**

*   It uses **multi-indexes** that include **only flat or qFlat indexes**

KDB.AI does not currently support deletions on tables with any other index types.

Key considerations before deleting data
---------------------------------------

### 1. Performance

Delete operations in KDB.AI are inherently slow - small deletions may complete in seconds, but larger datasets can take several hours to process.

This is because KDB.AI is built on a system-of-record model optimized for continuously appending data rather than modifying or removing it. While this design benefits high-throughput, real-time workloads, it makes deletions a heavier operation that requires more processing time.

### 2. Timing

For best performance and to minimize impact on other operations, schedule delete operations at the end of the day or during maintenance windows when no other tasks are active.

### 3. Data safety

The system includes safety mechanisms to handle data consistency during delete operations.

However, we strongly recommend backing up all critical data before performing a delete, as unforeseen corruption or system failures can lead to irreversible data loss.

### 4. Use of filters

Always apply filters when executing a delete operation to precisely target the data you intend to remove.

If no filter is specified, the operation will delete all data from the table without any confirmation, which can lead to unintended consequences.

### 5. Disk and memory requirements

**Disk usage**

The delete operation creates a backup of the data before deletion. As a result, it temporarily consumes additional disk space equal to the size of the table plus size of index being deleted. Ensure sufficient disk space is available to accommodate this backup during the operation.

**Memory usage**

The peak memory usage during deletion is determined by the largest column in the table. Ensure that the system has enough available memory to handle this maximum load efficiently.

Best practices
--------------

*   Preview your `delete` filter on a subset of data to ensure correctness.

*   Log all delete operations for audit purposes.

*   Test deletes in non-production environments before applying them in live systems.

Backup and rollback behavior
----------------------------

The delete operation creates a backup of the target data in the mounted data directory before attempting deletion. This backup is **automatically cleaned up** upon a **successful delete**.

In the case of a **delete failure**, the operation will:

*   Rollback by restoring data from the backup.

*   Retain the backup directory to ensure data is available for verification and recovery.

This behavior is intentional to safeguard against potential data corruption.

**Action Required**

After a delete failure, make sure you:

*   Verify the restored data integrity.

*   If data corruption is detected, manually recover it from the backup.

*   Delete the backup directory manually to reclaim disk space.

Example: delete rows
--------------------

The examples below show how to delete one or more rows based on a condition, using the KDB.AI q, Ptyhon, and REST APIs.

For instance, let's delete rows where `date = 2025.05.14` and `sym = "Vod.l"` from the `trade` table in the `default` database:

Python q REST 

```python
# Delete rows from the 'trade' table where 'date' is '2025.05.14' and 'sym' is 'Vod.l'
table.delete_data(
    filter=[
        ['=', 'date', '2025.05.14'],
        ['=', 'sym', 'Vod.l']
    ]
)
```

```q
// Delete rows from 'trade' in 'default' database where date is 2025.05.14 and sym is "Vod.l"
gw(
`deleteData;
args: `database`table`filter!(
    `default;
    `trade;
    (("=";"date";"2025.05.14"); ("=";"sym";"Vod.l"))
)
```

```sh
POST /api/v2/databases/default/tables/trade/data/delete
Content-Type: application/json

{
"filter": [
    ["=", "date", "2025.05.14"],
    ["=", "sym", "Vod.l"]
]
}
```

Next steps
----------

*   Read the [latest release notes](https://code.kx.com/kdbai/latest/releaseNotes/release-notes-latest.html).

[Previous Query Data](https://code.kx.com/kdbai/latest/use/query.html)[Next Use Indexes](https://code.kx.com/kdbai/latest/use/supported-indexes.html)

 © 2026 KX Systems, Inc. KX, KDB-X, and kdb+ are registered trademarks of KX Systems, Inc., a subsidiary of KX Software Limited. 

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

![Image 1](https://id.rlcdn.com/464526.gif)

By clicking “Accept All Cookies”, you agree to the storing of cookies on your device to enhance site navigation, analyze site usage, and assist in our marketing efforts.[Cookies Policy.](https://kx.com/cookie-policy/)

Cookies Settings Reject All Accept All

![Image 2: KX Logo](https://cdn-ukwest.onetrust.com/logos/2e246b76-a09f-455a-b12d-cb0cc60b7d47/36d73287-3cef-4657-ad68-1de87d20bcfb/e5b10d3a-3252-4f3a-8f47-e55d701ecfdf/KX-Logo-Black-500x500.png)

Privacy Preference Center
-------------------------

*   ### Your Privacy 
*   ### Strictly Necessary Cookies 
*   ### Performance Cookies 
*   ### Functional Cookies 
*   ### Targeting Cookies 

#### Your Privacy

When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. 

[More information](https://cookiepedia.co.uk/giving-consent-to-cookies)

#### Strictly Necessary Cookies

Always Active

These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.

#### Performance Cookies

- [x] Performance Cookies 

These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.

#### Functional Cookies

- [x] Functional Cookies 

These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.

#### Targeting Cookies

- [x] Targeting Cookies 

These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.

### Cookie List

Consent Leg.Interest

- [x] checkbox label label

- [x] checkbox label label

- [x] checkbox label label

Clear

- [x] checkbox label label

Apply Cancel

Confirm My Choices

Allow All

[![Image 3: Powered by Onetrust](https://cdn-ukwest.onetrust.com/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)
