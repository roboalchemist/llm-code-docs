# Source: https://docs.together.ai/reference/cli/getting-started.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started

The Together Python library comes with a command-line interface you can use to query Together's open-source models, upload new data files to your account, or manage your account's fine-tune jobs.

## Prerequisites

* Make sure your local machine has [Python](https://www.python.org/) installed.
* If you haven't already, [register for a Together account](https://api.together.xyz/settings/api-keys) to get an API key.

## Install the library

Launch your terminal and install or update the Together CLI with the following command:

<CodeGroup>
  ```sh pip theme={null}
  pip install --upgrade together
  ```

  ```sh uv theme={null}
  uv add together
  ```
</CodeGroup>

## Authenticate your shell

The CLI relies on the `TOGETHER_API_KEY` environment variable being set to your account's API token to authenticate requests. You can find your API token in your [account settings](https://api.together.xyz/settings/api-keys).

To create an environment variable in the current shell, run:

```sh Shell theme={null}
export TOGETHER_API_KEY=xxxxx
```

You can also add it to your shell's global configuration so all new sessions can access it. Different shells have different semantics for setting global environment variables, so see your preferred shell's documentation to learn more.

## Usage

```sh Shell theme={null}
# example
together [OPTIONS] COMMAND [ARGS]...

# Usage of inline api key
together --api-key xxx COMMAND [ARGS]...
```

### Options

| Name            | Option | Description                                                           |
| --------------- | ------ | --------------------------------------------------------------------- |
| `--api-key`     | string | Together API Key. Defaults to environment variable `TOGETHER_API_KEY` |
| `--timeout`     | number | Request timeout, defaults to 5 seconds.                               |
| `--max-retries` | number | Maximum number of HTTP retries.                                       |
| `--version`     |        | Print version                                                         |
| `--debug`       |        | Debug mode                                                            |

If you know what you're looking for, find your use case in the sidebar to learn more! The CLI is primarily used for fine-tuning so we recommend visiting **[Files](/reference/cli/files)** or **[Fine-tuning](/reference/cli/finetune)**.


Built with [Mintlify](https://mintlify.com).