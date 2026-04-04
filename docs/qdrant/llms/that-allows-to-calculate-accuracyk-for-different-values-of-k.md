# That allows to calculate accuracy@k for different values of k.
k_max = 10
answer_positions = []
for embedding, pubid in tqdm(zip(question_response.embeddings, ids)):
    response = qdrant_client.search(
        collection_name="pubmed_qa",
        query_vector=embedding,
        limit=k_max,
    )

    answer_ids = [record.id for record in response]
    if pubid in answer_ids:
        answer_positions.append(answer_ids.index(pubid))
    else:
        answer_positions.append(-1)

```

Saved answer positions allow us to calculate the metric for different _k_ values.

```python