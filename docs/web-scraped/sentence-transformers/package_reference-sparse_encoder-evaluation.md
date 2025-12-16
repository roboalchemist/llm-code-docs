# Source: https://www.sbert.net/docs/package_reference/sparse_encoder/evaluation.html

# Evaluation[ïƒ?](#evaluation "Link to this heading")

[`sentence_transformers.sparse_encoder.evaluation`] defines different classes, that can be used to evaluate the SparseEncoder model during training.

## SparseInformationRetrievalEvaluator[ïƒ?](#sparseinformationretrievalevaluator "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.evaluation.]][[SparseInformationRetrievalEvaluator]][(]*[[queries]][[:]][ ][[dict][[\[]][str][[,]][ ][str][[\]]]]*, *[[corpus]][[:]][ ][[dict][[\[]][str][[,]][ ][str][[\]]]]*, *[[relevant_docs]][[:]][ ][[dict][[\[]][str][[,]][ ][set][[\[]][str][[\]]][[\]]]]*, *[[corpus_chunk_size]][[:]][ ][[int]][ ][[=]][ ][[50000]]*, *[[mrr_at_k]][[:]][ ][[list][[\[]][int][[\]]]][ ][[=]][ ][[\[10\]]]*, *[[ndcg_at_k]][[:]][ ][[list][[\[]][int][[\]]]][ ][[=]][ ][[\[10\]]]*, *[[accuracy_at_k]][[:]][ ][[list][[\[]][int][[\]]]][ ][[=]][ ][[\[1,] [3,] [5,] [10\]]]*, *[[precision_recall_at_k]][[:]][ ][[list][[\[]][int][[\]]]][ ][[=]][ ][[\[1,] [3,] [5,] [10\]]]*, *[[map_at_k]][[:]][ ][[list][[\[]][int][[\]]]][ ][[=]][ ][[\[100\]]]*, *[[show_progress_bar]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[name]][[:]][ ][[str]][ ][[=]][ ][[\'\']]*, *[[write_csv]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[max_active_dims]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[score_functions]][[:]][ ][[dict][[\[]][str][[,]][ ][Callable][[\[]][[\[]][[torch.Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[,]][ ][[torch.Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]][[,]][ ][[torch.Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[main_score_function]][[:]][ ][[str][ ][[\|]][ ][[SimilarityFunction]](SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[query_prompt]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[query_prompt_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[corpus_prompt]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[corpus_prompt_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[write_predictions]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\evaluation\SparseInformationRetrievalEvaluator.py#L24-L309)[ïƒ?](#sentence_transformers.sparse_encoder.evaluation.SparseInformationRetrievalEvaluator "Link to this definition")

