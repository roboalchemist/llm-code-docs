# Source: https://www.sbert.net/docs/package_reference/sparse_encoder/losses.html

# Losses[ïƒ?](#losses "Link to this heading")

[`sentence_transformers.sparse_encoder.losses`] defines different loss functions that can be used to fine-tune saprse embedding models on training data. The choice of loss function plays a critical role when fine-tuning the model. It determines how well our embedding model will work for the specific downstream task.

Sadly, there is no â€œone size fits allâ€? loss function. Which loss function is suitable depends on the available training data and on the target task. Consider checking out the [[Loss Overview]](../../sparse_encoder/loss_overview.html) to help narrow down your choice of loss function(s).

Warning

To train a [[`SparseEncoder`]](SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder"), you need either [[`SpladeLoss`]](#sentence_transformers.sparse_encoder.losses.SpladeLoss "sentence_transformers.sparse_encoder.losses.SpladeLoss") or [[`CSRLoss`]](#sentence_transformers.sparse_encoder.losses.CSRLoss "sentence_transformers.sparse_encoder.losses.CSRLoss"), depending on the architecture. These are wrapper losses that add sparsity regularization on top of a main loss function, which must be provided as a parameter. The only loss that can be used independently is [[`SparseMSELoss`]](#sentence_transformers.sparse_encoder.losses.SparseMSELoss "sentence_transformers.sparse_encoder.losses.SparseMSELoss"), as it performs embedding-level distillation, ensuring sparsity by directly copying the teacherâ€™s sparse embedding.

## SpladeLoss[ïƒ?](#spladeloss "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.losses.]][[SpladeLoss]][(]*[[model]][[:]][ ][[[SparseEncoder]](SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder.SparseEncoder")]*, *[[loss]][[:]][ ][[[Module]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")]*, *[[document_regularizer_weight]][[:]][ ][[float]]*, *[[query_regularizer_weight]][[:]][ ][[float][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[document_regularizer]][[:]][ ][[[Module]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[query_regularizer]][[:]][ ][[[Module]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[document_regularizer_threshold]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[query_regularizer_threshold]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[use_document_regularizer_only]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\losses\SpladeLoss.py#L15-L203)[ïƒ?](#sentence_transformers.sparse_encoder.losses.SpladeLoss "Link to this definition")

:   SpladeLoss implements the loss function for the SPLADE (Sparse Lexical and Expansion) model, which combines a main loss function with regularization terms to control efficiency.

    This loss function balances effectiveness (via the main loss) with efficiency by regularizing both the query and document representations to be sparse, reducing computational requirements at inference time.

    Parameters[:]

    :   - **model** â€" SparseEncoder model

        - **loss** â€" The principal loss function to use can be any of the SparseEncoder losses except CSR related losses and flops loss.

        - **document_regularizer_weight** â€" Weight for the corpus regularization term. This term encourages sparsity in the document embeddings. Will be applied to positive documents and all negatives one if some are provided. In some papers, this parameter is referred to as â€œlambda_dâ€? (document) or â€œlambda_câ€? (corpus).

        - **query_regularizer_weight** â€" Weight for the query regularization term. This term encourages sparsity in the query embeddings. If None, no query regularization will be applied, itâ€™s not a problem if you are in an inference-free setup or if you are having use_document_regularizer_only=True. Else you should have a query_regularizer_weight \> 0. In some papers, this parameter is referred to as â€œlambda_qâ€? (query).

        - **document_regularizer** â€" Optional regularizer to use specifically for corpus regularization instead of the default FlopsLoss. This allows for different regularization strategies for documents vs queries.

        - **query_regularizer** â€" Optional regularizer to use specifically for query regularization instead of the default FlopsLoss. This allows for different regularization strategies for queries vs documents.

        - **document_regularizer_threshold** â€" Optional threshold for the number of non-zero (active) elements in the corpus embeddings to be considered in the FlopsLoss. If specified, only corpus embeddings with more than this number of non-zero (active) elements will be considered. Only used when document_regularizer is None (for the default FlopsLoss).

        - **query_regularizer_threshold** â€" Optional threshold for the number of non-zero (active) elements in the query embeddings to be considered in the FlopsLoss. If specified, only query embeddings with more than this number of non-zero (active) elements will be considered. Only used when query_regularizer is None (for the default FlopsLoss).

        - **use_document_regularizer_only** â€" If True, all input embeddings are treated as documents and regularized together with document_regularizer_weight. Especially useful when training with symmetric texts (e.g. pairs of documents) or more.

    References

    - For more details, see the paper â€œFrom Distillation to Hard Negative Sampling: Making Sparse Neural IR Models More Effectiveâ€? [https://huggingface.co/papers/2205.04733](https://huggingface.co/papers/2205.04733)

    Requirements:

    :   1.  Input requirements depend on the chosen loss

        2.  Usually used with a teacher model in a knowledge distillation setup and an associated loss

    Example

    :::: 
    ::: highlight
        from datasets import Dataset

        from sentence_transformers.sparse_encoder import SparseEncoder, SparseEncoderTrainer, losses

        student_model = SparseEncoder("distilbert/distilbert-base-uncased")
        teacher_model = SparseEncoder("naver/splade-cocondenser-ensembledistil")
        train_dataset = Dataset.from_dict(
            
        )

        def compute_labels(batch):
            emb_queries = teacher_model.encode(batch["query"])
            emb_passages1 = teacher_model.encode(batch["passage1"])
            emb_passages2 = teacher_model.encode(batch["passage2"])
            return 

        train_dataset = train_dataset.map(compute_labels, batched=True)
        loss = losses.SpladeLoss(
            student_model,
            loss=losses.SparseMarginMSELoss(student_model),
            document_regularizer_weight=3e-5,
            query_regularizer_weight=5e-5,
        )

        trainer = SparseEncoderTrainer(model=student_model, train_dataset=train_dataset, loss=loss)
        trainer.train()
    :::
    ::::

## FlopsLoss[ïƒ?](#flopsloss "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.losses.]][[FlopsLoss]][(]*[[model]][[:]][ ][[[SparseEncoder]](SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder.SparseEncoder")]*, *[[threshold]][[:]][ ][[float][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\losses\FlopsLoss.py#L11-L64)[ïƒ?](#sentence_transformers.sparse_encoder.losses.FlopsLoss "Link to this definition")

:   FlopsLoss implements a regularization technique to promote sparsity in sparse encoder models. It calculates the squared L2 norm of the mean embedding vector, which helps reduce the number of floating-point operations (FLOPs) required during inference by encouraging more zero values in the embeddings. It can use a threshold to ignore embeddings with too few non-zero (active) elements.

    This loss is used as a regularization component within other losses like [[`SpladeLoss`]](#sentence_transformers.sparse_encoder.losses.SpladeLoss "sentence_transformers.sparse_encoder.losses.SpladeLoss") rather than being used as a standalone loss function.

    Parameters[:]

    :   - **model** â€" SparseEncoder model to be regularized

        - **threshold** â€" Optional threshold for the number of non-zero (active) elements in the embeddings. If specified, only embeddings with more than this number of non-zero (active) elements will be considered. This can help to ignore embeddings that are too sparse and may not contribute meaningfully to the loss.

    References

    - For further details, see: [https://huggingface.co/papers/2004.05665](https://huggingface.co/papers/2004.05665) for the general FLOPS loss and [https://huggingface.co/papers/2504.14839](https://huggingface.co/papers/2504.14839) for FLOPS with thresholds, a.k.a. FLOPS with l0 masking.

    Relations:

    :   - Used as a component within [[`SpladeLoss`]](#sentence_transformers.sparse_encoder.losses.SpladeLoss "sentence_transformers.sparse_encoder.losses.SpladeLoss") to regularize both query and document embeddings

    Example

    - This loss is typically used within the [[`SpladeLoss`]](#sentence_transformers.sparse_encoder.losses.SpladeLoss "sentence_transformers.sparse_encoder.losses.SpladeLoss") class, which combines it with other loss components.

## CSRLoss[ïƒ?](#csrloss "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.losses.]][[CSRLoss]][(]*[[model]][[:]][ ][[[SparseEncoder]](SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder.SparseEncoder")]*, *[[loss]][[:]][ ][[[Module]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[beta]][[:]][ ][[float]][ ][[=]][ ][[0.1]]*, *[[gamma]][[:]][ ][[float]][ ][[=]][ ][[1.0]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\losses\CSRLoss.py#L129-L228)[ïƒ?](#sentence_transformers.sparse_encoder.losses.CSRLoss "Link to this definition")

:   CSRLoss implements a combined loss function for Contrastive Sparse Representation (CSR) models.

    This loss combines two components:

    1.  

        A reconstruction loss [[`CSRReconstructionLoss`]](#sentence_transformers.sparse_encoder.losses.CSRReconstructionLoss "sentence_transformers.sparse_encoder.losses.CSRReconstructionLoss") that ensures the sparse representation can faithfully

        :   reconstruct the original embedding.

    2.  

        A main loss, which in the paper is a [[`SparseMultipleNegativesRankingLoss`]](#sentence_transformers.sparse_encoder.losses.SparseMultipleNegativesRankingLoss "sentence_transformers.sparse_encoder.losses.SparseMultipleNegativesRankingLoss") that ensures semantically

        :   similar sentences have similar representations.

    The total loss is linear combination of the two losses.

    Parameters[:]

    :   - **model** â€" SparseEncoder model

        - **loss** â€" The principal loss function to use can be any of the SparseEncoder losses except flops loss and CSRReconstruction loss. If None, the default loss is used, which is the SparseMultipleNegativesRankingLoss.

        - **beta** â€" Weight for the L_aux component in the reconstruction loss. Default is 0.1.

        - **gamma** â€" Weight for the main loss component (MNRL a.k.a. InfoNCE by default). Default is 1.0.

    References

    - For more details, see the paper â€œBeyond Matryoshka: Revisiting Sparse Coding for Adaptive Representationâ€?

    [https://huggingface.co/papers/2503.01776](https://huggingface.co/papers/2503.01776)

    Requirements:

    :   1.  Input requirements depend on the chosen loss

        2.  Uses autoencoder components of the SparseEncoder model

    Relations:

    :   - Uses [[`CSRReconstructionLoss`]](#sentence_transformers.sparse_encoder.losses.CSRReconstructionLoss "sentence_transformers.sparse_encoder.losses.CSRReconstructionLoss") for the reconstruction component

    Example

    :::: 
    ::: highlight
        from datasets import Dataset
        from sentence_transformers.sparse_encoder import SparseEncoder, SparseEncoderTrainer, losses

        model = SparseEncoder("sentence-transformers/all-MiniLM-L6-v2")
        train_dataset = Dataset.from_dict(
            
        )
        loss = losses.CSRLoss(model, beta=0.1, gamma=1.0)

        trainer = SparseEncoderTrainer(model=model, train_dataset=train_dataset, loss=loss)
        trainer.train()
    :::
    ::::

## CSRReconstructionLoss[ïƒ?](#csrreconstructionloss "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.losses.]][[CSRReconstructionLoss]][(]*[[model]][[:]][ ][[[SparseEncoder]](SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder.SparseEncoder")]*, *[[beta]][[:]][ ][[float]][ ][[=]][ ][[1.0]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\losses\CSRLoss.py#L28-L126)[ïƒ?](#sentence_transformers.sparse_encoder.losses.CSRReconstructionLoss "Link to this definition")

:   CSRReconstructionLoss implements the reconstruction loss component for Contrastive Sparse Representation (CSR) models.

    This loss ensures that the sparse encoding can accurately reconstruct the original model embeddings through three components:

    1.  A primary reconstruction loss (L_k) that measures the error between the original embedding and its reconstruction using the top-k sparse components.

    2.  A secondary reconstruction loss (L_4k) that measures the error using the top-4k sparse components.

    3.  An auxiliary loss (L_aux) that helps to learn residual information.

    Parameters[:]

    :   - **model** â€" SparseEncoder model with autoencoder components

        - **beta** â€" Weight for the auxiliary loss component (L_aux)

    References

    - For more details, see the paper â€œBeyond Matryoshka: Revisiting Sparse Coding for Adaptive Representationâ€? [https://huggingface.co/papers/2503.01776](https://huggingface.co/papers/2503.01776)

    Requirements:

    :   1.  The model must be configured to output the necessary reconstruction components

        2.  Used with SparseEncoder models that implement compositional sparse autoencoding

    Relations:

    :   - Used as a component within [[`CSRLoss`]](#sentence_transformers.sparse_encoder.losses.CSRLoss "sentence_transformers.sparse_encoder.losses.CSRLoss") combined with a contrastive loss

    Example

    - This loss is never used standalone, but instead used within the [[`CSRLoss`]](#sentence_transformers.sparse_encoder.losses.CSRLoss "sentence_transformers.sparse_encoder.losses.CSRLoss") class. See that loss for more details.

## SparseMultipleNegativesRankingLoss[ïƒ?](#sparsemultiplenegativesrankingloss "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.losses.]][[SparseMultipleNegativesRankingLoss]][(]*[[model:] [\~sentence_transformers.sparse_encoder.SparseEncoder.SparseEncoder]]*, *[[scale:] [float] [=] [1.0]]*, *[[similarity_fct=\<function] [dot_score\>]]*, *[[gather_across_devices:] [bool] [=] [False]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\losses\SparseMultipleNegativesRankingLoss.py#L12-L102)[ïƒ?](#sentence_transformers.sparse_encoder.losses.SparseMultipleNegativesRankingLoss "Link to this definition")

:   Given a list of (anchor, positive) pairs or (anchor, positive, negative) triplets, this loss optimizes the following:

    1.  Given an anchor (e.g. a question), assign the highest similarity to the corresponding positive (i.e. answer) out of every single positive and negative (e.g. all answers) in the batch.

    If you provide the optional negatives, they will all be used as extra options from which the model must pick the correct positive. Within reason, the harder this â€œpickingâ€? is, the stronger the model will become. Because of this, a higher batch size results in more in-batch negatives, which then increases performance (to a point).

    This loss function works great to train embeddings for retrieval setups where you have positive pairs (e.g. (query, answer)) as it will sample in each batch [`n-1`] negative docs randomly.

    This loss is also known as InfoNCE loss, SimCSE loss, Cross-Entropy Loss with in-batch negatives, or simply in-batch negatives loss.

    Parameters[:]

    :   - **model** â€" SparseEncoder model

        - **scale** â€" Output of similarity function is multiplied by scale value. In some literature, the scaling parameter is referred to as temperature, which is the inverse of the scale. In short: scale = 1 / temperature, so scale=20.0 is equivalent to temperature=0.05. A scale of 1.0 is often used for dot product similarity, and values around 20.0 to 50.0 are often used for cosine similarity.

        - **similarity_fct** â€" similarity function between sentence embeddings. By default, dot product is used. Can also be set to cosine similarity (and then set scale to e.g. 20.0)

        - **gather_across_devices** â€" If True, gather the embeddings across all devices before computing the loss. Recommended when training on multiple GPUs, as it allows for larger batch sizes, but it may slow down training due to communication overhead, and can potentially lead to out-of-memory errors.

    Requirements:

    :   1.  Need to be used in SpladeLoss or CSRLoss as a loss function.

        2.  (anchor, positive) pairs or (anchor, positive, negative) triplets

    Inputs:

    :   
          Texts                                             Labels
          ------------------------------------------------- --------
          (anchor, positive) pairs                          none
          (anchor, positive, negative) triplets             none
          (anchor, positive, negative_1, â€¦, negative_n)   none

    Recommendations:

    :   - Use [`BatchSamplers.NO_DUPLICATES`] ([[`docs`]](../sentence_transformer/sampler.html#sentence_transformers.training_args.BatchSamplers "sentence_transformers.training_args.BatchSamplers")) to ensure that no in-batch negatives are duplicates of the anchor or positive samples.

    Relations:

    :   - [`SparseCachedMultipleNegativesRankingLoss`] is equivalent to this loss, but it uses caching that allows for much higher batch sizes (and thus better performance) without extra memory usage. However, it is slightly slower.

        - [`SparseGISTEmbedLoss`] is equivalent to this loss, but uses a guide model to guide the in-batch negative sample selection. SparseGISTEmbedLoss yields a stronger training signal at the cost of some training overhead.

    Example

    :::: 
    ::: highlight
        from datasets import Dataset

        from sentence_transformers.sparse_encoder import SparseEncoder, SparseEncoderTrainer, losses

        model = SparseEncoder("distilbert/distilbert-base-uncased")
        train_dataset = Dataset.from_dict(
            
        )
        loss = losses.SpladeLoss(
            model=model, loss=losses.SparseMultipleNegativesRankingLoss(model), document_regularizer_weight=3e-5, query_regularizer_weight=5e-5
        )

        trainer = SparseEncoderTrainer(model=model, train_dataset=train_dataset, loss=loss)
        trainer.train()
    :::
    ::::

## SparseMarginMSELoss[ïƒ?](#sparsemarginmseloss "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.losses.]][[SparseMarginMSELoss]][(]*[[model:] [\~sentence_transformers.sparse_encoder.SparseEncoder.SparseEncoder]]*, *[[similarity_fct=\<function] [pairwise_dot_score\>]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\losses\SparseMarginMSELoss.py#L12-L176)[ïƒ?](#sentence_transformers.sparse_encoder.losses.SparseMarginMSELoss "Link to this definition")

:   Compute the MSE loss between the [`|sim(Query,`]` `[`Pos)`]` `[`-`]` `[`sim(Query,`]` `[`Neg)|`] and [`|gold_sim(Query,`]` `[`Pos)`]` `[`-`]` `[`gold_sim(Query,`]` `[`Neg)|`]. By default, sim() is the dot-product. The gold_sim is often the similarity score from a teacher model.

    In contrast to [[`SparseMultipleNegativesRankingLoss`]](#sentence_transformers.sparse_encoder.losses.SparseMultipleNegativesRankingLoss "sentence_transformers.sparse_encoder.losses.SparseMultipleNegativesRankingLoss"), the two passages do not have to be strictly positive and negative, both can be relevant or not relevant for a given query. This can be an advantage of SparseMarginMSELoss over SparseMultipleNegativesRankingLoss, but note that the SparseMarginMSELoss is much slower to train. With SparseMultipleNegativesRankingLoss, with a batch size of 64, we compare one query against 128 passages. With SparseMarginMSELoss, we compare a query only against two passages. Itâ€™s also possible to use multiple negatives with SparseMarginMSELoss, but the training would be even slower to train.

    Parameters[:]

    :   - **model** â€" SparseEncoder

        - **similarity_fct** â€" Which similarity function to use.

    References

    - For more details, please refer to [https://huggingface.co/papers/2010.02666](https://huggingface.co/papers/2010.02666).

    Requirements:

    :   1.  Need to be used in SpladeLoss or CSRLoss as a loss function.

        2.  (query, passage_one, passage_two) triplets or (query, positive, negative_1, â€¦, negative_n)

        3.  Usually used with a finetuned teacher M in a knowledge distillation setup

    Inputs:

    :   
          Texts                                            Labels
          ------------------------------------------------ -------------------------------------------------------------------------
          (query, passage_one, passage_two) triplets       M(query, passage_one) - M(query, passage_two)
          (query, passage_one, passage_two) triplets       \[M(query, passage_one), M(query, passage_two)\]
          (query, positive, negative_1, â€¦, negative_n)   \[M(query, positive) - M(query, negative_i) for i in 1..n\]
          (query, positive, negative_1, â€¦, negative_n)   \[M(query, positive), M(query, negative_1), â€¦, M(query, negative_n)\]

    Relations:

    :   - [[`SparseMSELoss`]](#sentence_transformers.sparse_encoder.losses.SparseMSELoss "sentence_transformers.sparse_encoder.losses.SparseMSELoss") is similar to this loss, but without a margin through the negative pair.

    Example

    With gold labels, e.g. if you have hard scores for sentences. Imagine you want a model to embed sentences with similar â€œqualityâ€? close to each other. If the â€œtext1â€? has quality 5 out of 5, â€œtext2â€? has quality 1 out of 5, and â€œtext3â€? has quality 3 out of 5, then the similarity of a pair can be defined as the difference of the quality scores. So, the similarity between â€œtext1â€? and â€œtext2â€? is 4, and the similarity between â€œtext1â€? and â€œtext3â€? is 2. If we use this as our â€œTeacher Modelâ€?, the label becomes similraity(â€œtext1â€?, â€œtext2â€?) - similarity(â€œtext1â€?, â€œtext3â€?) = 4 - 2 = 2.

    Positive values denote that the first passage is more similar to the query than the second passage, while negative values denote the opposite.

    :::: 
    ::: highlight
        from datasets import Dataset

        from sentence_transformers.sparse_encoder import SparseEncoder, SparseEncoderTrainer, losses

        model = SparseEncoder("naver/splade-cocondenser-ensembledistil")
        train_dataset = Dataset.from_dict(
            
        )

        loss = losses.SpladeLoss(
            model, losses.SparseMarginMSELoss(model), document_regularizer_weight=3e-5, query_regularizer_weight=5e-5
        )

        trainer = SparseEncoderTrainer(model=model, train_dataset=train_dataset, loss=loss)
        trainer.train()
    :::
    ::::

    We can also use a teacher model to compute the similarity scores. In this case, we can use the teacher model to compute the similarity scores and use them as the silver labels. This is often used in knowledge distillation.

    :::: 
    ::: highlight
        from datasets import Dataset

        from sentence_transformers.sparse_encoder import SparseEncoder, SparseEncoderTrainer, losses

        student_model = SparseEncoder("distilbert/distilbert-base-uncased")
        teacher_model = SparseEncoder("naver/splade-cocondenser-ensembledistil")
        train_dataset = Dataset.from_dict(
            
        )

        def compute_labels(batch):
            emb_queries = teacher_model.encode(batch["query"])
            emb_passages1 = teacher_model.encode(batch["passage1"])
            emb_passages2 = teacher_model.encode(batch["passage2"])
            return 

        train_dataset = train_dataset.map(compute_labels, batched=True)
        loss = losses.SpladeLoss(
            student_model, losses.SparseMarginMSELoss(student_model), document_regularizer_weight=3e-5, query_regularizer_weight=5e-5
        )

        trainer = SparseEncoderTrainer(model=student_model, train_dataset=train_dataset, loss=loss)
        trainer.train()
    :::
    ::::

    We can also use multiple negatives during the knowledge distillation.

    :::: 
    ::: highlight
        import torch
        from datasets import Dataset

        from sentence_transformers.sparse_encoder import SparseEncoder, SparseEncoderTrainer, losses

        student_model = SparseEncoder("distilbert/distilbert-base-uncased")
        teacher_model = SparseEncoder("naver/splade-cocondenser-ensembledistil")
        train_dataset = Dataset.from_dict(
            
        )

        def compute_labels(batch):
            emb_queries = teacher_model.encode(batch["query"])
            emb_passages1 = teacher_model.encode(batch["passage1"])
            emb_passages2 = teacher_model.encode(batch["passage2"])
            emb_passages3 = teacher_model.encode(batch["passage3"])
            return 

        train_dataset = train_dataset.map(compute_labels, batched=True)
        loss = losses.SpladeLoss(
            student_model, loss=losses.SparseMarginMSELoss(student_model), document_regularizer_weight=3e-5, query_regularizer_weight=5e-5
        )

        trainer = SparseEncoderTrainer(model=student_model, train_dataset=train_dataset, loss=loss)
        trainer.train()
    :::
    ::::

## SparseDistillKLDivLoss[ïƒ?](#sparsedistillkldivloss "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.losses.]][[SparseDistillKLDivLoss]][(]*[[model:] [\~sentence_transformers.sparse_encoder.SparseEncoder.SparseEncoder]]*, *[[similarity_fct=\<function] [pairwise_dot_score\>]]*, *[[temperature:] [float] [=] [2.0]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\losses\SparseDistillKLDivLoss.py#L12-L139)[ïƒ?](#sentence_transformers.sparse_encoder.losses.SparseDistillKLDivLoss "Link to this definition")

:   Compute the KL divergence loss between probability distributions derived from student and teacher modelsâ€™ similarity scores. By default, similarity is calculated using the dot-product. This loss is designed for knowledge distillation where a smaller student model learns from a more powerful teacher model.

    The loss computes softmax probabilities from the teacher similarity scores and log-softmax probabilities from the student model, then calculates the KL divergence between these distributions.

    Parameters[:]

    :   - **model** â€" SentenceTransformer model (student model)

        - **similarity_fct** â€" Which similarity function to use for the student model

        - **temperature** â€" Temperature parameter to soften probability distributions (higher temperature = softer distributions) When combined with other losses, a temperature of 1.0 is also viable, but a higher temperature (e.g., 2.0 or 4.0) can help prevent the student model from going to zero active dimensions. Defaults to 2.0.

    References

    - For more details, please refer to [https://huggingface.co/papers/2010.11386](https://huggingface.co/papers/2010.11386)

    Requirements:

    :   1.  Need to be used in SpladeLoss or CSRLoss as a loss function.

        2.  (query, positive, negative_1, â€¦, negative_n) examples

        3.  Labels containing teacher modelâ€™s scores between query-positive and query-negative pairs

    Inputs:

    :   
          Texts                                            Labels
          ------------------------------------------------ -------------------------------------------------------------
          (query, positive, negative)                      \[Teacher(query, positive), Teacher(query, negative)\]
          (query, positive, negative_1, â€¦, negative_n)   \[Teacher(query, positive), Teacher(query, negative_i)â€¦\]

    Relations:

    :   - Similar to [[`SparseMarginMSELoss`]](#sentence_transformers.sparse_encoder.losses.SparseMarginMSELoss "sentence_transformers.sparse_encoder.losses.SparseMarginMSELoss") but uses KL divergence instead of MSE

        - More suited for distillation tasks where preserving ranking is important

    Example

    Using a teacher model to compute similarity scores for distillation:

    :::: 
    ::: highlight
        import torch
        from datasets import Dataset

        from sentence_transformers.sparse_encoder import SparseEncoder, SparseEncoderTrainer, losses

        student_model = SparseEncoder("distilbert/distilbert-base-uncased")
        teacher_model = SparseEncoder("naver/splade-cocondenser-ensembledistil")
        train_dataset = Dataset.from_dict(
            
        )

        def compute_labels(batch):
            emb_queries = teacher_model.encode(batch["query"])
            emb_positives = teacher_model.encode(batch["positive"])
            emb_negatives = teacher_model.encode(batch["negative"])

            pos_scores = teacher_model.similarity_pairwise(emb_queries, emb_positives)
            neg_scores = teacher_model.similarity_pairwise(emb_queries, emb_negatives)

            # Stack the scores for positive and negative pairs
            return 

        train_dataset = train_dataset.map(compute_labels, batched=True)
        loss = losses.SpladeLoss(
            student_model, loss=losses.SparseDistillKLDivLoss(student_model), document_regularizer_weight=3e-5, query_regularizer_weight=5e-5
        )

        trainer = SparseEncoderTrainer(model=student_model, train_dataset=train_dataset, loss=loss)
        trainer.train()
    :::
    ::::

    With multiple negatives:

    :::: 
    ::: highlight
        import torch
        from datasets import Dataset

        from sentence_transformers.sparse_encoder import SparseEncoder, SparseEncoderTrainer, losses

        student_model = SparseEncoder("distilbert/distilbert-base-uncased")
        teacher_model = SparseEncoder("naver/splade-cocondenser-ensembledistil")
        train_dataset = Dataset.from_dict(
            
        )

        def compute_labels(batch):
            emb_queries = teacher_model.encode(batch["query"])
            emb_positives = teacher_model.encode(batch["positive"])
            emb_negatives1 = teacher_model.encode(batch["negative1"])
            emb_negatives2 = teacher_model.encode(batch["negative2"])

            pos_scores = teacher_model.similarity_pairwise(emb_queries, emb_positives)
            neg_scores1 = teacher_model.similarity_pairwise(emb_queries, emb_negatives1)
            neg_scores2 = teacher_model.similarity_pairwise(emb_queries, emb_negatives2)

            # Stack the scores for positive and multiple negative pairs
            return 

        train_dataset = train_dataset.map(compute_labels, batched=True)
        loss = losses.SpladeLoss(
            student_model, loss=losses.SparseDistillKLDivLoss(student_model), document_regularizer_weight=3e-5, query_regularizer_weight=5e-5
        )

        trainer = SparseEncoderTrainer(model=student_model, train_dataset=train_dataset, loss=loss)
        trainer.train()
    :::
    ::::

## SparseTripletLoss[ïƒ?](#sparsetripletloss "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.losses.]][[SparseTripletLoss]][(]*[[model:] [\~sentence_transformers.sparse_encoder.SparseEncoder.SparseEncoder]]*, *[[distance_metric=\<function] [TripletDistanceMetric.\<lambda\>\>]]*, *[[triplet_margin:] [float] [=] [5]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\losses\SparseTripletLoss.py#L11-L71)[ïƒ?](#sentence_transformers.sparse_encoder.losses.SparseTripletLoss "Link to this definition")

:   This class implements triplet loss. Given a triplet of (anchor, positive, negative), the loss minimizes the distance between anchor and positive while it maximizes the distance between anchor and negative. It compute the following loss function:

    [`loss`]` `[`=`]` `[`max(||anchor`]` `[`-`]` `[`positive||`]` `[`-`]` `[`||anchor`]` `[`-`]` `[`negative||`]` `[`+`]` `[`margin,`]` `[`0)`].

    Margin is an important hyperparameter and needs to be tuned respectively.

    Parameters[:]

    :   - **model** â€" SparseEncoder

        - **distance_metric** â€" Function to compute distance between two embeddings. The class TripletDistanceMetric contains common distance metrices that can be used.

        - **triplet_margin** â€" The negative should be at least this much further away from the anchor than the positive.

    References

    - For further details, see: [https://en.wikipedia.org/wiki/Triplet_loss](https://en.wikipedia.org/wiki/Triplet_loss)

    Requirements:

    :   1.  Need to be used in SpladeLoss or CSRLoss as a loss function.

        2.  (anchor, positive, negative) triplets

    Inputs:

    :   
          Texts                                   Labels
          --------------------------------------- --------
          (anchor, positive, negative) triplets   none

    Example

    :::: 
    ::: highlight
        from datasets import Dataset

        from sentence_transformers.sparse_encoder import SparseEncoder, SparseEncoderTrainer, losses

        model = SparseEncoder("distilbert/distilbert-base-uncased")
        train_dataset = Dataset.from_dict(
            
        )
        loss = losses.SpladeLoss(
            model=model, loss=losses.SparseTripletLoss(model), document_regularizer_weight=3e-5, query_regularizer_weight=5e-5
        )

        trainer = SparseEncoderTrainer(model=model, train_dataset=train_dataset, loss=loss)
        trainer.train()
    :::
    ::::

## SparseCosineSimilarityLoss[ïƒ?](#sparsecosinesimilarityloss "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.losses.]][[SparseCosineSimilarityLoss]][(]*[[model]][[:]][ ][[[SparseEncoder]](SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder.SparseEncoder")]*, *[[loss_fct]][[:]][ ][[[Module]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")][ ][[=]][ ][[MSELoss()]]*, *[[cos_score_transformation]][[:]][ ][[[Module]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")][ ][[=]][ ][[Identity()]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\losses\SparseCosineSimilarityLoss.py#L12-L76)[ïƒ?](#sentence_transformers.sparse_encoder.losses.SparseCosineSimilarityLoss "Link to this definition")

:   SparseCosineSimilarityLoss expects that the InputExamples consists of two texts and a float label. It computes the vectors [`u`]` `[`=`]` `[`model(sentence_A)`] and [`v`]` `[`=`]` `[`model(sentence_B)`] and measures the cosine-similarity between the two. By default, it minimizes the following loss: [`||input_label`]` `[`-`]` `[`cos_score_transformation(cosine_sim(u,v))||_2`].

    Parameters[:]

    :   - **model** â€" SparseEncoder model

        - **loss_fct** â€" Which pytorch loss function should be used to compare the [`cosine_similarity(u,`]` `[`v)`] with the input_label? By default, MSE is used: [`||input_label`]` `[`-`]` `[`cosine_sim(u,`]` `[`v)||_2`]

        - **cos_score_transformation** â€" The cos_score_transformation function is applied on top of cosine_similarity. By default, the identify function is used (i.e. no change).

    Requirements:

    :   - Need to be used in SpladeLoss or CSRLoss as a loss function.

        - Sentence pairs with corresponding similarity scores in range \[0, 1\]

    Inputs:

    :   
          Texts                            Labels
          -------------------------------- ------------------------
          (sentence_A, sentence_B) pairs   float similarity score

    Relations:

    :   - [[`SparseAnglELoss`]](#sentence_transformers.sparse_encoder.losses.SparseAnglELoss "sentence_transformers.sparse_encoder.losses.SparseAnglELoss") is [[`SparseCoSENTLoss`]](#sentence_transformers.sparse_encoder.losses.SparseCoSENTLoss "sentence_transformers.sparse_encoder.losses.SparseCoSENTLoss") with [`pairwise_angle_sim`] as the metric, rather than [`pairwise_cos_sim`].

    Example

    :::: 
    ::: highlight
        from datasets import Dataset
        from sentence_transformers.sparse_encoder import SparseEncoder, SparseEncoderTrainer, losses

        model = SparseEncoder("distilbert/distilbert-base-uncased")
        train_dataset = Dataset.from_dict(
            
        )
        loss = losses.SpladeLoss(
            model=model,
            loss=losses.SparseCosineSimilarityLoss(model),
            document_regularizer_weight=5e-5,
            use_document_regularizer_only=True,
        )

        trainer = SparseEncoderTrainer(model=model, train_dataset=train_dataset, loss=loss)
        trainer.train()
    :::
    ::::

## SparseCoSENTLoss[ïƒ?](#sparsecosentloss "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.losses.]][[SparseCoSENTLoss]][(]*[[model:] [\~sentence_transformers.sparse_encoder.SparseEncoder.SparseEncoder]]*, *[[scale:] [float] [=] [20.0]]*, *[[similarity_fct=\<function] [cos_sim\>]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\losses\SparseCoSENTLoss.py#L12-L76)[ïƒ?](#sentence_transformers.sparse_encoder.losses.SparseCoSENTLoss "Link to this definition")

:   This class implements CoSENT (Cosine Sentence). It expects that each of the InputExamples consists of a pair of texts and a float valued label, representing the expected similarity score between the pair.

    It computes the following loss function:

    [`loss`]` `[`=`]` `[`logsum(1+exp(s(i,j)-s(k,l))+exp...)`], where [`(i,j)`] and [`(k,l)`] are any of the input pairs in the batch such that the expected similarity of [`(i,j)`] is greater than [`(k,l)`]. The summation is over all possible pairs of input pairs in the batch that match this condition.

    Parameters[:]

    :   - **model** â€" SparseEncoder

        - **similarity_fct** â€" Function to compute the PAIRWISE similarity between embeddings. Default is [`util.pairwise_cos_sim`].

        - **scale** â€" Output of similarity function is multiplied by scale value. Represents the inverse temperature.

    References

    - For further details, see: [https://kexue.fm/archives/8847](https://kexue.fm/archives/8847)

    Requirements:

    :   - Need to be used in SpladeLoss or CSRLoss as a loss function.

        - Sentence pairs with corresponding similarity scores in range of the similarity function. Default is \[-1,1\].

    Inputs:

    :   
          Texts                            Labels
          -------------------------------- ------------------------
          (sentence_A, sentence_B) pairs   float similarity score

    Relations:

    :   - [[`SparseAnglELoss`]](#sentence_transformers.sparse_encoder.losses.SparseAnglELoss "sentence_transformers.sparse_encoder.losses.SparseAnglELoss") is SparseCoSENTLoss with [`pairwise_angle_sim`] as the metric, rather than [`pairwise_cos_sim`].

    Example

    :::: 
    ::: highlight
        from datasets import Dataset

        from sentence_transformers.sparse_encoder import SparseEncoder, SparseEncoderTrainer, losses

        model = SparseEncoder("distilbert/distilbert-base-uncased")
        train_dataset = Dataset.from_dict(
            
        )
        loss = losses.SpladeLoss(
            model=model, loss=losses.SparseCoSENTLoss(model), document_regularizer_weight=5e-5, use_document_regularizer_only=True
        )

        trainer = SparseEncoderTrainer(model=model, train_dataset=train_dataset, loss=loss)
        trainer.train()
    :::
    ::::

## SparseAnglELoss[ïƒ?](#sparseangleloss "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.losses.]][[SparseAnglELoss]][(]*[[model]][[:]][ ][[[SparseEncoder]](SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder.SparseEncoder")]*, *[[scale]][[:]][ ][[float]][ ][[=]][ ][[20.0]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\losses\SparseAnglELoss.py#L12-L78)[ïƒ?](#sentence_transformers.sparse_encoder.losses.SparseAnglELoss "Link to this definition")

:   This class implements AnglE (Angle Optimized). This is a modification of [[`SparseCoSENTLoss`]](#sentence_transformers.sparse_encoder.losses.SparseCoSENTLoss "sentence_transformers.sparse_encoder.losses.SparseCoSENTLoss"), designed to address the following issue: The cosine functionâ€™s gradient approaches 0 as the wave approaches the top or bottom of its form. This can hinder the optimization process, so AnglE proposes to instead optimize the angle difference in complex space in order to mitigate this effect.

    It expects that each of the InputExamples consists of a pair of texts and a float valued label, representing the expected similarity score between the pair.

    It computes the following loss function:

    [`loss`]` `[`=`]` `[`logsum(1+exp(s(k,l)-s(i,j))+exp...)`], where [`(i,j)`] and [`(k,l)`] are any of the input pairs in the batch such that the expected similarity of [`(i,j)`] is greater than [`(k,l)`]. The summation is over all possible pairs of input pairs in the batch that match this condition. This is the same as CoSENTLoss, with a different similarity function.

    Parameters[:]

    :   - **model** â€" SparseEncoder

        - **scale** â€" Output of similarity function is multiplied by scale value. Represents the inverse temperature.

    References

    - For further details, see: [https://huggingface.co/papers/2309.12871](https://huggingface.co/papers/2309.12871)

    Requirements:

    :   - Need to be used in SpladeLoss or CSRLoss as a loss function.

        - Sentence pairs with corresponding similarity scores in range of the similarity function. Default is \[-1,1\].

    Inputs:

    :   
          Texts                            Labels
          -------------------------------- ------------------------
          (sentence_A, sentence_B) pairs   float similarity score

    Relations:

    :   - [[`SparseCoSENTLoss`]](#sentence_transformers.sparse_encoder.losses.SparseCoSENTLoss "sentence_transformers.sparse_encoder.losses.SparseCoSENTLoss") is AnglELoss with [`pairwise_cos_sim`] as the metric, rather than [`pairwise_angle_sim`].

    Example

    :::: 
    ::: highlight
        from datasets import Dataset

        from sentence_transformers.sparse_encoder import SparseEncoder, SparseEncoderTrainer, losses

        model = SparseEncoder("distilbert/distilbert-base-uncased")
        train_dataset = Dataset.from_dict(
            
        )
        loss = losses.SpladeLoss(
            model=model, loss=losses.SparseAnglELoss(model), document_regularizer_weight=5e-5, use_document_regularizer_only=True
        )

        trainer = SparseEncoderTrainer(model=model, train_dataset=train_dataset, loss=loss)
        trainer.train()
    :::
    ::::

## SparseMSELoss[ïƒ?](#sparsemseloss "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.losses.]][[SparseMSELoss]][(]*[[model]][[:]][ ][[[SparseEncoder]](SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder.SparseEncoder")]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\sparse_encoder\losses\SparseMSELoss.py#L7-L59)[ïƒ?](#sentence_transformers.sparse_encoder.losses.SparseMSELoss "Link to this definition")

:   Computes the MSE loss between the computed sentence embedding and a target sentence embedding. This loss is used when extending sentence embeddings to new languages as described in our publication Making Monolingual Sentence Embeddings Multilingual using Knowledge Distillation.

    Parameters[:]

    :   **model** â€" SparseEncoder

    Requirements:

    :   1.  Usually uses a finetuned teacher M in a knowledge distillation setup

    Inputs:

    :   
          Texts                                     Labels
          ----------------------------------------- ---------------------------
          sentence                                  model sentence embeddings
          sentence_1, sentence_2, â€¦, sentence_N   model sentence embeddings

    Relations:

    :   - [[`SparseMarginMSELoss`]](#sentence_transformers.sparse_encoder.losses.SparseMarginMSELoss "sentence_transformers.sparse_encoder.losses.SparseMarginMSELoss") is equivalent to this loss, but with a margin through a negative pair.

    Example

    :::: 
    ::: highlight
        from datasets import Dataset
        from sentence_transformers.sparse_encoder import SparseEncoder, SparseEncoderTrainer, losses

        student_model = SparseEncoder("prithivida/Splade_PP_en_v1")
        teacher_model = SparseEncoder("naver/splade-cocondenser-ensembledistil")
        train_dataset = Dataset.from_dict(
            
        )

        def compute_labels(batch):
            return 

        train_dataset = train_dataset.map(compute_labels, batched=True)
        loss = losses.SparseMSELoss(student_model)

        trainer = SparseEncoderTrainer(model=student_model, train_dataset=train_dataset, loss=loss)
        trainer.train()
    :::
    ::::