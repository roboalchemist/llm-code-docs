# [Anchor](https://qdrant.tech/documentation/search-precision/reranking-semantic-search/\#understanding-reranking) Understanding Reranking

This section is broken down into key parts to help you easily grasp the background, mechanics, and significance of reranking.

## [Anchor](https://qdrant.tech/documentation/search-precision/reranking-semantic-search/\#background) Background

In search systems, two metrics—precision and recall—are the backbone of success. But what do they mean? Precision tells us how many of the retrieved results are actually relevant, while recall measures how well we’ve captured all the relevant results out there. Simply put:

![image5.png](https://qdrant.tech/documentation/examples/reranking-semantic-search/image5.png)

Sparse vector searches usually give you high precision because they’re great at finding exact matches. But, here’s the catch—your recall can suffer when relevant documents don’t contain those exact keywords. On the flip side, dense vector searches are fantastic for recall since they grasp the broader, semantic meaning of your query. However, this can lead to lower precision, where you might see results that are only loosely related.

This is exactly where reranking comes to the rescue. It takes a wide net of documents (giving you high recall) and then refines them by reordering the top candidates based on their relevance scores—boosting precision without losing that broad understanding. Typically, we retain only the top K candidates after reordering to focus on the most relevant results.

## [Anchor](https://qdrant.tech/documentation/search-precision/reranking-semantic-search/\#working) Working

Picture this: You walk into a massive library and ask for a book on “climate change.” The librarian pulls out a dozen books for you—some are scientific papers, others are personal essays, and one’s even a novel. Sure, they’re all relevant, but the first one you get handed is the novel. Not exactly what you were hoping for, right?

Now, imagine a smarter, more intuitive librarian who really gets what you’re after. This one knows exactly which books are most impactful, the most current, and perfectly aligned with what you need. That’s what reranking does for your search results—it doesn’t just grab any relevant document; it smartly reorders them so the best ones land at the top of your list. It’s like having a librarian who knows exactly what you’re looking for before you do!

![image6.png](https://qdrant.tech/documentation/examples/reranking-semantic-search/image6.png)

An illustration of the rerank model prioritizing better results

To become that smart, intuitive librarian, your algorithm needs to learn how to understand both your queries and the documents it retrieves. It has to evaluate the relationship between them effectively, so it can give you exactly what you’re looking for.

The way reranker models operate varies based on their type, which will be discussed later, but in general, they calculate a relevance score for each document-query pair.Unlike embedding models, which squash everything into a single vector upfront, rerankers keep all the important details intact by using the full transformer output to calculate a similarity score. The result? Precision. But, there’s a trade-off—reranking can be slow. Processing millions of documents can take hours, which is why rerankers focus on refining results, not searching through the entire document collection.

Rerankers come in different types, each with its own strengths. Let’s break them down:

1. **Cross Encoder Models**: These boost reranking by using a classification system to evaluate pairs of data—like sentences or documents. They spit out a similarity score from 0 to 1, showing how closely the document matches your query. The catch? Cross-encoders need both query and document, so they can’t handle standalone documents or queries by themselves.
2. **Multi-Vector Rerankers (e.g., ColBERT)**: These models take a more efficient route. They encode your query and the documents separately and only compare them later, reducing the computational load. This means document representations can be precomputed, speeding up retrieval times
3. **Large Language Models (LLMs) as Rerankers**: This is a newer, smarter way to rerank. LLMs, like GPT, are getting better by the day. With the right instructions, they can prioritize the most relevant documents for you, leveraging their massive understanding of language to deliver even more accurate results.

Each of these rerankers has its own special way of making sure you get the best search results, fast and relevant to what you need.

## [Anchor](https://qdrant.tech/documentation/search-precision/reranking-semantic-search/\#importance) Importance

In the previous section, we explored the background and mechanics of reranking, but now let’s talk about the three big wins you get from using it:

- **Enhancing Search Accuracy:** Reranking is all about making your search results sharper and more relevant. After the initial ranking, rerankers step in, reshuffling the results based on deeper analysis to ensure that the most crucial information is front and center. [Research shows that rerankers](https://cohere.com/blog/rerank) can pull off a serious boost—improving the top results for about 72% of search queries. That’s a huge leap in precision.
- **Reducing Information Overload:** If you feel like you’re drowning in a sea of search results, rerankers can come to your rescue. They filter and fine-tune the flood of information so you get exactly what you need, without the overwhelm. It makes your search experience more focused and way less chaotic.
- **Balancing Speed and Relevance:** First stage retrieval and second stage reranking strike the perfect balance between speed and accuracy. Sure, the second stage may add a bit of latency due to their processing power, but the trade-off is worth it. You get highly relevant results, and in the end, that’s what matters most.

Now that you know why reranking is such a game-changer, let’s dive into the practical side of things.