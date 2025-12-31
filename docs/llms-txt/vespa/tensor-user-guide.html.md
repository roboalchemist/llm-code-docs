# Source: https://docs.vespa.ai/en/ranking/tensor-user-guide.html.md

# Tensor Guide

 

Vespa provides a _tensor_ data model and computation engine to support advanced computations over data. This guide explains the tensor support in Vespa. See also the [tensor reference](../reference/ranking/tensor.html), and our [published paper](https://dl.acm.org/doi/10.1145/3459104.3459152)([pdf](../../assets/a_tensor_formalism_for_computer_science.pdf)).

## Tensor concepts

A tensor in Vespa is a data structure which generalizes scalars, vectors and matrices to any number of dimensions:

- A scalar is a tensor of rank 0
- A vector is a tensor of rank 1
- A matrix is a tensor of rank 2
- ...

Tensors consist of a set of scalar valued _cells_, with each cell having a unique _address_. A cell's address is specified by its index or label in all the dimensions of that tensor. The number of dimensions in a tensor is the _rank_ of the tensor. Each dimension can be either _mapped_ or _indexed_. Mapped dimensions are sparse and allow any label (string identifier) designating their address, while indexed dimensions use dense numeric indices starting at 0.

Example: Using [literal form](../reference/ranking/tensor.html#tensor-literal-form), the tensor:

```
{
    {user:bob, movie:"Heat"}:0.1,
    {user:alice, movie:"Frozen"}:0.9,
    {user:carol, movie:"Top Gun"}:0.3,
}
```

has two dimensions named `user` and `movie`, and has three cells with defined values:

 ![Tensor graphical representation](/assets/img/tensor-mapped.png)

A tensor has a _type_, which consists of a set of dimension names, dimension types, and a [tensor cell value type](../reference/ranking/tensor.html#tensor-type-spec). The dimension name can be anything. This defines a 2-dimensional mapped tensor (sparse 2D matrix) of floats as illustrated above:

```
tensor<float>(user{},movie{})
```
This is a 2-dimensional indexed tensor (a 2D 1280x720 matrix). For example, used to represent an image:
```
tensor<int8>(x[1280],y[720])
```
This is a 3-dimensional indexed tensor. For example, used to represent spatial data:
```
tensor<float>(x[256], y[256], z[128])
```
This is a _mixed_ tensor combining a _mapped_ dimension and an _indexed_ dimension. For example, used to represent word2vec:
```
tensor<bfloat16>(word_id{},vec[300])
```
Another mixed tensor used to represent paragraph [embeddings](../rag/embedding.html)used to power [multi-vector indexing](https://blog.vespa.ai/semantic-search-with-multi-vector-indexing/).
```
tensor<float>(paragraph{},embedding[768])
```

Vespa uses the tensor type information to optimize tensor expression execution plans at configuration time.

## Tensor document fields

Document fields in [schemas](../basics/schemas.html) can be of any tensor type:

```
schema product {

    document product {

        field title type string {
            indexing: summary | index
        }

        field price type int {
            indexing: summary | attribute
        }

        field popularity type float {
            indexing: summary | attribute
        }

        field sales_score type tensor<float>(category{}) {
            indexing: summary | attribute
        }

        field embedding type tensor<float>(x[4]) {
            indexing: summary | attribute | index
            attribute {
                distance-metric: dotproduct
            }
        }
    }
}
```

The above schema exemplifies a _product_ with two tensor fields. The `sales_score` tensor field represents how popular a product is per unique _category_. This information could be used when [ranking](../basics/ranking.html) products for a user query. The `embedding` tensor field represents an embedding vector representation of the product.

- **sales\_score** is a _mapped_ tensor with a single mapped dimension `category`. Mapped dimensions are sparse and allow any label (string identifier) designating their address.
- **embedding** is an _indexed_ tensor. Indexed dimensions use dense numeric indices starting at 0.

To perform computations over a document tensor field in [ranking](ranking-intro), the field must be defined with [attribute](../content/attributes.html).

Tensors with the following types can be indexed with [HNSW](../querying/approximate-nn-hnsw) and searched efficiently using the [nearestNeighbor](../reference/querying/yql.html#nearestneighbor) query operator:

- One indexed dimension - single vector per tensor field
- One mapped and one indexed dimension - multiple vectors per tensor field

See [nearest neighbor search](../querying/nearest-neighbor-search) and [approximate nearest neighbor search](../querying/approximate-nn-hnsw).

## Feeding tensors

An example _product_ document in Vespa JSON format. This example uses the product category string as the mapped label key. The _embedding_ tensor stores and indexes ([HNSW](../querying/approximate-nn-hnsw)) a dense [embedding](../rag/embedding.html).

```
```
{
    "put": "id:shopping:product::B0BFW5SXX2",
    "fields": {
        "title": "Keyboard Case for iPad Pro 12.9 inch",
        "price": 29,
        "popularity": 0.8,
        "sales_score": {
            "Tablet Keyboard Cases": 8.0,
            "Keyboards": 2.0,
            "Personal Computers": 0.1
        },
        "embedding": [
            1,
            2,
            3,
            4
        ]
    }
}
```
```

The JSON feed format example above uses short value form. Tensor fields can be represented using different[JSON format](../reference/schemas/document-json-format.html#tensor) verbosity.

You can use [partial updates](../writing/partial-updates.html) of tensor fields with[add](../reference/schemas/document-json-format.html#tensor-add),[remove](../reference/schemas/document-json-format.html#tensor-remove) and[modify](../reference/schemas/document-json-format.html#tensor-modify) tensor cells, or[assign](../reference/schemas/document-json-format.html#tensor-field) a completely new tensor value. From [container components](../applications/components.html) you can create and modify tensor values using the[tensor Java API](https://javadoc.io/doc/com.yahoo.vespa/vespajlib/latest/com/yahoo/tensor/Tensor.html).

You would typically re-calculate the per category sales scores outside Vespa and update them continuously using [partial updates](../writing/partial-updates.html) to avoid re-feeding or re-indexing of other fields.

## Querying with tensors

Query input tensors **must** be defined in the schema [rank-profile](ranking-intro) using[inputs](../reference/schemas/schemas.html#inputs):

```
rank-profile product_ranking inherits default {
    inputs {
        query(q_category) tensor<float>(category{})
        query(q_embedding) tensor<float>(x[4])
    }
    .....
}
```

The above defines two query input tensors that we can reference in [ranking](ranking-intro) expressions. With the tensor query name and tensor type defined, you can:

- Add it to the query in a [Searcher](../applications/searchers.html) using the [Tensor class](https://javadoc.io/doc/com.yahoo.vespa/vespajlib/latest/com/yahoo/tensor/Tensor.html) and setting it by `Query.getRanking().getFeatures.put("query(q_embedding)", myTensorInstance)`, or 
- Pass it in the request, using an HTTP parameter like `input.query(q_embedding)` and passing a tensor [value](../reference/ranking/tensor.html#tensor-literal-form). 

An example query request using [Vespa CLI query request](../clients/vespa-cli.html#queries):

```
```
vespa query 'yql=select * from product where {targetHits:1}nearestNeighbor(embedding,q_embedding)' \
  'input.query(q_embedding)=[1,2,3,4]' \
  'input.query(q_category)={"Tablet Keyboard Cases":0.8, "Keyboards":0.3}' \
  'ranking=product_ranking'
```
```

This query request example assumes that the user query has been mapped (classified) to be related to the_Tablet Keyboard Cases_ and _Keyboards_ categories. Similarly, the user query has been mapped to a dense vector representation (`query(q_embedding`) and is used as input to the [nearestNeighbor](../reference/querying/yql.html#nearestneighbor)query operator, expressed with the [YQL query language](../querying/query-language.html).

The Vespa CLI uses HTTP GET and you can use the _-v_ flag to see the curl GET equivalent. For[POST](../querying/query-api.html#using-post) query requests using JSON, the equivalent JSON is:

```
```
{
    "yql": "select * from product where {targetHits:1}nearestNeighbor(embedding,q_embedding)",
    "input": {
        "query(q_embedding)": [
            1,
            2,
            3,
            4
        ],
        "query(q_category)": {
          "Tablet Keyboard Cases": 0.8,
          "Keyboards":0.3
        }
    },
    "ranking": "product_ranking"
}
```
```

If the input query tensor used for the [nearestNeighbor](../reference/querying/yql.html#nearestneighbor) operator is not defined in the schema rank-profile, the request will fail:

```
"Expected 'query(q_embedding)' to be a tensor, but it is the string '[1,2,3,4]'"
```

## Ranking with tensors

Tensors can be used in making inference computations over documents that are matched by a query. These computations are expressed with [ranking expressions](../reference/ranking/ranking-expressions.html) in schema [rank profiles](../reference/schemas/schemas.html#rank-profile). We can use this support to rank products by both the dense embedding dot product similarity and the category sales score.

```
rank-profile product_ranking inherits default {

    inputs {
        query(q_category) tensor<float>(category{})
        query(q_embedding) tensor<float>(x[4])
    }

    function p_sales_score() {
        expression: sum(query(q_category) * attribute(sales_score))
    }

    function p_embedding_score() {
        expression: closeness(field, embedding)
    }

    first-phase {
        expression: p_sales_score() + p_embedding_score()
    }
    match-features: p_sales_score() p_embedding_score()
}
```

The above profile uses a combination of two dot product calculations in the [first phase](phased-ranking.html) expression. The `first-phase` expression is invoked for all documents that are **retrieved**by the [YQL query language](../querying/query-language.html).

- The _p\_sales\_score_ function calculates the sparse tensor dotproduct between the _query(q\_category)_ and _attribute(sales\_score)_ tensor. 
- The _p\_embedding\_score_ calculates the dense tensor dotproduct between the _query(q\_embedding)_ and _attribute(embedding)_ tensors. The function uses the [closeness(dimension,name)](../reference/ranking/rank-features.html#closeness(dimension,name)) [rank-feature](../reference/ranking/rank-features.html) which is calculated by the [nearestNeighbor](../reference/querying/yql.html#nearestneighbor) query operator. Alternatively, if we don't use the _nearestNeighbor_ operator in the query request, we could use sparse tensor dotproduct:
```
function p_embedding_score() {
    expression: sum(query(q_embedding) * attribute(embedding))
}
```

The full list of tensor functions are listed in the[ranking expression reference](../reference/ranking/ranking-expressions.html#tensor-functions). Using [match-features](../reference/schemas/schemas.html#match-features), developers can debug, or log function outputs in the search result.

```
"matchfeatures": {
    "p_embedding_score": 30.0,
    "p_sales_score": 8.0,
},
"documentid": "id:shopping:product::B0BFW5SXX2",
"title": "Keyboard Case for iPad Pro 12.9 inch"
```

## Creating tensors from document fields

If you need to make tensor computations from non-tensor single-valued attributes, arrays, weighted sets, or array\<struct\> fields, you can convert them in a ranking expression:

- Creating an _indexed_ tensor where the _values_ are lifted from single-value attributes (price and popularity) using the tensor generate function:
```
function to_indexed_tensor() {
    expression: tensor(x[2]):[attribute(price),attribute(popularity)]
}
```
- Creating a _mapped_ tensor where the _values_ are lifted from single-value attributes using the tensor generate function:
```
function to_mapped_tensor() {
    expression: tensor(x{}):{key1:attribute(price),key2:attribute(popularity)}
}
```
- Creating a _mapped_ tensor where the _label(s)_ are lifted from a string array or single-value attribute can be done with the [document feature](../reference/ranking/rank-features.html#document-features) `tensorFromLabels`. 
- Creating a _mapped_ tensor where the labels _and_ values are lifted from a weighted set can be done with the [document feature](../reference/ranking/rank-features.html#document-features) `tensorFromWeightedSet`. 
- Creating a _mapped_ tensor where labels and values are lifted from an `array<struct>` attribute can be done with the [document feature](../reference/ranking/rank-features.html#document-features) `tensorFromStructs`. 

Converting non-tensor fields to tensors at query runtime has a performance penalty that is linear with the number of elements in the array, weighted set, or struct array. Prefer using native tensor fields instead. The benefit of converting non-tensor fields is that non-tensor fields like `int`, `float`, `weightedset`, or `array<struct>` can be efficiently queried. Only specific tensor types can be searched efficiently using the [nearestNeighbor](../reference/querying/yql.html#nearestneighbor) query operator.

## Constant tensors

In addition to document tensors and query tensors,[constant tensors](../reference/schemas/schemas.html#constant)can be put in the [application package](../reference/applications/application-packages.html). This is useful for adding machine learned models. Example:

```
constants {
    my_tensor_constant tensor<float>(x[4]): file: constants/constant_tensor_file.json
}
```

This defines a new tensor with the type as defined and the contents distributed with the application package in the file_constants/constant\_tensor\_file.json_. The format of this file is the[constant tensor JSON format](../reference/ranking/constant-tensor-json-format.html):

```
```
{
    "type": "tensor<float>(x[4])",
    "values": [
        0,
        0,
        0,
        1.0
    ]
}
```
```

To use this constant tensor in a ranking expression, encapsulate the constant name with `constant(...)`:

```
rank-profile use_constant_tensor inherits product_ranking {
    constants {
        my_tensor_constant tensor<float>(x[4]): file: constants/constant_tensor_file.json
    }
    first-phase {
        expression: sum(query(q_embedding) * attribute(embedding) * constant(my_tensor_constant))
    }
}
```

Note that the rank profile `inherit` the inputs we defined in the `product_ranking` profile. With the example data used, the first-phase expression returns the 16.0 since:

```
"embedding": [
    1.0,
    2.0,
    3.0,
    4.0
  ],
  "query(q_embedding)": [
    1.0,
    2.0,
    3.0,
    4.0
  ],
  "constant(my_tensor_constant)": [
    0.0,
    0.0,
    0.0,
    1.0
  ]
```

## Tensors with strings

Tensors in Vespa cannot have strings as values, since the mathematical tensor functions would be undefined for such "tensors". However, you can still represent sets of strings in tensors by using the strings as keys in a mapped tensor dimensions, using e.g 1.0 as values. This allows you to perform set operations on strings and similar without making those tensors incompatible with other tensors and with normal tensor operations.

## Further reading

See also:

- [Blog post: Computing with tensors in Vespa](https://blog.vespa.ai/computing-with-tensors/).
- [Using ONNX models](onnx) to use machine-learned models taking tensor input in Vespa.
- Some [practical tensor computation examples](tensor-examples.html).
- The [tensor playground](https://docs.vespa.ai/playground/#N4KABGBEBmkFxgNrgmUrWQPYAd5QGNIAaFDSPBdDTAF30gAkBTAJ2bAE8sBXMAgIYA7MDgA2AzmAGteQgCbSFYZgA8cbAJYBbZkNpgA7ptoALMLT0BnLKytLFloTdYr17K1c1ZnAOjAs7GCa9gJgVqa2BgA6QmoC2uLMxFy8-MJg0JrK2rYc2dC22gK03iIlYLGIZhxOLmA8VmxgAOY8mvLMALoAFKa0tDhWcAD0I-JYBFa+AG7MVjgCvgKaI3ojdbYAtI1sW20dzL792mIAlJBkqAC+V9ekGNTkuAxEDzQU+E8f9AiQAIIWay2YKhMDyEphKy0Vg8Ai0HhBMwVELSVp6NgCMSaABeJTKYCw0HCggkdhSc3htlCORKrE0BHm-liABVgXYwKYBHM0UIeNoAEbNIngnTWMr2ZEGQQiIUqEymZqdZwcEELGRNQmuMIELCC7L4ny+WL-ETxRJiVXEqGLOy1dlwS40MC3DD3K7fCDYShQZgkK5en2ezBCBjqu0AfU2rH9zq9fr+0Z6qmA1zOcGAAjgAEZiAK4AAma5Omium7vCDB72vWMfIMBugMQHKzXRowKiyGLCi3TOCUpTS+I5o4owzSqR0NssQd2PBvVv5+iuYetxqChv4t5hR9m152QBNQJOqRAFrrETiIADMXXTiEQuYLxBvxEQABZiABWYgANi6XRLN07mXKsXj+N551XONIF+KA2Wcal0hELkeQFLAzHCW1NWERQtx7cUfCsFIPB4MRSiEFpgnKMBtHHZhHHZfxAg4YwMJqMAAANoDELASg42IIVoMJaE4DRJ2dacXRA+cwN9PcVy+BsvQ3KBaNUeidwQmNl3IQ8YPZAAebjeNoAA+ZNUwva9bwzLMH2IJ8X3zd8v1-LpiynYCPRkn1IAg-coP3WDIHglx7BQjgoWYAwRVwTFSkI6QxB44wKMyEEwnkTQ5jtcJosJYldUSHghISoR-AAMRBbJoWERkUjCDiACssGyDjxNLLy533WSD3kwNFLXSAVMgfrMD0lrsh6cMmk0lwUjUjToxSaAegEPMzjWgAqAUzguTy3WknrfP8utBug4KWVMVFUWYABHdoZixPQDFoLAOqAw7vOOhgl0g879xGsb4zDLDtzbLaaLo+Q5tsQCbi61BQJOsbPioJSjwYKrXFyIJzSSIi8o4RAJimWZ5kWZZVnWaMtnxy1phOMRen6QZhjGUnpjmdUqbWIQNnZOnVASAnjloU59oku4UC6EBriAA) which allows you to create and compute with Vespa tensors in your browser.
- The [Tensor Java API](https://javadoc.io/doc/com.yahoo.vespa/vespajlib/latest/com/yahoo/tensor/Tensor.html).
- [Tensor ranking performance](../performance/feature-tuning.html#tensor-ranking).

 Copyright © 2025 - [Cookie Preferences](#)

### On this page:

- [Tensor concepts](#tensor-concepts)
- [Tensor document fields](#tensor-document-fields)
- [Feeding tensors](#feeding-tensors)
- [Querying with tensors](#querying-with-tensors)
- [Ranking with tensors](#ranking-with-tensors)
- [Creating tensors from document fields](#creating-tensors-from-document-fields)
- [Constant tensors](#constant-tensors)
- [Tensors with strings](#tensors-with-strings)
- [Further reading](#further-reading)

