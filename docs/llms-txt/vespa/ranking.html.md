# Source: https://docs.vespa.ai/en/basics/ranking.html.md

# Ranking

 

_Ranking_ in Vespa is the computation that is done on matching documents during query execution. These are specified as [ranking functions](../ranking/ranking-expressions-features.html) in_rank profiles_ in the schema.

The special function named `first-phase` will determine the initial _rank_ of the matches, such that the top k can be selected as response to a query:

```
rank-profile my-rank-profile {
    first-phase {
      expression: 0.7 * bm25(text) + 0.3 * attribute(popularity)
    }
  }
```

## Ranking functions and features

The ranking functions can be any mathematical function combining rank features, including [tensor math](../ranking/tensor-user-guide.html#ranking-with-tensors) and[machine-learned models](#machine-learned-model-inference).

The rank features these functions can use are of three categories:

- **Document features**, using `attribute(fieldName)`: Any document field which has `attribute` in the indexing statement.
- **Query features**, aka inputs, using `query(name)`: Any value sent with the query as an input. When these are tensors (not scalars) they must be declared as an input in the rank profile. 
- **Match features**: A built-in feature which says something about how well a query and document matches, e.g. bm25 or closeness.

Refer to the [full list of rank features](../reference/ranking/rank-features.html).

Query features (inputs) that are tensors must be declared in the rank profile:

```
rank-profile my-rank-profile {
    inputs {
      query(user_context) tensor<float>(x[3])
    }
    first-phase {
      expression: bm25(text) + sum(query(user_context) * attribute(document_context))
    }
  }
```

This is also how the type of query vectors in vector search are declared.

## Rank profiles

A schema can have any number of rank profiles specifying computations and ranking for different use cases, experiments, and so on. Queries select one using the[ranking.profile](../reference/api/query.html#ranking.profile) parameter in requests or a [query profile](../querying/query-profiles.html). If no profile is specified in the request, the one called `default` is used, and if that isn't specified in the schema, a default one ranking by the [nativeRank](../ranking/nativerank.html)feature is used. Another built-in rank profile `unranked` is also always available. Specifying this boosts serving performance in queries which do not need ranking because ordering is not important or[explicit field sorting](../reference/querying/sorting-language.html) is used.

To avoid very long schema files, rank profiles can also be specified in their own files in the application package, named`schemas/[schema-name]/[profile-name].profile`. See the [schema reference](../reference/schemas/schemas.html#rank-profile) for documentation of all the content of rank profiles.

Rank profiles can inherit other profiles to avoid duplication, as in`rank-profile myProfile inherits default, another`.

## Phased ranking

In addition to first-phase which specify the initial ranking that will be applied on all matching documents during matching, rank profiles can also specify functions that will be applied to _rerank_ the top k documents before returning the final result. This is useful to direct more computation towards the most promising candidate documents:

```
schema myapp {

    rank-profile my-rank-profile {

        first-phase {
            expression {
                attribute(quality) * freshness(timestamp) + bm25(title)
            }
        }

        second-phase {
            expression: xgboost(my_xgboost_reranker)
            rerank-count: 1000 # per content node
        }

        global-phase {
          expression: sum(onnx(my_large_onnx_model))
          rerank-count: 20 # globally
        }

    }

}
```

The `second-phase` expression is executed locally on the content node, using local data. This is efficient on thousands of candidates. The `global-phase` expression is executed on the global result set after merging, in the container node and is best used for any very expensive and high quality final reranking. See [phased ranking](../ranking/phased-ranking.html) for details.

## Ranking functions

A rank profile can define any number of functions which can be used in other ranking expressions or (when taking no arguments) be returned with results.

```
schema myapp {

    rank-profile my-rank-profile {

        function clickProbability() {
            expression: xgboost('myClickModel')
        }

        function textRanking(field) {
            expression: 0.7 * bm25(field) + 0.3 * nativeProximity(field)
        }

        first-phase {
            expression {
                0.1 * clickProbability()
                0.2 * closeness(embeddingsField) +
                0.3 * textRanking(titleField) +
                0.4 * textRanking(bodyField)
            }
        }

        summary-features {
            clickProbability() # Returned with every mathed document
        }

    }

}
```

Read more in [ranking expressions and functions](../ranking/ranking-expressions-features.html).

## Layered ranking

In addition to ranking _documents_, a rank profile can also rank and select array elements within documents. This is most commonly used to select individual chunks within documents in RAG applications, see[working with chunks](../rag/working-with-chunks.html#layered-ranking-selecting-chunks-to-return).

## Machine-Learned model inference

The best quality is achieved by learning relevance functions using machine learning from a training set. Vespa lets you use machine-learned models in these formats in distributed ranking (first-and second phase):

- [ONNX](../ranking/onnx), allowing importing models from ML frameworks like Tensorflow, PyTorch and scikit-learn.
- [XGBoost](../ranking/xgboost)
- [LightGBM](../ranking/lightgbm)

As these are exposed as rank features, they can be used in ranking expressions exactly like any other rank feature.

  

#### Next: [Operations](operations.html)

 Copyright © 2025 - [Cookie Preferences](#)

### On this page:

- [Ranking functions and features](#ranking-functions-and-features)
- [Rank profiles](#rank-profiles)
- [Phased ranking](#phased-ranking)
- [Ranking functions](#ranking-functions)
- [Layered ranking](#layered-ranking)
- [Machine-Learned model inference](#machine-learned-model-inference)

