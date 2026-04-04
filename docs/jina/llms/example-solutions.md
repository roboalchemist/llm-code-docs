# Example solutions

1. Basic search:
- For simple queries, use the search API with the given queries;
- For better relevancy, first use the search API to retrieve results, then use the reranker API to find the most relevant results;

2. Classification tasks:
- To classify text snippets (multi-lingual texts), you can use the classification API with jina-embeddings-v3 or jina-embeddings-v4 model;
- To classify images, you can use the classification API with jina-clip-v2 or jina-embeddings-v4 model;

3. Web content processing:
- To scrape a webpage, use the reader API directly;
- To embed the contents of a webpage, first use the reader API to scrape the text content of the webpage and then use the embeddings API;

4. Image understanding tasks:
- To describe or analyze images, use the VLM API with jina-vlm model;
- To answer questions about images (visual QA), use the VLM API with image and text input;
- For multimodal conversations with images, use the VLM API with message history;