# Source: https://docs.debricked.com/overview/getting-started.md

# Getting started

Follow these steps after [creating an account](https://docs.debricked.com/overview/getting-started/create-a-debricked-account) with OpenText Core SCA:

1. [**Set up an integration**](https://docs.debricked.com/tools-and-integrations/integrations)\
   If you have a project's dependency file but setting up an integration is not applicable at the moment, you can [upload the dependency file manually](https://docs.debricked.com/product/administration/repositories/upload-a-dependency-file-manually).
2. [**Set up a license use case**](https://docs.debricked.com/product/license-risk-management/set-up-a-use-case)\
   When you first access the license view, you will see that all repositories are marked as "Unknown" in the risk column. This is because you have not configured any use cases for your repositories yet. Defining a use case helps the tool understand how you organize the code in your repositories, which affects the risk associated with any particular license.
3. [**Set up automations**](https://docs.debricked.com/product/automation/create-an-automation-rule)\
   The automations engine allows for rules to be triggered based on conditions. For example, a rule can fail a pipeline if it detects a new high-risk vulnerability detected, or an unwanted license.

   By default, OpenText Core SCA has set up a number of rules to prevent unwanted licenses or dangerous vulnerabilities. Click the toggle button to disable any rule.
