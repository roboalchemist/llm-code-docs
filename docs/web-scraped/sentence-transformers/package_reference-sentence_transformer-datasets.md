# Source: https://www.sbert.net/docs/package_reference/sentence_transformer/datasets.html

# Datasets[ïƒ?](#datasets "Link to this heading")

Note

The [`sentence_transformers.datasets`] classes have been deprecated, and only exist for compatibility with the [deprecated training](../../sentence_transformer/training_overview.html#deprecated-training).

- Instead of [[`SentenceLabelDataset`]](#sentence_transformers.datasets.SentenceLabelDataset "sentence_transformers.datasets.SentenceLabelDataset"), you can now use [`BatchSamplers.GROUP_BY_LABEL`] to use the [[`GroupByLabelBatchSampler`]](sampler.html#sentence_transformers.sampler.GroupByLabelBatchSampler "sentence_transformers.sampler.GroupByLabelBatchSampler").

- Instead of [[`NoDuplicatesDataLoader`]](#sentence_transformers.datasets.NoDuplicatesDataLoader "sentence_transformers.datasets.NoDuplicatesDataLoader"), you can now use the [`BatchSamplers.NO_DUPLICATES`] to use the [[`NoDuplicatesBatchSampler`]](sampler.html#sentence_transformers.sampler.NoDuplicatesBatchSampler "sentence_transformers.sampler.NoDuplicatesBatchSampler").

[`sentence_transformers.datasets`] contains classes to organize your training input examples.

## ParallelSentencesDataset[ïƒ?](#parallelsentencesdataset "Link to this heading")

[`ParallelSentencesDataset`] is used for multilingual training. For details, see [[multilingual training]](../../../examples/sentence_transformer/training/multilingual/README.html).

*[class][ ]*[[sentence_transformers.datasets.]][[ParallelSentencesDataset]][(]*[[student_model]][[:]][ ][[[SentenceTransformer]](SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")]*, *[[teacher_model]][[:]][ ][[[SentenceTransformer]](SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")]*, *[[batch_size]][[:]][ ][[int]][ ][[=]][ ][[8]]*, *[[use_embedding_cache]][[:]][ ][[bool]][ ][[=]][ ][[True]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\datasets\ParallelSentencesDataset.py#L25-L204)[ïƒ?](#sentence_transformers.datasets.ParallelSentencesDataset "Link to this definition")

:   This dataset reader can be used to read-in parallel sentences, i.e., it reads in a file with tab-seperated sentences with the same sentence in different languages. For example, the file can look like this (EN DE ES): hello world hallo welt hola mundo second sentence zweiter satz segunda oraciÃ³n

    The sentence in the first column will be mapped to a sentence embedding using the given the embedder. For example, embedder is a mono-lingual sentence embedding method for English. The sentences in the other languages will also be mapped to this English sentence embedding.

    When getting a sample from the dataset, we get one sentence with the according sentence embedding for this sentence.

    teacher_model can be any class that implement an encode function. The encode function gets a list of sentences and returns a list of sentence embeddings

    Parallel sentences dataset reader to train student model given a teacher model

    Parameters[:]

    :   - **student_model** ([*SentenceTransformer*](SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")) â€" The student sentence embedding model that should be trained.

        - **teacher_model** ([*SentenceTransformer*](SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")) â€" The teacher model that provides the sentence embeddings for the first column in the dataset file.

        - **batch_size** (*int,* *optional*) â€" The batch size for training. Defaults to 8.

        - **use_embedding_cache** (*bool,* *optional*) â€" Whether to use an embedding cache. Defaults to True.

## SentenceLabelDataset[ïƒ?](#sentencelabeldataset "Link to this heading")

[`SentenceLabelDataset`] can be used if you have labeled sentences and want to train with triplet loss.

*[class][ ]*[[sentence_transformers.datasets.]][[SentenceLabelDataset]][(]*[[examples]][[:]][ ][[list][[\[]][InputExample][[\]]]]*, *[[samples_per_label]][[:]][ ][[int]][ ][[=]][ ][[2]]*, *[[with_replacement]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\datasets\SentenceLabelDataset.py#L23-L111)[ïƒ?](#sentence_transformers.datasets.SentenceLabelDataset "Link to this definition")

:   This dataset can be used for some specific Triplet Losses like BATCH_HARD_TRIPLET_LOSS which requires multiple examples with the same label in a batch.

    It draws n consecutive, random and unique samples from one label at a time. This is repeated for each label.

    Labels with fewer than n unique samples are ignored. This also applied to drawing without replacement, once less than n samples remain for a label, it is skipped.

    This *DOES NOT* check if there are more labels than the batch is large or if the batch size is divisible by the samples drawn per label.

    Creates a LabelSampler for a SentenceLabelDataset.

    Parameters[:]

    :   - **examples** (*List\[InputExample\]*) â€" A list of InputExamples.

        - **samples_per_label** (*int,* *optional*) â€" The number of consecutive, random, and unique samples drawn per label. The batch size should be a multiple of samples_per_label. Defaults to 2.

        - **with_replacement** (*bool,* *optional*) â€" If True, each sample is drawn at most once (depending on the total number of samples per label). If False, one sample can be drawn in multiple draws, but not multiple times in the same drawing. Defaults to False.

## DenoisingAutoEncoderDataset[ïƒ?](#denoisingautoencoderdataset "Link to this heading")

[`DenoisingAutoEncoderDataset`] is used for unsupervised training with the TSDAE method.

*[class][ ]*[[sentence_transformers.datasets.]][[DenoisingAutoEncoderDataset]][(]*[sentences:] [list\[str\],] [noise_fn=\<function] [DenoisingAutoEncoderDataset.\<lambda\>\>]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\datasets\DenoisingAutoEncoderDataset.py#L21-L62)[ïƒ?](#sentence_transformers.datasets.DenoisingAutoEncoderDataset "Link to this definition")

:   The DenoisingAutoEncoderDataset returns InputExamples in the format: texts=\[noise_fn(sentence), sentence\] It is used in combination with the DenoisingAutoEncoderLoss: Here, a decoder tries to re-construct the sentence without noise.

    Parameters[:]

    :   - **sentences** â€" A list of sentences

        - **noise_fn** â€" A noise function: Given a string, it returns a string with noise, e.g. deleted words

## NoDuplicatesDataLoader[ïƒ?](#noduplicatesdataloader "Link to this heading")

[`NoDuplicatesDataLoader`]can be used together with MultipleNegativeRankingLoss to ensure that no duplicates are within the same batch.

*[class][ ]*[[sentence_transformers.datasets.]][[NoDuplicatesDataLoader]][(]*[[train_examples]]*, *[[batch_size]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\datasets\NoDuplicatesDataLoader.py#L17-L60)[ïƒ?](#sentence_transformers.datasets.NoDuplicatesDataLoader "Link to this definition")

:   A special data loader to be used with MultipleNegativesRankingLoss. The data loader ensures that there are no duplicate sentences within the same batch