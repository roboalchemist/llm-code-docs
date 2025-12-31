# Source: https://docs.vllm.ai/en/stable/examples/offline_inference/simple_profiling/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/offline_inference/simple_profiling.md "Edit this page")

# Simple Profiling[¶](#simple-profiling "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/simple_profiling.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project

    import time

    from vllm import LLM, SamplingParams

    # Sample prompts.
    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        "The capital of France is",
        "The future of AI is",
    ]
    # Create a sampling params object.
    sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

    def main():
        # Create an LLM.
        llm = LLM(
            model="facebook/opt-125m",
            tensor_parallel_size=1,
            profiler_config=,
        )

        llm.start_profile()

        # Generate texts from the prompts. The output is a list of RequestOutput
        # objects that contain the prompt, generated text, and other information.
        outputs = llm.generate(prompts, sampling_params)

        llm.stop_profile()

        # Print the outputs.
        print("-" * 50)
        for output in outputs:
            prompt = output.prompt
            generated_text = output.outputs[0].text
            print(f"Prompt: \nGenerated text: ")
            print("-" * 50)

        # Add a buffer to wait for profiler in the background process
        # (in case MP is on) to finish writing profiling output.
        time.sleep(10)

    if __name__ == "__main__":
        main()