# Question Answering as a Service with Cohere and Qdrant

Kacper Łukawski

·

November 29, 2022

![Question Answering as a Service with Cohere and Qdrant](https://qdrant.tech/articles_data/qa-with-cohere-and-qdrant/preview/title.jpg)

Bi-encoders are probably the most efficient way of setting up a semantic Question Answering system.
This architecture relies on the same neural model that creates vector embeddings for both questions and answers.
The assumption is, both question and answer should have representations close to each other in the latent space.
It should be like that because they should both describe the same semantic concept. That doesn’t apply
to answers like “Yes” or “No” though, but standard FAQ-like problems are a bit easier as there is typically
an overlap between both texts. Not necessarily in terms of wording, but in their semantics.

![Bi-encoder structure. Both queries (questions) and documents (answers) are vectorized by the same neural encoder. Output embeddings are then compared by a chosen distance function, typically cosine similarity.](https://qdrant.tech/articles_data/qa-with-cohere-and-qdrant/biencoder-diagram.png)

And yeah, you need to **bring your own embeddings**, in order to even start. There are various ways how
to obtain them, but using Cohere [co.embed API](https://docs.cohere.ai/reference/embed) is probably
the easiest and most convenient method.

## [Anchor](https://qdrant.tech/articles/qa-with-cohere-and-qdrant/\#why-coembed-api-and-qdrant-go-well-together) Why co.embed API and Qdrant go well together?

Maintaining a **Large Language Model** might be hard and expensive. Scaling it up and down, when the traffic
changes, require even more effort and becomes unpredictable. That might be definitely a blocker for any semantic
search system. But if you want to start right away, you may consider using a SaaS model, Cohere’s
[co.embed API](https://docs.cohere.ai/reference/embed) in particular. It gives you state-of-the-art language
models available as a Highly Available HTTP service with no need to train or maintain your own service. As all
the communication is done with JSONs, you can simply provide the co.embed output as Qdrant input.

```python