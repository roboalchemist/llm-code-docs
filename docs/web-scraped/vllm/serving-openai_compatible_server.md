# Source: https://docs.vllm.ai/en/stable/serving/openai_compatible_server/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/serving/openai_compatible_server.md "Edit this page")

# OpenAI-Compatible Server[¶](#openai-compatible-server "Permanent link")

vLLM provides an HTTP server that implements OpenAI\'s [Completions API](https://platform.openai.com/docs/api-reference/completions), [Chat API](https://platform.openai.com/docs/api-reference/chat), and more! This functionality lets you serve models and interact with them using an HTTP client.

In your terminal, you can [install](../../getting_started/installation/) vLLM, then start the server with the [`vllm serve`](../../configuration/serve_args/) command. (You can also use our [Docker](../../deployment/docker/) image.)

    vllm serve NousResearch/Meta-Llama-3-8B-Instruct \
      --dtype auto \
      --api-key token-abc123

To call the server, in your preferred text editor, create a script that uses an HTTP client. Include any messages that you want to send to the model. Then run that script. Below is an example script using the [official OpenAI Python client](https://github.com/openai/openai-python).

Code

    from openai import OpenAI
    client = OpenAI(
        base_url="http://localhost:8000/v1",
        api_key="token-abc123",
    )

    completion = client.chat.completions.create(
        model="NousResearch/Meta-Llama-3-8B-Instruct",
        messages=[
            ,
        ],
    )

    print(completion.choices[0].message)

Tip

vLLM supports some parameters that are not supported by OpenAI, `top_k` for example. You can pass these parameters to vLLM using the OpenAI client in the `extra_body` parameter of your requests, i.e. `extra_body=` for `top_k`.

Important

By default, the server applies `generation_config.json` from the Hugging Face model repository if it exists. This means the default values of certain sampling parameters can be overridden by those recommended by the model creator.

To disable this behavior, please pass `--generation-config vllm` when launching the server.

## Supported APIs[¶](#supported-apis "Permanent link")

We currently support the following OpenAI APIs:

-   [Completions API](#completions-api) (`/v1/completions`)
    -   Only applicable to [text generation models](../../models/generative_models/).
    -   *Note: `suffix` parameter is not supported.*
-   [Chat Completions API](#chat-api) (`/v1/chat/completions`)
    -   Only applicable to [text generation models](../../models/generative_models/) with a [chat template](./#chat-template).
    -   *Note: `user` parameter is ignored.*
    -   *Note:* Setting the `parallel_tool_calls` parameter to `false` ensures vLLM only returns zero or one tool call per request. Setting it to `true` (the default) allows returning more than one tool call per request. There is no guarantee more than one tool call will be returned if this is set to `true`, as that behavior is model dependent and not all models are designed to support parallel tool calls.
-   [Embeddings API](#embeddings-api) (`/v1/embeddings`)
    -   Only applicable to [embedding models](../../models/pooling_models/).
-   [Transcriptions API](#transcriptions-api) (`/v1/audio/transcriptions`)
    -   Only applicable to [Automatic Speech Recognition (ASR) models](../../models/supported_models/#transcription).
-   [Translation API](#translations-api) (`/v1/audio/translations`)
    -   Only applicable to [Automatic Speech Recognition (ASR) models](../../models/supported_models/#transcription).

In addition, we have the following custom APIs:

-   [Tokenizer API](#tokenizer-api) (`/tokenize`, `/detokenize`)
    -   Applicable to any model with a tokenizer.
-   [Pooling API](#pooling-api) (`/pooling`)
    -   Applicable to all [pooling models](../../models/pooling_models/).
-   [Classification API](#classification-api) (`/classify`)
    -   Only applicable to [classification models](../../models/pooling_models/).
-   [Score API](#score-api) (`/score`)
    -   Applicable to [embedding models and cross-encoder models](../../models/pooling_models/).
-   [Re-rank API](#re-rank-api) (`/rerank`, `/v1/rerank`, `/v2/rerank`)
    -   Implements [Jina AI\'s v1 re-rank API](https://jina.ai/reranker/)
    -   Also compatible with [Cohere\'s v1 & v2 re-rank APIs](https://docs.cohere.com/v2/reference/rerank)
    -   Jina and Cohere\'s APIs are very similar; Jina\'s includes extra information in the rerank endpoint\'s response.
    -   Only applicable to [cross-encoder models](../../models/pooling_models/).

## Chat Template[¶](#chat-template "Permanent link")

In order for the language model to support chat protocol, vLLM requires the model to include a chat template in its tokenizer configuration. The chat template is a Jinja2 template that specifies how roles, messages, and other chat-specific tokens are encoded in the input.

An example chat template for `NousResearch/Meta-Llama-3-8B-Instruct` can be found [here](https://github.com/meta-llama/llama3?tab=readme-ov-file#instruction-tuned-models)

Some models do not provide a chat template even though they are instruction/chat fine-tuned. For those models, you can manually specify their chat template in the `--chat-template` parameter with the file path to the chat template, or the template in string form. Without a chat template, the server will not be able to process chat and all chat requests will error.

    vllm serve <model> --chat-template ./path-to-chat-template.jinja

vLLM community provides a set of chat templates for popular models. You can find them under the [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples](https://github.com/vllm-project/vllm/tree/main/examples) directory.

With the inclusion of multi-modal chat APIs, the OpenAI spec now accepts chat messages in a new format which specifies both a `type` and a `text` field. An example is provided below:

    completion = client.chat.completions.create(
        model="NousResearch/Meta-Llama-3-8B-Instruct",
        messages=[
            ,
                ],
            },
        ],
    )

Most chat templates for LLMs expect the `content` field to be a string, but there are some newer models like `meta-llama/Llama-Guard-3-1B` that expect the content to be formatted according to the OpenAI schema in the request. vLLM provides best-effort support to detect this automatically, which is logged as a string like *\"Detected the chat template content format to be\...\"*, and internally converts incoming requests to match the detected format, which can be one of:

-   `"string"`: A string.
    -   Example: `"Hello world"`
-   `"openai"`: A list of dictionaries, similar to OpenAI schema.
    -   Example: `[]`

If the result is not what you expect, you can set the `--chat-template-content-format` CLI argument to override which format to use.

## Extra Parameters[¶](#extra-parameters "Permanent link")

vLLM supports a set of parameters that are not part of the OpenAI API. In order to use them, you can pass them as extra parameters in the OpenAI client. Or directly merge them into the JSON payload if you are using HTTP call directly.

    completion = client.chat.completions.create(
        model="NousResearch/Meta-Llama-3-8B-Instruct",
        messages=[
            ,
        ],
        extra_body=,
        },
    )

## Extra HTTP Headers[¶](#extra-http-headers "Permanent link")

Only `X-Request-Id` HTTP request header is supported for now. It can be enabled with `--enable-request-id-headers`.

Code

    completion = client.chat.completions.create(
        model="NousResearch/Meta-Llama-3-8B-Instruct",
        messages=[
            ,
        ],
        extra_headers=,
    )
    print(completion._request_id)

    completion = client.completions.create(
        model="NousResearch/Meta-Llama-3-8B-Instruct",
        prompt="A robot may not injure a human being",
        extra_headers=,
    )
    print(completion._request_id)

## API Reference[¶](#api-reference "Permanent link")

### Completions API[¶](#completions-api "Permanent link")

Our Completions API is compatible with [OpenAI\'s Completions API](https://platform.openai.com/docs/api-reference/completions); you can use the [official OpenAI Python client](https://github.com/openai/openai-python) to interact with it.

Code example: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/online_serving/openai_completion_client.py](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_completion_client.py)

#### Extra parameters[¶](#extra-parameters_1 "Permanent link") 

The following [sampling parameters](../../api/#inference-parameters) are supported.

Code

        use_beam_search: bool = False
        top_k: int | None = None
        min_p: float | None = None
        repetition_penalty: float | None = None
        length_penalty: float = 1.0
        stop_token_ids: list[int] | None = []
        include_stop_str_in_output: bool = False
        ignore_eos: bool = False
        min_tokens: int = 0
        skip_special_tokens: bool = True
        spaces_between_special_tokens: bool = True
        truncate_prompt_tokens: Annotated[int, Field(ge=-1)] | None = None
        allowed_token_ids: list[int] | None = None
        prompt_logprobs: int | None = None

The following extra parameters are supported:

Code

        prompt_embeds: bytes | list[bytes] | None = None
        add_special_tokens: bool = Field(
            default=True,
            description=(
                "If true (the default), special tokens (e.g. BOS) will be added to "
                "the prompt."
            ),
        )
        response_format: AnyResponseFormat | None = Field(
            default=None,
            description=(
                "Similar to chat completion, this parameter specifies the format "
                "of output. Only , "
                ", , or  is supported."
            ),
        )
        structured_outputs: StructuredOutputsParams | None = Field(
            default=None,
            description="Additional kwargs for structured outputs",
        )
        priority: int = Field(
            default=0,
            description=(
                "The priority of the request (lower means earlier handling; "
                "default: 0). Any priority other than 0 will raise an error "
                "if the served model does not use priority scheduling."
            ),
        )
        request_id: str = Field(
            default_factory=random_uuid,
            description=(
                "The request_id related to this request. If the caller does "
                "not set it, a random_uuid will be generated. This id is used "
                "through out the inference process and return in response."
            ),
        )
        logits_processors: LogitsProcessors | None = Field(
            default=None,
            description=(
                "A list of either qualified names of logits processors, or "
                "constructor objects, to apply when sampling. A constructor is "
                "a JSON object with a required 'qualname' field specifying the "
                "qualified name of the processor class/factory, and optional "
                "'args' and 'kwargs' fields containing positional and keyword "
                "arguments. For example: }."
            ),
        )

        return_tokens_as_token_ids: bool | None = Field(
            default=None,
            description=(
                "If specified with 'logprobs', tokens are represented "
                " as strings of the form 'token_id:' so that tokens "
                "that are not JSON-encodable can be identified."
            ),
        )
        return_token_ids: bool | None = Field(
            default=None,
            description=(
                "If specified, the result will include token IDs alongside the "
                "generated text. In streaming mode, prompt_token_ids is included "
                "only in the first chunk, and token_ids contains the delta tokens "
                "for each chunk. This is useful for debugging or when you "
                "need to map generated text back to input tokens."
            ),
        )

        cache_salt: str | None = Field(
            default=None,
            description=(
                "If specified, the prefix cache will be salted with the provided "
                "string to prevent an attacker to guess prompts in multi-user "
                "environments. The salt should be random, protected from "
                "access by 3rd parties, and long enough to be "
                "unpredictable (e.g., 43 characters base64-encoded, corresponding "
                "to 256 bit)."
            ),
        )

        kv_transfer_params: dict[str, Any] | None = Field(
            default=None,
            description="KVTransfer parameters used for disaggregated serving.",
        )

        vllm_xargs: dict[str, str | int | float] | None = Field(
            default=None,
            description=(
                "Additional request parameters with string or "
                "numeric values, used by custom extensions."
            ),
        )

### Chat API[¶](#chat-api "Permanent link")

Our Chat API is compatible with [OpenAI\'s Chat Completions API](https://platform.openai.com/docs/api-reference/chat); you can use the [official OpenAI Python client](https://github.com/openai/openai-python) to interact with it.

We support both [Vision](https://platform.openai.com/docs/guides/vision)- and [Audio](https://platform.openai.com/docs/guides/audio?audio-generation-quickstart-example=audio-in)-related parameters; see our [Multimodal Inputs](../../features/multimodal_inputs/) guide for more information.

-   *Note: `image_url.detail` parameter is not supported.*

Code example: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/online_serving/openai_chat_completion_client.py](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_chat_completion_client.py)

#### Extra parameters[¶](#extra-parameters_2 "Permanent link") 

The following [sampling parameters](../../api/#inference-parameters) are supported.

Code

        use_beam_search: bool = False
        top_k: int | None = None
        min_p: float | None = None
        repetition_penalty: float | None = None
        length_penalty: float = 1.0
        stop_token_ids: list[int] | None = []
        include_stop_str_in_output: bool = False
        ignore_eos: bool = False
        min_tokens: int = 0
        skip_special_tokens: bool = True
        spaces_between_special_tokens: bool = True
        truncate_prompt_tokens: Annotated[int, Field(ge=-1)] | None = None
        prompt_logprobs: int | None = None
        allowed_token_ids: list[int] | None = None
        bad_words: list[str] = Field(default_factory=list)

The following extra parameters are supported:

Code

        echo: bool = Field(
            default=False,
            description=(
                "If true, the new message will be prepended with the last message "
                "if they belong to the same role."
            ),
        )
        add_generation_prompt: bool = Field(
            default=True,
            description=(
                "If true, the generation prompt will be added to the chat template. "
                "This is a parameter used by chat template in tokenizer config of the "
                "model."
            ),
        )
        continue_final_message: bool = Field(
            default=False,
            description=(
                "If this is set, the chat will be formatted so that the final "
                "message in the chat is open-ended, without any EOS tokens. The "
                "model will continue this message rather than starting a new one. "
                'This allows you to "prefill" part of the model\'s response for it. '
                "Cannot be used at the same time as `add_generation_prompt`."
            ),
        )
        add_special_tokens: bool = Field(
            default=False,
            description=(
                "If true, special tokens (e.g. BOS) will be added to the prompt "
                "on top of what is added by the chat template. "
                "For most models, the chat template takes care of adding the "
                "special tokens so this should be set to false (as is the "
                "default)."
            ),
        )
        documents: list[dict[str, str]] | None = Field(
            default=None,
            description=(
                "A list of dicts representing documents that will be accessible to "
                "the model if it is performing RAG (retrieval-augmented generation)."
                " If the template does not support RAG, this argument will have no "
                "effect. We recommend that each document should be a dict containing "
                '"title" and "text" keys.'
            ),
        )
        chat_template: str | None = Field(
            default=None,
            description=(
                "A Jinja template to use for this conversion. "
                "As of transformers v4.44, default chat template is no longer "
                "allowed, so you must provide a chat template if the tokenizer "
                "does not define one."
            ),
        )
        chat_template_kwargs: dict[str, Any] | None = Field(
            default=None,
            description=(
                "Additional keyword args to pass to the template renderer. "
                "Will be accessible by the chat template."
            ),
        )
        mm_processor_kwargs: dict[str, Any] | None = Field(
            default=None,
            description=("Additional kwargs to pass to the HF processor."),
        )
        structured_outputs: StructuredOutputsParams | None = Field(
            default=None,
            description="Additional kwargs for structured outputs",
        )
        priority: int = Field(
            default=0,
            description=(
                "The priority of the request (lower means earlier handling; "
                "default: 0). Any priority other than 0 will raise an error "
                "if the served model does not use priority scheduling."
            ),
        )
        request_id: str = Field(
            default_factory=random_uuid,
            description=(
                "The request_id related to this request. If the caller does "
                "not set it, a random_uuid will be generated. This id is used "
                "through out the inference process and return in response."
            ),
        )
        logits_processors: LogitsProcessors | None = Field(
            default=None,
            description=(
                "A list of either qualified names of logits processors, or "
                "constructor objects, to apply when sampling. A constructor is "
                "a JSON object with a required 'qualname' field specifying the "
                "qualified name of the processor class/factory, and optional "
                "'args' and 'kwargs' fields containing positional and keyword "
                "arguments. For example: }."
            ),
        )
        return_tokens_as_token_ids: bool | None = Field(
            default=None,
            description=(
                "If specified with 'logprobs', tokens are represented "
                " as strings of the form 'token_id:' so that tokens "
                "that are not JSON-encodable can be identified."
            ),
        )
        return_token_ids: bool | None = Field(
            default=None,
            description=(
                "If specified, the result will include token IDs alongside the "
                "generated text. In streaming mode, prompt_token_ids is included "
                "only in the first chunk, and token_ids contains the delta tokens "
                "for each chunk. This is useful for debugging or when you "
                "need to map generated text back to input tokens."
            ),
        )
        cache_salt: str | None = Field(
            default=None,
            description=(
                "If specified, the prefix cache will be salted with the provided "
                "string to prevent an attacker to guess prompts in multi-user "
                "environments. The salt should be random, protected from "
                "access by 3rd parties, and long enough to be "
                "unpredictable (e.g., 43 characters base64-encoded, corresponding "
                "to 256 bit)."
            ),
        )
        kv_transfer_params: dict[str, Any] | None = Field(
            default=None,
            description="KVTransfer parameters used for disaggregated serving.",
        )

        vllm_xargs: dict[str, str | int | float | list[str | int | float]] | None = Field(
            default=None,
            description=(
                "Additional request parameters with (list of) string or "
                "numeric values, used by custom extensions."
            ),
        )

### Embeddings API[¶](#embeddings-api "Permanent link")

Our Embeddings API is compatible with [OpenAI\'s Embeddings API](https://platform.openai.com/docs/api-reference/embeddings); you can use the [official OpenAI Python client](https://github.com/openai/openai-python) to interact with it.

Code example: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/pooling/embed/openai_embedding_client.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/embed/openai_embedding_client.py)

If the model has a [chat template](./#chat-template), you can replace `inputs` with a list of `messages` (same schema as [Chat API](#chat-api)) which will be treated as a single prompt to the model. Here is a convenience function for calling the API while retaining OpenAI\'s type annotations:

Code

    from openai import OpenAI
    from openai._types import NOT_GIVEN, NotGiven
    from openai.types.chat import ChatCompletionMessageParam
    from openai.types.create_embedding_response import CreateEmbeddingResponse

    def create_chat_embeddings(
        client: OpenAI,
        *,
        messages: list[ChatCompletionMessageParam],
        model: str,
        encoding_format: Union[Literal["base64", "float"], NotGiven] = NOT_GIVEN,
    ) -> CreateEmbeddingResponse:
        return client.post(
            "/embeddings",
            cast_to=CreateEmbeddingResponse,
            body=,
        )

#### Multi-modal inputs[¶](#multi-modal-inputs "Permanent link")

You can pass multi-modal inputs to embedding models by defining a custom chat template for the server and passing a list of `messages` in the request. Refer to the examples below for illustration.

VLM2VecDSE-Qwen2-MRL

To serve the model:

    vllm serve TIGER-Lab/VLM2Vec-Full --runner pooling \
      --trust-remote-code \
      --max-model-len 4096 \
      --chat-template examples/template_vlm2vec_phi3v.jinja

Important

Since VLM2Vec has the same model architecture as Phi-3.5-Vision, we have to explicitly pass `--runner pooling` to run this model in embedding mode instead of text generation mode.

The custom chat template is completely different from the original one for this model, and can be found here: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/template_vlm2vec_phi3v.jinja](https://github.com/vllm-project/vllm/blob/main/examples/template_vlm2vec_phi3v.jinja)

Since the request schema is not defined by OpenAI client, we post a request to the server using the lower-level `requests` library:

Code

    from openai import OpenAI
    client = OpenAI(
        base_url="http://localhost:8000/v1",
        api_key="EMPTY",
    )
    image_url = "https://vllm-public-assets.s3.us-west-2.amazonaws.com/vision_model_images/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"

    response = create_chat_embeddings(
        client,
        model="TIGER-Lab/VLM2Vec-Full",
        messages=[
            },
                    ,
                ],
            }
        ],
        encoding_format="float",
    )

    print("Image embedding output:", response.data[0].embedding)

To serve the model:

    vllm serve MrLight/dse-qwen2-2b-mrl-v1 --runner pooling \
      --trust-remote-code \
      --max-model-len 8192 \
      --chat-template examples/template_dse_qwen2_vl.jinja

Important

Like with VLM2Vec, we have to explicitly pass `--runner pooling`.

Additionally, `MrLight/dse-qwen2-2b-mrl-v1` requires an EOS token for embeddings, which is handled by a custom chat template: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/template_dse_qwen2_vl.jinja](https://github.com/vllm-project/vllm/blob/main/examples/template_dse_qwen2_vl.jinja)

Important

`MrLight/dse-qwen2-2b-mrl-v1` requires a placeholder image of the minimum image size for text query embeddings. See the full code example below for details.

Full example: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/pooling/embed/openai_chat_embedding_client_for_multimodal.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/embed/openai_chat_embedding_client_for_multimodal.py)

#### Extra parameters[¶](#extra-parameters_3 "Permanent link") 

The following [pooling parameters](../../api/vllm/#vllm.PoolingParams "            PoolingParams") are supported.

        truncate_prompt_tokens: Annotated[int, msgspec.Meta(ge=-1)] | None = None
        dimensions: int | None = None
        normalize: bool | None = None

The following extra parameters are supported by default:

Code

        add_special_tokens: bool = Field(
            default=True,
            description=(
                "If true (the default), special tokens (e.g. BOS) will be added to "
                "the prompt."
            ),
        )
        priority: int = Field(
            default=0,
            description=(
                "The priority of the request (lower means earlier handling; "
                "default: 0). Any priority other than 0 will raise an error "
                "if the served model does not use priority scheduling."
            ),
        )
        request_id: str = Field(
            default_factory=random_uuid,
            description=(
                "The request_id related to this request. If the caller does "
                "not set it, a random_uuid will be generated. This id is used "
                "through out the inference process and return in response."
            ),
        )
        normalize: bool | None = Field(
            default=None,
            description="Whether to normalize the embeddings outputs. Default is True.",
        )
        embed_dtype: EmbedDType = Field(
            default="float32",
            description=(
                "What dtype to use for encoding. Default to using float32 for base64 "
                "encoding to match the OpenAI python client behavior. "
                "This parameter will affect base64 and binary_response."
            ),
        )
        endianness: Endianness = Field(
            default="native",
            description=(
                "What endianness to use for encoding. Default to using native for "
                "base64 encoding to match the OpenAI python client behavior."
                "This parameter will affect base64 and binary_response."
            ),
        )

For chat-like input (i.e. if `messages` is passed), these extra parameters are supported instead:

Code

        add_generation_prompt: bool = Field(
            default=False,
            description=(
                "If true, the generation prompt will be added to the chat template. "
                "This is a parameter used by chat template in tokenizer config of the "
                "model."
            ),
        )

        add_special_tokens: bool = Field(
            default=False,
            description=(
                "If true, special tokens (e.g. BOS) will be added to the prompt "
                "on top of what is added by the chat template. "
                "For most models, the chat template takes care of adding the "
                "special tokens so this should be set to false (as is the "
                "default)."
            ),
        )
        chat_template: str | None = Field(
            default=None,
            description=(
                "A Jinja template to use for this conversion. "
                "As of transformers v4.44, default chat template is no longer "
                "allowed, so you must provide a chat template if the tokenizer "
                "does not define one."
            ),
        )
        chat_template_kwargs: dict[str, Any] | None = Field(
            default=None,
            description=(
                "Additional keyword args to pass to the template renderer. "
                "Will be accessible by the chat template."
            ),
        )
        mm_processor_kwargs: dict[str, Any] | None = Field(
            default=None,
            description=("Additional kwargs to pass to the HF processor."),
        )
        priority: int = Field(
            default=0,
            description=(
                "The priority of the request (lower means earlier handling; "
                "default: 0). Any priority other than 0 will raise an error "
                "if the served model does not use priority scheduling."
            ),
        )
        request_id: str = Field(
            default_factory=random_uuid,
            description=(
                "The request_id related to this request. If the caller does "
                "not set it, a random_uuid will be generated. This id is used "
                "through out the inference process and return in response."
            ),
        )
        normalize: bool | None = Field(
            default=None,
            description="Whether to normalize the embeddings outputs. Default is True.",
        )
        embed_dtype: EmbedDType = Field(
            default="float32",
            description=(
                "What dtype to use for encoding. Default to using float32 for base64 "
                "encoding to match the OpenAI python client behavior. "
                "This parameter will affect base64 and binary_response."
            ),
        )
        endianness: Endianness = Field(
            default="native",
            description=(
                "What endianness to use for encoding. Default to using native for "
                "base64 encoding to match the OpenAI python client behavior."
                "This parameter will affect base64 and binary_response."
            ),
        )

### Transcriptions API[¶](#transcriptions-api "Permanent link")

Our Transcriptions API is compatible with [OpenAI\'s Transcriptions API](https://platform.openai.com/docs/api-reference/audio/createTranscription); you can use the [official OpenAI Python client](https://github.com/openai/openai-python) to interact with it.

Note

To use the Transcriptions API, please install with extra audio dependencies using `pip install vllm[audio]`.

Code example: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/online_serving/openai_transcription_client.py](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_transcription_client.py)

#### API Enforced Limits[¶](#api-enforced-limits "Permanent link")

Set the maximum audio file size (in MB) that VLLM will accept, via the `VLLM_MAX_AUDIO_CLIP_FILESIZE_MB` environment variable. Default is 25 MB.

#### Uploading Audio Files[¶](#uploading-audio-files "Permanent link")

The Transcriptions API supports uploading audio files in various formats including FLAC, MP3, MP4, MPEG, MPGA, M4A, OGG, WAV, and WEBM.

**Using OpenAI Python Client:**

Code

    from openai import OpenAI

    client = OpenAI(
        base_url="http://localhost:8000/v1",
        api_key="token-abc123",
    )

    # Upload audio file from disk
    with open("audio.mp3", "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="openai/whisper-large-v3-turbo",
            file=audio_file,
            language="en",
            response_format="verbose_json",
        )

    print(transcription.text)

**Using curl with multipart/form-data:**

Code

    curl -X POST "http://localhost:8000/v1/audio/transcriptions" \
      -H "Authorization: Bearer token-abc123" \
      -F "[email protected]" \
      -F "model=openai/whisper-large-v3-turbo" \
      -F "language=en" \
      -F "response_format=verbose_json"

**Supported Parameters:**

-   `file`: The audio file to transcribe (required)
-   `model`: The model to use for transcription (required)
-   `language`: The language code (e.g., \"en\", \"zh\") (optional)
-   `prompt`: Optional text to guide the transcription style (optional)
-   `response_format`: Format of the response (\"json\", \"text\") (optional)
-   `temperature`: Sampling temperature between 0 and 1 (optional)

For the complete list of supported parameters including sampling parameters and vLLM extensions, see the [protocol definitions](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/protocol.py#L2182).

**Response Format:**

For `verbose_json` response format:

Code

    
      ]
    }

Currently "verbose_json" response format doesn't support avg_logprob, compression_ratio, no_speech_prob.

#### Extra Parameters[¶](#extra-parameters_4 "Permanent link") 

The following [sampling parameters](../../api/#inference-parameters) are supported.

Code

        temperature: float = Field(default=0.0)
        """The sampling temperature, between 0 and 1.

        Higher values like 0.8 will make the output more random, while lower values
        like 0.2 will make it more focused / deterministic. If set to 0, the model
        will use [log probability](https://en.wikipedia.org/wiki/Log_probability)
        to automatically increase the temperature until certain thresholds are hit.
        """

        top_p: float | None = None
        """Enables nucleus (top-p) sampling, where tokens are selected from the
        smallest possible set whose cumulative probability exceeds `p`.
        """

        top_k: int | None = None
        """Limits sampling to the `k` most probable tokens at each step."""

        min_p: float | None = None
        """Filters out tokens with a probability lower than `min_p`, ensuring a
        minimum likelihood threshold during sampling.
        """

        seed: int | None = Field(None, ge=_LONG_INFO.min, le=_LONG_INFO.max)
        """The seed to use for sampling."""

        frequency_penalty: float | None = 0.0
        """The frequency penalty to use for sampling."""

        repetition_penalty: float | None = None
        """The repetition penalty to use for sampling."""

        presence_penalty: float | None = 0.0
        """The presence penalty to use for sampling."""

The following extra parameters are supported:

Code

        # Flattened stream option to simplify form data.
        stream_include_usage: bool | None = False
        stream_continuous_usage_stats: bool | None = False

        vllm_xargs: dict[str, str | int | float] | None = Field(
            default=None,
            description=(
                "Additional request parameters with string or "
                "numeric values, used by custom extensions."
            ),
        )

### Translations API[¶](#translations-api "Permanent link")

Our Translation API is compatible with [OpenAI\'s Translations API](https://platform.openai.com/docs/api-reference/audio/createTranslation); you can use the [official OpenAI Python client](https://github.com/openai/openai-python) to interact with it. Whisper models can translate audio from one of the 55 non-English supported languages into English. Please mind that the popular `openai/whisper-large-v3-turbo` model does not support translating.

Note

To use the Translation API, please install with extra audio dependencies using `pip install vllm[audio]`.

Code example: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/online_serving/openai_translation_client.py](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_translation_client.py)

#### Extra Parameters[¶](#extra-parameters_5 "Permanent link") 

The following [sampling parameters](../../api/#inference-parameters) are supported.

        seed: int | None = Field(None, ge=_LONG_INFO.min, le=_LONG_INFO.max)
        """The seed to use for sampling."""

        temperature: float = Field(default=0.0)
        """The sampling temperature, between 0 and 1.

        Higher values like 0.8 will make the output more random, while lower values
        like 0.2 will make it more focused / deterministic. If set to 0, the model
        will use [log probability](https://en.wikipedia.org/wiki/Log_probability)
        to automatically increase the temperature until certain thresholds are hit.
        """

The following extra parameters are supported:

        language: str | None = None
        """The language of the input audio we translate from.

        Supplying the input language in
        [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format
        will improve accuracy.
        """

        to_language: str | None = None
        """The language of the input audio we translate to.

        Please note that this is not supported by all models, refer to the specific
        model documentation for more details.
        For instance, Whisper only supports `to_language=en`.
        """

        stream: bool | None = False
        """Custom field not present in the original OpenAI definition. When set,
        it will enable output to be streamed in a similar fashion as the Chat
        Completion endpoint.
        """
        # Flattened stream option to simplify form data.
        stream_include_usage: bool | None = False
        stream_continuous_usage_stats: bool | None = False

### Tokenizer API[¶](#tokenizer-api "Permanent link")

Our Tokenizer API is a simple wrapper over [HuggingFace-style tokenizers](https://huggingface.co/docs/transformers/en/main_classes/tokenizer). It consists of two endpoints:

-   `/tokenize` corresponds to calling `tokenizer.encode()`.
-   `/detokenize` corresponds to calling `tokenizer.decode()`.

### Pooling API[¶](#pooling-api "Permanent link")

Our Pooling API encodes input prompts using a [pooling model](../../models/pooling_models/) and returns the corresponding hidden states.

The input format is the same as [Embeddings API](#embeddings-api), but the output data can contain an arbitrary nested list, not just a 1-D list of floats.

Code example: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/pooling/pooling/openai_pooling_client.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/pooling/openai_pooling_client.py)

### Classification API[¶](#classification-api "Permanent link")

Our Classification API directly supports Hugging Face sequence-classification models such as [ai21labs/Jamba-tiny-reward-dev](https://huggingface.co/ai21labs/Jamba-tiny-reward-dev) and [jason9693/Qwen2.5-1.5B-apeach](https://huggingface.co/jason9693/Qwen2.5-1.5B-apeach).

We automatically wrap any other transformer via `as_seq_cls_model()`, which pools on the last token, attaches a `RowParallelLinear` head, and applies a softmax to produce per-class probabilities.

Code example: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/pooling/classify/openai_classification_client.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/classify/openai_classification_client.py)

#### Example Requests[¶](#example-requests "Permanent link")

You can classify multiple texts by passing an array of strings:

    curl -v "http://127.0.0.1:8000/classify" \
      -H "Content-Type: application/json" \
      -d ''

Response

    ,
        
      ],
      "usage": 
    }

You can also pass a string directly to the `input` field:

    curl -v "http://127.0.0.1:8000/classify" \
      -H "Content-Type: application/json" \
      -d ''

Response

    
      ],
      "usage": 
    }

#### Extra parameters[¶](#extra-parameters_6 "Permanent link") 

The following [pooling parameters](../../api/vllm/#vllm.PoolingParams "            PoolingParams") are supported.

        truncate_prompt_tokens: Annotated[int, msgspec.Meta(ge=-1)] | None = None
        softmax: bool | None = None
        activation: bool | None = None
        use_activation: bool | None = None

The following extra parameters are supported:

        priority: int = Field(
            default=0,
            description=(
                "The priority of the request (lower means earlier handling; "
                "default: 0). Any priority other than 0 will raise an error "
                "if the served model does not use priority scheduling."
            ),
        )
        add_special_tokens: bool = Field(
            default=True,
            description=(
                "If true (the default), special tokens (e.g. BOS) will be added to "
                "the prompt."
            ),
        )
        request_id: str = Field(
            default_factory=random_uuid,
            description=(
                "The request_id related to this request. If the caller does "
                "not set it, a random_uuid will be generated. This id is used "
                "through out the inference process and return in response."
            ),
        )
        softmax: bool | None = Field(
            default=None,
            description="softmax will be deprecated, please use use_activation instead.",
        )

        activation: bool | None = Field(
            default=None,
            description="activation will be deprecated, please use use_activation instead.",
        )

        use_activation: bool | None = Field(
            default=None,
            description="Whether to use activation for classification outputs. "
            "Default is True.",
        )

### Score API[¶](#score-api "Permanent link")

Our Score API can apply a cross-encoder model or an embedding model to predict scores for sentence or multimodal pairs. When using an embedding model the score corresponds to the cosine similarity between each embedding pair. Usually, the score for a sentence pair refers to the similarity between two sentences, on a scale of 0 to 1.

You can find the documentation for cross encoder models at [sbert.net](https://www.sbert.net/docs/package_reference/cross_encoder/cross_encoder.html).

Code example: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/pooling/score/openai_cross_encoder_score.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/openai_cross_encoder_score.py)

#### Single inference[¶](#single-inference "Permanent link")

You can pass a string to both `text_1` and `text_2`, forming a single sentence pair.

    curl -X 'POST' \
      'http://127.0.0.1:8000/score' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d ''

Response

    
      ],
      "usage": 
    }

#### Batch inference[¶](#batch-inference "Permanent link")

You can pass a string to `text_1` and a list to `text_2`, forming multiple sentence pairs where each pair is built from `text_1` and a string in `text_2`. The total number of pairs is `len(text_2)`.

Request

    curl -X 'POST' \
      'http://127.0.0.1:8000/score' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d ''

Response

    ,
        
      ],
      "usage": 
    }

You can pass a list to both `text_1` and `text_2`, forming multiple sentence pairs where each pair is built from a string in `text_1` and the corresponding string in `text_2` (similar to `zip()`). The total number of pairs is `len(text_2)`.

Request

    curl -X 'POST' \
      'http://127.0.0.1:8000/score' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d ''

Response

    ,
        
      ],
      "usage": 
    }

#### Multi-modal inputs[¶](#multi-modal-inputs_1 "Permanent link") 

You can pass multi-modal inputs to scoring models by passing `content` including a list of multi-modal input (image, etc.) in the request. Refer to the examples below for illustration.

JinaVL-Reranker

To serve the model:

    vllm serve jinaai/jina-reranker-m0

Since the request schema is not defined by OpenAI client, we post a request to the server using the lower-level `requests` library:

Code

    import requests

    response = requests.post(
        "http://localhost:8000/v1/score",
        json=,
                    },
                    ,
                    },
                ],
            },
        },
    )
    response.raise_for_status()
    response_json = response.json()
    print("Scoring output:", response_json["data"][0]["score"])
    print("Scoring output:", response_json["data"][1]["score"])

Full example: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/pooling/score/openai_cross_encoder_score_for_multimodal.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/openai_cross_encoder_score_for_multimodal.py)

#### Extra parameters[¶](#extra-parameters_7 "Permanent link") 

The following [pooling parameters](../../api/vllm/#vllm.PoolingParams "            PoolingParams") are supported.

        truncate_prompt_tokens: Annotated[int, msgspec.Meta(ge=-1)] | None = None
        softmax: bool | None = None
        activation: bool | None = None
        use_activation: bool | None = None

The following extra parameters are supported:

        mm_processor_kwargs: dict[str, Any] | None = Field(
            default=None,
            description=("Additional kwargs to pass to the HF processor."),
        )

        priority: int = Field(
            default=0,
            description=(
                "The priority of the request (lower means earlier handling; "
                "default: 0). Any priority other than 0 will raise an error "
                "if the served model does not use priority scheduling."
            ),
        )

        softmax: bool | None = Field(
            default=None,
            description="softmax will be deprecated, please use use_activation instead.",
        )

        activation: bool | None = Field(
            default=None,
            description="activation will be deprecated, please use use_activation instead.",
        )

        use_activation: bool | None = Field(
            default=None,
            description="Whether to use activation for classification outputs. "
            "Default is True.",
        )

### Re-rank API[¶](#re-rank-api "Permanent link")

Our Re-rank API can apply an embedding model or a cross-encoder model to predict relevant scores between a single query, and each of a list of documents. Usually, the score for a sentence pair refers to the similarity between two sentences or multi-modal inputs (image, etc.), on a scale of 0 to 1.

You can find the documentation for cross encoder models at [sbert.net](https://www.sbert.net/docs/package_reference/cross_encoder/cross_encoder.html).

The rerank endpoints support popular re-rank models such as `BAAI/bge-reranker-base` and other models supporting the `score` task. Additionally, `/rerank`, `/v1/rerank`, and `/v2/rerank` endpoints are compatible with both [Jina AI\'s re-rank API interface](https://jina.ai/reranker/) and [Cohere\'s re-rank API interface](https://docs.cohere.com/v2/reference/rerank) to ensure compatibility with popular open-source tools.

Code example: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/pooling/score/openai_reranker.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/openai_reranker.py)

#### Example Request[¶](#example-request "Permanent link")

Note that the `top_n` request parameter is optional and will default to the length of the `documents` field. Result documents will be sorted by relevance, and the `index` property can be used to determine original order.

Request

    curl -X 'POST' \
      'http://127.0.0.1:8000/v1/rerank' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d ''

Response

    ,
      "results": [
        ,
          "relevance_score": 0.99853515625
        },
        ,
          "relevance_score": 0.0005860328674316406
        }
      ]
    }

#### Extra parameters[¶](#extra-parameters_8 "Permanent link") 

The following [pooling parameters](../../api/vllm/#vllm.PoolingParams "            PoolingParams") are supported.

        truncate_prompt_tokens: Annotated[int, msgspec.Meta(ge=-1)] | None = None
        softmax: bool | None = None
        activation: bool | None = None
        use_activation: bool | None = None

The following extra parameters are supported:

        mm_processor_kwargs: dict[str, Any] | None = Field(
            default=None,
            description=("Additional kwargs to pass to the HF processor."),
        )

        priority: int = Field(
            default=0,
            description=(
                "The priority of the request (lower means earlier handling; "
                "default: 0). Any priority other than 0 will raise an error "
                "if the served model does not use priority scheduling."
            ),
        )

        softmax: bool | None = Field(
            default=None,
            description="softmax will be deprecated, please use use_activation instead.",
        )

        activation: bool | None = Field(
            default=None,
            description="activation will be deprecated, please use use_activation instead.",
        )

        use_activation: bool | None = Field(
            default=None,
            description="Whether to use activation for classification outputs. "
            "Default is True.",
        )

## Ray Serve LLM[¶](#ray-serve-llm "Permanent link")

Ray Serve LLM enables scalable, production-grade serving of the vLLM engine. It integrates tightly with vLLM and extends it with features such as auto-scaling, load balancing, and back-pressure.

Key capabilities:

-   Exposes an OpenAI-compatible HTTP API as well as a Pythonic API.
-   Scales from a single GPU to a multi-node cluster without code changes.
-   Provides observability and autoscaling policies through Ray dashboards and metrics.

The following example shows how to deploy a large model like DeepSeek R1 with Ray Serve LLM: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/online_serving/ray_serve_deepseek.py](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/ray_serve_deepseek.py).

Learn more about Ray Serve LLM with the official [Ray Serve LLM documentation](https://docs.ray.io/en/latest/serve/llm/serving-llms.html).

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [December 11, 2025] ]