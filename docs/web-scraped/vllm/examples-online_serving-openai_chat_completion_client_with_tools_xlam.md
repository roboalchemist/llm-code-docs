# Source: https://docs.vllm.ai/en/stable/examples/online_serving/openai_chat_completion_client_with_tools_xlam/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/openai_chat_completion_client_with_tools_xlam.md "Edit this page")

# OpenAI Chat Completion Client With Tools Xlam[¶](#openai-chat-completion-client-with-tools-xlam "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_chat_completion_client_with_tools_xlam.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    # ruff: noqa: E501
    """
    Set up this example by starting a vLLM OpenAI-compatible server with tool call
    options enabled for xLAM-2 models:

    vllm serve --model Salesforce/Llama-xLAM-2-8b-fc-r --enable-auto-tool-choice --tool-call-parser xlam

    OR

    vllm serve --model Salesforce/xLAM-2-3b-fc-r --enable-auto-tool-choice --tool-call-parser xlam
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

    def process_response(response, tool_functions, original_query):
        """Process a non-streaming response with possible tool calls"""

        print("\n--- Response Output ---")

        # Check if the response has content
        if response.choices[0].message.content:
            print(f"Content: ")

        # Check if the response has tool calls
        if response.choices[0].message.tool_calls:
            print("--------------------------------")
            print(f"Tool calls: ")
            print("--------------------------------")

            # Collect all tool calls and results before making follow-up request
            tool_results = []
            assistant_message = 

            if response.choices[0].message.content:
                assistant_message["content"] = response.choices[0].message.content

            assistant_tool_calls = []

            # Process each tool call
            for tool_call in response.choices[0].message.tool_calls:
                function_name = tool_call.function.name
                function_args = tool_call.function.arguments
                function_id = tool_call.id

                print(f"Function called: ")
                print(f"Arguments: ")
                print(f"Function ID: ")

                # Execute the function
                try:
                    # Parse the JSON arguments
                    args = json.loads(function_args)

                    # Call the function with the arguments
                    function_result = tool_functions[function_name](**args)
                    print(f"\n--- Function Result ---\n\n")

                    # Add tool call to assistant message
                    assistant_tool_calls.append(
                        ,
                        }
                    )

                    # Add tool result to tool_results
                    tool_results.append(
                        
                    )

                except Exception as e:
                    print(f"Error executing function: ")

            # Add tool_calls to assistant message
            assistant_message["tool_calls"] = assistant_tool_calls

            # Create a follow-up message with all function results
            follow_up_messages = [
                ,
                assistant_message,
            ]

            # Add all tool results to the messages
            follow_up_messages.extend(tool_results)

            # Get completion with all tool results in a single follow-up
            follow_up_response = client.chat.completions.create(
                model=client.models.list().data[0].id,
                messages=follow_up_messages,
                stream=False,
            )

            print("\n--- Follow-up Response ---")
            print(follow_up_response.choices[0].message.content)
            print("--- End Follow-up ---\n")

        print("--- End Response ---\n")

    def run_test_case(query, test_name):
        """Run a single test case with the given query"""
        print(f"\n\nTEST CASE: \n")
        print(f"Query: ''")

        start_time = time.time()

        # Create non-streaming chat completion request
        response = client.chat.completions.create(
            model=client.models.list().data[0].id,
            messages=[],
            tools=tools,
            tool_choice="auto",
            stream=False,
        )

        # Process the non-streaming response, passing the original query
        process_response(response, tool_functions, query)

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