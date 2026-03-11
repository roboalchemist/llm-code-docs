# Source: https://docs.envzero.com/changelogs/2023/07/env0-hosted-encrypted-state.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🔐 env0-Hosted Encrypted State

> You can now use env0-hosted encrypted state as an alternative to setting up [PersistentVolumeClaims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) (PVCs) when using env0's Self-Hosted Agents. env0 will encrypt (with a customer provided encryption key) the working directory and persist it in env0's secure cloud native file system. Simply add a `"env0StateEncryptionKey"` key-value pair to your agent's `<your_agent_key>_values.yaml` and you're all set. Find out more at [Env0-Hosted Encrypted State](/guides/admin-guide/self-hosted-kubernetes-agent/env0-hosted-encrypted-state).

You can now use env0-hosted encrypted state as an alternative to setting up [PersistentVolumeClaims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) (PVCs) when using env0's Self-Hosted Agents. env0 will encrypt (with a customer provided encryption key) the working directory and persist it in env0's secure cloud native file system.

Simply add a `"env0StateEncryptionKey"` key-value pair to your agent's `<your_agent_key>_values.yaml` and you're all set. Find out more at [Env0-Hosted Encrypted State](/guides/admin-guide/self-hosted-kubernetes-agent/env0-hosted-encrypted-state).

Built with [Mintlify](https://mintlify.com).
