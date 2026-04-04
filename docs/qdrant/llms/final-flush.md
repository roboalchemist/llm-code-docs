# Final flush
if points_batch:
    client.upsert(collection_name=collection_name, points=points_batch)
    print("Uploaded final batch.")

```

## [Anchor](https://qdrant.tech/documentation/examples/qdrant-dspy-medicalbot/\#retrieval-augmented-generation-rag-pipeline) Retrieval-Augmented Generation (RAG) Pipeline

Our chatbot will use a Retrieval-Augmented Generation (RAG) pipeline to ensure its answers are grounded in medical literature.

### [Anchor](https://qdrant.tech/documentation/examples/qdrant-dspy-medicalbot/\#integration-of-dspy-and-qdrant) Integration of DSPy and Qdrant

At the heart of the application is the Qdrant vector database that provides the information sent to DSPy to generate the final answer. This is what happens when a user submits a query:

- DSPy searches against the Qdrant vector database to retrieve the top documents and answers the query. The results are also filtered with a particular year range for a specific specialty.
- The retrieved passages are then reranked using ColBERT multivector embeddings, leading to the most relevant and contextually appropriate answers.
- DSPy uses these passages to guide the language model through a chain-of-thought reasoning to generate the most accurate answer.

```python
def rerank_with_colbert(query_text, min_year, max_year, specialty):
    from fastembed import TextEmbedding, LateInteractionTextEmbedding

    # Encode query once with both models
    dense_model = TextEmbedding("BAAI/bge-small-en")
    colbert_model = LateInteractionTextEmbedding("colbert-ir/colbertv2.0")

    dense_query = list(dense_model.embed(query_text))[0]
    colbert_query = list(colbert_model.embed(query_text))[0]

    # Combined query: retrieve with dense,
    # rerank with ColBERT
    results = client.query_points(
        collection_name=collection_name,
        prefetch=models.Prefetch(query=dense_query, using="dense"),
        query=colbert_query,
        using="colbert",
        limit=5,
        with_payload=True,
        query_filter=Filter(
            must=[\
                FieldCondition(key="specialty", match=MatchValue(value=specialty)),\
                FieldCondition(\
                    key="year",\
                    range=models.Range(gt=None, gte=min_year, lt=None, lte=max_year),\
                ),\
            ]
        ),
    )

    points = results.points
    docs = []

    for point in points:
        docs.append(point.payload["passage_text"])

    return docs


```

The pipeline ensures that each response is grounded in real and recent medical literature and is aligned with the user’s needs.

## [Anchor](https://qdrant.tech/documentation/examples/qdrant-dspy-medicalbot/\#guardrails-and-medical-question-detection) Guardrails and Medical Question Detection

Since this is a medical chatbot, we can introduce a simple guardrail to ensure it doesn’t respond to unrelated questions like the weather. This can be implemented using a DSPy module.

The chatbot checks if every question is medical-related before attempting to answer it. This is achieved by a DSPy module that classifies each incoming query as medical or not. If the question is not medical-related, the chatbot declines to answer, reducing the risk of misinformation or inappropriate responses.

```python
class MedicalGuardrail(dspy.Module):
    def forward(self, question):
        prompt = (
            """
            Is the following question a medical question?
            Answer with 'Yes' or 'No'.n"
            f"Question: {question}n"
            "Answer:
            """
        )
        response = dspy.settings.lm(prompt)
        answer = response[0].strip().lower()
        return answer.startswith("yes")

if not self.guardrail.forward(question):

    class DummyResult:
        final_answer = """
        Sorry, I can only answer medical questions.
         Please ask a question related to medicine or healthcare
         """

    return DummyResult()

```

By combining this guardrail with specialty and year filtering, we ensure that the chatbot:

- Only answers medical questions.
- Answers questions from recent medical literature.
- Doesn’t make up answers by grounding its answers in the provided literature.

![medicalbot demo](https://qdrant.tech/articles_data/Qdrant-DSPy-medicalbot/medicaldemo.png)

## [Anchor](https://qdrant.tech/documentation/examples/qdrant-dspy-medicalbot/\#conclusion) Conclusion

By leveraging Qdrant and DSPy, you can build a medical chatbot that generates accurate and up-to-date medical responses. Qdrant provides the technology and enables fast and scalable retrieval, while DSPy synthesizes this information to provide correct answers grounded in the medical literature. As a result, you can achieve a medical system that is truthful, safe, and provides relevant responses. Check out the entire project from this [notebook](https://github.com/qdrant/examples/blob/master/DSPy-medical-bot/medical_bot_DSPy_Qdrant.ipynb). You’ll need a free [Qdrant Cloud](https://qdrant.tech/cloud/) account to run the notebook.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/examples/Qdrant-DSPy-medicalbot.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/examples/Qdrant-DSPy-medicalbot.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-133-lllmstxt|>
## beginner-tutorials
- [Documentation](https://qdrant.tech/documentation/)
- Vector Search Basics