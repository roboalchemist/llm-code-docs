# Source: https://docs.vllm.ai/en/stable/configuration/engine_args/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/configuration/engine_args.md "Edit this page")

# Engine Arguments[¶](#engine-arguments "Permanent link")

Engine arguments control the behavior of the vLLM engine.

-   For [offline inference](../../serving/offline_inference/), they are part of the arguments to [LLM](../../api/vllm/#vllm.LLM "            LLM") class.
-   For [online serving](../../serving/openai_compatible_server/), they are part of the arguments to `vllm serve`.

The engine argument classes, [EngineArgs](../../api/vllm/engine/arg_utils/#vllm.engine.arg_utils.EngineArgs "            EngineArgs

  
      dataclass
  ") and [AsyncEngineArgs](../../api/vllm/engine/arg_utils/#vllm.engine.arg_utils.AsyncEngineArgs "            AsyncEngineArgs

  
      dataclass
  "), are a combination of the configuration classes defined in [vllm.config](../../api/vllm/config/#vllm.config "            vllm.config"). Therefore, if you are interested in developer documentation, we recommend looking at these configuration classes as they are the source of truth for types, defaults and docstrings.

When passing JSON CLI arguments, the following sets of arguments are equivalent:

-   `--json-arg '}'`
-   `--json-arg.key1 value1 --json-arg.key2.key3 value2`

Additionally, list elements can be passed individually using `+`:

-   `--json-arg ''`
-   `--json-arg.key4+ value3 --json-arg.key4+='value4,value5'`

## `EngineArgs`[¶](#engineargs "Permanent link")

## `AsyncEngineArgs`[¶](#asyncengineargs "Permanent link")

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [August 11, 2025] ]