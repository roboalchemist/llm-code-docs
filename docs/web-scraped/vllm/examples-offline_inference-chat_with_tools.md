# Source: https://docs.vllm.ai/en/stable/examples/offline_inference/chat_with_tools/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/offline_inference/chat_with_tools.md "Edit this page")

# Chat With Tools[¶](#chat-with-tools "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/chat_with_tools.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project

    # ruff: noqa
    import json
    import random
    import string

    from vllm import LLM
    from vllm.sampling_params import SamplingParams

    # This script is an offline demo for function calling
    #
    # If you want to run a server/client setup, please follow this code:
    #
    # - Server:
    #
    # ```bash
    # vllm serve mistralai/Mistral-7B-Instruct-v0.3 --tokenizer-mode mistral --load-format mistral --config-format mistral
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

    model_name = "mistralai/Mistral-7B-Instruct-v0.3"
    # or switch to "mistralai/Mistral-Nemo-Instruct-2407"
    # or "mistralai/Mistral-Large-Instruct-2407"
    # or any other mistral model with function calling ability

    sampling_params = SamplingParams(max_tokens=8192, temperature=0.0)
    llm = LLM(
        model=model_name,
        tokenizer_mode="mistral",
        config_format="mistral",
        load_format="mistral",
    )

    def generate_random_id(length=9):
        characters = string.ascii_letters + string.digits
        random_id = "".join(random.choice(characters) for _ in range(length))
        return random_id

    # simulate an API that can be called
    def get_current_weather(city: str, state: str, unit: "str"):
        return (
            f"The weather in ,  is 85 degrees . It is "
            "partly cloudly, with highs in the 90's."
        )

    tool_functions = 

    tools = [
        ,
                        "state": ,
                        "unit": ,
                    },
                    "required": ["city", "state", "unit"],
                },
            },
        }
    ]

    messages = [
        
    ]

    outputs = llm.chat(messages, sampling_params=sampling_params, tools=tools)
    output = outputs[0].outputs[0].text.strip()

    # append the assistant message
    messages.append(
        
    )

    # let's now actually parse and execute the model's output simulating an API call by using the
    # above defined function
    tool_calls = json.loads(output)
    tool_answers = [
        tool_functions[call["name"]](**call["arguments"]) for call in tool_calls
    ]

    # append the answer as a tool message and let the LLM give you an answer
    messages.append(
        
    )

    outputs = llm.chat(messages, sampling_params, tools=tools)

    print(outputs[0].outputs[0].text.strip())
    # yields
    #   'The weather in Dallas, TX is 85 degrees Fahrenheit. '
    #   'It is partly cloudly, with highs in the 90's.'