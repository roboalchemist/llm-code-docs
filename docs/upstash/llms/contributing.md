# Source: https://upstash.com/docs/vector/sdks/ts/contributing.md

# Source: https://upstash.com/docs/search/sdks/ts/contributing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Contributing

## Preparing the environment

This project uses [Bun](https://bun.sh/) for packaging and dependency management. Make sure you have the relevant dependencies.

```commandline  theme={"system"}
curl -fsSL https://bun.sh/install | bash
```

You will also need a search database on [Upstash](https://console.upstash.com/search).

***

## Code Formatting

Run the following command to format code:

```bash  theme={"system"}
bun run fmt
```

***

## Running tests

To run all the tests, make sure you have the relevant environment variables.

```bash  theme={"system"}
bun run test
```
