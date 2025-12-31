# Source: https://docs.vllm.ai/en/stable/features/quantization/gguf/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/features/quantization/gguf.md "Edit this page")

# GGUF[¶](#gguf "Permanent link")

Warning

Please note that GGUF support in vLLM is highly experimental and under-optimized at the moment, it might be incompatible with other features. Currently, you can use GGUF as a way to reduce memory footprint. If you encounter any issues, please report them to the vLLM team.

Warning

Currently, vllm only supports loading single-file GGUF models. If you have a multi-files GGUF model, you can use [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] gguf-split](https://github.com/ggerganov/llama.cpp/pull/6135) tool to merge them to a single-file model.

To run a GGUF model with vLLM, you can download and use the local GGUF model from [TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF) with the following command:

    wget https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf
    # We recommend using the tokenizer from base model to avoid long-time and buggy tokenizer conversion.
    vllm serve ./tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf \
       --tokenizer TinyLlama/TinyLlama-1.1B-Chat-v1.0

You can also add `--tensor-parallel-size 2` to enable tensor parallelism inference with 2 GPUs:

    # We recommend using the tokenizer from base model to avoid long-time and buggy tokenizer conversion.
    vllm serve ./tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf \
       --tokenizer TinyLlama/TinyLlama-1.1B-Chat-v1.0 \
       --tensor-parallel-size 2

Warning

We recommend using the tokenizer from base model instead of GGUF model. Because the tokenizer conversion from GGUF is time-consuming and unstable, especially for some models with large vocab size.

GGUF assumes that huggingface can convert the metadata to a config file. In case huggingface doesn\'t support your model you can manually create a config and pass it as hf-config-path

    # If you model is not supported by huggingface you can manually provide a huggingface compatible config path
    vllm serve ./tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf \
       --tokenizer TinyLlama/TinyLlama-1.1B-Chat-v1.0 \
       --hf-config-path Tinyllama/TInyLlama-1.1B-Chat-v1.0

You can also use the GGUF model directly through the LLM entrypoint:

Code

    from vllm import LLM, SamplingParams

    # In this script, we demonstrate how to pass input to the chat method:
    conversation = [
       ,
       ,
       ,
       ,
    ]

    # Create a sampling params object.
    sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

    # Create an LLM.
    llm = LLM(
       model="./tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
       tokenizer="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    )
    # Generate texts from the prompts. The output is a list of RequestOutput objects
    # that contain the prompt, generated text, and other information.
    outputs = llm.chat(conversation, sampling_params)

    # Print the outputs.
    for output in outputs:
       prompt = output.prompt
       generated_text = output.outputs[0].text
       print(f"Prompt: , Generated text: ")

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [October 15, 2025] ]