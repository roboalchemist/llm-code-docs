# Source: https://configcat.com/docs/advanced/code-references/azure-devops.md

# Azure DevOps - Scan your source code for feature flags

This section describes how to use the [ConfigCat CLI](https://configcat.com/docs/docs/advanced/cli/.md) in [Azure DevOps Pipelines](https://docs.microsoft.com/en-us/azure/devops/pipelines/?view=azure-devops) to automatically scan your source code for feature flag and setting usages and upload the found code references to ConfigCat.

## Setup[â€‹](#setup "Direct link to Setup")

1. Create a new [ConfigCat Management API credential](https://app.configcat.com/my-account/public-api-credentials) and store its values in Azure DevOps [Pipeline Variables](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/variables) with the following names: `CONFIGCAT_API_USER`, `CONFIGCAT_API_PASS`.

   ![Azure secrets](/docs/assets/cli/scan/azure_secrets.png)

2. Get your selected [Config's ID](https://configcat.com/docs/docs/advanced/code-references/overview/.md#config-id).

3. Create a new or open your existing `azure-pipelines.yml` file, and add the following [job](https://docs.microsoft.com/en-us/azure/devops/pipelines/yaml-schema#job) to your `jobs` definition. Don't forget to replace the `PASTE-YOUR-CONFIG-ID-HERE` value with your actual Config ID.

   ```
   - job: configcat_scan_and_upload
     container: configcat/cli:azure-devops-2.4.2
     pool:
       vmImage: ubuntu-latest
     steps:
       - checkout: self
         persistCredentials: true
       - script: configcat scan $(Build.Repository.LocalPath)
           --config-id=PASTE-YOUR-CONFIG-ID-HERE
           --repo=$(Build.Repository.Name)
           --branch=$(Build.SourceBranchName)
           --file-url-template="$(Build.Repository.Uri)?path={filePath}&version=GC{commitHash}&line={lineNumber}&lineStartColumn=1&lineEndColumn=1"
           --commit-url-template="$(Build.Repository.Uri)/commit/{commitHash}"
           --runner="ConfigCat Azure DevOps Job"
           --upload
           --non-interactive
         name: scan_repository
         env:
           CONFIGCAT_API_PASS: $(CONFIGCAT_API_PASS)
           CONFIGCAT_API_USER: $(CONFIGCAT_API_USER)
   ```

info

If you are using a different VCS than Azure DevOps' Git, you should set the `--file-url-template` and `--commit-url-template` according to your VCS provider.

4. Commit & push your changes.

Scan reports are uploaded for each branch of your repository that triggers the job.
