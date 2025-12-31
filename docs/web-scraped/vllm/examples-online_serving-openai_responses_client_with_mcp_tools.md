# Source: https://docs.vllm.ai/en/stable/examples/online_serving/openai_responses_client_with_mcp_tools/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/openai_responses_client_with_mcp_tools.md "Edit this page")

# OpenAI Responses Client With Mcp Tools[¶](#openai-responses-client-with-mcp-tools "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_responses_client_with_mcp_tools.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """
    Example demonstrating MCP (Model Context Protocol) tools with the Responses API.

    This example shows how to use MCP tools with different allowed_tools configurations:
    1. No filter (allows all tools from the MCP server)
    2. Wildcard "*" (explicitly allows all tools)
    3. Specific tool names (filters to only those tools)

    Set up this example by starting a vLLM OpenAI-compatible server with MCP tools enabled.
    For example:
    vllm serve openai/gpt-oss-20b --enforce-eager --tool-server demo

    Environment variables:
    - VLLM_ENABLE_RESPONSES_API_STORE=1
    - VLLM_GPT_OSS_SYSTEM_TOOL_MCP_LABELS=code_interpreter,container
    - VLLM_GPT_OSS_HARMONY_SYSTEM_INSTRUCTIONS=1
    """

    from openai import OpenAI
    from utils import get_first_model

    def example_no_filter():
        """Example with no allowed_tools filter - allows all tools."""
        print("=" * 60)
        print("Example 1: No allowed_tools filter (allows all tools)")
        print("=" * 60)

        base_url = "http://0.0.0.0:8000/v1"
        client = OpenAI(base_url=base_url, api_key="empty")
        model = get_first_model(client)

        response = client.responses.create(
            model=model,
            input="Execute this code: print('Hello from Python!')",
            instructions="Use the Python tool to execute code.",
            tools=[
                
            ],
        )

        print(f"Status: ")
        print(f"Output: ")
        print()

    def example_wildcard():
        """Example with allowed_tools=['*'] - explicitly allows all tools."""
        print("=" * 60)
        print("Example 2: allowed_tools=['*'] (select all tools)")
        print("=" * 60)

        base_url = "http://0.0.0.0:8000/v1"
        client = OpenAI(base_url=base_url, api_key="empty")
        model = get_first_model(client)

        response = client.responses.create(
            model=model,
            input="Execute this code: print('Hello from Python with wildcard!')",
            instructions="Use the Python tool to execute code.",
            tools=[
                
            ],
        )

        print(f"Status: ")
        print(f"Output: ")
        print()

    def example_specific_tools():
        """Example with specific allowed_tools list - filters available tools.

        Note: This example uses 'web_search_preview' (browser) which has multiple
        sub-tools: 'search', 'open', 'find'. The code_interpreter (python) doesn't
        have sub-tools, so filtering doesn't apply there.
        """
        print("=" * 60)
        print("Example 3: allowed_tools=['search'] (filter browser to specific tools)")
        print("=" * 60)

        base_url = "http://0.0.0.0:8000/v1"
        client = OpenAI(base_url=base_url, api_key="empty")
        model = get_first_model(client)

        response = client.responses.create(
            model=model,
            input="Search for 'Python programming tutorials'",
            instructions="Use the browser tool to search.",
            tools=[
                
            ],
        )

        print(f"Status: ")
        print(f"Output: ")
        print()

    def example_object_format():
        """Example using object format for allowed_tools with browser tools."""
        print("=" * 60)
        print("Example 4: allowed_tools with object format")
        print("=" * 60)

        base_url = "http://0.0.0.0:8000/v1"
        client = OpenAI(base_url=base_url, api_key="empty")
        model = get_first_model(client)

        response = client.responses.create(
            model=model,
            input="Search for 'machine learning' and open the first result",
            instructions="Use the browser tool.",
            tools=[
                ,
                }
            ],
        )

        print(f"Status: ")
        print(f"Output: ")
        print()

    def main():
        """Run all examples."""
        print("\n" + "=" * 60)
        print("MCP Tools with allowed_tools Examples")
        print("=" * 60 + "\n")

        # Run all examples
        example_no_filter()
        example_wildcard()
        example_specific_tools()
        example_object_format()

        print("=" * 60)
        print("Summary:")
        print("  - No filter or '*' → All tools available from server")
        print("  - Specific list → Only those sub-tools available")
        print("  - Object format → More control with tool_names field")
        print("")
        print("Note: allowed_tools filters SUB-TOOLS within an MCP server:")
        print("  - code_interpreter (python): No sub-tools to filter")
        print("  - web_search_preview (browser): Has 'search', 'open', 'find'")
        print("=" * 60)

    if __name__ == "__main__":
        main()