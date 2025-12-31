# Source: https://docs.vllm.ai/en/stable/cli/bench/serve/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/cli/bench/serve.md "Edit this page")

# vllm bench serve[¶](#vllm-bench-serve "Permanent link")

## JSON CLI Arguments[¶](#json-cli-arguments "Permanent link")

When passing JSON CLI arguments, the following sets of arguments are equivalent:

-   `--json-arg '}'`
-   `--json-arg.key1 value1 --json-arg.key2.key3 value2`

Additionally, list elements can be passed individually using `+`:

-   `--json-arg ''`
-   `--json-arg.key4+ value3 --json-arg.key4+='value4,value5'`

## Arguments[¶](#arguments "Permanent link")

#### `--seed`[¶](#-seed "Permanent link") 

Default: `0`

#### `--num-prompts`[¶](#-num-prompts "Permanent link") 

Number of prompts to process.

Default: `1000`

#### `--dataset-name`[¶](#-dataset-name "Permanent link") 

Possible choices: `sharegpt`, `burstgpt`, `sonnet`, `random`, `random-mm`, `random-rerank`, `hf`, `custom`, `prefix_repetition`, `spec_bench`

Name of the dataset to benchmark on.

Default: `random`

#### `--no-stream`[¶](#-no-stream "Permanent link") 

Do not load the dataset in streaming mode.

Default: `False`

#### `--dataset-path`[¶](#-dataset-path "Permanent link") 

Path to the sharegpt/sonnet dataset. Or the huggingface dataset ID if using HF dataset.

Default: `None`

#### `--no-oversample`[¶](#-no-oversample "Permanent link") 

Do not oversample if the dataset has fewer samples than num-prompts.

Default: `False`

#### `--skip-chat-template`[¶](#-skip-chat-template "Permanent link") 

Skip applying chat template to prompt for datasets that support it.

Default: `False`

#### `--disable-shuffle`[¶](#-disable-shuffle "Permanent link") 

Disable shuffling of dataset samples for deterministic ordering.

Default: `False`

#### `--label`[¶](#-label "Permanent link") 

The label (prefix) of the benchmark results. If not specified, the value of \'\--backend\' will be used as the label.

Default: `None`

#### `--backend`[¶](#-backend "Permanent link") 

Possible choices: `vllm`, `openai`, `openai-chat`, `openai-audio`, `openai-embeddings`, `openai-embeddings-chat`, `openai-embeddings-clip`, `openai-embeddings-vlm2vec`, `infinity-embeddings`, `infinity-embeddings-clip`, `vllm-rerank`

The type of backend or endpoint to use for the benchmark.

Default: `openai`

#### `--base-url`[¶](#-base-url "Permanent link") 

Server or API base url if not using http host and port.

Default: `None`

#### `--host`[¶](#-host "Permanent link") 

Default: `127.0.0.1`

#### `--port`[¶](#-port "Permanent link") 

Default: `8000`

#### `--endpoint`[¶](#-endpoint "Permanent link") 

API endpoint.

Default: `/v1/completions`

#### `--header`[¶](#-header "Permanent link") 

Key-value pairs (e.g, \--header x-additional-info=0.3.3) for headers to be passed with each request. These headers override per backend constants and values set via environment variable, and will be overridden by other arguments (such as request ids).

Default: `None`

#### `--max-concurrency`[¶](#-max-concurrency "Permanent link") 

Maximum number of concurrent requests. This can be used to help simulate an environment where a higher level component is enforcing a maximum number of concurrent requests. While the \--request-rate argument controls the rate at which requests are initiated, this argument will control how many are actually allowed to execute at a time. This means that when used in combination, the actual request rate may be lower than specified with \--request-rate, if the server is not processing requests fast enough to keep up.

Default: `None`

#### `--model`[¶](#-model "Permanent link") 

Name of the model.

Default: `None`

#### `--tokenizer`[¶](#-tokenizer "Permanent link") 

Name or path of the tokenizer, if not using the default tokenizer.

Default: `None`

#### `--tokenizer-mode`[¶](#-tokenizer-mode "Permanent link") 

Tokenizer mode:

        - "auto" will use the tokenizer from `mistral_common` for Mistral models
        if available, otherwise it will use the "hf" tokenizer.

        - "hf" will use the fast tokenizer if available.

        - "slow" will always use the slow tokenizer.

        - "mistral" will always use the tokenizer from `mistral_common`.

        - "deepseek_v32" will always use the tokenizer from `deepseek_v32`.

        - Other custom values can be supported via plugins.

Default: `auto`

#### `--use-beam-search`[¶](#-use-beam-search "Permanent link") 

Default: `False`

