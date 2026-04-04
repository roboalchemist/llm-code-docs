# Source: https://sbert.net/examples/sentence_transformer/training/hpo/README.html

Title: Hyperparameter Optimization — Sentence Transformers documentation

URL Source: https://sbert.net/examples/sentence_transformer/training/hpo/README.html

Markdown Content:
Hyperparameter Optimization — Sentence Transformers documentation
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

    *   [Hyperparameter Optimization](https://sbert.net/examples/sentence_transformer/training/hpo/README.html#)
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
*   [Training Examples](https://sbert.net/docs/sentence_transformer/training/examples.html)
*   Hyperparameter Optimization
*   [Edit on GitHub](https://github.com/huggingface/sentence-transformers/blob/main/examples/sentence_transformer/training/hpo/README.rst)

* * *

Hyperparameter Optimization[](https://sbert.net/examples/sentence_transformer/training/hpo/README.html#hyperparameter-optimization "Link to this heading")
===========================================================================================================================================================

The [`SentenceTransformerTrainer`](https://sbert.net/docs/package_reference/sentence_transformer/trainer.html#sentence_transformers.trainer.SentenceTransformerTrainer "sentence_transformers.trainer.SentenceTransformerTrainer") supports hyperparameter optimization using `transformers`, which in turn supports four hyperparameter search backends: [optuna](https://optuna.org/), [sigopt](https://sigopt.org/), [raytune](https://docs.ray.io/en/latest/tune/index.html), and [wandb](https://wandb.ai/site/sweeps). You should install your backend of choice before using it:

pip install optuna/sigopt/wandb/ray[tune]

On this page, we’ll show you how to use the hyperparameter optimization feature with the optuna backend. The other backends are similar to use, but you should refer to their respective documentation or the [transformers HPO documentation](https://huggingface.co/docs/transformers/en/hpo_train) for more information.

HPO Components[](https://sbert.net/examples/sentence_transformer/training/hpo/README.html#hpo-components "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------

The hyperparameter optimization process consists of the following components:

[Hyperparameter Search Space Specify ranges for hyperparameter values.](https://sbert.net/examples/sentence_transformer/training/hpo/README.html#hyperparameter-search-space)[Model Initialization Initialize a SentenceTransformer model for a trial.](https://sbert.net/examples/sentence_transformer/training/hpo/README.html#model-initialization)[Loss Initialization Initialize a loss function given a model.](https://sbert.net/examples/sentence_transformer/training/hpo/README.html#loss-initialization)[Compute Objective Determines the value to be minimized or maximized.](https://sbert.net/examples/sentence_transformer/training/hpo/README.html#compute-objective)

### Hyperparameter Search Space[](https://sbert.net/examples/sentence_transformer/training/hpo/README.html#hyperparameter-search-space "Link to this heading")

The hyperparameter search space is defined by a function that returns a dictionary of hyperparameters and their respective search spaces. Here’s an example using `optuna` of a search space function that defines the hyperparameters for a SentenceTransformer model:

def hpo_search_space(trial):
    return {
        "num_train_epochs": trial.suggest_int("num_train_epochs", 1, 2),
        "per_device_train_batch_size": trial.suggest_int("per_device_train_batch_size", 32, 128),
        "warmup_ratio": trial.suggest_float("warmup_ratio", 0, 0.3),
        "learning_rate": trial.suggest_float("learning_rate", 1e-6, 1e-4, log=True),
    }

### Model Initialization[](https://sbert.net/examples/sentence_transformer/training/hpo/README.html#model-initialization "Link to this heading")

The model initialization function is a function that takes the hyperparameters of the current “trial” as input and returns a SentenceTransformer model. Generally, this function is quite simple. Here’s an example of a model initialization function:

def hpo_model_init(trial):
    return SentenceTransformer("distilbert-base-uncased")

### Loss Initialization[](https://sbert.net/examples/sentence_transformer/training/hpo/README.html#loss-initialization "Link to this heading")

The loss initialization function is a function that takes the model initialized for the current trial and returns a loss function. Here’s an example of a loss initialization function:

def hpo_loss_init(model):
    return losses.CosineSimilarityLoss(model)

### Compute Objective[](https://sbert.net/examples/sentence_transformer/training/hpo/README.html#compute-objective "Link to this heading")

The compute objective function is a function that takes the evaluation `metrics` and returns the float value to be minimized or maximized. Here’s an example of a compute objective function:

def hpo_compute_objective(metrics):
    return metrics["eval_sts-dev_spearman_cosine"]

Putting It All Together[](https://sbert.net/examples/sentence_transformer/training/hpo/README.html#putting-it-all-together "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------

You can perform HPO on any regular training loop, the only difference being that you don’t call [`SentenceTransformerTrainer.train`](https://sbert.net/docs/package_reference/sentence_transformer/trainer.html#sentence_transformers.trainer.SentenceTransformerTrainer.train "sentence_transformers.trainer.SentenceTransformerTrainer.train"), but [`SentenceTransformerTrainer.hyperparameter_search`](https://sbert.net/docs/package_reference/sentence_transformer/trainer.html#sentence_transformers.trainer.SentenceTransformerTrainer.hyperparameter_search "sentence_transformers.trainer.SentenceTransformerTrainer.hyperparameter_search") instead. Here’s an example of how to put it all together:

Documentation

1.   [sentence-transformers/all-nli](https://huggingface.co/datasets/sentence-transformers/all-nli)

2.   [`EmbeddingSimilarityEvaluator`](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator "sentence_transformers.evaluation.EmbeddingSimilarityEvaluator")

3.   [Hyperparameter Search Space](https://sbert.net/examples/sentence_transformer/training/hpo/README.html#hyperparameter-search-space)

4.   [Model Initialization](https://sbert.net/examples/sentence_transformer/training/hpo/README.html#model-initialization)

5.   [Loss Initialization](https://sbert.net/examples/sentence_transformer/training/hpo/README.html#loss-initialization)

6.   [Compute Objective](https://sbert.net/examples/sentence_transformer/training/hpo/README.html#compute-objective)

7.   [`SentenceTransformerTrainingArguments`](https://sbert.net/docs/package_reference/sentence_transformer/training_args.html#sentence_transformers.training_args.SentenceTransformerTrainingArguments "sentence_transformers.training_args.SentenceTransformerTrainingArguments")

8.   [`SentenceTransformerTrainer`](https://sbert.net/docs/package_reference/sentence_transformer/trainer.html#sentence_transformers.trainer.SentenceTransformerTrainer "sentence_transformers.trainer.SentenceTransformerTrainer")

9.   [`hyperparameter_search()`](https://sbert.net/docs/package_reference/sentence_transformer/trainer.html#sentence_transformers.trainer.SentenceTransformerTrainer.hyperparameter_search "sentence_transformers.trainer.SentenceTransformerTrainer.hyperparameter_search")

from sentence_transformers import losses
from sentence_transformers import SentenceTransformer, SentenceTransformerTrainer, SentenceTransformerTrainingArguments
from sentence_transformers.evaluation import EmbeddingSimilarityEvaluator, SimilarityFunction
from sentence_transformers.training_args import BatchSamplers
from datasets import load_dataset

# 1. Load the AllNLI dataset: https://huggingface.co/datasets/sentence-transformers/all-nli, only 10k train and 1k dev
train_dataset = load_dataset("sentence-transformers/all-nli", "triplet", split="train[:10000]")
eval_dataset = load_dataset("sentence-transformers/all-nli", "triplet", split="dev[:1000]")

# 2. Create an evaluator to perform useful HPO
stsb_eval_dataset = load_dataset("sentence-transformers/stsb", split="validation")
dev_evaluator = EmbeddingSimilarityEvaluator(
    sentences1=stsb_eval_dataset["sentence1"],
    sentences2=stsb_eval_dataset["sentence2"],
    scores=stsb_eval_dataset["score"],
    main_similarity=SimilarityFunction.COSINE,
    name="sts-dev",
)

# 3. Define the Hyperparameter Search Space
def hpo_search_space(trial):
    return {
        "num_train_epochs": trial.suggest_int("num_train_epochs", 1, 2),
        "per_device_train_batch_size": trial.suggest_int("per_device_train_batch_size", 32, 128),
        "warmup_ratio": trial.suggest_float("warmup_ratio", 0, 0.3),
        "learning_rate": trial.suggest_float("learning_rate", 1e-6, 1e-4, log=True),
    }

# 4. Define the Model Initialization
def hpo_model_init(trial):
    return SentenceTransformer("distilbert-base-uncased")

# 5. Define the Loss Initialization
def hpo_loss_init(model):
    return losses.MultipleNegativesRankingLoss(model)

# 6. Define the Objective Function
def hpo_compute_objective(metrics):
 """
 Valid keys are: 'eval_loss', 'eval_sts-dev_pearson_cosine', 'eval_sts-dev_spearman_cosine',
 'eval_sts-dev_pearson_manhattan', 'eval_sts-dev_spearman_manhattan', 'eval_sts-dev_pearson_euclidean',
 'eval_sts-dev_spearman_euclidean', 'eval_sts-dev_pearson_dot', 'eval_sts-dev_spearman_dot',
 'eval_sts-dev_pearson_max', 'eval_sts-dev_spearman_max', 'eval_runtime', 'eval_samples_per_second',
 'eval_steps_per_second', 'epoch'

 due to the evaluator that we're using.
 """
    return metrics["eval_sts-dev_spearman_cosine"]

# 7. Define the training arguments
args = SentenceTransformerTrainingArguments(
    # Required parameter:
    output_dir="checkpoints",
    # Optional training parameters:
    # max_steps=10000, # We might want to limit the number of steps for HPO
    fp16=True,  # Set to False if you get an error that your GPU can't run on FP16
    bf16=False,  # Set to True if you have a GPU that supports BF16
    batch_sampler=BatchSamplers.NO_DUPLICATES,  # MultipleNegativesRankingLoss benefits from no duplicate samples in a batch
    # Optional tracking/debugging parameters:
    eval_strategy="no", # We don't need to evaluate/save during HPO
    save_strategy="no",
    logging_steps=10,
    run_name="hpo",  # Will be used in W&B if `wandb` is installed
)

# 8. Create the trainer with model_init rather than model
trainer = SentenceTransformerTrainer(
    model=None,
    args=args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    evaluator=dev_evaluator,
    model_init=hpo_model_init,
    loss=hpo_loss_init,
)

# 9. Perform the HPO
best_trial = trainer.hyperparameter_search(
    hp_space=hpo_search_space,
    compute_objective=hpo_compute_objective,
    n_trials=20,
    direction="maximize",
    backend="optuna",
)
print(best_trial)

[I 2024-05-17 15:10:47,844] Trial 0 finished with value: 0.7889856589698055 and parameters: {'num_train_epochs': 1, 'per_device_train_batch_size': 123, 'warmup_ratio': 0.07380948785410107, 'learning_rate': 2.686331417509812e-06}. Best is trial 0 with value: 0.7889856589698055.
[I 2024-05-17 15:12:13,283] Trial 1 finished with value: 0.7927780672090986 and parameters: {'num_train_epochs': 2, 'per_device_train_batch_size': 69, 'warmup_ratio': 0.2927897848007451, 'learning_rate': 5.885372118095137e-06}. Best is trial 1 with value: 0.7927780672090986.
[I 2024-05-17 15:12:43,896] Trial 2 finished with value: 0.7684829743509601 and parameters: {'num_train_epochs': 1, 'per_device_train_batch_size': 114, 'warmup_ratio': 0.0739429232666916, 'learning_rate': 7.344415188959276e-05}. Best is trial 1 with value: 0.7927780672090986.
[I 2024-05-17 15:14:49,730] Trial 3 finished with value: 0.7873032743147989 and parameters: {'num_train_epochs': 2, 'per_device_train_batch_size': 43, 'warmup_ratio': 0.15184370143796674, 'learning_rate': 9.703232080395476e-06}. Best is trial 1 with value: 0.7927780672090986.
[I 2024-05-17 15:15:39,597] Trial 4 finished with value: 0.7759251781929949 and parameters: {'num_train_epochs': 2, 'per_device_train_batch_size': 127, 'warmup_ratio': 0.263946220093495, 'learning_rate': 1.231454337152625e-06}. Best is trial 1 with value: 0.7927780672090986.
[I 2024-05-17 15:17:02,191] Trial 5 finished with value: 0.7964580509886684 and parameters: {'num_train_epochs': 1, 'per_device_train_batch_size': 34, 'warmup_ratio': 0.2276865359631089, 'learning_rate': 7.889007438884571e-06}. Best is trial 5 with value: 0.7964580509886684.
[I 2024-05-17 15:18:55,559] Trial 6 finished with value: 0.7901878917859169 and parameters: {'num_train_epochs': 2, 'per_device_train_batch_size': 48, 'warmup_ratio': 0.23228838664572948, 'learning_rate': 2.883013292682523e-06}. Best is trial 5 with value: 0.7964580509886684.
[I 2024-05-17 15:20:27,027] Trial 7 finished with value: 0.7935671067660925 and parameters: {'num_train_epochs': 2, 'per_device_train_batch_size': 62, 'warmup_ratio': 0.22061123927198237, 'learning_rate': 2.95413457610349e-06}. Best is trial 5 with value: 0.7964580509886684.
[I 2024-05-17 15:22:23,147] Trial 8 finished with value: 0.7848123114933252 and parameters: {'num_train_epochs': 2, 'per_device_train_batch_size': 45, 'warmup_ratio': 0.23071701022961139, 'learning_rate': 9.793681667449783e-06}. Best is trial 5 with value: 0.7964580509886684.
[I 2024-05-17 15:22:52,826] Trial 9 finished with value: 0.7909708416168918 and parameters: {'num_train_epochs': 1, 'per_device_train_batch_size': 121, 'warmup_ratio': 0.22440506724181647, 'learning_rate': 4.0744671365843346e-05}. Best is trial 5 with value: 0.7964580509886684.
[I 2024-05-17 15:23:30,395] Trial 10 finished with value: 0.7928991732385567 and parameters: {'num_train_epochs': 1, 'per_device_train_batch_size': 89, 'warmup_ratio': 0.14607293301068847, 'learning_rate': 2.5557492055039498e-05}. Best is trial 5 with value: 0.7964580509886684.
[I 2024-05-17 15:24:18,024] Trial 11 finished with value: 0.7991870087507459 and parameters: {'num_train_epochs': 1, 'per_device_train_batch_size': 66, 'warmup_ratio': 0.16886154348739527, 'learning_rate': 3.705926066938032e-06}. Best is trial 11 with value: 0.7991870087507459.
[I 2024-05-17 15:25:44,198] Trial 12 finished with value: 0.7923304174306207 and parameters: {'num_train_epochs': 1, 'per_device_train_batch_size': 33, 'warmup_ratio': 0.15953772535423974, 'learning_rate': 1.8076298025704224e-05}. Best is trial 11 with value: 0.7991870087507459.
[I 2024-05-17 15:26:20,739] Trial 13 finished with value: 0.8020260244040395 and parameters: {'num_train_epochs': 1, 'per_device_train_batch_size': 90, 'warmup_ratio': 0.18105202625281253, 'learning_rate': 5.513908793512551e-06}. Best is trial 13 with value: 0.8020260244040395.
[I 2024-05-17 15:26:57,783] Trial 14 finished with value: 0.7571110256860063 and parameters: {'num_train_epochs': 1, 'per_device_train_batch_size': 95, 'warmup_ratio': 0.00122391151793258, 'learning_rate': 1.0432486633629492e-06}. Best is trial 13 with value: 0.8020260244040395.
[I 2024-05-17 15:27:32,581] Trial 15 finished with value: 0.8009013936824717 and parameters: {'num_train_epochs': 1, 'per_device_train_batch_size': 101, 'warmup_ratio': 0.1761274711346081, 'learning_rate': 4.5918293464430035e-06}. Best is trial 13 with value: 0.8020260244040395.
[I 2024-05-17 15:28:05,850] Trial 16 finished with value: 0.8017668050806169 and parameters: {'num_train_epochs': 1, 'per_device_train_batch_size': 103, 'warmup_ratio': 0.10766501647726355, 'learning_rate': 5.0309795522333e-06}. Best is trial 13 with value: 0.8020260244040395.
[I 2024-05-17 15:28:37,393] Trial 17 finished with value: 0.7769412380909586 and parameters: {'num_train_epochs': 1, 'per_device_train_batch_size': 108, 'warmup_ratio': 0.1036610178950246, 'learning_rate': 1.7747598626081271e-06}. Best is trial 13 with value: 0.8020260244040395.
[I 2024-05-17 15:29:19,340] Trial 18 finished with value: 0.8011921300048339 and parameters: {'num_train_epochs': 1, 'per_device_train_batch_size': 80, 'warmup_ratio': 0.117014165550441, 'learning_rate': 1.238558867958792e-05}. Best is trial 13 with value: 0.8020260244040395.
[I 2024-05-17 15:29:59,508] Trial 19 finished with value: 0.8027501854704168 and parameters: {'num_train_epochs': 1, 'per_device_train_batch_size': 84, 'warmup_ratio': 0.014601112207929548, 'learning_rate': 5.627813947769514e-06}. Best is trial 19 with value: 0.8027501854704168.

BestRun(run_id='19', objective=0.8027501854704168, hyperparameters={'num_train_epochs': 1, 'per_device_train_batch_size': 84, 'warmup_ratio': 0.014601112207929548, 'learning_rate': 5.627813947769514e-06}, run_summary=None)

As you can see, the strongest hyperparameters reached **0.802** Spearman correlation on the STS (dev) benchmark. For context, training with the default training arguments (`per_device_train_batch_size=8`, `learning_rate=5e-5`) results in **0.736**, and hyperparameters chosen based on experience (`per_device_train_batch_size=64`, `learning_rate=2e-5`) results in **0.783** Spearman correlation. Consequently, HPO proved quite effective here in improving the model performance.

Example Scripts[](https://sbert.net/examples/sentence_transformer/training/hpo/README.html#example-scripts "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------

*   [hpo_nli.py](https://github.com/huggingface/sentence-transformers/blob/main/examples/sentence_transformer/training/hpo/hpo_nli.py) - An example script that performs hyperparameter optimization on the AllNLI dataset.

[Previous](https://sbert.net/examples/sentence_transformer/domain_adaptation/README.html "Domain Adaptation")[Next](https://sbert.net/docs/sentence_transformer/training/distributed.html "Distributed Training")

* * *

© Copyright 2026.

 Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org/).
