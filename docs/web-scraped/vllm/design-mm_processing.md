# Source: https://docs.vllm.ai/en/stable/design/mm_processing/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/design/mm_processing.md "Edit this page")

# Multi-Modal Data Processing[¶](#multi-modal-data-processing "Permanent link")

To enable various optimizations in vLLM such as [chunked prefill](../../configuration/optimization/#chunked-prefill) and [prefix caching](../../features/automatic_prefix_caching/), we use [BaseMultiModalProcessor](../../api/vllm/multimodal/processing/#vllm.multimodal.processing.BaseMultiModalProcessor "            BaseMultiModalProcessor") to provide the correspondence between placeholder feature tokens (e.g. `<image>`) and multi-modal inputs (e.g. the raw input image) based on the outputs of HF processor.

Here are the main features of [BaseMultiModalProcessor](../../api/vllm/multimodal/processing/#vllm.multimodal.processing.BaseMultiModalProcessor "            BaseMultiModalProcessor"):

## Prompt Update Detection[¶](#prompt-update-detection "Permanent link")

One of the main responsibilities of HF processor is to update the prompt with placeholder tokens. For example:

-   Insert feature placeholder tokens (e.g. `<image><image>...<image>`, the number of which equals to the feature size) at the start of the string.
-   Replace existing input placeholder tokens (e.g. `<image>` for a single image) with feature placeholder tokens (e.g. `<image><image>...<image>`, the number of which equals to the feature size).

The information about which tokens have been updated is key to finding the correspondence between placeholder feature tokens and multi-modal inputs.

In vLLM, this information is specified using [PromptUpdate](../../api/vllm/multimodal/processing/#vllm.multimodal.processing.PromptUpdate "            PromptUpdate

  
      dataclass
  ") in [\_get_prompt_updates](../../api/vllm/multimodal/processing/#vllm.multimodal.processing.BaseMultiModalProcessor._get_prompt_updates "            _get_prompt_updates

  
      abstractmethod
  "). We can automatically detect whether HF has updated the prompt by checking the existence of the updated tokens.

## Tokenized Prompt Inputs[¶](#tokenized-prompt-inputs "Permanent link")

To enable tokenization in a separate process, we support passing input token IDs alongside multi-modal data.

### The problem[¶](#the-problem "Permanent link")

Consider that HF processors follow these main steps:

1.  Tokenize the text
2.  Process multi-modal inputs
3.  Perform prompt updates

And we require that:

-   For text + multi-modal inputs, apply all steps 1\--3.
-   For tokenized + multi-modal inputs, apply only steps 2\--3.

How can we achieve this without rewriting HF processors? We can try to call the HF processor several times on different inputs:

-   For text + multi-modal inputs, simply call the HF processor directly.
-   For tokenized + multi-modal inputs, call the processor only on the multi-modal inputs.

While HF processors support text + multi-modal inputs natively, this is not so for tokenized + multi-modal inputs: an error is thrown if the number of input placeholder tokens do not correspond to the number of multi-modal inputs.

Moreover, since the tokenized text has not passed through the HF processor, we have to apply Step 3 by ourselves to keep the output tokens and multi-modal data consistent with each other.

### Dummy text[¶](#dummy-text "Permanent link")

We work around the first issue by requiring each model to define how to generate dummy text based on the number of multi-modal inputs, via [get_dummy_text](../../api/vllm/multimodal/profiling/#vllm.multimodal.profiling.BaseDummyInputsBuilder.get_dummy_text "            get_dummy_text

  
      abstractmethod
  "). This lets us generate dummy text corresponding to the multi-modal inputs and input them together to obtain the processed multi-modal data.

### Automatic prompt updating[¶](#automatic-prompt-updating "Permanent link")

We address the second issue by implementing model-agnostic code in [\_apply_prompt_updates](../../api/vllm/multimodal/processing/#vllm.multimodal.processing.BaseMultiModalProcessor._apply_prompt_updates "            _apply_prompt_updates") to automatically update the prompt with feature placeholder tokens based on the specification outputted by [\_get_prompt_updates](../../api/vllm/multimodal/processing/#vllm.multimodal.processing.BaseMultiModalProcessor._get_prompt_updates "            _get_prompt_updates

  
      abstractmethod
  ").

### Summary[¶](#summary "Permanent link")

With the help of dummy text and automatic prompt updating, our multi-modal processor can finally accept both text and token prompts with multi-modal data. The detailed logic is shown in [\_apply_hf_processor_main](../../api/vllm/multimodal/processing/#vllm.multimodal.processing.BaseMultiModalProcessor._apply_hf_processor_main "            _apply_hf_processor_main").

## Processor Output Caching[¶](#processor-output-caching "Permanent link")

Some HF processors, such as the one for Qwen2-VL, are [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] very slow](https://github.com/vllm-project/vllm/issues/9238). To alleviate this problem, we cache the multi-modal outputs of HF processor to avoid processing the same multi-modal input (e.g. image) again.

When new data is passed in, we first check which items are in the cache, and which ones are missing. The missing items are passed into the HF processor in a single batch and cached, before being merged with the existing items in the cache.

Since we only process the missing multi-modal data items, the number of input placeholder tokens no longer corresponds to the number of the multi-modal inputs, so they can\'t be passed alongside the text prompt to HF processor. Therefore, we process the text and multi-modal inputs separately, using [dummy text](#dummy-text) to avoid HF errors. Since this skips HF\'s prompt updating code, we apply [automatic prompt updating](#automatic-prompt-updating) afterwards to keep the output tokens and multi-modal data consistent with each other.

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [October 17, 2025] ]