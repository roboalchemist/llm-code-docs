# Source: https://docs.vllm.ai/en/stable/features/custom_arguments/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/features/custom_arguments.md "Edit this page")

# Custom Arguments[¶](#custom-arguments "Permanent link")

You can use vLLM *custom arguments* to pass in arguments which are not part of the vLLM `SamplingParams` and REST API specifications. Adding or removing a vLLM custom argument does not require recompiling vLLM, since the custom arguments are passed in as a dictionary.

Custom arguments can be useful if, for example, you want to use a [custom logits processor](../custom_logitsprocs/) without modifying the vLLM source code.

Note

Make sure your custom logits processor have implemented `validate_params` for custom arguments. Otherwise, invalid custom arguments can cause unexpected behaviour.

## Offline Custom Arguments[¶](#offline-custom-arguments "Permanent link")

Custom arguments passed to `SamplingParams.extra_args` as a `dict` will be visible to any code which has access to `SamplingParams`:

    SamplingParams(extra_args=)

This allows arguments which are not already part of `SamplingParams` to be passed into `LLM` as part of a request.

## Online Custom Arguments[¶](#online-custom-arguments "Permanent link")

The vLLM REST API allows custom arguments to be passed to the vLLM server via `vllm_xargs`. The example below integrates custom arguments into a vLLM REST API request:

    curl http://localhost:8000/v1/completions \
        -H "Content-Type: application/json" \
        -d '
        }'

Furthermore, OpenAI SDK users can access `vllm_xargs` via the `extra_body` argument:

    batch = await client.completions.create(
        model="Qwen/Qwen2.5-1.5B-Instruct",
        ...,
        extra_body=
        }
    )

Note

`vllm_xargs` is assigned to `SamplingParams.extra_args` under the hood, so code which uses `SamplingParams.extra_args` is compatible with both offline and online scenarios.

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [November 16, 2025] ]