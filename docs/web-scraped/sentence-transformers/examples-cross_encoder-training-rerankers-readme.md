# Source: https://www.sbert.net/examples/cross_encoder/training/rerankers/README.html

# Rerankers[ïƒ?](#rerankers "Link to this heading")

Reranker models are often [[`CrossEncoder`]](../../../../docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder") models with 1 output class, i.e. given a pair of texts (query, answer), the model outputs one score. This score, either a float score that reasonably ranges between -10.0 and 10.0, or a score thatâ€™s bound to 0â€¦1, denotes to what extent the answer can help answer the query.

Many reranker models are trained on MS MARCO:

- [MS MARCO Pre-trained Cross Encoders](../../../../docs/cross_encoder/pretrained_models.html#ms-marco)

- [Cross Encoder \> Training Examples \> MS MARCO](../ms_marco/README.html)

But most likely, you will get the best results when training on your dataset. Because of this, this page includes some examples training scripts that you can adopt for your own data:

- **[[training_gooaq_bce.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/cross_encoder/training/rerankers/training_gooaq_bce.py)**:

  This example uses [[`BinaryCrossEntropyLoss`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss "sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss") on labeled pair data that was mined from the [GooAQ](https://huggingface.co/datasets/sentence-transformers/gooaq) dataset using an efficient [`SentenceTransformers`].

  The model is evaluated on subsets of [MS MARCO](https://huggingface.co/datasets/sentence-transformers/NanoMSMARCO-bm25), [NFCorpus](https://huggingface.co/datasets/sentence-transformers/NanoNFCorpus-bm25), [NQ](https://huggingface.co/datasets/sentence-transformers/NanoNQ-bm25) via the [[`CrossEncoderNanoBEIREvaluator`]](../../../../docs/package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderNanoBEIREvaluator "sentence_transformers.cross_encoder.evaluation.CrossEncoderNanoBEIREvaluator"). Additionally, it is evaluated on the performance gain when reranking the top 100 results from an efficient [`SentenceTransformers`] on the GooAQ development set.

- **[[training_gooaq_cmnrl.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/cross_encoder/training/rerankers/training_gooaq_cmnrl.py)**:

  This example uses [[`CachedMultipleNegativesRankingLoss`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.CachedMultipleNegativesRankingLoss "sentence_transformers.cross_encoder.losses.CachedMultipleNegativesRankingLoss") on positive pair data loaded from the [GooAQ](https://huggingface.co/datasets/sentence-transformers/gooaq) dataset.

  The model is evaluated on subsets of [MS MARCO](https://huggingface.co/datasets/sentence-transformers/NanoMSMARCO-bm25), [NFCorpus](https://huggingface.co/datasets/sentence-transformers/NanoNFCorpus-bm25), [NQ](https://huggingface.co/datasets/sentence-transformers/NanoNQ-bm25) via the [[`CrossEncoderNanoBEIREvaluator`]](../../../../docs/package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderNanoBEIREvaluator "sentence_transformers.cross_encoder.evaluation.CrossEncoderNanoBEIREvaluator").

- **[[training_gooaq_lambda.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/cross_encoder/training/rerankers/training_gooaq_lambda.py)**:

  This example uses [[`LambdaLoss`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.LambdaLoss "sentence_transformers.cross_encoder.losses.LambdaLoss") on labeled list data that was mined from the [GooAQ](https://huggingface.co/datasets/sentence-transformers/gooaq) dataset using an efficient [`SentenceTransformers`].

  The model is evaluated on subsets of [MS MARCO](https://huggingface.co/datasets/sentence-transformers/NanoMSMARCO-bm25), [NFCorpus](https://huggingface.co/datasets/sentence-transformers/NanoNFCorpus-bm25), [NQ](https://huggingface.co/datasets/sentence-transformers/NanoNQ-bm25) via the [[`CrossEncoderNanoBEIREvaluator`]](../../../../docs/package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderNanoBEIREvaluator "sentence_transformers.cross_encoder.evaluation.CrossEncoderNanoBEIREvaluator"). Additionally, it is evaluated on the performance gain when reranking the top 100 results from an efficient [`SentenceTransformers`] on the GooAQ development set.

- **[[training_nq_bce.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/cross_encoder/training/rerankers/training_nq_bce.py)**:

  This example uses a near-identical training script as [`training_gooaq_bce.py`], except on the smaller [NQ (natural questions)](https://huggingface.co/datasets/sentence-transformers/natural-questions) dataset.

## BinaryCrossEntropyLoss[ïƒ?](#binarycrossentropyloss "Link to this heading")

The [[`BinaryCrossEntropyLoss`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss "sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss") is a very strong yet simple loss. Given pairs of texts (e.g. (query, answer) pairs), this loss uses the [[`CrossEncoder`]](../../../../docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder") model to compute prediction scores. It compares these against the gold (or silver, a.k.a. determined with some model) labels, and computes a lower loss the better the model is doing.

## CachedMultipleNegativesRankingLoss[ïƒ?](#cachedmultiplenegativesrankingloss "Link to this heading")

The [[`CachedMultipleNegativesRankingLoss`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.CachedMultipleNegativesRankingLoss "sentence_transformers.cross_encoder.losses.CachedMultipleNegativesRankingLoss") (a.k.a. InfoNCE with GradCache) is more complex than the common [[`BinaryCrossEntropyLoss`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss "sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss"). It accepts positive pairs (i.e. (query, answer) pairs) or triplets (i.e. (query, right_answer, wrong_answer) triplets), and will then randomly find [`num_negatives`] extra incorrect answers per query by taking answers from other questions in the batch. This is often referred to as â€œin-batch negativesâ€?.

The loss will then compute scores for all (query, answer) pairs, *including* the incorrect answers ones it just selected. The loss will then use a Cross Entropy Loss to ensure that the score of the (query, correct_answer) is higher than (query, wrong_answer) for all (randomly selected) wrong answers.

The [[`CachedMultipleNegativesRankingLoss`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.CachedMultipleNegativesRankingLoss "sentence_transformers.cross_encoder.losses.CachedMultipleNegativesRankingLoss") uses an approach called [GradCache](https://huggingface.co/papers/2101.06983) to allow computing the scores in mini-batches without increasing the memory usage excessively. This loss is recommended over the â€œstandardâ€? [[`MultipleNegativesRankingLoss`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.MultipleNegativesRankingLoss "sentence_transformers.cross_encoder.losses.MultipleNegativesRankingLoss") (a.k.a. InfoNCE) loss, which does not have this clever mini-batching support and thus requires a lot of memory.

Experimentation with an [`activation_fn`] and [`scale`] is warranted for this loss. [[`torch.nn.Sigmoid`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Sigmoid.html#torch.nn.Sigmoid "(in PyTorch v2.9)") with [`scale=10.0`] works okay, [`` torch.nn.Identity` ``] with [`scale=1.0`] also works, and the [mGTE](https://huggingface.co/papers/2407.19669) paper authors suggest using [[`torch.nn.Tanh`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Tanh.html#torch.nn.Tanh "(in PyTorch v2.9)") with [`scale=10.0`].

## Inference[ïƒ?](#inference "Link to this heading")

The [tomaarsen/reranker-ModernBERT-base-gooaq-bce](https://huggingface.co/tomaarsen/reranker-ModernBERT-base-gooaq-bce) model was trained with the first script. If you want to try out the model before training something yourself, feel free to use this script:

    from sentence_transformers import CrossEncoder

    # Download from the ð¤ Hub
    model = CrossEncoder("tomaarsen/reranker-ModernBERT-base-gooaq-bce")

    # Get scores for pairs of texts
    pairs = [
        ["how to obtain a teacher's certificate in texas?", 'Some aspiring educators may be confused about the difference between teaching certification and teaching certificates. Teacher certification is another term for the licensure required to teach in public schools, while a teaching certificate is awarded upon completion of an academic program.'],
        ["how to obtain a teacher's certificate in texas?", '["Step 1: Obtain a Bachelor\'s Degree. One of the most important Texas teacher qualifications is a bachelor\'s degree. ... ", \'Step 2: Complete an Educator Preparation Program (EPP) ... \', \'Step 3: Pass Texas Teacher Certification Exams. ... \', \'Step 4: Complete a Final Application and Background Check.\']'],
        ["how to obtain a teacher's certificate in texas?", "Washington Teachers Licensing Application Process Official transcripts showing proof of bachelor's degree. Proof of teacher program completion at an approved teacher preparation school. Passing scores on the required examinations. Completed application for teacher certification in Washington."],
        ["how to obtain a teacher's certificate in texas?", 'Teacher education programs may take 4 years to complete after which certification plans are prepared for a three year period. During this plan period, the teacher must obtain a Standard Certification within 1-2 years. Learn how to get certified to teach in Texas.'],
        ["how to obtain a teacher's certificate in texas?", 'In Texas, the minimum age to work is 14. Unlike some states, Texas does not require juvenile workers to obtain a child employment certificate or an age certificate to work. A prospective employer that wants one can request a certificate of age for any minors it employs, obtainable from the Texas Workforce Commission.'],
    ]
    scores = model.predict(pairs)
    print(scores)
    # [0.00121048 0.97105724 0.00536712 0.8632406  0.00168043]

    # Or rank different texts based on similarity to a single text
    ranks = model.rank(
        "how to obtain a teacher's certificate in texas?",
        [
            "[\"Step 1: Obtain a Bachelor's Degree. One of the most important Texas teacher qualifications is a bachelor's degree. ... \", 'Step 2: Complete an Educator Preparation Program (EPP) ... ', 'Step 3: Pass Texas Teacher Certification Exams. ... ', 'Step 4: Complete a Final Application and Background Check.']",
            "Teacher education programs may take 4 years to complete after which certification plans are prepared for a three year period. During this plan period, the teacher must obtain a Standard Certification within 1-2 years. Learn how to get certified to teach in Texas.",
            "Washington Teachers Licensing Application Process Official transcripts showing proof of bachelor's degree. Proof of teacher program completion at an approved teacher preparation school. Passing scores on the required examinations. Completed application for teacher certification in Washington.",
            "Some aspiring educators may be confused about the difference between teaching certification and teaching certificates. Teacher certification is another term for the licensure required to teach in public schools, while a teaching certificate is awarded upon completion of an academic program.",
            "In Texas, the minimum age to work is 14. Unlike some states, Texas does not require juvenile workers to obtain a child employment certificate or an age certificate to work. A prospective employer that wants one can request a certificate of age for any minors it employs, obtainable from the Texas Workforce Commission.",
        ],
    )
    print(ranks)
    # [
    #     ,
    #     ,
    #     ,
    #     ,
    #     ,
    # ]