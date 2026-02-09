# Source: https://docs.datafold.com/deployment-testing/configuration/datafold-ci/specifc.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Running Data Diff on Specific Branches

> By default, Datafold CI runs on every new pull/merge request and commits to existing ones.

You can set **Custom base branch** option in the Datafold app [CI settings](https://app.datafold.com/settings/integrations/ci), to only run Datafold CI on pull requests that have a specific base branch. This might be useful if you have multiple environments built from different branches. For example, `staging` and `production` environments built from `staging` and `main` branches respectively. Using the option, you can have 2 different CI configurations in Datafold, one for each environment, and only run the CI for the corresponding branch.
