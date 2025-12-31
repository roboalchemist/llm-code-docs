# Source: https://docs.vllm.ai/en/stable/examples/offline_inference/mistral-small/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/offline_inference/mistral-small.md "Edit this page")

# Mistral-Small[¶](#mistral-small "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/mistral-small.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project

    # ruff: noqa
    import argparse

    from vllm import LLM
    from vllm.sampling_params import SamplingParams
    from vllm.assets.image import ImageAsset

    # This script is an offline demo for running Mistral-Small-3.1
    #
    # If you want to run a server/client setup, please follow this code:
    #
    # - Server:
    #
    # ```bash
    # # Mistral format
    # vllm serve mistralai/Mistral-Small-3.1-24B-Instruct-2503 \
    #   --tokenizer-mode mistral --config-format mistral --load-format mistral \
    #   --limit-mm-per-prompt '' --max-model-len 16384
    #
    # # HF format
    # vllm serve mistralai/Mistral-Small-3.1-24B-Instruct-2503 \
    #   --limit-mm-per-prompt '' --max-model-len 16384
    # ```
    #
    # - Client:
    #
    # ```bash
    # curl --location 'http://<your-node-url>:8000/v1/chat/completions' \
    # --header 'Content-Type: application/json' \
    # --header 'Authorization: Bearer token' \
    # --data ',
    #             },
    #             ,
    #             }
    #         ]
    #       }
    #     ]
    #   }'
    # ```
    #
    # Usage:
    #     python demo.py simple
    #     python demo.py advanced

    # Lower max_model_len and/or max_num_seqs on low-VRAM GPUs.
    # These scripts have been tested on 2x L40 GPUs

    def run_simple_demo(args: argparse.Namespace):
        model_name = "mistralai/Mistral-Small-3.1-24B-Instruct-2503"
        sampling_params = SamplingParams(max_tokens=8192)

        llm = LLM(
            model=model_name,
            tokenizer_mode="mistral" if args.format == "mistral" else "auto",
            config_format="mistral" if args.format == "mistral" else "auto",
            load_format="mistral" if args.format == "mistral" else "auto",
            limit_mm_per_prompt=,
            max_model_len=4096,
            max_num_seqs=2,
            tensor_parallel_size=2,
            mm_processor_cache_gb=0 if args.disable_mm_processor_cache else 4,
        )

        prompt = "Describe this image in one sentence."

        messages = [
            ,
                    ,
                ],
            },
        ]
        outputs = llm.chat(messages, sampling_params=sampling_params)
        print("-" * 50)
        print(outputs[0].outputs[0].text)
        print("-" * 50)

    def run_advanced_demo(args: argparse.Namespace):
        model_name = "mistralai/Mistral-Small-3.1-24B-Instruct-2503"
        max_img_per_msg = 3
        max_tokens_per_img = 4096

        sampling_params = SamplingParams(max_tokens=8192, temperature=0.7)
        llm = LLM(
            model=model_name,
            tokenizer_mode="mistral" if args.format == "mistral" else "auto",
            config_format="mistral" if args.format == "mistral" else "auto",
            load_format="mistral" if args.format == "mistral" else "auto",
            limit_mm_per_prompt=,
            max_model_len=max_img_per_msg * max_tokens_per_img,
            tensor_parallel_size=2,
            mm_processor_cache_gb=0 if args.disable_mm_processor_cache else 4,
        )

        prompt = "Describe the following image."

        url_1 = "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/yosemite.png"
        url_2 = "https://picsum.photos/seed/picsum/200/300"
        url_3 = "https://picsum.photos/id/32/512/512"

        messages = [
            ,
                    },
                    },
                ],
            },
            ,
            ,
            },
                ],
            },
        ]

        outputs = llm.chat(messages=messages, sampling_params=sampling_params)
        print("-" * 50)
        print(outputs[0].outputs[0].text)
        print("-" * 50)

    def parse_args():
        parser = argparse.ArgumentParser(
            description="Run a demo in simple or advanced mode."
        )

        parser.add_argument(
            "mode",
            choices=["simple", "advanced"],
            help="Specify the demo mode: 'simple' or 'advanced'",
        )

        parser.add_argument(
            "--format",
            choices=["mistral", "hf"],
            default="mistral",
            help="Specify the format of the model to load.",
        )

        parser.add_argument(
            "--disable-mm-processor-cache",
            action="store_true",
            help="If True, disables caching of multi-modal processor.",
        )
        return parser.parse_args()

    def main():
        args = parse_args()

        if args.mode == "simple":
            print("Running simple demo...")
            run_simple_demo(args)
        elif args.mode == "advanced":
            print("Running advanced demo...")
            run_advanced_demo(args)

    if __name__ == "__main__":
        main()