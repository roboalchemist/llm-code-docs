# Source: https://www.sbert.net/docs/sparse_encoder/loss_overview.html

# Loss Overview[ïƒ?](#loss-overview "Link to this heading")

Warning

To train a [[`SparseEncoder`]](../package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder"), you need either [[`SpladeLoss`]](../package_reference/sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.SpladeLoss "sentence_transformers.sparse_encoder.losses.SpladeLoss") or [[`CSRLoss`]](../package_reference/sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.CSRLoss "sentence_transformers.sparse_encoder.losses.CSRLoss"), depending on the architecture. These are wrapper losses that add sparsity regularization on top of a main loss function, which must be provided as a parameter. The only loss that can be used independently is [[`SparseMSELoss`]](../package_reference/sparse_encoder/losses.html#sentence_transformers.sparse_encoder.losses.SparseMSELoss "sentence_transformers.sparse_encoder.losses.SparseMSELoss"), as it performs embedding-level distillation, ensuring sparsity by directly copying the teacherâ€™s sparse embedding.

## Sparse specific Loss Functions[ïƒ?](#sparse-specific-loss-functions "Link to this heading")

### SPLADE Loss[ïƒ?](#splade-loss "Link to this heading")

The [`SpladeLoss`](../package_reference/sparse_encoder/losses.html#spladeloss) implements a specialized loss function for SPLADE (Sparse Lexical and Expansion) models. It combines a main loss function with regularization terms to control efficiency:

- Supports all the losses mention below as main loss but three principal loss types: [`SparseMultipleNegativesRankingLoss`](../package_reference/sparse_encoder/losses.html#sparsemultiplenegativesrankingloss), [`SparseMarginMSELoss`](../package_reference/sparse_encoder/losses.html#sparsemarginmseloss) and [`SparseDistillKLDivLoss`](../package_reference/sparse_encoder/losses.html#sparsedistillkldivloss).

- Uses [`FlopsLoss`](../package_reference/sparse_encoder/losses.html#flopsloss) for regularization to control sparsity by default, but supports custom regularizers.

- Balances effectiveness (via the main loss) with efficiency by regularizing both query and document representations.

- Allows using different regularizers for queries and documents via the [`query_regularizer`] and [`document_regularizer`] parameters, enabling fine-grained control over sparsity patterns for different types of inputs.

- Supports separate threshold values for queries and documents via the [`query_regularizer_threshold`] and [`document_regularizer_threshold`] parameters, allowing different sparsity strictness levels for each input type.

### CSR Loss[ïƒ?](#csr-loss "Link to this heading")

If you are using the [`SparseAutoEncoder`](../package_reference/sparse_encoder/models.html#sparseautoencoder) module, then you have to use the [`CSRLoss`](../package_reference/sparse_encoder/losses.html#csrloss) (Contrastive Sparse Representation Loss). It combines two components:

- A reconstruction loss [`CSRReconstructionLoss`](../package_reference/sparse_encoder/losses.html#csrreconstructionloss) that ensures sparse representation can faithfully reconstruct original embeddings.

- A main loss, which in the paper is a contrastive learning component using [[`SparseMultipleNegativesRankingLoss`]](../package_reference/sparse_encoder/losses.html#sparsemultiplenegativesrankingloss) that ensures semanticallysimilar sentences have similar representations. But itâ€™s theorically possible to use all the losses mention below as main loss like for [`SpladeLoss`](../package_reference/sparse_encoder/losses.html#spladeloss) .

## Loss Table[ïƒ?](#loss-table "Link to this heading")

Loss functions play a critical role in the performance of your fine-tuned model. Sadly, there is no â€œone size fits allâ€? loss function. Ideally, this table should help narrow down your choice of loss function(s) by matching them to your data formats.

Note

> ::: 
> You can often convert one training data format into another, allowing more loss functions to be viable for your scenario. For example, [`(sentence_A,`]` `[`sentence_B)`]` `[`pairs`] with [`class`] labels can be converted into [`(anchor,`]` `[`positive,`]` `[`negative)`]` `[`triplets`] by sampling sentences with the same or different classes.
> :::

Note

The loss functions in [SentenceTransformer \> Loss Overview](../sentence_transformer/loss_overview.html) that appear here with the [`Sparse`] prefix are identical to their dense versions. The prefix is used only to indicate which losses can be used as main losses to train a [[`SparseEncoder`]](../package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder")

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Inputs                                              Labels                                     Appropriate Loss Functions
  --------------------------------------------------- ------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------
  `(anchor, positive) pairs`                          `none`                                     [`SparseMultipleNegativesRankingLoss`](../package_reference/sparse_encoder/losses.html#sparsemultiplenegativesrankingloss)

  `(sentence_A, sentence_B) pairs`                    `float similarity score between 0 and 1`   [`SparseCoSENTLoss`](../package_reference/sparse_encoder/losses.html#sparsecosentloss)\
                                                                                                 [`SparseAnglELoss`](../package_reference/sparse_encoder/losses.html#sparseangleloss)\
                                                                                                 [`SparseCosineSimilarityLoss`](../package_reference/sparse_encoder/losses.html#sparsecosinesimilarityloss)

  `(anchor, positive, negative) triplets`             `none`                                     [`SparseMultipleNegativesRankingLoss`](../package_reference/sparse_encoder/losses.html#sparsemultiplenegativesrankingloss)\
                                                                                                 [`SparseTripletLoss`](../package_reference/sparse_encoder/losses.html#sparsetripletloss)

  `(anchor, positive, negative_1, ..., negative_n)`   `none`                                     [`SparseMultipleNegativesRankingLoss`](../package_reference/sparse_encoder/losses.html#sparsemultiplenegativesrankingloss)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Distillation[ïƒ?](#distillation "Link to this heading")

These loss functions are specifically designed to be used when distilling the knowledge from one model into another. This is rather commonly used when training Sparse embedding models.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Texts                                              Labels                                                                      Appropriate Loss Functions
  -------------------------------------------------- --------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------
  `sentence`                                         `model sentence embeddings`                                                 [`SparseMSELoss`](../package_reference/sparse_encoder/losses.html#sparsemseloss)

  `(sentence_1, sentence_2, ..., sentence_N)`        `model sentence embeddings`                                                 [`SparseMSELoss`](../package_reference/sparse_encoder/losses.html#sparsemseloss)

  `(query, passage_one, passage_two)`                `gold_sim(query, passage_one) - gold_sim(query, passage_two)`               [`SparseMarginMSELoss`](../package_reference/sparse_encoder/losses.html#sparsemarginmseloss)

  `(query, positive, negative_1, ..., negative_n)`   `[gold_sim(query, positive) - gold_sim(query, negative_i) for i in 1..n]`   [`SparseMarginMSELoss`](../package_reference/sparse_encoder/losses.html#sparsemarginmseloss)

  `(query, positive, negative)`                      `[gold_sim(query, positive), gold_sim(query, negative)]`                    [`SparseDistillKLDivLoss`](../package_reference/sparse_encoder/losses.html#sparsedistillkldivloss)\
                                                                                                                                 [`SparseMarginMSELoss`](../package_reference/sparse_encoder/losses.html#sparsemarginmseloss)

  `(query, positive, negative_1, ..., negative_n)`   `[gold_sim(query, positive), gold_sim(query, negative_i)...]`               [`SparseDistillKLDivLoss`](../package_reference/sparse_encoder/losses.html#sparsedistillkldivloss)\
                                                                                                                                 [`SparseMarginMSELoss`](../package_reference/sparse_encoder/losses.html#sparsemarginmseloss)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Commonly used Loss Functions[ïƒ?](#commonly-used-loss-functions "Link to this heading")

In practice, not all loss functions get used equally often. The most common scenarios are:

- [`(anchor,`]` `[`positive)`]` `[`pairs`] without any labels: [`SparseMultipleNegativesRankingLoss`](../package_reference/sparse_encoder/losses.html#sparsemultiplenegativesrankingloss) (a.k.a. InfoNCE or in-batch negatives loss) is commonly used to train the top performing embedding models. This data is often relatively cheap to obtain, and the models are generally very performant. Here for our sparse retrieval tasks, this format works well with [`SpladeLoss`](../package_reference/sparse_encoder/losses.html#spladeloss) or [`CSRLoss`](../package_reference/sparse_encoder/losses.html#csrloss), both typically using InfoNCE as their underlying loss function.

- [`(query,`]` `[`positive,`]` `[`negative_1,`]` `[`...,`]` `[`negative_n)`] format: This structure with multiple negatives is particularly effective with [`SpladeLoss`](../package_reference/sparse_encoder/losses.html#spladeloss) configured with [`SparseMarginMSELoss`](../package_reference/sparse_encoder/losses.html#sparsemarginmseloss), especially in knowledge distillation scenarios where a teacher model provides similarity scores. The strongest models are trained with distillation losses like [`SparseDistillKLDivLoss`](../package_reference/sparse_encoder/losses.html#sparsedistillkldivloss) or [`SparseMarginMSELoss`](../package_reference/sparse_encoder/losses.html#sparsemarginmseloss).

## Custom Loss Functions[ïƒ?](#custom-loss-functions "Link to this heading")

Advanced users can create and train with their own loss functions. Custom loss functions only have a few requirements:

- They must be a subclass of [[`torch.nn.Module`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)").

- They must have [`model`] as the first argument in the constructor.

- They must implement a [`forward`] method that accepts [`sentence_features`] and [`labels`]. The former is a list of tokenized batches, one element for each column. These tokenized batches can be fed directly to the [`model`] being trained to produce embeddings. The latter is an optional tensor of labels. The method must return a single loss value or a dictionary of loss components (component names to loss values) that will be summed to produce the final loss value. When returning a dictionary, the individual components will be logged separately in addition to the summed loss, allowing you to monitor the individual components of the loss.

To get full support with the automatic model card generation, you may also wish to implement:

- a [`get_config_dict`] method that returns a dictionary of loss parameters.

- a [`citation`] property so your work gets cited in all models that train with the loss.

Consider inspecting existing loss functions to get a feel for how loss functions are commonly implemented.