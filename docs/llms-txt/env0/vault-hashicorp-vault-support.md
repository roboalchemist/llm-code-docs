# Source: https://docs.envzero.com/changelogs/2022/07/vault-hashicorp-vault-support.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🤫 HashiCorp Vault Support For Self-Hosted Agent

> Self-hosted agents allow you to run your env0 deployment workloads on your own infrastructure. This gives you the ability to isolate your infrastructure as code deployments in a more secure way, within your private network. This also allows you to manage your secrets in your preferred secret manager. Today you can also store those secrets natively inside Hashicopr Vault, and give your agent the ability to resolve those secrets for each deployment automatically.

Self-hosted agents allow you to run your env0 deployment workloads on your own infrastructure. This gives you the ability to isolate your infrastructure as code deployments in a more secure way, within your private network. This also allows you to manage your secrets in your preferred secret manager. Today you can also store those secrets natively inside Hashicorp Vault, and give your agent the ability to resolve those secrets for each deployment automatically.

### ✨ Configure Vault ✨

<Warning>
  **Vault Integration**

  As mentioned above, this feature is only available with Self-Hosted agents. However, with the SaaS, this can also be achieved manually using our [custom flow](/guides/admin-guide/custom-flows).

  In order to easily integrate your self-hosted agent to read your Vault secrets, you will need to configure the Vault URL and token for authentication, and env0 will take care of the rest.
  Read all about it in our [docs](/guides/admin-guide/variables) and also how to configure it [here](/guides/admin-guide/self-hosted-kubernetes-agent)
</Warning>

Built with [Mintlify](https://mintlify.com).
