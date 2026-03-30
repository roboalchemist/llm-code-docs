# Source: https://code.kx.com/kdbai/latest/reference/metrics.html

Title: About KDB.AI similarity metrics - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/reference/metrics.html

Markdown Content:
About KDB.AI similarity metrics - KDB.AI Documentation
===============
- [x] - [x] 

[Skip to content](https://code.kx.com/kdbai/latest/reference/metrics.html#similarity-metrics)

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

 About KDB.AI similarity metrics 

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
    *   - [x]  Similarity Metrics  [Similarity Metrics](https://code.kx.com/kdbai/latest/reference/metrics.html) On this page  
        *   [Euclidean distance: Represented as L2](https://code.kx.com/kdbai/latest/reference/metrics.html#euclidean-distance-represented-as-l2)
        *   [Dot product: Represented as IP](https://code.kx.com/kdbai/latest/reference/metrics.html#dot-product-represented-as-ip)
        *   [Cosine similarity: Represented as CS](https://code.kx.com/kdbai/latest/reference/metrics.html#cosine-similarity-represented-as-cs)

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
*   [Euclidean distance: Represented as L2](https://code.kx.com/kdbai/latest/reference/metrics.html#euclidean-distance-represented-as-l2)
*   [Dot product: Represented as IP](https://code.kx.com/kdbai/latest/reference/metrics.html#dot-product-represented-as-ip)
*   [Cosine similarity: Represented as CS](https://code.kx.com/kdbai/latest/reference/metrics.html#cosine-similarity-represented-as-cs)

Similarity Metrics
==================

_This page contains details on the different similarity metrics available to use with KDB.AI._

If you're already familiar with this topic, you can skip ahead to the [How-to guide](https://code.kx.com/kdbai/latest/use/search.html).

Distance metrics are used to measure similarities among vectors. A number of similarity metrics are available, but you would generally choose the same metric used by your embedding model. Before you create your table, ensure you assign your metric as part of the table schema. Explore the examples below.

KDB.AI supports the following distance metrics:

**Euclidean distance**: Represented as **L2**
---------------------------------------------

![Image 4](https://latex.codecogs.com/svg.latex?{\color{NavyBlue}%20{\fontsize{20}{20}%20\boxed{\|\vec{x}-\vec{y}\|}}})

Euclidean Distance is a measure of the straight-line distance between two points in Euclidean space. In the context of vectors, Euclidean Distance is calculated as the square root of the sum of squared differences between corresponding elements of two vectors. With this metric, both magnitude and direction of vectors are used.

The following **example** uses 
```python
'metric': 'L2'
```
 to assign the euclidean metric to the 
```python
documents
```
 table.

Python 

```py
schema = {'columns': [{'name': 'id', 'pytype': 'str'},
                      {'name': 'vectors',
                        'vectorIndex': {'dims': 8, 'metric': 'L2', 'type': 'flat'}}]}
table = session.create_table('documents',schema)
```

**Dot product**: Represented as **IP**
--------------------------------------

![Image 5](https://latex.codecogs.com/svg.latex?{\color{NavyBlue}%20{\fontsize{20}{20}%20\boxed{\vec{x}%20\cdot%20\vec{y}}})

The Dot Product measures the similarity or alignment between two vectors. It quantifies how much the vectors point in the same direction. For two vectors 
```python
A
```
 and 
```python
B
```
 in n-dimensional space, the Dot Product is calculated as the sum of the products of their corresponding elements.

The Dot Product can be positive (if vectors are aligned in the same direction), negative (if vectors are aligned in opposite directions), or zero (if vectors are orthogonal). With this metric, both magnitude and direction of vectors are used.

The following **example** uses 
```python
'metric': 'IP'
```
 to assign the dot product metric to the 
```python
movies
```
 table.

Python 

```py
schema = {'columns': [{'name': 'id', 'pytype': 'str'},
                      {'name': 'vectors',
                        'vectorIndex': {'dims': 8, 'metric': 'IP', 'type': 'flat'}}]}
table = session.create_table('movies',schema)
```

**Cosine similarity**: Represented as **CS**
--------------------------------------------

![Image 6](https://latex.codecogs.com/svg.latex?{\color{NavyBlue}%20{\fontsize{20}{20}%20\boxed{\frac{\vec{x}%20\cdot%20\vec{y}}{\|\vec{x}\|%20\cdot%20\|%20\vec{y}\|}}})

Cosine Similarity is a metric that measures the cosine of the angle between two vectors. It assesses the similarity in terms of the direction of vectors, rather than their magnitude. Cosine Similarity values range from 
```python
-1
```
 (perfect dissimilarity) to 
```python
1
```
 (perfect similarity), with 
```python
0
```
 indicating orthogonality (perfect non-relation). With this metric, only the direction of vectors is used.

The following **example** uses 
```python
'metric': 'CS'
```
 to assign the cosine similarity metric to the 
```python
imaging
```
 table.

Python 

```py
schema = {'columns': [{'name': 'id', 'pytype': 'str'},
                      {'name': 'vectors',
                        'vectorIndex': {'dims': 8, 'metric': 'CS', 'type': 'flat'}}]}
table = session.create_table('imaging',schema)
```

[Previous Index](https://code.kx.com/kdbai/latest/reference/index.html)[Next Hybrid Search](https://code.kx.com/kdbai/latest/reference/hybrid.html)

 © 2026 KX Systems, Inc. KX, KDB-X, and kdb+ are registered trademarks of KX Systems, Inc., a subsidiary of KX Software Limited. 

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

![Image 7](https://id.rlcdn.com/464526.gif)

By clicking “Accept All Cookies”, you agree to the storing of cookies on your device to enhance site navigation, analyze site usage, and assist in our marketing efforts.[Cookies Policy.](https://kx.com/cookie-policy/)

Cookies Settings Reject All Accept All

![Image 8: KX Logo](https://cdn-ukwest.onetrust.com/logos/2e246b76-a09f-455a-b12d-cb0cc60b7d47/36d73287-3cef-4657-ad68-1de87d20bcfb/e5b10d3a-3252-4f3a-8f47-e55d701ecfdf/KX-Logo-Black-500x500.png)

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

[![Image 9: Powered by Onetrust](https://cdn-ukwest.onetrust.com/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)
