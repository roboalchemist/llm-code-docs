# [Anchor](https://qdrant.tech/documentation/search-precision/automate-filtering-with-llms/\#automate-filtering-with-llms) Automate filtering with LLMs

Our [complete guide to filtering in vector search](https://qdrant.tech/articles/vector-search-filtering/) describes why filtering is
important, and how to implement it with Qdrant. However, applying filters is easier when you build an application
with a traditional interface. Your UI may contain a form with checkboxes, sliders, and other elements that users can
use to set their criteria. But what if you want to build a RAG-powered application with just the conversational
interface, or even voice commands? In this case, you need to automate the filtering process!

LLMs seem to be particularly good at this task. They can understand natural language and generate structured output
based on it. In this tutorial, we’ll show you how to use LLMs to automate filtering in your vector search application.

## [Anchor](https://qdrant.tech/documentation/search-precision/automate-filtering-with-llms/\#few-notes-on-qdrant-filters) Few notes on Qdrant filters

Qdrant Python SDK defines the models using [Pydantic](https://docs.pydantic.dev/latest/). This library is de facto
standard for data validation and serialization in Python. It allows you to define the structure of your data using
Python type hints. For example, our `Filter` model is defined as follows:

```python
class Filter(BaseModel, extra="forbid"):
    should: Optional[Union[List["Condition"], "Condition"]] = Field(
        default=None, description="At least one of those conditions should match"
    )
    min_should: Optional["MinShould"] = Field(
        default=None, description="At least minimum amount of given conditions should match"
    )
    must: Optional[Union[List["Condition"], "Condition"]] = Field(default=None, description="All conditions must match")
    must_not: Optional[Union[List["Condition"], "Condition"]] = Field(
        default=None, description="All conditions must NOT match"
    )

```

Qdrant filters may be nested, and you can express even the most complex conditions using the `must`, `should`, and
`must_not` notation.

## [Anchor](https://qdrant.tech/documentation/search-precision/automate-filtering-with-llms/\#structured-output-from-llms) Structured output from LLMs

It isn’t an uncommon practice to use LLMs to generate structured output. It is primarily useful if their output is
intended for further processing by a different application. For example, you can use LLMs to generate SQL queries,
JSON objects, and most importantly, Qdrant filters. Pydantic got adopted by the LLM ecosystem quite well, so there is
plenty of libraries which uses Pydantic models to define the structure of the output for the Language Models.

One of the interesting projects in this area is [Instructor](https://python.useinstructor.com/) that allows you to
play with different LLM providers and restrict their output to a specific structure. Let’s install the library and
already choose a provider we’ll use in this tutorial:

```shell
pip install "instructor[anthropic]"

```

Anthropic is not the only option out there, as Instructor supports many other providers including OpenAI, Ollama,
Llama, Gemini, Vertex AI, Groq, Litellm and others. You can choose the one that fits your needs the best, or the one
you already use in your RAG.

## [Anchor](https://qdrant.tech/documentation/search-precision/automate-filtering-with-llms/\#using-instructor-to-generate-qdrant-filters) Using Instructor to generate Qdrant filters

Instructor has some helper methods to decorate the LLM APIs, so you can interact with them as if you were using their
normal SDKs. In case of Anthropic, you just pass an instance of `Anthropic` class to the `from_anthropic` function:

```python
import instructor
from anthropic import Anthropic

anthropic_client = instructor.from_anthropic(
    client=Anthropic(
        api_key="YOUR_API_KEY",
    )
)

```

A decorated client slightly modifies the original API, so you can pass the `response_model` parameter to the
`.messages.create` method. This parameter should be a Pydantic model that defines the structure of the output. In case
of Qdrant filters, it should be a `Filter` model:

```python
from qdrant_client import models

qdrant_filter = anthropic_client.messages.create(
    model="claude-3-5-sonnet-latest",
    response_model=models.Filter,
    max_tokens=1024,
    messages=[\
        {\
            "role": "user",\
            "content": "red T-shirt"\
        }\
    ],
)

```

The output of this code will be a Pydantic model that represents a Qdrant filter. Surprisingly, there is no need to pass
additional instructions to already figure out that the user wants to filter by the color and the type of the product.
Here is how the output looks like:

```python
Filter(
    should=None,
    min_should=None,
    must=[\
        FieldCondition(\
            key="color",\
            match=MatchValue(value="red"),\
            range=None,\
            geo_bounding_box=None,\
            geo_radius=None,\
            geo_polygon=None,\
            values_count=None\
        ),\
        FieldCondition(\
            key="type",\
            match=MatchValue(value="t-shirt"),\
            range=None,\
            geo_bounding_box=None,\
            geo_radius=None,\
            geo_polygon=None,\
            values_count=None\
        )\
    ],
    must_not=None
)

```

Obviously, giving the model complete freedom to generate the filter may lead to unexpected results, or no results at
all. Your collection probably has payloads with a specific structure, so it doesn’t make sense to use anything else.
Moreover, **it’s considered a good practice to filter by the fields that have been indexed**. That’s why it makes sense
to automatically determine the indexed fields and restrict the output to them.

### [Anchor](https://qdrant.tech/documentation/search-precision/automate-filtering-with-llms/\#restricting-the-available-fields) Restricting the available fields

Qdrant collection info contains a list of the indexes created on a particular collection. You can use this information
to automatically determine the fields that can be used for filtering. Here is how you can do it:

```python
from qdrant_client import QdrantClient

client = QdrantClient("http://localhost:6333")
collection_info = client.get_collection(collection_name="test_filter")
indexes = collection_info.payload_schema
print(indexes)

```

Output:

```python
{
    "city.location": PayloadIndexInfo(
        data_type=PayloadSchemaType.GEO,
        ...
    ),
    "city.name": PayloadIndexInfo(
        data_type=PayloadSchemaType.KEYWORD,
        ...
    ),
    "color": PayloadIndexInfo(
        data_type=PayloadSchemaType.KEYWORD,
        ...
    ),
    "fabric": PayloadIndexInfo(
        data_type=PayloadSchemaType.KEYWORD,
        ...
    ),
    "price": PayloadIndexInfo(
        data_type=PayloadSchemaType.FLOAT,
        ...
    ),
}

```

Our LLM should know the names of the fields it can use, but also their type, as e.g., range filtering only makes sense
for numerical fields, and geo filtering on non-geo fields won’t yield anything meaningful. You can pass this information
as a part of the prompt to the LLM, so let’s encode it as a string:

```python
formatted_indexes = "\n".join([\
    f"- {index_name} - {index.data_type.name}"\
    for index_name, index in indexes.items()\
])
print(formatted_indexes)

```

Output:

```text
- fabric - KEYWORD
- city.name - KEYWORD
- color - KEYWORD
- price - FLOAT
- city.location - GEO

```

**It’s a good idea to cache the list of the available fields and their types**, as they are not supposed to change
often. Our interactions with the LLM should be slightly different now:

```python
qdrant_filter = anthropic_client.messages.create(
    model="claude-3-5-sonnet-latest",
    response_model=models.Filter,
    max_tokens=1024,
    messages=[\
        {\
            "role": "user",\
            "content": (\
                "<query>color is red</query>"\
                f"<indexes>\n{formatted_indexes}\n</indexes>"\
            )\
        }\
    ],
)

```

Output:

```python
Filter(
    should=None,
    min_should=None,
    must=FieldCondition(
        key="color",
        match=MatchValue(value="red"),
        range=None,
        geo_bounding_box=None,
        geo_radius=None,
        geo_polygon=None,
        values_count=None
    ),
    must_not=None
)

```

The same query, restricted to the available fields, now generates better criteria, as it doesn’t try to filter by the
fields that don’t exist in the collection.

### [Anchor](https://qdrant.tech/documentation/search-precision/automate-filtering-with-llms/\#testing-the-llm-output) Testing the LLM output

Although the LLMs are quite powerful, they are not perfect. If you plan to automate filtering, it makes sense to run
some tests to see how well they perform. Especially edge cases, like queries that cannot be expressed as filters. Let’s
see how the LLM will handle the following query:

```python
qdrant_filter = anthropic_client.messages.create(
    model="claude-3-5-sonnet-latest",
    response_model=models.Filter,
    max_tokens=1024,
    messages=[\
        {\
            "role": "user",\
            "content": (\
                "<query>fruit salad with no more than 100 calories</query>"\
                f"<indexes>\n{formatted_indexes}\n</indexes>"\
            )\
        }\
    ],
)

```

Output:

```python
Filter(
    should=None,
    min_should=None,
    must=FieldCondition(
        key="price",
        match=None,
        range=Range(lt=None, gt=None, gte=None, lte=100.0),
        geo_bounding_box=None,
        geo_radius=None,
        geo_polygon=None,
        values_count=None
    ),
    must_not=None
)

```

Surprisingly, the LLM extracted the calorie information from the query and generated a filter based on the price field.
It somehow extracts any numerical information from the query and tries to match it with the available fields.

Generally, giving model some more guidance on how to interpret the query may lead to better results. Adding a system
prompt that defines the rules for the query interpretation may help the model to do a better job. Here is how you can
do it:

```python
SYSTEM_PROMPT = """
You are extracting filters from a text query. Please follow the following rules:
1. Query is provided in the form of a text enclosed in <query> tags.
2. Available indexes are put at the end of the text in the form of a list enclosed in <indexes> tags.
3. You cannot use any field that is not available in the indexes.
4. Generate a filter only if you are certain that user's intent matches the field name.
5. Prices are always in USD.
6. It's better not to generate a filter than to generate an incorrect one.
"""

qdrant_filter = anthropic_client.messages.create(
    model="claude-3-5-sonnet-latest",
    response_model=models.Filter,
    max_tokens=1024,
    messages=[\
        {\
            "role": "user",\
            "content": SYSTEM_PROMPT.strip(),\
        },\
        {\
            "role": "assistant",\
            "content": "Okay, I will follow all the rules."\
        },\
        {\
            "role": "user",\
            "content": (\
                "<query>fruit salad with no more than 100 calories</query>"\
                f"<indexes>\n{formatted_indexes}\n</indexes>"\
            )\
        }\
    ],
)

```

Current output:

```python
Filter(
    should=None,
    min_should=None,
    must=None,
    must_not=None
)

```

### [Anchor](https://qdrant.tech/documentation/search-precision/automate-filtering-with-llms/\#handling-complex-queries) Handling complex queries

We have a bunch of indexes created on the collection, and it is quite interesting to see how the LLM will handle more
complex queries. For example, let’s see how it will handle the following query:

```python
qdrant_filter = anthropic_client.messages.create(
    model="claude-3-5-sonnet-latest",
    response_model=models.Filter,
    max_tokens=1024,
    messages=[\
        {\
            "role": "user",\
            "content": SYSTEM_PROMPT.strip(),\
        },\
        {\
            "role": "assistant",\
            "content": "Okay, I will follow all the rules."\
        },\
        {\
            "role": "user",\
            "content": (\
                "<query>"\
                "white T-shirt available no more than 30 miles from London, "\
                "but not in the city itself, below $15.70, not made from polyester"\
                "</query>\n"\
                "<indexes>\n"\
                f"{formatted_indexes}\n"\
                "</indexes>"\
            )\
        },\
    ],
)

```

It might be surprising, but Anthropic Claude is able to generate even such complex filters. Here is the output:

```python
Filter(
    should=None,
    min_should=None,
    must=[\
        FieldCondition(\
            key="color",\
            match=MatchValue(value="white"),\
            range=None,\
            geo_bounding_box=None,\
            geo_radius=None,\
            geo_polygon=None,\
            values_count=None\
        ),\
        FieldCondition(\
            key="city.location",\
            match=None,\
            range=None,\
            geo_bounding_box=None,\
            geo_radius=GeoRadius(\
                center=GeoPoint(lon=-0.1276, lat=51.5074),\
                radius=48280.0\
            ),\
            geo_polygon=None,\
            values_count=None\
        ),\
        FieldCondition(\
            key="price",\
            match=None,\
            range=Range(lt=15.7, gt=None, gte=None, lte=None),\
            geo_bounding_box=None,\
            geo_radius=None,\
            geo_polygon=None,\
            values_count=None\
        )\
    ], must_not=[\
        FieldCondition(\
            key="city.name",\
            match=MatchValue(value="London"),\
            range=None,\
            geo_bounding_box=None,\
            geo_radius=None,\
            geo_polygon=None,\
            values_count=None\
        ),\
        FieldCondition(\
            key="fabric",\
            match=MatchValue(value="polyester"),\
            range=None,\
            geo_bounding_box=None,\
            geo_radius=None,\
            geo_polygon=None,\
            values_count=None\
        )\
    ]
)

```

The model even knows the coordinates of London and uses them to generate the geo filter. It isn’t the best idea to
rely on the model to generate such complex filters, but it’s quite impressive that it can do it.

## [Anchor](https://qdrant.tech/documentation/search-precision/automate-filtering-with-llms/\#further-steps) Further steps

Real production systems would rather require more testing and validation of the LLM output. Building a ground truth
dataset with the queries and the expected filters would be a good idea. You can use this dataset to evaluate the model
performance and to see how it behaves in different scenarios.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/search-precision/automate-filtering-with-llms.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/search-precision/automate-filtering-with-llms.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-31-lllmstxt|>
## sitemap.xml
https://qdrant.tech/articles/distance-based-exploration/2025-03-11T14:27:31+01:00https://qdrant.tech/articles/modern-sparse-neural-retrieval/2025-05-15T19:37:07+05:30https://qdrant.tech/articles/cross-encoder-integration-gsoc/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/what-is-a-vector-database/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/what-is-vector-quantization/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/vector-search-resource-optimization/2025-05-09T12:38:02+05:30https://qdrant.tech/articles/vector-search-filtering/2025-01-06T10:45:10+01:00https://qdrant.tech/articles/immutable-data-structures/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/minicoil/2025-05-13T18:20:11+02:00https://qdrant.tech/articles/search-feedback-loop/2025-04-01T12:23:31+02:00https://qdrant.tech/articles/dedicated-vector-search/2025-02-18T12:54:36-05:00https://qdrant.tech/articles/late-interaction-models/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/indexing-optimization/2025-03-24T19:51:41+01:00https://qdrant.tech/articles/gridstore-key-value-storage/2025-02-05T09:42:23-05:00https://qdrant.tech/articles/agentic-rag/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/hybrid-search/2025-01-03T10:53:26+01:00https://qdrant.tech/articles/what-is-rag-in-ai/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/bm42/2025-04-10T12:02:16+02:00https://qdrant.tech/articles/qdrant-1.8.x/2024-07-07T18:34:56-07:00https://qdrant.tech/articles/rapid-rag-optimization-with-qdrant-and-quotient/2025-05-15T19:33:44+05:30https://qdrant.tech/articles/rag-is-dead/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/binary-quantization-openai/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/multitenancy/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/data-privacy/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/discovery-search/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/what-are-embeddings/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/sparse-vectors/2025-03-04T22:08:36+01:00https://qdrant.tech/articles/qdrant-1.7.x/2024-10-05T03:39:41+05:30https://qdrant.tech/articles/new-recommendation-api/2024-03-07T20:31:05+01:00https://qdrant.tech/articles/dedicated-service/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/fastembed/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/geo-polygon-filter-gsoc/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/binary-quantization/2025-04-10T09:21:38-03:00https://qdrant.tech/articles/food-discovery-demo/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/web-ui-gsoc/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/dimension-reduction-qsoc/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/search-as-you-type/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/vector-similarity-beyond-search/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/serverless/2025-02-18T21:01:07+05:30https://qdrant.tech/documentation/database-tutorials/bulk-upload/2025-03-25T21:43:45-03:00https://qdrant.tech/benchmarks/benchmarks-intro/2024-06-27T12:40:08+02:00https://qdrant.tech/documentation/faq/qdrant-fundamentals/2025-05-02T10:37:48+02:00https://qdrant.tech/documentation/search-precision/reranking-semantic-search/2025-05-21T15:27:35+08:00https://qdrant.tech/documentation/cloud-rbac/role-management/2025-05-02T16:53:21+02:00https://qdrant.tech/documentation/beginner-tutorials/search-beginners/2025-04-25T19:32:48+03:00https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-setup/2025-03-10T22:19:22+01:00https://qdrant.tech/documentation/private-cloud/private-cloud-setup/2025-06-03T09:48:32+02:00https://qdrant.tech/documentation/overview/vector-search/2024-10-05T03:39:41+05:30https://qdrant.tech/articles/qdrant-1.3.x/2024-03-07T20:31:05+01:00https://qdrant.tech/benchmarks/single-node-speed-benchmark/2024-06-17T22:01:23+02:00https://qdrant.tech/benchmarks/single-node-speed-benchmark-2022/2024-01-11T19:41:06+05:30https://qdrant.tech/documentation/search-precision/automate-filtering-with-llms/2025-05-27T18:00:51+02:00https://qdrant.tech/documentation/beginner-tutorials/neural-search/2024-11-18T15:26:15-08:00https://qdrant.tech/documentation/private-cloud/configuration/2025-03-21T16:37:49+01:00https://qdrant.tech/documentation/database-tutorials/create-snapshot/2025-06-12T09:02:54+03:00https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-cluster-creation/2025-06-16T17:51:31+02:00https://qdrant.tech/documentation/data-ingestion-beginners/2025-05-15T20:16:43+05:30https://qdrant.tech/documentation/faq/database-optimization/2024-10-05T03:39:41+05:30https://qdrant.tech/documentation/2024-12-20T13:10:51+01:00https://qdrant.tech/documentation/advanced-tutorials/using-multivector-representations/2025-06-10T11:40:10+03:00https://qdrant.tech/documentation/database-tutorials/large-scale-search/2025-03-24T14:27:15-03:00https://qdrant.tech/documentation/fastembed/fastembed-quickstart/2024-08-06T15:42:27-07:00https://qdrant.tech/documentation/advanced-tutorials/reranking-hybrid-search/2025-06-05T14:05:27+03:00https://qdrant.tech/documentation/advanced-tutorials/code-search/2025-05-15T19:33:03+05:30https://qdrant.tech/documentation/agentic-rag-crewai-zoom/2025-04-09T12:55:16+02:00https://qdrant.tech/documentation/cloud-rbac/user-management/2025-05-02T18:40:38+02:00https://qdrant.tech/articles/io\_uring/2024-12-20T13:10:51+01:00https://qdrant.tech/benchmarks/filtered-search-intro/2024-01-11T19:41:06+05:30https://qdrant.tech/documentation/agentic-rag-langgraph/2025-05-15T19:37:07+05:30https://qdrant.tech/documentation/advanced-tutorials/collaborative-filtering/2024-11-18T15:26:15-08:00https://qdrant.tech/documentation/hybrid-cloud/operator-configuration/2024-12-23T12:11:13+01:00https://qdrant.tech/documentation/fastembed/fastembed-semantic-search/2025-04-26T13:30:39+03:00https://qdrant.tech/documentation/database-tutorials/huggingface-datasets/2024-11-18T15:26:15-08:00https://qdrant.tech/documentation/private-cloud/qdrant-cluster-management/2025-06-16T17:51:31+02:00https://qdrant.tech/documentation/cloud-rbac/permission-reference/2025-06-13T08:39:21+02:00https://qdrant.tech/documentation/beginner-tutorials/hybrid-search-fastembed/2025-04-26T18:10:19+03:00https://qdrant.tech/documentation/overview/2025-04-26T22:59:20-07:00https://qdrant.tech/articles/product-quantization/2025-02-04T13:55:26+01:00https://qdrant.tech/benchmarks/filtered-search-benchmark/2024-01-11T19:41:06+05:30https://qdrant.tech/documentation/agentic-rag-camelai-discord/2025-04-09T12:55:16+02:00https://qdrant.tech/documentation/private-cloud/backups/2024-09-05T15:17:16+02:00https://qdrant.tech/documentation/database-tutorials/async-api/2025-02-18T21:01:07+05:30https://qdrant.tech/documentation/cloud-quickstart/2025-05-29T08:51:37-04:00https://qdrant.tech/documentation/quickstart/2025-01-20T10:08:10+01:00https://qdrant.tech/documentation/private-cloud/logging-monitoring/2025-02-11T18:21:40+01:00https://qdrant.tech/documentation/beginner-tutorials/retrieval-quality/2024-11-18T15:26:15-08:00https://qdrant.tech/documentation/hybrid-cloud/networking-logging-monitoring/2025-02-11T18:21:40+01:00https://qdrant.tech/documentation/advanced-tutorials/pdf-retrieval-at-scale/2025-01-28T15:29:08+01:00https://qdrant.tech/articles/scalar-quantization/2024-12-20T13:10:51+01:00https://qdrant.tech/documentation/interfaces/2024-11-21T17:41:45+05:30https://qdrant.tech/documentation/private-cloud/api-reference/2025-06-03T09:48:32+02:00https://qdrant.tech/documentation/private-cloud/changelog/2025-06-03T09:48:32+02:00https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/2024-11-18T15:42:18-08:00https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/2025-04-30T22:48:05+05:30https://qdrant.tech/documentation/guides/installation/2025-05-02T10:37:48+02:00https://qdrant.tech/documentation/multimodal-search/2025-04-09T12:55:16+02:00https://qdrant.tech/documentation/fastembed/fastembed-splade/2025-04-25T19:38:33+03:00https://qdrant.tech/articles/seed-round/2024-03-07T20:31:05+01:00https://qdrant.tech/articles/langchain-integration/2024-12-20T13:10:51+01:00https://qdrant.tech/documentation/rag-deepseek/2025-04-26T13:02:13+03:00https://qdrant.tech/documentation/web-ui/2024-11-20T23:14:39+05:30https://qdrant.tech/documentation/fastembed/fastembed-colbert/2025-06-19T16:21:03+04:00https://qdrant.tech/articles/chatgpt-plugin/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/memory-consumption/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/qa-with-cohere-and-qdrant/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/qdrant-1.2.x/2024-03-07T20:31:05+01:00https://qdrant.tech/articles/dataset-quality/2024-12-20T13:10:51+01:00https://qdrant.tech/documentation/concepts/2024-11-14T18:59:28+01:00https://qdrant.tech/documentation/fastembed/fastembed-rerankers/2025-04-26T13:20:52+03:00https://qdrant.tech/articles/faq-question-answering/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/why-rust/2024-09-05T13:07:07-07:00https://qdrant.tech/articles/embedding-recycler/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/cars-recognition/2024-12-20T13:10:51+01:00https://qdrant.tech/documentation/guides/administration/2025-05-19T15:01:52+02:00https://qdrant.tech/benchmarks/benchmark-faq/2024-01-11T19:41:06+05:30https://qdrant.tech/documentation/guides/running-with-gpu/2025-03-20T15:19:07+01:00https://qdrant.tech/articles/vector-search-manuals/2024-12-20T13:10:51+01:00https://qdrant.tech/documentation/guides/capacity-planning/2024-10-05T03:39:41+05:30https://qdrant.tech/documentation/fastembed/2025-05-27T18:00:51+02:00https://qdrant.tech/documentation/guides/optimize/2025-04-07T00:40:39+02:00https://qdrant.tech/documentation/cloud-getting-started/2025-05-02T16:53:21+02:00https://qdrant.tech/documentation/guides/multiple-partitions/2025-04-07T00:40:39+02:00https://qdrant.tech/documentation/qdrant-mcp-server/2025-05-27T18:00:51+02:00https://qdrant.tech/documentation/cloud-account-setup/2025-05-02T18:40:38+02:00https://qdrant.tech/documentation/cloud-rbac/2025-05-02T16:53:21+02:00https://qdrant.tech/documentation/cloud/2025-05-02T16:53:21+02:00https://qdrant.tech/documentation/hybrid-cloud/2025-05-02T16:53:21+02:00https://qdrant.tech/documentation/beginner-tutorials/2024-11-18T15:26:15-08:00https://qdrant.tech/documentation/advanced-tutorials/2025-02-07T18:51:10-05:00https://qdrant.tech/documentation/private-cloud/2025-05-02T16:53:21+02:00https://qdrant.tech/documentation/cloud-pricing-payments/2025-05-02T16:53:21+02:00https://qdrant.tech/documentation/examples/qdrant-dspy-medicalbot/2025-06-19T11:54:06+03:00https://qdrant.tech/documentation/data-management/2025-05-31T21:49:18+02:00https://qdrant.tech/documentation/examples/llama-index-multitenancy/2024-04-11T13:13:14-07:00https://qdrant.tech/documentation/database-tutorials/2025-06-11T19:02:35+03:00https://qdrant.tech/documentation/embeddings/2024-11-28T08:54:13+05:30https://qdrant.tech/documentation/cloud-premium/2025-05-02T16:53:21+02:00https://qdrant.tech/articles/metric-learning-tips/2024-12-20T13:10:51+01:00https://qdrant.tech/documentation/cloud/create-cluster/2025-05-02T16:53:21+02:00https://qdrant.tech/documentation/frameworks/2025-05-19T21:17:24+05:30https://qdrant.tech/articles/qdrant-internals/2024-12-20T13:10:51+01:00https://qdrant.tech/documentation/observability/2024-11-14T18:59:28+01:00https://qdrant.tech/documentation/platforms/2025-05-14T07:24:10-04:00https://qdrant.tech/documentation/examples/rag-chatbot-red-hat-openshift-haystack/2024-05-15T18:01:28+02:00https://qdrant.tech/documentation/examples/cohere-rag-connector/2025-02-18T21:01:07+05:30https://qdrant.tech/documentation/send-data/2024-11-14T18:59:28+01:00https://qdrant.tech/documentation/examples/2025-06-19T11:54:06+03:00https://qdrant.tech/documentation/examples/rag-customer-support-cohere-airbyte-aws/2025-02-18T21:01:07+05:30https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/2024-04-15T17:41:39-07:00https://qdrant.tech/documentation/cloud-api/2025-06-06T09:56:35+02:00https://qdrant.tech/documentation/cloud-tools/2024-11-19T17:56:47-08:00https://qdrant.tech/documentation/examples/rag-contract-management-stackit-aleph-alpha/2025-02-18T21:01:07+05:30https://qdrant.tech/documentation/datasets/2024-11-14T18:59:28+01:00https://qdrant.tech/articles/detecting-coffee-anomalies/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/triplet-loss/2024-12-20T13:10:51+01:00https://qdrant.tech/documentation/cloud/authentication/2025-05-02T16:53:21+02:00https://qdrant.tech/documentation/concepts/collections/2025-04-07T00:40:39+02:00https://qdrant.tech/articles/data-exploration/2024-12-20T13:10:51+01:00https://qdrant.tech/documentation/examples/natural-language-search-oracle-cloud-infrastructure-cohere-langchain/2024-04-15T19:50:07-07:00https://qdrant.tech/documentation/examples/rag-chatbot-vultr-dspy-ollama/2025-05-15T19:37:07+05:30https://qdrant.tech/documentation/examples/recommendation-system-ovhcloud/2024-08-23T22:48:27+05:30https://qdrant.tech/documentation/examples/rag-chatbot-scaleway/2025-02-18T21:01:07+05:30https://qdrant.tech/documentation/cloud/cluster-access/2025-05-02T16:53:21+02:00https://qdrant.tech/documentation/support/2025-04-08T10:25:18+02:00https://qdrant.tech/documentation/send-data/databricks/2024-07-29T21:03:45+05:30https://qdrant.tech/documentation/send-data/qdrant-airflow-astronomer/2024-08-13T13:38:38+03:00https://qdrant.tech/articles/machine-learning/2024-12-20T13:10:51+01:00https://qdrant.tech/documentation/concepts/points/2025-04-07T00:40:39+02:00https://qdrant.tech/documentation/concepts/vectors/2025-04-07T00:40:39+02:00https://qdrant.tech/documentation/concepts/payload/2025-04-07T00:40:39+02:00https://qdrant.tech/documentation/send-data/data-streaming-kafka-qdrant/2024-07-22T17:09:17-07:00https://qdrant.tech/articles/neural-search-tutorial/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/rag-and-genai/2024-12-20T13:10:51+01:00https://qdrant.tech/documentation/cloud/cluster-scaling/2025-05-02T16:53:21+02:00https://qdrant.tech/documentation/concepts/search/2025-04-07T00:40:39+02:00https://qdrant.tech/documentation/concepts/explore/2025-06-12T10:45:50-04:00https://qdrant.tech/documentation/cloud/cluster-monitoring/2025-05-02T16:53:21+02:00https://qdrant.tech/documentation/cloud/cluster-upgrades/2025-05-02T16:53:21+02:00https://qdrant.tech/documentation/concepts/hybrid-queries/2025-04-23T11:15:58+02:00https://qdrant.tech/articles/filtrable-hnsw/2024-12-20T13:10:51+01:00https://qdrant.tech/documentation/concepts/filtering/2025-06-09T18:30:19+03:30https://qdrant.tech/articles/practicle-examples/2024-12-20T13:10:51+01:00https://qdrant.tech/documentation/cloud/backups/2025-05-02T16:53:21+02:00https://qdrant.tech/articles/qdrant-0-11-release/2022-12-06T13:12:27+01:00https://qdrant.tech/articles/qdrant-0-10-release/2024-05-15T18:01:28+02:00https://qdrant.tech/documentation/concepts/optimizer/2024-11-27T16:59:34+01:00https://qdrant.tech/documentation/concepts/storage/2025-04-07T00:40:39+02:00https://qdrant.tech/documentation/concepts/indexing/2025-04-07T00:40:39+02:00https://qdrant.tech/documentation/guides/distributed\_deployment/2025-02-03T17:33:39+06:00https://qdrant.tech/documentation/concepts/snapshots/2025-06-12T09:02:54+03:00https://qdrant.tech/documentation/guides/quantization/2025-04-07T00:40:39+02:00https://qdrant.tech/documentation/guides/monitoring/2025-02-11T18:21:40+01:00https://qdrant.tech/documentation/guides/configuration/2025-02-04T11:00:51+01:00https://qdrant.tech/documentation/guides/security/2025-01-20T16:32:23+01:00https://qdrant.tech/documentation/guides/usage-statistics/2024-12-03T17:03:30+01:00https://qdrant.tech/documentation/guides/common-errors/2025-05-27T12:04:07+02:00https://qdrant.tech/documentation/database-tutorials/migration/2025-06-11T18:57:35+03:00https://qdrant.tech/blog/hybrid-cloud-vultr/2024-05-21T10:11:09+02:00https://qdrant.tech/articles/quantum-quantization/2023-07-13T01:45:36+02:00https://qdrant.tech/blog/hybrid-cloud-stackit/2024-05-21T10:11:09+02:00https://qdrant.tech/blog/hybrid-cloud-scaleway/2024-05-21T10:11:09+02:00https://qdrant.tech/blog/hybrid-cloud-red-hat-openshift/2024-05-21T10:11:09+02:00https://qdrant.tech/blog/hybrid-cloud-ovhcloud/2024-05-21T10:11:09+02:00https://qdrant.tech/blog/hybrid-cloud-llamaindex/2024-05-21T10:11:09+02:00https://qdrant.tech/blog/hybrid-cloud-langchain/2024-05-21T10:11:09+02:00https://qdrant.tech/blog/hybrid-cloud-jinaai/2024-05-21T10:11:09+02:00https://qdrant.tech/blog/hybrid-cloud-haystack/2024-09-24T14:30:20-04:00https://qdrant.tech/blog/hybrid-cloud-digitalocean/2024-05-21T10:11:09+02:00https://qdrant.tech/blog/hybrid-cloud-aleph-alpha/2025-02-04T13:55:26+01:00https://qdrant.tech/blog/hybrid-cloud-airbyte/2025-02-04T13:55:26+01:00https://qdrant.tech/documentation/observability/openllmetry/2024-08-15T08:50:37+05:30https://qdrant.tech/documentation/observability/openlit/2024-08-15T08:50:37+05:30https://qdrant.tech/blog/case-study-lettria-v2/2025-06-16T22:38:02-07:00https://qdrant.tech/2025-06-19T16:21:03+04:00https://qdrant.tech/blog/beta-database-migration-tool/2025-06-18T11:55:05-04:00https://qdrant.tech/blog/case-study-lawme/2025-06-11T09:42:37-07:00https://qdrant.tech/blog/case-study-convosearch/2025-06-10T09:54:12-07:00https://qdrant.tech/blog/legal-tech-builders-guide/2025-06-13T15:44:13-07:00https://qdrant.tech/blog/soc-2-type-ii-hipaa/2025-06-17T16:48:22-07:00https://qdrant.tech/blog/n8n-node/2025-06-09T15:38:39+02:00https://qdrant.tech/blog/datatalks-course/2025-06-05T09:19:05-04:00https://qdrant.tech/blog/case-study-qovery/2025-05-27T11:19:41-07:00https://qdrant.tech/blog/case-study-tripadvisor/2025-05-13T23:15:13-07:00https://qdrant.tech/blog/case-study-aracor/2025-05-13T11:23:13-07:00https://qdrant.tech/blog/case-study-garden-intel/2025-05-09T11:56:26-07:00https://qdrant.tech/blog/product-ui-changes/2025-05-08T09:28:12-04:00https://qdrant.tech/blog/case-study-pariti/2025-05-01T10:05:43-07:00https://qdrant.tech/articles/vector-search-production/2025-04-30T17:47:55+02:00https://qdrant.tech/blog/case-study-dust-v2/2025-05-08T11:45:46-07:00https://qdrant.tech/blog/case-study-sayone/2025-04-29T09:15:10-07:00https://qdrant.tech/blog/superlinked-multimodal-search/2025-04-24T14:10:50+02:00https://qdrant.tech/blog/qdrant-1.14.x/2025-05-02T15:26:42-03:00https://qdrant.tech/blog/case-study-pathwork/2025-05-16T09:10:33-07:00https://qdrant.tech/blog/case-study-lyzr/2025-05-16T09:10:33-07:00https://qdrant.tech/blog/case-study-mixpeek/2025-05-16T09:10:33-07:00https://qdrant.tech/blog/qdrant-n8n-beyond-simple-similarity-search/2025-04-08T11:38:52+02:00https://qdrant.tech/blog/satellite-vector-broadcasting/2025-04-01T08:09:34+02:00https://qdrant.tech/blog/case-study-hubspot/2025-05-16T09:10:33-07:00https://qdrant.tech/blog/webinar-vibe-coding-rag/2025-03-21T16:36:29+01:00https://qdrant.tech/blog/case-study-deutsche-telekom/2025-04-03T08:09:56-04:00https://qdrant.tech/blog/enterprise-vector-search/2025-04-07T15:17:30-04:00https://qdrant.tech/blog/metadata-deasy-labs/2025-02-24T15:04:44-03:00https://qdrant.tech/blog/webinar-crewai-qdrant-obsidian/2025-01-24T16:10:16+01:00https://qdrant.tech/blog/qdrant-1.13.x/2025-01-24T04:19:54-05:00https://qdrant.tech/blog/static-embeddings/2025-01-17T14:53:25+01:00https://qdrant.tech/blog/case-study-voiceflow/2024-12-10T10:26:56-08:00https://qdrant.tech/blog/facial-recognition/2024-12-03T20:56:40-08:00https://qdrant.tech/blog/colpali-qdrant-optimization/2024-11-30T18:57:48-03:00https://qdrant.tech/blog/rag-evaluation-guide/2025-02-18T21:01:07+05:30https://qdrant.tech/blog/case-study-qatech/2024-11-21T16:42:35-08:00https://qdrant.tech/blog/qdrant-colpali/2024-11-06T17:18:48-08:00https://qdrant.tech/blog/case-study-sprinklr/2024-10-18T09:03:19-07:00https://qdrant.tech/blog/qdrant-1.12.x/2024-10-08T19:49:58-07:00https://qdrant.tech/blog/qdrant-deeplearning-ai-course/2024-10-07T12:25:14-07:00https://qdrant.tech/blog/qdrant-for-startups-launch/2024-10-02T19:07:16+05:30https://qdrant.tech/blog/case-study-shakudo/2025-03-13T17:47:05+01:00https://qdrant.tech/blog/qdrant-relari/2024-09-17T15:53:48-07:00https://qdrant.tech/blog/case-study-nyris/2024-09-23T14:05:33-07:00https://qdrant.tech/blog/case-study-kern/2024-09-23T14:05:33-07:00https://qdrant.tech/blog/qdrant-1.11.x/2024-08-16T00:01:23+02:00https://qdrant.tech/blog/case-study-kairoswealth/2024-09-11T14:59:00-07:00https://qdrant.tech/blog/qdrant-1.10.x/2024-07-16T22:00:30+05:30https://qdrant.tech/blog/community-highlights-1/2024-06-21T02:34:01-03:00https://qdrant.tech/blog/cve-2024-3829-response/2024-06-10T12:42:49-04:00https://qdrant.tech/blog/qdrant-soc2-type2-audit/2024-08-29T19:19:43+05:30https://qdrant.tech/blog/qdrant-stars-announcement/2024-10-05T03:39:41+05:30https://qdrant.tech/blog/qdrant-cpu-intel-benchmark/2024-10-08T12:41:46-07:00https://qdrant.tech/blog/qsoc24-interns-announcement/2024-05-08T18:04:46-03:00https://qdrant.tech/articles/semantic-cache-ai-data-retrieval/2024-12-20T13:10:51+01:00https://qdrant.tech/blog/are-you-vendor-locked/2024-05-21T10:11:09+02:00https://qdrant.tech/blog/case-study-visua/2024-05-01T17:59:13-07:00https://qdrant.tech/blog/qdrant-1.9.x/2024-05-21T10:11:09+02:00https://qdrant.tech/blog/hybrid-cloud-launch-partners/2024-05-21T10:11:09+02:00https://qdrant.tech/blog/hybrid-cloud/2024-05-21T10:11:09+02:00https://qdrant.tech/blog/rag-advancements-challenges/2024-04-12T14:45:02+00:00https://qdrant.tech/blog/building-search-rag-open-api/2024-04-12T14:23:42+00:00https://qdrant.tech/blog/gen-ai-and-vector-search/2024-07-07T19:32:50-07:00https://qdrant.tech/blog/teaching-vector-db-at-scale/2024-04-09T11:06:17+00:00https://qdrant.tech/blog/meow-with-cheshire-cat/2024-04-09T11:05:51+00:00https://qdrant.tech/blog/cve-2024-2221-response/2024-08-15T17:31:04+02:00https://qdrant.tech/blog/fastllm-announcement/2024-04-01T04:13:26-07:00https://qdrant.tech/blog/virtualbrain-best-rag/2024-09-20T10:12:14-04:00https://qdrant.tech/blog/youtube-without-paying-cent/2024-03-27T12:44:32+00:00https://qdrant.tech/blog/azure-marketplace/2024-10-05T03:39:41+05:30https://qdrant.tech/blog/real-time-news-distillation-rag/2024-03-25T08:49:27+00:00https://qdrant.tech/blog/insight-generation-platform/2024-03-25T08:51:56+00:00https://qdrant.tech/blog/llm-as-a-judge/2024-03-19T15:05:24+00:00https://qdrant.tech/blog/vector-search-vector-recommendation/2024-03-19T14:22:15+00:00https://qdrant.tech/blog/using-qdrant-and-langchain/2024-05-15T18:01:28+02:00https://qdrant.tech/blog/iris-agent-qdrant/2024-03-06T09:17:19-08:00https://qdrant.tech/blog/case-study-dailymotion/2024-03-07T20:31:05+01:00https://qdrant.tech/blog/comparing-qdrant-vs-pinecone-vector-databases/2025-02-04T13:55:26+01:00https://qdrant.tech/blog/what-is-vector-similarity/2024-09-05T13:07:07-07:00https://qdrant.tech/blog/dspy-vs-langchain/2025-05-15T19:37:07+05:30https://qdrant.tech/blog/qdrant-summer-of-code-24/2024-03-14T18:24:32+01:00https://qdrant.tech/blog/dust-and-qdrant/2024-09-20T10:19:38-04:00https://qdrant.tech/blog/bitter-lesson-generative-language-model/2024-01-29T16:31:02+00:00https://qdrant.tech/blog/indexify-content-extraction-engine/2024-03-07T18:59:29+00:00https://qdrant.tech/blog/qdrant-x-dust-vector-search/2024-07-07T19:40:44-07:00https://qdrant.tech/blog/series-a-funding-round/2024-10-08T12:41:46-07:00https://qdrant.tech/blog/qdrant-cloud-on-microsoft-azure/2024-03-07T20:31:05+01:00https://qdrant.tech/blog/qdrant-benchmarks-2024/2024-03-07T20:31:05+01:00https://qdrant.tech/blog/navigating-challenges-innovations/2024-05-21T09:57:56+02:00https://qdrant.tech/blog/open-source-vector-search-engine-vector-database/2024-07-07T19:36:05-07:00https://qdrant.tech/blog/vector-image-search-rag/2024-01-25T17:51:08+01:00https://qdrant.tech/blog/semantic-search-vector-database/2024-07-07T19:46:08-07:00https://qdrant.tech/blog/llm-complex-search-copilot/2024-01-10T11:42:02+00:00https://qdrant.tech/blog/entity-matching-qdrant/2024-01-10T11:37:51+00:00https://qdrant.tech/blog/fast-embed-models/2024-01-22T10:15:56-08:00https://qdrant.tech/blog/human-language-ai-models/2024-01-10T10:31:15+00:00https://qdrant.tech/blog/binary-quantization/2024-01-10T10:26:06+00:00https://qdrant.tech/blog/qdrant-unstructured/2024-03-07T20:31:05+01:00https://qdrant.tech/blog/qdrant-n8n/2024-03-07T20:31:05+01:00https://qdrant.tech/blog/vector-search-and-applications-record/2024-09-06T13:14:12+02:00https://qdrant.tech/blog/cohere-embedding-v3/2024-09-06T13:14:12+02:00https://qdrant.tech/blog/case-study-pienso/2024-04-10T17:59:48-07:00https://qdrant.tech/blog/case-study-bloop/2024-07-18T19:11:22-07:00https://qdrant.tech/articles/qdrant-introduces-full-text-filters-and-indexes/2024-09-18T15:57:29-07:00https://qdrant.tech/articles/storing-multiple-vectors-per-object-in-qdrant/2024-12-20T13:10:51+01:00https://qdrant.tech/articles/batch-vector-search-with-qdrant/2024-12-20T13:10:51+01:00https://qdrant.tech/blog/qdrant-supports-arm-architecture/2024-01-16T22:02:52+05:30https://qdrant.tech/about-us/2024-05-21T09:57:56+02:00https://qdrant.tech/data-analysis-anomaly-detection/2024-08-29T10:01:03-04:00https://qdrant.tech/advanced-search/2024-08-21T16:31:41-07:00https://qdrant.tech/ai-agents/2025-02-12T08:47:39-06:00https://qdrant.tech/e-commerce/2025-05-22T20:23:57+02:00https://qdrant.tech/documentation/data-management/airbyte/2024-08-15T08:50:37+05:30https://qdrant.tech/documentation/embeddings/aleph-alpha/2024-11-28T08:54:13+05:30https://qdrant.tech/get\_anonymous\_id/2025-03-05T11:26:52+00:00https://qdrant.tech/documentation/data-management/airflow/2025-02-18T21:01:07+05:30https://qdrant.tech/documentation/data-management/nifi/2024-08-15T08:50:37+05:30https://qdrant.tech/documentation/data-management/spark/2025-03-06T10:23:24+05:30https://qdrant.tech/documentation/platforms/apify/2024-08-15T08:50:37+05:30https://qdrant.tech/documentation/frameworks/autogen/2024-11-20T11:50:06+05:30https://qdrant.tech/documentation/embeddings/bedrock/2024-11-28T08:54:13+05:30https://qdrant.tech/documentation/frameworks/lakechain/2024-10-17T11:42:14+05:30https://qdrant.tech/about-us/about-us-resources/2025-05-30T14:14:31+03:00https://qdrant.tech/brand-resources/2024-06-17T16:56:32+03:00https://qdrant.tech/documentation/platforms/bubble/2024-08-15T08:50:37+05:30https://qdrant.tech/security/bug-bounty-program/2025-03-28T09:40:53+01:00https://qdrant.tech/documentation/build/2024-11-18T14:53:02-08:00https://qdrant.tech/documentation/platforms/buildship/2024-08-15T08:50:37+05:30https://qdrant.tech/documentation/frameworks/camel/2024-12-20T13:31:09+05:30https://qdrant.tech/documentation/frameworks/cheshire-cat/2025-01-24T11:47:11+01:00https://qdrant.tech/documentation/data-management/cocoindex/2025-04-20T23:11:21-07:00https://qdrant.tech/documentation/data-management/cognee/2025-05-31T22:06:39+02:00https://qdrant.tech/documentation/embeddings/cohere/2025-02-19T10:27:39+03:00https://qdrant.tech/community/2025-01-07T11:56:39-06:00https://qdrant.tech/documentation/data-management/confluent/2024-08-15T08:50:37+05:30https://qdrant.tech/contact-us/2025-03-13T17:47:05+01:00https://qdrant.tech/legal/credits/2022-04-25T15:19:19+02:00https://qdrant.tech/documentation/frameworks/crewai/2025-02-27T09:21:41+01:00https://qdrant.tech/customers/2024-06-17T16:56:32+03:00https://qdrant.tech/documentation/frameworks/dagster/2025-04-15T18:20:05+05:30https://qdrant.tech/documentation/observability/datadog/2024-10-31T05:56:39+05:30https://qdrant.tech/documentation/frameworks/deepeval/2025-04-24T16:09:40+08:00https://qdrant.tech/documentation/data-management/dlt/2024-08-15T08:50:37+05:30https://qdrant.tech/documentation/frameworks/docarray/2024-08-15T08:50:37+05:30https://qdrant.tech/documentation/platforms/docsgpt/2025-02-18T21:01:07+05:30https://qdrant.tech/documentation/frameworks/dsrag/2024-11-27T17:59:33+05:30https://qdrant.tech/documentation/frameworks/dynamiq/2025-03-24T10:22:45+02:00https://qdrant.tech/articles/ecosystem/2024-12-20T13:10:51+01:00https://qdrant.tech/enterprise-solutions/2024-08-20T14:08:09-04:00https://qdrant.tech/documentation/frameworks/feast/2025-02-18T21:01:07+05:30https://qdrant.tech/documentation/frameworks/fifty-one/2024-08-15T08:50:37+05:30https://qdrant.tech/documentation/frameworks/genkit/2024-10-05T03:39:41+05:30https://qdrant.tech/documentation/data-management/fondant/2024-08-15T08:50:37+05:30https://qdrant.tech/documentation/embeddings/gemini/2024-11-28T08:54:13+05:30https://qdrant.tech/documentation/frameworks/haystack/2024-08-15T08:50:37+05:30https://qdrant.tech/documentation/frameworks/honeyhive/2025-05-09T04:07:10-03:00https://qdrant.tech/hospitality-and-travel/2025-05-21T18:13:48+02:00https://qdrant.tech/legal/impressum/2024-02-28T17:57:34+01:00https://qdrant.tech/documentation/data-management/fluvio/2024-09-15T21:31:35+05:30https://qdrant.tech/documentation/platforms/rivet/2024-08-15T08:50:37+05:30https://qdrant.tech/documentation/embeddings/jina-embeddings/2024-11-28T08:54:13+05:30https://qdrant.tech/about-us/about-us-get-started/2025-05-30T14:14:31+03:00https://qdrant.tech/documentation/platforms/keboola/2025-05-14T07:24:10-04:00https://qdrant.tech/documentation/platforms/kotaemon/2024-11-07T03:37:15+05:30https://qdrant.tech/documentation/frameworks/langchain/2024-08-29T19:19:43+05:30https://qdrant.tech/documentation/frameworks/langchain-go/2024-11-04T16:55:24+01:00https://qdrant.tech/documentation/frameworks/langchain4j/2024-08-15T08:50:37+05:30https://qdrant.tech/documentation/frameworks/langgraph/2024-11-20T19:27:09+05:30https://qdrant.tech/legal-tech/2025-04-24T18:13:38+02:00https://qdrant.tech/documentation/frameworks/llama-index/2024-08-15T08:50:37+05:30https://qdrant.tech/documentation/platforms/make/2024-08-15T08:50:37+05:30https://qdrant.tech/documentation/frameworks/mastra/2024-12-20T13:30:42+05:30https://qdrant.tech/documentation/frameworks/mem0/2024-10-05T13:55:10+05:30https://qdrant.tech/documentation/frameworks/nlweb/2025-05-19T21:26:59+05:30https://qdrant.tech/documentation/data-management/mindsdb/2024-08-15T08:50:37+05:30https://qdrant.tech/documentation/embeddings/mistral/2024-11-28T08:54:13+05:30https://qdrant.tech/documentation/embeddings/mixedbread/2024-11-28T08:54:13+05:30https://qdrant.tech/documentation/embeddings/mixpeek/2024-11-28T08:54:13+05:30https://qdrant.tech/documentation/platforms/n8n/2025-06-06T22:10:24+05:30https://qdrant.tech/documentation/frameworks/neo4j-graphrag/2024-11-07T02:58:58+05:30https://qdrant.tech/documentation/embeddings/nomic/2024-11-28T08:54:13+05:30https://qdrant.tech/documentation/embeddings/nvidia/2024-11-28T08:54:13+05:30https://qdrant.tech/documentation/embeddings/ollama/2024-11-28T08:54:13+05:30https://qdrant.tech/documentation/embeddings/openai/2024-11-28T08:54:13+05:30https://qdrant.tech/documentation/frameworks/openai-agents/2025-04-30T14:10:48+05:30https://qdrant.tech/about-us/about-us-engineering-culture/2025-05-30T14:14:31+03:00https://qdrant.tech/documentation/frameworks/pandas-ai/2025-02-18T21:01:07+05:30https://qdrant.tech/partners/2024-06-17T16:56:32+03:00https://qdrant.tech/documentation/frameworks/canopy/2024-08-15T08:50:37+05:30https://qdrant.tech/documentation/platforms/pipedream/2024-08-15T08:50:37+05:30https://qdrant.tech/documentation/platforms/portable/2024-08-15T08:50:37+05:30https://qdrant.tech/documentation/platforms/powerapps/2025-01-10T21:05:50+05:30https://qdrant.tech/documentation/embeddings/premai/2024-11-28T08:54:13+05:30https://qdrant.tech/pricing/2024-08-20T12:47:35-07:00https://qdrant.tech/legal/privacy-policy/2025-06-19T13:22:43+02:00https://qdrant.tech/private-cloud/2024-05-21T09:57:56+02:00https://qdrant.tech/documentation/platforms/privategpt/2024-08-15T08:50:37+05:30https://qdrant.tech/documentation/cloud-tools/pulumi/2024-11-19T18:01:59-08:00https://qdrant.tech/articles/2024-12-20T13:10:51+01:00https://qdrant.tech/blog/2024-05-21T09:57:56+02:00https://qdrant.tech/cloud/2024-08-20T11:44:59-07:00https://qdrant.tech/demo/2024-09-06T13:14:12+02:00https://qdrant.tech/qdrant-for-startups/2024-09-30T18:44:08+02:00https://qdrant.tech/hybrid-cloud/2024-05-21T10:11:09+02:00https://qdrant.tech/stars/2024-06-17T16:56:32+03:00https://qdrant.tech/qdrant-vector-database/2024-08-29T08:43:52-04:00https://qdrant.tech/rag/rag-evaluation-guide/2024-09-16T18:43:11+02:00https://qdrant.tech/rag/2024-08-20T11:45:42-07:00https://qdrant.tech/documentation/frameworks/ragbits/2024-11-07T08:29:10+05:30https://qdrant.tech/recommendations/2024-08-20T12:49:28-07:00https://qdrant.tech/documentation/data-management/redpanda/2024-08-15T22:23:17+05:30https://qdrant.tech/documentation/frameworks/rig-rs/2024-11-07T08:04:53+05:30https://qdrant.tech/documentation/platforms/mulesoft/2025-01-10T21:16:11+05:30https://qdrant.tech/documentation/frameworks/semantic-router/2024-08-15T08:50:37+05:30https://qdrant.tech/documentation/frameworks/smolagents/2025-01-04T22:43:37+05:30https://qdrant.tech/documentation/embeddings/snowflake/2024-11-28T08:54:13+05:30https://qdrant.tech/documentation/frameworks/solon/2025-04-15T18:20:05+05:30https://qdrant.tech/documentation/frameworks/spring-ai/2024-08-29T19:19:43+05:30https://qdrant.tech/documentation/frameworks/dspy/2025-06-16T17:32:35+03:00https://qdrant.tech/subscribe-confirmation/2023-12-26T11:53:00+00:00https://qdrant.tech/subscribe/2025-02-04T13:55:26+01:00https://qdrant.tech/documentation/frameworks/superduper/2024-11-27T17:46:12+05:30https://qdrant.tech/documentation/frameworks/sycamore/2024-10-17T11:40:28+05:30https://qdrant.tech/legal/terms\_and\_conditions/2021-12-10T10:29:52+01:00https://qdrant.tech/documentation/cloud-tools/terraform/2024-11-19T18:01:59-08:00https://qdrant.tech/documentation/frameworks/testcontainers/2025-04-24T18:47:10+10:00https://qdrant.tech/documentation/platforms/tooljet/2025-03-06T14:58:05+05:30https://qdrant.tech/documentation/embeddings/twelvelabs/2025-01-07T21:51:22+05:30https://qdrant.tech/documentation/frameworks/txtai/2024-08-15T08:50:37+05:30https://qdrant.tech/documentation/data-management/unstructured/2025-02-18T21:01:07+05:30https://qdrant.tech/documentation/embeddings/upstage/2024-11-28T08:54:13+05:30https://qdrant.tech/documentation/frameworks/vanna-ai/2024-08-15T08:50:37+05:30https://qdrant.tech/documentation/frameworks/mirror-security/2025-02-21T09:20:59+05:30https://qdrant.tech/benchmarks/2023-02-16T18:40:22+04:00https://qdrant.tech/use-cases/2024-09-04T08:01:21-07:00https://qdrant.tech/documentation/platforms/vectorize/2025-02-05T06:14:34-05:00https://qdrant.tech/documentation/embeddings/voyage/2024-11-28T08:54:13+05:30https://qdrant.tech/documentation/cloud-intro/2025-05-02T16:53:21+02:00

<urlsetxmlns="http://www.sitemaps.org/schemas/sitemap/0.9"xmlns:xhtml="http://www.w3.org/1999/xhtml">

<url>

<loc>https://qdrant.tech/articles/distance-based-exploration/</loc>

<lastmod>2025-03-11T14:27:31+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/modern-sparse-neural-retrieval/</loc>

<lastmod>2025-05-15T19:37:07+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/cross-encoder-integration-gsoc/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/what-is-a-vector-database/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/what-is-vector-quantization/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/vector-search-resource-optimization/</loc>

<lastmod>2025-05-09T12:38:02+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/vector-search-filtering/</loc>

<lastmod>2025-01-06T10:45:10+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/immutable-data-structures/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/minicoil/</loc>

<lastmod>2025-05-13T18:20:11+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/search-feedback-loop/</loc>

<lastmod>2025-04-01T12:23:31+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/dedicated-vector-search/</loc>

<lastmod>2025-02-18T12:54:36-05:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/late-interaction-models/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/indexing-optimization/</loc>

<lastmod>2025-03-24T19:51:41+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/gridstore-key-value-storage/</loc>

<lastmod>2025-02-05T09:42:23-05:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/agentic-rag/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/hybrid-search/</loc>

<lastmod>2025-01-03T10:53:26+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/what-is-rag-in-ai/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/bm42/</loc>

<lastmod>2025-04-10T12:02:16+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/qdrant-1.8.x/</loc>

<lastmod>2024-07-07T18:34:56-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/rapid-rag-optimization-with-qdrant-and-quotient/</loc>

<lastmod>2025-05-15T19:33:44+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/rag-is-dead/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/binary-quantization-openai/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/multitenancy/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/data-privacy/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/discovery-search/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/what-are-embeddings/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/sparse-vectors/</loc>

<lastmod>2025-03-04T22:08:36+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/qdrant-1.7.x/</loc>

<lastmod>2024-10-05T03:39:41+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/new-recommendation-api/</loc>

<lastmod>2024-03-07T20:31:05+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/dedicated-service/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/fastembed/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/geo-polygon-filter-gsoc/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/binary-quantization/</loc>

<lastmod>2025-04-10T09:21:38-03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/food-discovery-demo/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/web-ui-gsoc/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/dimension-reduction-qsoc/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/search-as-you-type/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/vector-similarity-beyond-search/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/serverless/</loc>

<lastmod>2025-02-18T21:01:07+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/database-tutorials/bulk-upload/</loc>

<lastmod>2025-03-25T21:43:45-03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/benchmarks/benchmarks-intro/</loc>

<lastmod>2024-06-27T12:40:08+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/faq/qdrant-fundamentals/</loc>

<lastmod>2025-05-02T10:37:48+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/search-precision/reranking-semantic-search/</loc>

<lastmod>2025-05-21T15:27:35+08:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/cloud-rbac/role-management/</loc>

<lastmod>2025-05-02T16:53:21+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/beginner-tutorials/search-beginners/</loc>

<lastmod>2025-04-25T19:32:48+03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-setup/</loc>

<lastmod>2025-03-10T22:19:22+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/private-cloud/private-cloud-setup/</loc>

<lastmod>2025-06-03T09:48:32+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/overview/vector-search/</loc>

<lastmod>2024-10-05T03:39:41+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/qdrant-1.3.x/</loc>

<lastmod>2024-03-07T20:31:05+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/benchmarks/single-node-speed-benchmark/</loc>

<lastmod>2024-06-17T22:01:23+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/benchmarks/single-node-speed-benchmark-2022/</loc>

<lastmod>2024-01-11T19:41:06+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/search-precision/automate-filtering-with-llms/</loc>

<lastmod>2025-05-27T18:00:51+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/beginner-tutorials/neural-search/</loc>

<lastmod>2024-11-18T15:26:15-08:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/private-cloud/configuration/</loc>

<lastmod>2025-03-21T16:37:49+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/database-tutorials/create-snapshot/</loc>

<lastmod>2025-06-12T09:02:54+03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-cluster-creation/</loc>

<lastmod>2025-06-16T17:51:31+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/data-ingestion-beginners/</loc>

<lastmod>2025-05-15T20:16:43+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/faq/database-optimization/</loc>

<lastmod>2024-10-05T03:39:41+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/advanced-tutorials/using-multivector-representations/</loc>

<lastmod>2025-06-10T11:40:10+03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/database-tutorials/large-scale-search/</loc>

<lastmod>2025-03-24T14:27:15-03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/fastembed/fastembed-quickstart/</loc>

<lastmod>2024-08-06T15:42:27-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/advanced-tutorials/reranking-hybrid-search/</loc>

<lastmod>2025-06-05T14:05:27+03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/advanced-tutorials/code-search/</loc>

<lastmod>2025-05-15T19:33:03+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/agentic-rag-crewai-zoom/</loc>

<lastmod>2025-04-09T12:55:16+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/cloud-rbac/user-management/</loc>

<lastmod>2025-05-02T18:40:38+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/io\_uring/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/benchmarks/filtered-search-intro/</loc>

<lastmod>2024-01-11T19:41:06+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/agentic-rag-langgraph/</loc>

<lastmod>2025-05-15T19:37:07+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/advanced-tutorials/collaborative-filtering/</loc>

<lastmod>2024-11-18T15:26:15-08:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/hybrid-cloud/operator-configuration/</loc>

<lastmod>2024-12-23T12:11:13+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/fastembed/fastembed-semantic-search/</loc>

<lastmod>2025-04-26T13:30:39+03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/database-tutorials/huggingface-datasets/</loc>

<lastmod>2024-11-18T15:26:15-08:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/private-cloud/qdrant-cluster-management/</loc>

<lastmod>2025-06-16T17:51:31+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/cloud-rbac/permission-reference/</loc>

<lastmod>2025-06-13T08:39:21+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/beginner-tutorials/hybrid-search-fastembed/</loc>

<lastmod>2025-04-26T18:10:19+03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/overview/</loc>

<lastmod>2025-04-26T22:59:20-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/product-quantization/</loc>

<lastmod>2025-02-04T13:55:26+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/benchmarks/filtered-search-benchmark/</loc>

<lastmod>2024-01-11T19:41:06+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/agentic-rag-camelai-discord/</loc>

<lastmod>2025-04-09T12:55:16+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/private-cloud/backups/</loc>

<lastmod>2024-09-05T15:17:16+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/database-tutorials/async-api/</loc>

<lastmod>2025-02-18T21:01:07+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/cloud-quickstart/</loc>

<lastmod>2025-05-29T08:51:37-04:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/quickstart/</loc>

<lastmod>2025-01-20T10:08:10+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/private-cloud/logging-monitoring/</loc>

<lastmod>2025-02-11T18:21:40+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/beginner-tutorials/retrieval-quality/</loc>

<lastmod>2024-11-18T15:26:15-08:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/hybrid-cloud/networking-logging-monitoring/</loc>

<lastmod>2025-02-11T18:21:40+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/advanced-tutorials/pdf-retrieval-at-scale/</loc>

<lastmod>2025-01-28T15:29:08+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/scalar-quantization/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/interfaces/</loc>

<lastmod>2024-11-21T17:41:45+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/private-cloud/api-reference/</loc>

<lastmod>2025-06-03T09:48:32+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/private-cloud/changelog/</loc>

<lastmod>2025-06-03T09:48:32+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/</loc>

<lastmod>2024-11-18T15:42:18-08:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/</loc>

<lastmod>2025-04-30T22:48:05+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/guides/installation/</loc>

<lastmod>2025-05-02T10:37:48+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/multimodal-search/</loc>

<lastmod>2025-04-09T12:55:16+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/fastembed/fastembed-splade/</loc>

<lastmod>2025-04-25T19:38:33+03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/seed-round/</loc>

<lastmod>2024-03-07T20:31:05+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/langchain-integration/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/rag-deepseek/</loc>

<lastmod>2025-04-26T13:02:13+03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/web-ui/</loc>

<lastmod>2024-11-20T23:14:39+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/fastembed/fastembed-colbert/</loc>

<lastmod>2025-06-19T16:21:03+04:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/chatgpt-plugin/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/memory-consumption/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/qa-with-cohere-and-qdrant/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/qdrant-1.2.x/</loc>

<lastmod>2024-03-07T20:31:05+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/dataset-quality/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/concepts/</loc>

<lastmod>2024-11-14T18:59:28+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/fastembed/fastembed-rerankers/</loc>

<lastmod>2025-04-26T13:20:52+03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/faq-question-answering/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/why-rust/</loc>

<lastmod>2024-09-05T13:07:07-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/embedding-recycler/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/cars-recognition/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/guides/administration/</loc>

<lastmod>2025-05-19T15:01:52+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/benchmarks/benchmark-faq/</loc>

<lastmod>2024-01-11T19:41:06+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/guides/running-with-gpu/</loc>

<lastmod>2025-03-20T15:19:07+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/vector-search-manuals/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/guides/capacity-planning/</loc>

<lastmod>2024-10-05T03:39:41+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/fastembed/</loc>

<lastmod>2025-05-27T18:00:51+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/guides/optimize/</loc>

<lastmod>2025-04-07T00:40:39+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/cloud-getting-started/</loc>

<lastmod>2025-05-02T16:53:21+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/guides/multiple-partitions/</loc>

<lastmod>2025-04-07T00:40:39+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/qdrant-mcp-server/</loc>

<lastmod>2025-05-27T18:00:51+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/cloud-account-setup/</loc>

<lastmod>2025-05-02T18:40:38+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/cloud-rbac/</loc>

<lastmod>2025-05-02T16:53:21+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/cloud/</loc>

<lastmod>2025-05-02T16:53:21+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/hybrid-cloud/</loc>

<lastmod>2025-05-02T16:53:21+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/beginner-tutorials/</loc>

<lastmod>2024-11-18T15:26:15-08:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/advanced-tutorials/</loc>

<lastmod>2025-02-07T18:51:10-05:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/private-cloud/</loc>

<lastmod>2025-05-02T16:53:21+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/cloud-pricing-payments/</loc>

<lastmod>2025-05-02T16:53:21+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/examples/qdrant-dspy-medicalbot/</loc>

<lastmod>2025-06-19T11:54:06+03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/data-management/</loc>

<lastmod>2025-05-31T21:49:18+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/examples/llama-index-multitenancy/</loc>

<lastmod>2024-04-11T13:13:14-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/database-tutorials/</loc>

<lastmod>2025-06-11T19:02:35+03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/embeddings/</loc>

<lastmod>2024-11-28T08:54:13+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/cloud-premium/</loc>

<lastmod>2025-05-02T16:53:21+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/metric-learning-tips/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/cloud/create-cluster/</loc>

<lastmod>2025-05-02T16:53:21+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/</loc>

<lastmod>2025-05-19T21:17:24+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/qdrant-internals/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/observability/</loc>

<lastmod>2024-11-14T18:59:28+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/platforms/</loc>

<lastmod>2025-05-14T07:24:10-04:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/examples/rag-chatbot-red-hat-openshift-haystack/</loc>

<lastmod>2024-05-15T18:01:28+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/examples/cohere-rag-connector/</loc>

<lastmod>2025-02-18T21:01:07+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/send-data/</loc>

<lastmod>2024-11-14T18:59:28+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/examples/</loc>

<lastmod>2025-06-19T11:54:06+03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/examples/rag-customer-support-cohere-airbyte-aws/</loc>

<lastmod>2025-02-18T21:01:07+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/</loc>

<lastmod>2024-04-15T17:41:39-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/cloud-api/</loc>

<lastmod>2025-06-06T09:56:35+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/cloud-tools/</loc>

<lastmod>2024-11-19T17:56:47-08:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/examples/rag-contract-management-stackit-aleph-alpha/</loc>

<lastmod>2025-02-18T21:01:07+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/datasets/</loc>

<lastmod>2024-11-14T18:59:28+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/detecting-coffee-anomalies/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/triplet-loss/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/cloud/authentication/</loc>

<lastmod>2025-05-02T16:53:21+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/concepts/collections/</loc>

<lastmod>2025-04-07T00:40:39+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/data-exploration/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/examples/natural-language-search-oracle-cloud-infrastructure-cohere-langchain/</loc>

<lastmod>2024-04-15T19:50:07-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/examples/rag-chatbot-vultr-dspy-ollama/</loc>

<lastmod>2025-05-15T19:37:07+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/examples/recommendation-system-ovhcloud/</loc>

<lastmod>2024-08-23T22:48:27+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/examples/rag-chatbot-scaleway/</loc>

<lastmod>2025-02-18T21:01:07+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/cloud/cluster-access/</loc>

<lastmod>2025-05-02T16:53:21+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/support/</loc>

<lastmod>2025-04-08T10:25:18+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/send-data/databricks/</loc>

<lastmod>2024-07-29T21:03:45+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/send-data/qdrant-airflow-astronomer/</loc>

<lastmod>2024-08-13T13:38:38+03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/machine-learning/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/concepts/points/</loc>

<lastmod>2025-04-07T00:40:39+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/concepts/vectors/</loc>

<lastmod>2025-04-07T00:40:39+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/concepts/payload/</loc>

<lastmod>2025-04-07T00:40:39+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/send-data/data-streaming-kafka-qdrant/</loc>

<lastmod>2024-07-22T17:09:17-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/neural-search-tutorial/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/rag-and-genai/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/cloud/cluster-scaling/</loc>

<lastmod>2025-05-02T16:53:21+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/concepts/search/</loc>

<lastmod>2025-04-07T00:40:39+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/concepts/explore/</loc>

<lastmod>2025-06-12T10:45:50-04:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/cloud/cluster-monitoring/</loc>

<lastmod>2025-05-02T16:53:21+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/cloud/cluster-upgrades/</loc>

<lastmod>2025-05-02T16:53:21+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/concepts/hybrid-queries/</loc>

<lastmod>2025-04-23T11:15:58+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/filtrable-hnsw/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/concepts/filtering/</loc>

<lastmod>2025-06-09T18:30:19+03:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/practicle-examples/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/cloud/backups/</loc>

<lastmod>2025-05-02T16:53:21+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/qdrant-0-11-release/</loc>

<lastmod>2022-12-06T13:12:27+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/qdrant-0-10-release/</loc>

<lastmod>2024-05-15T18:01:28+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/concepts/optimizer/</loc>

<lastmod>2024-11-27T16:59:34+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/concepts/storage/</loc>

<lastmod>2025-04-07T00:40:39+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/concepts/indexing/</loc>

<lastmod>2025-04-07T00:40:39+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/guides/distributed\_deployment/</loc>

<lastmod>2025-02-03T17:33:39+06:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/concepts/snapshots/</loc>

<lastmod>2025-06-12T09:02:54+03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/guides/quantization/</loc>

<lastmod>2025-04-07T00:40:39+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/guides/monitoring/</loc>

<lastmod>2025-02-11T18:21:40+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/guides/configuration/</loc>

<lastmod>2025-02-04T11:00:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/guides/security/</loc>

<lastmod>2025-01-20T16:32:23+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/guides/usage-statistics/</loc>

<lastmod>2024-12-03T17:03:30+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/guides/common-errors/</loc>

<lastmod>2025-05-27T12:04:07+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/database-tutorials/migration/</loc>

<lastmod>2025-06-11T18:57:35+03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/hybrid-cloud-vultr/</loc>

<lastmod>2024-05-21T10:11:09+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/quantum-quantization/</loc>

<lastmod>2023-07-13T01:45:36+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/hybrid-cloud-stackit/</loc>

<lastmod>2024-05-21T10:11:09+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/hybrid-cloud-scaleway/</loc>

<lastmod>2024-05-21T10:11:09+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/hybrid-cloud-red-hat-openshift/</loc>

<lastmod>2024-05-21T10:11:09+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/hybrid-cloud-ovhcloud/</loc>

<lastmod>2024-05-21T10:11:09+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/hybrid-cloud-llamaindex/</loc>

<lastmod>2024-05-21T10:11:09+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/hybrid-cloud-langchain/</loc>

<lastmod>2024-05-21T10:11:09+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/hybrid-cloud-jinaai/</loc>

<lastmod>2024-05-21T10:11:09+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/hybrid-cloud-haystack/</loc>

<lastmod>2024-09-24T14:30:20-04:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/hybrid-cloud-digitalocean/</loc>

<lastmod>2024-05-21T10:11:09+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/hybrid-cloud-aleph-alpha/</loc>

<lastmod>2025-02-04T13:55:26+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/hybrid-cloud-airbyte/</loc>

<lastmod>2025-02-04T13:55:26+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/observability/openllmetry/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/observability/openlit/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-lettria-v2/</loc>

<lastmod>2025-06-16T22:38:02-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/</loc>

<lastmod>2025-06-19T16:21:03+04:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/beta-database-migration-tool/</loc>

<lastmod>2025-06-18T11:55:05-04:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-lawme/</loc>

<lastmod>2025-06-11T09:42:37-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-convosearch/</loc>

<lastmod>2025-06-10T09:54:12-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/legal-tech-builders-guide/</loc>

<lastmod>2025-06-13T15:44:13-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/soc-2-type-ii-hipaa/</loc>

<lastmod>2025-06-17T16:48:22-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/n8n-node/</loc>

<lastmod>2025-06-09T15:38:39+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/datatalks-course/</loc>

<lastmod>2025-06-05T09:19:05-04:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-qovery/</loc>

<lastmod>2025-05-27T11:19:41-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-tripadvisor/</loc>

<lastmod>2025-05-13T23:15:13-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-aracor/</loc>

<lastmod>2025-05-13T11:23:13-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-garden-intel/</loc>

<lastmod>2025-05-09T11:56:26-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/product-ui-changes/</loc>

<lastmod>2025-05-08T09:28:12-04:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-pariti/</loc>

<lastmod>2025-05-01T10:05:43-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/vector-search-production/</loc>

<lastmod>2025-04-30T17:47:55+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-dust-v2/</loc>

<lastmod>2025-05-08T11:45:46-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-sayone/</loc>

<lastmod>2025-04-29T09:15:10-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/superlinked-multimodal-search/</loc>

<lastmod>2025-04-24T14:10:50+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/qdrant-1.14.x/</loc>

<lastmod>2025-05-02T15:26:42-03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-pathwork/</loc>

<lastmod>2025-05-16T09:10:33-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-lyzr/</loc>

<lastmod>2025-05-16T09:10:33-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-mixpeek/</loc>

<lastmod>2025-05-16T09:10:33-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/qdrant-n8n-beyond-simple-similarity-search/</loc>

<lastmod>2025-04-08T11:38:52+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/satellite-vector-broadcasting/</loc>

<lastmod>2025-04-01T08:09:34+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-hubspot/</loc>

<lastmod>2025-05-16T09:10:33-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/webinar-vibe-coding-rag/</loc>

<lastmod>2025-03-21T16:36:29+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-deutsche-telekom/</loc>

<lastmod>2025-04-03T08:09:56-04:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/enterprise-vector-search/</loc>

<lastmod>2025-04-07T15:17:30-04:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/metadata-deasy-labs/</loc>

<lastmod>2025-02-24T15:04:44-03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/webinar-crewai-qdrant-obsidian/</loc>

<lastmod>2025-01-24T16:10:16+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/qdrant-1.13.x/</loc>

<lastmod>2025-01-24T04:19:54-05:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/static-embeddings/</loc>

<lastmod>2025-01-17T14:53:25+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-voiceflow/</loc>

<lastmod>2024-12-10T10:26:56-08:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/facial-recognition/</loc>

<lastmod>2024-12-03T20:56:40-08:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/colpali-qdrant-optimization/</loc>

<lastmod>2024-11-30T18:57:48-03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/rag-evaluation-guide/</loc>

<lastmod>2025-02-18T21:01:07+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-qatech/</loc>

<lastmod>2024-11-21T16:42:35-08:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/qdrant-colpali/</loc>

<lastmod>2024-11-06T17:18:48-08:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-sprinklr/</loc>

<lastmod>2024-10-18T09:03:19-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/qdrant-1.12.x/</loc>

<lastmod>2024-10-08T19:49:58-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/qdrant-deeplearning-ai-course/</loc>

<lastmod>2024-10-07T12:25:14-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/qdrant-for-startups-launch/</loc>

<lastmod>2024-10-02T19:07:16+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-shakudo/</loc>

<lastmod>2025-03-13T17:47:05+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/qdrant-relari/</loc>

<lastmod>2024-09-17T15:53:48-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-nyris/</loc>

<lastmod>2024-09-23T14:05:33-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-kern/</loc>

<lastmod>2024-09-23T14:05:33-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/qdrant-1.11.x/</loc>

<lastmod>2024-08-16T00:01:23+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-kairoswealth/</loc>

<lastmod>2024-09-11T14:59:00-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/qdrant-1.10.x/</loc>

<lastmod>2024-07-16T22:00:30+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/community-highlights-1/</loc>

<lastmod>2024-06-21T02:34:01-03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/cve-2024-3829-response/</loc>

<lastmod>2024-06-10T12:42:49-04:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/qdrant-soc2-type2-audit/</loc>

<lastmod>2024-08-29T19:19:43+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/qdrant-stars-announcement/</loc>

<lastmod>2024-10-05T03:39:41+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/qdrant-cpu-intel-benchmark/</loc>

<lastmod>2024-10-08T12:41:46-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/qsoc24-interns-announcement/</loc>

<lastmod>2024-05-08T18:04:46-03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/semantic-cache-ai-data-retrieval/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/are-you-vendor-locked/</loc>

<lastmod>2024-05-21T10:11:09+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-visua/</loc>

<lastmod>2024-05-01T17:59:13-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/qdrant-1.9.x/</loc>

<lastmod>2024-05-21T10:11:09+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/hybrid-cloud-launch-partners/</loc>

<lastmod>2024-05-21T10:11:09+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/hybrid-cloud/</loc>

<lastmod>2024-05-21T10:11:09+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/rag-advancements-challenges/</loc>

<lastmod>2024-04-12T14:45:02+00:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/building-search-rag-open-api/</loc>

<lastmod>2024-04-12T14:23:42+00:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/gen-ai-and-vector-search/</loc>

<lastmod>2024-07-07T19:32:50-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/teaching-vector-db-at-scale/</loc>

<lastmod>2024-04-09T11:06:17+00:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/meow-with-cheshire-cat/</loc>

<lastmod>2024-04-09T11:05:51+00:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/cve-2024-2221-response/</loc>

<lastmod>2024-08-15T17:31:04+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/fastllm-announcement/</loc>

<lastmod>2024-04-01T04:13:26-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/virtualbrain-best-rag/</loc>

<lastmod>2024-09-20T10:12:14-04:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/youtube-without-paying-cent/</loc>

<lastmod>2024-03-27T12:44:32+00:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/azure-marketplace/</loc>

<lastmod>2024-10-05T03:39:41+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/real-time-news-distillation-rag/</loc>

<lastmod>2024-03-25T08:49:27+00:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/insight-generation-platform/</loc>

<lastmod>2024-03-25T08:51:56+00:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/llm-as-a-judge/</loc>

<lastmod>2024-03-19T15:05:24+00:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/vector-search-vector-recommendation/</loc>

<lastmod>2024-03-19T14:22:15+00:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/using-qdrant-and-langchain/</loc>

<lastmod>2024-05-15T18:01:28+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/iris-agent-qdrant/</loc>

<lastmod>2024-03-06T09:17:19-08:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-dailymotion/</loc>

<lastmod>2024-03-07T20:31:05+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/comparing-qdrant-vs-pinecone-vector-databases/</loc>

<lastmod>2025-02-04T13:55:26+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/what-is-vector-similarity/</loc>

<lastmod>2024-09-05T13:07:07-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/dspy-vs-langchain/</loc>

<lastmod>2025-05-15T19:37:07+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/qdrant-summer-of-code-24/</loc>

<lastmod>2024-03-14T18:24:32+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/dust-and-qdrant/</loc>

<lastmod>2024-09-20T10:19:38-04:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/bitter-lesson-generative-language-model/</loc>

<lastmod>2024-01-29T16:31:02+00:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/indexify-content-extraction-engine/</loc>

<lastmod>2024-03-07T18:59:29+00:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/qdrant-x-dust-vector-search/</loc>

<lastmod>2024-07-07T19:40:44-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/series-a-funding-round/</loc>

<lastmod>2024-10-08T12:41:46-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/qdrant-cloud-on-microsoft-azure/</loc>

<lastmod>2024-03-07T20:31:05+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/qdrant-benchmarks-2024/</loc>

<lastmod>2024-03-07T20:31:05+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/navigating-challenges-innovations/</loc>

<lastmod>2024-05-21T09:57:56+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/open-source-vector-search-engine-vector-database/</loc>

<lastmod>2024-07-07T19:36:05-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/vector-image-search-rag/</loc>

<lastmod>2024-01-25T17:51:08+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/semantic-search-vector-database/</loc>

<lastmod>2024-07-07T19:46:08-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/llm-complex-search-copilot/</loc>

<lastmod>2024-01-10T11:42:02+00:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/entity-matching-qdrant/</loc>

<lastmod>2024-01-10T11:37:51+00:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/fast-embed-models/</loc>

<lastmod>2024-01-22T10:15:56-08:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/human-language-ai-models/</loc>

<lastmod>2024-01-10T10:31:15+00:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/binary-quantization/</loc>

<lastmod>2024-01-10T10:26:06+00:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/qdrant-unstructured/</loc>

<lastmod>2024-03-07T20:31:05+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/qdrant-n8n/</loc>

<lastmod>2024-03-07T20:31:05+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/vector-search-and-applications-record/</loc>

<lastmod>2024-09-06T13:14:12+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/cohere-embedding-v3/</loc>

<lastmod>2024-09-06T13:14:12+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-pienso/</loc>

<lastmod>2024-04-10T17:59:48-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/case-study-bloop/</loc>

<lastmod>2024-07-18T19:11:22-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/qdrant-introduces-full-text-filters-and-indexes/</loc>

<lastmod>2024-09-18T15:57:29-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/storing-multiple-vectors-per-object-in-qdrant/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/batch-vector-search-with-qdrant/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/qdrant-supports-arm-architecture/</loc>

<lastmod>2024-01-16T22:02:52+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/about-us/</loc>

<lastmod>2024-05-21T09:57:56+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/data-analysis-anomaly-detection/</loc>

<lastmod>2024-08-29T10:01:03-04:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/advanced-search/</loc>

<lastmod>2024-08-21T16:31:41-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/ai-agents/</loc>

<lastmod>2025-02-12T08:47:39-06:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/e-commerce/</loc>

<lastmod>2025-05-22T20:23:57+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/data-management/airbyte/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/embeddings/aleph-alpha/</loc>

<lastmod>2024-11-28T08:54:13+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/get\_anonymous\_id/</loc>

<lastmod>2025-03-05T11:26:52+00:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/data-management/airflow/</loc>

<lastmod>2025-02-18T21:01:07+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/data-management/nifi/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/data-management/spark/</loc>

<lastmod>2025-03-06T10:23:24+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/platforms/apify/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/autogen/</loc>

<lastmod>2024-11-20T11:50:06+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/embeddings/bedrock/</loc>

<lastmod>2024-11-28T08:54:13+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/lakechain/</loc>

<lastmod>2024-10-17T11:42:14+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/about-us/about-us-resources/</loc>

<lastmod>2025-05-30T14:14:31+03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/brand-resources/</loc>

<lastmod>2024-06-17T16:56:32+03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/platforms/bubble/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/security/bug-bounty-program/</loc>

<lastmod>2025-03-28T09:40:53+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/build/</loc>

<lastmod>2024-11-18T14:53:02-08:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/platforms/buildship/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/camel/</loc>

<lastmod>2024-12-20T13:31:09+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/cheshire-cat/</loc>

<lastmod>2025-01-24T11:47:11+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/data-management/cocoindex/</loc>

<lastmod>2025-04-20T23:11:21-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/data-management/cognee/</loc>

<lastmod>2025-05-31T22:06:39+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/embeddings/cohere/</loc>

<lastmod>2025-02-19T10:27:39+03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/community/</loc>

<lastmod>2025-01-07T11:56:39-06:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/data-management/confluent/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/contact-us/</loc>

<lastmod>2025-03-13T17:47:05+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/legal/credits/</loc>

<lastmod>2022-04-25T15:19:19+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/crewai/</loc>

<lastmod>2025-02-27T09:21:41+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/customers/</loc>

<lastmod>2024-06-17T16:56:32+03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/dagster/</loc>

<lastmod>2025-04-15T18:20:05+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/observability/datadog/</loc>

<lastmod>2024-10-31T05:56:39+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/deepeval/</loc>

<lastmod>2025-04-24T16:09:40+08:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/data-management/dlt/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/docarray/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/platforms/docsgpt/</loc>

<lastmod>2025-02-18T21:01:07+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/dsrag/</loc>

<lastmod>2024-11-27T17:59:33+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/dynamiq/</loc>

<lastmod>2025-03-24T10:22:45+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/ecosystem/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/enterprise-solutions/</loc>

<lastmod>2024-08-20T14:08:09-04:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/feast/</loc>

<lastmod>2025-02-18T21:01:07+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/fifty-one/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/genkit/</loc>

<lastmod>2024-10-05T03:39:41+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/data-management/fondant/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/embeddings/gemini/</loc>

<lastmod>2024-11-28T08:54:13+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/haystack/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/honeyhive/</loc>

<lastmod>2025-05-09T04:07:10-03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/hospitality-and-travel/</loc>

<lastmod>2025-05-21T18:13:48+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/legal/impressum/</loc>

<lastmod>2024-02-28T17:57:34+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/data-management/fluvio/</loc>

<lastmod>2024-09-15T21:31:35+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/platforms/rivet/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/embeddings/jina-embeddings/</loc>

<lastmod>2024-11-28T08:54:13+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/about-us/about-us-get-started/</loc>

<lastmod>2025-05-30T14:14:31+03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/platforms/keboola/</loc>

<lastmod>2025-05-14T07:24:10-04:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/platforms/kotaemon/</loc>

<lastmod>2024-11-07T03:37:15+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/langchain/</loc>

<lastmod>2024-08-29T19:19:43+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/langchain-go/</loc>

<lastmod>2024-11-04T16:55:24+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/langchain4j/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/langgraph/</loc>

<lastmod>2024-11-20T19:27:09+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/legal-tech/</loc>

<lastmod>2025-04-24T18:13:38+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/llama-index/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/platforms/make/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/mastra/</loc>

<lastmod>2024-12-20T13:30:42+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/mem0/</loc>

<lastmod>2024-10-05T13:55:10+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/nlweb/</loc>

<lastmod>2025-05-19T21:26:59+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/data-management/mindsdb/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/embeddings/mistral/</loc>

<lastmod>2024-11-28T08:54:13+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/embeddings/mixedbread/</loc>

<lastmod>2024-11-28T08:54:13+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/embeddings/mixpeek/</loc>

<lastmod>2024-11-28T08:54:13+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/platforms/n8n/</loc>

<lastmod>2025-06-06T22:10:24+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/neo4j-graphrag/</loc>

<lastmod>2024-11-07T02:58:58+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/embeddings/nomic/</loc>

<lastmod>2024-11-28T08:54:13+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/embeddings/nvidia/</loc>

<lastmod>2024-11-28T08:54:13+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/embeddings/ollama/</loc>

<lastmod>2024-11-28T08:54:13+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/embeddings/openai/</loc>

<lastmod>2024-11-28T08:54:13+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/openai-agents/</loc>

<lastmod>2025-04-30T14:10:48+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/about-us/about-us-engineering-culture/</loc>

<lastmod>2025-05-30T14:14:31+03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/pandas-ai/</loc>

<lastmod>2025-02-18T21:01:07+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/partners/</loc>

<lastmod>2024-06-17T16:56:32+03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/canopy/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/platforms/pipedream/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/platforms/portable/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/platforms/powerapps/</loc>

<lastmod>2025-01-10T21:05:50+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/embeddings/premai/</loc>

<lastmod>2024-11-28T08:54:13+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/pricing/</loc>

<lastmod>2024-08-20T12:47:35-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/legal/privacy-policy/</loc>

<lastmod>2025-06-19T13:22:43+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/private-cloud/</loc>

<lastmod>2024-05-21T09:57:56+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/platforms/privategpt/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/cloud-tools/pulumi/</loc>

<lastmod>2024-11-19T18:01:59-08:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/articles/</loc>

<lastmod>2024-12-20T13:10:51+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/blog/</loc>

<lastmod>2024-05-21T09:57:56+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/cloud/</loc>

<lastmod>2024-08-20T11:44:59-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/demo/</loc>

<lastmod>2024-09-06T13:14:12+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/qdrant-for-startups/</loc>

<lastmod>2024-09-30T18:44:08+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/hybrid-cloud/</loc>

<lastmod>2024-05-21T10:11:09+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/stars/</loc>

<lastmod>2024-06-17T16:56:32+03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/qdrant-vector-database/</loc>

<lastmod>2024-08-29T08:43:52-04:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/rag/rag-evaluation-guide/</loc>

<lastmod>2024-09-16T18:43:11+02:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/rag/</loc>

<lastmod>2024-08-20T11:45:42-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/ragbits/</loc>

<lastmod>2024-11-07T08:29:10+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/recommendations/</loc>

<lastmod>2024-08-20T12:49:28-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/data-management/redpanda/</loc>

<lastmod>2024-08-15T22:23:17+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/rig-rs/</loc>

<lastmod>2024-11-07T08:04:53+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/platforms/mulesoft/</loc>

<lastmod>2025-01-10T21:16:11+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/semantic-router/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/smolagents/</loc>

<lastmod>2025-01-04T22:43:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/embeddings/snowflake/</loc>

<lastmod>2024-11-28T08:54:13+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/solon/</loc>

<lastmod>2025-04-15T18:20:05+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/spring-ai/</loc>

<lastmod>2024-08-29T19:19:43+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/dspy/</loc>

<lastmod>2025-06-16T17:32:35+03:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/subscribe-confirmation/</loc>

<lastmod>2023-12-26T11:53:00+00:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/subscribe/</loc>

<lastmod>2025-02-04T13:55:26+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/superduper/</loc>

<lastmod>2024-11-27T17:46:12+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/sycamore/</loc>

<lastmod>2024-10-17T11:40:28+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/legal/terms\_and\_conditions/</loc>

<lastmod>2021-12-10T10:29:52+01:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/cloud-tools/terraform/</loc>

<lastmod>2024-11-19T18:01:59-08:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/testcontainers/</loc>

<lastmod>2025-04-24T18:47:10+10:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/platforms/tooljet/</loc>

<lastmod>2025-03-06T14:58:05+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/embeddings/twelvelabs/</loc>

<lastmod>2025-01-07T21:51:22+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/txtai/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/data-management/unstructured/</loc>

<lastmod>2025-02-18T21:01:07+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/embeddings/upstage/</loc>

<lastmod>2024-11-28T08:54:13+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/vanna-ai/</loc>

<lastmod>2024-08-15T08:50:37+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/frameworks/mirror-security/</loc>

<lastmod>2025-02-21T09:20:59+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/benchmarks/</loc>

<lastmod>2023-02-16T18:40:22+04:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/use-cases/</loc>

<lastmod>2024-09-04T08:01:21-07:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/platforms/vectorize/</loc>

<lastmod>2025-02-05T06:14:34-05:00</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/embeddings/voyage/</loc>

<lastmod>2024-11-28T08:54:13+05:30</lastmod>

...

</url>

<url>

<loc>https://qdrant.tech/documentation/cloud-intro/</loc>

<lastmod>2025-05-02T16:53:21+02:00</lastmod>

...

</url>

...

</urlset>

<|page-32-lllmstxt|>
## cloud-tools
- [Documentation](https://qdrant.tech/documentation/)
- Infrastructure Tools

## [Anchor](https://qdrant.tech/documentation/cloud-tools/\#cloud-tools) Cloud Tools

| Integration | Description |
| --- | --- |
| [Pulumi](https://qdrant.tech/documentation/cloud-tools/pulumi/) | Infrastructure as code tool for creating, deploying, and managing cloud infrastructure |
| [Terraform](https://qdrant.tech/documentation/cloud-tools/terraform/) | infrastructure as code tool to define resources in human-readable configuration files. |

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud-tools/_index.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud-tools/_index.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-33-lllmstxt|>
## common-errors
- [Documentation](https://qdrant.tech/documentation/)
- [Guides](https://qdrant.tech/documentation/guides/)
- Troubleshooting