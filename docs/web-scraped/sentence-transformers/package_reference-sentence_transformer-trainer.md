# Source: https://www.sbert.net/docs/package_reference/sentence_transformer/trainer.html

# Trainer[ïƒ?](#trainer "Link to this heading")

## SentenceTransformerTrainer[ïƒ?](#sentencetransformertrainer "Link to this heading")

*[class][ ]*[[sentence_transformers.trainer.]][[SentenceTransformerTrainer]][(]*[[model]][[:]][ ][[[SentenceTransformer]](SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[args]][[:]][ ][[[SentenceTransformerTrainingArguments]](training_args.html#sentence_transformers.training_args.SentenceTransformerTrainingArguments "sentence_transformers.training_args.SentenceTransformerTrainingArguments")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[train_dataset]][[:]][ ][[Dataset][ ][[\|]][ ][DatasetDict][ ][[\|]][ ][IterableDataset][ ][[\|]][ ][dict][[\[]][str][[,]][ ][Dataset][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[eval_dataset]][[:]][ ][[Dataset][ ][[\|]][ ][DatasetDict][ ][[\|]][ ][IterableDataset][ ][[\|]][ ][dict][[\[]][str][[,]][ ][Dataset][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[loss]][[:]][ ][[nn.Module][ ][[\|]][ ][dict][[\[]][str][[,]][ ][nn.Module][[\]]][ ][[\|]][ ][Callable][[\[]][[\[]][[SentenceTransformer]](SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")[[\]]][[,]][ ][[torch.nn.Module]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][dict][[\[]][str][[,]][ ][Callable][[\[]][[\[]][[SentenceTransformer]](SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")[[\]]][[,]][ ][[torch.nn.Module]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")[[\]]][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[evaluator]][[:]][ ][[[SentenceEvaluator]](evaluation.html#sentence_transformers.evaluation.SentenceEvaluator "sentence_transformers.evaluation.SentenceEvaluator")[ ][[\|]][ ][list][[\[]][[SentenceEvaluator]](evaluation.html#sentence_transformers.evaluation.SentenceEvaluator "sentence_transformers.evaluation.SentenceEvaluator")[[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[data_collator]][[:]][ ][[DataCollator][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[tokenizer]][[:]][ ][[PreTrainedTokenizerBase][ ][[\|]][ ][Callable][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[model_init]][[:]][ ][[Callable][[\[]][[\[]][[\]]][[,]][ ][[SentenceTransformer]](SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")[[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[compute_metrics]][[:]][ ][[Callable][[\[]][[\[]][EvalPrediction][[\]]][[,]][ ][dict][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[callbacks]][[:]][ ][[list][[\[]][TrainerCallback][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[optimizers]][[:]][ ][[tuple][[\[]][[torch.optim.Optimizer]](https://docs.pytorch.org/docs/stable/optim.html#torch.optim.Optimizer "(in PyTorch v2.9)")[[,]][ ][[torch.optim.lr_scheduler.LambdaLR]](https://docs.pytorch.org/docs/stable/generated/torch.optim.lr_scheduler.LambdaLR.html#torch.optim.lr_scheduler.LambdaLR "(in PyTorch v2.9)")[[\]]]][ ][[=]][ ][[(None,] [None)]]*, *[[preprocess_logits_for_metrics]][[:]][ ][[Callable][[\[]][[\[]][[torch.Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[,]][ ][[torch.Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]][[,]][ ][[torch.Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\trainer.py#L60-L1305)[ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer "Link to this definition")

:   SentenceTransformerTrainer is a simple but feature-complete training and eval loop for PyTorch based on the ðŸ¤--- Transformers [[`Trainer`]](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.Trainer "(in transformers vmain)").

    This trainer integrates support for various [[`transformers.TrainerCallback`]](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.TrainerCallback "(in transformers vmain)") subclasses, such as:

    - [[`WandbCallback`]](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.integrations.WandbCallback "(in transformers vmain)") to automatically log training metrics to W&B if wandb is installed

    - [[`TensorBoardCallback`]](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.integrations.TensorBoardCallback "(in transformers vmain)") to log training metrics to TensorBoard if tensorboard is accessible.

    - [[`CodeCarbonCallback`]](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.integrations.CodeCarbonCallback "(in transformers vmain)") to track the carbon emissions of your model during training if codecarbon is installed.

      > ::: 
      > - Note: These carbon emissions will be included in your automatically generated model card.
      > :::

    See the Transformers [Callbacks](https://huggingface.co/docs/transformers/main/en/main_classes/callback) documentation for more information on the integrated callbacks and how to write your own callbacks.

    Parameters[:]

    :   - **model** ([[`SentenceTransformer`]](SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer"), *optional*) â€" The model to train, evaluate or use for predictions. If not provided, a model_init must be passed.

        - **args** ([[`SentenceTransformerTrainingArguments`]](training_args.html#sentence_transformers.training_args.SentenceTransformerTrainingArguments "sentence_transformers.training_args.SentenceTransformerTrainingArguments"), *optional*) â€" The arguments to tweak for training. Will default to a basic instance of [[`SentenceTransformerTrainingArguments`]](training_args.html#sentence_transformers.training_args.SentenceTransformerTrainingArguments "sentence_transformers.training_args.SentenceTransformerTrainingArguments") with the output_dir set to a directory named *tmp_trainer* in the current directory if not provided.

        - **train_dataset** (Union\[[[`datasets.Dataset`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)"), [[`datasets.DatasetDict`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.DatasetDict "(in datasets vmain)"), [[`datasets.IterableDataset`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.IterableDataset "(in datasets vmain)"), Dict\[str, [[`datasets.Dataset`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)")\]\], *optional*) â€" The dataset to use for training. Must have a format accepted by your loss function, see [Training Overview \> Dataset Format](../../../docs/sentence_transformer/training_overview.html#dataset-format).

        - **eval_dataset** (Union\[[[`datasets.Dataset`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)"), [[`datasets.DatasetDict`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.DatasetDict "(in datasets vmain)"), [[`datasets.IterableDataset`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.IterableDataset "(in datasets vmain)"), Dict\[str, [[`datasets.Dataset`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)")\]\], *optional*) â€"

          The dataset to use for evaluation. Must have a format accepted by your loss function, see [Training Overview \> Dataset Format](../../../docs/sentence_transformer/training_overview.html#dataset-format).

        - **loss** (Optional\[Union\[[[`torch.nn.Module`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)"), Dict\[str, [[`torch.nn.Module`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")\], Callable\[\[[[`SentenceTransformer`]](SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")\], [[`torch.nn.Module`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")\], Dict\[str, Callable\[\[[[`SentenceTransformer`]](SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")\]\]\]\], *optional*) â€" The loss function to use for training. Can either be a loss class instance, a dictionary mapping dataset names to loss class instances, a function that returns a loss class instance given a model, or a dictionary mapping dataset names to functions that return a loss class instance given a model. In practice, the latter two are primarily used for hyper-parameter optimization. Will default to [[`CoSENTLoss`]](losses.html#sentence_transformers.losses.CoSENTLoss "sentence_transformers.losses.CoSENTLoss") if no [`loss`] is provided.

        - **evaluator** (Union\[[[`SentenceEvaluator`]](evaluation.html#sentence_transformers.evaluation.SentenceEvaluator "sentence_transformers.evaluation.SentenceEvaluator"), List\[[[`SentenceEvaluator`]](evaluation.html#sentence_transformers.evaluation.SentenceEvaluator "sentence_transformers.evaluation.SentenceEvaluator")\]\], *optional*) â€" The evaluator instance for useful evaluation metrics during training. You can use an [`evaluator`] with or without an [`eval_dataset`], and vice versa. Generally, the metrics that an [`evaluator`] returns are more useful than the loss value returned from the [`eval_dataset`]. A list of evaluators will be wrapped in a [[`SequentialEvaluator`]](evaluation.html#sentence_transformers.evaluation.SequentialEvaluator "sentence_transformers.evaluation.SequentialEvaluator") to run them sequentially.

        - **callbacks** (List of \[[[`transformers.TrainerCallback`]](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.TrainerCallback "(in transformers vmain)")\], *optional*) â€"

          A list of callbacks to customize the training loop. Will add those to the list of default callbacks detailed in \[here\](callback).

          If you want to remove one of the default callbacks used, use the \[Trainer.remove_callback\] method.

        - **optimizers** (Tuple\[:class:\`torch.optim.Optimizer, [[`torch.optim.lr_scheduler.LambdaLR`]](https://docs.pytorch.org/docs/stable/generated/torch.optim.lr_scheduler.LambdaLR.html#torch.optim.lr_scheduler.LambdaLR "(in PyTorch v2.9)")\]\`, *optional*, defaults to (None, None)) â€" A tuple containing the optimizer and the scheduler to use. Will default to an instance of [[`torch.optim.AdamW`]](https://docs.pytorch.org/docs/stable/generated/torch.optim.AdamW.html#torch.optim.AdamW "(in PyTorch v2.9)") on your model and a scheduler given by [[`transformers.get_linear_schedule_with_warmup()`]](https://huggingface.co/docs/transformers/main/en/main_classes/optimizer_schedules#transformers.get_linear_schedule_with_warmup "(in transformers vmain)") controlled by args.

    Important attributes:

    > ::: 
    > - **model** â€" Always points to the core model. If using a transformers model, it will be a \[PreTrainedModel\] subclass.
    >
    > - **model_wrapped** â€" Always points to the most external model in case one or more other modules wrap the original model. This is the model that should be used for the forward pass. For example, under DeepSpeed, the inner model is wrapped in DeepSpeed and then again in torch.nn.DistributedDataParallel. If the inner model hasnâ€™t been wrapped, then self.model_wrapped is the same as self.model.
    >
    > - **is_model_parallel** â€" Whether or not a model has been switched to a model parallel mode (different from data parallelism, this means some of the model layers are split on different GPUs).
    >
    > - **place_model_on_device** â€" Whether or not to automatically place the model on the device - it will be set to False if model parallel or deepspeed is used, or if the default TrainingArguments.place_model_on_device is overridden to return False .
    >
    > - **is_in_train** â€" Whether or not a model is currently running train (e.g. when evaluate is called while in train)
    > :::

    [[add_callback]][(]*[[callback]]*[)][ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.add_callback "Link to this definition")

    :   Add a callback to the current list of \[\~transformers.TrainerCallback\].

        Parameters[:]

        :   **callback** (type or \[\~transformers.TrainerCallback\]) â€" A \[\~transformers.TrainerCallback\] class or an instance of a \[\~transformers.TrainerCallback\]. In the first case, will instantiate a member of that class.

    *[static][ ]*[[add_dataset_name_transform]][(]*[[batch]][[:]][ ][[dict][[\[]][str][[,]][ ][list][[\[]][Any][[\]]][[\]]]]*, *[[dataset_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[transform]][[:]][ ][[Callable][[\[]][[\[]][dict][[\[]][str][[,]][ ][list][[\[]][Any][[\]]][[\]]][[\]]][[,]][ ][dict][[\[]][str][[,]][ ][list][[\[]][Any][[\]]][[\]]][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[dict][[\[]][str][[,]][ ][list][[\[]][Any][[\]]][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\trainer.py#L1165-L1197)[ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.add_dataset_name_transform "Link to this definition")

    :   A transform/map function that adds prompts or dataset names to the batch.

        Parameters[:]

        :   - **batch** (*dict\[str,* *list\[Any\]\]*) â€" The batch of data, where each key is a column name and each value is a list of values.

            - **dataset_name** (*str* *\|* *None,* *optional*) â€" The name of this dataset, only if there are multiple datasets that use a different loss. Defaults to None.

            - **transform** (*Callable\[\[dict\[str,* *list\[Any\]\]\],* *dict\[str,* *list\[Any\]\]\],* *optional*) â€" An optional transform function to apply on the batch before adding prompts, etc. Defaults to None.

        Returns[:]

        :   The â€œjust-in-timeâ€? transformed batch with prompts and/or dataset names added.

        Return type[:]

        :   dict\[str, list\[Any\]\]

    [[add_model_card_callback]][(]*[[default_args_dict]][[:]][ ][[dict][[\[]][str][[,]][ ][Any][[\]]]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\trainer.py#L330-L348)[ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.add_model_card_callback "Link to this definition")

    :   Add a callback responsible for automatically tracking data required for the automatic model card generation

        This method is called in the [`__init__`] method of the [[`SentenceTransformerTrainer`]](#sentence_transformers.trainer.SentenceTransformerTrainer "sentence_transformers.trainer.SentenceTransformerTrainer") class.

        Parameters[:]

        :   **default_args_dict** (*Dict\[str,* *Any\]*) â€" A dictionary of the default training arguments, so we can determine which arguments have been changed for the model card.

        ::: 
        Note

        This method can be overridden by subclassing the trainer to remove/customize this callback in custom uses cases
        :::

    [[compute_loss]][(]*[[model]][[:]][ ][[[SentenceTransformer]](SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")]*, *[[inputs]][[:]][ ][[dict][[\[]][str][[,]][ ][[torch.Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][Any][[\]]]]*, *[[return_outputs]][[:]][ ][[bool]][ ][[=]][ ][[False]]*, *[[num_items_in_batch]][[=]][[None]]*[)] [[→] [[[torch.Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][tuple][[\[]][[torch.Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[[,]][ ][dict][[\[]][str][[,]][ ][Any][[\]]][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\trainer.py#L394-L444)[ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.compute_loss "Link to this definition")

    :   Computes the loss for the SentenceTransformer model.

        It uses [`self.loss`] to compute the loss, which can be a single loss function or a dictionary of loss functions for different datasets. If the loss is a dictionary, the dataset name is expected to be passed in the inputs under the key â€œdataset_nameâ€?. This is done automatically in the [`add_dataset_name_column`] method. Note that even if [`return_outputs`]` `[`=`]` `[`True`], the outputs will be empty, as the SentenceTransformers losses do not return outputs.

        Parameters[:]

        :   - **model** ([*SentenceTransformer*](SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")) â€" The SentenceTransformer model.

            - **inputs** (*Dict\[str,* *Union\[*[*torch.Tensor*](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")*,* *Any\]\]*) â€" The input data for the model.

            - **return_outputs** (*bool,* *optional*) â€" Whether to return the outputs along with the loss. Defaults to False.

            - **num_items_in_batch** (*int,* *optional*) â€" The number of items in the batch. Defaults to None. Unused, but required by the transformers Trainer.

        Returns[:]

        :   The computed loss. If return_outputs is True, returns a tuple of loss and outputs. Otherwise, returns only the loss.

        Return type[:]

        :   Union\[[torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)"), Tuple\[[torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)"), Dict\[str, Any\]\]\]

    [[create_model_card]][(]*[[language]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[license]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[tags]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[model_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[finetuned_from]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[tasks]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[dataset_tags]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[dataset]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[dataset_args]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\trainer.py#L1199-L1222)[ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.create_model_card "Link to this definition")

    :   Creates a draft of a model card using the information available to the Trainer.

        Parameters[:]

        :   - **language** (str, *optional*) â€" The language of the model (if applicable)

            - **license** (str, *optional*) â€" The license of the model. Will default to the license of the pretrained model used, if the original model given to the Trainer comes from a repo on the Hub.

            - **tags** (str or List\[str\], *optional*) â€" Some tags to be included in the metadata of the model card.

            - **model_name** (str, *optional*) â€" The name of the model.

            - **finetuned_from** (str, *optional*) â€" The name of the model used to fine-tune this one (if applicable). Will default to the name of the repo of the original model given to the Trainer (if it comes from the Hub).

            - **tasks** (str or List\[str\], *optional*) â€" One or several task identifiers, to be included in the metadata of the model card.

            - **dataset_tags** (str or List\[str\], *optional*) â€" One or several dataset tags, to be included in the metadata of the model card.

            - **dataset** (str or List\[str\], *optional*) â€" One or several dataset identifiers, to be included in the metadata of the model card.

            - **dataset_args** (str or List\[str\], *optional*) â€" One or several dataset arguments, to be included in the metadata of the model card.

    [[create_optimizer]][(][)][ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.create_optimizer "Link to this definition")

    :   Setup the optimizer.

        We provide a reasonable default that works well. If you want to use something else, you can pass a tuple in the Trainerâ€™s init through optimizers, or subclass and override this method in a subclass.

    [[create_optimizer_and_scheduler]][(]*[[num_training_steps]][[:]][ ][[int]]*[)][ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.create_optimizer_and_scheduler "Link to this definition")

    :   Setup the optimizer and the learning rate scheduler.

        We provide a reasonable default that works well. If you want to use something else, you can pass a tuple in the Trainerâ€™s init through optimizers, or subclass and override this method (or create_optimizer and/or create_scheduler) in a subclass.

    [[create_scheduler]][(]*[[num_training_steps]][[:]][ ][[int]]*, *[[optimizer]][[:]][ ][[[Optimizer]](https://docs.pytorch.org/docs/stable/optim.html#torch.optim.Optimizer "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.create_scheduler "Link to this definition")

    :   Setup the scheduler. The optimizer of the trainer must have been set up either before this method is called or passed as an argument.

        Parameters[:]

        :   **num_training_steps** (*int*) â€" The number of training steps to do.

    [[evaluate]][(]*[[eval_dataset]][[:]][ ][[Dataset][ ][[\|]][ ][dict][[\[]][str][[,]][ ][Dataset][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[ignore_keys]][[:]][ ][[list][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[metric_key_prefix]][[:]][ ][[str]][ ][[=]][ ][[\'eval\']]*[)] [[→] [[dict][[\[]][str][[,]][ ][float][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\trainer.py#L534-L546)[ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.evaluate "Link to this definition")

    :   Run evaluation and returns metrics.

        The calling script will be responsible for providing a method to compute metrics, as they are task-dependent (pass it to the init compute_metrics argument).

        You can also subclass and override this method to inject custom behavior.

        Parameters[:]

        :   - **eval_dataset** (Union\[Dataset, Dict\[str, Dataset\]), *optional*) â€"

              Pass a dataset if you wish to override self.eval_dataset. If it is a \[\~datasets.Dataset\], columns not accepted by the model.forward() method are automatically removed. If it is a dictionary, it will evaluate on each dataset, prepending the dictionary key to the metric name. Datasets must implement the \_\_len\_\_ method.

              \<Tip\>

              If you pass a dictionary with names of datasets as keys and datasets as values, evaluate will run separate evaluations on each dataset. This can be useful to monitor how training affects other datasets or simply to get a more fine-grained evaluation. When used with load_best_model_at_end, make sure metric_for_best_model references exactly one of the datasets. If you, for example, pass in  for two datasets data1 and data2, you could specify metric_for_best_model=â€?eval_data1_lossâ€? for using the loss on data1 and metric_for_best_model=â€?eval_data2_lossâ€? for the loss on data2.

              \</Tip\>

            - **ignore_keys** (List\[str\], *optional*) â€" A list of keys in the output of your model (if it is a dictionary) that should be ignored when gathering predictions.

            - **metric_key_prefix** (str, *optional*, defaults to â€œevalâ€?) â€" An optional prefix to be used as the metrics key prefix. For example the metrics â€œbleuâ€? will be named â€œeval_bleuâ€? if the prefix is â€œevalâ€? (default)

        Returns[:]

        :   A dictionary containing the evaluation loss and the potential metrics computed from the predictions. The dictionary also contains the epoch number which comes from the training state.

    [[get_batch_sampler]][(]*[[dataset]][[:]][ ][[Dataset]]*, *[[batch_size]][[:]][ ][[int]]*, *[[drop_last]][[:]][ ][[bool]]*, *[[valid_label_columns]][[:]][ ][[list][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[generator]][[:]][ ][[[Generator]](https://docs.pytorch.org/docs/stable/generated/torch.Generator.html#torch.Generator "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[seed]][[:]][ ][[int]][ ][[=]][ ][[0]]*[)] [[→] [[[BatchSampler]](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.BatchSampler "(in PyTorch v2.9)")[ ][[\|]][ ][None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\trainer.py#L626-L686)[ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.get_batch_sampler "Link to this definition")

    :   Returns the appropriate batch sampler based on the [`batch_sampler`] argument in [`self.args`]. This batch sampler class supports [`__len__`] and [`__iter__`] methods, and is used as the [`batch_sampler`] to create the [[`torch.utils.data.DataLoader`]](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader "(in PyTorch v2.9)").

        ::: 
        Note

        Override this method to provide a custom batch sampler.
        :::

        Parameters[:]

        :   - **dataset** (*Dataset*) â€" The dataset to sample from.

            - **batch_size** (*int*) â€" Number of samples per batch.

            - **drop_last** (*bool*) â€" If True, drop the last incomplete batch if the dataset size is not divisible by the batch size.

            - **valid_label_columns** (*List\[str\]*) â€" List of column names to check for labels. The first column name from [`valid_label_columns`] found in the dataset will be used as the label column.

            - **generator** ([*torch.Generator*](https://docs.pytorch.org/docs/stable/generated/torch.Generator.html#torch.Generator "(in PyTorch v2.9)")*,* *optional*) â€" Optional random number generator for shuffling the indices.

            - **seed** (*int*) â€" Seed for the random number generator to ensure reproducibility. Defaults to 0.

    [[get_eval_dataloader]][(]*[[eval_dataset]][[:]][ ][[Dataset][ ][[\|]][ ][DatasetDict][ ][[\|]][ ][IterableDataset][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[[DataLoader]](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader "(in PyTorch v2.9)")]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\trainer.py#L822-L912)[ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.get_eval_dataloader "Link to this definition")

    :   Returns the evaluation \[\~torch.utils.data.DataLoader\].

        Subclass and override this method if you want to inject some custom behavior.

        Parameters[:]

        :   **eval_dataset** (torch.utils.data.Dataset, *optional*) â€" If provided, will override self.eval_dataset. If it is a \[\~datasets.Dataset\], columns not accepted by the model.forward() method are automatically removed. It must implement \_\_len\_\_.

    [[get_learning_rates]][(][)][ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.get_learning_rates "Link to this definition")

    :   Returns the learning rate of each parameter from self.optimizer.

    [[get_multi_dataset_batch_sampler]][(]*[[dataset]][[:]][ ][[[ConcatDataset]](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.ConcatDataset "(in PyTorch v2.9)")]*, *[[batch_samplers]][[:]][ ][[list][[\[]][[BatchSampler]](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.BatchSampler "(in PyTorch v2.9)")[[\]]]]*, *[[generator]][[:]][ ][[[Generator]](https://docs.pytorch.org/docs/stable/generated/torch.Generator.html#torch.Generator "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[seed]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[0]]*[)] [[→] [[[BatchSampler]](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.BatchSampler "(in PyTorch v2.9)")]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\trainer.py#L688-L730)[ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.get_multi_dataset_batch_sampler "Link to this definition")

    :   Returns the appropriate multi-dataset batch sampler based on the [`multi_dataset_batch_sampler`] argument in [`self.args`]. This batch sampler class supports [`__len__`] and [`__iter__`] methods, and is used as the [`batch_sampler`] to create the [[`torch.utils.data.DataLoader`]](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader "(in PyTorch v2.9)").

        ::: 
        Note

        Override this method to provide a custom multi-dataset batch sampler.
        :::

        Parameters[:]

        :   - **dataset** (*ConcatDataset*) â€" The concatenation of all datasets.

            - **batch_samplers** (*List\[BatchSampler\]*) â€" List of batch samplers for each dataset in the concatenated dataset.

            - **generator** ([*torch.Generator*](https://docs.pytorch.org/docs/stable/generated/torch.Generator.html#torch.Generator "(in PyTorch v2.9)")*,* *optional*) â€" Optional random number generator for shuffling the indices.

            - **seed** (*int,* *optional*) â€" Optional seed for the random number generator

    [[get_num_trainable_parameters]][(][)][ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.get_num_trainable_parameters "Link to this definition")

    :   Get the number of trainable parameters.

    [[get_optimizer_group]][(]*[[param]][[:]][ ][[str][ ][[\|]][ ][[Parameter]](https://docs.pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.get_optimizer_group "Link to this definition")

    :   Returns optimizer group for a parameter if given, else returns all optimizer groups for params.

        Parameters[:]

        :   **param** (str or torch.nn.parameter.Parameter, *optional*) â€" The parameter for which optimizer group needs to be returned.

    [[get_test_dataloader]][(]*[[test_dataset]][[:]][ ][[Dataset][ ][[\|]][ ][DatasetDict][ ][[\|]][ ][IterableDataset]]*[)] [[→] [[[DataLoader]](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader "(in PyTorch v2.9)")]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\trainer.py#L914-L998)[ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.get_test_dataloader "Link to this definition")

    :   Returns the training \[\~torch.utils.data.DataLoader\].

        Subclass and override this method if you want to inject some custom behavior.

        Parameters[:]

        :   **test_dataset** (torch.utils.data.Dataset, *optional*) â€" The test dataset to use. If it is a \[\~datasets.Dataset\], columns not accepted by the model.forward() method are automatically removed. It must implement \_\_len\_\_.

    [[get_train_dataloader]][(][)] [[→] [[[DataLoader]](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader "(in PyTorch v2.9)")]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\trainer.py#L732-L820)[ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.get_train_dataloader "Link to this definition")

    :   Returns the training \[\~torch.utils.data.DataLoader\].

        Will use no sampler if train_dataset does not implement \_\_len\_\_, a random sampler (adapted to distributed training if necessary) otherwise.

        Subclass and override this method if you want to inject some custom behavior.

    [[hyperparameter_search]][(]*[[hp_space]][[:]][ ][[Callable][[\[]][[\[]][optuna.Trial][[\]]][[,]][ ][dict][[\[]][str][[,]][ ][float][[\]]][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[compute_objective]][[:]][ ][[Callable][[\[]][[\[]][dict][[\[]][str][[,]][ ][float][[\]]][[\]]][[,]][ ][float][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[n_trials]][[:]][ ][[int]][ ][[=]][ ][[20]]*, *[[direction]][[:]][ ][[str][ ][[\|]][ ][list][[\[]][str][[\]]]][ ][[=]][ ][[\'minimize\']]*, *[[backend]][[:]][ ][[str][ ][[\|]][ ][HPSearchBackend][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[hp_name]][[:]][ ][[Callable][[\[]][[\[]][optuna.Trial][[\]]][[,]][ ][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[BestRun][ ][[\|]][ ][list][[\[]][BestRun][[\]]]]][ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.hyperparameter_search "Link to this definition")

    :   Launch an hyperparameter search using optuna or Ray Tune or SigOpt. The optimized quantity is determined by compute_objective, which defaults to a function returning the evaluation loss when no metric is provided, the sum of all metrics otherwise.

        \<Tip warning=\>

        To use this method, you need to have provided a model_init when initializing your \[Trainer\]: we need to reinitialize the model at each new run. This is incompatible with the optimizers argument, so you need to subclass \[Trainer\] and override the method \[\~Trainer.create_optimizer_and_scheduler\] for custom optimizer/scheduler.

        \</Tip\>

        Parameters[:]

        :   - **hp_space** (Callable\[\[â€œoptuna.Trialâ€?\], Dict\[str, float\]\], *optional*) â€" A function that defines the hyperparameter search space. Will default to \[\~trainer_utils.default_hp_space_optuna\] or \[\~trainer_utils.default_hp_space_ray\] or \[\~trainer_utils.default_hp_space_sigopt\] depending on your backend.

            - **compute_objective** (Callable\[\[Dict\[str, float\]\], float\], *optional*) â€" A function computing the objective to minimize or maximize from the metrics returned by the evaluate method. Will default to \[\~trainer_utils.default_compute_objective\].

            - **n_trials** (int, *optional*, defaults to 100) â€" The number of trial runs to test.

            - **direction** (str or List\[str\], *optional*, defaults to â€œminimizeâ€?) â€" If itâ€™s single objective optimization, direction is str, can be â€œminimizeâ€? or â€œmaximizeâ€?, you should pick â€œminimizeâ€? when optimizing the validation loss, â€œmaximizeâ€? when optimizing one or several metrics. If itâ€™s multi objectives optimization, direction is List\[str\], can be List of â€œminimizeâ€? and â€œmaximizeâ€?, you should pick â€œminimizeâ€? when optimizing the validation loss, â€œmaximizeâ€? when optimizing one or several metrics.

            - **backend** (str or \[\~training_utils.HPSearchBackend\], *optional*) â€" The backend to use for hyperparameter search. Will default to optuna or Ray Tune or SigOpt, depending on which one is installed. If all are installed, will default to optuna.

            - **hp_name** (Callable\[\[â€œoptuna.Trialâ€?\], str\]\], *optional*) â€" A function that defines the trial/run name. Will default to None.

            - **kwargs** (Dict\[str, Any\], *optional*) â€"

              Additional keyword arguments for each backend:

              - optuna: parameters from \[optuna.study.create_study\]([https://optuna.readthedocs.io/en/stable/reference/generated/optuna.study.create_study.html](https://optuna.readthedocs.io/en/stable/reference/generated/optuna.study.create_study.html)) and also the parameters timeout, n_jobs and gc_after_trial from \[optuna.study.Study.optimize\]([https://optuna.readthedocs.io/en/stable/reference/generated/optuna.study.Study.html#optuna.study.Study.optimize](https://optuna.readthedocs.io/en/stable/reference/generated/optuna.study.Study.html#optuna.study.Study.optimize))

              - ray: parameters from \[tune.run\]([https://docs.ray.io/en/latest/tune/api_docs/execution.html#tune-run](https://docs.ray.io/en/latest/tune/api_docs/execution.html#tune-run)). If resources_per_trial is not set in the kwargs, it defaults to 1 CPU core and 1 GPU (if available). If progress_reporter is not set in the kwargs, \[ray.tune.CLIReporter\]([https://docs.ray.io/en/latest/tune/api/doc/ray.tune.CLIReporter.html](https://docs.ray.io/en/latest/tune/api/doc/ray.tune.CLIReporter.html)) is used.

              - sigopt: the parameter proxies from \[sigopt.Connection.set_proxies\]([https://docs.sigopt.com/support/faq#how-do-i-use-sigopt-with-a-proxy](https://docs.sigopt.com/support/faq#how-do-i-use-sigopt-with-a-proxy)).

        Returns[:]

        :   All the information about the best run or best runs for multi-objective optimization. Experiment summary can be found in run_summary attribute for Ray backend.

        Return type[:]

        :   \[trainer_utils.BestRun or List\[trainer_utils.BestRun\]\]

    [[is_local_process_zero]][(][)] [[→] [[bool]]][ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.is_local_process_zero "Link to this definition")

    :   Whether or not this process is the local (e.g., on one machine if training in a distributed fashion on several machines) main process.

    [[is_world_process_zero]][(][)] [[→] [[bool]]][ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.is_world_process_zero "Link to this definition")

    :   Whether or not this process is the global main process (when training in a distributed fashion on several machines, this is only going to be True for one process).

    [[log]][(]*[[logs]][[:]][ ][[dict][[\[]][str][[,]][ ][float][[\]]]]*, *[[start_time]][[:]][ ][[float][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\trainer.py#L467-L497)[ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.log "Link to this definition")

    :   Log logs on the various objects watching training.

        Subclass and override this method to inject custom behavior.

        Parameters[:]

        :   - **logs** (Dict\[str, float\]) â€" The values to log.

            - **start_time** (Optional\[float\]) â€" The start of training.

    [[maybe_add_dataset_name_column]][(]*[[dataset]][[:]][ ][[DatasetDict][ ][[\|]][ ][Dataset][ ][[\|]][ ][None]]*, *[[prompts]][[:]][ ][[dict][[\[]][str][[,]][ ][dict][[\[]][str][[,]][ ][str][[\]]][[\]]][ ][[\|]][ ][dict][[\[]][str][[,]][ ][str][[\]]][ ][[\|]][ ][str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[router_mapping]][[:]][ ][[dict][[\[]][str][[,]][ ][dict][[\[]][str][[,]][ ][str][[\]]][[\]]][ ][[\|]][ ][dict][[\[]][str][[,]][ ][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[dataset_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[DatasetDict][ ][[\|]][ ][Dataset][ ][[\|]][ ][None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\trainer.py#L1075-L1115)[ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.maybe_add_dataset_name_column "Link to this definition")

    :   Maybe add a dataset name column to the dataset, if

        1.  the dataset is a DatasetDict, and one of:

            > ::: 
            > 1.  The loss is a dictionary, or
            >
            > 2.  The prompts contain a mapping of dataset names, or
            >
            > 3.  The router_mapping contains a mapping of dataset names.
            > :::

        Parameters[:]

        :   **dataset** (*DatasetDict* *\|* *Dataset* *\|* *None*) â€" The dataset to add prompts or dataset names to.

        Returns[:]

        :   The dataset with prompts or dataset names added.

        Return type[:]

        :   DatasetDict \| Dataset \| None

    [[pop_callback]][(]*[[callback]]*[)][ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.pop_callback "Link to this definition")

    :   Remove a callback from the current list of \[\~transformers.TrainerCallback\] and returns it.

        If the callback is not found, returns None (and no error is raised).

        Parameters[:]

        :   **callback** (type or \[\~transformers.TrainerCallback\]) â€" A \[\~transformers.TrainerCallback\] class or an instance of a \[\~transformers.TrainerCallback\]. In the first case, will pop the first member of that class found in the list of callbacks.

        Returns[:]

        :   The callback removed, if found.

        Return type[:]

        :   \[\~transformers.TrainerCallback\]

    [[preprocess_dataset]][(]*[[dataset]][[:]][ ][[DatasetDict][ ][[\|]][ ][Dataset][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[prompts]][[:]][ ][[dict][[\[]][str][[,]][ ][dict][[\[]][str][[,]][ ][str][[\]]][[\]]][ ][[\|]][ ][dict][[\[]][str][[,]][ ][str][[\]]][ ][[\|]][ ][str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[router_mapping]][[:]][ ][[dict][[\[]][str][[,]][ ][dict][[\[]][str][[,]][ ][str][[\]]][[\]]][ ][[\|]][ ][dict][[\[]][str][[,]][ ][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[dataset_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[DatasetDict][ ][[\|]][ ][Dataset][ ][[\|]][ ][None]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\trainer.py#L1036-L1073)[ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.preprocess_dataset "Link to this definition")

    :   Preprocess the dataset by optionally lazily adding a dataset name column, required for multi-dataset training with multiple losses, for dataset-specific prompts, or for dataset-specific router mappings.

        Parameters[:]

        :   - **dataset** (*DatasetDict* *\|* *Dataset* *\|* *None*) â€" The dataset to preprocess. If None, no preprocessing is done.

            - **prompts** (*dict\[str,* *dict\[str,* *str\]\]* *\|* *dict\[str,* *str\]* *\|* *str* *\|* *None*) â€" Optional prompts to add to the dataset. If a string, it is used as a single prompt for all datasets, but it can also be a dictionary mapping dataset names to prompts, a dictionary mapping column names to prompts, or a nested dictionary mapping dataset names to column names to prompts.

            - **router_mapping** (*dict\[str,* *dict\[str,* *str\]\]* *\|* *dict\[str,* *str\]* *\|* *None*) â€" Optional router mapping to add to the dataset. Either a dictionary mapping of column names to [[`Router`]](models.html#sentence_transformers.models.Router "sentence_transformers.models.Router") routes or a nested dictionary mapping dataset names to column names to routes.

            - **dataset_name** (*str* *\|* *None*) â€" The name of the dataset, used for multi-dataset training with multiple losses.

        Returns[:]

        :   The preprocessed dataset, perhaps with dataset names added as a lazy column.

        Return type[:]

        :   DatasetDict \| Dataset \| None

    [[propagate_args_to_deepspeed]][(]*[[auto_find_batch_size]][[=]][[False]]*[)][ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.propagate_args_to_deepspeed "Link to this definition")

    :   Sets values in the deepspeed plugin based on the Trainer args

    [[push_to_hub]][(]*[[commit_message]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[\'End] [of] [training\']]*, *[[blocking]][[:]][ ][[bool]][ ][[=]][ ][[True]]*, *[[token]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[revision]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[str]]][ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.push_to_hub "Link to this definition")

    :   Upload self.model and self.processing_class to the ðŸ¤--- model hub on the repo self.args.hub_model_id.

        Parameters[:]

        :   - **commit_message** (str, *optional*, defaults to â€œEnd of trainingâ€?) â€" Message to commit while pushing.

            - **blocking** (bool, *optional*, defaults to True) â€" Whether the function should return only when the git push has finished.

            - **token** (str, *optional*, defaults to None) â€" Token with write permission to overwrite Trainerâ€™s original args.

            - **revision** (str, *optional*) â€" The git revision to commit from. Defaults to the head of the â€œmainâ€? branch.

            - **kwargs** (Dict\[str, Any\], *optional*) â€" Additional keyword arguments passed along to \[\~Trainer.create_model_card\].

        Returns[:]

        :   The URL of the repository where the model was pushed if blocking=False, or a Future object tracking the progress of the commit if blocking=True.

    [[remove_callback]][(]*[[callback]]*[)][ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.remove_callback "Link to this definition")

    :   Remove a callback from the current list of \[\~transformers.TrainerCallback\].

        Parameters[:]

        :   **callback** (type or \[\~transformers.TrainerCallback\]) â€" A \[\~transformers.TrainerCallback\] class or an instance of a \[\~transformers.TrainerCallback\]. In the first case, will remove the first member of that class found in the list of callbacks.

    [[save_model]][(]*[[output_dir]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\_internal_call]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)][ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.save_model "Link to this definition")

    :   Will save the model, so you can reload it using from_pretrained().

        Will only save from the main process.

    [[set_initial_training_values]][(]*[[args]][[:]][ ][[TrainingArguments]]*, *[[dataloader]][[:]][ ][[[DataLoader]](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader "(in PyTorch v2.9)")]*, *[[total_train_batch_size]][[:]][ ][[int]]*[)][ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.set_initial_training_values "Link to this definition")

    :   Calculates and returns the following values: - num_train_epochs - num_update_steps_per_epoch - num_examples - num_train_samples - epoch_based - len_dataloader - max_steps

    [[train]][(]*[[resume_from_checkpoint]][[:]][ ][[bool][ ][[\|]][ ][str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[trial]][[:]][ ][[optuna.Trial][ ][[\|]][ ][dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[ignore_keys_for_eval]][[:]][ ][[list][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\*\*]][[kwargs]]*[)][ïƒ?](#sentence_transformers.trainer.SentenceTransformerTrainer.train "Link to this definition")

    :   Main training entry point.

        Parameters[:]

        :   - **resume_from_checkpoint** (str or bool, *optional*) â€" If a str, local path to a saved checkpoint as saved by a previous instance of \[Trainer\]. If a bool and equals True, load the last checkpoint in *args.output_dir* as saved by a previous instance of \[Trainer\]. If present, training will resume from the model/optimizer/scheduler states loaded here.

            - **trial** (optuna.Trial or Dict\[str, Any\], *optional*) â€" The trial run or the hyperparameter dictionary for hyperparameter search.

            - **ignore_keys_for_eval** (List\[str\], *optional*) â€" A list of keys in the output of your model (if it is a dictionary) that should be ignored when gathering predictions for evaluation during the training.

            - **kwargs** (Dict\[str, Any\], *optional*) â€" Additional keyword arguments used to hide deprecated arguments