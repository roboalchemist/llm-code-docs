# Source: https://www.sbert.net/examples/sentence_transformer/applications/paraphrase-mining/README.html

# Paraphrase Mining[ïƒ?](#paraphrase-mining "Link to this heading")

Paraphrase mining is the task of finding paraphrases (texts with identical / similar meaning) in a large corpus of sentences. In [[Semantic Textual Similarity]](../../../../docs/sentence_transformer/usage/semantic_textual_similarity.html) we saw a simplified version of finding paraphrases in a list of sentences. The approach presented there used a brute-force approach to score and rank all pairs.

However, as this has a quadratic runtime, it fails to scale to large (10,000 and more) collections of sentences. For larger collections, the [[`paraphrase_mining()`]](#sentence_transformers.util.paraphrase_mining "sentence_transformers.util.paraphrase_mining") function can be used:

    from sentence_transformers import SentenceTransformer
    from sentence_transformers.util import paraphrase_mining

    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Single list of sentences - Possible tens of thousands of sentences
    sentences = [
        "The cat sits outside",
        "A man is playing guitar",
        "I love pasta",
        "The new movie is awesome",
        "The cat plays in the garden",
        "A woman watches TV",
        "The new movie is so great",
        "Do you like pizza?",
    ]

    paraphrases = paraphrase_mining(model, sentences)

    for paraphrase in paraphrases[0:10]:
        score, i, j = paraphrase
        print(" \t\t  \t\t Score: ".format(sentences[i], sentences[j], score))

The [[`paraphrase_mining()`]](#sentence_transformers.util.paraphrase_mining "sentence_transformers.util.paraphrase_mining") accepts the following parameters:

[[sentence_transformers.util.]][[paraphrase_mining]][(]*[model:] [SentenceTransformer,] [sentences:] [list\[str\],] [show_progress_bar:] [bool] [=] [False,] [batch_size:] [int] [=] [32,] [query_chunk_size:] [int] [=] [5000,] [corpus_chunk_size:] [int] [=] [100000,] [max_pairs:] [int] [=] [500000,] [top_k:] [int] [=] [100,] [score_function:] [Callable\[\[Tensor,] [Tensor\],] [Tensor\]] [=] [\<function] [cos_sim\>,] [truncate_dim:] [int] [\|] [None] [=] [None,] [prompt_name:] [str] [\|] [None] [=] [None,] [prompt:] [str] [\|] [None] [=] [None]*[)] [[→] [[list][[\[]][list][[\[]][float][ ][[\|]][ ][int][[\]]][[\]]]]][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers\util\retrieval.py#L23-L86)[ïƒ?](#sentence_transformers.util.paraphrase_mining "Link to this definition")

:   Given a list of sentences / texts, this function performs paraphrase mining. It compares all sentences against all other sentences and returns a list with the pairs that have the highest cosine similarity score.

    Parameters[:]

    :   - **model** ([*SentenceTransformer*](../../../../docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")) â€" SentenceTransformer model for embedding computation

        - **sentences** (*List\[str\]*) â€" A list of strings (texts or sentences)

        - **show_progress_bar** (*bool,* *optional*) â€" Plotting of a progress bar. Defaults to False.

        - **batch_size** (*int,* *optional*) â€" Number of texts that are encoded simultaneously by the model. Defaults to 32.

        - **query_chunk_size** (*int,* *optional*) â€" Search for most similar pairs for #query_chunk_size at the same time. Decrease, to lower memory footprint (increases run-time). Defaults to 5000.

        - **corpus_chunk_size** (*int,* *optional*) â€" Compare a sentence simultaneously against #corpus_chunk_size other sentences. Decrease, to lower memory footprint (increases run-time). Defaults to 100000.

        - **max_pairs** (*int,* *optional*) â€" Maximal number of text pairs returned. Defaults to 500000.

        - **top_k** (*int,* *optional*) â€" For each sentence, we retrieve up to top_k other sentences. Defaults to 100.

        - **score_function** (*Callable\[\[Tensor,* *Tensor\],* *Tensor\],* *optional*) â€" Function for computing scores. By default, cosine similarity. Defaults to cos_sim.

        - **truncate_dim** (*int,* *optional*) â€" The dimension to truncate sentence embeddings to. If None, uses the modelâ€™s ones. Defaults to None.

        - **prompt_name** (*Optional\[str\],* *optional*) â€"

          The name of a predefined prompt to use when encoding the sentence. It must match a key in the model prompts dictionary, which can be set during model initialization or loaded from the model configuration.

          Ignored if prompt is provided. Defaults to None.

        - **prompt** (*Optional\[str\],* *optional*) â€"

          A raw prompt string to prepend directly to the input sentence during encoding.

          For instance, prompt=â€?query: â€œ transforms the sentence â€œWhat is the capital of France?â€? into: â€œquery: What is the capital of France?â€?. Use this to override the prompt logic entirely and supply your own prefix. This takes precedence over prompt_name. Defaults to None.

    Returns[:]

    :   Returns a list of triplets with the format \[score, id1, id2\]

    Return type[:]

    :   List\[List\[Union\[float, int\]\]\]

To optimize memory and computation time, paraphrase mining is performed in chunks, as specified by [`query_chunk_size`] and [`corpus_chunk_size`]. To be specific, only [`query_chunk_size`]` `[`*`]` `[`corpus_chunk_size`] pairs will be compared at a time, rather than [`len(sentences)`]` `[`*`]` `[`len(sentences)`]. This is more time- and memory-efficient. Additionally, [[`paraphrase_mining()`]](#sentence_transformers.util.paraphrase_mining "sentence_transformers.util.paraphrase_mining") only considers the [`top_k`] best scores per sentences per chunk. You can experiment with this value as an efficiency-performance trade-off.

For example, for each sentence you will get only the one most relevant sentence in this script.

    paraphrases = paraphrase_mining(model, sentences, corpus_chunk_size=len(sentences), top_k=1)

The final key parameter is [`max_pairs`], which determines the maximum number of paraphrase pairs that the function returns. Usually, you get fewer pairs returned because the list is cleaned of duplicates, e.g., if it contains (A, B) and (B, A), then only one is returned.

Note

If B is the most similar sentence for A, A is not necessarily the most similar sentence for B. So it can happen that the returned list contains entries like (A, B) and (B, C).