# Source: https://docs.pipecat.ai/server/utilities/text/overview.md

# Source: https://docs.pipecat.ai/guides/telephony/overview.md

# Source: https://docs.pipecat.ai/guides/learn/overview.md

# Source: https://docs.pipecat.ai/deployment/pipecat-cloud/sdk-reference/overview.md

# Source: https://docs.pipecat.ai/deployment/pipecat-cloud/guides/container-registries/overview.md

# Source: https://docs.pipecat.ai/deployment/overview.md

# Source: https://docs.pipecat.ai/cli/overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pipecat.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# CLI Overview

> Command-line tool for scaffolding, deploying, and monitoring Pipecat bots

<CardGroup cols={3}>
  <Card title="Scaffold Projects" icon="wand-magic-sparkles" href="/cli/init">
    Create new phone or web/mobile bots with interactive setup
  </Card>

  <Card title="Deploy to Cloud" icon="rocket" href="/cli/cloud/auth">
    Push your bots to production with one command
  </Card>

  <Card title="Monitor Live Bots" icon="chart-line" href="/cli/tail">
    Watch real-time logs, conversations, and metrics
  </Card>
</CardGroup>

## Requirements

* Python 3.10 or later

## Installation

Install the CLI globally using [uv](https://docs.astral.sh/uv/) (recommended) or [pipx](https://pipx.pypa.io/):

```bash  theme={null}
uv tool install pipecat-ai-cli
# or
pipx install pipecat-ai-cli
```

Verify installation:

```bash  theme={null}
pipecat --version
```

<Tip>All commands can use either `pipecat` or the shorter `pc` alias.</Tip>

## Commands

**[`pipecat init`](/cli/init)** - Scaffold new projects with interactive setup

**[`pipecat tail`](/cli/tail)** - Monitor sessions in real-time with a terminal dashboard

**[`pipecat cloud`](/cli/cloud/auth)** - Deploy and manage bots on Pipecat Cloud

## Getting Help

View help for any command:

```bash  theme={null}
pipecat --help
pipecat init --help
pipecat tail --help
pipecat cloud --help
```

## Next Steps

<Card title="Create Your First Bot" icon="rocket" href="/cli/init">
  Scaffold a new project with pipecat init
</Card>
