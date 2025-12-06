# Source: https://www.sbert.net/docs/cross_encoder/training_overview.html

# Training Overview[ïƒ?](#training-overview "Link to this heading")

## Why Finetune?[ïƒ?](#why-finetune "Link to this heading")

Cross Encoder models are very often used as 2nd stage rerankers in a [[Retrieve and Rerank]](../../examples/sentence_transformer/applications/retrieve_rerank/README.html) search stack. In such a situation, the Cross Encoder reranks the top X candidates from the retriever (which can be a [[Sentence Transformer model]](../sentence_transformer/usage/usage.html)). To avoid the reranker model reducing the performance on your use case, finetuning it can be crucial. Rerankers always have just 1 output label.

Beyond that, Cross Encoder models can also be used as pair classifiers. For example, a model trained on Natural Language Inference data can be used to classify pairs of texts as â€œcontradictionâ€?, â€œentailmentâ€?, and â€œneutralâ€?. Pair Classifiers generally have more than 1 output label.

See [[**Training Examples**]](training/examples.html) for numerous training scripts for common real-world applications that you can adopt.

## Training Components[ïƒ?](#training-components "Link to this heading")

Training Cross Encoder models involves between 4 to 6 components, just like [[training Sentence Transformer models]](../sentence_transformer/training_overview.html):

