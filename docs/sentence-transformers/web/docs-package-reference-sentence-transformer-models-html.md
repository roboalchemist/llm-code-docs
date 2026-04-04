# Source: https://sbert.net/docs/package_reference/sentence_transformer/models.html

Title: Modules — Sentence Transformers documentation

URL Source: https://sbert.net/docs/package_reference/sentence_transformer/models.html

Published Time: Tue, 17 Feb 2026 14:05:52 GMT

Markdown Content:
Modules — Sentence Transformers documentation
===============

[![Image 1: Logo](https://sbert.net/_static/logo.png)](https://sbert.net/index.html)

Getting Started

*   [Installation](https://sbert.net/docs/installation.html)
    *   [Install with pip](https://sbert.net/docs/installation.html#install-with-pip)
    *   [Install with Conda](https://sbert.net/docs/installation.html#install-with-conda)
    *   [Install from Source](https://sbert.net/docs/installation.html#install-from-source)
    *   [Editable Install](https://sbert.net/docs/installation.html#editable-install)
    *   [Install PyTorch with CUDA support](https://sbert.net/docs/installation.html#install-pytorch-with-cuda-support)

*   [Quickstart](https://sbert.net/docs/quickstart.html)
    *   [Sentence Transformer](https://sbert.net/docs/quickstart.html#sentence-transformer)
    *   [Cross Encoder](https://sbert.net/docs/quickstart.html#cross-encoder)
    *   [Sparse Encoder](https://sbert.net/docs/quickstart.html#sparse-encoder)
    *   [Next Steps](https://sbert.net/docs/quickstart.html#next-steps)

*   [Migration Guide](https://sbert.net/docs/migration_guide.html)
    *   [Migrating from v4.x to v5.x](https://sbert.net/docs/migration_guide.html#migrating-from-v4-x-to-v5-x)
        *   [Migration for model.encode](https://sbert.net/docs/migration_guide.html#migration-for-model-encode)
        *   [Migration for Asym to Router](https://sbert.net/docs/migration_guide.html#migration-for-asym-to-router)
        *   [Migration of advanced usage](https://sbert.net/docs/migration_guide.html#migration-of-advanced-usage)

    *   [Migrating from v3.x to v4.x](https://sbert.net/docs/migration_guide.html#migrating-from-v3-x-to-v4-x)
        *   [Migration for parameters on `CrossEncoder` initialization and methods](https://sbert.net/docs/migration_guide.html#migration-for-parameters-on-crossencoder-initialization-and-methods)
        *   [Migration for specific parameters from `CrossEncoder.fit`](https://sbert.net/docs/migration_guide.html#migration-for-specific-parameters-from-crossencoder-fit)
        *   [Migration for CrossEncoder evaluators](https://sbert.net/docs/migration_guide.html#migration-for-crossencoder-evaluators)

    *   [Migrating from v2.x to v3.x](https://sbert.net/docs/migration_guide.html#migrating-from-v2-x-to-v3-x)
        *   [Migration for specific parameters from `SentenceTransformer.fit`](https://sbert.net/docs/migration_guide.html#migration-for-specific-parameters-from-sentencetransformer-fit)
        *   [Migration for custom Datasets and DataLoaders used in `SentenceTransformer.fit`](https://sbert.net/docs/migration_guide.html#migration-for-custom-datasets-and-dataloaders-used-in-sentencetransformer-fit)

Sentence Transformer

*   [Usage](https://sbert.net/docs/sentence_transformer/usage/usage.html)
    *   [Computing Embeddings](https://sbert.net/examples/sentence_transformer/applications/computing-embeddings/README.html)
        *   [Initializing a Sentence Transformer Model](https://sbert.net/examples/sentence_transformer/applications/computing-embeddings/README.html#initializing-a-sentence-transformer-model)
        *   [Calculating Embeddings](https://sbert.net/examples/sentence_transformer/applications/computing-embeddings/README.html#calculating-embeddings)
        *   [Prompt Templates](https://sbert.net/examples/sentence_transformer/applications/computing-embeddings/README.html#prompt-templates)
        *   [Input Sequence Length](https://sbert.net/examples/sentence_transformer/applications/computing-embeddings/README.html#input-sequence-length)
        *   [Multi-Process / Multi-GPU Encoding](https://sbert.net/examples/sentence_transformer/applications/computing-embeddings/README.html#multi-process-multi-gpu-encoding)

    *   [Semantic Textual Similarity](https://sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html)
        *   [Similarity Calculation](https://sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html#similarity-calculation)

    *   [Semantic Search](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html)
        *   [Background](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html#background)
        *   [Symmetric vs. Asymmetric Semantic Search](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html#symmetric-vs-asymmetric-semantic-search)
        *   [Manual Implementation](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html#manual-implementation)
        *   [Optimized Implementation](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html#optimized-implementation)
        *   [Speed Optimization](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html#speed-optimization)
        *   [Elasticsearch](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html#elasticsearch)
        *   [OpenSearch](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html#opensearch)
        *   [Approximate Nearest Neighbor](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html#approximate-nearest-neighbor)
        *   [Retrieve & Re-Rank](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html#retrieve-re-rank)
        *   [Examples](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html#examples)

    *   [Retrieve & Re-Rank](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html)
        *   [Retrieve & Re-Rank Pipeline](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html#retrieve-re-rank-pipeline)
        *   [Retrieval: Bi-Encoder](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html#retrieval-bi-encoder)
        *   [Re-Ranker: Cross-Encoder](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html#re-ranker-cross-encoder)
        *   [Example Scripts](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html#example-scripts)
        *   [Pre-trained Bi-Encoders (Retrieval)](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html#pre-trained-bi-encoders-retrieval)
        *   [Pre-trained Cross-Encoders (Re-Ranker)](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html#pre-trained-cross-encoders-re-ranker)

    *   [Clustering](https://sbert.net/examples/sentence_transformer/applications/clustering/README.html)
        *   [k-Means](https://sbert.net/examples/sentence_transformer/applications/clustering/README.html#k-means)
        *   [Agglomerative Clustering](https://sbert.net/examples/sentence_transformer/applications/clustering/README.html#agglomerative-clustering)
        *   [Fast Clustering](https://sbert.net/examples/sentence_transformer/applications/clustering/README.html#fast-clustering)
        *   [Topic Modeling](https://sbert.net/examples/sentence_transformer/applications/clustering/README.html#topic-modeling)

    *   [Paraphrase Mining](https://sbert.net/examples/sentence_transformer/applications/paraphrase-mining/README.html)
        *   [`paraphrase_mining()`](https://sbert.net/examples/sentence_transformer/applications/paraphrase-mining/README.html#sentence_transformers.util.paraphrase_mining)

    *   [Translated Sentence Mining](https://sbert.net/examples/sentence_transformer/applications/parallel-sentence-mining/README.html)
        *   [Margin Based Mining](https://sbert.net/examples/sentence_transformer/applications/parallel-sentence-mining/README.html#margin-based-mining)
        *   [Examples](https://sbert.net/examples/sentence_transformer/applications/parallel-sentence-mining/README.html#examples)

    *   [Image Search](https://sbert.net/examples/sentence_transformer/applications/image-search/README.html)
        *   [Installation](https://sbert.net/examples/sentence_transformer/applications/image-search/README.html#installation)
        *   [Usage](https://sbert.net/examples/sentence_transformer/applications/image-search/README.html#usage)
        *   [Examples](https://sbert.net/examples/sentence_transformer/applications/image-search/README.html#examples)

    *   [Embedding Quantization](https://sbert.net/examples/sentence_transformer/applications/embedding-quantization/README.html)
        *   [Binary Quantization](https://sbert.net/examples/sentence_transformer/applications/embedding-quantization/README.html#binary-quantization)
        *   [Scalar (int8) Quantization](https://sbert.net/examples/sentence_transformer/applications/embedding-quantization/README.html#scalar-int8-quantization)
        *   [Additional extensions](https://sbert.net/examples/sentence_transformer/applications/embedding-quantization/README.html#additional-extensions)
        *   [Demo](https://sbert.net/examples/sentence_transformer/applications/embedding-quantization/README.html#demo)
        *   [Try it yourself](https://sbert.net/examples/sentence_transformer/applications/embedding-quantization/README.html#try-it-yourself)

    *   [Creating Custom Models](https://sbert.net/docs/sentence_transformer/usage/custom_models.html)
        *   [Structure of Sentence Transformer Models](https://sbert.net/docs/sentence_transformer/usage/custom_models.html#structure-of-sentence-transformer-models)
        *   [Sentence Transformer Model from a Transformers Model](https://sbert.net/docs/sentence_transformer/usage/custom_models.html#sentence-transformer-model-from-a-transformers-model)
        *   [Advanced: Custom Modules](https://sbert.net/docs/sentence_transformer/usage/custom_models.html#advanced-custom-modules)

    *   [Evaluation with MTEB](https://sbert.net/docs/sentence_transformer/usage/mteb_evaluation.html)
        *   [Installation](https://sbert.net/docs/sentence_transformer/usage/mteb_evaluation.html#installation)
        *   [Evaluation](https://sbert.net/docs/sentence_transformer/usage/mteb_evaluation.html#evaluation)
        *   [Additional Arguments](https://sbert.net/docs/sentence_transformer/usage/mteb_evaluation.html#additional-arguments)
        *   [Results Handling](https://sbert.net/docs/sentence_transformer/usage/mteb_evaluation.html#results-handling)
        *   [Leaderboard Submission](https://sbert.net/docs/sentence_transformer/usage/mteb_evaluation.html#leaderboard-submission)

    *   [Speeding up Inference](https://sbert.net/docs/sentence_transformer/usage/efficiency.html)
        *   [PyTorch](https://sbert.net/docs/sentence_transformer/usage/efficiency.html#pytorch)
        *   [ONNX](https://sbert.net/docs/sentence_transformer/usage/efficiency.html#onnx)
        *   [OpenVINO](https://sbert.net/docs/sentence_transformer/usage/efficiency.html#openvino)
        *   [Benchmarks](https://sbert.net/docs/sentence_transformer/usage/efficiency.html#benchmarks)

*   [Pretrained Models](https://sbert.net/docs/sentence_transformer/pretrained_models.html)
    *   [Original Models](https://sbert.net/docs/sentence_transformer/pretrained_models.html#original-models)
    *   [Semantic Search Models](https://sbert.net/docs/sentence_transformer/pretrained_models.html#semantic-search-models)
        *   [Multi-QA Models](https://sbert.net/docs/sentence_transformer/pretrained_models.html#multi-qa-models)
        *   [MSMARCO Passage Models](https://sbert.net/docs/sentence_transformer/pretrained_models.html#msmarco-passage-models)

    *   [Multilingual Models](https://sbert.net/docs/sentence_transformer/pretrained_models.html#multilingual-models)
        *   [Semantic Similarity Models](https://sbert.net/docs/sentence_transformer/pretrained_models.html#semantic-similarity-models)
        *   [Bitext Mining](https://sbert.net/docs/sentence_transformer/pretrained_models.html#bitext-mining)

    *   [Image & Text-Models](https://sbert.net/docs/sentence_transformer/pretrained_models.html#image-text-models)
    *   [INSTRUCTOR models](https://sbert.net/docs/sentence_transformer/pretrained_models.html#instructor-models)
    *   [Scientific Similarity Models](https://sbert.net/docs/sentence_transformer/pretrained_models.html#scientific-similarity-models)

*   [Training Overview](https://sbert.net/docs/sentence_transformer/training_overview.html)
    *   [Why Finetune?](https://sbert.net/docs/sentence_transformer/training_overview.html#why-finetune)
    *   [Training Components](https://sbert.net/docs/sentence_transformer/training_overview.html#training-components)
    *   [Model](https://sbert.net/docs/sentence_transformer/training_overview.html#model)
    *   [Dataset](https://sbert.net/docs/sentence_transformer/training_overview.html#dataset)
        *   [Dataset Format](https://sbert.net/docs/sentence_transformer/training_overview.html#dataset-format)

    *   [Loss Function](https://sbert.net/docs/sentence_transformer/training_overview.html#loss-function)
    *   [Training Arguments](https://sbert.net/docs/sentence_transformer/training_overview.html#training-arguments)
    *   [Evaluator](https://sbert.net/docs/sentence_transformer/training_overview.html#evaluator)
    *   [Trainer](https://sbert.net/docs/sentence_transformer/training_overview.html#trainer)
        *   [Callbacks](https://sbert.net/docs/sentence_transformer/training_overview.html#callbacks)

    *   [Multi-Dataset Training](https://sbert.net/docs/sentence_transformer/training_overview.html#multi-dataset-training)
    *   [Deprecated Training](https://sbert.net/docs/sentence_transformer/training_overview.html#deprecated-training)
    *   [Best Base Embedding Models](https://sbert.net/docs/sentence_transformer/training_overview.html#best-base-embedding-models)
    *   [Comparisons with CrossEncoder Training](https://sbert.net/docs/sentence_transformer/training_overview.html#comparisons-with-crossencoder-training)

*   [Dataset Overview](https://sbert.net/docs/sentence_transformer/dataset_overview.html)
    *   [Datasets on the Hugging Face Hub](https://sbert.net/docs/sentence_transformer/dataset_overview.html#datasets-on-the-hugging-face-hub)
    *   [Pre-existing Datasets](https://sbert.net/docs/sentence_transformer/dataset_overview.html#pre-existing-datasets)

*   [Loss Overview](https://sbert.net/docs/sentence_transformer/loss_overview.html)
    *   [Loss Table](https://sbert.net/docs/sentence_transformer/loss_overview.html#loss-table)
    *   [Loss modifiers](https://sbert.net/docs/sentence_transformer/loss_overview.html#loss-modifiers)
    *   [Distillation](https://sbert.net/docs/sentence_transformer/loss_overview.html#distillation)
    *   [Commonly used Loss Functions](https://sbert.net/docs/sentence_transformer/loss_overview.html#commonly-used-loss-functions)
    *   [Custom Loss Functions](https://sbert.net/docs/sentence_transformer/loss_overview.html#custom-loss-functions)

*   [Training Examples](https://sbert.net/docs/sentence_transformer/training/examples.html)
    *   [Semantic Textual Similarity](https://sbert.net/examples/sentence_transformer/training/sts/README.html)
        *   [Training data](https://sbert.net/examples/sentence_transformer/training/sts/README.html#training-data)
        *   [Loss Function](https://sbert.net/examples/sentence_transformer/training/sts/README.html#loss-function)

    *   [Natural Language Inference](https://sbert.net/examples/sentence_transformer/training/nli/README.html)
        *   [Data](https://sbert.net/examples/sentence_transformer/training/nli/README.html#data)
        *   [SoftmaxLoss](https://sbert.net/examples/sentence_transformer/training/nli/README.html#softmaxloss)
        *   [MultipleNegativesRankingLoss](https://sbert.net/examples/sentence_transformer/training/nli/README.html#multiplenegativesrankingloss)

    *   [Paraphrase Data](https://sbert.net/examples/sentence_transformer/training/paraphrases/README.html)
        *   [Pre-Trained Models](https://sbert.net/examples/sentence_transformer/training/paraphrases/README.html#pre-trained-models)

    *   [Quora Duplicate Questions](https://sbert.net/examples/sentence_transformer/training/quora_duplicate_questions/README.html)
        *   [Training](https://sbert.net/examples/sentence_transformer/training/quora_duplicate_questions/README.html#training)
        *   [MultipleNegativesRankingLoss](https://sbert.net/examples/sentence_transformer/training/quora_duplicate_questions/README.html#multiplenegativesrankingloss)
        *   [Pretrained Models](https://sbert.net/examples/sentence_transformer/training/quora_duplicate_questions/README.html#pretrained-models)

    *   [MS MARCO](https://sbert.net/examples/sentence_transformer/training/ms_marco/README.html)
        *   [Bi-Encoder](https://sbert.net/examples/sentence_transformer/training/ms_marco/README.html#bi-encoder)

    *   [Matryoshka Embeddings](https://sbert.net/examples/sentence_transformer/training/matryoshka/README.html)
        *   [Use Cases](https://sbert.net/examples/sentence_transformer/training/matryoshka/README.html#use-cases)
        *   [Results](https://sbert.net/examples/sentence_transformer/training/matryoshka/README.html#results)
        *   [Training](https://sbert.net/examples/sentence_transformer/training/matryoshka/README.html#training)
        *   [Inference](https://sbert.net/examples/sentence_transformer/training/matryoshka/README.html#inference)
        *   [Code Examples](https://sbert.net/examples/sentence_transformer/training/matryoshka/README.html#code-examples)

    *   [Adaptive Layers](https://sbert.net/examples/sentence_transformer/training/adaptive_layer/README.html)
        *   [Use Cases](https://sbert.net/examples/sentence_transformer/training/adaptive_layer/README.html#use-cases)
        *   [Results](https://sbert.net/examples/sentence_transformer/training/adaptive_layer/README.html#results)
        *   [Training](https://sbert.net/examples/sentence_transformer/training/adaptive_layer/README.html#training)
        *   [Inference](https://sbert.net/examples/sentence_transformer/training/adaptive_layer/README.html#inference)
        *   [Code Examples](https://sbert.net/examples/sentence_transformer/training/adaptive_layer/README.html#code-examples)

    *   [Multilingual Models](https://sbert.net/examples/sentence_transformer/training/multilingual/README.html)
        *   [Extend your own models](https://sbert.net/examples/sentence_transformer/training/multilingual/README.html#extend-your-own-models)
        *   [Training](https://sbert.net/examples/sentence_transformer/training/multilingual/README.html#training)
        *   [Datasets](https://sbert.net/examples/sentence_transformer/training/multilingual/README.html#datasets)
        *   [Sources for Training Data](https://sbert.net/examples/sentence_transformer/training/multilingual/README.html#sources-for-training-data)
        *   [Evaluation](https://sbert.net/examples/sentence_transformer/training/multilingual/README.html#evaluation)
        *   [Available Pre-trained Models](https://sbert.net/examples/sentence_transformer/training/multilingual/README.html#available-pre-trained-models)
        *   [Usage](https://sbert.net/examples/sentence_transformer/training/multilingual/README.html#usage)
        *   [Performance](https://sbert.net/examples/sentence_transformer/training/multilingual/README.html#performance)
        *   [Citation](https://sbert.net/examples/sentence_transformer/training/multilingual/README.html#citation)

    *   [Model Distillation](https://sbert.net/examples/sentence_transformer/training/distillation/README.html)
        *   [Knowledge Distillation](https://sbert.net/examples/sentence_transformer/training/distillation/README.html#knowledge-distillation)
        *   [Speed - Performance Trade-Off](https://sbert.net/examples/sentence_transformer/training/distillation/README.html#speed-performance-trade-off)
        *   [Dimensionality Reduction](https://sbert.net/examples/sentence_transformer/training/distillation/README.html#dimensionality-reduction)
        *   [Quantization](https://sbert.net/examples/sentence_transformer/training/distillation/README.html#quantization)

    *   [Augmented SBERT](https://sbert.net/examples/sentence_transformer/training/data_augmentation/README.html)
        *   [Motivation](https://sbert.net/examples/sentence_transformer/training/data_augmentation/README.html#motivation)
        *   [Extend to your own datasets](https://sbert.net/examples/sentence_transformer/training/data_augmentation/README.html#extend-to-your-own-datasets)
        *   [Methodology](https://sbert.net/examples/sentence_transformer/training/data_augmentation/README.html#methodology)
        *   [Scenario 1: Limited or small annotated datasets (few labeled sentence-pairs)](https://sbert.net/examples/sentence_transformer/training/data_augmentation/README.html#scenario-1-limited-or-small-annotated-datasets-few-labeled-sentence-pairs)
        *   [Scenario 2: No annotated datasets (Only unlabeled sentence-pairs)](https://sbert.net/examples/sentence_transformer/training/data_augmentation/README.html#scenario-2-no-annotated-datasets-only-unlabeled-sentence-pairs)
        *   [Training](https://sbert.net/examples/sentence_transformer/training/data_augmentation/README.html#training)
        *   [Citation](https://sbert.net/examples/sentence_transformer/training/data_augmentation/README.html#citation)

    *   [Training with Prompts](https://sbert.net/examples/sentence_transformer/training/prompts/README.html)
        *   [What are Prompts?](https://sbert.net/examples/sentence_transformer/training/prompts/README.html#what-are-prompts)
        *   [Why would we train with Prompts?](https://sbert.net/examples/sentence_transformer/training/prompts/README.html#why-would-we-train-with-prompts)
        *   [How do we train with Prompts?](https://sbert.net/examples/sentence_transformer/training/prompts/README.html#how-do-we-train-with-prompts)

    *   [Training with PEFT Adapters](https://sbert.net/examples/sentence_transformer/training/peft/README.html)
        *   [Compatibility Methods](https://sbert.net/examples/sentence_transformer/training/peft/README.html#compatibility-methods)
        *   [Adding a New Adapter](https://sbert.net/examples/sentence_transformer/training/peft/README.html#adding-a-new-adapter)
        *   [Loading a Pretrained Adapter](https://sbert.net/examples/sentence_transformer/training/peft/README.html#loading-a-pretrained-adapter)
        *   [Training Script](https://sbert.net/examples/sentence_transformer/training/peft/README.html#training-script)

    *   [Unsupervised Learning](https://sbert.net/examples/sentence_transformer/unsupervised_learning/README.html)
        *   [TSDAE](https://sbert.net/examples/sentence_transformer/unsupervised_learning/README.html#tsdae)
        *   [SimCSE](https://sbert.net/examples/sentence_transformer/unsupervised_learning/README.html#simcse)
        *   [CT](https://sbert.net/examples/sentence_transformer/unsupervised_learning/README.html#ct)
        *   [CT (In-Batch Negative Sampling)](https://sbert.net/examples/sentence_transformer/unsupervised_learning/README.html#ct-in-batch-negative-sampling)
        *   [Masked Language Model (MLM)](https://sbert.net/examples/sentence_transformer/unsupervised_learning/README.html#masked-language-model-mlm)
        *   [GenQ](https://sbert.net/examples/sentence_transformer/unsupervised_learning/README.html#genq)
        *   [GPL](https://sbert.net/examples/sentence_transformer/unsupervised_learning/README.html#gpl)
        *   [Performance Comparison](https://sbert.net/examples/sentence_transformer/unsupervised_learning/README.html#performance-comparison)

    *   [Domain Adaptation](https://sbert.net/examples/sentence_transformer/domain_adaptation/README.html)
        *   [Domain Adaptation vs. Unsupervised Learning](https://sbert.net/examples/sentence_transformer/domain_adaptation/README.html#domain-adaptation-vs-unsupervised-learning)
        *   [Adaptive Pre-Training](https://sbert.net/examples/sentence_transformer/domain_adaptation/README.html#adaptive-pre-training)
        *   [GPL: Generative Pseudo-Labeling](https://sbert.net/examples/sentence_transformer/domain_adaptation/README.html#gpl-generative-pseudo-labeling)

    *   [Hyperparameter Optimization](https://sbert.net/examples/sentence_transformer/training/hpo/README.html)
        *   [HPO Components](https://sbert.net/examples/sentence_transformer/training/hpo/README.html#hpo-components)
        *   [Putting It All Together](https://sbert.net/examples/sentence_transformer/training/hpo/README.html#putting-it-all-together)
        *   [Example Scripts](https://sbert.net/examples/sentence_transformer/training/hpo/README.html#example-scripts)

    *   [Distributed Training](https://sbert.net/docs/sentence_transformer/training/distributed.html)
        *   [Comparison](https://sbert.net/docs/sentence_transformer/training/distributed.html#comparison)
        *   [FSDP](https://sbert.net/docs/sentence_transformer/training/distributed.html#fsdp)

Cross Encoder

*   [Usage](https://sbert.net/docs/cross_encoder/usage/usage.html)
    *   [Cross-Encoder vs Bi-Encoder](https://sbert.net/examples/cross_encoder/applications/README.html)
        *   [Cross-Encoder vs. Bi-Encoder](https://sbert.net/examples/cross_encoder/applications/README.html#cross-encoder-vs-bi-encoder)
        *   [When to use Cross- / Bi-Encoders?](https://sbert.net/examples/cross_encoder/applications/README.html#when-to-use-cross-bi-encoders)
        *   [Cross-Encoders Usage](https://sbert.net/examples/cross_encoder/applications/README.html#cross-encoders-usage)
        *   [Combining Bi- and Cross-Encoders](https://sbert.net/examples/cross_encoder/applications/README.html#combining-bi-and-cross-encoders)
        *   [Training Cross-Encoders](https://sbert.net/examples/cross_encoder/applications/README.html#training-cross-encoders)

    *   [Retrieve & Re-Rank](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html)
        *   [Retrieve & Re-Rank Pipeline](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html#retrieve-re-rank-pipeline)
        *   [Retrieval: Bi-Encoder](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html#retrieval-bi-encoder)
        *   [Re-Ranker: Cross-Encoder](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html#re-ranker-cross-encoder)
        *   [Example Scripts](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html#example-scripts)
        *   [Pre-trained Bi-Encoders (Retrieval)](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html#pre-trained-bi-encoders-retrieval)
        *   [Pre-trained Cross-Encoders (Re-Ranker)](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html#pre-trained-cross-encoders-re-ranker)

    *   [Speeding up Inference](https://sbert.net/docs/cross_encoder/usage/efficiency.html)
        *   [PyTorch](https://sbert.net/docs/cross_encoder/usage/efficiency.html#pytorch)
        *   [ONNX](https://sbert.net/docs/cross_encoder/usage/efficiency.html#onnx)
        *   [OpenVINO](https://sbert.net/docs/cross_encoder/usage/efficiency.html#openvino)
        *   [Benchmarks](https://sbert.net/docs/cross_encoder/usage/efficiency.html#benchmarks)

*   [Pretrained Models](https://sbert.net/docs/cross_encoder/pretrained_models.html)
    *   [MS MARCO](https://sbert.net/docs/cross_encoder/pretrained_models.html#ms-marco)
    *   [SQuAD (QNLI)](https://sbert.net/docs/cross_encoder/pretrained_models.html#squad-qnli)
    *   [STSbenchmark](https://sbert.net/docs/cross_encoder/pretrained_models.html#stsbenchmark)
    *   [Quora Duplicate Questions](https://sbert.net/docs/cross_encoder/pretrained_models.html#quora-duplicate-questions)
    *   [NLI](https://sbert.net/docs/cross_encoder/pretrained_models.html#nli)
    *   [Community Models](https://sbert.net/docs/cross_encoder/pretrained_models.html#community-models)

*   [Training Overview](https://sbert.net/docs/cross_encoder/training_overview.html)
    *   [Why Finetune?](https://sbert.net/docs/cross_encoder/training_overview.html#why-finetune)
    *   [Training Components](https://sbert.net/docs/cross_encoder/training_overview.html#training-components)
    *   [Model](https://sbert.net/docs/cross_encoder/training_overview.html#model)
    *   [Dataset](https://sbert.net/docs/cross_encoder/training_overview.html#dataset)
        *   [Dataset Format](https://sbert.net/docs/cross_encoder/training_overview.html#dataset-format)
        *   [Hard Negatives Mining](https://sbert.net/docs/cross_encoder/training_overview.html#hard-negatives-mining)

    *   [Loss Function](https://sbert.net/docs/cross_encoder/training_overview.html#loss-function)
    *   [Training Arguments](https://sbert.net/docs/cross_encoder/training_overview.html#training-arguments)
    *   [Evaluator](https://sbert.net/docs/cross_encoder/training_overview.html#evaluator)
    *   [Trainer](https://sbert.net/docs/cross_encoder/training_overview.html#trainer)
        *   [Callbacks](https://sbert.net/docs/cross_encoder/training_overview.html#callbacks)

    *   [Multi-Dataset Training](https://sbert.net/docs/cross_encoder/training_overview.html#multi-dataset-training)
    *   [Training Tips](https://sbert.net/docs/cross_encoder/training_overview.html#training-tips)
    *   [Deprecated Training](https://sbert.net/docs/cross_encoder/training_overview.html#deprecated-training)
    *   [Comparisons with SentenceTransformer Training](https://sbert.net/docs/cross_encoder/training_overview.html#comparisons-with-sentencetransformer-training)

*   [Loss Overview](https://sbert.net/docs/cross_encoder/loss_overview.html)
    *   [Loss Table](https://sbert.net/docs/cross_encoder/loss_overview.html#loss-table)
    *   [Distillation](https://sbert.net/docs/cross_encoder/loss_overview.html#distillation)
    *   [Commonly used Loss Functions](https://sbert.net/docs/cross_encoder/loss_overview.html#commonly-used-loss-functions)
    *   [Custom Loss Functions](https://sbert.net/docs/cross_encoder/loss_overview.html#custom-loss-functions)

*   [Training Examples](https://sbert.net/docs/cross_encoder/training/examples.html)
    *   [Semantic Textual Similarity](https://sbert.net/examples/cross_encoder/training/sts/README.html)
        *   [Training data](https://sbert.net/examples/cross_encoder/training/sts/README.html#training-data)
        *   [Loss Function](https://sbert.net/examples/cross_encoder/training/sts/README.html#loss-function)
        *   [Inference](https://sbert.net/examples/cross_encoder/training/sts/README.html#inference)

    *   [Natural Language Inference](https://sbert.net/examples/cross_encoder/training/nli/README.html)
        *   [Data](https://sbert.net/examples/cross_encoder/training/nli/README.html#data)
        *   [CrossEntropyLoss](https://sbert.net/examples/cross_encoder/training/nli/README.html#crossentropyloss)
        *   [Inference](https://sbert.net/examples/cross_encoder/training/nli/README.html#inference)

    *   [Quora Duplicate Questions](https://sbert.net/examples/cross_encoder/training/quora_duplicate_questions/README.html)
        *   [Training](https://sbert.net/examples/cross_encoder/training/quora_duplicate_questions/README.html#training)
        *   [Inference](https://sbert.net/examples/cross_encoder/training/quora_duplicate_questions/README.html#inference)

    *   [MS MARCO](https://sbert.net/examples/cross_encoder/training/ms_marco/README.html)
        *   [Cross Encoder](https://sbert.net/examples/cross_encoder/training/ms_marco/README.html#cross-encoder)
        *   [Training Scripts](https://sbert.net/examples/cross_encoder/training/ms_marco/README.html#training-scripts)
        *   [Inference](https://sbert.net/examples/cross_encoder/training/ms_marco/README.html#inference)

    *   [Rerankers](https://sbert.net/examples/cross_encoder/training/rerankers/README.html)
        *   [BinaryCrossEntropyLoss](https://sbert.net/examples/cross_encoder/training/rerankers/README.html#binarycrossentropyloss)
        *   [CachedMultipleNegativesRankingLoss](https://sbert.net/examples/cross_encoder/training/rerankers/README.html#cachedmultiplenegativesrankingloss)
        *   [Inference](https://sbert.net/examples/cross_encoder/training/rerankers/README.html#inference)

    *   [Model Distillation](https://sbert.net/examples/cross_encoder/training/distillation/README.html)
        *   [Cross Encoder Knowledge Distillation](https://sbert.net/examples/cross_encoder/training/distillation/README.html#cross-encoder-knowledge-distillation)
        *   [Inference](https://sbert.net/examples/cross_encoder/training/distillation/README.html#inference)

    *   [Distributed Training](https://sbert.net/docs/sentence_transformer/training/distributed.html)
        *   [Comparison](https://sbert.net/docs/sentence_transformer/training/distributed.html#comparison)
        *   [FSDP](https://sbert.net/docs/sentence_transformer/training/distributed.html#fsdp)

Sparse Encoder

*   [Usage](https://sbert.net/docs/sparse_encoder/usage/usage.html)
    *   [Computing Sparse Embeddings](https://sbert.net/examples/sparse_encoder/applications/computing_embeddings/README.html)
        *   [Initializing a Sparse Encoder Model](https://sbert.net/examples/sparse_encoder/applications/computing_embeddings/README.html#initializing-a-sparse-encoder-model)
        *   [Calculating Embeddings](https://sbert.net/examples/sparse_encoder/applications/computing_embeddings/README.html#calculating-embeddings)
        *   [Input Sequence Length](https://sbert.net/examples/sparse_encoder/applications/computing_embeddings/README.html#input-sequence-length)
        *   [Controlling Sparsity](https://sbert.net/examples/sparse_encoder/applications/computing_embeddings/README.html#controlling-sparsity)
        *   [Interpretability with SPLADE Models](https://sbert.net/examples/sparse_encoder/applications/computing_embeddings/README.html#interpretability-with-splade-models)
        *   [Multi-Process / Multi-GPU Encoding](https://sbert.net/examples/sparse_encoder/applications/computing_embeddings/README.html#multi-process-multi-gpu-encoding)

    *   [Semantic Textual Similarity](https://sbert.net/examples/sparse_encoder/applications/semantic_textual_similarity/README.html)
        *   [Similarity Calculation](https://sbert.net/examples/sparse_encoder/applications/semantic_textual_similarity/README.html#similarity-calculation)

    *   [Semantic Search](https://sbert.net/examples/sparse_encoder/applications/semantic_search/README.html)
        *   [Manual Search](https://sbert.net/examples/sparse_encoder/applications/semantic_search/README.html#manual-search)
        *   [Vector Database Search](https://sbert.net/examples/sparse_encoder/applications/semantic_search/README.html#vector-database-search)
        *   [Qdrant Integration](https://sbert.net/examples/sparse_encoder/applications/semantic_search/README.html#qdrant-integration)
        *   [OpenSearch Integration](https://sbert.net/examples/sparse_encoder/applications/semantic_search/README.html#opensearch-integration)
        *   [Elasticsearch Integration](https://sbert.net/examples/sparse_encoder/applications/semantic_search/README.html#elasticsearch-integration)
        *   [Seismic Integration](https://sbert.net/examples/sparse_encoder/applications/semantic_search/README.html#seismic-integration)
        *   [SPLADE-index Integration](https://sbert.net/examples/sparse_encoder/applications/semantic_search/README.html#splade-index-integration)

    *   [Retrieve & Re-Rank](https://sbert.net/examples/sparse_encoder/applications/retrieve_rerank/README.html)
        *   [Overview](https://sbert.net/examples/sparse_encoder/applications/retrieve_rerank/README.html#overview)
        *   [Interactive Demo: Simple Wikipedia Search](https://sbert.net/examples/sparse_encoder/applications/retrieve_rerank/README.html#interactive-demo-simple-wikipedia-search)
        *   [Comprehensive Evaluation: Hybrid Search Pipeline](https://sbert.net/examples/sparse_encoder/applications/retrieve_rerank/README.html#comprehensive-evaluation-hybrid-search-pipeline)
        *   [Pre-trained Models](https://sbert.net/examples/sparse_encoder/applications/retrieve_rerank/README.html#pre-trained-models)

    *   [Sparse Encoder Evaluation](https://sbert.net/examples/sparse_encoder/evaluation/README.html)
        *   [Example with Retrieval Evaluation:](https://sbert.net/examples/sparse_encoder/evaluation/README.html#example-with-retrieval-evaluation)

    *   [Speeding up Inference](https://sbert.net/docs/sparse_encoder/usage/efficiency.html)
        *   [PyTorch](https://sbert.net/docs/sparse_encoder/usage/efficiency.html#pytorch)
        *   [ONNX](https://sbert.net/docs/sparse_encoder/usage/efficiency.html#onnx)
        *   [OpenVINO](https://sbert.net/docs/sparse_encoder/usage/efficiency.html#openvino)
        *   [Benchmarks](https://sbert.net/docs/sparse_encoder/usage/efficiency.html#benchmarks)

*   [Pretrained Models](https://sbert.net/docs/sparse_encoder/pretrained_models.html)
    *   [Core SPLADE Models](https://sbert.net/docs/sparse_encoder/pretrained_models.html#core-splade-models)
    *   [Inference-Free SPLADE Models](https://sbert.net/docs/sparse_encoder/pretrained_models.html#inference-free-splade-models)
    *   [Model Collections](https://sbert.net/docs/sparse_encoder/pretrained_models.html#model-collections)

*   [Training Overview](https://sbert.net/docs/sparse_encoder/training_overview.html)
    *   [Why Finetune?](https://sbert.net/docs/sparse_encoder/training_overview.html#why-finetune)
    *   [Training Components](https://sbert.net/docs/sparse_encoder/training_overview.html#training-components)
    *   [Model](https://sbert.net/docs/sparse_encoder/training_overview.html#model)
    *   [Dataset](https://sbert.net/docs/sparse_encoder/training_overview.html#dataset)
        *   [Dataset Format](https://sbert.net/docs/sparse_encoder/training_overview.html#dataset-format)

    *   [Loss Function](https://sbert.net/docs/sparse_encoder/training_overview.html#loss-function)
    *   [Training Arguments](https://sbert.net/docs/sparse_encoder/training_overview.html#training-arguments)
    *   [Evaluator](https://sbert.net/docs/sparse_encoder/training_overview.html#evaluator)
    *   [Trainer](https://sbert.net/docs/sparse_encoder/training_overview.html#trainer)
        *   [Callbacks](https://sbert.net/docs/sparse_encoder/training_overview.html#callbacks)

    *   [Multi-Dataset Training](https://sbert.net/docs/sparse_encoder/training_overview.html#multi-dataset-training)
    *   [Training Tips](https://sbert.net/docs/sparse_encoder/training_overview.html#training-tips)

*   [Dataset Overview](https://sbert.net/docs/sentence_transformer/dataset_overview.html)
    *   [Datasets on the Hugging Face Hub](https://sbert.net/docs/sentence_transformer/dataset_overview.html#datasets-on-the-hugging-face-hub)
    *   [Pre-existing Datasets](https://sbert.net/docs/sentence_transformer/dataset_overview.html#pre-existing-datasets)

*   [Loss Overview](https://sbert.net/docs/sparse_encoder/loss_overview.html)
    *   [Sparse specific Loss Functions](https://sbert.net/docs/sparse_encoder/loss_overview.html#sparse-specific-loss-functions)
        *   [SPLADE Loss](https://sbert.net/docs/sparse_encoder/loss_overview.html#splade-loss)
        *   [CSR Loss](https://sbert.net/docs/sparse_encoder/loss_overview.html#csr-loss)

    *   [Loss Table](https://sbert.net/docs/sparse_encoder/loss_overview.html#loss-table)
    *   [Distillation](https://sbert.net/docs/sparse_encoder/loss_overview.html#distillation)
    *   [Commonly used Loss Functions](https://sbert.net/docs/sparse_encoder/loss_overview.html#commonly-used-loss-functions)
    *   [Custom Loss Functions](https://sbert.net/docs/sparse_encoder/loss_overview.html#custom-loss-functions)

*   [Training Examples](https://sbert.net/docs/sparse_encoder/training/examples.html)
    *   [Model Distillation](https://sbert.net/examples/sparse_encoder/training/distillation/README.html)
        *   [MarginMSE](https://sbert.net/examples/sparse_encoder/training/distillation/README.html#marginmse)

    *   [MS MARCO](https://sbert.net/examples/sparse_encoder/training/ms_marco/README.html)
        *   [SparseMultipleNegativesRankingLoss](https://sbert.net/examples/sparse_encoder/training/ms_marco/README.html#sparsemultiplenegativesrankingloss)

    *   [Semantic Textual Similarity](https://sbert.net/examples/sparse_encoder/training/sts/README.html)
        *   [Training data](https://sbert.net/examples/sparse_encoder/training/sts/README.html#training-data)
        *   [Loss Function](https://sbert.net/examples/sparse_encoder/training/sts/README.html#loss-function)

    *   [Natural Language Inference](https://sbert.net/examples/sparse_encoder/training/nli/README.html)
        *   [Data](https://sbert.net/examples/sparse_encoder/training/nli/README.html#data)
        *   [SpladeLoss](https://sbert.net/examples/sparse_encoder/training/nli/README.html#spladeloss)

    *   [Quora Duplicate Questions](https://sbert.net/examples/sparse_encoder/training/quora_duplicate_questions/README.html)
        *   [Training](https://sbert.net/examples/sparse_encoder/training/quora_duplicate_questions/README.html#training)

    *   [Information Retrieval](https://sbert.net/examples/sparse_encoder/training/retrievers/README.html)
        *   [SparseMultipleNegativesRankingLoss (MNRL)](https://sbert.net/examples/sparse_encoder/training/retrievers/README.html#sparsemultiplenegativesrankingloss-mnrl)
        *   [Inference & Evaluation](https://sbert.net/examples/sparse_encoder/training/retrievers/README.html#inference-evaluation)

    *   [Distributed Training](https://sbert.net/docs/sentence_transformer/training/distributed.html)
        *   [Comparison](https://sbert.net/docs/sentence_transformer/training/distributed.html#comparison)
        *   [FSDP](https://sbert.net/docs/sentence_transformer/training/distributed.html#fsdp)

Package Reference

*   [Sentence Transformer](https://sbert.net/docs/package_reference/sentence_transformer/index.html)
    *   [SentenceTransformer](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html)
        *   [SentenceTransformer](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#id1)
        *   [SentenceTransformerModelCardData](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentencetransformermodelcarddata)
        *   [SimilarityFunction](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#similarityfunction)

    *   [Trainer](https://sbert.net/docs/package_reference/sentence_transformer/trainer.html)
        *   [SentenceTransformerTrainer](https://sbert.net/docs/package_reference/sentence_transformer/trainer.html#sentencetransformertrainer)

    *   [Training Arguments](https://sbert.net/docs/package_reference/sentence_transformer/training_args.html)
        *   [SentenceTransformerTrainingArguments](https://sbert.net/docs/package_reference/sentence_transformer/training_args.html#sentencetransformertrainingarguments)

    *   [Losses](https://sbert.net/docs/package_reference/sentence_transformer/losses.html)
        *   [BatchAllTripletLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#batchalltripletloss)
        *   [BatchHardSoftMarginTripletLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#batchhardsoftmargintripletloss)
        *   [BatchHardTripletLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#batchhardtripletloss)
        *   [BatchSemiHardTripletLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#batchsemihardtripletloss)
        *   [ContrastiveLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#contrastiveloss)
        *   [OnlineContrastiveLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#onlinecontrastiveloss)
        *   [ContrastiveTensionLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#contrastivetensionloss)
        *   [ContrastiveTensionLossInBatchNegatives](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#contrastivetensionlossinbatchnegatives)
        *   [CoSENTLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosentloss)
        *   [AnglELoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#angleloss)
        *   [CosineSimilarityLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosinesimilarityloss)
        *   [DenoisingAutoEncoderLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#denoisingautoencoderloss)
        *   [GISTEmbedLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#gistembedloss)
        *   [CachedGISTEmbedLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cachedgistembedloss)
        *   [MSELoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#mseloss)
        *   [MarginMSELoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#marginmseloss)
        *   [MatryoshkaLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#matryoshkaloss)
        *   [Matryoshka2dLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#matryoshka2dloss)
        *   [AdaptiveLayerLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#adaptivelayerloss)
        *   [MegaBatchMarginLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#megabatchmarginloss)
        *   [MultipleNegativesRankingLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss)
        *   [CachedMultipleNegativesRankingLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cachedmultiplenegativesrankingloss)
        *   [MultipleNegativesSymmetricRankingLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativessymmetricrankingloss)
        *   [CachedMultipleNegativesSymmetricRankingLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cachedmultiplenegativessymmetricrankingloss)
        *   [SoftmaxLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#softmaxloss)
        *   [TripletLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#tripletloss)
        *   [DistillKLDivLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#distillkldivloss)

    *   [Samplers](https://sbert.net/docs/package_reference/sentence_transformer/sampler.html)
        *   [BatchSamplers](https://sbert.net/docs/package_reference/sentence_transformer/sampler.html#batchsamplers)
        *   [MultiDatasetBatchSamplers](https://sbert.net/docs/package_reference/sentence_transformer/sampler.html#multidatasetbatchsamplers)

    *   [Evaluation](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html)
        *   [BinaryClassificationEvaluator](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#binaryclassificationevaluator)
        *   [EmbeddingSimilarityEvaluator](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#embeddingsimilarityevaluator)
        *   [InformationRetrievalEvaluator](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#informationretrievalevaluator)
        *   [NanoBEIREvaluator](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#nanobeirevaluator)
        *   [MSEEvaluator](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#mseevaluator)
        *   [ParaphraseMiningEvaluator](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#paraphraseminingevaluator)
        *   [RerankingEvaluator](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#rerankingevaluator)
        *   [SentenceEvaluator](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentenceevaluator)
        *   [SequentialEvaluator](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sequentialevaluator)
        *   [TranslationEvaluator](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#translationevaluator)
        *   [TripletEvaluator](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#tripletevaluator)

    *   [Datasets](https://sbert.net/docs/package_reference/sentence_transformer/datasets.html)
        *   [ParallelSentencesDataset](https://sbert.net/docs/package_reference/sentence_transformer/datasets.html#parallelsentencesdataset)
        *   [SentenceLabelDataset](https://sbert.net/docs/package_reference/sentence_transformer/datasets.html#sentencelabeldataset)
        *   [DenoisingAutoEncoderDataset](https://sbert.net/docs/package_reference/sentence_transformer/datasets.html#denoisingautoencoderdataset)
        *   [NoDuplicatesDataLoader](https://sbert.net/docs/package_reference/sentence_transformer/datasets.html#noduplicatesdataloader)

    *   [Modules](https://sbert.net/docs/package_reference/sentence_transformer/models.html#)
        *   [Main Modules](https://sbert.net/docs/package_reference/sentence_transformer/models.html#main-modules)
        *   [Further Modules](https://sbert.net/docs/package_reference/sentence_transformer/models.html#further-modules)
        *   [Base Modules](https://sbert.net/docs/package_reference/sentence_transformer/models.html#base-modules)

    *   [quantization](https://sbert.net/docs/package_reference/sentence_transformer/quantization.html)
        *   [`quantize_embeddings()`](https://sbert.net/docs/package_reference/sentence_transformer/quantization.html#sentence_transformers.quantization.quantize_embeddings)
        *   [`semantic_search_faiss()`](https://sbert.net/docs/package_reference/sentence_transformer/quantization.html#sentence_transformers.quantization.semantic_search_faiss)
        *   [`semantic_search_usearch()`](https://sbert.net/docs/package_reference/sentence_transformer/quantization.html#sentence_transformers.quantization.semantic_search_usearch)

*   [Cross Encoder](https://sbert.net/docs/package_reference/cross_encoder/index.html)
    *   [CrossEncoder](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html)
        *   [CrossEncoder](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#id1)
        *   [CrossEncoderModelCardData](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#crossencodermodelcarddata)

    *   [Trainer](https://sbert.net/docs/package_reference/cross_encoder/trainer.html)
        *   [CrossEncoderTrainer](https://sbert.net/docs/package_reference/cross_encoder/trainer.html#crossencodertrainer)

    *   [Training Arguments](https://sbert.net/docs/package_reference/cross_encoder/training_args.html)
        *   [CrossEncoderTrainingArguments](https://sbert.net/docs/package_reference/cross_encoder/training_args.html#crossencodertrainingarguments)

    *   [Losses](https://sbert.net/docs/package_reference/cross_encoder/losses.html)
        *   [BinaryCrossEntropyLoss](https://sbert.net/docs/package_reference/cross_encoder/losses.html#binarycrossentropyloss)
        *   [CrossEntropyLoss](https://sbert.net/docs/package_reference/cross_encoder/losses.html#crossentropyloss)
        *   [LambdaLoss](https://sbert.net/docs/package_reference/cross_encoder/losses.html#lambdaloss)
        *   [ListMLELoss](https://sbert.net/docs/package_reference/cross_encoder/losses.html#listmleloss)
        *   [PListMLELoss](https://sbert.net/docs/package_reference/cross_encoder/losses.html#plistmleloss)
        *   [ListNetLoss](https://sbert.net/docs/package_reference/cross_encoder/losses.html#listnetloss)
        *   [MultipleNegativesRankingLoss](https://sbert.net/docs/package_reference/cross_encoder/losses.html#multiplenegativesrankingloss)
        *   [CachedMultipleNegativesRankingLoss](https://sbert.net/docs/package_reference/cross_encoder/losses.html#cachedmultiplenegativesrankingloss)
        *   [MSELoss](https://sbert.net/docs/package_reference/cross_encoder/losses.html#mseloss)
        *   [MarginMSELoss](https://sbert.net/docs/package_reference/cross_encoder/losses.html#marginmseloss)
        *   [RankNetLoss](https://sbert.net/docs/package_reference/cross_encoder/losses.html#ranknetloss)

    *   [Evaluation](https://sbert.net/docs/package_reference/cross_encoder/evaluation.html)
        *   [CrossEncoderRerankingEvaluator](https://sbert.net/docs/package_reference/cross_encoder/evaluation.html#crossencoderrerankingevaluator)
        *   [CrossEncoderNanoBEIREvaluator](https://sbert.net/docs/package_reference/cross_encoder/evaluation.html#crossencodernanobeirevaluator)
        *   [CrossEncoderClassificationEvaluator](https://sbert.net/docs/package_reference/cross_encoder/evaluation.html#crossencoderclassificationevaluator)
        *   [CrossEncoderCorrelationEvaluator](https://sbert.net/docs/package_reference/cross_encoder/evaluation.html#crossencodercorrelationevaluator)

*   [Sparse Encoder](https://sbert.net/docs/package_reference/sparse_encoder/index.html)
    *   [SparseEncoder](https://sbert.net/docs/package_reference/sparse_encoder/SparseEncoder.html)
        *   [SparseEncoder](https://sbert.net/docs/package_reference/sparse_encoder/SparseEncoder.html#id1)
        *   [SparseEncoderModelCardData](https://sbert.net/docs/package_reference/sparse_encoder/SparseEncoder.html#sparseencodermodelcarddata)
        *   [SimilarityFunction](https://sbert.net/docs/package_reference/sparse_encoder/SparseEncoder.html#similarityfunction)

    *   [Trainer](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html)
        *   [SparseEncoderTrainer](https://sbert.net/docs/package_reference/sparse_encoder/trainer.html#sparseencodertrainer)

    *   [Training Arguments](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html)
        *   [SparseEncoderTrainingArguments](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sparseencodertrainingarguments)

    *   [Losses](https://sbert.net/docs/package_reference/sparse_encoder/losses.html)
        *   [SpladeLoss](https://sbert.net/docs/package_reference/sparse_encoder/losses.html#spladeloss)
        *   [FlopsLoss](https://sbert.net/docs/package_reference/sparse_encoder/losses.html#flopsloss)
        *   [CSRLoss](https://sbert.net/docs/package_reference/sparse_encoder/losses.html#csrloss)
        *   [CSRReconstructionLoss](https://sbert.net/docs/package_reference/sparse_encoder/losses.html#csrreconstructionloss)
        *   [SparseMultipleNegativesRankingLoss](https://sbert.net/docs/package_reference/sparse_encoder/losses.html#sparsemultiplenegativesrankingloss)
        *   [SparseMarginMSELoss](https://sbert.net/docs/package_reference/sparse_encoder/losses.html#sparsemarginmseloss)
        *   [SparseDistillKLDivLoss](https://sbert.net/docs/package_reference/sparse_encoder/losses.html#sparsedistillkldivloss)
        *   [SparseTripletLoss](https://sbert.net/docs/package_reference/sparse_encoder/losses.html#sparsetripletloss)
        *   [SparseCosineSimilarityLoss](https://sbert.net/docs/package_reference/sparse_encoder/losses.html#sparsecosinesimilarityloss)
        *   [SparseCoSENTLoss](https://sbert.net/docs/package_reference/sparse_encoder/losses.html#sparsecosentloss)
        *   [SparseAnglELoss](https://sbert.net/docs/package_reference/sparse_encoder/losses.html#sparseangleloss)
        *   [SparseMSELoss](https://sbert.net/docs/package_reference/sparse_encoder/losses.html#sparsemseloss)

    *   [Samplers](https://sbert.net/docs/package_reference/sentence_transformer/sampler.html)
        *   [BatchSamplers](https://sbert.net/docs/package_reference/sentence_transformer/sampler.html#batchsamplers)
        *   [MultiDatasetBatchSamplers](https://sbert.net/docs/package_reference/sentence_transformer/sampler.html#multidatasetbatchsamplers)

    *   [Evaluation](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html)
        *   [SparseInformationRetrievalEvaluator](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sparseinformationretrievalevaluator)
        *   [SparseNanoBEIREvaluator](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sparsenanobeirevaluator)
        *   [SparseEmbeddingSimilarityEvaluator](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sparseembeddingsimilarityevaluator)
        *   [SparseBinaryClassificationEvaluator](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sparsebinaryclassificationevaluator)
        *   [SparseTripletEvaluator](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sparsetripletevaluator)
        *   [SparseRerankingEvaluator](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sparsererankingevaluator)
        *   [SparseTranslationEvaluator](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sparsetranslationevaluator)
        *   [SparseMSEEvaluator](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sparsemseevaluator)
        *   [ReciprocalRankFusionEvaluator](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#reciprocalrankfusionevaluator)

    *   [Modules](https://sbert.net/docs/package_reference/sparse_encoder/models.html)
        *   [SPLADE Pooling](https://sbert.net/docs/package_reference/sparse_encoder/models.html#splade-pooling)
        *   [MLM Transformer](https://sbert.net/docs/package_reference/sparse_encoder/models.html#mlm-transformer)
        *   [SparseAutoEncoder](https://sbert.net/docs/package_reference/sparse_encoder/models.html#sparseautoencoder)
        *   [SparseStaticEmbedding](https://sbert.net/docs/package_reference/sparse_encoder/models.html#sparsestaticembedding)

    *   [Callbacks](https://sbert.net/docs/package_reference/sparse_encoder/callbacks.html)
        *   [SpladeRegularizerWeightSchedulerCallback](https://sbert.net/docs/package_reference/sparse_encoder/callbacks.html#spladeregularizerweightschedulercallback)

    *   [Search Engines](https://sbert.net/docs/package_reference/sparse_encoder/search_engines.html)
        *   [`semantic_search_elasticsearch()`](https://sbert.net/docs/package_reference/sparse_encoder/search_engines.html#sentence_transformers.sparse_encoder.search_engines.semantic_search_elasticsearch)
        *   [`semantic_search_opensearch()`](https://sbert.net/docs/package_reference/sparse_encoder/search_engines.html#sentence_transformers.sparse_encoder.search_engines.semantic_search_opensearch)
        *   [`semantic_search_qdrant()`](https://sbert.net/docs/package_reference/sparse_encoder/search_engines.html#sentence_transformers.sparse_encoder.search_engines.semantic_search_qdrant)
        *   [`semantic_search_seismic()`](https://sbert.net/docs/package_reference/sparse_encoder/search_engines.html#sentence_transformers.sparse_encoder.search_engines.semantic_search_seismic)

*   [util](https://sbert.net/docs/package_reference/util.html)
    *   [Helper Functions](https://sbert.net/docs/package_reference/util.html#module-sentence_transformers.util)
        *   [`community_detection()`](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.community_detection)
        *   [`http_get()`](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.http_get)
        *   [`is_training_available()`](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.is_training_available)
        *   [`mine_hard_negatives()`](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.mine_hard_negatives)
        *   [`normalize_embeddings()`](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.normalize_embeddings)
        *   [`paraphrase_mining()`](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.paraphrase_mining)
        *   [`semantic_search()`](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.semantic_search)
        *   [`truncate_embeddings()`](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.truncate_embeddings)

    *   [Model Optimization](https://sbert.net/docs/package_reference/util.html#module-sentence_transformers.backend)
        *   [`export_dynamic_quantized_onnx_model()`](https://sbert.net/docs/package_reference/util.html#sentence_transformers.backend.export_dynamic_quantized_onnx_model)
        *   [`export_optimized_onnx_model()`](https://sbert.net/docs/package_reference/util.html#sentence_transformers.backend.export_optimized_onnx_model)
        *   [`export_static_quantized_openvino_model()`](https://sbert.net/docs/package_reference/util.html#sentence_transformers.backend.export_static_quantized_openvino_model)

    *   [Similarity Metrics](https://sbert.net/docs/package_reference/util.html#module-sentence_transformers.util)
        *   [`cos_sim()`](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.cos_sim)
        *   [`dot_score()`](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.dot_score)
        *   [`euclidean_sim()`](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.euclidean_sim)
        *   [`manhattan_sim()`](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.manhattan_sim)
        *   [`pairwise_cos_sim()`](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.pairwise_cos_sim)
        *   [`pairwise_dot_score()`](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.pairwise_dot_score)
        *   [`pairwise_euclidean_sim()`](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.pairwise_euclidean_sim)
        *   [`pairwise_manhattan_sim()`](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.pairwise_manhattan_sim)

[Sentence Transformers](https://sbert.net/index.html)

*   [](https://sbert.net/index.html)
*   [Sentence Transformer](https://sbert.net/docs/package_reference/sentence_transformer/index.html)
*   Modules
*   [Edit on GitHub](https://github.com/huggingface/sentence-transformers/blob/main/docs/package_reference/sentence_transformer/models.md)

* * *

Modules[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#modules "Link to this heading")
====================================================================================================================

`sentence_transformers.models` defines different building blocks, a.k.a. Modules, that can be used to create SentenceTransformer models from scratch. For more details, see [Creating Custom Models](https://sbert.net/docs/sentence_transformer/usage/custom_models.html).

Main Modules[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#main-modules "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.models.Transformer(_model\_name\_or\_path:str_, _max\_seq\_length:int|None=None_, _model\_args:dict[str,Any]|None=None_, _tokenizer\_args:dict[str,Any]|None=None_, _config\_args:dict[str,Any]|None=None_, _cache\_dir:str|None=None_, _do\_lower\_case:bool=False_, _tokenizer\_name\_or\_path:str|None=None_, _backend:str='torch'_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/Transformer.py#L38-L470)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Transformer "Link to this definition")
Hugging Face AutoModel to generate token embeddings. Loads the correct class, e.g. BERT / RoBERTa etc.

Parameters:
*   **model_name_or_path** – Hugging Face models name ([https://huggingface.co/models](https://huggingface.co/models))

*   **max_seq_length** – Truncate any inputs longer than max_seq_length

*   **model_args** – Keyword arguments passed to the Hugging Face Transformers model

*   **tokenizer_args** – Keyword arguments passed to the Hugging Face Transformers tokenizer

*   **config_args** – Keyword arguments passed to the Hugging Face Transformers config

*   **cache_dir** – Cache dir for Hugging Face Transformers to store/load models

*   **do_lower_case** – If true, lowercases the input (independent if the model is cased or not)

*   **tokenizer_name_or_path** – Name or path of the tokenizer. When None, then model_name_or_path is used

*   **backend** – Backend used for model inference. Can be torch, onnx, or openvino. Default is torch.

_class_ sentence_transformers.models.Pooling(_word\_embedding\_dimension:int_, _pooling\_mode:str|None=None_, _pooling\_mode\_cls\_token:bool=False_, _pooling\_mode\_max\_tokens:bool=False_, _pooling\_mode\_mean\_tokens:bool=True_, _pooling\_mode\_mean\_sqrt\_len\_tokens:bool=False_, _pooling\_mode\_weightedmean\_tokens:bool=False_, _pooling\_mode\_lasttoken:bool=False_, _include\_prompt:bool=True_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/Pooling.py#L9-L247)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Pooling "Link to this definition")
Performs pooling (max or mean) on the token embeddings.

Using pooling, it generates from a variable sized sentence a fixed sized sentence embedding. This layer also allows to use the CLS token if it is returned by the underlying word embedding model. You can concatenate multiple poolings together.

Parameters:
*   **word_embedding_dimension** – Dimensions for the word embeddings

*   **pooling_mode** – Either “cls”, “lasttoken”, “max”, “mean”, “mean_sqrt_len_tokens”, or “weightedmean”. If set, overwrites the other pooling_mode_* settings

*   **pooling_mode_cls_token** – Use the first token (CLS token) as text representations

*   **pooling_mode_max_tokens** – Use max in each dimension over all tokens.

*   **pooling_mode_mean_tokens** – Perform mean-pooling

*   **pooling_mode_mean_sqrt_len_tokens** – Perform mean-pooling, but divide by sqrt(input_length).

*   **pooling_mode_weightedmean_tokens** – Perform (position) weighted mean pooling. See [SGPT: GPT Sentence Embeddings for Semantic Search](https://huggingface.co/papers/2202.08904).

*   **pooling_mode_lasttoken** –

Perform last token pooling. See [SGPT: GPT Sentence Embeddings for Semantic Search](https://huggingface.co/papers/2202.08904) and [Text and Code Embeddings by Contrastive Pre-Training](https://huggingface.co/papers/2201.10005).

*   **include_prompt** – If set to false, the prompt tokens are not included in the pooling. This is useful for reproducing work that does not include the prompt tokens in the pooling like INSTRUCTOR, but otherwise not recommended.

_class_ sentence_transformers.models.Dense(_in\_features:int_, _out\_features:int_, _bias:bool=True_, _activation\_function:Callable[[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")],[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")]|None=Tanh()_, _init\_weight:[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")|None=None_, _init\_bias:[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")|None=None_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/Dense.py#L16-L105)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Dense "Link to this definition")
Feed-forward function with activation function.

This layer takes a fixed-sized sentence embedding and passes it through a feed-forward layer. Can be used to generate deep averaging networks (DAN).

Parameters:
*   **in_features** – Size of the input dimension

*   **out_features** – Output size

*   **bias** – Add a bias vector

*   **activation_function** – Pytorch activation function applied on output

*   **init_weight** – Initial value for the matrix of the linear layer

*   **init_bias** – Initial value for the bias of the linear layer

_class_ sentence_transformers.models.Normalize[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/Normalize.py#L14-L29)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Normalize "Link to this definition")
This layer normalizes embeddings to unit length

_class_ sentence_transformers.models.Router(_sub\_modules:dict[str,list[[Module](https://sbert.net/docs/package\_reference/sentence\_transformer/models.html#sentence\_transformers.models.Module "sentence\_transformers.models.Module.Module")]]_, _default\_route:str|None=None_, _allow\_empty\_key:bool=True_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/Router.py#L22-L413)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Router "Link to this definition")
This model allows to create asymmetric SentenceTransformer models that apply different modules depending on the specified route, such as “query” or “document”. Especially useful for models that have different encoders for queries and documents.

Notably, the `task` argument of `model.encode` can be used to specify which route to use, and `model.encode_query` and `model.encode_document` are shorthands for using `task="query"` and `task="document"`, respectively. These methods also optionally apply `prompts` specific to queries or documents.

Note

When training models with the [`Router`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Router "sentence_transformers.models.Router") module, you must use the `router_mapping` argument in the [`SentenceTransformerTrainingArguments`](https://sbert.net/docs/package_reference/sentence_transformer/training_args.html#sentence_transformers.training_args.SentenceTransformerTrainingArguments "sentence_transformers.training_args.SentenceTransformerTrainingArguments") or [`SparseEncoderTrainingArguments`](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments "sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments") to map the training dataset columns to the correct route (“query” or “document”). For example, if your training dataset(s) have `["question", "positive", "negative"]` columns, then you can use the following mapping:

args = SparseEncoderTrainingArguments(
    ...,
    router_mapping={
        "question": "query",
        "positive": "document",
        "negative": "document",
    }
)

Additionally, it is common to use a different learning rate for the different routes. For this, you should use the `learning_rate_mapping` argument in the [`SentenceTransformerTrainingArguments`](https://sbert.net/docs/package_reference/sentence_transformer/training_args.html#sentence_transformers.training_args.SentenceTransformerTrainingArguments "sentence_transformers.training_args.SentenceTransformerTrainingArguments") or [`SparseEncoderTrainingArguments`](https://sbert.net/docs/package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments "sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments") to map parameter patterns to their learning rates. For example, if you want to use a learning rate of `1e-3` for an SparseStaticEmbedding module and `2e-5` for the rest of the model, you can do this:

args = SparseEncoderTrainingArguments(
    ...,
    learning_rate=2e-5,
    learning_rate_mapping={
        r"SparseStaticEmbedding\.*": 1e-3,
    }
)

In the below examples, the `Router` model is used to create asymmetric models with different encoders for queries and documents. In these examples, the “query” route is efficient (e.g., using SparseStaticEmbedding), while the “document” route uses a more complex model (e.g. a Transformers module). This allows for efficient query encoding while still using a powerful document encoder, but the combinations are not limited to this.

Example

from sentence_transformers import SentenceTransformer
from sentence_transformers.models import Router, Normalize

# Use a regular SentenceTransformer for the document embeddings, and a static embedding model for the query embeddings
document_embedder = SentenceTransformer("mixedbread-ai/mxbai-embed-large-v1")
query_embedder = SentenceTransformer("sentence-transformers/static-retrieval-mrl-en-v1")
router = Router.for_query_document(
    query_modules=list(query_embedder.children()),
    document_modules=list(document_embedder.children()),
)
normalize = Normalize()

# Create an asymmetric model with different encoders for queries and documents
model = SentenceTransformer(
    modules=[router, normalize],
)

# ... requires more training to align the vector spaces

# Use the query & document routes
query_embedding = model.encode_query("What is the capital of France?")
document_embedding = model.encode_document("Paris is the capital of France.")

from sentence_transformers.models import Router
from sentence_transformers.sparse_encoder import SparseEncoder
from sentence_transformers.sparse_encoder.models import MLMTransformer, SparseStaticEmbedding, SpladePooling

# Load an asymmetric model with different encoders for queries and documents
doc_encoder = MLMTransformer("opensearch-project/opensearch-neural-sparse-encoding-doc-v3-distill")
router = Router.for_query_document(
    query_modules=[
        SparseStaticEmbedding.from_json(
            "opensearch-project/opensearch-neural-sparse-encoding-doc-v3-distill",
            tokenizer=doc_encoder.tokenizer,
            frozen=True,
        ),
    ],
    document_modules=[
        doc_encoder,
        SpladePooling(pooling_strategy="max", activation_function="log1p_relu"),
    ],
)

model = SparseEncoder(modules=[router], similarity_fn_name="dot")

query = "What's the weather in ny now?"
document = "Currently New York is rainy."

query_embed = model.encode_query(query)
document_embed = model.encode_document(document)

sim = model.similarity(query_embed, document_embed)
print(f"Similarity: {sim}")

# Visualize top tokens for each text
top_k = 10
print(f"Top tokens {top_k} for each text:")

decoded_query = model.decode(query_embed, top_k=top_k)
decoded_document = model.decode(document_embed)

for i in range(min(top_k, len(decoded_query))):
    query_token, query_score = decoded_query[i]
    doc_score = next((score for token, score in decoded_document if token == query_token), 0)
    if doc_score != 0:
        print(f"Token: {query_token}, Query score: {query_score:.4f}, Document score: {doc_score:.4f}")

'''
Similarity: tensor([[11.1105]], device='cuda:0')
Top tokens 10 for each text:
Token: ny, Query score: 5.7729, Document score: 0.8049
Token: weather, Query score: 4.5684, Document score: 0.9710
Token: now, Query score: 3.5895, Document score: 0.4720
Token: ?, Query score: 3.3313, Document score: 0.0286
Token: what, Query score: 2.7699, Document score: 0.0787
Token: in, Query score: 0.4989, Document score: 0.0417
'''

Note

These models are not necessarily stronger than non-asymmetric models. Rudimentary experiments indicate that non-Router models perform better in many cases.

Parameters:
*   **sub_modules** – Mapping of route keys to lists of modules. Each key corresponds to a specific task type, often “query” or “document”, and the list contains the modules to be applied for that task type.

*   **default_route** – The default route to use if no task type is specified. If None, an exception will be thrown if no task type is specified. If `allow_empty_key` is True, the first key in sub_modules will be used as the default route. Defaults to None.

*   **allow_empty_key** – If True, allows the default route to be set to the first key in sub_modules if `default_route` is None. Defaults to True.

_classmethod_ for_query_document(_query\_modules:list[[Module](https://sbert.net/docs/package\_reference/sentence\_transformer/models.html#sentence\_transformers.models.Module "sentence\_transformers.models.Module.Module")]_, _document\_modules:list[[Module](https://sbert.net/docs/package\_reference/sentence\_transformer/models.html#sentence\_transformers.models.Module "sentence\_transformers.models.Module.Module")]_, _default\_route:str|None=None_, _allow\_empty\_key:bool=True_)→Self[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/Router.py#L187-L215)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Router.for_query_document "Link to this definition")
Creates a Router model specifically for query and document modules, allowing convenient usage via model.encode_query and model.encode_document.

Parameters:
*   **query_modules** – List of modules to be applied for the “query” task type.

*   **document_modules** – List of modules to be applied for the “document” task type.

*   **default_route** – The default route to use if no task type is specified. If None, an exception will be thrown if no task type is specified. If `allow_empty_key` is True, the first key in sub_modules will be used as the default route. Defaults to None.

*   **allow_empty_key** – If True, allows the default route to be set to the first key in sub_modules if `default_route` is None. Defaults to True.

Returns:
An instance of the Router model with the specified query and document modules.

Return type:
[Router](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Router "sentence_transformers.models.Router.Router")

_class_ sentence_transformers.models.StaticEmbedding(_tokenizer:Tokenizer|PreTrainedTokenizerFast_, _embedding\_weights:ndarray|[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")|None=None_, _embedding\_dim:int|None=None_, _**kwargs_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/StaticEmbedding.py#L28-L268)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.StaticEmbedding "Link to this definition")
Initializes the StaticEmbedding model given a tokenizer. The model is a simple embedding bag model that takes the mean of trained per-token embeddings to compute text embeddings.

Parameters:
*   **tokenizer** (_Tokenizer_ _|_ _PreTrainedTokenizerFast_) – The tokenizer to be used. Must be a fast tokenizer from `transformers` or `tokenizers`.

*   **embedding_weights** (_np.ndarray_ _|_[_torch.Tensor_](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_|_ _None_ _,_ _optional_) – Pre-trained embedding weights. Defaults to None.

*   **embedding_dim** (_int_ _|_ _None_ _,_ _optional_) – Dimension of the embeddings. Required if embedding_weights is not provided. Defaults to None.

Tip

Due to the extremely efficient nature of this module architecture, the overhead for moving inputs to the GPU can be larger than the actual computation time. Therefore, consider using a CPU device for inference and training.

Example:

from sentence_transformers import SentenceTransformer
from sentence_transformers.models import StaticEmbedding
from tokenizers import Tokenizer

# Pre-distilled embeddings:
static_embedding = StaticEmbedding.from_model2vec("minishlab/potion-base-8M")
# or distill your own embeddings:
static_embedding = StaticEmbedding.from_distillation("BAAI/bge-base-en-v1.5", device="cuda")
# or start with randomized embeddings:
tokenizer = Tokenizer.from_pretrained("FacebookAI/xlm-roberta-base")
static_embedding = StaticEmbedding(tokenizer, embedding_dim=512)

model = SentenceTransformer(modules=[static_embedding])

embeddings = model.encode(["What are Pandas?", "The giant panda, also known as the panda bear or simply the panda, is a bear native to south central China."])
similarity = model.similarity(embeddings[0], embeddings[1])
# tensor([[0.8093]]) (If you use potion-base-8M)
# tensor([[0.6234]]) (If you use the distillation method)
# tensor([[-0.0693]]) (For example, if you use randomized embeddings)

Raises:
*   **ValueError** – If the tokenizer is not a fast tokenizer.

*   **ValueError** – If neither embedding_weights nor embedding_dim is provided.

_classmethod_ from_distillation(_model\_name:str_, _vocabulary:list[str]|None=None_, _device:str|None=None_, _pca\_dims:int|None=256_, _apply\_zipf:bool=True_, _sif\_coefficient:float|None=0.0001_, _token\_remove\_pattern:str|None='\\[unused\\d+\\]'_, _quantize\_to:str='float32'_, _use\_subword:bool=True_, _**kwargs:Any_)→[StaticEmbedding](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.StaticEmbedding "sentence_transformers.models.StaticEmbedding.StaticEmbedding")[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/StaticEmbedding.py#L164-L237)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.StaticEmbedding.from_distillation "Link to this definition")
Creates a StaticEmbedding instance from a distillation process using the model2vec package.

Parameters:
*   **model_name** (_str_) – The name of the model to distill.

*   **vocabulary** (_list_ _[_ _str_ _]_ _|_ _None_ _,_ _optional_) – A list of vocabulary words to use. Defaults to None.

*   **device** (_str_) – The device to run the distillation on (e.g., ‘cpu’, ‘cuda’). If not specified, the strongest device is automatically detected. Defaults to None.

*   **pca_dims** (_int_ _|_ _None_ _,_ _optional_) – The number of dimensions for PCA reduction. Defaults to 256.

*   **apply_zipf** (_bool_) – Whether to apply Zipf’s law during distillation. Defaults to True.

*   **sif_coefficient** (_float_ _|_ _None_ _,_ _optional_) – The coefficient for SIF weighting. Defaults to 1e-4.

*   **token_remove_pattern** (_str_ _|_ _None_ _,_ _optional_) – A regex pattern to remove tokens from the vocabulary. Defaults to r”[unusedd+]”.

*   **quantize_to** (_str_) – The data type to quantize the weights to. Defaults to ‘float32’.

*   **use_subword** (_bool_) – Whether to use subword tokenization. Defaults to True.

Returns:An instance of StaticEmbedding initialized with the distilled model’s
tokenizer and embedding weights.

Return type:
[StaticEmbedding](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.StaticEmbedding "sentence_transformers.models.StaticEmbedding.StaticEmbedding")

Raises:
**ImportError** – If the model2vec package is not installed.

_classmethod_ from_model2vec(_model\_id\_or\_path:str_)→[StaticEmbedding](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.StaticEmbedding "sentence_transformers.models.StaticEmbedding.StaticEmbedding")[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/StaticEmbedding.py#L239-L268)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.StaticEmbedding.from_model2vec "Link to this definition")
Create a StaticEmbedding instance from a model2vec model. This method loads a pre-trained model2vec model and extracts the embedding weights and tokenizer to create a StaticEmbedding instance.

Parameters:
**model_id_or_path** (_str_) – The identifier or path to the pre-trained model2vec model.

Returns:An instance of StaticEmbedding initialized with the tokenizer and embedding weights
the model2vec model.

Return type:
[StaticEmbedding](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.StaticEmbedding "sentence_transformers.models.StaticEmbedding.StaticEmbedding")

Raises:
**ImportError** – If the model2vec package is not installed.

Further Modules[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#further-modules "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.models.BoW(_vocab:list[str]_, _word\_weights:dict[str,float]={}_, _unknown\_word\_weight:float=1_, _cumulative\_term\_frequency:bool=True_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/BoW.py#L16-L87)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.BoW "Link to this definition")
Implements a Bag-of-Words (BoW) model to derive sentence embeddings.

A weighting can be added to allow the generation of tf-idf vectors. The output vector has the size of the vocab.

_class_ sentence_transformers.models.CNN(_in\_word\_embedding\_dimension:int_, _out\_channels:int=256_, _kernel\_sizes:list[int]=[1,3,5]_, _stride\_sizes:list[int]|None=None_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/CNN.py#L14-L88)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.CNN "Link to this definition")
CNN-layer with multiple kernel-sizes over the word embeddings

_class_ sentence_transformers.models.LSTM(_word\_embedding\_dimension:int_, _hidden\_dim:int_, _num\_layers:int=1_, _dropout:float=0_, _bidirectional:bool=True_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/LSTM.py#L14-L94)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.LSTM "Link to this definition")
Bidirectional LSTM running over word embeddings.

_class_ sentence_transformers.models.WeightedLayerPooling(_word\_embedding\_dimension_, _num\_hidden\_layers:int=12_, _layer\_start:int=4_, _layer\_weights=None_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/WeightedLayerPooling.py#L14-L72)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.WeightedLayerPooling "Link to this definition")
Token embeddings are weighted mean of their different hidden layer representations

_class_ sentence_transformers.models.WordEmbeddings(_tokenizer:WordTokenizer|PreTrainedTokenizerBase_, _embedding\_weights_, _update\_embeddings:bool=False_, _max\_seq\_length:int=1000000_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/WordEmbeddings.py#L27-L193)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.WordEmbeddings "Link to this definition")_class_ sentence_transformers.models.WordWeights(_vocab:list[str]_, _word\_weights:dict[str,float]_, _unknown\_word\_weight:float=1_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/WordWeights.py#L13-L70)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.WordWeights "Link to this definition")
This model can weight word embeddings, for example, with idf-values.

Initializes the WordWeights class.

Parameters:
*   **vocab** (_List_ _[_ _str_ _]_) – Vocabulary of the tokenizer.

*   **word_weights** (_Dict_ _[_ _str_ _,_ _float_ _]_) – Mapping of tokens to a float weight value. Word embeddings are multiplied by this float value. Tokens in word_weights must not be equal to the vocab (can contain more or less values).

*   **unknown_word_weight** (_float_ _,_ _optional_) – Weight for words in vocab that do not appear in the word_weights lookup. These can be, for example, rare words in the vocab where no weight exists. Defaults to 1.

Base Modules[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#base-modules "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.models.Module(_*args_, _**kwargs_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/Module.py#L21-L411)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module "Link to this definition")
Base class for all modules in the Sentence Transformers library.

This class provides a common interface for all modules, including methods for loading and saving the module’s configuration and weights. It also provides a method for performing the forward pass of the module.

Two abstract methods are defined in this class, which must be implemented by subclasses:

*   [`sentence_transformers.models.Module.forward()`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.forward "sentence_transformers.models.Module.forward"): The forward pass of the module.

*   [`sentence_transformers.models.Module.save()`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.save "sentence_transformers.models.Module.save"): Save the module to disk.

Optionally, you may also have to override:

*   [`sentence_transformers.models.Module.load()`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.load "sentence_transformers.models.Module.load"): Load the module from disk.

To assist with loading and saving the module, several utility methods are provided:

*   [`sentence_transformers.models.Module.load_config()`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.load_config "sentence_transformers.models.Module.load_config"): Load the module’s configuration from a JSON file.

*   [`sentence_transformers.models.Module.load_file_path()`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.load_file_path "sentence_transformers.models.Module.load_file_path"): Load a file from the module’s directory, regardless of whether the module is saved locally or on Hugging Face.

*   [`sentence_transformers.models.Module.load_dir_path()`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.load_dir_path "sentence_transformers.models.Module.load_dir_path"): Load a directory from the module’s directory, regardless of whether the module is saved locally or on Hugging Face.

*   [`sentence_transformers.models.Module.load_torch_weights()`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.load_torch_weights "sentence_transformers.models.Module.load_torch_weights"): Load the PyTorch weights of the module, regardless of whether the module is saved locally or on Hugging Face.

*   [`sentence_transformers.models.Module.save_config()`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.save_config "sentence_transformers.models.Module.save_config"): Save the module’s configuration to a JSON file.

*   [`sentence_transformers.models.Module.save_torch_weights()`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.save_torch_weights "sentence_transformers.models.Module.save_torch_weights"): Save the PyTorch weights of the module.

*   [`sentence_transformers.models.Module.get_config_dict()`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.get_config_dict "sentence_transformers.models.Module.get_config_dict"): Get the module’s configuration as a dictionary.

And several class variables are defined to assist with loading and saving the module:

*   [`sentence_transformers.models.Module.config_file_name`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.config_file_name "sentence_transformers.models.Module.config_file_name"): The name of the configuration file used to save the module’s configuration.

*   [`sentence_transformers.models.Module.config_keys`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.config_keys "sentence_transformers.models.Module.config_keys"): A list of keys used to save the module’s configuration.

*   [`sentence_transformers.models.Module.save_in_root`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.save_in_root "sentence_transformers.models.Module.save_in_root"): Whether to save the module’s configuration in the root directory of the model or in a subdirectory named after the module.

config_file_name _:str_ _='config.json'_[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.config_file_name "Link to this definition")
The name of the configuration file used to save the module’s configuration. This file is used to initialize the module when loading it from a pre-trained model.

config_keys _:list[str]_ _=[]_[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.config_keys "Link to this definition")
A list of keys used to save the module’s configuration. These keys are used to save the module’s configuration when saving the model to disk.

_abstract_ forward(_features:dict[str,[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")|Any]_, _**kwargs_)→dict[str,[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")|Any][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/Module.py#L77-L102)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.forward "Link to this definition")
Forward pass of the module. This method should be overridden by subclasses to implement the specific behavior of the module.

The forward method takes a dictionary of features as input and returns a dictionary of features as output. The keys in the `features` dictionary depend on the position of the module in the model pipeline, as the `features` dictionary is passed from one module to the next. Common keys in the `features` dictionary are:

> *   `input_ids`: The input IDs of the tokens in the input text.
> 
> *   `attention_mask`: The attention mask for the input tokens.
> 
> *   `token_type_ids`: The token type IDs for the input tokens.
> 
> *   `token_embeddings`: The token embeddings for the input tokens.
> 
> *   `sentence_embedding`: The sentence embedding for the input text, i.e. pooled token embeddings.

Optionally, the `forward` method can accept additional keyword arguments (`**kwargs`) that can be used to pass additional information from `model.encode` to this module.

Parameters:
*   **features** (_dict_ _[_ _str_ _,_[_torch.Tensor_](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_|_ _Any_ _]_) – A dictionary of features to be processed by the module.

*   ****kwargs** – Additional keyword arguments that can be used to pass additional information from `model.encode`.

Returns:
A dictionary of features after processing by the module.

Return type:
dict[str, [torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)") | Any]

get_config_dict()→dict[str,Any][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/Module.py#L104-L115)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.get_config_dict "Link to this definition")
Returns a dictionary of the configuration parameters of the module.

These parameters are used to save the module’s configuration when saving the model to disk, and again used to initialize the module when loading it from a pre-trained model. The keys used in the dictionary are defined in the `config_keys` class variable.

Returns:
A dictionary of the configuration parameters of the module.

Return type:
dict[str, Any]

_classmethod_ load(_model\_name\_or\_path:str_, _subfolder:str=''_, _token:bool|str|None=None_, _cache\_folder:str|None=None_, _revision:str|None=None_, _local\_files\_only:bool=False_, _**kwargs_)→Self[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/Module.py#L117-L157)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.load "Link to this definition")
Load this module from a model checkpoint. The checkpoint can be either a local directory or a model id on Hugging Face.

Parameters:
*   **model_name_or_path** (_str_) – The path to the model directory or the name of the model on Hugging Face.

*   **subfolder** (_str_ _,_ _optional_) – The subfolder within the model directory to load from, e.g. `"1_Pooling"`. Defaults to `""`.

*   **token** (_bool_ _|_ _str_ _|_ _None_ _,_ _optional_) – The token to use for authentication when loading from Hugging Face. If None, tries to use a token saved using `huggingface-cli login` or the `HF_TOKEN` environment variable. Defaults to None.

*   **cache_folder** (_str_ _|_ _None_ _,_ _optional_) – The folder to use for caching the model files. If None, uses the default cache folder for Hugging Face, `~/.cache/huggingface`. Defaults to None.

*   **revision** (_str_ _|_ _None_ _,_ _optional_) – The revision of the model to load. If None, uses the latest revision. Defaults to None.

*   **local_files_only** (_bool_ _,_ _optional_) – Whether to only load local files. Defaults to False.

*   ****kwargs** – Additional module-specific arguments used in an overridden `load` method, such as `trust_remote_code`, `model_kwargs`, `tokenizer_kwargs`, `config_kwargs`, `backend`, etc.

Returns:
The loaded module.

Return type:
Self

_classmethod_ load_config(_model\_name\_or\_path:str_, _subfolder:str=''_, _config\_filename:str|None=None_, _token:bool|str|None=None_, _cache\_folder:str|None=None_, _revision:str|None=None_, _local\_files\_only:bool=False_)→dict[str,Any][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/Module.py#L159-L207)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.load_config "Link to this definition")
Load the configuration of the module from a model checkpoint. The checkpoint can be either a local directory or a model id on Hugging Face. The configuration is loaded from a JSON file, which contains the parameters used to initialize the module.

Parameters:
*   **model_name_or_path** (_str_) – The path to the model directory or the name of the model on Hugging Face.

*   **subfolder** (_str_ _,_ _optional_) – The subfolder within the model directory to load from, e.g. `"1_Pooling"`. Defaults to `""`.

*   **config_filename** (_str_ _|_ _None_ _,_ _optional_) – The name of the configuration file to load. If None, uses the default configuration file name defined in the `config_file_name` class variable. Defaults to None.

*   **token** (_bool_ _|_ _str_ _|_ _None_ _,_ _optional_) – The token to use for authentication when loading from Hugging Face. If None, tries to use a token saved using `huggingface-cli login` or the `HF_TOKEN` environment variable. Defaults to None.

*   **cache_folder** (_str_ _|_ _None_ _,_ _optional_) – The folder to use for caching the model files. If None, uses the default cache folder for Hugging Face, `~/.cache/huggingface`. Defaults to None.

*   **revision** (_str_ _|_ _None_ _,_ _optional_) – The revision of the model to load. If None, uses the latest revision. Defaults to None.

*   **local_files_only** (_bool_ _,_ _optional_) – Whether to only load local files. Defaults to False.

Returns:
A dictionary of the configuration parameters of the module.

Return type:
dict[str, Any]

_static_ load_dir_path(_model\_name\_or\_path:str_, _subfolder:str=''_, _token:bool|str|None=None_, _cache\_folder:str|None=None_, _revision:str|None=None_, _local\_files\_only:bool=False_)→str[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/Module.py#L250-L285)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.load_dir_path "Link to this definition")
A utility function to load a directory from a model checkpoint. The checkpoint can be either a local directory or a model id on Hugging Face.

Parameters:
*   **model_name_or_path** (_str_) – The path to the model directory or the name of the model on Hugging Face.

*   **subfolder** (_str_ _,_ _optional_) – The subfolder within the model directory to load from, e.g. `"1_Pooling"`. Defaults to `""`.

*   **token** (_bool_ _|_ _str_ _|_ _None_ _,_ _optional_) – The token to use for authentication when loading from Hugging Face. If None, tries to use a token saved using `huggingface-cli login` or the `HF_TOKEN` environment variable. Defaults to None.

*   **cache_folder** (_str_ _|_ _None_ _,_ _optional_) – The folder to use for caching the model files. If None, uses the default cache folder for Hugging Face, `~/.cache/huggingface`. Defaults to None.

*   **revision** (_str_ _|_ _None_ _,_ _optional_) – The revision of the model to load. If None, uses the latest revision. Defaults to None.

*   **local_files_only** (_bool_ _,_ _optional_) – Whether to only load local files. Defaults to False.

Returns:
The path to the loaded directory.

Return type:
str

_static_ load_file_path(_model\_name\_or\_path:str_, _filename:str_, _subfolder:str=''_, _token:bool|str|None=None_, _cache\_folder:str|None=None_, _revision:str|None=None_, _local\_files\_only:bool=False_)→str|None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/Module.py#L209-L248)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.load_file_path "Link to this definition")
A utility function to load a file from a model checkpoint. The checkpoint can be either a local directory or a model id on Hugging Face. The file is loaded from the specified subfolder within the model directory.

Parameters:
*   **model_name_or_path** (_str_) – The path to the model directory or the name of the model on Hugging Face.

*   **filename** (_str_) – The name of the file to load.

*   **subfolder** (_str_ _,_ _optional_) – The subfolder within the model directory to load from, e.g. `"1_Pooling"`. Defaults to `""`.

*   **token** (_bool_ _|_ _str_ _|_ _None_ _,_ _optional_) – The token to use for authentication when loading from Hugging Face. If None, tries to use a token saved using `huggingface-cli login` or the `HF_TOKEN` environment variable. Defaults to None.

*   **cache_folder** (_str_ _|_ _None_ _,_ _optional_) – The folder to use for caching the model files. If None, uses the default cache folder for Hugging Face, `~/.cache/huggingface`. Defaults to None.

*   **revision** (_str_ _|_ _None_ _,_ _optional_) – The revision of the model to load. If None, uses the latest revision. Defaults to None.

*   **local_files_only** (_bool_ _,_ _optional_) – Whether to only load local files. Defaults to False.

Returns:
The path to the loaded file, or None if the file was not found.

Return type:
str | None

_classmethod_ load_torch_weights(_model\_name\_or\_path:str_, _subfolder:str=''_, _token:bool|str|None=None_, _cache\_folder:str|None=None_, _revision:str|None=None_, _local\_files\_only:bool=False_, _model:Self|None=None_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/Module.py#L287-L364)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.load_torch_weights "Link to this definition")
A utility function to load the PyTorch weights of a model from a checkpoint. The checkpoint can be either a local directory or a model id on Hugging Face. The weights are loaded from either a `model.safetensors` file or a `pytorch_model.bin` file, depending on which one is available. This method either loads the weights into the model or returns the weights as a state dictionary.

Parameters:
*   **model_name_or_path** (_str_) – The path to the model directory or the name of the model on Hugging Face.

*   **subfolder** (_str_ _,_ _optional_) – The subfolder within the model directory to load from, e.g. `"2_Dense"`. Defaults to `""`.

*   **token** (_bool_ _|_ _str_ _|_ _None_ _,_ _optional_) – The token to use for authentication when loading from Hugging Face. If None, tries to use a token saved using `huggingface-cli login` or the `HF_TOKEN` environment variable. Defaults to None.

*   **cache_folder** (_str_ _|_ _None_ _,_ _optional_) – The folder to use for caching the model files. If None, uses the default cache folder for Hugging Face, `~/.cache/huggingface`. Defaults to None.

*   **revision** (_str_ _|_ _None_ _,_ _optional_) – The revision of the model to load. If None, uses the latest revision. Defaults to None.

*   **local_files_only** (_bool_ _,_ _optional_) – Whether to only load local files. Defaults to False.

*   **model** (_Self_ _|_ _None_ _,_ _optional_) – The model to load the weights into. If None, returns the weights as a state dictionary. Defaults to None.

Raises:
**ValueError** – If neither a `model.safetensors` file nor a `pytorch_model.bin` file is found in the model checkpoint in the `subfolder`.

Returns:The model with the loaded weights or the weights as a state dictionary,
depending on the value of the `model` argument.

Return type:
Self | dict[str, [torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")]

_abstract_ save(_output\_path:str_, _*args_, _safe\_serialization:bool=True_, _**kwargs_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/Module.py#L366-L377)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.save "Link to this definition")
Save the module to disk. This method should be overridden by subclasses to implement the specific behavior of the module.

Parameters:
*   **output_path** (_str_) – The path to the directory where the module should be saved.

*   ***args** – Additional arguments that can be used to pass additional information to the save method.

*   **safe_serialization** (_bool_ _,_ _optional_) – Whether to use the safetensors format for saving the model weights. Defaults to True.

*   ****kwargs** – Additional keyword arguments that can be used to pass additional information to the save method.

save_config(_output\_path:str_, _filename:str|None=None_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/Module.py#L379-L394)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.save_config "Link to this definition")
Save the configuration of the module to a JSON file.

Parameters:
*   **output_path** (_str_) – The path to the directory where the configuration file should be saved.

*   **filename** (_str_ _|_ _None_ _,_ _optional_) – The name of the configuration file. If None, uses the default configuration file name defined in the `config_file_name` class variable. Defaults to None.

Returns:
None

save_in_root _:bool_ _=False_[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.save_in_root "Link to this definition")
Whether to save the module’s configuration in the root directory of the model or in a subdirectory named after the module.

save_torch_weights(_output\_path:str_, _safe\_serialization:bool=True_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/Module.py#L396-L411)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.save_torch_weights "Link to this definition")
Save the PyTorch weights of the module to disk.

Parameters:
*   **output_path** (_str_) – The path to the directory where the weights should be saved.

*   **safe_serialization** (_bool_ _,_ _optional_) – Whether to use the safetensors format for saving the model weights. Defaults to True.

Returns:
None

_class_ sentence_transformers.models.InputModule(_*args_, _**kwargs_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/InputModule.py#L13-L92)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.InputModule "Link to this definition")
Subclass of [`sentence_transformers.models.Module`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module"), base class for all input modules in the Sentence Transformers library, i.e. modules that are used to process inputs and optionally also perform processing in the forward pass.

This class provides a common interface for all input modules, including methods for loading and saving the module’s configuration and weights, as well as input processing. It also provides a method for performing the forward pass of the module.

Three abstract methods are defined in this class, which must be implemented by subclasses:

*   [`sentence_transformers.models.Module.forward()`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.forward "sentence_transformers.models.Module.forward"): The forward pass of the module.

*   [`sentence_transformers.models.Module.save()`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.save "sentence_transformers.models.Module.save"): Save the module to disk.

*   [`sentence_transformers.models.InputModule.tokenize()`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.InputModule.tokenize "sentence_transformers.models.InputModule.tokenize"): Tokenize the input texts and return a dictionary of tokenized features.

Optionally, you may also have to override:

*   [`sentence_transformers.models.Module.load()`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.load "sentence_transformers.models.Module.load"): Load the module from disk.

To assist with loading and saving the module, several utility methods are provided:

*   [`sentence_transformers.models.Module.load_config()`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.load_config "sentence_transformers.models.Module.load_config"): Load the module’s configuration from a JSON file.

*   [`sentence_transformers.models.Module.load_file_path()`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.load_file_path "sentence_transformers.models.Module.load_file_path"): Load a file from the module’s directory, regardless of whether the module is saved locally or on Hugging Face.

*   [`sentence_transformers.models.Module.load_dir_path()`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.load_dir_path "sentence_transformers.models.Module.load_dir_path"): Load a directory from the module’s directory, regardless of whether the module is saved locally or on Hugging Face.

*   [`sentence_transformers.models.Module.load_torch_weights()`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.load_torch_weights "sentence_transformers.models.Module.load_torch_weights"): Load the PyTorch weights of the module, regardless of whether the module is saved locally or on Hugging Face.

*   [`sentence_transformers.models.Module.save_config()`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.save_config "sentence_transformers.models.Module.save_config"): Save the module’s configuration to a JSON file.

*   [`sentence_transformers.models.Module.save_torch_weights()`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.save_torch_weights "sentence_transformers.models.Module.save_torch_weights"): Save the PyTorch weights of the module.

*   [`sentence_transformers.models.InputModule.save_tokenizer()`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.InputModule.save_tokenizer "sentence_transformers.models.InputModule.save_tokenizer"): Save the tokenizer used by the module.

*   [`sentence_transformers.models.Module.get_config_dict()`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.get_config_dict "sentence_transformers.models.Module.get_config_dict"): Get the module’s configuration as a dictionary.

And several class variables are defined to assist with loading and saving the module:

*   [`sentence_transformers.models.Module.config_file_name`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.config_file_name "sentence_transformers.models.Module.config_file_name"): The name of the configuration file used to save the module’s configuration.

*   [`sentence_transformers.models.Module.config_keys`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module.config_keys "sentence_transformers.models.Module.config_keys"): A list of keys used to save the module’s configuration.

*   [`sentence_transformers.models.InputModule.save_in_root`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.InputModule.save_in_root "sentence_transformers.models.InputModule.save_in_root"): Whether to save the module’s configuration in the root directory of the model or in a subdirectory named after the module.

*   [`sentence_transformers.models.InputModule.tokenizer`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.InputModule.tokenizer "sentence_transformers.models.InputModule.tokenizer"): The tokenizer used by the module.

save_in_root _:bool_ _=True_[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.InputModule.save_in_root "Link to this definition")
Whether to save the module’s configuration in the root directory of the model or in a subdirectory named after the module.

save_tokenizer(_output\_path:str_, _**kwargs_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/InputModule.py#L74-L92)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.InputModule.save_tokenizer "Link to this definition")
Saves the tokenizer to the specified output path.

Parameters:
*   **output_path** (_str_) – Path to save the tokenizer.

*   ****kwargs** – Additional keyword arguments for saving the tokenizer.

Returns:
None

_abstract_ tokenize(_texts:list[str]_, _**kwargs_)→dict[str,[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")|Any][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/models/InputModule.py#L60-L72)[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.InputModule.tokenize "Link to this definition")
Tokenizes the input texts and returns a dictionary of tokenized features.

Parameters:
*   **texts** (_list_ _[_ _str_ _]_) – List of input texts to tokenize.

*   ****kwargs** – Additional keyword arguments for tokenization, e.g. `task`.

Returns:Dictionary containing tokenized features, e.g.
`{"input_ids": ..., "attention_mask": ...}`

Return type:
dict[str, [torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)") | Any]

tokenizer _:PreTrainedTokenizerBase|Tokenizer_[](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.InputModule.tokenizer "Link to this definition")
The tokenizer used for tokenizing the input texts. It can be either a [`transformers.PreTrainedTokenizerBase`](https://huggingface.co/docs/transformers/main/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase "(in transformers vmain)") subclass or a Tokenizer from the `tokenizers` library.

[Previous](https://sbert.net/docs/package_reference/sentence_transformer/datasets.html "Datasets")[Next](https://sbert.net/docs/package_reference/sentence_transformer/quantization.html "quantization")

* * *

© Copyright 2026.

 Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org/).
