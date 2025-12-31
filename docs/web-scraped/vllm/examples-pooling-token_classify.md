# Source: https://docs.vllm.ai/en/stable/examples/pooling/token_classify/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/pooling/token_classify.md "Edit this page")

# Token Classify[¶](#token-classify "Permanent link")

Source <https://github.com/vllm-project/vllm/tree/main/examples/pooling/token_classify>.

## NER[¶](#ner "Permanent link")

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    # Adapted from https://huggingface.co/boltuix/NeuroBERT-NER

    from argparse import Namespace

    from vllm import LLM, EngineArgs
    from vllm.utils.argparse_utils import FlexibleArgumentParser

    def parse_args():
        parser = FlexibleArgumentParser()
        parser = EngineArgs.add_cli_args(parser)
        # Set example specific arguments
        parser.set_defaults(
            model="boltuix/NeuroBERT-NER",
            runner="pooling",
            enforce_eager=True,
            trust_remote_code=True,
        )
        return parser.parse_args()

    def main(args: Namespace):
        # Sample prompts.
        prompts = [
            "Barack Obama visited Microsoft headquarters in Seattle on January 2025."
        ]

        # Create an LLM.
        llm = LLM(**vars(args))
        tokenizer = llm.get_tokenizer()
        label_map = llm.llm_engine.vllm_config.model_config.hf_config.id2label

        # Run inference
        outputs = llm.encode(prompts, pooling_task="token_classify")

        for prompt, output in zip(prompts, outputs):
            logits = output.outputs.data
            predictions = logits.argmax(dim=-1)

            # Map predictions to labels
            tokens = tokenizer.convert_ids_to_tokens(output.prompt_token_ids)
            labels = [label_map[p.item()] for p in predictions]

            # Print results
            for token, label in zip(tokens, labels):
                if token not in tokenizer.all_special_tokens:
                    print(f" → ")

    if __name__ == "__main__":
        args = parse_args()
        main(args)

## NER Client[¶](#ner-client "Permanent link")

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    # Adapted from https://huggingface.co/boltuix/NeuroBERT-NER

    """
    Example online usage of Pooling API for Named Entity Recognition (NER).

    Run `vllm serve <model> --runner pooling`
    to start up the server in vLLM. e.g.

    vllm serve boltuix/NeuroBERT-NER
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
        parser.add_argument("--model", type=str, default="boltuix/NeuroBERT-NER")

        return parser.parse_args()

    def main(args):
        from transformers import AutoConfig, AutoTokenizer

        api_url = f"http://:/pooling"
        model_name = args.model

        # Load tokenizer and config
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        config = AutoConfig.from_pretrained(model_name)
        label_map = config.id2label

        # Input text
        text = "Barack Obama visited Microsoft headquarters in Seattle on January 2025."
        prompt = 

        pooling_response = post_http_request(prompt=prompt, api_url=api_url)

        # Run inference
        output = pooling_response.json()["data"][0]
        logits = torch.tensor(output["data"])
        predictions = logits.argmax(dim=-1)
        inputs = tokenizer(text, return_tensors="pt")

        # Map predictions to labels
        tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
        labels = [label_map[p.item()] for p in predictions]
        assert len(tokens) == len(predictions)

        # Print results
        for token, label in zip(tokens, labels):
            if token not in tokenizer.all_special_tokens:
                print(f" → ")

    if __name__ == "__main__":
        args = parse_args()
        main(args)