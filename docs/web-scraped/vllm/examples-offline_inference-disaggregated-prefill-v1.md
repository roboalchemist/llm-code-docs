# Source: https://docs.vllm.ai/en/stable/examples/offline_inference/disaggregated-prefill-v1/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/offline_inference/disaggregated-prefill-v1.md "Edit this page")

# Disaggregated Prefill V1[¶](#disaggregated-prefill-v1 "Permanent link")

Source <https://github.com/vllm-project/vllm/tree/main/examples/offline_inference/disaggregated-prefill-v1>.

This example contains scripts that demonstrate disaggregated prefill in the offline setting of vLLM.

## Files[¶](#files "Permanent link")

-   `run.sh` - A helper script that will run `prefill_example.py` and `decode_example.py` sequentially.
    -   Make sure you are in the `examples/offline_inference/disaggregated-prefill-v1` directory before running `run.sh`.
-   `prefill_example.py` - A script which performs prefill only, saving the KV state to the `local_storage` directory and the prompts to `output.txt`.
-   `decode_example.py` - A script which performs decode only, loading the KV state from the `local_storage` directory and the prompts from `output.txt`.

## Example materials[¶](#example-materials "Permanent link")

decode_example.py

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project

    from vllm import LLM, SamplingParams
    from vllm.config import KVTransferConfig

    def read_prompts():
        """Read prompts from output.txt"""
        prompts = []
        try:
            with open("output.txt") as f:
                for line in f:
                    prompts.append(line.strip())
            print(f"Loaded  prompts from output.txt")
            return prompts
        except FileNotFoundError:
            print("Error: output.txt file not found")
            exit(-1)

    def main():
        prompts = read_prompts()
        sampling_params = SamplingParams(temperature=0, top_p=0.95, max_tokens=10)

        llm = LLM(
            model="meta-llama/Llama-3.2-1B-Instruct",
            enforce_eager=True,
            gpu_memory_utilization=0.8,
            max_num_batched_tokens=64,
            max_num_seqs=16,
            kv_transfer_config=KVTransferConfig(
                kv_connector="ExampleConnector",
                kv_role="kv_both",
                kv_connector_extra_config=,
            ),
        )  # , max_model_len=2048, max_num_batched_tokens=2048)

        # 1ST generation (prefill instance)
        outputs = llm.generate(prompts, sampling_params)

        print("-" * 30)
        for output in outputs:
            prompt = output.prompt
            generated_text = output.outputs[0].text
            print(f"Prompt: \nGenerated text: ")
            print("-" * 30)

    if __name__ == "__main__":
        main()

prefill_example.py

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project

    from vllm import LLM, SamplingParams
    from vllm.config import KVTransferConfig

    def read_prompts():
        context = "Hi " * 1000
        context2 = "Hey " * 500
        return [
            context + "Hello, my name is",
            context + "The capital of France is",
            context2 + "Your name is",
            context2 + "The capital of China is",
        ]

    def main():
        prompts = read_prompts()

        sampling_params = SamplingParams(temperature=0, top_p=0.95, max_tokens=1)

        llm = LLM(
            model="meta-llama/Llama-3.2-1B-Instruct",
            enforce_eager=True,
            gpu_memory_utilization=0.8,
            kv_transfer_config=KVTransferConfig(
                kv_connector="ExampleConnector",
                kv_role="kv_both",
                kv_connector_extra_config=,
            ),
        )  # , max_model_len=2048, max_num_batched_tokens=2048)

        # 1ST generation (prefill instance)
        outputs = llm.generate(
            prompts,
            sampling_params,
        )

        new_prompts = []
        print("-" * 30)
        for output in outputs:
            prompt = output.prompt
            generated_text = output.outputs[0].text
            new_prompts.append(prompt + generated_text)
            print(f"Prompt: \nGenerated text: ")
            print("-" * 30)

        # Write new_prompts to output.txt
        with open("output.txt", "w") as f:
            for prompt in new_prompts:
                f.write(prompt + "\n")
        print(f"Saved  prompts to output.txt")

    if __name__ == "__main__":
        main()

run.sh

    rm -rf local_storage/

    if [ -f "output.txt" ]; then
        rm output.txt
    fi

    # The directory of current script
    SCRIPT_DIR=$(dirname "$(readlink -f "$0")")

    VLLM_ENABLE_V1_MULTIPROCESSING=0 CUDA_VISIBLE_DEVICES=0 python3 "$SCRIPT_DIR/prefill_example.py"
    VLLM_ENABLE_V1_MULTIPROCESSING=0 CUDA_VISIBLE_DEVICES=0 python3 "$SCRIPT_DIR/decode_example.py"