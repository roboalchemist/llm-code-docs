# Source: https://www.sbert.net/docs/sparse_encoder/training_overview.html

# Training Overview[ïƒ?](#training-overview "Link to this heading")

## Why Finetune?[ïƒ?](#why-finetune "Link to this heading")

Finetuning Sparse Encoder models often heavily improves the performance of the model on your use case, because each task requires a different notion of similarity. For example, given news articles:

- â€œApple launches the new iPadâ€?

- â€œNVIDIA is gearing up for the next GPU generationâ€?

Then the following use cases, we may have different notions of similarity:

- a model for **classification** of news articles as Economy, Sports, Technology, Politics, etc., should produce **similar embeddings** for these texts.

- a model for **semantic textual similarity** should produce **dissimilar embeddings** for these texts, as they have different meanings.

- a model for **semantic search** would **not need a notion for similarity** between two documents, as it should only compare queries and documents.

Also see [[**Training Examples**]](training/examples.html) for numerous training scripts for common real-world applications that you can adopt.

## Training Components[ïƒ?](#training-components "Link to this heading")

Training Sparse Encoder models involves between 4 to 6 components:

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

Sparse Encoder models consist of a sequence of [Modules](../package_reference/sentence_transformer/models.html), [Sparse Encoder specific Modules](../package_reference/sparse_encoder/models.html) or [Custom Modules](../sentence_transformer/usage/custom_models.html#advanced-custom-modules), allowing for a lot of flexibility. If you want to further finetune a SparseEncoder model (e.g. it has a [modules.json file](https://huggingface.co/naver/splade-cocondenser-ensembledistil/tree/main/modules.json)), then you donâ€™t have to worry about which modules are used:

    from sentence_transformers import SparseEncoder

    model = SparseEncoder("naver/splade-cocondenser-ensembledistil")

But if instead you want to train from another checkpoint, or from scratch, then these are the most common architectures you can use:

Splade

Splade models use the [[`MLMTransformer`]](../package_reference/sparse_encoder/models.html#sentence_transformers.sparse_encoder.models.MLMTransformer "sentence_transformers.sparse_encoder.models.MLMTransformer") followed by a [[`SpladePooling`]](../package_reference/sparse_encoder/models.html#sentence_transformers.sparse_encoder.models.SpladePooling "sentence_transformers.sparse_encoder.models.SpladePooling") modules. The former loads a pretrained [Masked Language Modeling transformer model](https://huggingface.co/models?pipeline_tag=fill-mask) (e.g. [BERT](https://huggingface.co/google-bert/bert-base-uncased), [RoBERTa](https://huggingface.co/FacebookAI/roberta-base), [DistilBERT](https://huggingface.co/distilbert/distilbert-base-uncased), [ModernBERT](https://huggingface.co/answerdotai/ModernBERT-base), etc.) and the latter pools the output of the MLMHead to produce a single sparse embedding of the size of the vocabulary.

Documentation

- [[`sentence_transformers.sparse_encoder.models.MLMTransformer`]](../package_reference/sparse_encoder/models.html#sentence_transformers.sparse_encoder.models.MLMTransformer)
- [[`sentence_transformers.sparse_encoder.models.SpladePooling`]](../package_reference/sparse_encoder/models.html#sentence_transformers.sparse_encoder.models.SpladePooling)

    from sentence_transformers import models, SparseEncoder
    from sentence_transformers.sparse_encoder.models import MLMTransformer, SpladePooling

    # Initialize MLM Transformer (use a fill-mask model)
    mlm_transformer = MLMTransformer("google-bert/bert-base-uncased")

    # Initialize SpladePooling module
    splade_pooling = SpladePooling(pooling_strategy="max")

    # Create the Splade model
    model = SparseEncoder(modules=[mlm_transformer, splade_pooling])

This architecture is the default if you provide a fill-mask model architecture to SparseEncoder, so itâ€™s easier to use the shortcut:

    from sentence_transformers import SparseEncoder

    model = SparseEncoder("google-bert/bert-base-uncased")
    # SparseEncoder(
    #   (0): MLMTransformer()
    #   (1): SpladePooling()
    # )

Inference-free Splade

Inference-free Splade uses a [[`Router`]](../package_reference/sentence_transformer/models.html#sentence_transformers.models.Router "sentence_transformers.models.Router") module with different modules for queries and documents. Usually for this type of architecture, the documents part is a traditional Splade architecture (a [[`MLMTransformer`]](../package_reference/sparse_encoder/models.html#sentence_transformers.sparse_encoder.models.MLMTransformer "sentence_transformers.sparse_encoder.models.MLMTransformer") followed by a [[`SpladePooling`]](../package_reference/sparse_encoder/models.html#sentence_transformers.sparse_encoder.models.SpladePooling "sentence_transformers.sparse_encoder.models.SpladePooling") module) and the query part is an [[`SparseStaticEmbedding`]](../package_reference/sparse_encoder/models.html#sentence_transformers.sparse_encoder.models.SparseStaticEmbedding "sentence_transformers.sparse_encoder.models.SparseStaticEmbedding") module, which just returns a pre-computed score for every token in the query.

Documentation

- [[`sentence_transformers.models.Router`]](../package_reference/sentence_transformer/models.html#sentence_transformers.models.Router)
- [[`sentence_transformers.sparse_encoder.models.SparseStaticEmbedding`]](../package_reference/sparse_encoder/models.html#sentence_transformers.sparse_encoder.models.SparseStaticEmbedding)
- [[`sentence_transformers.sparse_encoder.models.MLMTransformer`]](../package_reference/sparse_encoder/models.html#sentence_transformers.sparse_encoder.models.MLMTransformer)
- [[`sentence_transformers.sparse_encoder.models.SpladePooling`]](../package_reference/sparse_encoder/models.html#sentence_transformers.sparse_encoder.models.SpladePooling)

    from sentence_transformers import SparseEncoder
    from sentence_transformers.models import Router
    from sentence_transformers.sparse_encoder.models import MLMTransformer, SparseStaticEmbedding, SpladePooling

    # Initialize MLM Transformer for document encoding
    doc_encoder = MLMTransformer("google-bert/bert-base-uncased")

    # Create a router model with different paths for queries and documents
    router = Router.for_query_document(
        query_modules=[SparseStaticEmbedding(tokenizer=doc_encoder.tokenizer, frozen=False)],
        # Document path: full MLM transformer + pooling
        document_modules=[doc_encoder, SpladePooling("max")],
    )

    # Create the inference-free model
    model = SparseEncoder(modules=[router], similarity_fn_name="dot")
    # SparseEncoder(
    #   (0): Router(
    #     (query_0_SparseStaticEmbedding): SparseStaticEmbedding(, dim:30522, tokenizer: BertTokenizerFast)
    #     (document_0_MLMTransformer): MLMTransformer()
    #     (document_1_SpladePooling): SpladePooling()
    #   )
    # )

This architecture allows for fast query-time processing using the lightweight SparseStaticEmbedding approach, that can be trained and seen as a linear weights, while documents are processed with the full MLM transformer and SpladePooling.

Tip

Inference-free Splade is particularly useful for search applications where query latency is critical, as it shifts the computational complexity to the document indexing phase which can be done offline.

Note

When training models with the [[`Router`]](../package_reference/sentence_transformer/models.html#sentence_transformers.models.Router "sentence_transformers.models.Router") module, you must use the [`router_mapping`] argument in the [`SparseEncoderTrainingArguments`] to map the training dataset columns to the correct route (â€œqueryâ€? or â€œdocumentâ€?). For example, if your dataset(s) have [`["question",`]` `[`"answer"]`] columns, then you can use the following mapping:

    args = SparseEncoderTrainingArguments(
        ...,
        router_mapping=
    )

Additionally, it is recommended to use a much higher learning rate for the SparseStaticEmbedding module than for the rest of the model. For this, you should use the [`learning_rate_mapping`] argument in the [`SparseEncoderTrainingArguments`] to map parameter patterns to their learning rates. For example, if you want to use a learning rate of [`1e-3`] for the SparseStaticEmbedding module and [`2e-5`] for the rest of the model, you can do this:

    args = SparseEncoderTrainingArguments(
        ...,
        learning_rate=2e-5,
        learning_rate_mapping=
    )

Contrastive Sparse Representation (CSR)

Contrastive Sparse Representation (CSR) models apply a [[`SparseAutoEncoder`]](../package_reference/sparse_encoder/models.html#sentence_transformers.sparse_encoder.models.SparseAutoEncoder "sentence_transformers.sparse_encoder.models.SparseAutoEncoder") module on top of a dense Sentence Transformer model, which usually consist of a [[`Transformer`]](../package_reference/sentence_transformer/models.html#sentence_transformers.models.Transformer "sentence_transformers.models.Transformer") followed by a [[`Pooling`]](../package_reference/sentence_transformer/models.html#sentence_transformers.models.Pooling "sentence_transformers.models.Pooling") module. You can initialize one from scratch like so:

Documentation

- [[`sentence_transformers.models.Transformer`]](../package_reference/sentence_transformer/models.html#sentence_transformers.models.Transformer)
- [[`sentence_transformers.models.Pooling`]](../package_reference/sentence_transformer/models.html#sentence_transformers.models.Pooling)
- [[`sentence_transformers.sparse_encoder.models.SparseAutoEncoder`]](../package_reference/sparse_encoder/models.html#sentence_transformers.sparse_encoder.models.SparseAutoEncoder)

    from sentence_transformers import models, SparseEncoder
    from sentence_transformers.sparse_encoder.models import SparseAutoEncoder

    # Initialize transformer (can be any dense encoder model)
    transformer = models.Transformer("google-bert/bert-base-uncased")

    # Initialize pooling
    pooling = models.Pooling(transformer.get_word_embedding_dimension(), pooling_mode="mean")

    # Initialize SparseAutoEncoder module
    sae = SparseAutoEncoder(
        input_dim=transformer.get_word_embedding_dimension(),
        hidden_dim=4 * transformer.get_word_embedding_dimension(),
        k=256,  # Number of top values to keep
        k_aux=512,  # Number of top values for auxiliary loss
    )
    # Create the CSR model
    model = SparseEncoder(modules=[transformer, pooling, sae])

Or if your base model is 1) a dense Sentence Transformer model or 2) a non-MLM Transformer model (those are loaded as Splade models by default), then this shortcut will automatically initialize the CSR model for you:

    from sentence_transformers import SparseEncoder

    model = SparseEncoder("mixedbread-ai/mxbai-embed-large-v1")
    # SparseEncoder(
    #   (0): Transformer()
    #   (1): Pooling()
    #   (2): SparseAutoEncoder()
    # )

Warning

Unlike (Inference-free) Splade models, sparse embeddings by CSR models donâ€™t have the same size as the vocabulary of the base model. This means you canâ€™t directly interpret which words are activated in your embedding like you can with Splade models, where each dimension corresponds to a specific token in the vocabulary.

Beyond that, CSR models are most effective on dense encoder models that use high-dimensional representations (e.g. 1024-4096 dimensions).

## Dataset[ïƒ?](#dataset "Link to this heading")

The [`SparseEncoderTrainer`] trains and evaluates using [[`datasets.Dataset`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)") (one dataset) or [[`datasets.DatasetDict`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.DatasetDict "(in datasets vmain)") instances (multiple datasets, see also [Multi-dataset training](#multi-dataset-training)).

Data on ðŸ¤--- Hugging Face Hub

If you want to load data from the [Hugging Face Datasets](https://huggingface.co/datasets), then you should use [[`datasets.load_dataset()`]](https://huggingface.co/docs/datasets/main/en/package_reference/loading_methods#datasets.load_dataset "(in datasets vmain)"):

Documentation

- [Datasets, Loading from the Hugging Face Hub](https://huggingface.co/docs/datasets/main/en/loading#hugging-face-hub)
- [[`datasets.load_dataset()`]](https://huggingface.co/docs/datasets/main/en/package_reference/loading_methods#datasets.load_dataset "(in datasets vmain)")
- [sentence-transformers/all-nli](https://huggingface.co/datasets/sentence-transformers/all-nli)

    from datasets import load_dataset

    train_dataset = load_dataset("sentence-transformers/all-nli", "triplet", split="train")
    eval_dataset = load_dataset("sentence-transformers/all-nli", "triplet", split="dev")

    print(train_dataset)
    """
    Dataset()
    """

Some datasets (including [sentence-transformers/all-nli](https://huggingface.co/datasets/sentence-transformers/all-nli)) require you to provide a â€œsubsetâ€? alongside the dataset name. [`sentence-transformers/all-nli`] has 4 subsets, each with different data formats: [pair](https://huggingface.co/datasets/sentence-transformers/all-nli/viewer/pair), [pair-class](https://huggingface.co/datasets/sentence-transformers/all-nli/viewer/pair-class), [pair-score](https://huggingface.co/datasets/sentence-transformers/all-nli/viewer/pair-score), [triplet](https://huggingface.co/datasets/sentence-transformers/all-nli/viewer/triplet).

Note

Many Hugging Face datasets that work out of the box with Sentence Transformers have been tagged with [`sentence-transformers`], allowing you to easily find them by browsing to [https://huggingface.co/datasets?other=sentence-transformers](https://huggingface.co/datasets?other=sentence-transformers). We strongly recommend that you browse these datasets to find training datasets that might be useful for your tasks.

Local Data (CSV, JSON, Parquet, Arrow, SQL)

If you have local data in common file-formats, then you can load this data easily using [[`datasets.load_dataset()`]](https://huggingface.co/docs/datasets/main/en/package_reference/loading_methods#datasets.load_dataset "(in datasets vmain)"):

Documentation

- [Datasets, Loading local files](https://huggingface.co/docs/datasets/main/en/loading#local-and-remote-files)
- [[`datasets.load_dataset()`]](https://huggingface.co/docs/datasets/main/en/package_reference/loading_methods#datasets.load_dataset "(in datasets vmain)")

    from datasets import load_dataset

    dataset = load_dataset("csv", data_files="my_file.csv")

or:

    from datasets import load_dataset

    dataset = load_dataset("json", data_files="my_file.json")

Local Data that requires pre-processing

If you have local data that requires some extra pre-processing, my recommendation is to initialize your dataset using [[`datasets.Dataset.from_dict()`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset.from_dict "(in datasets vmain)") and a dictionary of lists, like so:

Documentation

- [[`datasets.Dataset.from_dict()`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset.from_dict "(in datasets vmain)")

    from datasets import Dataset

    anchors = []
    positives = []
    # Open a file, do preprocessing, filtering, cleaning, etc.
    # and append to the lists

    dataset = Dataset.from_dict()

Each key from the dictionary will become a column in the resulting dataset.

### Dataset Format[ïƒ?](#dataset-format "Link to this heading")

It is important that your dataset format matches your loss function (or that you choose a loss function that matches your dataset format). Verifying whether a dataset format works with a loss function involves two steps:

1.  If your loss function requires a *Label* according to the [Loss Overview](loss_overview.html) table, then your dataset must have a **column named â€œlabelâ€? or â€œscoreâ€?**. This column is automatically taken as the label.

2.  All columns not named â€œlabelâ€? or â€œscoreâ€? are considered *Inputs* according to the [Loss Overview](loss_overview.html) table. The number of remaining columns must match the number of valid inputs for your chosen loss. The names of these columns are **irrelevant**, only the **order matters**.

For example, given a dataset with columns [`["text1",`]` `[`"text2",`]` `[`"label"]`] where the â€œlabelâ€? column has float similarity score between 0 and 1, we can use it with [[`SparseCoSENTLoss`]](../package_reference/sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.SparseCoSENTLoss "sentence_transformers.sparse_encoder.losses.SparseCoSENTLoss"), [[`SparseAnglELoss`]](../package_reference/sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.SparseAnglELoss "sentence_transformers.sparse_encoder.losses.SparseAnglELoss"), and [[`SparseCosineSimilarityLoss`]](../package_reference/sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.SparseCosineSimilarityLoss "sentence_transformers.sparse_encoder.losses.SparseCosineSimilarityLoss") because it:

1.  has a â€œlabelâ€? column as is required for these loss functions.

2.  has 2 non-label columns, exactly the amount required by these loss functions.

Be sure to re-order your dataset columns with [[`Dataset.select_columns`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset.select_columns "(in datasets vmain)") if your columns are not ordered correctly. For example, if your dataset has [`["good_answer",`]` `[`"bad_answer",`]` `[`"question"]`] as columns, then this dataset can technically be used with a loss that requires (anchor, positive, negative) triplets, but the [`good_answer`] column will be taken as the anchor, [`bad_answer`] as the positive, and [`question`] as the negative.

Additionally, if your dataset has extraneous columns (e.g. sample_id, metadata, source, type), you should remove these with [[`Dataset.remove_columns`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset.remove_columns "(in datasets vmain)") as they will be used as inputs otherwise. You can also use [[`Dataset.select_columns`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset.select_columns "(in datasets vmain)") to keep only the desired columns.

## Loss Function[ïƒ?](#loss-function "Link to this heading")

Loss functions quantify how well a model performs for a given batch of data, allowing an optimizer to update the model weights to produce more favourable (i.e., lower) loss values. This is the core of the training process.

Sadly, there is no single loss function that works best for all use-cases. Instead, which loss function to use greatly depends on your available data and on your target task. See [Dataset Format](#dataset-format) to learn what datasets are valid for which loss functions. Additionally, the [[Loss Overview]](loss_overview.html) will be your best friend to learn about the options.

Warning

To train a [[`SparseEncoder`]](../package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder"), you need either [[`SpladeLoss`]](../package_reference/sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.SpladeLoss "sentence_transformers.sparse_encoder.losses.SpladeLoss") or [[`CSRLoss`]](../package_reference/sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.CSRLoss "sentence_transformers.sparse_encoder.losses.CSRLoss"), depending on the architecture. These are wrapper losses that add sparsity regularization on top of a main loss function, which must be provided as a parameter. The only loss that can be used independently is [[`SparseMSELoss`]](../package_reference/sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.SparseMSELoss "sentence_transformers.sparse_encoder.losses.SparseMSELoss"), as it performs embedding-level distillation, ensuring sparsity by directly copying the teacherâ€™s sparse embedding.

Most loss functions can be initialized with just the [[`SparseEncoder`]](../package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder") that youâ€™re training, alongside some optional parameters, e.g.:

Documentation

- [[`sentence_transformers.sparse_encoder.losses.SpladeLoss`]](../package_reference/sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.SpladeLoss "sentence_transformers.sparse_encoder.losses.SpladeLoss")

- [[`sentence_transformers.sparse_encoder.losses.CSRLoss`]](../package_reference/sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.CSRLoss "sentence_transformers.sparse_encoder.losses.CSRLoss")

- [Losses API Reference](../package_reference/sparse_encoder/losses.html)

- [Loss Overview](loss_overview.html)

    from datasets import load_dataset
    from sentence_transformers import SparseEncoder
    from sentence_transformers.sparse_encoder.losses import SpladeLoss, SparseMultipleNegativesRankingLoss

    # Load a model to train/finetune
    model = SparseEncoder("distilbert/distilbert-base-uncased")

    # Initialize the SpladeLoss with a SparseMultipleNegativesRankingLoss
    # This loss requires pairs of related texts or triplets
    loss = SpladeLoss(
        model=model,
        loss=SparseMultipleNegativesRankingLoss(model=model),
        query_regularizer_weight=5e-5,  # Weight for query loss
        document_regularizer_weight=3e-5,
    )

    # Load an example training dataset that works with our loss function:
    train_dataset = load_dataset("sentence-transformers/natural-questions", split="train")
    print(train_dataset)
    """
    Dataset()
    """

## Training Arguments[ïƒ?](#training-arguments "Link to this heading")

The [[`SparseEncoderTrainingArguments`]](../package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments "sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments") class can be used to specify parameters for influencing training performance as well as defining the tracking/debugging parameters. Although it is optional, it is heavily recommended to experiment with the various useful arguments.

Key Training Arguments for improving training performance

[`learning_rate`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.learning_rate) [`lr_scheduler_type`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.lr_scheduler_type) [`warmup_ratio`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.warmup_ratio) [`num_train_epochs`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.num_train_epochs) [`max_steps`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.max_steps) [`per_device_train_batch_size`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.per_device_train_batch_size) [`per_device_eval_batch_size`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.per_device_eval_batch_size) [`auto_find_batch_size`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.auto_find_batch_size%20) [`fp16`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.fp16) [`bf16`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.bf16) [`load_best_model_at_end`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.load_best_model_at_end) [`metric_for_best_model`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.metric_for_best_model) [`gradient_accumulation_steps`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.gradient_accumulation_steps) [`gradient_checkpointing`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.gradient_checkpointing) [`eval_accumulation_steps`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.eval_accumulation_steps) [`optim`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.optim) [`batch_sampler`](../package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments) [`multi_dataset_batch_sampler`](../package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments) [`prompts`](../package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments) [`router_mapping`](../package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments) [`learning_rate_mapping`](../package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments)

\

Key Training Arguments for observing training performance

[`eval_strategy`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.eval_strategy) [`eval_steps`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.eval_steps) [`save_strategy`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.save_strategy) [`save_steps`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.save_steps) [`save_total_limit`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.save_total_limit) [`report_to`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.report_to) [`run_name`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.run_name) [`log_level`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.log_level) [`logging_steps`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.logging_steps) [`push_to_hub`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.push_to_hub) [`hub_model_id`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.hub_model_id) [`hub_strategy`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.hub_strategy) [`hub_private_repo`](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.hub_private_repo)

\

Here is an example of how [[`SparseEncoderTrainingArguments`]](../package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments "sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments") can be initialized:

    args = SparseEncoderTrainingArguments(
        # Required parameter:
        output_dir="models/splade-distilbert-base-uncased-nq",
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
        run_name="splade-distilbert-base-uncased-nq",  # Will be used in W&B if `wandb` is installed
    )

## Evaluator[ïƒ?](#evaluator "Link to this heading")

You can provide the [[`SparseEncoderTrainer`]](../package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer "sentence_transformers.sparse_encoder.trainer.SparseEncoderTrainer") with an [`eval_dataset`] to get the evaluation loss during training, but it may be useful to get more concrete metrics during training, too. For this, you can use evaluators to assess the modelâ€™s performance with useful metrics before, during, or after training. You can use both an [`eval_dataset`] and an evaluator, one or the other, or neither. They evaluate based on the [`eval_strategy`] and [`eval_steps`] [Training Arguments](#training-arguments).

Here are the implemented Evaluators that come with Sentence Transformers for Sparse Encoder models:

  Evaluator                                                                                                                                                                                                                                                                                                                                                   Required Data
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [[`SparseBinaryClassificationEvaluator`]](../package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.SparseBinaryClassificationEvaluator "sentence_transformers.sparse_encoder.evaluation.SparseBinaryClassificationEvaluator")   Pairs with class labels.
  [[`SparseEmbeddingSimilarityEvaluator`]](../package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.SparseEmbeddingSimilarityEvaluator "sentence_transformers.sparse_encoder.evaluation.SparseEmbeddingSimilarityEvaluator")      Pairs with similarity scores.
  [[`SparseInformationRetrievalEvaluator`]](../package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.SparseInformationRetrievalEvaluator "sentence_transformers.sparse_encoder.evaluation.SparseInformationRetrievalEvaluator")   Queries (qid =\> question), Corpus (cid =\> document), and relevant documents (qid =\> set\[cid\]).
  [[`SparseNanoBEIREvaluator`]](../package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.SparseNanoBEIREvaluator "sentence_transformers.sparse_encoder.evaluation.SparseNanoBEIREvaluator")                                       No data required.
  [[`SparseMSEEvaluator`]](../package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.SparseMSEEvaluator "sentence_transformers.sparse_encoder.evaluation.SparseMSEEvaluator")                                                      Source sentences to embed with a teacher model and target sentences to embed with the student model. Can be the same texts.
  [[`SparseRerankingEvaluator`]](../package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.SparseRerankingEvaluator "sentence_transformers.sparse_encoder.evaluation.SparseRerankingEvaluator")                                    List of [`]` `[`'...',`]` `[`'positive':`]` `[`[...],`]` `[`'negative':`]` `[`[...]}`] dictionaries.
  [[`SparseTranslationEvaluator`]](../package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.SparseTranslationEvaluator "sentence_transformers.sparse_encoder.evaluation.SparseTranslationEvaluator")                              Pairs of sentences in two separate languages.
  [[`SparseTripletEvaluator`]](../package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.SparseTripletEvaluator "sentence_transformers.sparse_encoder.evaluation.SparseTripletEvaluator")                                          (anchor, positive, negative) pairs.

Additionally, [[`SequentialEvaluator`]](../package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.SequentialEvaluator "sentence_transformers.evaluation.SequentialEvaluator") should be used to combine multiple evaluators into one Evaluator that can be passed to the [[`SparseEncoderTrainer`]](../package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer "sentence_transformers.sparse_encoder.trainer.SparseEncoderTrainer").

Sometimes you donâ€™t have the required evaluation data to prepare one of these evaluators on your own, but you still want to track how well the model performs on some common benchmarks. In that case, you can use these evaluators with data from Hugging Face.

SparseNanoBEIREvaluator

Documentation

- [[`sentence_transformers.sparse_encoder.evaluation.SparseNanoBEIREvaluator`]](../package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.SparseNanoBEIREvaluator "sentence_transformers.sparse_encoder.evaluation.SparseNanoBEIREvaluator")

    from sentence_transformers.sparse_encoder.evaluation import SparseNanoBEIREvaluator

    # Initialize the evaluator. Unlike most other evaluators, this one loads the relevant datasets
    # directly from Hugging Face, so there's no mandatory arguments
    dev_evaluator = SparseNanoBEIREvaluator()
    # You can run evaluation like so:
    # results = dev_evaluator(model)

SparseEmbeddingSimilarityEvaluator with STSb

Documentation

- [sentence-transformers/stsb](https://huggingface.co/datasets/sentence-transformers/stsb)
- [[`sentence_transformers.sparse_encoder.evaluation.SparseEmbeddingSimilarityEvaluator`]](../package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.SparseEmbeddingSimilarityEvaluator "sentence_transformers.sparse_encoder.evaluation.SparseEmbeddingSimilarityEvaluator")
- [[`sentence_transformers.SimilarityFunction`]](../package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")

    from datasets import load_dataset
    from sentence_transformers.evaluation import SimilarityFunction
    from sentence_transformers.sparse_encoder.evaluation import SparseEmbeddingSimilarityEvaluator

    # Load the STSB dataset (https://huggingface.co/datasets/sentence-transformers/stsb)
    eval_dataset = load_dataset("sentence-transformers/stsb", split="validation")

    # Initialize the evaluator
    dev_evaluator = SparseEmbeddingSimilarityEvaluator(
        sentences1=eval_dataset["sentence1"],
        sentences2=eval_dataset["sentence2"],
        scores=eval_dataset["score"],
        main_similarity=SimilarityFunction.COSINE,
        name="sts-dev",
    )
    # You can run evaluation like so:
    # results = dev_evaluator(model)

SparseTripletEvaluator with AllNLI

Documentation

- [sentence-transformers/all-nli](https://huggingface.co/datasets/sentence-transformers/all-nli)
- [[`sentence_transformers.sparse_encoder.evaluation.SparseTripletEvaluator`]](../package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.SparseTripletEvaluator "sentence_transformers.sparse_encoder.evaluation.SparseTripletEvaluator")
- [[`sentence_transformers.SimilarityFunction`]](../package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")

    from datasets import load_dataset
    from sentence_transformers.evaluation import SimilarityFunction
    from sentence_transformers.sparse_encoder.evaluation import SparseTripletEvaluator

    # Load triplets from the AllNLI dataset (https://huggingface.co/datasets/sentence-transformers/all-nli)
    max_samples = 1000
    eval_dataset = load_dataset("sentence-transformers/all-nli", "triplet", split=f"dev[:]")

    # Initialize the evaluator
    dev_evaluator = SparseTripletEvaluator(
        anchors=eval_dataset["anchor"],
        positives=eval_dataset["positive"],
        negatives=eval_dataset["negative"],
        main_distance_function=SimilarityFunction.DOT,
        name="all-nli-dev",
    )
    # You can run evaluation like so:
    # results = dev_evaluator(model)

Tip

When evaluating frequently during training with a small [`eval_steps`], consider using a tiny [`eval_dataset`] to minimize evaluation overhead. If youâ€™re concerned about the evaluation set size, a 90-1-9 train-eval-test split can provide a balance, reserving a reasonably sized test set for final evaluations. After training, you can assess your modelâ€™s performance using [`trainer.evaluate(test_dataset)`] for test loss or initialize a testing evaluator with [`test_evaluator(model)`] for detailed test metrics.

If you evaluate after training, but before saving the model, your automatically generated model card will still include the test results.

Warning

When using [Distributed Training](../sentence_transformer/training/distributed.html), the evaluator only runs on the first device, unlike the training and evaluation datasets, which are shared across all devices.

## Trainer[ïƒ?](#trainer "Link to this heading")

The [[`SparseEncoderTrainer`]](../package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer "sentence_transformers.sparse_encoder.trainer.SparseEncoderTrainer") is where all previous components come together. We only have to specify the trainer with the model, training arguments (optional), training dataset, evaluation dataset (optional), loss function, evaluator (optional) and we can start training. Letâ€™s have a look at a script where all of these components come together:

SPLADE

Documentation

1.  [[`SparseEncoder`]](../package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder")

    1.  [[`MLMTransformer`]](../package_reference/sparse_encoder/models.html#sentence_transformers.sparse_encoder.models.MLMTransformer "sentence_transformers.sparse_encoder.models.MLMTransformer")

    2.  [[`SpladePooling`]](../package_reference/sparse_encoder/models.html#sentence_transformers.sparse_encoder.models.SpladePooling "sentence_transformers.sparse_encoder.models.SpladePooling")

2.  [[`SparseEncoderModelCardData`]](../package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.model_card.SparseEncoderModelCardData "sentence_transformers.sparse_encoder.model_card.SparseEncoderModelCardData")

3.  [[`load_dataset()`]](https://huggingface.co/docs/datasets/main/en/package_reference/loading_methods#datasets.load_dataset "(in datasets vmain)")

4.  [[`SparseMultipleNegativesRankingLoss`]](../package_reference/sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.SparseMultipleNegativesRankingLoss "sentence_transformers.sparse_encoder.losses.SparseMultipleNegativesRankingLoss")

5.  [[`SparseEncoderTrainingArguments`]](../package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments "sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments")

6.  [[`SparseTripletEvaluator`]](../package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.SparseTripletEvaluator "sentence_transformers.sparse_encoder.evaluation.SparseTripletEvaluator")

7.  [[`SparseEncoderTrainer`]](../package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer "sentence_transformers.sparse_encoder.trainer.SparseEncoderTrainer")

8.  [[`SparseEncoder.save_pretrained`]](../package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder.save_pretrained "sentence_transformers.sparse_encoder.SparseEncoder.save_pretrained")

9.  [[`SparseEncoder.push_to_hub`]](../package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder.push_to_hub "sentence_transformers.sparse_encoder.SparseEncoder.push_to_hub")

- [Training Examples](training/examples.html)

    import logging

    from datasets import load_dataset

    from sentence_transformers import (
        SparseEncoder,
        SparseEncoderModelCardData,
        SparseEncoderTrainer,
        SparseEncoderTrainingArguments,
    )
    from sentence_transformers.sparse_encoder.evaluation import SparseNanoBEIREvaluator
    from sentence_transformers.sparse_encoder.losses import SparseMultipleNegativesRankingLoss, SpladeLoss
    from sentence_transformers.training_args import BatchSamplers

    logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=logging.INFO)

    # 1. Load a model to finetune with 2. (Optional) model card data
    model = SparseEncoder(
        "distilbert/distilbert-base-uncased",
        model_card_data=SparseEncoderModelCardData(
            language="en",
            license="apache-2.0",
            model_name="DistilBERT base trained on Natural-Questions tuples",
        )
    )

    # 3. Load a dataset to finetune on
    full_dataset = load_dataset("sentence-transformers/natural-questions", split="train").select(range(100_000))
    dataset_dict = full_dataset.train_test_split(test_size=1_000, seed=12)
    train_dataset = dataset_dict["train"]
    eval_dataset = dataset_dict["test"]

    # 4. Define a loss function
    loss = SpladeLoss(
        model=model,
        loss=SparseMultipleNegativesRankingLoss(model=model),
        query_regularizer_weight=5e-5,
        document_regularizer_weight=3e-5,
    )

    # 5. (Optional) Specify training arguments
    run_name = "splade-distilbert-base-uncased-nq"
    args = SparseEncoderTrainingArguments(
        # Required parameter:
        output_dir=f"models/",
        # Optional training parameters:
        num_train_epochs=1,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        learning_rate=2e-5,
        warmup_ratio=0.1,
        fp16=True,  # Set to False if you get an error that your GPU can't run on FP16
        bf16=False,  # Set to True if you have a GPU that supports BF16
        batch_sampler=BatchSamplers.NO_DUPLICATES,  # MultipleNegativesRankingLoss benefits from no duplicate samples in a batch
        # Optional tracking/debugging parameters:
        eval_strategy="steps",
        eval_steps=1000,
        save_strategy="steps",
        save_steps=1000,
        save_total_limit=2,
        logging_steps=200,
        run_name=run_name,  # Will be used in W&B if `wandb` is installed
    )

    # 6. (Optional) Create an evaluator & evaluate the base model
    dev_evaluator = SparseNanoBEIREvaluator(dataset_names=["msmarco", "nfcorpus", "nq"], batch_size=16)

    # 7. Create a trainer & train
    trainer = SparseEncoderTrainer(
        model=model,
        args=args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        loss=loss,
        evaluator=dev_evaluator,
    )
    trainer.train()

    # 8. Evaluate the model performance again after training
    dev_evaluator(model)

    # 9. Save the trained model
    model.save_pretrained(f"models//final")

    # 10. (Optional) Push it to the Hugging Face Hub
    model.push_to_hub(run_name)

Inference-free SPLADE

Documentation

1.  [[`SparseEncoder`]](../package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder")

    1.  [[`SparseStaticEmbedding`]](../package_reference/sparse_encoder/models.html#sentence_transformers.sparse_encoder.models.SparseStaticEmbedding "sentence_transformers.sparse_encoder.models.SparseStaticEmbedding")

    2.  [[`MLMTransformer`]](../package_reference/sparse_encoder/models.html#sentence_transformers.sparse_encoder.models.MLMTransformer "sentence_transformers.sparse_encoder.models.MLMTransformer")

    3.  [[`SpladePooling`]](../package_reference/sparse_encoder/models.html#sentence_transformers.sparse_encoder.models.SpladePooling "sentence_transformers.sparse_encoder.models.SpladePooling")

    4.  [[`Router`]](../package_reference/sentence_transformer/models.html#sentence_transformers.models.Router "sentence_transformers.models.Router")

2.  [[`SparseEncoderModelCardData`]](../package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.model_card.SparseEncoderModelCardData "sentence_transformers.sparse_encoder.model_card.SparseEncoderModelCardData")

3.  [[`load_dataset()`]](https://huggingface.co/docs/datasets/main/en/package_reference/loading_methods#datasets.load_dataset "(in datasets vmain)")

4.  [[`SparseMultipleNegativesRankingLoss`]](../package_reference/sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.SparseMultipleNegativesRankingLoss "sentence_transformers.sparse_encoder.losses.SparseMultipleNegativesRankingLoss")

5.  [[`SparseEncoderTrainingArguments`]](../package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments "sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments")

6.  [[`SparseTripletEvaluator`]](../package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.SparseTripletEvaluator "sentence_transformers.sparse_encoder.evaluation.SparseTripletEvaluator")

7.  [[`SparseEncoderTrainer`]](../package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer "sentence_transformers.sparse_encoder.trainer.SparseEncoderTrainer")

8.  [[`SparseEncoder.save_pretrained`]](../package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder.save_pretrained "sentence_transformers.sparse_encoder.SparseEncoder.save_pretrained")

9.  [[`SparseEncoder.push_to_hub`]](../package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder.push_to_hub "sentence_transformers.sparse_encoder.SparseEncoder.push_to_hub")

- [Training Examples](training/examples.html)

    import logging

    from datasets import load_dataset

    from sentence_transformers import (
        SparseEncoder,
        SparseEncoderModelCardData,
        SparseEncoderTrainer,
        SparseEncoderTrainingArguments,
    )
    from sentence_transformers.models import Router
    from sentence_transformers.sparse_encoder.evaluation import SparseNanoBEIREvaluator
    from sentence_transformers.sparse_encoder.losses import SparseMultipleNegativesRankingLoss, SpladeLoss
    from sentence_transformers.sparse_encoder.models import MLMTransformer, SparseStaticEmbedding, SpladePooling
    from sentence_transformers.training_args import BatchSamplers

    logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=logging.INFO)

    # 1. Load a model to finetune with 2. (Optional) model card data
    mlm_transformer = MLMTransformer("distilbert/distilbert-base-uncased", tokenizer_args=)
    splade_pooling = SpladePooling(
        pooling_strategy="max", word_embedding_dimension=mlm_transformer.get_sentence_embedding_dimension()
    )
    router = Router.for_query_document(
        query_modules=[SparseStaticEmbedding(tokenizer=mlm_transformer.tokenizer, frozen=False)],
        document_modules=[mlm_transformer, splade_pooling],
    )

    model = SparseEncoder(
        modules=[router],
        model_card_data=SparseEncoderModelCardData(
            language="en",
            license="apache-2.0",
            model_name="Inference-free SPLADE distilbert-base-uncased trained on Natural-Questions tuples",
        ),
    )

    # 3. Load a dataset to finetune on
    full_dataset = load_dataset("sentence-transformers/natural-questions", split="train").select(range(100_000))
    dataset_dict = full_dataset.train_test_split(test_size=1_000, seed=12)
    train_dataset = dataset_dict["train"]
    eval_dataset = dataset_dict["test"]
    print(train_dataset)
    print(train_dataset[0])

    # 4. Define a loss function
    loss = SpladeLoss(
        model=model,
        loss=SparseMultipleNegativesRankingLoss(model=model),
        query_regularizer_weight=0,
        document_regularizer_weight=3e-4,
    )

    # 5. (Optional) Specify training arguments
    run_name = "inference-free-splade-distilbert-base-uncased-nq"
    args = SparseEncoderTrainingArguments(
        # Required parameter:
        output_dir=f"models/",
        # Optional training parameters:
        num_train_epochs=1,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        learning_rate=2e-5,
        learning_rate_mapping=,  # Set a higher learning rate for the SparseStaticEmbedding module
        warmup_ratio=0.1,
        fp16=True,  # Set to False if you get an error that your GPU can't run on FP16
        bf16=False,  # Set to True if you have a GPU that supports BF16
        batch_sampler=BatchSamplers.NO_DUPLICATES,  # MultipleNegativesRankingLoss benefits from no duplicate samples in a batch
        router_mapping=,  # Map the column names to the routes
        # Optional tracking/debugging parameters:
        eval_strategy="steps",
        eval_steps=1000,
        save_strategy="steps",
        save_steps=1000,
        save_total_limit=2,
        logging_steps=200,
        run_name=run_name,  # Will be used in W&B if `wandb` is installed
    )

    # 6. (Optional) Create an evaluator & evaluate the base model
    dev_evaluator = SparseNanoBEIREvaluator(dataset_names=["msmarco", "nfcorpus", "nq"], batch_size=16)

    # 7. Create a trainer & train
    trainer = SparseEncoderTrainer(
        model=model,
        args=args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        loss=loss,
        evaluator=dev_evaluator,
    )
    trainer.train()

    # 8. Evaluate the model performance again after training
    dev_evaluator(model)

    # 9. Save the trained model
    model.save_pretrained(f"models//final")

    # 10. (Optional) Push it to the Hugging Face Hub
    model.push_to_hub(run_name)

### Callbacks[ïƒ?](#callbacks "Link to this heading")

This Sparse Encoder trainer integrates support for various [[`transformers.TrainerCallback`]](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.TrainerCallback "(in transformers vmain)") subclasses, such as:

- [[`SpladeRegularizerWeightSchedulerCallback`]](../package_reference/sparse_encoder/callbacks.html#sentence_transformers.sparse_encoder.callbacks.splade_callbacks.SpladeRegularizerWeightSchedulerCallback "sentence_transformers.sparse_encoder.callbacks.splade_callbacks.SpladeRegularizerWeightSchedulerCallback") to schedule the lambda parameters of the [[`SpladeLoss`]](../package_reference/sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.SpladeLoss "sentence_transformers.sparse_encoder.losses.SpladeLoss") loss during training.

- [[`WandbCallback`]](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.integrations.WandbCallback "(in transformers vmain)") to automatically log training metrics to W&B if [`wandb`] is installed

- [[`TensorBoardCallback`]](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.integrations.TensorBoardCallback "(in transformers vmain)") to log training metrics to TensorBoard if [`tensorboard`] is accessible.

- [[`CodeCarbonCallback`]](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.integrations.CodeCarbonCallback "(in transformers vmain)") to track the carbon emissions of your model during training if [`codecarbon`] is installed.

  > ::: 
  > - Note: These carbon emissions will be included in your automatically generated model card.
  > :::

See the Transformers [Callbacks](https://huggingface.co/docs/transformers/main/en/main_classes/callback) documentation for more information on the integrated callbacks and how to write your own callbacks.

## Multi-Dataset Training[ïƒ?](#multi-dataset-training "Link to this heading")

The top performing models are trained using many datasets at once. Normally, this is rather tricky, as each dataset has a different format. However, [[`SparseEncoderTrainer`]](../package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer "sentence_transformers.sparse_encoder.trainer.SparseEncoderTrainer") can train with multiple datasets without having to convert each dataset to the same format. It can even apply different loss functions to each of the datasets. The steps to train with multiple datasets are:

- Use a dictionary of [[`Dataset`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)") instances (or a [[`DatasetDict`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.DatasetDict "(in datasets vmain)")) as the [`train_dataset`] (and optionally also [`eval_dataset`]).

- (Optional) Use a dictionary of loss functions mapping dataset names to losses. Only required if you wish to use different loss function for different datasets.

Each training/evaluation batch will only contain samples from one of the datasets. The order in which batches are samples from the multiple datasets is defined by the [[`MultiDatasetBatchSamplers`]](../package_reference/sentence_transformer/sampler.html#sentence_transformers.training_args.MultiDatasetBatchSamplers "sentence_transformers.training_args.MultiDatasetBatchSamplers") enum, which can be passed to the [[`SparseEncoderTrainingArguments`]](../package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments "sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments") via [`multi_dataset_batch_sampler`]. Valid options are:

- [`MultiDatasetBatchSamplers.ROUND_ROBIN`]: Round-robin sampling from each dataset until one is exhausted. With this strategy, itâ€™s likely that not all samples from each dataset are used, but each dataset is sampled from equally.

- [`MultiDatasetBatchSamplers.PROPORTIONAL`] (default): Sample from each dataset in proportion to its size. With this strategy, all samples from each dataset are used and larger datasets are sampled from more frequently.

## Training Tips[ïƒ?](#training-tips "Link to this heading")

Sparse Encoder models have a few quirks that you should be aware of when training them:

1.  Sparse Encoder models should not be evaluated solely using the evaluation scores, but also with the sparsity of the embeddings. After all, a low sparsity means that the model embeddings are expensive to store and slow to retrieve. This also means that the parameters that determine sparsity (e.g. [`query_regularizer_weight`], [`document_regularizer_weight`] in [[`SpladeLoss`]](../package_reference/sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.SpladeLoss "sentence_transformers.sparse_encoder.losses.SpladeLoss") and [`beta`] and [`gamma`] in the [[`CSRLoss`]](../package_reference/sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.CSRLoss "sentence_transformers.sparse_encoder.losses.CSRLoss")) should be tuned to achieve a good balance between performance and sparsity. Each [Evaluator](../package_reference/sparse_encoder/evaluation.html) outputs the [`active_dims`] and [`sparsity_ratio`] metrics that can be used to assess the sparsity of the embeddings.

2.  It is not recommended to use an [Evaluator](../package_reference/sparse_encoder/evaluation.html) on an untrained model prior to training, as the sparsity will be very low, and so the memory usage might be unexpectedly high.

3.  The stronger Sparse Encoder models are trained almost exclusively with distillation from a stronger teacher model (e.g. a [CrossEncoder model](../cross_encoder/usage/usage.html)), instead of training directly from text pairs or triplets. See for example the [SPLADE-v3 paper](https://huggingface.co/papers/2403.06789), which uses [[`SparseDistillKLDivLoss`]](../package_reference/sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.SparseDistillKLDivLoss "sentence_transformers.sparse_encoder.losses.SparseDistillKLDivLoss") and [[`SparseMarginMSELoss`]](../package_reference/sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.SparseMarginMSELoss "sentence_transformers.sparse_encoder.losses.SparseMarginMSELoss") for distillation.

4.  Whereas the majority of dense embedding models are trained to be used with cosine similarity, [[`SparseEncoder`]](../package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder") models are commonly trained to be used with dot product to compute similarity. Some losses require you to provide a similarity function, and you might be better off using dot product there. Note that you can often provide the loss with [[`model.similarity`]](../package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder.similarity "sentence_transformers.sparse_encoder.SparseEncoder.similarity") or [[`model.similarity_pairwise`]](../package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder.similarity_pairwise "sentence_transformers.sparse_encoder.SparseEncoder.similarity_pairwise").