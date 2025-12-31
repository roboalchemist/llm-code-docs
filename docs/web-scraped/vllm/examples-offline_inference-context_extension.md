# Source: https://docs.vllm.ai/en/stable/examples/offline_inference/context_extension/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/offline_inference/context_extension.md "Edit this page")

# Context Extension[¶](#context-extension "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/context_extension.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """
    This script demonstrates how to extend the context length
    of a Qwen model using the YARN method (rope_parameters)
    and run a simple chat example.

    Usage:
        python examples/offline_inference/context_extension.py
    """

    from vllm import LLM, SamplingParams

    def create_llm():
        rope_theta = 1000000
        original_max_position_embeddings = 32768
        factor = 4.0

        # Use yarn to extend context
        hf_overrides = ,
            "max_model_len": int(original_max_position_embeddings * factor),
        }

        llm = LLM(model="Qwen/Qwen3-0.6B", hf_overrides=hf_overrides)
        return llm

    def run_llm_chat(llm):
        sampling_params = SamplingParams(
            temperature=0.8,
            top_p=0.95,
            max_tokens=128,
        )

        conversation = [
            ,
            ,
            ,
        ]
        outputs = llm.chat(conversation, sampling_params, use_tqdm=False)
        return outputs

    def print_outputs(outputs):
        print("\nGenerated Outputs:\n" + "-" * 80)
        for output in outputs:
            prompt = output.prompt
            generated_text = output.outputs[0].text
            print(f"Prompt: \n")
            print(f"Generated text: ")
            print("-" * 80)

    def main():
        llm = create_llm()
        outputs = run_llm_chat(llm)
        print_outputs(outputs)

    if __name__ == "__main__":
        main()