# Source: https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html

Title: SentenceTransformer — Sentence Transformers documentation

URL Source: https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html

Published Time: Tue, 17 Feb 2026 14:05:52 GMT

Markdown Content:
SentenceTransformer — Sentence Transformers documentation
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
    *   [SentenceTransformer](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#)
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
*   SentenceTransformer
*   [Edit on GitHub](https://github.com/huggingface/sentence-transformers/blob/main/docs/package_reference/sentence_transformer/SentenceTransformer.md)

* * *

SentenceTransformer[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentencetransformer "Link to this heading")
=========================================================================================================================================================

SentenceTransformer[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#id1 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.SentenceTransformer(_model\_name\_or\_path:str|None=None_, _modules:Iterable[[Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.10)")]|None=None_, _device:str|None=None_, _prompts:dict[str,str]|None=None_, _default\_prompt\_name:str|None=None_, _similarity\_fn\_name:str|[SimilarityFunction](https://sbert.net/docs/package\_reference/sparse\_encoder/SparseEncoder.html#sentence\_transformers.SimilarityFunction "sentence\_transformers.similarity\_functions.SimilarityFunction")|None=None_, _cache\_folder:str|None=None_, _trust\_remote\_code:bool=False_, _revision:str|None=None_, _local\_files\_only:bool=False_, _token:bool|str|None=None_, _use\_auth\_token:bool|str|None=None_, _truncate\_dim:int|None=None_, _model\_kwargs:dict[str,Any]|None=None_, _tokenizer\_kwargs:dict[str,Any]|None=None_, _config\_kwargs:dict[str,Any]|None=None_, _model\_card\_data:[SentenceTransformerModelCardData](https://sbert.net/docs/package\_reference/sentence\_transformer/SentenceTransformer.html#sentence\_transformers.model\_card.SentenceTransformerModelCardData "sentence\_transformers.model\_card.SentenceTransformerModelCardData")|None=None_, _backend:Literal['torch','onnx','openvino']='torch'_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/SentenceTransformer.py#L61-L2514)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "Link to this definition")
Loads or creates a SentenceTransformer model that can be used to map sentences / text to embeddings.

Parameters:
*   **model_name_or_path** (_str_ _,_ _optional_) – If it is a filepath on disk, it loads the model from that path. If it is not a path, it first tries to download a pre-trained SentenceTransformer model. If that fails, tries to construct a model from the Hugging Face Hub with that name.

*   **modules** (_Iterable_ _[_ _nn.Module_ _]_ _,_ _optional_) – A list of torch Modules that should be called sequentially, can be used to create custom SentenceTransformer models from scratch.

*   **device** (_str_ _,_ _optional_) – Device (like “cuda”, “cpu”, “mps”, “npu”) that should be used for computation. If None, checks if a GPU can be used.

*   **prompts** (_Dict_ _[_ _str_ _,_ _str_ _]_ _,_ _optional_) – A dictionary with prompts for the model. The key is the prompt name, the value is the prompt text. The prompt text will be prepended before any text to encode. For example: {“query”: “query: “, “passage”: “passage: “} or {“clustering”: “Identify the main category based on the titles in “}.

*   **default_prompt_name** (_str_ _,_ _optional_) – The name of the prompt that should be used by default. If not set, no prompt will be applied.

*   **similarity_fn_name** (_str_ _or_[_SimilarityFunction_](https://sbert.net/docs/package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")_,_ _optional_) – The name of the similarity function to use. Valid options are “cosine”, “dot”, “euclidean”, and “manhattan”. If not set, it is automatically set to “cosine” if similarity or similarity_pairwise are called while model.similarity_fn_name is still None.

*   **cache_folder** (_str_ _,_ _optional_) – Path to store models. Can also be set by the SENTENCE_TRANSFORMERS_HOME environment variable.

*   **trust_remote_code** (_bool_ _,_ _optional_) – Whether or not to allow for custom models defined on the Hub in their own modeling files. This option should only be set to True for repositories you trust and in which you have read the code, as it will execute code present on the Hub on your local machine.

*   **revision** (_str_ _,_ _optional_) – The specific model version to use. It can be a branch name, a tag name, or a commit id, for a stored model on Hugging Face.

*   **local_files_only** (_bool_ _,_ _optional_) – Whether or not to only look at local files (i.e., do not try to download the model).

*   **token** (_bool_ _or_ _str_ _,_ _optional_) – Hugging Face authentication token to download private models.

*   **use_auth_token** (_bool_ _or_ _str_ _,_ _optional_) – Deprecated argument. Please use token instead.

*   **truncate_dim** (_int_ _,_ _optional_) – The dimension to truncate sentence embeddings to. Defaults to None.

*   **model_kwargs** (_Dict_ _[_ _str_ _,_ _Any_ _]_ _,_ _optional_) –

Additional model configuration parameters to be passed to the Hugging Face Transformers model. Particularly useful options are:

    *   `torch_dtype`: Override the default torch.dtype and load the model under a specific dtype. The different options are:

> 1. `torch.float16`, `torch.bfloat16` or `torch.float`: load in a specified `dtype`, ignoring the model’s `config.torch_dtype` if one exists. If not specified - the model will get loaded in `torch.float` (fp32).
> 
> 
> 2. `"auto"` - A `torch_dtype` entry in the `config.json` file of the model will be attempted to be used. If this entry isn’t found then next check the `dtype` of the first weight in the checkpoint that’s of a floating point type and use that as `dtype`. This will load the model using the `dtype` it was saved in at the end of the training. It can’t be used as an indicator of how the model was trained. Since it could be trained in one of half precision dtypes, but saved in fp32.

    *   `attn_implementation`: The attention implementation to use in the model (if relevant). Can be any of “eager” (manual implementation of the attention), “sdpa” (using [F.scaled_dot_product_attention](https://pytorch.org/docs/master/generated/torch.nn.functional.scaled_dot_product_attention.html)), or “flash_attention_2” (using [Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention)). By default, if available, SDPA will be used for torch>=2.1.1. The default is otherwise the manual “eager” implementation.

    *   `provider`: If backend is “onnx”, this is the provider to use for inference, for example “CPUExecutionProvider”, “CUDAExecutionProvider”, etc. See [https://onnxruntime.ai/docs/execution-providers/](https://onnxruntime.ai/docs/execution-providers/) for all ONNX execution providers.

    *   `file_name`: If backend is “onnx” or “openvino”, this is the file name to load, useful for loading optimized or quantized ONNX or OpenVINO models.

    *   `export`: If backend is “onnx” or “openvino”, then this is a boolean flag specifying whether this model should be exported to the backend. If not specified, the model will be exported only if the model repository or directory does not already contain an exported model.

See the [PreTrainedModel.from_pretrained](https://huggingface.co/docs/transformers/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) documentation for more details.

*   **tokenizer_kwargs** (_Dict_ _[_ _str_ _,_ _Any_ _]_ _,_ _optional_) – Additional tokenizer configuration parameters to be passed to the Hugging Face Transformers tokenizer. See the [AutoTokenizer.from_pretrained](https://huggingface.co/docs/transformers/en/model_doc/auto#transformers.AutoTokenizer.from_pretrained) documentation for more details.

*   **config_kwargs** (_Dict_ _[_ _str_ _,_ _Any_ _]_ _,_ _optional_) – Additional model configuration parameters to be passed to the Hugging Face Transformers config. See the [AutoConfig.from_pretrained](https://huggingface.co/docs/transformers/en/model_doc/auto#transformers.AutoConfig.from_pretrained) documentation for more details.

*   **model_card_data** ([`SentenceTransformerModelCardData`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.model_card.SentenceTransformerModelCardData "sentence_transformers.model_card.SentenceTransformerModelCardData"), optional) – A model card data object that contains information about the model. This is used to generate a model card when saving the model. If not set, a default model card data object is created.

*   **backend** (_str_) – The backend to use for inference. Can be one of “torch” (default), “onnx”, or “openvino”. See [https://sbert.net/docs/sentence_transformer/usage/efficiency.html](https://sbert.net/docs/sentence_transformer/usage/efficiency.html) for benchmarking information on the different backends.

Example

from sentence_transformers import SentenceTransformer

# Load a pre-trained SentenceTransformer model
model = SentenceTransformer('all-mpnet-base-v2')

# Encode some texts
sentences = [
    "The weather is lovely today.",
    "It's so sunny outside!",
    "He drove to the stadium.",
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# (3, 768)

# Get the similarity scores between all sentences
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.6817, 0.0492],
# [0.6817, 1.0000, 0.0421],
# [0.0492, 0.0421, 1.0000]])

Initializes internal Module state, shared by both nn.Module and ScriptModule.

active_adapters()→list[str][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/peft_mixin.py#L107-L119)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.active_adapters "Link to this definition")
If you are not familiar with adapters and PEFT methods, we invite you to read more about them on the PEFT official documentation: [https://huggingface.co/docs/peft](https://huggingface.co/docs/peft)

Gets the current active adapters of the model. In case of multi-adapter inference (combining multiple adapters for inference) returns the list of all active adapters so that users can deal with them accordingly.

For previous PEFT versions (that does not support multi-adapter inference), module.active_adapter will return a single string.

add_adapter(_*args_, _**kwargs_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/peft_mixin.py#L58-L76)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.add_adapter "Link to this definition")
Adds a fresh new adapter to the current model for training purposes. If no adapter name is passed, a default name is assigned to the adapter to follow the convention of PEFT library (in PEFT we use “default” as the default adapter name).

Requires peft as a backend to load the adapter weights and the underlying model to be compatible with PEFT.

Parameters:
*   ***args** – Positional arguments to pass to the underlying AutoModel add_adapter function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.add_adapter](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.add_adapter)

*   ****kwargs** – Keyword arguments to pass to the underlying AutoModel add_adapter function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.add_adapter](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.add_adapter)

bfloat16()→T[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.bfloat16 "Link to this definition")
Casts all floating point parameters and buffers to `bfloat16` datatype.

Note

This method modifies the module in-place.

Returns:
self

Return type:
[Module](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

compile(_*args_, _**kwargs_)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.compile "Link to this definition")
Compile this Module’s forward using [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "(in PyTorch v2.10)").

This Module’s  __call__  method is compiled and all arguments are passed as-is to [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "(in PyTorch v2.10)").

See [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "(in PyTorch v2.10)") for details on the arguments for this function.

cpu()→T[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.cpu "Link to this definition")
Moves all model parameters and buffers to the CPU.

Note

This method modifies the module in-place.

Returns:
self

Return type:
[Module](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

cuda(_device:int|[device](https://docs.pytorch.org/docs/stable/tensor\_attributes.html#torch.device "(in PyTorch v2.10)")|None=None_)→T[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.cuda "Link to this definition")
Moves all model parameters and buffers to the GPU.

This also makes associated parameters and buffers different objects. So it should be called before constructing optimizer if the module will live on GPU while being optimized.

Note

This method modifies the module in-place.

Parameters:
**device** (_int_ _,_ _optional_) – if specified, all parameters will be copied to that device

Returns:
self

Return type:
[Module](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

delete_adapter(_*args_, _**kwargs_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/peft_mixin.py#L143-L158)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.delete_adapter "Link to this definition")
If you are not familiar with adapters and PEFT methods, we invite you to read more about them on the PEFT official documentation: [https://huggingface.co/docs/peft](https://huggingface.co/docs/peft)

Delete an adapter’s LoRA layers from the underlying model.

Parameters:
*   ***args** – Positional arguments to pass to the underlying AutoModel delete_adapter function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.delete_adapter](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.delete_adapter)

*   ****kwargs** – Keyword arguments to pass to the underlying AutoModel delete_adapter function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.delete_adapter](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.delete_adapter)

_property_ device _:[device](https://docs.pytorch.org/docs/stable/tensor\_attributes.html#torch.device "(in PyTorch v2.10)")_[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.device "Link to this definition")
Get torch.device from module, assuming that the whole module has one device. In case there are no PyTorch parameters, fall back to CPU.

disable_adapters()→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/peft_mixin.py#L93-L98)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.disable_adapters "Link to this definition")
Disable all adapters that are attached to the model. This leads to inferring with the base model only.

double()→T[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.double "Link to this definition")
Casts all floating point parameters and buffers to `double` datatype.

Note

This method modifies the module in-place.

Returns:
self

Return type:
[Module](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

enable_adapters()→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/peft_mixin.py#L100-L105)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.enable_adapters "Link to this definition")
Enable adapters that are attached to the model. The model will use self.active_adapter()

encode(_sentences:str_, _prompt\_name:str|None=None_, _prompt:str|None=None_, _batch\_size:int=32_, _show\_progress\_bar:bool|None=None_, _output\_value:Literal['sentence\_embedding','token\_embeddings']='sentence\_embedding'_, _precision:Literal['float32','int8','uint8','binary','ubinary']='float32'_, _convert\_to\_numpy:Literal[False]=True_, _convert\_to\_tensor:bool=False_, _device:str|list[str|[torch.device](https://docs.pytorch.org/docs/stable/tensor\_attributes.html#torch.device "(in PyTorch v2.10)")]|None=None_, _normalize\_embeddings:bool=False_, _truncate\_dim:int|None=None_, _pool:dict[Literal['input','output','processes'],Any]|None=None_, _chunk\_size:int|None=None_, _**kwargs_)→Tensor[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/SentenceTransformer.py#L856-L1159)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode "Link to this definition")encode(_sentences:str|list[str]|np.ndarray_, _prompt\_name:str|None=None_, _prompt:str|None=None_, _batch\_size:int=32_, _show\_progress\_bar:bool|None=None_, _output\_value:Literal['sentence\_embedding']='sentence\_embedding'_, _precision:Literal['float32','int8','uint8','binary','ubinary']='float32'_, _convert\_to\_numpy:Literal[True]=True_, _convert\_to\_tensor:Literal[False]=False_, _device:str|list[str|[torch.device](https://docs.pytorch.org/docs/stable/tensor\_attributes.html#torch.device "(in PyTorch v2.10)")]|None=None_, _normalize\_embeddings:bool=False_, _truncate\_dim:int|None=None_, _pool:dict[Literal['input','output','processes'],Any]|None=None_, _chunk\_size:int|None=None_, _**kwargs_)→np.ndarray encode(_sentences:str|list[str]|np.ndarray_, _prompt\_name:str|None=None_, _prompt:str|None=None_, _batch\_size:int=32_, _show\_progress\_bar:bool|None=None_, _output\_value:Literal['sentence\_embedding']='sentence\_embedding'_, _precision:Literal['float32','int8','uint8','binary','ubinary']='float32'_, _convert\_to\_numpy:bool=True_, _convert\_to\_tensor:Literal[True]=False_, _device:str|list[str|[torch.device](https://docs.pytorch.org/docs/stable/tensor\_attributes.html#torch.device "(in PyTorch v2.10)")]|None=None_, _normalize\_embeddings:bool=False_, _truncate\_dim:int|None=None_, _pool:dict[Literal['input','output','processes'],Any]|None=None_, _chunk\_size:int|None=None_, _**kwargs_)→Tensor encode(_sentences:list[str]|np.ndarray_, _prompt\_name:str|None=None_, _prompt:str|None=None_, _batch\_size:int=32_, _show\_progress\_bar:bool|None=None_, _output\_value:Literal['sentence\_embedding','token\_embeddings']='sentence\_embedding'_, _precision:Literal['float32','int8','uint8','binary','ubinary']='float32'_, _convert\_to\_numpy:bool=True_, _convert\_to\_tensor:bool=False_, _device:str|list[str|[torch.device](https://docs.pytorch.org/docs/stable/tensor\_attributes.html#torch.device "(in PyTorch v2.10)")]|None=None_, _normalize\_embeddings:bool=False_, _truncate\_dim:int|None=None_, _pool:dict[Literal['input','output','processes'],Any]|None=None_, _chunk\_size:int|None=None_, _**kwargs_)→list[Tensor]encode(_sentences:list[str]|np.ndarray_, _prompt\_name:str|None=None_, _prompt:str|None=None_, _batch\_size:int=32_, _show\_progress\_bar:bool|None=None_, _output\_value:None='sentence\_embedding'_, _precision:Literal['float32','int8','uint8','binary','ubinary']='float32'_, _convert\_to\_numpy:bool=True_, _convert\_to\_tensor:bool=False_, _device:str|list[str|[torch.device](https://docs.pytorch.org/docs/stable/tensor\_attributes.html#torch.device "(in PyTorch v2.10)")]|None=None_, _normalize\_embeddings:bool=False_, _truncate\_dim:int|None=None_, _pool:dict[Literal['input','output','processes'],Any]|None=None_, _chunk\_size:int|None=None_, _**kwargs_)→list[dict[str,Tensor]]encode(_sentences:str_, _prompt\_name:str|None=None_, _prompt:str|None=None_, _batch\_size:int=32_, _show\_progress\_bar:bool|None=None_, _output\_value:None='sentence\_embedding'_, _precision:Literal['float32','int8','uint8','binary','ubinary']='float32'_, _convert\_to\_numpy:bool=True_, _convert\_to\_tensor:bool=False_, _device:str|list[str|[torch.device](https://docs.pytorch.org/docs/stable/tensor\_attributes.html#torch.device "(in PyTorch v2.10)")]|None=None_, _normalize\_embeddings:bool=False_, _truncate\_dim:int|None=None_, _pool:dict[Literal['input','output','processes'],Any]|None=None_, _chunk\_size:int|None=None_, _**kwargs_)→dict[str,Tensor]encode(_sentences:str_, _prompt\_name:str|None=None_, _prompt:str|None=None_, _batch\_size:int=32_, _show\_progress\_bar:bool|None=None_, _output\_value:Literal['token\_embeddings']='sentence\_embedding'_, _precision:Literal['float32','int8','uint8','binary','ubinary']='float32'_, _convert\_to\_numpy:bool=True_, _convert\_to\_tensor:bool=False_, _device:str|list[str|[torch.device](https://docs.pytorch.org/docs/stable/tensor\_attributes.html#torch.device "(in PyTorch v2.10)")]|None=None_, _normalize\_embeddings:bool=False_, _truncate\_dim:int|None=None_, _pool:dict[Literal['input','output','processes'],Any]|None=None_, _chunk\_size:int|None=None_, _**kwargs_)→Tensor
Computes sentence embeddings.

Tip

If you are unsure whether you should use [`encode()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode"), [`encode_query()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode_query "sentence_transformers.SentenceTransformer.encode_query"), or [`encode_document()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode_document "sentence_transformers.SentenceTransformer.encode_document"), your best bet is to use [`encode_query()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode_query "sentence_transformers.SentenceTransformer.encode_query") and [`encode_document()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode_document "sentence_transformers.SentenceTransformer.encode_document") for Information Retrieval tasks with clear query and document/passage distinction, and use [`encode()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode") for all other tasks.

Note that [`encode()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode") is the most general method and can be used for any task, including Information Retrieval, and that if the model was not trained with predefined prompts and/or task types, then all three methods will return identical embeddings.

Parameters:
*   **sentences** (_Union_ _[_ _str_ _,_ _List_ _[_ _str_ _]_ _]_) – The sentences to embed.

*   **prompt_name** (_Optional_ _[_ _str_ _]_ _,_ _optional_) – The name of the prompt to use for encoding. Must be a key in the prompts dictionary, which is either set in the constructor or loaded from the model configuration. For example if `prompt_name` is “query” and the `prompts` is {“query”: “query: “, …}, then the sentence “What is the capital of France?” will be encoded as “query: What is the capital of France?” because the sentence is appended to the prompt. If `prompt` is also set, this argument is ignored. Defaults to None.

*   **prompt** (_Optional_ _[_ _str_ _]_ _,_ _optional_) – The prompt to use for encoding. For example, if the prompt is “query: “, then the sentence “What is the capital of France?” will be encoded as “query: What is the capital of France?” because the sentence is appended to the prompt. If `prompt` is set, `prompt_name` is ignored. Defaults to None.

*   **batch_size** (_int_ _,_ _optional_) – The batch size used for the computation. Defaults to 32.

*   **show_progress_bar** (_bool_ _,_ _optional_) – Whether to output a progress bar when encode sentences. Defaults to None.

*   **output_value** (_Optional_ _[_ _Literal_ _[_ _"sentence\_embedding"_ _,_ _"token\_embeddings"_ _]_ _]_ _,_ _optional_) – The type of embeddings to return: “sentence_embedding” to get sentence embeddings, “token_embeddings” to get wordpiece token embeddings, and None, to get all output values. Defaults to “sentence_embedding”.

*   **precision** (_Literal_ _[_ _"float32"_ _,_ _"int8"_ _,_ _"uint8"_ _,_ _"binary"_ _,_ _"ubinary"_ _]_ _,_ _optional_) – The precision to use for the embeddings. Can be “float32”, “int8”, “uint8”, “binary”, or “ubinary”. All non-float32 precisions are quantized embeddings. Quantized embeddings are smaller in size and faster to compute, but may have a lower accuracy. They are useful for reducing the size of the embeddings of a corpus for semantic search, among other tasks. Defaults to “float32”.

*   **convert_to_numpy** (_bool_ _,_ _optional_) – Whether the output should be a list of numpy vectors. If False, it is a list of PyTorch tensors. Defaults to True.

*   **convert_to_tensor** (_bool_ _,_ _optional_) – Whether the output should be one large tensor. Overwrites convert_to_numpy. Defaults to False.

*   **device** (_Union_ _[_ _str_ _,_ _List_ _[_ _str_ _]_ _,_ _None_ _]_ _,_ _optional_) –

Device(s) to use for computation. Can be:

    *   A single device string (e.g., “cuda:0”, “cpu”) for single-process encoding

    *   A list of device strings (e.g., [“cuda:0”, “cuda:1”], [“cpu”, “cpu”, “cpu”, “cpu”]) to distribute encoding across multiple processes

    *   None to auto-detect available device for single-process encoding

If a list is provided, multi-process encoding will be used. Defaults to None.

*   **normalize_embeddings** (_bool_ _,_ _optional_) – Whether to normalize returned vectors to have length 1. In that case, the faster dot-product (util.dot_score) instead of cosine similarity can be used. Defaults to False.

*   **truncate_dim** (_int_ _,_ _optional_) – The dimension to truncate sentence embeddings to. Truncation is especially interesting for [Matryoshka models](https://sbert.net/examples/sentence_transformer/training/matryoshka/README.html), i.e. models that are trained to still produce useful embeddings even if the embedding dimension is reduced. Truncated embeddings require less memory and are faster to perform retrieval with, but note that inference is just as fast, and the embedding performance is worse than the full embeddings. If None, the `truncate_dim` from the model initialization is used. Defaults to None.

*   **pool** (_Dict_ _[_ _Literal_ _[_ _"input"_ _,_ _"output"_ _,_ _"processes"_ _]_ _,_ _Any_ _]_ _,_ _optional_) – A pool created by start_multi_process_pool() for multi-process encoding. If provided, the encoding will be distributed across multiple processes. This is recommended for large datasets and when multiple GPUs are available. Defaults to None.

*   **chunk_size** (_int_ _,_ _optional_) – Size of chunks for multi-process encoding. Only used with multiprocessing, i.e. when `pool` is not None or `device` is a list. If None, a sensible default is calculated. Defaults to None.

Returns:
By default, a 2d numpy array with shape [num_inputs, output_dimension] is returned. If only one string input is provided, then the output is a 1d array with shape [output_dimension]. If `convert_to_tensor`, a torch Tensor is returned instead. If `self.truncate_dim <= output_dimension` then output_dimension is `self.truncate_dim`.

Return type:
Union[List[Tensor], ndarray, Tensor]

Example

from sentence_transformers import SentenceTransformer

# Load a pre-trained SentenceTransformer model
model = SentenceTransformer("all-mpnet-base-v2")

# Encode some texts
sentences = [
    "The weather is lovely today.",
    "It's so sunny outside!",
    "He drove to the stadium.",
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# (3, 768)

encode_document(_sentences:str|list[str]|ndarray_, _prompt\_name:str|None=None_, _prompt:str|None=None_, _batch\_size:int=32_, _show\_progress\_bar:bool|None=None_, _output\_value:Literal['sentence\_embedding','token\_embeddings']|None='sentence\_embedding'_, _precision:Literal['float32','int8','uint8','binary','ubinary']='float32'_, _convert\_to\_numpy:bool=True_, _convert\_to\_tensor:bool=False_, _device:str|list[str|[device](https://docs.pytorch.org/docs/stable/tensor\_attributes.html#torch.device "(in PyTorch v2.10)")]|None=None_, _normalize\_embeddings:bool=False_, _truncate\_dim:int|None=None_, _pool:dict[Literal['input','output','processes'],Any]|None=None_, _chunk\_size:int|None=None_, _**kwargs_)→list[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")]|ndarray|[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")|dict[str,[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")]|list[dict[str,[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")]][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/SentenceTransformer.py#L575-L705)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode_document "Link to this definition")
Computes sentence embeddings specifically optimized for document/passage representation.

This method is a specialized version of [`encode()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode") that differs in exactly two ways:

1.   If no `prompt_name` or `prompt` is provided, it uses a predefined “document” prompt, if available in the model’s `prompts` dictionary.

2.   It sets the `task` to “document”. If the model has a [`Router`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Router "sentence_transformers.models.Router") module, it will use the “document” task type to route the input through the appropriate submodules.

Tip

If you are unsure whether you should use [`encode()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode"), [`encode_query()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode_query "sentence_transformers.SentenceTransformer.encode_query"), or [`encode_document()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode_document "sentence_transformers.SentenceTransformer.encode_document"), your best bet is to use [`encode_query()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode_query "sentence_transformers.SentenceTransformer.encode_query") and [`encode_document()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode_document "sentence_transformers.SentenceTransformer.encode_document") for Information Retrieval tasks with clear query and document/passage distinction, and use [`encode()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode") for all other tasks.

Note that [`encode()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode") is the most general method and can be used for any task, including Information Retrieval, and that if the model was not trained with predefined prompts and/or task types, then all three methods will return identical embeddings.

Parameters:
*   **sentences** (_Union_ _[_ _str_ _,_ _List_ _[_ _str_ _]_ _]_) – The sentences to embed.

*   **prompt_name** (_Optional_ _[_ _str_ _]_ _,_ _optional_) – The name of the prompt to use for encoding. Must be a key in the prompts dictionary, which is either set in the constructor or loaded from the model configuration. For example if `prompt_name` is “query” and the `prompts` is {“query”: “query: “, …}, then the sentence “What is the capital of France?” will be encoded as “query: What is the capital of France?” because the sentence is appended to the prompt. If `prompt` is also set, this argument is ignored. Defaults to None.

*   **prompt** (_Optional_ _[_ _str_ _]_ _,_ _optional_) – The prompt to use for encoding. For example, if the prompt is “query: “, then the sentence “What is the capital of France?” will be encoded as “query: What is the capital of France?” because the sentence is appended to the prompt. If `prompt` is set, `prompt_name` is ignored. Defaults to None.

*   **batch_size** (_int_ _,_ _optional_) – The batch size used for the computation. Defaults to 32.

*   **show_progress_bar** (_bool_ _,_ _optional_) – Whether to output a progress bar when encode sentences. Defaults to None.

*   **output_value** (_Optional_ _[_ _Literal_ _[_ _"sentence\_embedding"_ _,_ _"token\_embeddings"_ _]_ _]_ _,_ _optional_) – The type of embeddings to return: “sentence_embedding” to get sentence embeddings, “token_embeddings” to get wordpiece token embeddings, and None, to get all output values. Defaults to “sentence_embedding”.

*   **precision** (_Literal_ _[_ _"float32"_ _,_ _"int8"_ _,_ _"uint8"_ _,_ _"binary"_ _,_ _"ubinary"_ _]_ _,_ _optional_) – The precision to use for the embeddings. Can be “float32”, “int8”, “uint8”, “binary”, or “ubinary”. All non-float32 precisions are quantized embeddings. Quantized embeddings are smaller in size and faster to compute, but may have a lower accuracy. They are useful for reducing the size of the embeddings of a corpus for semantic search, among other tasks. Defaults to “float32”.

*   **convert_to_numpy** (_bool_ _,_ _optional_) – Whether the output should be a list of numpy vectors. If False, it is a list of PyTorch tensors. Defaults to True.

*   **convert_to_tensor** (_bool_ _,_ _optional_) – Whether the output should be one large tensor. Overwrites convert_to_numpy. Defaults to False.

*   **device** (_Union_ _[_ _str_ _,_ _List_ _[_ _str_ _]_ _,_ _None_ _]_ _,_ _optional_) –

Device(s) to use for computation. Can be:

    *   A single device string (e.g., “cuda:0”, “cpu”) for single-process encoding

    *   A list of device strings (e.g., [“cuda:0”, “cuda:1”], [“cpu”, “cpu”, “cpu”, “cpu”]) to distribute encoding across multiple processes

    *   None to auto-detect available device for single-process encoding

If a list is provided, multi-process encoding will be used. Defaults to None.

*   **normalize_embeddings** (_bool_ _,_ _optional_) – Whether to normalize returned vectors to have length 1. In that case, the faster dot-product (util.dot_score) instead of cosine similarity can be used. Defaults to False.

*   **truncate_dim** (_int_ _,_ _optional_) –

The dimension to truncate sentence embeddings to. Truncation is especially interesting for [Matryoshka models](https://sbert.net/examples/sentence_transformer/training/matryoshka/README.html), i.e. models that are trained to still produce useful embeddings even if the embedding dimension is reduced. Truncated embeddings require less memory and are faster to perform retrieval with, but note that inference is just as fast, and the embedding performance is worse than the full embeddings. If None, the `truncate_dim` from the model initialization is used. Defaults to None.

*   **pool** (_Dict_ _[_ _Literal_ _[_ _"input"_ _,_ _"output"_ _,_ _"processes"_ _]_ _,_ _Any_ _]_ _,_ _optional_) – A pool created by start_multi_process_pool() for multi-process encoding. If provided, the encoding will be distributed across multiple processes. This is recommended for large datasets and when multiple GPUs are available. Defaults to None.

*   **chunk_size** (_int_ _,_ _optional_) – Size of chunks for multi-process encoding. Only used with multiprocessing, i.e. when `pool` is not None or `device` is a list. If None, a sensible default is calculated. Defaults to None.

Returns:
By default, a 2d numpy array with shape [num_inputs, output_dimension] is returned. If only one string input is provided, then the output is a 1d array with shape [output_dimension]. If `convert_to_tensor`, a torch Tensor is returned instead. If `self.truncate_dim <= output_dimension` then output_dimension is `self.truncate_dim`.

Return type:
Union[List[Tensor], ndarray, Tensor]

Example

from sentence_transformers import SentenceTransformer

# Load a pre-trained SentenceTransformer model
model = SentenceTransformer("mixedbread-ai/mxbai-embed-large-v1")

# Encode some documents
documents = [
    "This research paper discusses the effects of climate change on marine life.",
    "The article explores the history of artificial intelligence development.",
    "This document contains technical specifications for the new product line.",
]

# Using document-specific encoding
embeddings = model.encode_document(documents)
print(embeddings.shape)
# (3, 768)

encode_multi_process(_sentences:list[str]_, _pool:dict[Literal['input','output','processes'],Any]_, _prompt\_name:str|None=None_, _prompt:str|None=None_, _batch\_size:int=32_, _chunk\_size:int|None=None_, _show\_progress\_bar:bool|None=None_, _precision:Literal['float32','int8','uint8','binary','ubinary']='float32'_, _normalize\_embeddings:bool=False_, _truncate\_dim:int|None=None_)→ndarray[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/SentenceTransformer.py#L1374-L1467)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode_multi_process "Link to this definition")

Warning

This method is deprecated. You can now call [`SentenceTransformer.encode`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode") with the same parameters instead, which will automatically handle multi-process encoding using the provided `pool`.

Encodes a list of sentences using multiple processes and GPUs via [`SentenceTransformer.encode`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode"). The sentences are chunked into smaller packages and sent to individual processes, which encode them on different GPUs or CPUs. This method is only suitable for encoding large sets of sentences.

Parameters:
*   **sentences** (_List_ _[_ _str_ _]_) – List of sentences to encode.

*   **pool** (_Dict_ _[_ _Literal_ _[_ _"input"_ _,_ _"output"_ _,_ _"processes"_ _]_ _,_ _Any_ _]_) – A pool of workers started with [`SentenceTransformer.start_multi_process_pool`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.start_multi_process_pool "sentence_transformers.SentenceTransformer.start_multi_process_pool").

*   **prompt_name** (_Optional_ _[_ _str_ _]_ _,_ _optional_) – The name of the prompt to use for encoding. Must be a key in the prompts dictionary, which is either set in the constructor or loaded from the model configuration. For example if `prompt_name` is “query” and the `prompts` is {“query”: “query: “, …}, then the sentence “What is the capital of France?” will be encoded as “query: What is the capital of France?” because the sentence is appended to the prompt. If `prompt` is also set, this argument is ignored. Defaults to None.

*   **prompt** (_Optional_ _[_ _str_ _]_ _,_ _optional_) – The prompt to use for encoding. For example, if the prompt is “query: “, then the sentence “What is the capital of France?” will be encoded as “query: What is the capital of France?” because the sentence is appended to the prompt. If `prompt` is set, `prompt_name` is ignored. Defaults to None.

*   **batch_size** (_int_) – Encode sentences with batch size. (default: 32)

*   **chunk_size** (_int_) – Sentences are chunked and sent to the individual processes. If None, it determines a sensible size. Defaults to None.

*   **show_progress_bar** (_bool_ _,_ _optional_) – Whether to output a progress bar when encode sentences. Defaults to None.

*   **precision** (_Literal_ _[_ _"float32"_ _,_ _"int8"_ _,_ _"uint8"_ _,_ _"binary"_ _,_ _"ubinary"_ _]_) – The precision to use for the embeddings. Can be “float32”, “int8”, “uint8”, “binary”, or “ubinary”. All non-float32 precisions are quantized embeddings. Quantized embeddings are smaller in size and faster to compute, but may have lower accuracy. They are useful for reducing the size of the embeddings of a corpus for semantic search, among other tasks. Defaults to “float32”.

*   **normalize_embeddings** (_bool_) – Whether to normalize returned vectors to have length 1. In that case, the faster dot-product (util.dot_score) instead of cosine similarity can be used. Defaults to False.

*   **truncate_dim** (_int_ _,_ _optional_) –

The dimension to truncate sentence embeddings to. Truncation is especially interesting for [Matryoshka models](https://sbert.net/examples/sentence_transformer/training/matryoshka/README.html), i.e. models that are trained to still produce useful embeddings even if the embedding dimension is reduced. Truncated embeddings require less memory and are faster to perform retrieval with, but note that inference is just as fast, and the embedding performance is worse than the full embeddings. If None, the `truncate_dim` from the model initialization is used. Defaults to None.

Returns:
A 2D numpy array with shape [num_inputs, output_dimension].

Return type:
np.ndarray

Example

from sentence_transformers import SentenceTransformer

def main():
    model = SentenceTransformer("all-mpnet-base-v2")
    sentences = ["The weather is so nice!", "It's so sunny outside.", "He's driving to the movie theater.", "She's going to the cinema."] * 1000

    pool = model.start_multi_process_pool()
    embeddings = model.encode_multi_process(sentences, pool)
    model.stop_multi_process_pool(pool)

    print(embeddings.shape)
    # => (4000, 768)

if  __name__  == "__main__":
    main()

encode_query(_sentences:str|list[str]|ndarray_, _prompt\_name:str|None=None_, _prompt:str|None=None_, _batch\_size:int=32_, _show\_progress\_bar:bool|None=None_, _output\_value:Literal['sentence\_embedding','token\_embeddings']|None='sentence\_embedding'_, _precision:Literal['float32','int8','uint8','binary','ubinary']='float32'_, _convert\_to\_numpy:bool=True_, _convert\_to\_tensor:bool=False_, _device:str|list[str|[device](https://docs.pytorch.org/docs/stable/tensor\_attributes.html#torch.device "(in PyTorch v2.10)")]|None=None_, _normalize\_embeddings:bool=False_, _truncate\_dim:int|None=None_, _pool:dict[Literal['input','output','processes'],Any]|None=None_, _chunk\_size:int|None=None_, _**kwargs_)→list[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")]|ndarray|[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")|dict[str,[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")]|list[dict[str,[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")]][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/SentenceTransformer.py#L446-L573)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode_query "Link to this definition")
Computes sentence embeddings specifically optimized for query representation.

This method is a specialized version of [`encode()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode") that differs in exactly two ways:

1.   If no `prompt_name` or `prompt` is provided, it uses a predefined “query” prompt, if available in the model’s `prompts` dictionary.

2.   It sets the `task` to “query”. If the model has a [`Router`](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Router "sentence_transformers.models.Router") module, it will use the “query” task type to route the input through the appropriate submodules.

Tip

If you are unsure whether you should use [`encode()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode"), [`encode_query()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode_query "sentence_transformers.SentenceTransformer.encode_query"), or [`encode_document()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode_document "sentence_transformers.SentenceTransformer.encode_document"), your best bet is to use [`encode_query()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode_query "sentence_transformers.SentenceTransformer.encode_query") and [`encode_document()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode_document "sentence_transformers.SentenceTransformer.encode_document") for Information Retrieval tasks with clear query and document/passage distinction, and use [`encode()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode") for all other tasks.

Note that [`encode()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode") is the most general method and can be used for any task, including Information Retrieval, and that if the model was not trained with predefined prompts and/or task types, then all three methods will return identical embeddings.

Parameters:
*   **sentences** (_Union_ _[_ _str_ _,_ _List_ _[_ _str_ _]_ _]_) – The sentences to embed.

*   **prompt_name** (_Optional_ _[_ _str_ _]_ _,_ _optional_) – The name of the prompt to use for encoding. Must be a key in the prompts dictionary, which is either set in the constructor or loaded from the model configuration. For example if `prompt_name` is “query” and the `prompts` is {“query”: “query: “, …}, then the sentence “What is the capital of France?” will be encoded as “query: What is the capital of France?” because the sentence is appended to the prompt. If `prompt` is also set, this argument is ignored. Defaults to None.

*   **prompt** (_Optional_ _[_ _str_ _]_ _,_ _optional_) – The prompt to use for encoding. For example, if the prompt is “query: “, then the sentence “What is the capital of France?” will be encoded as “query: What is the capital of France?” because the sentence is appended to the prompt. If `prompt` is set, `prompt_name` is ignored. Defaults to None.

*   **batch_size** (_int_ _,_ _optional_) – The batch size used for the computation. Defaults to 32.

*   **show_progress_bar** (_bool_ _,_ _optional_) – Whether to output a progress bar when encode sentences. Defaults to None.

*   **output_value** (_Optional_ _[_ _Literal_ _[_ _"sentence\_embedding"_ _,_ _"token\_embeddings"_ _]_ _]_ _,_ _optional_) – The type of embeddings to return: “sentence_embedding” to get sentence embeddings, “token_embeddings” to get wordpiece token embeddings, and None, to get all output values. Defaults to “sentence_embedding”.

*   **precision** (_Literal_ _[_ _"float32"_ _,_ _"int8"_ _,_ _"uint8"_ _,_ _"binary"_ _,_ _"ubinary"_ _]_ _,_ _optional_) – The precision to use for the embeddings. Can be “float32”, “int8”, “uint8”, “binary”, or “ubinary”. All non-float32 precisions are quantized embeddings. Quantized embeddings are smaller in size and faster to compute, but may have a lower accuracy. They are useful for reducing the size of the embeddings of a corpus for semantic search, among other tasks. Defaults to “float32”.

*   **convert_to_numpy** (_bool_ _,_ _optional_) – Whether the output should be a list of numpy vectors. If False, it is a list of PyTorch tensors. Defaults to True.

*   **convert_to_tensor** (_bool_ _,_ _optional_) – Whether the output should be one large tensor. Overwrites convert_to_numpy. Defaults to False.

*   **device** (_Union_ _[_ _str_ _,_ _List_ _[_ _str_ _]_ _,_ _None_ _]_ _,_ _optional_) –

Device(s) to use for computation. Can be:

    *   A single device string (e.g., “cuda:0”, “cpu”) for single-process encoding

    *   A list of device strings (e.g., [“cuda:0”, “cuda:1”], [“cpu”, “cpu”, “cpu”, “cpu”]) to distribute encoding across multiple processes

    *   None to auto-detect available device for single-process encoding

If a list is provided, multi-process encoding will be used. Defaults to None.

*   **normalize_embeddings** (_bool_ _,_ _optional_) – Whether to normalize returned vectors to have length 1. In that case, the faster dot-product (util.dot_score) instead of cosine similarity can be used. Defaults to False.

*   **truncate_dim** (_int_ _,_ _optional_) –

The dimension to truncate sentence embeddings to. Truncation is especially interesting for [Matryoshka models](https://sbert.net/examples/sentence_transformer/training/matryoshka/README.html), i.e. models that are trained to still produce useful embeddings even if the embedding dimension is reduced. Truncated embeddings require less memory and are faster to perform retrieval with, but note that inference is just as fast, and the embedding performance is worse than the full embeddings. If None, the `truncate_dim` from the model initialization is used. Defaults to None.

*   **pool** (_Dict_ _[_ _Literal_ _[_ _"input"_ _,_ _"output"_ _,_ _"processes"_ _]_ _,_ _Any_ _]_ _,_ _optional_) – A pool created by start_multi_process_pool() for multi-process encoding. If provided, the encoding will be distributed across multiple processes. This is recommended for large datasets and when multiple GPUs are available. Defaults to None.

*   **chunk_size** (_int_ _,_ _optional_) – Size of chunks for multi-process encoding. Only used with multiprocessing, i.e. when `pool` is not None or `device` is a list. If None, a sensible default is calculated. Defaults to None.

Returns:
By default, a 2d numpy array with shape [num_inputs, output_dimension] is returned. If only one string input is provided, then the output is a 1d array with shape [output_dimension]. If `convert_to_tensor`, a torch Tensor is returned instead. If `self.truncate_dim <= output_dimension` then output_dimension is `self.truncate_dim`.

Return type:
Union[List[Tensor], ndarray, Tensor]

Example

from sentence_transformers import SentenceTransformer

# Load a pre-trained SentenceTransformer model
model = SentenceTransformer("mixedbread-ai/mxbai-embed-large-v1")

# Encode some queries
queries = [
    "What are the effects of climate change?",
    "History of artificial intelligence",
    "Technical specifications product XYZ",
]

# Using query-specific encoding
embeddings = model.encode_query(queries)
print(embeddings.shape)
# (3, 768)

eval()→T[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.eval "Link to this definition")
Sets the module in evaluation mode.

This has any effect only on certain modules. See documentations of particular modules for details of their behaviors in training/evaluation mode, if they are affected, e.g. `Dropout`, `BatchNorm`, etc.

This is equivalent with [`self.train(False)`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.train "(in PyTorch v2.10)").

See [Locally disabling gradient computation](https://docs.pytorch.org/docs/stable/notes/autograd.html#locally-disable-grad-doc "(in PyTorch v2.10)") for a comparison between .eval() and several similar mechanisms that may be confused with it.

Returns:
self

Return type:
[Module](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

evaluate(_evaluator:[SentenceEvaluator](https://sbert.net/docs/package\_reference/sentence\_transformer/evaluation.html#sentence\_transformers.evaluation.SentenceEvaluator "sentence\_transformers.evaluation.SentenceEvaluator.SentenceEvaluator")_, _output\_path:str|None=None_)→dict[str,float]|float[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/SentenceTransformer.py#L2052-L2065)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.evaluate "Link to this definition")
Evaluate the model based on an evaluator

Parameters:
*   **evaluator** ([_SentenceEvaluator_](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.SentenceEvaluator "sentence_transformers.evaluation.SentenceEvaluator")) – The evaluator used to evaluate the model.

*   **output_path** (_str_ _,_ _optional_) – The path where the evaluator can write the results. Defaults to None.

Returns:
The evaluation results.

fit(_train\_objectives:~collections.abc.Iterable[tuple[~torch.utils.data.dataloader.DataLoader,~torch.nn.modules.module.Module]],evaluator:~sentence\_transformers.evaluation.SentenceEvaluator.SentenceEvaluator|None=None,epochs:int=1,steps\_per\_epoch=None,scheduler:str='WarmupLinear',warmup\_steps:int=10000,optimizer\_class:type[~torch.optim.optimizer.Optimizer]=<class'torch.optim.adamw.AdamW'>,optimizer\_params:dict[str,object]={'lr':2e-05},weight\_decay:float=0.01,evaluation\_steps:int=0,output\_path:str|None=None,save\_best\_model:bool=True,max\_grad\_norm:float=1,use\_amp:bool=False,callback:~collections.abc.Callable[[float,int,int],None]|None=None,show\_progress\_bar:bool=True,checkpoint\_path:str|None=None,checkpoint\_save\_steps:int=500,checkpoint\_save\_total\_limit:int=0,resume\_from\_checkpoint:bool=False_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/fit_mixin.py#L165-L408)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.fit "Link to this definition")
Deprecated training method from before Sentence Transformers v3.0, it is recommended to use [`SentenceTransformerTrainer`](https://sbert.net/docs/package_reference/sentence_transformer/trainer.html#sentence_transformers.trainer.SentenceTransformerTrainer "sentence_transformers.trainer.SentenceTransformerTrainer") instead. This method uses [`SentenceTransformerTrainer`](https://sbert.net/docs/package_reference/sentence_transformer/trainer.html#sentence_transformers.trainer.SentenceTransformerTrainer "sentence_transformers.trainer.SentenceTransformerTrainer") behind the scenes, but does not provide as much flexibility as the Trainer itself.

This training approach uses a list of DataLoaders and Loss functions to train the model. Each DataLoader is sampled in turn for one batch. We sample only as many batches from each DataLoader as there are in the smallest one to make sure of equal training with each dataset, i.e. round robin sampling.

This method should produce equivalent results in v3.0+ as before v3.0, but if you encounter any issues with your existing training scripts, then you may wish to use [`SentenceTransformer.old_fit`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.old_fit "sentence_transformers.SentenceTransformer.old_fit") instead. That uses the old training method from before v3.0.

Parameters:
*   **train_objectives** – Tuples of (DataLoader, LossFunction). Pass more than one for multi-task learning

*   **evaluator** – An evaluator (sentence_transformers.evaluation) evaluates the model performance during training on held- out dev data. It is used to determine the best model that is saved to disk.

*   **epochs** – Number of epochs for training

*   **steps_per_epoch** – Number of training steps per epoch. If set to None (default), one epoch is equal the DataLoader size from train_objectives.

*   **scheduler** – Learning rate scheduler. Available schedulers: constantlr, warmupconstant, warmuplinear, warmupcosine, warmupcosinewithhardrestarts

*   **warmup_steps** – Behavior depends on the scheduler. For WarmupLinear (default), the learning rate is increased from o up to the maximal learning rate. After these many training steps, the learning rate is decreased linearly back to zero.

*   **optimizer_class** – Optimizer

*   **optimizer_params** – Optimizer parameters

*   **weight_decay** – Weight decay for model parameters

*   **evaluation_steps** – If > 0, evaluate the model using evaluator after each number of training steps

*   **output_path** – Storage path for the model and evaluation files

*   **save_best_model** – If true, the best model (according to evaluator) is stored at output_path

*   **max_grad_norm** – Used for gradient normalization.

*   **use_amp** – Use Automatic Mixed Precision (AMP). Only for Pytorch >= 1.6.0

*   **callback** – Callback function that is invoked after each evaluation. It must accept the following three parameters in this order: score, epoch, steps

*   **show_progress_bar** – If True, output a tqdm progress bar

*   **checkpoint_path** – Folder to save checkpoints during training

*   **checkpoint_save_steps** – Will save a checkpoint after so many steps

*   **checkpoint_save_total_limit** – Total number of checkpoints to store

*   **resume_from_checkpoint** – If true, searches for checkpoints to continue training from.

float()→T[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.float "Link to this definition")
Casts all floating point parameters and buffers to `float` datatype.

Note

This method modifies the module in-place.

Returns:
self

Return type:
[Module](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

get_adapter_state_dict(_*args_, _**kwargs_)→dict[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/peft_mixin.py#L124-L141)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.get_adapter_state_dict "Link to this definition")
If you are not familiar with adapters and PEFT methods, we invite you to read more about them on the PEFT official documentation: [https://huggingface.co/docs/peft](https://huggingface.co/docs/peft)

Gets the adapter state dict that should only contain the weights tensors of the specified adapter_name adapter. If no adapter_name is passed, the active adapter is used.

Parameters:
*   ***args** – Positional arguments to pass to the underlying AutoModel get_adapter_state_dict function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.get_adapter_state_dict](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.get_adapter_state_dict)

*   ****kwargs** – Keyword arguments to pass to the underlying AutoModel get_adapter_state_dict function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.get_adapter_state_dict](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.get_adapter_state_dict)

get_backend()→Literal['torch','onnx','openvino'][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/SentenceTransformer.py#L408-L414)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.get_backend "Link to this definition")
Return the backend used for inference, which can be one of “torch”, “onnx”, or “openvino”.

Returns:
The backend used for inference.

Return type:
str

get_max_seq_length()→int|None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/SentenceTransformer.py#L1597-L1607)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.get_max_seq_length "Link to this definition")
Returns the maximal sequence length that the model accepts. Longer inputs will be truncated.

Returns:
The maximal sequence length that the model accepts, or None if it is not defined.

Return type:
Optional[int]

get_model_kwargs()→list[str][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/SentenceTransformer.py#L416-L444)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.get_model_kwargs "Link to this definition")
Get the keyword arguments specific to this model for the encode, encode_query, or encode_document methods.

Example

>>> from sentence_transformers import SentenceTransformer, SparseEncoder
>>> SentenceTransformer("all-MiniLM-L6-v2").get_model_kwargs()
[]
>>> SentenceTransformer("jinaai/jina-embeddings-v4", trust_remote_code=True).get_model_kwargs()
['task', 'truncate_dim']
>>> SparseEncoder("opensearch-project/opensearch-neural-sparse-encoding-doc-v3-distill").get_model_kwargs()
['task']

Returns:
A list of keyword arguments for the forward pass.

Return type:
list[str]

get_sentence_embedding_dimension()→int|None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/SentenceTransformer.py#L1628-L1645)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.get_sentence_embedding_dimension "Link to this definition")
Returns the number of dimensions in the output of [`SentenceTransformer.encode`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode").

Returns:
The number of dimensions in the output of encode. If it’s not known, it’s None.

Return type:
Optional[int]

half()→T[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.half "Link to this definition")
Casts all floating point parameters and buffers to `half` datatype.

Note

This method modifies the module in-place.

Returns:
self

Return type:
[Module](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

load_adapter(_*args_, _**kwargs_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/peft_mixin.py#L40-L56)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.load_adapter "Link to this definition")
Load adapter weights from file or remote Hub folder.” If you are not familiar with adapters and PEFT methods, we invite you to read more about them on PEFT official documentation: [https://huggingface.co/docs/peft](https://huggingface.co/docs/peft)

Requires peft as a backend to load the adapter weights and the underlying model to be compatible with PEFT.

Parameters:
*   ***args** – Positional arguments to pass to the underlying AutoModel load_adapter function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.load_adapter](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.load_adapter)

*   ****kwargs** – Keyword arguments to pass to the underlying AutoModel load_adapter function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.load_adapter](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.load_adapter)

_property_ max_seq_length _:int_[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.max_seq_length "Link to this definition")
Returns the maximal input sequence length for the model. Longer inputs will be truncated.

Returns:
The maximal input sequence length.

Return type:
int

Example

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-mpnet-base-v2")
print(model.max_seq_length)
# => 384

model_card_data_class[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/model_card.py#L265-L1196)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.model_card_data_class "Link to this definition")
alias of [`SentenceTransformerModelCardData`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.model_card.SentenceTransformerModelCardData "sentence_transformers.model_card.SentenceTransformerModelCardData")

old_fit(_train\_objectives:~collections.abc.Iterable[tuple[~torch.utils.data.dataloader.DataLoader,~torch.nn.modules.module.Module]],evaluator:~sentence\_transformers.evaluation.SentenceEvaluator.SentenceEvaluator|None=None,epochs:int=1,steps\_per\_epoch=None,scheduler:str='WarmupLinear',warmup\_steps:int=10000,optimizer\_class:type[~torch.optim.optimizer.Optimizer]=<class'torch.optim.adamw.AdamW'>,optimizer\_params:dict[str,object]={'lr':2e-05},weight\_decay:float=0.01,evaluation\_steps:int=0,output\_path:str|None=None,save\_best\_model:bool=True,max\_grad\_norm:float=1,use\_amp:bool=False,callback:~collections.abc.Callable[[float,int,int],None]|None=None,show\_progress\_bar:bool=True,checkpoint\_path:str|None=None,checkpoint\_save\_steps:int=500,checkpoint\_save\_total\_limit:int=0_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/fit_mixin.py#L469-L696)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.old_fit "Link to this definition")
Deprecated training method from before Sentence Transformers v3.0, it is recommended to use [`sentence_transformers.trainer.SentenceTransformerTrainer`](https://sbert.net/docs/package_reference/sentence_transformer/trainer.html#sentence_transformers.trainer.SentenceTransformerTrainer "sentence_transformers.trainer.SentenceTransformerTrainer") instead. This method should only be used if you encounter issues with your existing training scripts after upgrading to v3.0+.

This training approach uses a list of DataLoaders and Loss functions to train the model. Each DataLoader is sampled in turn for one batch. We sample only as many batches from each DataLoader as there are in the smallest one to make sure of equal training with each dataset, i.e. round robin sampling.

Parameters:
*   **train_objectives** – Tuples of (DataLoader, LossFunction). Pass more than one for multi-task learning

*   **evaluator** – An evaluator (sentence_transformers.evaluation) evaluates the model performance during training on held- out dev data. It is used to determine the best model that is saved to disk.

*   **epochs** – Number of epochs for training

*   **steps_per_epoch** – Number of training steps per epoch. If set to None (default), one epoch is equal the DataLoader size from train_objectives.

*   **scheduler** – Learning rate scheduler. Available schedulers: constantlr, warmupconstant, warmuplinear, warmupcosine, warmupcosinewithhardrestarts

*   **warmup_steps** – Behavior depends on the scheduler. For WarmupLinear (default), the learning rate is increased from o up to the maximal learning rate. After these many training steps, the learning rate is decreased linearly back to zero.

*   **optimizer_class** – Optimizer

*   **optimizer_params** – Optimizer parameters

*   **weight_decay** – Weight decay for model parameters

*   **evaluation_steps** – If > 0, evaluate the model using evaluator after each number of training steps

*   **output_path** – Storage path for the model and evaluation files

*   **save_best_model** – If true, the best model (according to evaluator) is stored at output_path

*   **max_grad_norm** – Used for gradient normalization.

*   **use_amp** – Use Automatic Mixed Precision (AMP). Only for Pytorch >= 1.6.0

*   **callback** – Callback function that is invoked after each evaluation. It must accept the following three parameters in this order: score, epoch, steps

*   **show_progress_bar** – If True, output a tqdm progress bar

*   **checkpoint_path** – Folder to save checkpoints during training

*   **checkpoint_save_steps** – Will save a checkpoint after so many steps

*   **checkpoint_save_total_limit** – Total number of checkpoints to store

push_to_hub(_repo\_id:str_, _token:str|None=None_, _private:bool|None=None_, _safe\_serialization:bool=True_, _commit\_message:str|None=None_, _local\_model\_path:str|None=None_, _exist\_ok:bool=False_, _replace\_model\_card:bool=False_, _train\_datasets:list[str]|None=None_, _revision:str|None=None_, _create\_pr:bool=False_)→str[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/SentenceTransformer.py#L1918-L2034)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.push_to_hub "Link to this definition")
Uploads all elements of this Sentence Transformer to a new HuggingFace Hub repository.

Parameters:
*   **repo_id** (_str_) – Repository name for your model in the Hub, including the user or organization.

*   **token** (_str_ _,_ _optional_) – An authentication token (See [https://huggingface.co/settings/token](https://huggingface.co/settings/token))

*   **private** (_bool_ _,_ _optional_) – Set to true, for hosting a private model

*   **safe_serialization** (_bool_ _,_ _optional_) – If true, save the model using safetensors. If false, save the model the traditional PyTorch way

*   **commit_message** (_str_ _,_ _optional_) – Message to commit while pushing.

*   **local_model_path** (_str_ _,_ _optional_) – Path of the model locally. If set, this file path will be uploaded. Otherwise, the current model will be uploaded

*   **exist_ok** (_bool_ _,_ _optional_) – If true, saving to an existing repository is OK. If false, saving only to a new repository is possible

*   **replace_model_card** (_bool_ _,_ _optional_) – If true, replace an existing model card in the hub with the automatically created model card

*   **train_datasets** (_List_ _[_ _str_ _]_ _,_ _optional_) – Datasets used to train the model. If set, the datasets will be added to the model card in the Hub.

*   **revision** (_str_ _,_ _optional_) – Branch to push the uploaded files to

*   **create_pr** (_bool_ _,_ _optional_) – If True, create a pull request instead of pushing directly to the main branch

Returns:
The url of the commit of your model in the repository on the Hugging Face Hub.

Return type:
str

save_pretrained(_path:str_, _model\_name:str|None=None_, _create\_model\_card:bool=True_, _train\_datasets:list[str]|None=None_, _safe\_serialization:bool=True_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/SentenceTransformer.py#L1778-L1804)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.save_pretrained "Link to this definition")
Saves a model and its configuration files to a directory, so that it can be loaded with `SentenceTransformer(path)` again.

Parameters:
*   **path** (_str_) – Path on disk where the model will be saved.

*   **model_name** (_str_ _,_ _optional_) – Optional model name.

*   **create_model_card** (_bool_ _,_ _optional_) – If True, create a README.md with basic information about this model.

*   **train_datasets** (_List_ _[_ _str_ _]_ _,_ _optional_) – Optional list with the names of the datasets used to train the model.

*   **safe_serialization** (_bool_ _,_ _optional_) – If True, save the model using safetensors. If False, save the model the traditional (but unsafe) PyTorch way.

set_adapter(_*args_, _**kwargs_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/peft_mixin.py#L78-L91)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.set_adapter "Link to this definition")
Sets a specific adapter by forcing the model to use a that adapter and disable the other adapters.

Parameters:
*   ***args** – Positional arguments to pass to the underlying AutoModel set_adapter function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.set_adapter](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.set_adapter)

*   ****kwargs** – Keyword arguments to pass to the underlying AutoModel set_adapter function. More information can be found in the transformers documentation [https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.set_adapter](https://huggingface.co/docs/transformers/main/en/main_classes/peft#transformers.integrations.PeftAdapterMixin.set_adapter)

set_pooling_include_prompt(_include\_prompt:bool_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/SentenceTransformer.py#L1558-L1574)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.set_pooling_include_prompt "Link to this definition")
Sets the include_prompt attribute in the pooling layer in the model, if there is one.

This is useful for INSTRUCTOR models, as the prompt should be excluded from the pooling strategy for these models.

Parameters:
**include_prompt** (_bool_) – Whether to include the prompt in the pooling layer.

Returns:
None

_property_ similarity _:Callable[[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")|ndarray[Any,dtype[float32]],[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")|ndarray[Any,dtype[float32]]],[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")]_[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.similarity "Link to this definition")
Compute the similarity between two collections of embeddings. The output will be a matrix with the similarity scores between all embeddings from the first parameter and all embeddings from the second parameter. This differs from similarity_pairwise which computes the similarity between each pair of embeddings. This method supports only embeddings with fp32 precision and does not accommodate quantized embeddings.

Parameters:
*   **embeddings1** (_Union_ _[_ _Tensor_ _,_ _ndarray_ _]_) – [num_embeddings_1, embedding_dim] or [embedding_dim]-shaped numpy array or torch tensor.

*   **embeddings2** (_Union_ _[_ _Tensor_ _,_ _ndarray_ _]_) – [num_embeddings_2, embedding_dim] or [embedding_dim]-shaped numpy array or torch tensor.

Returns:
A [num_embeddings_1, num_embeddings_2]-shaped torch tensor with similarity scores.

Return type:
Tensor

Example

>>> model = SentenceTransformer("all-mpnet-base-v2")
>>> sentences = [
...     "The weather is so nice!",
...     "It's so sunny outside.",
...     "He's driving to the movie theater.",
...     "She's going to the cinema.",
... ]
>>> embeddings = model.encode(sentences, normalize_embeddings=True)
>>> model.similarity(embeddings, embeddings)
tensor([[1.0000, 0.7235, 0.0290, 0.1309],
 [0.7235, 1.0000, 0.0613, 0.1129],
 [0.0290, 0.0613, 1.0000, 0.5027],
 [0.1309, 0.1129, 0.5027, 1.0000]])
>>> model.similarity_fn_name
"cosine"
>>> model.similarity_fn_name = "euclidean"
>>> model.similarity(embeddings, embeddings)
tensor([[-0.0000, -0.7437, -1.3935, -1.3184],
 [-0.7437, -0.0000, -1.3702, -1.3320],
 [-1.3935, -1.3702, -0.0000, -0.9973],
 [-1.3184, -1.3320, -0.9973, -0.0000]])

_property_ similarity_fn_name _:Literal['cosine','dot','euclidean','manhattan']_[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.similarity_fn_name "Link to this definition")
Return the name of the similarity function used by [`SentenceTransformer.similarity()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.similarity "sentence_transformers.SentenceTransformer.similarity") and [`SentenceTransformer.similarity_pairwise()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.similarity_pairwise "sentence_transformers.SentenceTransformer.similarity_pairwise").

Returns:The name of the similarity function. Can be None if not set, in which case it will
default to “cosine” when first called.

Return type:
Optional[str]

Example

>>> model = SentenceTransformer("multi-qa-mpnet-base-dot-v1")
>>> model.similarity_fn_name
'dot'

_property_ similarity_pairwise _:Callable[[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")|ndarray[Any,dtype[float32]],[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")|ndarray[Any,dtype[float32]]],[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")]_[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.similarity_pairwise "Link to this definition")
Compute the similarity between two collections of embeddings. The output will be a vector with the similarity scores between each pair of embeddings. This method supports only embeddings with fp32 precision and does not accommodate quantized embeddings.

Parameters:
*   **embeddings1** (_Union_ _[_ _Tensor_ _,_ _ndarray_ _]_) – [num_embeddings, embedding_dim] or [embedding_dim]-shaped numpy array or torch tensor.

*   **embeddings2** (_Union_ _[_ _Tensor_ _,_ _ndarray_ _]_) – [num_embeddings, embedding_dim] or [embedding_dim]-shaped numpy array or torch tensor.

Returns:
A [num_embeddings]-shaped torch tensor with pairwise similarity scores.

Return type:
Tensor

Example

>>> model = SentenceTransformer("all-mpnet-base-v2")
>>> sentences = [
...     "The weather is so nice!",
...     "It's so sunny outside.",
...     "He's driving to the movie theater.",
...     "She's going to the cinema.",
... ]
>>> embeddings = model.encode(sentences, normalize_embeddings=True)
>>> model.similarity_pairwise(embeddings[::2], embeddings[1::2])
tensor([0.7235, 0.5027])
>>> model.similarity_fn_name
"cosine"
>>> model.similarity_fn_name = "euclidean"
>>> model.similarity_pairwise(embeddings[::2], embeddings[1::2])
tensor([-0.7437, -0.9973])

smart_batching_collate(_batch:list[InputExample]_)→tuple[list[dict[str,Tensor]],Tensor][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/fit_mixin.py#L441-L463)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.smart_batching_collate "Link to this definition")
Transforms a batch from a SmartBatchingDataset to a batch of tensors for the model Here, batch is a list of InputExample instances: [InputExample(…), …]

Parameters:
**batch** – a batch from a SmartBatchingDataset

Returns:
a batch of tensors for the model

start_multi_process_pool(_target\_devices:list[str]|None=None_)→dict[Literal['input','output','processes'],Any][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/SentenceTransformer.py#L1304-L1351)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.start_multi_process_pool "Link to this definition")
Starts a multi-process pool to process the encoding with several independent processes via [`SentenceTransformer.encode_multi_process`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode_multi_process "sentence_transformers.SentenceTransformer.encode_multi_process").

This method is recommended if you want to encode on multiple GPUs or CPUs. It is advised to start only one process per GPU. This method works together with encode_multi_process and stop_multi_process_pool.

Parameters:
**target_devices** (_List_ _[_ _str_ _]_ _,_ _optional_) – PyTorch target devices, e.g. [“cuda:0”, “cuda:1”, …], [“npu:0”, “npu:1”, …], or [“cpu”, “cpu”, “cpu”, “cpu”]. If target_devices is None and CUDA/NPU is available, then all available CUDA/NPU devices will be used. If target_devices is None and CUDA/NPU is not available, then 4 CPU devices will be used.

Returns:
A dictionary with the target processes, an input queue, and an output queue.

Return type:
Dict[str, Any]

_static_ stop_multi_process_pool(_pool:dict[Literal['input','output','processes'],Any]_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/SentenceTransformer.py#L1353-L1372)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.stop_multi_process_pool "Link to this definition")
Stops all processes started with start_multi_process_pool.

Parameters:
**pool** (_Dict_ _[_ _str_ _,_ _object_ _]_) – A dictionary containing the input queue, output queue, and process list.

Returns:
None

to(_*args_, _**kwargs_)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.to "Link to this definition")
Moves and/or casts the parameters and buffers.

This can be called as

to(_device=None_, _dtype=None_, _non\_blocking=False_)to(_dtype_, _non\_blocking=False_)to(_tensor_, _non\_blocking=False_)to(_memory\_format=torch.channels\_last_)
Its signature is similar to [`torch.Tensor.to()`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.to.html#torch.Tensor.to "(in PyTorch v2.10)"), but only accepts floating point or complex `dtype`s. In addition, this method will only cast the floating point or complex parameters and buffers to `dtype` (if given). The integral parameters and buffers will be moved [`device`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.device "sentence_transformers.SentenceTransformer.device"), if that is given, but with dtypes unchanged. When `non_blocking` is set, it tries to convert/move asynchronously with respect to the host if possible, e.g., moving CPU Tensors with pinned memory to CUDA devices.

See below for examples.

Note

This method modifies the module in-place.

Parameters:
*   **device** ([`torch.device`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.device "(in PyTorch v2.10)")) – the desired device of the parameters and buffers in this module

*   **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.dtype "(in PyTorch v2.10)")) – the desired floating point or complex dtype of the parameters and buffers in this module

*   **tensor** ([_torch.Tensor_](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")) – Tensor whose dtype and device are the desired dtype and device for all parameters and buffers in this module

*   **memory_format** ([`torch.memory_format`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.memory_format "(in PyTorch v2.10)")) – the desired memory format for 4D parameters and buffers in this module (keyword only argument)

Returns:
self

Return type:
[Module](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

Examples:

>>> # xdoctest: +IGNORE_WANT("non-deterministic")
>>> linear = nn.Linear(2, 2)
>>> linear.weight
Parameter containing:
tensor([[ 0.1913, -0.3420],
 [-0.5113, -0.2325]])
>>> linear.to(torch.double)
Linear(in_features=2, out_features=2, bias=True)
>>> linear.weight
Parameter containing:
tensor([[ 0.1913, -0.3420],
 [-0.5113, -0.2325]], dtype=torch.float64)
>>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_CUDA1)
>>> gpu1 = torch.device("cuda:1")
>>> linear.to(gpu1, dtype=torch.half, non_blocking=True)
Linear(in_features=2, out_features=2, bias=True)
>>> linear.weight
Parameter containing:
tensor([[ 0.1914, -0.3420],
 [-0.5112, -0.2324]], dtype=torch.float16, device='cuda:1')
>>> cpu = torch.device("cpu")
>>> linear.to(cpu)
Linear(in_features=2, out_features=2, bias=True)
>>> linear.weight
Parameter containing:
tensor([[ 0.1914, -0.3420],
 [-0.5112, -0.2324]], dtype=torch.float16)

>>> linear = nn.Linear(2, 2, bias=None).to(torch.cdouble)
>>> linear.weight
Parameter containing:
tensor([[ 0.3741+0.j, 0.2382+0.j],
 [ 0.5593+0.j, -0.4443+0.j]], dtype=torch.complex128)
>>> linear(torch.ones(3, 2, dtype=torch.cdouble))
tensor([[0.6122+0.j, 0.1150+0.j],
 [0.6122+0.j, 0.1150+0.j],
 [0.6122+0.j, 0.1150+0.j]], dtype=torch.complex128)

tokenize(_texts:list[str]|list[dict]|list[tuple[str,str]]_, _**kwargs_)→dict[str,[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/SentenceTransformer.py#L1609-L1623)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.tokenize "Link to this definition")
Tokenizes the texts.

Parameters:
**texts** (_Union_ _[_ _List_ _[_ _str_ _]_ _,_ _List_ _[_ _Dict_ _]_ _,_ _List_ _[_ _Tuple_ _[_ _str_ _,_ _str_ _]_ _]_ _]_) – A list of texts to be tokenized.

Returns:A dictionary of tensors with the tokenized texts. Common keys are “input_ids”,
”attention_mask”, and “token_type_ids”.

Return type:
Dict[str, Tensor]

_property_ tokenizer _:Any_[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.tokenizer "Link to this definition")
Property to get the tokenizer that is used by this model

train(_mode:bool=True_)→T[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.train "Link to this definition")
Sets the module in training mode.

This has any effect only on certain modules. See documentations of particular modules for details of their behaviors in training/evaluation mode, if they are affected, e.g. `Dropout`, `BatchNorm`, etc.

Parameters:
**mode** (_bool_) – whether to set training mode (`True`) or evaluation mode (`False`). Default: `True`.

Returns:
self

Return type:
[Module](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

_property_ transformers_model _:PreTrainedModel|None_[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.transformers_model "Link to this definition")
Property to get the underlying transformers PreTrainedModel instance, if it exists. Note that it’s possible for a model to have multiple underlying transformers models, but this property will return the first one it finds in the module hierarchy.

Returns:
The underlying transformers model or None if not found.

Return type:
PreTrainedModel or None

Example

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-mpnet-base-v2")

# You can now access the underlying transformers model
transformers_model = model.transformers_model
print(type(transformers_model))
# => <class 'transformers.models.mpnet.modeling_mpnet.MPNetModel'>

truncate_sentence_embeddings(_truncate\_dim:int|None_)→Iterator[None][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/SentenceTransformer.py#L1647-L1675)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.truncate_sentence_embeddings "Link to this definition")
In this context, [`SentenceTransformer.encode`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode") outputs sentence embeddings truncated at dimension `truncate_dim`.

This may be useful when you are using the same model for different applications where different dimensions are needed.

Parameters:
**truncate_dim** (_int_ _,_ _optional_) – The dimension to truncate sentence embeddings to. `None` does no truncation.

Example

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-mpnet-base-v2")

with model.truncate_sentence_embeddings(truncate_dim=16):
    embeddings_truncated = model.encode(["hello there", "hiya"])
assert embeddings_truncated.shape[-1] == 16

SentenceTransformerModelCardData[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentencetransformermodelcarddata "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.model_card.SentenceTransformerModelCardData(_language:str|list[str]|None=<factory>_, _license:str|None=None_, _model\_name:str|None=None_, _model\_id:str|None=None_, _train\_datasets:list[dict[str_, _str]]=<factory>_, _eval\_datasets:list[dict[str_, _str]]=<factory>_, _task\_name:str='semantic textual similarity_, _semantic search_, _paraphrase mining_, _text classification_, _clustering_, _and more'_, _tags:list[str]|None=<factory>_, _local\_files\_only:bool=False_, _generate\_widget\_examples:bool=True_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/model_card.py#L265-L1196)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.model_card.SentenceTransformerModelCardData "Link to this definition")
A dataclass storing data used in the model card.

Parameters:
*   **language** (Optional[Union[str, List[str]]]) – The model language, either a string or a list, e.g. “en” or [“en”, “de”, “nl”]

*   **license** (Optional[str]) – The license of the model, e.g. “apache-2.0”, “mit”, or “cc-by-nc-sa-4.0”

*   **model_name** (Optional[str]) – The pretty name of the model, e.g. “SentenceTransformer based on microsoft/mpnet-base”.

*   **model_id** (Optional[str]) – The model ID when pushing the model to the Hub, e.g. “tomaarsen/sbert-mpnet-base-allnli”.

*   **train_datasets** (List[Dict[str, str]]) – A list of the names and/or Hugging Face dataset IDs of the training datasets. e.g. [{“name”: “SNLI”, “id”: “stanfordnlp/snli”}, {“name”: “MultiNLI”, “id”: “nyu-mll/multi_nli”}, {“name”: “STSB”}]

*   **eval_datasets** (List[Dict[str, str]]) – A list of the names and/or Hugging Face dataset IDs of the evaluation datasets. e.g. [{“name”: “SNLI”, “id”: “stanfordnlp/snli”}, {“id”: “mteb/stsbenchmark-sts”}]

*   **task_name** (str) – The human-readable task the model is trained on, e.g. “semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more”.

*   **tags** (Optional[List[str]]) – A list of tags for the model, e.g. [“sentence-transformers”, “sentence-similarity”, “feature-extraction”].

*   **local_files_only** (bool) – If True, don’t attempt to find dataset or base model information on the Hub. Defaults to False.

*   **generate_widget_examples** (bool) – If True, generate widget examples from the evaluation or training dataset, and compute their similarities. Defaults to True.

Tip

Install [codecarbon](https://github.com/mlco2/codecarbon) to automatically track carbon emission usage and include it in your model cards.

Example:

>>> model = SentenceTransformer(
...     "microsoft/mpnet-base",
...     model_card_data=SentenceTransformerModelCardData(
...         model_id="tomaarsen/sbert-mpnet-base-allnli",
...         train_datasets=[{"name": "SNLI", "id": "stanfordnlp/snli"}, {"name": "MultiNLI", "id": "nyu-mll/multi_nli"}],
...         eval_datasets=[{"name": "SNLI", "id": "stanfordnlp/snli"}, {"name": "MultiNLI", "id": "nyu-mll/multi_nli"}],
...         license="apache-2.0",
...         language="en",
...     ),
... )

SimilarityFunction[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#similarityfunction "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.SimilarityFunction(_value_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/similarity_functions.py#L21-L129)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SimilarityFunction "Link to this definition")
Enum class for supported similarity functions. The following functions are supported:

*   `SimilarityFunction.COSINE` (`"cosine"`): Cosine similarity

*   `SimilarityFunction.DOT_PRODUCT` (`"dot"`, `dot_product`): Dot product similarity

*   `SimilarityFunction.EUCLIDEAN` (`"euclidean"`): Euclidean distance

*   `SimilarityFunction.MANHATTAN` (`"manhattan"`): Manhattan distance

_static_ possible_values()→list[str][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/similarity_functions.py#L116-L129)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SimilarityFunction.possible_values "Link to this definition")
Returns a list of possible values for the SimilarityFunction enum.

Returns:
A list of possible values for the SimilarityFunction enum.

Return type:
list

Example

>>> possible_values = SimilarityFunction.possible_values()
>>> possible_values
['cosine', 'dot', 'euclidean', 'manhattan']

_static_ to_similarity_fn(_similarity\_function:str|[SimilarityFunction](https://sbert.net/docs/package\_reference/sparse\_encoder/SparseEncoder.html#sentence\_transformers.SimilarityFunction "sentence\_transformers.similarity\_functions.SimilarityFunction")_)→Callable[[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")|ndarray,[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")|ndarray],[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/similarity_functions.py#L37-L73)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SimilarityFunction.to_similarity_fn "Link to this definition")
Converts a similarity function name or enum value to the corresponding similarity function.

Parameters:
**similarity_function** (_Union_ _[_ _str_ _,_[_SimilarityFunction_](https://sbert.net/docs/package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")_]_) – The name or enum value of the similarity function.

Returns:
The corresponding similarity function.

Return type:
Callable[[Union[Tensor, ndarray], Union[Tensor, ndarray]], Tensor]

Raises:
**ValueError** – If the provided function is not supported.

Example

>>> similarity_fn = SimilarityFunction.to_similarity_fn("cosine")
>>> similarity_scores = similarity_fn(embeddings1, embeddings2)
>>> similarity_scores
tensor([[0.3952, 0.0554],
 [0.0992, 0.1570]])

_static_ to_similarity_pairwise_fn(_similarity\_function:str|[SimilarityFunction](https://sbert.net/docs/package\_reference/sparse\_encoder/SparseEncoder.html#sentence\_transformers.SimilarityFunction "sentence\_transformers.similarity\_functions.SimilarityFunction")_)→Callable[[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")|ndarray,[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")|ndarray],[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/similarity_functions.py#L75-L114)[](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SimilarityFunction.to_similarity_pairwise_fn "Link to this definition")
Converts a similarity function into a pairwise similarity function.

The pairwise similarity function returns the diagonal vector from the similarity matrix, i.e. it only computes the similarity(a[i], b[i]) for each i in the range of the input tensors, rather than computing the similarity between all pairs of a and b.

Parameters:
**similarity_function** (_Union_ _[_ _str_ _,_[_SimilarityFunction_](https://sbert.net/docs/package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")_]_) – The name or enum value of the similarity function.

Returns:
The pairwise similarity function.

Return type:
Callable[[Union[Tensor, ndarray], Union[Tensor, ndarray]], Tensor]

Raises:
**ValueError** – If the provided similarity function is not supported.

Example

>>> pairwise_fn = SimilarityFunction.to_similarity_pairwise_fn("cosine")
>>> similarity_scores = pairwise_fn(embeddings1, embeddings2)
>>> similarity_scores
tensor([0.3952, 0.1570])

[Previous](https://sbert.net/docs/package_reference/sentence_transformer/index.html "Sentence Transformer")[Next](https://sbert.net/docs/package_reference/sentence_transformer/trainer.html "Trainer")

* * *

© Copyright 2026.

 Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org/).
