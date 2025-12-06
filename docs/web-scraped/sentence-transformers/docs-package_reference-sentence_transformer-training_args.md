# Source: https://www.sbert.net/docs/package_reference/sentence_transformer/training_args.html

# Training Arguments[ïƒ?](#training-arguments "Link to this heading")

## SentenceTransformerTrainingArguments[ïƒ?](#sentencetransformertrainingarguments "Link to this heading")

*[class][ ]*[[sentence_transformers.training_args.]][[SentenceTransformerTrainingArguments]][(]*[output_dir:] [str] [\|] [None] [=] [None,] [overwrite_output_dir:] [bool] [=] [False,] [do_train:] [bool] [=] [False,] [do_eval:] [bool] [=] [False,] [do_predict:] [bool] [=] [False,] [eval_strategy:] [\~transformers.trainer_utils.IntervalStrategy] [\|] [str] [=] [\'no\',] [prediction_loss_only:] [bool] [=] [False,] [per_device_train_batch_size:] [int] [=] [8,] [per_device_eval_batch_size:] [int] [=] [8,] [per_gpu_train_batch_size:] [int] [\|] [None] [=] [None,] [per_gpu_eval_batch_size:] [int] [\|] [None] [=] [None,] [gradient_accumulation_steps:] [int] [=] [1,] [eval_accumulation_steps:] [int] [\|] [None] [=] [None,] [eval_delay:] [float] [\|] [None] [=] [0,] [torch_empty_cache_steps:] [int] [\|] [None] [=] [None,] [learning_rate:] [float] [=] [5e-05,] [weight_decay:] [float] [=] [0.0,] [adam_beta1:] [float] [=] [0.9,] [adam_beta2:] [float] [=] [0.999,] [adam_epsilon:] [float] [=] [1e-08,] [max_grad_norm:] [float] [=] [1.0,] [num_train_epochs:] [float] [=] [3.0,] [max_steps:] [int] [=] [-1,] [lr_scheduler_type:] [\~transformers.trainer_utils.SchedulerType] [\|] [str] [=] [\'linear\',] [lr_scheduler_kwargs:] [dict] [\|] [str] [\|] [None] [=] [\<factory\>,] [warmup_ratio:] [float] [=] [0.0,] [warmup_steps:] [int] [=] [0,] [log_level:] [str] [\|] [None] [=] [\'passive\',] [log_level_replica:] [str] [\|] [None] [=] [\'warning\',] [log_on_each_node:] [bool] [=] [True,] [logging_dir:] [str] [\|] [None] [=] [None,] [logging_strategy:] [\~transformers.trainer_utils.IntervalStrategy] [\|] [str] [=] [\'steps\',] [logging_first_step:] [bool] [=] [False,] [logging_steps:] [float] [=] [500,] [logging_nan_inf_filter:] [bool] [=] [True,] [save_strategy:] [\~transformers.trainer_utils.SaveStrategy] [\|] [str] [=] [\'steps\',] [save_steps:] [float] [=] [500,] [save_total_limit:] [int] [\|] [None] [=] [None,] [save_safetensors:] [bool] [\|] [None] [=] [True,] [save_on_each_node:] [bool] [=] [False,] [save_only_model:] [bool] [=] [False,] [restore_callback_states_from_checkpoint:] [bool] [=] [False,] [no_cuda:] [bool] [=] [False,] [use_cpu:] [bool] [=] [False,] [use_mps_device:] [bool] [=] [False,] [seed:] [int] [=] [42,] [data_seed:] [int] [\|] [None] [=] [None,] [jit_mode_eval:] [bool] [=] [False,] [use_ipex:] [bool] [=] [False,] [bf16:] [bool] [=] [False,] [fp16:] [bool] [=] [False,] [fp16_opt_level:] [str] [=] [\'O1\',] [half_precision_backend:] [str] [=] [\'auto\',] [bf16_full_eval:] [bool] [=] [False,] [fp16_full_eval:] [bool] [=] [False,] [tf32:] [bool] [\|] [None] [=] [None,] [local_rank:] [int] [=] [-1,] [ddp_backend:] [str] [\|] [None] [=] [None,] [tpu_num_cores:] [int] [\|] [None] [=] [None,] [tpu_metrics_debug:] [bool] [=] [False,] [debug:] [str] [\|] [list\[\~transformers.debug_utils.DebugOption\]] [=] [\'\',] [dataloader_drop_last:] [bool] [=] [False,] [eval_steps:] [float] [\|] [None] [=] [None,] [dataloader_num_workers:] [int] [=] [0,] [dataloader_prefetch_factor:] [int] [\|] [None] [=] [None,] [past_index:] [int] [=] [-1,] [run_name:] [str] [\|] [None] [=] [None,] [disable_tqdm:] [bool] [\|] [None] [=] [None,] [remove_unused_columns:] [bool] [\|] [None] [=] [True,] [label_names:] [list\[str\]] [\|] [None] [=] [None,] [load_best_model_at_end:] [bool] [\|] [None] [=] [False,] [metric_for_best_model:] [str] [\|] [None] [=] [None,] [greater_is_better:] [bool] [\|] [None] [=] [None,] [ignore_data_skip:] [bool] [=] [False,] [fsdp:] [list\[\~transformers.trainer_utils.FSDPOption\]] [\|] [str] [\|] [None] [=] [\'\',] [fsdp_min_num_params:] [int] [=] [0,] [fsdp_config:] [dict] [\|] [str] [\|] [None] [=] [None,] [tp_size:] [int] [\|] [None] [=] [0,] [fsdp_transformer_layer_cls_to_wrap:] [str] [\|] [None] [=] [None,] [accelerator_config:] [dict] [\|] [str] [\|] [None] [=] [None,] [deepspeed:] [dict] [\|] [str] [\|] [None] [=] [None,] [label_smoothing_factor:] [float] [=] [0.0,] [optim:] [\~transformers.training_args.OptimizerNames] [\|] [str] [=] [\'adamw_torch\',] [optim_args:] [str] [\|] [None] [=] [None,] [adafactor:] [bool] [=] [False,] [group_by_length:] [bool] [=] [False,] [length_column_name:] [str] [\|] [None] [=] [\'length\',] [report_to:] [str] [\|] [list\[str\]] [\|] [None] [=] [None,] [ddp_find_unused_parameters:] [bool] [\|] [None] [=] [None,] [ddp_bucket_cap_mb:] [int] [\|] [None] [=] [None,] [ddp_broadcast_buffers:] [bool] [\|] [None] [=] [None,] [dataloader_pin_memory:] [bool] [=] [True,] [dataloader_persistent_workers:] [bool] [=] [False,] [skip_memory_metrics:] [bool] [=] [True,] [use_legacy_prediction_loop:] [bool] [=] [False,] [push_to_hub:] [bool] [=] [False,] [resume_from_checkpoint:] [str] [\|] [None] [=] [None,] [hub_model_id:] [str] [\|] [None] [=] [None,] [hub_strategy:] [\~transformers.trainer_utils.HubStrategy] [\|] [str] [=] [\'every_save\',] [hub_token:] [str] [\|] [None] [=] [None,] [hub_private_repo:] [bool] [\|] [None] [=] [None,] [hub_always_push:] [bool] [=] [False,] [gradient_checkpointing:] [bool] [=] [False,] [gradient_checkpointing_kwargs:] [dict] [\|] [str] [\|] [None] [=] [None,] [include_inputs_for_metrics:] [bool] [=] [False,] [include_for_metrics:] [list\[str\]] [=] [\<factory\>,] [eval_do_concat_batches:] [bool] [=] [True,] [fp16_backend:] [str] [=] [\'auto\',] [push_to_hub_model_id:] [str] [\|] [None] [=] [None,] [push_to_hub_organization:] [str] [\|] [None] [=] [None,] [push_to_hub_token:] [str] [\|] [None] [=] [None,] [mp_parameters:] [str] [=] [\'\',] [auto_find_batch_size:] [bool] [=] [False,] [full_determinism:] [bool] [=] [False,] [torchdynamo:] [str] [\|] [None] [=] [None,] [ray_scope:] [str] [\|] [None] [=] [\'last\',] [ddp_timeout:] [int] [\|] [None] [=] [1800,] [torch_compile:] [bool] [=] [False,] [torch_compile_backend:] [str] [\|] [None] [=] [None,] [torch_compile_mode:] [str] [\|] [None] [=] [None,] [include_tokens_per_second:] [bool] [\|] [None] [=] [False,] [include_num_input_tokens_seen:] [bool] [\|] [None] [=] [False,] [neftune_noise_alpha:] [float] [\|] [None] [=] [None,] [optim_target_modules:] [str] [\|] [list\[str\]] [\|] [None] [=] [None,] [batch_eval_metrics:] [bool] [=] [False,] [eval_on_start:] [bool] [=] [False,] [use_liger_kernel:] [bool] [\|] [None] [=] [False,] [eval_use_gather_object:] [bool] [\|] [None] [=] [False,] [average_tokens_across_devices:] [bool] [\|] [None] [=] [False,] [prompts:] [dict\[str,] [dict\[str,] [str\]\]] [\|] [dict\[str,] [str\]] [\|] [str] [\|] [None] [=] [None,] [batch_sampler:] [\~sentence_transformers.training_args.BatchSamplers] [\|] [str] [\|] [\~sentence_transformers.sampler.DefaultBatchSampler] [\|] [\~collections.abc.Callable\[\[\...\],] [\~sentence_transformers.sampler.DefaultBatchSampler\]] [=] [BatchSamplers.BATCH_SAMPLER,] [multi_dataset_batch_sampler:] [\~sentence_transformers.training_args.MultiDatasetBatchSamplers] [\|] [str] [\|] [\~sentence_transformers.sampler.MultiDatasetDefaultBatchSampler] [\|] [\~collections.abc.Callable\[\[\...\],] [\~sentence_transformers.sampler.MultiDatasetDefaultBatchSampler\]] [=] [MultiDatasetBatchSamplers.PROPORTIONAL,] [router_mapping:] [str] [\|] [None] [\|] [dict\[str,] [str\]] [\|] [dict\[str,] [dict\[str,] [str\]\]] [=] [\<factory\>,] [learning_rate_mapping:] [str] [\|] [None] [\|] [dict\[str,] [float\]] [=] [\<factory\>]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\training_args.py#L156-L310)[ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments "Link to this definition")

:   SentenceTransformerTrainingArguments extends [[`TrainingArguments`]](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments "(in transformers vmain)") with additional arguments specific to Sentence Transformers. See [[`TrainingArguments`]](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments "(in transformers vmain)") for the complete list of available arguments.

    Parameters[:]

    :   - **output_dir** (str) â€" The output directory where the model checkpoints will be written.

        - **prompts** (Union\[Dict\[str, Dict\[str, str\]\], Dict\[str, str\], str\], *optional*) â€"

          The prompts to use for each column in the training, evaluation and test datasets. Four formats are accepted:

          1.  str: A single prompt to use for all columns in the datasets, regardless of whether the training/evaluation/test datasets are [[`datasets.Dataset`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)") or a [[`datasets.DatasetDict`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.DatasetDict "(in datasets vmain)").

          2.  Dict\[str, str\]: A dictionary mapping column names to prompts, regardless of whether the training/evaluation/test datasets are [[`datasets.Dataset`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)") or a [[`datasets.DatasetDict`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.DatasetDict "(in datasets vmain)").

          3.  Dict\[str, str\]: A dictionary mapping dataset names to prompts. This should only be used if your training/evaluation/test datasets are a [[`datasets.DatasetDict`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.DatasetDict "(in datasets vmain)") or a dictionary of [[`datasets.Dataset`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)").

          4.  Dict\[str, Dict\[str, str\]\]: A dictionary mapping dataset names to dictionaries mapping column names to prompts. This should only be used if your training/evaluation/test datasets are a [[`datasets.DatasetDict`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.DatasetDict "(in datasets vmain)") or a dictionary of [[`datasets.Dataset`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)").

        - **batch_sampler** (Union\[[[`BatchSamplers`]](sampler.html#sentence_transformers.training_args.BatchSamplers "sentence_transformers.training_args.BatchSamplers"), str, [[`DefaultBatchSampler`]](sampler.html#sentence_transformers.sampler.DefaultBatchSampler "sentence_transformers.sampler.DefaultBatchSampler"), Callable\[\[â€¦\], [[`DefaultBatchSampler`]](sampler.html#sentence_transformers.sampler.DefaultBatchSampler "sentence_transformers.sampler.DefaultBatchSampler")\]\], *optional*) â€" The batch sampler to use. See [[`BatchSamplers`]](sampler.html#sentence_transformers.training_args.BatchSamplers "sentence_transformers.training_args.BatchSamplers") for valid options. Defaults to [`BatchSamplers.BATCH_SAMPLER`].

        - **multi_dataset_batch_sampler** (Union\[[[`MultiDatasetBatchSamplers`]](sampler.html#sentence_transformers.training_args.MultiDatasetBatchSamplers "sentence_transformers.training_args.MultiDatasetBatchSamplers"), str, [[`MultiDatasetDefaultBatchSampler`]](sampler.html#sentence_transformers.sampler.MultiDatasetDefaultBatchSampler "sentence_transformers.sampler.MultiDatasetDefaultBatchSampler"), Callable\[\[â€¦\], [[`MultiDatasetDefaultBatchSampler`]](sampler.html#sentence_transformers.sampler.MultiDatasetDefaultBatchSampler "sentence_transformers.sampler.MultiDatasetDefaultBatchSampler")\]\], *optional*) â€" The multi-dataset batch sampler to use. See [[`MultiDatasetBatchSamplers`]](sampler.html#sentence_transformers.training_args.MultiDatasetBatchSamplers "sentence_transformers.training_args.MultiDatasetBatchSamplers") for valid options. Defaults to [`MultiDatasetBatchSamplers.PROPORTIONAL`].

        - **router_mapping** (Dict\[str, str\] \| Dict\[str, Dict\[str, str\]\], *optional*) â€"

          A mapping of dataset column names to Router routes, like â€œqueryâ€? or â€œdocumentâ€?. This is used to specify which Router submodule to use for each dataset. Two formats are accepted:

          1.  Dict\[str, str\]: A mapping of column names to routes.

          2.  Dict\[str, Dict\[str, str\]\]: A mapping of dataset names to a mapping of column names to routes for multi-dataset training/evaluation.

        - **learning_rate_mapping** (Dict\[str, float\] \| None, *optional*) â€" A mapping of parameter name regular expressions to learning rates. This allows you to set different learning rates for different parts of the model, e.g.,  for the SparseStaticEmbedding module. This is useful when you want to fine-tune specific parts of the model with different learning rates.

    *[property][ ]*[[ddp_timeout_delta]]*[[:]][ ][timedelta]*[ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.ddp_timeout_delta "Link to this definition")

    :   The actual timeout for torch.distributed.init_process_group since it expects a timedelta variable.

    *[property][ ]*[[device]]*[[:]][ ][[device]](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "(in PyTorch v2.9)")*[ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.device "Link to this definition")

    :   The device used by this process.

    *[property][ ]*[[eval_batch_size]]*[[:]][ ][int]*[ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.eval_batch_size "Link to this definition")

    :   The actual batch size for evaluation (may differ from per_gpu_eval_batch_size in distributed training).

    [[get_process_log_level]][(][)][ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.get_process_log_level "Link to this definition")

    :   Returns the log level to be used depending on whether this process is the main process of node 0, main process of node non-0, or a non-main process.

        For the main process the log level defaults to the logging level set (logging.WARNING if you didnâ€™t do anything) unless overridden by log_level argument.

        For the replica processes the log level defaults to logging.WARNING unless overridden by log_level_replica argument.

        The choice between the main and replica process settings is made according to the return value of should_log.

    [[get_warmup_steps]][(]*[[num_training_steps]][[:]][ ][[int]]*[)][ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.get_warmup_steps "Link to this definition")

    :   Get number of steps used for a linear warmup.

    *[property][ ]*[[local_process_index]][ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.local_process_index "Link to this definition")

    :   The index of the local process used.

    [[main_process_first]][(]*[[local]][[=]][[True]]*, *[[desc]][[=]][[\'work\']]*[)][ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.main_process_first "Link to this definition")

    :   A context manager for torch distributed environment where on needs to do something on the main process, while blocking replicas, and when itâ€™s finished releasing the replicas.

        One such use is for datasetsâ€™s map feature which to be efficient should be run once on the main process, which upon completion saves a cached version of results and which then automatically gets loaded by the replicas.

        Parameters[:]

        :   - **local** (bool, *optional*, defaults to True) â€" if True first means process of rank 0 of each node if False first means process of rank 0 of node rank 0 In multi-node environment with a shared filesystem you most likely will want to use local=False so that only the main process of the first node will do the processing. If however, the filesystem is not shared, then the main process of each node will need to do the processing, which is the default behavior.

            - **desc** (str, *optional*, defaults to â€œworkâ€?) â€" a work description to be used in debug logs

    *[property][ ]*[[n_gpu]][ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.n_gpu "Link to this definition")

    :   The number of GPUs used by this process.

        ::: 
        Note

        This will only be greater than one when you have multiple GPUs available but are not using distributed training. For distributed training, it will always be 1.
        :::

    *[property][ ]*[[parallel_mode]][ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.parallel_mode "Link to this definition")

    :   The current mode used for parallelism if multiple GPUs/TPU cores are available. One of:

        - ParallelMode.NOT_PARALLEL: no parallelism (CPU or one GPU).

        - ParallelMode.NOT_DISTRIBUTED: several GPUs in one single process (uses torch.nn.DataParallel).

        - ParallelMode.DISTRIBUTED: several GPUs, each having its own process (uses torch.nn.DistributedDataParallel).

        - ParallelMode.TPU: several TPU cores.

    *[property][ ]*[[place_model_on_device]][ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.place_model_on_device "Link to this definition")

    :   Can be subclassed and overridden for some specific integrations.

    *[property][ ]*[[process_index]][ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.process_index "Link to this definition")

    :   The index of the current process used.

    [[set_dataloader]][(]*[[train_batch_size]][[:]][ ][[int]][ ][[=]][ ][[8]]*, *[[eval_batch_size]][[:]][ ][[int]][ ][[=]][ ][[8]]*, *[[drop_last]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[num_workers]][[:]][ ][[int]][ ][[=]][ ][[0]]*, *[[pin_memory]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[persistent_workers]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[prefetch_factor]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[auto_find_batch_size]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[ignore_data_skip]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[sampler_seed]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.set_dataloader "Link to this definition")

    :   A method that regroups all arguments linked to the dataloaders creation.

        Parameters[:]

        :   - **drop_last** (bool, *optional*, defaults to False) â€" Whether to drop the last incomplete batch (if the length of the dataset is not divisible by the batch size) or not.

            - **num_workers** (int, *optional*, defaults to 0) â€" Number of subprocesses to use for data loading (PyTorch only). 0 means that the data will be loaded in the main process.

            - **pin_memory** (bool, *optional*, defaults to True) â€" Whether you want to pin memory in data loaders or not. Will default to True.

            - **persistent_workers** (bool, *optional*, defaults to False) â€" If True, the data loader will not shut down the worker processes after a dataset has been consumed once. This allows to maintain the workers Dataset instances alive. Can potentially speed up training, but will increase RAM usage. Will default to False.

            - **prefetch_factor** (int, *optional*) â€" Number of batches loaded in advance by each worker. 2 means there will be a total of 2 \* num_workers batches prefetched across all workers.

            - **auto_find_batch_size** (bool, *optional*, defaults to False) â€" Whether to find a batch size that will fit into memory automatically through exponential decay, avoiding CUDA Out-of-Memory errors. Requires accelerate to be installed (pip install accelerate)

            - **ignore_data_skip** (bool, *optional*, defaults to False) â€" When resuming training, whether or not to skip the epochs and batches to get the data loading at the same stage as in the previous training. If set to True, the training will begin faster (as that skipping step can take a long time) but will not yield the same results as the interrupted training would have.

            - **sampler_seed** (int, *optional*) â€" Random seed to be used with data samplers. If not set, random generators for data sampling will use the same seed as self.seed. This can be used to ensure reproducibility of data sampling, independent of the model seed.

        Example:

        [[\`\`]](#id1)[[\`]](#id3)py \>\>\> from transformers import TrainingArguments

        :::: 
        ::: highlight
            >>> args = TrainingArguments("working_dir")
            >>> args = args.set_dataloader(train_batch_size=16, eval_batch_size=64)
            >>> args.per_device_train_batch_size
            16
            ```
        :::
        ::::

    [[set_evaluate]][(]*[[strategy]][[:]][ ][[str][ ][[\|]][ ][IntervalStrategy]][ ][[=]][ ][[\'no\']]*, *[[steps]][[:]][ ][[int]][ ][[=]][ ][[500]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[8]]*, *[[accumulation_steps]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[delay]][[:]][ ][[float][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[loss_only]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[jit_mode]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)][ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.set_evaluate "Link to this definition")

    :   A method that regroups all arguments linked to evaluation.

        Parameters[:]

        :   - **strategy** (str or \[\~trainer_utils.IntervalStrategy\], *optional*, defaults to â€œnoâ€?) â€"

              The evaluation strategy to adopt during training. Possible values are:

              > ::: 
              > - â€?noâ€?: No evaluation is done during training.
              >
              > - â€?stepsâ€?: Evaluation is done (and logged) every steps.
              >
              > - â€?epochâ€?: Evaluation is done at the end of each epoch.
              > :::

              Setting a strategy different from â€œnoâ€? will set self.do_eval to True.

            - **steps** (int, *optional*, defaults to 500) â€" Number of update steps between two evaluations if strategy=â€?stepsâ€?.

            - **batch_size** (int *optional*, defaults to 8) â€" The batch size per device (GPU/TPU core/CPUâ€¦) used for evaluation.

            - **accumulation_steps** (int, *optional*) â€" Number of predictions steps to accumulate the output tensors for, before moving the results to the CPU. If left unset, the whole predictions are accumulated on GPU/TPU before being moved to the CPU (faster but requires more memory).

            - **delay** (float, *optional*) â€" Number of epochs or steps to wait for before the first evaluation can be performed, depending on the eval_strategy.

            - **loss_only** (bool, *optional*, defaults to False) â€" Ignores all outputs except the loss.

            - **jit_mode** (bool, *optional*) â€" Whether or not to use PyTorch jit trace for inference.

        Example:

        [[\`\`]](#id5)[[\`]](#id7)py \>\>\> from transformers import TrainingArguments

        :::: 
        ::: highlight
            >>> args = TrainingArguments("working_dir")
            >>> args = args.set_evaluate(strategy="steps", steps=100)
            >>> args.eval_steps
            100
            ```
        :::
        ::::

    [[set_logging]][(]*[[strategy]][[:]][ ][[str][ ][[\|]][ ][IntervalStrategy]][ ][[=]][ ][[\'steps\']]*, *[[steps]][[:]][ ][[int]][ ][[=]][ ][[500]]*, *[[report_to]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][[\]]]][ ][[=]][ ][[\'none\']]*, *[[level]][[:]][ ][[str]][ ][[=]][ ][[\'passive\']]*, *[[first_step]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[nan_inf_filter]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[on_each_node]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[replica_level]][[:]][ ][[str]][ ][[=]][ ][[\'passive\']]*[)][ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.set_logging "Link to this definition")

    :   A method that regroups all arguments linked to logging.

        Parameters[:]

        :   - **strategy** (str or \[\~trainer_utils.IntervalStrategy\], *optional*, defaults to â€œstepsâ€?) â€"

              The logging strategy to adopt during training. Possible values are:

              > ::: 
              > - â€?noâ€?: No logging is done during training.
              >
              > - â€?epochâ€?: Logging is done at the end of each epoch.
              >
              > - â€?stepsâ€?: Logging is done every logging_steps.
              > :::

            - **steps** (int, *optional*, defaults to 500) â€" Number of update steps between two logs if strategy=â€?stepsâ€?.

            - **level** (str, *optional*, defaults to â€œpassiveâ€?) â€" Logger log level to use on the main process. Possible choices are the log levels as strings: â€œdebugâ€?, â€œinfoâ€?, â€œwarningâ€?, â€œerrorâ€? and â€œcriticalâ€?, plus a â€œpassiveâ€? level which doesnâ€™t set anything and lets the application set the level.

            - **report_to** (str or List\[str\], *optional*, defaults to â€œallâ€?) â€" The list of integrations to report the results and logs to. Supported platforms are â€œazure_mlâ€?, â€œclearmlâ€?, â€œcodecarbonâ€?, â€œcomet_mlâ€?, â€œdagshubâ€?, â€œdvcliveâ€?, â€œflyteâ€?, â€œmlflowâ€?, â€œneptuneâ€?, â€œswanlabâ€?, â€œtensorboardâ€?, and â€œwandbâ€?. Use â€œallâ€? to report to all integrations installed, â€œnoneâ€? for no integrations.

            - **first_step** (bool, *optional*, defaults to False) â€" Whether to log and evaluate the first global_step or not.

            - **nan_inf_filter** (bool, *optional*, defaults to True) â€"

              Whether to filter nan and inf losses for logging. If set to True the loss of every step that is nan or inf is filtered and the average loss of the current logging window is taken instead.

              \<Tip\>

              nan_inf_filter only influences the logging of loss values, it does not change the behavior the gradient is computed or applied to the model.

              \</Tip\>

            - **on_each_node** (bool, *optional*, defaults to True) â€" In multinode distributed training, whether to log using log_level once per node, or only on the main node.

            - **replica_level** (str, *optional*, defaults to â€œpassiveâ€?) â€" Logger log level to use on replicas. Same choices as log_level

        Example:

        [[\`\`]](#id9)[[\`]](#id11)py \>\>\> from transformers import TrainingArguments

        :::: 
        ::: highlight
            >>> args = TrainingArguments("working_dir")
            >>> args = args.set_logging(strategy="steps", steps=100)
            >>> args.logging_steps
            100
            ```
        :::
        ::::

    [[set_lr_scheduler]][(]*[[name]][[:]][ ][[str][ ][[\|]][ ][SchedulerType]][ ][[=]][ ][[\'linear\']]*, *[[num_epochs]][[:]][ ][[float]][ ][[=]][ ][[3.0]]*, *[[max_steps]][[:]][ ][[int]][ ][[=]][ ][[-1]]*, *[[warmup_ratio]][[:]][ ][[float]][ ][[=]][ ][[0]]*, *[[warmup_steps]][[:]][ ][[int]][ ][[=]][ ][[0]]*[)][ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.set_lr_scheduler "Link to this definition")

    :   A method that regroups all arguments linked to the learning rate scheduler and its hyperparameters.

        Parameters[:]

        :   - **name** (str or \[SchedulerType\], *optional*, defaults to â€œlinearâ€?) â€" The scheduler type to use. See the documentation of \[SchedulerType\] for all possible values.

            - **num_epochs** (float, *optional*, defaults to 3.0) â€" Total number of training epochs to perform (if not an integer, will perform the decimal part percents of the last epoch before stopping training).

            - **max_steps** (int, *optional*, defaults to -1) â€" If set to a positive number, the total number of training steps to perform. Overrides num_train_epochs. For a finite dataset, training is reiterated through the dataset (if all data is exhausted) until max_steps is reached.

            - **warmup_ratio** (float, *optional*, defaults to 0.0) â€" Ratio of total training steps used for a linear warmup from 0 to learning_rate.

            - **warmup_steps** (int, *optional*, defaults to 0) â€" Number of steps used for a linear warmup from 0 to learning_rate. Overrides any effect of warmup_ratio.

        Example:

        [[\`\`]](#id13)[[\`]](#id15)py \>\>\> from transformers import TrainingArguments

        :::: 
        ::: highlight
            >>> args = TrainingArguments("working_dir")
            >>> args = args.set_lr_scheduler(name="cosine", warmup_ratio=0.05)
            >>> args.warmup_ratio
            0.05
            ```
        :::
        ::::

    [[set_optimizer]][(]*[[name]][[:]][ ][[str][ ][[\|]][ ][OptimizerNames]][ ][[=]][ ][[\'adamw_torch\']]*, *[[learning_rate]][[:]][ ][[float]][ ][[=]][ ][[5e-05]]*, *[[weight_decay]][[:]][ ][[float]][ ][[=]][ ][[0]]*, *[[beta1]][[:]][ ][[float]][ ][[=]][ ][[0.9]]*, *[[beta2]][[:]][ ][[float]][ ][[=]][ ][[0.999]]*, *[[epsilon]][[:]][ ][[float]][ ][[=]][ ][[1e-08]]*, *[[args]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.set_optimizer "Link to this definition")

    :   A method that regroups all arguments linked to the optimizer and its hyperparameters.

        Parameters[:]

        :   - **name** (str or \[training_args.OptimizerNames\], *optional*, defaults to â€œadamw_torchâ€?) â€" The optimizer to use: â€œadamw_torchâ€?, â€œadamw_torch_fusedâ€?, â€œadamw_apex_fusedâ€?, â€œadamw_anyprecisionâ€? or â€œadafactorâ€?.

            - **learning_rate** (float, *optional*, defaults to 5e-5) â€" The initial learning rate.

            - **weight_decay** (float, *optional*, defaults to 0) â€" The weight decay to apply (if not zero) to all layers except all bias and LayerNorm weights.

            - **beta1** (float, *optional*, defaults to 0.9) â€" The beta1 hyperparameter for the adam optimizer or its variants.

            - **beta2** (float, *optional*, defaults to 0.999) â€" The beta2 hyperparameter for the adam optimizer or its variants.

            - **epsilon** (float, *optional*, defaults to 1e-8) â€" The epsilon hyperparameter for the adam optimizer or its variants.

            - **args** (str, *optional*) â€" Optional arguments that are supplied to AnyPrecisionAdamW (only useful when optim=â€?adamw_anyprecisionâ€?).

        Example:

        [[\`\`]](#id17)[[\`]](#id19)py \>\>\> from transformers import TrainingArguments

        :::: 
        ::: highlight
            >>> args = TrainingArguments("working_dir")
            >>> args = args.set_optimizer(name="adamw_torch", beta1=0.8)
            >>> args.optim
            'adamw_torch'
            ```
        :::
        ::::

    [[set_push_to_hub]][(]*[[model_id]][[:]][ ][[str]]*, *[[strategy]][[:]][ ][[str][ ][[\|]][ ][HubStrategy]][ ][[=]][ ][[\'every_save\']]*, *[[token]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[private_repo]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[always_push]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)][ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.set_push_to_hub "Link to this definition")

    :   A method that regroups all arguments linked to synchronizing checkpoints with the Hub.

        \<Tip\>

        Calling this method will set self.push_to_hub to True, which means the output_dir will begin a git directory synced with the repo (determined by model_id) and the content will be pushed each time a save is triggered (depending on your self.save_strategy). Calling \[\~Trainer.save_model\] will also trigger a push.

        \</Tip\>

        Parameters[:]

        :   - **model_id** (str) â€" The name of the repository to keep in sync with the local *output_dir*. It can be a simple model ID in which case the model will be pushed in your namespace. Otherwise it should be the whole repository name, for instance â€œuser_name/modelâ€?, which allows you to push to an organization you are a member of with â€œorganization_name/modelâ€?.

            - **strategy** (str or \[\~trainer_utils.HubStrategy\], *optional*, defaults to â€œevery_saveâ€?) â€"

              Defines the scope of what is pushed to the Hub and when. Possible values are:

              - â€?endâ€?: push the model, its configuration, the processing_class e.g. tokenizer (if passed along to the \[Trainer\]) and a

              draft of a model card when the \[\~Trainer.save_model\] method is called. - â€œevery_saveâ€?: push the model, its configuration, the processing_class e.g. tokenizer (if passed along to the \[Trainer\])

              > ::: 
              > and
              > :::

              a draft of a model card each time there is a model save. The pushes are asynchronous to not block training, and in case the save are very frequent, a new push is only attempted if the previous one is finished. A last push is made with the final model at the end of training. - â€œcheckpointâ€?: like â€œevery_saveâ€? but the latest checkpoint is also pushed in a subfolder named last-checkpoint, allowing you to resume training easily with trainer.train(resume_from_checkpoint=â€?last-checkpointâ€?). - â€œall_checkpointsâ€?: like â€œcheckpointâ€? but all checkpoints are pushed like they appear in the

              > ::: 
              > output
              > :::

              folder (so you will get one checkpoint folder per folder in your final repository)

            - **token** (str, *optional*) â€" The token to use to push the model to the Hub. Will default to the token in the cache folder obtained with huggingface-cli login.

            - **private_repo** (bool, *optional*, defaults to False) â€" Whether to make the repo private. If None (default), the repo will be public unless the organizationâ€™s default is private. This value is ignored if the repo already exists.

            - **always_push** (bool, *optional*, defaults to False) â€" Unless this is True, the Trainer will skip pushing a checkpoint when the previous push is not finished.

        Example:

        [[\`\`]](#id21)[[\`]](#id23)py \>\>\> from transformers import TrainingArguments

        :::: 
        ::: highlight
            >>> args = TrainingArguments("working_dir")
            >>> args = args.set_push_to_hub("me/awesome-model")
            >>> args.hub_model_id
            'me/awesome-model'
            ```
        :::
        ::::

    [[set_save]][(]*[[strategy]][[:]][ ][[str][ ][[\|]][ ][IntervalStrategy]][ ][[=]][ ][[\'steps\']]*, *[[steps]][[:]][ ][[int]][ ][[=]][ ][[500]]*, *[[total_limit]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[on_each_node]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)][ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.set_save "Link to this definition")

    :   A method that regroups all arguments linked to checkpoint saving.

        Parameters[:]

        :   - **strategy** (str or \[\~trainer_utils.IntervalStrategy\], *optional*, defaults to â€œstepsâ€?) â€"

              The checkpoint save strategy to adopt during training. Possible values are:

              > ::: 
              > - â€?noâ€?: No save is done during training.
              >
              > - â€?epochâ€?: Save is done at the end of each epoch.
              >
              > - â€?stepsâ€?: Save is done every save_steps.
              > :::

            - **steps** (int, *optional*, defaults to 500) â€" Number of updates steps before two checkpoint saves if strategy=â€?stepsâ€?.

            - **total_limit** (int, *optional*) â€" If a value is passed, will limit the total amount of checkpoints. Deletes the older checkpoints in output_dir.

            - **on_each_node** (bool, *optional*, defaults to False) â€"

              When doing multi-node distributed training, whether to save models and checkpoints on each node, or only on the main one.

              This should not be activated when the different nodes use the same storage as the files will be saved with the same names for each node.

        Example:

        [[\`\`]](#id25)[[\`]](#id27)py \>\>\> from transformers import TrainingArguments

        :::: 
        ::: highlight
            >>> args = TrainingArguments("working_dir")
            >>> args = args.set_save(strategy="steps", steps=100)
            >>> args.save_steps
            100
            ```
        :::
        ::::

    [[set_testing]][(]*[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[8]]*, *[[loss_only]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[jit_mode]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)][ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.set_testing "Link to this definition")

    :   A method that regroups all basic arguments linked to testing on a held-out dataset.

        \<Tip\>

        Calling this method will automatically set self.do_predict to True.

        \</Tip\>

        Parameters[:]

        :   - **batch_size** (int *optional*, defaults to 8) â€" The batch size per device (GPU/TPU core/CPUâ€¦) used for testing.

            - **loss_only** (bool, *optional*, defaults to False) â€" Ignores all outputs except the loss.

            - **jit_mode** (bool, *optional*) â€" Whether or not to use PyTorch jit trace for inference.

        Example:

        [[\`\`]](#id29)[[\`]](#id31)py \>\>\> from transformers import TrainingArguments

        :::: 
        ::: highlight
            >>> args = TrainingArguments("working_dir")
            >>> args = args.set_testing(batch_size=32)
            >>> args.per_device_eval_batch_size
            32
            ```
        :::
        ::::

    [[set_training]][(]*[[learning_rate]][[:]][ ][[float]][ ][[=]][ ][[5e-05]]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[8]]*, *[[weight_decay]][[:]][ ][[float]][ ][[=]][ ][[0]]*, *[[num_epochs]][[:]][ ][[float]][ ][[=]][ ][[3]]*, *[[max_steps]][[:]][ ][[int]][ ][[=]][ ][[-1]]*, *[[gradient_accumulation_steps]][[:]][ ][[int]][ ][[=]][ ][[1]]*, *[[seed]][[:]][ ][[int]][ ][[=]][ ][[42]]*, *[[gradient_checkpointing]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)][ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.set_training "Link to this definition")

    :   A method that regroups all basic arguments linked to the training.

        \<Tip\>

        Calling this method will automatically set self.do_train to True.

        \</Tip\>

        Parameters[:]

        :   - **learning_rate** (float, *optional*, defaults to 5e-5) â€" The initial learning rate for the optimizer.

            - **batch_size** (int *optional*, defaults to 8) â€" The batch size per device (GPU/TPU core/CPUâ€¦) used for training.

            - **weight_decay** (float, *optional*, defaults to 0) â€" The weight decay to apply (if not zero) to all layers except all bias and LayerNorm weights in the optimizer.

            - **num_train_epochs** (float, *optional*, defaults to 3.0) â€" Total number of training epochs to perform (if not an integer, will perform the decimal part percents of the last epoch before stopping training).

            - **max_steps** (int, *optional*, defaults to -1) â€" If set to a positive number, the total number of training steps to perform. Overrides num_train_epochs. For a finite dataset, training is reiterated through the dataset (if all data is exhausted) until max_steps is reached.

            - **gradient_accumulation_steps** (int, *optional*, defaults to 1) â€"

              Number of updates steps to accumulate the gradients for, before performing a backward/update pass.

              \<Tip warning=\>

              When using gradient accumulation, one step is counted as one step with backward pass. Therefore, logging, evaluation, save will be conducted every gradient_accumulation_steps \* xxx_step training examples.

              \</Tip\>

            - **seed** (int, *optional*, defaults to 42) â€" Random seed that will be set at the beginning of training. To ensure reproducibility across runs, use the \[\~Trainer.model_init\] function to instantiate the model if it has some randomly initialized parameters.

            - **gradient_checkpointing** (bool, *optional*, defaults to False) â€" If True, use gradient checkpointing to save memory at the expense of slower backward pass.

        Example:

        [[\`\`]](#id33)[[\`]](#id35)py \>\>\> from transformers import TrainingArguments

        :::: 
        ::: highlight
            >>> args = TrainingArguments("working_dir")
            >>> args = args.set_training(learning_rate=1e-4, batch_size=32)
            >>> args.learning_rate
            1e-4
            ```
        :::
        ::::

    *[property][ ]*[[should_log]][ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.should_log "Link to this definition")

    :   Whether or not the current process should produce log.

    *[property][ ]*[[should_save]][ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.should_save "Link to this definition")

    :   Whether or not the current process should write to disk, e.g., to save models and checkpoints.

    [[to_dict]][(][)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\training_args.py#L304-L310)[ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.to_dict "Link to this definition")

    :   Serializes this instance while replace Enum by their values (for JSON serialization support). It obfuscates the token values by removing their value.

    [[to_json_string]][(][)][ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.to_json_string "Link to this definition")

    :   Serializes this instance to a JSON string.

    [[to_sanitized_dict]][(][)] [[→] [[dict][[\[]][str][[,]][ ][Any][[\]]]]][ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.to_sanitized_dict "Link to this definition")

    :   Sanitized serialization to use with TensorBoardâ€™s hparams

    *[property][ ]*[[train_batch_size]]*[[:]][ ][int]*[ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.train_batch_size "Link to this definition")

    :   The actual batch size for training (may differ from per_gpu_train_batch_size in distributed training).

    *[property][ ]*[[world_size]][ïƒ?](#sentence_transformers.training_args.SentenceTransformerTrainingArguments.world_size "Link to this definition")

    :   The number of processes used in parallel.