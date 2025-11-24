# Source: https://docs.fireworks.ai/accounts/service-accounts.md

# Service Accounts

> How to manage and use service accounts in Fireworks

Service accounts in Fireworks allow applications, scripts, and automated systems to authenticate and perform actions securely—without relying on human credentials. They are ideal for CI/CD pipelines, backend services, and automated workflows. Service Accounts let you avoid shared credentials and easily distinguish between what automated systems did vs humans in audit logs.

Service accounts can take actions using an API key, like creating deployments, running models or creating datasets (see [API reference](https://fireworks.ai/docs/api-reference/introduction)). Service accounts cannot login through the web interface or use OIDC tokens.

## Creating a Service Account

Using our firectl you can create service accounts

```bash  theme={null}
firectl create user --user-id "my-service-account" --service-account
```

## Creating an API Key for Service Account

Using our firectl you can create an api key on behalf of a service account

```bash  theme={null}
firectl create api-key --service-account "my-service-account"
```

## Billing

* Service accounts count toward the same account quotas and limits assigned to the account
* Usage is tracked by the account, not individual user vs service account

## Auditing

In audit logs users are referenced by their email id's. Service accounts are referenced by `my-service-account@my-account.sa.fireworks.ai`.
