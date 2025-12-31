# Source: https://docs.vllm.ai/en/stable/examples/pooling/token_embed/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/pooling/token_embed.md "Edit this page")

# Token Embed[¶](#token-embed "Permanent link")

Source <https://github.com/vllm-project/vllm/tree/main/examples/pooling/token_embed>.

## Jina Embeddings V4[¶](#jina-embeddings-v4 "Permanent link")

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project

    import torch

    from vllm import LLM
    from vllm.inputs.data import TextPrompt
    from vllm.multimodal.utils import fetch_image

    # Initialize model
    model = LLM(
        model="jinaai/jina-embeddings-v4-vllm-text-matching",
        runner="pooling",
        max_model_len=1024,
        gpu_memory_utilization=0.8,
    )

    # Create text prompts
    text1 = "Ein wunderschöner Sonnenuntergang am Strand"
    text1_prompt = TextPrompt(prompt=f"Query: ")

    text2 = "浜辺に沈む美しい夕日"
    text2_prompt = TextPrompt(prompt=f"Query: ")

    # Create image prompt
    image = fetch_image(
        "https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/eskimo.jpg"  # noqa: E501
    )
    image_prompt = TextPrompt(
        prompt="<|im_start|>user\n<|vision_start|><|image_pad|><|vision_end|>Describe the image.<|im_end|>\n",  # noqa: E501
        multi_modal_data=,
    )

    # Encode all prompts
    prompts = [text1_prompt, text2_prompt, image_prompt]
    outputs = model.encode(prompts, pooling_task="token_embed")

    def get_embeddings(outputs):
        VISION_START_TOKEN_ID, VISION_END_TOKEN_ID = 151652, 151653

        embeddings = []
        for output in outputs:
            if VISION_START_TOKEN_ID in output.prompt_token_ids:
                # Gather only vision tokens
                img_start_pos = torch.where(
                    torch.tensor(output.prompt_token_ids) == VISION_START_TOKEN_ID
                )[0][0]
                img_end_pos = torch.where(
                    torch.tensor(output.prompt_token_ids) == VISION_END_TOKEN_ID
                )[0][0]
                embeddings_tensor = output.outputs.data.detach().clone()[
                    img_start_pos : img_end_pos + 1
                ]
            else:
                # Use all tokens for text-only prompts
                embeddings_tensor = output.outputs.data.detach().clone()

            # Pool and normalize embeddings
            pooled_output = (
                embeddings_tensor.sum(dim=0, dtype=torch.float32)
                / embeddings_tensor.shape[0]
            )
            embeddings.append(torch.nn.functional.normalize(pooled_output, dim=-1))
        return embeddings

    embeddings = get_embeddings(outputs)

    for embedding in embeddings:
        print(embedding.shape)

## Multi Vector Retrieval[¶](#multi-vector-retrieval "Permanent link")

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
            model="BAAI/bge-m3",
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
        # You should pass runner="pooling" for embedding models
        llm = LLM(**vars(args))

        # Generate embedding. The output is a list of EmbeddingRequestOutputs.
        outputs = llm.embed(prompts)

        # Print the outputs.
        print("\nGenerated Outputs:\n" + "-" * 60)
        for prompt, output in zip(prompts, outputs):
            embeds = output.outputs.embedding
            print(len(embeds))

        # Generate embedding for each token. The output is a list of PoolingRequestOutput.
        outputs = llm.encode(prompts, pooling_task="token_embed")

        # Print the outputs.
        print("\nGenerated Outputs:\n" + "-" * 60)
        for prompt, output in zip(prompts, outputs):
            multi_vector = output.outputs.data
            print(multi_vector.shape)

    if __name__ == "__main__":
        args = parse_args()
        main(args)

## Multi Vector Retrieval Client[¶](#multi-vector-retrieval-client "Permanent link")

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project

    """
    Example online usage of Pooling API for multi vector retrieval.

    Run `vllm serve <model> --runner pooling`
    to start up the server in vLLM. e.g.

    vllm serve BAAI/bge-m3
    """

    import argparse

    import requests
    import torch

    def post_http_request(prompt: dict, api_url: str) -> requests.Response:
        headers = 
        response = requests.post(api_url, headers=headers, json=prompt)
        return response

    def parse_args():
        parser = argparse.ArgumentParser()
        parser.add_argument("--host", type=str, default="localhost")
        parser.add_argument("--port", type=int, default=8000)
        parser.add_argument("--model", type=str, default="BAAI/bge-m3")

        return parser.parse_args()

    def main(args):
        api_url = f"http://:/pooling"
        model_name = args.model

        prompts = [
            "Hello, my name is",
            "The president of the United States is",
            "The capital of France is",
            "The future of AI is",
        ]
        prompt = 

        pooling_response = post_http_request(prompt=prompt, api_url=api_url)
        for output in pooling_response.json()["data"]:
            multi_vector = torch.tensor(output["data"])
            print(multi_vector.shape)

    if __name__ == "__main__":
        args = parse_args()
        main(args)