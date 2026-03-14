# Source: https://docs.envzero.com/guides/admin-guide/self-hosted-kubernetes-agent/env-zero-hosted-encrypted-state.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# env zero Hosted Encrypted State

> Use env zero hosted encrypted state storage to avoid configuring PVCs for the self-hosted Kubernetes agent

env zero has removed the requirement for setting up [PersistentVolumeClaims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) (PVCs) when using env zero's Self-Hosted Agents. env zero will encrypt (with a customer provided encryption key) the working directory and persist it in env zero's secure cloud native file system.

## How does it work

1. Add a `"env0StateEncryptionKey" = "<your_base64_encoded_state_encryption_key>"` key-value pair to your agent's `<your_agent_key>_values.yaml` configuration file. On existing agents, upgrade helm to apply the changes made in your configuration file. **The encryption key can be any random string.**
2. When deploying an environment, the agent uses your encryption key to encrypt deployment state and working directory, and upload them to env zero's secure cloud native file system.

<Info>
  **About Privacy**

  We don't have access to your state files or your encryption key. Your encryption key belongs to you and your agent.
</Info>

## Key rotation

In case you want to change the encryption key, edit the `env0StateEncryptionKey` value in your agent's configuration file, and replace it with a different base64 encoded string.

<Warning>
  Warning

  When using local state files, adding, removing or rotating the encryption key will result in state loss for existing environments. In such cases, Terraform resources will be re-created.

  To remedy this, we recommend using a remote backend (e.g. [env zero Remote Backend](/guides/admin-guide/remote-backend)).
</Warning>

Built with [Mintlify](https://mintlify.com).
