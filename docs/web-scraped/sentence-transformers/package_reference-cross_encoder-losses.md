# Source: https://www.sbert.net/docs/package_reference/cross_encoder/losses.html

# Losses[ïƒ?](#losses "Link to this heading")

[`sentence_transformers.cross_encoder.losses`] defines different loss functions that can be used to fine-tune cross-encoder models on training data. The choice of loss function plays a critical role when fine-tuning the model. It determines how well our model will work for the specific downstream task.

Sadly, there is no â€œone size fits allâ€? loss function. Which loss function is suitable depends on the available training data and on the target task. Consider checking out the [[Loss Overview]](../../cross_encoder/loss_overview.html) to help narrow down your choice of loss function(s).

## BinaryCrossEntropyLoss[ïƒ?](#binarycrossentropyloss "Link to this heading")

*[class][ ]*[[sentence_transformers.cross_encoder.losses.]][[BinaryCrossEntropyLoss]][(]*[[model]][[:]][ ][[[CrossEncoder]](cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder.CrossEncoder")]*, *[[activation_fn]][[:]][ ][[[Module]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")][ ][[=]][ ][[Identity()]]*, *[[pos_weight]][[:]][ ][[[Tensor]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\cross_encoder\losses\BinaryCrossEntropyLoss.py#L9-L116)[ïƒ?](#sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss "Link to this definition")

:   Computes the Binary Cross Entropy Loss for a CrossEncoder model. This loss is used to train a model to predict a high logit for positive pairs and a low logit for negative pairs. The model should be initialized with [`num_labels`]` `[`=`]` `[`1`] (a.k.a. the default) to predict one class.

    It has been used to train many of the strong [CrossEncoder MS MARCO Reranker models](https://huggingface.co/models?author=cross-encoder&search=marco).

    Parameters[:]

    :   - **model** ([[`CrossEncoder`]](cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")) â€" A CrossEncoder model to be trained.

        - **activation_fn** ([[`Module`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")) â€" Activation function applied to the logits before computing the loss. Defaults to [[`Identity`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Identity.html#torch.nn.Identity "(in PyTorch v2.9)").

        - **pos_weight** (*Tensor,* *optional*) â€" A weight of positive examples. Must be a [[`torch.Tensor`]](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.9)") like [`torch.tensor(4)`] for a weight of 4. Defaults to None.

        - **\*\*kwargs** â€" Additional keyword arguments passed to the underlying [[`torch.nn.BCEWithLogitsLoss`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.BCEWithLogitsLoss.html#torch.nn.BCEWithLogitsLoss "(in PyTorch v2.9)").

    References

    - [[`torch.nn.BCEWithLogitsLoss`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.BCEWithLogitsLoss.html#torch.nn.BCEWithLogitsLoss "(in PyTorch v2.9)")

    - [Cross Encoder \> Training Examples \> Semantic Textual Similarity](../../../examples/cross_encoder/training/sts/README.html)

    - [Cross Encoder \> Training Examples \> Quora Duplicate Questions](../../../examples/cross_encoder/training/quora_duplicate_questions/README.html)

    - [Cross Encoder \> Training Examples \> MS MARCO](../../../examples/cross_encoder/training/ms_marco/README.html)

    - [Cross Encoder \> Training Examples \> Rerankers](../../../examples/cross_encoder/training/rerankers/README.html)

    Requirements:

    :   1.  Your model must be initialized with num_labels = 1 (a.k.a. the default) to predict one class.

    Inputs:

    :   
          Texts                               Labels                                   Number of Model Output Labels
          ----------------------------------- ---------------------------------------- -------------------------------
          (anchor, positive/negative) pairs   1 if positive, 0 if negative             1
          (sentence_A, sentence_B) pairs      float similarity score between 0 and 1   1

    Recommendations:

    :   - Use [[`mine_hard_negatives`]](../util.html#sentence_transformers.util.mine_hard_negatives "sentence_transformers.util.mine_hard_negatives") with [`output_format="labeled-pair"`] to convert question-answer pairs to the [`(anchor,`]` `[`positive/negative)`]` `[`pairs`] format with labels as 1 or 0, using hard negatives.

    Example

    :::: 
    ::: highlight
        from sentence_transformers.cross_encoder import CrossEncoder, CrossEncoderTrainer, losses
        from datasets import Dataset

        model = CrossEncoder("microsoft/mpnet-base")
        train_dataset = Dataset.from_dict()
        loss = losses.BinaryCrossEntropyLoss(model)

        trainer = CrossEncoderTrainer(
            model=model,
            train_dataset=train_dataset,
            loss=loss,
        )
        trainer.train()
    :::
    ::::

## CrossEntropyLoss[ïƒ?](#crossentropyloss "Link to this heading")

*[class][ ]*[[sentence_transformers.cross_encoder.losses.]][[CrossEntropyLoss]][(]*[[model]][[:]][ ][[[CrossEncoder]](cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder.CrossEncoder")]*, *[[activation_fn]][[:]][ ][[[Module]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")][ ][[=]][ ][[Identity()]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\cross_encoder\losses\CrossEntropyLoss.py#L8-L84)[ïƒ?](#sentence_transformers.cross_encoder.losses.CrossEntropyLoss "Link to this definition")

:   Computes the Cross Entropy Loss for a CrossEncoder model. This loss is used to train a model to predict the correct class label for a given pair of sentences. The number of classes should be equal to the number of model output labels.

    Parameters[:]

    :   - **model** ([[`CrossEncoder`]](cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")) â€" A CrossEncoder model to be trained.

        - **activation_fn** ([[`Module`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")) â€" Activation function applied to the logits before computing the loss. Defaults to [[`Identity`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Identity.html#torch.nn.Identity "(in PyTorch v2.9)").

        - **\*\*kwargs** â€" Additional keyword arguments passed to the underlying [[`torch.nn.CrossEntropyLoss`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html#torch.nn.CrossEntropyLoss "(in PyTorch v2.9)").

    References

    - [[`torch.nn.CrossEntropyLoss`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html#torch.nn.CrossEntropyLoss "(in PyTorch v2.9)")

    - [Cross Encoder \> Training Examples \> Natural Language Inference](../../../examples/cross_encoder/training/nli/README.html)

    Requirements:

    :   1.  Your model can be initialized with num_labels \> 1 to predict multiple classes.

        2.  The number of dataset classes should be equal to the number of model output labels (model.num_labels).

    Inputs:

    :   
          Texts                            Labels   Number of Model Output Labels
          -------------------------------- -------- -------------------------------
          (sentence_A, sentence_B) pairs   class    num_classes

    Example

    :::: 
    ::: highlight
        from sentence_transformers.cross_encoder import CrossEncoder, CrossEncoderTrainer, losses
        from datasets import Dataset

        model = CrossEncoder("microsoft/mpnet-base", num_labels=2)
        train_dataset = Dataset.from_dict()
        loss = losses.CrossEntropyLoss(model)

        trainer = CrossEncoderTrainer(
            model=model,
            train_dataset=train_dataset,
            loss=loss,
        )
        trainer.train()
    :::
    ::::

## LambdaLoss[ïƒ?](#lambdaloss "Link to this heading")

*[class][ ]*[[sentence_transformers.cross_encoder.losses.]][[LambdaLoss]][(]*[[model:] [\~sentence_transformers.cross_encoder.CrossEncoder.CrossEncoder]]*, *[[weighting_scheme:] [\~sentence_transformers.cross_encoder.losses.LambdaLoss.BaseWeightingScheme] [\|] [None] [=] [NDCGLoss2PPScheme(]   [(ndcg_loss2):] [NDCGLoss2Scheme()]   [(lambda_rank):] [LambdaRankScheme()] [)]]*, *[[k:] [int] [\|] [None] [=] [None]]*, *[[sigma:] [float] [=] [1.0]]*, *[[eps:] [float] [=] [1e-10]]*, *[[reduction_log:] [\~typing.Literal\[\'natural\']]*, *[[\'binary\'\]] [=] [\'binary\']]*, *[[activation_fn:] [\~torch.nn.modules.module.Module] [\|] [None] [=] [Identity()]]*, *[[mini_batch_size:] [int] [\|] [None] [=] [None]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\cross_encoder\losses\LambdaLoss.py#L103-L360)[ïƒ?](#sentence_transformers.cross_encoder.losses.LambdaLoss "Link to this definition")

:   The LambdaLoss Framework for Ranking Metric Optimization. This loss function implements the LambdaLoss framework for ranking metric optimization, which provides various weighting schemes including LambdaRank and NDCG variations. The implementation is optimized to handle padded documents efficiently by only processing valid documents during model inference.

    ::: 
    Note

    The number of documents per query can vary between samples with the [`LambdaLoss`].
    :::

    Parameters[:]

    :   - **model** ([*CrossEncoder*](cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")) â€" CrossEncoder model to be trained

        - **weighting_scheme** ([[`BaseWeightingScheme`]](#sentence_transformers.cross_encoder.losses.LambdaLoss.BaseWeightingScheme "sentence_transformers.cross_encoder.losses.LambdaLoss.BaseWeightingScheme"), optional) â€"

          Weighting scheme to use for the loss.

          - [[`NoWeightingScheme`]](#sentence_transformers.cross_encoder.losses.NoWeightingScheme "sentence_transformers.cross_encoder.losses.NoWeightingScheme"): No weighting scheme (weights = 1.0)

          - [[`NDCGLoss1Scheme`]](#sentence_transformers.cross_encoder.losses.NDCGLoss1Scheme "sentence_transformers.cross_encoder.losses.NDCGLoss1Scheme"): NDCG Loss1 weighting scheme

          - [[`NDCGLoss2Scheme`]](#sentence_transformers.cross_encoder.losses.NDCGLoss2Scheme "sentence_transformers.cross_encoder.losses.NDCGLoss2Scheme"): NDCG Loss2 weighting scheme

          - [[`LambdaRankScheme`]](#sentence_transformers.cross_encoder.losses.LambdaRankScheme "sentence_transformers.cross_encoder.losses.LambdaRankScheme"): LambdaRank weighting scheme

          - [[`NDCGLoss2PPScheme`]](#sentence_transformers.cross_encoder.losses.NDCGLoss2PPScheme "sentence_transformers.cross_encoder.losses.NDCGLoss2PPScheme"): NDCG Loss2++ weighting scheme

          Defaults to NDCGLoss2PPScheme. In the original LambdaLoss paper, the NDCGLoss2PPScheme was shown to reach the strongest performance, with the NDCGLoss2Scheme following closely.

        - **k** (*int,* *optional*) â€" Number of documents to consider for NDCG@K. Defaults to None (use all documents).

        - **sigma** (*float*) â€" Score difference weight used in sigmoid

        - **eps** (*float*) â€" Small constant for numerical stability

        - **reduction_log** (*str*) â€" Type of logarithm to use - â€œnaturalâ€?: Natural logarithm (log) - â€œbinaryâ€?: Binary logarithm (log2)

        - **activation_fn** ([[`Module`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")) â€" Activation function applied to the logits before computing the loss. Defaults to [[`Identity`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Identity.html#torch.nn.Identity "(in PyTorch v2.9)").

        - **mini_batch_size** (*int,* *optional*) â€"

          Number of samples to process in each forward pass. This has a significant impact on the memory consumption and speed of the training process. Three cases are possible:

          - If [`mini_batch_size`] is None, the [`mini_batch_size`] is set to the batch size.

          - If [`mini_batch_size`] is greater than 0, the batch is split into mini-batches of size [`mini_batch_size`].

          - If [`mini_batch_size`] is \<= 0, the entire batch is processed at once.

          Defaults to None.

    References

    - The LambdaLoss Framework for Ranking Metric Optimization: [https://marc.najork.org/papers/cikm2018.pdf](https://marc.najork.org/papers/cikm2018.pdf)

    - Context-Aware Learning to Rank with Self-Attention: [https://huggingface.co/papers/2005.10084](https://huggingface.co/papers/2005.10084)

    - [Cross Encoder \> Training Examples \> MS MARCO](../../../examples/cross_encoder/training/ms_marco/README.html)

    Requirements:

    :   1.  Query with multiple documents (listwise approach)

        2.  Documents must have relevance scores/labels. Both binary and continuous labels are supported.

    Inputs:

    :   
          Texts                                Labels                            Number of Model Output Labels
          ------------------------------------ --------------------------------- -------------------------------
          (query, \[doc1, doc2, â€¦, docN\])   \[score1, score2, â€¦, scoreN\]   1

    Recommendations:

    :   - Use [[`mine_hard_negatives`]](../util.html#sentence_transformers.util.mine_hard_negatives "sentence_transformers.util.mine_hard_negatives") with [`output_format="labeled-list"`] to convert question-answer pairs to the required input format with hard negatives.

    Relations:

    :   - [[`LambdaLoss`]](#sentence_transformers.cross_encoder.losses.LambdaLoss "sentence_transformers.cross_encoder.losses.LambdaLoss") anecdotally performs better than the other losses with the same input format.

    Example

    :::: 
    ::: highlight
        from sentence_transformers.cross_encoder import CrossEncoder, CrossEncoderTrainer, losses
        from datasets import Dataset

        model = CrossEncoder("microsoft/mpnet-base")
        train_dataset = Dataset.from_dict()
        loss = losses.LambdaLoss(model)

        trainer = CrossEncoderTrainer(
            model=model,
            train_dataset=train_dataset,
            loss=loss,
        )
        trainer.train()
    :::
    ::::

<!-- -->

*[class][ ]*[[sentence_transformers.cross_encoder.losses.LambdaLoss.]][[BaseWeightingScheme]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\cross_encoder\losses\LambdaLoss.py#L12-L31)[ïƒ?](#sentence_transformers.cross_encoder.losses.LambdaLoss.BaseWeightingScheme "Link to this definition")

:   Base class for implementing weighting schemes in LambdaLoss.

<!-- -->

*[class][ ]*[[sentence_transformers.cross_encoder.losses.]][[NoWeightingScheme]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\cross_encoder\losses\LambdaLoss.py#L34-L38)[ïƒ?](#sentence_transformers.cross_encoder.losses.NoWeightingScheme "Link to this definition")

:   Implementation of no weighting scheme (weights = 1.0).

<!-- -->

*[class][ ]*[[sentence_transformers.cross_encoder.losses.]][[NDCGLoss1Scheme]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\cross_encoder\losses\LambdaLoss.py#L41-L50)[ïƒ?](#sentence_transformers.cross_encoder.losses.NDCGLoss1Scheme "Link to this definition")

:   Implementation of NDCG Loss1 weighting scheme.

    It is used to optimize for the NDCG metric, but this weighting scheme is not recommended as the NDCGLoss2Scheme and NDCGLoss2PPScheme were shown to reach superior performance in the original LambdaLoss paper.

<!-- -->

*[class][ ]*[[sentence_transformers.cross_encoder.losses.]][[NDCGLoss2Scheme]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\cross_encoder\losses\LambdaLoss.py#L53-L69)[ïƒ?](#sentence_transformers.cross_encoder.losses.NDCGLoss2Scheme "Link to this definition")

:   Implementation of NDCG Loss2 weighting scheme.

    This scheme uses a tighter bound than NDCGLoss1Scheme and was shown to reach superior performance in the original LambdaLoss paper. It is used to optimize for the NDCG metric.

<!-- -->

*[class][ ]*[[sentence_transformers.cross_encoder.losses.]][[LambdaRankScheme]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\cross_encoder\losses\LambdaLoss.py#L72-L81)[ïƒ?](#sentence_transformers.cross_encoder.losses.LambdaRankScheme "Link to this definition")

:   Implementation of LambdaRank weighting scheme.

    This weighting optimizes a coarse upper bound of NDCG.

<!-- -->

*[class][ ]*[[sentence_transformers.cross_encoder.losses.]][[NDCGLoss2PPScheme]][(]*[[mu]][[:]][ ][[float]][ ][[=]][ ][[10.0]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\cross_encoder\losses\LambdaLoss.py#L84-L100)[ïƒ?](#sentence_transformers.cross_encoder.losses.NDCGLoss2PPScheme "Link to this definition")

:   Implementation of NDCG Loss2++ weighting scheme.

    It is a hybrid weighting scheme that combines the NDCGLoss2 and LambdaRank schemes. It was shown to reach the strongest performance in the original LambdaLoss paper.

## ListMLELoss[ïƒ?](#listmleloss "Link to this heading")

*[class][ ]*[[sentence_transformers.cross_encoder.losses.]][[ListMLELoss]][(]*[[model]][[:]][ ][[[CrossEncoder]](cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder.CrossEncoder")]*, *[[activation_fn]][[:]][ ][[[Module]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[Identity()]]*, *[[mini_batch_size]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[respect_input_order]][[:]][ ][[bool]][ ][[=]][ ][[True]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\cross_encoder\losses\ListMLELoss.py#L9-L126)[ïƒ?](#sentence_transformers.cross_encoder.losses.ListMLELoss "Link to this definition")

:   This loss function implements the ListMLE learning to rank algorithm, which uses a list-wise approach based on maximum likelihood estimation of permutations. It maximizes the likelihood of the permutation induced by the ground truth labels.

    ::: 
    Note

    The number of documents per query can vary between samples with the [`ListMLELoss`].
    :::

    Parameters[:]

    :   - **model** ([*CrossEncoder*](cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")) â€" CrossEncoder model to be trained

        - **activation_fn** ([[`Module`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")) â€" Activation function applied to the logits before computing the loss. Defaults to [[`Identity`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Identity.html#torch.nn.Identity "(in PyTorch v2.9)").

        - **mini_batch_size** (*int,* *optional*) â€"

          Number of samples to process in each forward pass. This has a significant impact on the memory consumption and speed of the training process. Three cases are possible:

          - If [`mini_batch_size`] is None, the [`mini_batch_size`] is set to the batch size.

          - If [`mini_batch_size`] is greater than 0, the batch is split into mini-batches of size [`mini_batch_size`].

          - If [`mini_batch_size`] is \<= 0, the entire batch is processed at once.

          Defaults to None.

        - **respect_input_order** (*bool*) â€" Whether to respect the original input order of documents. If True, assumes the input documents are already ordered by relevance (most relevant first). If False, sorts documents by label values. Defaults to True.

    References

    - Listwise approach to learning to rank: theory and algorithm: [https://dl.acm.org/doi/abs/10.1145/1390156.1390306](https://dl.acm.org/doi/abs/10.1145/1390156.1390306)

    - [Cross Encoder \> Training Examples \> MS MARCO](../../../examples/cross_encoder/training/ms_marco/README.html)

    Requirements:

    :   1.  Query with multiple documents (listwise approach)

        2.  Documents must have relevance scores/labels. Both binary and continuous labels are supported.

        3.  Documents must be sorted in a defined rank order.

    Inputs:

    :   
          Texts                                Labels                            Number of Model Output Labels
          ------------------------------------ --------------------------------- -------------------------------
          (query, \[doc1, doc2, â€¦, docN\])   \[score1, score2, â€¦, scoreN\]   1

    Recommendations:

    :   - Use [[`mine_hard_negatives`]](../util.html#sentence_transformers.util.mine_hard_negatives "sentence_transformers.util.mine_hard_negatives") with [`output_format="labeled-list"`] to convert question-answer pairs to the required input format with hard negatives.

    Relations:

    :   - The [[`PListMLELoss`]](#sentence_transformers.cross_encoder.losses.PListMLELoss "sentence_transformers.cross_encoder.losses.PListMLELoss") is an extension of the [[`ListMLELoss`]](#sentence_transformers.cross_encoder.losses.ListMLELoss "sentence_transformers.cross_encoder.losses.ListMLELoss") and allows for positional weighting of the loss. [[`PListMLELoss`]](#sentence_transformers.cross_encoder.losses.PListMLELoss "sentence_transformers.cross_encoder.losses.PListMLELoss") generally outperforms [[`ListMLELoss`]](#sentence_transformers.cross_encoder.losses.ListMLELoss "sentence_transformers.cross_encoder.losses.ListMLELoss") and is recommended over it.

        - [[`LambdaLoss`]](#sentence_transformers.cross_encoder.losses.LambdaLoss "sentence_transformers.cross_encoder.losses.LambdaLoss") takes the same inputs, and generally outperforms this loss.

    Example

    :::: 
    ::: highlight
        from sentence_transformers.cross_encoder import CrossEncoder, CrossEncoderTrainer, losses
        from datasets import Dataset

        model = CrossEncoder("microsoft/mpnet-base")
        train_dataset = Dataset.from_dict()

        # Standard ListMLE loss respecting input order
        loss = losses.ListMLELoss(model)

        trainer = CrossEncoderTrainer(
            model=model,
            train_dataset=train_dataset,
            loss=loss,
        )
        trainer.train()
    :::
    ::::

## PListMLELoss[ïƒ?](#plistmleloss "Link to this heading")

*[class][ ]*[[sentence_transformers.cross_encoder.losses.]][[PListMLELoss]][(]*[[model]][[:]][ ][[[CrossEncoder]](cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder.CrossEncoder")]*, *[[lambda_weight]][[:]][ ][[[PListMLELambdaWeight]](#sentence_transformers.cross_encoder.losses.PListMLELambdaWeight "sentence_transformers.cross_encoder.losses.PListMLELoss.PListMLELambdaWeight")[ ][[\|]][ ][None]][ ][[=]][ ][[PListMLELambdaWeight()]]*, *[[activation_fn]][[:]][ ][[[Module]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[Identity()]]*, *[[mini_batch_size]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[respect_input_order]][[:]][ ][[bool]][ ][[=]][ ][[True]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\cross_encoder\losses\PListMLELoss.py#L45-L294)[ïƒ?](#sentence_transformers.cross_encoder.losses.PListMLELoss "Link to this definition")

:   PListMLE loss for learning to rank with position-aware weighting. This loss function implements the ListMLE ranking algorithm which uses a list-wise approach based on maximum likelihood estimation of permutations. It maximizes the likelihood of the permutation induced by the ground truth labels with position-aware weighting.

    This loss is also known as Position-Aware ListMLE or p-ListMLE.

    ::: 
    Note

    The number of documents per query can vary between samples with the [`PListMLELoss`].
    :::

    Parameters[:]

    :   - **model** ([*CrossEncoder*](cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")) â€" CrossEncoder model to be trained

        - **lambda_weight** ([*PListMLELambdaWeight*](#sentence_transformers.cross_encoder.losses.PListMLELambdaWeight "sentence_transformers.cross_encoder.losses.PListMLELoss.PListMLELambdaWeight")*,* *optional*) â€" Weighting scheme to use. When specified, implements Position-Aware ListMLE which applies different weights to different rank positions. Default is None (standard PListMLE).

        - **activation_fn** ([[`Module`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")) â€" Activation function applied to the logits before computing the loss. Defaults to [[`Identity`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Identity.html#torch.nn.Identity "(in PyTorch v2.9)").

        - **mini_batch_size** (*int,* *optional*) â€"

          Number of samples to process in each forward pass. This has a significant impact on the memory consumption and speed of the training process. Three cases are possible:

          - If [`mini_batch_size`] is None, the [`mini_batch_size`] is set to the batch size.

          - If [`mini_batch_size`] is greater than 0, the batch is split into mini-batches of size [`mini_batch_size`].

          - If [`mini_batch_size`] is \<= 0, the entire batch is processed at once.

          Defaults to None.

        - **respect_input_order** (*bool*) â€" Whether to respect the original input order of documents. If True, assumes the input documents are already ordered by relevance (most relevant first). If False, sorts documents by label values. Defaults to True.

    References

    - Position-Aware ListMLE: A Sequential Learning Process for Ranking: [https://auai.org/uai2014/proceedings/individuals/164.pdf](https://auai.org/uai2014/proceedings/individuals/164.pdf)

    - [Cross Encoder \> Training Examples \> MS MARCO](../../../examples/cross_encoder/training/ms_marco/README.html)

    Requirements:

    :   1.  Query with multiple documents (listwise approach)

        2.  Documents must have relevance scores/labels. Both binary and continuous labels are supported.

        3.  Documents must be sorted in a defined rank order.

    Inputs:

    :   
          Texts                                Labels                            Number of Model Output Labels
          ------------------------------------ --------------------------------- -------------------------------
          (query, \[doc1, doc2, â€¦, docN\])   \[score1, score2, â€¦, scoreN\]   1

    Recommendations:

    :   - Use [[`mine_hard_negatives`]](../util.html#sentence_transformers.util.mine_hard_negatives "sentence_transformers.util.mine_hard_negatives") with [`output_format="labeled-list"`] to convert question-answer pairs to the required input format with hard negatives.

    Relations:

    :   - The [[`PListMLELoss`]](#sentence_transformers.cross_encoder.losses.PListMLELoss "sentence_transformers.cross_encoder.losses.PListMLELoss") is an extension of the [[`ListMLELoss`]](#sentence_transformers.cross_encoder.losses.ListMLELoss "sentence_transformers.cross_encoder.losses.ListMLELoss") and allows for positional weighting of the loss. [[`PListMLELoss`]](#sentence_transformers.cross_encoder.losses.PListMLELoss "sentence_transformers.cross_encoder.losses.PListMLELoss") generally outperforms [[`ListMLELoss`]](#sentence_transformers.cross_encoder.losses.ListMLELoss "sentence_transformers.cross_encoder.losses.ListMLELoss") and is recommended over it.

        - [[`LambdaLoss`]](#sentence_transformers.cross_encoder.losses.LambdaLoss "sentence_transformers.cross_encoder.losses.LambdaLoss") takes the same inputs, and generally outperforms this loss.

    Example

    :::: 
    ::: highlight
        from sentence_transformers.cross_encoder import CrossEncoder, CrossEncoderTrainer, losses
        from datasets import Dataset

        model = CrossEncoder("microsoft/mpnet-base")
        train_dataset = Dataset.from_dict()

        # Either: Position-Aware ListMLE with default weighting
        lambda_weight = losses.PListMLELambdaWeight()
        loss = losses.PListMLELoss(model, lambda_weight=lambda_weight)

        # or: Position-Aware ListMLE with custom weighting function
        def custom_discount(ranks): # e.g. ranks: [1, 2, 3, 4, 5]
            return 1.0 / torch.log1p(ranks)
        lambda_weight = losses.PListMLELambdaWeight(rank_discount_fn=custom_discount)
        loss = losses.PListMLELoss(model, lambda_weight=lambda_weight)

        trainer = CrossEncoderTrainer(
            model=model,
            train_dataset=train_dataset,
            loss=loss,
        )
        trainer.train()
    :::
    ::::

<!-- -->

*[class][ ]*[[sentence_transformers.cross_encoder.losses.]][[PListMLELambdaWeight]][(]*[[rank_discount_fn]][[=]][[None]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\cross_encoder\losses\PListMLELoss.py#L10-L42)[ïƒ?](#sentence_transformers.cross_encoder.losses.PListMLELambdaWeight "Link to this definition")

:   Base class for implementing weighting schemes in Position-Aware ListMLE Loss.

    Initialize a lambda weight for PListMLE loss.

    Parameters[:]

    :   **rank_discount_fn** â€" Function that computes a discount for each rank position. If None, uses default discount of 2\^(num_docs - rank) - 1.

## ListNetLoss[ïƒ?](#listnetloss "Link to this heading")

*[class][ ]*[[sentence_transformers.cross_encoder.losses.]][[ListNetLoss]][(]*[[model]][[:]][ ][[[CrossEncoder]](cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder.CrossEncoder")]*, *[[activation_fn]][[:]][ ][[[Module]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[Identity()]]*, *[[mini_batch_size]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\cross_encoder\losses\ListNetLoss.py#L10-L197)[ïƒ?](#sentence_transformers.cross_encoder.losses.ListNetLoss "Link to this definition")

:   ListNet loss for learning to rank. This loss function implements the ListNet ranking algorithm which uses a list-wise approach to learn ranking models. It minimizes the cross entropy between the predicted ranking distribution and the ground truth ranking distribution. The implementation is optimized to handle padded documents efficiently by only processing valid documents during model inference.

    ::: 
    Note

    The number of documents per query can vary between samples with the [`ListNetLoss`].
    :::

    Parameters[:]

    :   - **model** ([*CrossEncoder*](cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")) â€" CrossEncoder model to be trained

        - **activation_fn** ([[`Module`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")) â€" Activation function applied to the logits before computing the loss. Defaults to [[`Identity`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Identity.html#torch.nn.Identity "(in PyTorch v2.9)").

        - **mini_batch_size** (*int,* *optional*) â€"

          Number of samples to process in each forward pass. This has a significant impact on the memory consumption and speed of the training process. Three cases are possible:

          - If [`mini_batch_size`] is None, the [`mini_batch_size`] is set to the batch size.

          - If [`mini_batch_size`] is greater than 0, the batch is split into mini-batches of size [`mini_batch_size`].

          - If [`mini_batch_size`] is \<= 0, the entire batch is processed at once.

          Defaults to None.

    References

    - Learning to Rank: From Pairwise Approach to Listwise Approach: [https://www.microsoft.com/en-us/research/publication/learning-to-rank-from-pairwise-approach-to-listwise-approach/](https://www.microsoft.com/en-us/research/publication/learning-to-rank-from-pairwise-approach-to-listwise-approach/)

    - Context-Aware Learning to Rank with Self-Attention: [https://huggingface.co/papers/2005.10084](https://huggingface.co/papers/2005.10084)

    - [Cross Encoder \> Training Examples \> MS MARCO](../../../examples/cross_encoder/training/ms_marco/README.html)

    Requirements:

    :   1.  Query with multiple documents (listwise approach)

        2.  Documents must have relevance scores/labels. Both binary and continuous labels are supported.

    Inputs:

    :   
          Texts                                Labels                            Number of Model Output Labels
          ------------------------------------ --------------------------------- -------------------------------
          (query, \[doc1, doc2, â€¦, docN\])   \[score1, score2, â€¦, scoreN\]   1

    Recommendations:

    :   - Use [[`mine_hard_negatives`]](../util.html#sentence_transformers.util.mine_hard_negatives "sentence_transformers.util.mine_hard_negatives") with [`output_format="labeled-list"`] to convert question-answer pairs to the required input format with hard negatives.

    Relations:

    :   - [[`LambdaLoss`]](#sentence_transformers.cross_encoder.losses.LambdaLoss "sentence_transformers.cross_encoder.losses.LambdaLoss") takes the same inputs, and generally outperforms this loss.

    Example

    :::: 
    ::: highlight
        from sentence_transformers.cross_encoder import CrossEncoder, CrossEncoderTrainer, losses
        from datasets import Dataset

        model = CrossEncoder("microsoft/mpnet-base")
        train_dataset = Dataset.from_dict()
        loss = losses.ListNetLoss(model)

        trainer = CrossEncoderTrainer(
            model=model,
            train_dataset=train_dataset,
            loss=loss,
        )
        trainer.train()
    :::
    ::::

## MultipleNegativesRankingLoss[ïƒ?](#multiplenegativesrankingloss "Link to this heading")

*[class][ ]*[[sentence_transformers.cross_encoder.losses.]][[MultipleNegativesRankingLoss]][(]*[[model]][[:]][ ][[[CrossEncoder]](cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder.CrossEncoder")]*, *[[num_negatives]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[4]]*, *[[scale]][[:]][ ][[int]][ ][[=]][ ][[10.0]]*, *[[activation_fn]][[:]][ ][[[Module]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[Sigmoid()]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\cross_encoder\losses\MultipleNegativesRankingLoss.py#L12-L191)[ïƒ?](#sentence_transformers.cross_encoder.losses.MultipleNegativesRankingLoss "Link to this definition")

:   Given a list of (anchor, positive) pairs or (anchor, positive, negative) triplets, this loss optimizes the following:

    - Given an anchor (e.g. a question), assign the highest similarity to the corresponding positive (i.e. answer) out of every single positive and negative (e.g. all answers) in the batch.

    If you provide the optional negatives, they will all be used as extra options from which the model must pick the correct positive. Within reason, the harder this â€œpickingâ€? is, the stronger the model will become. Because of this, a higher batch size results in more in-batch negatives, which then increases performance (to a point).

    This loss function works great to train embeddings for retrieval setups where you have positive pairs (e.g. (query, answer)) as it will sample in each batch [`n-1`] negative docs randomly.

    This loss is also known as InfoNCE loss, SimCSE loss, Cross-Entropy Loss with in-batch negatives, or simply in-batch negatives loss.

    Parameters[:]

    :   - **model** ([[`CrossEncoder`]](cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")) â€" A CrossEncoder model to be trained.

        - **num_negatives** (*int,* *optional*) â€" Number of in-batch negatives to sample for each anchor. Defaults to 4.

        - **scale** (*int,* *optional*) â€" Output of similarity function is multiplied by scale value. Defaults to 10.0.

        - **activation_fn** ([[`Module`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")) â€" Activation function applied to the logits before computing the loss. Defaults to [[`Sigmoid`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Sigmoid.html#torch.nn.Sigmoid "(in PyTorch v2.9)").

    ::: 
    Note

    The current default values are subject to change in the future. Experimentation is encouraged.
    :::

    References

    - Efficient Natural Language Response Suggestion for Smart Reply, Section 4.4: [https://huggingface.co/papers/1705.00652](https://huggingface.co/papers/1705.00652)

    Requirements:

    :   1.  Your model must be initialized with num_labels = 1 (a.k.a. the default) to predict one class.

    Inputs:

    :   
          Texts                                             Labels   Number of Model Output Labels
          ------------------------------------------------- -------- -------------------------------
          (anchor, positive) pairs                          none     1
          (anchor, positive, negative) triplets             none     1
          (anchor, positive, negative_1, â€¦, negative_n)   none     1

    Recommendations:

    :   - Use [`BatchSamplers.NO_DUPLICATES`] ([[`docs`]](../sentence_transformer/sampler.html#sentence_transformers.training_args.BatchSamplers "sentence_transformers.training_args.BatchSamplers")) to ensure that no in-batch negatives are duplicates of the anchor or positive samples.

        - Use [[`mine_hard_negatives`]](../util.html#sentence_transformers.util.mine_hard_negatives "sentence_transformers.util.mine_hard_negatives") with [`output_format="n-tuple"`] or [`output_format="triplet"`] to convert question-answer pairs to triplets with hard negatives.

    Relations:

    :   - [[`CachedMultipleNegativesRankingLoss`]](#sentence_transformers.cross_encoder.losses.CachedMultipleNegativesRankingLoss "sentence_transformers.cross_encoder.losses.CachedMultipleNegativesRankingLoss") is equivalent to this loss, but it uses caching that allows for much higher batch sizes (and thus better performance) without extra memory usage. However, it is slightly slower.

    Example

    :::: 
    ::: highlight
        from sentence_transformers.cross_encoder import CrossEncoder, CrossEncoderTrainer, losses
        from datasets import Dataset

        model = CrossEncoder("microsoft/mpnet-base")
        train_dataset = Dataset.from_dict()
        loss = losses.MultipleNegativesRankingLoss(model)

        trainer = CrossEncoderTrainer(
            model=model,
            train_dataset=train_dataset,
            loss=loss,
        )
        trainer.train()
    :::
    ::::

## CachedMultipleNegativesRankingLoss[ïƒ?](#cachedmultiplenegativesrankingloss "Link to this heading")

*[class][ ]*[[sentence_transformers.cross_encoder.losses.]][[CachedMultipleNegativesRankingLoss]][(]*[[model]][[:]][ ][[[CrossEncoder]](cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder.CrossEncoder")]*, *[[num_negatives]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[4]]*, *[[scale]][[:]][ ][[float]][ ][[=]][ ][[10.0]]*, *[[activation_fn]][[:]][ ][[[Module]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[Sigmoid()]]*, *[[mini_batch_size]][[:]][ ][[int]][ ][[=]][ ][[32]]*, *[[show_progress_bar]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\cross_encoder\losses\CachedMultipleNegativesRankingLoss.py#L62-L281)[ïƒ?](#sentence_transformers.cross_encoder.losses.CachedMultipleNegativesRankingLoss "Link to this definition")

:   Boosted version of [[`MultipleNegativesRankingLoss`]](#sentence_transformers.cross_encoder.losses.MultipleNegativesRankingLoss "sentence_transformers.cross_encoder.losses.MultipleNegativesRankingLoss") that caches the gradients of the logits wrt. the loss. This allows for much higher batch sizes without extra memory usage. However, it is slightly slower.

    In detail:

    > ::: 
    > 1.  It first does a quick prediction step without gradients/computation graphs to get all the logits;
    >
    > 2.  Calculate the loss, backward up to the logits and cache the gradients wrt. to the logits;
    >
    > 3.  A 2nd prediction step with gradients/computation graphs and connect the cached gradients into the backward chain.
    > :::

    Notes: All steps are done with mini-batches. In the original implementation of GradCache, (2) is not done in mini-batches and requires a lot memory when the batch size is large. The gradient caching will sacrifice around 20% computation time according to the paper.

    Given a list of (anchor, positive) pairs or (anchor, positive, negative) triplets, this loss optimizes the following:

    - Given an anchor (e.g. a question), assign the highest similarity to the corresponding positive (i.e. answer) out of every single positive and negative (e.g. all answers) in the batch.

    If you provide the optional negatives, they will all be used as extra options from which the model must pick the correct positive. Within reason, the harder this â€œpickingâ€? is, the stronger the model will become. Because of this, a higher batch size results in more in-batch negatives, which then increases performance (to a point).

    This loss function works great to train embeddings for retrieval setups where you have positive pairs (e.g. (query, answer)) as it will sample in each batch [`n-1`] negative docs randomly.

    This loss is also known as InfoNCE loss with GradCache.

    Parameters[:]

    :   - **model** ([[`CrossEncoder`]](cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")) â€" A CrossEncoder model to be trained.

        - **num_negatives** (*int,* *optional*) â€" Number of in-batch negatives to sample for each anchor. Defaults to 4.

        - **scale** (*int,* *optional*) â€" Output of similarity function is multiplied by scale value. Defaults to 10.0.

        - **activation_fn** ([[`Module`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")) â€" Activation function applied to the logits before computing the loss. Defaults to [[`Sigmoid`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Sigmoid.html#torch.nn.Sigmoid "(in PyTorch v2.9)").

        - **mini_batch_size** (*int,* *optional*) â€" Mini-batch size for the forward pass. This informs the memory usage. Defaults to 32.

        - **show_progress_bar** (*bool,* *optional*) â€" Whether to show a progress bar during the forward pass. Defaults to False.

    ::: 
    Note

    The current default values are subject to change in the future. Experimentation is encouraged.
    :::

    References

    - Efficient Natural Language Response Suggestion for Smart Reply, Section 4.4: [https://huggingface.co/papers/1705.00652](https://huggingface.co/papers/1705.00652)

    - Scaling Deep Contrastive Learning Batch Size under Memory Limited Setup: [https://huggingface.co/papers/2101.06983](https://huggingface.co/papers/2101.06983)

    - [Cross Encoder \> Training Examples \> MS MARCO](../../../examples/cross_encoder/training/ms_marco/README.html)

    - [Cross Encoder \> Training Examples \> Rerankers](../../../examples/cross_encoder/training/rerankers/README.html)

    Requirements:

    :   1.  Your model must be initialized with num_labels = 1 (a.k.a. the default) to predict one class.

        2.  Should be used with large per_device_train_batch_size and low mini_batch_size for superior performance, but slower training time than [[`MultipleNegativesRankingLoss`]](#sentence_transformers.cross_encoder.losses.MultipleNegativesRankingLoss "sentence_transformers.cross_encoder.losses.MultipleNegativesRankingLoss").

    Inputs:

    :   
          Texts                                             Labels   Number of Model Output Labels
          ------------------------------------------------- -------- -------------------------------
          (anchor, positive) pairs                          none     1
          (anchor, positive, negative) triplets             none     1
          (anchor, positive, negative_1, â€¦, negative_n)   none     1

    Recommendations:

    :   - Use [`BatchSamplers.NO_DUPLICATES`] ([[`docs`]](../sentence_transformer/sampler.html#sentence_transformers.training_args.BatchSamplers "sentence_transformers.training_args.BatchSamplers")) to ensure that no in-batch negatives are duplicates of the anchor or positive samples.

        - Use [[`mine_hard_negatives`]](../util.html#sentence_transformers.util.mine_hard_negatives "sentence_transformers.util.mine_hard_negatives") with [`output_format="n-tuple"`] or [`output_format="triplet"`] to convert question-answer pairs to triplets with hard negatives.

    Relations:

    :   - Equivalent to [[`MultipleNegativesRankingLoss`]](#sentence_transformers.cross_encoder.losses.MultipleNegativesRankingLoss "sentence_transformers.cross_encoder.losses.MultipleNegativesRankingLoss"), but with caching that allows for much higher batch sizes (and thus better performance) without extra memory usage. This loss also trains slower than [[`MultipleNegativesRankingLoss`]](#sentence_transformers.cross_encoder.losses.MultipleNegativesRankingLoss "sentence_transformers.cross_encoder.losses.MultipleNegativesRankingLoss").

    Example

    :::: 
    ::: highlight
        from sentence_transformers.cross_encoder import CrossEncoder, CrossEncoderTrainer, losses
        from datasets import Dataset

        model = CrossEncoder("microsoft/mpnet-base")
        train_dataset = Dataset.from_dict()
        loss = losses.CachedMultipleNegativesRankingLoss(model, mini_batch_size=32)

        trainer = CrossEncoderTrainer(
            model=model,
            train_dataset=train_dataset,
            loss=loss,
        )
        trainer.train()
    :::
    ::::

## MSELoss[ïƒ?](#mseloss "Link to this heading")

*[class][ ]*[[sentence_transformers.cross_encoder.losses.]][[MSELoss]][(]*[[model]][[:]][ ][[[CrossEncoder]](cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder.CrossEncoder")]*, *[[activation_fn]][[:]][ ][[[Module]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")][ ][[=]][ ][[Identity()]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\cross_encoder\losses\MSELoss.py#L9-L110)[ïƒ?](#sentence_transformers.cross_encoder.losses.MSELoss "Link to this definition")

:   Computes the MSE loss between the computed query-passage score and a target query-passage score. This loss is used to distill a cross-encoder model from a teacher cross-encoder model or gold labels.

    Parameters[:]

    :   - **model** ([[`CrossEncoder`]](cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")) â€" A CrossEncoder model to be trained.

        - **activation_fn** ([[`Module`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")) â€" Activation function applied to the logits before computing the loss.

        - **\*\*kwargs** â€" Additional keyword arguments passed to the underlying [[`torch.nn.MSELoss`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.MSELoss.html#torch.nn.MSELoss "(in PyTorch v2.9)").

    ::: 
    Note

    Be mindful of the magnitude of both the labels and what the model produces. If the teacher model produces logits with Sigmoid to bound them to \[0, 1\], then you may wish to use a Sigmoid activation function in the loss.
    :::

    References

    - Improving Efficient Neural Ranking Models with Cross-Architecture Knowledge Distillation: [https://huggingface.co/papers/2010.02666](https://huggingface.co/papers/2010.02666)

    - [Cross Encoder \> Training Examples \> Distillation](../../../examples/cross_encoder/training/distillation/README.html)

    Requirements:

    :   1.  Your model must be initialized with num_labels = 1 (a.k.a. the default) to predict one class.

        2.  Usually uses a finetuned CrossEncoder teacher M in a knowledge distillation setup.

    Inputs:

    :   
          Texts                            Labels             Number of Model Output Labels
          -------------------------------- ------------------ -------------------------------
          (sentence_A, sentence_B) pairs   similarity score   1

    Relations:

    :   - [[`MarginMSELoss`]](#sentence_transformers.cross_encoder.losses.MarginMSELoss "sentence_transformers.cross_encoder.losses.MarginMSELoss") is similar to this loss, but with a margin through a negative pair.

    Example

    :::: 
    ::: highlight
        from sentence_transformers.cross_encoder import CrossEncoder, CrossEncoderTrainer, losses
        from datasets import Dataset

        student_model = CrossEncoder("microsoft/mpnet-base")
        teacher_model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L12-v2")
        train_dataset = Dataset.from_dict()

        def compute_labels(batch):
            return 

        train_dataset = train_dataset.map(compute_labels, batched=True)
        loss = losses.MSELoss(student_model)

        trainer = CrossEncoderTrainer(
            model=student_model,
            train_dataset=train_dataset,
            loss=loss,
        )
        trainer.train()
    :::
    ::::

## MarginMSELoss[ïƒ?](#marginmseloss "Link to this heading")

*[class][ ]*[[sentence_transformers.cross_encoder.losses.]][[MarginMSELoss]][(]*[[model]][[:]][ ][[[CrossEncoder]](cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder.CrossEncoder")]*, *[[activation_fn]][[:]][ ][[[Module]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")][ ][[=]][ ][[Identity()]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\cross_encoder\losses\MarginMSELoss.py#L10-L177)[ïƒ?](#sentence_transformers.cross_encoder.losses.MarginMSELoss "Link to this definition")

:   Computes the MSE loss between [`|sim(Query,`]` `[`Pos)`]` `[`-`]` `[`sim(Query,`]` `[`Neg)|`] and [`|gold_sim(Query,`]` `[`Pos)`]` `[`-`]` `[`gold_sim(Query,`]` `[`Neg)|`]. This loss is often used to distill a cross-encoder model from a teacher cross-encoder model or gold labels.

    In contrast to [[`MultipleNegativesRankingLoss`]](#sentence_transformers.cross_encoder.losses.MultipleNegativesRankingLoss "sentence_transformers.cross_encoder.losses.MultipleNegativesRankingLoss"), the two passages do not have to be strictly positive and negative, both can be relevant or not relevant for a given query. This can be an advantage of MarginMSELoss over MultipleNegativesRankingLoss.

    ::: 
    Note

    Be mindful of the magnitude of both the labels and what the model produces. If the teacher model produces logits with Sigmoid to bound them to \[0, 1\], then you may wish to use a Sigmoid activation function in the loss.
    :::

    Parameters[:]

    :   - **model** ([[`CrossEncoder`]](cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")) â€" A CrossEncoder model to be trained.

        - **activation_fn** ([[`Module`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")) â€" Activation function applied to the logits before computing the loss.

        - **\*\*kwargs** â€" Additional keyword arguments passed to the underlying [[`torch.nn.MSELoss`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.MSELoss.html#torch.nn.MSELoss "(in PyTorch v2.9)").

    References

    - Improving Efficient Neural Ranking Models with Cross-Architecture Knowledge Distillation: [https://huggingface.co/papers/2010.02666](https://huggingface.co/papers/2010.02666)

    - [Cross Encoder \> Training Examples \> Distillation](../../../examples/cross_encoder/training/distillation/README.html)

    Requirements:

    :   1.  Your model must be initialized with num_labels = 1 (a.k.a. the default) to predict one class.

        2.  Usually uses a finetuned CrossEncoder teacher M in a knowledge distillation setup.

    Inputs:

    :   
          Texts                                            Labels                                                                                         Number of Model Output Labels
          ------------------------------------------------ ---------------------------------------------------------------------------------------------- -------------------------------
          (query, passage_one, passage_two) triplets       gold_sim(query, passage_one) - gold_sim(query, passage_two)                                    1
          (query, passage_one, passage_two) triplets       \[gold_sim(query, passage_one), gold_sim(query, passage_two)\]                                 1
          (query, positive, negative_1, â€¦, negative_n)   \[gold_sim(query, positive) - gold_sim(query, negative_i) for i in 1..n\]                      1
          (query, positive, negative_1, â€¦, negative_n)   \[gold_sim(query, positive), gold_sim(query, negative_1), â€¦, gold_sim(query, negative_n)\]   1

    Relations:

    :   - [[`MSELoss`]](#sentence_transformers.cross_encoder.losses.MSELoss "sentence_transformers.cross_encoder.losses.MSELoss") is similar to this loss, but without a margin through the negative pair.

    Example

    :::: 
    ::: highlight
        from sentence_transformers.cross_encoder import CrossEncoder, CrossEncoderTrainer, losses
        from datasets import Dataset

        student_model = CrossEncoder("microsoft/mpnet-base")
        teacher_model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L12-v2")
        train_dataset = Dataset.from_dict()

        def compute_labels(batch):
            positive_scores = teacher_model.predict(list(zip(batch["query"], batch["positive"])))
            negative_scores = teacher_model.predict(list(zip(batch["query"], batch["negative"])))
            return 

        train_dataset = train_dataset.map(compute_labels, batched=True)
        loss = losses.MarginMSELoss(student_model)

        trainer = CrossEncoderTrainer(
            model=student_model,
            train_dataset=train_dataset,
            loss=loss,
        )
        trainer.train()
    :::
    ::::

## RankNetLoss[ïƒ?](#ranknetloss "Link to this heading")

*[class][ ]*[[sentence_transformers.cross_encoder.losses.]][[RankNetLoss]][(]*[[model]][[:]][ ][[[CrossEncoder]](cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder.CrossEncoder")]*, *[[k]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[sigma]][[:]][ ][[float]][ ][[=]][ ][[1.0]]*, *[[eps]][[:]][ ][[float]][ ][[=]][ ][[1e-10]]*, *[[reduction_log]][[:]][ ][[Literal][[\[]][[\'natural\']][[,]][ ][[\'binary\']][[\]]]][ ][[=]][ ][[\'binary\']]*, *[[activation_fn]][[:]][ ][[[Module]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")[ ][[\|]][ ][None]][ ][[=]][ ][[Identity()]]*, *[[mini_batch_size]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\cross_encoder\losses\RankNetLoss.py#L11-L123)[ïƒ?](#sentence_transformers.cross_encoder.losses.RankNetLoss "Link to this definition")

:   RankNet loss implementation for learning to rank. This loss function implements the RankNet algorithm, which learns a ranking function by optimizing pairwise document comparisons using a neural network. The implementation is optimized to handle padded documents efficiently by only processing valid documents during model inference.

    Parameters[:]

    :   - **model** ([*CrossEncoder*](cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")) â€" CrossEncoder model to be trained

        - **sigma** (*float*) â€" Score difference weight used in sigmoid (default: 1.0)

        - **eps** (*float*) â€" Small constant for numerical stability (default: 1e-10)

        - **activation_fn** ([[`Module`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "(in PyTorch v2.9)")) â€" Activation function applied to the logits before computing the loss. Defaults to [[`Identity`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Identity.html#torch.nn.Identity "(in PyTorch v2.9)").

        - **mini_batch_size** (*int,* *optional*) â€" Number of samples to process in each forward pass. This has a significant impact on the memory consumption and speed of the training process. Three cases are possible: - If [`mini_batch_size`] is None, the [`mini_batch_size`] is set to the batch size. - If [`mini_batch_size`] is greater than 0, the batch is split into mini-batches of size [`mini_batch_size`]. - If [`mini_batch_size`] is \<= 0, the entire batch is processed at once. Defaults to None.

    References

    - Learning to Rank using Gradient Descent: [https://icml.cc/Conferences/2015/wp-content/uploads/2015/06/icml_ranking.pdf](https://icml.cc/Conferences/2015/wp-content/uploads/2015/06/icml_ranking.pdf)

    - [Cross Encoder \> Training Examples \> MS MARCO](../../../examples/cross_encoder/training/ms_marco/README.html)

    Requirements:

    :   1.  Query with multiple documents (pairwise approach)

        2.  Documents must have relevance scores/labels. Both binary and continuous labels are supported.

    Inputs:

    :   
          Texts                                Labels                            Number of Model Output Labels
          ------------------------------------ --------------------------------- -------------------------------
          (query, \[doc1, doc2, â€¦, docN\])   \[score1, score2, â€¦, scoreN\]   1

    Recommendations:

    :   - Use [[`mine_hard_negatives`]](../util.html#sentence_transformers.util.mine_hard_negatives "sentence_transformers.util.mine_hard_negatives") with [`output_format="labeled-list"`] to convert question-answer pairs to the required input format with hard negatives.

    Relations:

    :   - [[`LambdaLoss`]](#sentence_transformers.cross_encoder.losses.LambdaLoss "sentence_transformers.cross_encoder.losses.LambdaLoss") can be seen as an extension of this loss where each score pair is weighted. Alternatively, this loss can be seen as a special case of the [[`LambdaLoss`]](#sentence_transformers.cross_encoder.losses.LambdaLoss "sentence_transformers.cross_encoder.losses.LambdaLoss") without a weighting scheme.

        - [[`LambdaLoss`]](#sentence_transformers.cross_encoder.losses.LambdaLoss "sentence_transformers.cross_encoder.losses.LambdaLoss") with its default NDCGLoss2++ weighting scheme anecdotally performs better than the other losses with the same input format.

    Example

    :::: 
    ::: highlight
        from sentence_transformers.cross_encoder import CrossEncoder, CrossEncoderTrainer, losses
        from datasets import Dataset

        model = CrossEncoder("microsoft/mpnet-base")
        train_dataset = Dataset.from_dict()
        loss = losses.RankNetLoss(model)

        trainer = CrossEncoderTrainer(
            model=model,
            train_dataset=train_dataset,
            loss=loss,
        )
        trainer.train()
    :::
    ::::