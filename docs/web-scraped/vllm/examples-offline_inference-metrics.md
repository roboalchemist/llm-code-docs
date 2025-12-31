# Source: https://docs.vllm.ai/en/stable/examples/offline_inference/metrics/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/offline_inference/metrics.md "Edit this page")

# Metrics[¶](#metrics "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/metrics.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project

    from vllm import LLM, SamplingParams
    from vllm.v1.metrics.reader import Counter, Gauge, Histogram, Vector

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
        llm = LLM(model="facebook/opt-125m", disable_log_stats=False)

        # Generate texts from the prompts.
        outputs = llm.generate(prompts, sampling_params)

        # Print the outputs.
        print("-" * 50)
        for output in outputs:
            prompt = output.prompt
            generated_text = output.outputs[0].text
            print(f"Prompt: \nGenerated text: ")
            print("-" * 50)

        # Dump all metrics
        for metric in llm.get_metrics():
            if isinstance(metric, Gauge):
                print(f" (gauge) = ")
            elif isinstance(metric, Counter):
                print(f" (counter) = ")
            elif isinstance(metric, Vector):
                print(f" (vector) = ")
            elif isinstance(metric, Histogram):
                print(f" (histogram)")
                print(f"    sum = ")
                print(f"    count = ")
                for bucket_le, value in metric.buckets.items():
                    print(f"     = ")

    if __name__ == "__main__":
        main()