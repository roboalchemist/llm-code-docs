# Source: https://www.sbert.net/docs/package_reference/sparse_encoder/models.html

# Modules[ïƒ?](#modules "Link to this heading")

[`sentence_transformers.sparse_encoder.models`] defines different building blocks, that can be used to create SparseEncoder networks from scratch. For more details, see [[Training Overview]](../../sparse_encoder/training_overview.html). Note that modules from [`sentence_transformers.models`] can also be used for Sparse models, such as [`sentence_transformers.models.Transformer`] from [[SentenceTransformer \> Modules]](../sentence_transformer/models.html)

## SPLADE Pooling[ïƒ?](#splade-pooling "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.models.]][[SpladePooling]][(]*[[pooling_strategy]][[:]][ ][[Literal][[\[]][[\'max\']][[,]][ ][[\'sum\']][[\]]]][ ][[=]][ ][[\'max\']]*, *[[activation_function]][[:]][ ][[Literal][[\[]][[\'relu\']][[,]][ ][[\'log1p_relu\']][[\]]]][ ][[=]][ ][[\'relu\']]*, *[[word_embedding_dimension]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[chunk_size]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\models\SpladePooling.py#L13-L147)[ïƒ?](#sentence_transformers.sparse_encoder.models.SpladePooling "Link to this definition")

