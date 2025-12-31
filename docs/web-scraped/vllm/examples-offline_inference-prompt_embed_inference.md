# Source: https://docs.vllm.ai/en/stable/examples/offline_inference/prompt_embed_inference/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/offline_inference/prompt_embed_inference.md "Edit this page")

# Prompt Embed Inference[¶](#prompt-embed-inference "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/prompt_embed_inference.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """
    Demonstrates how to generate prompt embeddings using
    Hugging Face Transformers  and use them as input to vLLM
    for both single and batch inference.

    Model: meta-llama/Llama-3.2-1B-Instruct
    Note: This model is gated on Hugging Face Hub.
          You must request access to use it:
          https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct

    Requirements:
    - vLLM
    - transformers

    Run:
        python examples/offline_inference/prompt_embed_inference.py
    """

    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer, PreTrainedTokenizer

    from vllm import LLM

    def init_tokenizer_and_llm(model_name: str):
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        transformers_model = AutoModelForCausalLM.from_pretrained(model_name)
        embedding_layer = transformers_model.get_input_embeddings()
        llm = LLM(model=model_name, enable_prompt_embeds=True)
        return tokenizer, embedding_layer, llm

    def get_prompt_embeds(
        chat: list[dict[str, str]],
        tokenizer: PreTrainedTokenizer,
        embedding_layer: torch.nn.Module,
    ):
        token_ids = tokenizer.apply_chat_template(
            chat, add_generation_prompt=True, return_tensors="pt"
        )
        prompt_embeds = embedding_layer(token_ids).squeeze(0)
        return prompt_embeds

    def single_prompt_inference(
        llm: LLM, tokenizer: PreTrainedTokenizer, embedding_layer: torch.nn.Module
    ):
        chat = []
        prompt_embeds = get_prompt_embeds(chat, tokenizer, embedding_layer)

        outputs = llm.generate(
            
        )

        print("\n[Single Inference Output]")
        print("-" * 30)
        for o in outputs:
            print(o.outputs[0].text)
        print("-" * 30)

    def batch_prompt_inference(
        llm: LLM, tokenizer: PreTrainedTokenizer, embedding_layer: torch.nn.Module
    ):
        chats = [
            [],
            [],
            [],
        ]

        prompt_embeds_list = [
            get_prompt_embeds(chat, tokenizer, embedding_layer) for chat in chats
        ]

        outputs = llm.generate([ for embeds in prompt_embeds_list])

        print("\n[Batch Inference Outputs]")
        print("-" * 30)
        for i, o in enumerate(outputs):
            print(f"Q: ")
            print(f"A: \n")
        print("-" * 30)

    def main():
        model_name = "meta-llama/Llama-3.2-1B-Instruct"
        tokenizer, embedding_layer, llm = init_tokenizer_and_llm(model_name)
        single_prompt_inference(llm, tokenizer, embedding_layer)
        batch_prompt_inference(llm, tokenizer, embedding_layer)

    if __name__ == "__main__":
        main()