#### `--logprobs`[¶](#-logprobs "Permanent link") 

Number of logprobs-per-token to compute & return as part of the request. If unspecified, then either (1) if beam search is disabled, no logprobs are computed & a single dummy logprob is returned for each token; or (2) if beam search is enabled 1 logprob per token is computed

Default: `None`

#### `--request-rate`[¶](#-request-rate "Permanent link") 

Number of requests per second. If this is inf, then all the requests are sent at time 0. Otherwise, we use Poisson process or gamma distribution to synthesize the request arrival times.

Default: `inf`

#### `--burstiness`[¶](#-burstiness "Permanent link") 

Burstiness factor of the request generation. Only take effect when request_rate is not inf. Default value is 1, which follows Poisson process. Otherwise, the request intervals follow a gamma distribution. A lower burstiness value (0 \< burstiness \< 1) results in more bursty requests. A higher burstiness value (burstiness \> 1) results in a more uniform arrival of requests.

Default: `1.0`

#### `--trust-remote-code`[¶](#-trust-remote-code "Permanent link") 

Trust remote code from huggingface

Default: `False`

#### `--disable-tqdm`[¶](#-disable-tqdm "Permanent link") 

Specify to disable tqdm progress bar.

Default: `False`

#### `--num-warmups`[¶](#-num-warmups "Permanent link") 

Number of warmup requests.

Default: `0`

#### `--profile`[¶](#-profile "Permanent link") 

Use vLLM Profiling. \--profiler-config must be provided on the server.

Default: `False`

#### `--save-result`[¶](#-save-result "Permanent link") 

Specify to save benchmark results to a json file

Default: `False`

#### `--save-detailed`[¶](#-save-detailed "Permanent link") 

When saving the results, whether to include per request information such as response, error, ttfs, tpots, etc.

Default: `False`

#### `--append-result`[¶](#-append-result "Permanent link") 

Append the benchmark result to the existing json file.

Default: `False`

#### `--metadata`[¶](#-metadata "Permanent link") 

Key-value pairs (e.g, \--metadata version=0.3.3 tp=1) for metadata of this run to be saved in the result JSON file for record keeping purposes.

Default: `None`

#### `--result-dir`[¶](#-result-dir "Permanent link") 

Specify directory to save benchmark json results.If not specified, results are saved in the current directory.

Default: `None`

#### `--result-filename`[¶](#-result-filename "Permanent link") 

Specify the filename to save benchmark json results.If not specified, results will be saved in -qps--.json format.

Default: `None`

#### `--ignore-eos`[¶](#-ignore-eos "Permanent link") 

Set ignore_eos flag when sending the benchmark request.Warning: ignore_eos is not supported in deepspeed_mii and tgi.

Default: `False`

#### `--percentile-metrics`[¶](#-percentile-metrics "Permanent link") 

Comma-separated list of selected metrics to report percentiles. This argument specifies the metrics to report percentiles. Allowed metric names are \"ttft\", \"tpot\", \"itl\", \"e2el\". If not specified, defaults to \"ttft,tpot,itl\" for generative models and \"e2el\" for pooling models.

Default: `None`

#### `--metric-percentiles`[¶](#-metric-percentiles "Permanent link") 

Comma-separated list of percentiles for selected metrics. To report 25-th, 50-th, and 75-th percentiles, use \"25,50,75\". Default value is \"99\".Use \"\--percentile-metrics\" to select metrics.

Default: `99`

#### `--goodput`[¶](#-goodput "Permanent link") 

Specify service level objectives for goodput as \"KEY:VALUE\" pairs, where the key is a metric name, and the value is in milliseconds. Multiple \"KEY:VALUE\" pairs can be provided, separated by spaces. Allowed request level metric names are \"ttft\", \"tpot\", \"e2el\". For more context on the definition of goodput, refer to DistServe paper: https://arxiv.org/pdf/2401.09670 and the blog: https://hao-ai-lab.github.io/blogs/distserve

Default: `None`

#### `--request-id-prefix`[¶](#-request-id-prefix "Permanent link") 

Specify the prefix of request id.

Default: `bench-8dbfd74f-`

#### `--served-model-name`[¶](#-served-model-name "Permanent link") 

The model name used in the API. If not specified, the model name will be the same as the `--model` argument.

Default: `None`

#### `--lora-modules`[¶](#-lora-modules "Permanent link") 

A subset of LoRA module names passed in when launching the server. For each request, the script chooses a LoRA module at random.

Default: `None`

#### `--ramp-up-strategy`[¶](#-ramp-up-strategy "Permanent link") 

Possible choices: `linear`, `exponential`

