# Source: https://docs.vllm.ai/en/stable/models/generative_models/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/models/generative_models.md "Edit this page")

# Generative Models[¶](#generative-models "Permanent link")

vLLM provides first-class support for generative models, which covers most of LLMs.

In vLLM, generative models implement the[VllmModelForTextGeneration](../../api/vllm/model_executor/models/#vllm.model_executor.models.VllmModelForTextGeneration "            VllmModelForTextGeneration") interface. Based on the final hidden states of the input, these models output log probabilities of the tokens to generate, which are then passed through [Sampler](../../api/vllm/v1/sample/sampler/#vllm.v1.sample.sampler.Sampler "            Sampler") to obtain the final text.

## Configuration[¶](#configuration "Permanent link")

### Model Runner (`--runner`)[¶](#model-runner-runner "Permanent link") 

Run a model in generation mode via the option `--runner generate`.

Tip

There is no need to set this option in the vast majority of cases as vLLM can automatically detect the model runner to use via `--runner auto`.

## Offline Inference[¶](#offline-inference "Permanent link")

The [LLM](../../api/vllm/#vllm.LLM "            LLM") class provides various methods for offline inference. See [configuration](../../api/#configuration) for a list of options when initializing the model.

### `LLM.generate`[¶](#llmgenerate "Permanent link") 

The [generate](../../api/vllm/#vllm.LLM.generate "            generate") method is available to all generative models in vLLM. It is similar to [its counterpart in HF Transformers](https://huggingface.co/docs/transformers/main/en/main_classes/text_generation#transformers.GenerationMixin.generate), except that tokenization and detokenization are also performed automatically.

    from vllm import LLM

    llm = LLM(model="facebook/opt-125m")
    outputs = llm.generate("Hello, my name is")

    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: , Generated text: ")

You can optionally control the language generation by passing [SamplingParams](../../api/vllm/#vllm.SamplingParams "            SamplingParams"). For example, you can use greedy sampling by setting `temperature=0`:

    from vllm import LLM, SamplingParams

    llm = LLM(model="facebook/opt-125m")
    params = SamplingParams(temperature=0)
    outputs = llm.generate("Hello, my name is", params)

    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: , Generated text: ")

Important

By default, vLLM will use sampling parameters recommended by model creator by applying the `generation_config.json` from the huggingface model repository if it exists. In most cases, this will provide you with the best results by default if [SamplingParams](../../api/vllm/#vllm.SamplingParams "            SamplingParams") is not specified.

However, if vLLM\'s default sampling parameters are preferred, please pass `generation_config="vllm"` when creating the [LLM](../../api/vllm/#vllm.LLM "            LLM") instance.

A code example can be found here: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/offline_inference/basic/basic.py](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/basic/basic.py)

### `LLM.beam_search`[¶](#llmbeam_search "Permanent link") 

The [beam_search](../../api/vllm/#vllm.LLM.beam_search "            beam_search") method implements [beam search](https://huggingface.co/docs/transformers/en/generation_strategies#beam-search) on top of [generate](../../api/vllm/#vllm.LLM.generate "            generate"). For example, to search using 5 beams and output at most 50 tokens:

    from vllm import LLM
    from vllm.sampling_params import BeamSearchParams

    llm = LLM(model="facebook/opt-125m")
    params = BeamSearchParams(beam_width=5, max_tokens=50)
    outputs = llm.beam_search([], params)

    for output in outputs:
        generated_text = output.sequences[0].text
        print(f"Generated text: ")

### `LLM.chat`[¶](#llmchat "Permanent link") 

The [chat](../../api/vllm/#vllm.LLM.chat "            chat") method implements chat functionality on top of [generate](../../api/vllm/#vllm.LLM.generate "            generate"). In particular, it accepts input similar to [OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat) and automatically applies the model\'s [chat template](https://huggingface.co/docs/transformers/en/chat_templating) to format the prompt.

Important

In general, only instruction-tuned models have a chat template. Base models may perform poorly as they are not trained to respond to the chat conversation.

Code

    from vllm import LLM

    llm = LLM(model="meta-llama/Meta-Llama-3-8B-Instruct")
    conversation = [
        ,
        ,
        ,
        ,
    ]
    outputs = llm.chat(conversation)

    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: , Generated text: ")

A code example can be found here: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/offline_inference/basic/chat.py](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/basic/chat.py)

If the model doesn\'t have a chat template or you want to specify another one, you can explicitly pass a chat template:

    from vllm.entrypoints.chat_utils import load_chat_template

    # You can find a list of existing chat templates under `examples/`
    custom_template = load_chat_template(chat_template="<path_to_template>")
    print("Loaded chat template:", custom_template)

    outputs = llm.chat(conversation, chat_template=custom_template)

## Online Serving[¶](#online-serving "Permanent link")

Our [OpenAI-Compatible Server](../../serving/openai_compatible_server/) provides endpoints that correspond to the offline APIs:

-   [Completions API](../../serving/openai_compatible_server/#completions-api) is similar to `LLM.generate` but only accepts text.
-   [Chat API](../../serving/openai_compatible_server/#chat-api) is similar to `LLM.chat`, accepting both text and [multi-modal inputs](../../features/multimodal_inputs/) for models with a chat template.

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [October 17, 2025] ]