# This triggers the model download
model = SparseTextEmbedding(model_name=model_name)

```

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-splade/\#embed-data) Embed data

You need to define a list of documents to be embedded.

```python
documents: list[str] = [\
    "Chandrayaan-3 is India's third lunar mission",\
    "It aimed to land a rover on the Moon's surface - joining the US, China and Russia",\
    "The mission is a follow-up to Chandrayaan-2, which had partial success",\
    "Chandrayaan-3 will be launched by the Indian Space Research Organisation (ISRO)",\
    "The estimated cost of the mission is around $35 million",\
    "It will carry instruments to study the lunar surface and atmosphere",\
    "Chandrayaan-3 landed on the Moon's surface on 23rd August 2023",\
    "It consists of a lander named Vikram and a rover named Pragyan similar to Chandrayaan-2. Its propulsion module would act like an orbiter.",\
    "The propulsion module carries the lander and rover configuration until the spacecraft is in a 100-kilometre (62 mi) lunar orbit",\
    "The mission used GSLV Mk III rocket for its launch",\
    "Chandrayaan-3 was launched from the Satish Dhawan Space Centre in Sriharikota",\
    "Chandrayaan-3 was launched earlier in the year 2023",\
]

```

Then, generate sparse embeddings for each document.
Here, `batch_size` is optional and helps to process documents in batches.

```python
sparse_embeddings_list: list[SparseEmbedding] = list(
    model.embed(documents, batch_size=6)
)

```

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-splade/\#retrieve-embeddings) Retrieve embeddings

`sparse_embeddings_list` contains sparse embeddings for the documents provided earlier. Each element in this list is a `SparseEmbedding` object that contains the sparse vector representation of a document.

```python
index = 0
sparse_embeddings_list[index]

```

This output is a `SparseEmbedding` object for the first document in our list. It contains two arrays: `values` and `indices`. \- The `values` array represents the weights of the features (tokens) in the document. - The `indices` array represents the indices of these features in the model’s vocabulary.

Each pair of corresponding `values` and `indices` represents a token and its weight in the document.

```python
SparseEmbedding(values=array([0.05297208, 0.01963477, 0.36459631, 1.38508618, 0.71776593,\
       0.12667948, 0.46230844, 0.446771  , 0.26897505, 1.01519883,\
       1.5655334 , 0.29412213, 1.53102326, 0.59785569, 1.1001817 ,\
       0.02079751, 0.09955651, 0.44249091, 0.09747757, 1.53519952,\
       1.36765671, 0.15740395, 0.49882549, 0.38629025, 0.76612782,\
       1.25805044, 0.39058095, 0.27236196, 0.45152301, 0.48262018,\
       0.26085234, 1.35912788, 0.70710695, 1.71639752]), indices=array([ 1010,  1011,  1016,  1017,  2001,  2018,  2034,  2093,  2117,\
        2319,  2353,  2509,  2634,  2686,  2796,  2817,  2922,  2959,\
        3003,  3148,  3260,  3390,  3462,  3523,  3822,  4231,  4316,\
        4774,  5590,  5871,  6416, 11926, 12076, 16469]))

```

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-splade/\#examine-weights) Examine weights

Now, print the first 5 features and their weights for better understanding.

```python
for i in range(5):
    print(f"Token at index {sparse_embeddings_list[0].indices[i]} has weight {sparse_embeddings_list[0].values[i]}")

```

The output will display the token indices and their corresponding weights for the first document.

```python
Token at index 1010 has weight 0.05297207832336426
Token at index 1011 has weight 0.01963476650416851
Token at index 1016 has weight 0.36459630727767944
Token at index 1017 has weight 1.385086178779602
Token at index 2001 has weight 0.7177659273147583

```

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-splade/\#analyze-results) Analyze results

Let’s use the tokenizer vocab to make sense of these indices.

```python
import json
from tokenizers import Tokenizer

tokenizer = Tokenizer.from_pretrained("Qdrant/Splade_PP_en_v1")

```

The `get_tokens_and_weights` function takes a `SparseEmbedding` object and a `tokenizer` as input. It will construct a dictionary where the keys are the decoded tokens, and the values are their corresponding weights.

```python
def get_tokens_and_weights(sparse_embedding, tokenizer):
    token_weight_dict = {}
    for i in range(len(sparse_embedding.indices)):
        token = tokenizer.decode([sparse_embedding.indices[i]])
        weight = sparse_embedding.values[i]
        token_weight_dict[token] = weight

    # Sort the dictionary by weights
    token_weight_dict = dict(sorted(token_weight_dict.items(), key=lambda item: item[1], reverse=True))
    return token_weight_dict