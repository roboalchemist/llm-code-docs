# Source: https://www.sbert.net/docs/package_reference/sparse_encoder/SparseEncoder.html

# SparseEncoder[ïƒ?](#sparseencoder "Link to this heading")

## SparseEncoder[ïƒ?](#id1 "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.]][[SparseEncoder]][(]*[[model_name_or_path]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[modules]][[:]][ ][[Iterable][[\[]][[Module]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[device]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[prompts]][[:]][ ][[dict][[\[]][str][[,]][ ][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[default_prompt_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[similarity_fn_name]][[:]][ ][[str][ ][[\|]][ ][[SimilarityFunction]](#sentence_transformers.SimilarityFunction "sentence_transformers.similarity_functions.SimilarityFunction")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[cache_folder]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[trust_remote_code]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[revision]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[local_files_only]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[token]][[:]][ ][[bool][ ][[\|]][ ][str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[max_active_dims]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[model_kwargs]][[:]][ ][[dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[tokenizer_kwargs]][[:]][ ][[dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[config_kwargs]][[:]][ ][[dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[model_card_data]][[:]][ ][[[SparseEncoderModelCardData]](#sentence_transformers.sparse_encoder.model_card.SparseEncoderModelCardData "sentence_transformers.sparse_encoder.model_card.SparseEncoderModelCardData")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[backend]][[:]][ ][[Literal][[\[]][[\'torch\']][[,]][ ][[\'onnx\']][[,]][ ][[\'openvino\']][[\]]]][ ][[=]][ ][[\'torch\']]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\sparse_encoder\SparseEncoder.py#L27-L1428)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder "Link to this definition")

