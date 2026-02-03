# Source: https://configcat.com/docs/integrations/bitrise.md

# Bitrise - Scan your code for feature flag usages

Copy page

ConfigCat's<!-- --> [Bitrise Step](https://www.bitrise.io/integrations/steps/configcat-feature-flag-sync) <!-- -->has the ability to scan your source code for feature flag and setting usages and upload the found code references to ConfigCat.

This feature makes the elimination of the technical debt easier, as it can show which repositories reference your feature flags and settings in one centralized place on your [Dashboard](https://app.configcat.com).

[Here](https://configcat.com/docs/advanced/code-references/overview.md) you can find more details about how this feature works.

This section describes how to use ConfigCat's [Bitrise Step](https://www.bitrise.io/integrations/steps/configcat-feature-flag-sync) to automatically scan your source code for feature flag and setting usages and upload the found code references to ConfigCat. [Bitrise](https://www.bitrise.io/) is full-featured mobile CI/CD platform. You can find more information about Bitrise Steps [here](https://devcenter.bitrise.io/en/steps-and-workflows/introduction-to-steps.html).

## Setup[​](#setup "Direct link to Setup")

1. Create a new [ConfigCat Management API credential](https://app.configcat.com/my-account/public-api-credentials) and store its values in secure pipeline variables with the following names: `CONFIGCAT_API_USER`, `CONFIGCAT_API_PASS`.

   ![Bitrise secrets](/docs/assets/cli/scan/bitrise_secrets.png)

2. Get your selected [Config's ID](https://configcat.com/docs/advanced/code-references/overview.md#config-id).

3. Add the following step to the workflows section of your `bitrise.yml` file. Don't forget to replace the `PASTE-YOUR-CONFIG-ID-HERE` value with your actual Config ID.

   ```yaml
   - configcat-feature-flag-sync@0:
     inputs:
       - configcat_config_id: 'PASTE-YOUR-CONFIG-ID-HERE' # required
       # - line-count: 3           # optional
       # - sub-folder: 'src'       # optional
       # - exclude-keys: >         # optional
       #   flag_key_to_exclude_1
       #   flag_key_to_exclude_2
       # - alias-patterns: "(\w+) = :CC_KEY,const (\w+) = feature_flags\.enabled\(:CC_KEY\)" # optional
       # - usage-patterns: feature_flags\.enabled\(:CC_KEY\)   # optional
       # - verbose: true           # optional

   ```

4. Commit & push your changes.

Scan reports are uploaded for each branch of your repository that triggers the job.

## Available Options[​](#available-options "Direct link to Available Options")

| Parameter             | Description                                                                                                                                                             | Required | Default             |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------- |
| `configcat_config_id` | The [config ID](https://configcat.com/docs/advanced/code-references/overview.md#config-id) tells the step which feature flags it should search for in your source code. | ☑        |                     |
| `configcat_api_host`  | ConfigCat Management API host.                                                                                                                                          |          | `api.configcat.com` |
| `line_count`          | Code snippet line count before and after the reference line. (min: 1, max: 10)                                                                                          |          | 4                   |
| `sub_folder`          | Sub-folder to scan, relative to the repository root folder.                                                                                                             |          |                     |
| `exclude-keys`        | List of feature flag keys that must be excluded from the scan report.                                                                                                   |          |                     |
| `alias-patterns`      | Comma delimited list of custom regex patterns used to search for additional aliases.                                                                                    |          |                     |
| `usage-patterns`      | Comma delimited list of custom regex patterns that describe additional feature flag key usages.                                                                         |          |                     |
| `verbose`             | Turns on detailed logging.                                                                                                                                              |          | false               |