The ramp-up strategy. This would be used to ramp up the request rate from initial RPS to final RPS rate (specified by \--ramp-up-start-rps and \--ramp-up-end-rps.) over the duration of the benchmark.

Default: `None`

#### `--ramp-up-start-rps`[¶](#-ramp-up-start-rps "Permanent link") 

The starting request rate for ramp-up (RPS). Needs to be specified when \--ramp-up-strategy is used.

Default: `None`

#### `--ramp-up-end-rps`[¶](#-ramp-up-end-rps "Permanent link") 

The ending request rate for ramp-up (RPS). Needs to be specified when \--ramp-up-strategy is used.

Default: `None`

#### `--ready-check-timeout-sec`[¶](#-ready-check-timeout-sec "Permanent link") 

Maximum time to wait for the endpoint to become ready in seconds (default: 600 seconds / 10 minutes). If set to 0, the ready check will be skipped.

Default: `600`

#### `--extra-body`[¶](#-extra-body "Permanent link") 

A JSON string representing extra body parameters to include in each request.Example: \'}\'

Default: `None`

### custom dataset options[¶](#custom-dataset-options "Permanent link")

#### `--custom-output-len`[¶](#-custom-output-len "Permanent link") 

Number of output tokens per request, used only for custom dataset.

Default: `256`

### spec bench dataset options[¶](#spec-bench-dataset-options "Permanent link")

#### `--spec-bench-output-len`[¶](#-spec-bench-output-len "Permanent link") 

Num of output tokens per request, used only for spec bench dataset.

Default: `256`

#### `--spec-bench-category`[¶](#-spec-bench-category "Permanent link") 

Category for spec bench dataset. If None, use all categories.

Default: `None`

### sonnet dataset options[¶](#sonnet-dataset-options "Permanent link")

#### `--sonnet-input-len`[¶](#-sonnet-input-len "Permanent link") 

Number of input tokens per request, used only for sonnet dataset.

Default: `550`

#### `--sonnet-output-len`[¶](#-sonnet-output-len "Permanent link") 

Number of output tokens per request, used only for sonnet dataset.

Default: `150`

#### `--sonnet-prefix-len`[¶](#-sonnet-prefix-len "Permanent link") 

Number of prefix tokens per request, used only for sonnet dataset.

Default: `200`

### sharegpt dataset options[¶](#sharegpt-dataset-options "Permanent link")

#### `--sharegpt-output-len`[¶](#-sharegpt-output-len "Permanent link") 

Output length for each request. Overrides the output length from the ShareGPT dataset.

Default: `None`

### blazedit dataset options[¶](#blazedit-dataset-options "Permanent link")

#### `--blazedit-min-distance`[¶](#-blazedit-min-distance "Permanent link") 

Minimum distance for blazedit dataset. Min: 0, Max: 1.0

Default: `0.0`

#### `--blazedit-max-distance`[¶](#-blazedit-max-distance "Permanent link") 

Maximum distance for blazedit dataset. Min: 0, Max: 1.0

Default: `1.0`

### random dataset options[¶](#random-dataset-options "Permanent link")

#### `--random-input-len`[¶](#-random-input-len "Permanent link") 

Number of input tokens per request, used only for random sampling.

Default: `1024`

#### `--random-output-len`[¶](#-random-output-len "Permanent link") 

Number of output tokens per request, used only for random sampling.

Default: `128`

#### `--random-range-ratio`[¶](#-random-range-ratio "Permanent link") 

Range ratio for sampling input/output length, used only for random sampling. Must be in the range \[0, 1) to define a symmetric sampling range\[length \* (1 - range_ratio), length \* (1 + range_ratio)\].

Default: `0.0`

#### `--random-prefix-len`[¶](#-random-prefix-len "Permanent link") 

Number of fixed prefix tokens before the random context in a request. The total input length is the sum of `random-prefix-len` and a random context length sampled from \[input_len \* (1 - range_ratio), input_len \* (1 + range_ratio)\].

Default: `0`

#### `--random-batch-size`[¶](#-random-batch-size "Permanent link") 

Batch size for random sampling. Only used for embeddings benchmark.

Default: `1`

#### `--no-reranker`[¶](#-no-reranker "Permanent link") 

Whether the model supports reranking natively. Only used for reranker benchmark.

Default: `False`

### random multimodal dataset options extended from random dataset[¶](#random-multimodal-dataset-options-extended-from-random-dataset "Permanent link")

#### `--random-mm-base-items-per-request`[¶](#-random-mm-base-items-per-request "Permanent link") 

Base number of multimodal items per request for random-mm. Actual per-request count is sampled around this base using \--random-mm-num-mm-items-range-ratio.

Default: `1`

