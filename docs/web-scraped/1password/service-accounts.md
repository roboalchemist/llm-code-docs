# Source: https://developer.1password.com/docs/service-accounts

On this page

# 1Password Service Accounts

1Password Service Accounts help automate secrets management in your applications and infrastructure without the need to deploy additional services.

Service accounts work well for shared environments because they provide an authentication method for [1Password CLI](/docs/cli/) that isn\'t associated with an individual. You control which vaults are accessible and which actions the service account can perform. And you can see what items a service account accesses by creating a [usage report](https://support.1password.com/reports#create-a-usage-report-for-a-team-member-service-account-or-vault).

You can create up to 100 service accounts.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]Not sure if service accounts are for you?

See the [secrets automation comparison table](/docs/secrets-automation#comparison).

## Use cases[â€‹](#use-cases "Direct link to Use cases") 

You can use 1Password Service Accounts to accomplish a variety of tasks:

## Web services 

### Provision web services with secrets 

Use a service account to provision an account with a secret stored in 1Password.

If a web service needs access to a database (and the credentials for the database are in 1Password), you can use a service account to provision an account with the needed secret and allow the web service to access the secret during test runs.