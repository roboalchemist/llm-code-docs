# Source: https://sbert.net/docs/package_reference/sparse_encoder/trainer.html

Title: Trainer — Sentence Transformers documentation

URL Source: https://sbert.net/docs/package_reference/sparse_encoder/trainer.html

Markdown Content:
SparseEncoderTrainer[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sparseencodertrainer "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.sparse_encoder.SparseEncoderTrainer(_model:[SparseEncoder](https://sbert.net/docs/package\_reference/sparse\_encoder/SparseEncoder.html#sentence\_transformers.sparse\_encoder.SparseEncoder "sentence\_transformers.sparse\_encoder.SparseEncoder.SparseEncoder")|None=None_, _args:[SparseEncoderTrainingArguments](https://sbert.net/docs/package\_reference/sparse\_encoder/training\_args.html#sentence\_transformers.sparse\_encoder.training\_args.SparseEncoderTrainingArguments "sentence\_transformers.sparse\_encoder.training\_args.SparseEncoderTrainingArguments")|None=None_, _train\_dataset:Dataset|DatasetDict|dict[str,Dataset]|None=None_, _eval\_dataset:Dataset|DatasetDict|dict[str,Dataset]|None=None_, _loss:[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.10)")|dict[str,[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.10)")]|Callable[[[SparseEncoder](https://sbert.net/docs/package\_reference/sparse\_encoder/SparseEncoder.html#sentence\_transformers.sparse\_encoder.SparseEncoder "sentence\_transformers.sparse\_encoder.SparseEncoder.SparseEncoder")],[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.10)")]|dict[str,Callable[[[SparseEncoder](https://sbert.net/docs/package\_reference/sparse\_encoder/SparseEncoder.html#sentence\_transformers.sparse\_encoder.SparseEncoder "sentence\_transformers.sparse\_encoder.SparseEncoder.SparseEncoder")],[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.10)")]]|None=None_, _evaluator:[SentenceEvaluator](https://sbert.net/docs/package\_reference/sentence\_transformer/evaluation.html#sentence\_transformers.evaluation.SentenceEvaluator "sentence\_transformers.evaluation.SentenceEvaluator.SentenceEvaluator")|list[[SentenceEvaluator](https://sbert.net/docs/package\_reference/sentence\_transformer/evaluation.html#sentence\_transformers.evaluation.SentenceEvaluator "sentence\_transformers.evaluation.SentenceEvaluator.SentenceEvaluator")]|None=None_, _data\_collator:SparseEncoderDataCollator|None=None_, _tokenizer:PreTrainedTokenizerBase|Callable|None=None_, _model\_init:Callable[[],[SparseEncoder](https://sbert.net/docs/package\_reference/sparse\_encoder/SparseEncoder.html#sentence\_transformers.sparse\_encoder.SparseEncoder "sentence\_transformers.sparse\_encoder.SparseEncoder.SparseEncoder")]|None=None_, _compute\_metrics:Callable[[EvalPrediction],dict]|None=None_, _callbacks:list[TrainerCallback]|None=None_, _optimizers:tuple[[Optimizer](https://docs.pytorch.org/docs/stable/optim.html#torch.optim.Optimizer "(in PyTorch v2.10)"),[LambdaLR](https://docs.pytorch.org/docs/stable/generated/torch.optim.lr\_scheduler.LambdaLR.html#torch.optim.lr\_scheduler.LambdaLR "(in PyTorch v2.10)")]=(None,None)_, _preprocess\_logits\_for\_metrics:Callable[[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)"),[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")],[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")]|None=None_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/sparse_encoder/trainer.py#L32-L415)[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer "Link to this definition")
SparseEncoderTrainer is a simple but feature-complete training and eval loop for PyTorch based on the SentenceTransformerTrainer that based on 🤗 Transformers [`Trainer`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.Trainer "(in transformers vmain)").

This trainer integrates support for various [`transformers.TrainerCallback`](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.TrainerCallback "(in transformers vmain)") subclasses, such as:

*   [`WandbCallback`](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.integrations.WandbCallback "(in transformers vmain)") to automatically log training metrics to W&B if wandb is installed

*   [`TensorBoardCallback`](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.integrations.TensorBoardCallback "(in transformers vmain)") to log training metrics to TensorBoard if tensorboard is accessible.

*   [`CodeCarbonCallback`](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.integrations.CodeCarbonCallback "(in transformers vmain)") to track the carbon emissions of your model during training if codecarbon is installed.

> *   Note: These carbon emissions will be included in your automatically generated model card.

See the Transformers [Callbacks](https://huggingface.co/docs/transformers/main/en/main_classes/callback) documentation for more information on the integrated callbacks and how to write your own callbacks.

Parameters:
*   **model** (`SparseEncoder`, _optional_) – The model to train, evaluate or use for predictions. If not provided, a model_init must be passed.

*   **args** ([`SparseEncoderTrainingArguments`](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments "sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments"), _optional_) – The arguments to tweak for training. Will default to a basic instance of [`SparseEncoderTrainingArguments`](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments "sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments") with the output_dir set to a directory named _tmp\_trainer_ in the current directory if not provided.

*   **train_dataset** (Union[[`datasets.Dataset`](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)"), [`datasets.DatasetDict`](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.DatasetDict "(in datasets vmain)"), [`datasets.IterableDataset`](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.IterableDataset "(in datasets vmain)"), Dict[str, [`datasets.Dataset`](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)")]], _optional_) – The dataset to use for training. Must have a format accepted by your loss function, see [Training Overview > Dataset Format](https://sbert.net/docs/sentence_transformer/training_overview.html#dataset-format).

*   **eval_dataset** (Union[[`datasets.Dataset`](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)"), [`datasets.DatasetDict`](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.DatasetDict "(in datasets vmain)"), [`datasets.IterableDataset`](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.IterableDataset "(in datasets vmain)"), Dict[str, [`datasets.Dataset`](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)")]], _optional_) –

The dataset to use for evaluation. Must have a format accepted by your loss function, see [Training Overview > Dataset Format](https://sbert.net/docs/sentence_transformer/training_overview.html#dataset-format).

*   **loss** (Optional[Union[[`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.10)"), Dict[str, [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.10)")], Callable[[`SparseEncoder`], [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.10)")], Dict[str, Callable[[`SparseEncoder`]]]], _optional_) – The loss function to use for training. Can either be a loss class instance, a dictionary mapping dataset names to loss class instances, a function that returns a loss class instance given a model, or a dictionary mapping dataset names to functions that return a loss class instance given a model. In practice, the latter two are primarily used for hyper-parameter optimization. Will default to [`SparseMultipleNegativesRankingLoss`](https://sbert.net/docs/package_reference/sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.SparseMultipleNegativesRankingLoss "sentence_transformers.sparse_encoder.losses.SparseMultipleNegativesRankingLoss") if no `loss` is provided.

*   **evaluator** (Union[[`SentenceEvaluator`](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.SentenceEvaluator "sentence_transformers.evaluation.SentenceEvaluator"), List[[`SentenceEvaluator`](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.SentenceEvaluator "sentence_transformers.evaluation.SentenceEvaluator")]], _optional_) – The evaluator instance for useful evaluation metrics during training. You can use an `evaluator` with or without an `eval_dataset`, and vice versa. Generally, the metrics that an `evaluator` returns are more useful than the loss value returned from the `eval_dataset`. A list of evaluators will be wrapped in a [`SequentialEvaluator`](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.SequentialEvaluator "sentence_transformers.evaluation.SequentialEvaluator") to run them sequentially.

*   **callbacks** (List of [[`transformers.TrainerCallback`](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.TrainerCallback "(in transformers vmain)")], _optional_) –

A list of callbacks to customize the training loop. Will add those to the list of default callbacks detailed in [here](callback).

If you want to remove one of the default callbacks used, use the [Trainer.remove_callback] method.

*   **optimizers** (Tuple[:class:`torch.optim.Optimizer, [`torch.optim.lr_scheduler.LambdaLR`](https://docs.pytorch.org/docs/stable/generated/torch.optim.lr_scheduler.LambdaLR.html#torch.optim.lr_scheduler.LambdaLR "(in PyTorch v2.10)")]`, _optional_, defaults to (None, None)) – A tuple containing the optimizer and the scheduler to use. Will default to an instance of [`torch.optim.AdamW`](https://docs.pytorch.org/docs/stable/generated/torch.optim.AdamW.html#torch.optim.AdamW "(in PyTorch v2.10)") on your model and a scheduler given by [`transformers.get_linear_schedule_with_warmup()`](https://huggingface.co/docs/transformers/main/en/main_classes/optimizer_schedules#transformers.get_linear_schedule_with_warmup "(in transformers vmain)") controlled by args.

Important attributes:

> *   **model** – Always points to the core model. If using a transformers model, it will be a [PreTrainedModel] subclass.
> 
> *   **model_wrapped** – Always points to the most external model in case one or more other modules wrap the original model. This is the model that should be used for the forward pass. For example, under DeepSpeed, the inner model is wrapped in DeepSpeed and then again in torch.nn.DistributedDataParallel. If the inner model hasn’t been wrapped, then self.model_wrapped is the same as self.model.
> 
> *   **is_model_parallel** – Whether or not a model has been switched to a model parallel mode (different from data parallelism, this means some of the model layers are split on different GPUs).
> 
> *   **place_model_on_device** – Whether or not to automatically place the model on the device - it will be set to False if model parallel or deepspeed is used, or if the default TrainingArguments.place_model_on_device is overridden to return False .
> 
> *   **is_in_train** – Whether or not a model is currently running train (e.g. when evaluate is called while in train)

add_callback(_callback_)[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.add_callback "Link to this definition")
Add a callback to the current list of [~transformers.TrainerCallback].

Parameters:
**callback** (type or [~transformers.TrainerCallback]) – A [~transformers.TrainerCallback] class or an instance of a [~transformers.TrainerCallback]. In the first case, will instantiate a member of that class.

_static_ add_dataset_name_transform(_batch:dict[str,list[Any]]_, _dataset\_name:str|None=None_, _transform:Callable[[dict[str,list[Any]]],dict[str,list[Any]]]|None=None_, _**kwargs_)→dict[str,list[Any]][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/trainer.py#L1179-L1211)[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.add_dataset_name_transform "Link to this definition")
A transform/map function that adds prompts or dataset names to the batch.

Parameters:
*   **batch** (_dict_ _[_ _str_ _,_ _list_ _[_ _Any_ _]_ _]_) – The batch of data, where each key is a column name and each value is a list of values.

*   **dataset_name** (_str_ _|_ _None_ _,_ _optional_) – The name of this dataset, only if there are multiple datasets that use a different loss. Defaults to None.

*   **transform** (_Callable_ _[_ _[_ _dict_ _[_ _str_ _,_ _list_ _[_ _Any_ _]_ _]_ _]_ _,_ _dict_ _[_ _str_ _,_ _list_ _[_ _Any_ _]_ _]_ _]_ _,_ _optional_) – An optional transform function to apply on the batch before adding prompts, etc. Defaults to None.

Returns:
The “just-in-time” transformed batch with prompts and/or dataset names added.

Return type:
dict[str, list[Any]]

add_model_card_callback(_default\_args\_dict:dict[str,Any]_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/sparse_encoder/trainer.py#L313-L327)[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.add_model_card_callback "Link to this definition")
Add a callback responsible for automatically tracking data required for the automatic model card generation

This method is called in the `__init__` method of the [`SparseEncoderTrainer`](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer "sentence_transformers.sparse_encoder.trainer.SparseEncoderTrainer") class.

Parameters:
**default_args_dict** (_Dict_ _[_ _str_ _,_ _Any_ _]_) – A dictionary of the default training arguments, so we can determine which arguments have been changed for the model card.

compute_loss(_model:[SparseEncoder](https://sbert.net/docs/package\_reference/sparse\_encoder/SparseEncoder.html#sentence\_transformers.sparse\_encoder.SparseEncoder "sentence\_transformers.sparse\_encoder.SparseEncoder.SparseEncoder")_, _inputs:dict[str,[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")|Any]_, _return\_outputs:bool=False_, _num\_items\_in\_batch=None_)→[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")|tuple[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)"),dict[str,Any]][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/sparse_encoder/trainer.py#L376-L403)[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.compute_loss "Link to this definition")
Computes the loss for the SparseEncoder model.

It uses `self.loss` to compute the loss, which can be a single loss function or a dictionary of loss functions for different datasets. If the loss is a dictionary, the dataset name is expected to be passed in the inputs under the key “dataset_name”. This is done automatically in the `add_dataset_name_column` method. Note that even if `return_outputs = True`, the outputs will be empty, as the SparseEncoder losses do not return outputs.

Parameters:
*   **model** ([_SparseEncoder_](https://sbert.net/docs/package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder")) – The SparseEncoder model.

*   **inputs** (_Dict_ _[_ _str_ _,_ _Union_ _[_[_torch.Tensor_](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_,_ _Any_ _]_ _]_) – The input data for the model.

*   **return_outputs** (_bool_ _,_ _optional_) – Whether to return the outputs along with the loss. Defaults to False.

*   **num_items_in_batch** (_int_ _,_ _optional_) – The number of items in the batch. Defaults to None. Unused, but required by the transformers Trainer.

Returns:
The computed loss. If return_outputs is True, returns a tuple of loss and outputs. Otherwise, returns only the loss.

Return type:
Union[[torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)"), Tuple[[torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)"), Dict[str, Any]]]

create_model_card(_language:str|None=None_, _license:str|None=None_, _tags:str|list[str]|None=None_, _model\_name:str|None=None_, _finetuned\_from:str|None=None_, _tasks:str|list[str]|None=None_, _dataset\_tags:str|list[str]|None=None_, _dataset:str|list[str]|None=None_, _dataset\_args:str|list[str]|None=None_, _**kwargs_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/trainer.py#L1213-L1236)[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.create_model_card "Link to this definition")
Creates a draft of a model card using the information available to the Trainer.

Parameters:
*   **language** (str, _optional_) – The language of the model (if applicable)

*   **license** (str, _optional_) – The license of the model. Will default to the license of the pretrained model used, if the original model given to the Trainer comes from a repo on the Hub.

*   **tags** (str or List[str], _optional_) – Some tags to be included in the metadata of the model card.

*   **model_name** (str, _optional_) – The name of the model.

*   **finetuned_from** (str, _optional_) – The name of the model used to fine-tune this one (if applicable). Will default to the name of the repo of the original model given to the Trainer (if it comes from the Hub).

*   **tasks** (str or List[str], _optional_) – One or several task identifiers, to be included in the metadata of the model card.

*   **dataset_tags** (str or List[str], _optional_) – One or several dataset tags, to be included in the metadata of the model card.

*   **dataset** (str or List[str], _optional_) – One or several dataset identifiers, to be included in the metadata of the model card.

*   **dataset_args** (str or List[str], _optional_) – One or several dataset arguments, to be included in the metadata of the model card.

create_optimizer()[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.create_optimizer "Link to this definition")
Setup the optimizer.

We provide a reasonable default that works well. If you want to use something else, you can pass a tuple in the Trainer’s init through optimizers, or subclass and override this method in a subclass.

create_optimizer_and_scheduler(_num\_training\_steps:int_)[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.create_optimizer_and_scheduler "Link to this definition")
Setup the optimizer and the learning rate scheduler.

We provide a reasonable default that works well. If you want to use something else, you can pass a tuple in the Trainer’s init through optimizers, or subclass and override this method (or create_optimizer and/or create_scheduler) in a subclass.

create_scheduler(_num\_training\_steps:int_, _optimizer:[Optimizer](https://docs.pytorch.org/docs/stable/optim.html#torch.optim.Optimizer "(in PyTorch v2.10)")|None=None_)[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.create_scheduler "Link to this definition")
Setup the scheduler. The optimizer of the trainer must have been set up either before this method is called or passed as an argument.

Parameters:
**num_training_steps** (_int_) – The number of training steps to do.

evaluate(_eval\_dataset:Dataset|dict[str,Dataset]|None=None_, _ignore\_keys:list[str]|None=None_, _metric\_key\_prefix:str='eval'_)→dict[str,float][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/trainer.py#L543-L555)[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.evaluate "Link to this definition")
Run evaluation and returns metrics.

The calling script will be responsible for providing a method to compute metrics, as they are task-dependent (pass it to the init compute_metrics argument).

You can also subclass and override this method to inject custom behavior.

Parameters:
*   **eval_dataset** (Union[Dataset, Dict[str, Dataset]), _optional_) –

Pass a dataset if you wish to override self.eval_dataset. If it is a [~datasets.Dataset], columns not accepted by the model.forward() method are automatically removed. If it is a dictionary, it will evaluate on each dataset, prepending the dictionary key to the metric name. Datasets must implement the  __len__  method.

<Tip>

If you pass a dictionary with names of datasets as keys and datasets as values, evaluate will run separate evaluations on each dataset. This can be useful to monitor how training affects other datasets or simply to get a more fine-grained evaluation. When used with load_best_model_at_end, make sure metric_for_best_model references exactly one of the datasets. If you, for example, pass in {“data1”: data1, “data2”: data2} for two datasets data1 and data2, you could specify metric_for_best_model=”eval_data1_loss” for using the loss on data1 and metric_for_best_model=”eval_data2_loss” for the loss on data2.

</Tip>

*   **ignore_keys** (List[str], _optional_) – A list of keys in the output of your model (if it is a dictionary) that should be ignored when gathering predictions.

*   **metric_key_prefix** (str, _optional_, defaults to “eval”) – An optional prefix to be used as the metrics key prefix. For example the metrics “bleu” will be named “eval_bleu” if the prefix is “eval” (default)

Returns:
A dictionary containing the evaluation loss and the potential metrics computed from the predictions. The dictionary also contains the epoch number which comes from the training state.

get_batch_sampler(_dataset:Dataset_, _batch\_size:int_, _drop\_last:bool_, _valid\_label\_columns:list[str]|None=None_, _generator:[Generator](https://docs.pytorch.org/docs/stable/generated/torch.Generator.html#torch.Generator "(in PyTorch v2.10)")|None=None_, _seed:int=0_)→[BatchSampler](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.BatchSampler "(in PyTorch v2.10)")|None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/trainer.py#L635-L695)[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.get_batch_sampler "Link to this definition")
Returns the appropriate batch sampler based on the `batch_sampler` argument in `self.args`. This batch sampler class supports `__len__` and `__iter__` methods, and is used as the `batch_sampler` to create the [`torch.utils.data.DataLoader`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader "(in PyTorch v2.10)").

Note

Override this method to provide a custom batch sampler.

Parameters:
*   **dataset** (_Dataset_) – The dataset to sample from.

*   **batch_size** (_int_) – Number of samples per batch.

*   **drop_last** (_bool_) – If True, drop the last incomplete batch if the dataset size is not divisible by the batch size.

*   **valid_label_columns** (_List_ _[_ _str_ _]_) – List of column names to check for labels. The first column name from `valid_label_columns` found in the dataset will be used as the label column.

*   **generator** ([_torch.Generator_](https://docs.pytorch.org/docs/stable/generated/torch.Generator.html#torch.Generator "(in PyTorch v2.10)")_,_ _optional_) – Optional random number generator for shuffling the indices.

*   **seed** (_int_) – Seed for the random number generator to ensure reproducibility. Defaults to 0.

get_eval_dataloader(_eval\_dataset:Dataset|DatasetDict|IterableDataset|None=None_)→[DataLoader](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader "(in PyTorch v2.10)")[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/trainer.py#L831-L921)[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.get_eval_dataloader "Link to this definition")
Returns the evaluation [~torch.utils.data.DataLoader].

Subclass and override this method if you want to inject some custom behavior.

Parameters:
**eval_dataset** (torch.utils.data.Dataset, _optional_) – If provided, will override self.eval_dataset. If it is a [~datasets.Dataset], columns not accepted by the model.forward() method are automatically removed. It must implement  __len__ .

get_learning_rates()[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.get_learning_rates "Link to this definition")
Returns the learning rate of each parameter from self.optimizer.

get_multi_dataset_batch_sampler(_dataset:[ConcatDataset](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.ConcatDataset "(in PyTorch v2.10)")_, _batch\_samplers:list[[BatchSampler](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.BatchSampler "(in PyTorch v2.10)")]_, _generator:[Generator](https://docs.pytorch.org/docs/stable/generated/torch.Generator.html#torch.Generator "(in PyTorch v2.10)")|None=None_, _seed:int|None=0_)→[BatchSampler](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.BatchSampler "(in PyTorch v2.10)")[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/trainer.py#L697-L739)[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.get_multi_dataset_batch_sampler "Link to this definition")
Returns the appropriate multi-dataset batch sampler based on the `multi_dataset_batch_sampler` argument in `self.args`. This batch sampler class supports `__len__` and `__iter__` methods, and is used as the `batch_sampler` to create the [`torch.utils.data.DataLoader`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader "(in PyTorch v2.10)").

Note

Override this method to provide a custom multi-dataset batch sampler.

Parameters:
*   **dataset** (_ConcatDataset_) – The concatenation of all datasets.

*   **batch_samplers** (_List_ _[_ _BatchSampler_ _]_) – List of batch samplers for each dataset in the concatenated dataset.

*   **generator** ([_torch.Generator_](https://docs.pytorch.org/docs/stable/generated/torch.Generator.html#torch.Generator "(in PyTorch v2.10)")_,_ _optional_) – Optional random number generator for shuffling the indices.

*   **seed** (_int_ _,_ _optional_) – Optional seed for the random number generator

get_num_trainable_parameters()[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.get_num_trainable_parameters "Link to this definition")
Get the number of trainable parameters.

get_optimizer_group(_param:str|[Parameter](https://docs.pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "(in PyTorch v2.10)")|None=None_)[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.get_optimizer_group "Link to this definition")
Returns optimizer group for a parameter if given, else returns all optimizer groups for params.

Parameters:
**param** (str or torch.nn.parameter.Parameter, _optional_) – The parameter for which optimizer group needs to be returned.

get_test_dataloader(_test\_dataset:Dataset|DatasetDict|IterableDataset_)→[DataLoader](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader "(in PyTorch v2.10)")[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/trainer.py#L923-L1007)[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.get_test_dataloader "Link to this definition")
Returns the training [~torch.utils.data.DataLoader].

Subclass and override this method if you want to inject some custom behavior.

Parameters:
**test_dataset** (torch.utils.data.Dataset, _optional_) – The test dataset to use. If it is a [~datasets.Dataset], columns not accepted by the model.forward() method are automatically removed. It must implement  __len__ .

get_train_dataloader()→[DataLoader](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader "(in PyTorch v2.10)")[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/trainer.py#L741-L829)[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.get_train_dataloader "Link to this definition")
Returns the training [~torch.utils.data.DataLoader].

Will use no sampler if train_dataset does not implement  __len__ , a random sampler (adapted to distributed training if necessary) otherwise.

Subclass and override this method if you want to inject some custom behavior.

hyperparameter_search(_hp\_space:Callable[[optuna.Trial],dict[str,float]]|None=None_, _compute\_objective:Callable[[dict[str,float]],float]|None=None_, _n\_trials:int=20_, _direction:str|list[str]='minimize'_, _backend:str|HPSearchBackend|None=None_, _hp\_name:Callable[[optuna.Trial],str]|None=None_, _**kwargs_)→BestRun|list[BestRun][](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.hyperparameter_search "Link to this definition")
Launch an hyperparameter search using optuna or Ray Tune or SigOpt. The optimized quantity is determined by compute_objective, which defaults to a function returning the evaluation loss when no metric is provided, the sum of all metrics otherwise.

<Tip warning={true}>

To use this method, you need to have provided a model_init when initializing your [Trainer]: we need to reinitialize the model at each new run. This is incompatible with the optimizers argument, so you need to subclass [Trainer] and override the method [~Trainer.create_optimizer_and_scheduler] for custom optimizer/scheduler.

</Tip>

Parameters:
*   **hp_space** (Callable[[“optuna.Trial”], Dict[str, float]], _optional_) – A function that defines the hyperparameter search space. Will default to [~trainer_utils.default_hp_space_optuna] or [~trainer_utils.default_hp_space_ray] or [~trainer_utils.default_hp_space_sigopt] depending on your backend.

*   **compute_objective** (Callable[[Dict[str, float]], float], _optional_) – A function computing the objective to minimize or maximize from the metrics returned by the evaluate method. Will default to [~trainer_utils.default_compute_objective].

*   **n_trials** (int, _optional_, defaults to 100) – The number of trial runs to test.

*   **direction** (str or List[str], _optional_, defaults to “minimize”) – If it’s single objective optimization, direction is str, can be “minimize” or “maximize”, you should pick “minimize” when optimizing the validation loss, “maximize” when optimizing one or several metrics. If it’s multi objectives optimization, direction is List[str], can be List of “minimize” and “maximize”, you should pick “minimize” when optimizing the validation loss, “maximize” when optimizing one or several metrics.

*   **backend** (str or [~training_utils.HPSearchBackend], _optional_) – The backend to use for hyperparameter search. Will default to optuna or Ray Tune or SigOpt, depending on which one is installed. If all are installed, will default to optuna.

*   **hp_name** (Callable[[“optuna.Trial”], str]], _optional_) – A function that defines the trial/run name. Will default to None.

*   **kwargs** (Dict[str, Any], _optional_) –

Additional keyword arguments for each backend:

    *   optuna: parameters from [optuna.study.create_study]([https://optuna.readthedocs.io/en/stable/reference/generated/optuna.study.create_study.html](https://optuna.readthedocs.io/en/stable/reference/generated/optuna.study.create_study.html)) and also the parameters timeout, n_jobs and gc_after_trial from [optuna.study.Study.optimize]([https://optuna.readthedocs.io/en/stable/reference/generated/optuna.study.Study.html#optuna.study.Study.optimize](https://optuna.readthedocs.io/en/stable/reference/generated/optuna.study.Study.html#optuna.study.Study.optimize))

    *   ray: parameters from [tune.run]([https://docs.ray.io/en/latest/tune/api_docs/execution.html#tune-run](https://docs.ray.io/en/latest/tune/api_docs/execution.html#tune-run)). If resources_per_trial is not set in the kwargs, it defaults to 1 CPU core and 1 GPU (if available). If progress_reporter is not set in the kwargs, [ray.tune.CLIReporter]([https://docs.ray.io/en/latest/tune/api/doc/ray.tune.CLIReporter.html](https://docs.ray.io/en/latest/tune/api/doc/ray.tune.CLIReporter.html)) is used.

    *   sigopt: the parameter proxies from [sigopt.Connection.set_proxies]([https://docs.sigopt.com/support/faq#how-do-i-use-sigopt-with-a-proxy](https://docs.sigopt.com/support/faq#how-do-i-use-sigopt-with-a-proxy)).

Returns:
All the information about the best run or best runs for multi-objective optimization. Experiment summary can be found in run_summary attribute for Ray backend.

Return type:
[trainer_utils.BestRun or List[trainer_utils.BestRun]]

is_local_process_zero()→bool[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.is_local_process_zero "Link to this definition")
Whether or not this process is the local (e.g., on one machine if training in a distributed fashion on several machines) main process.

is_world_process_zero()→bool[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.is_world_process_zero "Link to this definition")
Whether or not this process is the global main process (when training in a distributed fashion on several machines, this is only going to be True for one process).

log(_logs:dict[str,float]_, _start\_time:float|None=None_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/trainer.py#L467-L506)[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.log "Link to this definition")
Log logs on the various objects watching training.

Subclass and override this method to inject custom behavior.

Parameters:
*   **logs** (Dict[str, float]) – The values to log.

*   **start_time** (Optional[float]) – The start of training.

maybe_add_dataset_name_column(_dataset:DatasetDict|Dataset|None_, _prompts:dict[str,dict[str,str]]|dict[str,str]|str|None=None_, _router\_mapping:dict[str,dict[str,str]]|dict[str,str]|None=None_, _dataset\_name:str|None=None_)→DatasetDict|Dataset|None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/trainer.py#L1089-L1129)[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.maybe_add_dataset_name_column "Link to this definition")
Maybe add a dataset name column to the dataset, if

1.   the dataset is a DatasetDict, and one of:

> 1.   The loss is a dictionary, or
> 
>     2.   The prompts contain a mapping of dataset names, or
> 
>     3.   The router_mapping contains a mapping of dataset names.

Parameters:
**dataset** (_DatasetDict_ _|_ _Dataset_ _|_ _None_) – The dataset to add prompts or dataset names to.

Returns:
The dataset with prompts or dataset names added.

Return type:
DatasetDict | Dataset | None

pop_callback(_callback_)[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.pop_callback "Link to this definition")
Remove a callback from the current list of [~transformers.TrainerCallback] and returns it.

If the callback is not found, returns None (and no error is raised).

Parameters:
**callback** (type or [~transformers.TrainerCallback]) – A [~transformers.TrainerCallback] class or an instance of a [~transformers.TrainerCallback]. In the first case, will pop the first member of that class found in the list of callbacks.

Returns:
The callback removed, if found.

Return type:
[~transformers.TrainerCallback]

preprocess_dataset(_dataset:DatasetDict|Dataset|None=None_, _prompts:dict[str,dict[str,str]]|dict[str,str]|str|None=None_, _router\_mapping:dict[str,dict[str,str]]|dict[str,str]|None=None_, _dataset\_name:str|None=None_)→DatasetDict|Dataset|None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/trainer.py#L1050-L1087)[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.preprocess_dataset "Link to this definition")
Preprocess the dataset by optionally lazily adding a dataset name column, required for multi-dataset training with multiple losses, for dataset-specific prompts, or for dataset-specific router mappings.

Parameters:
*   **dataset** (_DatasetDict_ _|_ _Dataset_ _|_ _None_) – The dataset to preprocess. If None, no preprocessing is done.

*   **prompts** (_dict_ _[_ _str_ _,_ _dict_ _[_ _str_ _,_ _str_ _]_ _]_ _|_ _dict_ _[_ _str_ _,_ _str_ _]_ _|_ _str_ _|_ _None_) – Optional prompts to add to the dataset. If a string, it is used as a single prompt for all datasets, but it can also be a dictionary mapping dataset names to prompts, a dictionary mapping column names to prompts, or a nested dictionary mapping dataset names to column names to prompts.

*   **router_mapping** (_dict_ _[_ _str_ _,_ _dict_ _[_ _str_ _,_ _str_ _]_ _]_ _|_ _dict_ _[_ _str_ _,_ _str_ _]_ _|_ _None_) – Optional router mapping to add to the dataset. Either a dictionary mapping of column names to [`Router`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Router "sentence_transformers.models.Router") routes or a nested dictionary mapping dataset names to column names to routes.

*   **dataset_name** (_str_ _|_ _None_) – The name of the dataset, used for multi-dataset training with multiple losses.

Returns:
The preprocessed dataset, perhaps with dataset names added as a lazy column.

Return type:
DatasetDict | Dataset | None

propagate_args_to_deepspeed(_auto\_find\_batch\_size=False_)[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.propagate_args_to_deepspeed "Link to this definition")
Sets values in the deepspeed plugin based on the Trainer args

push_to_hub(_commit\_message:str|None='End of training'_, _blocking:bool=True_, _token:str|None=None_, _revision:str|None=None_, _**kwargs_)→str[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.push_to_hub "Link to this definition")
Upload self.model and self.processing_class to the 🤗 model hub on the repo self.args.hub_model_id.

Parameters:
*   **commit_message** (str, _optional_, defaults to “End of training”) – Message to commit while pushing.

*   **blocking** (bool, _optional_, defaults to True) – Whether the function should return only when the git push has finished.

*   **token** (str, _optional_, defaults to None) – Token with write permission to overwrite Trainer’s original args.

*   **revision** (str, _optional_) – The git revision to commit from. Defaults to the head of the “main” branch.

*   **kwargs** (Dict[str, Any], _optional_) – Additional keyword arguments passed along to [~Trainer.create_model_card].

Returns:
The URL of the repository where the model was pushed if blocking=False, or a Future object tracking the progress of the commit if blocking=True.

remove_callback(_callback_)[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.remove_callback "Link to this definition")
Remove a callback from the current list of [~transformers.TrainerCallback].

Parameters:
**callback** (type or [~transformers.TrainerCallback]) – A [~transformers.TrainerCallback] class or an instance of a [~transformers.TrainerCallback]. In the first case, will remove the first member of that class found in the list of callbacks.

save_model(_output\_dir:str|None=None_, _\_internal\_call:bool=False_)[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.save_model "Link to this definition")
Will save the model, so you can reload it using from_pretrained().

Will only save from the main process.

set_initial_training_values(_args:TrainingArguments_, _dataloader:[DataLoader](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader "(in PyTorch v2.10)")_, _total\_train\_batch\_size:int_)[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.set_initial_training_values "Link to this definition")
Calculates and returns the following values: - num_train_epochs - num_update_steps_per_epoch - num_examples - num_train_samples - epoch_based - len_dataloader - max_steps

train(_resume\_from\_checkpoint:bool|str|None=None_, _trial:optuna.Trial|dict[str,Any]|None=None_, _ignore\_keys\_for\_eval:list[str]|None=None_, _**kwargs_)[](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer.train "Link to this definition")
Main training entry point.

Parameters:
*   **resume_from_checkpoint** (str or bool, _optional_) – If a str, local path to a saved checkpoint as saved by a previous instance of [Trainer]. If a bool and equals True, load the last checkpoint in _args.output\_dir_ as saved by a previous instance of [Trainer]. If present, training will resume from the model/optimizer/scheduler states loaded here.

*   **trial** (optuna.Trial or Dict[str, Any], _optional_) – The trial run or the hyperparameter dictionary for hyperparameter search.

*   **ignore_keys_for_eval** (List[str], _optional_) – A list of keys in the output of your model (if it is a dictionary) that should be ignored when gathering predictions for evaluation during the training.

*   **kwargs** (Dict[str, Any], _optional_) – Additional keyword arguments used to hide deprecated arguments
