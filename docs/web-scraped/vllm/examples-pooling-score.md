# Source: https://docs.vllm.ai/en/stable/examples/pooling/score/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/pooling/score.md "Edit this page")

# Score[¶](#score "Permanent link")

Source <https://github.com/vllm-project/vllm/tree/main/examples/pooling/score>.

## Cohere Rerank Client[¶](#cohere-rerank-client "Permanent link")

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """
    Example of using the OpenAI entrypoint's rerank API which is compatible with
    the Cohere SDK: https://github.com/cohere-ai/cohere-python
    Note that `pip install cohere` is needed to run this example.

    run: vllm serve BAAI/bge-reranker-base
    """

    import cohere
    from cohere import Client, ClientV2

    model = "BAAI/bge-reranker-base"

    query = "What is the capital of France?"

    documents = [
        "The capital of France is Paris",
        "Reranking is fun!",
        "vLLM is an open-source framework for fast AI serving",
    ]

    def cohere_rerank(
        client: Client | ClientV2, model: str, query: str, documents: list[str]
    ) -> dict:
        return client.rerank(model=model, query=query, documents=documents)

    def main():
        # cohere v1 client
        cohere_v1 = cohere.Client(base_url="http://localhost:8000", api_key="sk-fake-key")
        rerank_v1_result = cohere_rerank(cohere_v1, model, query, documents)
        print("-" * 50)
        print("rerank_v1_result:\n", rerank_v1_result)
        print("-" * 50)

        # or the v2
        cohere_v2 = cohere.ClientV2("sk-fake-key", base_url="http://localhost:8000")
        rerank_v2_result = cohere_rerank(cohere_v2, model, query, documents)
        print("rerank_v2_result:\n", rerank_v2_result)
        print("-" * 50)

    if __name__ == "__main__":
        main()

## Convert Model To Seq Cls[¶](#convert-model-to-seq-cls "Permanent link")

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    # ruff: noqa: E501

    import argparse
    import json

    import torch
    import transformers

    # Usage:
    # for BAAI/bge-reranker-v2-gemma
    # Caution: "Yes" and "yes" are two different tokens
    # python convert_model_to_seq_cls.py --model_name BAAI/bge-reranker-v2-gemma --classifier_from_tokens '["Yes"]' --method no_post_processing --path ./bge-reranker-v2-gemma-seq-cls
    # for mxbai-rerank-v2
    # python convert_model_to_seq_cls.py --model_name mixedbread-ai/mxbai-rerank-base-v2 --classifier_from_tokens '["0", "1"]' --method from_2_way_softmax --path ./mxbai-rerank-base-v2-seq-cls
    # for Qwen3-Reranker
    # python convert_model_to_seq_cls.py --model_name Qwen/Qwen3-Reranker-0.6B --classifier_from_tokens '["no", "yes"]' --method from_2_way_softmax --path ./Qwen3-Reranker-0.6B-seq-cls

    def from_2_way_softmax(causal_lm, seq_cls_model, tokenizer, tokens, device):
        # refer to https://huggingface.co/Qwen/Qwen3-Reranker-0.6B/discussions/3
        assert len(tokens) == 2

        lm_head_weights = causal_lm.lm_head.weight

        false_id = tokenizer.convert_tokens_to_ids(tokens[0])
        true_id = tokenizer.convert_tokens_to_ids(tokens[1])

        score_weight = lm_head_weights[true_id].to(device).to(
            torch.float32
        ) - lm_head_weights[false_id].to(device).to(torch.float32)

        with torch.no_grad():
            seq_cls_model.score.weight.copy_(score_weight.unsqueeze(0))
            if seq_cls_model.score.bias is not None:
                seq_cls_model.score.bias.zero_()

    def no_post_processing(causal_lm, seq_cls_model, tokenizer, tokens, device):
        lm_head_weights = causal_lm.lm_head.weight

        token_ids = [tokenizer.convert_tokens_to_ids(t) for t in tokens]

        score_weight = lm_head_weights[token_ids].to(device)

        with torch.no_grad():
            seq_cls_model.score.weight.copy_(score_weight)
            if seq_cls_model.score.bias is not None:
                seq_cls_model.score.bias.zero_()

    method_map = 

    def converting(
        model_name, classifier_from_tokens, path, method, use_pad_token=False, device="cpu"
    ):
        assert method in method_map

        if method == "from_2_way_softmax":
            assert len(classifier_from_tokens) == 2
            num_labels = 1
        else:
            num_labels = len(classifier_from_tokens)

        tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
        causal_lm = transformers.AutoModelForCausalLM.from_pretrained(
            model_name, device_map=device
        )

        seq_cls_model = transformers.AutoModelForSequenceClassification.from_pretrained(
            model_name,
            num_labels=num_labels,
            ignore_mismatched_sizes=True,
            device_map=device,
        )

        method_map[method](
            causal_lm, seq_cls_model, tokenizer, classifier_from_tokens, device
        )

        # `llm as reranker` defaults to not using pad_token
        seq_cls_model.config.use_pad_token = use_pad_token
        seq_cls_model.config.pad_token_id = tokenizer.pad_token_id

        seq_cls_model.save_pretrained(path)
        tokenizer.save_pretrained(path)

    def parse_args():
        parser = argparse.ArgumentParser(
            description="Converting *ForCausalLM models to "
            "*ForSequenceClassification models."
        )
        parser.add_argument(
            "--model_name",
            type=str,
            default="BAAI/bge-reranker-v2-gemma",
            help="Model name",
        )
        parser.add_argument(
            "--classifier_from_tokens",
            type=str,
            default='["Yes"]',
            help="classifier from tokens",
        )
        parser.add_argument(
            "--method", type=str, default="no_post_processing", help="Converting converting"
        )
        parser.add_argument(
            "--use-pad-token", action="store_true", help="Whether to use pad_token"
        )
        parser.add_argument(
            "--path",
            type=str,
            default="./bge-reranker-v2-gemma-seq-cls",
            help="Path to save converted model",
        )
        return parser.parse_args()

    if __name__ == "__main__":
        args = parse_args()

        converting(
            model_name=args.model_name,
            classifier_from_tokens=json.loads(args.classifier_from_tokens),
            method=args.method,
            use_pad_token=args.use_pad_token,
            path=args.path,
        )

