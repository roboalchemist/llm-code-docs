# Source: https://docs.vespa.ai/en/querying/searching-multivalue-fields.html.md

# Searching and ranking of multivalued fields

 

This guide explains how to search and rank over structured multivalued fields. The examples in this guide use the [weightedset](../reference/schemas/schemas.html#weightedset)[field type](../reference/schemas/schemas.html#field). The generic [map\<key-type,value-type\>](../reference/schemas/schemas.html#map) field type does not currently support ranking and can only be used for matching and filtering.

When building a search application we need to think about:

- How to [match](query-language.html) a user specified query against a [document schema](../basics/schemas.html)using Vespa [query language](query-language.html).
- How to [rank](../basics/ranking.html) documents matching the query.

## Matching documents

There is a lot of text matching options we should think about when designing and mapping our document model to a Vespa document schema:

- For string fields we should think about using text style matching or database-style exact matching.
- For string fields there are also several[linguistic processing](../linguistics/linguistics.html) options like [tokenization](../linguistics/linguistics.html#tokenization), normalization and language dependent [stemming](../linguistics/linguistics.html#stemming).
- String fields which shares the same [match](../reference/schemas/schemas.html#match) and linguistic processing settings can be combined using [fieldsets](../reference/schemas/schemas.html#fieldset).

At query time, we can take the user query and translate it into a valid Vespa query request which implements our matching and retrieval strategy over the designed document schema.

## Ranking documents

The documents which match the query and are retrieved by the query are scored using a ranking model. Once a document is retrieved by the query logic the document can be scored using the full flexibility of the Vespa [ranking](../basics/ranking.html) framework.

## A minimal Vespa application

In the following sections we explore matching and ranking over multivalued string fields.

**Prerequisites:**

- Linux, macOS or Windows 10 Pro on x86\_64 or arm64, with Podman or [Docker](https://docs.docker.com/engine/install/) installed. See [Docker Containers](/en/operations/self-managed/docker-containers.html) for system limits and other settings. For CPUs older than Haswell (2013), see [CPU Support](/en/cpu-support.html)
- Memory: Minimum 4 GB RAM dedicated to Docker/Podman. [Memory recommendations](/en/operations/self-managed/node-setup.html#memory-settings). 
- Disk: Avoid `NO_SPACE` - the vespaengine/vespa container image + headroom for data requires disk space. [Read more](/en/writing/feed-block.html). 
- [Homebrew](https://brew.sh/) to install the [Vespa CLI](/en/clients/vespa-cli.html), or download the Vespa CLI from [Github releases](https://github.com/vespa-engine/vespa/releases). 

Assuming we have the following sample data document where we have a structured tag-like field where there is a weight associated with each element.

```
{
    "put": "id:photos:photo::0",
    "fields": {
        "title": "Mira in the sunset",
        "description": "A sunny afternoon with our dogs",
        "tags": {
            "no filter":1,
            "light": 3,
            "black and white": 3,
            "clear sky": 2,
            "sunset dogs": 4
        }
    }
}
```

Structured data like the `tags`, where we both want to match and rank is best represented using the [weightedset](../reference/schemas/schemas.html#weightedset) [field type](../reference/schemas/schemas.html#field). The Vespa weightedset field type can be used to represent:

- Document side tags like in the above example.
- [Document expansion by query prediction](https://github.com/castorini/docTTTTTquery).
- Editorial ranking overrides, for example sponsored search listings.

How should we design our Vespa schema, and how should we match and search this data model for end-user free text queries?

- We want to use text matching when searching the title and description.
- We also want to match the free form tags field as these tags might increase recall and the weight of the matched element(s) could influence ranking of documents matched - schema:

```
schema photo {

    stemming: none
  
    document photo {

        field title type string {
            indexing: summary | index
            match:text
            index: enable-bm25
        }

        field description type string {
            indexing: summary | index
            match:text
            index: enable-bm25
        }

        field interestingness type float {
            indexing: summary | attribute
        }

        field tags type weightedset<string> {
            indexing: summary | index
            match:text
            index: enable-bm25
        }

    }

    fieldset default {
        fields: title, description, tags
    }

    rank-profile default {
        first-phase {
            expression: nativeRank
        }
    }
}
```

In the schema we disable [stemming](../reference/schemas/schemas.html#stemming) and also enable [bm25](../ranking/bm25.html) text ranking feature for all string fields.

Since all string fields shares the same [match](../reference/schemas/schemas.html#match)settings we can use a [fieldset](../reference/schemas/schemas.html#fieldset) so that queries does not need to mention all three fields.

We also include a default rank profile (this is the implicit default rank profile) using the Vespa [nativeRank](../ranking/nativerank.html) text matching rank feature.

Along with the schema, we also need a [services.xml](../reference/applications/services/services.html) file to make up a Vespa [application package](../reference/applications/application-packages.html):

```
<?xml version="1.0" encoding="UTF-8"?>
<services version="1.0">

    <container id="default" version="1.0">
        <search />
        <document-api />
        <nodes>
            <node hostalias="node1"></node>
        </nodes>
    </container>

    <content id="photos" version="1.0">
        <redundancy>1</redundancy>
        <documents>
            <document type="photo" mode="index"/>
        </documents>
        <nodes>
            <node hostalias="node1" distribution-key="0" />
        </nodes>
    </content>

</services>
```

## Starting Vespa

This example uses the vespa container image:

```
$ docker pull vespaengine/vespa
$ docker run --detach --name vespa --hostname vespa-container \
  --publish 8080:8080 --publish 19071:19071 \
  vespaengine/vespa
```

Install [Vespa-cli](../clients/vespa-cli.html) using Homebrew:

```
$ brew install vespa-cli
```

Deploy the application:

```
$ vespa deploy --wait 300 my-app
```

## Feeding to Vespa

Feed a sample document:

```
$ vespa document -v doc.json
```

## Query the data

Assuming a free text query _sunset photos featuring dogs_, translate the user query into a Vespa query request using YQL:

```
$ vespa query 'yql=select * from photos where userQuery()' \
  'query=sunset photos featuring dogs' \
  'type=all'
```

The above query returns 0 hits, since the query requires that _all_ query terms matches the document. By adding [trace.level](../reference/api/query.html#trace.level) to the query request we can see how the query is parsed and executed against the content nodes:

```
$ vespa query 'yql=select * from photos where userQuery()' \
  'query=sunset photos featuring dogs' \
  'type=all' \
  'trace.level=3'
```

In the trace we can see the query which is dispatched to the content nodes:`query=[AND sunshot photos featuring dogs]`

Using tracing is very useful when debugging why documents match or does not match.

Since the sample document does not contain the term _featuring_ or _photos_, the query fails to retrieve the example document. Relax the query matching to instead of requiring that **all** terms match, to use **any**. See [model.type](../reference/api/query.html#model.type) query api reference for supported query types:

```
$ vespa query 'yql=select * from photos where userQuery()' \
  'query=sunset photos featuring dogs' \
  'type=any'
```

Changing the type to `any`, recalls the sample document as we no longer require that all query terms must match. With `type` it also possible to require that individual query terms match by using `+`:

```
$ vespa query 'yql=select * from photos where userQuery()' \
  'query=+sunset photos featuring +dogs' \
  'type=any'
```

In this example `sunset` and `dogs` must be matched. Note that we have disabled stemming so querying for `dogs` won't recall documents with `dog`. This is one of the reasons we disabled stemming, to demonstrate that stemming has impact on recall. Requiring `dog` will cause the query to not recall our sample document.

```
$ vespa query 'yql=select * from photos where userQuery()' \
  'query=+sunset photos featuring +dog' \
  'type=any'
```

Now, explore how Vespa matches the multivalued tags field of type [weightedset](../reference/schemas/schemas.html#weightedset). Notice that we change back to `type=all`. In this example we also use the [default-index](../reference/api/query.html#model.defaultindex) query parameter to limit matching to the `tags` field.

```
$ vespa query 'yql=select * from photos where userQuery()' \
  'query=clear sky' \
  'type=all' \
  'default-index=tags'
```

The query matches the document which is no surprise since a tag contains the exact content `clear sky`. Let us search for just `clear` instead:

```
$ vespa query 'yql=select * from photos where userQuery()' \
  'query=clear' \
  'type=all' \
  'default-index=tags'
```

Also matches the document, this demonstrates that matching is partial, it does not require to match the set element exactly. `clear` matches `clear sky` and `sky` will match `clear sky`.

But what about `black sky`:

```
$ vespa query 'yql=select * from photos where userQuery()' \
  'query=black sky' \
  'type=all' \
  'default-index=tags'
```

Also matches the document. This is an example of cross-element matching. With weightedset using `indexing:index` with `match:text` multi term queries match across elements.

This might be a good decision, as we increase recall, however in some cases we want to differentiate an exact match from a partial match during ranking, so that exact matches are ranked higher than partial matches.

## Ranking

We have now explored querying and matching, now it's time to focus on how to rank the documents matched. You might not have noticed, but in the above examples, each of the queries produced a `relevance` score per hit, this score was in our previous examples calculated using the `default` rank profile which in our case used [nativeRank](../ranking/nativerank.html).

We can start by analyzing other [rank features](../reference/ranking/rank-features.html) by asking Vespa to produce them for us. We use [match-features](../reference/schemas/schemas.html#match-features)to return rank features with the retrieved documents. We explicitly mention which ranking features we want to have calculated and returned. Notice that we don't change the actual scoring, we still use `nativeRank` as the scoring function:

```
schema photo {

    stemming: none

    document photo {

        field title type string {
            indexing: summary | index
            match:text
            index: enable-bm25
        }

        field description type string {
            indexing: summary | index
            match:text
            index: enable-bm25
        }

        field interestingness type float {
            indexing: summary | attribute
        }

        field tags type weightedset<string> {
            indexing: summary | index
            match:text
            index: enable-bm25
        }

    }

    fieldset default {
        fields: title, description, tags
    }

    rank-profile default {
        first-phase {
            expression: nativeRank
        }

        match-features {
            bm25(title)
            bm25(description)
            bm25(tags)

            nativeRank
            nativeRank(title)
            nativeRank(description)

            elementSimilarity(tags)
            elementCompleteness(tags).elementWeight
            elementCompleteness(tags).fieldCompleteness
            elementCompleteness(tags).queryCompleteness
            elementCompleteness(tags).completeness
        }
    }
}
```

Re-deploy with the changed rank profile:

```
$ vespa deploy --wait 300 my-app
```

Now we will see a list of features in the response:

```
$ vespa query 'yql=select * from photos where userQuery()' \
  'query=clear sky' \
  'type=any'
```

The output includes [matchfeatures](../reference/querying/default-result-format.html#matchfeatures)where we can see the various scores for the features:

Especially look at the `elementCompleteness` and `elementSimilarity` rank features which are example of [features for indexed multivalued string fields](../reference/ranking/rank-features.html#features-for-indexed-multivalue-string-fields).

We can also notice that `elementCompleteness(tags).fieldCompleteness` is 1.0 which means that the tag was matched exactly and the `"elementCompleteness(tags).elementWeight` outputs the weight of the best matched element.

The `elementSimilarity(tags)` ranking feature is very flexible and even allow us to override the [calculation and output new features](../reference/ranking/rank-feature-configuration.html#elementSimilarity).

In this example we defined two new ranking features:

- `elementSimilarity(tags).sumWeight` which uses the sum of matching elements using field completeness x weight.
- `elementSimilarity(tags).maxWeight` which uses the max over the matching elements using field completeness x weight.

```
schema photo {

    stemming: none

    document photo {

        field title type string {
            indexing: summary | index
            match:text
            index: enable-bm25
        }

        field description type string {
            indexing: summary | index
            match:text
            index: enable-bm25
        }

        field interestingness type float {
            indexing: summary | attribute
        }

        field tags type weightedset<string> {
            indexing: summary | index
            match:text
            index: enable-bm25
        }

    }

    fieldset default {
        fields: title, description, tags
    }

    rank-profile default {
        rank-properties {
            elementSimilarity(tags).output.sumWeight: "sum(f*w)"
            elementSimilarity(tags).output.maxWeight: "max(f*w)"
        }
   
        first-phase {
            expression: nativeRank
        }

        match-features {
            bm25(title)
            bm25(description)
            bm25(tags)

            nativeRank
            nativeRank(title)
            nativeRank(description)

            elementSimilarity(tags)
            elementSimilarity(tags).sumWeight
            elementSimilarity(tags).maxWeight

            elementCompleteness(tags).elementWeight
            elementCompleteness(tags).fieldCompleteness
            elementCompleteness(tags).queryCompleteness
            elementCompleteness(tags).completeness
        }
    }
}
```

Re-deploy with the changed rank profile:

```
$ vespa deploy --wait 300 my-app
```

Now we will see a list of features in the response:

```
$ vespa query 'yql=select * from photos where userQuery()' \
  'query=clear sky' 'type=any'
```

Each hit returned contains a [matchfeatures](../reference/querying/default-result-format.html#matchfeatures) field where we can see the various scores for the features.

Now, we can include these features in a ranking expression used in `first-phase` to actually change the ranking. The actual _best_ scoring function is data dependent. A trained function using machine learning is by far the easiest way.

The bag of words [bm25](../ranking/bm25.html) ranking feature is not normalized, so combining it in a linear function is challenging, as the score range of the feature is unbound. To overcome this, and allow easy exploration without changing the rank profile, make the parameters in the function overridable on a per-query basis by:

```
first-phase {
    expression {
        query(titleWeight)*bm25(title) +
        query(descriptionWeight)*bm25(description) +
        query(tagWeight)*elementSimilarity(tags).maxWeight
    }
}
```

See [using query variables](../ranking/ranking-expressions-features.html#using-query-variables).

```
schema photo {

    stemming: none

    document photo {

        field title type string {
            indexing: summary | index
            match:text
            index: enable-bm25
        }

        field description type string {
            indexing: summary | index
            match:text
            index: enable-bm25
        }

        field interestingness type float {
            indexing: summary | attribute
        }

        field tags type weightedset<string> {
            indexing: summary | index
            match:text
            index: enable-bm25
        }
    }

    fieldset default {
        fields: title, description, tags
    }

    rank-profile tunable inherits default {
        inputs {
            query(titleWeight): 2
            query(descriptionWeight): 1
            query(tagWeight): 2
        }

        rank-properties {
            elementSimilarity(tags).output.sumWeight: "sum(f*w)"
            elementSimilarity(tags).output.maxWeight: "max(f*w)"
        }
   
        first-phase {
            expression {
                query(titleWeight)*bm25(title) + query(descriptionWeight)*bm25(description) +
                query(tagWeight)*elementSimilarity(tags).maxWeight
            }
        }

        match-features {
            bm25(title)
            bm25(description)
            bm25(tags)
            elementSimilarity(tags).maxWeight
            firstPhase
        }
    }
}
```

Re-deploy:

```
$ vespa deploy --wait 300 my-app
```

Run a query with the new rank profile:

```
$ vespa query 'yql=select * from photos where userQuery()' \
  'query=clear sky' 'type=any' 'ranking=tunable'
```

With the function above, since 'clear sky' does not match any of the title or description fields, the bm25 features becomes zero.

Our `elementSimilarity(tags).maxWeight` feature is 2.0 and the first phase expression becomes 4 which is reflected in the hit relevance score.

Change the `query(tagWeight)` with the query request and observe that the relevance becomes 6.0:

```
$ vespa query 'yql=select * from photos where userQuery()' \
  'query=clear sky' \
  'type=any' \
  'ranking=tunable' \
  'input.query(tagWeight)=3'
```

Similar, we could also include a document-only signal to our ranking function by:

```
inputs {
    query(titleWeight): 2
    query(descriptionWeight): 1
    query(tagWeight): 2
    query(staticWeight): 1
}

rank-properties {
    elementSimilarity(tags).output.sumWeight: "sum(f*w)"
    elementSimilarity(tags).output.maxWeight: "max(f*w)"
}

first-phase {
    expression {
        query(titleWeight)*bm25(title) + query(descriptionWeight)*bm25(description) +
        query(tagWeight)*elementSimilarity(tags).maxWeight + query(staticWeight)*attribute(interestingness)
    }
}
```

That concludes the matching and ranking experiments. To shut down the container:

```
$ docker rm -f vespa
```

 Copyright © 2025 - [Cookie Preferences](#)

### On this page:

- [Matching documents](#matching-documents)
- [Ranking documents](#ranking-documents)
- [A minimal Vespa application](#a-minimal-vespa-application)
- [Starting Vespa](#starting-vespa)
- [Feeding to Vespa](#feeding-to-vespa)
- [Query the data](#query-the-data)
- [Ranking](#ranking)

