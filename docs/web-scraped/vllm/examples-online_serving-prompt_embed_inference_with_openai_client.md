# Source: https://docs.vllm.ai/en/stable/examples/online_serving/prompt_embed_inference_with_openai_client/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/prompt_embed_inference_with_openai_client.md "Edit this page")

# Prompt Embed Inference With OpenAI Client[¶](#prompt-embed-inference-with-openai-client "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/online_serving/prompt_embed_inference_with_openai_client.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """
    vLLM OpenAI-Compatible Client with Prompt Embeddings

    This script demonstrates how to:
    1. Generate prompt embeddings using Hugging Face Transformers
    2. Encode them in base64 format
    3. Send them to a vLLM server via the OpenAI-compatible Completions API

    Run the vLLM server first:
    vllm serve meta-llama/Llama-3.2-1B-Instruct \
      --runner generate \
      --max-model-len 4096 \
      --enable-prompt-embeds

    Run the client:
    python examples/online_serving/prompt_embed_inference_with_openai_client.py

    Model: meta-llama/Llama-3.2-1B-Instruct
    Note: This model is gated on Hugging Face Hub.
          You must request access to use it:
          https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct

    Dependencies:
    - transformers
    - torch
    - openai
    """

    import transformers
    from openai import OpenAI

    from vllm.utils.serial_utils import tensor2base64

    def main():
        client = OpenAI(
            api_key="EMPTY",
            base_url="http://localhost:8000/v1",
        )

        model_name = "meta-llama/Llama-3.2-1B-Instruct"

        # Transformers
        tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
        transformers_model = transformers.AutoModelForCausalLM.from_pretrained(model_name)

        # Refer to the HuggingFace repo for the correct format to use
        chat = []
        token_ids = tokenizer.apply_chat_template(
            chat, add_generation_prompt=True, return_tensors="pt"
        )

        embedding_layer = transformers_model.get_input_embeddings()
        prompt_embeds = embedding_layer(token_ids).squeeze(0)

        # Prompt embeddings
        encoded_embeds = tensor2base64(prompt_embeds)

        completion = client.completions.create(
            model=model_name,
            # NOTE: The OpenAI client does not allow `None` as an input to
            # `prompt`. Use an empty string if you have no text prompts.
            prompt="",
            max_tokens=5,
            temperature=0.0,
            # NOTE: The OpenAI client allows passing in extra JSON body via the
            # `extra_body` argument.
            extra_body=,
        )

        print("-" * 30)
        print(completion.choices[0].text)
        print("-" * 30)

    if __name__ == "__main__":
        main()