[](#model)

Model

Learn how to initialize the **model** for training. [](#dataset)

Dataset

Learn how to prepare the **data** for training. [](#loss-function)

Loss Function

Learn how to prepare and choose a **loss** function. [](#training-arguments)

Training Arguments

Learn which **training arguments** are useful. [](#evaluator)

Evaluator

Learn how to **evaluate** during and after training. [](#trainer)

Trainer

Learn how to start the **training** process.

## Model[ïƒ?](#model "Link to this heading")

Cross Encoder models are initialized by loading a pretrained [transformers](https://huggingface.co/docs/transformers) model using a sequence classification head. If the model itself does not have such a head, then it will be added automatically. Consequently, initializing a Cross Encoder model is rather simple:

Documentation

- [[`sentence_transformers.cross_encoder.CrossEncoder`]](../package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")

    from sentence_transformers import CrossEncoder

    # This model already has a sequence classification head
    model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")
    # And this model does not, so it will be added automatically
    model = CrossEncoder("google-bert/bert-base-uncased")

Tip

You can find pretrained reranker models in the [Cross Encoder \> Pretrained Models](pretrained_models.html) documentation.

For other models, the strongest pretrained models are often â€œencoder modelsâ€?, i.e. models that are trained to produce a meaningful token embedding for inputs. You can find strong candidates here:

- [fill-mask models](https://huggingface.co/models?pipeline_tag=fill-mask) - trained for token embeddings

- [sentence similarity models](https://huggingface.co/models?pipeline_tag=sentence-similarity) - trained for text embeddings

- [feature-extraction models](https://huggingface.co/models?pipeline_tag=feature-extraction) - trained for text embeddings

Consider looking for base models that are designed on your language and/or domain of interest. For example, [klue/bert-base](https://huggingface.co/klue/bert-base) will work much better than [google-bert/bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased) for Korean.

## Dataset[ïƒ?](#dataset "Link to this heading")

The [`CrossEncoderTrainer`] trains and evaluates using [[`datasets.Dataset`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)") (one dataset) or [[`datasets.DatasetDict`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.DatasetDict "(in datasets vmain)") instances (multiple datasets, see also [Multi-dataset training](#multi-dataset-training)).

Data on ðŸ¤--- Hugging Face Hub

If you want to load data from the [Hugging Face Datasets](https://huggingface.co/datasets), then you should use [[`datasets.load_dataset()`]](https://huggingface.co/docs/datasets/main/en/package_reference/loading_methods#datasets.load_dataset "(in datasets vmain)"):

    from datasets import load_dataset

    train_dataset = load_dataset("sentence-transformers/all-nli", "pair-class", split="train")
    eval_dataset = load_dataset("sentence-transformers/all-nli", "pair-class", split="dev")

    print(train_dataset)
    """
    Dataset()
    """

Some datasets (including [sentence-transformers/all-nli](https://huggingface.co/datasets/sentence-transformers/all-nli)) require you to provide a â€œsubsetâ€? alongside the dataset name. [`sentence-transformers/all-nli`] has 4 subsets, each with different data formats: [pair](https://huggingface.co/datasets/sentence-transformers/all-nli/viewer/pair), [pair-class](https://huggingface.co/datasets/sentence-transformers/all-nli/viewer/pair-class), [pair-score](https://huggingface.co/datasets/sentence-transformers/all-nli/viewer/pair-score), [triplet](https://huggingface.co/datasets/sentence-transformers/all-nli/viewer/triplet).

Note

Many Hugging Face datasets that work out of the box with Sentence Transformers have been tagged with [`sentence-transformers`], allowing you to easily find them by browsing to [https://huggingface.co/datasets?other=sentence-transformers](https://huggingface.co/datasets?other=sentence-transformers). We strongly recommend that you browse these datasets to find training datasets that might be useful for your tasks.

Local Data (CSV, JSON, Parquet, Arrow, SQL)

If you have local data in common file-formats, then you can load this data easily using [[`datasets.load_dataset()`]](https://huggingface.co/docs/datasets/main/en/package_reference/loading_methods#datasets.load_dataset "(in datasets vmain)"):

    from datasets import load_dataset

    dataset = load_dataset("csv", data_files="my_file.csv")

or:

    from datasets import load_dataset

    dataset = load_dataset("json", data_files="my_file.json")

Local Data that requires pre-processing

If you have local data that requires some extra pre-processing, my recommendation is to initialize your dataset using [[`datasets.Dataset.from_dict()`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset.from_dict "(in datasets vmain)") and a dictionary of lists, like so:

    from datasets import Dataset

    anchors = []
    positives = []
    # Open a file, do preprocessing, filtering, cleaning, etc.
    # and append to the lists

    dataset = Dataset.from_dict()

Each key from the dictionary will become a column in the resulting dataset.

### Dataset Format[ïƒ?](#dataset-format "Link to this heading")

It is important that your dataset format matches your loss function (or that you choose a loss function that matches your dataset format and model). Verifying whether a dataset format and model work with a loss function involves three steps:

1.  All columns not named â€œlabelâ€?, â€œlabelsâ€?, â€œscoreâ€?, or â€œscoresâ€? are considered *Inputs* according to the [Loss Overview](loss_overview.html) table. The number of remaining columns must match the number of valid inputs for your chosen loss. The names of these columns are **irrelevant**, only the **order matters**.

2.  If your loss function requires a *Label* according to the [Loss Overview](loss_overview.html) table, then your dataset must have a **column named â€œlabelâ€?, â€œlabelsâ€?, â€œscoreâ€?, or â€œscoresâ€?**. This column is automatically taken as the label.

3.  The number of model output labels matches what is required for the loss according to [Loss Overview](loss_overview.html) table.

For example, given a dataset with columns [`["text1",`]` `[`"text2",`]` `[`"label"]`] where the â€œlabelâ€? column has float similarity score ranging from 0 to 1 and a model outputting 1 label, we can use it with [[`BinaryCrossEntropyLoss`]](../package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss "sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss") because:

1.  the dataset has a â€œlabelâ€? column as is required for this loss function.

2.  the dataset has 2 non-label columns, exactly the amount required by this loss functions.

3.  the model has 1 output label, exactly as required by this loss function.

Be sure to re-order your dataset columns with [[`Dataset.select_columns`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset.select_columns "(in datasets vmain)") if your columns are not ordered correctly. For example, if your dataset has [`["good_answer",`]` `[`"bad_answer",`]` `[`"question"]`] as columns, then this dataset can technically be used with a loss that requires (anchor, positive, negative) triplets, but the [`good_answer`] column will be taken as the anchor, [`bad_answer`] as the positive, and [`question`] as the negative.

Additionally, if your dataset has extraneous columns (e.g. sample_id, metadata, source, type), you should remove these with [[`Dataset.remove_columns`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset.remove_columns "(in datasets vmain)") as they will be used as inputs otherwise. You can also use [[`Dataset.select_columns`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset.select_columns "(in datasets vmain)") to keep only the desired columns.

### Hard Negatives Mining[ïƒ?](#hard-negatives-mining "Link to this heading")

The success of training CrossEncoder models often depends on the quality of the *negatives*, i.e. the passages for which the query-negative score should be low. Negatives can be divided into two types:

- **Soft negatives**: passages that are completely unrelated.

- **Hard negatives**: passages that seem like they might be relevant for the query, but are not.

A concise example is:

- **Query**: Where was Apple founded?

- **Soft Negative**: The Cache River Bridge is a Parker pony truss that spans the Cache River between Walnut Ridge and Paragould, Arkansas.

- **Hard Negative**: The Fuji apple is an apple cultivar developed in the late 1930s, and brought to market in 1962.

The strongest CrossEncoder models are generally trained to recognize hard negatives, and so itâ€™s valuable to be able to â€œmineâ€? hard negatives. Sentence Transformers supports a strong [[`mine_hard_negatives()`]](../package_reference/util.html#sentence_transformers.util.mine_hard_negatives "sentence_transformers.util.mine_hard_negatives") function that can assist, given a dataset of query-answer pairs:

Documentation

- [sentence-transformers/gooaq](https://huggingface.co/datasets/sentence-transformers/gooaq)

- [sentence-transformers/static-retrieval-mrl-en-v1](https://huggingface.co/sentence-transformers/static-retrieval-mrl-en-v1)

- [[`SentenceTransformer`]](../package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")

- [[`mine_hard_negatives()`]](../package_reference/util.html#sentence_transformers.util.mine_hard_negatives "sentence_transformers.util.mine_hard_negatives")

    from datasets import load_dataset
    from sentence_transformers import SentenceTransformer
    from sentence_transformers.util import mine_hard_negatives

    # Load the GooAQ dataset: https://huggingface.co/datasets/sentence-transformers/gooaq
    train_dataset = load_dataset("sentence-transformers/gooaq", split=f"train").select(range(100_000))
    print(train_dataset)

    # Mine hard negatives using a very efficient embedding model
    embedding_model = SentenceTransformer("sentence-transformers/static-retrieval-mrl-en-v1", device="cpu")
    hard_train_dataset = mine_hard_negatives(
        train_dataset,
        embedding_model,
        num_negatives=5,  # How many negatives per question-answer pair
        range_min=10,  # Skip the x most similar samples
        range_max=100,  # Consider only the x most similar samples
        max_score=0.8,  # Only consider samples with a similarity score of at most x
        absolute_margin=0.1,  # Anchor-negative similarity is at least x lower than anchor-positive similarity
        relative_margin=0.1,  # Anchor-negative similarity is at most 1-x times the anchor-positive similarity, e.g. 90%
        sampling_strategy="top",  # Sample the top negatives from the range
        batch_size=4096,  # Use a batch size of 4096 for the embedding model
        output_format="labeled-pair",  # The output format is (query, passage, label), as required by BinaryCrossEntropyLoss
        use_faiss=True,  # Using FAISS is recommended to keep memory usage low (pip install faiss-gpu or pip install faiss-cpu)
    )
    print(hard_train_dataset)
    print(hard_train_dataset[1])

Click to see the outputs of this script.

    Dataset()

    Batches: 100%|ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 22/22 [00:01<00:00, 12.74it/s]
    Batches: 100%|ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 25/25 [00:00<00:00, 37.50it/s]
    Querying FAISS index: 100%|âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ| 7/7 [00:18<00:00,  2.66s/it]
    Metric       Positive       Negative     Difference
    Count         100,000        436,925
    Mean           0.5882         0.4040         0.2157
    Median         0.5989         0.4024         0.1836
    Std            0.1425         0.0905         0.1013
    Min           -0.0514         0.1405         0.1014
    25%            0.4993         0.3377         0.1352
    50%            0.5989         0.4024         0.1836
    75%            0.6888         0.4681         0.2699
    Max            0.9748         0.7486         0.7545
    Skipped 2,420,871 potential negatives (23.97%) due to the absolute_margin of 0.1.
    Skipped 43 potential negatives (0.00%) due to the max_score of 0.8.
    Could not find enough negatives for 63075 samples (12.62%). Consider adjusting the range_max, range_min, absolute_margin, relative_margin and max_score parameters if you'd like to find more valid negatives.
    Dataset()

    

\

## Loss Function[ïƒ?](#loss-function "Link to this heading")

Loss functions quantify how well a model performs for a given batch of data, allowing an optimizer to update the model weights to produce more favourable (i.e., lower) loss values. This is the core of the training process.

Sadly, there is no single loss function that works best for all use-cases. Instead, which loss function to use greatly depends on your available data and on your target task. See [Dataset Format](#dataset-format) to learn what datasets are valid for which loss functions. Additionally, the [[Loss Overview]](loss_overview.html) will be your best friend to learn about the options.

Most loss functions can be initialized with just the [[`CrossEncoder`]](../package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder") that youâ€™re training, alongside some optional parameters, e.g.:

Documentation

- [[`sentence_transformers.cross_encoder.losses.MultipleNegativesRankingLoss`]](../package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.MultipleNegativesRankingLoss "sentence_transformers.cross_encoder.losses.MultipleNegativesRankingLoss")

- [Losses API Reference](../package_reference/cross_encoder/losses.html)

- [Loss Overview](loss_overview.html)

    from datasets import load_dataset
    from sentence_transformers import CrossEncoder
    from sentence_transformers.cross_encoder.losses import MultipleNegativesRankingLoss

    # Load a model to train/finetune
    model = CrossEncoder("xlm-roberta-base", num_labels=1) # num_labels=1 is for rerankers

    # Initialize the MultipleNegativesRankingLoss
    # This loss requires pairs of related texts or triplets
    loss = MultipleNegativesRankingLoss(model)

    # Load an example training dataset that works with our loss function:
    train_dataset = load_dataset("sentence-transformers/gooaq", split="train")

## Training Arguments[ïƒ?](#training-arguments "Link to this heading")

The [[`CrossEncoderTrainingArguments`]](../package_reference/cross_encoder/training_args.html#sentence_transformers.cross_encoder.training_args.CrossEncoderTrainingArguments "sentence_transformers.cross_encoder.training_args.CrossEncoderTrainingArguments") class can be used to specify parameters for influencing training performance as well as defining the tracking/debugging parameters. Although it is optional, it is heavily recommended to experiment with the various useful arguments.

Key Training Arguments for improving training performance

[`learning_rate`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.learning_rate) [`lr_scheduler_type`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.lr_scheduler_type) [`warmup_ratio`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.warmup_ratio) [`num_train_epochs`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.num_train_epochs) [`max_steps`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.max_steps) [`per_device_train_batch_size`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.per_device_train_batch_size) [`per_device_eval_batch_size`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.per_device_eval_batch_size) [`auto_find_batch_size`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.auto_find_batch_size%20) [`fp16`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.fp16) [`bf16`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.bf16) [`load_best_model_at_end`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.load_best_model_at_end) [`metric_for_best_model`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.metric_for_best_model) [`gradient_accumulation_steps`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.gradient_accumulation_steps) [`gradient_checkpointing`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.gradient_checkpointing) [`eval_accumulation_steps`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.eval_accumulation_steps) [`optim`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.optim) [`dataloader_num_workers`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.dataloader_num_workers) [`dataloader_prefetch_factor`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.dataloader_prefetch_factor) [`batch_sampler`](../package_reference/cross_encoder/training_args.html#sentence_transformers.cross_encoder.training_args.SentenceTransformerTrainingArguments) [`multi_dataset_batch_sampler`](../package_reference/cross_encoder/training_args.html#sentence_transformers.cross_encoder.training_args.SentenceTransformerTrainingArguments) [`learning_rate_mapping`](../package_reference/cross_encoder/training_args.html#sentence_transformers.cross_encoder.training_args.SentenceTransformerTrainingArguments)

\

Key Training Arguments for observing training performance

[`eval_strategy`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.eval_strategy) [`eval_steps`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.eval_steps) [`save_strategy`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.save_strategy) [`save_steps`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.save_steps) [`save_total_limit`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.save_total_limit) [`report_to`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.report_to) [`run_name`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.run_name) [`log_level`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.log_level) [`logging_steps`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.logging_steps) [`push_to_hub`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.push_to_hub) [`hub_model_id`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.hub_model_id) [`hub_strategy`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.hub_strategy) [`hub_private_repo`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.hub_private_repo)

\

Here is an example of how [[`CrossEncoderTrainingArguments`]](../package_reference/cross_encoder/training_args.html#sentence_transformers.cross_encoder.training_args.CrossEncoderTrainingArguments "sentence_transformers.cross_encoder.training_args.CrossEncoderTrainingArguments") can be initialized:

    from sentence_transformers.cross_encoder import CrossEncoderTrainingArguments

    args = CrossEncoderTrainingArguments(
        # Required parameter:
        output_dir="models/reranker-MiniLM-msmarco-v1",
        # Optional training parameters:
        num_train_epochs=1,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        learning_rate=2e-5,
        warmup_ratio=0.1,
        fp16=True,  # Set to False if you get an error that your GPU can't run on FP16
        bf16=False,  # Set to True if you have a GPU that supports BF16
        batch_sampler=BatchSamplers.NO_DUPLICATES,  # losses that use "in-batch negatives" benefit from no duplicates
        # Optional tracking/debugging parameters:
        eval_strategy="steps",
        eval_steps=100,
        save_strategy="steps",
        save_steps=100,
        save_total_limit=2,
        logging_steps=100,
        run_name="reranker-MiniLM-msmarco-v1",  # Will be used in W&B if `wandb` is installed
    )

## Evaluator[ïƒ?](#evaluator "Link to this heading")

You can provide the [[`CrossEncoderTrainer`]](../package_reference/cross_encoder/trainer.html#sentence_transformers.cross_encoder.trainer.CrossEncoderTrainer "sentence_transformers.cross_encoder.trainer.CrossEncoderTrainer") with an [`eval_dataset`] to get the evaluation loss during training, but it may be useful to get more concrete metrics during training, too. For this, you can use evaluators to assess the modelâ€™s performance with useful metrics before, during, or after training. You can use both an [`eval_dataset`] and an evaluator, one or the other, or neither. They evaluate based on the [`eval_strategy`] and [`eval_steps`] [Training Arguments](#training-arguments).

Here are the implemented Evaluators that come with Sentence Transformers for Cross Encoder models:

  Evaluator                                                                                                                                                                                                                                                                                                                                                Required Data
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [[`CrossEncoderClassificationEvaluator`]](../package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderClassificationEvaluator "sentence_transformers.cross_encoder.evaluation.CrossEncoderClassificationEvaluator")   Pairs with class labels (binary or multiclass).
  [[`CrossEncoderCorrelationEvaluator`]](../package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderCorrelationEvaluator "sentence_transformers.cross_encoder.evaluation.CrossEncoderCorrelationEvaluator")            Pairs with similarity scores.
  [[`CrossEncoderNanoBEIREvaluator`]](../package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderNanoBEIREvaluator "sentence_transformers.cross_encoder.evaluation.CrossEncoderNanoBEIREvaluator")                     No data required.
  [[`CrossEncoderRerankingEvaluator`]](../package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderRerankingEvaluator "sentence_transformers.cross_encoder.evaluation.CrossEncoderRerankingEvaluator")                  List of [`]` `[`'...',`]` `[`'positive':`]` `[`[...],`]` `[`'negative':`]` `[`[...]}`] dictionaries. Negatives can be mined with [[`mine_hard_negatives()`]](../package_reference/util.html#sentence_transformers.util.mine_hard_negatives "sentence_transformers.util.mine_hard_negatives").

Additionally, [[`SequentialEvaluator`]](../package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.SequentialEvaluator "sentence_transformers.evaluation.SequentialEvaluator") should be used to combine multiple evaluators into one Evaluator that can be passed to the [[`CrossEncoderTrainer`]](../package_reference/cross_encoder/trainer.html#sentence_transformers.cross_encoder.trainer.CrossEncoderTrainer "sentence_transformers.cross_encoder.trainer.CrossEncoderTrainer").

Sometimes you donâ€™t have the required evaluation data to prepare one of these evaluators on your own, but you still want to track how well the model performs on some common benchmarks. In that case, you can use these evaluators with data from Hugging Face.

CrossEncoderNanoBEIREvaluator

    from sentence_transformers import CrossEncoder
    from sentence_transformers.cross_encoder.evaluation import CrossEncoderNanoBEIREvaluator

    # Load a model
    model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")

    # Initialize the evaluator. Unlike most other evaluators, this one loads the relevant datasets
    # directly from Hugging Face, so there's no mandatory arguments
    dev_evaluator = CrossEncoderNanoBEIREvaluator()
    # You can run evaluation like so:
    # results = dev_evaluator(model)

CrossEncoderRerankingEvaluator with GooAQ mined negatives

Preparing data for [[`CrossEncoderRerankingEvaluator`]](../package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderRerankingEvaluator "sentence_transformers.cross_encoder.evaluation.CrossEncoderRerankingEvaluator") can be difficult as you need negatives in addition to your query-positive data.

The [[`mine_hard_negatives()`]](../package_reference/util.html#sentence_transformers.util.mine_hard_negatives "sentence_transformers.util.mine_hard_negatives") function has a convenient [`include_positives`] parameter, which can be set to [`True`] to also mine for the positive texts. When supplied as [`documents`] (which have to be 1. ranked and 2. contain positives) to [[`CrossEncoderRerankingEvaluator`]](../package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderRerankingEvaluator "sentence_transformers.cross_encoder.evaluation.CrossEncoderRerankingEvaluator"), the evaluator will not just evaluate the reranking performance of the CrossEncoder, but also the original rankings by the embedding model used for mining.

For example:

    CrossEncoderRerankingEvaluator: Evaluating the model on the gooaq-dev dataset:
    Queries:  1000     Positives: Min 1.0, Mean 1.0, Max 1.0   Negatives: Min 49.0, Mean 49.1, Max 50.0
              Base  -> Reranked
    MAP:      53.28 -> 67.28
    MRR@10:   52.40 -> 66.65
    NDCG@10:  59.12 -> 71.35

Note that by default, if you are using [[`CrossEncoderRerankingEvaluator`]](../package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderRerankingEvaluator "sentence_transformers.cross_encoder.evaluation.CrossEncoderRerankingEvaluator") with [`documents`], the evaluator will rerank with *all* positives, even if they are not in the documents. This is useful for getting a stronger signal out of your evaluator, but does give a slightly unrealistic performance. After all, the maximum performance is now 100, whereas normally its bounded by whether the first-stage retriever actually retrieved the positives.

You can enable the realistic behaviour by setting [`always_rerank_positives=False`] when initializing [[`CrossEncoderRerankingEvaluator`]](../package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderRerankingEvaluator "sentence_transformers.cross_encoder.evaluation.CrossEncoderRerankingEvaluator"). Repeating the same script with this realistic two-stage performance results in:

    CrossEncoderRerankingEvaluator: Evaluating the model on the gooaq-dev dataset:
    Queries:  1000     Positives: Min 1.0, Mean 1.0, Max 1.0   Negatives: Min 49.0, Mean 49.1, Max 50.0
              Base  -> Reranked
    MAP:      53.28 -> 66.12
    MRR@10:   52.40 -> 65.61
    NDCG@10:  59.12 -> 70.10

    from datasets import load_dataset
    from sentence_transformers import SentenceTransformer
    from sentence_transformers.cross_encoder import CrossEncoder
    from sentence_transformers.cross_encoder.evaluation import CrossEncoderRerankingEvaluator
    from sentence_transformers.util import mine_hard_negatives

    # Load a model
    model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")

    # Load the GooAQ dataset: https://huggingface.co/datasets/sentence-transformers/gooaq
    full_dataset = load_dataset("sentence-transformers/gooaq", split=f"train").select(range(100_000))
    dataset_dict = full_dataset.train_test_split(test_size=1_000, seed=12)
    train_dataset = dataset_dict["train"]
    eval_dataset = dataset_dict["test"]
    print(eval_dataset)
    """
    Dataset()
    """

    # Mine hard negatives using a very efficient embedding model
    embedding_model = SentenceTransformer("sentence-transformers/static-retrieval-mrl-en-v1", device="cpu")
    hard_eval_dataset = mine_hard_negatives(
        eval_dataset,
        embedding_model,
        corpus=full_dataset["answer"],  # Use the full dataset as the corpus
        num_negatives=50,  # How many negatives per question-answer pair
        batch_size=4096,  # Use a batch size of 4096 for the embedding model
        output_format="n-tuple",  # The output format is (query, positive, negative1, negative2, ...) for the evaluator
        include_positives=True,  # Key: Include the positive answer in the list of negatives
        use_faiss=True,  # Using FAISS is recommended to keep memory usage low (pip install faiss-gpu or pip install faiss-cpu)
    )
    print(hard_eval_dataset)
    """
    Dataset()
    """

    reranking_evaluator = CrossEncoderRerankingEvaluator(
        samples=[
            
            for sample in hard_eval_dataset
        ],
        batch_size=32,
        name="gooaq-dev",
    )
    # You can run evaluation like so
    results = reranking_evaluator(model)
    """
    CrossEncoderRerankingEvaluator: Evaluating the model on the gooaq-dev dataset:
    Queries:  1000     Positives: Min 1.0, Mean 1.0, Max 1.0   Negatives: Min 49.0, Mean 49.1, Max 50.0
              Base  -> Reranked
    MAP:      53.28 -> 67.28
    MRR@10:   52.40 -> 66.65
    NDCG@10:  59.12 -> 71.35
    """
    # 

CrossEncoderCorrelationEvaluator with STSb

    from datasets import load_dataset
    from sentence_transformers import CrossEncoder
    from sentence_transformers.cross_encoder.evaluation import CrossEncoderCorrelationEvaluator

    # Load a model
    model = CrossEncoder("cross-encoder/stsb-TinyBERT-L4")

    # Load the STSB dataset (https://huggingface.co/datasets/sentence-transformers/stsb)
    eval_dataset = load_dataset("sentence-transformers/stsb", split="validation")
    pairs = list(zip(eval_dataset["sentence1"], eval_dataset["sentence2"]))

    # Initialize the evaluator
    dev_evaluator = CrossEncoderCorrelationEvaluator(
        sentence_pairs=pairs,
        scores=eval_dataset["score"],
        name="sts_dev",
    )
    # You can run evaluation like so:
    # results = dev_evaluator(model)

CrossEncoderClassificationEvaluator with AllNLI

    from datasets import load_dataset
    from sentence_transformers import CrossEncoder
    from sentence_transformers.evaluation import TripletEvaluator, SimilarityFunction

    # Load a model
    model = CrossEncoder("cross-encoder/nli-deberta-v3-base")

    # Load triplets from the AllNLI dataset (https://huggingface.co/datasets/sentence-transformers/all-nli)
    max_samples = 1000
    eval_dataset = load_dataset("sentence-transformers/all-nli", "pair-class", split=f"dev[:]")

    # Create a list of pairs, and map the labels to the labels that the model knows
    pairs = list(zip(eval_dataset["premise"], eval_dataset["hypothesis"]))
    label_mapping = 
    labels = [label_mapping[label] for label in eval_dataset["label"]]

    # Initialize the evaluator
    cls_evaluator = CrossEncoderClassificationEvaluator(
        sentence_pairs=pairs,
        labels=labels,
        name="all-nli-dev",
    )
    # You can run evaluation like so:
    # results = cls_evaluator(model)

Warning

When using [Distributed Training](training/distributed.html), the evaluator only runs on the first device, unlike the training and evaluation datasets, which are shared across all devices.

## Trainer[ïƒ?](#trainer "Link to this heading")

The [[`CrossEncoderTrainer`]](../package_reference/cross_encoder/trainer.html#sentence_transformers.cross_encoder.trainer.CrossEncoderTrainer "sentence_transformers.cross_encoder.trainer.CrossEncoderTrainer") is where all previous components come together. We only have to specify the trainer with the model, training arguments (optional), training dataset, evaluation dataset (optional), loss function, evaluator (optional) and we can start training. Letâ€™s have a look at a script where all of these components come together:

Simple Example

    import logging
    import traceback

    from datasets import load_dataset

    from sentence_transformers.cross_encoder import (
        CrossEncoder,
        CrossEncoderModelCardData,
        CrossEncoderTrainer,
        CrossEncoderTrainingArguments,
    )
    from sentence_transformers.cross_encoder.evaluation import CrossEncoderNanoBEIREvaluator
    from sentence_transformers.cross_encoder.losses import CachedMultipleNegativesRankingLoss

    # Set the log level to INFO to get more information
    logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=logging.INFO)

    model_name = "microsoft/MiniLM-L12-H384-uncased"
    train_batch_size = 64
    num_epochs = 1
    num_rand_negatives = 5  # How many random negatives should be used for each question-answer pair

    # 1a. Load a model to finetune with 1b. (Optional) model card data
    model = CrossEncoder(
        model_name,
        model_card_data=CrossEncoderModelCardData(
            language="en",
            license="apache-2.0",
            model_name="MiniLM-L12-H384 trained on GooAQ",
        ),
    )
    print("Model max length:", model.max_length)
    print("Model num labels:", model.num_labels)

    # 2. Load the GooAQ dataset: https://huggingface.co/datasets/sentence-transformers/gooaq
    logging.info("Read the gooaq training dataset")
    full_dataset = load_dataset("sentence-transformers/gooaq", split="train").select(range(100_000))
    dataset_dict = full_dataset.train_test_split(test_size=1_000, seed=12)
    train_dataset = dataset_dict["train"]
    eval_dataset = dataset_dict["test"]
    logging.info(train_dataset)
    logging.info(eval_dataset)

    # 3. Define our training loss.
    loss = CachedMultipleNegativesRankingLoss(
        model=model,
        num_negatives=num_rand_negatives,
        mini_batch_size=32,  # Informs the memory usage
    )

    # 4. Use CrossEncoderNanoBEIREvaluator, a light-weight evaluator for English reranking
    evaluator = CrossEncoderNanoBEIREvaluator(
        dataset_names=["msmarco", "nfcorpus", "nq"],
        batch_size=train_batch_size,
    )
    evaluator(model)

    # 5. Define the training arguments
    short_model_name = model_name if "/" not in model_name else model_name.split("/")[-1]
    run_name = f"reranker--gooaq-cmnrl"
    args = CrossEncoderTrainingArguments(
        # Required parameter:
        output_dir=f"models/",
        # Optional training parameters:
        num_train_epochs=num_epochs,
        per_device_train_batch_size=train_batch_size,
        per_device_eval_batch_size=train_batch_size,
        learning_rate=2e-5,
        warmup_ratio=0.1,
        fp16=False,  # Set to False if you get an error that your GPU can't run on FP16
        bf16=True,  # Set to True if you have a GPU that supports BF16
        # Optional tracking/debugging parameters:
        eval_strategy="steps",
        eval_steps=100,
        save_strategy="steps",
        save_steps=100,
        save_total_limit=2,
        logging_steps=50,
        logging_first_step=True,
        run_name=run_name,  # Will be used in W&B if `wandb` is installed
        seed=12,
    )

    # 6. Create the trainer & start training
    trainer = CrossEncoderTrainer(
        model=model,
        args=args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        loss=loss,
        evaluator=evaluator,
    )
    trainer.train()

    # 7. Evaluate the final model, useful to include these in the model card
    evaluator(model)

    # 8. Save the final model
    final_output_dir = f"models//final"
    model.save_pretrained(final_output_dir)

    # 9. (Optional) save the model to the Hugging Face Hub!
    # It is recommended to run `huggingface-cli login` to log into your Hugging Face account first
    try:
        model.push_to_hub(run_name)
    except Exception:
        logging.error(
            f"Error uploading model to the Hugging Face Hub:\nTo upload it manually, you can run "
            f"`huggingface-cli login`, followed by loading the model using `model = CrossEncoder()` "
            f"and saving it using `model.push_to_hub('')`."
        )

Extensive Example

    import logging
    import traceback

    import torch
    from datasets import load_dataset

    from sentence_transformers import SentenceTransformer
    from sentence_transformers.cross_encoder import (
        CrossEncoder,
        CrossEncoderModelCardData,
        CrossEncoderTrainer,
        CrossEncoderTrainingArguments,
    )
    from sentence_transformers.cross_encoder.evaluation import (
        CrossEncoderNanoBEIREvaluator,
        CrossEncoderRerankingEvaluator,
    )
    from sentence_transformers.cross_encoder.losses import BinaryCrossEntropyLoss
    from sentence_transformers.evaluation import SequentialEvaluator
    from sentence_transformers.util import mine_hard_negatives

    # Set the log level to INFO to get more information
    logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=logging.INFO)

    def main():
        model_name = "answerdotai/ModernBERT-base"

        train_batch_size = 64
        num_epochs = 1
        num_hard_negatives = 5  # How many hard negatives should be mined for each question-answer pair

        # 1a. Load a model to finetune with 1b. (Optional) model card data
        model = CrossEncoder(
            model_name,
            model_card_data=CrossEncoderModelCardData(
                language="en",
                license="apache-2.0",
                model_name="ModernBERT-base trained on GooAQ",
            ),
        )
        print("Model max length:", model.max_length)
        print("Model num labels:", model.num_labels)

        # 2a. Load the GooAQ dataset: https://huggingface.co/datasets/sentence-transformers/gooaq
        logging.info("Read the gooaq training dataset")
        full_dataset = load_dataset("sentence-transformers/gooaq", split="train").select(range(100_000))
        dataset_dict = full_dataset.train_test_split(test_size=1_000, seed=12)
        train_dataset = dataset_dict["train"]
        eval_dataset = dataset_dict["test"]
        logging.info(train_dataset)
        logging.info(eval_dataset)

        # 2b. Modify our training dataset to include hard negatives using a very efficient embedding model
        embedding_model = SentenceTransformer("sentence-transformers/static-retrieval-mrl-en-v1", device="cpu")
        hard_train_dataset = mine_hard_negatives(
            train_dataset,
            embedding_model,
            num_negatives=num_hard_negatives,  # How many negatives per question-answer pair
            margin=0,  # Similarity between query and negative samples should be x lower than query-positive similarity
            range_min=0,  # Skip the x most similar samples
            range_max=100,  # Consider only the x most similar samples
            sampling_strategy="top",  # Sample the top negatives from the range
            batch_size=4096,  # Use a batch size of 4096 for the embedding model
            output_format="labeled-pair",  # The output format is (query, passage, label), as required by BinaryCrossEntropyLoss
            use_faiss=True,
        )
        logging.info(hard_train_dataset)

        # 2c. (Optionally) Save the hard training dataset to disk
        # hard_train_dataset.save_to_disk("gooaq-hard-train")
        # Load again with:
        # hard_train_dataset = load_from_disk("gooaq-hard-train")

        # 3. Define our training loss.
        # pos_weight is recommended to be set as the ratio between positives to negatives, a.k.a. `num_hard_negatives`
        loss = BinaryCrossEntropyLoss(model=model, pos_weight=torch.tensor(num_hard_negatives))

        # 4a. Define evaluators. We use the CrossEncoderNanoBEIREvaluator, which is a light-weight evaluator for English reranking
        nano_beir_evaluator = CrossEncoderNanoBEIREvaluator(
            dataset_names=["msmarco", "nfcorpus", "nq"],
            batch_size=train_batch_size,
        )

        # 4b. Define a reranking evaluator by mining hard negatives given query-answer pairs
        # We include the positive answer in the list of negatives, so the evaluator can use the performance of the
        # embedding model as a baseline.
        hard_eval_dataset = mine_hard_negatives(
            eval_dataset,
            embedding_model,
            corpus=full_dataset["answer"],  # Use the full dataset as the corpus
            num_negatives=30,  # How many documents to rerank
            batch_size=4096,
            include_positives=True,
            output_format="n-tuple",
            use_faiss=True,
        )
        logging.info(hard_eval_dataset)
        reranking_evaluator = CrossEncoderRerankingEvaluator(
            samples=[
                
                for sample in hard_eval_dataset
            ],
            batch_size=train_batch_size,
            name="gooaq-dev",
            # Realistic setting: only rerank the positives that the retriever found
            # Set to True to rerank *all* positives
            always_rerank_positives=False,
        )

        # 4c. Combine the evaluators & run the base model on them
        evaluator = SequentialEvaluator([reranking_evaluator, nano_beir_evaluator])
        evaluator(model)

        # 5. Define the training arguments
        short_model_name = model_name if "/" not in model_name else model_name.split("/")[-1]
        run_name = f"reranker--gooaq-bce"
        args = CrossEncoderTrainingArguments(
            # Required parameter:
            output_dir=f"models/",
            # Optional training parameters:
            num_train_epochs=num_epochs,
            per_device_train_batch_size=train_batch_size,
            per_device_eval_batch_size=train_batch_size,
            learning_rate=2e-5,
            warmup_ratio=0.1,
            fp16=False,  # Set to False if you get an error that your GPU can't run on FP16
            bf16=True,  # Set to True if you have a GPU that supports BF16
            dataloader_num_workers=4,
            load_best_model_at_end=True,
            metric_for_best_model="eval_gooaq-dev_ndcg@10",
            # Optional tracking/debugging parameters:
            eval_strategy="steps",
            eval_steps=1000,
            save_strategy="steps",
            save_steps=1000,
            save_total_limit=2,
            logging_steps=200,
            logging_first_step=True,
            run_name=run_name,  # Will be used in W&B if `wandb` is installed
            seed=12,
        )

        # 6. Create the trainer & start training
        trainer = CrossEncoderTrainer(
            model=model,
            args=args,
            train_dataset=hard_train_dataset,
            loss=loss,
            evaluator=evaluator,
        )
        trainer.train()

        # 7. Evaluate the final model, useful to include these in the model card
        evaluator(model)

        # 8. Save the final model
        final_output_dir = f"models//final"
        model.save_pretrained(final_output_dir)

        # 9. (Optional) save the model to the Hugging Face Hub!
        # It is recommended to run `huggingface-cli login` to log into your Hugging Face account first
        try:
            model.push_to_hub(run_name)
        except Exception:
            logging.error(
                f"Error uploading model to the Hugging Face Hub:\nTo upload it manually, you can run "
                f"`huggingface-cli login`, followed by loading the model using `model = CrossEncoder()` "
                f"and saving it using `model.push_to_hub('')`."
            )

    if __name__ == "__main__":
        main()

### Callbacks[ïƒ?](#callbacks "Link to this heading")

This CrossEncoder trainer integrates support for various [[`transformers.TrainerCallback`]](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.TrainerCallback "(in transformers vmain)") subclasses, such as:

- [[`WandbCallback`]](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.integrations.WandbCallback "(in transformers vmain)") to automatically log training metrics to W&B if [`wandb`] is installed

- [[`TensorBoardCallback`]](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.integrations.TensorBoardCallback "(in transformers vmain)") to log training metrics to TensorBoard if [`tensorboard`] is accessible.

- [[`CodeCarbonCallback`]](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.integrations.CodeCarbonCallback "(in transformers vmain)") to track the carbon emissions of your model during training if [`codecarbon`] is installed.

  > ::: 
  > - Note: These carbon emissions will be included in your automatically generated model card.
  > :::

See the Transformers [Callbacks](https://huggingface.co/docs/transformers/main/en/main_classes/callback) documentation for more information on the integrated callbacks and how to write your own callbacks.

## Multi-Dataset Training[ïƒ?](#multi-dataset-training "Link to this heading")

The top performing models are trained using many datasets at once. Normally, this is rather tricky, as each dataset has a different format. However, [[`CrossEncoderTrainer`]](../package_reference/cross_encoder/trainer.html#sentence_transformers.cross_encoder.trainer.CrossEncoderTrainer "sentence_transformers.cross_encoder.trainer.CrossEncoderTrainer") can train with multiple datasets without having to convert each dataset to the same format. It can even apply different loss functions to each of the datasets. The steps to train with multiple datasets are:

- Use a dictionary of [[`Dataset`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)") instances (or a [[`DatasetDict`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.DatasetDict "(in datasets vmain)")) as the [`train_dataset`] (and optionally also [`eval_dataset`]).

- (Optional) Use a dictionary of loss functions mapping dataset names to losses. Only required if you wish to use different loss function for different datasets.

Each training/evaluation batch will only contain samples from one of the datasets. The order in which batches are samples from the multiple datasets is defined by the [[`MultiDatasetBatchSamplers`]](../package_reference/sentence_transformer/sampler.html#sentence_transformers.training_args.MultiDatasetBatchSamplers "sentence_transformers.training_args.MultiDatasetBatchSamplers") enum, which can be passed to the [[`CrossEncoderTrainingArguments`]](../package_reference/cross_encoder/training_args.html#sentence_transformers.cross_encoder.training_args.CrossEncoderTrainingArguments "sentence_transformers.cross_encoder.training_args.CrossEncoderTrainingArguments") via [`multi_dataset_batch_sampler`]. Valid options are:

- [`MultiDatasetBatchSamplers.ROUND_ROBIN`]: Round-robin sampling from each dataset until one is exhausted. With this strategy, itâ€™s likely that not all samples from each dataset are used, but each dataset is sampled from equally.

- [`MultiDatasetBatchSamplers.PROPORTIONAL`] (default): Sample from each dataset in proportion to its size. With this strategy, all samples from each dataset are used and larger datasets are sampled from more frequently.

## Training Tips[ïƒ?](#training-tips "Link to this heading")

Cross Encoder models have their own unique quirks, so hereâ€™s some tips to help you out:

1.  [[`CrossEncoder`]](../package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder") models overfit rather quickly, so itâ€™s recommended to use an evaluator like [[`CrossEncoderNanoBEIREvaluator`]](../package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderNanoBEIREvaluator "sentence_transformers.cross_encoder.evaluation.CrossEncoderNanoBEIREvaluator") or [[`CrossEncoderRerankingEvaluator`]](../package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderRerankingEvaluator "sentence_transformers.cross_encoder.evaluation.CrossEncoderRerankingEvaluator") together with the [`load_best_model_at_end`] and [`metric_for_best_model`] training arguments to load the model with the best evaluation performance after training.

2.  [[`CrossEncoder`]](../package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder") are particularly receptive to strong hard negatives ([[`mine_hard_negatives()`]](../package_reference/util.html#sentence_transformers.util.mine_hard_negatives "sentence_transformers.util.mine_hard_negatives")). They teach the model to be very strict, useful e.g. when distinguishing between passages that answer a question or passages that relate to a question.

    > ::: 
    > 1.  Note that if you only use hard negatives, [your model may unexpectedly perform worse for easier tasks](https://huggingface.co/papers/2411.11767). This can mean that reranking the top 200 results from a first-stage retrieval system (e.g. with a [[`SentenceTransformer`]](../package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer") model) can actually give worse top-10 results than reranking the top 100. Training using random negatives alongside hard negatives can mitigate this.
    > :::

3.  Donâ€™t underestimate [[`BinaryCrossEntropyLoss`]](../package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss "sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss"), it remains a very strong option despite being simpler than learning-to-rank ([[`LambdaLoss`]](../package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.LambdaLoss "sentence_transformers.cross_encoder.losses.LambdaLoss"), [[`ListNetLoss`]](../package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.ListNetLoss "sentence_transformers.cross_encoder.losses.ListNetLoss")) or in-batch negatives ([[`CachedMultipleNegativesRankingLoss`]](../package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.CachedMultipleNegativesRankingLoss "sentence_transformers.cross_encoder.losses.CachedMultipleNegativesRankingLoss"), [[`MultipleNegativesRankingLoss`]](../package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.MultipleNegativesRankingLoss "sentence_transformers.cross_encoder.losses.MultipleNegativesRankingLoss")) losses, and its data is easy to prepare, especially using [[`mine_hard_negatives()`]](../package_reference/util.html#sentence_transformers.util.mine_hard_negatives "sentence_transformers.util.mine_hard_negatives").

## Deprecated Training[ïƒ?](#deprecated-training "Link to this heading")

Prior to the Sentence Transformers v4.0 release, models would be trained with the [[`CrossEncoder.fit()`]](../package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.fit "sentence_transformers.cross_encoder.CrossEncoder.fit") method and a [[`DataLoader`]](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader "(in PyTorch v2.9)") of [`InputExample`], which looked something like this:

    from sentence_transformers import CrossEncoder, InputExample
    from torch.utils.data import DataLoader

    # Define the model. Either from scratch of by loading a pre-trained model
    model = CrossEncoder("distilbert/distilbert-base-uncased")

    # Define your train examples. You need more than just two examples...
    train_examples = [
        InputExample(texts=["What are pandas?", "The giant panda ..."], label=1),
        InputExample(texts=["What's a panda?", "Mount Vesuvius is a ..."], label=0),
    ]

    # Define your train dataset, the dataloader and the train loss
    train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=16)

    # Tune the model
    model.fit(train_dataloader=train_dataloader, epochs=1, warmup_steps=100)

Since the v4.0 release, using [[`CrossEncoder.fit()`]](../package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.fit "sentence_transformers.cross_encoder.CrossEncoder.fit") is still possible, but it will initialize a [[`CrossEncoderTrainer`]](../package_reference/cross_encoder/trainer.html#sentence_transformers.cross_encoder.trainer.CrossEncoderTrainer "sentence_transformers.cross_encoder.trainer.CrossEncoderTrainer") behind the scenes. It is recommended to use the Trainer directly, as you will have more control via the [[`CrossEncoderTrainingArguments`]](../package_reference/cross_encoder/training_args.html#sentence_transformers.cross_encoder.training_args.CrossEncoderTrainingArguments "sentence_transformers.cross_encoder.training_args.CrossEncoderTrainingArguments"), but existing training scripts relying on [[`CrossEncoder.fit()`]](../package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.fit "sentence_transformers.cross_encoder.CrossEncoder.fit") should still work.

In case there are issues with the updated [[`CrossEncoder.fit()`]](../package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.fit "sentence_transformers.cross_encoder.CrossEncoder.fit"), you can also get exactly the old behaviour by calling [[`CrossEncoder.old_fit()`]](../package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.old_fit "sentence_transformers.cross_encoder.CrossEncoder.old_fit") instead, but this method is planned to be deprecated fully in the future.

## Comparisons with SentenceTransformer Training[ïƒ?](#comparisons-with-sentencetransformer-training "Link to this heading")

Training [[`CrossEncoder`]](../package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder") models is very similar as training [[`SentenceTransformer`]](../package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer") models, with some key differences:

- Instead of just [`score`] and [`label`], columns named [`scores`] and [`labels`] will also be considered â€œlabel columnsâ€? for [[`CrossEncoder`]](../package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder") training. As you can see in the [Loss Overview](loss_overview.html) documentation, some losses require specific labels/scores in a column with one of these names.

- In [[`SentenceTransformer`]](../package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer") training, you cannot use lists of inputs (e.g. texts) in a column of the training/evaluation dataset(s). For [[`CrossEncoder`]](../package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder") training, you **can** use (variably sized) lists of texts in a column. This is required for the [[`ListNetLoss`]](../package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.ListNetLoss "sentence_transformers.cross_encoder.losses.ListNetLoss") class, for example.

See the [Sentence Transformer \> Training Overview](../sentence_transformer/training_overview.html) documentation for more details on training [[`SentenceTransformer`]](../package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer") models.