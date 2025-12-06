# Source: https://www.sbert.net/docs/package_reference/cross_encoder/cross_encoder.html

# CrossEncoder[ïƒ?](#crossencoder "Link to this heading")

## CrossEncoder[ïƒ?](#id1 "Link to this heading")

For an introduction to Cross-Encoders, see [[Cross-Encoders]](../../cross_encoder/usage/usage.html).

*[class][ ]*[[sentence_transformers.cross_encoder.]][[CrossEncoder]][(]*[[model_name_or_path]][[:]][ ][[str]]*, *[[num_labels]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[max_length]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[activation_fn]][[:]][ ][[Callable][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[device]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[cache_folder]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[trust_remote_code]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[revision]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[local_files_only]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[token]][[:]][ ][[bool][ ][[\|]][ ][str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[model_kwargs]][[:]][ ][[dict][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[tokenizer_kwargs]][[:]][ ][[dict][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[config_kwargs]][[:]][ ][[dict][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[model_card_data]][[:]][ ][[[CrossEncoderModelCardData]](#sentence_transformers.cross_encoder.model_card.CrossEncoderModelCardData "sentence_transformers.cross_encoder.model_card.CrossEncoderModelCardData")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[backend]][[:]][ ][[Literal][[\[]][[\'torch\']][[,]][ ][[\'onnx\']][[,]][ ][[\'openvino\']][[\]]]][ ][[=]][ ][[\'torch\']]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\cross_encoder\CrossEncoder.py#L49-L766)[ïƒ?](#sentence_transformers.cross_encoder.CrossEncoder "Link to this definition")

:   A CrossEncoder takes exactly two sentences / texts as input and either predicts a score or label for this sentence pair. It can for example predict the similarity of the sentence pair on a scale of 0 â€¦ 1.

    It does not yield a sentence embedding and does not work for individual sentences.

    Parameters[:]

    :   - **model_name_or_path** (*str*) â€" A model name from Hugging Face Hub that can be loaded with AutoModel, or a path to a local model. We provide several pre-trained CrossEncoder models that can be used for common tasks.

        - **num_labels** (*int,* *optional*) â€" Number of labels of the classifier. If 1, the CrossEncoder is a regression model that outputs a continuous score 0â€¦1. If \> 1, it output several scores that can be soft-maxed to get probability scores for the different classes. Defaults to None.

        - **max_length** (*int,* *optional*) â€" Max length for input sequences. Longer sequences will be truncated. If None, max length of the model will be used. Defaults to None.

        - **activation_fn** (*Callable,* *optional*) â€" Callable (like nn.Sigmoid) about the default activation function that should be used on-top of model.predict(). If None. nn.Sigmoid() will be used if num_labels=1, else nn.Identity(). Defaults to None.

        - **device** (*str,* *optional*) â€" Device (like â€œcudaâ€?, â€œcpuâ€?, â€œmpsâ€?, â€œnpuâ€?) that should be used for computation. If None, checks if a GPU can be used.

        - **cache_folder** (str, Path, optional) â€" Path to the folder where cached files are stored.

        - **trust_remote_code** (*bool,* *optional*) â€" Whether or not to allow for custom models defined on the Hub in their own modeling files. This option should only be set to True for repositories you trust and in which you have read the code, as it will execute code present on the Hub on your local machine. Defaults to False.

        - **revision** (*str,* *optional*) â€" The specific model version to use. It can be a branch name, a tag name, or a commit id, for a stored model on Hugging Face. Defaults to None.

        - **local_files_only** (*bool,* *optional*) â€" Whether or not to only look at local files (i.e., do not try to download the model).

        - **token** (*bool* *or* *str,* *optional*) â€" Hugging Face authentication token to download private models.

        - **model_kwargs** (*Dict\[str,* *Any\],* *optional*) â€"

          Additional model configuration parameters to be passed to the Hugging Face Transformers model. Particularly useful options are:

          - [`torch_dtype`]: Override the default torch.dtype and load the model under a specific dtype. The different options are:

            > ::: 
            > 1\. [`torch.float16`], [`torch.bfloat16`] or [`torch.float`]: load in a specified [`dtype`], ignoring the modelâ€™s [`config.torch_dtype`] if one exists. If not specified - the model will get loaded in [`torch.float`] (fp32).
            >
            > 2\. [`"auto"`] - A [`torch_dtype`] entry in the [`config.json`] file of the model will be attempted to be used. If this entry isnâ€™t found then next check the [`dtype`] of the first weight in the checkpoint thatâ€™s of a floating point type and use that as [`dtype`]. This will load the model using the [`dtype`] it was saved in at the end of the training. It canâ€™t be used as an indicator of how the model was trained. Since it could be trained in one of half precision dtypes, but saved in fp32.
            > :::

          - [`attn_implementation`]: The attention implementation to use in the model (if relevant). Can be any of â€œeagerâ€? (manual implementation of the attention), â€œsdpaâ€? (using [F.scaled_dot_product_attention](https://pytorch.org/docs/master/generated/torch.nn.functional.scaled_dot_product_attention.html)), or â€œflash_attention_2â€? (using [Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention)). By default, if available, SDPA will be used for torch\>=2.1.1. The default is otherwise the manual â€œeagerâ€? implementation.

          See the [AutoModelForSequenceClassification.from_pretrained](https://huggingface.co/docs/transformers/en/model_doc/auto#transformers.AutoModelForSequenceClassification.from_pretrained) documentation for more details.

        - **tokenizer_kwargs** (*Dict\[str,* *Any\],* *optional*) â€" Additional tokenizer configuration parameters to be passed to the Hugging Face Transformers tokenizer. See the [AutoTokenizer.from_pretrained](https://huggingface.co/docs/transformers/en/model_doc/auto#transformers.AutoTokenizer.from_pretrained) documentation for more details.

        - **config_kwargs** (*Dict\[str,* *Any\],* *optional*) â€" Additional model configuration parameters to be passed to the Hugging Face Transformers config. See the [AutoConfig.from_pretrained](https://huggingface.co/docs/transformers/en/model_doc/auto#transformers.AutoConfig.from_pretrained) documentation for more details. For example, you can set [`classifier_dropout`] via this parameter.

        - **model_card_data** ([[`SentenceTransformerModelCardData`]](../sentence_transformer/SentenceTransformer.html#sentence_transformers.model_card.SentenceTransformerModelCardData "sentence_transformers.model_card.SentenceTransformerModelCardData"), optional) â€" A model card data object that contains information about the model. This is used to generate a model card when saving the model. If not set, a default model card data object is created.

        - **backend** (*str*) â€" The backend to use for inference. Can be one of â€œtorchâ€? (default), â€œonnxâ€?, or â€œopenvinoâ€?. See [https://sbert.net/docs/cross_encoder/usage/efficiency.html](https://sbert.net/docs/cross_encoder/usage/efficiency.html) for benchmarking information on the different backends.

    Initializes internal Module state, shared by both nn.Module and ScriptModule.

    [[bfloat16]][(][)] [[→] [[T]]][ïƒ?](#sentence_transformers.cross_encoder.CrossEncoder.bfloat16 "Link to this definition")

    :   Casts all floating point parameters and buffers to [`bfloat16`] datatype.

        ::: 
        Note

        This method modifies the module in-place.
        :::

        Returns[:]

        :   self

        Return type[:]

        :   [Module](../sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

    [[compile]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][ïƒ?](#sentence_transformers.cross_encoder.CrossEncoder.compile "Link to this definition")

    :   Compile this Moduleâ€™s forward using [[`torch.compile()`]](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "(in PyTorch v2.9)").

        This Moduleâ€™s \_\_call\_\_ method is compiled and all arguments are passed as-is to [[`torch.compile()`]](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "(in PyTorch v2.9)").

        See [[`torch.compile()`]](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "(in PyTorch v2.9)") for details on the arguments for this function.

    [[cpu]][(][)] [[→] [[T]]][ïƒ?](#sentence_transformers.cross_encoder.CrossEncoder.cpu "Link to this definition")

    :   Moves all model parameters and buffers to the CPU.

        ::: 
        Note

        This method modifies the module in-place.
        :::

        Returns[:]

        :   self

        Return type[:]

        :   [Module](../sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

    [[cuda]][(]*[[device]][[:]][ ][[int][ ][[\|]][ ][[device]](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[T]]][ïƒ?](#sentence_transformers.cross_encoder.CrossEncoder.cuda "Link to this definition")

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

    [[double]][(][)] [[→] [[T]]][ïƒ?](#sentence_transformers.cross_encoder.CrossEncoder.double "Link to this definition")

    :   Casts all floating point parameters and buffers to [`double`] datatype.

        ::: 
        Note

        This method modifies the module in-place.
        :::

        Returns[:]

        :   self

        Return type[:]

        :   [Module](../sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

    [[eval]][(][)] [[→] [[T]]][ïƒ?](#sentence_transformers.cross_encoder.CrossEncoder.eval "Link to this definition")

    :   Sets the module in evaluation mode.

        This has any effect only on certain modules. See documentations of particular modules for details of their behaviors in training/evaluation mode, if they are affected, e.g. [`Dropout`], [`BatchNorm`], etc.

        This is equivalent with [[`self.train(False)`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.train "(in PyTorch v2.9)").

        See [Locally disabling gradient computation](https://docs.pytorch.org/docs/stable/notes/autograd.html#locally-disable-grad-doc "(in PyTorch v2.9)") for a comparison between .eval() and several similar mechanisms that may be confused with it.

        Returns[:]

        :   self

        Return type[:]

        :   [Module](../sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

    [[fit]][(]*[train_dataloader:] [DataLoader,] [evaluator:] [SentenceEvaluator] [\|] [None] [=] [None,] [epochs:] [int] [=] [1,] [loss_fct=None,] [activation_fct=Identity(),] [scheduler:] [str] [=] [\'WarmupLinear\',] [warmup_steps:] [int] [=] [10000,] [optimizer_class:] [type\[Optimizer\]] [=] [\<class] [\'torch.optim.adamw.AdamW\'\>,] [optimizer_params:] [dict\[str,] [object\]] [=] [ [2e-05},] [weight_decay:] [float] [=] [0.01,] [evaluation_steps:] [int] [=] [0,] [output_path:] [str] [\|] [None] [=] [None,] [save_best_model:] [bool] [=] [True,] [max_grad_norm:] [float] [=] [1,] [use_amp:] [bool] [=] [False,] [callback:] [Callable\[\[float,] [int,] [int\],] [None\]] [=] [None,] [show_progress_bar:] [bool] [=] [True]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\cross_encoder\fit_mixin.py#L182-L369)[ïƒ?](#sentence_transformers.cross_encoder.CrossEncoder.fit "Link to this definition")

    :   Deprecated training method from before Sentence Transformers v4.0, it is recommended to use [`CrossEncoderTrainer`] instead. This method uses [`CrossEncoderTrainer`] behind the scenes, but does not provide as much flexibility as the Trainer itself.

        This training approach uses a DataLoader and Loss function to train the model.

        This method should produce equivalent results in v4.0 as before v4.0, but if you encounter any issues with your existing training scripts, then you may wish to use [[`CrossEncoder.old_fit`]](#sentence_transformers.cross_encoder.CrossEncoder.old_fit "sentence_transformers.cross_encoder.CrossEncoder.old_fit") instead. That uses the old training method from before v4.0.

        Parameters[:]

        :   - **train_dataloader** â€" The DataLoader with InputExample instances

            - **evaluator** â€" An evaluator (sentence_transformers.cross_encoder.evaluation) evaluates the model performance during training on held- out dev data. It is used to determine the best model that is saved to disk.

            - **epochs** â€" Number of epochs for training

            - **loss_fct** â€" Which loss function to use for training. If None, will use BinaryCrossEntropy() if self.config.num_labels == 1 else CrossEntropyLoss(). Defaults to None.

            - **activation_fct** â€" Activation function applied on top of logits output of model.

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

    [[float]][(][)] [[→] [[T]]][ïƒ?](#sentence_transformers.cross_encoder.CrossEncoder.float "Link to this definition")

    :   Casts all floating point parameters and buffers to [`float`] datatype.

        ::: 
        Note

        This method modifies the module in-place.
        :::

        Returns[:]

        :   self

        Return type[:]

        :   [Module](../sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

    [[get_backend]][(][)] [[→] [[Literal][[\[]][[\'torch\']][[,]][ ][[\'onnx\']][[,]][ ][[\'openvino\']][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\cross_encoder\CrossEncoder.py#L260-L266)[ïƒ?](#sentence_transformers.cross_encoder.CrossEncoder.get_backend "Link to this definition")

    :   Return the backend used for inference, which can be one of â€œtorchâ€?, â€œonnxâ€?, or â€œopenvinoâ€?.

        Returns[:]

        :   The backend used for inference.

        Return type[:]

        :   str

    [[half]][(][)] [[→] [[T]]][ïƒ?](#sentence_transformers.cross_encoder.CrossEncoder.half "Link to this definition")

    :   Casts all floating point parameters and buffers to [`half`] datatype.

        ::: 
        Note

        This method modifies the module in-place.
        :::

        Returns[:]

        :   self

        Return type[:]

        :   [Module](../sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

    [[old_fit]][(]*[train_dataloader:] [\~torch.utils.data.dataloader.DataLoader,] [evaluator:] [\~sentence_transformers.evaluation.SentenceEvaluator.SentenceEvaluator] [\|] [None] [=] [None,] [epochs:] [int] [=] [1,] [loss_fct=None,] [activation_fct=Identity(),] [scheduler:] [str] [=] [\'WarmupLinear\',] [warmup_steps:] [int] [=] [10000,] [optimizer_class:] [type\[\~torch.optim.optimizer.Optimizer\]] [=] [\<class] [\'torch.optim.adamw.AdamW\'\>,] [optimizer_params:] [dict\[str,] [object\]] [=] [ [2e-05},] [weight_decay:] [float] [=] [0.01,] [evaluation_steps:] [int] [=] [0,] [output_path:] [str] [\|] [None] [=] [None,] [save_best_model:] [bool] [=] [True,] [max_grad_norm:] [float] [=] [1,] [use_amp:] [bool] [=] [False,] [callback:] [\~collections.abc.Callable\[\[float,] [int,] [int\],] [None\]] [\|] [None] [=] [None,] [show_progress_bar:] [bool] [=] [True]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\cross_encoder\fit_mixin.py#L417-L567)[ïƒ?](#sentence_transformers.cross_encoder.CrossEncoder.old_fit "Link to this definition")

    :   Deprecated training method from before Sentence Transformers v4.0, it is recommended to use [`CrossEncoderTrainer`] instead. This method should only be used if you encounter issues with your existing training scripts after upgrading to v4.0.

        This training approach uses a DataLoader and Loss function to train the model.

        Parameters[:]

        :   - **train_dataloader** â€" The DataLoader with InputExample instances

            - **evaluator** â€" An evaluator (sentence_transformers.cross_encoder.evaluation) evaluates the model performance during training on held- out dev data. It is used to determine the best model that is saved to disk.

            - **epochs** â€" Number of epochs for training

            - **loss_fct** â€" Which loss function to use for training. If None, will use BinaryCrossEntropy() if self.config.num_labels == 1 else CrossEntropyLoss(). Defaults to None.

            - **activation_fct** â€" Activation function applied on top of logits output of model.

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

    [[predict]][(]*[[sentences]][[:]][ ][[tuple][[\[]][str][[,]][ ][str][[\]]][ ][[\|]][ ][list][[\[]][str][[\]]]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[show_progress_bar]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[activation_fn]][[:]][ ][[Callable][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[apply_softmax]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[False]]*, *[[convert_to_numpy]][[:]][ ][[Literal][[\[]][[False]][[\]]]][ ][[=]][ ][[True]]*, *[[convert_to_tensor]][[:]][ ][[Literal][[\[]][[False]][[\]]]][ ][[=]][ ][[False]]*[)] [[→] [[[torch.Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\cross_encoder\CrossEncoder.py#L393-L487)[ïƒ?](#sentence_transformers.cross_encoder.CrossEncoder.predict "Link to this definition")\
    [[predict]][(]*[[sentences]][[:]][ ][[list][[\[]][tuple][[\[]][str][[,]][ ][str][[\]]][[\]]][ ][[\|]][ ][list][[\[]][list][[\[]][str][[\]]][[\]]][ ][[\|]][ ][tuple][[\[]][str][[,]][ ][str][[\]]][ ][[\|]][ ][list][[\[]][str][[\]]]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[show_progress_bar]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[activation_fn]][[:]][ ][[Callable][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[apply_softmax]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[False]]*, *[[convert_to_numpy]][[:]][ ][[Literal][[\[]][[True]][[\]]]][ ][[=]][ ][[True]]*, *[[convert_to_tensor]][[:]][ ][[Literal][[\[]][[False]][[\]]]][ ][[=]][ ][[False]]*[)] [[→] [[np.ndarray]]]\
    [[predict]][(]*[[sentences]][[:]][ ][[list][[\[]][tuple][[\[]][str][[,]][ ][str][[\]]][[\]]][ ][[\|]][ ][list][[\[]][list][[\[]][str][[\]]][[\]]][ ][[\|]][ ][tuple][[\[]][str][[,]][ ][str][[\]]][ ][[\|]][ ][list][[\[]][str][[\]]]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[show_progress_bar]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[activation_fn]][[:]][ ][[Callable][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[apply_softmax]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[False]]*, *[[convert_to_numpy]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[convert_to_tensor]][[:]][ ][[Literal][[\[]][[True]][[\]]]][ ][[=]][ ][[False]]*[)] [[→] [[[torch.Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")]]\
    [[predict]][(]*[[sentences]][[:]][ ][[list][[\[]][tuple][[\[]][str][[,]][ ][str][[\]]][[\]]][ ][[\|]][ ][list][[\[]][list][[\[]][str][[\]]][[\]]]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[show_progress_bar]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[activation_fn]][[:]][ ][[Callable][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[apply_softmax]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[False]]*, *[[convert_to_numpy]][[:]][ ][[Literal][[\[]][[False]][[\]]]][ ][[=]][ ][[True]]*, *[[convert_to_tensor]][[:]][ ][[Literal][[\[]][[False]][[\]]]][ ][[=]][ ][[False]]*[)] [[→] [[list][[\[]][[torch.Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]]]]

    :   Performs predictions with the CrossEncoder on the given sentence pairs.

        Parameters[:]

        :   - **sentences** (*Union\[List\[Tuple\[str,* *str\]\],* *Tuple\[str,* *str\]\]*) â€" A list of sentence pairs \[(Sent1, Sent2), (Sent3, Sent4)\] or one sentence pair (Sent1, Sent2).

            - **batch_size** (*int,* *optional*) â€" Batch size for encoding. Defaults to 32.

            - **show_progress_bar** (*bool,* *optional*) â€" Output progress bar. Defaults to None.

            - **activation_fn** (*callable,* *optional*) â€" Activation function applied on the logits output of the CrossEncoder. If None, the [`model.activation_fn`] will be used, which defaults to [[`torch.nn.Sigmoid`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Sigmoid.html#torch.nn.Sigmoid "(in PyTorch v2.9)") if num_labels=1, else [[`torch.nn.Identity`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Identity.html#torch.nn.Identity "(in PyTorch v2.9)"). Defaults to None.

            - **convert_to_numpy** (*bool,* *optional*) â€" Convert the output to a numpy matrix. Defaults to True.

            - **apply_softmax** (*bool,* *optional*) â€" If set to True and model.num_labels \> 1, applies softmax on the logits output such that for each sample, the scores of each class sum to 1. Defaults to False.

            - **convert_to_numpy** â€" Whether the output should be a list of numpy vectors. If False, output a list of PyTorch tensors. Defaults to True.

            - **convert_to_tensor** (*bool,* *optional*) â€" Whether the output should be one large tensor. Overwrites convert_to_numpy. Defaults to False.

        Returns[:]

        :   Predictions for the passed sentence pairs. The return type depends on the [`convert_to_numpy`] and [`convert_to_tensor`] parameters. If [`convert_to_tensor`] is True, the output will be a [[`torch.Tensor`]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)"). If [`convert_to_numpy`] is True, the output will be a [`numpy.ndarray`]. Otherwise, the output will be a list of [[`torch.Tensor`]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)") values.

        Return type[:]

        :   Union\[List\[[torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")\], np.ndarray, [torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")\]

        Examples

        :::: 
        ::: highlight
            from sentence_transformers import CrossEncoder

            model = CrossEncoder("cross-encoder/stsb-roberta-base")
            sentences = [["I love cats", "Cats are amazing"], ["I prefer dogs", "Dogs are loyal"]]
            model.predict(sentences)
            # => array([0.6912767, 0.4303499], dtype=float32)
        :::
        ::::

    [[push_to_hub]][(]*[[repo_id]][[:]][ ][[str]]*, *[[\*]]*, *[[token]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[private]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[safe_serialization]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[commit_message]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[exist_ok]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[revision]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[create_pr]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[tags]][[:]][ ][[list][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[str]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\cross_encoder\CrossEncoder.py#L645-L723)[ïƒ?](#sentence_transformers.cross_encoder.CrossEncoder.push_to_hub "Link to this definition")

    :   Upload the CrossEncoder model to the Hugging Face Hub.

        Example

        :::: 
        ::: highlight
            from sentence_transformers import CrossEncoder

            model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")
            model.push_to_hub("username/my-crossencoder-model")
            # => "https://huggingface.co/username/my-crossencoder-model"
        :::
        ::::

        Parameters[:]

        :   - **repo_id** (*str*) â€" The name of the repository on the Hugging Face Hub, e.g. â€œusername/repo_nameâ€?, â€œorganization/repo_nameâ€? or just â€œrepo_nameâ€?.

            - **token** (*str,* *optional*) â€" The authentication token to use for the Hugging Face Hub API. If not provided, will use the token stored via the Hugging Face CLI.

            - **private** (*bool,* *optional*) â€" Whether to create a private repository. If not specified, the repository will be public.

            - **safe_serialization** (*bool,* *optional*) â€" Whether or not to convert the model weights in safetensors format for safer serialization. Defaults to True.

            - **commit_message** (*str,* *optional*) â€" The commit message to use for the push. Defaults to â€œAdd new CrossEncoder modelâ€?.

            - **exist_ok** (*bool,* *optional*) â€" If True, do not raise an error if the repository already exists. Ignored if [`create_pr=True`]. Defaults to False.

            - **revision** (*str,* *optional*) â€" The git branch to commit to. Defaults to the head of the â€˜mainâ€™ branch.

            - **create_pr** (*bool,* *optional*) â€" Whether to create a Pull Request with the upload or directly commit. Defaults to False.

            - **tags** (*list\[str\],* *optional*) â€" A list of tags to add to the model card. Defaults to None.

        Returns[:]

        :   URL of the commit or pull request (if create_pr=True)

        Return type[:]

        :   str

    [[rank]][(]*[[query]][[:]][ ][[str]]*, *[[documents]][[:]][ ][[list][[\[]][str][[\]]]]*, *[[top_k]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[return_documents]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[show_progress_bar]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[activation_fn]][[:]][ ][[Callable][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[apply_softmax]][[=]][[False]]*, *[[convert_to_numpy]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[convert_to_tensor]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)] [[→] [[list][[\[]][dict][[\[]][Literal][[\[]][[\'corpus_id\']][[,]][ ][[\'score\']][[,]][ ][[\'text\']][[\]]][[,]][ ][int][ ][[\|]][ ][float][ ][[\|]][ ][str][[\]]][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\cross_encoder\CrossEncoder.py#L489-L580)[ïƒ?](#sentence_transformers.cross_encoder.CrossEncoder.rank "Link to this definition")

    :   Performs ranking with the CrossEncoder on the given query and documents. Returns a sorted list with the document indices and scores.

        Parameters[:]

        :   - **query** (*str*) â€" A single query.

            - **documents** (*List\[str\]*) â€" A list of documents.

            - **top_k** (*Optional\[int\],* *optional*) â€" Return the top-k documents. If None, all documents are returned. Defaults to None.

            - **return_documents** (*bool,* *optional*) â€" If True, also returns the documents. If False, only returns the indices and scores. Defaults to False.

            - **batch_size** (*int,* *optional*) â€" Batch size for encoding. Defaults to 32.

            - **show_progress_bar** (*bool,* *optional*) â€" Output progress bar. Defaults to None.

            - **activation_fn** (*\[type\],* *optional*) â€" Activation function applied on the logits output of the CrossEncoder. If None, nn.Sigmoid() will be used if num_labels=1, else nn.Identity. Defaults to None.

            - **convert_to_numpy** (*bool,* *optional*) â€" Convert the output to a numpy matrix. Defaults to True.

            - **apply_softmax** (*bool,* *optional*) â€" If there are more than 2 dimensions and apply_softmax=True, applies softmax on the logits output. Defaults to False.

            - **convert_to_tensor** (*bool,* *optional*) â€" Convert the output to a tensor. Defaults to False.

        Returns[:]

        :   A sorted list with the â€œcorpus_idâ€?, â€œscoreâ€?, and optionally â€œtextâ€? of the documents.

        Return type[:]

        :   List\[Dict\[Literal\[â€œcorpus_idâ€?, â€œscoreâ€?, â€œtextâ€?\], Union\[int, float, str\]\]\]

        Example

        :::: 
        ::: highlight
            from sentence_transformers import CrossEncoder
            model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")

            query = "Who wrote 'To Kill a Mockingbird'?"
            documents = [
                "'To Kill a Mockingbird' is a novel by Harper Lee published in 1960. It was immediately successful, winning the Pulitzer Prize, and has become a classic of modern American literature.",
                "The novel 'Moby-Dick' was written by Herman Melville and first published in 1851. It is considered a masterpiece of American literature and deals with complex themes of obsession, revenge, and the conflict between good and evil.",
                "Harper Lee, an American novelist widely known for her novel 'To Kill a Mockingbird', was born in 1926 in Monroeville, Alabama. She received the Pulitzer Prize for Fiction in 1961.",
                "Jane Austen was an English novelist known primarily for her six major novels, which interpret, critique and comment upon the British landed gentry at the end of the 18th century.",
                "The 'Harry Potter' series, which consists of seven fantasy novels written by British author J.K. Rowling, is among the most popular and critically acclaimed books of the modern era.",
                "'The Great Gatsby', a novel written by American author F. Scott Fitzgerald, was published in 1925. The story is set in the Jazz Age and follows the life of millionaire Jay Gatsby and his pursuit of Daisy Buchanan."
            ]

            model.rank(query, documents, return_documents=True)
        :::
        ::::

        :::: 
        ::: highlight
            [,
            ,
            ,
            ,
            ]
        :::
        ::::

    [[save_pretrained]][(]*[[path]][[:]][ ][[str]]*, *[[\*]]*, *[[safe_serialization]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\cross_encoder\CrossEncoder.py#L595-L608)[ïƒ?](#sentence_transformers.cross_encoder.CrossEncoder.save_pretrained "Link to this definition")

    :   Save the model and tokenizer to the specified path.

        Parameters[:]

        :   - **path** (*str*) â€" Directory where the model should be saved

            - **safe_serialization** (*bool,* *optional*) â€" Whether to save using safetensors or the traditional PyTorch way. Defaults to True.

            - **\*\*kwargs** â€" Additional arguments passed to the underlying save methods of the model and tokenizer.

        Returns[:]

        :   None

    [[set_config_value]][(]*[[key]][[:]][ ][[str]]*, *[[value]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\cross_encoder\CrossEncoder.py#L303-L316)[ïƒ?](#sentence_transformers.cross_encoder.CrossEncoder.set_config_value "Link to this definition")

    :   Set a value in the underlying modelâ€™s config.

        Parameters[:]

        :   - **key** (*str*) â€" The key to set.

            - **value** â€" The value to set.

    [[to]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][ïƒ?](#sentence_transformers.cross_encoder.CrossEncoder.to "Link to this definition")

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

        Its signature is similar to [[`torch.Tensor.to()`]](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.to.html#torch.Tensor.to "(in PyTorch v2.9)"), but only accepts floating point or complex [`dtype`]s. In addition, this method will only cast the floating point or complex parameters and buffers to [`dtype`] (if given). The integral parameters and buffers will be moved [`device`], if that is given, but with dtypes unchanged. When [`non_blocking`] is set, it tries to convert/move asynchronously with respect to the host if possible, e.g., moving CPU Tensors with pinned memory to CUDA devices.

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

    [[train]][(]*[[mode]][[:]][ ][[bool]][ ][[=]][ ][[True]]*[)] [[→] [[T]]][ïƒ?](#sentence_transformers.cross_encoder.CrossEncoder.train "Link to this definition")

    :   Sets the module in training mode.

        This has any effect only on certain modules. See documentations of particular modules for details of their behaviors in training/evaluation mode, if they are affected, e.g. [`Dropout`], [`BatchNorm`], etc.

        Parameters[:]

        :   **mode** (*bool*) â€" whether to set training mode ([`True`]) or evaluation mode ([`False`]). Default: [`True`].

        Returns[:]

        :   self

        Return type[:]

        :   [Module](../sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

    *[property][ ]*[[transformers_model]]*[[:]][ ][PreTrainedModel][ ][[\|]][ ][None]*[ïƒ?](#sentence_transformers.cross_encoder.CrossEncoder.transformers_model "Link to this definition")

    :   Property to get the underlying transformers PreTrainedModel instance.

        Returns[:]

        :   The underlying transformers model or None if not found.

        Return type[:]

        :   PreTrainedModel or None

        Example

        :::: 
        ::: highlight
            from sentence_transformers import CrossEncoder

            model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")

            # You can now access the underlying transformers model
            transformers_model = model.transformers_model
            print(type(transformers_model))
            # => <class 'transformers.models.bert.modeling_bert.BertForSequenceClassification'>
        :::
        ::::

## CrossEncoderModelCardData[ïƒ?](#crossencodermodelcarddata "Link to this heading")

*[class][ ]*[[sentence_transformers.cross_encoder.model_card.]][[CrossEncoderModelCardData]][(]*[[language:] [str] [\|] [list\[str\]] [\|] [None] [=] [\<factory\>]]*, *[[license:] [str] [\|] [None] [=] [None]]*, *[[model_name:] [str] [\|] [None] [=] [None]]*, *[[model_id:] [str] [\|] [None] [=] [None]]*, *[[train_datasets:] [list\[dict\[str]]*, *[[str\]\]] [=] [\<factory\>]]*, *[[eval_datasets:] [list\[dict\[str]]*, *[[str\]\]] [=] [\<factory\>]]*, *[[task_name:] [str] [\|] [None] [=] [None]]*, *[[tags:] [list\[str\]] [\|] [None] [=] [\<factory\>]]*, *[[local_files_only:] [bool] [=] [False]]*, *[[generate_widget_examples:] [bool] [=] [True]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\cross_encoder\model_card.py#L27-L159)[ïƒ?](#sentence_transformers.cross_encoder.model_card.CrossEncoderModelCardData "Link to this definition")

:   A dataclass storing data used in the model card.

    Parameters[:]

    :   - **language** (Optional\[Union\[str, List\[str\]\]\]) â€" The model language, either a string or a list, e.g. â€œenâ€? or \[â€œenâ€?, â€œdeâ€?, â€œnlâ€?\]

        - **license** (Optional\[str\]) â€" The license of the model, e.g. â€œapache-2.0â€?, â€œmitâ€?, or â€œcc-by-nc-sa-4.0â€?

        - **model_name** (Optional\[str\]) â€" The pretty name of the model, e.g. â€œCrossEncoder based on answerdotai/ModernBERT-baseâ€?.

        - **model_id** (Optional\[str\]) â€" The model ID when pushing the model to the Hub, e.g. â€œtomaarsen/ce-mpnet-base-ms-marcoâ€?.

        - **train_datasets** (List\[Dict\[str, str\]\]) â€" A list of the names and/or Hugging Face dataset IDs of the training datasets. e.g. \[, , \]

        - **eval_datasets** (List\[Dict\[str, str\]\]) â€" A list of the names and/or Hugging Face dataset IDs of the evaluation datasets. e.g. \[, \]

        - **task_name** (str) â€" The human-readable task the model is trained on, e.g. â€œsemantic search and paraphrase miningâ€?.

        - **tags** (Optional\[List\[str\]\]) â€" A list of tags for the model, e.g. \[â€œsentence-transformersâ€?, â€œcross-encoderâ€?\].

        - **local_files_only** (bool) â€" If True, donâ€™t attempt to find dataset or base model information on the Hub. Defaults to False.

    ::: 
    Tip

    Install [codecarbon](https://github.com/mlco2/codecarbon) to automatically track carbon emission usage and include it in your model cards.
    :::

    Example:

    :::: 
    ::: highlight
        >>> model = CrossEncoder(
        ...     "microsoft/mpnet-base",
        ...     model_card_data=CrossEncoderModelCardData(
        ...         model_id="tomaarsen/ce-mpnet-base-allnli",
        ...         train_datasets=[, ],
        ...         eval_datasets=[, ],
        ...         license="apache-2.0",
        ...         language="en",
        ...     ),
        ... )
    :::
    ::::