# Source: https://www.sbert.net/docs/package_reference/sentence_transformer/sampler.html

# Samplers[ïƒ?](#samplers "Link to this heading")

## BatchSamplers[ïƒ?](#batchsamplers "Link to this heading")

*[class][ ]*[[sentence_transformers.training_args.]][[BatchSamplers]][(]*[[value]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\training_args.py#L17-L82)[ïƒ?](#sentence_transformers.training_args.BatchSamplers "Link to this definition")

:   Stores the acceptable string identifiers for batch samplers.

    The batch sampler is responsible for determining how samples are grouped into batches during training. Valid options are:

    - [`BatchSamplers.BATCH_SAMPLER`]: **\[default\]** Uses [[`DefaultBatchSampler`]](#sentence_transformers.sampler.DefaultBatchSampler "sentence_transformers.sampler.DefaultBatchSampler"), the default PyTorch batch sampler.

    - [`BatchSamplers.NO_DUPLICATES`]: Uses [[`NoDuplicatesBatchSampler`]](#sentence_transformers.sampler.NoDuplicatesBatchSampler "sentence_transformers.sampler.NoDuplicatesBatchSampler"), ensuring no duplicate samples in a batch. Recommended for losses that use in-batch negatives, such as:

      > ::: 
      > - [[`MultipleNegativesRankingLoss`]](losses.html#sentence_transformers.losses.MultipleNegativesRankingLoss "sentence_transformers.losses.MultipleNegativesRankingLoss")
      >
      > - [[`CachedMultipleNegativesRankingLoss`]](losses.html#sentence_transformers.losses.CachedMultipleNegativesRankingLoss "sentence_transformers.losses.CachedMultipleNegativesRankingLoss")
      >
      > - [[`MultipleNegativesSymmetricRankingLoss`]](losses.html#sentence_transformers.losses.MultipleNegativesSymmetricRankingLoss "sentence_transformers.losses.MultipleNegativesSymmetricRankingLoss")
      >
      > - [[`CachedMultipleNegativesSymmetricRankingLoss`]](losses.html#sentence_transformers.losses.CachedMultipleNegativesSymmetricRankingLoss "sentence_transformers.losses.CachedMultipleNegativesSymmetricRankingLoss")
      >
      > - [[`MegaBatchMarginLoss`]](losses.html#sentence_transformers.losses.MegaBatchMarginLoss "sentence_transformers.losses.MegaBatchMarginLoss")
      >
      > - [[`GISTEmbedLoss`]](losses.html#sentence_transformers.losses.GISTEmbedLoss "sentence_transformers.losses.GISTEmbedLoss")
      >
      > - [[`CachedGISTEmbedLoss`]](losses.html#sentence_transformers.losses.CachedGISTEmbedLoss "sentence_transformers.losses.CachedGISTEmbedLoss")
      > :::

    - [`BatchSamplers.GROUP_BY_LABEL`]: Uses [[`GroupByLabelBatchSampler`]](#sentence_transformers.sampler.GroupByLabelBatchSampler "sentence_transformers.sampler.GroupByLabelBatchSampler"), ensuring that each batch has 2+ samples from the same label. Recommended for losses that require multiple samples from the same label, such as:

      > ::: 
      > - [[`BatchAllTripletLoss`]](losses.html#sentence_transformers.losses.BatchAllTripletLoss "sentence_transformers.losses.BatchAllTripletLoss")
      >
      > - [[`BatchHardSoftMarginTripletLoss`]](losses.html#sentence_transformers.losses.BatchHardSoftMarginTripletLoss "sentence_transformers.losses.BatchHardSoftMarginTripletLoss")
      >
      > - [[`BatchHardTripletLoss`]](losses.html#sentence_transformers.losses.BatchHardTripletLoss "sentence_transformers.losses.BatchHardTripletLoss")
      >
      > - [[`BatchSemiHardTripletLoss`]](losses.html#sentence_transformers.losses.BatchSemiHardTripletLoss "sentence_transformers.losses.BatchSemiHardTripletLoss")
      > :::

    If you want to use a custom batch sampler, then you can subclass [[`DefaultBatchSampler`]](#sentence_transformers.sampler.DefaultBatchSampler "sentence_transformers.sampler.DefaultBatchSampler") and pass the class (not an instance) to the [`batch_sampler`] argument in [[`SentenceTransformerTrainingArguments`]](training_args.html#sentence_transformers.training_args.SentenceTransformerTrainingArguments "sentence_transformers.training_args.SentenceTransformerTrainingArguments") (or [[`CrossEncoderTrainingArguments`]](../cross_encoder/training_args.html#sentence_transformers.cross_encoder.training_args.CrossEncoderTrainingArguments "sentence_transformers.cross_encoder.training_args.CrossEncoderTrainingArguments"), etc.). Alternatively, you can pass a function that accepts [`dataset`], [`batch_size`], [`drop_last`], [`valid_label_columns`], [`generator`], and [`seed`] and returns a [[`DefaultBatchSampler`]](#sentence_transformers.sampler.DefaultBatchSampler "sentence_transformers.sampler.DefaultBatchSampler") instance.

    Usage:

    :   :::: 
        ::: highlight
            from sentence_transformers import SentenceTransformer, SentenceTransformerTrainer, SentenceTransformerTrainingArguments
            from sentence_transformers.training_args import BatchSamplers
            from sentence_transformers.losses import MultipleNegativesRankingLoss
            from datasets import Dataset

            model = SentenceTransformer("microsoft/mpnet-base")
            train_dataset = Dataset.from_dict()
            loss = MultipleNegativesRankingLoss(model)
            args = SentenceTransformerTrainingArguments(
                output_dir="checkpoints",
                batch_sampler=BatchSamplers.NO_DUPLICATES,
            )
            trainer = SentenceTransformerTrainer(
                model=model,
                args=args,
                train_dataset=train_dataset,
                loss=loss,
            )
            trainer.train()
        :::
        ::::

<!-- -->

*[class][ ]*[[sentence_transformers.sampler.]][[DefaultBatchSampler]][(]*[[dataset]][[:]][ ][[Dataset]]*, *[[batch_size]][[:]][ ][[int]]*, *[[drop_last]][[:]][ ][[bool]]*, *[[valid_label_columns]][[:]][ ][[list][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[generator]][[:]][ ][[[Generator]](https://docs.pytorch.org/docs/stable/generated/torch.Generator.html#torch.Generator "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[seed]][[:]][ ][[int]][ ][[=]][ ][[0]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\sampler.py#L35-L66)[ïƒ?](#sentence_transformers.sampler.DefaultBatchSampler "Link to this definition")

:   This sampler is the default batch sampler used in the SentenceTransformer library. It is equivalent to the PyTorch BatchSampler.

    Parameters[:]

    :   - **sampler** (*Sampler* *or* *Iterable*) â€" The sampler used for sampling elements from the dataset, such as SubsetRandomSampler.

        - **batch_size** (*int*) â€" Number of samples per batch.

        - **drop_last** (*bool*) â€" If True, drop the last incomplete batch if the dataset size is not divisible by the batch size.

        - **valid_label_columns** (*List\[str\],* *optional*) â€" List of column names to check for labels. The first column name from [`valid_label_columns`] found in the dataset will be used as the label column.

        - **generator** ([*torch.Generator*](https://docs.pytorch.org/docs/stable/generated/torch.Generator.html#torch.Generator "(in PyTorch v2.9)")*,* *optional*) â€" Optional random number generator for shuffling the indices.

        - **seed** (*int*) â€" Seed for the random number generator to ensure reproducibility. Defaults to 0.

<!-- -->

*[class][ ]*[[sentence_transformers.sampler.]][[NoDuplicatesBatchSampler]][(]*[[dataset]][[:]][ ][[Dataset]]*, *[[batch_size]][[:]][ ][[int]]*, *[[drop_last]][[:]][ ][[bool]]*, *[[valid_label_columns]][[:]][ ][[list][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[generator]][[:]][ ][[[Generator]](https://docs.pytorch.org/docs/stable/generated/torch.Generator.html#torch.Generator "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[seed]][[:]][ ][[int]][ ][[=]][ ][[0]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\sampler.py#L156-L244)[ïƒ?](#sentence_transformers.sampler.NoDuplicatesBatchSampler "Link to this definition")

:   This sampler creates batches such that each batch contains samples where the values are unique, even across columns. This is useful when losses consider other samples in a batch to be in-batch negatives, and you want to ensure that the negatives are not duplicates of the anchor/positive sample.

    Recommended for:

    :   - [[`MultipleNegativesRankingLoss`]](losses.html#sentence_transformers.losses.MultipleNegativesRankingLoss "sentence_transformers.losses.MultipleNegativesRankingLoss")

        - [[`CachedMultipleNegativesRankingLoss`]](losses.html#sentence_transformers.losses.CachedMultipleNegativesRankingLoss "sentence_transformers.losses.CachedMultipleNegativesRankingLoss")

        - [[`MultipleNegativesSymmetricRankingLoss`]](losses.html#sentence_transformers.losses.MultipleNegativesSymmetricRankingLoss "sentence_transformers.losses.MultipleNegativesSymmetricRankingLoss")

        - [[`CachedMultipleNegativesSymmetricRankingLoss`]](losses.html#sentence_transformers.losses.CachedMultipleNegativesSymmetricRankingLoss "sentence_transformers.losses.CachedMultipleNegativesSymmetricRankingLoss")

        - [[`MegaBatchMarginLoss`]](losses.html#sentence_transformers.losses.MegaBatchMarginLoss "sentence_transformers.losses.MegaBatchMarginLoss")

        - [[`GISTEmbedLoss`]](losses.html#sentence_transformers.losses.GISTEmbedLoss "sentence_transformers.losses.GISTEmbedLoss")

        - [[`CachedGISTEmbedLoss`]](losses.html#sentence_transformers.losses.CachedGISTEmbedLoss "sentence_transformers.losses.CachedGISTEmbedLoss")

    Parameters[:]

    :   - **dataset** (*Dataset*) â€" The dataset to sample from.

        - **batch_size** (*int*) â€" Number of samples per batch.

        - **drop_last** (*bool*) â€" If True, drop the last incomplete batch if the dataset size is not divisible by the batch size.

        - **valid_label_columns** (*List\[str\],* *optional*) â€" List of column names to check for labels. The first column name from [`valid_label_columns`] found in the dataset will be used as the label column.

        - **generator** ([*torch.Generator*](https://docs.pytorch.org/docs/stable/generated/torch.Generator.html#torch.Generator "(in PyTorch v2.9)")*,* *optional*) â€" Optional random number generator for shuffling the indices.

        - **seed** (*int*) â€" Seed for the random number generator to ensure reproducibility. Defaults to 0.

<!-- -->

*[class][ ]*[[sentence_transformers.sampler.]][[GroupByLabelBatchSampler]][(]*[[dataset]][[:]][ ][[Dataset]]*, *[[batch_size]][[:]][ ][[int]]*, *[[drop_last]][[:]][ ][[bool]]*, *[[valid_label_columns]][[:]][ ][[list][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[generator]][[:]][ ][[[Generator]](https://docs.pytorch.org/docs/stable/generated/torch.Generator.html#torch.Generator "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[seed]][[:]][ ][[int]][ ][[=]][ ][[0]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\sampler.py#L69-L153)[ïƒ?](#sentence_transformers.sampler.GroupByLabelBatchSampler "Link to this definition")

:   This sampler groups samples by their labels and aims to create batches such that each batch contains samples where the labels are as homogeneous as possible. This sampler is meant to be used alongside the [`Batch...TripletLoss`] classes, which require that each batch contains at least 2 examples per label class.

    Recommended for:

    :   - [[`BatchAllTripletLoss`]](losses.html#sentence_transformers.losses.BatchAllTripletLoss "sentence_transformers.losses.BatchAllTripletLoss")

        - [[`BatchHardSoftMarginTripletLoss`]](losses.html#sentence_transformers.losses.BatchHardSoftMarginTripletLoss "sentence_transformers.losses.BatchHardSoftMarginTripletLoss")

        - [[`BatchHardTripletLoss`]](losses.html#sentence_transformers.losses.BatchHardTripletLoss "sentence_transformers.losses.BatchHardTripletLoss")

        - [[`BatchSemiHardTripletLoss`]](losses.html#sentence_transformers.losses.BatchSemiHardTripletLoss "sentence_transformers.losses.BatchSemiHardTripletLoss")

    Parameters[:]

    :   - **dataset** (*Dataset*) â€" The dataset to sample from.

        - **batch_size** (*int*) â€" Number of samples per batch. Must be divisible by 2.

        - **drop_last** (*bool*) â€" If True, drop the last incomplete batch if the dataset size is not divisible by the batch size.

        - **valid_label_columns** (*List\[str\],* *optional*) â€" List of column names to check for labels. The first column name from [`valid_label_columns`] found in the dataset will be used as the label column.

        - **generator** ([*torch.Generator*](https://docs.pytorch.org/docs/stable/generated/torch.Generator.html#torch.Generator "(in PyTorch v2.9)")*,* *optional*) â€" Optional random number generator for shuffling the indices.

        - **seed** (*int*) â€" Seed for the random number generator to ensure reproducibility. Defaults to 0.

## MultiDatasetBatchSamplers[ïƒ?](#multidatasetbatchsamplers "Link to this heading")

*[class][ ]*[[sentence_transformers.training_args.]][[MultiDatasetBatchSamplers]][(]*[[value]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\training_args.py#L85-L153)[ïƒ?](#sentence_transformers.training_args.MultiDatasetBatchSamplers "Link to this definition")

:   Stores the acceptable string identifiers for multi-dataset batch samplers.

    The multi-dataset batch sampler is responsible for determining in what order batches are sampled from multiple datasets during training. Valid options are:

    - [`MultiDatasetBatchSamplers.ROUND_ROBIN`]: Uses [[`RoundRobinBatchSampler`]](#sentence_transformers.sampler.RoundRobinBatchSampler "sentence_transformers.sampler.RoundRobinBatchSampler"), which uses round-robin sampling from each dataset until one is exhausted. With this strategy, itâ€™s likely that not all samples from each dataset are used, but each dataset is sampled from equally.

    - [`MultiDatasetBatchSamplers.PROPORTIONAL`]: **\[default\]** Uses [[`ProportionalBatchSampler`]](#sentence_transformers.sampler.ProportionalBatchSampler "sentence_transformers.sampler.ProportionalBatchSampler"), which samples from each dataset in proportion to its size. With this strategy, all samples from each dataset are used and larger datasets are sampled from more frequently.

    If you want to use a custom multi-dataset batch sampler, then you can subclass [[`MultiDatasetDefaultBatchSampler`]](#sentence_transformers.sampler.MultiDatasetDefaultBatchSampler "sentence_transformers.sampler.MultiDatasetDefaultBatchSampler") and pass the class (not an instance) to the [`multi_dataset_batch_sampler`] argument in [[`SentenceTransformerTrainingArguments`]](training_args.html#sentence_transformers.training_args.SentenceTransformerTrainingArguments "sentence_transformers.training_args.SentenceTransformerTrainingArguments"). (or [[`CrossEncoderTrainingArguments`]](../cross_encoder/training_args.html#sentence_transformers.cross_encoder.training_args.CrossEncoderTrainingArguments "sentence_transformers.cross_encoder.training_args.CrossEncoderTrainingArguments"), etc.). Alternatively, you can pass a function that accepts [`dataset`] (a [[`ConcatDataset`]](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.ConcatDataset "(in PyTorch v2.9)")), [`batch_samplers`] (i.e. a list of batch sampler for each of the datasets in the [[`ConcatDataset`]](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.ConcatDataset "(in PyTorch v2.9)")), [`generator`], and [`seed`] and returns a [[`MultiDatasetDefaultBatchSampler`]](#sentence_transformers.sampler.MultiDatasetDefaultBatchSampler "sentence_transformers.sampler.MultiDatasetDefaultBatchSampler") instance.

    Usage:

    :   :::: 
        ::: highlight
            from sentence_transformers import SentenceTransformer, SentenceTransformerTrainer, SentenceTransformerTrainingArguments
            from sentence_transformers.training_args import MultiDatasetBatchSamplers
            from sentence_transformers.losses import CoSENTLoss
            from datasets import Dataset, DatasetDict

            model = SentenceTransformer("microsoft/mpnet-base")
            train_general = Dataset.from_dict()
            train_medical = Dataset.from_dict()
            train_legal = Dataset.from_dict()
            train_dataset = DatasetDict()

            loss = CoSENTLoss(model)
            args = SentenceTransformerTrainingArguments(
                output_dir="checkpoints",
                multi_dataset_batch_sampler=MultiDatasetBatchSamplers.PROPORTIONAL,
            )
            trainer = SentenceTransformerTrainer(
                model=model,
                args=args,
                train_dataset=train_dataset,
                loss=loss,
            )
            trainer.train()
        :::
        ::::

<!-- -->

*[class][ ]*[[sentence_transformers.sampler.]][[MultiDatasetDefaultBatchSampler]][(]*[[dataset]][[:]][ ][[[ConcatDataset]](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.ConcatDataset "(in PyTorch v2.9)")]*, *[[batch_samplers]][[:]][ ][[list][[\[]][[BatchSampler]](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.BatchSampler "(in PyTorch v2.9)")[[\]]]]*, *[[generator]][[:]][ ][[[Generator]](https://docs.pytorch.org/docs/stable/generated/torch.Generator.html#torch.Generator "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[seed]][[:]][ ][[int]][ ][[=]][ ][[0]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\sampler.py#L247-L283)[ïƒ?](#sentence_transformers.sampler.MultiDatasetDefaultBatchSampler "Link to this definition")

:   Abstract base batch sampler that yields batches from multiple batch samplers. This class must be subclassed to implement specific sampling strategies, and cannot be used directly.

    Parameters[:]

    :   - **dataset** (*ConcatDataset*) â€" A concatenation of multiple datasets.

        - **batch_samplers** (*List\[BatchSampler\]*) â€" A list of batch samplers, one for each dataset in the ConcatDataset.

        - **generator** ([*torch.Generator*](https://docs.pytorch.org/docs/stable/generated/torch.Generator.html#torch.Generator "(in PyTorch v2.9)")*,* *optional*) â€" A generator for reproducible sampling. Defaults to None.

        - **seed** (*int*) â€" Seed for the random number generator to ensure reproducibility. Defaults to 0.

<!-- -->

*[class][ ]*[[sentence_transformers.sampler.]][[RoundRobinBatchSampler]][(]*[[dataset]][[:]][ ][[[ConcatDataset]](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.ConcatDataset "(in PyTorch v2.9)")]*, *[[batch_samplers]][[:]][ ][[list][[\[]][[BatchSampler]](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.BatchSampler "(in PyTorch v2.9)")[[\]]]]*, *[[generator]][[:]][ ][[[Generator]](https://docs.pytorch.org/docs/stable/generated/torch.Generator.html#torch.Generator "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[seed]][[:]][ ][[int]][ ][[=]][ ][[0]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\sampler.py#L286-L316)[ïƒ?](#sentence_transformers.sampler.RoundRobinBatchSampler "Link to this definition")

:   Batch sampler that yields batches in a round-robin fashion from multiple batch samplers, until one is exhausted. With this sampler, itâ€™s unlikely that all samples from each dataset are used, but we do ensure that each dataset is sampled from equally.

    Parameters[:]

    :   - **dataset** (*ConcatDataset*) â€" A concatenation of multiple datasets.

        - **batch_samplers** (*List\[BatchSampler\]*) â€" A list of batch samplers, one for each dataset in the ConcatDataset.

        - **generator** ([*torch.Generator*](https://docs.pytorch.org/docs/stable/generated/torch.Generator.html#torch.Generator "(in PyTorch v2.9)")*,* *optional*) â€" A generator for reproducible sampling. Defaults to None.

        - **seed** (*int*) â€" Seed for the random number generator to ensure reproducibility. Defaults to 0.

<!-- -->

*[class][ ]*[[sentence_transformers.sampler.]][[ProportionalBatchSampler]][(]*[[dataset]][[:]][ ][[[ConcatDataset]](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.ConcatDataset "(in PyTorch v2.9)")]*, *[[batch_samplers]][[:]][ ][[list][[\[]][[BatchSampler]](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.BatchSampler "(in PyTorch v2.9)")[[\]]]]*, *[[generator]][[:]][ ][[[Generator]](https://docs.pytorch.org/docs/stable/generated/torch.Generator.html#torch.Generator "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[seed]][[:]][ ][[int]][ ][[=]][ ][[0]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\sampler.py#L319-L350)[ïƒ?](#sentence_transformers.sampler.ProportionalBatchSampler "Link to this definition")

:   Batch sampler that samples from each dataset in proportion to its size, until all are exhausted simultaneously. With this sampler, all samples from each dataset are used and larger datasets are sampled from more frequently.

    Parameters[:]

    :   - **dataset** (*ConcatDataset*) â€" A concatenation of multiple datasets.

        - **batch_samplers** (*List\[BatchSampler\]*) â€" A list of batch samplers, one for each dataset in the ConcatDataset.

        - **generator** ([*torch.Generator*](https://docs.pytorch.org/docs/stable/generated/torch.Generator.html#torch.Generator "(in PyTorch v2.9)")*,* *optional*) â€" A generator for reproducible sampling. Defaults to None.

        - **seed** (*int*) â€" Seed for the random number generator to ensure reproducibility. Defaults to 0.