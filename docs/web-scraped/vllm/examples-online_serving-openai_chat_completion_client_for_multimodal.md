# Source: https://docs.vllm.ai/en/stable/examples/online_serving/openai_chat_completion_client_for_multimodal/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/openai_chat_completion_client_for_multimodal.md "Edit this page")

# OpenAI Chat Completion Client For Multimodal[¶](#openai-chat-completion-client-for-multimodal "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_chat_completion_client_for_multimodal.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """An example showing how to use vLLM to serve multimodal models
    and run online serving with OpenAI client.

    Launch the vLLM server with the following command:

    (single image inference with Llava)
    vllm serve llava-hf/llava-1.5-7b-hf

    (multi-image inference with Phi-3.5-vision-instruct)
    vllm serve microsoft/Phi-3.5-vision-instruct --runner generate \
        --trust-remote-code --max-model-len 4096 --limit-mm-per-prompt ''

    (audio inference with Ultravox)
    vllm serve fixie-ai/ultravox-v0_5-llama-3_2-1b \
        --max-model-len 4096 --trust-remote-code

    run the script with
    python openai_chat_completion_client_for_multimodal.py --chat-type audio
    """

    import base64

    import requests
    from openai import OpenAI
    from utils import get_first_model

    from vllm.utils.argparse_utils import FlexibleArgumentParser

    # Modify OpenAI's API key and API base to use vLLM's API server.
    openai_api_key = "EMPTY"
    openai_api_base = "http://localhost:8000/v1"

    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key=openai_api_key,
        base_url=openai_api_base,
    )

    headers = 

    def encode_base64_content_from_url(content_url: str) -> str:
        """Encode a content retrieved from a remote url to base64 format."""

        with requests.get(content_url, headers=headers) as response:
            response.raise_for_status()
            result = base64.b64encode(response.content).decode("utf-8")

        return result

    # Text-only inference
    def run_text_only(model: str, max_completion_tokens: int) -> None:
        chat_completion = client.chat.completions.create(
            messages=[],
            model=model,
            max_completion_tokens=max_completion_tokens,
        )

        result = chat_completion.choices[0].message.content
        print("Chat completion output:\n", result)

    # Single-image input inference
    def run_single_image(model: str, max_completion_tokens: int) -> None:
        ## Use image url in the payload
        image_url = "https://vllm-public-assets.s3.us-west-2.amazonaws.com/vision_model_images/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
        chat_completion_from_url = client.chat.completions.create(
            messages=[
                ,
                        ,
                        },
                    ],
                }
            ],
            model=model,
            max_completion_tokens=max_completion_tokens,
        )

        result = chat_completion_from_url.choices[0].message.content
        print("Chat completion output from image url:\n", result)

        ## Use base64 encoded image in the payload
        image_base64 = encode_base64_content_from_url(image_url)
        chat_completion_from_base64 = client.chat.completions.create(
            messages=[
                ,
                        "},
                        },
                    ],
                }
            ],
            model=model,
            max_completion_tokens=max_completion_tokens,
        )

        result = chat_completion_from_base64.choices[0].message.content
        print("Chat completion output from base64 encoded image:", result)

    # Multi-image input inference
    def run_multi_image(model: str, max_completion_tokens: int) -> None:
        image_url_duck = "https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/duck.jpg"
        image_url_lion = "https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/lion.jpg"
        chat_completion_from_url = client.chat.completions.create(
            messages=[
                ,
                        ,
                        },
                        ,
                        },
                    ],
                }
            ],
            model=model,
            max_completion_tokens=max_completion_tokens,
        )

        result = chat_completion_from_url.choices[0].message.content
        print("Chat completion output:\n", result)

    # Video input inference
    def run_video(model: str, max_completion_tokens: int) -> None:
        video_url = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4"
        video_base64 = encode_base64_content_from_url(video_url)

        ## Use video url in the payload
        chat_completion_from_url = client.chat.completions.create(
            messages=[
                ,
                        ,
                        },
                    ],
                }
            ],
            model=model,
            max_completion_tokens=max_completion_tokens,
        )

        result = chat_completion_from_url.choices[0].message.content
        print("Chat completion output from video url:\n", result)

        ## Use base64 encoded video in the payload
        chat_completion_from_base64 = client.chat.completions.create(
            messages=[
                ,
                        "},
                        },
                    ],
                }
            ],
            model=model,
            max_completion_tokens=max_completion_tokens,
        )

        result = chat_completion_from_base64.choices[0].message.content
        print("Chat completion output from base64 encoded video:\n", result)

    # Audio input inference
    def run_audio(model: str, max_completion_tokens: int) -> None:
        from vllm.assets.audio import AudioAsset

        audio_url = AudioAsset("winning_call").url
        audio_base64 = encode_base64_content_from_url(audio_url)

        # OpenAI-compatible schema (`input_audio`)
        chat_completion_from_base64 = client.chat.completions.create(
            messages=[
                ,
                        ,
                        },
                    ],
                }
            ],
            model=model,
            max_completion_tokens=max_completion_tokens,
        )

        result = chat_completion_from_base64.choices[0].message.content
        print("Chat completion output from input audio:\n", result)

        # HTTP URL
        chat_completion_from_url = client.chat.completions.create(
            messages=[
                ,
                        ,
                        },
                    ],
                }
            ],
            model=model,
            max_completion_tokens=max_completion_tokens,
        )

        result = chat_completion_from_url.choices[0].message.content
        print("Chat completion output from audio url:\n", result)

        # base64 URL
        chat_completion_from_base64 = client.chat.completions.create(
            messages=[
                ,
                        "
                            },
                        },
                    ],
                }
            ],
            model=model,
            max_completion_tokens=max_completion_tokens,
        )

        result = chat_completion_from_base64.choices[0].message.content
        print("Chat completion output from base64 encoded audio:\n", result)

    def run_multi_audio(model: str, max_completion_tokens: int) -> None:
        from vllm.assets.audio import AudioAsset

        # Two different audios to showcase batched inference.
        audio_url = AudioAsset("winning_call").url
        audio_base64 = encode_base64_content_from_url(audio_url)
        audio_url2 = AudioAsset("azacinto_foscolo").url
        audio_base64_2 = encode_base64_content_from_url(audio_url2)

        # OpenAI-compatible schema (`input_audio`)
        chat_completion_from_base64 = client.chat.completions.create(
            messages=[
                ,
                        ,
                        },
                        ,
                        },
                    ],
                }
            ],
            model=model,
            max_completion_tokens=max_completion_tokens,
        )

        result = chat_completion_from_base64.choices[0].message.content
        print("Chat completion output from input audio:\n", result)

    example_function_map = 

    def parse_args():
        parser = FlexibleArgumentParser(
            description="Demo on using OpenAI client for online serving with "
            "multimodal language models served with vLLM."
        )
        parser.add_argument(
            "--chat-type",
            "-c",
            type=str,
            default="single-image",
            choices=list(example_function_map.keys()),
            help="Conversation type with multimodal data.",
        )
        parser.add_argument(
            "--max-completion-tokens",
            "-n",
            type=int,
            default=128,
            help="Maximum number of tokens to generate for each completion.",
        )
        return parser.parse_args()

    def main(args) -> None:
        chat_type = args.chat_type
        model = get_first_model(client)
        example_function_map[chat_type](model, args.max_completion_tokens)

    if __name__ == "__main__":
        args = parse_args()
        main(args)