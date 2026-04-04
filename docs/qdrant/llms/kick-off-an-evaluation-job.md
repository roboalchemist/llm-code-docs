# Kick off an evaluation job
experiment_1 = run_eval(eval_df,
                        collection_name=COLLECTION_NAME,
                        recipe_id=recipe_mistral['id'],
                        num_docs=num_docs,
                        path=f"{COLLECTION_NAME}_{num_docs}_mistral.csv")

```

This may take few minutes (depending on the size of evaluation dataset!)

We can look at the results from our first (baseline) experiment as below :

![experiment1_eval.png](https://qdrant.tech/articles_data/rapid-rag-optimization-with-qdrant-and-quotient/experiment1_eval.png)

Notice that we have a pretty **low average Chunk Relevance** and **very large standard deviations for both Chunk Relevance and Context Relevance**.

Let’s take a look at some of the lower performing datapoints with **poor Faithfulness**:

```python
with pd.option_context('display.max_colwidth', 0):
    display(experiment_1[['content.input_text', 'content.answer','content.documents','Chunk Relevance','Context Relevance','Faithfulness']\
                ].sort_values(by='Faithfulness').head(2))

```

![experiment1_bad_examples.png](https://qdrant.tech/articles_data/rapid-rag-optimization-with-qdrant-and-quotient/experiment1_bad_examples.png)

In instances where the retrieved documents are **irrelevant (where both Chunk Relevance and Context Relevance are low)**, the model also shows **tendencies to hallucinate** and **produce poor quality responses**.

The quality of the retrieved text directly impacts the quality of the LLM-generated answer. Therefore, our focus will be on enhancing the RAG setup by **adjusting the chunking parameters**.

### [Anchor](https://qdrant.tech/articles/rapid-rag-optimization-with-qdrant-and-quotient/\#experiment-2---adjusting-the-chunk-parameter) Experiment 2 - Adjusting the chunk parameter

Keeping all other parameters constant, we changed the `chunk size` and `chunk overlap` to see if we can improve our results.

Parameters :

- **Embedding Model : `bge-small-en`**
- **Chunk size: `1024`**
- **Chunk overlap: `128`**
- **Number of docs retrieved (Retireval Window): `3`**
- **LLM: `Mistral-7B-Instruct`**

We will reprocess the data with the updated parameters above:

```python
## for iteration 2 - lets modify chunk configuration
## We will start with creating seperate collection to store vectors

chunk_size = 1024
chunk_overlap = 128
embedding_model_name = "BAAI/bge-small-en"
num_docs = 3

COLLECTION_NAME = f"experiment_{chunk_size}_{chunk_overlap}_{embedding_model_name.split('/')[1]}"

add_documents(client,
              collection_name=COLLECTION_NAME,
              chunk_size=chunk_size,
              chunk_overlap=chunk_overlap,
              embedding_model_name=embedding_model_name)

#Outputs
#processed: 2152
#content:   2152
#metadata:  2152

```

Followed by running evaluation :

![experiment2_eval.png](https://qdrant.tech/articles_data/rapid-rag-optimization-with-qdrant-and-quotient/experiment2_eval.png)

and **comparing it with the results from Experiment 1:**

![graph_exp1_vs_exp2.png](https://qdrant.tech/articles_data/rapid-rag-optimization-with-qdrant-and-quotient/graph_exp1_vs_exp2.png)

We observed slight enhancements in our LLM completion metrics (including BERT Sentence Similarity, BERTScore, ROUGE-L, and Knowledge F1) with the increase in _chunk size_. However, it’s noteworthy that there was a significant decrease in _Faithfulness_, which is the primary metric we are aiming to optimize.

Moreover, _Context Relevance_ demonstrated an increase, indicating that the RAG pipeline retrieved more relevant information required to address the query. Nonetheless, there was a considerable drop in _Chunk Relevance_, implying that a smaller portion of the retrieved documents contained pertinent information for answering the question.

**The correlation between the rise in Context Relevance and the decline in Chunk Relevance suggests that retrieving more documents using the smaller chunk size might yield improved results.**

### [Anchor](https://qdrant.tech/articles/rapid-rag-optimization-with-qdrant-and-quotient/\#experiment-3---increasing-the-number-of-documents-retrieved-retrieval-window) Experiment 3 - Increasing the number of documents retrieved (retrieval window)

This time, we are using the same RAG setup as `Experiment 1`, but increasing the number of retrieved documents from **3** to **5**.

Parameters :

- **Embedding Model : `bge-small-en`**
- **Chunk size: `512`**
- **Chunk overlap: `64`**
- **Number of docs retrieved (Retrieval Window): `5`**
- **LLM: : `Mistral-7B-Instruct`**

We can use the collection from Experiment 1 and run evaluation with modified `num_docs` parameter as :

```python
#collection name from Experiment 1
COLLECTION_NAME = f"experiment_{chunk_size}_{chunk_overlap}_{embedding_model_name.split('/')[1]}"

