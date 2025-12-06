# Source: https://www.sbert.net/examples/cross_encoder/training/ms_marco/README.html

# MS MARCO[ïƒ?](#ms-marco "Link to this heading")

[MS MARCO Passage Ranking](https://github.com/microsoft/MSMARCO-Passage-Ranking) is a large dataset to train models for information retrieval. It consists of about 500k real search queries from Bing search engine with the relevant text passage that answers the query. This page shows how to **train** Cross Encoder models on this dataset so that it can be used for searching text passages given queries (key words, phrases or questions).

If you are interested in how to use these models, see [[Application - Retrieve & Re-Rank]](../../../sentence_transformer/applications/retrieve_rerank/README.html). There are **pre-trained models** available, which you can directly use without the need of training your own models. For more information, see [[Pretrained Cross-Encoders for MS MARCO]](../../../../docs/cross_encoder/pretrained_models.html#ms-marco).

## Cross Encoder[ïƒ?](#cross-encoder "Link to this heading")

A [Cross Encoder](../../applications/README.html) accepts both a query and a possible relevant passage and returns a score denoting how relevant the passage is for the given query. Often times, a [[`torch.nn.Sigmoid`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.Sigmoid.html#torch.nn.Sigmoid "(in PyTorch v2.9)") is applied over the raw output prediction, casting it to a value between 0 and 1.

![CrossEncoder](https://raw.githubusercontent.com/UKPLab/sentence-transformers/master/docs/img/CrossEncoder.png)

[[`CrossEncoder`]](../../../../docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder") models are often used for **re-ranking**: Given a list with possible relevant passages for a query, for example retrieved from a [[`SentenceTransformer`]](../../../../docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer") model / BM25 / Elasticsearch, the cross-encoder re-ranks this list so that the most relevant passages are the top of the result list.

## Training Scripts[ïƒ?](#training-scripts "Link to this heading")

We provide several training scripts with various loss functions to train a [[`CrossEncoder`]](../../../../docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder") on MS MARCO.

In all scripts, the model is evaluated on subsets of [MS MARCO](https://huggingface.co/datasets/sentence-transformers/NanoMSMARCO-bm25), [NFCorpus](https://huggingface.co/datasets/sentence-transformers/NanoNFCorpus-bm25), [NQ](https://huggingface.co/datasets/sentence-transformers/NanoNQ-bm25) via the [[`CrossEncoderNanoBEIREvaluator`]](../../../../docs/package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderNanoBEIREvaluator "sentence_transformers.cross_encoder.evaluation.CrossEncoderNanoBEIREvaluator").

- **[[training_ms_marco_bce_preprocessed.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/cross_encoder/training/ms_marco/training_ms_marco_bce_preprocessed.py)**:

  This example uses [[`BinaryCrossEntropyLoss`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss "sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss") on a [pre-processed MS MARCO dataset](https://huggingface.co/datasets/sentence-transformers/msmarco).

- **[[training_ms_marco_bce.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/cross_encoder/training/ms_marco/training_ms_marco_bce.py)**:

  This example also uses the [[`BinaryCrossEntropyLoss`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss "sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss"), but now the dataset pre-processing into [`(query,`]` `[`answer)`] with [`label`] as 1 or 0 is done in the training script.

- **[[training_ms_marco_cmnrl.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/cross_encoder/training/ms_marco/training_ms_marco_cmnrl.py)**:

  This example uses the [[`CachedMultipleNegativesRankingLoss`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.CachedMultipleNegativesRankingLoss "sentence_transformers.cross_encoder.losses.CachedMultipleNegativesRankingLoss"). The script applies dataset pre-processing into [`(query,`]` `[`answer,`]` `[`negative_1,`]` `[`negative_2,`]` `[`negative_3,`]` `[`negative_4,`]` `[`negative_5)`].

- **[[training_ms_marco_listnet.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/cross_encoder/training/ms_marco/training_ms_marco_listnet.py)**:

  This example uses the [[`ListNetLoss`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.ListNetLoss "sentence_transformers.cross_encoder.losses.ListNetLoss"). The script applies dataset pre-processing into [`(query,`]` `[`[doc1,`]` `[`doc2,`]` `[`...,`]` `[`docN])`] with [`labels`] as [`[score1,`]` `[`score2,`]` `[`...,`]` `[`scoreN]`].

- **[[training_ms_marco_lambda.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/cross_encoder/training/ms_marco/training_ms_marco_lambda.py)**:

  This example uses the [[`LambdaLoss`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.LambdaLoss "sentence_transformers.cross_encoder.losses.LambdaLoss") with the [[`NDCGLoss2PPScheme`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.NDCGLoss2PPScheme "sentence_transformers.cross_encoder.losses.NDCGLoss2PPScheme") loss scheme. The script applies dataset pre-processing into [`(query,`]` `[`[doc1,`]` `[`doc2,`]` `[`...,`]` `[`docN])`] with [`labels`] as [`[score1,`]` `[`score2,`]` `[`...,`]` `[`scoreN]`].

- **[[training_ms_marco_lambda_preprocessed.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/cross_encoder/training/ms_marco/training_ms_marco_lambda_preprocessed.py)**:

  This example uses the [[`LambdaLoss`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.LambdaLoss "sentence_transformers.cross_encoder.losses.LambdaLoss") with the [[`NDCGLoss2PPScheme`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.NDCGLoss2PPScheme "sentence_transformers.cross_encoder.losses.NDCGLoss2PPScheme") loss scheme on a [pre-processed MS MARCO dataset](https://huggingface.co/datasets/sentence-transformers/msmarco).

- **[[training_ms_marco_lambda_hard_neg.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/cross_encoder/training/ms_marco/training_ms_marco_lambda_hard_neg.py)**:

  This example extends the above example by increasing the size of the training dataset by mining hard negatives with [[`mine_hard_negatives()`]](../../../../docs/package_reference/util.html#sentence_transformers.util.mine_hard_negatives "sentence_transformers.util.mine_hard_negatives").

- **[[training_ms_marco_listmle.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/cross_encoder/training/ms_marco/training_ms_marco_listmle.py)**:

  This example uses the [[`ListMLELoss`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.ListMLELoss "sentence_transformers.cross_encoder.losses.ListMLELoss"). The script applies dataset pre-processing into [`(query,`]` `[`[doc1,`]` `[`doc2,`]` `[`...,`]` `[`docN])`] with [`labels`] as [`[score1,`]` `[`score2,`]` `[`...,`]` `[`scoreN]`].

- **[[training_ms_marco_plistmle.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/cross_encoder/training/ms_marco/training_ms_marco_plistmle.py)**:

  This example uses the [[`PListMLELoss`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.PListMLELoss "sentence_transformers.cross_encoder.losses.PListMLELoss") with the default [[`PListMLELambdaWeight`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.PListMLELambdaWeight "sentence_transformers.cross_encoder.losses.PListMLELambdaWeight") position weighting. The script applies dataset pre-processing into [`(query,`]` `[`[doc1,`]` `[`doc2,`]` `[`...,`]` `[`docN])`] with [`labels`] as [`[score1,`]` `[`score2,`]` `[`...,`]` `[`scoreN]`].

- **[[training_ms_marco_ranknet.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/cross_encoder/training/ms_marco/training_ms_marco_ranknet.py)**:

  This example uses the [[`RankNetLoss`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.RankNetLoss "sentence_transformers.cross_encoder.losses.RankNetLoss"). The script applies dataset pre-processing into [`(query,`]` `[`[doc1,`]` `[`doc2,`]` `[`...,`]` `[`docN])`] with [`labels`] as [`[score1,`]` `[`score2,`]` `[`...,`]` `[`scoreN]`].

Out of these training scripts, I suspect that **[[training_ms_marco_lambda_preprocessed.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/cross_encoder/training/ms_marco/training_ms_marco_lambda_preprocessed.py)**, **[[training_ms_marco_lambda_hard_neg.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/cross_encoder/training/ms_marco/training_ms_marco_lambda_hard_neg.py)** or **[[training_ms_marco_bce_preprocessed.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/cross_encoder/training/ms_marco/training_ms_marco_bce_preprocessed.py)** produces the strongest model, as anecdotally [`LambdaLoss`] and [`BinaryCrossEntropyLoss`] are quite strong. It seems that [`LambdaLoss`] \> [`PListMLELoss`] \> [`ListNetLoss`] \> [`RankNetLoss`] \> [`ListMLELoss`] out of all learning to rank losses, but your milage may vary.

Additionally, you can also train with Distillation. See [[Cross Encoder \> Training Examples \> Distillation]](../distillation/README.html) for more details.

## Inference[ïƒ?](#inference "Link to this heading")

You can perform inference using any of the [[pre-trained CrossEncoder models for MS MARCO]](../../../../docs/cross_encoder/pretrained_models.html#ms-marco) like so:

    from sentence_transformers import CrossEncoder

    # 1. Load a pre-trained CrossEncoder model
    model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")

    # 2. Predict scores for a pair of sentences
    scores = model.predict([
        ("How many people live in Berlin?", "Berlin had a population of 3,520,031 registered inhabitants in an area of 891.82 square kilometers."),
        ("How many people live in Berlin?", "Berlin is well known for its museums."),
    ])
    # => array([ 8.607138 , -4.3200774], dtype=float32)

    # 3. Rank a list of passages for a query
    query = "How many people live in Berlin?"
    passages = [
        "Berlin had a population of 3,520,031 registered inhabitants in an area of 891.82 square kilometers.",
        "Berlin is well known for its museums.",
        "In 2014, the city state Berlin had 37,368 live births (+6.6%), a record number since 1991.",
        "The urban area of Berlin comprised about 4.1 million people in 2014, making it the seventh most populous urban area in the European Union.",
        "The city of Paris had a population of 2,165,423 people within its administrative city limits as of January 1, 2019",
        "An estimated 300,000-420,000 Muslims reside in Berlin, making up about 8-11 percent of the population.",
        "Berlin is subdivided into 12 boroughs or districts (Bezirke).",
        "In 2015, the total labour force in Berlin was 1.85 million.",
        "In 2013 around 600,000 Berliners were registered in one of the more than 2,300 sport and fitness clubs.",
        "Berlin has a yearly total of about 135 million day visitors, which puts it in third place among the most-visited city destinations in the European Union.",
    ]
    ranks = model.rank(query, passages)

    # Print the scores
    print("Query:", query)
    for rank in ranks:
        print(f"\t")
    """
    Query: How many people live in Berlin?
    8.92    The urban area of Berlin comprised about 4.1 million people in 2014, making it the seventh most populous urban area in the European Union.
    8.61    Berlin had a population of 3,520,031 registered inhabitants in an area of 891.82 square kilometers.
    8.24    An estimated 300,000-420,000 Muslims reside in Berlin, making up about 8-11 percent of the population.
    7.60    In 2014, the city state Berlin had 37,368 live births (+6.6%), a record number since 1991.
    6.35    In 2013 around 600,000 Berliners were registered in one of the more than 2,300 sport and fitness clubs.
    5.42    Berlin has a yearly total of about 135 million day visitors, which puts it in third place among the most-visited city destinations in the European Union.
    3.45    In 2015, the total labour force in Berlin was 1.85 million.
    0.33    Berlin is subdivided into 12 boroughs or districts (Bezirke).
    -4.24   The city of Paris had a population of 2,165,423 people within its administrative city limits as of January 1, 2019
    -4.32   Berlin is well known for its museums.
    """