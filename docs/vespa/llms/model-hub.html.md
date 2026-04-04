# Source: https://docs.vespa.ai/en/rag/model-hub.html.md

# Using machine-learned models from Vespa Cloud

 

Vespa Cloud provides a set of machine-learned models that you can use in your applications. These models will always be available on Vespa Cloud and are[frozen models](https://blog.vespa.ai/tailoring-frozen-embeddings-with-vespa/). You can also bring your own embedding model, by deploying it in the Vespa application package.

You specify to use a model provided by Vespa Cloud by setting the `model-id`attribute where you specify a model config. For example, when configuring the[Huggingface embedder](embedding.html#huggingface-embedder)provided by Vespa, you can write:

```
```
<container id="default" version="1.0">
    <component id="e5" type="hugging-face-embedder">
        <transformer-model model-id="e5-small-v2"/>
    </component>
    ...
</container>
```
```

With this, your application will have support for[text embedding](embedding.html#embedding-a-query-text)inference for both queries and documents. Nodes that have been provisioned with GPU acceleration, will automatically use GPU for embedding inference.

## Vespa Cloud Embedding Models

Models on Vespa model hub are selected open-source embedding models with great performance. See the [Massive Text Embedding Benchmark (MTEB) Leaderboard](https://huggingface.co/spaces/mteb/leaderboard) for details. These embedding models are useful for retrieval (semantic search), re-ranking, clustering, classification, and more.

### Huggingface Embedder

These models are available for the Huggingface Embedder `type="hugging-face-embedder"`. All these models supports both mapping from `string` or `array<string>` to tensor representations. The output tensor [cell-precision](../performance/feature-tuning.html#cell-value-types)can be `<float> ` or `<bfloat16>`.

| 
#### nomic-ai-modernbert
 |
| --- |
| 

Trained from ModernBERT-base on the Nomic Embed datasets, bringing the new advances of ModernBERT to embeddings.

 |
| Model id | `nomic-ai-modernbert` |
| Tensor definition | `tensor<float>(x[768])` (supports Matryoshka, so `x[256]` is also possible) |
| [distance-metric](../reference/schemas/schemas.html#distance-metric) | `angular` |
| License | [apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Source | [https://huggingface.co/nomic-ai/modernbert-embed-base](https://huggingface.co/nomic-ai/modernbert-embed-base) @ 92168cb |
| Language | English |
| Component declaration | 

```
```
<component id="my-embedder-id" type="hugging-face-embedder">
        <transformer-model model-id="nomic-ai-modernbert"/>
        <transformer-output>token_embeddings</transformer-output>
        <max-tokens>8192</max-tokens>
        <prepend>
            <query>search_query: </query>
            <document>search_document: </document>
        </prepend>
    </component>
```
```

 |
| 
#### lightonai-modernbert-large
 |
| --- |
| 

Trained from ModernBERT-large on the Nomic Embed datasets, bringing the new advances of ModernBERT to embeddings.

 |
| Model id | `lightonai-modernbert-large` |
| Tensor definition | `tensor<float>(x[1024])` |
| [distance-metric](../reference/schemas/schemas.html#distance-metric) | `angular` |
| License | [apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Source | [https://huggingface.co/lightonai/modernbert-embed-large](https://huggingface.co/lightonai/modernbert-embed-large) @ b3a781f |
| Language | English |
| Component declaration | 

```
```
<component id="my-embedder-id" type="hugging-face-embedder">
        <transformer-model model-id="lightonai-modernbert-large"/>
        <max-tokens>8192</max-tokens>
        <prepend>
            <query>search_query: </query>
            <document>search_document: </document>
        </prepend>
    </component>
```
```

 |
| 
#### alibaba-gte-modernbert
 |
| --- |
| 

GTE (General Text Embedding) model trained from ModernBERT-base.

 |
| Model id | `alibaba-gte-modernbert` |
| Tensor definition | `tensor<float>(x[768])` (supports Matryoshka, so `x[256]` is also possible) |
| [distance-metric](../reference/schemas/schemas.html#distance-metric) | `angular` |
| License | [apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Source | [https://huggingface.co/Alibaba-NLP/gte-modernbert-base](https://huggingface.co/Alibaba-NLP/gte-modernbert-base) @ 3ab3f8c |
| Language | English |
| Component declaration | 

```
```
<component id="my-embedder-id" type="hugging-face-embedder">
        <transformer-model model-id="alibaba-gte-modernbert"/>
        <max-tokens>8192</max-tokens>
        <pooling-strategy>cls</pooling-strategy>
    </component>
```
```

 |
| 
#### e5-small-v2
 |
| --- |
| 

The smallest and most cost-efficient model from the _E5_ family.

 |
| Model-id | e5-small-v2 |
| Tensor definition | `tensor<float>(x[384])` or `tensor<float>(p{},x[384])` |
| [distance-metric](../reference/schemas/schemas.html#distance-metric) | `angular` |
| License | [MIT](https://github.com/microsoft/unilm/blob/master/LICENSE) |
| Source | [https://huggingface.co/intfloat/e5-small-v2](https://huggingface.co/intfloat/e5-small-v2) |
| Language | English |
| Component declaration | 

```
```
<component id="my-embedder-id" type="hugging-face-embedder">
        <transformer-model model-id="e5-small-v2"/>
        <max-tokens>512</max-tokens>
        <prepend>
            <query>query: </query>
            <document>passage: </document>
        </prepend>
    </component>
```
```

 |
| 
#### e5-base-v2
 |
| --- |
| 

The base model of the _E5_ family.

 |
| Model-id | e5-base-v2 |
| Tensor definition | `tensor<float>(x[768])` or `tensor<float>(p{},x[768])` |
| [distance-metric](../reference/schemas/schemas.html#distance-metric) | `angular` |
| License | [MIT](https://github.com/microsoft/unilm/blob/master/LICENSE) |
| Source | [https://huggingface.co/intfloat/e5-base-v2](https://huggingface.co/intfloat/e5-base-v2) |
| Language | English |
| Component declaration | 

```
```
<component id="my-embedder-id" type="hugging-face-embedder">
        <transformer-model model-id="e5-base-v2"/>
        <max-tokens>512</max-tokens>
        <prepend>
            <query>query: </query>
            <document>passage: </document>
        </prepend>
    </component>
```
```

 |
| 
#### e5-large-v2
 |
| --- |
| 

The largest model of the _E5_ family, at time of writing, this is the best performing embedding model on the MTEB benchmark.

 |
| Model-id | e5-large-v2 |
| Tensor definition | `tensor<float>(x[1024])` or `tensor<float>(p{},x[1024])` |
| [distance-metric](../reference/schemas/schemas.html#distance-metric) | `angular` |
| License | [MIT](https://github.com/microsoft/unilm/blob/master/LICENSE) |
| Source | [https://huggingface.co/intfloat/e5-large-v2](https://huggingface.co/intfloat/e5-large-v2) |
| Language | English |
| Component declaration | 

```
```
<component id="my-embedder-id" type="hugging-face-embedder">
        <transformer-model model-id="e5-large-v2"/>
        <max-tokens>512</max-tokens>
        <prepend>
            <query>query: </query>
            <document>passage: </document>
        </prepend>
    </component>
```
```

 |
| 
#### multilingual-e5-base
 |
| --- |
| 

The multilingual model of the _E5_ family. Use this model for multilingual queries and documents.

 |
| Model-id | multilingual-e5-base |
| Tensor definition | `tensor<float>(x[768])` or `tensor<float>(p{},x[768])` |
| [distance-metric](../reference/schemas/schemas.html#distance-metric) | `angular` |
| License | [MIT](https://github.com/microsoft/unilm/blob/master/LICENSE) |
| Source | [https://huggingface.co/intfloat/multilingual-e5-base](https://huggingface.co/intfloat/multilingual-e5-base) |
| Language | Multilingual |
| Component declaration | 

```
```
<component id="my-embedder-id" type="hugging-face-embedder">
        <transformer-model model-id="multilingual-e5-base"/>
        <max-tokens>512</max-tokens>
        <prepend>
            <query>query: </query>
            <document>passage: </document>
        </prepend>
    </component>
```
```

 |

### Bert Embedder

These models are available for the [Bert Embedder](../rag/embedding.html#bert-embedder)`type="bert-embedder"`:

```
```
<container id="default" version="1.0">
    <component id="mini" type="bert-embedder">
        <transformer-model model-id="minilm-l6-v2"/>
        <tokenizer-vocab model-id="bert-base-uncased"/>
    </component>
    ...
</container>
```
```

Note bert-embedder requires both `transformer-model` and `tokenizer-vocab`.

| 
#### minilm-l6-v2
 |
| --- |
| 

A small, fast sentence-transformer model.

 |
| Model-id | minilm-l6-v2 |
| Tensor definition | `tensor<float>(x[384])` or `tensor<float>(p{},x[384])` |
| [distance-metric](../reference/schemas/schemas.html#distance-metric) | `angular` |
| License | [apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Source | [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) |
| Language | English |
| 
#### mpnet-base-v2
 |
| --- |
| 

A larger, but better than **minilm-l6-v2** sentence-transformer model.

 |
| Model-id | mpnet-base-v2 |
| Tensor definition | `tensor<float>(x[768])` or `tensor<float>(p{},x[768])` |
| [distance-metric](../reference/schemas/schemas.html#distance-metric) | `angular` |
| License | [apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Source | [https://huggingface.co/sentence-transformers/all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2) |
| Language | English |

### Tokenization Embedders

These are embedder implementations that tokenize text and embed string to the vocabulary identifiers. These are most useful for creating the tensor inputs to re-ranking models that take both the query and document token identifiers as input. Find examples in the [sample applications](https://github.com/vespa-engine/sample-apps/blob/master/README.md#vector-search-hybrid-search-and-embeddings).

| 
#### bert-base-uncased
 |
| --- |
| A vocabulary text (_vocab.txt_) file on the format expected by [WordPiece](../reference/rag/embedding.html#wordpiece-embedder): A text token per line. |
| Model-id | bert-base-uncased |
| License | [apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Source | [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) |
| 
#### e5-base-v2-vocab
 |
| --- |
| A _tokenizer.json_ configuration file on the format expected by [HF tokenizer](../reference/rag/embedding.html#huggingface-tokenizer-embedder). This tokenizer configuration can be used with `e5-base-v2`, `e5-small-v2` and `e5-large-v2`. |
| Model-id | e5-base-v2-vocab |
| License | [MIT](https://github.com/microsoft/unilm/blob/master/LICENSE) |
| Source | [https://huggingface.co/intfloat/e5-base-v2](https://huggingface.co/intfloat/e5-base-v2) |
| Language | English |
| 
#### multilingual-e5-base-vocab
 |
| --- |
| A _tokenizer.json_ configuration file on the format expected by [HF tokenizer](../reference/rag/embedding.html#huggingface-tokenizer-embedder). This tokenizer configuration can be used with `multilingual-e5-base-vocab`. |
| Model-id | multilingual-e5-base-vocab |
| License | [MIT](https://github.com/microsoft/unilm/blob/master/LICENSE) |
| Source | [https://huggingface.co/intfloat/multilingual-e5-base](https://huggingface.co/intfloat/multilingual-e5-base) |
| Language | Multilingual |

### Significance models

These are [global significance models](../ranking/significance#significance-models-in-servicesxml) that can be added to [significance element in services.xml](../reference/applications/services/search.html#significance).

| 
#### significance-en-wikipedia-v1
 |
| --- |
| This significance model was generated from [English Wikipedia dump data from 2024-08-01](https://dumps.wikimedia.org/enwiki/). Available in Vespa as of version 8.426.8. |
| Model-id | significance-en-wikipedia-v1 |
| License | [Creative Commons Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0) License](https://creativecommons.org/licenses/by-sa/3.0/deed.en). |
| Source | [https://data.vespa-cloud.com/significance\_models/significance-en-wikipedia-v1.json.zst](https://data.vespa-cloud.com/significance_models/significance-en-wikipedia-v1.json.zst) |
| Language | English |

## Creating applications working both self-hosted and on Vespa Cloud

You can also specify both a `model-id`, which will be used on Vespa Cloud, and a url/path, which will be used on self-hosted deployments:

```
```
<transformer-model model-id="minilm-l6-v2" path="myAppPackageModels/myModel.onnx"/>
```
```

This can be useful for example to create an application package which uses models from Vespa Cloud for production and a scaled-down or dummy model for self-hosted development.

## Using Vespa Cloud models with any config

Specifying a model-id can be done for any[config field of type `model`](../applications/configuring-components.html#adding-files-to-the-component-configuration), whether the config is from Vespa or defined by you.

 Copyright © 2026 - [Cookie Preferences](#)

### On this page:

- [Vespa Cloud Embedding Models](#vespa-cloud-embedding-models)
- [Huggingface Embedder](#hugging-face-embedder)
- [Bert Embedder](#bert-embedder)
- [Tokenization Embedders](#tokenization-embedders)
- [Significance models](#significance-models)
- [Creating applications working both self-hosted and on Vespa Cloud](#creating-applications-working-both-self-hosted-and-on-vespa-cloud)
- [Using Vespa Cloud models with any config](#using-vespa-cloud-models-with-any-config)

