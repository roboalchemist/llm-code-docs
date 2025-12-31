# Source: https://docs.vllm.ai/en/stable/examples/offline_inference/qwen_1m/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/offline_inference/qwen_1m.md "Edit this page")

# Qwen 1M[¶](#qwen-1m "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/qwen_1m.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    import os
    from urllib.request import urlopen

    from vllm import LLM, SamplingParams

    os.environ["VLLM_ALLOW_LONG_MAX_MODEL_LEN"] = "1"

    def load_prompt() -> str:
        # Test cases with various lengths can be found at:
        #
        # https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5-1M/test-data/64k.txt
        # https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5-1M/test-data/200k.txt
        # https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5-1M/test-data/600k.txt
        # https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5-1M/test-data/1m.txt

        with urlopen(
            "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5-1M/test-data/600k.txt",
            timeout=5,
        ) as response:
            prompt = response.read().decode("utf-8")
        return prompt

    # Processing the prompt.
    def process_requests(llm: LLM, prompts: list[str]) -> None:
        # Create a sampling params object.
        sampling_params = SamplingParams(
            temperature=0.7,
            top_p=0.8,
            top_k=20,
            repetition_penalty=1.05,
            detokenize=True,
            max_tokens=256,
        )
        # Generate texts from the prompts.
        outputs = llm.generate(prompts, sampling_params)
        # Print the outputs.
        for output in outputs:
            prompt_token_ids = output.prompt_token_ids
            generated_text = output.outputs[0].text
            print(
                f"Prompt length: , "
                f"Generated text: "
            )

    # Create an LLM.
    def initialize_engine() -> LLM:
        llm = LLM(
            model="Qwen/Qwen2.5-7B-Instruct-1M",
            max_model_len=1048576,
            tensor_parallel_size=4,
            enforce_eager=True,
            enable_chunked_prefill=True,
            max_num_batched_tokens=131072,
        )
        return llm

    def main():
        llm = initialize_engine()
        prompt = load_prompt()
        process_requests(llm, [prompt])

    if __name__ == "__main__":
        main()