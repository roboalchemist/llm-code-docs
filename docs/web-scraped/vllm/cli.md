# Source: https://docs.vllm.ai/en/stable/cli/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/cli/README.md "Edit this page")

# vLLM CLI Guide[¶](#vllm-cli-guide "Permanent link")

The vllm command-line tool is used to run and manage vLLM models. You can start by viewing the help message with:

    vllm --help

Available Commands:

    vllm 

## serve[¶](#serve "Permanent link")

Starts the vLLM OpenAI Compatible API server.

Start with a model:

    vllm serve meta-llama/Llama-2-7b-hf

Specify the port:

    vllm serve meta-llama/Llama-2-7b-hf --port 8100

Serve over a Unix domain socket:

    vllm serve meta-llama/Llama-2-7b-hf --uds /tmp/vllm.sock

Check with \--help for more options:

    # To list all groups
    vllm serve --help=listgroup

    # To view a argument group
    vllm serve --help=ModelConfig

    # To view a single argument
    vllm serve --help=max-num-seqs

    # To search by keyword
    vllm serve --help=max

    # To view full help with pager (less/more)
    vllm serve --help=page

See [vllm serve](serve/) for the full reference of all available arguments.

## chat[¶](#chat "Permanent link")

Generate chat completions via the running API server.

    # Directly connect to localhost API without arguments
    vllm chat

    # Specify API url
    vllm chat --url http://:/v1

    # Quick chat with a single prompt
    vllm chat --quick "hi"

See [vllm chat](chat/) for the full reference of all available arguments.

## complete[¶](#complete "Permanent link")

Generate text completions based on the given prompt via the running API server.

    # Directly connect to localhost API without arguments
    vllm complete

    # Specify API url
    vllm complete --url http://:/v1

    # Quick complete with a single prompt
    vllm complete --quick "The future of AI is"

See [vllm complete](complete/) for the full reference of all available arguments.

## bench[¶](#bench "Permanent link")

Run benchmark tests for latency online serving throughput and offline inference throughput.

To use benchmark commands, please install with extra dependencies using `pip install vllm[bench]`.

Available Commands:

    vllm bench 

### latency[¶](#latency "Permanent link")

Benchmark the latency of a single batch of requests.

    vllm bench latency \
        --model meta-llama/Llama-3.2-1B-Instruct \
        --input-len 32 \
        --output-len 1 \
        --enforce-eager \
        --load-format dummy

See [vllm bench latency](bench/latency/) for the full reference of all available arguments.

### serve[¶](#serve_1 "Permanent link") 

Benchmark the online serving throughput.

    vllm bench serve \
        --model meta-llama/Llama-3.2-1B-Instruct \
        --host server-host \
        --port server-port \
        --random-input-len 32 \
        --random-output-len 4  \
        --num-prompts  5

See [vllm bench serve](bench/serve/) for the full reference of all available arguments.

### throughput[¶](#throughput "Permanent link")

Benchmark offline inference throughput.

    vllm bench throughput \
        --model meta-llama/Llama-3.2-1B-Instruct \
        --input-len 32 \
        --output-len 1 \
        --enforce-eager \
        --load-format dummy

See [vllm bench throughput](bench/throughput/) for the full reference of all available arguments.

## collect-env[¶](#collect-env "Permanent link")

Start collecting environment information.

    vllm collect-env

## run-batch[¶](#run-batch "Permanent link")

Run batch prompts and write results to file.

Running with a local file:

    vllm run-batch \
        -i offline_inference/openai_batch/openai_example_batch.jsonl \
        -o results.jsonl \
        --model meta-llama/Meta-Llama-3-8B-Instruct

Using remote file:

    vllm run-batch \
        -i https://raw.githubusercontent.com/vllm-project/vllm/main/examples/offline_inference/openai_batch/openai_example_batch.jsonl \
        -o results.jsonl \
        --model meta-llama/Meta-Llama-3-8B-Instruct

See [vllm run-batch](run-batch/) for the full reference of all available arguments.

## More Help[¶](#more-help "Permanent link")

For detailed options of any subcommand, use:

    vllm <subcommand> --help

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [August 11, 2025] ]