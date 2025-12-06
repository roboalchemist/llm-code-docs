# Source: https://www.sbert.net/docs/package_reference/cross_encoder/evaluation.html

# Evaluation[ïƒ?](#evaluation "Link to this heading")

CrossEncoder have their own evaluation classes in [`sentence_transformers.cross_encoder.evaluation`].

## CrossEncoderRerankingEvaluator[ïƒ?](#crossencoderrerankingevaluator "Link to this heading")

*[class][ ]*[[sentence_transformers.cross_encoder.evaluation.]][[CrossEncoderRerankingEvaluator]][(]*[[samples]][[:]][ ][[list][[\[]][dict][[\[]][str][[,]][ ][str][ ][[\|]][ ][list][[\[]][str][[\]]][[\]]][[\]]]]*, *[[at_k]][[:]][ ][[int]][ ][[=]][ ][[10]]*, *[[always_rerank_positives]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[name]][[:]][ ][[str]][ ][[=]][ ][[\'\']]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[64]]*, *[[show_progress_bar]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[write_csv]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[mrr_at_k]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\cross_encoder\evaluation\reranking.py#L20-L304)[ïƒ?](#sentence_transformers.cross_encoder.evaluation.CrossEncoderRerankingEvaluator "Link to this definition")

:   This class evaluates a CrossEncoder model for the task of re-ranking.

    Given a query and a list of documents, it computes the score \[query, doc_i\] for all possible documents and sorts them in decreasing order. Then, [MRR@10](/cdn-cgi/l/email-protection#29647b7b0f0a1a1e120f0a1c1b120f0a1d11121819), [NDCG@10](/cdn-cgi/l/email-protection#98d6dcdbdfbebbabafa3bebbadaaa3bebbaca0a3a9a8) and MAP are computed to measure the quality of the ranking.

    The evaluator expects a list of samples. Each sample is a dictionary with the mandatory â€œqueryâ€? and â€œpositiveâ€? keys, and either a â€œnegativeâ€? or a â€œdocumentsâ€? key. The â€œqueryâ€? is the search query, the â€œpositiveâ€? is a list of relevant documents, and the â€œnegativeâ€? is a list of irrelevant documents. Alternatively, the â€œdocumentsâ€? key can be used to provide a list of all documents, including the positive ones. In this case, the evaluator will assume that the list is already ranked by similarity, with the most similar documents first, and will report both the reranking performance as well as the performance before reranking. This can be useful to measure the improvement of the reranking on top of a first-stage retrieval (e.g. a SentenceTransformer model).

    Note that the maximum score is 1.0 by default, because all positive documents are included in the ranking. This can be toggled off by using samples with [`documents`] instead of [`negative`], i.e. ranked lists of all documents including the positive ones, together with [`always_rerank_positives=False`]. [`always_rerank_positives=False`] only works when using [`documents`] instead of [`negative`].

    Parameters[:]

    :   - **samples** (*list*) â€"

          A list of dictionaries, where each dictionary represents a sample and has the following keys: - â€˜queryâ€™ (mandatory): The search query. - â€˜positiveâ€™ (mandatory): A list of positive (relevant) documents. - â€˜negativeâ€™ (optional): A list of negative (irrelevant) documents. Mutually exclusive with â€˜documentsâ€™. - â€˜documentsâ€™ (optional): A list of all documents, including the positive ones. This list is assumed to be

          > ::: 
          > ranked by similarity, with the most similar documents first. Mutually exclusive with â€˜negativeâ€™.
          > :::

        - **at_k** (*int,* *optional*) â€" Only consider the top k most similar documents to each query for the evaluation. Defaults to 10.

        - **always_rerank_positives** (*bool*) â€" If True, always evaluate with all positives included. If False, only include the positives that are already in the documents list. Always set to True if your [`samples`] contain [`negative`] instead of [`documents`]. When using [`documents`], setting this to True will result in a more useful evaluation signal, but setting it to False will result in a more realistic evaluation. Defaults to True.

        - **name** (*str,* *optional*) â€" Name of the evaluator, used for logging, saving in a CSV, and the model card. Defaults to â€œâ€?.

        - **batch_size** (*int*) â€" Batch size to compute sentence embeddings. Defaults to 64.

        - **show_progress_bar** (*bool*) â€" Show progress bar when computing embeddings. Defaults to False.

        - **write_csv** (*bool*) â€" Write results to CSV file. Defaults to True.

        - **mrr_at_k** (*Optional\[int\],* *optional*) â€" Deprecated parameter. Please use at_k instead. Defaults to None.

    Example

    :::: 
    ::: highlight
        from sentence_transformers import CrossEncoder
        from sentence_transformers.cross_encoder.evaluation import CrossEncoderRerankingEvaluator
        from datasets import load_dataset

        # Load a model
        model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")

        # Load a dataset with queries, positives, and negatives
        eval_dataset = load_dataset("microsoft/ms_marco", "v1.1", split="validation")

        samples = [
            
            for sample in eval_dataset
        ]

        # Initialize the evaluator
        reranking_evaluator = CrossEncoderRerankingEvaluator(
            samples=samples,
            name="ms-marco-dev",
            show_progress_bar=True,
        )
        results = reranking_evaluator(model)
        '''
        CrossEncoderRerankingEvaluator: Evaluating the model on the ms-marco-dev dataset:
        Queries: 10047    Positives: Min 0.0, Mean 1.1, Max 5.0   Negatives: Min 1.0, Mean 7.1, Max 10.0
                 Base  -> Reranked
        MAP:     34.03 -> 62.36
        MRR@10:  34.67 -> 62.96
        NDCG@10: 49.05 -> 71.05
        '''
        print(reranking_evaluator.primary_metric)
        # => ms-marco-dev_ndcg@10
        print(results[reranking_evaluator.primary_metric])
        # => 0.7104656857184184
    :::
    ::::

## CrossEncoderNanoBEIREvaluator[ïƒ?](#crossencodernanobeirevaluator "Link to this heading")

*[class][ ]*[[sentence_transformers.cross_encoder.evaluation.]][[CrossEncoderNanoBEIREvaluator]][(]*[dataset_names:] [list\[\~typing.Literal\[\'climatefever\',] [\'dbpedia\',] [\'fever\',] [\'fiqa2018\',] [\'hotpotqa\',] [\'msmarco\',] [\'nfcorpus\',] [\'nq\',] [\'quoraretrieval\',] [\'scidocs\',] [\'arguana\',] [\'scifact\',] [\'touche2020\'\]\]] [\|] [None] [=] [None,] [rerank_k:] [int] [=] [100,] [at_k:] [int] [=] [10,] [always_rerank_positives:] [bool] [=] [True,] [batch_size:] [int] [=] [32,] [show_progress_bar:] [bool] [=] [False,] [write_csv:] [bool] [=] [True,] [aggregate_fn:] [\~collections.abc.Callable\[\[list\[float\]\],] [float\]] [=] [\<function] [mean\>,] [aggregate_key:] [str] [=] [\'mean\']*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\cross_encoder\evaluation\nano_beir.py#L69-L348)[ïƒ?](#sentence_transformers.cross_encoder.evaluation.CrossEncoderNanoBEIREvaluator "Link to this definition")

:   This class evaluates a CrossEncoder model on the NanoBEIR collection of Information Retrieval datasets.

    The collection is a set of datasets based on the BEIR collection, but with a significantly smaller size, so it can be used for quickly evaluating the retrieval performance of a model before committing to a full evaluation. The datasets are available on Hugging Face in the [NanoBEIR with BM25 collection](https://huggingface.co/collections/sentence-transformers/nanobeir-with-bm25-rankings-67bdcbc629f007c15bf358d8). This evaluator will return the same metrics as the CrossEncoderRerankingEvaluator (i.e., MRR@k, nDCG@k, MAP), for each dataset and on average.

    Rather than reranking all documents for each query, the evaluator will only rerank the [`rerank_k`] documents from a BM25 ranking. When your logging is set to INFO, the evaluator will print the MAP, MRR@k, and nDCG@k for each dataset and the average over all datasets.

    Note that the maximum score is 1.0 by default, because all positive documents are included in the ranking. This can be toggled off by setting [`always_rerank_positives=False`], at which point the maximum score will be bound by the number of positive documents that BM25 ranks in the top [`rerank_k`] documents.

    ::: 
    Note

    This evaluator outputs its results using keys in the format [`NanoBEIR_R__`], where [`metric`] is one of [`map`], [`mrr@`], or [`ndcg@`], and [`rerank_k`], [`aggregate_key`] and [`at_k`] are the parameters of the evaluator. The primary metric is [`ndcg@`]. By default, the name of the primary metric is [`NanoBEIR_R100_mean_ndcg@10`].

    For the results of each dataset, the keys are in the format [`Nano_R_`], for example [`NanoMSMARCO_R100_mrr@10`].

    These can be used as [`metric_for_best_model`] alongside [`load_best_model_at_end=True`] in the [[`CrossEncoderTrainingArguments`]](training_args.html#sentence_transformers.cross_encoder.training_args.CrossEncoderTrainingArguments "sentence_transformers.cross_encoder.training_args.CrossEncoderTrainingArguments") to automatically load the best model based on a specific metric of interest.
    :::

    Parameters[:]

    :   - **dataset_names** (*List\[str\]*) â€" The names of the datasets to evaluate on. If not specified, use all datasets except arguana and touche2020.

        - **rerank_k** (*int*) â€" The number of documents to rerank from the BM25 ranking. Defaults to 100.

        - **at_k** (*int,* *optional*) â€" Only consider the top k most similar documents to each query for the evaluation. Defaults to 10.

        - **always_rerank_positives** (*bool*) â€" If True, always evaluate with all positives included. If False, only include the positives that are already in the documents list. Always set to True if your [`samples`] contain [`negative`] instead of [`documents`]. When using [`documents`], setting this to True will result in a more useful evaluation signal, but setting it to False will result in a more realistic evaluation. Defaults to True.

        - **batch_size** (*int*) â€" Batch size to compute sentence embeddings. Defaults to 64.

        - **show_progress_bar** (*bool*) â€" Show progress bar when computing embeddings. Defaults to False.

        - **write_csv** (*bool*) â€" Write results to CSV file. Defaults to True.

        - **aggregate_fn** (*Callable\[\[list\[float\]\],* *float\]*) â€" The function to aggregate the scores. Defaults to np.mean.

        - **aggregate_key** (*str*) â€" The key to use for the aggregated score. Defaults to â€œmeanâ€?.

    Example

    :::: 
    ::: highlight
        from sentence_transformers.cross_encoder import CrossEncoder
        from sentence_transformers.cross_encoder.evaluation import CrossEncoderNanoBEIREvaluator
        import logging

        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

        # Load a model
        model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")

        # Load & run the evaluator
        dataset_names = ["msmarco", "nfcorpus", "nq"]
        evaluator = CrossEncoderNanoBEIREvaluator(dataset_names)
        results = evaluator(model)
        '''
        NanoBEIR Evaluation of the model on ['msmarco', 'nfcorpus', 'nq'] dataset:
        Evaluating NanoMSMARCO
        CrossEncoderRerankingEvaluator: Evaluating the model on the NanoMSMARCO dataset:
                 Base  -> Reranked
        MAP:     48.96 -> 60.35
        MRR@10:  47.75 -> 59.63
        NDCG@10: 54.04 -> 66.86

        Evaluating NanoNFCorpus
        CrossEncoderRerankingEvaluator: Evaluating the model on the NanoNFCorpus dataset:
        Queries: 50   Positives: Min 1.0, Mean 50.4, Max 463.0        Negatives: Min 54.0, Mean 92.8, Max 100.0
                 Base  -> Reranked
        MAP:     26.10 -> 34.61
        MRR@10:  49.98 -> 58.85
        NDCG@10: 32.50 -> 39.30

        Evaluating NanoNQ
        CrossEncoderRerankingEvaluator: Evaluating the model on the NanoNQ dataset:
        Queries: 50   Positives: Min 1.0, Mean 1.1, Max 2.0   Negatives: Min 98.0, Mean 99.0, Max 100.0
                 Base  -> Reranked
        MAP:     41.96 -> 70.98
        MRR@10:  42.67 -> 73.55
        NDCG@10: 50.06 -> 75.99

        CrossEncoderNanoBEIREvaluator: Aggregated Results:
                 Base  -> Reranked
        MAP:     39.01 -> 55.31
        MRR@10:  46.80 -> 64.01
        NDCG@10: 45.54 -> 60.72
        '''
        print(evaluator.primary_metric)
        # NanoBEIR_R100_mean_ndcg@10
        print(results[evaluator.primary_metric])
        # 0.60716840988382
    :::
    ::::

## CrossEncoderClassificationEvaluator[ïƒ?](#crossencoderclassificationevaluator "Link to this heading")

*[class][ ]*[[sentence_transformers.cross_encoder.evaluation.]][[CrossEncoderClassificationEvaluator]][(]*[[sentence_pairs]][[:]][ ][[list][[\[]][list][[\[]][str][[\]]][[\]]]]*, *[[labels]][[:]][ ][[list][[\[]][int][[\]]]]*, *[[\*]]*, *[[name]][[:]][ ][[str]][ ][[=]][ ][[\'\']]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[show_progress_bar]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[write_csv]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\cross_encoder\evaluation\classification.py#L20-L181)[ïƒ?](#sentence_transformers.cross_encoder.evaluation.CrossEncoderClassificationEvaluator "Link to this definition")

:   Evaluate a CrossEncoder model based on the accuracy of the predicted class vs. the gold labels. The evaluator expects a list of sentence pairs and a list of gold labels. If the model has a single output, it is assumed to be a binary classification model and the evaluator will calculate accuracy, F1, precision, recall, and average precision. If the model has multiple outputs, the evaluator will calculate macro F1, micro F1, and weighted F1.

    Parameters[:]

    :   - **sentence_pairs** (*List\[List\[str\]\]*) â€" A list of sentence pairs with each element being a list of two strings.

        - **labels** (*List\[int\]*) â€" A list of integers with the gold labels for each sentence pair.

        - **name** (*str*) â€" Name of the evaluator, useful for the generated model card.

        - **batch_size** (*int*) â€" Batch size used for the evaluation. Defaults to 32.

        - **show_progress_bar** (*bool*) â€" Output a progress bar. Defaults to None, which shows the progress bar if the logging level is INFO or DEBUG.

        - **write_csv** (*bool*) â€" Write results to a CSV file. If a CSV already exists, then values are appended. Defaults to True.

    Example

    :::: 
    ::: highlight
        from sentence_transformers import CrossEncoder
        from sentence_transformers.cross_encoder.evaluation import CrossEncoderClassificationEvaluator
        from datasets import load_dataset

        # Load a model
        model = CrossEncoder("cross-encoder/nli-deberta-v3-base")

        # Load a dataset with two text columns and a class label column (https://huggingface.co/datasets/sentence-transformers/all-nli)
        eval_dataset = load_dataset("sentence-transformers/all-nli", "pair-class", split="dev[-1000:]")

        # Create a list of pairs, and map the labels to the labels that the model knows
        pairs = list(zip(eval_dataset["premise"], eval_dataset["hypothesis"]))
        label_mapping = 
        labels = [label_mapping[label] for label in eval_dataset["label"]]

        # Initialize the evaluator
        cls_evaluator = CrossEncoderClassificationEvaluator(
            sentence_pairs=pairs,
            labels=labels,
            name="all-nli-dev",
        )
        results = cls_evaluator(model)
        '''
        CrossEncoderClassificationEvaluator: Evaluating the model on all-nli-dev dataset:
        Macro F1:           89.43
        Micro F1:           89.30
        Weighted F1:        89.33
        '''
        print(cls_evaluator.primary_metric)
        # => all-nli-dev_f1_macro
        print(results[cls_evaluator.primary_metric])
        # => 0.8942858180262628
    :::
    ::::

## CrossEncoderCorrelationEvaluator[ïƒ?](#crossencodercorrelationevaluator "Link to this heading")

*[class][ ]*[[sentence_transformers.cross_encoder.evaluation.]][[CrossEncoderCorrelationEvaluator]][(]*[[sentence_pairs]][[:]][ ][[list][[\[]][list][[\[]][str][[\]]][[\]]]]*, *[[scores]][[:]][ ][[list][[\[]][float][[\]]]]*, *[[name]][[:]][ ][[str]][ ][[=]][ ][[\'\']]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[show_progress_bar]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[write_csv]][[:]][ ][[bool]][ ][[=]][ ][[True]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\cross_encoder\evaluation\correlation.py#L19-L132)[ïƒ?](#sentence_transformers.cross_encoder.evaluation.CrossEncoderCorrelationEvaluator "Link to this definition")

:   This evaluator can be used with the CrossEncoder class. Given sentence pairs and continuous scores, it compute the pearson & spearman correlation between the predicted score for the sentence pair and the gold score.

    Parameters[:]

    :   - **sentence_pairs** (*List\[List\[str\]\]*) â€" A list of sentence pairs with each element being a list of two strings.

        - **labels** (*List\[int\]*) â€" A list of integers with the gold labels for each sentence pair.

        - **name** (*str*) â€" Name of the evaluator, useful for the generated model card.

        - **batch_size** (*int*) â€" Batch size used for the evaluation. Defaults to 32.

        - **show_progress_bar** (*bool*) â€" Output a progress bar. Defaults to None, which shows the progress bar if the logging level is INFO or DEBUG.

        - **write_csv** (*bool*) â€" Write results to a CSV file. If a CSV already exists, then values are appended. Defaults to True.

    Examples

    :::: 
    ::: highlight
        from datasets import load_dataset
        from sentence_transformers import CrossEncoder
        from sentence_transformers.cross_encoder.evaluation import CrossEncoderCorrelationEvaluator

        # Load a model
        model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")

        # Load the STSB dataset (https://huggingface.co/datasets/sentence-transformers/stsb)
        eval_dataset = load_dataset("sentence-transformers/stsb", split="validation")
        pairs = list(zip(eval_dataset["sentence1"], eval_dataset["sentence2"]))

        # Initialize the evaluator
        dev_evaluator = CrossEncoderCorrelationEvaluator(
            sentence_pairs=pairs,
            scores=eval_dataset["score"],
            name="sts_dev",
        )
        results = dev_evaluator(model)
        '''
        CrossEncoderCorrelationEvaluator: Evaluating the model on sts_dev dataset:
        Correlation: Pearson: 0.8503 Spearman: 0.8486
        '''
        print(dev_evaluator.primary_metric)
        # => sts_dev_spearman
        print(results[dev_evaluator.primary_metric])
        # => 0.8486467897872038
    :::
    ::::