# Source: https://docs.rootly.com/integrations/hashicorp-vault.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# HashiCorp Vault

> Securely read secrets from HashiCorp Vault and use them in workflows with KV Secrets Engine v2 support.

**HashiCorp Vault** Integration allows you to:

* **Read** secrets from your Vault cluster and use your secrets in workflows securely.

<Note>
  Rootly only supports KV Secrets Engine - Version 2
</Note>

## Installation

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/DEGWl8qg20zbzmSF/images/integrations/hashicorp-vault/images-1.webp?fit=max&auto=format&n=DEGWl8qg20zbzmSF&q=85&s=cf0ad149ee69887da81dfbb410d141d1" width="877" height="680" data-path="images/integrations/hashicorp-vault/images-1.webp" />
</Frame>

## Configure

* Auth methods are currently done through `app role` + `app secret`. Need another way to authenticate? Contact us at [support@rootly.com](mailto:support@rootly.com).

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/DEGWl8qg20zbzmSF/images/integrations/hashicorp-vault/images-2.webp?fit=max&auto=format&n=DEGWl8qg20zbzmSF&q=85&s=d204d9ef94cf95ab879518fe25653454" width="871" height="827" data-path="images/integrations/hashicorp-vault/images-2.webp" />
</Frame>

## Define a secret

<Note>
  Generally only Rootly owners or admins are able to define secrets. You can tweak permissions through our RBAC controller.
</Note>

Under `Account > Secrets`, define a HashiCorp Secret and specify `mount`, `path` and `version`.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/DEGWl8qg20zbzmSF/images/integrations/hashicorp-vault/images-3.webp?fit=max&auto=format&n=DEGWl8qg20zbzmSF&q=85&s=1bc2bf1b1affe44e453300d357c8d942" width="886" height="1004" data-path="images/integrations/hashicorp-vault/images-3.webp" />
</Frame>

## How to use it

You can use our **liquid markup** in any of our workflow tasks:

Give the following secret in Vault:

```JSON  theme={null}
{
  "first-secret": "Vault Is The Way",
  "nested-secret": {
    "foo": "bar"
  }
}
```

You can now read secrets:

```JSON  theme={null}
{{ secrets.my_secret.first-secret }} // Will resolve to "Vault Is The Way"
{{ secrets.my_secret.nested-secret.foo }} // Will resolve to "bar"
```

## Uninstall

You can **uninstall** this integration in the integrations panel by clicking **Configure > Delete**


Built with [Mintlify](https://mintlify.com).