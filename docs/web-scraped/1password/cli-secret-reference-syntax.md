# Source: https://developer.1password.com/docs/cli/secret-reference-syntax

On this page

# Secret reference syntax

![An environment file using a plaintext secret and the same file using a secret reference.](/img/cli/use-case-secret-reference.png)![An environment file using a plaintext secret and the same file using a secret reference.](/img/cli/use-case-secret-reference.png)

Secret reference URIs point to where a secret is saved in your 1Password account using the names (or [unique identifiers](/docs/cli/reference#unique-identifiers-ids)) of the vault, item, section, and field where the information is stored.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

Secret references remove the risk of exposing plaintext secrets in your code and reflect changes you make in your 1Password account, so when you run a script you get the latest value.

You can use secret references with:

### 1Password CLI 

Load secrets into environment variables, configuration files, and scripts.

[Learn more ](/docs/cli/secret-references/)