:   This evaluator extends [[`InformationRetrievalEvaluator`]](../sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator "sentence_transformers.evaluation.InformationRetrievalEvaluator") but is specifically designed for sparse encoder models.

    This class evaluates an Information Retrieval (IR) setting.

    Given a set of queries and a large corpus set. It will retrieve for each query the top-k most similar document. It measures Mean Reciprocal Rank (MRR), Recall@k, and Normalized Discounted Cumulative Gain (NDCG)

    Parameters[:]

    :   - **queries** (*Dict\[str,* *str\]*) â€" A dictionary mapping query IDs to queries.

        - **corpus** (*Dict\[str,* *str\]*) â€" A dictionary mapping document IDs to documents.

        - **relevant_docs** (*Dict\[str,* *Set\[str\]\]*) â€" A dictionary mapping query IDs to a set of relevant document IDs.

        - **corpus_chunk_size** (*int*) â€" The size of each chunk of the corpus. Defaults to 50000.

        - **mrr_at_k** (*List\[int\]*) â€" A list of integers representing the values of k for MRR calculation. Defaults to \[10\].

        - **ndcg_at_k** (*List\[int\]*) â€" A list of integers representing the values of k for NDCG calculation. Defaults to \[10\].

        - **accuracy_at_k** (*List\[int\]*) â€" A list of integers representing the values of k for accuracy calculation. Defaults to \[1, 3, 5, 10\].

        - **precision_recall_at_k** (*List\[int\]*) â€" A list of integers representing the values of k for precision and recall calculation. Defaults to \[1, 3, 5, 10\].

        - **map_at_k** (*List\[int\]*) â€" A list of integers representing the values of k for MAP calculation. Defaults to \[100\].

        - **show_progress_bar** (*bool*) â€" Whether to show a progress bar during evaluation. Defaults to False.

        - **batch_size** (*int*) â€" The batch size for evaluation. Defaults to 32.

        - **name** (*str*) â€" A name for the evaluation. Defaults to â€œâ€?.

        - **write_csv** (*bool*) â€" Whether to write the evaluation results to a CSV file. Defaults to True.

        - **max_active_dims** (*Optional\[int\],* *optional*) â€" The maximum number of active dimensions to use. None uses the modelâ€™s current max_active_dims. Defaults to None.

        - **score_functions** (*Dict\[str,* *Callable\[\[Tensor,* *Tensor\],* *Tensor\]\]*) â€" A dictionary mapping score function names to score functions. Defaults to the [`similarity`] function from the [`model`].

        - **main_score_function** (*Union\[str,* [*SimilarityFunction*](SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")*\],* *optional*) â€" The main score function to use for evaluation. Defaults to None.

        - **query_prompt** (*str,* *optional*) â€" The prompt to be used when encoding the corpus. Defaults to None.

        - **query_prompt_name** (*str,* *optional*) â€" The name of the prompt to be used when encoding the corpus. Defaults to None.

        - **corpus_prompt** (*str,* *optional*) â€" The prompt to be used when encoding the corpus. Defaults to None.

        - **corpus_prompt_name** (*str,* *optional*) â€" The name of the prompt to be used when encoding the corpus. Defaults to None.

        - **write_predictions** (*bool*) â€" Whether to write the predictions to a JSONL file. Defaults to False. This can be useful for downstream evaluation as it can be used as input to the [[`ReciprocalRankFusionEvaluator`]](#sentence_transformers.sparse_encoder.evaluation.ReciprocalRankFusionEvaluator "sentence_transformers.sparse_encoder.evaluation.ReciprocalRankFusionEvaluator") that accept precomputed predictions.

    Example

    :::: 
    ::: highlight
        import logging

        from datasets import load_dataset

        from sentence_transformers import SparseEncoder
        from sentence_transformers.sparse_encoder.evaluation import SparseInformationRetrievalEvaluator

        logging.basicConfig(format="%(message)s", level=logging.INFO)

        # Load a model
        model = SparseEncoder("naver/splade-cocondenser-ensembledistil")

        # Load the NFcorpus IR dataset (https://huggingface.co/datasets/BeIR/nfcorpus, https://huggingface.co/datasets/BeIR/nfcorpus-qrels)
        corpus = load_dataset("BeIR/nfcorpus", "corpus", split="corpus")
        queries = load_dataset("BeIR/nfcorpus", "queries", split="queries")
        relevant_docs_data = load_dataset("BeIR/nfcorpus-qrels", split="test")

        # For this dataset, we want to concatenate the title and texts for the corpus
        corpus = corpus.map(lambda x: , remove_columns=["title"])

        # Convert the datasets to dictionaries
        corpus = dict(zip(corpus["_id"], corpus["text"]))  # Our corpus (cid => document)
        queries = dict(zip(queries["_id"], queries["text"]))  # Our queries (qid => question)
        relevant_docs =   # Query ID to relevant documents (qid => set([relevant_cids])
        for qid, corpus_ids in zip(relevant_docs_data["query-id"], relevant_docs_data["corpus-id"]):
            qid = str(qid)
            corpus_ids = str(corpus_ids)
            if qid not in relevant_docs:
                relevant_docs[qid] = set()
            relevant_docs[qid].add(corpus_ids)

        # Given queries, a corpus and a mapping with relevant documents, the SparseInformationRetrievalEvaluator computes different IR metrics.
        ir_evaluator = SparseInformationRetrievalEvaluator(
            queries=queries,
            corpus=corpus,
            relevant_docs=relevant_docs,
            name="BeIR-nfcorpus-subset-test",
            show_progress_bar=True,
            batch_size=16,
        )

        # Run evaluation
        results = ir_evaluator(model)
        '''
        Queries: 323
        Corpus: 3269

        Score-Function: dot
        Accuracy@1: 49.23%
        Accuracy@3: 63.47%
        Accuracy@5: 66.56%
        Accuracy@10: 71.83%
        Precision@1: 49.23%
        Precision@3: 39.63%
        Precision@5: 33.13%
        Precision@10: 25.23%
        Recall@1: 6.08%
        Recall@3: 11.60%
        Recall@5: 13.47%
        Recall@10: 17.01%
        MRR@10: 0.5706
        NDCG@10: 0.3530
        MAP@100: 0.1778
        Model Query Sparsity: Active Dimensions: 40.0, Sparsity Ratio: 0.9987
        Model Corpus Sparsity: Active Dimensions: 206.2, Sparsity Ratio: 0.9932
        Average FLOPS: 4.66
        '''
        # Print the results
        print(f"Primary metric: ")
        # => Primary metric: BeIR-nfcorpus-subset-test_dot_ndcg@10
        print(f"Primary metric value: ")
        # => Primary metric value: 0.3530
    :::
    ::::

## SparseNanoBEIREvaluator[ïƒ?](#sparsenanobeirevaluator "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.evaluation.]][[SparseNanoBEIREvaluator]][(]*[dataset_names:] [list\[DatasetNameType] [\|] [str\]] [\|] [None] [=] [None,] [dataset_id:] [str] [=] [\'sentence-transformers/NanoBEIR-en\',] [mrr_at_k:] [list\[int\]] [=] [\[10\],] [ndcg_at_k:] [list\[int\]] [=] [\[10\],] [accuracy_at_k:] [list\[int\]] [=] [\[1,] [3,] [5,] [10\],] [precision_recall_at_k:] [list\[int\]] [=] [\[1,] [3,] [5,] [10\],] [map_at_k:] [list\[int\]] [=] [\[100\],] [show_progress_bar:] [bool] [=] [False,] [batch_size:] [int] [=] [32,] [write_csv:] [bool] [=] [True,] [max_active_dims:] [int] [\|] [None] [=] [None,] [score_functions:] [dict\[str,] [Callable\[\[Tensor,] [Tensor\],] [Tensor\]\]] [\|] [None] [=] [None,] [main_score_function:] [str] [\|] [SimilarityFunction] [\|] [None] [=] [None,] [aggregate_fn:] [Callable\[\[list\[float\]\],] [float\]] [=] [\<function] [mean\>,] [aggregate_key:] [str] [=] [\'mean\',] [query_prompts:] [str] [\|] [dict\[str,] [str\]] [\|] [None] [=] [None,] [corpus_prompts:] [str] [\|] [dict\[str,] [str\]] [\|] [None] [=] [None,] [write_predictions:] [bool] [=] [False]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\evaluation\SparseNanoBEIREvaluator.py#L28-L332)[ïƒ?](#sentence_transformers.sparse_encoder.evaluation.SparseNanoBEIREvaluator "Link to this definition")

:   This evaluator extends [[`NanoBEIREvaluator`]](../sentence_transformer/evaluation.html#sentence_transformers.evaluation.NanoBEIREvaluator "sentence_transformers.evaluation.NanoBEIREvaluator") but is specifically designed for sparse encoder models.

    This class evaluates the performance of a SparseEncoder Model on the NanoBEIR collection of Information Retrieval datasets.

    The NanoBEIR collection consists of downsized versions of several BEIR information-retrieval datasets, making it suitable for quickly benchmarking a modelâ€™s retrieval performance before running a full-scale BEIR evaluation. The datasets are available on Hugging Face in the Sentence Transformers [NanoBEIR collection](https://huggingface.co/collections/sentence-transformers/nanobeir-datasets), which reformats the [original collection](https://huggingface.co/collections/zeta-alpha-ai/nanobeir) from Zeta Alpha into the default [NanoBEIR-en](https://huggingface.co/datasets/sentence-transformers/NanoBEIR-en) dataset, alongside many translated versions. This evaluator will return the same metrics as the [[`SparseInformationRetrievalEvaluator`]](#sentence_transformers.sparse_encoder.evaluation.SparseInformationRetrievalEvaluator "sentence_transformers.sparse_encoder.evaluation.SparseInformationRetrievalEvaluator") (i.e., MRR, nDCG, Recall@k, Sparsity, FLOPS), for each dataset and on average.

    Parameters[:]

    :   - **dataset_names** (*List\[str\]*) â€" The short names of the datasets to evaluate on (e.g., â€œclimatefeverâ€?, â€œmsmarcoâ€?). If not specified, all predefined NanoBEIR datasets are used. The full list of available datasets is: â€œclimatefeverâ€?, â€œdbpediaâ€?, â€œfeverâ€?, â€œfiqa2018â€?, â€œhotpotqaâ€?, â€œmsmarcoâ€?, â€œnfcorpusâ€?, â€œnqâ€?, â€œquoraretrievalâ€?, â€œscidocsâ€?, â€œarguanaâ€?, â€œscifactâ€?, and â€œtouche2020â€?.

        - **dataset_id** (*str*) â€" The HuggingFace dataset ID to load the datasets from. Defaults to â€œsentence-transformers/NanoBEIR-enâ€?. The dataset must contain â€œcorpusâ€?, â€œqueriesâ€?, and â€œqrelsâ€? subsets for each NanoBEIR dataset, stored under splits named [`Nano`] (for example, [`NanoMSMARCO`] or [`NanoNFCorpus`]).

        - **mrr_at_k** (*List\[int\]*) â€" A list of integers representing the values of k for MRR calculation. Defaults to \[10\].

        - **ndcg_at_k** (*List\[int\]*) â€" A list of integers representing the values of k for NDCG calculation. Defaults to \[10\].

        - **accuracy_at_k** (*List\[int\]*) â€" A list of integers representing the values of k for accuracy calculation. Defaults to \[1, 3, 5, 10\].

        - **precision_recall_at_k** (*List\[int\]*) â€" A list of integers representing the values of k for precision and recall calculation. Defaults to \[1, 3, 5, 10\].

        - **map_at_k** (*List\[int\]*) â€" A list of integers representing the values of k for MAP calculation. Defaults to \[100\].

        - **show_progress_bar** (*bool*) â€" Whether to show a progress bar during evaluation. Defaults to False.

        - **batch_size** (*int*) â€" The batch size for evaluation. Defaults to 32.

        - **write_csv** (*bool*) â€" Whether to write the evaluation results to a CSV file. Defaults to True.

        - **max_active_dims** (*Optional\[int\],* *optional*) â€" The maximum number of active dimensions to use. None uses the modelâ€™s current max_active_dims. Defaults to None.

        - **score_functions** (*Dict\[str,* *Callable\[\[Tensor,* *Tensor\],* *Tensor\]\]*) â€" A dictionary mapping score function names to score functions. Defaults to .

        - **main_score_function** (*Union\[str,* [*SimilarityFunction*](SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")*\],* *optional*) â€" The main score function to use for evaluation. Defaults to None.

        - **aggregate_fn** (*Callable\[\[list\[float\]\],* *float\]*) â€" The function to aggregate the scores. Defaults to np.mean.

        - **aggregate_key** (*str*) â€" The key to use for the aggregated score. Defaults to â€œmeanâ€?.

        - **query_prompts** (*str* *\|* *dict\[str,* *str\],* *optional*) â€" The prompts to add to the queries. If a string, will add the same prompt to all queries. If a dict, expects that all datasets in dataset_names are keys.

        - **corpus_prompts** (*str* *\|* *dict\[str,* *str\],* *optional*) â€" The prompts to add to the corpus. If a string, will add the same prompt to all corpus. If a dict, expects that all datasets in dataset_names are keys.

        - **write_predictions** (*bool*) â€" Whether to write the predictions to a JSONL file. Defaults to False. This can be useful for downstream evaluation as it can be used as input to the [[`ReciprocalRankFusionEvaluator`]](#sentence_transformers.sparse_encoder.evaluation.ReciprocalRankFusionEvaluator "sentence_transformers.sparse_encoder.evaluation.ReciprocalRankFusionEvaluator") that accept precomputed predictions.

    ::: 
    Tip

    See this [NanoBEIR datasets collection on Hugging Face](https://huggingface.co/collections/sentence-transformers/nanobeir-datasets) with valid NanoBEIR [`dataset_id`] options for different languages.
    :::

    Example

    :::: 
    ::: highlight
        import logging

        from sentence_transformers import SparseEncoder
        from sentence_transformers.sparse_encoder.evaluation import SparseNanoBEIREvaluator

        logging.basicConfig(format="%(message)s", level=logging.INFO)

        # Load a model
        model = SparseEncoder("naver/splade-cocondenser-ensembledistil")

        datasets = ["QuoraRetrieval", "MSMARCO"]

        evaluator = SparseNanoBEIREvaluator(
            dataset_names=datasets,
            show_progress_bar=True,
            batch_size=32,
        )

        # Run evaluation
        results = evaluator(model)
        '''
        Evaluating NanoQuoraRetrieval
        Information Retrieval Evaluation of the model on the NanoQuoraRetrieval dataset:
        Queries: 50
        Corpus: 5046

        Score-Function: dot
        Accuracy@1: 92.00%
        Accuracy@3: 96.00%
        Accuracy@5: 98.00%
        Accuracy@10: 100.00%
        Precision@1: 92.00%
        Precision@3: 40.00%
        Precision@5: 24.80%
        Precision@10: 13.20%
        Recall@1: 79.73%
        Recall@3: 92.53%
        Recall@5: 94.93%
        Recall@10: 98.27%
        MRR@10: 0.9439
        NDCG@10: 0.9339
        MAP@100: 0.9070
        Model Query Sparsity: Active Dimensions: 59.4, Sparsity Ratio: 0.9981
        Model Corpus Sparsity: Active Dimensions: 61.9, Sparsity Ratio: 0.9980
        Average FLOPS: 4.10

        Information Retrieval Evaluation of the model on the NanoMSMARCO dataset:
        Queries: 50
        Corpus: 5043

        Score-Function: dot
        Accuracy@1: 48.00%
        Accuracy@3: 74.00%
        Accuracy@5: 76.00%
        Accuracy@10: 86.00%
        Precision@1: 48.00%
        Precision@3: 24.67%
        Precision@5: 15.20%
        Precision@10: 8.60%
        Recall@1: 48.00%
        Recall@3: 74.00%
        Recall@5: 76.00%
        Recall@10: 86.00%
        MRR@10: 0.6191
        NDCG@10: 0.6780
        MAP@100: 0.6277
        Model Query Sparsity: Active Dimensions: 45.4, Sparsity Ratio: 0.9985
        Model Corpus Sparsity: Active Dimensions: 122.6, Sparsity Ratio: 0.9960
        Average FLOPS: 2.41

        Average Queries: 50.0
        Average Corpus: 5044.5
        Aggregated for Score Function: dot
        Accuracy@1: 70.00%
        Accuracy@3: 85.00%
        Accuracy@5: 87.00%
        Accuracy@10: 93.00%
        Precision@1: 70.00%
        Recall@1: 63.87%
        Precision@3: 32.33%
        Recall@3: 83.27%
        Precision@5: 20.00%
        Recall@5: 85.47%
        Precision@10: 10.90%
        Recall@10: 92.13%
        MRR@10: 0.7815
        NDCG@10: 0.8060
        MAP@100: 0.7674
        Model Query Sparsity: Active Dimensions: 52.4, Sparsity Ratio: 0.9983
        Model Corpus Sparsity: Active Dimensions: 92.2, Sparsity Ratio: 0.9970
        Average FLOPS: 2.59
        '''
        # Print the results
        print(f"Primary metric: ")
        # => Primary metric: NanoBEIR_mean_dot_ndcg@10
        print(f"Primary metric value: ")
        # => Primary metric value: 0.8060
    :::
    ::::

    Evaluating on custom/translated datasets:

    :::: 
    ::: highlight
        import logging
        from pprint import pprint

        from sentence_transformers import SparseEncoder
        from sentence_transformers.sparse_encoder.evaluation import SparseNanoBEIREvaluator

        logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=logging.INFO)

        model = SparseEncoder("opensearch-project/opensearch-neural-sparse-encoding-multilingual-v1")
        evaluator = SparseNanoBEIREvaluator(
            dataset_names=["msmarco", "nq"],
            dataset_id="lightonai/NanoBEIR-de",
            batch_size=32,
        )
        results = evaluator(model)
        print(results[evaluator.primary_metric])
        pprint()
    :::
    ::::

## SparseEmbeddingSimilarityEvaluator[ïƒ?](#sparseembeddingsimilarityevaluator "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.evaluation.]][[SparseEmbeddingSimilarityEvaluator]][(]*[[sentences1]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[sentences2]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[scores]][[:]][ ][[list][[\[]][float][[\]]]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[16]]*, *[[main_similarity]][[:]][ ][[str][ ][[\|]][ ][[SimilarityFunction]](SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[similarity_fn_names]][[:]][ ][[list][[\[]][Literal][[\[]][[\'cosine\']][[,]][ ][[\'euclidean\']][[,]][ ][[\'manhattan\']][[,]][ ][[\'dot\']][[\]]][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[name]][[:]][ ][[str]][ ][[=]][ ][[\'\']]*, *[[show_progress_bar]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[write_csv]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[max_active_dims]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\evaluation\SparseEmbeddingSimilarityEvaluator.py#L22-L168)[ïƒ?](#sentence_transformers.sparse_encoder.evaluation.SparseEmbeddingSimilarityEvaluator "Link to this definition")

:   This evaluator extends [[`EmbeddingSimilarityEvaluator`]](../sentence_transformer/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator "sentence_transformers.evaluation.EmbeddingSimilarityEvaluator") but is specifically designed for sparse encoder models.

    Evaluate a model based on the similarity of the embeddings by calculating the Spearman and Pearson rank correlation in comparison to the gold standard labels. The metrics are the cosine similarity as well as euclidean and Manhattan distance The returned score is the Spearman correlation with a specified metric.

    Parameters[:]

    :   - **sentences1** (*List\[str\]*) â€" List with the first sentence in a pair.

        - **sentences2** (*List\[str\]*) â€" List with the second sentence in a pair.

        - **scores** (*List\[float\]*) â€" Similarity score between sentences1\[i\] and sentences2\[i\].

        - **batch_size** (*int,* *optional*) â€" The batch size for processing the sentences. Defaults to 16.

        - **main_similarity** (*Optional\[Union\[str,* [*SimilarityFunction*](SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")*\]\],* *optional*) â€" The main similarity function to use. Can be a string (e.g. â€œcosineâ€?, â€œdotâ€?) or a SimilarityFunction object. Defaults to None.

        - **similarity_fn_names** (*List\[str\],* *optional*) â€" List of similarity function names to use. If None, the [`similarity_fn_name`] attribute of the model is used. Defaults to None.

        - **name** (*str,* *optional*) â€" The name of the evaluator. Defaults to â€œâ€?.

        - **show_progress_bar** (*bool,* *optional*) â€" Whether to show a progress bar during evaluation. Defaults to False.

        - **write_csv** (*bool,* *optional*) â€" Whether to write the evaluation results to a CSV file. Defaults to True.

        - **max_active_dims** (*Optional\[int\],* *optional*) â€" The maximum number of active dimensions to use. None uses the modelâ€™s current max_active_dims. Defaults to None.

    Example

    :::: 
    ::: highlight
        import logging

        from datasets import load_dataset

        from sentence_transformers import SparseEncoder, SimilarityFunction
        from sentence_transformers.sparse_encoder.evaluation import SparseEmbeddingSimilarityEvaluator

        logging.basicConfig(format="%(message)s", level=logging.INFO)

        # Load a model
        model = SparseEncoder("naver/splade-cocondenser-ensembledistil")

        # Load the STSB dataset (https://huggingface.co/datasets/sentence-transformers/stsb)
        eval_dataset = load_dataset("sentence-transformers/stsb", split="validation")

        # Initialize the evaluator
        dev_evaluator = SparseEmbeddingSimilarityEvaluator(
            sentences1=eval_dataset["sentence1"],
            sentences2=eval_dataset["sentence2"],
            scores=eval_dataset["score"],
            main_similarity=SimilarityFunction.COSINE, # even though the model is trained with dot, we need to set it to cosine for evaluation as the score in the dataset is cosine similarity
            name="sts_dev",
        )
        results = dev_evaluator(model)
        '''
        EmbeddingSimilarityEvaluator: Evaluating the model on the sts_dev dataset:
        Cosine-Similarity:      Pearson: 0.8429 Spearman: 0.8366
        Model Sparsity: Active Dimensions: 78.3, Sparsity Ratio: 0.9974
        '''
        # Print the results
        print(f"Primary metric: ")
        # => Primary metric: sts_dev_spearman_cosine
        print(f"Primary metric value: ")
        # => Primary metric value: 0.8366
    :::
    ::::

## SparseBinaryClassificationEvaluator[ïƒ?](#sparsebinaryclassificationevaluator "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.evaluation.]][[SparseBinaryClassificationEvaluator]][(]*[[sentences1]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[sentences2]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[labels]][[:]][ ][[list][[\[]][int][[\]]]]*, *[[name]][[:]][ ][[str]][ ][[=]][ ][[\'\']]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[show_progress_bar]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[write_csv]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[max_active_dims]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[similarity_fn_names]][[:]][ ][[list][[\[]][Literal][[\[]][[\'cosine\']][[,]][ ][[\'dot\']][[,]][ ][[\'euclidean\']][[,]][ ][[\'manhattan\']][[\]]][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\evaluation\SparseBinaryClassificationEvaluator.py#L21-L193)[ïƒ?](#sentence_transformers.sparse_encoder.evaluation.SparseBinaryClassificationEvaluator "Link to this definition")

:   This evaluator extends [[`BinaryClassificationEvaluator`]](../sentence_transformer/evaluation.html#sentence_transformers.evaluation.BinaryClassificationEvaluator "sentence_transformers.evaluation.BinaryClassificationEvaluator") but is specifically designed for sparse encoder models.

    Evaluate a model based on the similarity of the embeddings by calculating the accuracy of identifying similar and dissimilar sentences. The metrics are the cosine similarity, dot score, Euclidean and Manhattan distance The returned score is the accuracy with a specified metric.

    The results are written in a CSV. If a CSV already exists, then values are appended.

    The labels need to be 0 for dissimilar pairs and 1 for similar pairs.

    Parameters[:]

    :   - **sentences1** (*List\[str\]*) â€" The first column of sentences.

        - **sentences2** (*List\[str\]*) â€" The second column of sentences.

        - **labels** (*List\[int\]*) â€" labels\[i\] is the label for the pair (sentences1\[i\], sentences2\[i\]). Must be 0 or 1.

        - **name** (*str,* *optional*) â€" Name for the output. Defaults to â€œâ€?.

        - **batch_size** (*int,* *optional*) â€" Batch size used to compute embeddings. Defaults to 32.

        - **show_progress_bar** (*bool,* *optional*) â€" If true, prints a progress bar. Defaults to False.

        - **write_csv** (*bool,* *optional*) â€" Write results to a CSV file. Defaults to True.

        - **max_active_dims** (*Optional\[int\],* *optional*) â€" The maximum number of active dimensions to use. None uses the modelâ€™s current max_active_dims. Defaults to None.

        - **similarity_fn_names** (*Optional\[List\[Literal\[\"cosine\",* *\"dot\",* *\"euclidean\",* *\"manhattan\"\]\]\],* *optional*) â€" The similarity functions to use. If not specified, defaults to the [`similarity_fn_name`] attribute of the model. Defaults to None.

    Example

    :::: 
    ::: highlight
        import logging

        from datasets import load_dataset

        from sentence_transformers import SparseEncoder
        from sentence_transformers.sparse_encoder.evaluation import SparseBinaryClassificationEvaluator

        logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=logging.INFO)

        # Initialize the SPLADE model
        model = SparseEncoder("naver/splade-cocondenser-ensembledistil")

        # Load a dataset with two text columns and a class label column (https://huggingface.co/datasets/sentence-transformers/quora-duplicates)
        eval_dataset = load_dataset("sentence-transformers/quora-duplicates", "pair-class", split="train[-1000:]")

        # Initialize the evaluator
        binary_acc_evaluator = SparseBinaryClassificationEvaluator(
            sentences1=eval_dataset["sentence1"],
            sentences2=eval_dataset["sentence2"],
            labels=eval_dataset["label"],
            name="quora_duplicates_dev",
            show_progress_bar=True,
            similarity_fn_names=["cosine", "dot", "euclidean", "manhattan"],
        )
        results = binary_acc_evaluator(model)
        '''
        Accuracy with Cosine-Similarity:             75.00      (Threshold: 0.8668)
        F1 with Cosine-Similarity:                   67.22      (Threshold: 0.5974)
        Precision with Cosine-Similarity:            54.18
        Recall with Cosine-Similarity:               88.51
        Average Precision with Cosine-Similarity:    67.81
        Matthews Correlation with Cosine-Similarity: 49.56

        Accuracy with Dot-Product:             76.50    (Threshold: 23.4236)
        F1 with Dot-Product:                   67.00    (Threshold: 19.0095)
        Precision with Dot-Product:            55.93
        Recall with Dot-Product:               83.54
        Average Precision with Dot-Product:    65.89
        Matthews Correlation with Dot-Product: 48.88

        Accuracy with Euclidean-Distance:             67.70     (Threshold: -10.0041)
        F1 with Euclidean-Distance:                   48.60     (Threshold: -0.1876)
        Precision with Euclidean-Distance:            32.13
        Recall with Euclidean-Distance:               99.69
        Average Precision with Euclidean-Distance:    20.52
        Matthews Correlation with Euclidean-Distance: -4.59

        Accuracy with Manhattan-Distance:             67.70     (Threshold: -103.0263)
        F1 with Manhattan-Distance:                   48.60     (Threshold: -0.8532)
        Precision with Manhattan-Distance:            32.13
        Recall with Manhattan-Distance:               99.69
        Average Precision with Manhattan-Distance:    21.05
        Matthews Correlation with Manhattan-Distance: -4.59

        Model Sparsity: Active Dimensions: 61.2, Sparsity Ratio: 0.9980
        '''
        # Print the results
        print(f"Primary metric: ")
        # => Primary metric: quora_duplicates_dev_max_ap
        print(f"Primary metric value: ")
        # => Primary metric value: 0.6781
    :::
    ::::

## SparseTripletEvaluator[ïƒ?](#sparsetripletevaluator "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.evaluation.]][[SparseTripletEvaluator]][(]*[[anchors]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[positives]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[negatives]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[main_similarity_function]][[:]][ ][[str][ ][[\|]][ ][[SimilarityFunction]](SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[margin]][[:]][ ][[float][ ][[\|]][ ][dict][[\[]][str][[,]][ ][float][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[name]][[:]][ ][[str]][ ][[=]][ ][[\'\']]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[16]]*, *[[show_progress_bar]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[write_csv]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[max_active_dims]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[similarity_fn_names]][[:]][ ][[list][[\[]][Literal][[\[]][[\'cosine\']][[,]][ ][[\'dot\']][[,]][ ][[\'euclidean\']][[,]][ ][[\'manhattan\']][[\]]][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[main_distance_function]][[:]][ ][[str][ ][[\|]][ ][[SimilarityFunction]](SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")[ ][[\|]][ ][None]][ ][[=]][ ][[\'deprecated\']]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\evaluation\SparseTripletEvaluator.py#L23-L191)[ïƒ?](#sentence_transformers.sparse_encoder.evaluation.SparseTripletEvaluator "Link to this definition")

:   This evaluator extends [[`TripletEvaluator`]](../sentence_transformer/evaluation.html#sentence_transformers.evaluation.TripletEvaluator "sentence_transformers.evaluation.TripletEvaluator") but is specifically designed for sparse encoder models.

    Evaluate a model based on a triplet: (sentence, positive_example, negative_example). Checks if [`similarity(sentence,`]` `[`positive_example)`]` `[`<`]` `[`similarity(sentence,`]` `[`negative_example)`]` `[`+`]` `[`margin`].

    Parameters[:]

    :   - **anchors** (*List\[str\]*) â€" Sentences to check similarity to. (e.g. a query)

        - **positives** (*List\[str\]*) â€" List of positive sentences

        - **negatives** (*List\[str\]*) â€" List of negative sentences

        - **main_similarity_function** (*Union\[str,* [*SimilarityFunction*](SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")*\],* *optional*) â€" The similarity function to use. If not specified, use cosine similarity, dot product, Euclidean, and Manhattan similarity. Defaults to None.

        - **margin** (*Union\[float,* *Dict\[str,* *float\]\],* *optional*) â€" Margins for various similarity metrics. If a float is provided, it will be used as the margin for all similarity metrics. If a dictionary is provided, the keys should be â€˜cosineâ€™, â€˜dotâ€™, â€˜manhattanâ€™, and â€˜euclideanâ€™. The value specifies the minimum margin by which the negative sample should be further from the anchor than the positive sample. Defaults to None.

        - **name** (*str*) â€" Name for the output. Defaults to â€œâ€?.

        - **batch_size** (*int*) â€" Batch size used to compute embeddings. Defaults to 16.

        - **show_progress_bar** (*bool*) â€" If true, prints a progress bar. Defaults to False.

        - **write_csv** (*bool*) â€" Write results to a CSV file. Defaults to True.

        - **max_active_dims** (*Optional\[int\],* *optional*) â€" The maximum number of active dimensions to use. None uses the modelâ€™s current max_active_dims. Defaults to None.

        - **similarity_fn_names** (*List\[str\],* *optional*) â€" List of similarity function names to evaluate. If not specified, evaluate using the [`model.similarity_fn_name`]. Defaults to None.

    Example

    :::: 
    ::: highlight
        import logging

        from datasets import load_dataset

        from sentence_transformers import SparseEncoder
        from sentence_transformers.sparse_encoder.evaluation import SparseTripletEvaluator

        logging.basicConfig(format="%(message)s", level=logging.INFO)

        # Load a model
        model = SparseEncoder("naver/splade-cocondenser-ensembledistil")

        # Load triplets from the AllNLI dataset
        # The dataset contains triplets of (anchor, positive, negative) sentences
        dataset = load_dataset("sentence-transformers/all-nli", "triplet", split="dev[:1000]")

        # Initialize the SparseTripletEvaluator
        evaluator = SparseTripletEvaluator(
            anchors=dataset[:1000]["anchor"],
            positives=dataset[:1000]["positive"],
            negatives=dataset[:1000]["negative"],
            name="all_nli_dev",
            batch_size=32,
            show_progress_bar=True,
        )

        # Run the evaluation
        results = evaluator(model)
        '''
        TripletEvaluator: Evaluating the model on the all_nli_dev dataset:
        Accuracy Dot Similarity:        85.40%
        Model Anchor Sparsity: Active Dimensions: 103.0, Sparsity Ratio: 0.9966
        Model Positive Sparsity: Active Dimensions: 67.4, Sparsity Ratio: 0.9978
        Model Negative Sparsity: Active Dimensions: 65.9, Sparsity Ratio: 0.9978
        '''
        # Print the results
        print(f"Primary metric: ")
        # => Primary metric: all_nli_dev_dot_accuracy
        print(f"Primary metric value: ")
        # => Primary metric value: 0.8540
    :::
    ::::

## SparseRerankingEvaluator[ïƒ?](#sparsererankingevaluator "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.evaluation.]][[SparseRerankingEvaluator]][(]*[samples:] [list\[dict\[str,] [str] [\|] [list\[str\]\]\],] [at_k:] [int] [=] [10,] [name:] [str] [=] [\'\',] [write_csv:] [bool] [=] [True,] [similarity_fct:] [\~collections.abc.Callable\[\[\~torch.Tensor,] [\~torch.Tensor\],] [\~torch.Tensor\]] [=] [\<function] [cos_sim\>,] [batch_size:] [int] [=] [64,] [show_progress_bar:] [bool] [=] [False,] [use_batched_encoding:] [bool] [=] [True,] [max_active_dims:] [int] [\|] [None] [=] [None,] [mrr_at_k:] [int] [\|] [None] [=] [None]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\evaluation\SparseRerankingEvaluator.py#L22-L212)[ïƒ?](#sentence_transformers.sparse_encoder.evaluation.SparseRerankingEvaluator "Link to this definition")

:   This evaluator extends :class:[[\`]](#id1)\~sentence_transformers.evaluation.RerankingEvaluatorâ€™ but is specifically designed for sparse encoder models.

    This class evaluates a SparseEncoder model for the task of re-ranking.

    Given a query and a list of documents, it computes the score \[query, doc_i\] for all possible documents and sorts them in decreasing order. Then, [MRR@10](/cdn-cgi/l/email-protection#fbb6a9a9ddd8c8ccc0ddd8cec9c0ddd8cfc3c0cacb), [NDCG@10](/cdn-cgi/l/email-protection#1b555f585c3d38282c203d382e29203d382f23202a2b) and MAP is compute to measure the quality of the ranking.

    Parameters[:]

    :   - **samples** (*list*) â€"

          A list of dictionaries, where each dictionary represents a sample and has the following keys:

          - â€™queryâ€™: The search query.

          - â€™positiveâ€™: A list of positive (relevant) documents.

          - â€™negativeâ€™: A list of negative (irrelevant) documents.

        - **at_k** (*int,* *optional*) â€" Only consider the top k most similar documents to each query for the evaluation. Defaults to 10.

        - **name** (*str,* *optional*) â€" Name of the evaluator. Defaults to â€œâ€?.

        - **write_csv** (*bool,* *optional*) â€" Write results to CSV file. Defaults to True.

        - **similarity_fct** (*Callable\[\[*[*torch.Tensor*](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")*,* [*torch.Tensor*](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")*\],* [*torch.Tensor*](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")*\],* *optional*) â€" Similarity function between sentence embeddings. By default, cosine similarity. Defaults to cos_sim.

        - **batch_size** (*int,* *optional*) â€" Batch size to compute sentence embeddings. Defaults to 64.

        - **show_progress_bar** (*bool,* *optional*) â€" Show progress bar when computing embeddings. Defaults to False.

        - **use_batched_encoding** (*bool,* *optional*) â€" Whether or not to encode queries and documents in batches for greater speed, or 1-by-1 to save memory. Defaults to True.

        - **max_active_dims** (*Optional\[int\],* *optional*) â€" The maximum number of active dimensions to use. None uses the modelâ€™s current max_active_dims. Defaults to None.

        - **mrr_at_k** (*Optional\[int\],* *optional*) â€" Deprecated parameter. Please use at_k instead. Defaults to None.

    Example

    :::: 
    ::: highlight
        import logging

        from datasets import load_dataset

        from sentence_transformers import SparseEncoder
        from sentence_transformers.sparse_encoder.evaluation import SparseRerankingEvaluator

        logging.basicConfig(format="%(message)s", level=logging.INFO)

        # Load a model
        model = SparseEncoder("naver/splade-cocondenser-ensembledistil")

        # Load a dataset with queries, positives, and negatives
        eval_dataset = load_dataset("microsoft/ms_marco", "v1.1", split="validation").select(range(1000))

        samples = [
            
            for sample in eval_dataset
        ]

        # Now evaluate using only the documents from the 1000 samples
        reranking_evaluator = SparseRerankingEvaluator(
            samples=samples,
            name="ms-marco-dev-small",
            show_progress_bar=True,
            batch_size=32,
        )

        results = reranking_evaluator(model)
        '''
        RerankingEvaluator: Evaluating the model on the ms-marco-dev-small dataset:
        Queries: 967         Positives: Min 1.0, Mean 1.1, Max 3.0   Negatives: Min 1.0, Mean 7.1, Max 9.0
        MAP: 53.41
        MRR@10: 54.14
        NDCG@10: 65.06
        Model Query Sparsity: Active Dimensions: 42.2, Sparsity Ratio: 0.9986
        Model Corpus Sparsity: Active Dimensions: 126.5, Sparsity Ratio: 0.9959
        '''
        # Print the results
        print(f"Primary metric: ")
        # => Primary metric: ms-marco-dev-small_ndcg@10
        print(f"Primary metric value: ")
        # => Primary metric value: 0.6506
    :::
    ::::

## SparseTranslationEvaluator[ïƒ?](#sparsetranslationevaluator "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.evaluation.]][[SparseTranslationEvaluator]][(]*[[source_sentences]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[target_sentences]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[show_progress_bar]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[16]]*, *[[name]][[:]][ ][[str]][ ][[=]][ ][[\'\']]*, *[[print_wrong_matches]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[write_csv]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[max_active_dims]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\evaluation\SparseTranslationEvaluator.py#L23-L158)[ïƒ?](#sentence_transformers.sparse_encoder.evaluation.SparseTranslationEvaluator "Link to this definition")

:   This evaluator extends [[`TranslationEvaluator`]](../sentence_transformer/evaluation.html#sentence_transformers.evaluation.TranslationEvaluator "sentence_transformers.evaluation.TranslationEvaluator") but is specifically designed for sparse encoder models.

    Given two sets of sentences in different languages, e.g. (en_1, en_2, en_3â€¦) and (fr_1, fr_2, fr_3, â€¦), and assuming that fr_i is the translation of en_i. Checks if vec(en_i) has the highest similarity to vec(fr_i). Computes the accuracy in both directions

    The labels need to indicate the similarity between the sentences.

    Parameters[:]

    :   - **source_sentences** (*List\[str\]*) â€" List of sentences in the source language.

        - **target_sentences** (*List\[str\]*) â€" List of sentences in the target language.

        - **show_progress_bar** (*bool*) â€" Whether to show a progress bar when computing embeddings. Defaults to False.

        - **batch_size** (*int*) â€" The batch size to compute sentence embeddings. Defaults to 16.

        - **name** (*str*) â€" The name of the evaluator. Defaults to an empty string.

        - **print_wrong_matches** (*bool*) â€" Whether to print incorrect matches. Defaults to False.

        - **write_csv** (*bool*) â€" Whether to write the evaluation results to a CSV file. Defaults to True.

        - **max_active_dims** (*Optional\[int\],* *optional*) â€" The maximum number of active dimensions to use. None uses the modelâ€™s current max_active_dims. Defaults to None.

    Example

    :::: 
    ::: highlight
        import logging

        from datasets import load_dataset

        from sentence_transformers import SparseEncoder
        from sentence_transformers.sparse_encoder.evaluation import SparseTranslationEvaluator

        logging.basicConfig(format="%(message)s", level=logging.INFO)

        # Load a model, not mutilingual but hope to see some on the hub soon
        model = SparseEncoder("naver/splade-cocondenser-ensembledistil")

        # Load a parallel sentences dataset
        dataset = load_dataset("sentence-transformers/parallel-sentences-news-commentary", "en-nl", split="train[:1000]")

        # Initialize the TranslationEvaluator using the same texts from two languages
        translation_evaluator = SparseTranslationEvaluator(
            source_sentences=dataset["english"],
            target_sentences=dataset["non_english"],
            name="news-commentary-en-nl",
        )
        results = translation_evaluator(model)
        '''
        Evaluating translation matching Accuracy of the model on the news-commentary-en-nl dataset:
        Accuracy src2trg: 41.40
        Accuracy trg2src: 47.60
        Model Sparsity: Active Dimensions: 112.3, Sparsity Ratio: 0.9963
        '''
        # Print the results
        print(f"Primary metric: ")
        # => Primary metric: news-commentary-en-nl_mean_accuracy
        print(f"Primary metric value: ")
        # => Primary metric value: 0.4450
    :::
    ::::

## SparseMSEEvaluator[ïƒ?](#sparsemseevaluator "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.evaluation.]][[SparseMSEEvaluator]][(]*[[source_sentences]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[target_sentences]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[teacher_model]][[=]][[None]]*, *[[show_progress_bar]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[name]][[:]][ ][[str]][ ][[=]][ ][[\'\']]*, *[[write_csv]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[max_active_dims]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\evaluation\SparseMSEEvaluator.py#L20-L170)[ïƒ?](#sentence_transformers.sparse_encoder.evaluation.SparseMSEEvaluator "Link to this definition")

:   This evaluator extends [[`MSEEvaluator`]](../sentence_transformer/evaluation.html#sentence_transformers.evaluation.MSEEvaluator "sentence_transformers.evaluation.MSEEvaluator") but is specifically designed for sparse encoder models.

    Note that this evaluator doesnâ€™t take benefit of the sparse tensor torch representation yet, so memory issues may occur.

    Computes the mean squared error (x100) between the computed sentence embedding and some target sentence embedding.

    The MSE is computed between [`||teacher.encode(source_sentences)`]` `[`-`]` `[`student.encode(target_sentences)||`].

    For multilingual knowledge distillation ([https://huggingface.co/papers/2004.09813](https://huggingface.co/papers/2004.09813)), source_sentences are in English and target_sentences are in a different language like German, Chinese, Spanishâ€¦

    Parameters[:]

    :   - **source_sentences** (*List\[str\]*) â€" Source sentences to embed with the teacher model.

        - **target_sentences** (*List\[str\]*) â€" Target sentences to embed with the student model.

        - **teacher_model** ([*SparseEncoder*](SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder")*,* *optional*) â€" The teacher model to compute the source sentence embeddings.

        - **show_progress_bar** (*bool,* *optional*) â€" Show progress bar when computing embeddings. Defaults to False.

        - **batch_size** (*int,* *optional*) â€" Batch size to compute sentence embeddings. Defaults to 32.

        - **name** (*str,* *optional*) â€" Name of the evaluator. Defaults to â€œâ€?.

        - **write_csv** (*bool,* *optional*) â€" Write results to CSV file. Defaults to True.

        - **max_active_dims** (*Optional\[int\],* *optional*) â€" The maximum number of active dimensions to use. None uses the modelâ€™s current max_active_dims. Defaults to None.

    Example

    :::: 
    ::: highlight
        import logging

        from datasets import load_dataset

        from sentence_transformers import SparseEncoder
        from sentence_transformers.sparse_encoder.evaluation import SparseMSEEvaluator

        logging.basicConfig(format="%(message)s", level=logging.INFO)

        # Load a model
        student_model = SparseEncoder("prithivida/Splade_PP_en_v1")
        teacher_model = SparseEncoder("naver/splade-cocondenser-ensembledistil")

        # Load any dataset with some texts
        dataset = load_dataset("sentence-transformers/stsb", split="validation")
        sentences = dataset["sentence1"] + dataset["sentence2"]

        # Given queries, a corpus and a mapping with relevant documents, the SparseMSEEvaluator computes different MSE metrics.
        mse_evaluator = SparseMSEEvaluator(
            source_sentences=sentences,
            target_sentences=sentences,
            teacher_model=teacher_model,
            name="stsb-dev",
        )
        results = mse_evaluator(student_model)
        '''
        MSE evaluation (lower = better) on the stsb-dev dataset:
        MSE (*100):     0.034905
        Model Sparsity: Active Dimensions: 54.6, Sparsity Ratio: 0.9982
        '''
        # Print the results
        print(f"Primary metric: ")
        # => Primary metric: stsb-dev_negative_mse
        print(f"Primary metric value: ")
        # => Primary metric value: -0.0349
    :::
    ::::

## ReciprocalRankFusionEvaluator[ïƒ?](#reciprocalrankfusionevaluator "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.evaluation.]][[ReciprocalRankFusionEvaluator]][(]*[[dense_samples]][[:]][ ][[list][[\[]][dict][[\[]][str][[,]][ ][str][ ][[\|]][ ][list][[\[]][str][[\]]][[\]]][[\]]]]*, *[[sparse_samples]][[:]][ ][[list][[\[]][dict][[\[]][str][[,]][ ][str][ ][[\|]][ ][list][[\[]][str][[\]]][[\]]][[\]]]]*, *[[at_k]][[:]][ ][[int]][ ][[=]][ ][[10]]*, *[[rrf_k]][[:]][ ][[int]][ ][[=]][ ][[60]]*, *[[name]][[:]][ ][[str]][ ][[=]][ ][[\'\']]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[show_progress_bar]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[write_csv]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[write_predictions]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\evaluation\ReciprocalRankFusionEvaluator.py#L17-L351)[ïƒ?](#sentence_transformers.sparse_encoder.evaluation.ReciprocalRankFusionEvaluator "Link to this definition")

:   This class evaluates a hybrid search approach using Reciprocal Rank Fusion (RRF).

    Given a query and two separate ranked lists of documents from different retrievers (e.g., sparse and dense), it combines them using the RRF formula and computes metrics like MRR@k, NDCG@k, and MAP.

    Parameters[:]

    :   - **dense_samples** (*list*) â€" A list of dictionaries for dense retriever results. Each dictionary should have: - â€˜query_idâ€™: The ID of the query - â€˜queryâ€™: The search query text - â€˜positiveâ€™: A list of relevant documents - â€˜documentsâ€™: A list of all documents (including positives)

        - **sparse_samples** (*list*) â€" A list of dictionaries for sparse retriever results with the same format

        - **at_k** (*int*) â€" Only consider the top k documents for evaluation. Defaults to 10.

        - **rrf_k** (*int*) â€" Constant in the RRF formula. Defaults to 60.

        - **name** (*str*) â€" Name of the evaluator. Defaults to â€œâ€?.

        - **batch_size** (*int*) â€" Batch size used for the evaluation. Defaults to 32.

        - **show_progress_bar** (*bool*) â€" Output a progress bar. Defaults to False.

        - **write_csv** (*bool*) â€" Write results to CSV file. Defaults to True.

        - **write_predictions** (*bool*) â€" Whether to write the fused predictions to a JSONL file. Defaults to False.

    Example

    See an example usage [Applications \> Retrieve & Rerank](../../../examples/sparse_encoder/applications/retrieve_rerank/README.html)