:   SPLADE Pooling module for creating the sparse embeddings.

    This module implements the SPLADE pooling mechanism that:

    1.  Takes token logits from a masked language model (MLM).

    2.  Applies a sparse transformation using an activation function followed by log1p (i.e., log(1 + activation(MLM_logits))).

    3.  Applies a pooling strategy max or sum to produce sparse embeddings.

    The resulting embeddings are highly sparse and capture lexical information, making them suitable for efficient information retrieval.

    Parameters[:]

    :   - **pooling_strategy** (*str*) â€"

          Pooling method across token dimensions. Choices:

          > ::: 
          > - sum: Sum pooling (used in original SPLADE see [https://huggingface.co/papers/2107.05720](https://huggingface.co/papers/2107.05720)).
          >
          > - max: Max pooling (used in SPLADEv2 and later models see [https://huggingface.co/papers/2109.10086](https://huggingface.co/papers/2109.10086) or [https://huggingface.co/papers/2205.04733](https://huggingface.co/papers/2205.04733)).
          > :::

        - **activation_function** (*str*) â€"

          Activation function applied before log1p transformation. Choices:

          > ::: 
          > - relu: ReLU activation (standard in all Splade models).
          >
          > - log1p_relu: log(1 + ReLU(x)) variant used in Opensearch Splade models, see [https://huggingface.co/papers/2504.14839](https://huggingface.co/papers/2504.14839).
          > :::

        - **word_embedding_dimension** (*int,* *optional*) â€" Dimensionality of the output embeddings (if needed).

        - **chunk_size** (*int,* *optional*) â€" Chunk size along the sequence length dimension (i.e., number of tokens per chunk). If None, processes entire sequence at once. Using smaller chunks the reduces memory usage but may lower the training and inference speed. Default is None.

## MLM Transformer[ïƒ?](#mlm-transformer "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.models.]][[MLMTransformer]][(]*[[model_name_or_path]][[:]][ ][[str]]*, *[[max_seq_length]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[model_args]][[:]][ ][[dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[tokenizer_args]][[:]][ ][[dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[config_args]][[:]][ ][[dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[cache_dir]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[do_lower_case]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[tokenizer_name_or_path]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[backend]][[:]][ ][[str]][ ][[=]][ ][[\'torch\']]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\models\MLMTransformer.py#L26-L398)[ïƒ?](#sentence_transformers.sparse_encoder.models.MLMTransformer "Link to this definition")

:   MLMTransformer adapts a Masked Language Model (MLM) for sparse encoding applications.

    This class extends the Transformer class to work specifically with models that have a MLM head (like BERT, RoBERTa, etc.) and is designed to be used with SpladePooling for creating SPLADE sparse representations.

    MLMTransformer accesses the MLM prediction head to get vocabulary logits for each token, which are later used by SpladePooling to create sparse lexical representations.

    Parameters[:]

    :   - **model_name_or_path** â€" Hugging Face models name ([https://huggingface.co/models](https://huggingface.co/models))

        - **max_seq_length** â€" Truncate any inputs longer than max_seq_length

        - **model_args** â€" Keyword arguments passed to the Hugging Face MLMTransformers model

        - **tokenizer_args** â€" Keyword arguments passed to the Hugging Face MLMTransformers tokenizer

        - **config_args** â€" Keyword arguments passed to the Hugging Face MLMTransformers config

        - **cache_dir** â€" Cache dir for Hugging Face MLMTransformers to store/load models

        - **do_lower_case** â€" If true, lowercases the input (independent if the model is cased or not)

        - **tokenizer_name_or_path** â€" Name or path of the tokenizer. When None, then model_name_or_path is used

        - **backend** â€" Backend used for model inference. Can be only torch for now for this class.

## SparseAutoEncoder[ïƒ?](#sparseautoencoder "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.models.]][[SparseAutoEncoder]][(]*[[input_dim]][[:]][ ][[int]]*, *[[hidden_dim]][[:]][ ][[int]][ ][[=]][ ][[512]]*, *[[k]][[:]][ ][[int]][ ][[=]][ ][[8]]*, *[[k_aux]][[:]][ ][[int]][ ][[=]][ ][[512]]*, *[[normalize]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[dead_threshold]][[:]][ ][[int]][ ][[=]][ ][[30]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\models\SparseAutoEncoder.py#L33-L236)[ïƒ?](#sentence_transformers.sparse_encoder.models.SparseAutoEncoder "Link to this definition")

:   This module implements the Sparse AutoEncoder architecture based on the paper: Beyond Matryoshka: Revisiting Sparse Coding for Adaptive Representation, [https://huggingface.co/papers/2503.01776](https://huggingface.co/papers/2503.01776)

    This module transforms dense embeddings into sparse representations by:

    1.  Applying a multi-layer feed-forward network

    2.  Applying top-k sparsification to keep only the largest values

    3.  Supporting auxiliary losses for training stability (via k_aux parameter)

    Parameters[:]

    :   - **input_dim** â€" Dimension of the input embeddings.

        - **hidden_dim** â€" Dimension of the hidden layers. Defaults to 512.

        - **k** â€" Number of top values to keep in the final sparse representation. Defaults to 8.

        - **k_aux** â€" Number of top values to keep for auxiliary loss calculation. Defaults to 512.

        - **normalize** â€" Whether to apply layer normalization to the input embeddings. Defaults to False.

        - **dead_threshold** â€" Threshold for dead neurons. Neurons with non-zero activations below this threshold are considered dead. Defaults to 30.

## SparseStaticEmbedding[ïƒ?](#sparsestaticembedding "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.models.]][[SparseStaticEmbedding]][(]*[[tokenizer]][[:]][ ][[PreTrainedTokenizer]]*, *[[weight]][[:]][ ][[[torch.Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[frozen]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\models\SparseStaticEmbedding.py#L24-L228)[ïƒ?](#sentence_transformers.sparse_encoder.models.SparseStaticEmbedding "Link to this definition")

:   SparseStaticEmbedding module for efficient sparse representations.

    This lightweight module computes sparse representations by mapping input tokens to static weights, such as IDF (Inverse Document Frequency) weights. It is designed to encode queries or documents into fixed-size embeddings based on the presence of tokens in the input.

    A common scenario is to use this module for encoding queries, and using a heavier module like SPLADE (MLMTransformer + SpladePooling) for document encoding.

    Parameters[:]

    :   - **tokenizer** (*PreTrainedTokenizer*) â€" PreTrainedTokenizer to tokenize input texts into input IDs.

        - **weight** ([*torch.Tensor*](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)") *\|* *None*) â€" Static weights for vocabulary tokens (e.g., IDF weights), shape should be (vocab_size,). If None, initializes weights to a vector of ones. Default is None.

        - **frozen** (*bool*) â€" Whether the weights should be frozen (not trainable). Default is False.