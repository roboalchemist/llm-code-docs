# Source: https://www.sbert.net/docs/cross_encoder/loss_overview.html

# Loss Overview[ïƒ?](#loss-overview "Link to this heading")

## Loss Table[ïƒ?](#loss-table "Link to this heading")

Loss functions play a critical role in the performance of your fine-tuned Cross Encoder model. Sadly, there is no â€œone size fits allâ€? loss function. Ideally, this table should help narrow down your choice of loss function(s) by matching them to your data formats.

Note

You can often convert one training data format into another, allowing more loss functions to be viable for your scenario. For example, [`(sentence_A,`]` `[`sentence_B)`]` `[`pairs`] with [`class`] labels can be converted into [`(anchor,`]` `[`positive,`]` `[`negative)`]` `[`triplets`] by sampling sentences with the same or different classes.

Additionally, [[`mine_hard_negatives()`]](../package_reference/util.html#sentence_transformers.util.mine_hard_negatives "sentence_transformers.util.mine_hard_negatives") can easily be used to turn [`(anchor,`]` `[`positive)`] to:

- [`(anchor,`]` `[`positive,`]` `[`negative)`]` `[`triplets`] with [`output_format="triplet"`],

- [`(anchor,`]` `[`positive,`]` `[`negative_1,`]` `[`â€¦,`]` `[`negative_n)`]` `[`tuples`] with [`output_format="n-tuple"`].

- [`(anchor,`]` `[`passage,`]` `[`label)`]` `[`labeled`]` `[`pairs`] with a label of 0 for negative and 1 for positive with [`output_format="labeled-pair"`],

- [`(anchor,`]` `[`[doc1,`]` `[`doc2,`]` `[`...,`]` `[`docN],`]` `[`[label1,`]` `[`label2,`]` `[`...,`]` `[`labelN])`]` `[`triplets`] with labels of 0 for negative and 1 for positive with [`output_format="labeled-list"`],

+---------------------------------------------------+------------------------------------------+-------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Inputs                                            | Labels                                   | Number of Model Output Labels | Appropriate Loss Functions                                                                                                |
+===================================================+==========================================+===============================+===========================================================================================================================+
| `(sentence_A, sentence_B) pairs`                  | `class`                                  | `num_classes`                 | [`CrossEntropyLoss`](../package_reference/cross_encoder/losses.html#crossentropyloss)                                     |
+---------------------------------------------------+------------------------------------------+-------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| `(anchor, positive) pairs`                        | `none`                                   | `1`                           | [`MultipleNegativesRankingLoss`](../package_reference/cross_encoder/losses.html#multiplenegativesrankingloss)\            |
|                                                   |                                          |                               | [`CachedMultipleNegativesRankingLoss`](../package_reference/cross_encoder/losses.html#cachedmultiplenegativesrankingloss) |
+---------------------------------------------------+------------------------------------------+-------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| `(anchor, positive/negative) pairs`               | `1 if positive, 0 if negative`           | `1`                           | [`BinaryCrossEntropyLoss`](../package_reference/cross_encoder/losses.html#binarycrossentropyloss)                         |
+---------------------------------------------------+------------------------------------------+-------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| `(sentence_A, sentence_B) pairs`                  | `float similarity score between 0 and 1` | `1`                           | [`BinaryCrossEntropyLoss`](../package_reference/cross_encoder/losses.html#binarycrossentropyloss)                         |
+---------------------------------------------------+------------------------------------------+-------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| `(anchor, positive, negative) triplets`           | `none`                                   | `1`                           | [`MultipleNegativesRankingLoss`](../package_reference/cross_encoder/losses.html#multiplenegativesrankingloss)\            |
|                                                   |                                          |                               | [`CachedMultipleNegativesRankingLoss`](../package_reference/cross_encoder/losses.html#cachedmultiplenegativesrankingloss) |
+---------------------------------------------------+------------------------------------------+-------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| `(anchor, positive, negative_1, ..., negative_n)` | `none`                                   | `1`                           | [`MultipleNegativesRankingLoss`](../package_reference/cross_encoder/losses.html#multiplenegativesrankingloss)\            |
|                                                   |                                          |                               | [`CachedMultipleNegativesRankingLoss`](../package_reference/cross_encoder/losses.html#cachedmultiplenegativesrankingloss) |
+---------------------------------------------------+------------------------------------------+-------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| `(query, [doc1, doc2, ..., docN])`                | `[score1, score2, ..., scoreN]`          | `1`                           | 1.  [`LambdaLoss`](../package_reference/cross_encoder/losses.html#lambdaloss)                                             |
|                                                   |                                          |                               | 2.  [`PListMLELoss`](../package_reference/cross_encoder/losses.html#plistmleloss)                                         |
|                                                   |                                          |                               | 3.  [`ListNetLoss`](../package_reference/cross_encoder/losses.html#listnetloss)                                           |
|                                                   |                                          |                               | 4.  [`RankNetLoss`](../package_reference/cross_encoder/losses.html#ranknetloss)                                           |
|                                                   |                                          |                               | 5.  [`ListMLELoss`](../package_reference/cross_encoder/losses.html#listmleloss)                                           |
+---------------------------------------------------+------------------------------------------+-------------------------------+---------------------------------------------------------------------------------------------------------------------------+

## Distillation[ïƒ?](#distillation "Link to this heading")

These loss functions are specifically designed to be used when distilling the knowledge from one model into another. For example, when finetuning a small model to behave more like a larger & stronger one, or when finetuning a model to become multi-lingual.

  Texts                                              Labels                                                                      Appropriate Loss Functions
  -------------------------------------------------- --------------------------------------------------------------------------- ---------------------------------------------------------------------------------
  `(sentence_A, sentence_B) pairs`                   `similarity score`                                                          [`MSELoss`](../package_reference/cross_encoder/losses.html#mseloss)
  `(query, passage_one, passage_two) triplets`       `gold_sim(query, passage_one) - gold_sim(query, passage_two)`               [`MarginMSELoss`](../package_reference/cross_encoder/losses.html#marginmseloss)
  `(query, positive, negative_1, ..., negative_n)`   `[gold_sim(query, positive) - gold_sim(query, negative_i) for i in 1..n]`   [`MarginMSELoss`](../package_reference/cross_encoder/losses.html#marginmseloss)
  `(query, positive, negative)`                      `[gold_sim(query, positive), gold_sim(query, negative)]`                    [`MarginMSELoss`](../package_reference/cross_encoder/losses.html#marginmseloss)
  `(query, positive, negative_1, ..., negative_n)`   `[gold_sim(query, positive), gold_sim(query, negative_i)...]`               [`MarginMSELoss`](../package_reference/cross_encoder/losses.html#marginmseloss)

## Commonly used Loss Functions[ïƒ?](#commonly-used-loss-functions "Link to this heading")

In practice, not all loss functions get used equally often. The most common scenarios are:

- [`(sentence_A,`]` `[`sentence_B)`]` `[`pairs`] with [`float`]` `[`similarity`]` `[`score`] or [`1`]` `[`if`]` `[`positive,`]` `[`0`]` `[`if`]` `[`negative`]: [`BinaryCrossEntropyLoss`](../package_reference/cross_encoder/losses.html#binarycrossentropyloss) is a traditional option that remains very challenging to outperform.

- [`(anchor,`]` `[`positive)`]` `[`pairs`] without any labels: combined with [`mine_hard_negatives`](../package_reference/util.html#sentence_transformers.util.mine_hard_negatives)

  - with `output_format=â€?labeled-listâ€?`, then [`LambdaLoss`](../package_reference/cross_encoder/losses.html#lambdaloss) is frequently used for learning-to-rank tasks.

  - with `output_format=â€?labeled-pairâ€?`, then [`BinaryCrossEntropyLoss`](../package_reference/cross_encoder/losses.html#binarycrossentropyloss) remains a strong option.

## Custom Loss Functions[ïƒ?](#custom-loss-functions "Link to this heading")

Advanced users can create and train with their own loss functions. Custom loss functions only have a few requirements:

- They must be a subclass of [[`torch.nn.Module`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)").

- They must have [`model`] as the first argument in the constructor.

- They must implement a [`forward`] method that accepts [`inputs`] and [`labels`]. The former is a nested list of texts in the batch, with each element in the outer list representing a column in the training dataset. You have to combine these texts into pairs that can be 1) tokenized and 2) fed to the model. The latter is an optional (list of) tensor(s) of labels from a [`label`], [`labels`], [`score`], or [`scores`] column in the dataset. The method must return a single loss value or a dictionary of loss components (component names to loss values) that will be summed to produce the final loss value. When returning a dictionary, the individual components will be logged separately in addition to the summed loss, allowing you to monitor the individual components of the loss.

To get full support with the automatic model card generation, you may also wish to implement:

- a [`get_config_dict`] method that returns a dictionary of loss parameters.

- a [`citation`] property so your work gets cited in all models that train with the loss.

Consider inspecting existing loss functions to get a feel for how loss functions are commonly implemented.