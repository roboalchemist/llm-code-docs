# Source: https://sbert.net/docs/package_reference/sparse_encoder/training_args.html

Title: Training Arguments — Sentence Transformers documentation

URL Source: https://sbert.net/docs/package_reference/sparse_encoder/training_args.html

Markdown Content:
SparseEncoderTrainingArguments[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sparseencodertrainingarguments "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments(_output\_dir:str|None=None,overwrite\_output\_dir:bool=False,do\_train:bool=False,do\_eval:bool=False,do\_predict:bool=False,eval\_strategy:~transformers.trainer\_utils.IntervalStrategy|str='no',prediction\_loss\_only:bool=False,per\_device\_train\_batch\_size:int=8,per\_device\_eval\_batch\_size:int=8,per\_gpu\_train\_batch\_size:int|None=None,per\_gpu\_eval\_batch\_size:int|None=None,gradient\_accumulation\_steps:int=1,eval\_accumulation\_steps:int|None=None,eval\_delay:float|None=0,torch\_empty\_cache\_steps:int|None=None,learning\_rate:float=5e-05,weight\_decay:float=0.0,adam\_beta1:float=0.9,adam\_beta2:float=0.999,adam\_epsilon:float=1e-08,max\_grad\_norm:float=1.0,num\_train\_epochs:float=3.0,max\_steps:int=-1,lr\_scheduler\_type:~transformers.trainer\_utils.SchedulerType|str='linear',lr\_scheduler\_kwargs:dict|str|None=<factory>,warmup\_ratio:float=0.0,warmup\_steps:int=0,log\_level:str|None='passive',log\_level\_replica:str|None='warning',log\_on\_each\_node:bool=True,logging\_dir:str|None=None,logging\_strategy:~transformers.trainer\_utils.IntervalStrategy|str='steps',logging\_first\_step:bool=False,logging\_steps:float=500,logging\_nan\_inf\_filter:bool=True,save\_strategy:~transformers.trainer\_utils.SaveStrategy|str='steps',save\_steps:float=500,save\_total\_limit:int|None=None,save\_safetensors:bool|None=True,save\_on\_each\_node:bool=False,save\_only\_model:bool=False,restore\_callback\_states\_from\_checkpoint:bool=False,no\_cuda:bool=False,use\_cpu:bool=False,use\_mps\_device:bool=False,seed:int=42,data\_seed:int|None=None,jit\_mode\_eval:bool=False,use\_ipex:bool=False,bf16:bool=False,fp16:bool=False,fp16\_opt\_level:str='O1',half\_precision\_backend:str='auto',bf16\_full\_eval:bool=False,fp16\_full\_eval:bool=False,tf32:bool|None=None,local\_rank:int=-1,ddp\_backend:str|None=None,tpu\_num\_cores:int|None=None,tpu\_metrics\_debug:bool=False,debug:str|list[~transformers.debug\_utils.DebugOption]='',dataloader\_drop\_last:bool=False,eval\_steps:float|None=None,dataloader\_num\_workers:int=0,dataloader\_prefetch\_factor:int|None=None,past\_index:int=-1,run\_name:str|None=None,disable\_tqdm:bool|None=None,remove\_unused\_columns:bool|None=True,label\_names:list[str]|None=None,load\_best\_model\_at\_end:bool|None=False,metric\_for\_best\_model:str|None=None,greater\_is\_better:bool|None=None,ignore\_data\_skip:bool=False,fsdp:list[~transformers.trainer\_utils.FSDPOption]|str|None='',fsdp\_min\_num\_params:int=0,fsdp\_config:dict|str|None=None,tp\_size:int|None=0,fsdp\_transformer\_layer\_cls\_to\_wrap:str|None=None,accelerator\_config:dict|str|None=None,deepspeed:dict|str|None=None,label\_smoothing\_factor:float=0.0,optim:~transformers.training\_args.OptimizerNames|str='adamw\_torch',optim\_args:str|None=None,adafactor:bool=False,group\_by\_length:bool=False,length\_column\_name:str|None='length',report\_to:None|str|list[str]=None,ddp\_find\_unused\_parameters:bool|None=None,ddp\_bucket\_cap\_mb:int|None=None,ddp\_broadcast\_buffers:bool|None=None,dataloader\_pin\_memory:bool=True,dataloader\_persistent\_workers:bool=False,skip\_memory\_metrics:bool=True,use\_legacy\_prediction\_loop:bool=False,push\_to\_hub:bool=False,resume\_from\_checkpoint:str|None=None,hub\_model\_id:str|None=None,hub\_strategy:~transformers.trainer\_utils.HubStrategy|str='every\_save',hub\_token:str|None=None,hub\_private\_repo:bool|None=None,hub\_always\_push:bool=False,gradient\_checkpointing:bool=False,gradient\_checkpointing\_kwargs:dict|str|None=None,include\_inputs\_for\_metrics:bool=False,include\_for\_metrics:list[str]=<factory>,eval\_do\_concat\_batches:bool=True,fp16\_backend:str='auto',push\_to\_hub\_model\_id:str|None=None,push\_to\_hub\_organization:str|None=None,push\_to\_hub\_token:str|None=None,mp\_parameters:str='',auto\_find\_batch\_size:bool=False,full\_determinism:bool=False,torchdynamo:str|None=None,ray\_scope:str|None='last',ddp\_timeout:int|None=1800,torch\_compile:bool=False,torch\_compile\_backend:str|None=None,torch\_compile\_mode:str|None=None,include\_tokens\_per\_second:bool|None=False,include\_num\_input\_tokens\_seen:bool|None=False,neftune\_noise\_alpha:float|None=None,optim\_target\_modules:None|str|list[str]=None,batch\_eval\_metrics:bool=False,eval\_on\_start:bool=False,use\_liger\_kernel:bool|None=False,eval\_use\_gather\_object:bool|None=False,average\_tokens\_across\_devices:bool|None=False,prompts:Union[str,None,dict[str,str],dict[str,dict[str,str]]]=None,batch\_sampler:Union[BatchSamplers,str,DefaultBatchSampler,Callable[...,DefaultBatchSampler]]=BatchSamplers.BATCH\_SAMPLER,multi\_dataset\_batch\_sampler:Union[MultiDatasetBatchSamplers,str,MultiDatasetDefaultBatchSampler,Callable[...,MultiDatasetDefaultBatchSampler]]=MultiDatasetBatchSamplers.PROPORTIONAL,router\_mapping:Union[str,None,dict[str,str],dict[str,dict[str,str]]]=<factory>,learning\_rate\_mapping:Union[str,None,dict[str,float]]=<factory>_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/sparse_encoder/training_args.py#L8-L49)[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments "Link to this definition")
SparseEncoderTrainingArguments extends `SentenceTransformerTrainingArguments` which itself extend [`TrainingArguments`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments "(in transformers vmain)") with additional arguments specific to Sentence Transformers. See [`TrainingArguments`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments "(in transformers vmain)") for the complete list of available arguments.

Parameters:
*   **output_dir** (str) – The output directory where the model checkpoints will be written.

*   **prompts** (Union[Dict[str, Dict[str, str]], Dict[str, str], str], _optional_) –

The prompts to use for each column in the training, evaluation and test datasets. Four formats are accepted:

    1.   str: A single prompt to use for all columns in the datasets, regardless of whether the training/evaluation/test datasets are [`datasets.Dataset`](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)") or a [`datasets.DatasetDict`](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.DatasetDict "(in datasets vmain)").

    2.   Dict[str, str]: A dictionary mapping column names to prompts, regardless of whether the training/evaluation/test datasets are [`datasets.Dataset`](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)") or a [`datasets.DatasetDict`](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.DatasetDict "(in datasets vmain)").

    3.   Dict[str, str]: A dictionary mapping dataset names to prompts. This should only be used if your training/evaluation/test datasets are a [`datasets.DatasetDict`](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.DatasetDict "(in datasets vmain)") or a dictionary of [`datasets.Dataset`](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)").

    4.   Dict[str, Dict[str, str]]: A dictionary mapping dataset names to dictionaries mapping column names to prompts. This should only be used if your training/evaluation/test datasets are a [`datasets.DatasetDict`](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.DatasetDict "(in datasets vmain)") or a dictionary of [`datasets.Dataset`](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)").

*   **batch_sampler** (Union[[`BatchSamplers`](https://sbert.net/docs/package_reference/sentence_transformer/sampler.html#sentence_transformers.training_args.BatchSamplers "sentence_transformers.training_args.BatchSamplers"), str], _optional_) – The batch sampler to use. See [`BatchSamplers`](https://sbert.net/docs/package_reference/sentence_transformer/sampler.html#sentence_transformers.training_args.BatchSamplers "sentence_transformers.training_args.BatchSamplers") for valid options. Defaults to `BatchSamplers.BATCH_SAMPLER`.

*   **multi_dataset_batch_sampler** (Union[[`MultiDatasetBatchSamplers`](https://sbert.net/docs/package_reference/sentence_transformer/sampler.html#sentence_transformers.training_args.MultiDatasetBatchSamplers "sentence_transformers.training_args.MultiDatasetBatchSamplers"), str], _optional_) – The multi-dataset batch sampler to use. See [`MultiDatasetBatchSamplers`](https://sbert.net/docs/package_reference/sentence_transformer/sampler.html#sentence_transformers.training_args.MultiDatasetBatchSamplers "sentence_transformers.training_args.MultiDatasetBatchSamplers") for valid options. Defaults to `MultiDatasetBatchSamplers.PROPORTIONAL`.

*   **router_mapping** (Dict[str, str] | Dict[str, Dict[str, str]], _optional_) –

A mapping of dataset column names to Router routes, like “query” or “document”. This is used to specify which Router submodule to use for each dataset. Two formats are accepted:

    1.   Dict[str, str]: A mapping of column names to routes.

    2.   Dict[str, Dict[str, str]]: A mapping of dataset names to a mapping of column names to routes for multi-dataset training/evaluation.

*   **learning_rate_mapping** (Dict[str, float] | None, _optional_) – A mapping of parameter name regular expressions to learning rates. This allows you to set different learning rates for different parts of the model, e.g., {‘SparseStaticEmbedding.*’: 1e-3} for the SparseStaticEmbedding module. This is useful when you want to fine-tune specific parts of the model with different learning rates.

_property_ ddp_timeout_delta _:timedelta_[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.ddp_timeout_delta "Link to this definition")
The actual timeout for torch.distributed.init_process_group since it expects a timedelta variable.

_property_ device _:[device](https://docs.pytorch.org/docs/stable/tensor\_attributes.html#torch.device "(in PyTorch v2.10)")_[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.device "Link to this definition")
The device used by this process.

_property_ eval_batch_size _:int_[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.eval_batch_size "Link to this definition")
The actual batch size for evaluation (may differ from per_gpu_eval_batch_size in distributed training).

get_process_log_level()[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.get_process_log_level "Link to this definition")
Returns the log level to be used depending on whether this process is the main process of node 0, main process of node non-0, or a non-main process.

For the main process the log level defaults to the logging level set (logging.WARNING if you didn’t do anything) unless overridden by log_level argument.

For the replica processes the log level defaults to logging.WARNING unless overridden by log_level_replica argument.

The choice between the main and replica process settings is made according to the return value of should_log.

get_warmup_steps(_num\_training\_steps:int_)[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.get_warmup_steps "Link to this definition")
Get number of steps used for a linear warmup.

_property_ local_process_index[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.local_process_index "Link to this definition")
The index of the local process used.

main_process_first(_local=True_, _desc='work'_)[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.main_process_first "Link to this definition")
A context manager for torch distributed environment where on needs to do something on the main process, while blocking replicas, and when it’s finished releasing the replicas.

One such use is for datasets’s map feature which to be efficient should be run once on the main process, which upon completion saves a cached version of results and which then automatically gets loaded by the replicas.

Parameters:
*   **local** (bool, _optional_, defaults to True) – if True first means process of rank 0 of each node if False first means process of rank 0 of node rank 0 In multi-node environment with a shared filesystem you most likely will want to use local=False so that only the main process of the first node will do the processing. If however, the filesystem is not shared, then the main process of each node will need to do the processing, which is the default behavior.

*   **desc** (str, _optional_, defaults to “work”) – a work description to be used in debug logs

_property_ n_gpu[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.n_gpu "Link to this definition")
The number of GPUs used by this process.

Note

This will only be greater than one when you have multiple GPUs available but are not using distributed training. For distributed training, it will always be 1.

_property_ parallel_mode[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.parallel_mode "Link to this definition")
The current mode used for parallelism if multiple GPUs/TPU cores are available. One of:

*   ParallelMode.NOT_PARALLEL: no parallelism (CPU or one GPU).

*   ParallelMode.NOT_DISTRIBUTED: several GPUs in one single process (uses torch.nn.DataParallel).

*   ParallelMode.DISTRIBUTED: several GPUs, each having its own process (uses torch.nn.DistributedDataParallel).

*   ParallelMode.TPU: several TPU cores.

_property_ place_model_on_device[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.place_model_on_device "Link to this definition")
Can be subclassed and overridden for some specific integrations.

_property_ process_index[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.process_index "Link to this definition")
The index of the current process used.

set_dataloader(_train\_batch\_size:int=8_, _eval\_batch\_size:int=8_, _drop\_last:bool=False_, _num\_workers:int=0_, _pin\_memory:bool=True_, _persistent\_workers:bool=False_, _prefetch\_factor:int|None=None_, _auto\_find\_batch\_size:bool=False_, _ignore\_data\_skip:bool=False_, _sampler\_seed:int|None=None_)[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.set_dataloader "Link to this definition")
A method that regroups all arguments linked to the dataloaders creation.

Parameters:
*   **drop_last** (bool, _optional_, defaults to False) – Whether to drop the last incomplete batch (if the length of the dataset is not divisible by the batch size) or not.

*   **num_workers** (int, _optional_, defaults to 0) – Number of subprocesses to use for data loading (PyTorch only). 0 means that the data will be loaded in the main process.

*   **pin_memory** (bool, _optional_, defaults to True) – Whether you want to pin memory in data loaders or not. Will default to True.

*   **persistent_workers** (bool, _optional_, defaults to False) – If True, the data loader will not shut down the worker processes after a dataset has been consumed once. This allows to maintain the workers Dataset instances alive. Can potentially speed up training, but will increase RAM usage. Will default to False.

*   **prefetch_factor** (int, _optional_) – Number of batches loaded in advance by each worker. 2 means there will be a total of 2 * num_workers batches prefetched across all workers.

*   **auto_find_batch_size** (bool, _optional_, defaults to False) – Whether to find a batch size that will fit into memory automatically through exponential decay, avoiding CUDA Out-of-Memory errors. Requires accelerate to be installed (pip install accelerate)

*   **ignore_data_skip** (bool, _optional_, defaults to False) – When resuming training, whether or not to skip the epochs and batches to get the data loading at the same stage as in the previous training. If set to True, the training will begin faster (as that skipping step can take a long time) but will not yield the same results as the interrupted training would have.

*   **sampler_seed** (int, _optional_) – Random seed to be used with data samplers. If not set, random generators for data sampling will use the same seed as self.seed. This can be used to ensure reproducibility of data sampling, independent of the model seed.

Example:

[``](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#id1)[`](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#id3)py >>> from transformers import TrainingArguments

>>> args = TrainingArguments("working_dir")
>>> args = args.set_dataloader(train_batch_size=16, eval_batch_size=64)
>>> args.per_device_train_batch_size
16
```

set_evaluate(_strategy:str|IntervalStrategy='no'_, _steps:int=500_, _batch\_size:int=8_, _accumulation\_steps:int|None=None_, _delay:float|None=None_, _loss\_only:bool=False_, _jit\_mode:bool=False_)[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.set_evaluate "Link to this definition")
A method that regroups all arguments linked to evaluation.

Parameters:
*   **strategy** (str or [~trainer_utils.IntervalStrategy], _optional_, defaults to “no”) –

The evaluation strategy to adopt during training. Possible values are:

> *   ”no”: No evaluation is done during training.
> 
>     *   ”steps”: Evaluation is done (and logged) every steps.
> 
>     *   ”epoch”: Evaluation is done at the end of each epoch.

Setting a strategy different from “no” will set self.do_eval to True.

*   **steps** (int, _optional_, defaults to 500) – Number of update steps between two evaluations if strategy=”steps”.

*   **batch_size** (int _optional_, defaults to 8) – The batch size per device (GPU/TPU core/CPU…) used for evaluation.

*   **accumulation_steps** (int, _optional_) – Number of predictions steps to accumulate the output tensors for, before moving the results to the CPU. If left unset, the whole predictions are accumulated on GPU/TPU before being moved to the CPU (faster but requires more memory).

*   **delay** (float, _optional_) – Number of epochs or steps to wait for before the first evaluation can be performed, depending on the eval_strategy.

*   **loss_only** (bool, _optional_, defaults to False) – Ignores all outputs except the loss.

*   **jit_mode** (bool, _optional_) – Whether or not to use PyTorch jit trace for inference.

Example:

[``](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#id5)[`](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#id7)py >>> from transformers import TrainingArguments

>>> args = TrainingArguments("working_dir")
>>> args = args.set_evaluate(strategy="steps", steps=100)
>>> args.eval_steps
100
```

set_logging(_strategy:str|IntervalStrategy='steps'_, _steps:int=500_, _report\_to:str|list[str]='none'_, _level:str='passive'_, _first\_step:bool=False_, _nan\_inf\_filter:bool=False_, _on\_each\_node:bool=False_, _replica\_level:str='passive'_)[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.set_logging "Link to this definition")
A method that regroups all arguments linked to logging.

Parameters:
*   **strategy** (str or [~trainer_utils.IntervalStrategy], _optional_, defaults to “steps”) –

The logging strategy to adopt during training. Possible values are:

> *   ”no”: No logging is done during training.
> 
>     *   ”epoch”: Logging is done at the end of each epoch.
> 
>     *   ”steps”: Logging is done every logging_steps.

*   **steps** (int, _optional_, defaults to 500) – Number of update steps between two logs if strategy=”steps”.

*   **level** (str, _optional_, defaults to “passive”) – Logger log level to use on the main process. Possible choices are the log levels as strings: “debug”, “info”, “warning”, “error” and “critical”, plus a “passive” level which doesn’t set anything and lets the application set the level.

*   **report_to** (str or List[str], _optional_, defaults to “all”) – The list of integrations to report the results and logs to. Supported platforms are “azure_ml”, “clearml”, “codecarbon”, “comet_ml”, “dagshub”, “dvclive”, “flyte”, “mlflow”, “neptune”, “swanlab”, “tensorboard”, and “wandb”. Use “all” to report to all integrations installed, “none” for no integrations.

*   **first_step** (bool, _optional_, defaults to False) – Whether to log and evaluate the first global_step or not.

*   **nan_inf_filter** (bool, _optional_, defaults to True) –

Whether to filter nan and inf losses for logging. If set to True the loss of every step that is nan or inf is filtered and the average loss of the current logging window is taken instead.

<Tip>

nan_inf_filter only influences the logging of loss values, it does not change the behavior the gradient is computed or applied to the model.

</Tip>

*   **on_each_node** (bool, _optional_, defaults to True) – In multinode distributed training, whether to log using log_level once per node, or only on the main node.

*   **replica_level** (str, _optional_, defaults to “passive”) – Logger log level to use on replicas. Same choices as log_level

Example:

[``](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#id9)[`](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#id11)py >>> from transformers import TrainingArguments

>>> args = TrainingArguments("working_dir")
>>> args = args.set_logging(strategy="steps", steps=100)
>>> args.logging_steps
100
```

set_lr_scheduler(_name:str|SchedulerType='linear'_, _num\_epochs:float=3.0_, _max\_steps:int=-1_, _warmup\_ratio:float=0_, _warmup\_steps:int=0_)[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.set_lr_scheduler "Link to this definition")
A method that regroups all arguments linked to the learning rate scheduler and its hyperparameters.

Parameters:
*   **name** (str or [SchedulerType], _optional_, defaults to “linear”) – The scheduler type to use. See the documentation of [SchedulerType] for all possible values.

*   **num_epochs** (float, _optional_, defaults to 3.0) – Total number of training epochs to perform (if not an integer, will perform the decimal part percents of the last epoch before stopping training).

*   **max_steps** (int, _optional_, defaults to -1) – If set to a positive number, the total number of training steps to perform. Overrides num_train_epochs. For a finite dataset, training is reiterated through the dataset (if all data is exhausted) until max_steps is reached.

*   **warmup_ratio** (float, _optional_, defaults to 0.0) – Ratio of total training steps used for a linear warmup from 0 to learning_rate.

*   **warmup_steps** (int, _optional_, defaults to 0) – Number of steps used for a linear warmup from 0 to learning_rate. Overrides any effect of warmup_ratio.

Example:

[``](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#id13)[`](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#id15)py >>> from transformers import TrainingArguments

>>> args = TrainingArguments("working_dir")
>>> args = args.set_lr_scheduler(name="cosine", warmup_ratio=0.05)
>>> args.warmup_ratio
0.05
```

set_optimizer(_name:str|OptimizerNames='adamw\_torch'_, _learning\_rate:float=5e-05_, _weight\_decay:float=0_, _beta1:float=0.9_, _beta2:float=0.999_, _epsilon:float=1e-08_, _args:str|None=None_)[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.set_optimizer "Link to this definition")
A method that regroups all arguments linked to the optimizer and its hyperparameters.

Parameters:
*   **name** (str or [training_args.OptimizerNames], _optional_, defaults to “adamw_torch”) – The optimizer to use: “adamw_torch”, “adamw_torch_fused”, “adamw_apex_fused”, “adamw_anyprecision” or “adafactor”.

*   **learning_rate** (float, _optional_, defaults to 5e-5) – The initial learning rate.

*   **weight_decay** (float, _optional_, defaults to 0) – The weight decay to apply (if not zero) to all layers except all bias and LayerNorm weights.

*   **beta1** (float, _optional_, defaults to 0.9) – The beta1 hyperparameter for the adam optimizer or its variants.

*   **beta2** (float, _optional_, defaults to 0.999) – The beta2 hyperparameter for the adam optimizer or its variants.

*   **epsilon** (float, _optional_, defaults to 1e-8) – The epsilon hyperparameter for the adam optimizer or its variants.

*   **args** (str, _optional_) – Optional arguments that are supplied to AnyPrecisionAdamW (only useful when optim=”adamw_anyprecision”).

Example:

[``](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#id17)[`](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#id19)py >>> from transformers import TrainingArguments

>>> args = TrainingArguments("working_dir")
>>> args = args.set_optimizer(name="adamw_torch", beta1=0.8)
>>> args.optim
'adamw_torch'
```

set_push_to_hub(_model\_id:str_, _strategy:str|HubStrategy='every\_save'_, _token:str|None=None_, _private\_repo:bool|None=None_, _always\_push:bool=False_)[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.set_push_to_hub "Link to this definition")
A method that regroups all arguments linked to synchronizing checkpoints with the Hub.

<Tip>

Calling this method will set self.push_to_hub to True, which means the output_dir will begin a git directory synced with the repo (determined by model_id) and the content will be pushed each time a save is triggered (depending on your self.save_strategy). Calling [~Trainer.save_model] will also trigger a push.

</Tip>

Parameters:
*   **model_id** (str) – The name of the repository to keep in sync with the local _output\_dir_. It can be a simple model ID in which case the model will be pushed in your namespace. Otherwise it should be the whole repository name, for instance “user_name/model”, which allows you to push to an organization you are a member of with “organization_name/model”.

*   **strategy** (str or [~trainer_utils.HubStrategy], _optional_, defaults to “every_save”) –

Defines the scope of what is pushed to the Hub and when. Possible values are:

    *   ”end”: push the model, its configuration, the processing_class e.g. tokenizer (if passed along to the [Trainer]) and a

draft of a model card when the [~Trainer.save_model] method is called. - “every_save”: push the model, its configuration, the processing_class e.g. tokenizer (if passed along to the [Trainer])

> and

a draft of a model card each time there is a model save. The pushes are asynchronous to not block training, and in case the save are very frequent, a new push is only attempted if the previous one is finished. A last push is made with the final model at the end of training. - “checkpoint”: like “every_save” but the latest checkpoint is also pushed in a subfolder named last-checkpoint, allowing you to resume training easily with trainer.train(resume_from_checkpoint=”last-checkpoint”). - “all_checkpoints”: like “checkpoint” but all checkpoints are pushed like they appear in the

> output

folder (so you will get one checkpoint folder per folder in your final repository)

*   **token** (str, _optional_) – The token to use to push the model to the Hub. Will default to the token in the cache folder obtained with huggingface-cli login.

*   **private_repo** (bool, _optional_, defaults to False) – Whether to make the repo private. If None (default), the repo will be public unless the organization’s default is private. This value is ignored if the repo already exists.

*   **always_push** (bool, _optional_, defaults to False) – Unless this is True, the Trainer will skip pushing a checkpoint when the previous push is not finished.

Example:

[``](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#id21)[`](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#id23)py >>> from transformers import TrainingArguments

>>> args = TrainingArguments("working_dir")
>>> args = args.set_push_to_hub("me/awesome-model")
>>> args.hub_model_id
'me/awesome-model'
```

set_save(_strategy:str|IntervalStrategy='steps'_, _steps:int=500_, _total\_limit:int|None=None_, _on\_each\_node:bool=False_)[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.set_save "Link to this definition")
A method that regroups all arguments linked to checkpoint saving.

Parameters:
*   **strategy** (str or [~trainer_utils.IntervalStrategy], _optional_, defaults to “steps”) –

The checkpoint save strategy to adopt during training. Possible values are:

> *   ”no”: No save is done during training.
> 
>     *   ”epoch”: Save is done at the end of each epoch.
> 
>     *   ”steps”: Save is done every save_steps.

*   **steps** (int, _optional_, defaults to 500) – Number of updates steps before two checkpoint saves if strategy=”steps”.

*   **total_limit** (int, _optional_) – If a value is passed, will limit the total amount of checkpoints. Deletes the older checkpoints in output_dir.

*   **on_each_node** (bool, _optional_, defaults to False) –

When doing multi-node distributed training, whether to save models and checkpoints on each node, or only on the main one.

This should not be activated when the different nodes use the same storage as the files will be saved with the same names for each node.

Example:

[``](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#id25)[`](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#id27)py >>> from transformers import TrainingArguments

>>> args = TrainingArguments("working_dir")
>>> args = args.set_save(strategy="steps", steps=100)
>>> args.save_steps
100
```

set_testing(_batch\_size:int=8_, _loss\_only:bool=False_, _jit\_mode:bool=False_)[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.set_testing "Link to this definition")
A method that regroups all basic arguments linked to testing on a held-out dataset.

<Tip>

Calling this method will automatically set self.do_predict to True.

</Tip>

Parameters:
*   **batch_size** (int _optional_, defaults to 8) – The batch size per device (GPU/TPU core/CPU…) used for testing.

*   **loss_only** (bool, _optional_, defaults to False) – Ignores all outputs except the loss.

*   **jit_mode** (bool, _optional_) – Whether or not to use PyTorch jit trace for inference.

Example:

[``](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#id29)[`](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#id31)py >>> from transformers import TrainingArguments

>>> args = TrainingArguments("working_dir")
>>> args = args.set_testing(batch_size=32)
>>> args.per_device_eval_batch_size
32
```

set_training(_learning\_rate:float=5e-05_, _batch\_size:int=8_, _weight\_decay:float=0_, _num\_epochs:float=3_, _max\_steps:int=-1_, _gradient\_accumulation\_steps:int=1_, _seed:int=42_, _gradient\_checkpointing:bool=False_)[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.set_training "Link to this definition")
A method that regroups all basic arguments linked to the training.

<Tip>

Calling this method will automatically set self.do_train to True.

</Tip>

Parameters:
*   **learning_rate** (float, _optional_, defaults to 5e-5) – The initial learning rate for the optimizer.

*   **batch_size** (int _optional_, defaults to 8) – The batch size per device (GPU/TPU core/CPU…) used for training.

*   **weight_decay** (float, _optional_, defaults to 0) – The weight decay to apply (if not zero) to all layers except all bias and LayerNorm weights in the optimizer.

*   **num_train_epochs** (float, _optional_, defaults to 3.0) – Total number of training epochs to perform (if not an integer, will perform the decimal part percents of the last epoch before stopping training).

*   **max_steps** (int, _optional_, defaults to -1) – If set to a positive number, the total number of training steps to perform. Overrides num_train_epochs. For a finite dataset, training is reiterated through the dataset (if all data is exhausted) until max_steps is reached.

*   **gradient_accumulation_steps** (int, _optional_, defaults to 1) –

Number of updates steps to accumulate the gradients for, before performing a backward/update pass.

<Tip warning={true}>

When using gradient accumulation, one step is counted as one step with backward pass. Therefore, logging, evaluation, save will be conducted every gradient_accumulation_steps * xxx_step training examples.

</Tip>

*   **seed** (int, _optional_, defaults to 42) – Random seed that will be set at the beginning of training. To ensure reproducibility across runs, use the [~Trainer.model_init] function to instantiate the model if it has some randomly initialized parameters.

*   **gradient_checkpointing** (bool, _optional_, defaults to False) – If True, use gradient checkpointing to save memory at the expense of slower backward pass.

Example:

[``](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#id33)[`](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#id35)py >>> from transformers import TrainingArguments

>>> args = TrainingArguments("working_dir")
>>> args = args.set_training(learning_rate=1e-4, batch_size=32)
>>> args.learning_rate
1e-4
```

_property_ should_log[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.should_log "Link to this definition")
Whether or not the current process should produce log.

_property_ should_save[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.should_save "Link to this definition")
Whether or not the current process should write to disk, e.g., to save models and checkpoints.

to_dict()[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/training_args.py#L304-L310)[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.to_dict "Link to this definition")
Serializes this instance while replace Enum by their values (for JSON serialization support). It obfuscates the token values by removing their value.

to_json_string()[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.to_json_string "Link to this definition")
Serializes this instance to a JSON string.

to_sanitized_dict()→dict[str,Any][](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.to_sanitized_dict "Link to this definition")
Sanitized serialization to use with TensorBoard’s hparams

_property_ train_batch_size _:int_[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.train_batch_size "Link to this definition")
The actual batch size for training (may differ from per_gpu_train_batch_size in distributed training).

_property_ world_size[](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments.world_size "Link to this definition")
The number of processes used in parallel.