## Offline Reranker[¶](#offline-reranker "Permanent link")

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    # ruff: noqa: E501

    from vllm import LLM

    model_name = "Qwen/Qwen3-Reranker-0.6B"

    # What is the difference between the official original version and one
    # that has been converted into a sequence classification model?
    # Qwen3-Reranker is a language model that doing reranker by using the
    # logits of "no" and "yes" tokens.
    # It needs to computing 151669 tokens logits, making this method extremely
    # inefficient, not to mention incompatible with the vllm score API.
    # A method for converting the original model into a sequence classification
    # model was proposed. See：https://huggingface.co/Qwen/Qwen3-Reranker-0.6B/discussions/3
    # Models converted offline using this method can not only be more efficient
    # and support the vllm score API, but also make the init parameters more
    # concise, for example.
    # llm = LLM(model="tomaarsen/Qwen3-Reranker-0.6B-seq-cls", runner="pooling")

    # If you want to load the official original version, the init parameters are
    # as follows.

    def get_llm() -> LLM:
        """Initializes and returns the LLM model for Qwen3-Reranker."""
        return LLM(
            model=model_name,
            runner="pooling",
            hf_overrides=,
        )

    # Why do we need hf_overrides for the official original version:
    # vllm converts it to Qwen3ForSequenceClassification when loaded for
    # better performance.
    # - Firstly, we need using `"architectures": ["Qwen3ForSequenceClassification"],`
    # to manually route to Qwen3ForSequenceClassification.
    # - Then, we will extract the vector corresponding to classifier_from_token
    # from lm_head using `"classifier_from_token": ["no", "yes"]`.
    # - Third, we will convert these two vectors into one vector.  The use of
    # conversion logic is controlled by `using "is_original_qwen3_reranker": True`.

    # Please use the query_template and document_template to format the query and
    # document for better reranker results.

    prefix = '<|im_start|>system\nJudge whether the Document meets the requirements based on the Query and the Instruct provided. Note that the answer can only be "yes" or "no".<|im_end|>\n<|im_start|>user\n'
    suffix = "<|im_end|>\n<|im_start|>assistant\n<think>\n\n</think>\n\n"

    query_template = "<Instruct>: \n<Query>: \n"
    document_template = "<Document>: "

    def main() -> None:
        instruction = (
            "Given a web search query, retrieve relevant passages that answer the query"
        )

        queries = [
            "What is the capital of China?",
            "Explain gravity",
        ]

        documents = [
            "The capital of China is Beijing.",
            "Gravity is a force that attracts two bodies towards each other. It gives weight to physical objects and is responsible for the movement of planets around the sun.",
        ]

        queries = [
            query_template.format(prefix=prefix, instruction=instruction, query=query)
            for query in queries
        ]
        documents = [document_template.format(doc=doc, suffix=suffix) for doc in documents]

        llm = get_llm()
        outputs = llm.score(queries, documents)

        print("-" * 30)
        print([output.outputs.score for output in outputs])
        print("-" * 30)

    if __name__ == "__main__":
        main()

