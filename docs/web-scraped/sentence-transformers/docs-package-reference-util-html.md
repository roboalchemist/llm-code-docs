# Source: https://sbert.net/docs/package_reference/util.html

Title: util — Sentence Transformers documentation

URL Source: https://sbert.net/docs/package_reference/util.html

Published Time: Tue, 17 Feb 2026 14:05:46 GMT

Markdown Content:
util — Sentence Transformers documentation
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

    *   [Modules](https://sbert.net/docs/package_reference/sentence_transformer/models.html)
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

*   [util](https://sbert.net/docs/package_reference/util.html#)
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
*   util
*   [Edit on GitHub](https://github.com/huggingface/sentence-transformers/blob/main/docs/package_reference/util.md)

* * *

util[](https://sbert.net/docs/package_reference/util.html#util "Link to this heading")
=======================================================================================

`sentence_transformers.util` defines different helpful functions to work with text embeddings.

Helper Functions[](https://sbert.net/docs/package_reference/util.html#module-sentence_transformers.util "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------

sentence_transformers.util.community_detection(_embeddings:[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")|ndarray_, _threshold:float=0.75_, _min\_community\_size:int=10_, _batch\_size:int=1024_, _show\_progress\_bar:bool=False_)→list[list[int]][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/util/retrieval.py#L258-L357)[](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.community_detection "Link to this definition")
Function for Fast Community Detection.

Finds in the embeddings all communities, i.e. embeddings that are close (closer than threshold). Returns only communities that are larger than min_community_size. The communities are returned in decreasing order. The first element in each list is the central point in the community.

Parameters:
*   **embeddings** ([_torch.Tensor_](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_or_ _numpy.ndarray_) – The input embeddings.

*   **threshold** (_float_) – The threshold for determining if two embeddings are close. Defaults to 0.75.

*   **min_community_size** (_int_) – The minimum size of a community to be considered. Defaults to 10.

*   **batch_size** (_int_) – The batch size for computing cosine similarity scores. Defaults to 1024.

*   **show_progress_bar** (_bool_) – Whether to show a progress bar during computation. Defaults to False.

Returns:
A list of communities, where each community is represented as a list of indices.

Return type:
List[List[int]]

sentence_transformers.util.http_get(_url:str_, _path:str_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/util/file_io.py#L158-L207)[](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.http_get "Link to this definition")
Download a URL to a local file with a progress bar.

The content is streamed in chunks and first written to a temporary `"<path>_part"` file, which is atomically moved to `path` once the download has completed successfully. Parent directories of `path` are created automatically if they do not exist.

Parameters:
*   **url** (_str_) – The HTTP(S) URL to download.

*   **path** (_str_) – Destination file path on the local filesystem.

Raises:
*   **ImportError** – If the optional `httpx` dependency is not installed.

*   **httpx.HTTPStatusError** – If the HTTP request returns a non-success status code.

*   **OSError** – If the file cannot be written to `path`.

Returns:
None

sentence_transformers.util.is_training_available()→bool[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/util/environment.py#L71-L76)[](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.is_training_available "Link to this definition")
Returns True if we have the required dependencies for training Sentence Transformers models, i.e. Huggingface datasets and Huggingface accelerate.

sentence_transformers.util.mine_hard_negatives(_dataset:Dataset_, _model:[SentenceTransformer](https://sbert.net/docs/package\_reference/sentence\_transformer/SentenceTransformer.html#sentence\_transformers.SentenceTransformer "sentence\_transformers.SentenceTransformer")_, _anchor\_column\_name:str|None=None_, _positive\_column\_name:str|None=None_, _corpus:list[str]|None=None_, _cross\_encoder:[CrossEncoder](https://sbert.net/docs/package\_reference/cross\_encoder/cross\_encoder.html#sentence\_transformers.cross\_encoder.CrossEncoder "sentence\_transformers.cross\_encoder.CrossEncoder")|None=None_, _range\_min:int=0_, _range\_max:int|None=None_, _max\_score:float|None=None_, _min\_score:float|None=None_, _absolute\_margin:float|None=None_, _relative\_margin:float|None=None_, _num\_negatives:int=3_, _sampling\_strategy:Literal['random','top']='top'_, _query\_prompt\_name:str|None=None_, _query\_prompt:str|None=None_, _corpus\_prompt\_name:str|None=None_, _corpus\_prompt:str|None=None_, _include\_positives:bool=False_, _output\_format:Literal['triplet','n-tuple','labeled-pair','labeled-list']='triplet'_, _output\_scores:bool=False_, _batch\_size:int=32_, _faiss\_batch\_size:int=16384_, _use\_faiss:bool=False_, _use\_multi\_process:list[str]|bool=False_, _verbose:bool=True_, _cache\_folder:str|None=None_, _as\_triplets:bool|None=None_, _margin:float|None=None_)→Dataset[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/util/hard_negatives.py#L25-L851)[](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.mine_hard_negatives "Link to this definition")
Add hard negatives to a dataset of (anchor, positive) pairs to create (anchor, positive, negative) triplets or (anchor, positive, negative_1, …, negative_n) tuples.

Hard negative mining is a technique to improve the quality of a dataset by adding hard negatives, which are texts that may appear similar to the anchor, but are not. Using hard negatives can improve the performance of models trained on the dataset.

This function uses a SentenceTransformer model to embed the sentences in the dataset, and then finds the closest matches to each anchor sentence in the dataset. It then samples negatives from the closest matches, optionally using a CrossEncoder model to rescore the candidates.

Supports prompt formatting for models that expect specific instruction-style input.

You can influence the candidate negative selection in various ways:

*   **range_min**: Minimum rank of the closest matches to consider as negatives: useful to skip the most similar texts to avoid marking texts as negative that are actually positives.

*   **range_max**: Maximum rank of the closest matches to consider as negatives: useful to limit the number of candidates to sample negatives from. A lower value makes processing faster, but may result in less candidate negatives that satisfy the margin or max_score conditions.

*   **max_score**: Maximum score to consider as a negative: useful to skip candidates that are too similar to the anchor.

*   **min_score**: Minimum score to consider as a negative: useful to skip candidates that are too dissimilar to the anchor.

*   **absolute_margin**: Absolute margin for hard negative mining: useful to skip candidate negatives whose similarity to the anchor is within a certain margin of the positive pair. A value of 0 can be used to enforce that the negative is always further away from the anchor than the positive.

*   **relative_margin**: Relative margin for hard negative mining: useful to skip candidate negatives whose similarity to the anchor is within a certain margin of the positive pair. A value of 0.05 means that the negative is at most 95% as similar to the anchor as the positive.

*   **sampling_strategy**: Sampling strategy for negatives: “top” or “random”. “top” will always sample the top n candidates as negatives, while “random” will sample n negatives randomly from the candidates that satisfy the margin or max_score conditions.

Tip

The excellent [NV-Retriever paper](https://huggingface.co/papers/2407.15831) is a great resource for understanding the details of hard negative mining and how to use it effectively. Notably, it reaches the strongest performance using these settings:

dataset = mine_hard_negatives(
    dataset=dataset,
    model=model,
    relative_margin=0.05,         # 0.05 means that the negative is at most 95% as similar to the anchor as the positive
    num_negatives=num_negatives,  # 10 or less is recommended
    sampling_strategy="top",      # "top" means that we sample the top candidates as negatives
    batch_size=batch_size,        # Adjust as needed
    use_faiss=True,               # Optional: Use faiss/faiss-gpu for faster similarity search
)

This corresponds with the TopK-PercPos (95%) mining method.

Example

>>> from sentence_transformers.util import mine_hard_negatives
>>> from sentence_transformers import SentenceTransformer
>>> from datasets import load_dataset
>>> # Load a Sentence Transformer model
>>> model = SentenceTransformer("all-MiniLM-L6-v2")
>>>
>>> # Load a dataset to mine hard negatives from
>>> dataset = load_dataset("sentence-transformers/natural-questions", split="train")
>>> dataset
Dataset({
 features: ['query', 'answer'],
 num_rows: 100231
})
>>> dataset = mine_hard_negatives(
...     dataset=dataset,
...     model=model,
...     range_min=10,
...     range_max=50,
...     max_score=0.8,
...     relative_margin=0.05,
...     num_negatives=5,
...     sampling_strategy="random",
...     batch_size=128,
...     use_faiss=True,
... )
Batches: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████| 588/588 [00:32<00:00, 18.07it/s]
Batches: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████| 784/784 [00:08<00:00, 96.41it/s]
Querying FAISS index: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████| 7/7 [00:06<00:00, 1.06it/s]
Negative candidates mined, preparing dataset...
Metric Positive Negative Difference
Count 100,231 487,865
Mean 0.6866 0.4194 0.2752
Median 0.7010 0.4102 0.2760
Std 0.1125 0.0719 0.1136
Min 0.0303 0.1702 0.0209
25% 0.6221 0.3672 0.1899
50% 0.7010 0.4102 0.2760
75% 0.7667 0.4647 0.3590
Max 0.9584 0.7621 0.7073
Skipped 427,503 potential negatives (8.36%) due to the relative_margin of 0.05.
Skipped 978 potential negatives (0.02%) due to the max_score of 0.8.
Could not find enough negatives for 13290 samples (2.65%). Consider adjusting the range_max, range_min, relative_margin and max_score parameters if you'd like to find more valid negatives.
>>> dataset
Dataset({
 features: ['query', 'answer', 'negative'],
 num_rows: 487865
})
>>> dataset[0]
{
 'query': 'when did richmond last play in a preliminary final',
 'answer': "Richmond Football Club Richmond began 2017 with 5 straight wins, a feat it had not achieved since 1995. A series of close losses hampered the Tigers throughout the middle of the season, including a 5-point loss to the Western Bulldogs, 2-point loss to Fremantle, and a 3-point loss to the Giants. Richmond ended the season strongly with convincing victories over Fremantle and St Kilda in the final two rounds, elevating the club to 3rd on the ladder. Richmond's first final of the season against the Cats at the MCG attracted a record qualifying final crowd of 95,028; the Tigers won by 51 points. Having advanced to the first preliminary finals for the first time since 2001, Richmond defeated Greater Western Sydney by 36 points in front of a crowd of 94,258 to progress to the Grand Final against Adelaide, their first Grand Final appearance since 1982. The attendance was 100,021, the largest crowd to a grand final since 1986. The Crows led at quarter time and led by as many as 13, but the Tigers took over the game as it progressed and scored seven straight goals at one point. They eventually would win by 48 points – 16.12 (108) to Adelaide's 8.12 (60) – to end their 37-year flag drought.[22] Dustin Martin also became the first player to win a Premiership medal, the Brownlow Medal and the Norm Smith Medal in the same season, while Damien Hardwick was named AFL Coaches Association Coach of the Year. Richmond's jump from 13th to premiers also marked the biggest jump from one AFL season to the next.",
 'negative': "2018 NRL Grand Final The 2018 NRL Grand Final was the conclusive and premiership-deciding game of the 2018 National Rugby League season and was played on Sunday September 30 at Sydney's ANZ Stadium.[1] The match was contested between minor premiers the Sydney Roosters and defending premiers the Melbourne Storm. In front of a crowd of 82,688, Sydney won the match 21â€“6 to claim their 14th premiership title and their first since 2013. Roosters five-eighth Luke Keary was awarded the Clive Churchill Medal as the game's official man of the match."
}
>>> # To include similarity scores, use output_scores=True
>>> dataset_with_scores = mine_hard_negatives(
...     dataset=dataset,
...     model=model,
...     output_scores=True,
...     # ... other parameters
... )
>>> dataset_with_scores
Dataset({
 features: ['query', 'answer', 'negative', 'scores'],
 num_rows: 487865
})
>>> dataset.push_to_hub("natural-questions-hard-negatives", "triplet-all")

Parameters:
*   **dataset** (_Dataset_) – A dataset containing (anchor, positive) pairs.

*   **model** ([_SentenceTransformer_](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")) – A SentenceTransformer model to use for embedding the sentences.

*   **anchor_column_name** (_str_ _,_ _optional_) – The column name in dataset that contains the anchor/query. Defaults to None, in which case the first column in dataset will be used.

*   **positive_column_name** (_str_ _,_ _optional_) – The column name in dataset that contains the positive candidates. Defaults to None, in which case the second column in dataset will be used.

*   **corpus** (_List_ _[_ _str_ _]_ _,_ _optional_) – A list containing documents as strings that will be used as candidate negatives in addition to the second column in dataset. Defaults to None, in which case the second column in dataset will exclusively be used as the negative candidate corpus.

*   **cross_encoder** ([_CrossEncoder_](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")_,_ _optional_) – A CrossEncoder model to use for rescoring the candidates. Defaults to None.

*   **range_min** (_int_) – Minimum rank of the closest matches to consider as negatives. Defaults to 0.

*   **range_max** (_int_ _,_ _optional_) – Maximum rank of the closest matches to consider as negatives. Defaults to None.

*   **max_score** (_float_ _,_ _optional_) – Maximum score to consider as a negative. Defaults to None.

*   **min_score** (_float_ _,_ _optional_) – Minimum score to consider as a negative. Defaults to None.

*   **absolute_margin** (_float_ _,_ _optional_) – Absolute margin for hard negative mining, i.e. the minimum distance between the positive similarity and the negative similarity. Defaults to None.

*   **relative_margin** (_float_ _,_ _optional_) – Relative margin for hard negative mining, i.e. the maximum ratio between the positive similarity and the negative similarity. A value of 0.05 means that the negative is at most 95% as similar to the anchor as the positive. Defaults to None.

*   **num_negatives** (_int_) – Number of negatives to sample. Defaults to 3.

*   **sampling_strategy** (_Literal_ _[_ _"random"_ _,_ _"top"_ _]_) – Sampling strategy for negatives: “top” or “random”. Defaults to “top”.

*   **query_prompt_name** (_Optional_ _[_ _str_ _]_ _,_ _optional_) –

The name of a predefined prompt to use when encoding the first/anchor dataset column. It must match a key in the `model.prompts` dictionary, which can be set during model initialization or loaded from the model configuration.

For example, if `query_prompt_name="query"` and the model prompts dictionary includes {“query”: “query: “}, then the sentence “What is the capital of France?” is transformed into: “query: What is the capital of France?” before encoding. This is useful for models that were trained or fine-tuned with specific prompt formats.

Ignored if `query_prompt` is provided. Defaults to None.

*   **query_prompt** (_Optional_ _[_ _str_ _]_ _,_ _optional_) –

A raw prompt string to prepend directly to the first/anchor dataset column during encoding.

For instance, query_prompt=”query: “ transforms the sentence “What is the capital of France?” into: “query: What is the capital of France?”. Use this to override the prompt logic entirely and supply your own prefix. This takes precedence over `query_prompt_name`. Defaults to None.

*   **corpus_prompt_name** (_Optional_ _[_ _str_ _]_ _,_ _optional_) – The name of a predefined prompt to use when encoding the corpus. See `query_prompt_name` for more information. Defaults to None.

*   **corpus_prompt** (_Optional_ _[_ _str_ _]_ _,_ _optional_) – A raw prompt string to prepend directly to the corpus during encoding. See `query_prompt` for more information. Defaults to None.

*   **include_positives** (_bool_) – Whether to include the positives in the negative candidates. Setting this to True is primarily useful for creating Reranking evaluation datasets for CrossEncoder models, where it can be useful to get a full ranking (including the positives) from a first-stage retrieval model. Defaults to False.

*   **output_format** (_Literal_ _[_ _"triplet"_ _,_ _"n-tuple"_ _,_ _"labeled-pair"_ _,_ _"labeled-list"_ _]_) –

Output format for the datasets.Dataset. When `output_scores=False` (default), options are:

    *   ”triplet”: (anchor, positive, negative) triplets, i.e. 3 columns. Useful for e.g. [`CachedMultipleNegativesRankingLoss`](https://sbert.net/docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.CachedMultipleNegativesRankingLoss "sentence_transformers.cross_encoder.losses.CachedMultipleNegativesRankingLoss").

    *   ”n-tuple”: (anchor, positive, negative_1, …, negative_n) tuples, i.e. 2 + num_negatives columns. Useful for e.g. [`CachedMultipleNegativesRankingLoss`](https://sbert.net/docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.CachedMultipleNegativesRankingLoss "sentence_transformers.cross_encoder.losses.CachedMultipleNegativesRankingLoss").

    *   ”labeled-pair”: (anchor, passage, label) text tuples with a label of 0 for negative and 1 for positive, i.e. 3 columns. Useful for e.g. [`BinaryCrossEntropyLoss`](https://sbert.net/docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss "sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss").

    *   ”labeled-list”: (anchor, [doc1, doc2, …, docN], [label1, label2, …, labelN]) tuples with labels of 0 for negative and 1 for positive, i.e. 3 columns. Useful for e.g. [`LambdaLoss`](https://sbert.net/docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.LambdaLoss "sentence_transformers.cross_encoder.losses.LambdaLoss").

Defaults to “triplet”. See `output_scores` for the output formats when `output_scores=True`.

*   **output_scores** (_bool_) – Whether to include similarity scores in the output dataset. When True, adds score fields to the output: - For “triplet” format: adds scores column with query-positive and query-negative similarity scores, for 4 columns total. - For “n-tuple” format: adds scores column with a list of similarity scores for the query-positive and each of the query-negative pairs, for 3 + num_negatives columns total. Useful for e.g. [`SparseMarginMSELoss`](https://sbert.net/docs/package_reference/sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.SparseMarginMSELoss "sentence_transformers.sparse_encoder.losses.SparseMarginMSELoss"). - For “labeled-pair” format: replaces the label column with a score column. Labels are binary (1 for positive, 0 for negative), but scores contain the actual similarity scores computed by the model or cross_encoder. The output has 3 columns. - For “labeled-list” format: replaces the labels column with a scores column. Labels are binary (1 for positive, 0 for negative), but scores contain the actual similarity scores computed by the model or cross_encoder. The output has 3 columns. Defaults to False.

*   **batch_size** (_int_) – Batch size for encoding the dataset. Defaults to 32.

*   **faiss_batch_size** (_int_) – Batch size for FAISS top-k search. Defaults to 16384.

*   **use_faiss** (_bool_) – Whether to use FAISS for similarity search. May be recommended for large datasets. Defaults to False.

*   **use_multi_process** (_bool_ _|_ _List_ _[_ _str_ _]_ _,_ _optional_) – Whether to use multi-GPU/CPU processing. If True, uses all GPUs if CUDA is available, and 4 CPU processes if it’s not available. You can also pass a list of PyTorch devices like [“cuda:0”, “cuda:1”, …] or [“cpu”, “cpu”, “cpu”, “cpu”].

*   **verbose** (_bool_) – Whether to print statistics and logging. Defaults to True.

*   **cache_folder** (_str_ _,_ _optional_) – Directory path for caching embeddings. If provided, the function will save `query_embeddings_{hash}.npy` and `corpus_embeddings_{hash}.npy` under this folder after the first run, and on subsequent calls will load from these files if they exist to avoid recomputation. The hashes are computed based on the model name and the queries/corpus. Defaults to None.

*   **as_triplets** (_bool_ _,_ _optional_) – Deprecated. Use output_format instead. Defaults to None.

*   **margin** (_float_ _,_ _optional_) – Deprecated. Use absolute_margin or relative_margin instead. Defaults to None.

Returns:
A dataset containing the specified output format. If output_scores=False (default), the formats are:

*   ”triplet”: (anchor, positive, negative)

*   ”n-tuple”: (anchor, positive, negative_1, …, negative_n)

*   ”labeled-pair”: (anchor, passage, label)

*   ”labeled-list”: (anchor, [passages], [labels])

And if output_scores=True, the formats are:

*   ”triplet”: (anchor, positive, negative, [scores])

*   ”n-tuple”: (anchor, positive, negative_1, …, negative_n, [scores])

*   ”labeled-pair”: (anchor, passage, score)

*   ”labeled-list”: (anchor, [passages], [scores])

Return type:
Dataset

sentence_transformers.util.normalize_embeddings(_embeddings:[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_)→[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/util/tensor.py#L68-L94)[](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.normalize_embeddings "Link to this definition")
Normalizes the embeddings matrix, so that each sentence embedding has unit length.

Parameters:
**embeddings** (_Tensor_) – The input embeddings matrix.

Returns:
The normalized embeddings matrix.

Return type:
Tensor

sentence_transformers.util.paraphrase_mining(_model:SentenceTransformer,sentences:list[str],show\_progress\_bar:bool=False,batch\_size:int=32,query\_chunk\_size:int=5000,corpus\_chunk\_size:int=100000,max\_pairs:int=500000,top\_k:int=100,score\_function:Callable[[Tensor,Tensor],Tensor]=<function cos\_sim>,truncate\_dim:int|None=None,prompt\_name:str|None=None,prompt:str|None=None_)→list[list[float|int]][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/util/retrieval.py#L23-L86)[](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.paraphrase_mining "Link to this definition")
Given a list of sentences / texts, this function performs paraphrase mining. It compares all sentences against all other sentences and returns a list with the pairs that have the highest cosine similarity score.

Parameters:
*   **model** ([_SentenceTransformer_](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")) – SentenceTransformer model for embedding computation

*   **sentences** (_List_ _[_ _str_ _]_) – A list of strings (texts or sentences)

*   **show_progress_bar** (_bool_ _,_ _optional_) – Plotting of a progress bar. Defaults to False.

*   **batch_size** (_int_ _,_ _optional_) – Number of texts that are encoded simultaneously by the model. Defaults to 32.

*   **query_chunk_size** (_int_ _,_ _optional_) – Search for most similar pairs for #query_chunk_size at the same time. Decrease, to lower memory footprint (increases run-time). Defaults to 5000.

*   **corpus_chunk_size** (_int_ _,_ _optional_) – Compare a sentence simultaneously against #corpus_chunk_size other sentences. Decrease, to lower memory footprint (increases run-time). Defaults to 100000.

*   **max_pairs** (_int_ _,_ _optional_) – Maximal number of text pairs returned. Defaults to 500000.

*   **top_k** (_int_ _,_ _optional_) – For each sentence, we retrieve up to top_k other sentences. Defaults to 100.

*   **score_function** (_Callable_ _[_ _[_ _Tensor_ _,_ _Tensor_ _]_ _,_ _Tensor_ _]_ _,_ _optional_) – Function for computing scores. By default, cosine similarity. Defaults to cos_sim.

*   **truncate_dim** (_int_ _,_ _optional_) – The dimension to truncate sentence embeddings to. If None, uses the model’s ones. Defaults to None.

*   **prompt_name** (_Optional_ _[_ _str_ _]_ _,_ _optional_) –

The name of a predefined prompt to use when encoding the sentence. It must match a key in the model prompts dictionary, which can be set during model initialization or loaded from the model configuration.

Ignored if prompt is provided. Defaults to None.

*   **prompt** (_Optional_ _[_ _str_ _]_ _,_ _optional_) –

A raw prompt string to prepend directly to the input sentence during encoding.

For instance, prompt=”query: “ transforms the sentence “What is the capital of France?” into: “query: What is the capital of France?”. Use this to override the prompt logic entirely and supply your own prefix. This takes precedence over prompt_name. Defaults to None.

Returns:
Returns a list of triplets with the format [score, id1, id2]

Return type:
List[List[Union[float, int]]]

sentence_transformers.util.semantic_search(_query\_embeddings:~torch.Tensor,corpus\_embeddings:~torch.Tensor,query\_chunk\_size:int=100,corpus\_chunk\_size:int=500000,top\_k:int=10,score\_function:~collections.abc.Callable[[~torch.Tensor,~torch.Tensor],~torch.Tensor]=<function cos\_sim>_)→list[list[dict[str,int|float]]][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/util/retrieval.py#L167-L255)[](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.semantic_search "Link to this definition")
This function performs by default a cosine similarity search between a list of query embeddings and a list of corpus embeddings. It can be used for Information Retrieval / Semantic Search for corpora up to about 1 Million entries.

Parameters:
*   **query_embeddings** ([`Tensor`](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")) – A 2 dimensional tensor with the query embeddings. Can be a sparse tensor.

*   **corpus_embeddings** ([`Tensor`](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")) – A 2 dimensional tensor with the corpus embeddings. Can be a sparse tensor.

*   **query_chunk_size** (_int_ _,_ _optional_) – Process 100 queries simultaneously. Increasing that value increases the speed, but requires more memory. Defaults to 100.

*   **corpus_chunk_size** (_int_ _,_ _optional_) – Scans the corpus 100k entries at a time. Increasing that value increases the speed, but requires more memory. Defaults to 500000.

*   **top_k** (_int_ _,_ _optional_) – Retrieve top k matching entries. Defaults to 10.

*   **score_function** (Callable[[[`Tensor`](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)"), [`Tensor`](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")], [`Tensor`](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")], optional) – Function for computing scores. By default, cosine similarity.

Returns:
A list with one entry for each query. Each entry is a list of dictionaries with the keys ‘corpus_id’ and ‘score’, sorted by decreasing cosine similarity scores.

Return type:
List[List[Dict[str, Union[int, float]]]]

sentence_transformers.util.truncate_embeddings(_embeddings:ndarray|[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_, _truncate\_dim:int|None_)→ndarray|[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/util/tensor.py#L105-L134)[](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.truncate_embeddings "Link to this definition")
Truncates the embeddings matrix.

Parameters:
*   **embeddings** (_Union_ _[_ _np.ndarray_ _,_[_torch.Tensor_](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_]_) – Embeddings to truncate.

*   **truncate_dim** (_Optional_ _[_ _int_ _]_) – The dimension to truncate sentence embeddings to. None does no truncation.

Example

>>> from sentence_transformers import SentenceTransformer
>>> from sentence_transformers.util import truncate_embeddings
>>> model = SentenceTransformer("tomaarsen/mpnet-base-nli-matryoshka")
>>> embeddings = model.encode(["It's so nice outside!", "Today is a beautiful day.", "He drove to work earlier"])
>>> embeddings.shape
(3, 768)
>>> model.similarity(embeddings, embeddings)
tensor([[1.0000, 0.8100, 0.1426],
 [0.8100, 1.0000, 0.2121],
 [0.1426, 0.2121, 1.0000]])
>>> truncated_embeddings = truncate_embeddings(embeddings, 128)
>>> truncated_embeddings.shape
>>> model.similarity(truncated_embeddings, truncated_embeddings)
tensor([[1.0000, 0.8092, 0.1987],
 [0.8092, 1.0000, 0.2716],
 [0.1987, 0.2716, 1.0000]])

Returns:
Truncated embeddings.

Return type:
Union[np.ndarray, [torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")]

Model Optimization[](https://sbert.net/docs/package_reference/util.html#module-sentence_transformers.backend "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

sentence_transformers.backend.export_dynamic_quantized_onnx_model(_model:[SentenceTransformer](https://sbert.net/docs/package\_reference/sentence\_transformer/SentenceTransformer.html#sentence\_transformers.SentenceTransformer "sentence\_transformers.SentenceTransformer")|[SparseEncoder](https://sbert.net/docs/package\_reference/sparse\_encoder/SparseEncoder.html#sentence\_transformers.sparse\_encoder.SparseEncoder "sentence\_transformers.sparse\_encoder.SparseEncoder")|[CrossEncoder](https://sbert.net/docs/package\_reference/cross\_encoder/cross\_encoder.html#sentence\_transformers.cross\_encoder.CrossEncoder "sentence\_transformers.cross\_encoder.CrossEncoder")_, _quantization\_config:QuantizationConfig|Literal['arm64','avx2','avx512','avx512\_vnni']_, _model\_name\_or\_path:str_, _push\_to\_hub:bool=False_, _create\_pr:bool=False_, _file\_suffix:str|None=None_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/backend/quantize.py#L24-L121)[](https://sbert.net/docs/package_reference/util.html#sentence_transformers.backend.export_dynamic_quantized_onnx_model "Link to this definition")
Export a quantized ONNX model from a SentenceTransformer, SparseEncoder, or CrossEncoder model.

This function applies dynamic quantization, i.e. without a calibration dataset. Each of the default quantization configurations quantize the model to int8, allowing for faster inference on CPUs, but are likely slower on GPUs.

See the following pages for more information & benchmarks:

*   [Sentence Transformer > Usage > Speeding up Inference](https://sbert.net/docs/sentence_transformer/usage/efficiency.html)

*   [Cross Encoder > Usage > Speeding up Inference](https://sbert.net/docs/cross_encoder/usage/efficiency.html)

Parameters:
*   **model** ([_SentenceTransformer_](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")_|_[_SparseEncoder_](https://sbert.net/docs/package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder")_|_[_CrossEncoder_](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")) – The SentenceTransformer, SparseEncoder, or CrossEncoder model to be quantized. Must be loaded with backend=”onnx”.

*   **quantization_config** (_QuantizationConfig_) – The quantization configuration.

*   **model_name_or_path** (_str_) – The path or Hugging Face Hub repository name where the quantized model will be saved.

*   **push_to_hub** (_bool_ _,_ _optional_) – Whether to push the quantized model to the Hugging Face Hub. Defaults to False.

*   **create_pr** (_bool_ _,_ _optional_) – Whether to create a pull request when pushing to the Hugging Face Hub. Defaults to False.

*   **file_suffix** (_str_ _|_ _None_ _,_ _optional_) – The suffix to add to the quantized model file name. Defaults to None.

Raises:
*   **ImportError** – If the required packages optimum and onnxruntime are not installed.

*   **ValueError** – If the provided model is not a valid SentenceTransformer, SparseEncoder, or CrossEncoder model loaded with backend=”onnx”.

*   **ValueError** – If the provided quantization_config is not valid.

Returns:
None

sentence_transformers.backend.export_optimized_onnx_model(_model:[SentenceTransformer](https://sbert.net/docs/package\_reference/sentence\_transformer/SentenceTransformer.html#sentence\_transformers.SentenceTransformer "sentence\_transformers.SentenceTransformer")|[SparseEncoder](https://sbert.net/docs/package\_reference/sparse\_encoder/SparseEncoder.html#sentence\_transformers.sparse\_encoder.SparseEncoder "sentence\_transformers.sparse\_encoder.SparseEncoder")|[CrossEncoder](https://sbert.net/docs/package\_reference/cross\_encoder/cross\_encoder.html#sentence\_transformers.cross\_encoder.CrossEncoder "sentence\_transformers.cross\_encoder.CrossEncoder")_, _optimization\_config:OptimizationConfig|Literal['O1','O2','O3','O4']_, _model\_name\_or\_path:str_, _push\_to\_hub:bool=False_, _create\_pr:bool=False_, _file\_suffix:str|None=None_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/backend/optimize.py#L19-L120)[](https://sbert.net/docs/package_reference/util.html#sentence_transformers.backend.export_optimized_onnx_model "Link to this definition")
Export an optimized ONNX model from a SentenceTransformer, SparseEncoder, or CrossEncoder model.

The O1-O4 optimization levels are defined by Optimum and are documented here: [https://huggingface.co/docs/optimum/main/en/onnxruntime/usage_guides/optimization](https://huggingface.co/docs/optimum/main/en/onnxruntime/usage_guides/optimization)

The optimization levels are:

*   O1: basic general optimizations.

*   O2: basic and extended general optimizations, transformers-specific fusions.

*   O3: same as O2 with GELU approximation.

*   O4: same as O3 with mixed precision (fp16, GPU-only)

See the following pages for more information & benchmarks:

*   [Sentence Transformer > Usage > Speeding up Inference](https://sbert.net/docs/sentence_transformer/usage/efficiency.html)

*   [Cross Encoder > Usage > Speeding up Inference](https://sbert.net/docs/cross_encoder/usage/efficiency.html)

Parameters:
*   **model** ([_SentenceTransformer_](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")_|_[_SparseEncoder_](https://sbert.net/docs/package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder")_|_[_CrossEncoder_](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")) – The SentenceTransformer, SparseEncoder, or CrossEncoder model to be optimized. Must be loaded with backend=”onnx”.

*   **optimization_config** (_OptimizationConfig_ _|_ _Literal_ _[_ _"O1"_ _,_ _"O2"_ _,_ _"O3"_ _,_ _"O4"_ _]_) – The optimization configuration or level.

*   **model_name_or_path** (_str_) – The path or Hugging Face Hub repository name where the optimized model will be saved.

*   **push_to_hub** (_bool_ _,_ _optional_) – Whether to push the optimized model to the Hugging Face Hub. Defaults to False.

*   **create_pr** (_bool_ _,_ _optional_) – Whether to create a pull request when pushing to the Hugging Face Hub. Defaults to False.

*   **file_suffix** (_str_ _|_ _None_ _,_ _optional_) – The suffix to add to the optimized model file name. Defaults to None.

Raises:
*   **ImportError** – If the required packages optimum and onnxruntime are not installed.

*   **ValueError** – If the provided model is not a valid SentenceTransformer, SparseEncoder, or CrossEncoder model loaded with backend=”onnx”.

*   **ValueError** – If the provided optimization_config is not valid.

Returns:
None

sentence_transformers.backend.export_static_quantized_openvino_model(_model:[SentenceTransformer](https://sbert.net/docs/package\_reference/sentence\_transformer/SentenceTransformer.html#sentence\_transformers.SentenceTransformer "sentence\_transformers.SentenceTransformer")|[SparseEncoder](https://sbert.net/docs/package\_reference/sparse\_encoder/SparseEncoder.html#sentence\_transformers.sparse\_encoder.SparseEncoder "sentence\_transformers.sparse\_encoder.SparseEncoder")|[CrossEncoder](https://sbert.net/docs/package\_reference/cross\_encoder/cross\_encoder.html#sentence\_transformers.cross\_encoder.CrossEncoder "sentence\_transformers.cross\_encoder.CrossEncoder")_, _quantization\_config:OVQuantizationConfig|dict|None_, _model\_name\_or\_path:str_, _dataset\_name:str|None=None_, _dataset\_config\_name:str|None=None_, _dataset\_split:str|None=None_, _column\_name:str|None=None_, _push\_to\_hub:bool=False_, _create\_pr:bool=False_, _file\_suffix:str='qint8\_quantized'_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/backend/quantize.py#L124-L254)[](https://sbert.net/docs/package_reference/util.html#sentence_transformers.backend.export_static_quantized_openvino_model "Link to this definition")
Export a quantized OpenVINO model from a SentenceTransformer, SparseEncoder, or CrossEncoder model.

This function applies Post-Training Static Quantization (PTQ) using a calibration dataset, which calibrates quantization constants without requiring model retraining. Each default quantization configuration converts the model to int8 precision, enabling faster inference while maintaining accuracy.

See the following pages for more information & benchmarks:

*   [Sentence Transformer > Usage > Speeding up Inference](https://sbert.net/docs/sentence_transformer/usage/efficiency.html)

*   [Cross Encoder > Usage > Speeding up Inference](https://sbert.net/docs/cross_encoder/usage/efficiency.html)

Parameters:
*   **model** ([_SentenceTransformer_](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")_|_[_SparseEncoder_](https://sbert.net/docs/package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder")_|_[_CrossEncoder_](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")) – The SentenceTransformer, SparseEncoder, or CrossEncoder model to be quantized. Must be loaded with backend=”openvino”.

*   **quantization_config** (_OVQuantizationConfig_ _|_ _dict_ _|_ _None_) – The quantization configuration. If None, default values are used.

*   **model_name_or_path** (_str_) – The path or Hugging Face Hub repository name where the quantized model will be saved.

*   **dataset_name** (_str_ _,_ _optional_) – The name of the dataset to load for calibration. If not specified, the sst2 subset of the glue dataset will be used by default.

*   **dataset_config_name** (_str_ _,_ _optional_) – The specific configuration of the dataset to load.

*   **dataset_split** (_str_ _,_ _optional_) – The split of the dataset to load (e.g., ‘train’, ‘test’). Defaults to None.

*   **column_name** (_str_ _,_ _optional_) – The column name in the dataset to use for calibration. Defaults to None.

*   **push_to_hub** (_bool_ _,_ _optional_) – Whether to push the quantized model to the Hugging Face Hub. Defaults to False.

*   **create_pr** (_bool_ _,_ _optional_) – Whether to create a pull request when pushing to the Hugging Face Hub. Defaults to False.

*   **file_suffix** (_str_ _,_ _optional_) – The suffix to add to the quantized model file name. Defaults to qint8_quantized.

Raises:
*   **ImportError** – If the required packages optimum and openvino are not installed.

*   **ValueError** – If the provided model is not a valid SentenceTransformer, SparseEncoder, or CrossEncoder model loaded with backend=”openvino”.

*   **ValueError** – If the provided quantization_config is not valid.

Returns:
None

Similarity Metrics[](https://sbert.net/docs/package_reference/util.html#module-sentence_transformers.util "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------

sentence_transformers.util.cos_sim(_a:list|ndarray|[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_, _b:list|ndarray|[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_)→[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/util/similarity.py#L29-L45)[](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.cos_sim "Link to this definition")
Computes the cosine similarity between two tensors.

Parameters:
*   **a** (_Union_ _[_ _list_ _,_ _np.ndarray_ _,_ _Tensor_ _]_) – The first tensor.

*   **b** (_Union_ _[_ _list_ _,_ _np.ndarray_ _,_ _Tensor_ _]_) – The second tensor.

Returns:
Matrix with res[i][j] = cos_sim(a[i], b[j])

Return type:
Tensor

sentence_transformers.util.dot_score(_a:list|ndarray|[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_, _b:list|ndarray|[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_)→[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/util/similarity.py#L71-L85)[](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.dot_score "Link to this definition")
Computes the dot-product dot_prod(a[i], b[j]) for all i and j.

Parameters:
*   **a** (_Union_ _[_ _list_ _,_ _np.ndarray_ _,_ _Tensor_ _]_) – The first tensor.

*   **b** (_Union_ _[_ _list_ _,_ _np.ndarray_ _,_ _Tensor_ _]_) – The second tensor.

Returns:
Matrix with res[i][j] = dot_prod(a[i], b[j])

Return type:
Tensor

sentence_transformers.util.euclidean_sim(_a:list|ndarray|[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_, _b:list|ndarray|[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_)→[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/util/similarity.py#L149-L177)[](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.euclidean_sim "Link to this definition")
Computes the euclidean similarity (i.e., negative distance) between two tensors. Handles sparse tensors without converting to dense when possible.

Parameters:
*   **a** (_Union_ _[_ _list_ _,_ _np.ndarray_ _,_ _Tensor_ _]_) – The first tensor.

*   **b** (_Union_ _[_ _list_ _,_ _np.ndarray_ _,_ _Tensor_ _]_) – The second tensor.

Returns:
Matrix with res[i][j] = -euclidean_distance(a[i], b[j])

Return type:
Tensor

sentence_transformers.util.manhattan_sim(_a:list|ndarray|[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_, _b:list|ndarray|[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_)→[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/util/similarity.py#L105-L129)[](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.manhattan_sim "Link to this definition")
Computes the manhattan similarity (i.e., negative distance) between two tensors. Handles sparse tensors without converting to dense when possible.

Parameters:
*   **a** (_Union_ _[_ _list_ _,_ _np.ndarray_ _,_ _Tensor_ _]_) – The first tensor.

*   **b** (_Union_ _[_ _list_ _,_ _np.ndarray_ _,_ _Tensor_ _]_) – The second tensor.

Returns:
Matrix with res[i][j] = -manhattan_distance(a[i], b[j])

Return type:
Tensor

sentence_transformers.util.pairwise_cos_sim(_a:[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_, _b:[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_)→[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/util/similarity.py#L48-L68)[](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.pairwise_cos_sim "Link to this definition")
Computes the pairwise cosine similarity cos_sim(a[i], b[i]).

Parameters:
*   **a** (_Union_ _[_ _list_ _,_ _np.ndarray_ _,_ _Tensor_ _]_) – The first tensor.

*   **b** (_Union_ _[_ _list_ _,_ _np.ndarray_ _,_ _Tensor_ _]_) – The second tensor.

Returns:
Vector with res[i] = cos_sim(a[i], b[i])

Return type:
Tensor

sentence_transformers.util.pairwise_dot_score(_a:[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_, _b:[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_)→[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/util/similarity.py#L88-L102)[](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.pairwise_dot_score "Link to this definition")
Computes the pairwise dot-product dot_prod(a[i], b[i]).

Parameters:
*   **a** (_Union_ _[_ _list_ _,_ _np.ndarray_ _,_ _Tensor_ _]_) – The first tensor.

*   **b** (_Union_ _[_ _list_ _,_ _np.ndarray_ _,_ _Tensor_ _]_) – The second tensor.

Returns:
Vector with res[i] = dot_prod(a[i], b[i])

Return type:
Tensor

sentence_transformers.util.pairwise_euclidean_sim(_a:list|ndarray|[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_, _b:list|ndarray|[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/util/similarity.py#L180-L194)[](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.pairwise_euclidean_sim "Link to this definition")
Computes the euclidean distance (i.e., negative distance) between pairs of tensors.

Parameters:
*   **a** (_Union_ _[_ _list_ _,_ _np.ndarray_ _,_ _Tensor_ _]_) – The first tensor.

*   **b** (_Union_ _[_ _list_ _,_ _np.ndarray_ _,_ _Tensor_ _]_) – The second tensor.

Returns:
Vector with res[i] = -euclidean_distance(a[i], b[i])

Return type:
Tensor

sentence_transformers.util.pairwise_manhattan_sim(_a:list|ndarray|[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_, _b:list|ndarray|[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/util/similarity.py#L132-L146)[](https://sbert.net/docs/package_reference/util.html#sentence_transformers.util.pairwise_manhattan_sim "Link to this definition")
Computes the manhattan similarity (i.e., negative distance) between pairs of tensors.

Parameters:
*   **a** (_Union_ _[_ _list_ _,_ _np.ndarray_ _,_ _Tensor_ _]_) – The first tensor.

*   **b** (_Union_ _[_ _list_ _,_ _np.ndarray_ _,_ _Tensor_ _]_) – The second tensor.

Returns:
Vector with res[i] = -manhattan_distance(a[i], b[i])

Return type:
Tensor

[Previous](https://sbert.net/docs/package_reference/sparse_encoder/search_engines.html "Search Engines")

* * *

© Copyright 2026.

 Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org/).
