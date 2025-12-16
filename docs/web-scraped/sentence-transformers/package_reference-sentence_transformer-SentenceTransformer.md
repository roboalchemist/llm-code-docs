# Source: https://www.sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html

# SentenceTransformer[ïƒ?](#sentencetransformer "Link to this heading")

## SentenceTransformer[ïƒ?](#id1 "Link to this heading")

*[class][ ]*[[sentence_transformers.]][[SentenceTransformer]][(]*[[model_name_or_path]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[modules]][[:]][ ][[Iterable][[\[]][[Module]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[device]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[prompts]][[:]][ ][[dict][[\[]][str][[,]][ ][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[default_prompt_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[similarity_fn_name]][[:]][ ][[str][ ][[\|]][ ][[SimilarityFunction]](../sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.similarity_functions.SimilarityFunction")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[cache_folder]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[trust_remote_code]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[revision]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[local_files_only]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[token]][[:]][ ][[bool][ ][[\|]][ ][str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[use_auth_token]][[:]][ ][[bool][ ][[\|]][ ][str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[truncate_dim]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[model_kwargs]][[:]][ ][[dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[tokenizer_kwargs]][[:]][ ][[dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[config_kwargs]][[:]][ ][[dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[model_card_data]][[:]][ ][[[SentenceTransformerModelCardData]](#sentence_transformers.model_card.SentenceTransformerModelCardData "sentence_transformers.model_card.SentenceTransformerModelCardData")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[backend]][[:]][ ][[Literal][[\[]][[\'torch\']][[,]][ ][[\'onnx\']][[,]][ ][[\'openvino\']][[\]]]][ ][[=]][ ][[\'torch\']]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\SentenceTransformer.py#L61-L2514)[ïƒ?](#sentence_transformers.SentenceTransformer "Link to this definition")

:   Loads or creates a SentenceTransformer model that can be used to map sentences / text to embeddings.

    Parameters[:]

    :   - **model_name_or_path** (*str,* *optional*) â€" If it is a filepath on disk, it loads the model from that path. If it is not a path, it first tries to download a pre-trained SentenceTransformer model. If that fails, tries to construct a model from the Hugging Face Hub with that name.

        - **modules** (*Iterable\[nn.Module\],* *optional*) â€" A list of torch Modules that should be called sequentially, can be used to create custom SentenceTransformer models from scratch.

        - **device** (*str,* *optional*) â€" Device (like â€œcudaâ€?, â€œcpuâ€?, â€œmpsâ€?, â€œnpuâ€?) that should be used for computation. If None, checks if a GPU can be used.

        - **prompts** (*Dict\[str,* *str\],* *optional*) â€" A dictionary with prompts for the model. The key is the prompt name, the value is the prompt text. The prompt text will be prepended before any text to encode. For example:  or .

        - **default_prompt_name** (*str,* *optional*) â€" The name of the prompt that should be used by default. If not set, no prompt will be applied.

        - **similarity_fn_name** (*str* *or* [*SimilarityFunction*](../sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")*,* *optional*) â€" The name of the similarity function to use. Valid options are â€œcosineâ€?, â€œdotâ€?, â€œeuclideanâ€?, and â€œmanhattanâ€?. If not set, it is automatically set to â€œcosineâ€? if similarity or similarity_pairwise are called while model.similarity_fn_name is still None.

        - **cache_folder** (*str,* *optional*) â€" Path to store models. Can also be set by the SENTENCE_TRANSFORMERS_HOME environment variable.

        - **trust_remote_code** (*bool,* *optional*) â€" Whether or not to allow for custom models defined on the Hub in their own modeling files. This option should only be set to True for repositories you trust and in which you have read the code, as it will execute code present on the Hub on your local machine.

        - **revision** (*str,* *optional*) â€" The specific model version to use. It can be a branch name, a tag name, or a commit id, for a stored model on Hugging Face.

        - **local_files_only** (*bool,* *optional*) â€" Whether or not to only look at local files (i.e., do not try to download the model).

        - **token** (*bool* *or* *str,* *optional*) â€" Hugging Face authentication token to download private models.

        - **use_auth_token** (*bool* *or* *str,* *optional*) â€" Deprecated argument. Please use token instead.

        - **truncate_dim** (*int,* *optional*) â€" The dimension to truncate sentence embeddings to. Defaults to None.

        - **model_kwargs** (*Dict\[str,* *Any\],* *optional*) â€"

          Additional model configuration parameters to be passed to the Hugging Face Transformers model. Particularly useful options are:

          - [`torch_dtype`]: Override the default torch.dtype and load the model under a specific dtype. The different options are:

            > ::: 
            > 1\. [`torch.float16`], [`torch.bfloat16`] or [`torch.float`]: load in a specified [`dtype`], ignoring the modelâ€™s [`config.torch_dtype`] if one exists. If not specified - the model will get loaded in [`torch.float`] (fp32).
            >
            > 2\. [`"auto"`] - A [`torch_dtype`] entry in the [`config.json`] file of the model will be attempted to be used. If this entry isnâ€™t found then next check the [`dtype`] of the first weight in the checkpoint thatâ€™s of a floating point type and use that as [`dtype`]. This will load the model using the [`dtype`] it was saved in at the end of the training. It canâ€™t be used as an indicator of how the model was trained. Since it could be trained in one of half precision dtypes, but saved in fp32.
            > :::

          - [`attn_implementation`]: The attention implementation to use in the model (if relevant). Can be any of â€œeagerâ€? (manual implementation of the attention), â€œsdpaâ€? (using [F.scaled_dot_product_attention](https://pytorch.org/docs/master/generated/torch.nn.functional.scaled_dot_product_attention.html)), or â€œflash_attention_2â€? (using [Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention)). By default, if available, SDPA will be used for torch\>=2.1.1. The default is otherwise the manual â€œeagerâ€? implementation.

          - [`provider`]: If backend is â€œonnxâ€?, this is the provider to use for inference, for example â€œCPUExecutionProviderâ€?, â€œCUDAExecutionProviderâ€?, etc. See [https://onnxruntime.ai/docs/execution-providers/](https://onnxruntime.ai/docs/execution-providers/) for all ONNX execution providers.

          - [`file_name`]: If backend is â€œonnxâ€? or â€œopenvinoâ€?, this is the file name to load, useful for loading optimized or quantized ONNX or OpenVINO models.

          - [`export`]: If backend is â€œonnxâ€? or â€œopenvinoâ€?, then this is a boolean flag specifying whether this model should be exported to the backend. If not specified, the model will be exported only if the model repository or directory does not already contain an exported model.

          See the [PreTrainedModel.from_pretrained](https://huggingface.co/docs/transformers/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) documentation for more details.

        - **tokenizer_kwargs** (*Dict\[str,* *Any\],* *optional*) â€" Additional tokenizer configuration parameters to be passed to the Hugging Face Transformers tokenizer. See the [AutoTokenizer.from_pretrained](https://huggingface.co/docs/transformers/en/model_doc/auto#transformers.AutoTokenizer.from_pretrained) documentation for more details.

        - **config_kwargs** (*Dict\[str,* *Any\],* *optional*) â€" Additional model configuration parameters to be passed to the Hugging Face Transformers config. See the [AutoConfig.from_pretrained](https://huggingface.co/docs/transformers/en/model_doc/auto#transformers.AutoConfig.from_pretrained) documentation for more details.

        - **model_card_data** ([[`SentenceTransformerModelCardData`]](#sentence_transformers.model_card.SentenceTransformerModelCardData "sentence_transformers.model_card.SentenceTransformerModelCardData"), optional) â€" A model card data object that contains information about the model. This is used to generate a model card when saving the model. If not set, a default model card data object is created.

        - **backend** (*str*) â€" The backend to use for inference. Can be one of â€œtorchâ€? (default), â€œonnxâ€?, or â€œopenvinoâ€?. See [https://sbert.net/docs/sentence_transformer/usage/efficiency.html](https://sbert.net/docs/sentence_transformer/usage/efficiency.html) for benchmarking information on the different backends.

    Example

    :::: 
    ::: highlight
        from sentence_transformers import SentenceTransformer

        # Load a pre-trained SentenceTransformer model
        model = SentenceTransformer('all-mpnet-base-v2')

        # Encode some texts
        sentences = [
            "The weather is lovely today.",
            "It's so sunny outside!",
            "He drove to the stadium.",
        ]
        embeddings = model.encode(sentences)
        print(embeddings.shape)
        # (3, 768)

        # Get the similarity scores between all sentences
        similarities = model.similarity(embeddings, embeddings)
        print(similarities)
        # tensor([[1.0000, 0.6817, 0.0492],
        #         [0.6817, 1.0000, 0.0421],
        #         [0.0492, 0.0421, 1.0000]])
    :::
    ::::

    Initializes internal Module state, shared by both nn.Module and ScriptModule.

    [[active_adapters]][(][)] [[→] [[list][[\[]][str][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\peft_mixin.py#L107-L119)[ïƒ?](#sentence_transformers.SentenceTransformer.active_adapters "Link to this definition")

    :   If you are not familiar with adapters and PEFT methods, we invite you to read more about them on the PEFT official documentation: [https://huggingface.co/docs/peft](https://huggingface.co/docs/peft)

        Gets the current active adapters of the model. In case of multi-adapter inference (combining multiple adapters for inference) returns the list of all active adapters so that users can deal with them accordingly.

        For previous PEFT versions (that does not support multi-adapter inference), module.active_adapter will return a single string.

    [[add_adapter]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\peft_mixin.py#L58-L76)[ïƒ?](#sentence_transformers.SentenceTransformer.add_adapter "Link to this definition")

    :   Adds a fresh new adapter to the current model for training purposes. If no adapter name is passed, a default name is assigned to the adapter to follow the convention of PEFT library (in PEFT we use â€œdefaultâ€? as the default adapter name).

        Requires peft as a backend to load the adapter weights and the underlying model to be compatible with PEFT.

        Parameters[:]

        :   - **\*args** â€" Positional arguments to pass to the underlying AutoModel add_adapter function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.add_adapter](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.add_adapter)

            - **\*\*kwargs** â€" Keyword arguments to pass to the underlying AutoModel add_adapter function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.add_adapter](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.add_adapter)

    [[bfloat16]][(][)] [[→] [[T]]][ïƒ?](#sentence_transformers.SentenceTransformer.bfloat16 "Link to this definition")

    :   Casts all floating point parameters and buffers to [`bfloat16`] datatype.

        ::: 
        Note

        This method modifies the module in-place.
        :::

        Returns[:]

        :   self

        Return type[:]

        :   [Module](models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

    [[compile]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][ïƒ?](#sentence_transformers.SentenceTransformer.compile "Link to this definition")

    :   Compile this Moduleâ€™s forward using [[`torch.compile()`]](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "(in PyTorch v2.9)").

        This Moduleâ€™s \_\_call\_\_ method is compiled and all arguments are passed as-is to [[`torch.compile()`]](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "(in PyTorch v2.9)").

        See [[`torch.compile()`]](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "(in PyTorch v2.9)") for details on the arguments for this function.

    [[cpu]][(][)] [[→] [[T]]][ïƒ?](#sentence_transformers.SentenceTransformer.cpu "Link to this definition")

    :   Moves all model parameters and buffers to the CPU.

        ::: 
        Note

        This method modifies the module in-place.
        :::

        Returns[:]

        :   self

        Return type[:]

        :   [Module](models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

    [[cuda]][(]*[[device]][[:]][ ][[int][ ][[\|]][ ][[device]](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[T]]][ïƒ?](#sentence_transformers.SentenceTransformer.cuda "Link to this definition")

    :   Moves all model parameters and buffers to the GPU.

        This also makes associated parameters and buffers different objects. So it should be called before constructing optimizer if the module will live on GPU while being optimized.

        ::: 
        Note

        This method modifies the module in-place.
        :::

        Parameters[:]

        :   **device** (*int,* *optional*) â€" if specified, all parameters will be copied to that device

        Returns[:]

        :   self

        Return type[:]

        :   [Module](models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

    [[delete_adapter]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\peft_mixin.py#L143-L158)[ïƒ?](#sentence_transformers.SentenceTransformer.delete_adapter "Link to this definition")

    :   If you are not familiar with adapters and PEFT methods, we invite you to read more about them on the PEFT official documentation: [https://huggingface.co/docs/peft](https://huggingface.co/docs/peft)

        Delete an adapterâ€™s LoRA layers from the underlying model.

        Parameters[:]

        :   - **\*args** â€" Positional arguments to pass to the underlying AutoModel delete_adapter function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.delete_adapter](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.delete_adapter)

            - **\*\*kwargs** â€" Keyword arguments to pass to the underlying AutoModel delete_adapter function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.delete_adapter](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.delete_adapter)

    *[property][ ]*[[device]]*[[:]][ ][[device]](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "(in PyTorch v2.9)")*[ïƒ?](#sentence_transformers.SentenceTransformer.device "Link to this definition")

    :   Get torch.device from module, assuming that the whole module has one device. In case there are no PyTorch parameters, fall back to CPU.

    [[disable_adapters]][(][)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\peft_mixin.py#L93-L98)[ïƒ?](#sentence_transformers.SentenceTransformer.disable_adapters "Link to this definition")

    :   Disable all adapters that are attached to the model. This leads to inferring with the base model only.

    [[double]][(][)] [[→] [[T]]][ïƒ?](#sentence_transformers.SentenceTransformer.double "Link to this definition")

    :   Casts all floating point parameters and buffers to [`double`] datatype.

        ::: 
        Note

        This method modifies the module in-place.
        :::

        Returns[:]

        :   self

        Return type[:]

        :   [Module](models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

    [[enable_adapters]][(][)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\peft_mixin.py#L100-L105)[ïƒ?](#sentence_transformers.SentenceTransformer.enable_adapters "Link to this definition")

    :   Enable adapters that are attached to the model. The model will use self.active_adapter()

    [[encode]][(]*[[sentences]][[:]][ ][[str]]*, *[[prompt_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[prompt]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[show_progress_bar]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[output_value]][[:]][ ][[Literal][[\[]][[\'sentence_embedding\']][[,]][ ][[\'token_embeddings\']][[\]]]][ ][[=]][ ][[\'sentence_embedding\']]*, *[[precision]][[:]][ ][[Literal][[\[]][[\'float32\']][[,]][ ][[\'int8\']][[,]][ ][[\'uint8\']][[,]][ ][[\'binary\']][[,]][ ][[\'ubinary\']][[\]]]][ ][[=]][ ][[\'float32\']]*, *[[convert_to_numpy]][[:]][ ][[Literal][[\[]][[False]][[\]]]][ ][[=]][ ][[True]]*, *[[convert_to_tensor]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[device]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][ ][[\|]][ ][[torch.device]](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[normalize_embeddings]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[truncate_dim]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[pool]][[:]][ ][[dict][[\[]][Literal][[\[]][[\'input\']][[,]][ ][[\'output\']][[,]][ ][[\'processes\']][[\]]][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[chunk_size]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[Tensor]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\SentenceTransformer.py#L856-L1159)[ïƒ?](#sentence_transformers.SentenceTransformer.encode "Link to this definition")\
    [[encode]][(]*[[sentences]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][[\]]][ ][[\|]][ ][np.ndarray]]*, *[[prompt_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[prompt]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[show_progress_bar]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[output_value]][[:]][ ][[Literal][[\[]][[\'sentence_embedding\']][[\]]]][ ][[=]][ ][[\'sentence_embedding\']]*, *[[precision]][[:]][ ][[Literal][[\[]][[\'float32\']][[,]][ ][[\'int8\']][[,]][ ][[\'uint8\']][[,]][ ][[\'binary\']][[,]][ ][[\'ubinary\']][[\]]]][ ][[=]][ ][[\'float32\']]*, *[[convert_to_numpy]][[:]][ ][[Literal][[\[]][[True]][[\]]]][ ][[=]][ ][[True]]*, *[[convert_to_tensor]][[:]][ ][[Literal][[\[]][[False]][[\]]]][ ][[=]][ ][[False]]*, *[[device]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][ ][[\|]][ ][[torch.device]](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[normalize_embeddings]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[truncate_dim]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[pool]][[:]][ ][[dict][[\[]][Literal][[\[]][[\'input\']][[,]][ ][[\'output\']][[,]][ ][[\'processes\']][[\]]][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[chunk_size]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[np.ndarray]]]\
    [[encode]][(]*[[sentences]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][[\]]][ ][[\|]][ ][np.ndarray]]*, *[[prompt_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[prompt]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[show_progress_bar]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[output_value]][[:]][ ][[Literal][[\[]][[\'sentence_embedding\']][[\]]]][ ][[=]][ ][[\'sentence_embedding\']]*, *[[precision]][[:]][ ][[Literal][[\[]][[\'float32\']][[,]][ ][[\'int8\']][[,]][ ][[\'uint8\']][[,]][ ][[\'binary\']][[,]][ ][[\'ubinary\']][[\]]]][ ][[=]][ ][[\'float32\']]*, *[[convert_to_numpy]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[convert_to_tensor]][[:]][ ][[Literal][[\[]][[True]][[\]]]][ ][[=]][ ][[False]]*, *[[device]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][ ][[\|]][ ][[torch.device]](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[normalize_embeddings]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[truncate_dim]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[pool]][[:]][ ][[dict][[\[]][Literal][[\[]][[\'input\']][[,]][ ][[\'output\']][[,]][ ][[\'processes\']][[\]]][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[chunk_size]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[Tensor]]]\
    [[encode]][(]*[[sentences]][[:]][ ][[list][[\[]][str][[\]]][ ][[\|]][ ][np.ndarray]]*, *[[prompt_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[prompt]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[show_progress_bar]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[output_value]][[:]][ ][[Literal][[\[]][[\'sentence_embedding\']][[,]][ ][[\'token_embeddings\']][[\]]]][ ][[=]][ ][[\'sentence_embedding\']]*, *[[precision]][[:]][ ][[Literal][[\[]][[\'float32\']][[,]][ ][[\'int8\']][[,]][ ][[\'uint8\']][[,]][ ][[\'binary\']][[,]][ ][[\'ubinary\']][[\]]]][ ][[=]][ ][[\'float32\']]*, *[[convert_to_numpy]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[convert_to_tensor]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[device]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][ ][[\|]][ ][[torch.device]](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[normalize_embeddings]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[truncate_dim]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[pool]][[:]][ ][[dict][[\[]][Literal][[\[]][[\'input\']][[,]][ ][[\'output\']][[,]][ ][[\'processes\']][[\]]][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[chunk_size]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[list][[\[]][Tensor][[\]]]]]\
    [[encode]][(]*[[sentences]][[:]][ ][[list][[\[]][str][[\]]][ ][[\|]][ ][np.ndarray]]*, *[[prompt_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[prompt]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[show_progress_bar]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[output_value]][[:]][ ][[None]][ ][[=]][ ][[\'sentence_embedding\']]*, *[[precision]][[:]][ ][[Literal][[\[]][[\'float32\']][[,]][ ][[\'int8\']][[,]][ ][[\'uint8\']][[,]][ ][[\'binary\']][[,]][ ][[\'ubinary\']][[\]]]][ ][[=]][ ][[\'float32\']]*, *[[convert_to_numpy]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[convert_to_tensor]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[device]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][ ][[\|]][ ][[torch.device]](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[normalize_embeddings]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[truncate_dim]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[pool]][[:]][ ][[dict][[\[]][Literal][[\[]][[\'input\']][[,]][ ][[\'output\']][[,]][ ][[\'processes\']][[\]]][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[chunk_size]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[list][[\[]][dict][[\[]][str][[,]][ ][Tensor][[\]]][[\]]]]]\
    [[encode]][(]*[[sentences]][[:]][ ][[str]]*, *[[prompt_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[prompt]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[show_progress_bar]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[output_value]][[:]][ ][[None]][ ][[=]][ ][[\'sentence_embedding\']]*, *[[precision]][[:]][ ][[Literal][[\[]][[\'float32\']][[,]][ ][[\'int8\']][[,]][ ][[\'uint8\']][[,]][ ][[\'binary\']][[,]][ ][[\'ubinary\']][[\]]]][ ][[=]][ ][[\'float32\']]*, *[[convert_to_numpy]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[convert_to_tensor]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[device]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][ ][[\|]][ ][[torch.device]](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[normalize_embeddings]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[truncate_dim]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[pool]][[:]][ ][[dict][[\[]][Literal][[\[]][[\'input\']][[,]][ ][[\'output\']][[,]][ ][[\'processes\']][[\]]][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[chunk_size]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[dict][[\[]][str][[,]][ ][Tensor][[\]]]]]\
    [[encode]][(]*[[sentences]][[:]][ ][[str]]*, *[[prompt_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[prompt]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[show_progress_bar]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[output_value]][[:]][ ][[Literal][[\[]][[\'token_embeddings\']][[\]]]][ ][[=]][ ][[\'sentence_embedding\']]*, *[[precision]][[:]][ ][[Literal][[\[]][[\'float32\']][[,]][ ][[\'int8\']][[,]][ ][[\'uint8\']][[,]][ ][[\'binary\']][[,]][ ][[\'ubinary\']][[\]]]][ ][[=]][ ][[\'float32\']]*, *[[convert_to_numpy]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[convert_to_tensor]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[device]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][ ][[\|]][ ][[torch.device]](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[normalize_embeddings]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[truncate_dim]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[pool]][[:]][ ][[dict][[\[]][Literal][[\[]][[\'input\']][[,]][ ][[\'output\']][[,]][ ][[\'processes\']][[\]]][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[chunk_size]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[Tensor]]]

    :   Computes sentence embeddings.

        ::: 
        Tip

        If you are unsure whether you should use [[`encode()`]](#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode"), [[`encode_query()`]](#sentence_transformers.SentenceTransformer.encode_query "sentence_transformers.SentenceTransformer.encode_query"), or [[`encode_document()`]](#sentence_transformers.SentenceTransformer.encode_document "sentence_transformers.SentenceTransformer.encode_document"), your best bet is to use [[`encode_query()`]](#sentence_transformers.SentenceTransformer.encode_query "sentence_transformers.SentenceTransformer.encode_query") and [[`encode_document()`]](#sentence_transformers.SentenceTransformer.encode_document "sentence_transformers.SentenceTransformer.encode_document") for Information Retrieval tasks with clear query and document/passage distinction, and use [[`encode()`]](#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode") for all other tasks.

        Note that [[`encode()`]](#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode") is the most general method and can be used for any task, including Information Retrieval, and that if the model was not trained with predefined prompts and/or task types, then all three methods will return identical embeddings.
        :::

        Parameters[:]

        :   - **sentences** (*Union\[str,* *List\[str\]\]*) â€" The sentences to embed.

            - **prompt_name** (*Optional\[str\],* *optional*) â€" The name of the prompt to use for encoding. Must be a key in the prompts dictionary, which is either set in the constructor or loaded from the model configuration. For example if [`prompt_name`] is â€œqueryâ€? and the [`prompts`] is , then the sentence â€œWhat is the capital of France?â€? will be encoded as â€œquery: What is the capital of France?â€? because the sentence is appended to the prompt. If [`prompt`] is also set, this argument is ignored. Defaults to None.

            - **prompt** (*Optional\[str\],* *optional*) â€" The prompt to use for encoding. For example, if the prompt is â€œquery: â€œ, then the sentence â€œWhat is the capital of France?â€? will be encoded as â€œquery: What is the capital of France?â€? because the sentence is appended to the prompt. If [`prompt`] is set, [`prompt_name`] is ignored. Defaults to None.

            - **batch_size** (*int,* *optional*) â€" The batch size used for the computation. Defaults to 32.

            - **show_progress_bar** (*bool,* *optional*) â€" Whether to output a progress bar when encode sentences. Defaults to None.

            - **output_value** (*Optional\[Literal\[\"sentence_embedding\",* *\"token_embeddings\"\]\],* *optional*) â€" The type of embeddings to return: â€œsentence_embeddingâ€? to get sentence embeddings, â€œtoken_embeddingsâ€? to get wordpiece token embeddings, and None, to get all output values. Defaults to â€œsentence_embeddingâ€?.

            - **precision** (*Literal\[\"float32\",* *\"int8\",* *\"uint8\",* *\"binary\",* *\"ubinary\"\],* *optional*) â€" The precision to use for the embeddings. Can be â€œfloat32â€?, â€œint8â€?, â€œuint8â€?, â€œbinaryâ€?, or â€œubinaryâ€?. All non-float32 precisions are quantized embeddings. Quantized embeddings are smaller in size and faster to compute, but may have a lower accuracy. They are useful for reducing the size of the embeddings of a corpus for semantic search, among other tasks. Defaults to â€œfloat32â€?.

            - **convert_to_numpy** (*bool,* *optional*) â€" Whether the output should be a list of numpy vectors. If False, it is a list of PyTorch tensors. Defaults to True.

            - **convert_to_tensor** (*bool,* *optional*) â€" Whether the output should be one large tensor. Overwrites convert_to_numpy. Defaults to False.

            - **device** (*Union\[str,* *List\[str\],* *None\],* *optional*) â€"

              Device(s) to use for computation. Can be:

              - A single device string (e.g., â€œcuda:0â€?, â€œcpuâ€?) for single-process encoding

              - A list of device strings (e.g., \[â€œcuda:0â€?, â€œcuda:1â€?\], \[â€œcpuâ€?, â€œcpuâ€?, â€œcpuâ€?, â€œcpuâ€?\]) to distribute encoding across multiple processes

              - None to auto-detect available device for single-process encoding

              If a list is provided, multi-process encoding will be used. Defaults to None.

            - **normalize_embeddings** (*bool,* *optional*) â€" Whether to normalize returned vectors to have length 1. In that case, the faster dot-product (util.dot_score) instead of cosine similarity can be used. Defaults to False.

            - **truncate_dim** (*int,* *optional*) â€" The dimension to truncate sentence embeddings to. Truncation is especially interesting for [Matryoshka models](https://sbert.net/examples/sentence_transformer/training/matryoshka/README.html), i.e. models that are trained to still produce useful embeddings even if the embedding dimension is reduced. Truncated embeddings require less memory and are faster to perform retrieval with, but note that inference is just as fast, and the embedding performance is worse than the full embeddings. If None, the [`truncate_dim`] from the model initialization is used. Defaults to None.

            - **pool** (*Dict\[Literal\[\"input\",* *\"output\",* *\"processes\"\],* *Any\],* *optional*) â€" A pool created by start_multi_process_pool() for multi-process encoding. If provided, the encoding will be distributed across multiple processes. This is recommended for large datasets and when multiple GPUs are available. Defaults to None.

            - **chunk_size** (*int,* *optional*) â€" Size of chunks for multi-process encoding. Only used with multiprocessing, i.e. when [`pool`] is not None or [`device`] is a list. If None, a sensible default is calculated. Defaults to None.

        Returns[:]

        :   By default, a 2d numpy array with shape \[num_inputs, output_dimension\] is returned. If only one string input is provided, then the output is a 1d array with shape \[output_dimension\]. If [`convert_to_tensor`], a torch Tensor is returned instead. If [`self.truncate_dim`]` `[`<=`]` `[`output_dimension`] then output_dimension is [`self.truncate_dim`].

        Return type[:]

        :   Union\[List\[Tensor\], ndarray, Tensor\]

        Example

        :::: 
        ::: highlight
            from sentence_transformers import SentenceTransformer

            # Load a pre-trained SentenceTransformer model
            model = SentenceTransformer("all-mpnet-base-v2")

            # Encode some texts
            sentences = [
                "The weather is lovely today.",
                "It's so sunny outside!",
                "He drove to the stadium.",
            ]
            embeddings = model.encode(sentences)
            print(embeddings.shape)
            # (3, 768)
        :::
        ::::

    [[encode_document]][(]*[[sentences]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][[\]]][ ][[\|]][ ][ndarray]]*, *[[prompt_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[prompt]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[show_progress_bar]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[output_value]][[:]][ ][[Literal][[\[]][[\'sentence_embedding\']][[,]][ ][[\'token_embeddings\']][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[\'sentence_embedding\']]*, *[[precision]][[:]][ ][[Literal][[\[]][[\'float32\']][[,]][ ][[\'int8\']][[,]][ ][[\'uint8\']][[,]][ ][[\'binary\']][[,]][ ][[\'ubinary\']][[\]]]][ ][[=]][ ][[\'float32\']]*, *[[convert_to_numpy]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[convert_to_tensor]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[device]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][ ][[\|]][ ][[device]](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[normalize_embeddings]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[truncate_dim]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[pool]][[:]][ ][[dict][[\[]][Literal][[\[]][[\'input\']][[,]][ ][[\'output\']][[,]][ ][[\'processes\']][[\]]][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[chunk_size]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[list][[\[]][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][ndarray][ ][[\|]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][dict][[\[]][str][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][list][[\[]][dict][[\[]][str][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\SentenceTransformer.py#L575-L705)[ïƒ?](#sentence_transformers.SentenceTransformer.encode_document "Link to this definition")

    :   Computes sentence embeddings specifically optimized for document/passage representation.

        This method is a specialized version of [[`encode()`]](#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode") that differs in exactly two ways:

        1.  If no [`prompt_name`] or [`prompt`] is provided, it uses a predefined â€œdocumentâ€? prompt, if available in the modelâ€™s [`prompts`] dictionary.

        2.  It sets the [`task`] to â€œdocumentâ€?. If the model has a [[`Router`]](models.html#sentence_transformers.models.Router "sentence_transformers.models.Router") module, it will use the â€œdocumentâ€? task type to route the input through the appropriate submodules.

        ::: 
        Tip

        If you are unsure whether you should use [[`encode()`]](#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode"), [[`encode_query()`]](#sentence_transformers.SentenceTransformer.encode_query "sentence_transformers.SentenceTransformer.encode_query"), or [[`encode_document()`]](#sentence_transformers.SentenceTransformer.encode_document "sentence_transformers.SentenceTransformer.encode_document"), your best bet is to use [[`encode_query()`]](#sentence_transformers.SentenceTransformer.encode_query "sentence_transformers.SentenceTransformer.encode_query") and [[`encode_document()`]](#sentence_transformers.SentenceTransformer.encode_document "sentence_transformers.SentenceTransformer.encode_document") for Information Retrieval tasks with clear query and document/passage distinction, and use [[`encode()`]](#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode") for all other tasks.

        Note that [[`encode()`]](#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode") is the most general method and can be used for any task, including Information Retrieval, and that if the model was not trained with predefined prompts and/or task types, then all three methods will return identical embeddings.
        :::

        Parameters[:]

        :   - **sentences** (*Union\[str,* *List\[str\]\]*) â€" The sentences to embed.

            - **prompt_name** (*Optional\[str\],* *optional*) â€" The name of the prompt to use for encoding. Must be a key in the prompts dictionary, which is either set in the constructor or loaded from the model configuration. For example if [`prompt_name`] is â€œqueryâ€? and the [`prompts`] is , then the sentence â€œWhat is the capital of France?â€? will be encoded as â€œquery: What is the capital of France?â€? because the sentence is appended to the prompt. If [`prompt`] is also set, this argument is ignored. Defaults to None.

            - **prompt** (*Optional\[str\],* *optional*) â€" The prompt to use for encoding. For example, if the prompt is â€œquery: â€œ, then the sentence â€œWhat is the capital of France?â€? will be encoded as â€œquery: What is the capital of France?â€? because the sentence is appended to the prompt. If [`prompt`] is set, [`prompt_name`] is ignored. Defaults to None.

            - **batch_size** (*int,* *optional*) â€" The batch size used for the computation. Defaults to 32.

            - **show_progress_bar** (*bool,* *optional*) â€" Whether to output a progress bar when encode sentences. Defaults to None.

            - **output_value** (*Optional\[Literal\[\"sentence_embedding\",* *\"token_embeddings\"\]\],* *optional*) â€" The type of embeddings to return: â€œsentence_embeddingâ€? to get sentence embeddings, â€œtoken_embeddingsâ€? to get wordpiece token embeddings, and None, to get all output values. Defaults to â€œsentence_embeddingâ€?.

            - **precision** (*Literal\[\"float32\",* *\"int8\",* *\"uint8\",* *\"binary\",* *\"ubinary\"\],* *optional*) â€" The precision to use for the embeddings. Can be â€œfloat32â€?, â€œint8â€?, â€œuint8â€?, â€œbinaryâ€?, or â€œubinaryâ€?. All non-float32 precisions are quantized embeddings. Quantized embeddings are smaller in size and faster to compute, but may have a lower accuracy. They are useful for reducing the size of the embeddings of a corpus for semantic search, among other tasks. Defaults to â€œfloat32â€?.

            - **convert_to_numpy** (*bool,* *optional*) â€" Whether the output should be a list of numpy vectors. If False, it is a list of PyTorch tensors. Defaults to True.

            - **convert_to_tensor** (*bool,* *optional*) â€" Whether the output should be one large tensor. Overwrites convert_to_numpy. Defaults to False.

            - **device** (*Union\[str,* *List\[str\],* *None\],* *optional*) â€"

              Device(s) to use for computation. Can be:

              - A single device string (e.g., â€œcuda:0â€?, â€œcpuâ€?) for single-process encoding

              - A list of device strings (e.g., \[â€œcuda:0â€?, â€œcuda:1â€?\], \[â€œcpuâ€?, â€œcpuâ€?, â€œcpuâ€?, â€œcpuâ€?\]) to distribute encoding across multiple processes

              - None to auto-detect available device for single-process encoding

              If a list is provided, multi-process encoding will be used. Defaults to None.

            - **normalize_embeddings** (*bool,* *optional*) â€" Whether to normalize returned vectors to have length 1. In that case, the faster dot-product (util.dot_score) instead of cosine similarity can be used. Defaults to False.

            - **truncate_dim** (*int,* *optional*) â€"

              The dimension to truncate sentence embeddings to. Truncation is especially interesting for [Matryoshka models](https://sbert.net/examples/sentence_transformer/training/matryoshka/README.html), i.e. models that are trained to still produce useful embeddings even if the embedding dimension is reduced. Truncated embeddings require less memory and are faster to perform retrieval with, but note that inference is just as fast, and the embedding performance is worse than the full embeddings. If None, the [`truncate_dim`] from the model initialization is used. Defaults to None.

            - **pool** (*Dict\[Literal\[\"input\",* *\"output\",* *\"processes\"\],* *Any\],* *optional*) â€" A pool created by start_multi_process_pool() for multi-process encoding. If provided, the encoding will be distributed across multiple processes. This is recommended for large datasets and when multiple GPUs are available. Defaults to None.

            - **chunk_size** (*int,* *optional*) â€" Size of chunks for multi-process encoding. Only used with multiprocessing, i.e. when [`pool`] is not None or [`device`] is a list. If None, a sensible default is calculated. Defaults to None.

        Returns[:]

        :   By default, a 2d numpy array with shape \[num_inputs, output_dimension\] is returned. If only one string input is provided, then the output is a 1d array with shape \[output_dimension\]. If [`convert_to_tensor`], a torch Tensor is returned instead. If [`self.truncate_dim`]` `[`<=`]` `[`output_dimension`] then output_dimension is [`self.truncate_dim`].

        Return type[:]

        :   Union\[List\[Tensor\], ndarray, Tensor\]

        Example

        :::: 
        ::: highlight
            from sentence_transformers import SentenceTransformer

            # Load a pre-trained SentenceTransformer model
            model = SentenceTransformer("mixedbread-ai/mxbai-embed-large-v1")

            # Encode some documents
            documents = [
                "This research paper discusses the effects of climate change on marine life.",
                "The article explores the history of artificial intelligence development.",
                "This document contains technical specifications for the new product line.",
            ]

            # Using document-specific encoding
            embeddings = model.encode_document(documents)
            print(embeddings.shape)
            # (3, 768)
        :::
        ::::

    [[encode_multi_process]][(]*[[sentences]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[pool]][[:]][ ][[dict][[\[]][Literal][[\[]][[\'input\']][[,]][ ][[\'output\']][[,]][ ][[\'processes\']][[\]]][[,]][ ][Any][[\]]]]*, *[[prompt_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[prompt]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[chunk_size]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[show_progress_bar]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[precision]][[:]][ ][[Literal][[\[]][[\'float32\']][[,]][ ][[\'int8\']][[,]][ ][[\'uint8\']][[,]][ ][[\'binary\']][[,]][ ][[\'ubinary\']][[\]]]][ ][[=]][ ][[\'float32\']]*, *[[normalize_embeddings]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[truncate_dim]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[ndarray]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\SentenceTransformer.py#L1374-L1467)[ïƒ?](#sentence_transformers.SentenceTransformer.encode_multi_process "Link to this definition")

    :   ::: 
        Warning

        This method is deprecated. You can now call [[`SentenceTransformer.encode`]](#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode") with the same parameters instead, which will automatically handle multi-process encoding using the provided [`pool`].
        :::

        Encodes a list of sentences using multiple processes and GPUs via [[`SentenceTransformer.encode`]](#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode"). The sentences are chunked into smaller packages and sent to individual processes, which encode them on different GPUs or CPUs. This method is only suitable for encoding large sets of sentences.

        Parameters[:]

        :   - **sentences** (*List\[str\]*) â€" List of sentences to encode.

            - **pool** (*Dict\[Literal\[\"input\",* *\"output\",* *\"processes\"\],* *Any\]*) â€" A pool of workers started with [[`SentenceTransformer.start_multi_process_pool`]](#sentence_transformers.SentenceTransformer.start_multi_process_pool "sentence_transformers.SentenceTransformer.start_multi_process_pool").

            - **prompt_name** (*Optional\[str\],* *optional*) â€" The name of the prompt to use for encoding. Must be a key in the prompts dictionary, which is either set in the constructor or loaded from the model configuration. For example if [`prompt_name`] is â€œqueryâ€? and the [`prompts`] is , then the sentence â€œWhat is the capital of France?â€? will be encoded as â€œquery: What is the capital of France?â€? because the sentence is appended to the prompt. If [`prompt`] is also set, this argument is ignored. Defaults to None.

            - **prompt** (*Optional\[str\],* *optional*) â€" The prompt to use for encoding. For example, if the prompt is â€œquery: â€œ, then the sentence â€œWhat is the capital of France?â€? will be encoded as â€œquery: What is the capital of France?â€? because the sentence is appended to the prompt. If [`prompt`] is set, [`prompt_name`] is ignored. Defaults to None.

            - **batch_size** (*int*) â€" Encode sentences with batch size. (default: 32)

            - **chunk_size** (*int*) â€" Sentences are chunked and sent to the individual processes. If None, it determines a sensible size. Defaults to None.

            - **show_progress_bar** (*bool,* *optional*) â€" Whether to output a progress bar when encode sentences. Defaults to None.

            - **precision** (*Literal\[\"float32\",* *\"int8\",* *\"uint8\",* *\"binary\",* *\"ubinary\"\]*) â€" The precision to use for the embeddings. Can be â€œfloat32â€?, â€œint8â€?, â€œuint8â€?, â€œbinaryâ€?, or â€œubinaryâ€?. All non-float32 precisions are quantized embeddings. Quantized embeddings are smaller in size and faster to compute, but may have lower accuracy. They are useful for reducing the size of the embeddings of a corpus for semantic search, among other tasks. Defaults to â€œfloat32â€?.

            - **normalize_embeddings** (*bool*) â€" Whether to normalize returned vectors to have length 1. In that case, the faster dot-product (util.dot_score) instead of cosine similarity can be used. Defaults to False.

            - **truncate_dim** (*int,* *optional*) â€"

              The dimension to truncate sentence embeddings to. Truncation is especially interesting for [Matryoshka models](https://sbert.net/examples/sentence_transformer/training/matryoshka/README.html), i.e. models that are trained to still produce useful embeddings even if the embedding dimension is reduced. Truncated embeddings require less memory and are faster to perform retrieval with, but note that inference is just as fast, and the embedding performance is worse than the full embeddings. If None, the [`truncate_dim`] from the model initialization is used. Defaults to None.

        Returns[:]

        :   A 2D numpy array with shape \[num_inputs, output_dimension\].

        Return type[:]

        :   np.ndarray

        Example

        :::: 
        ::: highlight
            from sentence_transformers import SentenceTransformer

            def main():
                model = SentenceTransformer("all-mpnet-base-v2")
                sentences = ["The weather is so nice!", "It's so sunny outside.", "He's driving to the movie theater.", "She's going to the cinema."] * 1000

                pool = model.start_multi_process_pool()
                embeddings = model.encode_multi_process(sentences, pool)
                model.stop_multi_process_pool(pool)

                print(embeddings.shape)
                # => (4000, 768)

            if __name__ == "__main__":
                main()
        :::
        ::::

    [[encode_query]][(]*[[sentences]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][[\]]][ ][[\|]][ ][ndarray]]*, *[[prompt_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[prompt]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[show_progress_bar]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[output_value]][[:]][ ][[Literal][[\[]][[\'sentence_embedding\']][[,]][ ][[\'token_embeddings\']][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[\'sentence_embedding\']]*, *[[precision]][[:]][ ][[Literal][[\[]][[\'float32\']][[,]][ ][[\'int8\']][[,]][ ][[\'uint8\']][[,]][ ][[\'binary\']][[,]][ ][[\'ubinary\']][[\]]]][ ][[=]][ ][[\'float32\']]*, *[[convert_to_numpy]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[convert_to_tensor]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[device]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][ ][[\|]][ ][[device]](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[normalize_embeddings]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[truncate_dim]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[pool]][[:]][ ][[dict][[\[]][Literal][[\[]][[\'input\']][[,]][ ][[\'output\']][[,]][ ][[\'processes\']][[\]]][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[chunk_size]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[list][[\[]][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][ndarray][ ][[\|]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][dict][[\[]][str][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][list][[\[]][dict][[\[]][str][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\SentenceTransformer.py#L446-L573)[ïƒ?](#sentence_transformers.SentenceTransformer.encode_query "Link to this definition")

    :   Computes sentence embeddings specifically optimized for query representation.

        This method is a specialized version of [[`encode()`]](#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode") that differs in exactly two ways:

        1.  If no [`prompt_name`] or [`prompt`] is provided, it uses a predefined â€œqueryâ€? prompt, if available in the modelâ€™s [`prompts`] dictionary.

        2.  It sets the [`task`] to â€œqueryâ€?. If the model has a [[`Router`]](models.html#sentence_transformers.models.Router "sentence_transformers.models.Router") module, it will use the â€œqueryâ€? task type to route the input through the appropriate submodules.

        ::: 
        Tip

        If you are unsure whether you should use [[`encode()`]](#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode"), [[`encode_query()`]](#sentence_transformers.SentenceTransformer.encode_query "sentence_transformers.SentenceTransformer.encode_query"), or [[`encode_document()`]](#sentence_transformers.SentenceTransformer.encode_document "sentence_transformers.SentenceTransformer.encode_document"), your best bet is to use [[`encode_query()`]](#sentence_transformers.SentenceTransformer.encode_query "sentence_transformers.SentenceTransformer.encode_query") and [[`encode_document()`]](#sentence_transformers.SentenceTransformer.encode_document "sentence_transformers.SentenceTransformer.encode_document") for Information Retrieval tasks with clear query and document/passage distinction, and use [[`encode()`]](#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode") for all other tasks.

        Note that [[`encode()`]](#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode") is the most general method and can be used for any task, including Information Retrieval, and that if the model was not trained with predefined prompts and/or task types, then all three methods will return identical embeddings.
        :::

        Parameters[:]

        :   - **sentences** (*Union\[str,* *List\[str\]\]*) â€" The sentences to embed.

            - **prompt_name** (*Optional\[str\],* *optional*) â€" The name of the prompt to use for encoding. Must be a key in the prompts dictionary, which is either set in the constructor or loaded from the model configuration. For example if [`prompt_name`] is â€œqueryâ€? and the [`prompts`] is , then the sentence â€œWhat is the capital of France?â€? will be encoded as â€œquery: What is the capital of France?â€? because the sentence is appended to the prompt. If [`prompt`] is also set, this argument is ignored. Defaults to None.

            - **prompt** (*Optional\[str\],* *optional*) â€" The prompt to use for encoding. For example, if the prompt is â€œquery: â€œ, then the sentence â€œWhat is the capital of France?â€? will be encoded as â€œquery: What is the capital of France?â€? because the sentence is appended to the prompt. If [`prompt`] is set, [`prompt_name`] is ignored. Defaults to None.

            - **batch_size** (*int,* *optional*) â€" The batch size used for the computation. Defaults to 32.

            - **show_progress_bar** (*bool,* *optional*) â€" Whether to output a progress bar when encode sentences. Defaults to None.

            - **output_value** (*Optional\[Literal\[\"sentence_embedding\",* *\"token_embeddings\"\]\],* *optional*) â€" The type of embeddings to return: â€œsentence_embeddingâ€? to get sentence embeddings, â€œtoken_embeddingsâ€? to get wordpiece token embeddings, and None, to get all output values. Defaults to â€œsentence_embeddingâ€?.

            - **precision** (*Literal\[\"float32\",* *\"int8\",* *\"uint8\",* *\"binary\",* *\"ubinary\"\],* *optional*) â€" The precision to use for the embeddings. Can be â€œfloat32â€?, â€œint8â€?, â€œuint8â€?, â€œbinaryâ€?, or â€œubinaryâ€?. All non-float32 precisions are quantized embeddings. Quantized embeddings are smaller in size and faster to compute, but may have a lower accuracy. They are useful for reducing the size of the embeddings of a corpus for semantic search, among other tasks. Defaults to â€œfloat32â€?.

            - **convert_to_numpy** (*bool,* *optional*) â€" Whether the output should be a list of numpy vectors. If False, it is a list of PyTorch tensors. Defaults to True.

            - **convert_to_tensor** (*bool,* *optional*) â€" Whether the output should be one large tensor. Overwrites convert_to_numpy. Defaults to False.

            - **device** (*Union\[str,* *List\[str\],* *None\],* *optional*) â€"

              Device(s) to use for computation. Can be:

              - A single device string (e.g., â€œcuda:0â€?, â€œcpuâ€?) for single-process encoding

              - A list of device strings (e.g., \[â€œcuda:0â€?, â€œcuda:1â€?\], \[â€œcpuâ€?, â€œcpuâ€?, â€œcpuâ€?, â€œcpuâ€?\]) to distribute encoding across multiple processes

              - None to auto-detect available device for single-process encoding

              If a list is provided, multi-process encoding will be used. Defaults to None.

            - **normalize_embeddings** (*bool,* *optional*) â€" Whether to normalize returned vectors to have length 1. In that case, the faster dot-product (util.dot_score) instead of cosine similarity can be used. Defaults to False.

            - **truncate_dim** (*int,* *optional*) â€"

              The dimension to truncate sentence embeddings to. Truncation is especially interesting for [Matryoshka models](https://sbert.net/examples/sentence_transformer/training/matryoshka/README.html), i.e. models that are trained to still produce useful embeddings even if the embedding dimension is reduced. Truncated embeddings require less memory and are faster to perform retrieval with, but note that inference is just as fast, and the embedding performance is worse than the full embeddings. If None, the [`truncate_dim`] from the model initialization is used. Defaults to None.

            - **pool** (*Dict\[Literal\[\"input\",* *\"output\",* *\"processes\"\],* *Any\],* *optional*) â€" A pool created by start_multi_process_pool() for multi-process encoding. If provided, the encoding will be distributed across multiple processes. This is recommended for large datasets and when multiple GPUs are available. Defaults to None.

            - **chunk_size** (*int,* *optional*) â€" Size of chunks for multi-process encoding. Only used with multiprocessing, i.e. when [`pool`] is not None or [`device`] is a list. If None, a sensible default is calculated. Defaults to None.

        Returns[:]

        :   By default, a 2d numpy array with shape \[num_inputs, output_dimension\] is returned. If only one string input is provided, then the output is a 1d array with shape \[output_dimension\]. If [`convert_to_tensor`], a torch Tensor is returned instead. If [`self.truncate_dim`]` `[`<=`]` `[`output_dimension`] then output_dimension is [`self.truncate_dim`].

        Return type[:]

        :   Union\[List\[Tensor\], ndarray, Tensor\]

        Example

        :::: 
        ::: highlight
            from sentence_transformers import SentenceTransformer

            # Load a pre-trained SentenceTransformer model
            model = SentenceTransformer("mixedbread-ai/mxbai-embed-large-v1")

            # Encode some queries
            queries = [
                "What are the effects of climate change?",
                "History of artificial intelligence",
                "Technical specifications product XYZ",
            ]

            # Using query-specific encoding
            embeddings = model.encode_query(queries)
            print(embeddings.shape)
            # (3, 768)
        :::
        ::::

    [[eval]][(][)] [[→] [[T]]][ïƒ?](#sentence_transformers.SentenceTransformer.eval "Link to this definition")

    :   Sets the module in evaluation mode.

        This has any effect only on certain modules. See documentations of particular modules for details of their behaviors in training/evaluation mode, if they are affected, e.g. [`Dropout`], [`BatchNorm`], etc.

        This is equivalent with [[`self.train(False)`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.train "(in PyTorch v2.9)").

        See [Locally disabling gradient computation](https://docs.pytorch.org/docs/stable/notes/autograd.html#locally-disable-grad-doc "(in PyTorch v2.9)") for a comparison between .eval() and several similar mechanisms that may be confused with it.

        Returns[:]

        :   self

        Return type[:]

        :   [Module](models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

    [[evaluate]][(]*[[evaluator]][[:]][ ][[[SentenceEvaluator]](evaluation.html#sentence_transformers.evaluation.SentenceEvaluator "sentence_transformers.evaluation.SentenceEvaluator.SentenceEvaluator")]*, *[[output_path]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[dict][[\[]][str][[,]][ ][float][[\]]][ ][[\|]][ ][float]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\SentenceTransformer.py#L2052-L2065)[ïƒ?](#sentence_transformers.SentenceTransformer.evaluate "Link to this definition")

    :   Evaluate the model based on an evaluator

        Parameters[:]

        :   - **evaluator** ([*SentenceEvaluator*](evaluation.html#sentence_transformers.evaluation.SentenceEvaluator "sentence_transformers.evaluation.SentenceEvaluator")) â€" The evaluator used to evaluate the model.

            - **output_path** (*str,* *optional*) â€" The path where the evaluator can write the results. Defaults to None.

        Returns[:]

        :   The evaluation results.

    [[fit]][(]*[train_objectives:] [\~collections.abc.Iterable\[tuple\[\~torch.utils.data.dataloader.DataLoader,] [\~torch.nn.modules.module.Module\]\],] [evaluator:] [\~sentence_transformers.evaluation.SentenceEvaluator.SentenceEvaluator] [\|] [None] [=] [None,] [epochs:] [int] [=] [1,] [steps_per_epoch=None,] [scheduler:] [str] [=] [\'WarmupLinear\',] [warmup_steps:] [int] [=] [10000,] [optimizer_class:] [type\[\~torch.optim.optimizer.Optimizer\]] [=] [\<class] [\'torch.optim.adamw.AdamW\'\>,] [optimizer_params:] [dict\[str,] [object\]] [=] [ [2e-05},] [weight_decay:] [float] [=] [0.01,] [evaluation_steps:] [int] [=] [0,] [output_path:] [str] [\|] [None] [=] [None,] [save_best_model:] [bool] [=] [True,] [max_grad_norm:] [float] [=] [1,] [use_amp:] [bool] [=] [False,] [callback:] [\~collections.abc.Callable\[\[float,] [int,] [int\],] [None\]] [\|] [None] [=] [None,] [show_progress_bar:] [bool] [=] [True,] [checkpoint_path:] [str] [\|] [None] [=] [None,] [checkpoint_save_steps:] [int] [=] [500,] [checkpoint_save_total_limit:] [int] [=] [0,] [resume_from_checkpoint:] [bool] [=] [False]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\fit_mixin.py#L165-L408)[ïƒ?](#sentence_transformers.SentenceTransformer.fit "Link to this definition")

    :   Deprecated training method from before Sentence Transformers v3.0, it is recommended to use [[`SentenceTransformerTrainer`]](trainer.html#sentence_transformers.trainer.SentenceTransformerTrainer "sentence_transformers.trainer.SentenceTransformerTrainer") instead. This method uses [[`SentenceTransformerTrainer`]](trainer.html#sentence_transformers.trainer.SentenceTransformerTrainer "sentence_transformers.trainer.SentenceTransformerTrainer") behind the scenes, but does not provide as much flexibility as the Trainer itself.

        This training approach uses a list of DataLoaders and Loss functions to train the model. Each DataLoader is sampled in turn for one batch. We sample only as many batches from each DataLoader as there are in the smallest one to make sure of equal training with each dataset, i.e. round robin sampling.

        This method should produce equivalent results in v3.0+ as before v3.0, but if you encounter any issues with your existing training scripts, then you may wish to use [[`SentenceTransformer.old_fit`]](#sentence_transformers.SentenceTransformer.old_fit "sentence_transformers.SentenceTransformer.old_fit") instead. That uses the old training method from before v3.0.

        Parameters[:]

        :   - **train_objectives** â€" Tuples of (DataLoader, LossFunction). Pass more than one for multi-task learning

            - **evaluator** â€" An evaluator (sentence_transformers.evaluation) evaluates the model performance during training on held- out dev data. It is used to determine the best model that is saved to disk.

            - **epochs** â€" Number of epochs for training

            - **steps_per_epoch** â€" Number of training steps per epoch. If set to None (default), one epoch is equal the DataLoader size from train_objectives.

            - **scheduler** â€" Learning rate scheduler. Available schedulers: constantlr, warmupconstant, warmuplinear, warmupcosine, warmupcosinewithhardrestarts

            - **warmup_steps** â€" Behavior depends on the scheduler. For WarmupLinear (default), the learning rate is increased from o up to the maximal learning rate. After these many training steps, the learning rate is decreased linearly back to zero.

            - **optimizer_class** â€" Optimizer

            - **optimizer_params** â€" Optimizer parameters

            - **weight_decay** â€" Weight decay for model parameters

            - **evaluation_steps** â€" If \> 0, evaluate the model using evaluator after each number of training steps

            - **output_path** â€" Storage path for the model and evaluation files

            - **save_best_model** â€" If true, the best model (according to evaluator) is stored at output_path

            - **max_grad_norm** â€" Used for gradient normalization.

            - **use_amp** â€" Use Automatic Mixed Precision (AMP). Only for Pytorch \>= 1.6.0

            - **callback** â€" Callback function that is invoked after each evaluation. It must accept the following three parameters in this order: score, epoch, steps

            - **show_progress_bar** â€" If True, output a tqdm progress bar

            - **checkpoint_path** â€" Folder to save checkpoints during training

            - **checkpoint_save_steps** â€" Will save a checkpoint after so many steps

            - **checkpoint_save_total_limit** â€" Total number of checkpoints to store

            - **resume_from_checkpoint** â€" If true, searches for checkpoints to continue training from.

    [[float]][(][)] [[→] [[T]]][ïƒ?](#sentence_transformers.SentenceTransformer.float "Link to this definition")

    :   Casts all floating point parameters and buffers to [`float`] datatype.

        ::: 
        Note

        This method modifies the module in-place.
        :::

        Returns[:]

        :   self

        Return type[:]

        :   [Module](models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

    [[get_adapter_state_dict]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[dict]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\peft_mixin.py#L124-L141)[ïƒ?](#sentence_transformers.SentenceTransformer.get_adapter_state_dict "Link to this definition")

    :   If you are not familiar with adapters and PEFT methods, we invite you to read more about them on the PEFT official documentation: [https://huggingface.co/docs/peft](https://huggingface.co/docs/peft)

        Gets the adapter state dict that should only contain the weights tensors of the specified adapter_name adapter. If no adapter_name is passed, the active adapter is used.

        Parameters[:]

        :   - **\*args** â€" Positional arguments to pass to the underlying AutoModel get_adapter_state_dict function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.get_adapter_state_dict](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.get_adapter_state_dict)

            - **\*\*kwargs** â€" Keyword arguments to pass to the underlying AutoModel get_adapter_state_dict function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.get_adapter_state_dict](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.get_adapter_state_dict)

    [[get_backend]][(][)] [[→] [[Literal][[\[]][[\'torch\']][[,]][ ][[\'onnx\']][[,]][ ][[\'openvino\']][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\SentenceTransformer.py#L408-L414)[ïƒ?](#sentence_transformers.SentenceTransformer.get_backend "Link to this definition")

    :   Return the backend used for inference, which can be one of â€œtorchâ€?, â€œonnxâ€?, or â€œopenvinoâ€?.

        Returns[:]

        :   The backend used for inference.

        Return type[:]

        :   str

    [[get_max_seq_length]][(][)] [[→] [[int][ ][[\|]][ ][None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\SentenceTransformer.py#L1597-L1607)[ïƒ?](#sentence_transformers.SentenceTransformer.get_max_seq_length "Link to this definition")

    :   Returns the maximal sequence length that the model accepts. Longer inputs will be truncated.

        Returns[:]

        :   The maximal sequence length that the model accepts, or None if it is not defined.

        Return type[:]

        :   Optional\[int\]

    [[get_model_kwargs]][(][)] [[→] [[list][[\[]][str][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\SentenceTransformer.py#L416-L444)[ïƒ?](#sentence_transformers.SentenceTransformer.get_model_kwargs "Link to this definition")

    :   Get the keyword arguments specific to this model for the encode, encode_query, or encode_document methods.

        Example

        :::: 
        ::: highlight
            >>> from sentence_transformers import SentenceTransformer, SparseEncoder
            >>> SentenceTransformer("all-MiniLM-L6-v2").get_model_kwargs()
            []
            >>> SentenceTransformer("jinaai/jina-embeddings-v4", trust_remote_code=True).get_model_kwargs()
            ['task', 'truncate_dim']
            >>> SparseEncoder("opensearch-project/opensearch-neural-sparse-encoding-doc-v3-distill").get_model_kwargs()
            ['task']
        :::
        ::::

        Returns[:]

        :   A list of keyword arguments for the forward pass.

        Return type[:]

        :   list\[str\]

    [[get_sentence_embedding_dimension]][(][)] [[→] [[int][ ][[\|]][ ][None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\SentenceTransformer.py#L1628-L1645)[ïƒ?](#sentence_transformers.SentenceTransformer.get_sentence_embedding_dimension "Link to this definition")

    :   Returns the number of dimensions in the output of [[`SentenceTransformer.encode`]](#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode").

        Returns[:]

        :   The number of dimensions in the output of encode. If itâ€™s not known, itâ€™s None.

        Return type[:]

        :   Optional\[int\]

    [[half]][(][)] [[→] [[T]]][ïƒ?](#sentence_transformers.SentenceTransformer.half "Link to this definition")

    :   Casts all floating point parameters and buffers to [`half`] datatype.

        ::: 
        Note

        This method modifies the module in-place.
        :::

        Returns[:]

        :   self

        Return type[:]

        :   [Module](models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

    [[load_adapter]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\peft_mixin.py#L40-L56)[ïƒ?](#sentence_transformers.SentenceTransformer.load_adapter "Link to this definition")

    :   Load adapter weights from file or remote Hub folder.â€? If you are not familiar with adapters and PEFT methods, we invite you to read more about them on PEFT official documentation: [https://huggingface.co/docs/peft](https://huggingface.co/docs/peft)

        Requires peft as a backend to load the adapter weights and the underlying model to be compatible with PEFT.

        Parameters[:]

        :   - **\*args** â€" Positional arguments to pass to the underlying AutoModel load_adapter function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.load_adapter](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.load_adapter)

            - **\*\*kwargs** â€" Keyword arguments to pass to the underlying AutoModel load_adapter function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.load_adapter](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.load_adapter)

    *[property][ ]*[[max_seq_length]]*[[:]][ ][int]*[ïƒ?](#sentence_transformers.SentenceTransformer.max_seq_length "Link to this definition")

    :   Returns the maximal input sequence length for the model. Longer inputs will be truncated.

        Returns[:]

        :   The maximal input sequence length.

        Return type[:]

        :   int

        Example

        :::: 
        ::: highlight
            from sentence_transformers import SentenceTransformer

            model = SentenceTransformer("all-mpnet-base-v2")
            print(model.max_seq_length)
            # => 384
        :::
        ::::

    [[model_card_data_class]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\model_card.py#L265-L1196)[ïƒ?](#sentence_transformers.SentenceTransformer.model_card_data_class "Link to this definition")

    :   alias of [[`SentenceTransformerModelCardData`]](#sentence_transformers.model_card.SentenceTransformerModelCardData "sentence_transformers.model_card.SentenceTransformerModelCardData")

    [[old_fit]][(]*[train_objectives:] [\~collections.abc.Iterable\[tuple\[\~torch.utils.data.dataloader.DataLoader,] [\~torch.nn.modules.module.Module\]\],] [evaluator:] [\~sentence_transformers.evaluation.SentenceEvaluator.SentenceEvaluator] [\|] [None] [=] [None,] [epochs:] [int] [=] [1,] [steps_per_epoch=None,] [scheduler:] [str] [=] [\'WarmupLinear\',] [warmup_steps:] [int] [=] [10000,] [optimizer_class:] [type\[\~torch.optim.optimizer.Optimizer\]] [=] [\<class] [\'torch.optim.adamw.AdamW\'\>,] [optimizer_params:] [dict\[str,] [object\]] [=] [ [2e-05},] [weight_decay:] [float] [=] [0.01,] [evaluation_steps:] [int] [=] [0,] [output_path:] [str] [\|] [None] [=] [None,] [save_best_model:] [bool] [=] [True,] [max_grad_norm:] [float] [=] [1,] [use_amp:] [bool] [=] [False,] [callback:] [\~collections.abc.Callable\[\[float,] [int,] [int\],] [None\]] [\|] [None] [=] [None,] [show_progress_bar:] [bool] [=] [True,] [checkpoint_path:] [str] [\|] [None] [=] [None,] [checkpoint_save_steps:] [int] [=] [500,] [checkpoint_save_total_limit:] [int] [=] [0]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\fit_mixin.py#L469-L696)[ïƒ?](#sentence_transformers.SentenceTransformer.old_fit "Link to this definition")

    :   Deprecated training method from before Sentence Transformers v3.0, it is recommended to use [[`sentence_transformers.trainer.SentenceTransformerTrainer`]](trainer.html#sentence_transformers.trainer.SentenceTransformerTrainer "sentence_transformers.trainer.SentenceTransformerTrainer") instead. This method should only be used if you encounter issues with your existing training scripts after upgrading to v3.0+.

        This training approach uses a list of DataLoaders and Loss functions to train the model. Each DataLoader is sampled in turn for one batch. We sample only as many batches from each DataLoader as there are in the smallest one to make sure of equal training with each dataset, i.e. round robin sampling.

        Parameters[:]

        :   - **train_objectives** â€" Tuples of (DataLoader, LossFunction). Pass more than one for multi-task learning

            - **evaluator** â€" An evaluator (sentence_transformers.evaluation) evaluates the model performance during training on held- out dev data. It is used to determine the best model that is saved to disk.

            - **epochs** â€" Number of epochs for training

            - **steps_per_epoch** â€" Number of training steps per epoch. If set to None (default), one epoch is equal the DataLoader size from train_objectives.

            - **scheduler** â€" Learning rate scheduler. Available schedulers: constantlr, warmupconstant, warmuplinear, warmupcosine, warmupcosinewithhardrestarts

            - **warmup_steps** â€" Behavior depends on the scheduler. For WarmupLinear (default), the learning rate is increased from o up to the maximal learning rate. After these many training steps, the learning rate is decreased linearly back to zero.

            - **optimizer_class** â€" Optimizer

            - **optimizer_params** â€" Optimizer parameters

            - **weight_decay** â€" Weight decay for model parameters

            - **evaluation_steps** â€" If \> 0, evaluate the model using evaluator after each number of training steps

            - **output_path** â€" Storage path for the model and evaluation files

            - **save_best_model** â€" If true, the best model (according to evaluator) is stored at output_path

            - **max_grad_norm** â€" Used for gradient normalization.

            - **use_amp** â€" Use Automatic Mixed Precision (AMP). Only for Pytorch \>= 1.6.0

            - **callback** â€" Callback function that is invoked after each evaluation. It must accept the following three parameters in this order: score, epoch, steps

            - **show_progress_bar** â€" If True, output a tqdm progress bar

            - **checkpoint_path** â€" Folder to save checkpoints during training

            - **checkpoint_save_steps** â€" Will save a checkpoint after so many steps

            - **checkpoint_save_total_limit** â€" Total number of checkpoints to store

    [[push_to_hub]][(]*[[repo_id]][[:]][ ][[str]]*, *[[token]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[private]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[safe_serialization]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[commit_message]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[local_model_path]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[exist_ok]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[replace_model_card]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[train_datasets]][[:]][ ][[list][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[revision]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[create_pr]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)] [[→] [[str]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\SentenceTransformer.py#L1918-L2034)[ïƒ?](#sentence_transformers.SentenceTransformer.push_to_hub "Link to this definition")

    :   Uploads all elements of this Sentence Transformer to a new HuggingFace Hub repository.

        Parameters[:]

        :   - **repo_id** (*str*) â€" Repository name for your model in the Hub, including the user or organization.

            - **token** (*str,* *optional*) â€" An authentication token (See [https://huggingface.co/settings/token](https://huggingface.co/settings/token))

            - **private** (*bool,* *optional*) â€" Set to true, for hosting a private model

            - **safe_serialization** (*bool,* *optional*) â€" If true, save the model using safetensors. If false, save the model the traditional PyTorch way

            - **commit_message** (*str,* *optional*) â€" Message to commit while pushing.

            - **local_model_path** (*str,* *optional*) â€" Path of the model locally. If set, this file path will be uploaded. Otherwise, the current model will be uploaded

            - **exist_ok** (*bool,* *optional*) â€" If true, saving to an existing repository is OK. If false, saving only to a new repository is possible

            - **replace_model_card** (*bool,* *optional*) â€" If true, replace an existing model card in the hub with the automatically created model card

            - **train_datasets** (*List\[str\],* *optional*) â€" Datasets used to train the model. If set, the datasets will be added to the model card in the Hub.

            - **revision** (*str,* *optional*) â€" Branch to push the uploaded files to

            - **create_pr** (*bool,* *optional*) â€" If True, create a pull request instead of pushing directly to the main branch

        Returns[:]

        :   The url of the commit of your model in the repository on the Hugging Face Hub.

        Return type[:]

        :   str

    [[save_pretrained]][(]*[[path]][[:]][ ][[str]]*, *[[model_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[create_model_card]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[train_datasets]][[:]][ ][[list][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[safe_serialization]][[:]][ ][[bool]][ ][[=]][ ][[True]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\SentenceTransformer.py#L1778-L1804)[ïƒ?](#sentence_transformers.SentenceTransformer.save_pretrained "Link to this definition")

    :   Saves a model and its configuration files to a directory, so that it can be loaded with [`SentenceTransformer(path)`] again.

        Parameters[:]

        :   - **path** (*str*) â€" Path on disk where the model will be saved.

            - **model_name** (*str,* *optional*) â€" Optional model name.

            - **create_model_card** (*bool,* *optional*) â€" If True, create a README.md with basic information about this model.

            - **train_datasets** (*List\[str\],* *optional*) â€" Optional list with the names of the datasets used to train the model.

            - **safe_serialization** (*bool,* *optional*) â€" If True, save the model using safetensors. If False, save the model the traditional (but unsafe) PyTorch way.

    [[set_adapter]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\peft_mixin.py#L78-L91)[ïƒ?](#sentence_transformers.SentenceTransformer.set_adapter "Link to this definition")

    :   Sets a specific adapter by forcing the model to use a that adapter and disable the other adapters.

        Parameters[:]

        :   - **\*args** â€" Positional arguments to pass to the underlying AutoModel set_adapter function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.set_adapter](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.set_adapter)

            - **\*\*kwargs** â€" Keyword arguments to pass to the underlying AutoModel set_adapter function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.set_adapter](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.set_adapter)

    [[set_pooling_include_prompt]][(]*[[include_prompt]][[:]][ ][[bool]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\SentenceTransformer.py#L1558-L1574)[ïƒ?](#sentence_transformers.SentenceTransformer.set_pooling_include_prompt "Link to this definition")

    :   Sets the include_prompt attribute in the pooling layer in the model, if there is one.

        This is useful for INSTRUCTOR models, as the prompt should be excluded from the pooling strategy for these models.

        Parameters[:]

        :   **include_prompt** (*bool*) â€" Whether to include the prompt in the pooling layer.

        Returns[:]

        :   None

    *[property][ ]*[[similarity]]*[[:]][ ][Callable][[\[]][[\[]][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][ndarray][[\[]][Any][[,]][ ][dtype][[\[]][float32][[\]]][[\]]][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][ndarray][[\[]][Any][[,]][ ][dtype][[\[]][float32][[\]]][[\]]][[\]]][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]]*[ïƒ?](#sentence_transformers.SentenceTransformer.similarity "Link to this definition")

    :   Compute the similarity between two collections of embeddings. The output will be a matrix with the similarity scores between all embeddings from the first parameter and all embeddings from the second parameter. This differs from similarity_pairwise which computes the similarity between each pair of embeddings. This method supports only embeddings with fp32 precision and does not accommodate quantized embeddings.

        Parameters[:]

        :   - **embeddings1** (*Union\[Tensor,* *ndarray\]*) â€" \[num_embeddings_1, embedding_dim\] or \[embedding_dim\]-shaped numpy array or torch tensor.

            - **embeddings2** (*Union\[Tensor,* *ndarray\]*) â€" \[num_embeddings_2, embedding_dim\] or \[embedding_dim\]-shaped numpy array or torch tensor.

        Returns[:]

        :   A \[num_embeddings_1, num_embeddings_2\]-shaped torch tensor with similarity scores.

        Return type[:]

        :   Tensor

        Example

        :::: 
        ::: highlight
            >>> model = SentenceTransformer("all-mpnet-base-v2")
            >>> sentences = [
            ...     "The weather is so nice!",
            ...     "It's so sunny outside.",
            ...     "He's driving to the movie theater.",
            ...     "She's going to the cinema.",
            ... ]
            >>> embeddings = model.encode(sentences, normalize_embeddings=True)
            >>> model.similarity(embeddings, embeddings)
            tensor([[1.0000, 0.7235, 0.0290, 0.1309],
                    [0.7235, 1.0000, 0.0613, 0.1129],
                    [0.0290, 0.0613, 1.0000, 0.5027],
                    [0.1309, 0.1129, 0.5027, 1.0000]])
            >>> model.similarity_fn_name
            "cosine"
            >>> model.similarity_fn_name = "euclidean"
            >>> model.similarity(embeddings, embeddings)
            tensor([[-0.0000, -0.7437, -1.3935, -1.3184],
                    [-0.7437, -0.0000, -1.3702, -1.3320],
                    [-1.3935, -1.3702, -0.0000, -0.9973],
                    [-1.3184, -1.3320, -0.9973, -0.0000]])
        :::
        ::::

    *[property][ ]*[[similarity_fn_name]]*[[:]][ ][Literal][[\[]][[\'cosine\']][[,]][ ][[\'dot\']][[,]][ ][[\'euclidean\']][[,]][ ][[\'manhattan\']][[\]]]*[ïƒ?](#sentence_transformers.SentenceTransformer.similarity_fn_name "Link to this definition")

    :   Return the name of the similarity function used by [[`SentenceTransformer.similarity()`]](#sentence_transformers.SentenceTransformer.similarity "sentence_transformers.SentenceTransformer.similarity") and [[`SentenceTransformer.similarity_pairwise()`]](#sentence_transformers.SentenceTransformer.similarity_pairwise "sentence_transformers.SentenceTransformer.similarity_pairwise").

        Returns[:]

        :   

            The name of the similarity function. Can be None if not set, in which case it will

            :   default to â€œcosineâ€? when first called.

        Return type[:]

        :   Optional\[str\]

        Example

        :::: 
        ::: highlight
            >>> model = SentenceTransformer("multi-qa-mpnet-base-dot-v1")
            >>> model.similarity_fn_name
            'dot'
        :::
        ::::

    *[property][ ]*[[similarity_pairwise]]*[[:]][ ][Callable][[\[]][[\[]][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][ndarray][[\[]][Any][[,]][ ][dtype][[\[]][float32][[\]]][[\]]][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][ndarray][[\[]][Any][[,]][ ][dtype][[\[]][float32][[\]]][[\]]][[\]]][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]]*[ïƒ?](#sentence_transformers.SentenceTransformer.similarity_pairwise "Link to this definition")

    :   Compute the similarity between two collections of embeddings. The output will be a vector with the similarity scores between each pair of embeddings. This method supports only embeddings with fp32 precision and does not accommodate quantized embeddings.

        Parameters[:]

        :   - **embeddings1** (*Union\[Tensor,* *ndarray\]*) â€" \[num_embeddings, embedding_dim\] or \[embedding_dim\]-shaped numpy array or torch tensor.

            - **embeddings2** (*Union\[Tensor,* *ndarray\]*) â€" \[num_embeddings, embedding_dim\] or \[embedding_dim\]-shaped numpy array or torch tensor.

        Returns[:]

        :   A \[num_embeddings\]-shaped torch tensor with pairwise similarity scores.

        Return type[:]

        :   Tensor

        Example

        :::: 
        ::: highlight
            >>> model = SentenceTransformer("all-mpnet-base-v2")
            >>> sentences = [
            ...     "The weather is so nice!",
            ...     "It's so sunny outside.",
            ...     "He's driving to the movie theater.",
            ...     "She's going to the cinema.",
            ... ]
            >>> embeddings = model.encode(sentences, normalize_embeddings=True)
            >>> model.similarity_pairwise(embeddings[::2], embeddings[1::2])
            tensor([0.7235, 0.5027])
            >>> model.similarity_fn_name
            "cosine"
            >>> model.similarity_fn_name = "euclidean"
            >>> model.similarity_pairwise(embeddings[::2], embeddings[1::2])
            tensor([-0.7437, -0.9973])
        :::
        ::::

    [[smart_batching_collate]][(]*[[batch]][[:]][ ][[list][[\[]][InputExample][[\]]]]*[)] [[→] [[tuple][[\[]][list][[\[]][dict][[\[]][str][[,]][ ][Tensor][[\]]][[\]]][[,]][ ][Tensor][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\fit_mixin.py#L441-L463)[ïƒ?](#sentence_transformers.SentenceTransformer.smart_batching_collate "Link to this definition")

    :   Transforms a batch from a SmartBatchingDataset to a batch of tensors for the model Here, batch is a list of InputExample instances: \[InputExample(â€¦), â€¦\]

        Parameters[:]

        :   **batch** â€" a batch from a SmartBatchingDataset

        Returns[:]

        :   a batch of tensors for the model

    [[start_multi_process_pool]][(]*[[target_devices]][[:]][ ][[list][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[dict][[\[]][Literal][[\[]][[\'input\']][[,]][ ][[\'output\']][[,]][ ][[\'processes\']][[\]]][[,]][ ][Any][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\SentenceTransformer.py#L1304-L1351)[ïƒ?](#sentence_transformers.SentenceTransformer.start_multi_process_pool "Link to this definition")

    :   Starts a multi-process pool to process the encoding with several independent processes via [[`SentenceTransformer.encode_multi_process`]](#sentence_transformers.SentenceTransformer.encode_multi_process "sentence_transformers.SentenceTransformer.encode_multi_process").

        This method is recommended if you want to encode on multiple GPUs or CPUs. It is advised to start only one process per GPU. This method works together with encode_multi_process and stop_multi_process_pool.

        Parameters[:]

        :   **target_devices** (*List\[str\],* *optional*) â€" PyTorch target devices, e.g. \[â€œcuda:0â€?, â€œcuda:1â€?, â€¦\], \[â€œnpu:0â€?, â€œnpu:1â€?, â€¦\], or \[â€œcpuâ€?, â€œcpuâ€?, â€œcpuâ€?, â€œcpuâ€?\]. If target_devices is None and CUDA/NPU is available, then all available CUDA/NPU devices will be used. If target_devices is None and CUDA/NPU is not available, then 4 CPU devices will be used.

        Returns[:]

        :   A dictionary with the target processes, an input queue, and an output queue.

        Return type[:]

        :   Dict\[str, Any\]

    *[static][ ]*[[stop_multi_process_pool]][(]*[[pool]][[:]][ ][[dict][[\[]][Literal][[\[]][[\'input\']][[,]][ ][[\'output\']][[,]][ ][[\'processes\']][[\]]][[,]][ ][Any][[\]]]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\SentenceTransformer.py#L1353-L1372)[ïƒ?](#sentence_transformers.SentenceTransformer.stop_multi_process_pool "Link to this definition")

    :   Stops all processes started with start_multi_process_pool.

        Parameters[:]

        :   **pool** (*Dict\[str,* *object\]*) â€" A dictionary containing the input queue, output queue, and process list.

        Returns[:]

        :   None

    [[to]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][ïƒ?](#sentence_transformers.SentenceTransformer.to "Link to this definition")

    :   Moves and/or casts the parameters and buffers.

        This can be called as

        [[to]][(]*[[device]][[=]][[None]]*, *[[dtype]][[=]][[None]]*, *[[non_blocking]][[=]][[False]]*[)]

        :   

        [[to]][(]*[[dtype]]*, *[[non_blocking]][[=]][[False]]*[)]

        :   

        [[to]][(]*[[tensor]]*, *[[non_blocking]][[=]][[False]]*[)]

        :   

        [[to]][(]*[[memory_format]][[=]][[torch.channels_last]]*[)]

        :   

        Its signature is similar to [[`torch.Tensor.to()`]](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.to.html#torch.Tensor.to "(in PyTorch v2.9)"), but only accepts floating point or complex [`dtype`]s. In addition, this method will only cast the floating point or complex parameters and buffers to [`dtype`] (if given). The integral parameters and buffers will be moved [[`device`]](#sentence_transformers.SentenceTransformer.device "sentence_transformers.SentenceTransformer.device"), if that is given, but with dtypes unchanged. When [`non_blocking`] is set, it tries to convert/move asynchronously with respect to the host if possible, e.g., moving CPU Tensors with pinned memory to CUDA devices.

        See below for examples.

        ::: 
        Note

        This method modifies the module in-place.
        :::

        Parameters[:]

        :   - **device** ([[`torch.device`]](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "(in PyTorch v2.9)")) â€" the desired device of the parameters and buffers in this module

            - **dtype** ([[`torch.dtype`]](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.dtype "(in PyTorch v2.9)")) â€" the desired floating point or complex dtype of the parameters and buffers in this module

            - **tensor** ([*torch.Tensor*](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")) â€" Tensor whose dtype and device are the desired dtype and device for all parameters and buffers in this module

            - **memory_format** ([[`torch.memory_format`]](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.memory_format "(in PyTorch v2.9)")) â€" the desired memory format for 4D parameters and buffers in this module (keyword only argument)

        Returns[:]

        :   self

        Return type[:]

        :   [Module](models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

        Examples:

        :::: 
        ::: highlight
            >>> # xdoctest: +IGNORE_WANT("non-deterministic")
            >>> linear = nn.Linear(2, 2)
            >>> linear.weight
            Parameter containing:
            tensor([[ 0.1913, -0.3420],
                    [-0.5113, -0.2325]])
            >>> linear.to(torch.double)
            Linear(in_features=2, out_features=2, bias=True)
            >>> linear.weight
            Parameter containing:
            tensor([[ 0.1913, -0.3420],
                    [-0.5113, -0.2325]], dtype=torch.float64)
            >>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_CUDA1)
            >>> gpu1 = torch.device("cuda:1")
            >>> linear.to(gpu1, dtype=torch.half, non_blocking=True)
            Linear(in_features=2, out_features=2, bias=True)
            >>> linear.weight
            Parameter containing:
            tensor([[ 0.1914, -0.3420],
                    [-0.5112, -0.2324]], dtype=torch.float16, device='cuda:1')
            >>> cpu = torch.device("cpu")
            >>> linear.to(cpu)
            Linear(in_features=2, out_features=2, bias=True)
            >>> linear.weight
            Parameter containing:
            tensor([[ 0.1914, -0.3420],
                    [-0.5112, -0.2324]], dtype=torch.float16)

            >>> linear = nn.Linear(2, 2, bias=None).to(torch.cdouble)
            >>> linear.weight
            Parameter containing:
            tensor([[ 0.3741+0.j,  0.2382+0.j],
                    [ 0.5593+0.j, -0.4443+0.j]], dtype=torch.complex128)
            >>> linear(torch.ones(3, 2, dtype=torch.cdouble))
            tensor([[0.6122+0.j, 0.1150+0.j],
                    [0.6122+0.j, 0.1150+0.j],
                    [0.6122+0.j, 0.1150+0.j]], dtype=torch.complex128)
        :::
        ::::

    [[tokenize]][(]*[[texts]][[:]][ ][[list][[\[]][str][[\]]][ ][[\|]][ ][list][[\[]][dict][[\]]][ ][[\|]][ ][list][[\[]][tuple][[\[]][str][[,]][ ][str][[\]]][[\]]]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[dict][[\[]][str][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\SentenceTransformer.py#L1609-L1623)[ïƒ?](#sentence_transformers.SentenceTransformer.tokenize "Link to this definition")

    :   Tokenizes the texts.

        Parameters[:]

        :   **texts** (*Union\[List\[str\],* *List\[Dict\],* *List\[Tuple\[str,* *str\]\]\]*) â€" A list of texts to be tokenized.

        Returns[:]

        :   

            A dictionary of tensors with the tokenized texts. Common keys are â€œinput_idsâ€?,

            :   â€?attention_maskâ€?, and â€œtoken_type_idsâ€?.

        Return type[:]

        :   Dict\[str, Tensor\]

    *[property][ ]*[[tokenizer]]*[[:]][ ][Any]*[ïƒ?](#sentence_transformers.SentenceTransformer.tokenizer "Link to this definition")

    :   Property to get the tokenizer that is used by this model

    [[train]][(]*[[mode]][[:]][ ][[bool]][ ][[=]][ ][[True]]*[)] [[→] [[T]]][ïƒ?](#sentence_transformers.SentenceTransformer.train "Link to this definition")

    :   Sets the module in training mode.

        This has any effect only on certain modules. See documentations of particular modules for details of their behaviors in training/evaluation mode, if they are affected, e.g. [`Dropout`], [`BatchNorm`], etc.

        Parameters[:]

        :   **mode** (*bool*) â€" whether to set training mode ([`True`]) or evaluation mode ([`False`]). Default: [`True`].

        Returns[:]

        :   self

        Return type[:]

        :   [Module](models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

    *[property][ ]*[[transformers_model]]*[[:]][ ][PreTrainedModel][ ][[\|]][ ][None]*[ïƒ?](#sentence_transformers.SentenceTransformer.transformers_model "Link to this definition")

    :   Property to get the underlying transformers PreTrainedModel instance, if it exists. Note that itâ€™s possible for a model to have multiple underlying transformers models, but this property will return the first one it finds in the module hierarchy.

        Returns[:]

        :   The underlying transformers model or None if not found.

        Return type[:]

        :   PreTrainedModel or None

        Example

        :::: 
        ::: highlight
            from sentence_transformers import SentenceTransformer

            model = SentenceTransformer("all-mpnet-base-v2")

            # You can now access the underlying transformers model
            transformers_model = model.transformers_model
            print(type(transformers_model))
            # => <class 'transformers.models.mpnet.modeling_mpnet.MPNetModel'>
        :::
        ::::

    [[truncate_sentence_embeddings]][(]*[[truncate_dim]][[:]][ ][[int][ ][[\|]][ ][None]]*[)] [[→] [[Iterator][[\[]][None][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\SentenceTransformer.py#L1647-L1675)[ïƒ?](#sentence_transformers.SentenceTransformer.truncate_sentence_embeddings "Link to this definition")

    :   In this context, [[`SentenceTransformer.encode`]](#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode") outputs sentence embeddings truncated at dimension [`truncate_dim`].

        This may be useful when you are using the same model for different applications where different dimensions are needed.

        Parameters[:]

        :   **truncate_dim** (*int,* *optional*) â€" The dimension to truncate sentence embeddings to. [`None`] does no truncation.

        Example

        :::: 
        ::: highlight
            from sentence_transformers import SentenceTransformer

            model = SentenceTransformer("all-mpnet-base-v2")

            with model.truncate_sentence_embeddings(truncate_dim=16):
                embeddings_truncated = model.encode(["hello there", "hiya"])
            assert embeddings_truncated.shape[-1] == 16
        :::
        ::::

## SentenceTransformerModelCardData[ïƒ?](#sentencetransformermodelcarddata "Link to this heading")

*[class][ ]*[[sentence_transformers.model_card.]][[SentenceTransformerModelCardData]][(]*[[language:] [str] [\|] [list\[str\]] [\|] [None] [=] [\<factory\>]]*, *[[license:] [str] [\|] [None] [=] [None]]*, *[[model_name:] [str] [\|] [None] [=] [None]]*, *[[model_id:] [str] [\|] [None] [=] [None]]*, *[[train_datasets:] [list\[dict\[str]]*, *[[str\]\]] [=] [\<factory\>]]*, *[[eval_datasets:] [list\[dict\[str]]*, *[[str\]\]] [=] [\<factory\>]]*, *[[task_name:] [str] [=] [\'semantic] [textual] [similarity]]*, *[[semantic] [search]]*, *[[paraphrase] [mining]]*, *[[text] [classification]]*, *[[clustering]]*, *[[and] [more\']]*, *[[tags:] [list\[str\]] [\|] [None] [=] [\<factory\>]]*, *[[local_files_only:] [bool] [=] [False]]*, *[[generate_widget_examples:] [bool] [=] [True]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\model_card.py#L265-L1196)[ïƒ?](#sentence_transformers.model_card.SentenceTransformerModelCardData "Link to this definition")

:   A dataclass storing data used in the model card.

    Parameters[:]

    :   - **language** (Optional\[Union\[str, List\[str\]\]\]) â€" The model language, either a string or a list, e.g. â€œenâ€? or \[â€œenâ€?, â€œdeâ€?, â€œnlâ€?\]

        - **license** (Optional\[str\]) â€" The license of the model, e.g. â€œapache-2.0â€?, â€œmitâ€?, or â€œcc-by-nc-sa-4.0â€?

        - **model_name** (Optional\[str\]) â€" The pretty name of the model, e.g. â€œSentenceTransformer based on microsoft/mpnet-baseâ€?.

        - **model_id** (Optional\[str\]) â€" The model ID when pushing the model to the Hub, e.g. â€œtomaarsen/sbert-mpnet-base-allnliâ€?.

        - **train_datasets** (List\[Dict\[str, str\]\]) â€" A list of the names and/or Hugging Face dataset IDs of the training datasets. e.g. \[, , \]

        - **eval_datasets** (List\[Dict\[str, str\]\]) â€" A list of the names and/or Hugging Face dataset IDs of the evaluation datasets. e.g. \[, \]

        - **task_name** (str) â€" The human-readable task the model is trained on, e.g. â€œsemantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and moreâ€?.

        - **tags** (Optional\[List\[str\]\]) â€" A list of tags for the model, e.g. \[â€œsentence-transformersâ€?, â€œsentence-similarityâ€?, â€œfeature-extractionâ€?\].

        - **local_files_only** (bool) â€" If True, donâ€™t attempt to find dataset or base model information on the Hub. Defaults to False.

        - **generate_widget_examples** (bool) â€" If True, generate widget examples from the evaluation or training dataset, and compute their similarities. Defaults to True.

    ::: 
    Tip

    Install [codecarbon](https://github.com/mlco2/codecarbon) to automatically track carbon emission usage and include it in your model cards.
    :::

    Example:

    :::: 
    ::: highlight
        >>> model = SentenceTransformer(
        ...     "microsoft/mpnet-base",
        ...     model_card_data=SentenceTransformerModelCardData(
        ...         model_id="tomaarsen/sbert-mpnet-base-allnli",
        ...         train_datasets=[, ],
        ...         eval_datasets=[, ],
        ...         license="apache-2.0",
        ...         language="en",
        ...     ),
        ... )
    :::
    ::::

## SimilarityFunction[ïƒ?](#similarityfunction "Link to this heading")

*[class][ ]*[[sentence_transformers.]][[SimilarityFunction]][(]*[[value]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\similarity_functions.py#L21-L129)[ïƒ?](#sentence_transformers.SimilarityFunction "Link to this definition")

:   Enum class for supported similarity functions. The following functions are supported:

    - [`SimilarityFunction.COSINE`] ([`"cosine"`]): Cosine similarity

    - [`SimilarityFunction.DOT_PRODUCT`] ([`"dot"`], [`dot_product`]): Dot product similarity

    - [`SimilarityFunction.EUCLIDEAN`] ([`"euclidean"`]): Euclidean distance

    - [`SimilarityFunction.MANHATTAN`] ([`"manhattan"`]): Manhattan distance

    *[static][ ]*[[possible_values]][(][)] [[→] [[list][[\[]][str][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\similarity_functions.py#L116-L129)[ïƒ?](#sentence_transformers.SimilarityFunction.possible_values "Link to this definition")

    :   Returns a list of possible values for the SimilarityFunction enum.

        Returns[:]

        :   A list of possible values for the SimilarityFunction enum.

        Return type[:]

        :   list

        Example

        :::: 
        ::: highlight
            >>> possible_values = SimilarityFunction.possible_values()
            >>> possible_values
            ['cosine', 'dot', 'euclidean', 'manhattan']
        :::
        ::::

    *[static][ ]*[[to_similarity_fn]][(]*[[similarity_function]][[:]][ ][[str][ ][[\|]][ ][[SimilarityFunction]](../sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.similarity_functions.SimilarityFunction")]*[)] [[→] [[Callable][[\[]][[\[]][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][ndarray][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][ndarray][[\]]][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\similarity_functions.py#L37-L73)[ïƒ?](#sentence_transformers.SimilarityFunction.to_similarity_fn "Link to this definition")

    :   Converts a similarity function name or enum value to the corresponding similarity function.

        Parameters[:]

        :   **similarity_function** (*Union\[str,* [*SimilarityFunction*](../sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")*\]*) â€" The name or enum value of the similarity function.

        Returns[:]

        :   The corresponding similarity function.

        Return type[:]

        :   Callable\[\[Union\[Tensor, ndarray\], Union\[Tensor, ndarray\]\], Tensor\]

        Raises[:]

        :   **ValueError** â€" If the provided function is not supported.

        Example

        :::: 
        ::: highlight
            >>> similarity_fn = SimilarityFunction.to_similarity_fn("cosine")
            >>> similarity_scores = similarity_fn(embeddings1, embeddings2)
            >>> similarity_scores
            tensor([[0.3952, 0.0554],
                    [0.0992, 0.1570]])
        :::
        ::::

    *[static][ ]*[[to_similarity_pairwise_fn]][(]*[[similarity_function]][[:]][ ][[str][ ][[\|]][ ][[SimilarityFunction]](../sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.similarity_functions.SimilarityFunction")]*[)] [[→] [[Callable][[\[]][[\[]][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][ndarray][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][ndarray][[\]]][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\similarity_functions.py#L75-L114)[ïƒ?](#sentence_transformers.SimilarityFunction.to_similarity_pairwise_fn "Link to this definition")

    :   Converts a similarity function into a pairwise similarity function.

        The pairwise similarity function returns the diagonal vector from the similarity matrix, i.e. it only computes the similarity(a\[i\], b\[i\]) for each i in the range of the input tensors, rather than computing the similarity between all pairs of a and b.

        Parameters[:]

        :   **similarity_function** (*Union\[str,* [*SimilarityFunction*](../sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")*\]*) â€" The name or enum value of the similarity function.

        Returns[:]

        :   The pairwise similarity function.

        Return type[:]

        :   Callable\[\[Union\[Tensor, ndarray\], Union\[Tensor, ndarray\]\], Tensor\]

        Raises[:]

        :   **ValueError** â€" If the provided similarity function is not supported.

        Example

        :::: 
        ::: highlight
            >>> pairwise_fn = SimilarityFunction.to_similarity_pairwise_fn("cosine")
            >>> similarity_scores = pairwise_fn(embeddings1, embeddings2)
            >>> similarity_scores
            tensor([0.3952, 0.1570])
        :::
        ::::