#running eval for experiment 3
experiment_3 = run_eval(eval_df,
                        collection_name=COLLECTION_NAME,
                        recipe_id=recipe_mistral['id'],
                        num_docs=num_docs,
                        path=f"{COLLECTION_NAME}_{num_docs}_mistral.csv")

```

Observe the results as below :

![experiment_3_eval.png](https://qdrant.tech/articles_data/rapid-rag-optimization-with-qdrant-and-quotient/experiment_3_eval.png)

Comparing the results with Experiment 1 and 2 :

![graph_exp1_exp2_exp3.png](https://qdrant.tech/articles_data/rapid-rag-optimization-with-qdrant-and-quotient/graph_exp1_exp2_exp3.png)

As anticipated, employing the smaller chunk size while retrieving a larger number of documents resulted in achieving the highest levels of both _Context Relevance_ and _Chunk Relevance._ Additionally, it yielded the **best** (albeit marginal) _Faithfulness_ score, indicating a _reduced occurrence of inaccuracies or hallucinations_.

Looks like we have achieved a good hold on our chunking parameters but it is worth testing another embedding model to see if we can get better results.

### [Anchor](https://qdrant.tech/articles/rapid-rag-optimization-with-qdrant-and-quotient/\#experiment-4---changing-the-embedding-model) Experiment 4 - Changing the embedding model

Let us try using **MiniLM** for this experiment
\*\*\*\*Parameters :

- **Embedding Model : `MiniLM-L6-v2`**
- **Chunk size: `512`**
- **Chunk overlap: `64`**
- **Number of docs retrieved (Retrieval Window): `5`**
- **LLM: : `Mistral-7B-Instruct`**

We will have to create another collection for this experiment :

```python
#experiment-4
chunk_size=512
chunk_overlap=64
embedding_model_name="sentence-transformers/all-MiniLM-L6-v2"
num_docs=5

COLLECTION_NAME = f"experiment_{chunk_size}_{chunk_overlap}_{embedding_model_name.split('/')[1]}"

add_documents(client,
              collection_name=COLLECTION_NAME,
              chunk_size=chunk_size,
              chunk_overlap=chunk_overlap,
              embedding_model_name=embedding_model_name)

#Outputs
#processed: 4504
#content:   4504
#metadata:  4504

```

We will observe our evaluations as :

![experiment4_eval.png](https://qdrant.tech/articles_data/rapid-rag-optimization-with-qdrant-and-quotient/experiment4_eval.png)

Comparing these with our previous experiments :

![graph_exp1_exp2_exp3_exp4.png](https://qdrant.tech/articles_data/rapid-rag-optimization-with-qdrant-and-quotient/graph_exp1_exp2_exp3_exp4.png)

It appears that `bge-small` was more proficient in capturing the semantic nuances of the Qdrant Documentation.

Up to this point, our experimentation has focused solely on the _retrieval aspect_ of our RAG pipeline. Now, let’s explore altering the _generation aspect_ or LLM while retaining the optimal parameters identified in Experiment 3.

### [Anchor](https://qdrant.tech/articles/rapid-rag-optimization-with-qdrant-and-quotient/\#experiment-5---changing-the-llm) Experiment 5 - Changing the LLM

Parameters :

- **Embedding Model : `bge-small-en`**
- **Chunk size: `512`**
- **Chunk overlap: `64`**
- **Number of docs retrieved (Retrieval Window): `5`**
- **LLM: : `GPT-3.5-turbo`**

For this we can repurpose our collection from Experiment 3 while the evaluations to use a new recipe with **GPT-3.5-turbo** model.

```python
#collection name from Experiment 3
COLLECTION_NAME = f"experiment_{chunk_size}_{chunk_overlap}_{embedding_model_name.split('/')[1]}"