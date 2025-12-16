# Source: https://www.sbert.net/docs/package_reference/sentence_transformer/models.html

# Modules[ïƒ?](#modules "Link to this heading")

[`sentence_transformers.models`] defines different building blocks, a.k.a. Modules, that can be used to create SentenceTransformer models from scratch. For more details, see [[Creating Custom Models]](../../sentence_transformer/usage/custom_models.html).

## Main Modules[ïƒ?](#main-modules "Link to this heading")

*[class][ ]*[[sentence_transformers.models.]][[Transformer]][(]*[[model_name_or_path]][[:]][ ][[str]]*, *[[max_seq_length]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[model_args]][[:]][ ][[dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[tokenizer_args]][[:]][ ][[dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[config_args]][[:]][ ][[dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[cache_dir]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[do_lower_case]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[tokenizer_name_or_path]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[backend]][[:]][ ][[str]][ ][[=]][ ][[\'torch\']]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\Transformer.py#L38-L470)[ïƒ?](#sentence_transformers.models.Transformer "Link to this definition")

:   Hugging Face AutoModel to generate token embeddings. Loads the correct class, e.g. BERT / RoBERTa etc.

    Parameters[:]

    :   - **model_name_or_path** â€" Hugging Face models name ([https://huggingface.co/models](https://huggingface.co/models))

        - **max_seq_length** â€" Truncate any inputs longer than max_seq_length

        - **model_args** â€" Keyword arguments passed to the Hugging Face Transformers model

        - **tokenizer_args** â€" Keyword arguments passed to the Hugging Face Transformers tokenizer

        - **config_args** â€" Keyword arguments passed to the Hugging Face Transformers config

        - **cache_dir** â€" Cache dir for Hugging Face Transformers to store/load models

        - **do_lower_case** â€" If true, lowercases the input (independent if the model is cased or not)

        - **tokenizer_name_or_path** â€" Name or path of the tokenizer. When None, then model_name_or_path is used

        - **backend** â€" Backend used for model inference. Can be torch, onnx, or openvino. Default is torch.

<!-- -->

*[class][ ]*[[sentence_transformers.models.]][[Pooling]][(]*[[word_embedding_dimension]][[:]][ ][[int]]*, *[[pooling_mode]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[pooling_mode_cls_token]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[pooling_mode_max_tokens]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[pooling_mode_mean_tokens]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[pooling_mode_mean_sqrt_len_tokens]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[pooling_mode_weightedmean_tokens]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[pooling_mode_lasttoken]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[include_prompt]][[:]][ ][[bool]][ ][[=]][ ][[True]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\Pooling.py#L9-L247)[ïƒ?](#sentence_transformers.models.Pooling "Link to this definition")

:   Performs pooling (max or mean) on the token embeddings.

    Using pooling, it generates from a variable sized sentence a fixed sized sentence embedding. This layer also allows to use the CLS token if it is returned by the underlying word embedding model. You can concatenate multiple poolings together.

    Parameters[:]

    :   - **word_embedding_dimension** â€" Dimensions for the word embeddings

        - **pooling_mode** â€" Either â€œclsâ€?, â€œlasttokenâ€?, â€œmaxâ€?, â€œmeanâ€?, â€œmean_sqrt_len_tokensâ€?, or â€œweightedmeanâ€?. If set, overwrites the other pooling_mode\_\* settings

        - **pooling_mode_cls_token** â€" Use the first token (CLS token) as text representations

        - **pooling_mode_max_tokens** â€" Use max in each dimension over all tokens.

        - **pooling_mode_mean_tokens** â€" Perform mean-pooling

        - **pooling_mode_mean_sqrt_len_tokens** â€" Perform mean-pooling, but divide by sqrt(input_length).

        - **pooling_mode_weightedmean_tokens** â€" Perform (position) weighted mean pooling. See [SGPT: GPT Sentence Embeddings for Semantic Search](https://huggingface.co/papers/2202.08904).

        - **pooling_mode_lasttoken** â€"

          Perform last token pooling. See [SGPT: GPT Sentence Embeddings for Semantic Search](https://huggingface.co/papers/2202.08904) and [Text and Code Embeddings by Contrastive Pre-Training](https://huggingface.co/papers/2201.10005).

        - **include_prompt** â€" If set to false, the prompt tokens are not included in the pooling. This is useful for reproducing work that does not include the prompt tokens in the pooling like INSTRUCTOR, but otherwise not recommended.

<!-- -->

*[class][ ]*[[sentence_transformers.models.]][[Dense]][(]*[[in_features]][[:]][ ][[int]]*, *[[out_features]][[:]][ ][[int]]*, *[[bias]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[activation_function]][[:]][ ][[Callable][[\[]][[\[]][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[Tanh()]]*, *[[init_weight]][[:]][ ][[[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[init_bias]][[:]][ ][[[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\Dense.py#L16-L105)[ïƒ?](#sentence_transformers.models.Dense "Link to this definition")

:   Feed-forward function with activation function.

    This layer takes a fixed-sized sentence embedding and passes it through a feed-forward layer. Can be used to generate deep averaging networks (DAN).

    Parameters[:]

    :   - **in_features** â€" Size of the input dimension

        - **out_features** â€" Output size

        - **bias** â€" Add a bias vector

        - **activation_function** â€" Pytorch activation function applied on output

        - **init_weight** â€" Initial value for the matrix of the linear layer

        - **init_bias** â€" Initial value for the bias of the linear layer

<!-- -->

*[class][ ]*[[sentence_transformers.models.]][[Normalize]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\Normalize.py#L14-L29)[ïƒ?](#sentence_transformers.models.Normalize "Link to this definition")

:   This layer normalizes embeddings to unit length

<!-- -->

*[class][ ]*[[sentence_transformers.models.]][[Router]][(]*[[sub_modules]][[:]][ ][[dict][[\[]][str][[,]][ ][list][[\[]][[Module]](#sentence_transformers.models.Module "sentence_transformers.models.Module.Module")[[\]]][[\]]]]*, *[[default_route]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[allow_empty_key]][[:]][ ][[bool]][ ][[=]][ ][[True]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\Router.py#L22-L413)[ïƒ?](#sentence_transformers.models.Router "Link to this definition")

:   This model allows to create asymmetric SentenceTransformer models that apply different modules depending on the specified route, such as â€œqueryâ€? or â€œdocumentâ€?. Especially useful for models that have different encoders for queries and documents.

    Notably, the [`task`] argument of [`model.encode`] can be used to specify which route to use, and [`model.encode_query`] and [`model.encode_document`] are shorthands for using [`task="query"`] and [`task="document"`], respectively. These methods also optionally apply [`prompts`] specific to queries or documents.

    ::::::: 
    Note

    When training models with the [[`Router`]](#sentence_transformers.models.Router "sentence_transformers.models.Router") module, you must use the [`router_mapping`] argument in the [[`SentenceTransformerTrainingArguments`]](training_args.html#sentence_transformers.training_args.SentenceTransformerTrainingArguments "sentence_transformers.training_args.SentenceTransformerTrainingArguments") or [[`SparseEncoderTrainingArguments`]](../sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments "sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments") to map the training dataset columns to the correct route (â€œqueryâ€? or â€œdocumentâ€?). For example, if your training dataset(s) have [`["question",`]` `[`"positive",`]` `[`"negative"]`] columns, then you can use the following mapping:

    :::: 
    ::: highlight
        args = SparseEncoderTrainingArguments(
            ...,
            router_mapping=
        )
    :::
    ::::

    Additionally, it is common to use a different learning rate for the different routes. For this, you should use the [`learning_rate_mapping`] argument in the [[`SentenceTransformerTrainingArguments`]](training_args.html#sentence_transformers.training_args.SentenceTransformerTrainingArguments "sentence_transformers.training_args.SentenceTransformerTrainingArguments") or [[`SparseEncoderTrainingArguments`]](../sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments "sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments") to map parameter patterns to their learning rates. For example, if you want to use a learning rate of [`1e-3`] for an SparseStaticEmbedding module and [`2e-5`] for the rest of the model, you can do this:

    :::: 
    ::: highlight
        args = SparseEncoderTrainingArguments(
            ...,
            learning_rate=2e-5,
            learning_rate_mapping=
        )
    :::
    ::::
    :::::::

    In the below examples, the [`Router`] model is used to create asymmetric models with different encoders for queries and documents. In these examples, the â€œqueryâ€? route is efficient (e.g., using SparseStaticEmbedding), while the â€œdocumentâ€? route uses a more complex model (e.g. a Transformers module). This allows for efficient query encoding while still using a powerful document encoder, but the combinations are not limited to this.

    Example

    :::: 
    ::: highlight
        from sentence_transformers import SentenceTransformer
        from sentence_transformers.models import Router, Normalize

        # Use a regular SentenceTransformer for the document embeddings, and a static embedding model for the query embeddings
        document_embedder = SentenceTransformer("mixedbread-ai/mxbai-embed-large-v1")
        query_embedder = SentenceTransformer("sentence-transformers/static-retrieval-mrl-en-v1")
        router = Router.for_query_document(
            query_modules=list(query_embedder.children()),
            document_modules=list(document_embedder.children()),
        )
        normalize = Normalize()

        # Create an asymmetric model with different encoders for queries and documents
        model = SentenceTransformer(
            modules=[router, normalize],
        )

        # ... requires more training to align the vector spaces

        # Use the query & document routes
        query_embedding = model.encode_query("What is the capital of France?")
        document_embedding = model.encode_document("Paris is the capital of France.")
    :::
    ::::

    :::: 
    ::: highlight
        from sentence_transformers.models import Router
        from sentence_transformers.sparse_encoder import SparseEncoder
        from sentence_transformers.sparse_encoder.models import MLMTransformer, SparseStaticEmbedding, SpladePooling

        # Load an asymmetric model with different encoders for queries and documents
        doc_encoder = MLMTransformer("opensearch-project/opensearch-neural-sparse-encoding-doc-v3-distill")
        router = Router.for_query_document(
            query_modules=[
                SparseStaticEmbedding.from_json(
                    "opensearch-project/opensearch-neural-sparse-encoding-doc-v3-distill",
                    tokenizer=doc_encoder.tokenizer,
                    frozen=True,
                ),
            ],
            document_modules=[
                doc_encoder,
                SpladePooling(pooling_strategy="max", activation_function="log1p_relu"),
            ],
        )

        model = SparseEncoder(modules=[router], similarity_fn_name="dot")

        query = "What's the weather in ny now?"
        document = "Currently New York is rainy."

        query_embed = model.encode_query(query)
        document_embed = model.encode_document(document)

        sim = model.similarity(query_embed, document_embed)
        print(f"Similarity: ")

        # Visualize top tokens for each text
        top_k = 10
        print(f"Top tokens  for each text:")

        decoded_query = model.decode(query_embed, top_k=top_k)
        decoded_document = model.decode(document_embed)

        for i in range(min(top_k, len(decoded_query))):
            query_token, query_score = decoded_query[i]
            doc_score = next((score for token, score in decoded_document if token == query_token), 0)
            if doc_score != 0:
                print(f"Token: , Query score: , Document score: ")

        '''
        Similarity: tensor([[11.1105]], device='cuda:0')
        Top tokens 10 for each text:
        Token: ny, Query score: 5.7729, Document score: 0.8049
        Token: weather, Query score: 4.5684, Document score: 0.9710
        Token: now, Query score: 3.5895, Document score: 0.4720
        Token: ?, Query score: 3.3313, Document score: 0.0286
        Token: what, Query score: 2.7699, Document score: 0.0787
        Token: in, Query score: 0.4989, Document score: 0.0417
        '''
    :::
    ::::

    ::: 
    Note

    These models are not necessarily stronger than non-asymmetric models. Rudimentary experiments indicate that non-Router models perform better in many cases.
    :::

    Parameters[:]

    :   - **sub_modules** â€" Mapping of route keys to lists of modules. Each key corresponds to a specific task type, often â€œqueryâ€? or â€œdocumentâ€?, and the list contains the modules to be applied for that task type.

        - **default_route** â€" The default route to use if no task type is specified. If None, an exception will be thrown if no task type is specified. If [`allow_empty_key`] is True, the first key in sub_modules will be used as the default route. Defaults to None.

        - **allow_empty_key** â€" If True, allows the default route to be set to the first key in sub_modules if [`default_route`] is None. Defaults to True.

    *[classmethod][ ]*[[for_query_document]][(]*[[query_modules]][[:]][ ][[list][[\[]][[Module]](#sentence_transformers.models.Module "sentence_transformers.models.Module.Module")[[\]]]]*, *[[document_modules]][[:]][ ][[list][[\[]][[Module]](#sentence_transformers.models.Module "sentence_transformers.models.Module.Module")[[\]]]]*, *[[default_route]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[allow_empty_key]][[:]][ ][[bool]][ ][[=]][ ][[True]]*[)] [[→] [[Self]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\Router.py#L187-L215)[ïƒ?](#sentence_transformers.models.Router.for_query_document "Link to this definition")

    :   Creates a Router model specifically for query and document modules, allowing convenient usage via model.encode_query and model.encode_document.

        Parameters[:]

        :   - **query_modules** â€" List of modules to be applied for the â€œqueryâ€? task type.

            - **document_modules** â€" List of modules to be applied for the â€œdocumentâ€? task type.

            - **default_route** â€" The default route to use if no task type is specified. If None, an exception will be thrown if no task type is specified. If [`allow_empty_key`] is True, the first key in sub_modules will be used as the default route. Defaults to None.

            - **allow_empty_key** â€" If True, allows the default route to be set to the first key in sub_modules if [`default_route`] is None. Defaults to True.

        Returns[:]

        :   An instance of the Router model with the specified query and document modules.

        Return type[:]

        :   [Router](#sentence_transformers.models.Router "sentence_transformers.models.Router.Router")

<!-- -->

*[class][ ]*[[sentence_transformers.models.]][[StaticEmbedding]][(]*[[tokenizer]][[:]][ ][[Tokenizer][ ][[\|]][ ][PreTrainedTokenizerFast]]*, *[[embedding_weights]][[:]][ ][[ndarray][ ][[\|]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[embedding_dim]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\StaticEmbedding.py#L28-L268)[ïƒ?](#sentence_transformers.models.StaticEmbedding "Link to this definition")

:   Initializes the StaticEmbedding model given a tokenizer. The model is a simple embedding bag model that takes the mean of trained per-token embeddings to compute text embeddings.

    Parameters[:]

    :   - **tokenizer** (*Tokenizer* *\|* *PreTrainedTokenizerFast*) â€" The tokenizer to be used. Must be a fast tokenizer from [`transformers`] or [`tokenizers`].

        - **embedding_weights** (*np.ndarray* *\|* [*torch.Tensor*](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)") *\|* *None,* *optional*) â€" Pre-trained embedding weights. Defaults to None.

        - **embedding_dim** (*int* *\|* *None,* *optional*) â€" Dimension of the embeddings. Required if embedding_weights is not provided. Defaults to None.

    ::: 
    Tip

    Due to the extremely efficient nature of this module architecture, the overhead for moving inputs to the GPU can be larger than the actual computation time. Therefore, consider using a CPU device for inference and training.
    :::

    Example:

    :::: 
    ::: highlight
        from sentence_transformers import SentenceTransformer
        from sentence_transformers.models import StaticEmbedding
        from tokenizers import Tokenizer

        # Pre-distilled embeddings:
        static_embedding = StaticEmbedding.from_model2vec("minishlab/potion-base-8M")
        # or distill your own embeddings:
        static_embedding = StaticEmbedding.from_distillation("BAAI/bge-base-en-v1.5", device="cuda")
        # or start with randomized embeddings:
        tokenizer = Tokenizer.from_pretrained("FacebookAI/xlm-roberta-base")
        static_embedding = StaticEmbedding(tokenizer, embedding_dim=512)

        model = SentenceTransformer(modules=[static_embedding])

        embeddings = model.encode(["What are Pandas?", "The giant panda, also known as the panda bear or simply the panda, is a bear native to south central China."])
        similarity = model.similarity(embeddings[0], embeddings[1])
        # tensor([[0.8093]]) (If you use potion-base-8M)
        # tensor([[0.6234]]) (If you use the distillation method)
        # tensor([[-0.0693]]) (For example, if you use randomized embeddings)
    :::
    ::::

    Raises[:]

    :   - **ValueError** â€" If the tokenizer is not a fast tokenizer.

        - **ValueError** â€" If neither embedding_weights nor embedding_dim is provided.

    *[classmethod][ ]*[[from_distillation]][(]*[[model_name]][[:]][ ][[str]]*, *[[vocabulary]][[:]][ ][[list][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[device]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[pca_dims]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[256]]*, *[[apply_zipf]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[sif_coefficient]][[:]][ ][[float][ ][[\|]][ ][None]][ ][[=]][ ][[0.0001]]*, *[[token_remove_pattern]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[\'\\\\\[unused\\\\d+\\\\\]\']]*, *[[quantize_to]][[:]][ ][[str]][ ][[=]][ ][[\'float32\']]*, *[[use_subword]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[\*\*]][[kwargs]][[:]][ ][[Any]]*[)] [[→] [[[StaticEmbedding]](#sentence_transformers.models.StaticEmbedding "sentence_transformers.models.StaticEmbedding.StaticEmbedding")]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\StaticEmbedding.py#L164-L237)[ïƒ?](#sentence_transformers.models.StaticEmbedding.from_distillation "Link to this definition")

    :   Creates a StaticEmbedding instance from a distillation process using the model2vec package.

        Parameters[:]

        :   - **model_name** (*str*) â€" The name of the model to distill.

            - **vocabulary** (*list\[str\]* *\|* *None,* *optional*) â€" A list of vocabulary words to use. Defaults to None.

            - **device** (*str*) â€" The device to run the distillation on (e.g., â€˜cpuâ€™, â€˜cudaâ€™). If not specified, the strongest device is automatically detected. Defaults to None.

            - **pca_dims** (*int* *\|* *None,* *optional*) â€" The number of dimensions for PCA reduction. Defaults to 256.

            - **apply_zipf** (*bool*) â€" Whether to apply Zipfâ€™s law during distillation. Defaults to True.

            - **sif_coefficient** (*float* *\|* *None,* *optional*) â€" The coefficient for SIF weighting. Defaults to 1e-4.

            - **token_remove_pattern** (*str* *\|* *None,* *optional*) â€" A regex pattern to remove tokens from the vocabulary. Defaults to râ€?\[unusedd+\]â€?.

            - **quantize_to** (*str*) â€" The data type to quantize the weights to. Defaults to â€˜float32â€™.

            - **use_subword** (*bool*) â€" Whether to use subword tokenization. Defaults to True.

        Returns[:]

        :   

            An instance of StaticEmbedding initialized with the distilled modelâ€™s

            :   tokenizer and embedding weights.

        Return type[:]

        :   [StaticEmbedding](#sentence_transformers.models.StaticEmbedding "sentence_transformers.models.StaticEmbedding.StaticEmbedding")

        Raises[:]

        :   **ImportError** â€" If the model2vec package is not installed.

    *[classmethod][ ]*[[from_model2vec]][(]*[[model_id_or_path]][[:]][ ][[str]]*[)] [[→] [[[StaticEmbedding]](#sentence_transformers.models.StaticEmbedding "sentence_transformers.models.StaticEmbedding.StaticEmbedding")]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\StaticEmbedding.py#L239-L268)[ïƒ?](#sentence_transformers.models.StaticEmbedding.from_model2vec "Link to this definition")

    :   Create a StaticEmbedding instance from a model2vec model. This method loads a pre-trained model2vec model and extracts the embedding weights and tokenizer to create a StaticEmbedding instance.

        Parameters[:]

        :   **model_id_or_path** (*str*) â€" The identifier or path to the pre-trained model2vec model.

        Returns[:]

        :   

            An instance of StaticEmbedding initialized with the tokenizer and embedding weights

            :   the model2vec model.

        Return type[:]

        :   [StaticEmbedding](#sentence_transformers.models.StaticEmbedding "sentence_transformers.models.StaticEmbedding.StaticEmbedding")

        Raises[:]

        :   **ImportError** â€" If the model2vec package is not installed.

## Further Modules[ïƒ?](#further-modules "Link to this heading")

*[class][ ]*[[sentence_transformers.models.]][[BoW]][(]*[[vocab]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[word_weights]][[:]][ ][[dict][[\[]][str][[,]][ ][float][[\]]]][ ][[=]][ ][[]]*, *[[unknown_word_weight]][[:]][ ][[float]][ ][[=]][ ][[1]]*, *[[cumulative_term_frequency]][[:]][ ][[bool]][ ][[=]][ ][[True]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\BoW.py#L16-L87)[ïƒ?](#sentence_transformers.models.BoW "Link to this definition")

:   Implements a Bag-of-Words (BoW) model to derive sentence embeddings.

    A weighting can be added to allow the generation of tf-idf vectors. The output vector has the size of the vocab.

<!-- -->

*[class][ ]*[[sentence_transformers.models.]][[CNN]][(]*[[in_word_embedding_dimension]][[:]][ ][[int]]*, *[[out_channels]][[:]][ ][[int]][ ][[=]][ ][[256]]*, *[[kernel_sizes]][[:]][ ][[list][[\[]][int][[\]]]][ ][[=]][ ][[\[1,] [3,] [5\]]]*, *[[stride_sizes]][[:]][ ][[list][[\[]][int][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\CNN.py#L14-L88)[ïƒ?](#sentence_transformers.models.CNN "Link to this definition")

:   CNN-layer with multiple kernel-sizes over the word embeddings

<!-- -->

*[class][ ]*[[sentence_transformers.models.]][[LSTM]][(]*[[word_embedding_dimension]][[:]][ ][[int]]*, *[[hidden_dim]][[:]][ ][[int]]*, *[[num_layers]][[:]][ ][[int]][ ][[=]][ ][[1]]*, *[[dropout]][[:]][ ][[float]][ ][[=]][ ][[0]]*, *[[bidirectional]][[:]][ ][[bool]][ ][[=]][ ][[True]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\LSTM.py#L14-L94)[ïƒ?](#sentence_transformers.models.LSTM "Link to this definition")

:   Bidirectional LSTM running over word embeddings.

<!-- -->

*[class][ ]*[[sentence_transformers.models.]][[WeightedLayerPooling]][(]*[[word_embedding_dimension]]*, *[[num_hidden_layers]][[:]][ ][[int]][ ][[=]][ ][[12]]*, *[[layer_start]][[:]][ ][[int]][ ][[=]][ ][[4]]*, *[[layer_weights]][[=]][[None]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\WeightedLayerPooling.py#L14-L72)[ïƒ?](#sentence_transformers.models.WeightedLayerPooling "Link to this definition")

:   Token embeddings are weighted mean of their different hidden layer representations

<!-- -->

*[class][ ]*[[sentence_transformers.models.]][[WordEmbeddings]][(]*[[tokenizer]][[:]][ ][[WordTokenizer][ ][[\|]][ ][PreTrainedTokenizerBase]]*, *[[embedding_weights]]*, *[[update_embeddings]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[max_seq_length]][[:]][ ][[int]][ ][[=]][ ][[1000000]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\WordEmbeddings.py#L27-L193)[ïƒ?](#sentence_transformers.models.WordEmbeddings "Link to this definition")

:   

<!-- -->

*[class][ ]*[[sentence_transformers.models.]][[WordWeights]][(]*[[vocab]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[word_weights]][[:]][ ][[dict][[\[]][str][[,]][ ][float][[\]]]]*, *[[unknown_word_weight]][[:]][ ][[float]][ ][[=]][ ][[1]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\WordWeights.py#L13-L70)[ïƒ?](#sentence_transformers.models.WordWeights "Link to this definition")

:   This model can weight word embeddings, for example, with idf-values.

    Initializes the WordWeights class.

    Parameters[:]

    :   - **vocab** (*List\[str\]*) â€" Vocabulary of the tokenizer.

        - **word_weights** (*Dict\[str,* *float\]*) â€" Mapping of tokens to a float weight value. Word embeddings are multiplied by this float value. Tokens in word_weights must not be equal to the vocab (can contain more or less values).

        - **unknown_word_weight** (*float,* *optional*) â€" Weight for words in vocab that do not appear in the word_weights lookup. These can be, for example, rare words in the vocab where no weight exists. Defaults to 1.

## Base Modules[ïƒ?](#base-modules "Link to this heading")

*[class][ ]*[[sentence_transformers.models.]][[Module]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\Module.py#L21-L411)[ïƒ?](#sentence_transformers.models.Module "Link to this definition")

:   Base class for all modules in the Sentence Transformers library.

    This class provides a common interface for all modules, including methods for loading and saving the moduleâ€™s configuration and weights. It also provides a method for performing the forward pass of the module.

    Two abstract methods are defined in this class, which must be implemented by subclasses:

    - [[`sentence_transformers.models.Module.forward()`]](#sentence_transformers.models.Module.forward "sentence_transformers.models.Module.forward"): The forward pass of the module.

    - [[`sentence_transformers.models.Module.save()`]](#sentence_transformers.models.Module.save "sentence_transformers.models.Module.save"): Save the module to disk.

    Optionally, you may also have to override:

    - [[`sentence_transformers.models.Module.load()`]](#sentence_transformers.models.Module.load "sentence_transformers.models.Module.load"): Load the module from disk.

    To assist with loading and saving the module, several utility methods are provided:

    - [[`sentence_transformers.models.Module.load_config()`]](#sentence_transformers.models.Module.load_config "sentence_transformers.models.Module.load_config"): Load the moduleâ€™s configuration from a JSON file.

    - [[`sentence_transformers.models.Module.load_file_path()`]](#sentence_transformers.models.Module.load_file_path "sentence_transformers.models.Module.load_file_path"): Load a file from the moduleâ€™s directory, regardless of whether the module is saved locally or on Hugging Face.

    - [[`sentence_transformers.models.Module.load_dir_path()`]](#sentence_transformers.models.Module.load_dir_path "sentence_transformers.models.Module.load_dir_path"): Load a directory from the moduleâ€™s directory, regardless of whether the module is saved locally or on Hugging Face.

    - [[`sentence_transformers.models.Module.load_torch_weights()`]](#sentence_transformers.models.Module.load_torch_weights "sentence_transformers.models.Module.load_torch_weights"): Load the PyTorch weights of the module, regardless of whether the module is saved locally or on Hugging Face.

    - [[`sentence_transformers.models.Module.save_config()`]](#sentence_transformers.models.Module.save_config "sentence_transformers.models.Module.save_config"): Save the moduleâ€™s configuration to a JSON file.

    - [[`sentence_transformers.models.Module.save_torch_weights()`]](#sentence_transformers.models.Module.save_torch_weights "sentence_transformers.models.Module.save_torch_weights"): Save the PyTorch weights of the module.

    - [[`sentence_transformers.models.Module.get_config_dict()`]](#sentence_transformers.models.Module.get_config_dict "sentence_transformers.models.Module.get_config_dict"): Get the moduleâ€™s configuration as a dictionary.

    And several class variables are defined to assist with loading and saving the module:

    - [[`sentence_transformers.models.Module.config_file_name`]](#sentence_transformers.models.Module.config_file_name "sentence_transformers.models.Module.config_file_name"): The name of the configuration file used to save the moduleâ€™s configuration.

    - [[`sentence_transformers.models.Module.config_keys`]](#sentence_transformers.models.Module.config_keys "sentence_transformers.models.Module.config_keys"): A list of keys used to save the moduleâ€™s configuration.

    - [[`sentence_transformers.models.Module.save_in_root`]](#sentence_transformers.models.Module.save_in_root "sentence_transformers.models.Module.save_in_root"): Whether to save the moduleâ€™s configuration in the root directory of the model or in a subdirectory named after the module.

    [[config_file_name]]*[[:]][ ][str][ ][[=]][ ][\'config.json\']*[ïƒ?](#sentence_transformers.models.Module.config_file_name "Link to this definition")

    :   The name of the configuration file used to save the moduleâ€™s configuration. This file is used to initialize the module when loading it from a pre-trained model.

    [[config_keys]]*[[:]][ ][list][[\[]][str][[\]]][ ][[=]][ ][\[\]]*[ïƒ?](#sentence_transformers.models.Module.config_keys "Link to this definition")

    :   A list of keys used to save the moduleâ€™s configuration. These keys are used to save the moduleâ€™s configuration when saving the model to disk.

    *[abstract][ ]*[[forward]][(]*[[features]][[:]][ ][[dict][[\[]][str][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][Any][[\]]]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[dict][[\[]][str][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][Any][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\Module.py#L77-L102)[ïƒ?](#sentence_transformers.models.Module.forward "Link to this definition")

    :   Forward pass of the module. This method should be overridden by subclasses to implement the specific behavior of the module.

        The forward method takes a dictionary of features as input and returns a dictionary of features as output. The keys in the [`features`] dictionary depend on the position of the module in the model pipeline, as the [`features`] dictionary is passed from one module to the next. Common keys in the [`features`] dictionary are:

        > ::: 
        > - [`input_ids`]: The input IDs of the tokens in the input text.
        >
        > - [`attention_mask`]: The attention mask for the input tokens.
        >
        > - [`token_type_ids`]: The token type IDs for the input tokens.
        >
        > - [`token_embeddings`]: The token embeddings for the input tokens.
        >
        > - [`sentence_embedding`]: The sentence embedding for the input text, i.e. pooled token embeddings.
        > :::

        Optionally, the [`forward`] method can accept additional keyword arguments ([`**kwargs`]) that can be used to pass additional information from [`model.encode`] to this module.

        Parameters[:]

        :   - **features** (*dict\[str,* [*torch.Tensor*](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)") *\|* *Any\]*) â€" A dictionary of features to be processed by the module.

            - **\*\*kwargs** â€" Additional keyword arguments that can be used to pass additional information from [`model.encode`].

        Returns[:]

        :   A dictionary of features after processing by the module.

        Return type[:]

        :   dict\[str, [torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)") \| Any\]

    [[get_config_dict]][(][)] [[→] [[dict][[\[]][str][[,]][ ][Any][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\Module.py#L104-L115)[ïƒ?](#sentence_transformers.models.Module.get_config_dict "Link to this definition")

    :   Returns a dictionary of the configuration parameters of the module.

        These parameters are used to save the moduleâ€™s configuration when saving the model to disk, and again used to initialize the module when loading it from a pre-trained model. The keys used in the dictionary are defined in the [`config_keys`] class variable.

        Returns[:]

        :   A dictionary of the configuration parameters of the module.

        Return type[:]

        :   dict\[str, Any\]

    *[classmethod][ ]*[[load]][(]*[[model_name_or_path]][[:]][ ][[str]]*, *[[subfolder]][[:]][ ][[str]][ ][[=]][ ][[\'\']]*, *[[token]][[:]][ ][[bool][ ][[\|]][ ][str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[cache_folder]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[revision]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[local_files_only]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[Self]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\Module.py#L117-L157)[ïƒ?](#sentence_transformers.models.Module.load "Link to this definition")

    :   Load this module from a model checkpoint. The checkpoint can be either a local directory or a model id on Hugging Face.

        Parameters[:]

        :   - **model_name_or_path** (*str*) â€" The path to the model directory or the name of the model on Hugging Face.

            - **subfolder** (*str,* *optional*) â€" The subfolder within the model directory to load from, e.g. [`"1_Pooling"`]. Defaults to [`""`].

            - **token** (*bool* *\|* *str* *\|* *None,* *optional*) â€" The token to use for authentication when loading from Hugging Face. If None, tries to use a token saved using [`huggingface-cli`]` `[`login`] or the [`HF_TOKEN`] environment variable. Defaults to None.

            - **cache_folder** (*str* *\|* *None,* *optional*) â€" The folder to use for caching the model files. If None, uses the default cache folder for Hugging Face, [`~/.cache/huggingface`]. Defaults to None.

            - **revision** (*str* *\|* *None,* *optional*) â€" The revision of the model to load. If None, uses the latest revision. Defaults to None.

            - **local_files_only** (*bool,* *optional*) â€" Whether to only load local files. Defaults to False.

            - **\*\*kwargs** â€" Additional module-specific arguments used in an overridden [`load`] method, such as [`trust_remote_code`], [`model_kwargs`], [`tokenizer_kwargs`], [`config_kwargs`], [`backend`], etc.

        Returns[:]

        :   The loaded module.

        Return type[:]

        :   Self

    *[classmethod][ ]*[[load_config]][(]*[[model_name_or_path]][[:]][ ][[str]]*, *[[subfolder]][[:]][ ][[str]][ ][[=]][ ][[\'\']]*, *[[config_filename]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[token]][[:]][ ][[bool][ ][[\|]][ ][str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[cache_folder]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[revision]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[local_files_only]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)] [[→] [[dict][[\[]][str][[,]][ ][Any][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\Module.py#L159-L207)[ïƒ?](#sentence_transformers.models.Module.load_config "Link to this definition")

    :   Load the configuration of the module from a model checkpoint. The checkpoint can be either a local directory or a model id on Hugging Face. The configuration is loaded from a JSON file, which contains the parameters used to initialize the module.

        Parameters[:]

        :   - **model_name_or_path** (*str*) â€" The path to the model directory or the name of the model on Hugging Face.

            - **subfolder** (*str,* *optional*) â€" The subfolder within the model directory to load from, e.g. [`"1_Pooling"`]. Defaults to [`""`].

            - **config_filename** (*str* *\|* *None,* *optional*) â€" The name of the configuration file to load. If None, uses the default configuration file name defined in the [`config_file_name`] class variable. Defaults to None.

            - **token** (*bool* *\|* *str* *\|* *None,* *optional*) â€" The token to use for authentication when loading from Hugging Face. If None, tries to use a token saved using [`huggingface-cli`]` `[`login`] or the [`HF_TOKEN`] environment variable. Defaults to None.

            - **cache_folder** (*str* *\|* *None,* *optional*) â€" The folder to use for caching the model files. If None, uses the default cache folder for Hugging Face, [`~/.cache/huggingface`]. Defaults to None.

            - **revision** (*str* *\|* *None,* *optional*) â€" The revision of the model to load. If None, uses the latest revision. Defaults to None.

            - **local_files_only** (*bool,* *optional*) â€" Whether to only load local files. Defaults to False.

        Returns[:]

        :   A dictionary of the configuration parameters of the module.

        Return type[:]

        :   dict\[str, Any\]

    *[static][ ]*[[load_dir_path]][(]*[[model_name_or_path]][[:]][ ][[str]]*, *[[subfolder]][[:]][ ][[str]][ ][[=]][ ][[\'\']]*, *[[token]][[:]][ ][[bool][ ][[\|]][ ][str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[cache_folder]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[revision]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[local_files_only]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)] [[→] [[str]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\Module.py#L250-L285)[ïƒ?](#sentence_transformers.models.Module.load_dir_path "Link to this definition")

    :   A utility function to load a directory from a model checkpoint. The checkpoint can be either a local directory or a model id on Hugging Face.

        Parameters[:]

        :   - **model_name_or_path** (*str*) â€" The path to the model directory or the name of the model on Hugging Face.

            - **subfolder** (*str,* *optional*) â€" The subfolder within the model directory to load from, e.g. [`"1_Pooling"`]. Defaults to [`""`].

            - **token** (*bool* *\|* *str* *\|* *None,* *optional*) â€" The token to use for authentication when loading from Hugging Face. If None, tries to use a token saved using [`huggingface-cli`]` `[`login`] or the [`HF_TOKEN`] environment variable. Defaults to None.

            - **cache_folder** (*str* *\|* *None,* *optional*) â€" The folder to use for caching the model files. If None, uses the default cache folder for Hugging Face, [`~/.cache/huggingface`]. Defaults to None.

            - **revision** (*str* *\|* *None,* *optional*) â€" The revision of the model to load. If None, uses the latest revision. Defaults to None.

            - **local_files_only** (*bool,* *optional*) â€" Whether to only load local files. Defaults to False.

        Returns[:]

        :   The path to the loaded directory.

        Return type[:]

        :   str

    *[static][ ]*[[load_file_path]][(]*[[model_name_or_path]][[:]][ ][[str]]*, *[[filename]][[:]][ ][[str]]*, *[[subfolder]][[:]][ ][[str]][ ][[=]][ ][[\'\']]*, *[[token]][[:]][ ][[bool][ ][[\|]][ ][str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[cache_folder]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[revision]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[local_files_only]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)] [[→] [[str][ ][[\|]][ ][None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\Module.py#L209-L248)[ïƒ?](#sentence_transformers.models.Module.load_file_path "Link to this definition")

    :   A utility function to load a file from a model checkpoint. The checkpoint can be either a local directory or a model id on Hugging Face. The file is loaded from the specified subfolder within the model directory.

        Parameters[:]

        :   - **model_name_or_path** (*str*) â€" The path to the model directory or the name of the model on Hugging Face.

            - **filename** (*str*) â€" The name of the file to load.

            - **subfolder** (*str,* *optional*) â€" The subfolder within the model directory to load from, e.g. [`"1_Pooling"`]. Defaults to [`""`].

            - **token** (*bool* *\|* *str* *\|* *None,* *optional*) â€" The token to use for authentication when loading from Hugging Face. If None, tries to use a token saved using [`huggingface-cli`]` `[`login`] or the [`HF_TOKEN`] environment variable. Defaults to None.

            - **cache_folder** (*str* *\|* *None,* *optional*) â€" The folder to use for caching the model files. If None, uses the default cache folder for Hugging Face, [`~/.cache/huggingface`]. Defaults to None.

            - **revision** (*str* *\|* *None,* *optional*) â€" The revision of the model to load. If None, uses the latest revision. Defaults to None.

            - **local_files_only** (*bool,* *optional*) â€" Whether to only load local files. Defaults to False.

        Returns[:]

        :   The path to the loaded file, or None if the file was not found.

        Return type[:]

        :   str \| None

    *[classmethod][ ]*[[load_torch_weights]][(]*[[model_name_or_path]][[:]][ ][[str]]*, *[[subfolder]][[:]][ ][[str]][ ][[=]][ ][[\'\']]*, *[[token]][[:]][ ][[bool][ ][[\|]][ ][str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[cache_folder]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[revision]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[local_files_only]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[model]][[:]][ ][[Self][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\Module.py#L287-L364)[ïƒ?](#sentence_transformers.models.Module.load_torch_weights "Link to this definition")

    :   A utility function to load the PyTorch weights of a model from a checkpoint. The checkpoint can be either a local directory or a model id on Hugging Face. The weights are loaded from either a [`model.safetensors`] file or a [`pytorch_model.bin`] file, depending on which one is available. This method either loads the weights into the model or returns the weights as a state dictionary.

        Parameters[:]

        :   - **model_name_or_path** (*str*) â€" The path to the model directory or the name of the model on Hugging Face.

            - **subfolder** (*str,* *optional*) â€" The subfolder within the model directory to load from, e.g. [`"2_Dense"`]. Defaults to [`""`].

            - **token** (*bool* *\|* *str* *\|* *None,* *optional*) â€" The token to use for authentication when loading from Hugging Face. If None, tries to use a token saved using [`huggingface-cli`]` `[`login`] or the [`HF_TOKEN`] environment variable. Defaults to None.

            - **cache_folder** (*str* *\|* *None,* *optional*) â€" The folder to use for caching the model files. If None, uses the default cache folder for Hugging Face, [`~/.cache/huggingface`]. Defaults to None.

            - **revision** (*str* *\|* *None,* *optional*) â€" The revision of the model to load. If None, uses the latest revision. Defaults to None.

            - **local_files_only** (*bool,* *optional*) â€" Whether to only load local files. Defaults to False.

            - **model** (*Self* *\|* *None,* *optional*) â€" The model to load the weights into. If None, returns the weights as a state dictionary. Defaults to None.

        Raises[:]

        :   **ValueError** â€" If neither a [`model.safetensors`] file nor a [`pytorch_model.bin`] file is found in the model checkpoint in the [`subfolder`].

        Returns[:]

        :   

            The model with the loaded weights or the weights as a state dictionary,

            :   depending on the value of the [`model`] argument.

        Return type[:]

        :   Self \| dict\[str, [torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")\]

    *[abstract][ ]*[[save]][(]*[[output_path]][[:]][ ][[str]]*, *[[\*]][[args]]*, *[[safe_serialization]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\Module.py#L366-L377)[ïƒ?](#sentence_transformers.models.Module.save "Link to this definition")

    :   Save the module to disk. This method should be overridden by subclasses to implement the specific behavior of the module.

        Parameters[:]

        :   - **output_path** (*str*) â€" The path to the directory where the module should be saved.

            - **\*args** â€" Additional arguments that can be used to pass additional information to the save method.

            - **safe_serialization** (*bool,* *optional*) â€" Whether to use the safetensors format for saving the model weights. Defaults to True.

            - **\*\*kwargs** â€" Additional keyword arguments that can be used to pass additional information to the save method.

    [[save_config]][(]*[[output_path]][[:]][ ][[str]]*, *[[filename]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\Module.py#L379-L394)[ïƒ?](#sentence_transformers.models.Module.save_config "Link to this definition")

    :   Save the configuration of the module to a JSON file.

        Parameters[:]

        :   - **output_path** (*str*) â€" The path to the directory where the configuration file should be saved.

            - **filename** (*str* *\|* *None,* *optional*) â€" The name of the configuration file. If None, uses the default configuration file name defined in the [`config_file_name`] class variable. Defaults to None.

        Returns[:]

        :   None

    [[save_in_root]]*[[:]][ ][bool][ ][[=]][ ][False]*[ïƒ?](#sentence_transformers.models.Module.save_in_root "Link to this definition")

    :   Whether to save the moduleâ€™s configuration in the root directory of the model or in a subdirectory named after the module.

    [[save_torch_weights]][(]*[[output_path]][[:]][ ][[str]]*, *[[safe_serialization]][[:]][ ][[bool]][ ][[=]][ ][[True]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\Module.py#L396-L411)[ïƒ?](#sentence_transformers.models.Module.save_torch_weights "Link to this definition")

    :   Save the PyTorch weights of the module to disk.

        Parameters[:]

        :   - **output_path** (*str*) â€" The path to the directory where the weights should be saved.

            - **safe_serialization** (*bool,* *optional*) â€" Whether to use the safetensors format for saving the model weights. Defaults to True.

        Returns[:]

        :   None

<!-- -->

*[class][ ]*[[sentence_transformers.models.]][[InputModule]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\InputModule.py#L13-L92)[ïƒ?](#sentence_transformers.models.InputModule "Link to this definition")

:   Subclass of [[`sentence_transformers.models.Module`]](#sentence_transformers.models.Module "sentence_transformers.models.Module"), base class for all input modules in the Sentence Transformers library, i.e. modules that are used to process inputs and optionally also perform processing in the forward pass.

    This class provides a common interface for all input modules, including methods for loading and saving the moduleâ€™s configuration and weights, as well as input processing. It also provides a method for performing the forward pass of the module.

    Three abstract methods are defined in this class, which must be implemented by subclasses:

    - [[`sentence_transformers.models.Module.forward()`]](#sentence_transformers.models.Module.forward "sentence_transformers.models.Module.forward"): The forward pass of the module.

    - [[`sentence_transformers.models.Module.save()`]](#sentence_transformers.models.Module.save "sentence_transformers.models.Module.save"): Save the module to disk.

    - [[`sentence_transformers.models.InputModule.tokenize()`]](#sentence_transformers.models.InputModule.tokenize "sentence_transformers.models.InputModule.tokenize"): Tokenize the input texts and return a dictionary of tokenized features.

    Optionally, you may also have to override:

    - [[`sentence_transformers.models.Module.load()`]](#sentence_transformers.models.Module.load "sentence_transformers.models.Module.load"): Load the module from disk.

    To assist with loading and saving the module, several utility methods are provided:

    - [[`sentence_transformers.models.Module.load_config()`]](#sentence_transformers.models.Module.load_config "sentence_transformers.models.Module.load_config"): Load the moduleâ€™s configuration from a JSON file.

    - [[`sentence_transformers.models.Module.load_file_path()`]](#sentence_transformers.models.Module.load_file_path "sentence_transformers.models.Module.load_file_path"): Load a file from the moduleâ€™s directory, regardless of whether the module is saved locally or on Hugging Face.

    - [[`sentence_transformers.models.Module.load_dir_path()`]](#sentence_transformers.models.Module.load_dir_path "sentence_transformers.models.Module.load_dir_path"): Load a directory from the moduleâ€™s directory, regardless of whether the module is saved locally or on Hugging Face.

    - [[`sentence_transformers.models.Module.load_torch_weights()`]](#sentence_transformers.models.Module.load_torch_weights "sentence_transformers.models.Module.load_torch_weights"): Load the PyTorch weights of the module, regardless of whether the module is saved locally or on Hugging Face.

    - [[`sentence_transformers.models.Module.save_config()`]](#sentence_transformers.models.Module.save_config "sentence_transformers.models.Module.save_config"): Save the moduleâ€™s configuration to a JSON file.

    - [[`sentence_transformers.models.Module.save_torch_weights()`]](#sentence_transformers.models.Module.save_torch_weights "sentence_transformers.models.Module.save_torch_weights"): Save the PyTorch weights of the module.

    - [[`sentence_transformers.models.InputModule.save_tokenizer()`]](#sentence_transformers.models.InputModule.save_tokenizer "sentence_transformers.models.InputModule.save_tokenizer"): Save the tokenizer used by the module.

    - [[`sentence_transformers.models.Module.get_config_dict()`]](#sentence_transformers.models.Module.get_config_dict "sentence_transformers.models.Module.get_config_dict"): Get the moduleâ€™s configuration as a dictionary.

    And several class variables are defined to assist with loading and saving the module:

    - [[`sentence_transformers.models.Module.config_file_name`]](#sentence_transformers.models.Module.config_file_name "sentence_transformers.models.Module.config_file_name"): The name of the configuration file used to save the moduleâ€™s configuration.

    - [[`sentence_transformers.models.Module.config_keys`]](#sentence_transformers.models.Module.config_keys "sentence_transformers.models.Module.config_keys"): A list of keys used to save the moduleâ€™s configuration.

    - [[`sentence_transformers.models.InputModule.save_in_root`]](#sentence_transformers.models.InputModule.save_in_root "sentence_transformers.models.InputModule.save_in_root"): Whether to save the moduleâ€™s configuration in the root directory of the model or in a subdirectory named after the module.

    - [[`sentence_transformers.models.InputModule.tokenizer`]](#sentence_transformers.models.InputModule.tokenizer "sentence_transformers.models.InputModule.tokenizer"): The tokenizer used by the module.

    [[save_in_root]]*[[:]][ ][bool][ ][[=]][ ][True]*[ïƒ?](#sentence_transformers.models.InputModule.save_in_root "Link to this definition")

    :   Whether to save the moduleâ€™s configuration in the root directory of the model or in a subdirectory named after the module.

    [[save_tokenizer]][(]*[[output_path]][[:]][ ][[str]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\InputModule.py#L74-L92)[ïƒ?](#sentence_transformers.models.InputModule.save_tokenizer "Link to this definition")

    :   Saves the tokenizer to the specified output path.

        Parameters[:]

        :   - **output_path** (*str*) â€" Path to save the tokenizer.

            - **\*\*kwargs** â€" Additional keyword arguments for saving the tokenizer.

        Returns[:]

        :   None

    *[abstract][ ]*[[tokenize]][(]*[[texts]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[dict][[\[]][str][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][Any][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\models\InputModule.py#L60-L72)[ïƒ?](#sentence_transformers.models.InputModule.tokenize "Link to this definition")

    :   Tokenizes the input texts and returns a dictionary of tokenized features.

        Parameters[:]

        :   - **texts** (*list\[str\]*) â€" List of input texts to tokenize.

            - **\*\*kwargs** â€" Additional keyword arguments for tokenization, e.g. [`task`].

        Returns[:]

        :   

            Dictionary containing tokenized features, e.g.

            :   [`]` `[`...,`]` `[`"attention_mask":`]` `[`...}`]

        Return type[:]

        :   dict\[str, [torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)") \| Any\]

    [[tokenizer]]*[[:]][ ][PreTrainedTokenizerBase][ ][[\|]][ ][Tokenizer]*[ïƒ?](#sentence_transformers.models.InputModule.tokenizer "Link to this definition")

    :   The tokenizer used for tokenizing the input texts. It can be either a [[`transformers.PreTrainedTokenizerBase`]](https://huggingface.co/docs/transformers/main/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase "(in transformers vmain)") subclass or a Tokenizer from the [`tokenizers`] library.