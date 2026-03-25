# Source: https://code.kx.com/kdbai/latest/reference/non-transformed-tss.html

Title: About Non-Transformed Temporal Similarity Search

URL Source: https://code.kx.com/kdbai/latest/reference/non-transformed-tss.html

Markdown Content:
About Non-Transformed Temporal Similarity Search - KDB.AI Documentation
===============
- [x] - [x] 

[Skip to content](https://code.kx.com/kdbai/latest/reference/non-transformed-tss.html#non-transformed-tss)

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

 About Non-Transformed Temporal Similarity Search 

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
    *   - [x]  Non-Transformed TSS  [Non-Transformed TSS](https://code.kx.com/kdbai/latest/reference/non-transformed-tss.html) On this page  
        *   [Differences between Non-Transformed TSS and similarity search](https://code.kx.com/kdbai/latest/reference/non-transformed-tss.html#differences-between-non-transformed-tss-and-similarity-search)
        *   [Benefits of Non-Transformed TSS on temporal data](https://code.kx.com/kdbai/latest/reference/non-transformed-tss.html#benefits-of-non-transformed-tss-on-temporal-data)
        *   [Time series pattern matching](https://code.kx.com/kdbai/latest/reference/non-transformed-tss.html#time-series-pattern-matching)
        *   [Next steps](https://code.kx.com/kdbai/latest/reference/non-transformed-tss.html#next-steps)

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
*   [Differences between Non-Transformed TSS and similarity search](https://code.kx.com/kdbai/latest/reference/non-transformed-tss.html#differences-between-non-transformed-tss-and-similarity-search)
*   [Benefits of Non-Transformed TSS on temporal data](https://code.kx.com/kdbai/latest/reference/non-transformed-tss.html#benefits-of-non-transformed-tss-on-temporal-data)
*   [Time series pattern matching](https://code.kx.com/kdbai/latest/reference/non-transformed-tss.html#time-series-pattern-matching)
*   [Next steps](https://code.kx.com/kdbai/latest/reference/non-transformed-tss.html#next-steps)

Non-Transformed TSS
===================

_This page explains the Non-Transformed Temporal Similarity Search (Non-Transformed TSS) feature in KDB.AI._

If you're already familiar with this topic, you can skip ahead to the [How to perform a Non-Transformed TSS search](https://code.kx.com/kdbai/latest/use/non-transformed-tss.html) guide.

Non-Transformed TSS is a similarity search algorithm specific for time series data, with high precision: ![Image 3](https://latex.codecogs.com/svg.latex?{\color{NavyBlue}%20{10^{-9}}}) and measured up to 1 million data points. For a single series search, you can query extensive historical data using the 
```python
searchBy
```
 advanced option applied on splayed or [partitioned](https://code.kx.com/kdbai/latest/use/partitioning.html) tables running on [external kdb+ databases](https://code.kx.com/kdbai/latest/integrations/kdb.html).

For example usage, see our [GitHub repository](https://github.com/KxSystems/kdbai-samples).

The key concepts to understand are:

*   [differences between Non-Transformed TSS and similarity search](https://code.kx.com/kdbai/latest/reference/non-transformed-tss.html#differences-between-non-transformed-tss-and-similarity-search)
*   [the benefits of Non-Transformed TSS on temporal data](https://code.kx.com/kdbai/latest/reference/non-transformed-tss.html#benefits-of-non-transformed-tss-on-temporal-data)
*   [time series pattern matching](https://code.kx.com/kdbai/latest/reference/non-transformed-tss.html#time-series-pattern-matching).

Differences between Non-Transformed TSS and similarity search
-------------------------------------------------------------

Non-Transformed TSS differs from [similarity search](https://code.kx.com/kdbai/latest/use/search.html) indexes in the following ways:

*   There is no precomputation (index creation) involved.
*   It significantly reduces the time from data insertion to first query, which is an advantage for fast-moving data.

Benefits of Non-Transformed TSS on temporal data
------------------------------------------------

Non-Transformed TSS leverages the strengths of traditional vector similarity search and simultaneously addresses the unique challenges of temporal data in key areas such as:

*   **Specialized Temporal Data Analysis:** offers a more precise and efficient method for analysing temporal data.
*   **Near Real Time Data Processing:** provides a significant boost in speed as no index build is required; allows quicker queries and faster data analysis, essential in environments where near-real-time data processing is critical.
*   **Enhanced Accuracy and Recall:** recognizes and interprets the patterns and trends inherent in temporal data leading to improved recall, accuracy, and precision.
*   **Ease of Use:** operates on temporal data as is, no complex parameters need be passed in, no index needs to be built to search.
*   **Dynamic Searches:** can be configured at run time unlike [FAISS](https://faiss.ai/) searches which require expensive and time-consuming index rebuild operations.
*   **Scalability and Adaptability:** offers a scalable solution that can handle increasing amounts of time series data as it is memory and CPU efficient.

Time series pattern matching
----------------------------

Time series pattern matching refers to the process of identifying and recognizing specific patterns or trends within a time series data set. As time series is a sequence of data points collected over a period of time (where each data point is associated with a timestamp), the time series pattern matching involves searching for recurring patterns, anomalies, or specific shapes within the data.

![Image 4](https://code.kx.com/kdbai/latest/images/release-notes-Non-TSS-pattern-matching.PNG)

In the above example, we are searching for a query of 10 time points: 
```python
[q1, q2, ..., q10]
```
 among a data of 60 time points: 
```python
[x31, x32, ..., x90]
```
. A sliding window of length 10, the same as the query is created and the length-60 data is scanned through the sliding windows and try to match with the query. The three most similar results, referring to the windows 
```python
B
```
, 
```python
A
```
 and 
```python
C
```
 are being output by the time series matching algorithm accordingly.

Pattern matching in time series data can be useful in various applications, such as event detection, anomaly detection, forecasting, and signal processing.

Next steps
----------

Now that you are familiar with the Non-Transformed TSS concepts, you can:

*   Perform a [Non-Transformed TSS](https://code.kx.com/kdbai/latest/use/non-transformed-tss.html) search.
*   Explore use cases on the [KDB.AI Learning hub](https://kdb.ai/learning-hub/articles/discovering-time-series-insights-with-temporal-similarity-search/).
*   Download the pattern matching [Jupyter Notebook](https://github.com/KxSystems/kdbai-samples/blob/main/pattern_matching/pattern_matching.ipynb) and accompanying files at the repository on [GitHub](https://github.com/KxSystems/kdbai-samples/tree/main/pattern_matching).
*   Run the notebook directly in [Google Colab](https://colab.research.google.com/github/KxSystems/kdbai-samples/blob/main/pattern_matching/pattern_matching.ipynb).

[Previous Transformed TSS](https://code.kx.com/kdbai/latest/reference/transformed-tss.html)[Next Dynamic Time Warping](https://code.kx.com/kdbai/latest/reference/dynamic-time-warping.html)

 © 2026 KX Systems, Inc. KX, KDB-X, and kdb+ are registered trademarks of KX Systems, Inc., a subsidiary of KX Software Limited. 

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

![Image 5](https://id.rlcdn.com/464526.gif)

By clicking “Accept All Cookies”, you agree to the storing of cookies on your device to enhance site navigation, analyze site usage, and assist in our marketing efforts.[Cookies Policy.](https://kx.com/cookie-policy/)

Cookies Settings Reject All Accept All

![Image 6: KX Logo](https://cdn-ukwest.onetrust.com/logos/2e246b76-a09f-455a-b12d-cb0cc60b7d47/36d73287-3cef-4657-ad68-1de87d20bcfb/e5b10d3a-3252-4f3a-8f47-e55d701ecfdf/KX-Logo-Black-500x500.png)

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

[![Image 7: Powered by Onetrust](https://cdn-ukwest.onetrust.com/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)
