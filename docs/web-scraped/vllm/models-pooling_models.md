# Source: https://docs.vllm.ai/en/stable/models/pooling_models/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/models/pooling_models.md "Edit this page")

# Pooling Models[¶](#pooling-models "Permanent link")

vLLM also supports pooling models, such as embedding, classification, and reward models.

In vLLM, pooling models implement the [VllmModelForPooling](../../api/vllm/model_executor/models/#vllm.model_executor.models.VllmModelForPooling "            VllmModelForPooling") interface. These models use a [Pooler](../../api/vllm/model_executor/layers/pooler/#vllm.model_executor.layers.pooler.Pooler "            Pooler") to extract the final hidden states of the input before returning them.

Note

We currently support pooling models primarily for convenience. This is not guaranteed to provide any performance improvements over using Hugging Face Transformers or Sentence Transformers directly.

We plan to optimize pooling models in vLLM. Please comment on [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] Issue #21796](https://github.com/vllm-project/vllm/issues/21796) if you have any suggestions!

## Configuration[¶](#configuration "Permanent link")

### Model Runner[¶](#model-runner "Permanent link")

Run a model in pooling mode via the option `--runner pooling`.

Tip

There is no need to set this option in the vast majority of cases as vLLM can automatically detect the appropriate model runner via `--runner auto`.

### Model Conversion[¶](#model-conversion "Permanent link")

vLLM can adapt models for various pooling tasks via the option `--convert <type>`.

If `--runner pooling` has been set (manually or automatically) but the model does not implement the [VllmModelForPooling](../../api/vllm/model_executor/models/#vllm.model_executor.models.VllmModelForPooling "            VllmModelForPooling") interface, vLLM will attempt to automatically convert the model according to the architecture names shown in the table below.

  Architecture                                      `--convert`   Supported pooling tasks
  ------------------------------------------------- ------------- ---------------------------------------
  `*ForTextEncoding`, `*EmbeddingModel`, `*Model`   `embed`       `token_embed`, `embed`
  `*ForRewardModeling`, `*RewardModel`              `embed`       `token_embed`, `embed`
  `*For*Classification`, `*ClassificationModel`     `classify`    `token_classify`, `classify`, `score`

Tip

You can explicitly set `--convert <type>` to specify how to convert the model.

### Pooling Tasks[¶](#pooling-tasks "Permanent link")

Each pooling model in vLLM supports one or more of these tasks according to [Pooler.get_supported_tasks](../../api/vllm/model_executor/layers/pooler/#vllm.model_executor.layers.pooler.Pooler.get_supported_tasks "            get_supported_tasks

  
      abstractmethod
  "), enabling the corresponding APIs:

  Task               APIs
  ------------------ -------------------------------------------------------------------------------
  `embed`            `LLM.embed(...)`, `LLM.score(...)`\*, `LLM.encode(..., pooling_task="embed")`
  `classify`         `LLM.classify(...)`, `LLM.encode(..., pooling_task="classify")`
  `score`            `LLM.score(...)`
  `token_classify`   `LLM.reward(...)`, `LLM.encode(..., pooling_task="token_classify")`
  `token_embed`      `LLM.encode(..., pooling_task="token_embed")`
  `plugin`           `LLM.encode(..., pooling_task="plugin")`

\* The `LLM.score(...)` API falls back to `embed` task if the model does not support `score` task.

### Pooler Configuration[¶](#pooler-configuration "Permanent link")

#### Predefined models[¶](#predefined-models "Permanent link")

If the [Pooler](../../api/vllm/model_executor/layers/pooler/#vllm.model_executor.layers.pooler.Pooler "            Pooler") defined by the model accepts `pooler_config`, you can override some of its attributes via the `--pooler-config` option.

#### Converted models[¶](#converted-models "Permanent link")

If the model has been converted via `--convert` (see above), the pooler assigned to each task has the following attributes by default:

  Task         Pooling Type   Normalization   Softmax
  ------------ -------------- --------------- ---------
  `embed`      `LAST`         ✅︎              ❌
  `classify`   `LAST`         ❌              ✅︎

When loading [Sentence Transformers](https://huggingface.co/sentence-transformers) models, its Sentence Transformers configuration file (`modules.json`) takes priority over the model\'s defaults.

You can further customize this via the `--pooler-config` option, which takes priority over both the model\'s and Sentence Transformers\' defaults.

## Offline Inference[¶](#offline-inference "Permanent link")

The [LLM](../../api/vllm/#vllm.LLM "            LLM") class provides various methods for offline inference. See [configuration](../../api/#configuration) for a list of options when initializing the model.

### `LLM.embed`[¶](#llmembed "Permanent link") 

The [embed](../../api/vllm/#vllm.LLM.embed "            embed") method outputs an embedding vector for each prompt. It is primarily designed for embedding models.

    from vllm import LLM

    llm = LLM(model="intfloat/e5-small", runner="pooling")
    (output,) = llm.embed("Hello, my name is")

    embeds = output.outputs.embedding
    print(f"Embeddings:  (size=)")

A code example can be found here: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/offline_inference/basic/embed.py](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/basic/embed.py)

### `LLM.classify`[¶](#llmclassify "Permanent link") 

The [classify](../../api/vllm/#vllm.LLM.classify "            classify") method outputs a probability vector for each prompt. It is primarily designed for classification models.

    from vllm import LLM

    llm = LLM(model="jason9693/Qwen2.5-1.5B-apeach", runner="pooling")
    (output,) = llm.classify("Hello, my name is")

    probs = output.outputs.probs
    print(f"Class Probabilities:  (size=)")

A code example can be found here: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/offline_inference/basic/classify.py](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/basic/classify.py)

### `LLM.score`[¶](#llmscore "Permanent link") 

The [score](../../api/vllm/#vllm.LLM.score "            score") method outputs similarity scores between sentence pairs. It is designed for embedding models and cross-encoder models. Embedding models use cosine similarity, and [cross-encoder models](https://www.sbert.net/examples/applications/cross-encoder/README.html) serve as rerankers between candidate query-document pairs in RAG systems.

Note

vLLM can only perform the model inference component (e.g. embedding, reranking) of RAG. To handle RAG at a higher level, you should use integration frameworks such as [LangChain](https://github.com/langchain-ai/langchain).

    from vllm import LLM

    llm = LLM(model="BAAI/bge-reranker-v2-m3", runner="pooling")
    (output,) = llm.score(
        "What is the capital of France?",
        "The capital of Brazil is Brasilia.",
    )

    score = output.outputs.score
    print(f"Score: ")

A code example can be found here: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/offline_inference/basic/score.py](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/basic/score.py)

### `LLM.reward`[¶](#llmreward "Permanent link") 

The [reward](../../api/vllm/#vllm.LLM.reward "            reward") method is available to all reward models in vLLM.

    from vllm import LLM

    llm = LLM(model="internlm/internlm2-1_8b-reward", runner="pooling", trust_remote_code=True)
    (output,) = llm.reward("Hello, my name is")

    data = output.outputs.data
    print(f"Data: ")

A code example can be found here: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/offline_inference/basic/reward.py](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/basic/reward.py)

### `LLM.encode`[¶](#llmencode "Permanent link") 

The [encode](../../api/vllm/#vllm.LLM.encode "            encode") method is available to all pooling models in vLLM.

Note

Please use one of the more specific methods or set the task directly when using `LLM.encode`:

-   For embeddings, use `LLM.embed(...)` or `pooling_task="embed"`.
-   For classification logits, use `LLM.classify(...)` or `pooling_task="classify"`.
-   For similarity scores, use `LLM.score(...)`.
-   For rewards, use `LLM.reward(...)` or `pooling_task="token_classify"`.
-   For token classification, use `pooling_task="token_classify"`.
-   For multi-vector retrieval, use `pooling_task="token_embed"`.
-   For IO Processor Plugins, use `pooling_task="plugin"`.

    from vllm import LLM

    llm = LLM(model="intfloat/e5-small", runner="pooling")
    (output,) = llm.encode("Hello, my name is", pooling_task="embed")

    data = output.outputs.data
    print(f"Data: ")

## Online Serving[¶](#online-serving "Permanent link")

Our [OpenAI-Compatible Server](../../serving/openai_compatible_server/) provides endpoints that correspond to the offline APIs:

-   [Embeddings API](../../serving/openai_compatible_server/#embeddings-api) is similar to `LLM.embed`, accepting both text and [multi-modal inputs](../../features/multimodal_inputs/) for embedding models.
-   [Classification API](../../serving/openai_compatible_server/#classification-api) is similar to `LLM.classify` and is applicable to sequence classification models.
-   [Score API](../../serving/openai_compatible_server/#score-api) is similar to `LLM.score` for cross-encoder models.
-   [Pooling API](../../serving/openai_compatible_server/#pooling-api) is similar to `LLM.encode`, being applicable to all types of pooling models.

Note

Please use one of the more specific endpoints or set the task directly when using the [Pooling API](../../serving/openai_compatible_server/#pooling-api):

-   For embeddings, use [Embeddings API](../../serving/openai_compatible_server/#embeddings-api) or `"task":"embed"`.
-   For classification logits, use [Classification API](../../serving/openai_compatible_server/#classification-api) or `"task":"classify"`.
-   For similarity scores, use [Score API](../../serving/openai_compatible_server/#score-api).
-   For rewards, use `"task":"token_classify"`.
-   For token classification, use `"task":"token_classify"`.
-   For multi-vector retrieval, use `"task":"token_embed"`.
-   For IO Processor Plugins, use `"task":"plugin"`.

    # start a supported embeddings model server with `vllm serve`, e.g.
    # vllm serve intfloat/e5-small
    import requests

    host = "localhost"
    port = "8000"
    model_name = "intfloat/e5-small"

    api_url = f"http://:/pooling"

    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        "The capital of France is",
        "The future of AI is",
    ]
    prompt = 

    response = requests.post(api_url, json=prompt)

    for output in response.json()["data"]:
        data = output["data"]
        print(f"Data:  (size=)")

## Matryoshka Embeddings[¶](#matryoshka-embeddings "Permanent link")

[Matryoshka Embeddings](https://sbert.net/examples/sentence_transformer/training/matryoshka/README.html#matryoshka-embeddings) or [Matryoshka Representation Learning (MRL)](https://arxiv.org/abs/2205.13147) is a technique used in training embedding models. It allows users to trade off between performance and cost.

Warning

Not all embedding models are trained using Matryoshka Representation Learning. To avoid misuse of the `dimensions` parameter, vLLM returns an error for requests that attempt to change the output dimension of models that do not support Matryoshka Embeddings.

For example, setting `dimensions` parameter while using the `BAAI/bge-m3` model will result in the following error.

    

### Manually enable Matryoshka Embeddings[¶](#manually-enable-matryoshka-embeddings "Permanent link")

There is currently no official interface for specifying support for Matryoshka Embeddings. In vLLM, if `is_matryoshka` is `True` in `config.json`, you can change the output dimension to arbitrary values. Use `matryoshka_dimensions` to control the allowed output dimensions.

For models that support Matryoshka Embeddings but are not recognized by vLLM, manually override the config using `hf_overrides=` or `hf_overrides=` (offline), or `--hf-overrides ''` or `--hf-overrides ''` (online).

Here is an example to serve a model with Matryoshka Embeddings enabled.

    vllm serve Snowflake/snowflake-arctic-embed-m-v1.5 --hf-overrides ''

### Offline Inference[¶](#offline-inference_1 "Permanent link") 

You can change the output dimensions of embedding models that support Matryoshka Embeddings by using the dimensions parameter in [PoolingParams](../../api/vllm/#vllm.PoolingParams "            PoolingParams").

    from vllm import LLM, PoolingParams

    llm = LLM(
        model="jinaai/jina-embeddings-v3",
        runner="pooling",
        trust_remote_code=True,
    )
    outputs = llm.embed(
        ["Follow the white rabbit."],
        pooling_params=PoolingParams(dimensions=32),
    )
    print(outputs[0].outputs)

A code example can be found here: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/pooling/embed/embed_matryoshka_fy.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/embed/embed_matryoshka_fy.py)

### Online Inference[¶](#online-inference "Permanent link")

Use the following command to start the vLLM server.

    vllm serve jinaai/jina-embeddings-v3 --trust-remote-code

You can change the output dimensions of embedding models that support Matryoshka Embeddings by using the dimensions parameter.

    curl http://127.0.0.1:8000/v1/embeddings \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d ''

Expected output:

    ],"usage":}

An OpenAI client example can be found here: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/pooling/embed/openai_embedding_matryoshka_fy.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/embed/openai_embedding_matryoshka_fy.py)

## Deprecated Features[¶](#deprecated-features "Permanent link")

### Encode task[¶](#encode-task "Permanent link")

We have split the `encode` task into two more specific token-wise tasks: `token_embed` and `token_classify`:

-   `token_embed` is the same as `embed`, using normalization as the activation.
-   `token_classify` is the same as `classify`, by default using softmax as the activation.

### Remove softmax from PoolingParams[¶](#remove-softmax-from-poolingparams "Permanent link")

We are going to remove `softmax` and `activation` from `PoolingParams` in v0.15. Instead, use `use_activation`, since we allow `classify` and `token_classify` to use any activation function.

### as_reward_model[¶](#as_reward_model "Permanent link")

Warning

We are going to remove `--convert reward` in v0.15, use `--convert embed` instead.

Pooling models now default support all pooling, you can use it without any settings.

-   Extracting hidden states prefers using `token_embed` task.
-   Reward models prefers using `token_classify` task.

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [December 11, 2025] ]