# Source: https://configcat.com/docs/advanced/code-references/bitbucket-pipe.md

# Bitbucket Pipe - Scan your source code for feature flags

This section describes how to use ConfigCat's [Bitbucket Pipe](https://bitbucket.org/product/features/pipelines/integrations?p=configcat/scan-repository-pipe) to automatically scan your source code for feature flag and setting usages and upload the found code references to ConfigCat. You can find more information about Bitbucket Pipelines [here](https://bitbucket.org/product/features/pipelines).

## Setup[​](#setup "Direct link to Setup")

1. Create a new [ConfigCat Management API credential](https://app.configcat.com/my-account/public-api-credentials) and store its values in secure pipeline variables with the following names: `CONFIGCAT_API_USER`, `CONFIGCAT_API_PASS`.

   ![Bitbucket Pipe secrets](/docs/assets/cli/scan/pipe_secrets.png)

2. Get your selected [Config's ID](https://configcat.com/docs/docs/advanced/code-references/overview/.md#config-id).

3. Add the following snippet to the script section of your `bitbucket-pipelines.yml` file. Don't forget to replace the `PASTE-YOUR-CONFIG-ID-HERE` value with your actual Config ID.

   ```
   - pipe: configcat/scan-repository-pipe:1.8.1
     variables:
       CONFIG_ID: 'PASTE-YOUR-CONFIG-ID-HERE'
       # LINE_COUNT: '3'         # optional
       # TIMEOUT: '1800'         # optional
       # SUB_FOLDER: '/src'      # optional
       # EXCLUDE_KEYS: >         # optional
       #   flag_key_to_exclude_1
       #   flag_key_to_exclude_2
       # ALIAS_PATTERNS: (\w+) = :CC_KEY,const (\w+) = feature_flags\.enabled\(:CC_KEY\)  # optional
       # USAGE_PATTERNS: feature_flags\.enabled\(:CC_KEY\)
       # VERBOSE: 'true'         # optional
   ```

4. Commit & push your changes.

Scan reports are uploaded for each branch of your repository that triggers the job.

## Available Options[​](#available-options "Direct link to Available Options")

| Parameter            | Description                                                                                                                                                                             | Required | Default             |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------- |
| `CONFIG_ID`          | ID of the ConfigCat config to scan against.                                                                                                                                             | ☑        |                     |
| `CONFIGCAT_API_HOST` | ConfigCat Management API host.                                                                                                                                                          |          | `api.configcat.com` |
| `LINE_COUNT`         | Context line count before and after the reference line. (min: 1, max: 10)                                                                                                               |          | 4                   |
| `TIMEOUT`            | Scan timeout in seconds (default: 1800, min: 60). If the scan does not finish within this time, it is aborted. No partial results are returned. The command exits with a timeout error. |          | 1800                |
| `SUB_FOLDER`         | Sub-folder to scan, relative to the repository root folder.                                                                                                                             |          |                     |
| `EXCLUDE_KEYS`       | List of feature flag keys that must be excluded from the scan report.                                                                                                                   |          |                     |
| `ALIAS_PATTERNS`     | Comma delimited list of custom regex patterns used to search for additional aliases.                                                                                                    |          |                     |
| `USAGE_PATTERNS`     | Comma delimited list of custom regex patterns that describe additional feature flag key usages.                                                                                         |          |                     |
| `VERBOSE`            | Turns on detailed logging.                                                                                                                                                              |          | false               |
