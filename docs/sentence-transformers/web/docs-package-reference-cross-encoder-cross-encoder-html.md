# Source: https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html

Title: CrossEncoder — Sentence Transformers documentation

URL Source: https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html

Published Time: Tue, 17 Feb 2026 14:05:52 GMT

Markdown Content:
CrossEncoder — Sentence Transformers documentation
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
    *   [CrossEncoder](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#)
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
*   [Cross Encoder](https://sbert.net/docs/package_reference/cross_encoder/index.html)
*   CrossEncoder
*   [Edit on GitHub](https://github.com/huggingface/sentence-transformers/blob/main/docs/package_reference/cross_encoder/cross_encoder.md)

* * *

CrossEncoder[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#crossencoder "Link to this heading")
==============================================================================================================================

CrossEncoder[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#id1 "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

For an introduction to Cross-Encoders, see [Cross-Encoders](https://sbert.net/docs/cross_encoder/usage/usage.html).

_class_ sentence_transformers.cross_encoder.CrossEncoder(_model\_name\_or\_path:str_, _num\_labels:int|None=None_, _max\_length:int|None=None_, _activation\_fn:Callable|None=None_, _device:str|None=None_, _cache\_folder:str|None=None_, _trust\_remote\_code:bool=False_, _revision:str|None=None_, _local\_files\_only:bool=False_, _token:bool|str|None=None_, _model\_kwargs:dict|None=None_, _tokenizer\_kwargs:dict|None=None_, _config\_kwargs:dict|None=None_, _model\_card\_data:[CrossEncoderModelCardData](https://sbert.net/docs/package\_reference/cross\_encoder/cross\_encoder.html#sentence\_transformers.cross\_encoder.model\_card.CrossEncoderModelCardData "sentence\_transformers.cross\_encoder.model\_card.CrossEncoderModelCardData")|None=None_, _backend:Literal['torch','onnx','openvino']='torch'_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/cross_encoder/CrossEncoder.py#L54-L1028)[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "Link to this definition")
A CrossEncoder takes exactly two sentences / texts as input and either predicts a score or label for this sentence pair. It can for example predict the similarity of the sentence pair on a scale of 0 … 1.

It does not yield a sentence embedding and does not work for individual sentences.

Parameters:
*   **model_name_or_path** (_str_) – A model name from Hugging Face Hub that can be loaded with AutoModel, or a path to a local model. We provide several pre-trained CrossEncoder models that can be used for common tasks.

*   **num_labels** (_int_ _,_ _optional_) – Number of labels of the classifier. If 1, the CrossEncoder is a regression model that outputs a continuous score 0…1. If > 1, it output several scores that can be soft-maxed to get probability scores for the different classes. Defaults to None.

*   **max_length** (_int_ _,_ _optional_) – Max length for input sequences. Longer sequences will be truncated. If None, max length of the model will be used. Defaults to None.

*   **activation_fn** (_Callable_ _,_ _optional_) – Callable (like nn.Sigmoid) about the default activation function that should be used on-top of model.predict(). If None. nn.Sigmoid() will be used if num_labels=1, else nn.Identity(). Defaults to None.

*   **device** (_str_ _,_ _optional_) – Device (like “cuda”, “cpu”, “mps”, “npu”) that should be used for computation. If None, checks if a GPU can be used.

*   **cache_folder** (str, Path, optional) – Path to the folder where cached files are stored.

*   **trust_remote_code** (_bool_ _,_ _optional_) – Whether or not to allow for custom models defined on the Hub in their own modeling files. This option should only be set to True for repositories you trust and in which you have read the code, as it will execute code present on the Hub on your local machine. Defaults to False.

*   **revision** (_str_ _,_ _optional_) – The specific model version to use. It can be a branch name, a tag name, or a commit id, for a stored model on Hugging Face. Defaults to None.

*   **local_files_only** (_bool_ _,_ _optional_) – Whether or not to only look at local files (i.e., do not try to download the model).

*   **token** (_bool_ _or_ _str_ _,_ _optional_) – Hugging Face authentication token to download private models.

*   **model_kwargs** (_Dict_ _[_ _str_ _,_ _Any_ _]_ _,_ _optional_) –

Additional model configuration parameters to be passed to the Hugging Face Transformers model. Particularly useful options are:

    *   `torch_dtype`: Override the default torch.dtype and load the model under a specific dtype. The different options are:

> 1. `torch.float16`, `torch.bfloat16` or `torch.float`: load in a specified `dtype`, ignoring the model’s `config.torch_dtype` if one exists. If not specified - the model will get loaded in `torch.float` (fp32).
> 
> 
> 2. `"auto"` - A `torch_dtype` entry in the `config.json` file of the model will be attempted to be used. If this entry isn’t found then next check the `dtype` of the first weight in the checkpoint that’s of a floating point type and use that as `dtype`. This will load the model using the `dtype` it was saved in at the end of the training. It can’t be used as an indicator of how the model was trained. Since it could be trained in one of half precision dtypes, but saved in fp32.

    *   `attn_implementation`: The attention implementation to use in the model (if relevant). Can be any of “eager” (manual implementation of the attention), “sdpa” (using [F.scaled_dot_product_attention](https://pytorch.org/docs/master/generated/torch.nn.functional.scaled_dot_product_attention.html)), or “flash_attention_2” (using [Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention)). By default, if available, SDPA will be used for torch>=2.1.1. The default is otherwise the manual “eager” implementation.

See the [AutoModelForSequenceClassification.from_pretrained](https://huggingface.co/docs/transformers/en/model_doc/auto#transformers.AutoModelForSequenceClassification.from_pretrained) documentation for more details.

*   **tokenizer_kwargs** (_Dict_ _[_ _str_ _,_ _Any_ _]_ _,_ _optional_) – Additional tokenizer configuration parameters to be passed to the Hugging Face Transformers tokenizer. See the [AutoTokenizer.from_pretrained](https://huggingface.co/docs/transformers/en/model_doc/auto#transformers.AutoTokenizer.from_pretrained) documentation for more details.

*   **config_kwargs** (_Dict_ _[_ _str_ _,_ _Any_ _]_ _,_ _optional_) – Additional model configuration parameters to be passed to the Hugging Face Transformers config. See the [AutoConfig.from_pretrained](https://huggingface.co/docs/transformers/en/model_doc/auto#transformers.AutoConfig.from_pretrained) documentation for more details. For example, you can set `classifier_dropout` via this parameter.

*   **model_card_data** ([`SentenceTransformerModelCardData`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.model_card.SentenceTransformerModelCardData "sentence_transformers.model_card.SentenceTransformerModelCardData"), optional) – A model card data object that contains information about the model. This is used to generate a model card when saving the model. If not set, a default model card data object is created.

*   **backend** (_str_) – The backend to use for inference. Can be one of “torch” (default), “onnx”, or “openvino”. See [https://sbert.net/docs/cross_encoder/usage/efficiency.html](https://sbert.net/docs/cross_encoder/usage/efficiency.html) for benchmarking information on the different backends.

Initializes internal Module state, shared by both nn.Module and ScriptModule.

bfloat16()→T[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.bfloat16 "Link to this definition")
Casts all floating point parameters and buffers to `bfloat16` datatype.

Note

This method modifies the module in-place.

Returns:
self

Return type:
[Module](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

compile(_*args_, _**kwargs_)[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.compile "Link to this definition")
Compile this Module’s forward using [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "(in PyTorch v2.10)").

This Module’s  __call__  method is compiled and all arguments are passed as-is to [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "(in PyTorch v2.10)").

See [`torch.compile()`](https://docs.pytorch.org/docs/stable/generated/torch.compile.html#torch.compile "(in PyTorch v2.10)") for details on the arguments for this function.

cpu()→T[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.cpu "Link to this definition")
Moves all model parameters and buffers to the CPU.

Note

This method modifies the module in-place.

Returns:
self

Return type:
[Module](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

cuda(_device:int|[device](https://docs.pytorch.org/docs/stable/tensor\_attributes.html#torch.device "(in PyTorch v2.10)")|None=None_)→T[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.cuda "Link to this definition")
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

double()→T[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.double "Link to this definition")
Casts all floating point parameters and buffers to `double` datatype.

Note

This method modifies the module in-place.

Returns:
self

Return type:
[Module](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

eval()→T[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.eval "Link to this definition")
Sets the module in evaluation mode.

This has any effect only on certain modules. See documentations of particular modules for details of their behaviors in training/evaluation mode, if they are affected, e.g. `Dropout`, `BatchNorm`, etc.

This is equivalent with [`self.train(False)`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.train "(in PyTorch v2.10)").

See [Locally disabling gradient computation](https://docs.pytorch.org/docs/stable/notes/autograd.html#locally-disable-grad-doc "(in PyTorch v2.10)") for a comparison between .eval() and several similar mechanisms that may be confused with it.

Returns:
self

Return type:
[Module](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

fit(_train\_dataloader:DataLoader,evaluator:SentenceEvaluator|None=None,epochs:int=1,loss\_fct=None,activation\_fct=Identity(),scheduler:str='WarmupLinear',warmup\_steps:int=10000,optimizer\_class:type[Optimizer]=<class'torch.optim.adamw.AdamW'>,optimizer\_params:dict[str,object]={'lr':2e-05},weight\_decay:float=0.01,evaluation\_steps:int=0,output\_path:str|None=None,save\_best\_model:bool=True,max\_grad\_norm:float=1,use\_amp:bool=False,callback:Callable[[float,int,int],None]=None,show\_progress\_bar:bool=True_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/cross_encoder/fit_mixin.py#L182-L369)[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.fit "Link to this definition")
Deprecated training method from before Sentence Transformers v4.0, it is recommended to use `CrossEncoderTrainer` instead. This method uses `CrossEncoderTrainer` behind the scenes, but does not provide as much flexibility as the Trainer itself.

This training approach uses a DataLoader and Loss function to train the model.

This method should produce equivalent results in v4.0 as before v4.0, but if you encounter any issues with your existing training scripts, then you may wish to use [`CrossEncoder.old_fit`](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.old_fit "sentence_transformers.cross_encoder.CrossEncoder.old_fit") instead. That uses the old training method from before v4.0.

Parameters:
*   **train_dataloader** – The DataLoader with InputExample instances

*   **evaluator** – An evaluator (sentence_transformers.cross_encoder.evaluation) evaluates the model performance during training on held- out dev data. It is used to determine the best model that is saved to disk.

*   **epochs** – Number of epochs for training

*   **loss_fct** – Which loss function to use for training. If None, will use BinaryCrossEntropy() if self.config.num_labels == 1 else CrossEntropyLoss(). Defaults to None.

*   **activation_fct** – Activation function applied on top of logits output of model.

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

float()→T[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.float "Link to this definition")
Casts all floating point parameters and buffers to `float` datatype.

Note

This method modifies the module in-place.

Returns:
self

Return type:
[Module](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

get_backend()→Literal['torch','onnx','openvino'][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/cross_encoder/CrossEncoder.py#L265-L271)[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.get_backend "Link to this definition")
Return the backend used for inference, which can be one of “torch”, “onnx”, or “openvino”.

Returns:
The backend used for inference.

Return type:
str

half()→T[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.half "Link to this definition")
Casts all floating point parameters and buffers to `half` datatype.

Note

This method modifies the module in-place.

Returns:
self

Return type:
[Module](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

old_fit(_train\_dataloader:~torch.utils.data.dataloader.DataLoader,evaluator:~sentence\_transformers.evaluation.SentenceEvaluator.SentenceEvaluator|None=None,epochs:int=1,loss\_fct=None,activation\_fct=Identity(),scheduler:str='WarmupLinear',warmup\_steps:int=10000,optimizer\_class:type[~torch.optim.optimizer.Optimizer]=<class'torch.optim.adamw.AdamW'>,optimizer\_params:dict[str,object]={'lr':2e-05},weight\_decay:float=0.01,evaluation\_steps:int=0,output\_path:str|None=None,save\_best\_model:bool=True,max\_grad\_norm:float=1,use\_amp:bool=False,callback:~collections.abc.Callable[[float,int,int],None]|None=None,show\_progress\_bar:bool=True_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/cross_encoder/fit_mixin.py#L417-L567)[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.old_fit "Link to this definition")
Deprecated training method from before Sentence Transformers v4.0, it is recommended to use `CrossEncoderTrainer` instead. This method should only be used if you encounter issues with your existing training scripts after upgrading to v4.0.

This training approach uses a DataLoader and Loss function to train the model.

Parameters:
*   **train_dataloader** – The DataLoader with InputExample instances

*   **evaluator** – An evaluator (sentence_transformers.cross_encoder.evaluation) evaluates the model performance during training on held- out dev data. It is used to determine the best model that is saved to disk.

*   **epochs** – Number of epochs for training

*   **loss_fct** – Which loss function to use for training. If None, will use BinaryCrossEntropy() if self.config.num_labels == 1 else CrossEntropyLoss(). Defaults to None.

*   **activation_fct** – Activation function applied on top of logits output of model.

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

predict(_sentences:tuple[str,str]|list[str]_, _batch\_size:int=32_, _show\_progress\_bar:bool|None=None_, _activation\_fn:Callable|None=None_, _apply\_softmax:bool|None=False_, _convert\_to\_numpy:Literal[False]=True_, _convert\_to\_tensor:Literal[False]=False_, _device:str|list[str|[torch.device](https://docs.pytorch.org/docs/stable/tensor\_attributes.html#torch.device "(in PyTorch v2.10)")]|None=None_, _pool:dict[Literal['input','output','processes'],Any]|None=None_, _chunk\_size:int|None=None_)→[torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/cross_encoder/CrossEncoder.py#L597-L735)[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.predict "Link to this definition")predict(_sentences:list[tuple[str,str]]|list[list[str]]|tuple[str,str]|list[str]_, _batch\_size:int=32_, _show\_progress\_bar:bool|None=None_, _activation\_fn:Callable|None=None_, _apply\_softmax:bool|None=False_, _convert\_to\_numpy:Literal[True]=True_, _convert\_to\_tensor:Literal[False]=False_, _device:str|list[str|[torch.device](https://docs.pytorch.org/docs/stable/tensor\_attributes.html#torch.device "(in PyTorch v2.10)")]|None=None_, _pool:dict[Literal['input','output','processes'],Any]|None=None_, _chunk\_size:int|None=None_)→np.ndarray predict(_sentences:list[tuple[str,str]]|list[list[str]]|tuple[str,str]|list[str]_, _batch\_size:int=32_, _show\_progress\_bar:bool|None=None_, _activation\_fn:Callable|None=None_, _apply\_softmax:bool|None=False_, _convert\_to\_numpy:bool=True_, _convert\_to\_tensor:Literal[True]=False_, _device:str|list[str|[torch.device](https://docs.pytorch.org/docs/stable/tensor\_attributes.html#torch.device "(in PyTorch v2.10)")]|None=None_, _pool:dict[Literal['input','output','processes'],Any]|None=None_, _chunk\_size:int|None=None_)→[torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")predict(_sentences:list[tuple[str,str]]|list[list[str]]_, _batch\_size:int=32_, _show\_progress\_bar:bool|None=None_, _activation\_fn:Callable|None=None_, _apply\_softmax:bool|None=False_, _convert\_to\_numpy:Literal[False]=True_, _convert\_to\_tensor:Literal[False]=False_, _device:str|list[str|[torch.device](https://docs.pytorch.org/docs/stable/tensor\_attributes.html#torch.device "(in PyTorch v2.10)")]|None=None_, _pool:dict[Literal['input','output','processes'],Any]|None=None_, _chunk\_size:int|None=None_)→list[[torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")]
Performs predictions with the CrossEncoder on the given sentence pairs.

Parameters:
*   **sentences** (_Union_ _[_ _List_ _[_ _Tuple_ _[_ _str_ _,_ _str_ _]_ _]_ _,_ _Tuple_ _[_ _str_ _,_ _str_ _]_ _]_) – A list of sentence pairs [(Sent1, Sent2), (Sent3, Sent4)] or one sentence pair (Sent1, Sent2).

*   **batch_size** (_int_ _,_ _optional_) – Batch size for encoding. Defaults to 32.

*   **show_progress_bar** (_bool_ _,_ _optional_) – Output progress bar. Defaults to None.

*   **activation_fn** (_callable_ _,_ _optional_) – Activation function applied on the logits output of the CrossEncoder. If None, the `model.activation_fn` will be used, which defaults to [`torch.nn.Sigmoid`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Sigmoid.html#torch.nn.Sigmoid "(in PyTorch v2.10)") if num_labels=1, else [`torch.nn.Identity`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Identity.html#torch.nn.Identity "(in PyTorch v2.10)"). Defaults to None.

*   **convert_to_numpy** (_bool_ _,_ _optional_) – Convert the output to a numpy matrix. Defaults to True.

*   **apply_softmax** (_bool_ _,_ _optional_) – If set to True and model.num_labels > 1, applies softmax on the logits output such that for each sample, the scores of each class sum to 1. Defaults to False.

*   **convert_to_numpy** – Whether the output should be a list of numpy vectors. If False, output a list of PyTorch tensors. Defaults to True.

*   **convert_to_tensor** (_bool_ _,_ _optional_) – Whether the output should be one large tensor. Overwrites convert_to_numpy. Defaults to False.

*   **device** (_Union_ _[_ _str_ _,_ _List_ _[_ _str_ _]_ _]_ _,_ _optional_) – Device(s) to use for computation. Can be a single device string (e.g., “cuda:0”, “cpu”) or a list of devices (e.g., [“cuda:0”, “cuda:1”]). If a list is provided, multiprocessing will be used automatically. Defaults to None.

*   **pool** (_Dict_ _[_ _str_ _,_ _Any_ _]_ _,_ _optional_) – A pool of workers created with [`start_multi_process_pool()`](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.start_multi_process_pool "sentence_transformers.cross_encoder.CrossEncoder.start_multi_process_pool"). If provided, multiprocessing will be used. If None and `device` is a list, a pool will be created automatically. Defaults to None.

*   **chunk_size** (_int_ _,_ _optional_) – Size of chunks for multiprocessing. If None, a sensible default is calculated. Only used when `pool` is not None or `device` is a list. Defaults to None.

Returns:
Predictions for the passed sentence pairs. The return type depends on the `convert_to_numpy` and `convert_to_tensor` parameters. If `convert_to_tensor` is True, the output will be a [`torch.Tensor`](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)"). If `convert_to_numpy` is True, the output will be a `numpy.ndarray`. Otherwise, the output will be a list of [`torch.Tensor`](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)") values.

Return type:
Union[List[[torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")], np.ndarray, [torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")]

Examples

from sentence_transformers import CrossEncoder

model = CrossEncoder("cross-encoder/stsb-roberta-base")
sentences = [["I love cats", "Cats are amazing"], ["I prefer dogs", "Dogs are loyal"]]
model.predict(sentences)
# => array([0.6912767, 0.4303499], dtype=float32)

# Using multiprocessing with automatic pool
scores = model.predict(sentences, device=["cuda:0", "cuda:1"])

# Using multiprocessing with manual pool
pool = model.start_multi_process_pool()
scores = model.predict(sentences, pool=pool)
model.stop_multi_process_pool(pool)

push_to_hub(_repo\_id:str_, _*_, _token:str|None=None_, _private:bool|None=None_, _safe\_serialization:bool=True_, _commit\_message:str|None=None_, _exist\_ok:bool=False_, _revision:str|None=None_, _create\_pr:bool=False_, _tags:list[str]|None=None_)→str[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/cross_encoder/CrossEncoder.py#L907-L985)[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.push_to_hub "Link to this definition")
Upload the CrossEncoder model to the Hugging Face Hub.

Example

from sentence_transformers import CrossEncoder

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")
model.push_to_hub("username/my-crossencoder-model")
# => "https://huggingface.co/username/my-crossencoder-model"

Parameters:
*   **repo_id** (_str_) – The name of the repository on the Hugging Face Hub, e.g. “username/repo_name”, “organization/repo_name” or just “repo_name”.

*   **token** (_str_ _,_ _optional_) – The authentication token to use for the Hugging Face Hub API. If not provided, will use the token stored via the Hugging Face CLI.

*   **private** (_bool_ _,_ _optional_) – Whether to create a private repository. If not specified, the repository will be public.

*   **safe_serialization** (_bool_ _,_ _optional_) – Whether or not to convert the model weights in safetensors format for safer serialization. Defaults to True.

*   **commit_message** (_str_ _,_ _optional_) – The commit message to use for the push. Defaults to “Add new CrossEncoder model”.

*   **exist_ok** (_bool_ _,_ _optional_) – If True, do not raise an error if the repository already exists. Ignored if `create_pr=True`. Defaults to False.

*   **revision** (_str_ _,_ _optional_) – The git branch to commit to. Defaults to the head of the ‘main’ branch.

*   **create_pr** (_bool_ _,_ _optional_) – Whether to create a Pull Request with the upload or directly commit. Defaults to False.

*   **tags** (_list_ _[_ _str_ _]_ _,_ _optional_) – A list of tags to add to the model card. Defaults to None.

Returns:
URL of the commit or pull request (if create_pr=True)

Return type:
str

rank(_query:str_, _documents:list[str]_, _top\_k:int|None=None_, _return\_documents:bool=False_, _batch\_size:int=32_, _show\_progress\_bar:bool|None=None_, _activation\_fn:Callable|None=None_, _apply\_softmax=False_, _convert\_to\_numpy:bool=True_, _convert\_to\_tensor:bool=False_, _device:str|list[str|[device](https://docs.pytorch.org/docs/stable/tensor\_attributes.html#torch.device "(in PyTorch v2.10)")]|None=None_, _pool:dict[Literal['input','output','processes'],Any]|None=None_, _chunk\_size:int|None=None_)→list[dict[Literal['corpus_id','score','text'],int|float|str]][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/cross_encoder/CrossEncoder.py#L737-L842)[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.rank "Link to this definition")
Performs ranking with the CrossEncoder on the given query and documents. Returns a sorted list with the document indices and scores.

Parameters:
*   **query** (_str_) – A single query.

*   **documents** (_List_ _[_ _str_ _]_) – A list of documents.

*   **top_k** (_Optional_ _[_ _int_ _]_ _,_ _optional_) – Return the top-k documents. If None, all documents are returned. Defaults to None.

*   **return_documents** (_bool_ _,_ _optional_) – If True, also returns the documents. If False, only returns the indices and scores. Defaults to False.

*   **batch_size** (_int_ _,_ _optional_) – Batch size for encoding. Defaults to 32.

*   **show_progress_bar** (_bool_ _,_ _optional_) – Output progress bar. Defaults to None.

*   **activation_fn** (_[_ _type_ _]_ _,_ _optional_) – Activation function applied on the logits output of the CrossEncoder. If None, nn.Sigmoid() will be used if num_labels=1, else nn.Identity. Defaults to None.

*   **convert_to_numpy** (_bool_ _,_ _optional_) – Convert the output to a numpy matrix. Defaults to True.

*   **apply_softmax** (_bool_ _,_ _optional_) – If there are more than 2 dimensions and apply_softmax=True, applies softmax on the logits output. Defaults to False.

*   **convert_to_tensor** (_bool_ _,_ _optional_) – Convert the output to a tensor. Defaults to False.

*   **device** (_Union_ _[_ _str_ _,_ _List_ _[_ _str_ _]_ _]_ _,_ _optional_) – Device(s) to use for computation. Can be a single device string (e.g., “cuda:0”, “cpu”) or a list of devices (e.g., [“cuda:0”, “cuda:1”]). If a list is provided, multiprocessing will be used automatically. Defaults to None.

*   **pool** (_Dict_ _[_ _str_ _,_ _Any_ _]_ _,_ _optional_) – A pool of workers created with [`start_multi_process_pool()`](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.start_multi_process_pool "sentence_transformers.cross_encoder.CrossEncoder.start_multi_process_pool"). If provided, multiprocessing will be used. If None and `device` is a list, a pool will be created automatically. Defaults to None.

*   **chunk_size** (_int_ _,_ _optional_) – Size of chunks for multiprocessing. If None, a sensible default is calculated. Only used when `pool` is not None or `device` is a list. Defaults to None.

Returns:
A sorted list with the “corpus_id”, “score”, and optionally “text” of the documents.

Return type:
List[Dict[Literal[“corpus_id”, “score”, “text”], Union[int, float, str]]]

Example

from sentence_transformers import CrossEncoder
model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")

query = "Who wrote 'To Kill a Mockingbird'?"
documents = [
    "'To Kill a Mockingbird' is a novel by Harper Lee published in 1960. It was immediately successful, winning the Pulitzer Prize, and has become a classic of modern American literature.",
    "The novel 'Moby-Dick' was written by Herman Melville and first published in 1851. It is considered a masterpiece of American literature and deals with complex themes of obsession, revenge, and the conflict between good and evil.",
    "Harper Lee, an American novelist widely known for her novel 'To Kill a Mockingbird', was born in 1926 in Monroeville, Alabama. She received the Pulitzer Prize for Fiction in 1961.",
    "Jane Austen was an English novelist known primarily for her six major novels, which interpret, critique and comment upon the British landed gentry at the end of the 18th century.",
    "The 'Harry Potter' series, which consists of seven fantasy novels written by British author J.K. Rowling, is among the most popular and critically acclaimed books of the modern era.",
    "'The Great Gatsby', a novel written by American author F. Scott Fitzgerald, was published in 1925. The story is set in the Jazz Age and follows the life of millionaire Jay Gatsby and his pursuit of Daisy Buchanan."
]

model.rank(query, documents, return_documents=True)

[{'corpus_id': 0,
'score': 10.67858,
'text': "'To Kill a Mockingbird' is a novel by Harper Lee published in 1960. It was immediately successful, winning the Pulitzer Prize, and has become a classic of modern American literature."},
{'corpus_id': 2,
'score': 9.761677,
'text': "Harper Lee, an American novelist widely known for her novel 'To Kill a Mockingbird', was born in 1926 in Monroeville, Alabama. She received the Pulitzer Prize for Fiction in 1961."},
{'corpus_id': 1,
'score': -3.3099542,
'text': "The novel 'Moby-Dick' was written by Herman Melville and first published in 1851. It is considered a masterpiece of American literature and deals with complex themes of obsession, revenge, and the conflict between good and evil."},
{'corpus_id': 5,
'score': -4.8989105,
'text': "'The Great Gatsby', a novel written by American author F. Scott Fitzgerald, was published in 1925. The story is set in the Jazz Age and follows the life of millionaire Jay Gatsby and his pursuit of Daisy Buchanan."},
{'corpus_id': 4,
'score': -5.082967,
'text': "The 'Harry Potter' series, which consists of seven fantasy novels written by British author J.K. Rowling, is among the most popular and critically acclaimed books of the modern era."}]

save_pretrained(_path:str_, _*_, _safe\_serialization:bool=True_, _**kwargs_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/cross_encoder/CrossEncoder.py#L857-L870)[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.save_pretrained "Link to this definition")
Save the model and tokenizer to the specified path.

Parameters:
*   **path** (_str_) – Directory where the model should be saved

*   **safe_serialization** (_bool_ _,_ _optional_) – Whether to save using safetensors or the traditional PyTorch way. Defaults to True.

*   ****kwargs** – Additional arguments passed to the underlying save methods of the model and tokenizer.

Returns:
None

set_config_value(_key:str_, _value_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/cross_encoder/CrossEncoder.py#L495-L508)[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.set_config_value "Link to this definition")
Set a value in the underlying model’s config.

Parameters:
*   **key** (_str_) – The key to set.

*   **value** – The value to set.

start_multi_process_pool(_target\_devices:list[str]|None=None_)→dict[Literal['input','output','processes'],Any][[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/cross_encoder/CrossEncoder.py#L273-L321)[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.start_multi_process_pool "Link to this definition")
Starts a multi-process pool to process the prediction with several independent processes via [`CrossEncoder.predict`](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.predict "sentence_transformers.cross_encoder.CrossEncoder.predict").

This method is recommended if you want to predict on multiple GPUs or CPUs. It is advised to start only one process per GPU. This method works together with predict and stop_multi_process_pool.

Parameters:
**target_devices** (_List_ _[_ _str_ _]_ _,_ _optional_) – PyTorch target devices, e.g. [“cuda:0”, “cuda:1”, …], [“npu:0”, “npu:1”, …], or [“cpu”, “cpu”, “cpu”, “cpu”]. If target_devices is None and CUDA/NPU is available, then all available CUDA/NPU devices will be used. If target_devices is None and CUDA/NPU is not available, then 4 CPU devices will be used.

Returns:
A dictionary with the target processes, an input queue, and an output queue.

Return type:
Dict[str, Any]

_static_ stop_multi_process_pool(_pool:dict[Literal['input','output','processes'],Any]_)→None[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/cross_encoder/CrossEncoder.py#L323-L342)[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.stop_multi_process_pool "Link to this definition")
Stops all processes started with start_multi_process_pool.

Parameters:
**pool** (_Dict_ _[_ _str_ _,_ _object_ _]_) – A dictionary containing the input queue, output queue, and process list.

Returns:
None

to(_*args_, _**kwargs_)[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.to "Link to this definition")
Moves and/or casts the parameters and buffers.

This can be called as

to(_device=None_, _dtype=None_, _non\_blocking=False_)to(_dtype_, _non\_blocking=False_)to(_tensor_, _non\_blocking=False_)to(_memory\_format=torch.channels\_last_)
Its signature is similar to [`torch.Tensor.to()`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.to.html#torch.Tensor.to "(in PyTorch v2.10)"), but only accepts floating point or complex `dtype`s. In addition, this method will only cast the floating point or complex parameters and buffers to `dtype` (if given). The integral parameters and buffers will be moved `device`, if that is given, but with dtypes unchanged. When `non_blocking` is set, it tries to convert/move asynchronously with respect to the host if possible, e.g., moving CPU Tensors with pinned memory to CUDA devices.

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

train(_mode:bool=True_)→T[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.train "Link to this definition")
Sets the module in training mode.

This has any effect only on certain modules. See documentations of particular modules for details of their behaviors in training/evaluation mode, if they are affected, e.g. `Dropout`, `BatchNorm`, etc.

Parameters:
**mode** (_bool_) – whether to set training mode (`True`) or evaluation mode (`False`). Default: `True`.

Returns:
self

Return type:
[Module](https://sbert.net/docs/package_reference/sentence_transformer/models.html#sentence_transformers.models.Module "sentence_transformers.models.Module")

_property_ transformers_model _:PreTrainedModel|None_[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.transformers_model "Link to this definition")
Property to get the underlying transformers PreTrainedModel instance.

Returns:
The underlying transformers model or None if not found.

Return type:
PreTrainedModel or None

Example

from sentence_transformers import CrossEncoder

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")

# You can now access the underlying transformers model
transformers_model = model.transformers_model
print(type(transformers_model))
# => <class 'transformers.models.bert.modeling_bert.BertForSequenceClassification'>

CrossEncoderModelCardData[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#crossencodermodelcarddata "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.cross_encoder.model_card.CrossEncoderModelCardData(_language:str|list[str]|None=<factory>_, _license:str|None=None_, _model\_name:str|None=None_, _model\_id:str|None=None_, _train\_datasets:list[dict[str_, _str]]=<factory>_, _eval\_datasets:list[dict[str_, _str]]=<factory>_, _task\_name:str|None=None_, _tags:list[str]|None=<factory>_, _local\_files\_only:bool=False_, _generate\_widget\_examples:bool=True_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/cross_encoder/model_card.py#L27-L159)[](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.model_card.CrossEncoderModelCardData "Link to this definition")
A dataclass storing data used in the model card.

Parameters:
*   **language** (Optional[Union[str, List[str]]]) – The model language, either a string or a list, e.g. “en” or [“en”, “de”, “nl”]

*   **license** (Optional[str]) – The license of the model, e.g. “apache-2.0”, “mit”, or “cc-by-nc-sa-4.0”

*   **model_name** (Optional[str]) – The pretty name of the model, e.g. “CrossEncoder based on answerdotai/ModernBERT-base”.

*   **model_id** (Optional[str]) – The model ID when pushing the model to the Hub, e.g. “tomaarsen/ce-mpnet-base-ms-marco”.

*   **train_datasets** (List[Dict[str, str]]) – A list of the names and/or Hugging Face dataset IDs of the training datasets. e.g. [{“name”: “SNLI”, “id”: “stanfordnlp/snli”}, {“name”: “MultiNLI”, “id”: “nyu-mll/multi_nli”}, {“name”: “STSB”}]

*   **eval_datasets** (List[Dict[str, str]]) – A list of the names and/or Hugging Face dataset IDs of the evaluation datasets. e.g. [{“name”: “SNLI”, “id”: “stanfordnlp/snli”}, {“id”: “mteb/stsbenchmark-sts”}]

*   **task_name** (str) – The human-readable task the model is trained on, e.g. “semantic search and paraphrase mining”.

*   **tags** (Optional[List[str]]) – A list of tags for the model, e.g. [“sentence-transformers”, “cross-encoder”].

*   **local_files_only** (bool) – If True, don’t attempt to find dataset or base model information on the Hub. Defaults to False.

Tip

Install [codecarbon](https://github.com/mlco2/codecarbon) to automatically track carbon emission usage and include it in your model cards.

Example:

>>> model = CrossEncoder(
...     "microsoft/mpnet-base",
...     model_card_data=CrossEncoderModelCardData(
...         model_id="tomaarsen/ce-mpnet-base-allnli",
...         train_datasets=[{"name": "SNLI", "id": "stanfordnlp/snli"}, {"name": "MultiNLI", "id": "nyu-mll/multi_nli"}],
...         eval_datasets=[{"name": "SNLI", "id": "stanfordnlp/snli"}, {"name": "MultiNLI", "id": "nyu-mll/multi_nli"}],
...         license="apache-2.0",
...         language="en",
...     ),
... )

[Previous](https://sbert.net/docs/package_reference/cross_encoder/index.html "Cross Encoder")[Next](https://sbert.net/docs/package_reference/cross_encoder/trainer.html "Trainer")

* * *

© Copyright 2026.

 Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org/).
