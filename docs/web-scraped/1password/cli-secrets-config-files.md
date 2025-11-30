# Source: https://developer.1password.com/docs/cli/secrets-config-files

On this page

# Load secrets into config files

With 1Password CLI, you can use [secret references](/docs/cli/secret-reference-syntax/) to automatically load secrets into configuration files from your 1Password account without putting any plaintext secrets in code. This allows you to check config files into source control and keep them in sync throughout developer workstations, CI, and production servers, which is otherwise manual and error-prone work.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]tip

We recommend using [1Password Service Accounts](/docs/service-accounts/) to follow the [principle of least privilege](/docs/cli/best-practices/). Service accounts support restricting 1Password CLI to specific vaults, so that processes in your authorized terminal session can only access items required for a given purpose.

## Requirements[â€‹](#requirements "Direct link to Requirements") 

Before you can use 1Password to secure your config files, you\'ll need to:

1.  [Sign up for 1Password.](https://1password.com/pricing/password-manager)
2.  [Install 1Password CLI.](/docs/cli/get-started#step-1-install-1password-cli)
3.  Store the secrets you want to provision in your 1Password account.

## Step 1: Get secret references[â€‹](#step-1-get-secret-references "Direct link to Step 1: Get secret references") 

You can get secret references in several ways:

- [With the 1Password desktop app](/docs/cli/secret-reference-syntax#with-the-1password-desktop-app): Copy secret references from the app.
- [With 1Password for VSCode](/docs/vscode#get-values): Insert secret references from 1Password as you edit code.
- [With 1Password CLI](/docs/cli/secret-reference-syntax#with-1password-cli): Get secret references for one or multiple fields with `op item get`.
- Use the [secret reference syntax rules](/docs/cli/secret-reference-syntax#syntax-rules) to write secret references manually.

## Step 2: Use secret references in your config file[â€‹](#step-2-use-secret-references-in-your-config-file "Direct link to Step 2: Use secret references in your config file") 

Replace the plaintext secrets in your config file with the appropriate secret references, following the [template syntax](/docs/cli/secrets-template-syntax/).

For example, if you start with a config file that looks like this:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIGQ9Ik0xNSwzLjQxNDIxMzU2IEwxNSw3IEwxOC41ODU3ODY0LDcgTDE1LDMuNDE0MjEzNTYgWiBNMTksOSBMMTUsOSBDMTMuODk1NDMwNSw5IDEzLDguMTA0NTY5NSAxMyw3IEwxMywzIEw1LDMgTDUsMjEgTDE5LDIxIEwxOSw5IFogTTUsMSBMMTUuNDE0MjEzNiwxIEwyMSw2LjU4NTc4NjQ0IEwyMSwyMSBDMjEsMjIuMTA0NTY5NSAyMC4xMDQ1Njk1LDIzIDE5LDIzIEw1LDIzIEMzLjg5NTQzMDUsMjMgMywyMi4xMDQ1Njk1IDMsMjEgTDMsMyBDMywxLjg5NTQzMDUgMy44OTU0MzA1LDEgNSwxIFogTTExLjcwNzEwNjgsMTUuMjkyODkzMiBMMTAuMjkyODkzMiwxNi43MDcxMDY4IEw2LjU4NTc4NjQ0LDEzIEwxMC4yOTI4OTMyLDkuMjkyODkzMjIgTDExLjcwNzEwNjgsMTAuNzA3MTA2OCBMOS40MTQyMTM1NiwxMyBMMTEuNzA3MTA2OCwxNS4yOTI4OTMyIFogTTEyLjI5Mjg5MzIsMTIuNzA3MTA2OCBMMTMuNzA3MTA2OCwxMS4yOTI4OTMyIEwxNy40MTQyMTM2LDE1IEwxMy43MDcxMDY4LDE4LjcwNzEwNjggTDEyLjI5Mjg5MzIsMTcuMjkyODkzMiBMMTQuNTg1Nzg2NCwxNSBMMTIuMjkyODkzMiwxMi43MDcxMDY4IFoiIGZpbGwtcnVsZT0iZXZlbm9kZCIgLz48L3N2Zz4=)config.yml

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

And you saved the `username` and `password` secrets on the `mysql` item in the `prod` vault, you would end up with this templated config file:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIGQ9Ik0xNSwzLjQxNDIxMzU2IEwxNSw3IEwxOC41ODU3ODY0LDcgTDE1LDMuNDE0MjEzNTYgWiBNMTksOSBMMTUsOSBDMTMuODk1NDMwNSw5IDEzLDguMTA0NTY5NSAxMyw3IEwxMywzIEw1LDMgTDUsMjEgTDE5LDIxIEwxOSw5IFogTTUsMSBMMTUuNDE0MjEzNiwxIEwyMSw2LjU4NTc4NjQ0IEwyMSwyMSBDMjEsMjIuMTA0NTY5NSAyMC4xMDQ1Njk1LDIzIDE5LDIzIEw1LDIzIEMzLjg5NTQzMDUsMjMgMywyMi4xMDQ1Njk1IDMsMjEgTDMsMyBDMywxLjg5NTQzMDUgMy44OTU0MzA1LDEgNSwxIFogTTExLjcwNzEwNjgsMTUuMjkyODkzMiBMMTAuMjkyODkzMiwxNi43MDcxMDY4IEw2LjU4NTc4NjQ0LDEzIEwxMC4yOTI4OTMyLDkuMjkyODkzMjIgTDExLjcwNzEwNjgsMTAuNzA3MTA2OCBMOS40MTQyMTM1NiwxMyBMMTEuNzA3MTA2OCwxNS4yOTI4OTMyIFogTTEyLjI5Mjg5MzIsMTIuNzA3MTA2OCBMMTMuNzA3MTA2OCwxMS4yOTI4OTMyIEwxNy40MTQyMTM2LDE1IEwxMy43MDcxMDY4LDE4LjcwNzEwNjggTDEyLjI5Mjg5MzIsMTcuMjkyODkzMiBMMTQuNTg1Nzg2NCwxNSBMMTIuMjkyODkzMiwxMi43MDcxMDY4IFoiIGZpbGwtcnVsZT0iZXZlbm9kZCIgLz48L3N2Zz4=)config.yml.tpl

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

## Step 2: Inject the secrets[â€‹](#step-2-inject-the-secrets "Direct link to Step 2: Inject the secrets") 

To load secrets from the config file and provision them at runtime, use `op inject` to inject the secrets directly into your production environment. For example:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

In the output file, `config.yml`, you\'ll see the secret references replaced with the plaintext secrets they reference.

The config file template is stored together with the code in source control, so that every developer can see the structure of the file.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTUuMDUuMzFjLjgxIDIuMTcuNDEgMy4zOC0uNTIgNC4zMUMzLjU1IDUuNjcgMS45OCA2LjQ1LjkgNy45OGMtMS40NSAyLjA1LTEuNyA2LjUzIDMuNTMgNy43LTIuMi0xLjE2LTIuNjctNC41Mi0uMy02LjYxLS42MSAyLjAzLjUzIDMuMzMgMS45NCAyLjg2IDEuMzktLjQ3IDIuMy41MyAyLjI3IDEuNjctLjAyLjc4LS4zMSAxLjQ0LTEuMTMgMS44MSAzLjQyLS41OSA0Ljc4LTMuNDIgNC43OC01LjU2IDAtMi44NC0yLjUzLTMuMjItMS4yNS01LjYxLTEuNTIuMTMtMi4wMyAxLjEzLTEuODkgMi43NS4wOSAxLjA4LTEuMDIgMS44LTEuODYgMS4zMy0uNjctLjQxLS42Ni0xLjE5LS4wNi0xLjc4QzguMTggNS4zMSA4LjY4IDIuNDUgNS4wNS4zMkw1LjAzLjNsLjAyLjAxeiIgLz48L3N2Zz4=)]danger

Make sure to delete the resolved config file when you no longer need it.

## Step 3: Differentiate between environments[â€‹](#step-3-differentiate-between-environments "Direct link to Step 3: Differentiate between environments") 

We highly recommend you organize your 1Password items in the same way across all of your environments. For example: `app/dev/db/password` and `app/prod/db/password`.

If you do this, you can use variables in your template file to switch to a different set of secrets. You can have variables for your environment, stage, region, or anything else. For example:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIGQ9Ik0xNSwzLjQxNDIxMzU2IEwxNSw3IEwxOC41ODU3ODY0LDcgTDE1LDMuNDE0MjEzNTYgWiBNMTksOSBMMTUsOSBDMTMuODk1NDMwNSw5IDEzLDguMTA0NTY5NSAxMyw3IEwxMywzIEw1LDMgTDUsMjEgTDE5LDIxIEwxOSw5IFogTTUsMSBMMTUuNDE0MjEzNiwxIEwyMSw2LjU4NTc4NjQ0IEwyMSwyMSBDMjEsMjIuMTA0NTY5NSAyMC4xMDQ1Njk1LDIzIDE5LDIzIEw1LDIzIEMzLjg5NTQzMDUsMjMgMywyMi4xMDQ1Njk1IDMsMjEgTDMsMyBDMywxLjg5NTQzMDUgMy44OTU0MzA1LDEgNSwxIFogTTExLjcwNzEwNjgsMTUuMjkyODkzMiBMMTAuMjkyODkzMiwxNi43MDcxMDY4IEw2LjU4NTc4NjQ0LDEzIEwxMC4yOTI4OTMyLDkuMjkyODkzMjIgTDExLjcwNzEwNjgsMTAuNzA3MTA2OCBMOS40MTQyMTM1NiwxMyBMMTEuNzA3MTA2OCwxNS4yOTI4OTMyIFogTTEyLjI5Mjg5MzIsMTIuNzA3MTA2OCBMMTMuNzA3MTA2OCwxMS4yOTI4OTMyIEwxNy40MTQyMTM2LDE1IEwxMy43MDcxMDY4LDE4LjcwNzEwNjggTDEyLjI5Mjg5MzIsMTcuMjkyODkzMiBMMTQuNTg1Nzg2NCwxNSBMMTIuMjkyODkzMiwxMi43MDcxMDY4IFoiIGZpbGwtcnVsZT0iZXZlbm9kZCIgLz48L3N2Zz4=)config.yml.tpl

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

You can then set the `APP_ENV` variable when you inject into the template, using the [Template Syntax](/docs/cli/secrets-template-syntax/):

- Bash, Zsh, sh, fish
- PowerShell

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

1.  Set `APP_ENV` to `prod`:

    :::::: container_wh0u
    ::::: wrapper_Ok5U
    ::: 
    :::

    ::: 
    [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]
    :::
    :::::
    ::::::

2.  Inject the secrets:

    :::::: container_wh0u
    ::::: wrapper_Ok5U
    ::: 
    :::

    ::: 
    [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]
    :::
    :::::
    ::::::

This allows you to use the same template file, stored in source control next to your application, for all your deployments.

## Optional: Use `op inject` in production[â€‹](#optional-use-op-inject-in-production "Direct link to optional-use-op-inject-in-production") 

Now that the application works with the right configuration locally, you can use 1Password CLI to provision secrets in production environments.

To do this, you\'ll first need to:

1.  [Install 1Password CLI 2 in your production environment.](/docs/cli/install-server/)
2.  [Set up a Secrets Automation workflow](/docs/connect/).
3.  [Deploy 1Password Connect Server](/docs/connect/get-started#step-2-deploy-a-1password-connect-server) and make it accessible to your production environment.

To use 1Password CLI with a Connect server, set the `OP_CONNECT_HOST` and `OP_CONNECT_TOKEN` environment variables to your Connect instance\'s credentials in your production environment.

You can now move your secrets to config files and have them readily accessible with `op inject`.

The following commands can be used with a Connect server:

- `op run`
- `op inject`
- `op read`
- `op item get`

## Learn more[â€‹](#learn-more "Direct link to Learn more") 

- [Load secrets into the environment](/docs/cli/secrets-environment-variables/)
- [Secret reference syntax](/docs/cli/secret-reference-syntax/)
- [Template syntax](/docs/cli/secrets-template-syntax/)