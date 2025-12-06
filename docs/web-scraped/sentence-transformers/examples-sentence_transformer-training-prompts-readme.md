# Source: https://www.sbert.net/examples/sentence_transformer/training/prompts/README.html

# Training with Prompts[ïƒ?](#training-with-prompts "Link to this heading")

## What are Prompts?[ïƒ?](#what-are-prompts "Link to this heading")

Many modern embedding models are trained with â€œinstructionsâ€? or â€œpromptsâ€? following the [INSTRUCTOR paper](https://huggingface.co/papers/2212.09741). These prompts are strings, prefixed to each text to be embedded, allowing the model to distinguish between different types of text.

For example, the [mixedbread-ai/mxbai-embed-large-v1](https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1) model was trained with [`Represent`]` `[`this`]` `[`sentence`]` `[`for`]` `[`searching`]` `[`relevant`]` `[`passages:`]` ` as the prompt for all queries. This prompt is stored in the [model configuration](https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1/blob/main/config_sentence_transformers.json) under the prompt name [`"query"`], so users can specify that [`prompt_name`] in [`model.encode`]:

    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer("mixedbread-ai/mxbai-embed-large-v1")
    query_embedding = model.encode("What are Pandas?", prompt_name="query")
    # or
    # query_embedding = model.encode("What are Pandas?", prompt="Represent this sentence for searching relevant passages: ")
    document_embeddings = model.encode([
        "Pandas is a software library written for the Python programming language for data manipulation and analysis.",
        "Pandas are a species of bear native to South Central China. They are also known as the giant panda or simply panda.",
        "Koala bears are not actually bears, they are marsupials native to Australia.",
    ])
    similarity = model.similarity(query_embedding, document_embeddings)
    print(similarity)
    # => tensor([[0.7594, 0.7560, 0.4674]])

See [Prompt Templates](https://sbert.net/examples/applications/computing-embeddings/README.html#prompt-templates) for more information about inference with prompts.

## Why would we train with Prompts?[ïƒ?](#why-would-we-train-with-prompts "Link to this heading")

The [INSTRUCTOR paper](https://huggingface.co/papers/2212.09741) showed that adding prompts or instructions before each text could improve model performance by an average of \~6%, with major gains especially for classification, clustering, and semantic textual similarity. Note that the performance improvements for retrieval are notably lower at 0.4% and 2.7% for small and large models, respectively.

![instructor results](https://huggingface.co/tomaarsen/mpnet-base-nq-prompts/resolve/main/instructor.png)

More recently, the [BGE paper](https://huggingface.co/papers/2309.07597) showed similar findings, showing about a 1.4% performance increase for retrieval if the query is prefixed with [`Represent`]` `[`this`]` `[`sentence`]` `[`for`]` `[`searching`]` `[`relevant`]` `[`passages:`]` `. The authors conclude that using instructions may substantially contribute to the quality of task-specific fine-tuning.

![bge results](https://huggingface.co/tomaarsen/mpnet-base-nq-prompts/resolve/main/bge.png)

In essence, using instructions or prompts allows for improved performance as long as they are used both during training and inference.

## How do we train with Prompts?[ïƒ?](#how-do-we-train-with-prompts "Link to this heading")

Since the v3.3.0 Sentence Transformers release, itâ€™s possible to finetune embedding models with prompts using the [`prompts`] argument in the [[`SentenceTransformerTrainingArguments`]](../../../../docs/package_reference/sentence_transformer/training_args.html#sentence_transformers.training_args.SentenceTransformerTrainingArguments "sentence_transformers.training_args.SentenceTransformerTrainingArguments") class. There are 4 separate accepted formats for this argument:

1.  [`str`]: A single prompt to use for all columns in all datasets. For example:

    :::: 
    ::: highlight
        args = SentenceTransformerTrainingArguments(
            ...,
            prompts="text: ",
            ...,
        )
    :::
    ::::

2.  [`Dict[str,`]` `[`str]`]: A dictionary mapping column names to prompts, applied to all datasets. For example:

    :::: 
    ::: highlight
        args = SentenceTransformerTrainingArguments(
            ...,
            prompts=,
            ...,
        )
    :::
    ::::

3.  [`Dict[str,`]` `[`str]`]: A dictionary mapping dataset names to prompts. This should only be used if your training/evaluation/test datasets are a [[`DatasetDict`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.DatasetDict "(in datasets vmain)") or a dictionary of [[`Dataset`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)"). For example:

    :::: 
    ::: highlight
        args = SentenceTransformerTrainingArguments(
            ...,
            prompts=,
            ...,
        )
    :::
    ::::

4.  [`Dict[str,`]` `[`Dict[str,`]` `[`str]]`]: A dictionary mapping dataset names to dictionaries mapping column names to prompts. This should only be used if your training/evaluation/test datasets are a [[`DatasetDict`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.DatasetDict "(in datasets vmain)") or a dictionary of [[`Dataset`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)"). For example:

    :::: 
    ::: highlight
        args = SentenceTransformerTrainingArguments(
            ...,
            prompts=,
                "nq": ,
            },
            ...,
        )
    :::
    ::::

Additionally, some research papers ([INSTRUCTOR](https://huggingface.co/papers/2212.09741), [NV-Embed](https://huggingface.co/papers/2405.17428)) exclude the prompt from the mean pooling step, such that itâ€™s only used in the Transformer blocks. In Sentence Transformers, this can be configured with the [`include_prompt`] argument/attribute in the [[`Pooling`]](../../../../docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Pooling "sentence_transformers.models.Pooling") module or via the [[`SentenceTransformer.set_pooling_include_prompt()`]](../../../../docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.set_pooling_include_prompt "sentence_transformers.SentenceTransformer.set_pooling_include_prompt") method. In my personal experience, models that include the prompt in the pooling tend to perform better.

### Training Script[ïƒ?](#training-script "Link to this heading")

See the following script as an example of how to train with prompts in practice:

- [training_nq_prompts.py](https://github.com/huggingface/sentence-transformers/blob/master/examples/sentence_transformer/training/prompts/training_nq_prompts.py): This script finetunes [mpnet-base](https://huggingface.co/microsoft/mpnet-base) on 100k query-answer pairs from the [natural-questions](https://huggingface.co/datasets/sentence-transformers/natural-questions) dataset using the [[`CachedMultipleNegativesRankingLoss`]](../../../../docs/package_reference/sentence_transformer/losses.html#sentence_transformers.losses.CachedMultipleNegativesRankingLoss "sentence_transformers.losses.CachedMultipleNegativesRankingLoss") loss. The model is evaluated during training using the [[`NanoBEIREvaluator`]](../../../../docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.NanoBEIREvaluator "sentence_transformers.evaluation.NanoBEIREvaluator").

This script has two variables that affect 1) whether prompts are used and 2) whether prompts are included in the pooling. I have finetuned both [`mpnet-base`] and [`bert-base-uncased`] under the various different settings, resulting in a 0.66% and 0.90% relative improvements on [`NDCG@10`] at no extra cost.

Experiments with [`mpnet-base`]

Running the script under various settings resulted in these checkpoints:

- [tomaarsen/mpnet-base-nq](https://huggingface.co/tomaarsen/mpnet-base-nq)

- [tomaarsen/mpnet-base-nq-prompts](https://huggingface.co/tomaarsen/mpnet-base-nq-prompts)

Note

[`mpnet-base`] seems to be a tad unstable when training with prompts and excluding those prompts in the pooling: the loss spikes at some point, an effect not observed with e.g. [`bert-base-uncased`].

For these two models, the model trained with prompts consistently outperforms the baseline model all throughout training:

![NanoBEIR results of mpnet-base-nq vs mpnet-base-nq-prompts](https://huggingface.co/tomaarsen/mpnet-base-nq-prompts/resolve/main/mpnet_base_nq_nanobeir.png)

Additionally, the model trained with prompts includes these prompts in the training dataset details in the automatically generated model card: [tomaarsen/mpnet-base-nq-prompts#natural-questions](https://huggingface.co/tomaarsen/mpnet-base-nq-prompts#natural-questions).

Important

If you train with prompts, then itâ€™s heavily recommended to store prompts in the model configuration as a mapping of prompt names to prompt strings. You can do this by initializing the [[`SentenceTransformer`]](../../../../docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer") with a [`prompts`] dictionary before saving it, updating the [`model.prompts`] of a loaded model before saving it, and/or updating the [config_sentence_transformers.json](https://huggingface.co/tomaarsen/mpnet-base-nq-prompts/blob/main/config_sentence_transformers.json) file of the saved model.

After adding the prompts in the model configuration, the final usage of the prompt-trained model becomes:

    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer("tomaarsen/mpnet-base-nq-prompts")
    query_embedding = model.encode("What are Pandas?", prompt_name="query")
    document_embeddings = model.encode([
        "Pandas is a software library written for the Python programming language for data manipulation and analysis.",
        "Pandas are a species of bear native to South Central China. They are also known as the giant panda or simply panda.",
        "Koala bears are not actually bears, they are marsupials native to Australia.",
        ],
        prompt_name="document",
    )
    similarity = model.similarity(query_embedding, document_embeddings)
    print(similarity)
    # => tensor([[0.4725, 0.7339, 0.4369]])

Experiments with [`bert-base-uncased`]

Running the script under various settings resulted in these checkpoints:

- [tomaarsen/bert-base-nq](https://huggingface.co/tomaarsen/bert-base-nq)

- [tomaarsen/bert-base-nq-prompts](https://huggingface.co/tomaarsen/bert-base-nq-prompts)

- [tomaarsen/bert-base-nq-prompts-exclude-pooling-prompts](https://huggingface.co/tomaarsen/bert-base-nq-prompts-exclude-pooling-prompts)

For these three models, the model trained with prompts consistently outperforms the baseline model all throughout training, except for the very first evaluation. The model that excludes the prompt in the mean pooling consistently performs notably worse than either of the other two.

![NanoBEIR results](https://huggingface.co/tomaarsen/mpnet-base-nq-prompts/resolve/main/bert_base_nq_nanobeir.png)

Additionally, the model trained with prompts includes these prompts in the training dataset details in the automatically generated model card: [tomaarsen/bert-base-nq-prompts#natural-questions](https://huggingface.co/tomaarsen/bert-base-nq-prompts#natural-questions).

Important

If you train with prompts, then itâ€™s heavily recommended to store prompts in the model configuration as a mapping of prompt names to prompt strings. You can do this by initializing the [[`SentenceTransformer`]](../../../../docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer") with a [`prompts`] dictionary before saving it, updating the [`model.prompts`] of a loaded model before saving it, and/or updating the [config_sentence_transformers.json](https://huggingface.co/tomaarsen/mpnet-base-nq-prompts/blob/main/config_sentence_transformers.json) file of the saved model.

After adding the prompts in the model configuration, the final usage of the prompt-trained model becomes:

    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer("tomaarsen/bert-base-nq-prompts")
    query_embedding = model.encode("What are Pandas?", prompt_name="query")
    document_embeddings = model.encode([
        "Pandas is a software library written for the Python programming language for data manipulation and analysis.",
        "Pandas are a species of bear native to South Central China. They are also known as the giant panda or simply panda.",
        "Koala bears are not actually bears, they are marsupials native to Australia.",
        ],
        prompt_name="document",
    )
    similarity = model.similarity(query_embedding, document_embeddings)
    print(similarity)
    # => tensor([[0.3955, 0.8226, 0.5706]])