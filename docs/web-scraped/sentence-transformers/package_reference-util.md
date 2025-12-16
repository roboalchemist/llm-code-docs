# Source: https://www.sbert.net/docs/package_reference/util.html

# util[ïƒ?](#util "Link to this heading")

[`sentence_transformers.util`] defines different helpful functions to work with text embeddings.

[]

## Helper Functions[ïƒ?](#module-sentence_transformers.util "Link to this heading")

[[sentence_transformers.util.]][[community_detection]][(]*[[embeddings]][[:]][ ][[[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][ndarray]]*, *[[threshold]][[:]][ ][[float]][ ][[=]][ ][[0.75]]*, *[[min_community_size]][[:]][ ][[int]][ ][[=]][ ][[10]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[1024]]*, *[[show_progress_bar]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)] [[→] [[list][[\[]][list][[\[]][int][[\]]][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\util\retrieval.py#L258-L357)[ïƒ?](#sentence_transformers.util.community_detection "Link to this definition")

:   Function for Fast Community Detection.

    Finds in the embeddings all communities, i.e. embeddings that are close (closer than threshold). Returns only communities that are larger than min_community_size. The communities are returned in decreasing order. The first element in each list is the central point in the community.

    Parameters[:]

    :   - **embeddings** ([*torch.Tensor*](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)") *or* *numpy.ndarray*) â€" The input embeddings.

        - **threshold** (*float*) â€" The threshold for determining if two embeddings are close. Defaults to 0.75.

        - **min_community_size** (*int*) â€" The minimum size of a community to be considered. Defaults to 10.

        - **batch_size** (*int*) â€" The batch size for computing cosine similarity scores. Defaults to 1024.

        - **show_progress_bar** (*bool*) â€" Whether to show a progress bar during computation. Defaults to False.

    Returns[:]

    :   A list of communities, where each community is represented as a list of indices.

    Return type[:]

    :   List\[List\[int\]\]

<!-- -->

[[sentence_transformers.util.]][[http_get]][(]*[[url]][[:]][ ][[str]]*, *[[path]][[:]][ ][[str]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\util\file_io.py#L160-L194)[ïƒ?](#sentence_transformers.util.http_get "Link to this definition")

:   Downloads a URL to a given path on disk.

    Parameters[:]

    :   - **url** (*str*) â€" The URL to download.

        - **path** (*str*) â€" The path to save the downloaded file.

    Raises[:]

    :   **requests.HTTPError** â€" If the HTTP request returns a non-200 status code.

    Returns[:]

    :   None

<!-- -->

[[sentence_transformers.util.]][[is_training_available]][(][)] [[→] [[bool]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\util\environment.py#L71-L76)[ïƒ?](#sentence_transformers.util.is_training_available "Link to this definition")

:   Returns True if we have the required dependencies for training Sentence Transformers models, i.e. Huggingface datasets and Huggingface accelerate.

<!-- -->

[[sentence_transformers.util.]][[mine_hard_negatives]][(]*[[dataset]][[:]][ ][[Dataset]]*, *[[model]][[:]][ ][[[SentenceTransformer]](sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")]*, *[[anchor_column_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[positive_column_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[corpus]][[:]][ ][[list][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[cross_encoder]][[:]][ ][[[CrossEncoder]](cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[range_min]][[:]][ ][[int]][ ][[=]][ ][[0]]*, *[[range_max]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[max_score]][[:]][ ][[float][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[min_score]][[:]][ ][[float][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[absolute_margin]][[:]][ ][[float][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[relative_margin]][[:]][ ][[float][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[num_negatives]][[:]][ ][[int]][ ][[=]][ ][[3]]*, *[[sampling_strategy]][[:]][ ][[Literal][[\[]][[\'random\']][[,]][ ][[\'top\']][[\]]]][ ][[=]][ ][[\'top\']]*, *[[query_prompt_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[query_prompt]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[corpus_prompt_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[corpus_prompt]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[include_positives]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[output_format]][[:]][ ][[Literal][[\[]][[\'triplet\']][[,]][ ][[\'n-tuple\']][[,]][ ][[\'labeled-pair\']][[,]][ ][[\'labeled-list\']][[\]]]][ ][[=]][ ][[\'triplet\']]*, *[[output_scores]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[faiss_batch_size]][[:]][ ][[int]][ ][[=]][ ][[16384]]*, *[[use_faiss]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[use_multi_process]][[:]][ ][[list][[\[]][str][[\]]][ ][[\|]][ ][bool]][ ][[=]][ ][[False]]*, *[[verbose]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[cache_folder]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[as_triplets]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[margin]][[:]][ ][[float][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[Dataset]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\util\hard_negatives.py#L25-L851)[ïƒ?](#sentence_transformers.util.mine_hard_negatives "Link to this definition")

:   Add hard negatives to a dataset of (anchor, positive) pairs to create (anchor, positive, negative) triplets or (anchor, positive, negative_1, â€¦, negative_n) tuples.

    Hard negative mining is a technique to improve the quality of a dataset by adding hard negatives, which are texts that may appear similar to the anchor, but are not. Using hard negatives can improve the performance of models trained on the dataset.

    This function uses a SentenceTransformer model to embed the sentences in the dataset, and then finds the closest matches to each anchor sentence in the dataset. It then samples negatives from the closest matches, optionally using a CrossEncoder model to rescore the candidates.

    Supports prompt formatting for models that expect specific instruction-style input.

    You can influence the candidate negative selection in various ways:

    - **range_min**: Minimum rank of the closest matches to consider as negatives: useful to skip the most similar texts to avoid marking texts as negative that are actually positives.

    - **range_max**: Maximum rank of the closest matches to consider as negatives: useful to limit the number of candidates to sample negatives from. A lower value makes processing faster, but may result in less candidate negatives that satisfy the margin or max_score conditions.

    - **max_score**: Maximum score to consider as a negative: useful to skip candidates that are too similar to the anchor.

    - **min_score**: Minimum score to consider as a negative: useful to skip candidates that are too dissimilar to the anchor.

    - **absolute_margin**: Absolute margin for hard negative mining: useful to skip candidate negatives whose similarity to the anchor is within a certain margin of the positive pair. A value of 0 can be used to enforce that the negative is always further away from the anchor than the positive.

    - **relative_margin**: Relative margin for hard negative mining: useful to skip candidate negatives whose similarity to the anchor is within a certain margin of the positive pair. A value of 0.05 means that the negative is at most 95% as similar to the anchor as the positive.

    - **sampling_strategy**: Sampling strategy for negatives: â€œtopâ€? or â€œrandomâ€?. â€œtopâ€? will always sample the top n candidates as negatives, while â€œrandomâ€? will sample n negatives randomly from the candidates that satisfy the margin or max_score conditions.

    ::::: 
    Tip

    The excellent [NV-Retriever paper](https://huggingface.co/papers/2407.15831) is a great resource for understanding the details of hard negative mining and how to use it effectively. Notably, it reaches the strongest performance using these settings:

    :::: 
    ::: highlight
        dataset = mine_hard_negatives(
            dataset=dataset,
            model=model,
            relative_margin=0.05,         # 0.05 means that the negative is at most 95% as similar to the anchor as the positive
            num_negatives=num_negatives,  # 10 or less is recommended
            sampling_strategy="top",      # "top" means that we sample the top candidates as negatives
            batch_size=batch_size,        # Adjust as needed
            use_faiss=True,               # Optional: Use faiss/faiss-gpu for faster similarity search
        )
    :::
    ::::

    This corresponds with the TopK-PercPos (95%) mining method.
    :::::

    Example

    :::: 
    ::: highlight
        >>> from sentence_transformers.util import mine_hard_negatives
        >>> from sentence_transformers import SentenceTransformer
        >>> from datasets import load_dataset
        >>> # Load a Sentence Transformer model
        >>> model = SentenceTransformer("all-MiniLM-L6-v2")
        >>>
        >>> # Load a dataset to mine hard negatives from
        >>> dataset = load_dataset("sentence-transformers/natural-questions", split="train")
        >>> dataset
        Dataset()
        >>> dataset = mine_hard_negatives(
        ...     dataset=dataset,
        ...     model=model,
        ...     range_min=10,
        ...     range_max=50,
        ...     max_score=0.8,
        ...     relative_margin=0.05,
        ...     num_negatives=5,
        ...     sampling_strategy="random",
        ...     batch_size=128,
        ...     use_faiss=True,
        ... )
        Batches: 100%|ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 588/588 [00:32<00:00, 18.07it/s]
        Batches: 100%|ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 784/784 [00:08<00:00, 96.41it/s]
        Querying FAISS index: 100%|âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 7/7 [00:06<00:00,  1.06it/s]
        Negative candidates mined, preparing dataset...
        Metric       Positive       Negative     Difference
        Count         100,231        487,865
        Mean           0.6866         0.4194         0.2752
        Median         0.7010         0.4102         0.2760
        Std            0.1125         0.0719         0.1136
        Min            0.0303         0.1702         0.0209
        25%            0.6221         0.3672         0.1899
        50%            0.7010         0.4102         0.2760
        75%            0.7667         0.4647         0.3590
        Max            0.9584         0.7621         0.7073
        Skipped 427,503 potential negatives (8.36%) due to the relative_margin of 0.05.
        Skipped 978 potential negatives (0.02%) due to the max_score of 0.8.
        Could not find enough negatives for 13290 samples (2.65%). Consider adjusting the range_max, range_min, relative_margin and max_score parameters if you'd like to find more valid negatives.
        >>> dataset
        Dataset()
        >>> dataset[0]
        
        >>> # To include similarity scores, use output_scores=True
        >>> dataset_with_scores = mine_hard_negatives(
        ...     dataset=dataset,
        ...     model=model,
        ...     output_scores=True,
        ...     # ... other parameters
        ... )
        >>> dataset_with_scores
        Dataset()
        >>> dataset.push_to_hub("natural-questions-hard-negatives", "triplet-all")
    :::
    ::::

    Parameters[:]

    :   - **dataset** (*Dataset*) â€" A dataset containing (anchor, positive) pairs.

        - **model** ([*SentenceTransformer*](sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")) â€" A SentenceTransformer model to use for embedding the sentences.

        - **anchor_column_name** (*str,* *optional*) â€" The column name in dataset that contains the anchor/query. Defaults to None, in which case the first column in dataset will be used.

        - **positive_column_name** (*str,* *optional*) â€" The column name in dataset that contains the positive candidates. Defaults to None, in which case the second column in dataset will be used.

        - **corpus** (*List\[str\],* *optional*) â€" A list containing documents as strings that will be used as candidate negatives in addition to the second column in dataset. Defaults to None, in which case the second column in dataset will exclusively be used as the negative candidate corpus.

        - **cross_encoder** ([*CrossEncoder*](cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")*,* *optional*) â€" A CrossEncoder model to use for rescoring the candidates. Defaults to None.

        - **range_min** (*int*) â€" Minimum rank of the closest matches to consider as negatives. Defaults to 0.

        - **range_max** (*int,* *optional*) â€" Maximum rank of the closest matches to consider as negatives. Defaults to None.

        - **max_score** (*float,* *optional*) â€" Maximum score to consider as a negative. Defaults to None.

        - **min_score** (*float,* *optional*) â€" Minimum score to consider as a negative. Defaults to None.

        - **absolute_margin** (*float,* *optional*) â€" Absolute margin for hard negative mining, i.e. the minimum distance between the positive similarity and the negative similarity. Defaults to None.

        - **relative_margin** (*float,* *optional*) â€" Relative margin for hard negative mining, i.e. the maximum ratio between the positive similarity and the negative similarity. A value of 0.05 means that the negative is at most 95% as similar to the anchor as the positive. Defaults to None.

        - **num_negatives** (*int*) â€" Number of negatives to sample. Defaults to 3.

        - **sampling_strategy** (*Literal\[\"random\",* *\"top\"\]*) â€" Sampling strategy for negatives: â€œtopâ€? or â€œrandomâ€?. Defaults to â€œtopâ€?.

        - **query_prompt_name** (*Optional\[str\],* *optional*) â€"

          The name of a predefined prompt to use when encoding the first/anchor dataset column. It must match a key in the [`model.prompts`] dictionary, which can be set during model initialization or loaded from the model configuration.

          For example, if [`query_prompt_name="query"`] and the model prompts dictionary includes , then the sentence â€œWhat is the capital of France?â€? is transformed into: â€œquery: What is the capital of France?â€? before encoding. This is useful for models that were trained or fine-tuned with specific prompt formats.

          Ignored if [`query_prompt`] is provided. Defaults to None.

        - **query_prompt** (*Optional\[str\],* *optional*) â€"

          A raw prompt string to prepend directly to the first/anchor dataset column during encoding.

          For instance, query_prompt=â€?query: â€œ transforms the sentence â€œWhat is the capital of France?â€? into: â€œquery: What is the capital of France?â€?. Use this to override the prompt logic entirely and supply your own prefix. This takes precedence over [`query_prompt_name`]. Defaults to None.

        - **corpus_prompt_name** (*Optional\[str\],* *optional*) â€" The name of a predefined prompt to use when encoding the corpus. See [`query_prompt_name`] for more information. Defaults to None.

        - **corpus_prompt** (*Optional\[str\],* *optional*) â€" A raw prompt string to prepend directly to the corpus during encoding. See [`query_prompt`] for more information. Defaults to None.

        - **include_positives** (*bool*) â€" Whether to include the positives in the negative candidates. Setting this to True is primarily useful for creating Reranking evaluation datasets for CrossEncoder models, where it can be useful to get a full ranking (including the positives) from a first-stage retrieval model. Defaults to False.

        - **output_format** (*Literal\[\"triplet\",* *\"n-tuple\",* *\"labeled-pair\",* *\"labeled-list\"\]*) â€"

          Output format for the datasets.Dataset. When [`output_scores=False`] (default), options are:

          - â€?tripletâ€?: (anchor, positive, negative) triplets, i.e. 3 columns. Useful for e.g. [[`CachedMultipleNegativesRankingLoss`]](cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.CachedMultipleNegativesRankingLoss "sentence_transformers.cross_encoder.losses.CachedMultipleNegativesRankingLoss").

          - â€?n-tupleâ€?: (anchor, positive, negative_1, â€¦, negative_n) tuples, i.e. 2 + num_negatives columns. Useful for e.g. [[`CachedMultipleNegativesRankingLoss`]](cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.CachedMultipleNegativesRankingLoss "sentence_transformers.cross_encoder.losses.CachedMultipleNegativesRankingLoss").

          - â€?labeled-pairâ€?: (anchor, passage, label) text tuples with a label of 0 for negative and 1 for positive, i.e. 3 columns. Useful for e.g. [[`BinaryCrossEntropyLoss`]](cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss "sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss").

          - â€?labeled-listâ€?: (anchor, \[doc1, doc2, â€¦, docN\], \[label1, label2, â€¦, labelN\]) tuples with labels of 0 for negative and 1 for positive, i.e. 3 columns. Useful for e.g. [[`LambdaLoss`]](cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.LambdaLoss "sentence_transformers.cross_encoder.losses.LambdaLoss").

          Defaults to â€œtripletâ€?. See [`output_scores`] for the output formats when [`output_scores=True`].

        - **output_scores** (*bool*) â€" Whether to include similarity scores in the output dataset. When True, adds score fields to the output: - For â€œtripletâ€? format: adds scores column with query-positive and query-negative similarity scores, for 4 columns total. - For â€œn-tupleâ€? format: adds scores column with a list of similarity scores for the query-positive and each of the query-negative pairs, for 3 + num_negatives columns total. Useful for e.g. [[`SparseMarginMSELoss`]](sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.SparseMarginMSELoss "sentence_transformers.sparse_encoder.losses.SparseMarginMSELoss"). - For â€œlabeled-pairâ€? format: replaces the label column with a score column. Labels are binary (1 for positive, 0 for negative), but scores contain the actual similarity scores computed by the model or cross_encoder. The output has 3 columns. - For â€œlabeled-listâ€? format: replaces the labels column with a scores column. Labels are binary (1 for positive, 0 for negative), but scores contain the actual similarity scores computed by the model or cross_encoder. The output has 3 columns. Defaults to False.

        - **batch_size** (*int*) â€" Batch size for encoding the dataset. Defaults to 32.

        - **faiss_batch_size** (*int*) â€" Batch size for FAISS top-k search. Defaults to 16384.

        - **use_faiss** (*bool*) â€" Whether to use FAISS for similarity search. May be recommended for large datasets. Defaults to False.

        - **use_multi_process** (*bool* *\|* *List\[str\],* *optional*) â€" Whether to use multi-GPU/CPU processing. If True, uses all GPUs if CUDA is available, and 4 CPU processes if itâ€™s not available. You can also pass a list of PyTorch devices like \[â€œcuda:0â€?, â€œcuda:1â€?, â€¦\] or \[â€œcpuâ€?, â€œcpuâ€?, â€œcpuâ€?, â€œcpuâ€?\].

        - **verbose** (*bool*) â€" Whether to print statistics and logging. Defaults to True.

        - **cache_folder** (*str,* *optional*) â€" Directory path for caching embeddings. If provided, the function will save [`query_embeddings_.npy`] and [`corpus_embeddings_.npy`] under this folder after the first run, and on subsequent calls will load from these files if they exist to avoid recomputation. The hashes are computed based on the model name and the queries/corpus. Defaults to None.

        - **as_triplets** (*bool,* *optional*) â€" Deprecated. Use output_format instead. Defaults to None.

        - **margin** (*float,* *optional*) â€" Deprecated. Use absolute_margin or relative_margin instead. Defaults to None.

    Returns[:]

    :   A dataset containing the specified output format. If output_scores=False (default), the formats are:

        - â€?tripletâ€?: (anchor, positive, negative)

        - â€?n-tupleâ€?: (anchor, positive, negative_1, â€¦, negative_n)

        - â€?labeled-pairâ€?: (anchor, passage, label)

        - â€?labeled-listâ€?: (anchor, \[passages\], \[labels\])

        And if output_scores=True, the formats are:

        - â€?tripletâ€?: (anchor, positive, negative, \[scores\])

        - â€?n-tupleâ€?: (anchor, positive, negative_1, â€¦, negative_n, \[scores\])

        - â€?labeled-pairâ€?: (anchor, passage, score)

        - â€?labeled-listâ€?: (anchor, \[passages\], \[scores\])

    Return type[:]

    :   Dataset

<!-- -->

[[sentence_transformers.util.]][[normalize_embeddings]][(]*[[embeddings]][[:]][ ][[[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]*[)] [[→] [[[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\util\tensor.py#L68-L94)[ïƒ?](#sentence_transformers.util.normalize_embeddings "Link to this definition")

:   Normalizes the embeddings matrix, so that each sentence embedding has unit length.

    Parameters[:]

    :   **embeddings** (*Tensor*) â€" The input embeddings matrix.

    Returns[:]

    :   The normalized embeddings matrix.

    Return type[:]

    :   Tensor

<!-- -->

[[sentence_transformers.util.]][[paraphrase_mining]][(]*[model:] [SentenceTransformer,] [sentences:] [list\[str\],] [show_progress_bar:] [bool] [=] [False,] [batch_size:] [int] [=] [32,] [query_chunk_size:] [int] [=] [5000,] [corpus_chunk_size:] [int] [=] [100000,] [max_pairs:] [int] [=] [500000,] [top_k:] [int] [=] [100,] [score_function:] [Callable\[\[Tensor,] [Tensor\],] [Tensor\]] [=] [\<function] [cos_sim\>,] [truncate_dim:] [int] [\|] [None] [=] [None,] [prompt_name:] [str] [\|] [None] [=] [None,] [prompt:] [str] [\|] [None] [=] [None]*[)] [[→] [[list][[\[]][list][[\[]][float][ ][[\|]][ ][int][[\]]][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\util\retrieval.py#L23-L86)[ïƒ?](#sentence_transformers.util.paraphrase_mining "Link to this definition")

:   Given a list of sentences / texts, this function performs paraphrase mining. It compares all sentences against all other sentences and returns a list with the pairs that have the highest cosine similarity score.

    Parameters[:]

    :   - **model** ([*SentenceTransformer*](sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")) â€" SentenceTransformer model for embedding computation

        - **sentences** (*List\[str\]*) â€" A list of strings (texts or sentences)

        - **show_progress_bar** (*bool,* *optional*) â€" Plotting of a progress bar. Defaults to False.

        - **batch_size** (*int,* *optional*) â€" Number of texts that are encoded simultaneously by the model. Defaults to 32.

        - **query_chunk_size** (*int,* *optional*) â€" Search for most similar pairs for #query_chunk_size at the same time. Decrease, to lower memory footprint (increases run-time). Defaults to 5000.

        - **corpus_chunk_size** (*int,* *optional*) â€" Compare a sentence simultaneously against #corpus_chunk_size other sentences. Decrease, to lower memory footprint (increases run-time). Defaults to 100000.

        - **max_pairs** (*int,* *optional*) â€" Maximal number of text pairs returned. Defaults to 500000.

        - **top_k** (*int,* *optional*) â€" For each sentence, we retrieve up to top_k other sentences. Defaults to 100.

        - **score_function** (*Callable\[\[Tensor,* *Tensor\],* *Tensor\],* *optional*) â€" Function for computing scores. By default, cosine similarity. Defaults to cos_sim.

        - **truncate_dim** (*int,* *optional*) â€" The dimension to truncate sentence embeddings to. If None, uses the modelâ€™s ones. Defaults to None.

        - **prompt_name** (*Optional\[str\],* *optional*) â€"

          The name of a predefined prompt to use when encoding the sentence. It must match a key in the model prompts dictionary, which can be set during model initialization or loaded from the model configuration.

          Ignored if prompt is provided. Defaults to None.

        - **prompt** (*Optional\[str\],* *optional*) â€"

          A raw prompt string to prepend directly to the input sentence during encoding.

          For instance, prompt=â€?query: â€œ transforms the sentence â€œWhat is the capital of France?â€? into: â€œquery: What is the capital of France?â€?. Use this to override the prompt logic entirely and supply your own prefix. This takes precedence over prompt_name. Defaults to None.

    Returns[:]

    :   Returns a list of triplets with the format \[score, id1, id2\]

    Return type[:]

    :   List\[List\[Union\[float, int\]\]\]

<!-- -->

[[sentence_transformers.util.]][[semantic_search]][(]*[query_embeddings:] [\~torch.Tensor,] [corpus_embeddings:] [\~torch.Tensor,] [query_chunk_size:] [int] [=] [100,] [corpus_chunk_size:] [int] [=] [500000,] [top_k:] [int] [=] [10,] [score_function:] [\~collections.abc.Callable\[\[\~torch.Tensor,] [\~torch.Tensor\],] [\~torch.Tensor\]] [=] [\<function] [cos_sim\>]*[)] [[→] [[list][[\[]][list][[\[]][dict][[\[]][str][[,]][ ][int][ ][[\|]][ ][float][[\]]][[\]]][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\util\retrieval.py#L167-L255)[ïƒ?](#sentence_transformers.util.semantic_search "Link to this definition")

:   This function performs by default a cosine similarity search between a list of query embeddings and a list of corpus embeddings. It can be used for Information Retrieval / Semantic Search for corpora up to about 1 Million entries.

    Parameters[:]

    :   - **query_embeddings** ([[`Tensor`]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")) â€" A 2 dimensional tensor with the query embeddings. Can be a sparse tensor.

        - **corpus_embeddings** ([[`Tensor`]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")) â€" A 2 dimensional tensor with the corpus embeddings. Can be a sparse tensor.

        - **query_chunk_size** (*int,* *optional*) â€" Process 100 queries simultaneously. Increasing that value increases the speed, but requires more memory. Defaults to 100.

        - **corpus_chunk_size** (*int,* *optional*) â€" Scans the corpus 100k entries at a time. Increasing that value increases the speed, but requires more memory. Defaults to 500000.

        - **top_k** (*int,* *optional*) â€" Retrieve top k matching entries. Defaults to 10.

        - **score_function** (Callable\[\[[[`Tensor`]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)"), [[`Tensor`]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")\], [[`Tensor`]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")\], optional) â€" Function for computing scores. By default, cosine similarity.

    Returns[:]

    :   A list with one entry for each query. Each entry is a list of dictionaries with the keys â€˜corpus_idâ€™ and â€˜scoreâ€™, sorted by decreasing cosine similarity scores.

    Return type[:]

    :   List\[List\[Dict\[str, Union\[int, float\]\]\]\]

<!-- -->

[[sentence_transformers.util.]][[truncate_embeddings]][(]*[[embeddings]][[:]][ ][[ndarray][ ][[\|]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]*, *[[truncate_dim]][[:]][ ][[int][ ][[\|]][ ][None]]*[)] [[→] [[ndarray][ ][[\|]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\util\tensor.py#L105-L134)[ïƒ?](#sentence_transformers.util.truncate_embeddings "Link to this definition")

:   Truncates the embeddings matrix.

    Parameters[:]

    :   - **embeddings** (*Union\[np.ndarray,* [*torch.Tensor*](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")*\]*) â€" Embeddings to truncate.

        - **truncate_dim** (*Optional\[int\]*) â€" The dimension to truncate sentence embeddings to. None does no truncation.

    Example

    :::: 
    ::: highlight
        >>> from sentence_transformers import SentenceTransformer
        >>> from sentence_transformers.util import truncate_embeddings
        >>> model = SentenceTransformer("tomaarsen/mpnet-base-nli-matryoshka")
        >>> embeddings = model.encode(["It's so nice outside!", "Today is a beautiful day.", "He drove to work earlier"])
        >>> embeddings.shape
        (3, 768)
        >>> model.similarity(embeddings, embeddings)
        tensor([[1.0000, 0.8100, 0.1426],
                [0.8100, 1.0000, 0.2121],
                [0.1426, 0.2121, 1.0000]])
        >>> truncated_embeddings = truncate_embeddings(embeddings, 128)
        >>> truncated_embeddings.shape
        >>> model.similarity(truncated_embeddings, truncated_embeddings)
        tensor([[1.0000, 0.8092, 0.1987],
                [0.8092, 1.0000, 0.2716],
                [0.1987, 0.2716, 1.0000]])
    :::
    ::::

    Returns[:]

    :   Truncated embeddings.

    Return type[:]

    :   Union\[np.ndarray, [torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")\]

[]

## Model Optimization[ïƒ?](#module-sentence_transformers.backend "Link to this heading")

[[sentence_transformers.backend.]][[export_dynamic_quantized_onnx_model]][(]*[[model]][[:]][ ][[[SentenceTransformer]](sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")[ ][[\|]][ ][[SparseEncoder]](sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder")[ ][[\|]][ ][[CrossEncoder]](cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")]*, *[[quantization_config]][[:]][ ][[QuantizationConfig][ ][[\|]][ ][Literal][[\[]][[\'arm64\']][[,]][ ][[\'avx2\']][[,]][ ][[\'avx512\']][[,]][ ][[\'avx512_vnni\']][[\]]]]*, *[[model_name_or_path]][[:]][ ][[str]]*, *[[push_to_hub]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[create_pr]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[file_suffix]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\backend\quantize.py#L24-L121)[ïƒ?](#sentence_transformers.backend.export_dynamic_quantized_onnx_model "Link to this definition")

:   Export a quantized ONNX model from a SentenceTransformer, SparseEncoder, or CrossEncoder model.

    This function applies dynamic quantization, i.e. without a calibration dataset. Each of the default quantization configurations quantize the model to int8, allowing for faster inference on CPUs, but are likely slower on GPUs.

    See the following pages for more information & benchmarks:

    - [Sentence Transformer \> Usage \> Speeding up Inference](https://sbert.net/docs/sentence_transformer/usage/efficiency.html)

    - [Cross Encoder \> Usage \> Speeding up Inference](https://sbert.net/docs/cross_encoder/usage/efficiency.html)

    Parameters[:]

    :   - **model** ([*SentenceTransformer*](sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer") *\|* [*SparseEncoder*](sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder") *\|* [*CrossEncoder*](cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")) â€" The SentenceTransformer, SparseEncoder, or CrossEncoder model to be quantized. Must be loaded with backend=â€?onnxâ€?.

        - **quantization_config** (*QuantizationConfig*) â€" The quantization configuration.

        - **model_name_or_path** (*str*) â€" The path or Hugging Face Hub repository name where the quantized model will be saved.

        - **push_to_hub** (*bool,* *optional*) â€" Whether to push the quantized model to the Hugging Face Hub. Defaults to False.

        - **create_pr** (*bool,* *optional*) â€" Whether to create a pull request when pushing to the Hugging Face Hub. Defaults to False.

        - **file_suffix** (*str* *\|* *None,* *optional*) â€" The suffix to add to the quantized model file name. Defaults to None.

    Raises[:]

    :   - **ImportError** â€" If the required packages optimum and onnxruntime are not installed.

        - **ValueError** â€" If the provided model is not a valid SentenceTransformer, SparseEncoder, or CrossEncoder model loaded with backend=â€?onnxâ€?.

        - **ValueError** â€" If the provided quantization_config is not valid.

    Returns[:]

    :   None

<!-- -->

[[sentence_transformers.backend.]][[export_optimized_onnx_model]][(]*[[model]][[:]][ ][[[SentenceTransformer]](sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")[ ][[\|]][ ][[SparseEncoder]](sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder")[ ][[\|]][ ][[CrossEncoder]](cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")]*, *[[optimization_config]][[:]][ ][[OptimizationConfig][ ][[\|]][ ][Literal][[\[]][[\'O1\']][[,]][ ][[\'O2\']][[,]][ ][[\'O3\']][[,]][ ][[\'O4\']][[\]]]]*, *[[model_name_or_path]][[:]][ ][[str]]*, *[[push_to_hub]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[create_pr]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[file_suffix]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\backend\optimize.py#L19-L120)[ïƒ?](#sentence_transformers.backend.export_optimized_onnx_model "Link to this definition")

:   Export an optimized ONNX model from a SentenceTransformer, SparseEncoder, or CrossEncoder model.

    The O1-O4 optimization levels are defined by Optimum and are documented here: [https://huggingface.co/docs/optimum/main/en/onnxruntime/usage_guides/optimization](https://huggingface.co/docs/optimum/main/en/onnxruntime/usage_guides/optimization)

    The optimization levels are:

    - O1: basic general optimizations.

    - O2: basic and extended general optimizations, transformers-specific fusions.

    - O3: same as O2 with GELU approximation.

    - O4: same as O3 with mixed precision (fp16, GPU-only)

    See the following pages for more information & benchmarks:

    - [Sentence Transformer \> Usage \> Speeding up Inference](https://sbert.net/docs/sentence_transformer/usage/efficiency.html)

    - [Cross Encoder \> Usage \> Speeding up Inference](https://sbert.net/docs/cross_encoder/usage/efficiency.html)

    Parameters[:]

    :   - **model** ([*SentenceTransformer*](sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer") *\|* [*SparseEncoder*](sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder") *\|* [*CrossEncoder*](cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")) â€" The SentenceTransformer, SparseEncoder, or CrossEncoder model to be optimized. Must be loaded with backend=â€?onnxâ€?.

        - **optimization_config** (*OptimizationConfig* *\|* *Literal\[\"O1\",* *\"O2\",* *\"O3\",* *\"O4\"\]*) â€" The optimization configuration or level.

        - **model_name_or_path** (*str*) â€" The path or Hugging Face Hub repository name where the optimized model will be saved.

        - **push_to_hub** (*bool,* *optional*) â€" Whether to push the optimized model to the Hugging Face Hub. Defaults to False.

        - **create_pr** (*bool,* *optional*) â€" Whether to create a pull request when pushing to the Hugging Face Hub. Defaults to False.

        - **file_suffix** (*str* *\|* *None,* *optional*) â€" The suffix to add to the optimized model file name. Defaults to None.

    Raises[:]

    :   - **ImportError** â€" If the required packages optimum and onnxruntime are not installed.

        - **ValueError** â€" If the provided model is not a valid SentenceTransformer, SparseEncoder, or CrossEncoder model loaded with backend=â€?onnxâ€?.

        - **ValueError** â€" If the provided optimization_config is not valid.

    Returns[:]

    :   None

<!-- -->

[[sentence_transformers.backend.]][[export_static_quantized_openvino_model]][(]*[[model]][[:]][ ][[[SentenceTransformer]](sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")[ ][[\|]][ ][[SparseEncoder]](sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder")[ ][[\|]][ ][[CrossEncoder]](cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")]*, *[[quantization_config]][[:]][ ][[OVQuantizationConfig][ ][[\|]][ ][dict][ ][[\|]][ ][None]]*, *[[model_name_or_path]][[:]][ ][[str]]*, *[[dataset_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[dataset_config_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[dataset_split]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[column_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[push_to_hub]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[create_pr]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[file_suffix]][[:]][ ][[str]][ ][[=]][ ][[\'qint8_quantized\']]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\backend\quantize.py#L124-L254)[ïƒ?](#sentence_transformers.backend.export_static_quantized_openvino_model "Link to this definition")

:   Export a quantized OpenVINO model from a SentenceTransformer, SparseEncoder, or CrossEncoder model.

    This function applies Post-Training Static Quantization (PTQ) using a calibration dataset, which calibrates quantization constants without requiring model retraining. Each default quantization configuration converts the model to int8 precision, enabling faster inference while maintaining accuracy.

    See the following pages for more information & benchmarks:

    - [Sentence Transformer \> Usage \> Speeding up Inference](https://sbert.net/docs/sentence_transformer/usage/efficiency.html)

    - [Cross Encoder \> Usage \> Speeding up Inference](https://sbert.net/docs/cross_encoder/usage/efficiency.html)

    Parameters[:]

    :   - **model** ([*SentenceTransformer*](sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer") *\|* [*SparseEncoder*](sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder") *\|* [*CrossEncoder*](cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")) â€" The SentenceTransformer, SparseEncoder, or CrossEncoder model to be quantized. Must be loaded with backend=â€?openvinoâ€?.

        - **quantization_config** (*OVQuantizationConfig* *\|* *dict* *\|* *None*) â€" The quantization configuration. If None, default values are used.

        - **model_name_or_path** (*str*) â€" The path or Hugging Face Hub repository name where the quantized model will be saved.

        - **dataset_name** (*str,* *optional*) â€" The name of the dataset to load for calibration. If not specified, the sst2 subset of the glue dataset will be used by default.

        - **dataset_config_name** (*str,* *optional*) â€" The specific configuration of the dataset to load.

        - **dataset_split** (*str,* *optional*) â€" The split of the dataset to load (e.g., â€˜trainâ€™, â€˜testâ€™). Defaults to None.

        - **column_name** (*str,* *optional*) â€" The column name in the dataset to use for calibration. Defaults to None.

        - **push_to_hub** (*bool,* *optional*) â€" Whether to push the quantized model to the Hugging Face Hub. Defaults to False.

        - **create_pr** (*bool,* *optional*) â€" Whether to create a pull request when pushing to the Hugging Face Hub. Defaults to False.

        - **file_suffix** (*str,* *optional*) â€" The suffix to add to the quantized model file name. Defaults to qint8_quantized.

    Raises[:]

    :   - **ImportError** â€" If the required packages optimum and openvino are not installed.

        - **ValueError** â€" If the provided model is not a valid SentenceTransformer, SparseEncoder, or CrossEncoder model loaded with backend=â€?openvinoâ€?.

        - **ValueError** â€" If the provided quantization_config is not valid.

    Returns[:]

    :   None

[]

## Similarity Metrics[ïƒ?](#module-sentence_transformers.util "Link to this heading")

[[sentence_transformers.util.]][[cos_sim]][(]*[[a]][[:]][ ][[list][ ][[\|]][ ][ndarray][ ][[\|]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]*, *[[b]][[:]][ ][[list][ ][[\|]][ ][ndarray][ ][[\|]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]*[)] [[→] [[[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\util\similarity.py#L29-L45)[ïƒ?](#sentence_transformers.util.cos_sim "Link to this definition")

:   Computes the cosine similarity between two tensors.

    Parameters[:]

    :   - **a** (*Union\[list,* *np.ndarray,* *Tensor\]*) â€" The first tensor.

        - **b** (*Union\[list,* *np.ndarray,* *Tensor\]*) â€" The second tensor.

    Returns[:]

    :   Matrix with res\[i\]\[j\] = cos_sim(a\[i\], b\[j\])

    Return type[:]

    :   Tensor

<!-- -->

[[sentence_transformers.util.]][[dot_score]][(]*[[a]][[:]][ ][[list][ ][[\|]][ ][ndarray][ ][[\|]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]*, *[[b]][[:]][ ][[list][ ][[\|]][ ][ndarray][ ][[\|]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]*[)] [[→] [[[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\util\similarity.py#L71-L85)[ïƒ?](#sentence_transformers.util.dot_score "Link to this definition")

:   Computes the dot-product dot_prod(a\[i\], b\[j\]) for all i and j.

    Parameters[:]

    :   - **a** (*Union\[list,* *np.ndarray,* *Tensor\]*) â€" The first tensor.

        - **b** (*Union\[list,* *np.ndarray,* *Tensor\]*) â€" The second tensor.

    Returns[:]

    :   Matrix with res\[i\]\[j\] = dot_prod(a\[i\], b\[j\])

    Return type[:]

    :   Tensor

<!-- -->

[[sentence_transformers.util.]][[euclidean_sim]][(]*[[a]][[:]][ ][[list][ ][[\|]][ ][ndarray][ ][[\|]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]*, *[[b]][[:]][ ][[list][ ][[\|]][ ][ndarray][ ][[\|]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]*[)] [[→] [[[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\util\similarity.py#L149-L177)[ïƒ?](#sentence_transformers.util.euclidean_sim "Link to this definition")

:   Computes the euclidean similarity (i.e., negative distance) between two tensors. Handles sparse tensors without converting to dense when possible.

    Parameters[:]

    :   - **a** (*Union\[list,* *np.ndarray,* *Tensor\]*) â€" The first tensor.

        - **b** (*Union\[list,* *np.ndarray,* *Tensor\]*) â€" The second tensor.

    Returns[:]

    :   Matrix with res\[i\]\[j\] = -euclidean_distance(a\[i\], b\[j\])

    Return type[:]

    :   Tensor

<!-- -->

[[sentence_transformers.util.]][[manhattan_sim]][(]*[[a]][[:]][ ][[list][ ][[\|]][ ][ndarray][ ][[\|]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]*, *[[b]][[:]][ ][[list][ ][[\|]][ ][ndarray][ ][[\|]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]*[)] [[→] [[[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\util\similarity.py#L105-L129)[ïƒ?](#sentence_transformers.util.manhattan_sim "Link to this definition")

:   Computes the manhattan similarity (i.e., negative distance) between two tensors. Handles sparse tensors without converting to dense when possible.

    Parameters[:]

    :   - **a** (*Union\[list,* *np.ndarray,* *Tensor\]*) â€" The first tensor.

        - **b** (*Union\[list,* *np.ndarray,* *Tensor\]*) â€" The second tensor.

    Returns[:]

    :   Matrix with res\[i\]\[j\] = -manhattan_distance(a\[i\], b\[j\])

    Return type[:]

    :   Tensor

<!-- -->

[[sentence_transformers.util.]][[pairwise_cos_sim]][(]*[[a]][[:]][ ][[[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]*, *[[b]][[:]][ ][[[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]*[)] [[→] [[[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\util\similarity.py#L48-L68)[ïƒ?](#sentence_transformers.util.pairwise_cos_sim "Link to this definition")

:   Computes the pairwise cosine similarity cos_sim(a\[i\], b\[i\]).

    Parameters[:]

    :   - **a** (*Union\[list,* *np.ndarray,* *Tensor\]*) â€" The first tensor.

        - **b** (*Union\[list,* *np.ndarray,* *Tensor\]*) â€" The second tensor.

    Returns[:]

    :   Vector with res\[i\] = cos_sim(a\[i\], b\[i\])

    Return type[:]

    :   Tensor

<!-- -->

[[sentence_transformers.util.]][[pairwise_dot_score]][(]*[[a]][[:]][ ][[[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]*, *[[b]][[:]][ ][[[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]*[)] [[→] [[[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\util\similarity.py#L88-L102)[ïƒ?](#sentence_transformers.util.pairwise_dot_score "Link to this definition")

:   Computes the pairwise dot-product dot_prod(a\[i\], b\[i\]).

    Parameters[:]

    :   - **a** (*Union\[list,* *np.ndarray,* *Tensor\]*) â€" The first tensor.

        - **b** (*Union\[list,* *np.ndarray,* *Tensor\]*) â€" The second tensor.

    Returns[:]

    :   Vector with res\[i\] = dot_prod(a\[i\], b\[i\])

    Return type[:]

    :   Tensor

<!-- -->

[[sentence_transformers.util.]][[pairwise_euclidean_sim]][(]*[[a]][[:]][ ][[list][ ][[\|]][ ][ndarray][ ][[\|]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]*, *[[b]][[:]][ ][[list][ ][[\|]][ ][ndarray][ ][[\|]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\util\similarity.py#L180-L194)[ïƒ?](#sentence_transformers.util.pairwise_euclidean_sim "Link to this definition")

:   Computes the euclidean distance (i.e., negative distance) between pairs of tensors.

    Parameters[:]

    :   - **a** (*Union\[list,* *np.ndarray,* *Tensor\]*) â€" The first tensor.

        - **b** (*Union\[list,* *np.ndarray,* *Tensor\]*) â€" The second tensor.

    Returns[:]

    :   Vector with res\[i\] = -euclidean_distance(a\[i\], b\[i\])

    Return type[:]

    :   Tensor

<!-- -->

[[sentence_transformers.util.]][[pairwise_manhattan_sim]][(]*[[a]][[:]][ ][[list][ ][[\|]][ ][ndarray][ ][[\|]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]*, *[[b]][[:]][ ][[list][ ][[\|]][ ][ndarray][ ][[\|]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\util\similarity.py#L132-L146)[ïƒ?](#sentence_transformers.util.pairwise_manhattan_sim "Link to this definition")

:   Computes the manhattan similarity (i.e., negative distance) between pairs of tensors.

    Parameters[:]

    :   - **a** (*Union\[list,* *np.ndarray,* *Tensor\]*) â€" The first tensor.

        - **b** (*Union\[list,* *np.ndarray,* *Tensor\]*) â€" The second tensor.

    Returns[:]

    :   Vector with res\[i\] = -manhattan_distance(a\[i\], b\[i\])

    Return type[:]

    :   Tensor