#### `--random-mm-num-mm-items-range-ratio`[¶](#-random-mm-num-mm-items-range-ratio "Permanent link") 

Range ratio r in \[0, 1\] for sampling items per request. We sample uniformly from the closed integer range \[floor(n*(1-r)), ceil(n*(1+r))\] where n is the base items per request. r=0 keeps it fixed; r=1 allows 0 items. The maximum is clamped to the sum of per-modality limits from \--random-mm-limit-mm-per-prompt. An error is raised if the computed min exceeds the max.

Default: `0.0`

#### `--random-mm-limit-mm-per-prompt`[¶](#-random-mm-limit-mm-per-prompt "Permanent link") 

Per-modality hard caps for items attached per request, e.g. \'\'. The sampled per-request item count is clamped to the sum of these limits. When a modality reaches its cap, its buckets are excluded and probabilities are renormalized.OBS.: Only image sampling is supported for now.

Default: ``

#### `--random-mm-bucket-config`[¶](#-random-mm-bucket-config "Permanent link") 

The bucket config is a dictionary mapping a multimodal itemsampling configuration to a probability.Currently allows for 2 modalities: images and videos. An bucket key is a tuple of (height, width, num_frames)The value is the probability of sampling that specific item. Example: \--random-mm-bucket-config  First item: images with resolution 256x256 w.p. 0.5Second item: images with resolution 720x1280 w.p. 0.4 Third item: videos with resolution 720x1280 and 16 frames w.p. 0.1OBS.: If the probabilities do not sum to 1, they are normalized.OBS bis.: Only image sampling is supported for now.

Default: ``

### hf dataset options[¶](#hf-dataset-options "Permanent link")

#### `--hf-subset`[¶](#-hf-subset "Permanent link") 

Subset of the HF dataset.

Default: `None`

#### `--hf-split`[¶](#-hf-split "Permanent link") 

Split of the HF dataset.

Default: `None`

#### `--hf-name`[¶](#-hf-name "Permanent link") 

Name of the dataset on HuggingFace (e.g., \'lmarena-ai/VisionArena-Chat\'). Specify this if your dataset-path is a local path.

Default: `None`

#### `--hf-output-len`[¶](#-hf-output-len "Permanent link") 

Output length for each request. Overrides the output lengths from the sampled HF dataset.

Default: `None`

### prefix repetition dataset options[¶](#prefix-repetition-dataset-options "Permanent link")

#### `--prefix-repetition-prefix-len`[¶](#-prefix-repetition-prefix-len "Permanent link") 

Number of prefix tokens per request, used only for prefix repetition dataset.

Default: `256`

#### `--prefix-repetition-suffix-len`[¶](#-prefix-repetition-suffix-len "Permanent link") 

Number of suffix tokens per request, used only for prefix repetition dataset. Total input length is prefix_len + suffix_len.

Default: `256`

#### `--prefix-repetition-num-prefixes`[¶](#-prefix-repetition-num-prefixes "Permanent link") 

Number of prefixes to generate, used only for prefix repetition dataset. Prompts per prefix is num_requests // num_prefixes.

Default: `10`

#### `--prefix-repetition-output-len`[¶](#-prefix-repetition-output-len "Permanent link") 

Number of output tokens per request, used only for prefix repetition dataset.

Default: `128`

### sampling parameters[¶](#sampling-parameters "Permanent link")

#### `--top-p`[¶](#-top-p "Permanent link") 

Top-p sampling parameter. Only has effect on openai-compatible backends.

Default: `None`

#### `--top-k`[¶](#-top-k "Permanent link") 

Top-k sampling parameter. Only has effect on openai-compatible backends.

Default: `None`

#### `--min-p`[¶](#-min-p "Permanent link") 

Min-p sampling parameter. Only has effect on openai-compatible backends.

Default: `None`

#### `--temperature`[¶](#-temperature "Permanent link") 

Temperature sampling parameter. Only has effect on openai-compatible backends. If not specified, default to greedy decoding (i.e. temperature==0.0).

Default: `None`

#### `--frequency-penalty`[¶](#-frequency-penalty "Permanent link") 

Frequency penalty sampling parameter. Only has effect on openai-compatible backends.

Default: `None`

#### `--presence-penalty`[¶](#-presence-penalty "Permanent link") 

Presence penalty sampling parameter. Only has effect on openai-compatible backends.

Default: `None`

#### `--repetition-penalty`[¶](#-repetition-penalty "Permanent link") 

Repetition penalty sampling parameter. Only has effect on openai-compatible backends.

Default: `None`

#### `--common-prefix-len`[¶](#-common-prefix-len "Permanent link") 

Common prefix length shared by all prompts (used by random dataset)

Default: `None`

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [November 15, 2025] ]