:   Loads or creates a SparseEncoder model that can be used to map sentences / text to sparse embeddings.

    Parameters[:]

    :   - **model_name_or_path** (*str,* *optional*) â€" If it is a filepath on disk, it loads the model from that path. If it is not a path, it first tries to download a pre-trained SparseEncoder model. If that fails, tries to construct a model from the Hugging Face Hub with that name.

        - **modules** (*Iterable\[nn.Module\],* *optional*) â€" A list of torch Modules that should be called sequentially, can be used to create custom SparseEncoder models from scratch.

        - **device** (*str,* *optional*) â€" Device (like â€œcudaâ€?, â€œcpuâ€?, â€œmpsâ€?, â€œnpuâ€?) that should be used for computation. If None, checks if a GPU can be used.

        - **prompts** (*Dict\[str,* *str\],* *optional*) â€" A dictionary with prompts for the model. The key is the prompt name, the value is the prompt text. The prompt text will be prepended before any text to encode. For example:  or .

        - **default_prompt_name** (*str,* *optional*) â€" The name of the prompt that should be used by default. If not set, no prompt will be applied.

        - **similarity_fn_name** (*str* *or* [*SimilarityFunction*](#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")*,* *optional*) â€" The name of the similarity function to use. Valid options are â€œcosineâ€?, â€œdotâ€?, â€œeuclideanâ€?, and â€œmanhattanâ€?. If not set, it is automatically set to â€œcosineâ€? if similarity or similarity_pairwise are called while model.similarity_fn_name is still None.

        - **cache_folder** (*str,* *optional*) â€" Path to store models. Can also be set by the SENTENCE_TRANSFORMERS_HOME environment variable.

        - **trust_remote_code** (*bool,* *optional*) â€" Whether or not to allow for custom models defined on the Hub in their own modeling files. This option should only be set to True for repositories you trust and in which you have read the code, as it will execute code present on the Hub on your local machine.

        - **revision** (*str,* *optional*) â€" The specific model version to use. It can be a branch name, a tag name, or a commit id, for a stored model on Hugging Face.

        - **local_files_only** (*bool,* *optional*) â€" Whether or not to only look at local files (i.e., do not try to download the model).

        - **token** (*bool* *or* *str,* *optional*) â€" Hugging Face authentication token to download private models.

        - **max_active_dims** (*int,* *optional*) â€" The maximum number of active (non-zero) dimensions in the output of the model. Defaults to None. This means there will be no limit on the number of active dimensions and can be slow or memory-intensive if your model wasnâ€™t (yet) finetuned to high sparsity.

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

        - **model_card_data** ([[`SparseEncoderModelCardData`]](#sentence_transformers.sparse_encoder.model_card.SparseEncoderModelCardData "sentence_transformers.sparse_encoder.model_card.SparseEncoderModelCardData"), optional) â€" A model card data object that contains information about the model. This is used to generate a model card when saving the model. If not set, a default model card data object is created.

        - **backend** (*str*) â€" The backend to use for inference. Can be one of â€œtorchâ€? (default), â€œonnxâ€?, or â€œopenvinoâ€?. See [https://sbert.net/docs/sentence_transformer/usage/efficiency.html](https://sbert.net/docs/sentence_transformer/usage/efficiency.html) for benchmarking information on the different backends.

    Example

    :::: 
    ::: highlight
        from sentence_transformers import SparseEncoder

        # Load a pre-trained SparseEncoder model
        model = SparseEncoder('naver/splade-cocondenser-ensembledistil')

        # Encode some texts
        sentences = [
            "The weather is lovely today.",
            "It's so sunny outside!",
            "He drove to the stadium.",
        ]
        embeddings = model.encode(sentences)
        print(embeddings.shape)
        # (3, 30522)

        # Get the similarity scores between all sentences
        similarities = model.similarity(embeddings, embeddings)
        print(similarities)
        # tensor([[   35.629,     9.154,     0.098],
        #         [    9.154,    27.478,     0.019],
        #         [    0.098,     0.019,    29.553]])
    :::
    ::::

    Initializes internal Module state, shared by both nn.Module and ScriptModule.

    [[active_adapters]][(][)] [[→] [[list][[\[]][str][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\peft_mixin.py#L107-L119)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.active_adapters "Link to this definition")

    :   If you are not familiar with adapters and PEFT methods, we invite you to read more about them on the PEFT official documentation: [https://huggingface.co/docs/peft](https://huggingface.co/docs/peft)

        Gets the current active adapters of the model. In case of multi-adapter inference (combining multiple adapters for inference) returns the list of all active adapters so that users can deal with them accordingly.

        For previous PEFT versions (that does not support multi-adapter inference), module.active_adapter will return a single string.

    [[add_adapter]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\peft_mixin.py#L58-L76)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.add_adapter "Link to this definition")

    :   Adds a fresh new adapter to the current model for training purposes. If no adapter name is passed, a default name is assigned to the adapter to follow the convention of PEFT library (in PEFT we use â€œdefaultâ€? as the default adapter name).

        Requires peft as a backend to load the adapter weights and the underlying model to be compatible with PEFT.

        Parameters[:]

        :   - **\*args** â€" Positional arguments to pass to the underlying AutoModel add_adapter function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.add_adapter](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.add_adapter)

            - **\*\*kwargs** â€" Keyword arguments to pass to the underlying AutoModel add_adapter function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.add_adapter](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.add_adapter)

    [[bfloat16]][(][)] [[→] [[T]]][ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.bfloat16 "Link to this definition")

    :   Casts all floating point parameters and buffers to [`bfloat16`] datatype.

        ::: 
        Note

        This method modifies the module in-place.
        :::

        Returns[:]

        :   self

        Return type[:]

        :   [Module](../sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

    [[compile]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.compile "Link to this definition")

    :   Compile this Moduleâ€™s forward using [[`torch.compile()`]](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "(in PyTorch v2.9)").

        This Moduleâ€™s \_\_call\_\_ method is compiled and all arguments are passed as-is to [[`torch.compile()`]](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "(in PyTorch v2.9)").

        See [[`torch.compile()`]](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "(in PyTorch v2.9)") for details on the arguments for this function.

    [[cpu]][(][)] [[→] [[T]]][ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.cpu "Link to this definition")

    :   Moves all model parameters and buffers to the CPU.

        ::: 
        Note

        This method modifies the module in-place.
        :::

        Returns[:]

        :   self

        Return type[:]

        :   [Module](../sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

    [[cuda]][(]*[[device]][[:]][ ][[int][ ][[\|]][ ][[device]](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[T]]][ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.cuda "Link to this definition")

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

        :   [Module](../sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

    [[decode]][(]*[[embeddings]][[:]][ ][[[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]*, *[[top_k]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[list][[\[]][tuple][[\[]][str][[,]][ ][float][[\]]][[\]]][ ][[\|]][ ][list][[\[]][list][[\[]][tuple][[\[]][str][[,]][ ][float][[\]]][[\]]][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\sparse_encoder\SparseEncoder.py#L1314-L1428)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.decode "Link to this definition")

    :   Decode top K tokens and weights from a sparse embedding. If none will just return the all tokens and weights

        Parameters[:]

        :   - **embeddings** ([*torch.Tensor*](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")) â€" Sparse embedding tensor (batch, vocab) or (vocab).

            - **top_k** (*int,* *optional*) â€" Number of top tokens to return per sample. If None, returns all non-zero tokens.

        Returns[:]

        :   List of tuples (token, weight) for each embedding. If batch input, returns a list of lists of tuples.

        Return type[:]

        :   list\[tuple\[str, float\]\] \| list\[list\[tuple\[str, float\]\]\]

    [[delete_adapter]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\peft_mixin.py#L143-L158)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.delete_adapter "Link to this definition")

    :   If you are not familiar with adapters and PEFT methods, we invite you to read more about them on the PEFT official documentation: [https://huggingface.co/docs/peft](https://huggingface.co/docs/peft)

        Delete an adapterâ€™s LoRA layers from the underlying model.

        Parameters[:]

        :   - **\*args** â€" Positional arguments to pass to the underlying AutoModel delete_adapter function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.delete_adapter](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.delete_adapter)

            - **\*\*kwargs** â€" Keyword arguments to pass to the underlying AutoModel delete_adapter function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.delete_adapter](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.delete_adapter)

    *[property][ ]*[[device]]*[[:]][ ][[device]](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "(in PyTorch v2.9)")*[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.device "Link to this definition")

    :   Get torch.device from module, assuming that the whole module has one device. In case there are no PyTorch parameters, fall back to CPU.

    [[disable_adapters]][(][)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\peft_mixin.py#L93-L98)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.disable_adapters "Link to this definition")

    :   Disable all adapters that are attached to the model. This leads to inferring with the base model only.

    [[double]][(][)] [[→] [[T]]][ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.double "Link to this definition")

    :   Casts all floating point parameters and buffers to [`double`] datatype.

        ::: 
        Note

        This method modifies the module in-place.
        :::

        Returns[:]

        :   self

        Return type[:]

        :   [Module](../sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

    [[enable_adapters]][(][)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\peft_mixin.py#L100-L105)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.enable_adapters "Link to this definition")

    :   Enable adapters that are attached to the model. The model will use self.active_adapter()

    [[encode]][(]*[[sentences]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][[\]]][ ][[\|]][ ][ndarray]]*, *[[prompt_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[prompt]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[show_progress_bar]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[convert_to_tensor]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[convert_to_sparse_tensor]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[save_to_cpu]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[device]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][ ][[\|]][ ][[device]](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[max_active_dims]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[pool]][[:]][ ][[dict][[\[]][Literal][[\[]][[\'input\']][[,]][ ][[\'output\']][[,]][ ][[\'processes\']][[\]]][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[chunk_size]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\*\*]][[kwargs]][[:]][ ][[Any]]*[)] [[→] [[list][[\[]][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][ndarray][ ][[\|]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][dict][[\[]][str][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][list][[\[]][dict][[\[]][str][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\sparse_encoder\SparseEncoder.py#L412-L623)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.encode "Link to this definition")

    :   Computes sparse sentence embeddings.

        ::: 
        Tip

        If you are unsure whether you should use [[`encode()`]](#sentence_transformers.sparse_encoder.SparseEncoder.encode "sentence_transformers.sparse_encoder.SparseEncoder.encode"), [[`encode_query()`]](#sentence_transformers.sparse_encoder.SparseEncoder.encode_query "sentence_transformers.sparse_encoder.SparseEncoder.encode_query"), or [[`encode_document()`]](#sentence_transformers.sparse_encoder.SparseEncoder.encode_document "sentence_transformers.sparse_encoder.SparseEncoder.encode_document"), your best bet is to use [[`encode_query()`]](#sentence_transformers.sparse_encoder.SparseEncoder.encode_query "sentence_transformers.sparse_encoder.SparseEncoder.encode_query") and [[`encode_document()`]](#sentence_transformers.sparse_encoder.SparseEncoder.encode_document "sentence_transformers.sparse_encoder.SparseEncoder.encode_document") for Information Retrieval tasks with clear query and document/passage distinction, and use [[`encode()`]](#sentence_transformers.sparse_encoder.SparseEncoder.encode "sentence_transformers.sparse_encoder.SparseEncoder.encode") for all other tasks.

        Note that [[`encode()`]](#sentence_transformers.sparse_encoder.SparseEncoder.encode "sentence_transformers.sparse_encoder.SparseEncoder.encode") is the most general method and can be used for any task, including Information Retrieval, and that if the model was not trained with predefined prompts and/or task types, then all three methods will return identical embeddings.
        :::

        Parameters[:]

        :   - **sentences** (*Union\[str,* *List\[str\]\]*) â€" The sentences to embed.

            - **prompt_name** (*Optional\[str\],* *optional*) â€" The name of the prompt to use for encoding. Must be a key in the prompts dictionary, which is either set in the constructor or loaded from the model configuration. For example if [`prompt_name`] is â€œqueryâ€? and the [`prompts`] is , then the sentence â€œWhat is the capital of France?â€? will be encoded as â€œquery: What is the capital of France?â€? because the sentence is appended to the prompt. If [`prompt`] is also set, this argument is ignored. Defaults to None.

            - **prompt** (*Optional\[str\],* *optional*) â€" The prompt to use for encoding. For example, if the prompt is â€œquery: â€œ, then the sentence â€œWhat is the capital of France?â€? will be encoded as â€œquery: What is the capital of France?â€? because the sentence is appended to the prompt. If [`prompt`] is set, [`prompt_name`] is ignored. Defaults to None.

            - **batch_size** (*int,* *optional*) â€" The batch size used for the computation. Defaults to 32.

            - **show_progress_bar** (*bool,* *optional*) â€" Whether to output a progress bar when encode sentences. Defaults to None.

            - **convert_to_tensor** (*bool,* *optional*) â€" Whether the output should be a single stacked tensor (True) or a list of individual tensors (False). Sparse tensors may be challenging to slice, so this allows you to output lists of tensors instead. Defaults to True.

            - **convert_to_sparse_tensor** (*bool,* *optional*) â€" Whether the output should be in the format of a sparse (COO) tensor. Defaults to True.

            - **save_to_cpu** (*bool,* *optional*) â€" Whether the output should be moved to cpu or stay on the device it has been computed on. Defaults to False

            - **device** (*Union\[str,* *List\[str\],* *None\],* *optional*) â€"

              Device(s) to use for computation. Can be:

              - A single device string (e.g., â€œcuda:0â€?, â€œcpuâ€?) for single-process encoding

              - A list of device strings (e.g., \[â€œcuda:0â€?, â€œcuda:1â€?\], \[â€œcpuâ€?, â€œcpuâ€?, â€œcpuâ€?, â€œcpuâ€?\]) to distribute encoding across multiple processes

              - None to auto-detect available device for single-process encoding

              If a list is provided, multi-process encoding will be used. Defaults to None.

            - **max_active_dims** (*int,* *optional*) â€" The maximum number of active (non-zero) dimensions in the output of the model. None means we will used the value of the modelâ€™s config. Defaults to None. If None in modelâ€™s config it means there will be no limit on the number of active dimensions and can be slow or memory-intensive if your model wasnâ€™t (yet) finetuned to high sparsity.

            - **pool** (*Dict\[Literal\[\"input\",* *\"output\",* *\"processes\"\],* *Any\],* *optional*) â€" A pool created by start_multi_process_pool() for multi-process encoding. If provided, the encoding will be distributed across multiple processes. This is recommended for large datasets and when multiple GPUs are available. Defaults to None.

            - **chunk_size** (*int,* *optional*) â€" Size of chunks for multi-process encoding. Only used with multiprocessing, i.e. when [`pool`] is not None or [`device`] is a list. If None, a sensible default is calculated. Defaults to None.

        Returns[:]

        :   By default, a 2d torch sparse tensor with shape \[num_inputs, output_dimension\] is returned. If only one string input is provided, then the output is a 1d array with shape \[output_dimension\]. If save_to_cpu is True, the embeddings are moved to the CPU.

        Return type[:]

        :   Union\[List\[Tensor\], ndarray, Tensor\]

        Example

        :::: 
        ::: highlight
            from sentence_transformers import SparseEncoder

            # Load a pre-trained SparseEncoder model
            model = SparseEncoder("naver/splade-cocondenser-ensembledistil")

            # Encode some texts
            sentences = [
                "The weather is lovely today.",
                "It's so sunny outside!",
                "He drove to the stadium.",
            ]
            embeddings = model.encode(sentences)
            print(embeddings.shape)
            # (3, 30522)
        :::
        ::::

    [[encode_document]][(]*[[sentences]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][[\]]][ ][[\|]][ ][ndarray]]*, *[[prompt_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[prompt]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[show_progress_bar]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[convert_to_tensor]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[convert_to_sparse_tensor]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[save_to_cpu]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[device]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][ ][[\|]][ ][[device]](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[max_active_dims]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[pool]][[:]][ ][[dict][[\[]][Literal][[\[]][[\'input\']][[,]][ ][[\'output\']][[,]][ ][[\'processes\']][[\]]][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[chunk_size]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\*\*]][[kwargs]][[:]][ ][[Any]]*[)] [[→] [[list][[\[]][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][ndarray][ ][[\|]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][dict][[\[]][str][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][list][[\[]][dict][[\[]][str][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\sparse_encoder\SparseEncoder.py#L295-L410)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.encode_document "Link to this definition")

    :   Computes sentence embeddings specifically optimized for document/passage representation.

        This method is a specialized version of [[`encode()`]](#sentence_transformers.sparse_encoder.SparseEncoder.encode "sentence_transformers.sparse_encoder.SparseEncoder.encode") that differs in exactly two ways:

        1.  If no [`prompt_name`] or [`prompt`] is provided, it uses a predefined â€œdocumentâ€? prompt, if available in the modelâ€™s [`prompts`] dictionary.

        2.  It sets the [`task`] to â€œdocumentâ€?. If the model has a [[`Router`]](../sentence_transformer/models.html#sentence_transformers.models.Router "sentence_transformers.models.Router") module, it will use the â€œdocumentâ€? task type to route the input through the appropriate submodules.

        ::: 
        Tip

        If you are unsure whether you should use [[`encode()`]](#sentence_transformers.sparse_encoder.SparseEncoder.encode "sentence_transformers.sparse_encoder.SparseEncoder.encode"), [[`encode_query()`]](#sentence_transformers.sparse_encoder.SparseEncoder.encode_query "sentence_transformers.sparse_encoder.SparseEncoder.encode_query"), or [[`encode_document()`]](#sentence_transformers.sparse_encoder.SparseEncoder.encode_document "sentence_transformers.sparse_encoder.SparseEncoder.encode_document"), your best bet is to use [[`encode_query()`]](#sentence_transformers.sparse_encoder.SparseEncoder.encode_query "sentence_transformers.sparse_encoder.SparseEncoder.encode_query") and [[`encode_document()`]](#sentence_transformers.sparse_encoder.SparseEncoder.encode_document "sentence_transformers.sparse_encoder.SparseEncoder.encode_document") for Information Retrieval tasks with clear query and document/passage distinction, and use [[`encode()`]](#sentence_transformers.sparse_encoder.SparseEncoder.encode "sentence_transformers.sparse_encoder.SparseEncoder.encode") for all other tasks.

        Note that [[`encode()`]](#sentence_transformers.sparse_encoder.SparseEncoder.encode "sentence_transformers.sparse_encoder.SparseEncoder.encode") is the most general method and can be used for any task, including Information Retrieval, and that if the model was not trained with predefined prompts and/or task types, then all three methods will return identical embeddings.
        :::

        Parameters[:]

        :   - **sentences** (*Union\[str,* *List\[str\]\]*) â€" The sentences to embed.

            - **prompt_name** (*Optional\[str\],* *optional*) â€" The name of the prompt to use for encoding. Must be a key in the prompts dictionary, which is either set in the constructor or loaded from the model configuration. For example if [`prompt_name`] is â€œqueryâ€? and the [`prompts`] is , then the sentence â€œWhat is the capital of France?â€? will be encoded as â€œquery: What is the capital of France?â€? because the sentence is appended to the prompt. If [`prompt`] is also set, this argument is ignored. Defaults to None.

            - **prompt** (*Optional\[str\],* *optional*) â€" The prompt to use for encoding. For example, if the prompt is â€œquery: â€œ, then the sentence â€œWhat is the capital of France?â€? will be encoded as â€œquery: What is the capital of France?â€? because the sentence is appended to the prompt. If [`prompt`] is set, [`prompt_name`] is ignored. Defaults to None.

            - **batch_size** (*int,* *optional*) â€" The batch size used for the computation. Defaults to 32.

            - **show_progress_bar** (*bool,* *optional*) â€" Whether to output a progress bar when encode sentences. Defaults to None.

            - **convert_to_tensor** (*bool,* *optional*) â€" Whether the output should be a single stacked tensor (True) or a list of individual tensors (False). Sparse tensors may be challenging to slice, so this allows you to output lists of tensors instead. Defaults to True.

            - **convert_to_sparse_tensor** (*bool,* *optional*) â€" Whether the output should be in the format of a sparse (COO) tensor. Defaults to True.

            - **save_to_cpu** (*bool,* *optional*) â€" Whether the output should be moved to cpu or stay on the device it has been computed on. Defaults to False

            - **device** (*Union\[str,* *List\[str\],* *None\],* *optional*) â€"

              Device(s) to use for computation. Can be:

              - A single device string (e.g., â€œcuda:0â€?, â€œcpuâ€?) for single-process encoding

              - A list of device strings (e.g., \[â€œcuda:0â€?, â€œcuda:1â€?\], \[â€œcpuâ€?, â€œcpuâ€?, â€œcpuâ€?, â€œcpuâ€?\]) to distribute encoding across multiple processes

              - None to auto-detect available device for single-process encoding

              If a list is provided, multi-process encoding will be used. Defaults to None.

            - **max_active_dims** (*int,* *optional*) â€" The maximum number of active (non-zero) dimensions in the output of the model. None means we will used the value of the modelâ€™s config. Defaults to None. If None in modelâ€™s config it means there will be no limit on the number of active dimensions and can be slow or memory-intensive if your model wasnâ€™t (yet) finetuned to high sparsity.

            - **pool** (*Dict\[Literal\[\"input\",* *\"output\",* *\"processes\"\],* *Any\],* *optional*) â€" A pool created by start_multi_process_pool() for multi-process encoding. If provided, the encoding will be distributed across multiple processes. This is recommended for large datasets and when multiple GPUs are available. Defaults to None.

            - **chunk_size** (*int,* *optional*) â€" Size of chunks for multi-process encoding. Only used with multiprocessing, i.e. when [`pool`] is not None or [`device`] is a list. If None, a sensible default is calculated. Defaults to None.

        Returns[:]

        :   By default, a 2d torch sparse tensor with shape \[num_inputs, output_dimension\] is returned. If only one string input is provided, then the output is a 1d array with shape \[output_dimension\]. If save_to_cpu is True, the embeddings are moved to the CPU.

        Return type[:]

        :   Union\[List\[Tensor\], ndarray, Tensor\]

        Example

        :::: 
        ::: highlight
            from sentence_transformers import SparseEncoder

            # Load a pre-trained SparseEncoder model
            model = SparseEncoder("naver/splade-cocondenser-ensembledistil")

            # Encode some texts
            sentences = [
                "This research paper discusses the effects of climate change on marine life.",
                "The article explores the history of artificial intelligence development.",
                "This document contains technical specifications for the new product line.",
            ]
            embeddings = model.encode(sentences)
            print(embeddings.shape)
            # (3, 30522)
        :::
        ::::

    [[encode_query]][(]*[[sentences]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][[\]]][ ][[\|]][ ][ndarray]]*, *[[prompt_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[prompt]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[show_progress_bar]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[convert_to_tensor]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[convert_to_sparse_tensor]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[save_to_cpu]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[device]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][ ][[\|]][ ][[device]](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[max_active_dims]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[pool]][[:]][ ][[dict][[\[]][Literal][[\[]][[\'input\']][[,]][ ][[\'output\']][[,]][ ][[\'processes\']][[\]]][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[chunk_size]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\*\*]][[kwargs]][[:]][ ][[Any]]*[)] [[→] [[list][[\[]][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][ndarray][ ][[\|]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][dict][[\[]][str][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][list][[\[]][dict][[\[]][str][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\sparse_encoder\SparseEncoder.py#L181-L293)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.encode_query "Link to this definition")

    :   Computes sentence embeddings specifically optimized for query representation.

        This method is a specialized version of [[`encode()`]](#sentence_transformers.sparse_encoder.SparseEncoder.encode "sentence_transformers.sparse_encoder.SparseEncoder.encode") that differs in exactly two ways:

        1.  If no [`prompt_name`] or [`prompt`] is provided, it uses a predefined â€œqueryâ€? prompt, if available in the modelâ€™s [`prompts`] dictionary.

        2.  It sets the [`task`] to â€œqueryâ€?. If the model has a [[`Router`]](../sentence_transformer/models.html#sentence_transformers.models.Router "sentence_transformers.models.Router") module, it will use the â€œqueryâ€? task type to route the input through the appropriate submodules.

        ::: 
        Tip

        If you are unsure whether you should use [[`encode()`]](#sentence_transformers.sparse_encoder.SparseEncoder.encode "sentence_transformers.sparse_encoder.SparseEncoder.encode"), [[`encode_query()`]](#sentence_transformers.sparse_encoder.SparseEncoder.encode_query "sentence_transformers.sparse_encoder.SparseEncoder.encode_query"), or [[`encode_document()`]](#sentence_transformers.sparse_encoder.SparseEncoder.encode_document "sentence_transformers.sparse_encoder.SparseEncoder.encode_document"), your best bet is to use [[`encode_query()`]](#sentence_transformers.sparse_encoder.SparseEncoder.encode_query "sentence_transformers.sparse_encoder.SparseEncoder.encode_query") and [[`encode_document()`]](#sentence_transformers.sparse_encoder.SparseEncoder.encode_document "sentence_transformers.sparse_encoder.SparseEncoder.encode_document") for Information Retrieval tasks with clear query and document/passage distinction, and use [[`encode()`]](#sentence_transformers.sparse_encoder.SparseEncoder.encode "sentence_transformers.sparse_encoder.SparseEncoder.encode") for all other tasks.

        Note that [[`encode()`]](#sentence_transformers.sparse_encoder.SparseEncoder.encode "sentence_transformers.sparse_encoder.SparseEncoder.encode") is the most general method and can be used for any task, including Information Retrieval, and that if the model was not trained with predefined prompts and/or task types, then all three methods will return identical embeddings.
        :::

        Parameters[:]

        :   - **sentences** (*Union\[str,* *List\[str\]\]*) â€" The sentences to embed.

            - **prompt_name** (*Optional\[str\],* *optional*) â€" The name of the prompt to use for encoding. Must be a key in the prompts dictionary, which is either set in the constructor or loaded from the model configuration. For example if [`prompt_name`] is â€œqueryâ€? and the [`prompts`] is , then the sentence â€œWhat is the capital of France?â€? will be encoded as â€œquery: What is the capital of France?â€? because the sentence is appended to the prompt. If [`prompt`] is also set, this argument is ignored. Defaults to None.

            - **prompt** (*Optional\[str\],* *optional*) â€" The prompt to use for encoding. For example, if the prompt is â€œquery: â€œ, then the sentence â€œWhat is the capital of France?â€? will be encoded as â€œquery: What is the capital of France?â€? because the sentence is appended to the prompt. If [`prompt`] is set, [`prompt_name`] is ignored. Defaults to None.

            - **batch_size** (*int,* *optional*) â€" The batch size used for the computation. Defaults to 32.

            - **show_progress_bar** (*bool,* *optional*) â€" Whether to output a progress bar when encode sentences. Defaults to None.

            - **convert_to_tensor** (*bool,* *optional*) â€" Whether the output should be a single stacked tensor (True) or a list of individual tensors (False). Sparse tensors may be challenging to slice, so this allows you to output lists of tensors instead. Defaults to True.

            - **convert_to_sparse_tensor** (*bool,* *optional*) â€" Whether the output should be in the format of a sparse (COO) tensor. Defaults to True.

            - **save_to_cpu** (*bool,* *optional*) â€" Whether the output should be moved to cpu or stay on the device it has been computed on. Defaults to False

            - **device** (*Union\[str,* *List\[str\],* *None\],* *optional*) â€"

              Device(s) to use for computation. Can be:

              - A single device string (e.g., â€œcuda:0â€?, â€œcpuâ€?) for single-process encoding

              - A list of device strings (e.g., \[â€œcuda:0â€?, â€œcuda:1â€?\], \[â€œcpuâ€?, â€œcpuâ€?, â€œcpuâ€?, â€œcpuâ€?\]) to distribute encoding across multiple processes

              - None to auto-detect available device for single-process encoding

              If a list is provided, multi-process encoding will be used. Defaults to None.

            - **max_active_dims** (*int,* *optional*) â€" The maximum number of active (non-zero) dimensions in the output of the model. None means we will used the value of the modelâ€™s config. Defaults to None. If None in modelâ€™s config it means there will be no limit on the number of active dimensions and can be slow or memory-intensive if your model wasnâ€™t (yet) finetuned to high sparsity.

            - **pool** (*Dict\[Literal\[\"input\",* *\"output\",* *\"processes\"\],* *Any\],* *optional*) â€" A pool created by start_multi_process_pool() for multi-process encoding. If provided, the encoding will be distributed across multiple processes. This is recommended for large datasets and when multiple GPUs are available. Defaults to None.

            - **chunk_size** (*int,* *optional*) â€" Size of chunks for multi-process encoding. Only used with multiprocessing, i.e. when [`pool`] is not None or [`device`] is a list. If None, a sensible default is calculated. Defaults to None.

        Returns[:]

        :   By default, a 2d torch sparse tensor with shape \[num_inputs, output_dimension\] is returned. If only one string input is provided, then the output is a 1d array with shape \[output_dimension\]. If save_to_cpu is True, the embeddings are moved to the CPU.

        Return type[:]

        :   Union\[List\[Tensor\], ndarray, Tensor\]

        Example

        :::: 
        ::: highlight
            from sentence_transformers import SparseEncoder

            # Load a pre-trained SparseEncoder model
            model = SparseEncoder("naver/splade-cocondenser-ensembledistil")

            # Encode some texts
            queries = [
                "What are the effects of climate change?",
                "History of artificial intelligence",
                "Technical specifications product XYZ",
            ]
            embeddings = model.encode_query(queries)
            print(embeddings.shape)
            # (3, 30522)
        :::
        ::::

    [[eval]][(][)] [[→] [[T]]][ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.eval "Link to this definition")

    :   Sets the module in evaluation mode.

        This has any effect only on certain modules. See documentations of particular modules for details of their behaviors in training/evaluation mode, if they are affected, e.g. [`Dropout`], [`BatchNorm`], etc.

        This is equivalent with [[`self.train(False)`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.train "(in PyTorch v2.9)").

        See [Locally disabling gradient computation](https://docs.pytorch.org/docs/stable/notes/autograd.html#locally-disable-grad-doc "(in PyTorch v2.9)") for a comparison between .eval() and several similar mechanisms that may be confused with it.

        Returns[:]

        :   self

        Return type[:]

        :   [Module](../sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

    [[evaluate]][(]*[[evaluator]][[:]][ ][[[SentenceEvaluator]](../sentence_transformer/evaluation.html#sentence_transformers.evaluation.SentenceEvaluator "sentence_transformers.evaluation.SentenceEvaluator.SentenceEvaluator")]*, *[[output_path]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[dict][[\[]][str][[,]][ ][float][[\]]][ ][[\|]][ ][float]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\SentenceTransformer.py#L2052-L2065)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.evaluate "Link to this definition")

    :   Evaluate the model based on an evaluator

        Parameters[:]

        :   - **evaluator** ([*SentenceEvaluator*](../sentence_transformer/evaluation.html#sentence_transformers.evaluation.SentenceEvaluator "sentence_transformers.evaluation.SentenceEvaluator")) â€" The evaluator used to evaluate the model.

            - **output_path** (*str,* *optional*) â€" The path where the evaluator can write the results. Defaults to None.

        Returns[:]

        :   The evaluation results.

    [[float]][(][)] [[→] [[T]]][ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.float "Link to this definition")

    :   Casts all floating point parameters and buffers to [`float`] datatype.

        ::: 
        Note

        This method modifies the module in-place.
        :::

        Returns[:]

        :   self

        Return type[:]

        :   [Module](../sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

    [[get_adapter_state_dict]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[dict]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\peft_mixin.py#L124-L141)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.get_adapter_state_dict "Link to this definition")

    :   If you are not familiar with adapters and PEFT methods, we invite you to read more about them on the PEFT official documentation: [https://huggingface.co/docs/peft](https://huggingface.co/docs/peft)

        Gets the adapter state dict that should only contain the weights tensors of the specified adapter_name adapter. If no adapter_name is passed, the active adapter is used.

        Parameters[:]

        :   - **\*args** â€" Positional arguments to pass to the underlying AutoModel get_adapter_state_dict function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.get_adapter_state_dict](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.get_adapter_state_dict)

            - **\*\*kwargs** â€" Keyword arguments to pass to the underlying AutoModel get_adapter_state_dict function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.get_adapter_state_dict](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.get_adapter_state_dict)

    [[get_backend]][(][)] [[→] [[Literal][[\[]][[\'torch\']][[,]][ ][[\'onnx\']][[,]][ ][[\'openvino\']][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\SentenceTransformer.py#L408-L414)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.get_backend "Link to this definition")

    :   Return the backend used for inference, which can be one of â€œtorchâ€?, â€œonnxâ€?, or â€œopenvinoâ€?.

        Returns[:]

        :   The backend used for inference.

        Return type[:]

        :   str

    [[get_max_seq_length]][(][)] [[→] [[int][ ][[\|]][ ][None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\SentenceTransformer.py#L1597-L1607)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.get_max_seq_length "Link to this definition")

    :   Returns the maximal sequence length that the model accepts. Longer inputs will be truncated.

        Returns[:]

        :   The maximal sequence length that the model accepts, or None if it is not defined.

        Return type[:]

        :   Optional\[int\]

    [[get_model_kwargs]][(][)] [[→] [[list][[\[]][str][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\SentenceTransformer.py#L416-L444)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.get_model_kwargs "Link to this definition")

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

    [[get_sentence_embedding_dimension]][(][)] [[→] [[int][ ][[\|]][ ][None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\sparse_encoder\SparseEncoder.py#L824-L839)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.get_sentence_embedding_dimension "Link to this definition")

    :   Returns the number of dimensions in the output of [[`SparseEncoder.encode`]](#sentence_transformers.sparse_encoder.SparseEncoder.encode "sentence_transformers.sparse_encoder.SparseEncoder.encode"). We override the function without updating regarding the truncate dim as for sparse model the dimension of the output is the same, only the active dimensions number changes.

        Returns[:]

        :   The number of dimensions in the output of encode. If itâ€™s not known, itâ€™s None.

        Return type[:]

        :   Optional\[int\]

    [[half]][(][)] [[→] [[T]]][ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.half "Link to this definition")

    :   Casts all floating point parameters and buffers to [`half`] datatype.

        ::: 
        Note

        This method modifies the module in-place.
        :::

        Returns[:]

        :   self

        Return type[:]

        :   [Module](../sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

    [[intersection]][(]*[[embeddings_1]][[:]][ ][[[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]*, *[[embeddings_2]][[:]][ ][[[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]*[)] [[→] [[[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\sparse_encoder\SparseEncoder.py#L1272-L1312)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.intersection "Link to this definition")

    :   Compute the intersection of two sparse embeddings.

        Parameters[:]

        :   - **embeddings_1** ([*torch.Tensor*](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")) â€" First embedding tensor, (vocab).

            - **embeddings_2** ([*torch.Tensor*](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")) â€" Second embedding tensor, (vocab) or (batch_size, vocab).

        Returns[:]

        :   Intersection of the two embeddings.

        Return type[:]

        :   [torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")

    [[load_adapter]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\peft_mixin.py#L40-L56)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.load_adapter "Link to this definition")

    :   Load adapter weights from file or remote Hub folder.â€? If you are not familiar with adapters and PEFT methods, we invite you to read more about them on PEFT official documentation: [https://huggingface.co/docs/peft](https://huggingface.co/docs/peft)

        Requires peft as a backend to load the adapter weights and the underlying model to be compatible with PEFT.

        Parameters[:]

        :   - **\*args** â€" Positional arguments to pass to the underlying AutoModel load_adapter function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.load_adapter](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.load_adapter)

            - **\*\*kwargs** â€" Keyword arguments to pass to the underlying AutoModel load_adapter function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.load_adapter](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.load_adapter)

    *[property][ ]*[[max_seq_length]]*[[:]][ ][int]*[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.max_seq_length "Link to this definition")

    :   Returns the maximal input sequence length for the model. Longer inputs will be truncated.

        Returns[:]

        :   The maximal input sequence length.

        Return type[:]

        :   int

        Example

        :::: 
        ::: highlight
            from sentence_transformers import SparseEncoder

            model = SparseEncoder("naver/splade-cocondenser-ensembledistil")
            print(model.max_seq_length)
            # => 512
        :::
        ::::

    [[model_card_data_class]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\sparse_encoder\model_card.py#L22-L131)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.model_card_data_class "Link to this definition")

    :   alias of [[`SparseEncoderModelCardData`]](#sentence_transformers.sparse_encoder.model_card.SparseEncoderModelCardData "sentence_transformers.sparse_encoder.model_card.SparseEncoderModelCardData")

    [[push_to_hub]][(]*[[repo_id]][[:]][ ][[str]]*, *[[token]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[private]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[safe_serialization]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[commit_message]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[local_model_path]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[exist_ok]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[replace_model_card]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[train_datasets]][[:]][ ][[list][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[revision]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[create_pr]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)] [[→] [[str]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\sparse_encoder\SparseEncoder.py#L912-L957)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.push_to_hub "Link to this definition")

    :   Uploads all elements of this Sparse Encoder to a new HuggingFace Hub repository.

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

    [[save_pretrained]][(]*[[path]][[:]][ ][[str]]*, *[[model_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[create_model_card]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[train_datasets]][[:]][ ][[list][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[safe_serialization]][[:]][ ][[bool]][ ][[=]][ ][[True]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\sparse_encoder\SparseEncoder.py#L876-L902)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.save_pretrained "Link to this definition")

    :   Saves a model and its configuration files to a directory, so that it can be loaded with [`SparseEncoder(path)`] again.

        Parameters[:]

        :   - **path** (*str*) â€" Path on disk where the model will be saved.

            - **model_name** (*str,* *optional*) â€" Optional model name.

            - **create_model_card** (*bool,* *optional*) â€" If True, create a README.md with basic information about this model.

            - **train_datasets** (*List\[str\],* *optional*) â€" Optional list with the names of the datasets used to train the model.

            - **safe_serialization** (*bool,* *optional*) â€" If True, save the model using safetensors. If False, save the model the traditional (but unsafe) PyTorch way.

    [[set_adapter]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\peft_mixin.py#L78-L91)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.set_adapter "Link to this definition")

    :   Sets a specific adapter by forcing the model to use a that adapter and disable the other adapters.

        Parameters[:]

        :   - **\*args** â€" Positional arguments to pass to the underlying AutoModel set_adapter function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.set_adapter](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.set_adapter)

            - **\*\*kwargs** â€" Keyword arguments to pass to the underlying AutoModel set_adapter function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.set_adapter](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.set_adapter)

    [[set_pooling_include_prompt]][(]*[[include_prompt]][[:]][ ][[bool]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\SentenceTransformer.py#L1558-L1574)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.set_pooling_include_prompt "Link to this definition")

    :   Sets the include_prompt attribute in the pooling layer in the model, if there is one.

        This is useful for INSTRUCTOR models, as the prompt should be excluded from the pooling strategy for these models.

        Parameters[:]

        :   **include_prompt** (*bool*) â€" Whether to include the prompt in the pooling layer.

        Returns[:]

        :   None

    *[property][ ]*[[similarity]]*[[:]][ ][Callable][[\[]][[\[]][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][ndarray][[\[]][Any][[,]][ ][dtype][[\[]][float32][[\]]][[\]]][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][ndarray][[\[]][Any][[,]][ ][dtype][[\[]][float32][[\]]][[\]]][[\]]][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]]*[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.similarity "Link to this definition")

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
            >>> model = SparseEncoder("naver/splade-cocondenser-ensembledistil")
            >>> sentences = [
            ...     "The weather is so nice!",
            ...     "It's so sunny outside.",
            ...     "He's driving to the movie theater.",
            ...     "She's going to the cinema.",
            ... ]
            >>> embeddings = model.encode(sentences, normalize_embeddings=True)
            >>> model.similarity(embeddings, embeddings)
            tensor([[   30.953,    12.871,     0.000,     0.011],
                    [   12.871,    27.505,     0.580,     0.578],
                    [    0.000,     0.580,    36.068,    15.301],
                    [    0.011,     0.578,    15.301,    39.466]])
            >>> model.similarity_fn_name
            "dot"
            >>> model.similarity_fn_name = "cosine"
            >>> model.similarity(embeddings, embeddings)
            tensor([[    1.000,     0.441,     0.000,     0.000],
                    [    0.441,     1.000,     0.018,     0.018],
                    [    0.000,     0.018,     1.000,     0.406],
                    [    0.000,     0.018,     0.406,     1.000]])
        :::
        ::::

    *[property][ ]*[[similarity_fn_name]]*[[:]][ ][Literal][[\[]][[\'cosine\']][[,]][ ][[\'dot\']][[,]][ ][[\'euclidean\']][[,]][ ][[\'manhattan\']][[\]]]*[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.similarity_fn_name "Link to this definition")

    :   Return the name of the similarity function used by [[`SparseEncoder.similarity()`]](#sentence_transformers.sparse_encoder.SparseEncoder.similarity "sentence_transformers.sparse_encoder.SparseEncoder.similarity") and [[`SparseEncoder.similarity_pairwise()`]](#sentence_transformers.sparse_encoder.SparseEncoder.similarity_pairwise "sentence_transformers.sparse_encoder.SparseEncoder.similarity_pairwise").

        Returns[:]

        :   

            The name of the similarity function. Can be None if not set, in which case it will

            :   default to â€œcosineâ€? when first called.

        Return type[:]

        :   Optional\[str\]

        Example

        :::: 
        ::: highlight
            >>> model = SparseEncoder("naver/splade-cocondenser-ensembledistil")
            >>> model.similarity_fn_name
            'dot'
        :::
        ::::

    *[property][ ]*[[similarity_pairwise]]*[[:]][ ][Callable][[\[]][[\[]][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][ndarray][[\[]][Any][[,]][ ][dtype][[\[]][float32][[\]]][[\]]][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][ndarray][[\[]][Any][[,]][ ][dtype][[\[]][float32][[\]]][[\]]][[\]]][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]]*[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.similarity_pairwise "Link to this definition")

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
            >>> model = SparseEncoder("naver/splade-cocondenser-ensembledistil")
            >>> sentences = [
            ...     "The weather is so nice!",
            ...     "It's so sunny outside.",
            ...     "He's driving to the movie theater.",
            ...     "She's going to the cinema.",
            ... ]
            >>> embeddings = model.encode(sentences, convert_to_sparse_tensor=False)
            >>> model.similarity_pairwise(embeddings[::2], embeddings[1::2])
            tensor([12.871, 15.301])
            >>> model.similarity_fn_name
            "dot"
            >>> model.similarity_fn_name = "cosine"
            >>> model.similarity_pairwise(embeddings[::2], embeddings[1::2])
            tensor([0.441, 0.406])
        :::
        ::::

    [[smart_batching_collate]][(]*[[batch]][[:]][ ][[list][[\[]][InputExample][[\]]]]*[)] [[→] [[tuple][[\[]][list][[\[]][dict][[\[]][str][[,]][ ][Tensor][[\]]][[\]]][[,]][ ][Tensor][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\fit_mixin.py#L441-L463)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.smart_batching_collate "Link to this definition")

    :   Transforms a batch from a SmartBatchingDataset to a batch of tensors for the model Here, batch is a list of InputExample instances: \[InputExample(â€¦), â€¦\]

        Parameters[:]

        :   **batch** â€" a batch from a SmartBatchingDataset

        Returns[:]

        :   a batch of tensors for the model

    *[static][ ]*[[sparsity]][(]*[[embeddings]][[:]][ ][[[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]*[)] [[→] [[dict][[\[]][str][[,]][ ][float][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\sparse_encoder\SparseEncoder.py#L1130-L1191)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.sparsity "Link to this definition")

    :   Calculate sparsity statistics for the given embeddings, including the mean number of active dimensions and the mean sparsity ratio.

        Parameters[:]

        :   **embeddings** ([*torch.Tensor*](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")) â€" The embeddings to analyze.

        Returns[:]

        :   Dictionary with the mean active dimensions and mean sparsity ratio.

        Return type[:]

        :   dict\[str, float\]

        Example

        :   :::: 
            ::: highlight
                from sentence_transformers import SparseEncoder

                model = SparseEncoder("naver/splade-cocondenser-ensembledistil")
                embeddings = model.encode(["The weather is so nice!", "It's so sunny outside."])
                stats = model.sparsity(embeddings)
                print(stats)
                # => 
            :::
            ::::

    *[property][ ]*[[splade_pooling_chunk_size]]*[[:]][ ][int][ ][[\|]][ ][None]*[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.splade_pooling_chunk_size "Link to this definition")

    :   Returns the chunk size of the SpladePooling module, if present. This Chunk size is along the sequence length dimension (i.e., number of tokens per chunk). If None, processes entire sequence at once. Using smaller chunks the reduces memory usage but may lower the training and inference speed. Default is None.

        Returns[:]

        :   The chunk size, or None if SpladePooling is not found or chunk_size is not set.

        Return type[:]

        :   Optional\[int\]

    [[start_multi_process_pool]][(]*[[target_devices]][[:]][ ][[list][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[dict][[\[]][Literal][[\[]][[\'input\']][[,]][ ][[\'output\']][[,]][ ][[\'processes\']][[\]]][[,]][ ][Any][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\SentenceTransformer.py#L1304-L1351)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.start_multi_process_pool "Link to this definition")

    :   Starts a multi-process pool to process the encoding with several independent processes via [[`SentenceTransformer.encode_multi_process`]](../sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode_multi_process "sentence_transformers.SentenceTransformer.encode_multi_process").

        This method is recommended if you want to encode on multiple GPUs or CPUs. It is advised to start only one process per GPU. This method works together with encode_multi_process and stop_multi_process_pool.

        Parameters[:]

        :   **target_devices** (*List\[str\],* *optional*) â€" PyTorch target devices, e.g. \[â€œcuda:0â€?, â€œcuda:1â€?, â€¦\], \[â€œnpu:0â€?, â€œnpu:1â€?, â€¦\], or \[â€œcpuâ€?, â€œcpuâ€?, â€œcpuâ€?, â€œcpuâ€?\]. If target_devices is None and CUDA/NPU is available, then all available CUDA/NPU devices will be used. If target_devices is None and CUDA/NPU is not available, then 4 CPU devices will be used.

        Returns[:]

        :   A dictionary with the target processes, an input queue, and an output queue.

        Return type[:]

        :   Dict\[str, Any\]

    *[static][ ]*[[stop_multi_process_pool]][(]*[[pool]][[:]][ ][[dict][[\[]][Literal][[\[]][[\'input\']][[,]][ ][[\'output\']][[,]][ ][[\'processes\']][[\]]][[,]][ ][Any][[\]]]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\SentenceTransformer.py#L1353-L1372)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.stop_multi_process_pool "Link to this definition")

    :   Stops all processes started with start_multi_process_pool.

        Parameters[:]

        :   **pool** (*Dict\[str,* *object\]*) â€" A dictionary containing the input queue, output queue, and process list.

        Returns[:]

        :   None

    [[to]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.to "Link to this definition")

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

        Its signature is similar to [[`torch.Tensor.to()`]](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.to.html#torch.Tensor.to "(in PyTorch v2.9)"), but only accepts floating point or complex [`dtype`]s. In addition, this method will only cast the floating point or complex parameters and buffers to [`dtype`] (if given). The integral parameters and buffers will be moved [[`device`]](#sentence_transformers.sparse_encoder.SparseEncoder.device "sentence_transformers.sparse_encoder.SparseEncoder.device"), if that is given, but with dtypes unchanged. When [`non_blocking`] is set, it tries to convert/move asynchronously with respect to the host if possible, e.g., moving CPU Tensors with pinned memory to CUDA devices.

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

        :   [Module](../sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

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

    [[tokenize]][(]*[[texts]][[:]][ ][[list][[\[]][str][[\]]][ ][[\|]][ ][list][[\[]][dict][[\]]][ ][[\|]][ ][list][[\[]][tuple][[\[]][str][[,]][ ][str][[\]]][[\]]]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[dict][[\[]][str][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\SentenceTransformer.py#L1609-L1623)[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.tokenize "Link to this definition")

    :   Tokenizes the texts.

        Parameters[:]

        :   **texts** (*Union\[List\[str\],* *List\[Dict\],* *List\[Tuple\[str,* *str\]\]\]*) â€" A list of texts to be tokenized.

        Returns[:]

        :   

            A dictionary of tensors with the tokenized texts. Common keys are â€œinput_idsâ€?,

            :   â€?attention_maskâ€?, and â€œtoken_type_idsâ€?.

        Return type[:]

        :   Dict\[str, Tensor\]

    *[property][ ]*[[tokenizer]]*[[:]][ ][Any]*[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.tokenizer "Link to this definition")

    :   Property to get the tokenizer that is used by this model

    [[train]][(]*[[mode]][[:]][ ][[bool]][ ][[=]][ ][[True]]*[)] [[→] [[T]]][ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.train "Link to this definition")

    :   Sets the module in training mode.

        This has any effect only on certain modules. See documentations of particular modules for details of their behaviors in training/evaluation mode, if they are affected, e.g. [`Dropout`], [`BatchNorm`], etc.

        Parameters[:]

        :   **mode** (*bool*) â€" whether to set training mode ([`True`]) or evaluation mode ([`False`]). Default: [`True`].

        Returns[:]

        :   self

        Return type[:]

        :   [Module](../sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

    *[property][ ]*[[transformers_model]]*[[:]][ ][PreTrainedModel][ ][[\|]][ ][None]*[ïƒ?](#sentence_transformers.sparse_encoder.SparseEncoder.transformers_model "Link to this definition")

    :   Property to get the underlying transformers PreTrainedModel instance, if it exists. Note that itâ€™s possible for a model to have multiple underlying transformers models, but this property will return the first one it finds in the module hierarchy.

        Returns[:]

        :   The underlying transformers model or None if not found.

        Return type[:]

        :   PreTrainedModel or None

        Example

        :::: 
        ::: highlight
            from sentence_transformers import SparseEncoder

            model = SparseEncoder("naver/splade-v3")

            # You can now access the underlying transformers model
            transformers_model = model.transformers_model
            print(type(transformers_model))
            # => <class 'transformers.models.bert.modeling_bert.BertForMaskedLM'>
        :::
        ::::

## SparseEncoderModelCardData[ïƒ?](#sparseencodermodelcarddata "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.model_card.]][[SparseEncoderModelCardData]][(]*[[language:] [str] [\|] [list\[str\]] [\|] [None] [=] [\<factory\>]]*, *[[license:] [str] [\|] [None] [=] [None]]*, *[[model_name:] [str] [\|] [None] [=] [None]]*, *[[model_id:] [str] [\|] [None] [=] [None]]*, *[[train_datasets:] [list\[dict\[str]]*, *[[str\]\]] [=] [\<factory\>]]*, *[[eval_datasets:] [list\[dict\[str]]*, *[[str\]\]] [=] [\<factory\>]]*, *[[task_name:] [str] [\|] [None] [=] [None]]*, *[[tags:] [list\[str\]] [\|] [None] [=] [\<factory\>]]*, *[[local_files_only:] [bool] [=] [False]]*, *[[generate_widget_examples:] [bool] [=] [True]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\sparse_encoder\model_card.py#L22-L131)[ïƒ?](#sentence_transformers.sparse_encoder.model_card.SparseEncoderModelCardData "Link to this definition")

:   A dataclass storing data used in the model card.

    Parameters[:]

    :   - **language** (Optional\[Union\[str, List\[str\]\]\]) â€" The model language, either a string or a list, e.g. â€œenâ€? or \[â€œenâ€?, â€œdeâ€?, â€œnlâ€?\]

        - **license** (Optional\[str\]) â€" The license of the model, e.g. â€œapache-2.0â€?, â€œmitâ€?, or â€œcc-by-nc-sa-4.0â€?

        - **model_name** (Optional\[str\]) â€" The pretty name of the model, e.g. â€œSparseEncoder based on answerdotai/ModernBERT-baseâ€?.

        - **model_id** (Optional\[str\]) â€" The model ID when pushing the model to the Hub, e.g. â€œtomaarsen/se-mpnet-base-ms-marcoâ€?.

        - **train_datasets** (List\[Dict\[str, str\]\]) â€" A list of the names and/or Hugging Face dataset IDs of the training datasets. e.g. \[, , \]

        - **eval_datasets** (List\[Dict\[str, str\]\]) â€" A list of the names and/or Hugging Face dataset IDs of the evaluation datasets. e.g. \[, \]

        - **task_name** (str) â€" The human-readable task the model is trained on, e.g. â€œsemantic search and sparse retrievalâ€?.

        - **tags** (Optional\[List\[str\]\]) â€" A list of tags for the model, e.g. \[â€œsentence-transformersâ€?, â€œsparse-encoderâ€?\].

        - **local_files_only** (bool) â€" If True, donâ€™t attempt to find dataset or base model information on the Hub.Add commentMore actions Defaults to False.

        - **generate_widget_examples** (bool) â€" If True, generate widget examples from the evaluation or training dataset, and compute their similarities. Defaults to True.

    ::: 
    Tip

    Install [codecarbon](https://github.com/mlco2/codecarbon) to automatically track carbon emission usage and include it in your model cards.
    :::

    Example:

    :::: 
    ::: highlight
        >>> model = SparseEncoder(
        ...     "microsoft/mpnet-base",
        ...     model_card_data=SparseEncoderModelCardData(
        ...         model_id="tomaarsen/se-mpnet-base-allnli",
        ...         train_datasets=[, ],
        ...         eval_datasets=[, ],
        ...         license="apache-2.0",
        ...         language="en",
        ...     ),
        ... )
    :::
    ::::

    [[pipeline_tag]]*[[:]][ ][str][ ][[=]][ ][None]*[ïƒ?](#sentence_transformers.sparse_encoder.model_card.SparseEncoderModelCardData.pipeline_tag "Link to this definition")

    :   

    [[task_name]]*[[:]][ ][str][ ][[=]][ ][None]*[ïƒ?](#sentence_transformers.sparse_encoder.model_card.SparseEncoderModelCardData.task_name "Link to this definition")

    :   

## SimilarityFunction[ïƒ?](#similarityfunction "Link to this heading")

*[class][ ]*[[sentence_transformers.]][[SimilarityFunction]][(]*[[value]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\similarity_functions.py#L21-L129)[ïƒ?](#sentence_transformers.SimilarityFunction "Link to this definition")

:   Enum class for supported similarity functions. The following functions are supported:

    - [`SimilarityFunction.COSINE`] ([`"cosine"`]): Cosine similarity

    - [`SimilarityFunction.DOT_PRODUCT`] ([`"dot"`], [`dot_product`]): Dot product similarity

    - [`SimilarityFunction.EUCLIDEAN`] ([`"euclidean"`]): Euclidean distance

    - [`SimilarityFunction.MANHATTAN`] ([`"manhattan"`]): Manhattan distance

    *[static][ ]*[[possible_values]][(][)] [[→] [[list][[\[]][str][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\similarity_functions.py#L116-L129)[ïƒ?](#sentence_transformers.SimilarityFunction.possible_values "Link to this definition")

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

    *[static][ ]*[[to_similarity_fn]][(]*[[similarity_function]][[:]][ ][[str][ ][[\|]][ ][[SimilarityFunction]](#sentence_transformers.SimilarityFunction "sentence_transformers.similarity_functions.SimilarityFunction")]*[)] [[→] [[Callable][[\[]][[\[]][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][ndarray][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][ndarray][[\]]][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\similarity_functions.py#L37-L73)[ïƒ?](#sentence_transformers.SimilarityFunction.to_similarity_fn "Link to this definition")

    :   Converts a similarity function name or enum value to the corresponding similarity function.

        Parameters[:]

        :   **similarity_function** (*Union\[str,* [*SimilarityFunction*](#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")*\]*) â€" The name or enum value of the similarity function.

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

    *[static][ ]*[[to_similarity_pairwise_fn]][(]*[[similarity_function]][[:]][ ][[str][ ][[\|]][ ][[SimilarityFunction]](#sentence_transformers.SimilarityFunction "sentence_transformers.similarity_functions.SimilarityFunction")]*[)] [[→] [[Callable][[\[]][[\[]][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][ndarray][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][ndarray][[\]]][[,]][ ][[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\similarity_functions.py#L75-L114)[ïƒ?](#sentence_transformers.SimilarityFunction.to_similarity_pairwise_fn "Link to this definition")

    :   Converts a similarity function into a pairwise similarity function.

        The pairwise similarity function returns the diagonal vector from the similarity matrix, i.e. it only computes the similarity(a\[i\], b\[i\]) for each i in the range of the input tensors, rather than computing the similarity between all pairs of a and b.

        Parameters[:]

        :   **similarity_function** (*Union\[str,* [*SimilarityFunction*](#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")*\]*) â€" The name or enum value of the similarity function.

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