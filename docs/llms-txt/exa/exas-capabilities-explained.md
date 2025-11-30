# Source: https://docs.exa.ai/reference/exas-capabilities-explained.md

# Exa's Capabilities Explained

> This page explains some of the available feature functionalities of Exa and some unique ways you might use Exa for your use-case

## Search Types

## Auto search (prev. Magic Search)

| Where you would use it                                                                                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| When you want optimal results without manually choosing search methods. When you might not know ahead of time what the best search type is. Note Auto search is the default search type - when unspecified, Auto search is used. |

```Python Python theme={null}
result = exa.search("hottest AI startups", type="auto")
```

## Neural Search

| Description                                                                                                             | Where you would use it                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Uses Exa's embeddings-based index and query model to perform complex queries and provide semantically relevant results. | For exploratory searches or when looking for conceptually related content rather than exact matches. To find hard to find, specific results from the web |

```Python Python theme={null}
result = exa.search("Here is a startup building innovative solutions for climate change:", type="neural")
```

## Fast Search

| Description                                                   | Where you would use it                                                                                                                                                                       |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Streamlined versions of our search models for faster results. | When you need quick search results and speed is more important than comprehensive coverage. Ideal for real-time applications, AI agents, or when you need to make many search calls quickly. |

```Python Python theme={null}
result = exa.search("latest AI news", type="fast")
```

## Deep Search

| Description                                                                     | Where you would use it                                                                                                                                                                  |
| ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Comprehensive search with query expansion and detailed context for each result. | When you need thorough research results with high-quality context. Perfect for complex queries, research tasks, or when you want to explore different aspects of a topic in one search. |

```Python Python theme={null}
result = exa.search_and_contents(
    "blog post about AI", 
    type="deep",
    additional_queries=["AI blogpost", "machine learning blogs"],
    text=True,
    context=True
)
```

## Phrase Filter Search

| Description                                                         | Where you would use it                                                                                                                                                               |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Apply text filters atop of a neural search before returning results | When you want the power of Neural Search but also need to specify and filter on some key phrase. Often helpful when filtering on a piece of jargon where a specific match is crucial |

```Python Python theme={null}
result = exa.search(query, type='neural', includeText='Some_key_phrase_to_fiter_on')
```

[See a worked example here](/examples/niche-company-finder-with-phrase-filters)

## Large-scale Searches

| Description                                                | Where you would use it                                                                                                            |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Exa searches that return a large number of search results. | When desiring comprehensive, semantically relevant data for batch use cases, e.g., for enrichment of CRMs or full topic scraping. |

```Python Python theme={null}
result = exa.search("Companies selling sonar technology", num_results=1000)
```

Note high return results cost more and higher result caps (e.g., 1000 returns) are restricted to Enterprise/Custom plans only. [Get in touch ](https://cal.com/team/exa/exa-intro-chat?date=2024-11-14\&month=2024-11)if you are interested in learning more.

***

## Contents Retrieval

| Description                                                                         | Where you would use it                                                                         |
| ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Instantly retrieves whole, cleaned and parsed webpage contents from search results. | When you need the full text of webpages for analysis, summarization, or other post-processing. |

```Python Python theme={null}
result = exa.search_and_contents("latest advancements in quantum computing", text=True)
```

## Highlights

| Description                                                      | Where you would use it                                                                                                            |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Extracts relevant excerpts or highlights from retrieved content. | When you want a quick or targeted outputs from the most relevant parts of a search entity without wanted to handle the full text. |

```Python Python theme={null}
result = exa.search_and_contents("AI ethics", highlights=True)
```

***

## Prompt Engineering

Prompt engineering is crucial for getting the most out of Exa's capabilities. The right prompt can dramatically improve the relevance and usefulness of your search results. This is especially important for neural search and advanced features like writing continuation.

## Writing continuation queries

| Description                                                                                                                                                                                            | Where you would use it                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Prompt crafted by post-pending 'Here is a great resource to continue writing this piece of writing:'. Useful for research writing or any other citation-based text generation after passing to an LLM. | When you're in the middle of writing a piece and need to find relevant sources to continue or expand your content. This is particularly useful for academic writing, content creation, or any scenario where you need to find information that logically follows from what you've already written. |

```Python Python theme={null}
current_text = """
The impact of climate change on global agriculture has been significant.
Rising temperatures and changing precipitation patterns have led to shifts
in crop yields and growing seasons. Some regions have experienced increased
drought stress, while
"""
continuation_query = current_text + " If you found the above interesting, here's another useful resource to read:"
result = exa.search(continuation_query, type="neural")
```

## Long queries

| Description                                                                             | Where you would use it                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Utilizing Exa's long query window to perform matches against semantically rich content. | When you need to find content that matches complex, detailed descriptions or when you want to find content similar to a large piece of text. This is particularly useful for finding niche content or when you're looking for very specific information. |

```Python Python theme={null}
long_query = """
Abstract: In this study, we investigate the potential of quantum-enhanced machine learning algorithms
for drug discovery applications. We present a novel quantum-classical hybrid approach that leverages
quantum annealing for feature selection and a quantum-inspired tensor network for model training.
Our results demonstrate a 30% improvement in prediction accuracy for binding affinity in protein-ligand
interactions compared to classical machine learning methods. Furthermore, we show a significant
reduction in computational time for large-scale molecular dynamics simulations. These findings
suggest that quantum machine learning techniques could accelerate the drug discovery process
and potentially lead to more efficient identification of promising drug candidates.
"""
result = exa.search(long_query, type="neural")
```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt