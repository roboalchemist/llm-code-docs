# Source: https://docs.vllm.ai/en/stable/cli/complete/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/cli/complete.md "Edit this page")

# vllm complete[¶](#vllm-complete "Permanent link")

## Arguments[¶](#arguments "Permanent link")

#### `--url`[¶](#-url "Permanent link") 

url of the running OpenAI-Compatible RESTful API server

Default: `http://localhost:8000/v1`

#### `--model-name`[¶](#-model-name "Permanent link") 

The model name used in prompt completion, default to the first model in list models API call.

Default: `None`

#### `--api-key`[¶](#-api-key "Permanent link") 

API key for OpenAI services. If provided, this api key will overwrite the api key obtained through environment variables. It is important to note that this option only applies to the OpenAI-compatible API endpoints and NOT other endpoints that may be present in the server. See the security guide in the vLLM docs for more details.

Default: `None`

#### `--max-tokens`[¶](#-max-tokens "Permanent link") 

Maximum number of tokens to generate per output sequence.

Default: `None`

#### `-q`, `--quick`[¶](#-q-quick "Permanent link") 

Send a single prompt and print the completion output, then exit.

Default: `None`

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [November 15, 2025] ]