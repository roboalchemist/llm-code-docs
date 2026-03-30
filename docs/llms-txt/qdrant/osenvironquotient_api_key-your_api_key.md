# os.environ['QUOTIENT_API_KEY'] = "YOUR_API_KEY"

quotient = QuotientClient()

```

**QuotientAI** provides a seamless way to integrate _RAG evaluation_ into your applications. Here, we’ll see how to use it to evaluate text generated from an LLM, based on retrieved knowledge from the Qdrant vector database.

After retrieving the top similar documents and populating the `context` column, we can submit the evaluation dataset to Quotient and execute an evaluation job. To run a job, all you need is your evaluation dataset and a `recipe`.

_**A recipe is a combination of a prompt template and a specified LLM.**_

**Quotient** orchestrates the evaluation run and handles version control and asset management throughout the experimentation process.

_**Prior to assessing our RAG solution, it’s crucial to outline our optimization goals.**_

In the context of _question-answering on Qdrant documentation_, our focus extends beyond merely providing helpful responses. Ensuring the absence of any _inaccurate or misleading information_ is paramount.

In other words, **we want to minimize hallucinations** in the LLM outputs.

For our evaluation, we will be considering the following metrics, with a focus on **Faithfulness**:

- **Context Relevance**
- **Chunk Relevance**
- **Faithfulness**
- **ROUGE-L**
- **BERT Sentence Similarity**
- **BERTScore**

### [Anchor](https://qdrant.tech/articles/rapid-rag-optimization-with-qdrant-and-quotient/\#evaluation-in-action) Evaluation in action

The function below takes an evaluation dataset as input, which in this case contains questions and their corresponding answers. It retrieves relevant documents based on the questions in the dataset and populates the context field with this information from Qdrant. The prepared dataset is then submitted to QuotientAI for evaluation for the chosen metrics. After the evaluation is complete, the function displays aggregated statistics on the evaluation metrics followed by the summarized evaluation results.

```python
def run_eval(eval_df, collection_name, recipe_id, num_docs=3, path="eval_dataset_qdrant_questions.csv"):
    """
    This function evaluates the performance of a complete RAG pipeline on a given evaluation dataset.

    Given an evaluation dataset (containing questions and ground truth answers),
    this function retrieves relevant documents, populates the context field, and submits the dataset to QuotientAI for evaluation.
    Once the evaluation is complete, aggregated statistics on the evaluation metrics are displayed.

    The evaluation results are returned as a pandas dataframe.
    """

    # Add context to each question by retrieving relevant documents
    eval_df['documents'] = eval_df.apply(lambda x: get_documents(collection_name=collection_name,
                                                                query=x['input_text'],
                                                                num_documents=num_docs), axis=1)
    eval_df['context'] = eval_df.apply(lambda x: "\n".join(x['documents']), axis=1)

    # Now we'll save the eval_df to a CSV
    eval_df.to_csv(path, index=False)

    # Upload the eval dataset to QuotientAI
    dataset = quotient.create_dataset(
        file_path=path,
        name="qdrant-questions-eval-v1",
    )

    # Create a new task for the dataset
    task = quotient.create_task(
        dataset_id=dataset['id'],
        name='qdrant-questions-qa-v1',
        task_type='question_answering'
    )

    # Run a job to evaluate the model
    job = quotient.create_job(
        task_id=task['id'],
        recipe_id=recipe_id,
        num_fewshot_examples=0,
        limit=500,
        metric_ids=[5, 7, 8, 11, 12, 13, 50],
    )

    # Show the progress of the job
    show_job_progress(quotient, job['id'])

    # Once the job is complete, we can get our results
    data = quotient.get_eval_results(job_id=job['id'])

    # Add the results to a pandas dataframe to get statistics on performance
    df = pd.json_normalize(data, "results")
    df_stats = df[df.columns[df.columns.str.contains("metric|completion_time")]]

    df.columns = df.columns.str.replace("metric.", "")
    df_stats.columns = df_stats.columns.str.replace("metric.", "")

    metrics = {
        'completion_time_ms':'Completion Time (ms)',
        'chunk_relevance': 'Chunk Relevance',
        'selfcheckgpt_nli_relevance':"Context Relevance",
        'selfcheckgpt_nli':"Faithfulness",
        'rougeL_fmeasure':"ROUGE-L",
        'bert_score_f1':"BERTScore",
        'bert_sentence_similarity': "BERT Sentence Similarity",
        'completion_verbosity':"Completion Verbosity",
        'verbosity_ratio':"Verbosity Ratio",}

    df = df.rename(columns=metrics)
    df_stats = df_stats.rename(columns=metrics)

    display(df_stats[metrics.values()].describe())

    return df

main_metrics = [\
      'Context Relevance',\
      'Chunk Relevance',\
      'Faithfulness',\
      'ROUGE-L',\
      'BERT Sentence Similarity',\
      'BERTScore',\
      ]

```

## [Anchor](https://qdrant.tech/articles/rapid-rag-optimization-with-qdrant-and-quotient/\#experimentation) Experimentation

Our approach is rooted in the belief that improvement thrives in an environment of exploration and discovery. By systematically testing and tweaking various components of the RAG pipeline, we aim to incrementally enhance its capabilities and performance.

In the following section, we dive into the details of our experimentation process, outlining the specific experiments conducted and the insights gained.

### [Anchor](https://qdrant.tech/articles/rapid-rag-optimization-with-qdrant-and-quotient/\#experiment-1---baseline) Experiment 1 - Baseline

Parameters

- **Embedding Model: `bge-small-en`**
- **Chunk size: `512`**
- **Chunk overlap: `64`**
- **Number of docs retrieved (Retireval Window): `3`**
- **LLM: `Mistral-7B-Instruct`**

We’ll process our documents based on configuration above and ingest them into Qdrant using `add_documents` method introduced earlier

```python
#experiment1 - base config
chunk_size = 512
chunk_overlap = 64
embedding_model_name = "BAAI/bge-small-en"
num_docs = 3

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

Notice the `COLLECTION_NAME` which helps us segregate and identify our collections based on the experiments conducted.

To proceed with the evaluation, let’s create the `evaluation recipe` up next

```python