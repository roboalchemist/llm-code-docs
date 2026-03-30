# Source: https://zinc-staging.vercel.app/docs/v2/agent-skills/setup.md

> ## Documentation Index
> Fetch the complete documentation index at: https://zinc-staging.vercel.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setup

> Install and configure the Universal Checkout Skill for your AI agent.

## Installation

The Universal Checkout Skill is installed by cloning the repository into a location
your agent can discover. The exact steps depend on your platform.

<Tabs>
  <Tab title="Git Clone">
    Clone the skill into your project's `skills/` directory:

    ```bash  theme={null}
    git clone https://github.com/zincio/universal-checkout-skill.git ./skills/universal-checkout-skill
    ```

    Compatible agents automatically discover skills in the workspace `skills/` folder. No additional configuration is needed beyond setting the API key.
  </Tab>

  <Tab title="OpenClaw via Clawhub">
    **Option 1: Install via ClawHub**

    ```bash  theme={null}
    clawhub install a5huynh/universal-checkout
    ```

    **Option 2: Clone manually**

    Install at the user level (available across all projects):

    ```bash  theme={null}
    git clone https://github.com/zincio/universal-checkout-skill.git ~/.openclaw/skills/universal-checkout-skill
    ```

    Or at the workspace level (available only in the current project):

    ```bash  theme={null}
    git clone https://github.com/zincio/universal-checkout-skill.git ./skills/universal-checkout-skill
    ```

    <Info>
      OpenClaw loads skills from three locations, in priority order: workspace (`./skills/`), user (`~/.openclaw/skills/`), and bundled (shipped with installation). Additional directories can be configured via `skills.load.extraDirs`.
    </Info>

    OpenClaw hot-reloads skills when `SKILL.md` changes, so no restart is needed after updates.
  </Tab>
</Tabs>

<Tip>
  We recommend installing the skill via GitHub to ensure you're using the latest
  version.
</Tip>

## Configuration

### API Key

The skill requires a `ZINC_API_KEY` environment variable. Set it in your shell before starting your agent:

```bash  theme={null}
export ZINC_API_KEY=your-api-key
```

<Info>
  Get your API key from the{" "}

  <a href="https://app.zinc.com" target="_blank">
    Zinc dashboard
  </a>

  . You'll need to create an account and deposit funds to place orders.
</Info>

### OpenClaw Configuration File

If you're using OpenClaw, you can set the API key through the configuration file instead of an environment variable:

```json ~/.openclaw/openclaw.json theme={null}
{
  "skills": {
    "entries": {
      "zinc-orders": {
        "enabled": true,
        "env": {
          "ZINC_API_KEY": "your-api-key"
        }
      }
    }
  }
}
```

## Verifying the Installation

After installing, start your agent and ask it something like:

> "List my recent Zinc orders."

If the skill is loaded correctly, the agent will make a `GET /orders` request to the Zinc API and return your order history. If you see an authentication error, double-check that your `ZINC_API_KEY` is set correctly.

## Updating

To update the skill to the latest version, pull the latest changes:

```bash  theme={null}
cd ./skills/universal-checkout-skill && git pull
```


Built with [Mintlify](https://mintlify.com).