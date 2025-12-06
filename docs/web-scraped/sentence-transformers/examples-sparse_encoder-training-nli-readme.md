# Source: https://www.sbert.net/examples/sparse_encoder/training/nli/README.html

# Natural Language Inference[ïƒ?](#natural-language-inference "Link to this heading")

Given two sentence (premise and hypothesis), Natural Language Inference (NLI) is the task of deciding if the premise entails the hypothesis, if they are contradiction, or if they are neutral. Commonly used NLI dataset are [SNLI](https://huggingface.co/datasets/stanfordnlp/snli) and [MultiNLI](https://huggingface.co/datasets/nyu-mll/multi_nli).

[Conneau et al.](https://huggingface.co/papers/1705.02364) showed that NLI data can be quite useful when training Sentence Embedding methods. We also found this in our [Sentence-BERT-Paper](https://huggingface.co/papers/1908.10084) and often use NLI as a first fine-tuning step for sparse encoder methods.

To train on NLI, see the following example file:

- **[[train_splade_nli.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/sparse_encoder/training/nli/train_splade_nli.py)**:

  This script trains a SparseEncoder (specifically a SPLADE-like model, fine-tuning e.g., naver/splade-cocondenser-ensembledistil) for NLI. It uses the [[`SpladeLoss`]](../../../../docs/package_reference/sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.SpladeLoss "sentence_transformers.sparse_encoder.losses.SpladeLoss"). This loss is designed for training SPLADE-style models and combines two main components: 1. A ranking loss, typically [[`SparseMultipleNegativesRankingLoss`]](../../../../docs/package_reference/sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.SparseMultipleNegativesRankingLoss "sentence_transformers.sparse_encoder.losses.SparseMultipleNegativesRankingLoss"), to ensure that relevant (e.g., entailment) pairs have higher similarity scores than irrelevant ones (in-batch negatives). 2. Regularization terms (controlled by document_regularizer_weight and potentially other parameters in the loss) to encourage sparsity in the learned term weightings in the sparse vectors. This is a key characteristic of SPLADE models, leading to highly efficient and effective sparse representations.

  The script uses the AllNLI dataset, likely with the â€œpair-scoreâ€? or â€œpairâ€? configuration to extract (anchor, positive) pairs (e.g., premise and entailment hypothesis) for the ranking component of the loss.

## Data[ïƒ?](#data "Link to this heading")

We combine [SNLI](https://huggingface.co/datasets/stanfordnlp/snli) and [MultiNLI](https://huggingface.co/datasets/nyu-mll/multi_nli) into a dataset we call [AllNLI](https://huggingface.co/datasets/sentence-transformers/all-nli). These two datasets contain sentence pairs and one of three labels: entailment, neutral, contradiction:

  Sentence A (Premise)                                                 Sentence B (Hypothesis)                                              Label
  -------------------------------------------------------------------- -------------------------------------------------------------------- ---------------
  A soccer game with multiple males playing.                           Some men are playing a sport.                                        entailment
  An older and younger man smiling.                                    Two men are smiling and laughing at the cats playing on the floor.   neutral
  A man inspects the uniform of a figure in some East Asian country.   The man is sleeping.                                                 contradiction

We format AllNLI in a few different subsets, compatible with different loss functions. For the [`train_splade_nli.py`] script, the data is typically processed into (anchor, positive) pairs for the ranking loss component. For example, entailment pairs from NLI can serve as (anchor, positive) pairs.

- The [pair subset of AllNLI](https://huggingface.co/datasets/sentence-transformers/all-nli/viewer/pair) provides (anchor, positive) pairs directly.

- The [triplet subset of AllNLI](https://huggingface.co/datasets/sentence-transformers/all-nli/viewer/triplet) provides (anchor, positive, negative) triplets, where the negative is a hard negative (contradiction). While SpladeLoss primarily uses positive pairs for its ranking component, hard negatives could potentially be incorporated depending on the exact SparseMultipleNegativesRankingLoss configuration.

## SpladeLoss[ïƒ?](#spladeloss "Link to this heading")

The [[`SpladeLoss`]](../../../../docs/package_reference/sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.SpladeLoss "sentence_transformers.sparse_encoder.losses.SpladeLoss") is used in train_splade_nli.py. Itâ€™s specifically designed for training SPLADE (Sparse Lexical and Expansion) models. It wraps a ranking loss, such as [[`SparseMultipleNegativesRankingLoss`]](../../../../docs/package_reference/sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.SparseMultipleNegativesRankingLoss "sentence_transformers.sparse_encoder.losses.SparseMultipleNegativesRankingLoss"), and adds regularization terms to promote sparsity in the output vectors.

### Ranking Component: SparseMultipleNegativesRankingLoss[ïƒ?](#ranking-component-sparsemultiplenegativesrankingloss "Link to this heading")

The underlying ranking loss operates on sentence pairs \[(a~1~, b~1~), â€¦, (a~n~, b~n~)\] where (a~i~, b~i~) are similar sentences (e.g., premise and its entailed hypothesis) and (a~i~, b~j~) for i != j are treated as dissimilar sentences (in-batch negatives). The loss minimizes the distance (or maximizes similarity) between (a~i~, b~i~) while simultaneously maximizing the distance (or minimizing similarity) between (a~i~, b~j~) for all i != j.

![SBERT MultipleNegativeRankingLoss](https://raw.githubusercontent.com/UKPLab/sentence-transformers/master/docs/img/MultipleNegativeRankingLoss.png)

Using this with NLI data means defining entailment pairs as positive pairs. For example, (*â€œA soccer game with multiple males playing.â€?*, *â€œSome men are playing a sport.â€?*) should be close in the sparse vector space.

### Sparsity Regularization[ïƒ?](#sparsity-regularization "Link to this heading")

A key part of [`SpladeLoss`] is the regularization (e.g., FLOPS regularization via [`document_regularizer_weight`]) applied to the term weights in the sparse output vectors. This encourages the model to select only the most important terms for representation, leading to very sparse vectors, which is beneficial for efficient retrieval.