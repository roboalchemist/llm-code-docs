# Source: https://code.kx.com/kdbai/latest/use/query.html

Title: Query KDB.AI Tables - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/use/query.html

Markdown Content:
Query KDB.AI Tables - KDB.AI Documentation
===============
- [x] - [x] 

[Skip to content](https://code.kx.com/kdbai/latest/use/query.html#how-to-query-data-in-kdbai)

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

 Query KDB.AI Tables 

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
    *   - [x]  Query Data  [Query Data](https://code.kx.com/kdbai/latest/use/query.html) On this page  
        *   [Selecting the table to query](https://code.kx.com/kdbai/latest/use/query.html#selecting-the-table-to-query)
        *   [Queries](https://code.kx.com/kdbai/latest/use/query.html#queries)
        *   [Filters](https://code.kx.com/kdbai/latest/use/query.html#filters)
        *   [Processing results](https://code.kx.com/kdbai/latest/use/query.html#processing-results)
        *   [Supported aggregations](https://code.kx.com/kdbai/latest/use/query.html#supported-aggregations)
        *   [Next Steps](https://code.kx.com/kdbai/latest/use/query.html#next-steps)

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
*   [Selecting the table to query](https://code.kx.com/kdbai/latest/use/query.html#selecting-the-table-to-query)
*   [Queries](https://code.kx.com/kdbai/latest/use/query.html#queries)
*   [Filters](https://code.kx.com/kdbai/latest/use/query.html#filters)
*   [Processing results](https://code.kx.com/kdbai/latest/use/query.html#processing-results)
*   [Supported aggregations](https://code.kx.com/kdbai/latest/use/query.html#supported-aggregations)
*   [Next Steps](https://code.kx.com/kdbai/latest/use/query.html#next-steps)

How to Query Data in KDB.AI
===========================

_This page covers how to perform queries against tables in the KDB.AI database._

Selecting the table to query
----------------------------

Each table in KDB.AI has an associated name. To perform a query, specify the name of the table in which the relevant data is stored. Using Python client you can create a table object from the session. The REST client is more direct with the table name supplied as a field in the JSON payload.

Python 

```python
documents = session.database('default').table("documents")
```

Queries
-------

Obtain the data from the entire table using the following command:

Python REST q 

```python
documents.query()
```

```bash
curl -s -X POST localhost:8081/api/v2/databases/default/tables/documents/query | jq .
```

```q
gw(`query;`database`table!(`default;`documents));
```

Filters
-------

To select a subset of the data, you can apply filters as documented [here](https://code.kx.com/kdbai/latest/use/filter.html). These serve as `where` clauses.

Python REST q 

```python
import datetime
    start_time=datetime.datetime(2024,1,10)
    end_time=datetime.datetime(2024,10,10)
    results = table.query(filter=[("within","createdDate",[start_time, end_time]),("<=", "length", 100)])
    print(f'Results: {results}')
```

```bash
curl -s -H "Content-Type: application/json" localhost:8081/api/v2/databases/default/tables/documents/query \
-d '{"table":"documents","filter":[["within","createdDate",["2020.07.10D15:00:00.0000", "2021.07.10D15:00:00.0000"]],["<=", "length", 100]]}'
```

```q
gw(`query;`database`table`filter!(`default;`documents;((within;`time;(2000.06.15D00:00:00.000000001; 2000.08.15D00:00:00.000000001));(<=;`length;100))));
```

Processing results
------------------

You can return a subset of the columns in the table, reducing the amount of data sent back to the client.

Python REST q 

```python
documents.query(aggs={"author":"author","content":"content"})
```

```bash
curl -s -X POST -H 'Content-Type: application/json' localhost:8081/api/v2/databases/default/tables/documents/query \
-d '{"aggs":{"author":"author","content":"content"}}' | jq .
```

```q
gw(`query;`database`table`aggs!(`default;`documents;`author`content!`author`content))
```

In addition to returning a subset of the columns, you can return aggregated results, group by categorical variables, and sort based on a column name.

Python REST q 

```python
aggs = dict()
    aggs['SumLength'] = ('sum','length')

    print(f'Table data:\n\n {table.query()}')
    results = table.query(aggs=aggs, group_by=['author'], sort_columns=['SumLength'])
    print(f'Aggregate data results:\n {results}')
```

```bash
curl -s -H "Content-Type: application/json" localhost:8081/api/v2/databases/default/tables/documents/query \
-d '{"aggs":{"sumLength":["sum","length"]}, "groupBy":["author"], "sortColumns":["sumLength"]}'
```

```q
gw(`query;`database`table`aggs`groupBy`sortColumns!(`default;`documents;(enlist `sumLength)!(enlist `sum`length);`author;`sumLength))
```

Supported aggregations
----------------------

The table below lists all supported aggregation functions.

| **Function** | **Description** |
| --- | --- |
| `all` | Returns the logical 'and' of all values in a set. |
| `any` | Returns the logical 'or' of all values in a set. |
| `avg` | Calculates the mean value across the set of matching records. |
| `count` | Returns the number of records in the current selection. |
| `dev` | Calculates the standard deviation of a column. |
| `distinct` | Returns the distinct values from a column. |
| `first` | Returns the first occurrence of a value. This is useful when performing a group by aggregation. |
| `last` | Returns the last occurrence of a value. This is useful when performing a group by aggregation. |
| `max` | Takes the maximum value of a set of records. |
| `min` | Takes the minimum value of a set of records. |
| `prd` | Calculates the product of matching records. |
| `sdev` | Calculates the sample deviation of matching records. |
| `scov` | Calculates the sample covariance between matching records. |
| `sum` | Calculates the sum of matching records. |
| `svar` | Calculates the sample variance of matching records. |
| `var` | Calculates the variance of matching records. |

Next Steps
----------

Now that you're familiar with querying, move on to the following:

*   Try querying and fuzzy filtering in our [sample project](https://kdb.ai/learning-hub/samples/fuzzy-filtering/).
*   Review our articles on [metadata filtering](https://kdb.ai/learning-hub/articles/optimizing-vector-search-with-metadata-filtering/) and [fuzzy filtering](https://kdb.ai/learning-hub/articles/enhance-retrieval-with-fuzzy-filters-in-kdb-ai/) for more context.
*   Watch our video to learn more about [querying in vector databases](https://kdb.ai/learning-hub/video-lessons/querying-data-in-vector-databases/).

[Previous Ingest Data](https://code.kx.com/kdbai/latest/use/ingestion.html)[Next Delete Data](https://code.kx.com/kdbai/latest/use/delete-data.html)

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
