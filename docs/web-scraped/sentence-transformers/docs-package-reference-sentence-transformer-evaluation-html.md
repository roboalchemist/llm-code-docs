# Source: https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html

Title: Evaluation — Sentence Transformers documentation

URL Source: https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html

Published Time: Tue, 17 Feb 2026 14:05:52 GMT

Markdown Content:
Evaluation — Sentence Transformers documentation
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

    *   [Evaluation](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#)
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
*   Evaluation
*   [Edit on GitHub](https://github.com/huggingface/sentence-transformers/blob/main/docs/package_reference/sentence_transformer/evaluation.md)

* * *

Evaluation[](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#evaluation "Link to this heading")
==============================================================================================================================

`sentence_transformers.evaluation` defines different classes, that can be used to evaluate the model during training.

BinaryClassificationEvaluator[](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#binaryclassificationevaluator "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.evaluation.BinaryClassificationEvaluator(_sentences1:list[str]_, _sentences2:list[str]_, _labels:list[int]_, _name:str=''_, _batch\_size:int=32_, _show\_progress\_bar:bool=False_, _write\_csv:bool=True_, _truncate\_dim:int|None=None_, _similarity\_fn\_names:list[Literal['cosine','dot','euclidean','manhattan']]|None=None_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/evaluation/BinaryClassificationEvaluator.py#L27-L379)[](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.BinaryClassificationEvaluator "Link to this definition")
Evaluate a model based on the similarity of the embeddings by calculating the accuracy of identifying similar and dissimilar sentences. The metrics are the cosine similarity, dot score, Euclidean and Manhattan distance The returned score is the accuracy with a specified metric.

The results are written in a CSV. If a CSV already exists, then values are appended.

The labels need to be 0 for dissimilar pairs and 1 for similar pairs.

Parameters:
*   **sentences1** (_List_ _[_ _str_ _]_) – The first column of sentences.

*   **sentences2** (_List_ _[_ _str_ _]_) – The second column of sentences.

*   **labels** (_List_ _[_ _int_ _]_) – labels[i] is the label for the pair (sentences1[i], sentences2[i]). Must be 0 or 1.

*   **name** (_str_ _,_ _optional_) – Name for the output. Defaults to “”.

*   **batch_size** (_int_ _,_ _optional_) – Batch size used to compute embeddings. Defaults to 32.

*   **show_progress_bar** (_bool_ _,_ _optional_) – If true, prints a progress bar. Defaults to False.

*   **write_csv** (_bool_ _,_ _optional_) – Write results to a CSV file. Defaults to True.

*   **truncate_dim** (_Optional_ _[_ _int_ _]_ _,_ _optional_) – The dimension to truncate sentence embeddings to. None uses the model’s current truncation dimension. Defaults to None.

*   **similarity_fn_names** (_Optional_ _[_ _List_ _[_ _Literal_ _[_ _"cosine"_ _,_ _"dot"_ _,_ _"euclidean"_ _,_ _"manhattan"_ _]_ _]_ _]_ _,_ _optional_) – The similarity functions to use. If not specified, defaults to the `similarity_fn_name` attribute of the model. Defaults to None.

Example

from sentence_transformers import SentenceTransformer
from sentence_transformers.evaluation import BinaryClassificationEvaluator
from datasets import load_dataset

# Load a model
model = SentenceTransformer('all-mpnet-base-v2')

# Load a dataset with two text columns and a class label column (https://huggingface.co/datasets/sentence-transformers/quora-duplicates)
eval_dataset = load_dataset("sentence-transformers/quora-duplicates", "pair-class", split="train[-1000:]")

# Initialize the evaluator
binary_acc_evaluator = BinaryClassificationEvaluator(
    sentences1=eval_dataset["sentence1"],
    sentences2=eval_dataset["sentence2"],
    labels=eval_dataset["label"],
    name="quora_duplicates_dev",
)
results = binary_acc_evaluator(model)
'''
Binary Accuracy Evaluation of the model on the quora_duplicates_dev dataset:
Accuracy with Cosine-Similarity: 81.60 (Threshold: 0.8352)
F1 with Cosine-Similarity: 75.27 (Threshold: 0.7715)
Precision with Cosine-Similarity: 65.81
Recall with Cosine-Similarity: 87.89
Average Precision with Cosine-Similarity: 76.03
Matthews Correlation with Cosine-Similarity: 62.48
'''
print(binary_acc_evaluator.primary_metric)
# => "quora_duplicates_dev_cosine_ap"
print(results[binary_acc_evaluator.primary_metric])
# => 0.760277070888393

EmbeddingSimilarityEvaluator[](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#embeddingsimilarityevaluator "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.evaluation.EmbeddingSimilarityEvaluator(_sentences1:list[str]_, _sentences2:list[str]_, _scores:list[float]_, _batch\_size:int=16_, _main\_similarity:str|[SimilarityFunction](https://sbert.net/docs/package\_reference/sparse\_encoder/SparseEncoder.html#sentence\_transformers.SimilarityFunction "sentence\_transformers.similarity\_functions.SimilarityFunction")|None=None_, _similarity\_fn\_names:list[Literal['cosine','dot','euclidean','manhattan']]|None=None_, _name:str=''_, _show\_progress\_bar:bool=False_, _write\_csv:bool=True_, _precision:Literal['float32','int8','uint8','binary','ubinary']|None=None_, _truncate\_dim:int|None=None_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/evaluation/EmbeddingSimilarityEvaluator.py#L27-L272)[](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator "Link to this definition")
Evaluate a model based on the similarity of the embeddings by calculating the Spearman and Pearson rank correlation in comparison to the gold standard labels. The metrics are the cosine similarity as well as euclidean and Manhattan distance The returned score is the Spearman correlation with a specified metric.

Parameters:
*   **sentences1** (_List_ _[_ _str_ _]_) – List with the first sentence in a pair.

*   **sentences2** (_List_ _[_ _str_ _]_) – List with the second sentence in a pair.

*   **scores** (_List_ _[_ _float_ _]_) – Similarity score between sentences1[i] and sentences2[i].

*   **batch_size** (_int_ _,_ _optional_) – The batch size for processing the sentences. Defaults to 16.

*   **main_similarity** (_Optional_ _[_ _Union_ _[_ _str_ _,_[_SimilarityFunction_](https://sbert.net/docs/package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")_]_ _]_ _,_ _optional_) – The main similarity function to use. Can be a string (e.g. “cosine”, “dot”) or a SimilarityFunction object. Defaults to None.

*   **similarity_fn_names** (_List_ _[_ _str_ _]_ _,_ _optional_) – List of similarity function names to use. If None, the `similarity_fn_name` attribute of the model is used. Defaults to None.

*   **name** (_str_ _,_ _optional_) – The name of the evaluator. Defaults to “”.

*   **show_progress_bar** (_bool_ _,_ _optional_) – Whether to show a progress bar during evaluation. Defaults to False.

*   **write_csv** (_bool_ _,_ _optional_) – Whether to write the evaluation results to a CSV file. Defaults to True.

*   **precision** (_Optional_ _[_ _Literal_ _[_ _"float32"_ _,_ _"int8"_ _,_ _"uint8"_ _,_ _"binary"_ _,_ _"ubinary"_ _]_ _]_ _,_ _optional_) – The precision to use for the embeddings. Can be “float32”, “int8”, “uint8”, “binary”, or “ubinary”. Defaults to None.

*   **truncate_dim** (_Optional_ _[_ _int_ _]_ _,_ _optional_) – The dimension to truncate sentence embeddings to. None uses the model’s current truncation dimension. Defaults to None.

Example

from datasets import load_dataset
from sentence_transformers import SentenceTransformer
from sentence_transformers.evaluation import EmbeddingSimilarityEvaluator, SimilarityFunction

# Load a model
model = SentenceTransformer('all-mpnet-base-v2')

# Load the STSB dataset (https://huggingface.co/datasets/sentence-transformers/stsb)
eval_dataset = load_dataset("sentence-transformers/stsb", split="validation")

# Initialize the evaluator
dev_evaluator = EmbeddingSimilarityEvaluator(
    sentences1=eval_dataset["sentence1"],
    sentences2=eval_dataset["sentence2"],
    scores=eval_dataset["score"],
    name="sts_dev",
)
results = dev_evaluator(model)
'''
EmbeddingSimilarityEvaluator: Evaluating the model on the sts-dev dataset:
Cosine-Similarity: Pearson: 0.8806 Spearman: 0.8810
'''
print(dev_evaluator.primary_metric)
# => "sts_dev_pearson_cosine"
print(results[dev_evaluator.primary_metric])
# => 0.881019449484294

InformationRetrievalEvaluator[](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#informationretrievalevaluator "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.evaluation.InformationRetrievalEvaluator(_queries:dict[str,str]_, _corpus:dict[str,str]_, _relevant\_docs:dict[str,set[str]]_, _corpus\_chunk\_size:int=50000_, _mrr\_at\_k:list[int]=[10]_, _ndcg\_at\_k:list[int]=[10]_, _accuracy\_at\_k:list[int]=[1,3,5,10]_, _precision\_recall\_at\_k:list[int]=[1,3,5,10]_, _map\_at\_k:list[int]=[100]_, _show\_progress\_bar:bool=False_, _batch\_size:int=32_, _name:str=''_, _write\_csv:bool=True_, _truncate\_dim:int|None=None_, _score\_functions:dict[str,Callable[[[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)"),[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")],[Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")]]|None=None_, _main\_score\_function:str|[SimilarityFunction](https://sbert.net/docs/package\_reference/sparse\_encoder/SparseEncoder.html#sentence\_transformers.SimilarityFunction "sentence\_transformers.similarity\_functions.SimilarityFunction")|None=None_, _query\_prompt:str|None=None_, _query\_prompt\_name:str|None=None_, _corpus\_prompt:str|None=None_, _corpus\_prompt\_name:str|None=None_, _write\_predictions:bool=False_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/evaluation/InformationRetrievalEvaluator.py#L24-L569)[](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator "Link to this definition")
This class evaluates an Information Retrieval (IR) setting.

Given a set of queries and a large corpus set. It will retrieve for each query the top-k most similar document. It measures Mean Reciprocal Rank (MRR), Recall@k, and Normalized Discounted Cumulative Gain (NDCG)

Parameters:
*   **queries** (_Dict_ _[_ _str_ _,_ _str_ _]_) – A dictionary mapping query IDs to queries.

*   **corpus** (_Dict_ _[_ _str_ _,_ _str_ _]_) – A dictionary mapping document IDs to documents.

*   **relevant_docs** (_Dict_ _[_ _str_ _,_ _Set_ _[_ _str_ _]_ _]_) – A dictionary mapping query IDs to a set of relevant document IDs.

*   **corpus_chunk_size** (_int_) – The size of each chunk of the corpus. Defaults to 50000.

*   **mrr_at_k** (_List_ _[_ _int_ _]_) – A list of integers representing the values of k for MRR calculation. Defaults to [10].

*   **ndcg_at_k** (_List_ _[_ _int_ _]_) – A list of integers representing the values of k for NDCG calculation. Defaults to [10].

*   **accuracy_at_k** (_List_ _[_ _int_ _]_) – A list of integers representing the values of k for accuracy calculation. Defaults to [1, 3, 5, 10].

*   **precision_recall_at_k** (_List_ _[_ _int_ _]_) – A list of integers representing the values of k for precision and recall calculation. Defaults to [1, 3, 5, 10].

*   **map_at_k** (_List_ _[_ _int_ _]_) – A list of integers representing the values of k for MAP calculation. Defaults to [100].

*   **show_progress_bar** (_bool_) – Whether to show a progress bar during evaluation. Defaults to False.

*   **batch_size** (_int_) – The batch size for evaluation. Defaults to 32.

*   **name** (_str_) – A name for the evaluation. Defaults to “”.

*   **write_csv** (_bool_) – Whether to write the evaluation results to a CSV file. Defaults to True.

*   **truncate_dim** (_int_ _,_ _optional_) – The dimension to truncate the embeddings to. Defaults to None.

*   **score_functions** (_Dict_ _[_ _str_ _,_ _Callable_ _[_ _[_ _Tensor_ _,_ _Tensor_ _]_ _,_ _Tensor_ _]_ _]_) – A dictionary mapping score function names to score functions. Defaults to the `similarity` function from the `model`.

*   **main_score_function** (_Union_ _[_ _str_ _,_[_SimilarityFunction_](https://sbert.net/docs/package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")_]_ _,_ _optional_) – The main score function to use for evaluation. Defaults to None.

*   **query_prompt** (_str_ _,_ _optional_) – The prompt to be used when encoding the corpus. Defaults to None.

*   **query_prompt_name** (_str_ _,_ _optional_) – The name of the prompt to be used when encoding the corpus. Defaults to None.

*   **corpus_prompt** (_str_ _,_ _optional_) – The prompt to be used when encoding the corpus. Defaults to None.

*   **corpus_prompt_name** (_str_ _,_ _optional_) – The name of the prompt to be used when encoding the corpus. Defaults to None.

*   **write_predictions** (_bool_) – Whether to write the predictions to a JSONL file. Defaults to False. This can be useful for downstream evaluation as it can be used as input to the [`ReciprocalRankFusionEvaluator`](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.ReciprocalRankFusionEvaluator "sentence_transformers.sparse_encoder.evaluation.ReciprocalRankFusionEvaluator") that accept precomputed predictions.

Example

import random
from sentence_transformers import SentenceTransformer
from sentence_transformers.evaluation import InformationRetrievalEvaluator
from datasets import load_dataset

# Load a model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load the Touche-2020 IR dataset (https://huggingface.co/datasets/BeIR/webis-touche2020, https://huggingface.co/datasets/BeIR/webis-touche2020-qrels)
corpus = load_dataset("BeIR/webis-touche2020", "corpus", split="corpus")
queries = load_dataset("BeIR/webis-touche2020", "queries", split="queries")
relevant_docs_data = load_dataset("BeIR/webis-touche2020-qrels", split="test")

# For this dataset, we want to concatenate the title and texts for the corpus
corpus = corpus.map(lambda x: {'text': x['title'] + " " + x['text']}, remove_columns=['title'])

# Shrink the corpus size heavily to only the relevant documents + 30,000 random documents
required_corpus_ids = set(map(str, relevant_docs_data["corpus-id"]))
required_corpus_ids |= set(random.sample(corpus["_id"], k=30_000))
corpus = corpus.filter(lambda x: x["_id"] in required_corpus_ids)

# Convert the datasets to dictionaries
corpus = dict(zip(corpus["_id"], corpus["text"]))  # Our corpus (cid => document)
queries = dict(zip(queries["_id"], queries["text"]))  # Our queries (qid => question)
relevant_docs = {}  # Query ID to relevant documents (qid => set([relevant_cids])
for qid, corpus_ids in zip(relevant_docs_data["query-id"], relevant_docs_data["corpus-id"]):
    qid = str(qid)
    corpus_ids = str(corpus_ids)
    if qid not in relevant_docs:
        relevant_docs[qid] = set()
    relevant_docs[qid].add(corpus_ids)

# Given queries, a corpus and a mapping with relevant documents, the InformationRetrievalEvaluator computes different IR metrics.
ir_evaluator = InformationRetrievalEvaluator(
    queries=queries,
    corpus=corpus,
    relevant_docs=relevant_docs,
    name="BeIR-touche2020-subset-test",
)
results = ir_evaluator(model)
'''
Information Retrieval Evaluation of the model on the BeIR-touche2020-test dataset:
Queries: 49
Corpus: 31923

Score-Function: cosine
Accuracy@1: 77.55%
Accuracy@3: 93.88%
Accuracy@5: 97.96%
Accuracy@10: 100.00%
Precision@1: 77.55%
Precision@3: 72.11%
Precision@5: 71.43%
Precision@10: 62.65%
Recall@1: 1.72%
Recall@3: 4.78%
Recall@5: 7.90%
Recall@10: 13.86%
MRR@10: 0.8580
NDCG@10: 0.6606
MAP@100: 0.2934
'''
print(ir_evaluator.primary_metric)
# => "BeIR-touche2020-test_cosine_map@100"
print(results[ir_evaluator.primary_metric])
# => 0.29335196224364596

NanoBEIREvaluator[](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#nanobeirevaluator "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.evaluation.NanoBEIREvaluator(_dataset\_names:list[~typing.Literal['climatefever','dbpedia','fever','fiqa2018','hotpotqa','msmarco','nfcorpus','nq','quoraretrieval','scidocs','arguana','scifact','touche2020']|str]|None=None,dataset\_id:str='sentence-transformers/NanoBEIR-en',mrr\_at\_k:list[int]=[10],ndcg\_at\_k:list[int]=[10],accuracy\_at\_k:list[int]=[1,3,5,10],precision\_recall\_at\_k:list[int]=[1,3,5,10],map\_at\_k:list[int]=[100],show\_progress\_bar:bool=False,batch\_size:int=32,write\_csv:bool=True,truncate\_dim:int|None=None,score\_functions:dict[str,~collections.abc.Callable[[~torch.Tensor,~torch.Tensor],~torch.Tensor]]|None=None,main\_score\_function:str|~sentence\_transformers.similarity\_functions.SimilarityFunction|None=None,aggregate\_fn:~collections.abc.Callable[[list[float]],float]=<function mean>,aggregate\_key:str='mean',query\_prompts:str|dict[str,str]|None=None,corpus\_prompts:str|dict[str,str]|None=None,write\_predictions:bool=False_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/evaluation/NanoBEIREvaluator.py#L56-L535)[](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.NanoBEIREvaluator "Link to this definition")
This class evaluates the performance of a SentenceTransformer Model on the NanoBEIR collection of Information Retrieval datasets.

The NanoBEIR collection consists of downsized versions of several BEIR information-retrieval datasets, making it suitable for quickly benchmarking a model’s retrieval performance before running a full-scale BEIR evaluation. The datasets are available on Hugging Face in the Sentence Transformers [NanoBEIR collection](https://huggingface.co/collections/sentence-transformers/nanobeir-datasets), which reformats the [original collection](https://huggingface.co/collections/zeta-alpha-ai/nanobeir) from Zeta Alpha into the default [NanoBEIR-en](https://huggingface.co/datasets/sentence-transformers/NanoBEIR-en) dataset, alongside many translated versions. This evaluator reports the same metrics as the [`InformationRetrievalEvaluator`](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator "sentence_transformers.evaluation.InformationRetrievalEvaluator") (e.g., MRR, nDCG, Recall@k) for each dataset individually, as well as aggregated across all datasets.

Parameters:
*   **dataset_names** (_List_ _[_ _str_ _]_) – The short names of the datasets to evaluate on (e.g., “climatefever”, “msmarco”). If not specified, all predefined NanoBEIR datasets are used. The full list of available datasets is: “climatefever”, “dbpedia”, “fever”, “fiqa2018”, “hotpotqa”, “msmarco”, “nfcorpus”, “nq”, “quoraretrieval”, “scidocs”, “arguana”, “scifact”, and “touche2020”.

*   **dataset_id** (_str_) – The HuggingFace dataset ID to load the datasets from. Defaults to “sentence-transformers/NanoBEIR-en”. The dataset must contain “corpus”, “queries”, and “qrels” subsets for each NanoBEIR dataset, stored under splits named `Nano{DatasetName}` (for example, `NanoMSMARCO` or `NanoNFCorpus`).

*   **mrr_at_k** (_List_ _[_ _int_ _]_) – A list of integers representing the values of k for MRR calculation. Defaults to [10].

*   **ndcg_at_k** (_List_ _[_ _int_ _]_) – A list of integers representing the values of k for NDCG calculation. Defaults to [10].

*   **accuracy_at_k** (_List_ _[_ _int_ _]_) – A list of integers representing the values of k for accuracy calculation. Defaults to [1, 3, 5, 10].

*   **precision_recall_at_k** (_List_ _[_ _int_ _]_) – A list of integers representing the values of k for precision and recall calculation. Defaults to [1, 3, 5, 10].

*   **map_at_k** (_List_ _[_ _int_ _]_) – A list of integers representing the values of k for MAP calculation. Defaults to [100].

*   **show_progress_bar** (_bool_) – Whether to show a progress bar during evaluation. Defaults to False.

*   **batch_size** (_int_) – The batch size for evaluation. Defaults to 32.

*   **write_csv** (_bool_) – Whether to write the evaluation results to a CSV file. Defaults to True.

*   **truncate_dim** (_int_ _,_ _optional_) – The dimension to truncate the embeddings to. Defaults to None.

*   **score_functions** (_Dict_ _[_ _str_ _,_ _Callable_ _[_ _[_ _Tensor_ _,_ _Tensor_ _]_ _,_ _Tensor_ _]_ _]_) – A dictionary mapping score function names to score functions. Defaults to {SimilarityFunction.COSINE.value: cos_sim, SimilarityFunction.DOT_PRODUCT.value: dot_score}.

*   **main_score_function** (_Union_ _[_ _str_ _,_[_SimilarityFunction_](https://sbert.net/docs/package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")_]_ _,_ _optional_) – The main score function to use for evaluation. Defaults to None.

*   **aggregate_fn** (_Callable_ _[_ _[_ _list_ _[_ _float_ _]_ _]_ _,_ _float_ _]_) – The function to aggregate the scores. Defaults to np.mean.

*   **aggregate_key** (_str_) – The key to use for the aggregated score. Defaults to “mean”.

*   **query_prompts** (_str_ _|_ _dict_ _[_ _str_ _,_ _str_ _]_ _,_ _optional_) – The prompts to add to the queries. If a string, will add the same prompt to all queries. If a dict, expects that all datasets in dataset_names are keys.

*   **corpus_prompts** (_str_ _|_ _dict_ _[_ _str_ _,_ _str_ _]_ _,_ _optional_) – The prompts to add to the corpus. If a string, will add the same prompt to all corpus. If a dict, expects that all datasets in dataset_names are keys.

*   **write_predictions** (_bool_) – Whether to write the predictions to a JSONL file. Defaults to False. This can be useful for downstream evaluation as it can be used as input to the [`ReciprocalRankFusionEvaluator`](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.ReciprocalRankFusionEvaluator "sentence_transformers.sparse_encoder.evaluation.ReciprocalRankFusionEvaluator") that accept precomputed predictions.

Tip

See this [NanoBEIR datasets collection on Hugging Face](https://huggingface.co/collections/sentence-transformers/nanobeir-datasets) with valid NanoBEIR `dataset_id` options for different languages.

Example

from sentence_transformers import SentenceTransformer
from sentence_transformers.evaluation import NanoBEIREvaluator

model = SentenceTransformer('intfloat/multilingual-e5-large-instruct')

datasets = ["QuoraRetrieval", "MSMARCO"]
query_prompts = {
    "QuoraRetrieval": "Instruct: Given a question, retrieve questions that are semantically equivalent to the given question\nQuery: ",
    "MSMARCO": "Instruct: Given a web search query, retrieve relevant passages that answer the query\nQuery: "
}

evaluator = NanoBEIREvaluator(
    dataset_names=datasets,
    query_prompts=query_prompts,
)

results = evaluator(model)
'''
NanoBEIR Evaluation of the model on ['QuoraRetrieval', 'MSMARCO'] dataset:
Evaluating NanoQuoraRetrieval
Information Retrieval Evaluation of the model on the NanoQuoraRetrieval dataset:
Queries: 50
Corpus: 5046

Score-Function: cosine
Accuracy@1: 92.00%
Accuracy@3: 98.00%
Accuracy@5: 100.00%
Accuracy@10: 100.00%
Precision@1: 92.00%
Precision@3: 40.67%
Precision@5: 26.00%
Precision@10: 14.00%
Recall@1: 81.73%
Recall@3: 94.20%
Recall@5: 97.93%
Recall@10: 100.00%
MRR@10: 0.9540
NDCG@10: 0.9597
MAP@100: 0.9395

Evaluating NanoMSMARCO
Information Retrieval Evaluation of the model on the NanoMSMARCO dataset:
Queries: 50
Corpus: 5043

Score-Function: cosine
Accuracy@1: 40.00%
Accuracy@3: 74.00%
Accuracy@5: 78.00%
Accuracy@10: 88.00%
Precision@1: 40.00%
Precision@3: 24.67%
Precision@5: 15.60%
Precision@10: 8.80%
Recall@1: 40.00%
Recall@3: 74.00%
Recall@5: 78.00%
Recall@10: 88.00%
MRR@10: 0.5849
NDCG@10: 0.6572
MAP@100: 0.5892
Average Queries: 50.0
Average Corpus: 5044.5

Aggregated for Score Function: cosine
Accuracy@1: 66.00%
Accuracy@3: 86.00%
Accuracy@5: 89.00%
Accuracy@10: 94.00%
Precision@1: 66.00%
Recall@1: 60.87%
Precision@3: 32.67%
Recall@3: 84.10%
Precision@5: 20.80%
Recall@5: 87.97%
Precision@10: 11.40%
Recall@10: 94.00%
MRR@10: 0.7694
NDCG@10: 0.8085
'''
print(evaluator.primary_metric)
# => "NanoBEIR_mean_cosine_ndcg@10"
print(results[evaluator.primary_metric])
# => 0.8084508771660436

Evaluating on custom/translated datasets:

import logging
from pprint import pprint

from sentence_transformers import SentenceTransformer
from sentence_transformers.evaluation import NanoBEIREvaluator

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=logging.INFO)

model = SentenceTransformer("google/embeddinggemma-300m")
evaluator = NanoBEIREvaluator(
    ["msmarco", "nq"],
    dataset_id="lightonai/NanoBEIR-de",
    batch_size=32,
)
results = evaluator(model)
print(results[evaluator.primary_metric])
pprint({key: value for key, value in results.items() if "ndcg@10" in key})

MSEEvaluator[](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#mseevaluator "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.evaluation.MSEEvaluator(_source\_sentences:list[str]_, _target\_sentences:list[str]_, _teacher\_model=None_, _show\_progress\_bar:bool=False_, _batch\_size:int=32_, _name:str=''_, _write\_csv:bool=True_, _truncate\_dim:int|None=None_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/evaluation/MSEEvaluator.py#L18-L158)[](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.MSEEvaluator "Link to this definition")
Computes the mean squared error (x100) between the computed sentence embedding and some target sentence embedding.

The MSE is computed between ||teacher.encode(source_sentences) - student.encode(target_sentences)||.

For multilingual knowledge distillation ([https://huggingface.co/papers/2004.09813](https://huggingface.co/papers/2004.09813)), source_sentences are in English and target_sentences are in a different language like German, Chinese, Spanish…

Parameters:
*   **source_sentences** (_List_ _[_ _str_ _]_) – Source sentences to embed with the teacher model.

*   **target_sentences** (_List_ _[_ _str_ _]_) – Target sentences to embed with the student model.

*   **teacher_model** ([_SentenceTransformer_](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")_,_ _optional_) – The teacher model to compute the source sentence embeddings.

*   **show_progress_bar** (_bool_ _,_ _optional_) – Show progress bar when computing embeddings. Defaults to False.

*   **batch_size** (_int_ _,_ _optional_) – Batch size to compute sentence embeddings. Defaults to 32.

*   **name** (_str_ _,_ _optional_) – Name of the evaluator. Defaults to “”.

*   **write_csv** (_bool_ _,_ _optional_) – Write results to CSV file. Defaults to True.

*   **truncate_dim** (_int_ _,_ _optional_) – The dimension to truncate sentence embeddings to. None uses the model’s current truncation dimension. Defaults to None.

Example

from sentence_transformers import SentenceTransformer
from sentence_transformers.evaluation import MSEEvaluator
from datasets import load_dataset

# Load a model
student_model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')
teacher_model = SentenceTransformer('all-mpnet-base-v2')

# Load any dataset with some texts
dataset = load_dataset("sentence-transformers/stsb", split="validation")
sentences = dataset["sentence1"] + dataset["sentence2"]

# Given queries, a corpus and a mapping with relevant documents, the MSEEvaluator computes different MSE metrics.
mse_evaluator = MSEEvaluator(
    source_sentences=sentences,
    target_sentences=sentences,
    teacher_model=teacher_model,
    name="stsb-dev",
)
results = mse_evaluator(student_model)
'''
MSE evaluation (lower = better) on the stsb-dev dataset:
MSE (*100): 0.805045
'''
print(mse_evaluator.primary_metric)
# => "stsb-dev_negative_mse"
print(results[mse_evaluator.primary_metric])
# => -0.8050452917814255

ParaphraseMiningEvaluator[](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#paraphraseminingevaluator "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.evaluation.ParaphraseMiningEvaluator(_sentences\_map:dict[str,str]_, _duplicates\_list:list[tuple[str,str]]|None=None_, _duplicates\_dict:dict[str,dict[str,bool]]|None=None_, _add\_transitive\_closure:bool=False_, _query\_chunk\_size:int=5000_, _corpus\_chunk\_size:int=100000_, _max\_pairs:int=500000_, _top\_k:int=100_, _show\_progress\_bar:bool=False_, _batch\_size:int=16_, _name:str=''_, _write\_csv:bool=True_, _truncate\_dim:int|None=None_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/evaluation/ParaphraseMiningEvaluator.py#L18-L279)[](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.ParaphraseMiningEvaluator "Link to this definition")
Given a large set of sentences, this evaluator performs paraphrase (duplicate) mining and identifies the pairs with the highest similarity. It compare the extracted paraphrase pairs with a set of gold labels and computes the F1 score.

Parameters:
*   **sentences_map** (_Dict_ _[_ _str_ _,_ _str_ _]_) – A dictionary that maps sentence-ids to sentences. For example, sentences_map[id] => sentence.

*   **duplicates_list** (_List_ _[_ _Tuple_ _[_ _str_ _,_ _str_ _]_ _]_ _,_ _optional_) – A list with id pairs [(id1, id2), (id1, id5)] that identifies the duplicates / paraphrases in the sentences_map. Defaults to None.

*   **duplicates_dict** (_Dict_ _[_ _str_ _,_ _Dict_ _[_ _str_ _,_ _bool_ _]_ _]_ _,_ _optional_) – A default dictionary mapping [id1][id2] to true if id1 and id2 are duplicates. Must be symmetric, i.e., if [id1][id2] => True, then [id2][id1] => True. Defaults to None.

*   **add_transitive_closure** (_bool_ _,_ _optional_) – If true, it adds a transitive closure, i.e. if dup[a][b] and dup[b][c], then dup[a][c]. Defaults to False.

*   **query_chunk_size** (_int_ _,_ _optional_) – To identify the paraphrases, the cosine-similarity between all sentence-pairs will be computed. As this might require a lot of memory, we perform a batched computation. query_chunk_size sentences will be compared against up to corpus_chunk_size sentences. In the default setting, 5000 sentences will be grouped together and compared up-to against 100k other sentences. Defaults to 5000.

*   **corpus_chunk_size** (_int_ _,_ _optional_) – The corpus will be batched, to reduce the memory requirement. Defaults to 100000.

*   **max_pairs** (_int_ _,_ _optional_) – We will only extract up to max_pairs potential paraphrase candidates. Defaults to 500000.

*   **top_k** (_int_ _,_ _optional_) – For each query, we extract the top_k most similar pairs and add it to a sorted list. I.e., for one sentence we cannot find more than top_k paraphrases. Defaults to 100.

*   **show_progress_bar** (_bool_ _,_ _optional_) – Output a progress bar. Defaults to False.

*   **batch_size** (_int_ _,_ _optional_) – Batch size for computing sentence embeddings. Defaults to 16.

*   **name** (_str_ _,_ _optional_) – Name of the experiment. Defaults to “”.

*   **write_csv** (_bool_ _,_ _optional_) – Write results to CSV file. Defaults to True.

*   **truncate_dim** (_Optional_ _[_ _int_ _]_ _,_ _optional_) – The dimension to truncate sentence embeddings to. None uses the model’s current truncation dimension. Defaults to None.

Example

from datasets import load_dataset
from sentence_transformers.SentenceTransformer import SentenceTransformer
from sentence_transformers.evaluation import ParaphraseMiningEvaluator

# Load a model
model = SentenceTransformer('all-mpnet-base-v2')

# Load the Quora Duplicates Mining dataset
questions_dataset = load_dataset("sentence-transformers/quora-duplicates-mining", "questions", split="dev")
duplicates_dataset = load_dataset("sentence-transformers/quora-duplicates-mining", "duplicates", split="dev")

# Create a mapping from qid to question & a list of duplicates (qid1, qid2)
qid_to_questions = dict(zip(questions_dataset["qid"], questions_dataset["question"]))
duplicates = list(zip(duplicates_dataset["qid1"], duplicates_dataset["qid2"]))

# Initialize the paraphrase mining evaluator
paraphrase_mining_evaluator = ParaphraseMiningEvaluator(
    sentences_map=qid_to_questions,
    duplicates_list=duplicates,
    name="quora-duplicates-dev",
)
results = paraphrase_mining_evaluator(model)
'''
Paraphrase Mining Evaluation of the model on the quora-duplicates-dev dataset:
Number of candidate pairs: 250564
Average Precision: 56.51
Optimal threshold: 0.8325
Precision: 52.76
Recall: 59.19
F1: 55.79
'''
print(paraphrase_mining_evaluator.primary_metric)
# => "quora-duplicates-dev_average_precision"
print(results[paraphrase_mining_evaluator.primary_metric])
# => 0.5650940787776353

RerankingEvaluator[](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#rerankingevaluator "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.evaluation.RerankingEvaluator(_samples:list[dict[str,str|list[str]]],at\_k:int=10,name:str='',write\_csv:bool=True,similarity\_fct:~collections.abc.Callable[[~torch.Tensor,~torch.Tensor],~torch.Tensor]=<function cos\_sim>,batch\_size:int=64,show\_progress\_bar:bool=False,use\_batched\_encoding:bool=True,truncate\_dim:int|None=None,mrr\_at\_k:int|None=None_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/evaluation/RerankingEvaluator.py#L26-L373)[](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.RerankingEvaluator "Link to this definition")
This class evaluates a SentenceTransformer model for the task of re-ranking.

Given a query and a list of documents, it computes the score [query, doc_i] for all possible documents and sorts them in decreasing order. Then, [MRR@10](https://sbert.net/cdn-cgi/l/email-protection#e9a4bbbbcfcadaded2cfcadcdbd2cfcaddd1d2d8d9), [NDCG@10](https://sbert.net/cdn-cgi/l/email-protection#2b656f686c0d08181c100d081e19100d081f13101a1b) and MAP is compute to measure the quality of the ranking.

Parameters:
*   **samples** (_list_) –

A list of dictionaries, where each dictionary represents a sample and has the following keys:

    *   ’query’: The search query.

    *   ’positive’: A list of positive (relevant) documents.

    *   ’negative’: A list of negative (irrelevant) documents.

*   **at_k** (_int_ _,_ _optional_) – Only consider the top k most similar documents to each query for the evaluation. Defaults to 10.

*   **name** (_str_ _,_ _optional_) – Name of the evaluator. Defaults to “”.

*   **write_csv** (_bool_ _,_ _optional_) – Write results to CSV file. Defaults to True.

*   **similarity_fct** (_Callable_ _[_ _[_[_torch.Tensor_](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_,_[_torch.Tensor_](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_]_ _,_[_torch.Tensor_](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_]_ _,_ _optional_) – Similarity function between sentence embeddings. By default, cosine similarity. Defaults to cos_sim.

*   **batch_size** (_int_ _,_ _optional_) – Batch size to compute sentence embeddings. Defaults to 64.

*   **show_progress_bar** (_bool_ _,_ _optional_) – Show progress bar when computing embeddings. Defaults to False.

*   **use_batched_encoding** (_bool_ _,_ _optional_) – Whether or not to encode queries and documents in batches for greater speed, or 1-by-1 to save memory. Defaults to True.

*   **truncate_dim** (_Optional_ _[_ _int_ _]_ _,_ _optional_) – The dimension to truncate sentence embeddings to. None uses the model’s current truncation dimension. Defaults to None.

*   **mrr_at_k** (_Optional_ _[_ _int_ _]_ _,_ _optional_) – Deprecated parameter. Please use at_k instead. Defaults to None.

Example

from sentence_transformers import SentenceTransformer
from sentence_transformers.evaluation import RerankingEvaluator
from datasets import load_dataset

# Load a model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load a dataset with queries, positives, and negatives
eval_dataset = load_dataset("microsoft/ms_marco", "v1.1", split="validation")

samples = [
    {
        "query": sample["query"],
        "positive": [text for is_selected, text in zip(sample["passages"]["is_selected"], sample["passages"]["passage_text"]) if is_selected],
        "negative": [text for is_selected, text in zip(sample["passages"]["is_selected"], sample["passages"]["passage_text"]) if not is_selected],
    }
    for sample in eval_dataset
]

# Initialize the evaluator
reranking_evaluator = RerankingEvaluator(
    samples=samples,
    name="ms-marco-dev",
)
results = reranking_evaluator(model)
'''
RerankingEvaluator: Evaluating the model on the ms-marco-dev dataset:
Queries: 9706 Positives: Min 1.0, Mean 1.1, Max 5.0 Negatives: Min 1.0, Mean 7.1, Max 9.0
MAP: 56.07
MRR@10: 56.70
NDCG@10: 67.08
'''
print(reranking_evaluator.primary_metric)
# => ms-marco-dev_ndcg@10
print(results[reranking_evaluator.primary_metric])
# => 0.6708042171399308

SentenceEvaluator[](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentenceevaluator "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.evaluation.SentenceEvaluator[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/evaluation/SentenceEvaluator.py#L13-L120)[](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.SentenceEvaluator "Link to this definition")
Base class for all evaluators. Notably, this class introduces the `greater_is_better` and `primary_metric` attributes. The former is a boolean indicating whether a higher evaluation score is better, which is used for choosing the best checkpoint if `load_best_model_at_end` is set to `True` in the training arguments.

The latter is a string indicating the primary metric for the evaluator. This has to be defined whenever the evaluator returns a dictionary of metrics, and the primary metric is the key pointing to the primary metric, i.e. the one that is used for model selection and/or logging.

Extend this class and implement __call__ for custom evaluators.

SequentialEvaluator[](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sequentialevaluator "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.evaluation.SequentialEvaluator(_evaluators:~collections.abc.Iterable[~sentence\_transformers.evaluation.SentenceEvaluator.SentenceEvaluator],main\_score\_function=<function SequentialEvaluator.<lambda>>_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/evaluation/SequentialEvaluator.py#L12-L61)[](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.SequentialEvaluator "Link to this definition")
This evaluator allows that multiple sub-evaluators are passed. When the model is evaluated, the data is passed sequentially to all sub-evaluators.

All scores are passed to ‘main_score_function’, which derives one final score value

Parameters:
*   **evaluators** (_Iterable_ _[_[_SentenceEvaluator_](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.SentenceEvaluator "sentence_transformers.evaluation.SentenceEvaluator")_]_) – A collection of SentenceEvaluator objects.

*   **main_score_function** (_function_ _,_ _optional_) – A function that takes a list of scores and returns the main score. Defaults to selecting the last score in the list.

Example

evaluator1 = BinaryClassificationEvaluator(...)
evaluator2 = InformationRetrievalEvaluator(...)
evaluator3 = MSEEvaluator(...)
seq_evaluator = SequentialEvaluator([evaluator1, evaluator2, evaluator3])

TranslationEvaluator[](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#translationevaluator "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.evaluation.TranslationEvaluator(_source\_sentences:list[str]_, _target\_sentences:list[str]_, _show\_progress\_bar:bool=False_, _batch\_size:int=16_, _name:str=''_, _print\_wrong\_matches:bool=False_, _write\_csv:bool=True_, _truncate\_dim:int|None=None_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/evaluation/TranslationEvaluator.py#L22-L192)[](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.TranslationEvaluator "Link to this definition")
Given two sets of sentences in different languages, e.g. (en_1, en_2, en_3…) and (fr_1, fr_2, fr_3, …), and assuming that fr_i is the translation of en_i. Checks if vec(en_i) has the highest similarity to vec(fr_i). Computes the accuracy in both directions

The labels need to indicate the similarity between the sentences.

Parameters:
*   **source_sentences** (_List_ _[_ _str_ _]_) – List of sentences in the source language.

*   **target_sentences** (_List_ _[_ _str_ _]_) – List of sentences in the target language.

*   **show_progress_bar** (_bool_) – Whether to show a progress bar when computing embeddings. Defaults to False.

*   **batch_size** (_int_) – The batch size to compute sentence embeddings. Defaults to 16.

*   **name** (_str_) – The name of the evaluator. Defaults to an empty string.

*   **print_wrong_matches** (_bool_) – Whether to print incorrect matches. Defaults to False.

*   **write_csv** (_bool_) – Whether to write the evaluation results to a CSV file. Defaults to True.

*   **truncate_dim** (_int_ _,_ _optional_) – The dimension to truncate sentence embeddings to. If None, the model’s current truncation dimension will be used. Defaults to None.

Example

from sentence_transformers import SentenceTransformer
from sentence_transformers.evaluation import TranslationEvaluator
from datasets import load_dataset

# Load a model
model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')

# Load a parallel sentences dataset
dataset = load_dataset("sentence-transformers/parallel-sentences-news-commentary", "en-nl", split="train[:1000]")

# Initialize the TranslationEvaluator using the same texts from two languages
translation_evaluator = TranslationEvaluator(
    source_sentences=dataset["english"],
    target_sentences=dataset["non_english"],
    name="news-commentary-en-nl",
)
results = translation_evaluator(model)
'''
Evaluating translation matching Accuracy of the model on the news-commentary-en-nl dataset:
Accuracy src2trg: 90.80
Accuracy trg2src: 90.40
'''
print(translation_evaluator.primary_metric)
# => "news-commentary-en-nl_mean_accuracy"
print(results[translation_evaluator.primary_metric])
# => 0.906

TripletEvaluator[](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#tripletevaluator "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.evaluation.TripletEvaluator(_anchors:list[str]_, _positives:list[str]_, _negatives:list[str]_, _main\_similarity\_function:str|[SimilarityFunction](https://sbert.net/docs/package\_reference/sparse\_encoder/SparseEncoder.html#sentence\_transformers.SimilarityFunction "sentence\_transformers.similarity\_functions.SimilarityFunction")|None=None_, _margin:float|dict[str,float]|None=None_, _name:str=''_, _batch\_size:int=16_, _show\_progress\_bar:bool=False_, _write\_csv:bool=True_, _truncate\_dim:int|None=None_, _similarity\_fn\_names:list[Literal['cosine','dot','euclidean','manhattan']]|None=None_, _main\_distance\_function:str|[SimilarityFunction](https://sbert.net/docs/package\_reference/sparse\_encoder/SparseEncoder.html#sentence\_transformers.SimilarityFunction "sentence\_transformers.similarity\_functions.SimilarityFunction")|None='deprecated'_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/evaluation/TripletEvaluator.py#L26-L271)[](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.TripletEvaluator "Link to this definition")
Evaluate a model based on a triplet: (sentence, positive_example, negative_example). Checks if `similarity(sentence, positive_example) > similarity(sentence, negative_example) + margin`.

Parameters:
*   **anchors** (_List_ _[_ _str_ _]_) – Sentences to check similarity to. (e.g. a query)

*   **positives** (_List_ _[_ _str_ _]_) – List of positive sentences

*   **negatives** (_List_ _[_ _str_ _]_) – List of negative sentences

*   **main_similarity_function** (_Union_ _[_ _str_ _,_[_SimilarityFunction_](https://sbert.net/docs/package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")_]_ _,_ _optional_) – The similarity function to use. If not specified, use cosine similarity, dot product, Euclidean, and Manhattan similarity. Defaults to None.

*   **margin** (_Union_ _[_ _float_ _,_ _Dict_ _[_ _str_ _,_ _float_ _]_ _]_ _,_ _optional_) – Margins for various similarity metrics. If a float is provided, it will be used as the margin for all similarity metrics. If a dictionary is provided, the keys should be ‘cosine’, ‘dot’, ‘manhattan’, and ‘euclidean’. The value specifies the minimum margin by which the negative sample should be further from the anchor than the positive sample. Defaults to None.

*   **name** (_str_) – Name for the output. Defaults to “”.

*   **batch_size** (_int_) – Batch size used to compute embeddings. Defaults to 16.

*   **show_progress_bar** (_bool_) – If true, prints a progress bar. Defaults to False.

*   **write_csv** (_bool_) – Write results to a CSV file. Defaults to True.

*   **truncate_dim** (_int_ _,_ _optional_) – The dimension to truncate sentence embeddings to. None uses the model’s current truncation dimension. Defaults to None.

*   **similarity_fn_names** (_List_ _[_ _str_ _]_ _,_ _optional_) – List of similarity function names to evaluate. If not specified, evaluate using the `model.similarity_fn_name`. Defaults to None.

Example

from sentence_transformers import SentenceTransformer
from sentence_transformers.evaluation import TripletEvaluator
from datasets import load_dataset

# Load a model
model = SentenceTransformer('all-mpnet-base-v2')

# Load a dataset with (anchor, positive, negative) triplets
dataset = load_dataset("sentence-transformers/all-nli", "triplet", split="dev")

# Initialize the TripletEvaluator using anchors, positives, and negatives
triplet_evaluator = TripletEvaluator(
    anchors=dataset[:1000]["anchor"],
    positives=dataset[:1000]["positive"],
    negatives=dataset[:1000]["negative"],
    name="all_nli_dev",
)
results = triplet_evaluator(model)
'''
TripletEvaluator: Evaluating the model on the all-nli-dev dataset:
Accuracy Cosine Similarity: 95.60%
'''
print(triplet_evaluator.primary_metric)
# => "all_nli_dev_cosine_accuracy"
print(results[triplet_evaluator.primary_metric])
# => 0.956

[Previous](https://sbert.net/docs/package_reference/sentence_transformer/sampler.html "Samplers")[Next](https://sbert.net/docs/package_reference/sentence_transformer/datasets.html "Datasets")

* * *

© Copyright 2026.

 Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org/).
