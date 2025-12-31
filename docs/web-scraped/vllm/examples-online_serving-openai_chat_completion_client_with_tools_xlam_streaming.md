# Source: https://docs.vllm.ai/en/stable/examples/online_serving/openai_chat_completion_client_with_tools_xlam_streaming/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/openai_chat_completion_client_with_tools_xlam_streaming.md "Edit this page")

# OpenAI Chat Completion Client With Tools Xlam Streaming[¶](#openai-chat-completion-client-with-tools-xlam-streaming "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_chat_completion_client_with_tools_xlam_streaming.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    # ruff: noqa: E501
    """
    Set up this example by starting a vLLM OpenAI-compatible server with tool call
    options enabled for xLAM-2 models:

    vllm serve --model Salesforce/Llama-xLAM-2-8b-fc-r --enable-auto-tool-choice --tool-call-parser xlam

    OR

    vllm serve --model Salesforce/xLAM-2-3b-fc-r --enable-auto-tool-choice --tool-call-parser xlam

    This example demonstrates streaming tool calls with xLAM models.
    """

    import json
    import time

    from openai import OpenAI

    # Modify OpenAI's API key and API base to use vLLM's API server.
    openai_api_key = "empty"
    openai_api_base = "http://localhost:8000/v1"

    # Define tool functions
    def get_weather(location: str, unit: str):
        return f"Weather in  is 22 degrees ."

    def calculate_expression(expression: str):
        try:
            result = eval(expression)
            return f"The result of  is "
        except Exception as e:
            return f"Could not calculate : "

    def translate_text(text: str, target_language: str):
        return f"Translation of '' to : [translated content]"

    # Define tools
    tools = [
        ,
                        "unit": ,
                    },
                    "required": ["location", "unit"],
                },
            },
        },
        
                    },
                    "required": ["expression"],
                },
            },
        },
        ,
                        "target_language": ,
                    },
                    "required": ["text", "target_language"],
                },
            },
        },
    ]

    # Map of function names to implementations
    tool_functions = 

    def process_stream(response, tool_functions, original_query):
        """Process a streaming response with possible tool calls"""
        # Track multiple tool calls
        tool_calls =   # Dictionary to store tool calls by ID

        current_id = None

        print("\n--- Stream Output ---")
        for chunk in response:
            # Handle tool calls in the stream
            if chunk.choices[0].delta.tool_calls:
                for tool_call_chunk in chunk.choices[0].delta.tool_calls:
                    # Get the tool call ID
                    if hasattr(tool_call_chunk, "id") and tool_call_chunk.id:
                        current_id = tool_call_chunk.id
                        if current_id not in tool_calls:
                            tool_calls[current_id] = 

                    # Extract function information as it comes in chunks
                    if (
                        hasattr(tool_call_chunk, "function")
                        and current_id
                        and current_id in tool_calls
                    ):
                        if (
                            hasattr(tool_call_chunk.function, "name")
                            and tool_call_chunk.function.name
                        ):
                            tool_calls[current_id]["function_name"] = (
                                tool_call_chunk.function.name
                            )
                            print(f"Function called: ")

                        if (
                            hasattr(tool_call_chunk.function, "arguments")
                            and tool_call_chunk.function.arguments
                        ):
                            tool_calls[current_id]["function_args"] += (
                                tool_call_chunk.function.arguments
                            )
                            print(f"Arguments chunk: ")

            # Handle regular content in the stream
            elif chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="")

        print("\n--- End Stream ---\n")

        # Execute each function call and build messages for follow-up
        follow_up_messages = []

        for tool_id, tool_data in tool_calls.items():
            function_name = tool_data["function_name"]
            function_args = tool_data["function_args"]
            function_id = tool_data["function_id"]

            if function_name and function_args:
                try:
                    # Parse the JSON arguments
                    args = json.loads(function_args)

                    # Call the function with the arguments
                    function_result = tool_functions[function_name](**args)
                    print(
                        f"\n--- Function Result () ---\n\n"
                    )

                    # Add the assistant message with tool call
                    follow_up_messages.append(
                        ,
                                }
                            ],
                        }
                    )

                    # Add the tool message with function result
                    follow_up_messages.append(
                        
                    )

                except Exception as e:
                    print(f"Error executing function: ")

        # Only send follow-up if we have results to process
        if len(follow_up_messages) > 1:
            # Create a follow-up message with all the function results
            follow_up_response = client.chat.completions.create(
                model=client.models.list().data[0].id,
                messages=follow_up_messages,
                stream=True,
            )

            print("\n--- Follow-up Response ---")
            for chunk in follow_up_response:
                if chunk.choices[0].delta.content:
                    print(chunk.choices[0].delta.content, end="")
            print("\n--- End Follow-up ---\n")

    def run_test_case(query, test_name):
        """Run a single test case with the given query"""
        print(f"\n\nTEST CASE: \n")
        print(f"Query: ''")

        start_time = time.time()

        # Create streaming chat completion request
        response = client.chat.completions.create(
            model=client.models.list().data[0].id,
            messages=[],
            tools=tools,
            tool_choice="auto",
            stream=True,
        )

        # Process the streaming response
        process_stream(response, tool_functions, query)

        end_time = time.time()
        print(f"Test completed in  seconds")

    def main():
        # Initialize OpenAI client
        global client
        client = OpenAI(
            api_key=openai_api_key,
            base_url=openai_api_base,
        )

        # Run test cases
        test_cases = [
            ("I want to know the weather in San Francisco", "Weather Information"),
            ("Calculate 25 * 17 + 31", "Math Calculation"),
            ("Translate 'Hello world' to Spanish", "Text Translation"),
            ("What is the weather in Tokyo and New York in celsius", "Multiple Tool Usage"),
        ]

        # Execute all test cases
        for query, test_name in test_cases:
            run_test_case(query, test_name)
            time.sleep(1)  # Small delay between tests

        print("\nAll tests completed.")

    if __name__ == "__main__":
        main()