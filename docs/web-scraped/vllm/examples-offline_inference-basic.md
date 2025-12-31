# Source: https://docs.vllm.ai/en/stable/examples/offline_inference/basic/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/offline_inference/basic.md "Edit this page")

# Basic[¶](#basic "Permanent link")

Source <https://github.com/vllm-project/vllm/tree/main/examples/offline_inference/basic>.

The `LLM` class provides the primary Python interface for doing offline inference, which is interacting with a model without using a separate model inference server.

## Usage[¶](#usage "Permanent link")

The first script in this example shows the most basic usage of vLLM. If you are new to Python and vLLM, you should start here.

    python examples/offline_inference/basic/basic.py

The rest of the scripts include an [argument parser](https://docs.python.org/3/library/argparse.html), which you can use to pass any arguments that are compatible with [`LLM`](https://docs.vllm.ai/en/latest/api/offline_inference/llm.html). Try running the script with `--help` for a list of all available arguments.

    python examples/offline_inference/basic/classify.py

    python examples/offline_inference/basic/embed.py

    python examples/offline_inference/basic/score.py

The chat and generate scripts also accept the [sampling parameters](https://docs.vllm.ai/en/latest/api/inference_params.html#sampling-parameters): `max_tokens`, `temperature`, `top_p` and `top_k`.

    python examples/offline_inference/basic/chat.py

    python examples/offline_inference/basic/generate.py

## Features[¶](#features "Permanent link")

In the scripts that support passing arguments, you can experiment with the following features.

### Default generation config[¶](#default-generation-config "Permanent link")

The `--generation-config` argument specifies where the generation config will be loaded from when calling `LLM.get_default_sampling_params()`. If set to 'auto', the generation config will be loaded from model path. If set to a folder path, the generation config will be loaded from the specified folder path. If it is not provided, vLLM defaults will be used.

> If max_new_tokens is specified in generation config, then it sets a server-wide limit on the number of output tokens for all requests.

Try it yourself with the following argument:

    --generation-config auto

### Quantization[¶](#quantization "Permanent link")

#### GGUF[¶](#gguf "Permanent link")

vLLM supports models that are quantized using GGUF.

Try one yourself by downloading a quantized GGUF model and using the following arguments:

    from huggingface_hub import hf_hub_download
    repo_id = "bartowski/Phi-3-medium-4k-instruct-GGUF"
    filename = "Phi-3-medium-4k-instruct-IQ2_M.gguf"
    print(hf_hub_download(repo_id, filename=filename))

    --model  --tokenizer microsoft/Phi-3-medium-4k-instruct

### CPU offload[¶](#cpu-offload "Permanent link")

The `--cpu-offload-gb` argument can be seen as a virtual way to increase the GPU memory size. For example, if you have one 24 GB GPU and set this to 10, virtually you can think of it as a 34 GB GPU. Then you can load a 13B model with BF16 weight, which requires at least 26GB GPU memory. Note that this requires fast CPU-GPU interconnect, as part of the model is loaded from CPU memory to GPU memory on the fly in each model forward pass.

Try it yourself with the following arguments:

    --model meta-llama/Llama-2-13b-chat-hf --cpu-offload-gb 10

## Example materials[¶](#example-materials "Permanent link")

basic.py

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project

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
        llm = LLM(model="facebook/opt-125m")
        # Generate texts from the prompts.
        # The output is a list of RequestOutput objects
        # that contain the prompt, generated text, and other information.
        outputs = llm.generate(prompts, sampling_params)
        # Print the outputs.
        print("\nGenerated Outputs:\n" + "-" * 60)
        for output in outputs:
            prompt = output.prompt
            generated_text = output.outputs[0].text
            print(f"Prompt:    ")
            print(f"Output:    ")
            print("-" * 60)

    if __name__ == "__main__":
        main()

chat.py

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project

    from vllm import LLM, EngineArgs
    from vllm.utils.argparse_utils import FlexibleArgumentParser

    def create_parser():
        parser = FlexibleArgumentParser()
        # Add engine args
        EngineArgs.add_cli_args(parser)
        parser.set_defaults(model="meta-llama/Llama-3.2-1B-Instruct")
        # Add sampling params
        sampling_group = parser.add_argument_group("Sampling parameters")
        sampling_group.add_argument("--max-tokens", type=int)
        sampling_group.add_argument("--temperature", type=float)
        sampling_group.add_argument("--top-p", type=float)
        sampling_group.add_argument("--top-k", type=int)
        # Add example params
        parser.add_argument("--chat-template-path", type=str)

        return parser

    def main(args: dict):
        # Pop arguments not used by LLM
        max_tokens = args.pop("max_tokens")
        temperature = args.pop("temperature")
        top_p = args.pop("top_p")
        top_k = args.pop("top_k")
        chat_template_path = args.pop("chat_template_path")

        # Create an LLM
        llm = LLM(**args)

        # Create sampling params object
        sampling_params = llm.get_default_sampling_params()
        if max_tokens is not None:
            sampling_params.max_tokens = max_tokens
        if temperature is not None:
            sampling_params.temperature = temperature
        if top_p is not None:
            sampling_params.top_p = top_p
        if top_k is not None:
            sampling_params.top_k = top_k

        def print_outputs(outputs):
            print("\nGenerated Outputs:\n" + "-" * 80)
            for output in outputs:
                prompt = output.prompt
                generated_text = output.outputs[0].text
                print(f"Prompt: \n")
                print(f"Generated text: ")
                print("-" * 80)

        print("=" * 80)

        # In this script, we demonstrate how to pass input to the chat method:
        conversation = [
            ,
            ,
            ,
            ,
        ]
        outputs = llm.chat(conversation, sampling_params, use_tqdm=False)
        print_outputs(outputs)

        # You can run batch inference with llm.chat API
        conversations = [conversation for _ in range(10)]

        # We turn on tqdm progress bar to verify it's indeed running batch inference
        outputs = llm.chat(conversations, sampling_params, use_tqdm=True)
        print_outputs(outputs)

        # A chat template can be optionally supplied.
        # If not, the model will use its default chat template.
        if chat_template_path is not None:
            with open(chat_template_path) as f:
                chat_template = f.read()

            outputs = llm.chat(
                conversations,
                sampling_params,
                use_tqdm=False,
                chat_template=chat_template,
            )
            print_outputs(outputs)

    if __name__ == "__main__":
        parser = create_parser()
        args: dict = vars(parser.parse_args())
        main(args)

classify.py

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project

    from argparse import Namespace

    from vllm import LLM, EngineArgs
    from vllm.utils.argparse_utils import FlexibleArgumentParser

    def parse_args():
        parser = FlexibleArgumentParser()
        parser = EngineArgs.add_cli_args(parser)
        # Set example specific arguments
        parser.set_defaults(
            model="jason9693/Qwen2.5-1.5B-apeach",
            runner="pooling",
            enforce_eager=True,
        )
        return parser.parse_args()

    def main(args: Namespace):
        # Sample prompts.
        prompts = [
            "Hello, my name is",
            "The president of the United States is",
            "The capital of France is",
            "The future of AI is",
        ]

        # Create an LLM.
        # You should pass runner="pooling" for classification models
        llm = LLM(**vars(args))

        # Generate logits. The output is a list of ClassificationRequestOutputs.
        outputs = llm.classify(prompts)

        # Print the outputs.
        print("\nGenerated Outputs:\n" + "-" * 60)
        for prompt, output in zip(prompts, outputs):
            probs = output.outputs.probs
            probs_trimmed = (str(probs[:16])[:-1] + ", ...]") if len(probs) > 16 else probs
            print(
                f"Prompt:  \n"
                f"Class Probabilities:  (size=)"
            )
            print("-" * 60)

    if __name__ == "__main__":
        args = parse_args()
        main(args)

embed.py

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project

    from argparse import Namespace

    from vllm import LLM, EngineArgs
    from vllm.attention.backends.registry import AttentionBackendEnum
    from vllm.config import AttentionConfig
    from vllm.platforms import current_platform
    from vllm.utils.argparse_utils import FlexibleArgumentParser

    def parse_args():
        parser = FlexibleArgumentParser()
        parser = EngineArgs.add_cli_args(parser)
        # Set example specific arguments
        parser.set_defaults(
            model="intfloat/e5-small",
            runner="pooling",
            enforce_eager=True,
        )
        return parser.parse_args()

    def main(args: Namespace):
        if current_platform.is_rocm():
            args.attention_config = AttentionConfig(
                backend=AttentionBackendEnum.FLEX_ATTENTION
            )

        # Sample prompts.
        prompts = [
            "Hello, my name is",
            "The president of the United States is",
            "The capital of France is",
            "The future of AI is",
        ]

        # Create an LLM.
        # You should pass runner="pooling" for embedding models
        llm = LLM(**vars(args))

        # Generate embedding. The output is a list of EmbeddingRequestOutputs.
        outputs = llm.embed(prompts)

        # Print the outputs.
        print("\nGenerated Outputs:\n" + "-" * 60)
        for prompt, output in zip(prompts, outputs):
            embeds = output.outputs.embedding
            embeds_trimmed = (
                (str(embeds[:16])[:-1] + ", ...]") if len(embeds) > 16 else embeds
            )
            print(f"Prompt:  \nEmbeddings:  (size=)")
            print("-" * 60)

    if __name__ == "__main__":
        args = parse_args()
        main(args)

generate.py

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project

    from vllm import LLM, EngineArgs
    from vllm.utils.argparse_utils import FlexibleArgumentParser

    def create_parser():
        parser = FlexibleArgumentParser()
        # Add engine args
        EngineArgs.add_cli_args(parser)
        parser.set_defaults(model="meta-llama/Llama-3.2-1B-Instruct")
        # Add sampling params
        sampling_group = parser.add_argument_group("Sampling parameters")
        sampling_group.add_argument("--max-tokens", type=int)
        sampling_group.add_argument("--temperature", type=float)
        sampling_group.add_argument("--top-p", type=float)
        sampling_group.add_argument("--top-k", type=int)

        return parser

    def main(args: dict):
        # Pop arguments not used by LLM
        max_tokens = args.pop("max_tokens")
        temperature = args.pop("temperature")
        top_p = args.pop("top_p")
        top_k = args.pop("top_k")

        # Create an LLM
        llm = LLM(**args)

        # Create a sampling params object
        sampling_params = llm.get_default_sampling_params()
        if max_tokens is not None:
            sampling_params.max_tokens = max_tokens
        if temperature is not None:
            sampling_params.temperature = temperature
        if top_p is not None:
            sampling_params.top_p = top_p
        if top_k is not None:
            sampling_params.top_k = top_k

        # Generate texts from the prompts. The output is a list of RequestOutput
        # objects that contain the prompt, generated text, and other information.
        prompts = [
            "Hello, my name is",
            "The president of the United States is",
            "The capital of France is",
            "The future of AI is",
        ]
        outputs = llm.generate(prompts, sampling_params)
        # Print the outputs.
        print("-" * 50)
        for output in outputs:
            prompt = output.prompt
            generated_text = output.outputs[0].text
            print(f"Prompt: \nGenerated text: ")
            print("-" * 50)

    if __name__ == "__main__":
        parser = create_parser()
        args: dict = vars(parser.parse_args())
        main(args)

reward.py

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project

    from argparse import Namespace

    from vllm import LLM, EngineArgs
    from vllm.utils.argparse_utils import FlexibleArgumentParser

    def parse_args():
        parser = FlexibleArgumentParser()
        parser = EngineArgs.add_cli_args(parser)
        # Set example specific arguments
        parser.set_defaults(
            model="internlm/internlm2-1_8b-reward",
            runner="pooling",
            enforce_eager=True,
            max_model_len=1024,
            trust_remote_code=True,
        )
        return parser.parse_args()

    def main(args: Namespace):
        # Sample prompts.
        prompts = [
            "Hello, my name is",
            "The president of the United States is",
            "The capital of France is",
            "The future of AI is",
        ]

        # Create an LLM.
        # You should pass runner="pooling" for reward models
        llm = LLM(**vars(args))

        # Generate rewards. The output is a list of PoolingRequestOutput.
        outputs = llm.reward(prompts)

        # Print the outputs.
        print("\nGenerated Outputs:\n" + "-" * 60)
        for prompt, output in zip(prompts, outputs):
            rewards = output.outputs.data
            rewards_trimmed = (
                (str(rewards[:16])[:-1] + ", ...]") if len(rewards) > 16 else rewards
            )
            print(f"Prompt:  \nReward:  (size=)")
            print("-" * 60)

    if __name__ == "__main__":
        args = parse_args()
        main(args)

score.py

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project

    from argparse import Namespace

    from vllm import LLM, EngineArgs
    from vllm.attention.backends.registry import AttentionBackendEnum
    from vllm.config import AttentionConfig
    from vllm.platforms import current_platform
    from vllm.utils.argparse_utils import FlexibleArgumentParser

    def parse_args():
        parser = FlexibleArgumentParser()
        parser = EngineArgs.add_cli_args(parser)
        # Set example specific arguments
        parser.set_defaults(
            model="BAAI/bge-reranker-v2-m3",
            runner="pooling",
            enforce_eager=True,
        )
        return parser.parse_args()

    def main(args: Namespace):
        if current_platform.is_rocm():
            args.attention_config = AttentionConfig(
                backend=AttentionBackendEnum.FLEX_ATTENTION
            )

        # Sample prompts.
        text_1 = "What is the capital of France?"
        texts_2 = [
            "The capital of Brazil is Brasilia.",
            "The capital of France is Paris.",
        ]

        # Create an LLM.
        # You should pass runner="pooling" for cross-encoder models
        llm = LLM(**vars(args))

        # Generate scores. The output is a list of ScoringRequestOutputs.
        outputs = llm.score(text_1, texts_2)

        # Print the outputs.
        print("\nGenerated Outputs:\n" + "-" * 60)
        for text_2, output in zip(texts_2, outputs):
            score = output.outputs.score
            print(f"Pair:  \nScore: ")
            print("-" * 60)

    if __name__ == "__main__":
        args = parse_args()
        main(args)