# Source: https://docs.port.io/sso-rbac/port-secrets.md

# Port secrets

Port provides a secure way to store sensitive data, such as tokens, passwords, and other secrets used in different Port components.

Port secrets can be used in:

* Port-hosted integrations - any integration that is installed using the "Hosted by Port" method, for example: [Datadog](/build-your-software-catalog/sync-data-to-catalog/apm-alerting/datadog/.md?installation-methods=hosted-by-port\&deploy=argocd\&cicd-method=github#installation).
* [Self-service actions payload](/actions-and-automations/create-self-service-experiences/setup-the-backend/.md#define-the-actions-payload).
* [Automations payload](/actions-and-automations/define-automations/setup-action.md#define-the-payload).

## Usage[â](#usage "Direct link to Usage")

To view your organization secrets:

* In your [Port application](https://app.getport.io), click on the `...` button in the top right corner, and select `Credentials`.

* In the `Credentials` window, choose the `Secrets` tab.

To create a new secret, click on the `+ Secret` button.

![](/img/secrets/secretsTabExample.png)

One-time view

After creating a secret, you will be able to view its value only once.<br /><!-- -->Afterwards, you will be able to delete the secret or edit its value, but not to view it.

## Referencing secrets[â](#referencing-secrets "Direct link to Referencing secrets")

To reference a secret in your action or automation payloads, use the following syntax:

```
"token": "{{ .secrets.MY_SECRET_NAME }}"
```

Note that if your secret name contains hyphens or special characters, use bracket notation:

```
"token": "{{ .secrets["my-secret-name"] }}"
```

## Security[â](#security "Direct link to Security")

* Port secrets reside in Port's infrastructure (hosted on AWS), **per organization**, meaning that no other organization has any access to your secrets.
* Secrets are `AES-256` encrypted at rest, and are only decrypted when needed.
* Secrets are encrypted in transit using `TLS 1.2`.
