# Source: https://docs.vllm.ai/en/stable/examples/online_serving/structured_outputs/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/structured_outputs.md "Edit this page")

# Structured Outputs[¶](#structured-outputs "Permanent link")

Source <https://github.com/vllm-project/vllm/tree/main/examples/online_serving/structured_outputs>.

This script demonstrates various structured output capabilities of vLLM\'s OpenAI-compatible server. It can run individual constraint type or all of them. It supports both streaming responses and concurrent non-streaming requests.

To use this example, you must start an vLLM server with any model of your choice.

    vllm serve Qwen/Qwen2.5-3B-Instruct

To serve a reasoning model, you can use the following command:

    vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-7B \
        --reasoning-parser deepseek_r1

If you want to run this script standalone with `uv`, you can use the following:

    uvx --from git+https://github.com/vllm-project/vllm#subdirectory=examples/online_serving/structured_outputs \
        structured-outputs

See [feature docs](https://docs.vllm.ai/en/latest/features/structured_outputs.html) for more information.

Tip

If vLLM is running remotely, then set `OPENAI_BASE_URL=<remote_url>` before running the script.

## Usage[¶](#usage "Permanent link")

Run all constraints, non-streaming:

    uv run structured_outputs.py

Run all constraints, streaming:

    uv run structured_outputs.py --stream

Run certain constraints, for example `structural_tag` and `regex`, streaming:

    uv run structured_outputs.py \
        --constraint structural_tag regex \
        --stream

Run all constraints, with reasoning models and streaming:

    uv run structured_outputs.py --reasoning --stream

## Example materials[¶](#example-materials "Permanent link")

pyproject.toml

    [project]
    name = "examples-online-structured-outputs"
    requires-python = ">=3.10, <3.14"
    dependencies = ["openai==1.78.1", "pydantic==2.11.4"]
    version = "0.0.0"

    [project.scripts]
    structured-outputs = "structured_outputs:main"

structured_outputs.py

    # ruff: noqa: E501
    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    import argparse
    import asyncio
    import enum
    import os
    from typing import Any, Literal

    import openai
    import pydantic
    from openai.types.chat import ChatCompletionChunk

    ConstraintsFormat = Literal[
        "choice",
        "regex",
        "json",
        "grammar",
        "structural_tag",
    ]

    async def print_stream_response(
        stream_response: openai.AsyncStream[ChatCompletionChunk],
        title: str,
        args: argparse.Namespace,
    ):
        print(f"\n\n (Streaming):")

        local_reasoning_header_printed = False
        local_content_header_printed = False

        async for chunk in stream_response:
            delta = chunk.choices[0].delta

            reasoning_chunk_text: str | None = getattr(delta, "reasoning", None)
            content_chunk_text = delta.content

            if args.reasoning:
                if reasoning_chunk_text:
                    if not local_reasoning_header_printed:
                        print("  Reasoning: ", end="")
                        local_reasoning_header_printed = True
                    print(reasoning_chunk_text, end="", flush=True)

                if content_chunk_text:
                    if not local_content_header_printed:
                        if local_reasoning_header_printed:
                            print()
                        print("  Content: ", end="")
                        local_content_header_printed = True
                    print(content_chunk_text, end="", flush=True)
            else:
                if content_chunk_text:
                    if not local_content_header_printed:
                        print("  Content: ", end="")
                        local_content_header_printed = True
                    print(content_chunk_text, end="", flush=True)
        print()

    class CarType(str, enum.Enum):
        SEDAN = "SEDAN"
        SUV = "SUV"
        TRUCK = "TRUCK"
        COUPE = "COUPE"

    class CarDescription(pydantic.BaseModel):
        brand: str
        model: str
        car_type: CarType

    PARAMS: dict[ConstraintsFormat, dict[str, Any]] = 
            ],
            "extra_body": },
        },
        "regex": 
            ],
            "extra_body": @\w\.com\n"},
            },
        },
        "json": 
            ],
            "response_format": ,
            },
        },
        "grammar": 
            ],
            "extra_body": 
            },
        },
        "structural_tag": 
        }
    }

    If a you choose to call a function ONLY reply in the following format:
    <=>
    where

    start_tag => `<function`
    parameters => a JSON dict with the function argument name as key and function
                  argument value as value.
    end_tag => `</function>`

    Here is an example,
    <function=example_function_name></function>

    Reminder:
    - Function calls MUST follow the specified format
    - Required parameters MUST be specified
    - Only call one function at a time
    - Put the entire function call reply on one line
    - Always add your sources when using search results to answer the user query

    You are a helpful assistant.

    Given the previous instructions, what is the weather in New York City, Boston,
    and San Francisco?""",
                },
            ],
            "response_format": },
                            "required": ["city"],
                        },
                        "end": "</function>",
                    }
                ],
                "triggers": ["<function="],
            },
        },
    }

    async def cli():
        parser = argparse.ArgumentParser(
            description="Run OpenAI Chat Completion with various structured outputs capabilities",
        )
        _ = parser.add_argument(
            "--constraint",
            type=str,
            nargs="+",
            choices=[*list(PARAMS), "*"],
            default=["*"],
            help="Specify which constraint(s) to run.",
        )
        _ = parser.add_argument(
            "--stream",
            action=argparse.BooleanOptionalAction,
            default=False,
            help="Enable streaming output",
        )
        _ = parser.add_argument(
            "--reasoning",
            action=argparse.BooleanOptionalAction,
            default=False,
            help="Enable printing of reasoning traces if available.",
        )
        args = parser.parse_args()

        base_url = os.getenv("OPENAI_BASE_URL", "http://localhost:8000/v1")
        client = openai.AsyncOpenAI(base_url=base_url, api_key="EMPTY")
        constraints = list(PARAMS) if "*" in args.constraint else list(set(args.constraint))
        model = (await client.models.list()).data[0].id

        if args.stream:
            results = await asyncio.gather(
                *[
                    client.chat.completions.create(
                        model=model,
                        max_tokens=1024,
                        stream=True,
                        **PARAMS[name],
                    )
                    for name in constraints
                ]
            )
            for constraint, stream in zip(constraints, results):
                await print_stream_response(stream, constraint, args)
        else:
            results = await asyncio.gather(
                *[
                    client.chat.completions.create(
                        model=model,
                        max_tokens=1024,
                        stream=False,
                        **PARAMS[name],
                    )
                    for name in constraints
                ]
            )
            for constraint, response in zip(constraints, results):
                print(f"\n\n:")
                message = response.choices[0].message
                if args.reasoning and hasattr(message, "reasoning"):
                    print(f"  Reasoning: ")
                print(f"  Content: ")

    def main():
        asyncio.run(cli())

    if __name__ == "__main__":
        main()