# Source: https://www.sbert.net/docs/package_reference/sentence_transformer/quantization.html

# quantization[ïƒ?](#quantization "Link to this heading")

[`sentence_transformers.quantization`] defines different helpful functions to perform embedding quantization.

Note

[Embedding Quantization](../../../examples/sentence_transformer/applications/embedding-quantization/README.html) differs from model quantization. The former shrinks the size of embeddings such that semantic search/retrieval is faster and requires less memory and disk space. The latter refers to lowering the precision of the model weights to speed up inference. This page only shows documentation for the former.

[[sentence_transformers.quantization.]][[quantize_embeddings]][(]*[[embeddings]][[:]][ ][[[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][ndarray]]*, *[[precision]][[:]][ ][[Literal][[\[]][[\'float32\']][[,]][ ][[\'int8\']][[,]][ ][[\'uint8\']][[,]][ ][[\'binary\']][[,]][ ][[\'ubinary\']][[\]]]]*, *[[ranges]][[:]][ ][[ndarray][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[calibration_embeddings]][[:]][ ][[ndarray][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[ndarray]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\quantization.py#L371-L442)[ïƒ?](#sentence_transformers.quantization.quantize_embeddings "Link to this definition")

:   Quantizes embeddings to a lower precision. This can be used to reduce the memory footprint and increase the speed of similarity search. The supported precisions are â€œfloat32â€?, â€œint8â€?, â€œuint8â€?, â€œbinaryâ€?, and â€œubinaryâ€?.

    Parameters[:]

    :   - **embeddings** â€" Unquantized (e.g. float) embeddings with to quantize to a given precision

        - **precision** â€" The precision to convert to. Options are â€œfloat32â€?, â€œint8â€?, â€œuint8â€?, â€œbinaryâ€?, â€œubinaryâ€?.

        - **ranges** (*Optional\[np.ndarray\]*) â€" Ranges for quantization of embeddings. This is only used for int8 quantization, where the ranges refers to the minimum and maximum values for each dimension. So, itâ€™s a 2D array with shape (2, embedding_dim). Default is None, which means that the ranges will be calculated from the calibration embeddings.

        - **calibration_embeddings** (*Optional\[np.ndarray\]*) â€" Embeddings used for calibration during quantization. This is only used for int8 quantization, where the calibration embeddings can be used to compute ranges, i.e. the minimum and maximum values for each dimension. Default is None, which means that the ranges will be calculated from the query embeddings. This is not recommended.

    Returns[:]

    :   Quantized embeddings with the specified precision

<!-- -->

[[sentence_transformers.quantization.]][[semantic_search_faiss]][(]*[[query_embeddings]][[:]][ ][[np.ndarray]]*, *[[corpus_embeddings]][[:]][ ][[np.ndarray][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[corpus_index]][[:]][ ][[faiss.Index][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[corpus_precision]][[:]][ ][[Literal][[\[]][[\'float32\']][[,]][ ][[\'uint8\']][[,]][ ][[\'ubinary\']][[\]]]][ ][[=]][ ][[\'float32\']]*, *[[top_k]][[:]][ ][[int]][ ][[=]][ ][[10]]*, *[[ranges]][[:]][ ][[np.ndarray][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[calibration_embeddings]][[:]][ ][[np.ndarray][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[rescore]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[rescore_multiplier]][[:]][ ][[int]][ ][[=]][ ][[2]]*, *[[exact]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[output_index]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)] [[→] [[tuple][[\[]][list][[\[]][list][[\[]][dict][[\[]][str][[,]][ ][int][ ][[\|]][ ][float][[\]]][[\]]][[\]]][[,]][ ][float][[,]][ ][faiss.Index][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\quantization.py#L18-L182)[ïƒ?](#sentence_transformers.quantization.semantic_search_faiss "Link to this definition")

:   Performs semantic search using the FAISS library.

    Rescoring will be performed if: 1. rescore is True 2. The query embeddings are not quantized 3. The corpus is quantized, i.e. the corpus precision is not float32 Only if these conditions are true, will we search for top_k \* rescore_multiplier samples and then rescore to only keep top_k.

    Parameters[:]

    :   - **query_embeddings** â€" Embeddings of the query sentences. Ideally not quantized to allow for rescoring.

        - **corpus_embeddings** â€" Embeddings of the corpus sentences. Either corpus_embeddings or corpus_index should be used, not both. The embeddings can be quantized to â€œint8â€? or â€œbinaryâ€? for more efficient search.

        - **corpus_index** â€" FAISS index for the corpus sentences. Either corpus_embeddings or corpus_index should be used, not both.

        - **corpus_precision** â€" Precision of the corpus embeddings. The options are â€œfloat32â€?, â€œint8â€?, or â€œbinaryâ€?. Default is â€œfloat32â€?.

        - **top_k** â€" Number of top results to retrieve. Default is 10.

        - **ranges** â€" Ranges for quantization of embeddings. This is only used for int8 quantization, where the ranges refers to the minimum and maximum values for each dimension. So, itâ€™s a 2D array with shape (2, embedding_dim). Default is None, which means that the ranges will be calculated from the calibration embeddings.

        - **calibration_embeddings** â€" Embeddings used for calibration during quantization. This is only used for int8 quantization, where the calibration embeddings can be used to compute ranges, i.e. the minimum and maximum values for each dimension. Default is None, which means that the ranges will be calculated from the query embeddings. This is not recommended.

        - **rescore** â€" Whether to perform rescoring. Note that rescoring still will only be used if the query embeddings are not quantized and the corpus is quantized, i.e. the corpus precision is not â€œfloat32â€?. Default is True.

        - **rescore_multiplier** â€" Oversampling factor for rescoring. The code will now search top_k \* rescore_multiplier samples and then rescore to only keep top_k. Default is 2.

        - **exact** â€" Whether to use exact search or approximate search. Default is True.

        - **output_index** â€" Whether to output the FAISS index used for the search. Default is False.

    Returns[:]

    :   A tuple containing a list of search results and the time taken for the search. If output_index is True, the tuple will also contain the FAISS index used for the search.

    Raises[:]

    :   **ValueError** â€" If both corpus_embeddings and corpus_index are provided or if neither is provided.

    The list of search results is in the format: \[\[, â€¦\], â€¦\] The time taken for the search is a float value.

<!-- -->

[[sentence_transformers.quantization.]][[semantic_search_usearch]][(]*[[query_embeddings]][[:]][ ][[np.ndarray]]*, *[[corpus_embeddings]][[:]][ ][[np.ndarray][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[corpus_index]][[:]][ ][[usearch.index.Index][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[corpus_precision]][[:]][ ][[Literal][[\[]][[\'float32\']][[,]][ ][[\'int8\']][[,]][ ][[\'binary\']][[\]]]][ ][[=]][ ][[\'float32\']]*, *[[top_k]][[:]][ ][[int]][ ][[=]][ ][[10]]*, *[[ranges]][[:]][ ][[np.ndarray][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[calibration_embeddings]][[:]][ ][[np.ndarray][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[rescore]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[rescore_multiplier]][[:]][ ][[int]][ ][[=]][ ][[2]]*, *[[exact]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[output_index]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)] [[→] [[tuple][[\[]][list][[\[]][list][[\[]][dict][[\[]][str][[,]][ ][int][ ][[\|]][ ][float][[\]]][[\]]][[\]]][[,]][ ][float][[,]][ ][usearch.index.Index][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\quantization.py#L185-L368)[ïƒ?](#sentence_transformers.quantization.semantic_search_usearch "Link to this definition")

:   Performs semantic search using the usearch library.

    Rescoring will be performed if: 1. rescore is True 2. The query embeddings are not quantized 3. The corpus is quantized, i.e. the corpus precision is not float32 Only if these conditions are true, will we search for top_k \* rescore_multiplier samples and then rescore to only keep top_k.

    Parameters[:]

    :   - **query_embeddings** â€" Embeddings of the query sentences. Ideally not quantized to allow for rescoring.

        - **corpus_embeddings** â€" Embeddings of the corpus sentences. Either corpus_embeddings or corpus_index should be used, not both. The embeddings can be quantized to â€œint8â€? or â€œbinaryâ€? for more efficient search.

        - **corpus_index** â€" usearch index for the corpus sentences. Either corpus_embeddings or corpus_index should be used, not both.

        - **corpus_precision** â€" Precision of the corpus embeddings. The options are â€œfloat32â€?, â€œint8â€?, â€œubinaryâ€? or â€œbinaryâ€?. Default is â€œfloat32â€?.

        - **top_k** â€" Number of top results to retrieve. Default is 10.

        - **ranges** â€" Ranges for quantization of embeddings. This is only used for int8 quantization, where the ranges refers to the minimum and maximum values for each dimension. So, itâ€™s a 2D array with shape (2, embedding_dim). Default is None, which means that the ranges will be calculated from the calibration embeddings.

        - **calibration_embeddings** â€" Embeddings used for calibration during quantization. This is only used for int8 quantization, where the calibration embeddings can be used to compute ranges, i.e. the minimum and maximum values for each dimension. Default is None, which means that the ranges will be calculated from the query embeddings. This is not recommended.

        - **rescore** â€" Whether to perform rescoring. Note that rescoring still will only be used if the query embeddings are not quantized and the corpus is quantized, i.e. the corpus precision is not â€œfloat32â€?. Default is True.

        - **rescore_multiplier** â€" Oversampling factor for rescoring. The code will now search top_k \* rescore_multiplier samples and then rescore to only keep top_k. Default is 2.

        - **exact** â€" Whether to use exact search or approximate search. Default is True.

        - **output_index** â€" Whether to output the usearch index used for the search. Default is False.

    Returns[:]

    :   A tuple containing a list of search results and the time taken for the search. If output_index is True, the tuple will also contain the usearch index used for the search.

    Raises[:]

    :   **ValueError** â€" If both corpus_embeddings and corpus_index are provided or if neither is provided.

    The list of search results is in the format: \[\[, â€¦\], â€¦\] The time taken for the search is a float value.