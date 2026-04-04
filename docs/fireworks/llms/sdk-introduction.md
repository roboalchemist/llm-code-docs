# Source: https://docs.fireworks.ai/tools-sdks/python-client/sdk-introduction.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Build SDK Introduction

<Warning>
  This SDK documentation applies to version [0.19.20](https://pypi.org/project/fireworks-ai/0.19.20/) and earlier. The Build SDK will be deprecated and replaced with version 1.0.0 of the SDK (see our [changelog](/updates/changelog#2025-11-12) for more details). Please migrate to the [new SDK](/tools-sdks/python-sdk).
</Warning>

The [Fireworks Build SDK](https://pypi.org/project/fireworks-ai/) is a client library that allows you to interact with the Fireworks API using Python. It provides a simple and intuitive interface for working with Fireworks primitives like deployments, fine-tuning jobs, and datasets as Python objects.

<Note>
  The Build SDK is currently in beta and not all functionality may be supported. Please reach out to [dhuang@fireworks.ai](mailto:dhuang@fireworks.ai) to report any issues or feedback.
</Note>

## Installation

You can install the Fireworks Build SDK using pip:

```bash  theme={null}
pip install --upgrade fireworks-ai
```

Make sure to set the `FIREWORKS_API_KEY` environment variable to your Fireworks API key:

```bash  theme={null}
export FIREWORKS_API_KEY=<API_KEY>
```

You can create an API key in the [Fireworks AI web UI](https://app.fireworks.ai/settings/users/api-keys) or by installing the [firectl](/tools-sdks/firectl/firectl) CLI tool and running:

```bash  theme={null}
firectl signin
firectl api-key create --key-name <Your-Key-Name>
```

## Next Steps

Get started by [learning about the basics](/tools-sdks/python-client/sdk-basics) of working with the Build SDK. Or, if you'd prefer to jump straight in, we have prepared an [interactive tutorial](/tools-sdks/python-client/the-tutorial).
