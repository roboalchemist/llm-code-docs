# Source: https://docs.exa.ai/reference/how-exa-search-works.md

# How Exa Search Works

> Exa is a novel search engine that utilizes the latest advancements in AI language processing to return the best possible results.

***

We offer four search types:

* **Auto (Default)** - Our best search, intelligently combines multiple search methods
* **Fast** - A streamlined implementation for faster results
* **Deep** - Comprehensive search with query expansion and detailed context
* **Neural** - Our AI search model, predicts relevant links based on query meaning

## Neural search via 'next-link prediction'

At Exa, we've built our very own index of high quality web content, and have trained a model to query this index powered by the same embeddings-based technology that makes modern LLMs so powerful.

By using embeddings, we move beyond traditional searches to use 'next-link prediction', understanding the semantic content of queries and indexed documents. This method predicts which web links are most relevant based on the semantic meaning, not just direct word matches.

By doing this, our model anticipates the most relevant links by understanding complex queries, including indirect or thematic relationships. This approach is especially effective for exploratory searches, where precise terms may be unknown, or where queries demand many, often semantically dense, layered filters.

You can query our search model directly with search type `neural`. It is also incorporated into the `auto` and `fast` search types.

## Auto search combines multiple methods

Sometimes traditional search methods are the best way to query the web - for instance, you may have a specific word or piece of jargon that you want to match explicitly with results (often the case with proper nouns like place-names). In these cases, semantic searches alone are not the most useful.

To ensure our engine is comprehensive, we have built multiple search capabilities in parallel to our novel neural search. This means Exa is an 'all-in-one' search solution, no matter what your query needs are.

We surface the best results through search type `auto`, to give users the best of all worlds. It uses a reranker model that understands your query and ranks results from multiple search methods according to relevance.

## Deep search for comprehensive results

Deep search takes a different approach by expanding your query into multiple variations and running parallel searches to find comprehensive results. When you provide a single query, Deep search automatically generates additional query variations to capture different aspects of your search intent. You can also provide your own query variations using the `additionalQueries` parameter for even more control.

Deep search is particularly powerful for research tasks, complex questions, and when you need detailed context about each result. It returns rich context for each result, making it ideal for applications that need to understand the content of web pages in depth.

You can use Deep search by setting `type="deep"` in your search requests. Note that Deep search requires the `context` parameter to be set to `true` in the contents object to return the detailed context for each result.

## Fast search is the world's fastest search API

We built Fast search for when latency matters most. It trades off a small amount of performance for significant speed improvements.

Fast search is best for applications where milliseconds matter. It means a much better user experience for real-time applications like voice agents and autocomplete. It's also great for long running agents, like deep research, that might use hundreds of search calls so the latency adds up.

We achieved these latency improvements by making streamlined versions of our neural and reranker models. You can expect Fast search to run in less than 400 milliseconds, not accounting for network latency or live crawling.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt