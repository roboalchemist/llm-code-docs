# Source: https://www.sbert.net/docs/sentence_transformer/dataset_overview.html

# Dataset Overview[ïƒ?](#dataset-overview "Link to this heading")

Hint

**Quickstart:** Find [curated datasets](https://huggingface.co/collections/sentence-transformers/embedding-model-datasets-6644d7a3673a511914aa7552) or [community datasets](https://huggingface.co/datasets?other=sentence-transformers), choose a loss function via this [loss overview](loss_overview.html), and [verify](training_overview.html#dataset-format) that it works with your dataset.

It is important that your dataset format matches your loss function (or that you choose a loss function that matches your dataset format). See [[Training Overview \> Dataset Format]](training_overview.html#dataset-format) to learn how to verify whether a dataset format works with a loss function.

In practice, most dataset configurations will take one of four forms:

- **Positive Pair**: A pair of related sentences. This can be used both for symmetric tasks (semantic textual similarity) or asymmetric tasks (semantic search), with examples including pairs of paraphrases, pairs of full texts and their summaries, pairs of duplicate questions, pairs of ([`query`], [`response`]), or pairs of ([`source_language`], [`target_language`]). Natural Language Inference datasets can also be formatted this way by pairing entailing sentences.

  - **Examples:** [sentence-transformers/sentence-compression](https://huggingface.co/datasets/sentence-transformers/sentence-compression), [sentence-transformers/coco-captions](https://huggingface.co/datasets/sentence-transformers/coco-captions), [sentence-transformers/codesearchnet](https://huggingface.co/datasets/sentence-transformers/codesearchnet), [sentence-transformers/natural-questions](https://huggingface.co/datasets/sentence-transformers/natural-questions), [sentence-transformers/gooaq](https://huggingface.co/datasets/sentence-transformers/gooaq), [sentence-transformers/squad](https://huggingface.co/datasets/sentence-transformers/squad), [sentence-transformers/wikihow](https://huggingface.co/datasets/sentence-transformers/wikihow), [sentence-transformers/eli5](https://huggingface.co/datasets/sentence-transformers/eli5)

- **Triplets**: (anchor, positive, negative) text triplets. These datasets donâ€™t need labels.

  - **Examples:** [sentence-transformers/quora-duplicates](https://huggingface.co/datasets/sentence-transformers/quora-duplicates), [nirantk/triplets](https://huggingface.co/datasets/nirantk/triplets), [sentence-transformers/all-nli](https://huggingface.co/datasets/sentence-transformers/all-nli)

- **Pair with Similarity Score**: A pair of sentences with a score indicating their similarity. Common examples are â€œSemantic Textual Similarityâ€? datasets.

  - **Examples:** [sentence-transformers/stsb](https://huggingface.co/datasets/sentence-transformers/stsb), [PhilipMay/stsb_multi_mt](https://huggingface.co/datasets/PhilipMay/stsb_multi_mt).

- **Texts with Classes**: A text with its corresponding class. This data format is easily converted by loss functions into three sentences (triplets) where the first is an â€œanchorâ€?, the second a â€œpositiveâ€? of the same class as the anchor, and the third a â€œnegativeâ€? of a different class.

  - **Examples:** [trec](https://huggingface.co/datasets/trec), [yahoo_answers_topics](https://huggingface.co/datasets/yahoo_answers_topics).

Note that it is often simple to transform a dataset from one format to another, such that it works with your loss function of choice.

Tip

You can use [[`mine_hard_negatives()`]](../package_reference/util.html#sentence_transformers.util.mine_hard_negatives "sentence_transformers.util.mine_hard_negatives") to convert a dataset of positive pairs into a dataset of triplets. It uses a [[`SentenceTransformer`]](../package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer") model to find hard negatives: texts that are similar to the first dataset column, but are not quite as similar as the text in the second dataset column. Datasets with hard triplets often outperform datasets with just positive pairs.

For example, we mined hard negatives from [sentence-transformers/gooaq](https://huggingface.co/datasets/sentence-transformers/gooaq) to produce [tomaarsen/gooaq-hard-negatives](https://huggingface.co/datasets/tomaarsen/gooaq-hard-negatives) and trained [tomaarsen/mpnet-base-gooaq](https://huggingface.co/tomaarsen/mpnet-base-gooaq) and [tomaarsen/mpnet-base-gooaq-hard-negatives](https://huggingface.co/tomaarsen/mpnet-base-gooaq-hard-negatives) on the two datasets, respectively. Sadly, the two models use a different evaluation split, so their performance canâ€™t be compared directly.

## Datasets on the Hugging Face Hub[ïƒ?](#datasets-on-the-hugging-face-hub "Link to this heading")

The [Datasets library](https://huggingface.co/docs/datasets/index) ([`pip`]` `[`install`]` `[`datasets`]) allows you to load datasets from the Hugging Face Hub with the [[`load_dataset()`]](https://huggingface.co/docs/datasets/main/en/package_reference/loading_methods#datasets.load_dataset "(in datasets vmain)") function:

    from datasets import load_dataset

    # Indicate the dataset id from the Hub
    dataset_id = "sentence-transformers/natural-questions"
    dataset = load_dataset(dataset_id, split="train")
    """
    Dataset()
    """
    print(dataset[0])
    """
    
    """

For more information on how to manipulate your dataset see the [Datasets Documentation](https://huggingface.co/docs/datasets/access).

Tip

Itâ€™s common for Hugging Face Datasets to contain extraneous columns, e.g. sample_id, metadata, source, type, etc. You can use [[`Dataset.remove_columns`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset.remove_columns "(in datasets vmain)") to remove these columns, as they will be used as inputs otherwise. You can also use [[`Dataset.select_columns`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset.select_columns "(in datasets vmain)") to keep only the desired columns.

## Pre-existing Datasets[ïƒ?](#pre-existing-datasets "Link to this heading")

The [Hugging Face Hub](https://huggingface.co/datasets) hosts 150k+ datasets, many of which can be converted for training embedding models. We are aiming to tag all Hugging Face datasets that work out of the box with Sentence Transformers with [`sentence-transformers`], allowing you to easily find them by browsing to [https://huggingface.co/datasets?other=sentence-transformers](https://huggingface.co/datasets?other=sentence-transformers). We strongly recommend that you browse these datasets to find training datasets that might be useful for your tasks.

These are some of the popular pre-existing datasets tagged as [`sentence-transformers`] that can be used to train and fine-tune SentenceTransformer models:

  Dataset                                                                                                                                                                  Description
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------
  [GooAQ](https://huggingface.co/datasets/sentence-transformers/gooaq)                                                                                                     (Question, Answer) pairs from Google auto suggest
  [Yahoo Answers](https://huggingface.co/datasets/sentence-transformers/yahoo-answers)                                                                                     (Title+Question, Answer), (Title, Answer), (Title, Question), (Question, Answer) pairs from Yahoo Answers
  [MS MARCO Triplets (msmarco-distilbert-base-tas-b)](https://huggingface.co/datasets/sentence-transformers/msmarco-msmarco-distilbert-base-tas-b)                         (Question, Answer, Negative) triplets from MS MARCO Passages dataset with mined negatives
  [MS MARCO Triplets (msmarco-distilbert-base-v3)](https://huggingface.co/datasets/sentence-transformers/msmarco-msmarco-distilbert-base-v3)                               (Question, Answer, Negative) triplets from MS MARCO Passages dataset with mined negatives
  [MS MARCO Triplets (msmarco-MiniLM-L6-v3)](https://huggingface.co/datasets/sentence-transformers/msmarco-msmarco-MiniLM-L6-v3)                                           (Question, Answer, Negative) triplets from MS MARCO Passages dataset with mined negatives
  [MS MARCO Triplets (distilbert-margin-mse-cls-dot-v2)](https://huggingface.co/datasets/sentence-transformers/msmarco-distilbert-margin-mse-cls-dot-v2)                   (Question, Answer, Negative) triplets from MS MARCO Passages dataset with mined negatives
  [MS MARCO Triplets (distilbert-margin-mse-cls-dot-v1)](https://huggingface.co/datasets/sentence-transformers/msmarco-distilbert-margin-mse-cls-dot-v1)                   (Question, Answer, Negative) triplets from MS MARCO Passages dataset with mined negatives
  [MS MARCO Triplets (distilbert-margin-mse-mean-dot-v1)](https://huggingface.co/datasets/sentence-transformers/msmarco-distilbert-margin-mse-mean-dot-v1)                 (Question, Answer, Negative) triplets from MS MARCO Passages dataset with mined negatives
  [MS MARCO Triplets (mpnet-margin-mse-mean-v1)](https://huggingface.co/datasets/sentence-transformers/msmarco-mpnet-margin-mse-mean-v1)                                   (Question, Answer, Negative) triplets from MS MARCO Passages dataset with mined negatives
  [MS MARCO Triplets (co-condenser-margin-mse-cls-v1)](https://huggingface.co/datasets/sentence-transformers/msmarco-co-condenser-margin-mse-cls-v1)                       (Question, Answer, Negative) triplets from MS MARCO Passages dataset with mined negatives
  [MS MARCO Triplets (distilbert-margin-mse-mnrl-mean-v1)](https://huggingface.co/datasets/sentence-transformers/msmarco-distilbert-margin-mse-mnrl-mean-v1)               (Question, Answer, Negative) triplets from MS MARCO Passages dataset with mined negatives
  [MS MARCO Triplets (distilbert-margin-mse-sym-mnrl-mean-v1)](https://huggingface.co/datasets/sentence-transformers/msmarco-distilbert-margin-mse-sym-mnrl-mean-v1)       (Question, Answer, Negative) triplets from MS MARCO Passages dataset with mined negatives
  [MS MARCO Triplets (distilbert-margin-mse-sym-mnrl-mean-v2)](https://huggingface.co/datasets/sentence-transformers/msmarco-distilbert-margin-mse-sym-mnrl-mean-v2)       (Question, Answer, Negative) triplets from MS MARCO Passages dataset with mined negatives
  [MS MARCO Triplets (co-condenser-margin-mse-sym-mnrl-mean-v1)](https://huggingface.co/datasets/sentence-transformers/msmarco-co-condenser-margin-mse-sym-mnrl-mean-v1)   (Question, Answer, Negative) triplets from MS MARCO Passages dataset with mined negatives
  [MS MARCO Triplets (BM25)](https://huggingface.co/datasets/sentence-transformers/msmarco-bm25)                                                                           (Question, Answer, Negative) triplets from MS MARCO Passages dataset with mined negatives
  [Stack Exchange Duplicates](https://huggingface.co/datasets/sentence-transformers/stackexchange-duplicates)                                                              (Title, Title), (Title+Body, Title+Body), (Body, Body) pairs of duplicate questions from StackExchange
  [ELI5](https://huggingface.co/datasets/sentence-transformers/eli5)                                                                                                       (Question, Answer) pairs from ELI5 dataset
  [SQuAD](https://huggingface.co/datasets/sentence-transformers/squad)                                                                                                     (Question, Answer) pairs from SQuAD dataset
  [WikiHow](https://huggingface.co/datasets/sentence-transformers/wikihow)                                                                                                 (Summary, Text) pairs from WikiHow
  [Amazon Reviews 2018](https://huggingface.co/datasets/sentence-transformers/amazon-reviews)                                                                              (Title, review) pairs from Amazon Reviews
  [Natural Questions](https://huggingface.co/datasets/sentence-transformers/natural-questions)                                                                             (Query, Answer) pairs from the Natural Questions dataset
  [Amazon QA](https://huggingface.co/datasets/sentence-transformers/amazon-qa)                                                                                             (Question, Answer) pairs from Amazon
  [S2ORC](https://huggingface.co/datasets/sentence-transformers/s2orc)                                                                                                     (Title, Abstract), (Abstract, Citation), (Title, Citation) pairs of scientific papers
  [Quora Duplicates](https://huggingface.co/datasets/sentence-transformers/quora-duplicates)                                                                               Duplicate question pairs from Quora
  [WikiAnswers](https://huggingface.co/datasets/sentence-transformers/wikianswers-duplicates)                                                                              Duplicate question pairs from WikiAnswers
  [AGNews](https://huggingface.co/datasets/sentence-transformers/agnews)                                                                                                   (Title, Description) pairs of news articles from the AG News dataset
  [AllNLI](https://huggingface.co/datasets/sentence-transformers/all-nli)                                                                                                  (Anchor, Entailment, Contradiction) triplets from SNLI + MultiNLI
  [NPR](https://huggingface.co/datasets/sentence-transformers/npr)                                                                                                         (Title, Body) pairs from the npr.org website
  [SPECTER](https://huggingface.co/datasets/sentence-transformers/specter)                                                                                                 (Title, Positive Title, Negative Title) triplets of Scientific Publications from Specter
  [Simple Wiki](https://huggingface.co/datasets/sentence-transformers/simple-wiki)                                                                                         (English, Simple English) pairs from Wikipedia
  [PAQ](https://huggingface.co/datasets/sentence-transformers/paq)                                                                                                         (Query, Answer) from the Probably-Asked Questions dataset
  [altlex](https://huggingface.co/datasets/sentence-transformers/altlex)                                                                                                   (English, Simple English) pairs from Wikipedia
  [CC News](https://huggingface.co/datasets/sentence-transformers/ccnews)                                                                                                  (Title, article) pairs from the CC News dataset
  [CodeSearchNet](https://huggingface.co/datasets/sentence-transformers/codesearchnet)                                                                                     (Comment, Code) pairs from open source libraries on GitHub
  [Sentence Compression](https://huggingface.co/datasets/sentence-transformers/sentence-compression)                                                                       (Long text, Short text) pairs from the Sentence Compression dataset
  [Trivia QA](https://huggingface.co/datasets/sentence-transformers/trivia-qa)                                                                                             (Query, Answer) pairs from the TriviaQA dataset
  [Flickr30k Captions](https://huggingface.co/datasets/sentence-transformers/flickr30k-captions)                                                                           Duplicate captions from the Flickr30k dataset
  [xsum](https://huggingface.co/datasets/sentence-transformers/xsum)                                                                                                       (News Article, Summary) pairs from XSUM dataset
  [Coco Captions](https://huggingface.co/datasets/sentence-transformers/coco-captions)                                                                                     Duplicate captions from the Coco Captions dataset
  [Parallel Sentences: Europarl](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-europarl)                                                        (English, Non-English) pairs across numerous languages
  [Parallel Sentences: Global Voices](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-global-voices)                                              (English, Non-English) pairs across numerous languages
  [Parallel Sentences: MUSE](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-muse)                                                                (English, Non-English) pairs across numerous languages
  [Parallel Sentences: JW300](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-jw300)                                                              (English, Non-English) pairs across numerous languages
  [Parallel Sentences: News Commentary](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-news-commentary)                                          (English, Non-English) pairs across numerous languages
  [Parallel Sentences: OpenSubtitles](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-opensubtitles)                                              (English, Non-English) pairs across numerous languages
  [Parallel Sentences: Talks](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks)                                                              (English, Non-English) pairs across numerous languages
  [Parallel Sentences: Tatoeba](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-tatoeba)                                                          (English, Non-English) pairs across numerous languages
  [Parallel Sentences: WikiMatrix](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-wikimatrix)                                                    (English, Non-English) pairs across numerous languages
  [Parallel Sentences: WikiTitles](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-wikititles)                                                    (English, Non-English) pairs across numerous languages

Note

We advise users to tag datasets that can be used for training embedding models with [`sentence-transformers`] by adding [`tags:`]` `[`sentence-transformers`]. We would also gladly accept high quality datasets to be added to the list above for all to see and use.