# Source: https://docs.vllm.ai/en/stable/examples/online_serving/sagemaker-entrypoint/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/sagemaker-entrypoint.md "Edit this page")

# Sagemaker-Entrypoint[¶](#sagemaker-entrypoint "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/online_serving/sagemaker-entrypoint.sh>.

    #!/bin/bash

    # Define the prefix for environment variables to look for
    PREFIX="SM_VLLM_"
    ARG_PREFIX="--"

    # Initialize an array for storing the arguments
    # port 8080 required by sagemaker, https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html#your-algorithms-inference-code-container-response
    ARGS=(--port 8080)

    # Loop through all environment variables
    while IFS='=' read -r key value; do
        # Remove the prefix from the key, convert to lowercase, and replace underscores with dashes
        arg_name=$(echo "$"}" | tr '[:upper:]' '[:lower:]' | tr '_' '-')

        # Add the argument name and value to the ARGS array
        ARGS+=("$$")
        if [ -n "$value" ]; then
            ARGS+=("$value")
        fi
    done < <(env | grep "^$")

    # Pass the collected arguments to the main entrypoint
    exec vllm serve "$"