# Source: https://www.sbert.net/examples/sentence_transformer/training/nli/README.html

# Natural Language Inference[ïƒ?](#natural-language-inference "Link to this heading")

Given two sentence (premise and hypothesis), Natural Language Inference (NLI) is the task of deciding if the premise entails the hypothesis, if they are contradiction, or if they are neutral. Commonly used NLI dataset are [SNLI](https://huggingface.co/datasets/stanfordnlp/snli) and [MultiNLI](https://huggingface.co/datasets/nyu-mll/multi_nli).

[Conneau et al.](https://huggingface.co/papers/1705.02364) showed that NLI data can be quite useful when training Sentence Embedding methods. We also found this in our [Sentence-BERT-Paper](https://huggingface.co/papers/1908.10084) and often use NLI as a first fine-tuning step for sentence embedding methods.

To train on NLI, see the following example files:

1.  **[[training_nli.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/sentence_transformer/training/nli/training_nli.py)**:

    This example uses [[`SoftmaxLoss`]](../../../../docs/package_reference/sentence_transformer/losses.html#sentence_transformers.losses.SoftmaxLoss "sentence_transformers.losses.SoftmaxLoss") as described in the original \[Sentence Transformers paper\]([https://huggingface.co/papers/1908.10084](https://huggingface.co/papers/1908.10084)).

2.  **[[training_nli_v2.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/sentence_transformer/training/nli/training_nli_v2.py)**:

    The [[`SoftmaxLoss`]](../../../../docs/package_reference/sentence_transformer/losses.html#sentence_transformers.losses.SoftmaxLoss "sentence_transformers.losses.SoftmaxLoss") as used in our original SBERT paper does not yield optimal performance. A better loss is [[`MultipleNegativesRankingLoss`]](../../../../docs/package_reference/sentence_transformer/losses.html#sentence_transformers.losses.MultipleNegativesRankingLoss "sentence_transformers.losses.MultipleNegativesRankingLoss"), where we provide pairs or triplets. In this script, we provide a triplet of the format: (anchor, entailment_sentence, contradiction_sentence). The NLI data provides such triplets. The [[`MultipleNegativesRankingLoss`]](../../../../docs/package_reference/sentence_transformer/losses.html#sentence_transformers.losses.MultipleNegativesRankingLoss "sentence_transformers.losses.MultipleNegativesRankingLoss") yields much higher performances and is more intuitive than [[`SoftmaxLoss`]](../../../../docs/package_reference/sentence_transformer/losses.html#sentence_transformers.losses.SoftmaxLoss "sentence_transformers.losses.SoftmaxLoss"). We have used this loss to train the paraphrase model in our [Making Monolingual Sentence Embeddings Multilingual using Knowledge Distillation](https://huggingface.co/papers/2004.09813) paper.

3.  **[[training_nli_v3.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/sentence_transformer/training/nli/training_nli_v3.py)**

    Following the [GISTEmbed](https://huggingface.co/papers/2402.16829) paper, we can modify the in-batch negative selection from [[`MultipleNegativesRankingLoss`]](../../../../docs/package_reference/sentence_transformer/losses.html#sentence_transformers.losses.MultipleNegativesRankingLoss "sentence_transformers.losses.MultipleNegativesRankingLoss") using a guiding model. Candidate negative pairs are ignored during training if the guiding model considers the pair to be too similar. In practice, the [[`GISTEmbedLoss`]](../../../../docs/package_reference/sentence_transformer/losses.html#sentence_transformers.losses.GISTEmbedLoss "sentence_transformers.losses.GISTEmbedLoss") tends to produce a stronger training signal than [[`MultipleNegativesRankingLoss`]](../../../../docs/package_reference/sentence_transformer/losses.html#sentence_transformers.losses.MultipleNegativesRankingLoss "sentence_transformers.losses.MultipleNegativesRankingLoss") at the cost of some training overhead for running inference on the guiding model.

You can also train and use [[`CrossEncoder`]](../../../../docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder") models for this task. See [Cross Encoder \> Training Examples \> Natural Language Inference](../../../cross_encoder/training/nli/README.html) for more details.

## Data[ïƒ?](#data "Link to this heading")

We combine [SNLI](https://huggingface.co/datasets/stanfordnlp/snli) and [MultiNLI](https://huggingface.co/datasets/nyu-mll/multi_nli) into a dataset we call [AllNLI](https://huggingface.co/datasets/sentence-transformers/all-nli). These two datasets contain sentence pairs and one of three labels: entailment, neutral, contradiction:

  Sentence A (Premise)                                                 Sentence B (Hypothesis)                                              Label
  -------------------------------------------------------------------- -------------------------------------------------------------------- ---------------
  A soccer game with multiple males playing.                           Some men are playing a sport.                                        entailment
  An older and younger man smiling.                                    Two men are smiling and laughing at the cats playing on the floor.   neutral
  A man inspects the uniform of a figure in some East Asian country.   The man is sleeping.                                                 contradiction

We format AllNLI in a few different subsets, compatible with different loss functions. See for example the [triplet subset of AllNLI](https://huggingface.co/datasets/sentence-transformers/all-nli/viewer/triplet).

## SoftmaxLoss[ïƒ?](#softmaxloss "Link to this heading")

[Conneau et al.](https://huggingface.co/papers/1705.02364) described how a softmax classifier on top of a [siamese network](https://en.wikipedia.org/wiki/Siamese_neural_network) can be used to learn meaningful sentence representation. We can achieve this by using [[`SoftmaxLoss`]](../../../../docs/package_reference/sentence_transformer/losses.html#sentence_transformers.losses.SoftmaxLoss "sentence_transformers.losses.SoftmaxLoss"):

![SBERT SoftmaxLoss](https://raw.githubusercontent.com/UKPLab/sentence-transformers/master/docs/img/SBERT_SoftmaxLoss.png)

We pass the two sentences through our SentenceTransformer model and get the sentence embeddings *u* and *v*. We then concatenate *u*, *v* and *\|u-v\|* to form one long vector. This vector is then passed to a softmax classifier, which predicts our three classes (entailment, neutral, contradiction).

This setup learns sentence embeddings that can later be used for wide variety of tasks.

## MultipleNegativesRankingLoss[ïƒ?](#multiplenegativesrankingloss "Link to this heading")

That the [[`SoftmaxLoss`]](../../../../docs/package_reference/sentence_transformer/losses.html#sentence_transformers.losses.SoftmaxLoss "sentence_transformers.losses.SoftmaxLoss") with NLI data produces (relatively) good sentence embeddings is rather coincidental. The [[`MultipleNegativesRankingLoss`]](../../../../docs/package_reference/sentence_transformer/losses.html#sentence_transformers.losses.MultipleNegativesRankingLoss "sentence_transformers.losses.MultipleNegativesRankingLoss") is much more intuitive and produces significantly better sentence representations.

The training data for MultipleNegativesRankingLoss consists of sentence pairs \[(a~1~, b~1~), â€¦, (a~n~, b~n~)\] where we assume that (a~i~, b~i~) are similar sentences and (a~i~, b~j~) are dissimilar sentences for i != j. The minimizes the distance between (a~i~, b~i~) while it simultaneously maximizes the distance (a~i~, b~j~) for all i != j. For example, in the following picture:

![SBERT MultipleNegativeRankingLoss](https://raw.githubusercontent.com/UKPLab/sentence-transformers/master/docs/img/MultipleNegativeRankingLoss.png)

The distance between (a~1~, b~1~) is reduced, while the distance between (a~1~, b~2â€¦5~) will be increased. The same is done for a~2~, â€¦, a~5~.

Using [[`MultipleNegativesRankingLoss`]](../../../../docs/package_reference/sentence_transformer/losses.html#sentence_transformers.losses.MultipleNegativesRankingLoss "sentence_transformers.losses.MultipleNegativesRankingLoss") with NLI is rather easy: We define sentences that have an *entailment* label as positive pairs. E.g, we have pairs like (*â€œA soccer game with multiple males playing.â€?*, *â€œSome men are playing a sport.â€?*) and want that these pairs are close in vector space. The [pair subset of AllNLI](https://huggingface.co/datasets/sentence-transformers/all-nli/viewer/pair) has been prepared in this format.

### MultipleNegativesRankingLoss with Hard Negatives[ïƒ?](#multiplenegativesrankingloss-with-hard-negatives "Link to this heading")

We can further improve MultipleNegativesRankingLoss by providing triplets rather than pairs: \[(a~1~, b~1~, c~1~), â€¦, (a~n~, b~n~, c~n~)\]. The samples for c~i~ are so-called hard-negatives: On a lexical level, they are similar to a~i~ and b~i~, but on a semantic level, they mean different things and should not be close to a~i~ in the vector space.

For NLI data, we can use the contradiction-label to create such triplets with a hard negative. So our triplets look like this: (â€?*A soccer game with multiple males playing.â€?*, *â€œSome men are playing a sport.â€?*, *â€œA group of men playing a baseball game.â€?*). We want the sentences *â€œA soccer game with multiple males playing.â€?* and *â€œSome men are playing a sport.â€?* to be close in the vector space, while there should be a larger distance between *â€œA soccer game with multiple males playing.â€?* and â€œ*A group of men playing a baseball game.â€?*. The [triplet subset of AllNLI](https://huggingface.co/datasets/sentence-transformers/all-nli/viewer/triplet) has been prepared in this format.

### GISTEmbedLoss[ïƒ?](#gistembedloss "Link to this heading")

[[`MultipleNegativesRankingLoss`]](../../../../docs/package_reference/sentence_transformer/losses.html#sentence_transformers.losses.MultipleNegativesRankingLoss "sentence_transformers.losses.MultipleNegativesRankingLoss") can be extended even further by recognizing that the in-batch negative sampling as shown in [this example](#multiplenegativesrankingloss) is a bit flawed. In particular, we automatically assume that the pairs (a~1~, b~2~), â€¦, (a~1~, b~n~) are negative, but that does not strictly have to be true.

To address this, [[`GISTEmbedLoss`]](../../../../docs/package_reference/sentence_transformer/losses.html#sentence_transformers.losses.GISTEmbedLoss "sentence_transformers.losses.GISTEmbedLoss") uses a Sentence Transformer model to guide the in-batch negative sample selection. In particular, if the guide model considers the similarity of (a~1~, b~n~) to be larger than (a~1~, b~1~), then the (a~1~, b~n~) pair is considered a false negative and consequently ignored in the training process. In essence, this results in higher quality training data for the model.