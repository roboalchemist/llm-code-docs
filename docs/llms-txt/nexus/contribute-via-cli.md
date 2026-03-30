# Source: https://docs.nexus.xyz/network/proving-on-the-layer-1/contribute-via-cli.md

# Contribute via CLI

### Introduction

The [Nexus Network CLI](https://github.com/nexus-xyz/nexus-cli) is a command-line tool for contributing compute resources to the network.

![CLI nodes connecting to Nexus](https://content.gitbook.com/content/PUemy5iDAcT0e1cZJm4f/blobs/tuG5hSYQ04XzARtWDIzi/cli%20tui.png)

### Install Script

Quick install (scripted):

```
curl https://cli.nexus.xyz/ | sh
```

After installing, restart or refresh your terminal (e.g. `source ~/.bashrc`, `source ~/.zshrc`, etc.). To start with an existing node ID:

```
nexus-network start --node-id <your-node-id>
```

Alternatively, register your wallet address and create a node ID with the CLI, or at [app.nexus.xyz](https://docs.nexus.xyz/network/proving-on-the-layer-1/broken-reference):

```
nexus-network register-user --wallet-address <your-wallet-address>
nexus-network register-node
nexus-network start
```

The `register-user` and `register-node` commands will save your credentials to `~/.nexus/credentials.json`. To clear credentials, run:

```
nexus-network logout
```

### Setup & Configuration

{% stepper %}
{% step %}

### Initial setup

1. Run the CLI for the first time.
2. Accept the [Terms of Use](https://nexus.xyz/terms-of-use).
3. Choose between anonymous or linked proving (see the next step).
   {% endstep %}

{% step %}

### Choose proving mode

You have two options:

* Link to Nexus Account (Recommended)
  * Create an account at [app.nexus.xyz](https://app.nexus.xyz/).
  * Follow the account linking instructions.
  * Your contributions will earn NEX Points.
  * Track your progress on the leaderboard.
  * Manage all your nodes in one place.

To earn NEX Points, you must link your CLI to your Nexus account. Anonymous proving will not record contributions.
{% endstep %}
{% endstepper %}

### Troubleshooting

<details>

<summary>Known issues &#x26; help</summary>

* If you have previously proved with an older version of the CLI, you must run the install script for the new CLI, as the versions are not backwards compatible. Proofs submitted by the old CLI will not receive rewards in Testnet III.
* Check Documentation:
  * Search existing [GitHub Issues](https://github.com/nexus-xyz/nexus-cli/issues).
* Get Help:
  * Join our [Discord](https://discord.gg/nexus-xyz)
  * [Open a new GitHub issue](https://github.com/nexus-xyz/nexus-cli/issues/new) for technical problems

</details>

***

Related:

* Contribute via Web App: <https://docs.nexus.xyz/layer-1/testnet/web-node>
* FAQ: <https://docs.nexus.xyz/layer-1/testnet/faq>
