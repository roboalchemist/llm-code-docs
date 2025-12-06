# Source: https://www.sbert.net/index.html

Attention

Sentence Transformers is transitioning from [UKP Lab](http://www.ukp.tu-darmstadt.de/) to [ðŸ¤--- Hugging Face](https://huggingface.co). This formalizes the existing maintenance structure, as Hugging Face has been maintaining the project for the past two years. The projectâ€™s development roadmap, support, and commitment to the community remain unchanged. Read the [full announcement](https://huggingface.co/blog/sentence-transformers-joins-hf) for more details!

Note

Sentence Transformers v5.1 recently released, bringing the ONNX and OpenVINO backends to SparseEncoder models. Read [SparseEncoder \> Usage \> Speeding up Inference](docs/sparse_encoder/usage/efficiency.html) to read more about the performance boosts that you can expect, or read the [v5.1 Release Notes](https://github.com/huggingface/sentence-transformers/releases/tag/v5.1.0) for information on the other changes.

# SentenceTransformers Documentation[ïƒ?](#sentencetransformers-documentation "Link to this heading")

Sentence Transformers (a.k.a. SBERT) is the go-to Python module for accessing, using, and training state-of-the-art embedding and reranker models. It can be used to compute embeddings using Sentence Transformer models ([quickstart](docs/quickstart.html#sentence-transformer)), to calculate similarity scores using Cross-Encoder (a.k.a. reranker) models ([quickstart](docs/quickstart.html#cross-encoder)), or to generate sparse embeddings using Sparse Encoder models ([quickstart](docs/quickstart.html#sparse-encoder)). This unlocks a wide range of applications, including [semantic search](examples/sentence_transformer/applications/semantic-search/README.html), [semantic textual similarity](docs/sentence_transformer/usage/semantic_textual_similarity.html), and [paraphrase mining](examples/sentence_transformer/applications/paraphrase-mining/README.html).

A wide selection of over [10,000 pre-trained Sentence Transformers models](https://huggingface.co/models?library=sentence-transformers) are available for immediate use on ðŸ¤--- Hugging Face, including many of the state-of-the-art models from the [Massive Text Embeddings Benchmark (MTEB) leaderboard](https://huggingface.co/spaces/mteb/leaderboard). Additionally, it is easy to train or finetune your own [embedding models](docs/sentence_transformer/training_overview.html), [reranker models](docs/cross_encoder/training_overview.html), or [sparse encoder models](docs/sparse_encoder/training_overview.html) using Sentence Transformers, enabling you to create custom models for your specific use cases.

Sentence Transformers was created by [UKP Lab](http://www.ukp.tu-darmstadt.de/) and is being maintained by [ðŸ¤--- Hugging Face](https://huggingface.co). Donâ€™t hesitate to open an issue on the [Sentence Transformers repository](https://github.com/huggingface/sentence-transformers) if something is broken or if you have further questions.

# Usage[ïƒ?](#usage "Link to this heading")

See also

See the [Quickstart](docs/quickstart.html) for more quick information on how to use Sentence Transformers.

Working with Sentence Transformer models is straightforward:

Installation

You can install *sentence-transformers* using pip:

    pip install -U sentence-transformers

We recommend **Python 3.10+** and **PyTorch 1.11.0+**. See [installation](docs/installation.html) for further installation options.

Embedding Models

    from sentence_transformers import SentenceTransformer

    # 1. Load a pretrained Sentence Transformer model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # The sentences to encode
    sentences = [
        "The weather is lovely today.",
        "It's so sunny outside!",
        "He drove to the stadium.",
    ]

    # 2. Calculate embeddings by calling model.encode()
    embeddings = model.encode(sentences)
    print(embeddings.shape)
    # [3, 384]

    # 3. Calculate the embedding similarities
    similarities = model.similarity(embeddings, embeddings)
    print(similarities)
    # tensor([[1.0000, 0.6660, 0.1046],
    #         [0.6660, 1.0000, 0.1411],
    #         [0.1046, 0.1411, 1.0000]])

Reranker Models

    from sentence_transformers import CrossEncoder

    # 1. Load a pretrained CrossEncoder model
    model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")

    # The texts for which to predict similarity scores
    query = "How many people live in Berlin?"
    passages = [
        "Berlin had a population of 3,520,031 registered inhabitants in an area of 891.82 square kilometers.",
        "Berlin has a yearly total of about 135 million day visitors, making it one of the most-visited cities in the European Union.",
        "In 2013 around 600,000 Berliners were registered in one of the more than 2,300 sport and fitness clubs.",
    ]

    # 2a. Either predict scores pairs of texts
    scores = model.predict([(query, passage) for passage in passages])
    print(scores)
    # => [8.607139 5.506266 6.352977]

    # 2b. Or rank a list of passages for a query
    ranks = model.rank(query, passages, return_documents=True)

    print("Query:", query)
    for rank in ranks:
        print(f"- # (): ")
    """
    Query: How many people live in Berlin?
    - #0 (8.61): Berlin had a population of 3,520,031 registered inhabitants in an area of 891.82 square kilometers.
    - #2 (6.35): In 2013 around 600,000 Berliners were registered in one of the more than 2,300 sport and fitness clubs.
    - #1 (5.51): Berlin has a yearly total of about 135 million day visitors, making it one of the most-visited cities in the European Union.
    """

Sparse Encoder Models

    from sentence_transformers import SparseEncoder

    # 1. Load a pretrained SparseEncoder model
    model = SparseEncoder("naver/splade-cocondenser-ensembledistil")

    # The sentences to encode
    sentences = [
        "The weather is lovely today.",
        "It's so sunny outside!",
        "He drove to the stadium.",
    ]

    # 2. Calculate sparse embeddings by calling model.encode()
    embeddings = model.encode(sentences)
    print(embeddings.shape)
    # [3, 30522] - sparse representation with vocabulary size dimensions

    # 3. Calculate the embedding similarities
    similarities = model.similarity(embeddings, embeddings)
    print(similarities)
    # tensor([[   35.629,     9.154,     0.098],
    #         [    9.154,    27.478,     0.019],
    #         [    0.098,     0.019,    29.553]])

    # 4. Check sparsity stats
    stats = SparseEncoder.sparsity(embeddings)
    print(f"Sparsity: ")
    # Sparsity: 99.84%

# What Next?[ïƒ?](#what-next "Link to this heading")

Consider reading one of the following sections to answer the related questions:

- 

  Embedding Models:

  :   - How to **use** Sentence Transformer models? [Sentence Transformers \> Usage](docs/sentence_transformer/usage/usage.html)

      - What Sentence Transformer **models** can I use? [Sentence Transformers \> Pretrained Models](docs/sentence_transformer/pretrained_models.html)

      - How do I make Sentence Transformer models **faster**? [Sentence Transformers \> Usage \> Speeding up Inference](docs/sentence_transformer/usage/efficiency.html)

      - How do I **train/finetune** a Sentence Transformer model? [Sentence Transformers \> Training Overview](docs/sentence_transformer/training_overview.html)

- 

  Reranker Models:

  :   - How to **use** Cross Encoder models? [Cross Encoder \> Usage](docs/cross_encoder/usage/usage.html)

      - What Cross Encoder **models** can I use? [Cross Encoder \> Pretrained Models](docs/cross_encoder/pretrained_models.html)

      - How do I make Cross Encoder models **faster**? [Cross Encoder \> Usage \> Speeding up Inference](docs/cross_encoder/usage/efficiency.html)

      - How do I **train/finetune** a Cross Encoder model? [Cross Encoder \> Training Overview](docs/cross_encoder/training_overview.html)

- 

  Sparse Encoder Models:

  :   - How to **use** Sparse Encoder models? [Sparse Encoder \> Usage](docs/sparse_encoder/usage/usage.html)

      - What Sparse Encoder **models** can I use? [Sparse Encoder \> Pretrained Models](docs/sparse_encoder/pretrained_models.html)

      - How do I make Sparse Encoder models **faster**? [Sparse Encoder \> Usage \> Speeding up Inference](docs/sparse_encoder/usage/efficiency.html)

      - How do I **train/finetune** a Sparse Encoder model? [Sparse Encoder \> Training Overview](docs/sparse_encoder/training_overview.html)

      - How do I **integrate** Sparse Encoder models with search engines? [Sparse Encoder \> Vector Database Integration](examples/sparse_encoder/applications/semantic_search/README.html#vector-database-search)

# Citing[ïƒ?](#citing "Link to this heading")

If you find this repository helpful, feel free to cite our publication [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://huggingface.co/papers/1908.10084):

> ::::: 
> :::: 
> ::: highlight
>     @inproceedings
> :::
> ::::
> :::::

If you use one of the multilingual models, feel free to cite our publication [Making Monolingual Sentence Embeddings Multilingual using Knowledge Distillation](https://huggingface.co/papers/2004.09813):

> ::::: 
> :::: 
> ::: highlight
>     @inproceedings
> :::
> ::::
> :::::

If you use the code for [data augmentation](https://github.com/huggingface/sentence-transformers/tree/master/examples/sentence_transformer/training/data_augmentation), feel free to cite our publication [Augmented SBERT: Data Augmentation Method for Improving Bi-Encoders for Pairwise Sentence Scoring Tasks](https://huggingface.co/papers/2010.08240):

> ::::: 
> :::: 
> ::: highlight
>     @inproceedings: Data Augmentation Method for Improving Bi-Encoders for Pairwise Sentence Scoring Tasks",
>       author = "Thakur, Nandan and Reimers, Nils and Daxenberger, Johannes  and Gurevych, Iryna",
>       booktitle = "Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
>       month = jun,
>       year = "2021",
>       address = "Online",
>       publisher = "Association for Computational Linguistics",
>       url = "https://www.aclweb.org/anthology/2021.naacl-main.28",
>       pages = "296--310",
>     }
> :::
> ::::
> :::::