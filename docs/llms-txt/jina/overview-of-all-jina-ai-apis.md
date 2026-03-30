# Overview of all Jina AI APIs:
- Embeddings API: Given text, images, or code, generate embeddings.
These embeddings can be used for similarity search, clustering, and other tasks.
- r.reader API: Input a single website URL and get an LLM-friendly version of that single website.
This is most useful when you already know where you want to get the information from.
- s.reader API: Given a search term, get an LLM-friendly version of all websites in the search results.
This is useful when you don't know where to get the information from, but you just know what you are looking for.
The API adheres to the search engine results page (SERP) format.
- Re-Ranker API: Given a query and a list of search results, re-rank them. This is useful for improving the relevance of search results.
- VLM API: A vision-language model for image understanding and multimodal chat.
Best for describing images, visual QA, and multimodal conversations.
- DeepSearch API: Combines web searching, reading, and reasoning for comprehensive investigation
- Segmenter API: Given a text e.g. the output from r.reader or s.reader, split it into segments.
This is useful for breaking down long texts into smaller, more manageable parts.
Usually this is done to get the chunks that are passed to the embeddings API.
- Classification API: Given text or images, classify them into categories.