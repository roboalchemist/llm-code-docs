# Test the function with the first SparseEmbedding
print(json.dumps(get_tokens_and_weights(sparse_embeddings_list[index], tokenizer), indent=4))

```

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-splade/\#dictionary-output) Dictionary output

The dictionary is then sorted by weights in descending order.

```python
{
    "chandra": 1.7163975238800049,
    "third": 1.5655333995819092,
    "##ya": 1.535199522972107,
    "india": 1.5310232639312744,
    "3": 1.385086178779602,
    "mission": 1.3676567077636719,
    "lunar": 1.3591278791427612,
    "moon": 1.2580504417419434,
    "indian": 1.1001816987991333,
    "##an": 1.015198826789856,
    "3rd": 0.7661278247833252,
    "was": 0.7177659273147583,
    "spacecraft": 0.7071069478988647,
    "space": 0.5978556871414185,
    "flight": 0.4988254904747009,
    "satellite": 0.4826201796531677,
    "first": 0.46230843663215637,
    "expedition": 0.4515230059623718,
    "three": 0.4467709958553314,
    "fourth": 0.44249090552330017,
    "vehicle": 0.390580952167511,
    "iii": 0.3862902522087097,
    "2": 0.36459630727767944,
    "##3": 0.2941221296787262,
    "planet": 0.27236196398735046,
    "second": 0.26897504925727844,
    "missions": 0.2608523368835449,
    "launched": 0.15740394592285156,
    "had": 0.12667948007583618,
    "largest": 0.09955651313066483,
    "leader": 0.09747757017612457,
    ",": 0.05297207832336426,
    "study": 0.02079751156270504,
    "-": 0.01963476650416851
}

```

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-splade/\#observations) Observations

- The relative order of importance is quite useful. The most important tokens in the sentence have the highest weights.
- **Term Expansion:** The model can expand the terms in the document. This means that the model can generate weights for tokens that are not present in the document but are related to the tokens in the document. This is a powerful feature that allows the model to capture the context of the document. Here, you’ll see that the model has added the tokens ‘3’ from ’third’ and ‘moon’ from ’lunar’ to the sparse vector.

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-splade/\#design-choices) Design choices

- The weights are not normalized. This means that the sum of the weights is not 1 or 100. This is a common practice in sparse embeddings, as it allows the model to capture the importance of each token in the document.
- Tokens are included in the sparse vector only if they are present in the model’s vocabulary. This means that the model will not generate a weight for tokens that it has not seen during training.
- Tokens do not map to words directly – allowing you to gracefully handle typo errors and out-of-vocabulary tokens.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/fastembed/fastembed-splade.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/fastembed/fastembed-splade.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-48-lllmstxt|>
## authentication
- [Documentation](https://qdrant.tech/documentation/)
- [Cloud](https://qdrant.tech/documentation/cloud/)
- Authentication