# Source: https://www.sbert.net/docs/package_reference/sparse_encoder/search_engines.html

# Search Engines[ïƒ?](#search-engines "Link to this heading")

[`sentence_transformers.sparse_encoder.search_engines`] defines different helpful functions to integrate with vector databases and search engines the sparse embeddings produced.

[[sentence_transformers.sparse_encoder.search_engines.]][[semantic_search_elasticsearch]][(]*[[query_embeddings_decoded]][[:]][ ][[list][[\[]][list][[\[]][tuple][[\[]][str][[,]][ ][float][[\]]][[\]]][[\]]]]*, *[[corpus_embeddings_decoded]][[:]][ ][[list][[\[]][list][[\[]][tuple][[\[]][str][[,]][ ][float][[\]]][[\]]][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[corpus_index]][[:]][ ][[tuple][[\[]][Elasticsearch][[,]][ ][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[top_k]][[:]][ ][[int]][ ][[=]][ ][[10]]*, *[[output_index]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[\*\*]][[kwargs]][[:]][ ][[Any]]*[)] [[→] [[tuple][[\[]][list][[\[]][list][[\[]][dict][[\[]][str][[,]][ ][int][ ][[\|]][ ][float][[\]]][[\]]][[\]]][[,]][ ][float][[\]]][ ][[\|]][ ][tuple][[\[]][list][[\[]][list][[\[]][dict][[\[]][str][[,]][ ][int][ ][[\|]][ ][float][[\]]][[\]]][[\]]][[,]][ ][float][[,]][ ][tuple][[\[]][Elasticsearch][[,]][ ][str][[\]]][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\sparse_encoder\search_engines.py#L160-L296)[ïƒ?](#sentence_transformers.sparse_encoder.search_engines.semantic_search_elasticsearch "Link to this definition")

:   Performs semantic search using sparse embeddings with Elasticsearch.

    Parameters[:]

    :   - **query_embeddings_decoded** â€"

          List of query embeddings in format \[\[(â€œtokenâ€?: value), â€¦\], â€¦\] Example: To get this format from a SparseEncoder model:

          :::: 
          ::: highlight
              model = SparseEncoder('my-sparse-model')
              query_texts = ["your query text"]
              query_embeddings = model.encode(query_texts)
              query_embeddings_decoded = model.decode(query_embeddings)
          :::
          ::::

        - **corpus_embeddings_decoded** â€" List of corpus embeddings in format \[\[(â€œtokenâ€?: value), â€¦\], â€¦\] Only used if corpus_index is None Can be obtained using the same decode method as query embeddings

        - **corpus_index** â€" Tuple of (Elasticsearch, collection_name) If provided, uses this existing index for search

        - **top_k** â€" Number of top results to retrieve

        - **output_index** â€" Whether to return the Elasticsearch client and collection name

    Returns[:]

    :   - List of search results in format \[\[, â€¦\], â€¦\]

        - Time taken for search

        - (Optional) Tuple of (Elasticsearch, collection_name) if output_index is True

    Return type[:]

    :   A tuple containing

<!-- -->

[[sentence_transformers.sparse_encoder.search_engines.]][[semantic_search_opensearch]][(]*[[query_embeddings_decoded]][[:]][ ][[list][[\[]][list][[\[]][tuple][[\[]][str][[,]][ ][float][[\]]][[\]]][[\]]]]*, *[[corpus_embeddings_decoded]][[:]][ ][[list][[\[]][list][[\[]][tuple][[\[]][str][[,]][ ][float][[\]]][[\]]][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[corpus_index]][[:]][ ][[tuple][[\[]][OpenSearch][[,]][ ][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[top_k]][[:]][ ][[int]][ ][[=]][ ][[10]]*, *[[output_index]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[\*\*]][[kwargs]][[:]][ ][[Any]]*[)] [[→] [[tuple][[\[]][list][[\[]][list][[\[]][dict][[\[]][str][[,]][ ][int][ ][[\|]][ ][float][[\]]][[\]]][[\]]][[,]][ ][float][[\]]][ ][[\|]][ ][tuple][[\[]][list][[\[]][list][[\[]][dict][[\[]][str][[,]][ ][int][ ][[\|]][ ][float][[\]]][[\]]][[\]]][[,]][ ][float][[,]][ ][tuple][[\[]][OpenSearch][[,]][ ][str][[\]]][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\sparse_encoder\search_engines.py#L428-L555)[ïƒ?](#sentence_transformers.sparse_encoder.search_engines.semantic_search_opensearch "Link to this definition")

:   Performs semantic search using sparse embeddings with OpenSearch.

    Parameters[:]

    :   - **query_embeddings_decoded** â€"

          List of query embeddings in format \[\[(â€œtokenâ€?: value), â€¦\], â€¦\] Example: To get this format from a SparseEncoder model:

          :::: 
          ::: highlight
              model = SparseEncoder('my-sparse-model')
              query_texts = ["your query text"]
              query_embeddings = model.encode(query_texts)
              query_embeddings_decoded = model.decode(query_embeddings)
          :::
          ::::

        - **corpus_embeddings_decoded** â€" List of corpus embeddings in format \[\[(â€œtokenâ€?: value), â€¦\], â€¦\] Only used if corpus_index is None Can be obtained using the same decode method as query embeddings

        - **corpus_index** â€" Tuple of (OpenSearch, collection_name) If provided, uses this existing index for search

        - **top_k** â€" Number of top results to retrieve

        - **output_index** â€" Whether to return the OpenSearch client and collection name

        - **vocab** â€" The dict to transform tokens into token ids

    Returns[:]

    :   - List of search results in format \[\[, â€¦\], â€¦\]

        - Time taken for search

        - (Optional) Tuple of (OpenSearch, collection_name) if output_index is True

    Return type[:]

    :   A tuple containing

<!-- -->

[[sentence_transformers.sparse_encoder.search_engines.]][[semantic_search_qdrant]][(]*[[query_embeddings]][[:]][ ][[[torch.Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]*, *[[corpus_embeddings]][[:]][ ][[[torch.Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[corpus_index]][[:]][ ][[tuple][[\[]][QdrantClient][[,]][ ][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[top_k]][[:]][ ][[int]][ ][[=]][ ][[10]]*, *[[output_index]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[\*\*]][[kwargs]][[:]][ ][[Any]]*[)] [[→] [[tuple][[\[]][list][[\[]][list][[\[]][dict][[\[]][str][[,]][ ][int][ ][[\|]][ ][float][[\]]][[\]]][[\]]][[,]][ ][float][[\]]][ ][[\|]][ ][tuple][[\[]][list][[\[]][list][[\[]][dict][[\[]][str][[,]][ ][int][ ][[\|]][ ][float][[\]]][[\]]][[\]]][[,]][ ][float][[,]][ ][tuple][[\[]][QdrantClient][[,]][ ][str][[\]]][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\sparse_encoder\search_engines.py#L32-L157)[ïƒ?](#sentence_transformers.sparse_encoder.search_engines.semantic_search_qdrant "Link to this definition")

:   Performs semantic search using sparse embeddings with Qdrant.

    Parameters[:]

    :   - **query_embeddings** â€" PyTorch COO sparse tensor containing query embeddings

        - **corpus_embeddings** â€" PyTorch COO sparse tensor containing corpus embeddings Only used if corpus_index is None

        - **corpus_index** â€" Tuple of (QdrantClient, collection_name) If provided, uses this existing index for search

        - **top_k** â€" Number of top results to retrieve

        - **output_index** â€" Whether to return the Qdrant client and collection name

    Returns[:]

    :   - List of search results in format \[\[, â€¦\], â€¦\]

        - Time taken for search

        - (Optional) Tuple of (QdrantClient, collection_name) if output_index is True

    Return type[:]

    :   A tuple containing

<!-- -->

[[sentence_transformers.sparse_encoder.search_engines.]][[semantic_search_seismic]][(]*[[query_embeddings_decoded]][[:]][ ][[list][[\[]][list][[\[]][tuple][[\[]][str][[,]][ ][float][[\]]][[\]]][[\]]]]*, *[[corpus_embeddings_decoded]][[:]][ ][[list][[\[]][list][[\[]][tuple][[\[]][str][[,]][ ][float][[\]]][[\]]][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[corpus_index]][[:]][ ][[tuple][[\[]][SeismicIndex][[,]][ ][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[top_k]][[:]][ ][[int]][ ][[=]][ ][[10]]*, *[[output_index]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[index_kwargs]][[:]][ ][[dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[search_kwargs]][[:]][ ][[dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[tuple][[\[]][list][[\[]][list][[\[]][dict][[\[]][str][[,]][ ][int][ ][[\|]][ ][float][[\]]][[\]]][[\]]][[,]][ ][float][[\]]][ ][[\|]][ ][tuple][[\[]][list][[\[]][list][[\[]][dict][[\[]][str][[,]][ ][int][ ][[\|]][ ][float][[\]]][[\]]][[\]]][[,]][ ][float][[,]][ ][tuple][[\[]][SeismicIndex][[,]][ ][str][[\]]][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\sparse_encoder\search_engines.py#L299-L425)[ïƒ?](#sentence_transformers.sparse_encoder.search_engines.semantic_search_seismic "Link to this definition")

:   Performs semantic search using sparse embeddings with Seismic.

    Parameters[:]

    :   - **query_embeddings_decoded** â€"

          List of query embeddings in format \[\[(â€œtokenâ€?: value), â€¦\], â€¦\] Example: To get this format from a SparseEncoder model:

          :::: 
          ::: highlight
              model = SparseEncoder('my-sparse-model')
              query_texts = ["your query text"]
              query_embeddings = model.encode(query_texts)
              query_embeddings_decoded = model.decode(query_embeddings)
          :::
          ::::

        - **corpus_embeddings_decoded** â€" List of corpus embeddings in format \[\[(â€œtokenâ€?: value), â€¦\], â€¦\] Only used if corpus_index is None Can be obtained using the same decode method as query embeddings

        - **corpus_index** â€" Tuple of (SeismicIndex, collection_name) If provided, uses this existing index for search

        - **top_k** â€" Number of top results to retrieve

        - **output_index** â€" Whether to return the SeismicIndex client and collection name

        - **index_kwargs** â€" Additional arguments for SeismicIndex passed to build_from_dataset, such as centroid_fraction, min_cluster_size, summary_energy, nknn, knn_path, batched_indexing, or num_threads.

        - **search_kwargs** â€" Additional arguments for SeismicIndex passed to batch_search, such as query_cut, heap_factor, n_knn, sorted, or num_threads. Note: query_cut and heap_factor are set to default values if not provided.

    Returns[:]

    :   - List of search results in format \[\[, â€¦\], â€¦\]

        - Time taken for search

        - (Optional) Tuple of (SeismicIndex, collection_name) if output_index is True

    Return type[:]

    :   A tuple containing