## OpenAI Cross Encoder Score[¶](#openai-cross-encoder-score "Permanent link")

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """
    Example online usage of Score API.

    Run `vllm serve <model> --runner pooling` to start up the server in vLLM.
    """

    import argparse
    import pprint

    import requests

    def post_http_request(prompt: dict, api_url: str) -> requests.Response:
        headers = 
        response = requests.post(api_url, headers=headers, json=prompt)
        return response

    def parse_args():
        parser = argparse.ArgumentParser()
        parser.add_argument("--host", type=str, default="localhost")
        parser.add_argument("--port", type=int, default=8000)
        parser.add_argument("--model", type=str, default="BAAI/bge-reranker-v2-m3")
        return parser.parse_args()

    def main(args):
        api_url = f"http://:/score"
        model_name = args.model

        text_1 = "What is the capital of Brazil?"
        text_2 = "The capital of Brazil is Brasilia."
        prompt = 
        score_response = post_http_request(prompt=prompt, api_url=api_url)
        print("\nPrompt when text_1 and text_2 are both strings:")
        pprint.pprint(prompt)
        print("\nScore Response:")
        pprint.pprint(score_response.json())

        text_1 = "What is the capital of France?"
        text_2 = ["The capital of Brazil is Brasilia.", "The capital of France is Paris."]
        prompt = 
        score_response = post_http_request(prompt=prompt, api_url=api_url)
        print("\nPrompt when text_1 is string and text_2 is a list:")
        pprint.pprint(prompt)
        print("\nScore Response:")
        pprint.pprint(score_response.json())

        text_1 = ["What is the capital of Brazil?", "What is the capital of France?"]
        text_2 = ["The capital of Brazil is Brasilia.", "The capital of France is Paris."]
        prompt = 
        score_response = post_http_request(prompt=prompt, api_url=api_url)
        print("\nPrompt when text_1 and text_2 are both lists:")
        pprint.pprint(prompt)
        print("\nScore Response:")
        pprint.pprint(score_response.json())

    if __name__ == "__main__":
        args = parse_args()
        main(args)

## OpenAI Cross Encoder Score For Multimodal[¶](#openai-cross-encoder-score-for-multimodal "Permanent link")

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """
    Example online usage of Score API.

    Run `vllm serve <model> --runner pooling` to start up the server in vLLM.
    """

    import argparse
    import pprint

    import requests

    def post_http_request(prompt: dict, api_url: str) -> requests.Response:
        headers = 
        response = requests.post(api_url, headers=headers, json=prompt)
        return response

    def parse_args():
        parser = argparse.ArgumentParser()
        parser.add_argument("--host", type=str, default="localhost")
        parser.add_argument("--port", type=int, default=8000)
        parser.add_argument("--model", type=str, default="jinaai/jina-reranker-m0")
        return parser.parse_args()

    def main(args):
        api_url = f"http://:/score"
        model_name = args.model

        text_1 = "slm markdown"
        text_2 = ,
                },
                ,
                },
            ]
        }
        prompt = 
        score_response = post_http_request(prompt=prompt, api_url=api_url)
        print("\nPrompt when text_1 is string and text_2 is a image list:")
        pprint.pprint(prompt)
        print("\nScore Response:")
        pprint.pprint(score_response.json())

    if __name__ == "__main__":
        args = parse_args()
        main(args)

## OpenAI Reranker[¶](#openai-reranker "Permanent link")

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """
    Example of using the OpenAI entrypoint's rerank API which is compatible with
    Jina and Cohere https://jina.ai/reranker

    run: vllm serve BAAI/bge-reranker-base
    """

    import json

    import requests

    url = "http://127.0.0.1:8000/rerank"

    headers = 

    data = 

    def main():
        response = requests.post(url, headers=headers, json=data)

        # Check the response
        if response.status_code == 200:
            print("Request successful!")
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"Request failed with status code: ")
            print(response.text)

    if __name__ == "__main__":
        main()