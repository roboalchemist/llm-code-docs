# Source: https://code.kx.com/kdbai/latest/reference/database.html

Title: About databases in KDB.AI - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/reference/database.html

Markdown Content:
About databases in KDB.AI - KDB.AI Documentation
===============
- [x] - [x] 

[Skip to content](https://code.kx.com/kdbai/latest/reference/database.html#database)

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

 About databases in KDB.AI 

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
    *   - [x]  Database  [Database](https://code.kx.com/kdbai/latest/reference/database.html) On this page  
        *   [Vector databases](https://code.kx.com/kdbai/latest/reference/database.html#vector-databases)
        *   [Multiple Databases](https://code.kx.com/kdbai/latest/reference/database.html#multiple-databases)
        *   [Next steps](https://code.kx.com/kdbai/latest/reference/database.html#next-steps)

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
*   [Vector databases](https://code.kx.com/kdbai/latest/reference/database.html#vector-databases)
*   [Multiple Databases](https://code.kx.com/kdbai/latest/reference/database.html#multiple-databases)
*   [Next steps](https://code.kx.com/kdbai/latest/reference/database.html#next-steps)

Database
========

_This page explains the concept of database, vector databases, and multiple databases._

If you're already familiar with this topic, you can skip ahead to the [How-to guide](https://code.kx.com/kdbai/latest/use/database.html).

In KDB.AI, a database is a collection of tables which stores related data.

Basic info on databases
Databases are fundamental to modern computing, enabling efficient data management and retrieval, which is crucial for everything from business operations to scientific research.

A database is an organized collection of data that you can electronically access, store and manage. Databases allow you to retrieve large amounts of information efficiently. They are essential for various applications, from simple data storage to complex data analysis and processing.

Here are the key concepts associated with databases:

*   **Data**: The raw information that is stored in the database. This can include various formats, such as text, numbers, and images. 
*   **Database Management System (DBMS)**: Software platform that facilitates the interaction between the database, users, and applications to capture and analyze data (for example, MySQL). 
*   **Tables**: Relational databases organize data into tables. Each table consists of rows and columns, where a row is a record, and a column is a field within the record. 
*   **Queries**: Requests made to the database to retrieve or edit data. SQL (Structured Query Language) is commonly used for writing queries in relational databases. 
*   **Indexes**: Structures that speed up data retrieval operations on database tables. 
*   **Transactions**: A sequence of actions executed as a single logical unit of work. Transactions ensure data integrity and consistency. 

**Types of databases**

There are multiple types of databases, each uniquely suited to exact use cases and optimized for handling different kinds of data and queries:

*   **Relational databases**: Use structured query language (SQL) to define, manage and manipulate data organized into tables. 
*   **NoSQL databases**: Designed for unstructured data and can handle large volumes of diverse data types. 
*   **Time-Series databases**: Optimized to handle time-stamped data, they're ideal for applications like monitoring and IoT. 
*   **Graph databases**: Represent and store data using graph structures, which consist of nodes (entities), edges (relationships), and properties (attributes). 
*   **Vector databases**: Optimized for high-dimensional data and are particularly useful in AI applications such as Machine Learning (ML) and Natural Language Processing (NLP). 

Using multiple types of databases allows organizations to leverage the strengths of each type to handle different data and query requirements more effectively. For instance, a company might use a relational database for transactional data, a time-series database for monitoring system performance, and a vector database for AI-driven search and recommendation systems.

Vector databases
----------------

A vector database is a database specifically designed to efficiently store, manage, and retrieve vector data. Vectors are ordered sets of numerical values that represent various types of data, such as spatial coordinates, feature attributes, or embeddings used in machine learning.

Key features of vector databases:

*   **High-Dimensional Data**: Vector databases handle data represented as vectors (both sparse and dense). 
*   **Similarity Search**: Vector databases excel at finding similar items based on vector similarity, which is crucial for applications like recommendation systems, image and video search, and natural language processing. 
*   **Efficient Storage and Retrieval**: Optimized for low-latency queries, making them suitable for real-time applications. 

Multiple Databases
------------------

In the context of vector databases such as KDB.AI, having multiple databases typically means that the system can manage and store data across several distinct databases, each optimized for different types of data or use cases. For example, you might have databases like “market_data”, “trades”, and “hr_data”. Each of these databases can contain several tables.

Here are a few key points:

*   **Database structure**: Each table belongs to a specific database. Think of databases as individual containers that hold multiple tables.
*   **Organization**: This structure helps in organizing tables logically, so you don’t end up with a clutter of 100 tables in a single database. 
*   **Table naming**: You can have tables with the same name in different databases. For example, both 
```python
market_data
```
 and 
```python
trades
```
 can have a table named 
```python
transactions
```
 without any conflict. 

Next steps
----------

Now that you’re familiar with databases:

*   Learn how to [create, retrieve and delete a database](https://code.kx.com/kdbai/latest/use/database.html) in KDB.AI. 

[Previous Authentication and Authorization (New)](https://code.kx.com/kdbai/latest/reference/authentication.html)[Next Table](https://code.kx.com/kdbai/latest/reference/table.html)

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
