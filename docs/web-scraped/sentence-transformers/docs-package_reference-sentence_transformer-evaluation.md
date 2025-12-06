# Source: https://www.sbert.net/docs/package_reference/sentence_transformer/evaluation.html

# Evaluation[ïƒ?](#evaluation "Link to this heading")

[`sentence_transformers.evaluation`] defines different classes, that can be used to evaluate the model during training.

## BinaryClassificationEvaluator[ïƒ?](#binaryclassificationevaluator "Link to this heading")

*[class][ ]*[[sentence_transformers.evaluation.]][[BinaryClassificationEvaluator]][(]*[[sentences1]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[sentences2]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[labels]][[:]][ ][[list][[\[]][int][[\]]]]*, *[[name]][[:]][ ][[str]][ ][[=]][ ][[\'\']]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[show_progress_bar]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[write_csv]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[truncate_dim]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[similarity_fn_names]][[:]][ ][[list][[\[]][Literal][[\[]][[\'cosine\']][[,]][ ][[\'dot\']][[,]][ ][[\'euclidean\']][[,]][ ][[\'manhattan\']][[\]]][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\evaluation\BinaryClassificationEvaluator.py#L27-L379)[ïƒ?](#sentence_transformers.evaluation.BinaryClassificationEvaluator "Link to this definition")

:   Evaluate a model based on the similarity of the embeddings by calculating the accuracy of identifying similar and dissimilar sentences. The metrics are the cosine similarity, dot score, Euclidean and Manhattan distance The returned score is the accuracy with a specified metric.

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

        - **truncate_dim** (*Optional\[int\],* *optional*) â€" The dimension to truncate sentence embeddings to. None uses the modelâ€™s current truncation dimension. Defaults to None.

        - **similarity_fn_names** (*Optional\[List\[Literal\[\"cosine\",* *\"dot\",* *\"euclidean\",* *\"manhattan\"\]\]\],* *optional*) â€" The similarity functions to use. If not specified, defaults to the [`similarity_fn_name`] attribute of the model. Defaults to None.

    Example

    :::: 
    ::: highlight
        from sentence_transformers import SentenceTransformer
        from sentence_transformers.evaluation import BinaryClassificationEvaluator
        from datasets import load_dataset

        # Load a model
        model = SentenceTransformer('all-mpnet-base-v2')

        # Load a dataset with two text columns and a class label column (https://huggingface.co/datasets/sentence-transformers/quora-duplicates)
        eval_dataset = load_dataset("sentence-transformers/quora-duplicates", "pair-class", split="train[-1000:]")

        # Initialize the evaluator
        binary_acc_evaluator = BinaryClassificationEvaluator(
            sentences1=eval_dataset["sentence1"],
            sentences2=eval_dataset["sentence2"],
            labels=eval_dataset["label"],
            name="quora_duplicates_dev",
        )
        results = binary_acc_evaluator(model)
        '''
        Binary Accuracy Evaluation of the model on the quora_duplicates_dev dataset:
        Accuracy with Cosine-Similarity:             81.60  (Threshold: 0.8352)
        F1 with Cosine-Similarity:                   75.27  (Threshold: 0.7715)
        Precision with Cosine-Similarity:            65.81
        Recall with Cosine-Similarity:               87.89
        Average Precision with Cosine-Similarity:    76.03
        Matthews Correlation with Cosine-Similarity: 62.48
        '''
        print(binary_acc_evaluator.primary_metric)
        # => "quora_duplicates_dev_cosine_ap"
        print(results[binary_acc_evaluator.primary_metric])
        # => 0.760277070888393
    :::
    ::::

## EmbeddingSimilarityEvaluator[ïƒ?](#embeddingsimilarityevaluator "Link to this heading")

*[class][ ]*[[sentence_transformers.evaluation.]][[EmbeddingSimilarityEvaluator]][(]*[[sentences1]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[sentences2]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[scores]][[:]][ ][[list][[\[]][float][[\]]]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[16]]*, *[[main_similarity]][[:]][ ][[str][ ][[\|]][ ][[SimilarityFunction]](../sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.similarity_functions.SimilarityFunction")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[similarity_fn_names]][[:]][ ][[list][[\[]][Literal][[\[]][[\'cosine\']][[,]][ ][[\'dot\']][[,]][ ][[\'euclidean\']][[,]][ ][[\'manhattan\']][[\]]][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[name]][[:]][ ][[str]][ ][[=]][ ][[\'\']]*, *[[show_progress_bar]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[write_csv]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[precision]][[:]][ ][[Literal][[\[]][[\'float32\']][[,]][ ][[\'int8\']][[,]][ ][[\'uint8\']][[,]][ ][[\'binary\']][[,]][ ][[\'ubinary\']][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[truncate_dim]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\evaluation\EmbeddingSimilarityEvaluator.py#L27-L272)[ïƒ?](#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator "Link to this definition")

:   Evaluate a model based on the similarity of the embeddings by calculating the Spearman and Pearson rank correlation in comparison to the gold standard labels. The metrics are the cosine similarity as well as euclidean and Manhattan distance The returned score is the Spearman correlation with a specified metric.

    Parameters[:]

    :   - **sentences1** (*List\[str\]*) â€" List with the first sentence in a pair.

        - **sentences2** (*List\[str\]*) â€" List with the second sentence in a pair.

        - **scores** (*List\[float\]*) â€" Similarity score between sentences1\[i\] and sentences2\[i\].

        - **batch_size** (*int,* *optional*) â€" The batch size for processing the sentences. Defaults to 16.

        - **main_similarity** (*Optional\[Union\[str,* [*SimilarityFunction*](../sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")*\]\],* *optional*) â€" The main similarity function to use. Can be a string (e.g. â€œcosineâ€?, â€œdotâ€?) or a SimilarityFunction object. Defaults to None.

        - **similarity_fn_names** (*List\[str\],* *optional*) â€" List of similarity function names to use. If None, the [`similarity_fn_name`] attribute of the model is used. Defaults to None.

        - **name** (*str,* *optional*) â€" The name of the evaluator. Defaults to â€œâ€?.

        - **show_progress_bar** (*bool,* *optional*) â€" Whether to show a progress bar during evaluation. Defaults to False.

        - **write_csv** (*bool,* *optional*) â€" Whether to write the evaluation results to a CSV file. Defaults to True.

        - **precision** (*Optional\[Literal\[\"float32\",* *\"int8\",* *\"uint8\",* *\"binary\",* *\"ubinary\"\]\],* *optional*) â€" The precision to use for the embeddings. Can be â€œfloat32â€?, â€œint8â€?, â€œuint8â€?, â€œbinaryâ€?, or â€œubinaryâ€?. Defaults to None.

        - **truncate_dim** (*Optional\[int\],* *optional*) â€" The dimension to truncate sentence embeddings to. None uses the modelâ€™s current truncation dimension. Defaults to None.

    Example

    :::: 
    ::: highlight
        from datasets import load_dataset
        from sentence_transformers import SentenceTransformer
        from sentence_transformers.evaluation import EmbeddingSimilarityEvaluator, SimilarityFunction

        # Load a model
        model = SentenceTransformer('all-mpnet-base-v2')

        # Load the STSB dataset (https://huggingface.co/datasets/sentence-transformers/stsb)
        eval_dataset = load_dataset("sentence-transformers/stsb", split="validation")

        # Initialize the evaluator
        dev_evaluator = EmbeddingSimilarityEvaluator(
            sentences1=eval_dataset["sentence1"],
            sentences2=eval_dataset["sentence2"],
            scores=eval_dataset["score"],
            name="sts_dev",
        )
        results = dev_evaluator(model)
        '''
        EmbeddingSimilarityEvaluator: Evaluating the model on the sts-dev dataset:
        Cosine-Similarity:  Pearson: 0.8806 Spearman: 0.8810
        '''
        print(dev_evaluator.primary_metric)
        # => "sts_dev_pearson_cosine"
        print(results[dev_evaluator.primary_metric])
        # => 0.881019449484294
    :::
    ::::

## InformationRetrievalEvaluator[ïƒ?](#informationretrievalevaluator "Link to this heading")

*[class][ ]*[[sentence_transformers.evaluation.]][[InformationRetrievalEvaluator]][(]*[[queries]][[:]][ ][[dict][[\[]][str][[,]][ ][str][[\]]]]*, *[[corpus]][[:]][ ][[dict][[\[]][str][[,]][ ][str][[\]]]]*, *[[relevant_docs]][[:]][ ][[dict][[\[]][str][[,]][ ][set][[\[]][str][[\]]][[\]]]]*, *[[corpus_chunk_size]][[:]][ ][[int]][ ][[=]][ ][[50000]]*, *[[mrr_at_k]][[:]][ ][[list][[\[]][int][[\]]]][ ][[=]][ ][[\[10\]]]*, *[[ndcg_at_k]][[:]][ ][[list][[\[]][int][[\]]]][ ][[=]][ ][[\[10\]]]*, *[[accuracy_at_k]][[:]][ ][[list][[\[]][int][[\]]]][ ][[=]][ ][[\[1,] [3,] [5,] [10\]]]*, *[[precision_recall_at_k]][[:]][ ][[list][[\[]][int][[\]]]][ ][[=]][ ][[\[1,] [3,] [5,] [10\]]]*, *[[map_at_k]][[:]][ ][[list][[\[]][int][[\]]]][ ][[=]][ ][[\[100\]]]*, *[[show_progress_bar]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[name]][[:]][ ][[str]][ ][[=]][ ][[\'\']]*, *[[write_csv]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[truncate_dim]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[score_functions]][[:]][ ][[dict][[\[]][str][[,]][ ][Callable][[\[]][[\[]][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[main_score_function]][[:]][ ][[str][ ][[\|]][ ][[SimilarityFunction]](../sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.similarity_functions.SimilarityFunction")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[query_prompt]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[query_prompt_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[corpus_prompt]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[corpus_prompt_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[write_predictions]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\evaluation\InformationRetrievalEvaluator.py#L24-L569)[ïƒ?](#sentence_transformers.evaluation.InformationRetrievalEvaluator "Link to this definition")

:   This class evaluates an Information Retrieval (IR) setting.

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

        - **truncate_dim** (*int,* *optional*) â€" The dimension to truncate the embeddings to. Defaults to None.

        - **score_functions** (*Dict\[str,* *Callable\[\[Tensor,* *Tensor\],* *Tensor\]\]*) â€" A dictionary mapping score function names to score functions. Defaults to the [`similarity`] function from the [`model`].

        - **main_score_function** (*Union\[str,* [*SimilarityFunction*](../sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")*\],* *optional*) â€" The main score function to use for evaluation. Defaults to None.

        - **query_prompt** (*str,* *optional*) â€" The prompt to be used when encoding the corpus. Defaults to None.

        - **query_prompt_name** (*str,* *optional*) â€" The name of the prompt to be used when encoding the corpus. Defaults to None.

        - **corpus_prompt** (*str,* *optional*) â€" The prompt to be used when encoding the corpus. Defaults to None.

        - **corpus_prompt_name** (*str,* *optional*) â€" The name of the prompt to be used when encoding the corpus. Defaults to None.

        - **write_predictions** (*bool*) â€" Whether to write the predictions to a JSONL file. Defaults to False. This can be useful for downstream evaluation as it can be used as input to the [[`ReciprocalRankFusionEvaluator`]](../sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.ReciprocalRankFusionEvaluator "sentence_transformers.sparse_encoder.evaluation.ReciprocalRankFusionEvaluator") that accept precomputed predictions.

    Example

    :::: 
    ::: highlight
        import random
        from sentence_transformers import SentenceTransformer
        from sentence_transformers.evaluation import InformationRetrievalEvaluator
        from datasets import load_dataset

        # Load a model
        model = SentenceTransformer('all-MiniLM-L6-v2')

        # Load the Touche-2020 IR dataset (https://huggingface.co/datasets/BeIR/webis-touche2020, https://huggingface.co/datasets/BeIR/webis-touche2020-qrels)
        corpus = load_dataset("BeIR/webis-touche2020", "corpus", split="corpus")
        queries = load_dataset("BeIR/webis-touche2020", "queries", split="queries")
        relevant_docs_data = load_dataset("BeIR/webis-touche2020-qrels", split="test")

        # For this dataset, we want to concatenate the title and texts for the corpus
        corpus = corpus.map(lambda x: , remove_columns=['title'])

        # Shrink the corpus size heavily to only the relevant documents + 30,000 random documents
        required_corpus_ids = set(map(str, relevant_docs_data["corpus-id"]))
        required_corpus_ids |= set(random.sample(corpus["_id"], k=30_000))
        corpus = corpus.filter(lambda x: x["_id"] in required_corpus_ids)

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

        # Given queries, a corpus and a mapping with relevant documents, the InformationRetrievalEvaluator computes different IR metrics.
        ir_evaluator = InformationRetrievalEvaluator(
            queries=queries,
            corpus=corpus,
            relevant_docs=relevant_docs,
            name="BeIR-touche2020-subset-test",
        )
        results = ir_evaluator(model)
        '''
        Information Retrieval Evaluation of the model on the BeIR-touche2020-test dataset:
        Queries: 49
        Corpus: 31923

        Score-Function: cosine
        Accuracy@1: 77.55%
        Accuracy@3: 93.88%
        Accuracy@5: 97.96%
        Accuracy@10: 100.00%
        Precision@1: 77.55%
        Precision@3: 72.11%
        Precision@5: 71.43%
        Precision@10: 62.65%
        Recall@1: 1.72%
        Recall@3: 4.78%
        Recall@5: 7.90%
        Recall@10: 13.86%
        MRR@10: 0.8580
        NDCG@10: 0.6606
        MAP@100: 0.2934
        '''
        print(ir_evaluator.primary_metric)
        # => "BeIR-touche2020-test_cosine_map@100"
        print(results[ir_evaluator.primary_metric])
        # => 0.29335196224364596
    :::
    ::::

## NanoBEIREvaluator[ïƒ?](#nanobeirevaluator "Link to this heading")

*[class][ ]*[[sentence_transformers.evaluation.]][[NanoBEIREvaluator]][(]*[dataset_names:] [list\[\~typing.Literal\[\'climatefever\',] [\'dbpedia\',] [\'fever\',] [\'fiqa2018\',] [\'hotpotqa\',] [\'msmarco\',] [\'nfcorpus\',] [\'nq\',] [\'quoraretrieval\',] [\'scidocs\',] [\'arguana\',] [\'scifact\',] [\'touche2020\'\]\]] [\|] [None] [=] [None,] [mrr_at_k:] [list\[int\]] [=] [\[10\],] [ndcg_at_k:] [list\[int\]] [=] [\[10\],] [accuracy_at_k:] [list\[int\]] [=] [\[1,] [3,] [5,] [10\],] [precision_recall_at_k:] [list\[int\]] [=] [\[1,] [3,] [5,] [10\],] [map_at_k:] [list\[int\]] [=] [\[100\],] [show_progress_bar:] [bool] [=] [False,] [batch_size:] [int] [=] [32,] [write_csv:] [bool] [=] [True,] [truncate_dim:] [int] [\|] [None] [=] [None,] [score_functions:] [dict\[str,] [\~collections.abc.Callable\[\[\~torch.Tensor,] [\~torch.Tensor\],] [\~torch.Tensor\]\]] [\|] [None] [=] [None,] [main_score_function:] [str] [\|] [\~sentence_transformers.similarity_functions.SimilarityFunction] [\|] [None] [=] [None,] [aggregate_fn:] [\~collections.abc.Callable\[\[list\[float\]\],] [float\]] [=] [\<function] [mean\>,] [aggregate_key:] [str] [=] [\'mean\',] [query_prompts:] [str] [\|] [dict\[str,] [str\]] [\|] [None] [=] [None,] [corpus_prompts:] [str] [\|] [dict\[str,] [str\]] [\|] [None] [=] [None,] [write_predictions:] [bool] [=] [False]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\evaluation\NanoBEIREvaluator.py#L73-L483)[ïƒ?](#sentence_transformers.evaluation.NanoBEIREvaluator "Link to this definition")

:   This class evaluates the performance of a SentenceTransformer Model on the NanoBEIR collection of Information Retrieval datasets.

    The collection is a set of datasets based on the BEIR collection, but with a significantly smaller size, so it can be used for quickly evaluating the retrieval performance of a model before committing to a full evaluation. The datasets are available on Hugging Face in the [NanoBEIR collection](https://huggingface.co/collections/zeta-alpha-ai/nanobeir-66e1a0af21dfd93e620cd9f6). This evaluator will return the same metrics as the InformationRetrievalEvaluator (i.e., MRR, nDCG, Recall@k), for each dataset and on average.

    Parameters[:]

    :   - **dataset_names** (*List\[str\]*) â€" The names of the datasets to evaluate on. Defaults to all datasets.

        - **mrr_at_k** (*List\[int\]*) â€" A list of integers representing the values of k for MRR calculation. Defaults to \[10\].

        - **ndcg_at_k** (*List\[int\]*) â€" A list of integers representing the values of k for NDCG calculation. Defaults to \[10\].

        - **accuracy_at_k** (*List\[int\]*) â€" A list of integers representing the values of k for accuracy calculation. Defaults to \[1, 3, 5, 10\].

        - **precision_recall_at_k** (*List\[int\]*) â€" A list of integers representing the values of k for precision and recall calculation. Defaults to \[1, 3, 5, 10\].

        - **map_at_k** (*List\[int\]*) â€" A list of integers representing the values of k for MAP calculation. Defaults to \[100\].

        - **show_progress_bar** (*bool*) â€" Whether to show a progress bar during evaluation. Defaults to False.

        - **batch_size** (*int*) â€" The batch size for evaluation. Defaults to 32.

        - **write_csv** (*bool*) â€" Whether to write the evaluation results to a CSV file. Defaults to True.

        - **truncate_dim** (*int,* *optional*) â€" The dimension to truncate the embeddings to. Defaults to None.

        - **score_functions** (*Dict\[str,* *Callable\[\[Tensor,* *Tensor\],* *Tensor\]\]*) â€" A dictionary mapping score function names to score functions. Defaults to .

        - **main_score_function** (*Union\[str,* [*SimilarityFunction*](../sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")*\],* *optional*) â€" The main score function to use for evaluation. Defaults to None.

        - **aggregate_fn** (*Callable\[\[list\[float\]\],* *float\]*) â€" The function to aggregate the scores. Defaults to np.mean.

        - **aggregate_key** (*str*) â€" The key to use for the aggregated score. Defaults to â€œmeanâ€?.

        - **query_prompts** (*str* *\|* *dict\[str,* *str\],* *optional*) â€" The prompts to add to the queries. If a string, will add the same prompt to all queries. If a dict, expects that all datasets in dataset_names are keys.

        - **corpus_prompts** (*str* *\|* *dict\[str,* *str\],* *optional*) â€" The prompts to add to the corpus. If a string, will add the same prompt to all corpus. If a dict, expects that all datasets in dataset_names are keys.

        - **write_predictions** (*bool*) â€" Whether to write the predictions to a JSONL file. Defaults to False. This can be useful for downstream evaluation as it can be used as input to the [[`ReciprocalRankFusionEvaluator`]](../sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.ReciprocalRankFusionEvaluator "sentence_transformers.sparse_encoder.evaluation.ReciprocalRankFusionEvaluator") that accept precomputed predictions.

    Example

    :::: 
    ::: highlight
        from sentence_transformers import SentenceTransformer
        from sentence_transformers.evaluation import NanoBEIREvaluator

        model = SentenceTransformer('intfloat/multilingual-e5-large-instruct')

        datasets = ["QuoraRetrieval", "MSMARCO"]
        query_prompts = 

        evaluator = NanoBEIREvaluator(
            dataset_names=datasets,
            query_prompts=query_prompts,
        )

        results = evaluator(model)
        '''
        NanoBEIR Evaluation of the model on ['QuoraRetrieval', 'MSMARCO'] dataset:
        Evaluating NanoQuoraRetrieval
        Information Retrieval Evaluation of the model on the NanoQuoraRetrieval dataset:
        Queries: 50
        Corpus: 5046

        Score-Function: cosine
        Accuracy@1: 92.00%
        Accuracy@3: 98.00%
        Accuracy@5: 100.00%
        Accuracy@10: 100.00%
        Precision@1: 92.00%
        Precision@3: 40.67%
        Precision@5: 26.00%
        Precision@10: 14.00%
        Recall@1: 81.73%
        Recall@3: 94.20%
        Recall@5: 97.93%
        Recall@10: 100.00%
        MRR@10: 0.9540
        NDCG@10: 0.9597
        MAP@100: 0.9395

        Evaluating NanoMSMARCO
        Information Retrieval Evaluation of the model on the NanoMSMARCO dataset:
        Queries: 50
        Corpus: 5043

        Score-Function: cosine
        Accuracy@1: 40.00%
        Accuracy@3: 74.00%
        Accuracy@5: 78.00%
        Accuracy@10: 88.00%
        Precision@1: 40.00%
        Precision@3: 24.67%
        Precision@5: 15.60%
        Precision@10: 8.80%
        Recall@1: 40.00%
        Recall@3: 74.00%
        Recall@5: 78.00%
        Recall@10: 88.00%
        MRR@10: 0.5849
        NDCG@10: 0.6572
        MAP@100: 0.5892
        Average Queries: 50.0
        Average Corpus: 5044.5

        Aggregated for Score Function: cosine
        Accuracy@1: 66.00%
        Accuracy@3: 86.00%
        Accuracy@5: 89.00%
        Accuracy@10: 94.00%
        Precision@1: 66.00%
        Recall@1: 60.87%
        Precision@3: 32.67%
        Recall@3: 84.10%
        Precision@5: 20.80%
        Recall@5: 87.97%
        Precision@10: 11.40%
        Recall@10: 94.00%
        MRR@10: 0.7694
        NDCG@10: 0.8085
        '''
        print(evaluator.primary_metric)
        # => "NanoBEIR_mean_cosine_ndcg@10"
        print(results[evaluator.primary_metric])
        # => 0.8084508771660436
    :::
    ::::

## MSEEvaluator[ïƒ?](#mseevaluator "Link to this heading")

*[class][ ]*[[sentence_transformers.evaluation.]][[MSEEvaluator]][(]*[[source_sentences]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[target_sentences]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[teacher_model]][[=]][[None]]*, *[[show_progress_bar]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[name]][[:]][ ][[str]][ ][[=]][ ][[\'\']]*, *[[write_csv]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[truncate_dim]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\evaluation\MSEEvaluator.py#L18-L158)[ïƒ?](#sentence_transformers.evaluation.MSEEvaluator "Link to this definition")

:   Computes the mean squared error (x100) between the computed sentence embedding and some target sentence embedding.

    The MSE is computed between \|\|teacher.encode(source_sentences) - student.encode(target_sentences)\|\|.

    For multilingual knowledge distillation ([https://huggingface.co/papers/2004.09813](https://huggingface.co/papers/2004.09813)), source_sentences are in English and target_sentences are in a different language like German, Chinese, Spanishâ€¦

    Parameters[:]

    :   - **source_sentences** (*List\[str\]*) â€" Source sentences to embed with the teacher model.

        - **target_sentences** (*List\[str\]*) â€" Target sentences to embed with the student model.

        - **teacher_model** ([*SentenceTransformer*](SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")*,* *optional*) â€" The teacher model to compute the source sentence embeddings.

        - **show_progress_bar** (*bool,* *optional*) â€" Show progress bar when computing embeddings. Defaults to False.

        - **batch_size** (*int,* *optional*) â€" Batch size to compute sentence embeddings. Defaults to 32.

        - **name** (*str,* *optional*) â€" Name of the evaluator. Defaults to â€œâ€?.

        - **write_csv** (*bool,* *optional*) â€" Write results to CSV file. Defaults to True.

        - **truncate_dim** (*int,* *optional*) â€" The dimension to truncate sentence embeddings to. None uses the modelâ€™s current truncation dimension. Defaults to None.

    Example

    :::: 
    ::: highlight
        from sentence_transformers import SentenceTransformer
        from sentence_transformers.evaluation import MSEEvaluator
        from datasets import load_dataset

        # Load a model
        student_model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')
        teacher_model = SentenceTransformer('all-mpnet-base-v2')

        # Load any dataset with some texts
        dataset = load_dataset("sentence-transformers/stsb", split="validation")
        sentences = dataset["sentence1"] + dataset["sentence2"]

        # Given queries, a corpus and a mapping with relevant documents, the MSEEvaluator computes different MSE metrics.
        mse_evaluator = MSEEvaluator(
            source_sentences=sentences,
            target_sentences=sentences,
            teacher_model=teacher_model,
            name="stsb-dev",
        )
        results = mse_evaluator(student_model)
        '''
        MSE evaluation (lower = better) on the stsb-dev dataset:
        MSE (*100):  0.805045
        '''
        print(mse_evaluator.primary_metric)
        # => "stsb-dev_negative_mse"
        print(results[mse_evaluator.primary_metric])
        # => -0.8050452917814255
    :::
    ::::

## ParaphraseMiningEvaluator[ïƒ?](#paraphraseminingevaluator "Link to this heading")

*[class][ ]*[[sentence_transformers.evaluation.]][[ParaphraseMiningEvaluator]][(]*[[sentences_map]][[:]][ ][[dict][[\[]][str][[,]][ ][str][[\]]]]*, *[[duplicates_list]][[:]][ ][[list][[\[]][tuple][[\[]][str][[,]][ ][str][[\]]][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[duplicates_dict]][[:]][ ][[dict][[\[]][str][[,]][ ][dict][[\[]][str][[,]][ ][bool][[\]]][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[add_transitive_closure]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[query_chunk_size]][[:]][ ][[int]][ ][[=]][ ][[5000]]*, *[[corpus_chunk_size]][[:]][ ][[int]][ ][[=]][ ][[100000]]*, *[[max_pairs]][[:]][ ][[int]][ ][[=]][ ][[500000]]*, *[[top_k]][[:]][ ][[int]][ ][[=]][ ][[100]]*, *[[show_progress_bar]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[16]]*, *[[name]][[:]][ ][[str]][ ][[=]][ ][[\'\']]*, *[[write_csv]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[truncate_dim]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\evaluation\ParaphraseMiningEvaluator.py#L18-L279)[ïƒ?](#sentence_transformers.evaluation.ParaphraseMiningEvaluator "Link to this definition")

:   Given a large set of sentences, this evaluator performs paraphrase (duplicate) mining and identifies the pairs with the highest similarity. It compare the extracted paraphrase pairs with a set of gold labels and computes the F1 score.

    Parameters[:]

    :   - **sentences_map** (*Dict\[str,* *str\]*) â€" A dictionary that maps sentence-ids to sentences. For example, sentences_map\[id\] =\> sentence.

        - **duplicates_list** (*List\[Tuple\[str,* *str\]\],* *optional*) â€" A list with id pairs \[(id1, id2), (id1, id5)\] that identifies the duplicates / paraphrases in the sentences_map. Defaults to None.

        - **duplicates_dict** (*Dict\[str,* *Dict\[str,* *bool\]\],* *optional*) â€" A default dictionary mapping \[id1\]\[id2\] to true if id1 and id2 are duplicates. Must be symmetric, i.e., if \[id1\]\[id2\] =\> True, then \[id2\]\[id1\] =\> True. Defaults to None.

        - **add_transitive_closure** (*bool,* *optional*) â€" If true, it adds a transitive closure, i.e. if dup\[a\]\[b\] and dup\[b\]\[c\], then dup\[a\]\[c\]. Defaults to False.

        - **query_chunk_size** (*int,* *optional*) â€" To identify the paraphrases, the cosine-similarity between all sentence-pairs will be computed. As this might require a lot of memory, we perform a batched computation. query_chunk_size sentences will be compared against up to corpus_chunk_size sentences. In the default setting, 5000 sentences will be grouped together and compared up-to against 100k other sentences. Defaults to 5000.

        - **corpus_chunk_size** (*int,* *optional*) â€" The corpus will be batched, to reduce the memory requirement. Defaults to 100000.

        - **max_pairs** (*int,* *optional*) â€" We will only extract up to max_pairs potential paraphrase candidates. Defaults to 500000.

        - **top_k** (*int,* *optional*) â€" For each query, we extract the top_k most similar pairs and add it to a sorted list. I.e., for one sentence we cannot find more than top_k paraphrases. Defaults to 100.

        - **show_progress_bar** (*bool,* *optional*) â€" Output a progress bar. Defaults to False.

        - **batch_size** (*int,* *optional*) â€" Batch size for computing sentence embeddings. Defaults to 16.

        - **name** (*str,* *optional*) â€" Name of the experiment. Defaults to â€œâ€?.

        - **write_csv** (*bool,* *optional*) â€" Write results to CSV file. Defaults to True.

        - **truncate_dim** (*Optional\[int\],* *optional*) â€" The dimension to truncate sentence embeddings to. None uses the modelâ€™s current truncation dimension. Defaults to None.

    Example

    :::: 
    ::: highlight
        from datasets import load_dataset
        from sentence_transformers.SentenceTransformer import SentenceTransformer
        from sentence_transformers.evaluation import ParaphraseMiningEvaluator

        # Load a model
        model = SentenceTransformer('all-mpnet-base-v2')

        # Load the Quora Duplicates Mining dataset
        questions_dataset = load_dataset("sentence-transformers/quora-duplicates-mining", "questions", split="dev")
        duplicates_dataset = load_dataset("sentence-transformers/quora-duplicates-mining", "duplicates", split="dev")

        # Create a mapping from qid to question & a list of duplicates (qid1, qid2)
        qid_to_questions = dict(zip(questions_dataset["qid"], questions_dataset["question"]))
        duplicates = list(zip(duplicates_dataset["qid1"], duplicates_dataset["qid2"]))

        # Initialize the paraphrase mining evaluator
        paraphrase_mining_evaluator = ParaphraseMiningEvaluator(
            sentences_map=qid_to_questions,
            duplicates_list=duplicates,
            name="quora-duplicates-dev",
        )
        results = paraphrase_mining_evaluator(model)
        '''
        Paraphrase Mining Evaluation of the model on the quora-duplicates-dev dataset:
        Number of candidate pairs: 250564
        Average Precision: 56.51
        Optimal threshold: 0.8325
        Precision: 52.76
        Recall: 59.19
        F1: 55.79
        '''
        print(paraphrase_mining_evaluator.primary_metric)
        # => "quora-duplicates-dev_average_precision"
        print(results[paraphrase_mining_evaluator.primary_metric])
        # => 0.5650940787776353
    :::
    ::::

## RerankingEvaluator[ïƒ?](#rerankingevaluator "Link to this heading")

*[class][ ]*[[sentence_transformers.evaluation.]][[RerankingEvaluator]][(]*[samples:] [list\[dict\[str,] [str] [\|] [list\[str\]\]\],] [at_k:] [int] [=] [10,] [name:] [str] [=] [\'\',] [write_csv:] [bool] [=] [True,] [similarity_fct:] [\~collections.abc.Callable\[\[\~torch.Tensor,] [\~torch.Tensor\],] [\~torch.Tensor\]] [=] [\<function] [cos_sim\>,] [batch_size:] [int] [=] [64,] [show_progress_bar:] [bool] [=] [False,] [use_batched_encoding:] [bool] [=] [True,] [truncate_dim:] [int] [\|] [None] [=] [None,] [mrr_at_k:] [int] [\|] [None] [=] [None]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\evaluation\RerankingEvaluator.py#L26-L373)[ïƒ?](#sentence_transformers.evaluation.RerankingEvaluator "Link to this definition")

:   This class evaluates a SentenceTransformer model for the task of re-ranking.

    Given a query and a list of documents, it computes the score \[query, doc_i\] for all possible documents and sorts them in decreasing order. Then, [MRR@10](/cdn-cgi/l/email-protection#efa2bdbdc9ccdcd8d4c9ccdaddd4c9ccdbd7d4dedf), [NDCG@10](/cdn-cgi/l/email-protection#501e141317767363676b767365626b767364686b6160) and MAP is compute to measure the quality of the ranking.

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

        - **truncate_dim** (*Optional\[int\],* *optional*) â€" The dimension to truncate sentence embeddings to. None uses the modelâ€™s current truncation dimension. Defaults to None.

        - **mrr_at_k** (*Optional\[int\],* *optional*) â€" Deprecated parameter. Please use at_k instead. Defaults to None.

    Example

    :::: 
    ::: highlight
        from sentence_transformers import SentenceTransformer
        from sentence_transformers.evaluation import RerankingEvaluator
        from datasets import load_dataset

        # Load a model
        model = SentenceTransformer("all-MiniLM-L6-v2")

        # Load a dataset with queries, positives, and negatives
        eval_dataset = load_dataset("microsoft/ms_marco", "v1.1", split="validation")

        samples = [
            
            for sample in eval_dataset
        ]

        # Initialize the evaluator
        reranking_evaluator = RerankingEvaluator(
            samples=samples,
            name="ms-marco-dev",
        )
        results = reranking_evaluator(model)
        '''
        RerankingEvaluator: Evaluating the model on the ms-marco-dev dataset:
        Queries: 9706      Positives: Min 1.0, Mean 1.1, Max 5.0   Negatives: Min 1.0, Mean 7.1, Max 9.0
        MAP: 56.07
        MRR@10: 56.70
        NDCG@10: 67.08
        '''
        print(reranking_evaluator.primary_metric)
        # => ms-marco-dev_ndcg@10
        print(results[reranking_evaluator.primary_metric])
        # => 0.6708042171399308
    :::
    ::::

## SentenceEvaluator[ïƒ?](#sentenceevaluator "Link to this heading")

*[class][ ]*[[sentence_transformers.evaluation.]][[SentenceEvaluator]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\evaluation\SentenceEvaluator.py#L13-L120)[ïƒ?](#sentence_transformers.evaluation.SentenceEvaluator "Link to this definition")

:   Base class for all evaluators. Notably, this class introduces the [`greater_is_better`] and [`primary_metric`] attributes. The former is a boolean indicating whether a higher evaluation score is better, which is used for choosing the best checkpoint if [`load_best_model_at_end`] is set to [`True`] in the training arguments.

    The latter is a string indicating the primary metric for the evaluator. This has to be defined whenever the evaluator returns a dictionary of metrics, and the primary metric is the key pointing to the primary metric, i.e. the one that is used for model selection and/or logging.

    Extend this class and implement \_\_call\_\_ for custom evaluators.

## SequentialEvaluator[ïƒ?](#sequentialevaluator "Link to this heading")

*[class][ ]*[[sentence_transformers.evaluation.]][[SequentialEvaluator]][(]*[evaluators:] [\~collections.abc.Iterable\[\~sentence_transformers.evaluation.SentenceEvaluator.SentenceEvaluator\],] [main_score_function=\<function] [SequentialEvaluator.\<lambda\>\>]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\evaluation\SequentialEvaluator.py#L12-L61)[ïƒ?](#sentence_transformers.evaluation.SequentialEvaluator "Link to this definition")

:   This evaluator allows that multiple sub-evaluators are passed. When the model is evaluated, the data is passed sequentially to all sub-evaluators.

    All scores are passed to â€˜main_score_functionâ€™, which derives one final score value

    Parameters[:]

    :   - **evaluators** (*Iterable\[*[*SentenceEvaluator*](#sentence_transformers.evaluation.SentenceEvaluator "sentence_transformers.evaluation.SentenceEvaluator")*\]*) â€" A collection of SentenceEvaluator objects.

        - **main_score_function** (*function,* *optional*) â€" A function that takes a list of scores and returns the main score. Defaults to selecting the last score in the list.

    Example

    :::: 
    ::: highlight
        evaluator1 = BinaryClassificationEvaluator(...)
        evaluator2 = InformationRetrievalEvaluator(...)
        evaluator3 = MSEEvaluator(...)
        seq_evaluator = SequentialEvaluator([evaluator1, evaluator2, evaluator3])
    :::
    ::::

## TranslationEvaluator[ïƒ?](#translationevaluator "Link to this heading")

*[class][ ]*[[sentence_transformers.evaluation.]][[TranslationEvaluator]][(]*[[source_sentences]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[target_sentences]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[show_progress_bar]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[16]]*, *[[name]][[:]][ ][[str]][ ][[=]][ ][[\'\']]*, *[[print_wrong_matches]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[write_csv]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[truncate_dim]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\evaluation\TranslationEvaluator.py#L22-L192)[ïƒ?](#sentence_transformers.evaluation.TranslationEvaluator "Link to this definition")

:   Given two sets of sentences in different languages, e.g. (en_1, en_2, en_3â€¦) and (fr_1, fr_2, fr_3, â€¦), and assuming that fr_i is the translation of en_i. Checks if vec(en_i) has the highest similarity to vec(fr_i). Computes the accuracy in both directions

    The labels need to indicate the similarity between the sentences.

    Parameters[:]

    :   - **source_sentences** (*List\[str\]*) â€" List of sentences in the source language.

        - **target_sentences** (*List\[str\]*) â€" List of sentences in the target language.

        - **show_progress_bar** (*bool*) â€" Whether to show a progress bar when computing embeddings. Defaults to False.

        - **batch_size** (*int*) â€" The batch size to compute sentence embeddings. Defaults to 16.

        - **name** (*str*) â€" The name of the evaluator. Defaults to an empty string.

        - **print_wrong_matches** (*bool*) â€" Whether to print incorrect matches. Defaults to False.

        - **write_csv** (*bool*) â€" Whether to write the evaluation results to a CSV file. Defaults to True.

        - **truncate_dim** (*int,* *optional*) â€" The dimension to truncate sentence embeddings to. If None, the modelâ€™s current truncation dimension will be used. Defaults to None.

    Example

    :::: 
    ::: highlight
        from sentence_transformers import SentenceTransformer
        from sentence_transformers.evaluation import TranslationEvaluator
        from datasets import load_dataset

        # Load a model
        model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')

        # Load a parallel sentences dataset
        dataset = load_dataset("sentence-transformers/parallel-sentences-news-commentary", "en-nl", split="train[:1000]")

        # Initialize the TranslationEvaluator using the same texts from two languages
        translation_evaluator = TranslationEvaluator(
            source_sentences=dataset["english"],
            target_sentences=dataset["non_english"],
            name="news-commentary-en-nl",
        )
        results = translation_evaluator(model)
        '''
        Evaluating translation matching Accuracy of the model on the news-commentary-en-nl dataset:
        Accuracy src2trg: 90.80
        Accuracy trg2src: 90.40
        '''
        print(translation_evaluator.primary_metric)
        # => "news-commentary-en-nl_mean_accuracy"
        print(results[translation_evaluator.primary_metric])
        # => 0.906
    :::
    ::::

## TripletEvaluator[ïƒ?](#tripletevaluator "Link to this heading")

*[class][ ]*[[sentence_transformers.evaluation.]][[TripletEvaluator]][(]*[[anchors]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[positives]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[negatives]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[main_similarity_function]][[:]][ ][[str][ ][[\|]][ ][[SimilarityFunction]](../sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.similarity_functions.SimilarityFunction")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[margin]][[:]][ ][[float][ ][[\|]][ ][dict][[\[]][str][[,]][ ][float][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[name]][[:]][ ][[str]][ ][[=]][ ][[\'\']]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[16]]*, *[[show_progress_bar]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[write_csv]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[truncate_dim]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[similarity_fn_names]][[:]][ ][[list][[\[]][Literal][[\[]][[\'cosine\']][[,]][ ][[\'dot\']][[,]][ ][[\'euclidean\']][[,]][ ][[\'manhattan\']][[\]]][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[main_distance_function]][[:]][ ][[str][ ][[\|]][ ][[SimilarityFunction]](../sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.similarity_functions.SimilarityFunction")[ ][[\|]][ ][None]][ ][[=]][ ][[\'deprecated\']]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\evaluation\TripletEvaluator.py#L26-L271)[ïƒ?](#sentence_transformers.evaluation.TripletEvaluator "Link to this definition")

:   Evaluate a model based on a triplet: (sentence, positive_example, negative_example). Checks if [`similarity(sentence,`]` `[`positive_example)`]` `[`>`]` `[`similarity(sentence,`]` `[`negative_example)`]` `[`+`]` `[`margin`].

    Parameters[:]

    :   - **anchors** (*List\[str\]*) â€" Sentences to check similarity to. (e.g. a query)

        - **positives** (*List\[str\]*) â€" List of positive sentences

        - **negatives** (*List\[str\]*) â€" List of negative sentences

        - **main_similarity_function** (*Union\[str,* [*SimilarityFunction*](../sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")*\],* *optional*) â€" The similarity function to use. If not specified, use cosine similarity, dot product, Euclidean, and Manhattan similarity. Defaults to None.

        - **margin** (*Union\[float,* *Dict\[str,* *float\]\],* *optional*) â€" Margins for various similarity metrics. If a float is provided, it will be used as the margin for all similarity metrics. If a dictionary is provided, the keys should be â€˜cosineâ€™, â€˜dotâ€™, â€˜manhattanâ€™, and â€˜euclideanâ€™. The value specifies the minimum margin by which the negative sample should be further from the anchor than the positive sample. Defaults to None.

        - **name** (*str*) â€" Name for the output. Defaults to â€œâ€?.

        - **batch_size** (*int*) â€" Batch size used to compute embeddings. Defaults to 16.

        - **show_progress_bar** (*bool*) â€" If true, prints a progress bar. Defaults to False.

        - **write_csv** (*bool*) â€" Write results to a CSV file. Defaults to True.

        - **truncate_dim** (*int,* *optional*) â€" The dimension to truncate sentence embeddings to. None uses the modelâ€™s current truncation dimension. Defaults to None.

        - **similarity_fn_names** (*List\[str\],* *optional*) â€" List of similarity function names to evaluate. If not specified, evaluate using the [`model.similarity_fn_name`]. Defaults to None.

    Example

    :::: 
    ::: highlight
        from sentence_transformers import SentenceTransformer
        from sentence_transformers.evaluation import TripletEvaluator
        from datasets import load_dataset

        # Load a model
        model = SentenceTransformer('all-mpnet-base-v2')

        # Load a dataset with (anchor, positive, negative) triplets
        dataset = load_dataset("sentence-transformers/all-nli", "triplet", split="dev")

        # Initialize the TripletEvaluator using anchors, positives, and negatives
        triplet_evaluator = TripletEvaluator(
            anchors=dataset[:1000]["anchor"],
            positives=dataset[:1000]["positive"],
            negatives=dataset[:1000]["negative"],
            name="all_nli_dev",
        )
        results = triplet_evaluator(model)
        '''
        TripletEvaluator: Evaluating the model on the all-nli-dev dataset:
        Accuracy Cosine Similarity:        95.60%
        '''
        print(triplet_evaluator.primary_metric)
        # => "all_nli_dev_cosine_accuracy"
        print(results[triplet_evaluator.primary_metric])
        # => 0.956
    :::
    ::::