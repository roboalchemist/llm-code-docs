# Source: https://configcat.com/docs/integrations/github.md

# Scan your code for feature flag usages

Copy page

ConfigCat's<!-- --> [Scan Repository GitHub Action](https://github.com/marketplace/actions/configcat-scan-repository) <!-- -->has the ability to scan your source code for feature flag and setting usages and upload the found code references to ConfigCat.

This feature makes the elimination of the technical debt easier, as it can show which repositories reference your feature flags and settings in one centralized place on your [Dashboard](https://app.configcat.com).

[Here](https://configcat.com/docs/advanced/code-references/overview.md) you can find more details about how this feature works.

This section describes how to use ConfigCat's [Scan Repository GitHub Action](https://github.com/marketplace/actions/configcat-scan-repository) to automatically scan your source code for feature flag and setting usages and upload the found code references to ConfigCat. You can find more information about GitHub Actions [here](https://github.com/features/actions).

## Setup[​](#setup "Direct link to Setup")

1. Create a new [ConfigCat Management API credential](https://app.configcat.com/my-account/public-api-credentials) and store its values in your repository's [GitHub Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository) with the following names: `CONFIGCAT_API_USER`, `CONFIGCAT_API_PASS`.

   ![Github Action secrets](/docs/assets/cli/scan/github_secrets.png)

2. Get your selected [Config's ID](https://configcat.com/docs/advanced/code-references/overview.md#config-id).

3. Create a new Actions workflow in your GitHub repository under the `.github/workflows` folder, and put the following snippet into it. Don't forget to replace the `PASTE-YOUR-CONFIG-ID-HERE` value with your actual Config ID.

   ```yaml
   on: [push]
   name: Code references
   jobs:
     scan-repo:
       runs-on: ubuntu-latest
       name: Scan repository for code references
       steps:
         - name: Checkout
           uses: actions/checkout@v3
         - name: Scan & upload
           uses: configcat/scan-repository@v2
           with:
             api-user: ${{ secrets.CONFIGCAT_API_USER }}
             api-pass: ${{ secrets.CONFIGCAT_API_PASS }}
             config-id: PASTE-YOUR-CONFIG-ID-HERE
             # line-count: 5             # optional
             # timeout: 1800             # optional
             # sub-folder: src           # optional
             # exclude-keys: >           # optional
             #   flag_key_to_exclude_1
             #   flag_key_to_exclude_2
             # alias-patterns: (\w+) = :CC_KEY,const (\w+) = feature_flags\.enabled\(:CC_KEY\) #optional
             # usage-patterns: feature_flags\.enabled\(:CC_KEY\)   # optional, comma delimited flag key usage patterns
             # verbose: true             # optional

   ```

4. Commit & push your action.

The above example configures a workflow that executes the scan and code references upload on every git `push` event. Scan reports are uploaded for each branch of your repository that triggers the workflow.

## Available Options[​](#available-options "Direct link to Available Options")

| Parameter        | Description                                                                                                                                                                             | Required | Default             |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------- |
| `config-id`      | ID of the ConfigCat config to scan against.                                                                                                                                             | ☑        |                     |
| `api-user`       | [ConfigCat Management API basic authentication username](https://app.configcat.com/my-account/public-api-credentials).                                                                  | ☑        |                     |
| `api-pass`       | [ConfigCat Management API basic authentication password](https://app.configcat.com/my-account/public-api-credentials).                                                                  | ☑        |                     |
| `api-host`       | ConfigCat Management API host.                                                                                                                                                          |          | `api.configcat.com` |
| `line-count`     | Context line count before and after the reference line. (min: 1, max: 10)                                                                                                               |          | 4                   |
| `timeout`        | Scan timeout in seconds (default: 1800, min: 60). If the scan does not finish within this time, it is aborted. No partial results are returned. The command exits with a timeout error. |          | 1800                |
| `sub-folder`     | Sub-folder to scan, relative to the repository root folder.                                                                                                                             |          |                     |
| `exclude-keys`   | List of feature flag keys that must be excluded from the scan report.                                                                                                                   |          |                     |
| `alias-patterns` | Comma delimited list of custom regex patterns used to search for additional aliases.                                                                                                    |          |                     |
| `usage-patterns` | Comma delimited list of custom regex patterns that describe additional feature flag key usages.                                                                                         |          |                     |
| `verbose`        | Turns on detailed logging.                                                                                                                                                              |          | false               |
