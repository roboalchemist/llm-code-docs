# Source: https://code.kx.com/kdbai/latest/reference/table.html

Title: About tables in KDB.AI - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/reference/table.html

Markdown Content:
About tables in KDB.AI - KDB.AI Documentation
===============
- [x] - [x] 

[Skip to content](https://code.kx.com/kdbai/latest/reference/table.html#table)

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

 About tables in KDB.AI 

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
    *   - [x]  Table  [Table](https://code.kx.com/kdbai/latest/reference/table.html) On this page  
        *   [Table types](https://code.kx.com/kdbai/latest/reference/table.html#table-types)
            *   [Splayed tables](https://code.kx.com/kdbai/latest/reference/table.html#splayed-tables)
            *   [Partitioned tables](https://code.kx.com/kdbai/latest/reference/table.html#partitioned-tables)

        *   [Columnar storage](https://code.kx.com/kdbai/latest/reference/table.html#columnar-storage)
        *   [Memory mapping](https://code.kx.com/kdbai/latest/reference/table.html#memory-mapping)
        *   [Next steps](https://code.kx.com/kdbai/latest/reference/table.html#next-steps)

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
    *   [Delete Data](https://code.kx.com/kdbai/latest/use/delete-data.html)
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
*   [Table types](https://code.kx.com/kdbai/latest/reference/table.html#table-types)
    *   [Splayed tables](https://code.kx.com/kdbai/latest/reference/table.html#splayed-tables)
    *   [Partitioned tables](https://code.kx.com/kdbai/latest/reference/table.html#partitioned-tables)

*   [Columnar storage](https://code.kx.com/kdbai/latest/reference/table.html#columnar-storage)
*   [Memory mapping](https://code.kx.com/kdbai/latest/reference/table.html#memory-mapping)
*   [Next steps](https://code.kx.com/kdbai/latest/reference/table.html#next-steps)

Table
=====

_This page explains the concepts of table (splayed and partitioned), columnar storage, and memory mapping in KDB.AI._

If you're already familiar with this topic, you can skip ahead to the [How-to guide](https://code.kx.com/kdbai/latest/use/manage-tables.html).

In KDB.AI, tables are the main structures for storing and organizing data. They come in two types, each suited to different use cases and performance requirements.

Table types
-----------

Below is an overview of the types of tables supported in KDB.AI: splayed and partitioned:

| **Table Type** | **Splayed** | **Partitioned** |
| --- | --- | --- |
| **Description** | Stores each column as a separate file, improving performance for large datasets. | A splayed table further divided into partitions based on a column with special types like date, month, or year. |
| **Use cases** | Best for medium-sized tables (up to 100 million rows) where queries often access a subset of columns. | Suitable for very large datasets (over 100 million rows) or when data grows over time and queries can be limited to specific partitions. |
| **Additional information** | Requires more disk space and management but offers faster reading times for specific columns. | Enhances performance by reducing the amount of data scanned during queries. |

### Splayed tables

[Splayed tables](https://code.kx.com/q/kb/splayed-tables/) store each column in a separate file. This structure allows for more efficient queries, especially when only a subset of columns is needed. Splayed tables are particularly useful for medium-sized datasets where the overhead of managing multiple files is outweighed by the performance benefits.

### Partitioned tables

[Partitioned tables](https://code.kx.com/q/kb/partition/) take the concept of splayed tables further by dividing the data into partitions based on a specific column, such as date. Partitioning allows for even more efficient queries by limiting the data scanned to relevant partitions. Partitioned tables are ideal for very large datasets or datasets that grow over time, such as time-series data.

Examples in q:

Splayed table Partitioned table 

```q
// Example of creating a splayed table for trade data
trades: ([] 
date: `date$(), 
time: `time$(), 
sym: `symbol$(), 
price: `real$(), 
size: `int$(), 
cond: `char$()
)

// Insert sample data
`trades insert (2024.11.01; 10:03:54.347; `AAPL; 150.25; 1000; "N")
`trades insert (2024.11.01; 10:04:05.827; `GOOG; 2750.50; 500; "B")

// Save the table as splayed
`:trades/ set trades
```

```q
// Example of creating a partitioned table for trade data
trades: ([] 
date: `date$(), 
time: `time$(), 
sym: `symbol$(), 
price: `real$(), 
size: `int$(), 
cond: `char$()
)

// Insert sample data
`trades insert (2024.11.01; 10:03:54.347; `AAPL; 150.25; 1000; "N")
`trades insert (2024.11.01; 10:04:05.827; `GOOG; 2750.50; 500; "B")

// Save the table as partitioned by date
`:trades/2024.11.01/ set trades
```

Columnar storage
----------------

Columnar storage is a method of storing tables by column rather than by row. This approach significantly improves the performance of read-heavy operations, such as analytical queries, because it allows for more efficient data compression and faster access to the relevant columns. In KDB.AI, columnar storage is particularly beneficial for large datasets where only a few columns are queried at a time.

Benefits of columnar storage:

*   **Improved query performance:** By storing data in columns, queries that access only a subset of columns can be executed more quickly.
*   **Efficient compression:** Columnar storage allows for better data compression, reducing storage requirements and improving I/O performance.
*   **Optimized for analytical workloads:** Ideal for scenarios where read operations are more frequent than write operations, such as data analytics and reporting.

Memory mapping
--------------

Memory mapping is a technique used to access data stored on disk as if it were in memory. This method allows KDB.AI to handle large datasets efficiently by mapping files directly into the virtual memory space of a process. Memory mapping reduces the overhead of copying data between disk and memory, leading to faster data retrieval and improved performance.

Benefits of memory mapping:

*   **Faster data access:** By mapping files directly into memory, the need for data copying is eliminated, resulting in quicker data access.
*   **Efficient use of resources:** Memory mapping allows the system to use disk storage as if it were RAM, effectively increasing the available memory for large datasets.
*   **Reduced I/O overhead:** Direct access to the file data reduces the number of I/O operations, enhancing overall system performance.

Next steps
----------

*   [Manage tables](https://code.kx.com/kdbai/latest/use/manage-tables.html).

[Previous Database](https://code.kx.com/kdbai/latest/reference/database.html)[Next Data Types](https://code.kx.com/kdbai/latest/reference/supported-types.html)

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
