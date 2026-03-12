# Source: https://sbert.net/docs/sentence_transformer/usage/efficiency.html

Title: Speeding up Inference — Sentence Transformers documentation

URL Source: https://sbert.net/docs/sentence_transformer/usage/efficiency.html

Markdown Content:
Speeding up Inference — Sentence Transformers documentation
===============

[![Image 3: Logo](https://sbert.net/_static/logo.png)](https://sbert.net/index.html)

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

    *   [Speeding up Inference](https://sbert.net/docs/sentence_transformer/usage/efficiency.html#)
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
*   [Usage](https://sbert.net/docs/sentence_transformer/usage/usage.html)
*   Speeding up Inference
*   [Edit on GitHub](https://github.com/huggingface/sentence-transformers/blob/main/docs/sentence_transformer/usage/efficiency.rst)

* * *

Speeding up Inference[](https://sbert.net/docs/sentence_transformer/usage/efficiency.html#speeding-up-inference "Link to this heading")
========================================================================================================================================

Sentence Transformers supports 3 backends for computing embeddings, each with its own optimizations for speeding up inference:

[PyTorch The default backend for Sentence Transformers.](https://sbert.net/docs/sentence_transformer/usage/efficiency.html#pytorch)[ONNX Flexible and efficient model accelerator.](https://sbert.net/docs/sentence_transformer/usage/efficiency.html#onnx)[OpenVINO Optimization of models, mainly for Intel Hardware.](https://sbert.net/docs/sentence_transformer/usage/efficiency.html#openvino)[Benchmarks Benchmarks for the different backends.](https://sbert.net/docs/sentence_transformer/usage/efficiency.html#benchmarks)[User Interface GUI to export, optimize, and quantize models.](https://sbert.net/docs/sentence_transformer/usage/efficiency.html#user-interface)

PyTorch[](https://sbert.net/docs/sentence_transformer/usage/efficiency.html#pytorch "Link to this heading")
------------------------------------------------------------------------------------------------------------

The PyTorch backend is the default backend for Sentence Transformers. If you don’t specify a device, it will use the strongest available option across “cuda”, “mps”, and “cpu”. Its default usage looks like this:

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = ["This is an example sentence", "Each sentence is converted"]
embeddings = model.encode(sentences)

If you’re using a GPU, then you can use the following options to speed up your inference:

float16 (fp16) 

Float32 (fp32, full precision) is the default floating-point format in `torch`, whereas float16 (fp16, half precision) is a reduced-precision floating-point format that can speed up inference on GPUs at a minimal loss of model accuracy. To use it, you can specify the `torch_dtype` during initialization or call [`model.half()`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.half.html#torch.Tensor.half "(in PyTorch v2.10)") on the initialized model:

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2", model_kwargs={"torch_dtype": "float16"})
# or: model.half()

sentences = ["This is an example sentence", "Each sentence is converted"]
embeddings = model.encode(sentences)

bfloat16 (bf16) 

Bfloat16 (bf16) is similar to fp16, but preserves more of the original accuracy of fp32. To use it, you can specify the `torch_dtype` during initialization or call [`model.bfloat16()`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.bfloat16.html#torch.Tensor.bfloat16 "(in PyTorch v2.10)") on the initialized model:

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2", model_kwargs={"torch_dtype": "bfloat16"})
# or: model.bfloat16()

sentences = ["This is an example sentence", "Each sentence is converted"]
embeddings = model.encode(sentences)

ONNX[](https://sbert.net/docs/sentence_transformer/usage/efficiency.html#onnx "Link to this heading")
------------------------------------------------------------------------------------------------------

Export, Optimize, and Quantize Hugging Face models

This Hugging Face Space provides a user interface for exporting, optimizing, and quantizing models for either ONNX or OpenVINO:

*   [sentence-transformers/backend-export](https://huggingface.co/spaces/sentence-transformers/backend-export)

ONNX can be used to speed up inference by converting the model to ONNX format and using ONNX Runtime to run the model. To use the ONNX backend, you must install Sentence Transformers with the `onnx` or `onnx-gpu` extra for CPU or GPU acceleration, respectively:

pip install sentence-transformers[onnx-gpu]
# or
pip install sentence-transformers[onnx]

To convert a model to ONNX format, you can use the following code:

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2", backend="onnx")

sentences = ["This is an example sentence", "Each sentence is converted"]
embeddings = model.encode(sentences)

If the model path or repository already contains a model in ONNX format, Sentence Transformers will automatically use it. Otherwise, it will convert the model to the ONNX format.

Note

If you wish to use the ONNX model outside of Sentence Transformers, you’ll need to perform pooling and/or normalization yourself. The ONNX export only converts the Transformer component, which outputs token embeddings, not sentence embeddings. To get sentence embeddings, you’ll need to apply the appropriate pooling strategy (like mean pooling) and any normalization that the original model uses.

All keyword arguments passed via `model_kwargs` will be passed on to `ORTModel.from_pretrained`. Some notable arguments include:

*   `provider`: ONNX Runtime provider to use for loading the model, e.g. `"CPUExecutionProvider"` . See [https://onnxruntime.ai/docs/execution-providers/](https://onnxruntime.ai/docs/execution-providers/) for possible providers. If not specified, the strongest provider (E.g. `"CUDAExecutionProvider"`) will be used.

*   `file_name`: The name of the ONNX file to load. If not specified, will default to `"model.onnx"` or otherwise `"onnx/model.onnx"`. This argument is useful for specifying optimized or quantized models.

*   `export`: A boolean flag specifying whether the model will be exported. If not provided, `export` will be set to `True` if the model repository or directory does not already contain an ONNX model.

Tip

It’s heavily recommended to save the exported model to prevent having to re-export it every time you run your code. You can do this by calling [`model.save_pretrained()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.save_pretrained "sentence_transformers.SentenceTransformer.save_pretrained") if your model was local:

model = SentenceTransformer("path/to/my/model", backend="onnx")
model.save_pretrained("path/to/my/model")

or with [`model.push_to_hub()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.push_to_hub "sentence_transformers.SentenceTransformer.push_to_hub") if your model was from the Hugging Face Hub:

model = SentenceTransformer("intfloat/multilingual-e5-small", backend="onnx")
model.push_to_hub("intfloat/multilingual-e5-small", create_pr=True)

### Optimizing ONNX Models[](https://sbert.net/docs/sentence_transformer/usage/efficiency.html#optimizing-onnx-models "Link to this heading")

Export, Optimize, and Quantize Hugging Face models

This Hugging Face Space provides a user interface for exporting, optimizing, and quantizing models for either ONNX or OpenVINO:

*   [sentence-transformers/backend-export](https://huggingface.co/spaces/sentence-transformers/backend-export)

ONNX models can be optimized using [Optimum](https://huggingface.co/docs/optimum/index), allowing for speedups on CPUs and GPUs alike. To do this, you can use the [`export_optimized_onnx_model()`](https://sbert.net/docs/package_reference/util.html#sentence_transformers.backend.export_optimized_onnx_model "sentence_transformers.backend.export_optimized_onnx_model") function, which saves the optimized in a directory or model repository that you specify. It expects:

*   `model`: a Sentence Transformer, Sparse Encoder, or Cross Encoder model loaded with the ONNX backend.

*   `optimization_config`: `"O1"`, `"O2"`, `"O3"`, or `"O4"` representing optimization levels from `AutoOptimizationConfig`, or an `OptimizationConfig` instance.

*   `model_name_or_path`: a path to save the optimized model file, or the repository name if you want to push it to the Hugging Face Hub.

*   `push_to_hub`: (Optional) a boolean to push the optimized model to the Hugging Face Hub.

*   `create_pr`: (Optional) a boolean to create a pull request when pushing to the Hugging Face Hub. Useful when you don’t have write access to the repository.

*   `file_suffix`: (Optional) a string to append to the model name when saving it. If not specified, the optimization level name string will be used, or just `"optimized"` if the optimization config was not just a string optimization level.

See this example for exporting a model with optimization level 3 (basic and extended general optimizations, transformers-specific fusions, fast Gelu approximation):

Hugging Face Hub Model 

Only optimize once:

from sentence_transformers import SentenceTransformer, export_optimized_onnx_model

model = SentenceTransformer("all-MiniLM-L6-v2", backend="onnx")
export_optimized_onnx_model(
    model=model,
    optimization_config="O3",
    model_name_or_path="sentence-transformers/all-MiniLM-L6-v2",
    push_to_hub=True,
    create_pr=True,
)

Before the pull request gets merged:

from sentence_transformers import SentenceTransformer

pull_request_nr = 2 # TODO: Update this to the number of your pull request
model = SentenceTransformer(
    "all-MiniLM-L6-v2",
    backend="onnx",
    model_kwargs={"file_name": "onnx/model_O3.onnx"},
    revision=f"refs/pr/{pull_request_nr}"
)

Once the pull request gets merged:

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2",
    backend="onnx",
    model_kwargs={"file_name": "onnx/model_O3.onnx"},
)

Local Model 

Only optimize once:

from sentence_transformers import SentenceTransformer, export_optimized_onnx_model

model = SentenceTransformer("path/to/my/mpnet-legal-finetuned", backend="onnx")
export_optimized_onnx_model(
    model=model, optimization_config="O3", model_name_or_path="path/to/my/mpnet-legal-finetuned"
)

After optimizing:

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "path/to/my/mpnet-legal-finetuned",
    backend="onnx",
    model_kwargs={"file_name": "onnx/model_O3.onnx"},
)

### Quantizing ONNX Models[](https://sbert.net/docs/sentence_transformer/usage/efficiency.html#quantizing-onnx-models "Link to this heading")

Export, Optimize, and Quantize Hugging Face models

This Hugging Face Space provides a user interface for exporting, optimizing, and quantizing models for either ONNX or OpenVINO:

*   [sentence-transformers/backend-export](https://huggingface.co/spaces/sentence-transformers/backend-export)

ONNX models can be quantized to int8 precision using [Optimum](https://huggingface.co/docs/optimum/index), allowing for faster inference on CPUs. To do this, you can use the [`export_dynamic_quantized_onnx_model()`](https://sbert.net/docs/package_reference/util.html#sentence_transformers.backend.export_dynamic_quantized_onnx_model "sentence_transformers.backend.export_dynamic_quantized_onnx_model") function, which saves the quantized in a directory or model repository that you specify. Dynamic quantization, unlike static quantization, does not require a calibration dataset. It expects:

*   `model`: a Sentence Transformer, Sparse Encoder, or Cross Encoder model loaded with the ONNX backend.

*   `quantization_config`: `"arm64"`, `"avx2"`, `"avx512"`, or `"avx512_vnni"` representing quantization configurations from `AutoQuantizationConfig`, or an `QuantizationConfig` instance.

*   `model_name_or_path`: a path to save the quantized model file, or the repository name if you want to push it to the Hugging Face Hub.

*   `push_to_hub`: (Optional) a boolean to push the quantized model to the Hugging Face Hub.

*   `create_pr`: (Optional) a boolean to create a pull request when pushing to the Hugging Face Hub. Useful when you don’t have write access to the repository.

*   `file_suffix`: (Optional) a string to append to the model name when saving it. If not specified, `"qint8_quantized"` will be used.

On my CPU, each of the default quantization configurations (`"arm64"`, `"avx2"`, `"avx512"`, `"avx512_vnni"`) resulted in roughly equivalent speedups.

See this example for quantizing a model to `int8` with avx512_vnni:

Hugging Face Hub Model 

Only quantize once:

from sentence_transformers import SentenceTransformer, export_dynamic_quantized_onnx_model

model = SentenceTransformer("all-MiniLM-L6-v2", backend="onnx")
export_dynamic_quantized_onnx_model(
    model=model,
    quantization_config="avx512_vnni",
    model_name_or_path="sentence-transformers/all-MiniLM-L6-v2",
    push_to_hub=True,
    create_pr=True,
)

Before the pull request gets merged:

from sentence_transformers import SentenceTransformer

pull_request_nr = 2 # TODO: Update this to the number of your pull request
model = SentenceTransformer(
    "all-MiniLM-L6-v2",
    backend="onnx",
    model_kwargs={"file_name": "onnx/model_qint8_avx512_vnni.onnx"},
    revision=f"refs/pr/{pull_request_nr}",
)

Once the pull request gets merged:

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2",
    backend="onnx",
    model_kwargs={"file_name": "onnx/model_qint8_avx512_vnni.onnx"},
)

Local Model 

Only quantize once:

from sentence_transformers import SentenceTransformer, export_dynamic_quantized_onnx_model

model = SentenceTransformer("path/to/my/mpnet-legal-finetuned", backend="onnx")
export_dynamic_quantized_onnx_model(
    model=model, quantization_config="avx512_vnni", model_name_or_path="path/to/my/mpnet-legal-finetuned"
)

After quantizing:

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "path/to/my/mpnet-legal-finetuned",
    backend="onnx",
    model_kwargs={"file_name": "onnx/model_qint8_avx512_vnni.onnx"},
)

OpenVINO[](https://sbert.net/docs/sentence_transformer/usage/efficiency.html#openvino "Link to this heading")
--------------------------------------------------------------------------------------------------------------

Export, Optimize, and Quantize Hugging Face models

This Hugging Face Space provides a user interface for exporting, optimizing, and quantizing models for either ONNX or OpenVINO:

*   [sentence-transformers/backend-export](https://huggingface.co/spaces/sentence-transformers/backend-export)

OpenVINO allows for accelerated inference on CPUs by exporting the model to the OpenVINO format. To use the OpenVINO backend, you must install Sentence Transformers with the `openvino` extra:

pip install sentence-transformers[openvino]

To convert a model to OpenVINO format, you can use the following code:

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2", backend="openvino")

sentences = ["This is an example sentence", "Each sentence is converted"]
embeddings = model.encode(sentences)

If the model path or repository already contains a model in OpenVINO format, Sentence Transformers will automatically use it. Otherwise, it will convert the model to the OpenVINO format.

Note

If you wish to use the OpenVINO model outside of Sentence Transformers, you’ll need to perform pooling and/or normalization yourself. The OpenVINO export only converts the Transformer component, which outputs token embeddings, not sentence embeddings. To get sentence embeddings, you’ll need to apply the appropriate pooling strategy (like mean pooling) and any normalization that the original model uses.

 All keyword arguments passed via `model_kwargs` will be passed on to [`OVBaseModel.from_pretrained()`](https://huggingface.co/docs/optimum/intel/openvino/reference#optimum.intel.openvino.modeling_base.OVBaseModel.from_pretrained). Some notable arguments include:
*   `file_name`: The name of the ONNX file to load. If not specified, will default to `"openvino_model.xml"` or otherwise `"openvino/openvino_model.xml"`. This argument is useful for specifying optimized or quantized models.

*   `export`: A boolean flag specifying whether the model will be exported. If not provided, `export` will be set to `True` if the model repository or directory does not already contain an OpenVINO model.

Tip

It’s heavily recommended to save the exported model to prevent having to re-export it every time you run your code. You can do this by calling [`model.save_pretrained()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.save_pretrained "sentence_transformers.SentenceTransformer.save_pretrained") if your model was local:

model = SentenceTransformer("path/to/my/model", backend="openvino")
model.save_pretrained("path/to/my/model")

or with [`model.push_to_hub()`](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.push_to_hub "sentence_transformers.SentenceTransformer.push_to_hub") if your model was from the Hugging Face Hub:

model = SentenceTransformer("intfloat/multilingual-e5-small", backend="openvino")
model.push_to_hub("intfloat/multilingual-e5-small", create_pr=True)

### Quantizing OpenVINO Models[](https://sbert.net/docs/sentence_transformer/usage/efficiency.html#quantizing-openvino-models "Link to this heading")

Export, Optimize, and Quantize Hugging Face models

This Hugging Face Space provides a user interface for exporting, optimizing, and quantizing models for either ONNX or OpenVINO:

*   [sentence-transformers/backend-export](https://huggingface.co/spaces/sentence-transformers/backend-export)

OpenVINO models can be quantized to int8 precision using [Optimum Intel](https://huggingface.co/docs/optimum/main/en/intel/index) to speed up inference. To do this, you can use the [`export_static_quantized_openvino_model()`](https://sbert.net/docs/package_reference/util.html#sentence_transformers.backend.export_static_quantized_openvino_model "sentence_transformers.backend.export_static_quantized_openvino_model") function, which saves the quantized model in a directory or model repository that you specify. Post-Training Static Quantization expects:

*   `model`: a Sentence Transformer, Sparse Encoder, or Cross Encoder model loaded with the OpenVINO backend.

*   `quantization_config`: (Optional) The quantization configuration. This parameter accepts either: `None` for the default 8-bit quantization, a dictionary representing quantization configurations, or an `OVQuantizationConfig` instance.

*   `model_name_or_path`: a path to save the quantized model file, or the repository name if you want to push it to the Hugging Face Hub.

*   `dataset_name`: (Optional) The name of the dataset to load for calibration. If not specified, defaults to `sst2` subset from the `glue` dataset.

*   `dataset_config_name`: (Optional) The specific configuration of the dataset to load.

*   `dataset_split`: (Optional) The split of the dataset to load (e.g., ‘train’, ‘test’).

*   `column_name`: (Optional) The column name in the dataset to use for calibration.

*   `push_to_hub`: (Optional) a boolean to push the quantized model to the Hugging Face Hub.

*   `create_pr`: (Optional) a boolean to create a pull request when pushing to the Hugging Face Hub. Useful when you don’t have write access to the repository.

*   `file_suffix`: (Optional) a string to append to the model name when saving it. If not specified, `"qint8_quantized"` will be used.

See this example for quantizing a model to `int8` with [static quantization](https://huggingface.co/docs/optimum/main/en/intel/openvino/optimization#static-quantization):

Hugging Face Hub Model 

Only quantize once:

from sentence_transformers import SentenceTransformer, export_static_quantized_openvino_model

model = SentenceTransformer("all-MiniLM-L6-v2", backend="openvino")
export_static_quantized_openvino_model(
    model=model,
    quantization_config=None,
    model_name_or_path="sentence-transformers/all-MiniLM-L6-v2",
    push_to_hub=True,
    create_pr=True,
)

Before the pull request gets merged:

from sentence_transformers import SentenceTransformer

pull_request_nr = 2 # TODO: Update this to the number of your pull request
model = SentenceTransformer(
    "all-MiniLM-L6-v2",
    backend="openvino",
    model_kwargs={"file_name": "openvino/openvino_model_qint8_quantized.xml"},
    revision=f"refs/pr/{pull_request_nr}"
)

Once the pull request gets merged:

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2",
    backend="openvino",
    model_kwargs={"file_name": "openvino/openvino_model_qint8_quantized.xml"},
)

Local Model 

Only quantize once:

from sentence_transformers import SentenceTransformer, export_static_quantized_openvino_model
from optimum.intel import OVQuantizationConfig

model = SentenceTransformer("path/to/my/mpnet-legal-finetuned", backend="openvino")
quantization_config = OVQuantizationConfig()
export_static_quantized_openvino_model(
    model=model, quantization_config=quantization_config, model_name_or_path="path/to/my/mpnet-legal-finetuned"
)

After quantizing:

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "path/to/my/mpnet-legal-finetuned",
    backend="openvino",
    model_kwargs={"file_name": "openvino/openvino_model_qint8_quantized.xml"},
)

Benchmarks[](https://sbert.net/docs/sentence_transformer/usage/efficiency.html#benchmarks "Link to this heading")
------------------------------------------------------------------------------------------------------------------

The following images show the benchmark results for the different backends on GPUs and CPUs. The results are averaged across 4 models of various sizes, 3 datasets, and numerous batch sizes.

Expand the benchmark details

 Speedup ratio: 
*   **Hardware:**RTX 3090 GPU, i7-17300K CPU 
*   **Datasets:** 2000 samples for GPU tests, 1000 samples for CPU tests. 
    *   [sentence-transformers/stsb](https://huggingface.co/datasets/sentence-transformers/stsb): 38.9 characters on average (SD=13.9) 
    *   [sentence-transformers/natural-questions](https://huggingface.co/datasets/sentence-transformers/natural-questions): answers only, 619.6 characters on average (SD=345.3) 
    *   [stanfordnlp/imdb](https://huggingface.co/datasets/stanfordnlp/imdb): texts repeated 4 times, 9589.3 characters on average (SD=633.4) 

*   **Models:**
    *   [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2): 22.7M parameters; batch sizes of 16, 32, 64, 128 and 256. 
    *   [BAAI/bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5): 109M parameters; batch sizes of 16, 32, 64, and 128. 
    *   [mixedbread-ai/mxbai-embed-large-v1](https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1): 335M parameters; batch sizes of 8, 16, 32, and 64. Also 128 and 256 for GPU tests. 
    *   [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3): 567M parameters; batch sizes of 2, 4. Also 8, 16, and 32 for GPU tests. 

 Performance ratio: The same models and hardware was used. We compare the performance against the performance of PyTorch with fp32, i.e. the default backend and precision. 
*   **Evaluation:**
    *   **Semantic Textual Similarity:**Spearman rank correlation based on cosine similarity on the [sentence-transformers/stsb](https://huggingface.co/datasets/sentence-transformers/stsb) test set, computed via the EmbeddingSimilarityEvaluator. 
    *   **Information Retrieval:**NDCG@10 based on cosine similarity on the entire [NanoBEIR](https://huggingface.co/collections/zeta-alpha-ai/nanobeir-66e1a0af21dfd93e620cd9f6) collection of datasets, computed via the InformationRetrievalEvaluator. 

*   **Backends:**
    *   `torch-fp32`: PyTorch with float32 precision (default). 
    *   `torch-fp16`: PyTorch with float16 precision, via `model_kwargs={"torch_dtype": "float16"}`. 
    *   `torch-bf16`: PyTorch with bfloat16 precision, via `model_kwargs={"torch_dtype": "bfloat16"}`. 
    *   `onnx`: ONNX with float32 precision, via `backend="onnx"`. 
    *   `onnx-O1`: ONNX with float32 precision and O1 optimization, via `export_optimized_onnx_model(..., optimization_config="O1", ...)` and `backend="onnx"`. 
    *   `onnx-O2`: ONNX with float32 precision and O2 optimization, via `export_optimized_onnx_model(..., optimization_config="O2", ...)` and `backend="onnx"`. 
    *   `onnx-O3`: ONNX with float32 precision and O3 optimization, via `export_optimized_onnx_model(..., optimization_config="O3", ...)` and `backend="onnx"`. 
    *   `onnx-O4`: ONNX with float16 precision and O4 optimization, via `export_optimized_onnx_model(..., optimization_config="O4", ...)` and `backend="onnx"`. 
    *   `onnx-qint8`: ONNX quantized to int8 with "avx512_vnni", via `export_dynamic_quantized_onnx_model(..., quantization_config="avx512_vnni", ...)` and `backend="onnx"`. The different quantization configurations resulted in roughly equivalent speedups. 
    *   `openvino`: OpenVINO, via `backend="openvino"`. 
    *   `openvino-qint8`: OpenVINO quantized to int8 via `export_static_quantized_openvino_model(..., quantization_config=OVQuantizationConfig(), ...)` and `backend="openvino"`. 

 Note that the aggressive averaging across models, datasets, and batch sizes prevents some more intricate patterns from being visible. For example, for GPUs, if we only consider the stsb dataset with the shortest texts, ONNX becomes better: 1.46x for ONNX, and ONNX-O4 reaches 1.83x whereas fp16 and bf16 reach 1.54x and 1.53x respectively. So, for shorter texts we recommend ONNX on GPU.

 For CPU, ONNX is also stronger for the stsb dataset with the shortest texts: 1.39x for ONNX, outperforming 1.29x for OpenVINO. ONNX with int8 quantization is even stronger with a 3.08x speedup. For longer texts, ONNX and OpenVINO can even perform slightly worse than PyTorch, so we recommend testing the different backends with your specific model and data to find the best one for your use case. 

[![Image 4: Benchmark for GPUs](https://sbert.net/_images/backends_benchmark_gpu.png)](https://sbert.net/_images/backends_benchmark_gpu.png)[![Image 5: Benchmark for CPUs](https://sbert.net/_images/backends_benchmark_cpu.png)](https://sbert.net/_images/backends_benchmark_cpu.png)
### Recommendations[](https://sbert.net/docs/sentence_transformer/usage/efficiency.html#recommendations "Link to this heading")

Based on the benchmarks, this flowchart should help you decide which backend to use for your model:

        %%{init: {
   "theme": "neutral",
   "flowchart": {
      "curve": "bumpY"
   }
}}%%
graph TD
A(What is your hardware?) -->|GPU| B(Is your text usually smaller<br>than 500 characters?)
A -->|CPU| C(Is a 0.4% accuracy loss<br>acceptable?)
B -->|yes| D[onnx-O4]
B -->|no| F[float16]
C -->|yes| G[openvino-qint8]
C -->|no| H(Do you have an Intel CPU?)
H -->|yes| I[openvino]
H -->|no| J[onnx]
click D "#optimizing-onnx-models"
click F "#pytorch"
click G "#quantizing-openvino-models"
click I "#openvino"
click J "#onnx"
    

Note

Your milage may vary, and you should always test the different backends with your specific model and data to find the best one for your use case.

### User Interface[](https://sbert.net/docs/sentence_transformer/usage/efficiency.html#user-interface "Link to this heading")

This Hugging Face Space provides a user interface for exporting, optimizing, and quantizing models for either ONNX or OpenVINO:

*   [sentence-transformers/backend-export](https://huggingface.co/spaces/sentence-transformers/backend-export)

[Previous](https://sbert.net/docs/sentence_transformer/usage/mteb_evaluation.html "Evaluation with MTEB")[Next](https://sbert.net/docs/sentence_transformer/pretrained_models.html "Pretrained Models")

* * *

© Copyright 2026.

 Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org/).
